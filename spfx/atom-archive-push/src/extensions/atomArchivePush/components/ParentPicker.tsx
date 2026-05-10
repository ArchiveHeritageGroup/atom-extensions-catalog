import * as React from 'react';
import { TextField } from '@fluentui/react';
import { AtomClient } from '../services/AtomClient';

export interface IParentPickerProps {
  client: AtomClient;
  repositoryId?: number;
  onSelect: (parentId: number | undefined) => void;
}

/**
 * Free-text input for parent IO id. Phase 2.B v1.
 *
 * Phase 2.B.1 enhancement: replace with autocomplete that calls
 * /api/v2/informationobjects?q=&repository_id= and shows title + slug + level.
 * That endpoint exists on the AtoM apiv2 module already; just needs wiring.
 */
export class ParentPicker extends React.Component<IParentPickerProps> {
  public render(): React.ReactElement {
    return (
      <TextField
        label="Parent information object id (optional)"
        placeholder="Leave blank for top-level"
        type="number"
        onChange={(_, value) => {
          const v = value && value.trim() !== '' ? parseInt(value, 10) : undefined;
          this.props.onSelect(Number.isNaN(v as number) ? undefined : v);
        }}
      />
    );
  }
}
