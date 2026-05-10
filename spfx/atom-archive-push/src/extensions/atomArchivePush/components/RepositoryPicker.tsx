import * as React from 'react';
import { ComboBox, IComboBoxOption } from '@fluentui/react';
import { AtomClient } from '../services/AtomClient';

export interface IRepositoryPickerProps {
  client: AtomClient;
  onSelect: (repositoryId: number) => void;
}

interface IRepositoryPickerState {
  options: IComboBoxOption[];
  loading: boolean;
}

/**
 * Loads repositories from AtoM /api/v2/repositories (TODO: implement on AtoM side
 * or reuse existing apiv2 repositories endpoint). For Phase 2.B v1 the client
 * supplies a fetcher; if the endpoint isn't yet wired, we fall back to a free
 * text input.
 */
export class RepositoryPicker extends React.Component<IRepositoryPickerProps, IRepositoryPickerState> {
  public state: IRepositoryPickerState = { options: [], loading: true };

  public async componentDidMount(): Promise<void> {
    // TODO: this.props.client.repositories() — add to AtomClient when /api/v2/repositories is confirmed.
    // For now, allow free entry of repository id.
    this.setState({ loading: false });
  }

  public render(): React.ReactElement {
    return (
      <ComboBox
        label="Repository"
        placeholder="Type or pick a repository id"
        allowFreeform
        autoComplete="on"
        options={this.state.options}
        onChange={(_, option, __, value) => {
          const id = option?.key ? parseInt(option.key.toString(), 10) : parseInt(value ?? '0', 10);
          if (!isNaN(id) && id > 0) {
            this.props.onSelect(id);
          }
        }}
      />
    );
  }
}
