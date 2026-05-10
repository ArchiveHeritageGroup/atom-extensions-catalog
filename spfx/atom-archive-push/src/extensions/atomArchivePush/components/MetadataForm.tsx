import * as React from 'react';
import { TextField, Stack, Label } from '@fluentui/react';
import { ProjectedItem } from '../services/AtomClient';

export interface IMetadataFormProps {
  projected: ProjectedItem[];
  onChange: (updated: ProjectedItem[]) => void;
}

/**
 * Renders the editable metadata fields for the first selected item (Phase 2.B v1).
 * Multi-item review is a Phase 2.B.1 enhancement (tabbed accordion across items).
 *
 * Each row of metadata maps to an ISAD(G)-ish key. We render simple text fields;
 * a smarter version would consult sharepoint_mapping rules to know field types
 * (date_iso, html_strip, taxonomy_lookup) and render appropriate controls.
 */
export class MetadataForm extends React.Component<IMetadataFormProps> {
  public render(): React.ReactElement {
    const first = this.props.projected[0];
    if (!first) {
      return <div>No metadata to edit.</div>;
    }

    const meta = first.metadata as Record<string, string | number | null>;
    const editableKeys = Object.keys(meta).filter((k) => !k.startsWith('_'));

    return (
      <Stack tokens={{ childrenGap: 6 }}>
        <Label>Review metadata for: <strong>{first.name ?? first.sp_item_id}</strong></Label>
        {editableKeys.map((key) => (
          <TextField
            key={key}
            label={key}
            value={meta[key] !== null && meta[key] !== undefined ? String(meta[key]) : ''}
            onChange={(_, value) => {
              const updated = [...this.props.projected];
              updated[0] = {
                ...first,
                metadata: { ...first.metadata, [key]: value ?? '' },
              };
              this.props.onChange(updated);
            }}
          />
        ))}
        {first.disposition && (first.disposition as { compliance_tag?: string }).compliance_tag && (
          <div className="ms-fontSize-12 ms-fontColor-neutralSecondary">
            Compliance tag: <code>{(first.disposition as { compliance_tag: string }).compliance_tag}</code>
          </div>
        )}
      </Stack>
    );
  }
}
