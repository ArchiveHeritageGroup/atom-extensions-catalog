import { ListViewCommandSetContext } from '@microsoft/sp-listview-extensibility';
import { AadHttpClient, HttpClientResponse } from '@microsoft/sp-http';

export interface SpItemRef {
  site_id: string;
  drive_id: string;
  item_id: string;
  name?: string;
}

export interface ProjectedItem {
  sp_item_id: string;
  metadata: Record<string, unknown>;
  disposition: Record<string, unknown>;
  name?: string;
  mimeType?: string;
  size?: number;
}

export interface PushResult {
  ingest_job_id: number;
}

export interface IngestJobStatus {
  id: number;
  status?: string;
  progress?: number;
  error?: string;
  primary_object_id?: number | null;
}

/**
 * AtomClient — AAD-authed HTTP client for the AtoM/Heratio push endpoints.
 *
 * Uses SPFx's AadHttpClient which handles bearer token acquisition for the
 * AtoM API audience automatically (provided the tenant admin has approved
 * the webApiPermissionRequests entry in package-solution.json).
 */
export class AtomClient {
  private readonly aadAudience: string;

  public constructor(
    private context: ListViewCommandSetContext,
    private baseUrl: string,
    private tenantId: number,
  ) {
    // The audience matches what the AtoM API exposes (Expose an API > scope).
    // Resolve from a property or default to api://<atomClientId>.
    this.aadAudience = baseUrl.replace(/\/$/, '');
  }

  public async projection(items: SpItemRef[], driveId: number): Promise<ProjectedItem[]> {
    const resp = await this.post('/api/v2/sharepoint/push/projection', {
      tenant_id: this.tenantId,
      drive_id: driveId,
      items: items.map((i) => ({ site_id: i.site_id, drive_id: i.drive_id, item_id: i.item_id })),
    });
    if (!resp.ok) {
      throw new Error(`projection failed: ${resp.status} ${await resp.text()}`);
    }
    return await resp.json();
  }

  public async push(payload: {
    drive_id: number;
    repository_id?: number;
    parent_id?: number;
    items: Array<{ site_id: string; drive_id: string; item_id: string; metadata: Record<string, unknown> }>;
  }): Promise<PushResult> {
    const resp = await this.post('/api/v2/sharepoint/push', {
      tenant_id: this.tenantId,
      ...payload,
    });
    if (resp.status !== 201) {
      throw new Error(`push failed: ${resp.status} ${await resp.text()}`);
    }
    return await resp.json();
  }

  public async jobStatus(jobId: number): Promise<IngestJobStatus> {
    const resp = await this.get(`/api/v2/sharepoint/push/jobs/${jobId}?tenant_id=${this.tenantId}`);
    if (!resp.ok) {
      throw new Error(`job status failed: ${resp.status}`);
    }
    return await resp.json();
  }

  // ---- private helpers ----

  private async client(): Promise<AadHttpClient> {
    return await this.context.aadHttpClientFactory.getClient(this.aadAudience);
  }

  private async post(path: string, body: unknown): Promise<HttpClientResponse> {
    const c = await this.client();
    return await c.post(this.baseUrl + path, AadHttpClient.configurations.v1, {
      headers: new Headers({ 'Content-Type': 'application/json' }),
      body: JSON.stringify(body),
    });
  }

  private async get(path: string): Promise<HttpClientResponse> {
    const c = await this.client();
    return await c.get(this.baseUrl + path, AadHttpClient.configurations.v1);
  }
}
