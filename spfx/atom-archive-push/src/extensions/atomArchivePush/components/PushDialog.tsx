import * as React from 'react';
import {
  Dialog,
  DialogType,
  DialogFooter,
  PrimaryButton,
  DefaultButton,
  Spinner,
  MessageBar,
  MessageBarType,
  Stack,
} from '@fluentui/react';
import { AtomClient, ProjectedItem, SpItemRef } from '../services/AtomClient';
import { RepositoryPicker } from './RepositoryPicker';
import { ParentPicker } from './ParentPicker';
import { MetadataForm } from './MetadataForm';

export interface IPushDialogProps {
  client: AtomClient;
  items: SpItemRef[];
  onClose: () => void;
}

interface IPushDialogState {
  loading: boolean;
  error?: string;
  projected: ProjectedItem[];
  repositoryId?: number;
  parentId?: number;
  jobId?: number;
  jobStatus?: string;
  driveId?: number; // sharepoint_drive.id (must be resolved by AtoM-side helper or chosen up-front)
}

/**
 * Three-step dialog:
 *   1. Loading — fetch projection from AtoM
 *   2. Form — pick repo, parent, edit metadata
 *   3. Submitting — show progress, poll job status
 *
 * Production hardening (Phase 2.B integration):
 *   - Resolve `driveId` (sharepoint_drive.id) from the SP site/list URL by calling
 *     a lookup endpoint (TODO). For v1 we ask the user to enter it in the dialog
 *     or accept the first ingest-enabled drive returned from a list endpoint.
 *   - Add a "review per-item metadata" pass when multiple items selected.
 *   - Show validation errors inline.
 */
export class PushDialog extends React.Component<IPushDialogProps, IPushDialogState> {
  public state: IPushDialogState = {
    loading: true,
    projected: [],
  };

  public async componentDidMount(): Promise<void> {
    try {
      // TODO: resolve driveId via a lookup endpoint. Placeholder: 1.
      const driveId = 1;
      const projected = await this.props.client.projection(this.props.items, driveId);
      this.setState({ loading: false, projected, driveId });
    } catch (e) {
      this.setState({ loading: false, error: (e as Error).message });
    }
  }

  private onSubmit = async (): Promise<void> => {
    if (!this.state.driveId) {
      return;
    }
    this.setState({ loading: true, error: undefined });
    try {
      const payload = {
        drive_id: this.state.driveId,
        repository_id: this.state.repositoryId,
        parent_id: this.state.parentId,
        items: this.state.projected.map((p, idx) => ({
          site_id: this.props.items[idx].site_id,
          drive_id: this.props.items[idx].drive_id,
          item_id: this.props.items[idx].item_id,
          metadata: p.metadata,
        })),
      };
      const result = await this.props.client.push(payload);
      this.setState({ loading: false, jobId: result.ingest_job_id, jobStatus: 'submitted' });
      this.poll(result.ingest_job_id);
    } catch (e) {
      this.setState({ loading: false, error: (e as Error).message });
    }
  };

  private async poll(jobId: number): Promise<void> {
    for (let i = 0; i < 60; i++) {
      try {
        const s = await this.props.client.jobStatus(jobId);
        this.setState({ jobStatus: s.status });
        if (s.status === 'completed' || s.status === 'failed') {
          return;
        }
      } catch (e) {
        // transient error, keep polling
      }
      await new Promise((r) => setTimeout(r, 2000));
    }
  }

  public render(): React.ReactElement {
    const { loading, error, projected, jobId, jobStatus } = this.state;
    return (
      <Dialog
        hidden={false}
        onDismiss={this.props.onClose}
        dialogContentProps={{
          type: DialogType.normal,
          title: 'Send to Archive',
          subText: `${this.props.items.length} item(s) selected`,
        }}
        modalProps={{ isBlocking: false }}
      >
        {error && <MessageBar messageBarType={MessageBarType.error}>{error}</MessageBar>}
        {loading && <Spinner label="Working…" />}

        {!loading && !jobId && (
          <Stack tokens={{ childrenGap: 12 }}>
            <RepositoryPicker
              client={this.props.client}
              onSelect={(repositoryId) => this.setState({ repositoryId })}
            />
            <ParentPicker
              client={this.props.client}
              repositoryId={this.state.repositoryId}
              onSelect={(parentId) => this.setState({ parentId })}
            />
            <MetadataForm
              projected={projected}
              onChange={(updated) => this.setState({ projected: updated })}
            />
          </Stack>
        )}

        {jobId && (
          <Stack tokens={{ childrenGap: 8 }}>
            <div>Ingest job <strong>#{jobId}</strong> — status: {jobStatus ?? 'pending'}</div>
            {jobStatus === 'completed' && (
              <MessageBar messageBarType={MessageBarType.success}>
                Items pushed to AtoM successfully.
              </MessageBar>
            )}
            {jobStatus === 'failed' && (
              <MessageBar messageBarType={MessageBarType.error}>
                Ingest job failed. Check AtoM event log for details.
              </MessageBar>
            )}
          </Stack>
        )}

        <DialogFooter>
          {!jobId && (
            <PrimaryButton onClick={this.onSubmit} disabled={loading}>
              Push to AtoM
            </PrimaryButton>
          )}
          <DefaultButton onClick={this.props.onClose}>
            {jobId ? 'Close' : 'Cancel'}
          </DefaultButton>
        </DialogFooter>
      </Dialog>
    );
  }
}
