import { Log } from '@microsoft/sp-core-library';
import {
  BaseListViewCommandSet,
  Command,
  IListViewCommandSetExecuteEventParameters,
  ListViewStateChangedEventArgs,
} from '@microsoft/sp-listview-extensibility';
import { Dialog } from '@microsoft/sp-dialog';
import * as React from 'react';
import * as ReactDOM from 'react-dom';
import { PushDialog } from './components/PushDialog';
import { AtomClient } from './services/AtomClient';

export interface IAtomArchivePushCommandSetProperties {
  // Tenant config injected via package-solution.json or property pane.
  // For now we rely on web-part-property tenant binding; runtime uses
  // properties.atomBaseUrl set by tenant admin during install.
  atomBaseUrl?: string;
  atomTenantId?: string;
}

const LOG_SOURCE = 'AtomArchivePushCommandSet';

export default class AtomArchivePushCommandSet
  extends BaseListViewCommandSet<IAtomArchivePushCommandSetProperties> {

  public onInit(): Promise<void> {
    Log.info(LOG_SOURCE, 'Initialized AtomArchivePushCommandSet');

    const cmd: Command = this.tryGetCommand('ATOM_PUSH');
    if (cmd) {
      cmd.visible = false;
    }
    return Promise.resolve();
  }

  public onListViewUpdated(event: ListViewStateChangedEventArgs): void {
    const cmd: Command = this.tryGetCommand('ATOM_PUSH');
    if (cmd) {
      // Only enabled when at least one row is selected
      cmd.visible = event.target?.selectedRows?.length > 0;
    }
  }

  public async onExecute(event: IListViewCommandSetExecuteEventParameters): Promise<void> {
    if (event.itemId !== 'ATOM_PUSH') {
      return;
    }

    const selected = event.selectedRows ?? [];
    if (selected.length === 0) {
      Dialog.alert('No items selected.');
      return;
    }

    // Acquire AAD bearer token for AtoM API.
    // The tenant admin must register the AtoM API as a known endpoint via
    // webApiPermissionRequests in package-solution.json. SPFx then mints
    // tokens scoped to that audience automatically.
    const atomBaseUrl = this.properties.atomBaseUrl;
    const atomTenantId = this.properties.atomTenantId;
    if (!atomBaseUrl || !atomTenantId) {
      Dialog.alert('AtoM Archive Push is not configured. Tenant admin must set atomBaseUrl and atomTenantId.');
      return;
    }

    const atomClient = new AtomClient(this.context, atomBaseUrl, parseInt(atomTenantId, 10));

    // Build item references from the selected rows. SP gives us file refs;
    // we forward them to AtoM which will fetch via Graph (OBO).
    const items = selected.map((row) => ({
      site_id: this.context.pageContext.site.id.toString(),
      drive_id: row.getValueByName('UniqueId') ?? row.getValueByName('GUID') ?? '',
      item_id: row.getValueByName('ID') ?? '',
      name: row.getValueByName('FileLeafRef') ?? '',
    }));

    // Render the dialog into a host element.
    const host = document.createElement('div');
    document.body.appendChild(host);

    const onClose = (): void => {
      ReactDOM.unmountComponentAtNode(host);
      host.remove();
    };

    ReactDOM.render(
      React.createElement(PushDialog, {
        client: atomClient,
        items,
        onClose,
      }),
      host,
    );
  }
}
