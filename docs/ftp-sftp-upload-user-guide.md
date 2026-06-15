# FTP / SFTP Upload

## A Guide for Archivists and Administrators

---

## What is it?

The FTP / SFTP Upload plugin (`ahgFtpPlugin`) provides a **browser-based
drag-and-drop upload** interface for placing digital-object files on the server
without needing a separate FTP client. It is designed for CSV import workflows:
once files are uploaded, the plugin shows you the exact path to use in the
CSV `digitalObjectPath` column, so the importer can find them.

## Key features

- **Browser-based drag-and-drop upload** with per-file progress, using chunked
  transfer so large files upload reliably.
- **Folder upload** — files can be placed into a chosen subfolder on the server.
- **Remote file listing** with size, date and delete.
- **Prominent CSV path guidance** showing the exact `digitalObjectPath` prefix.
- **Three transfer modes** — FTP (active/passive), SFTP, or a `local` mode that
  writes straight to a server folder (no FTP/SFTP hop).
- **An FTP picker injected onto the Add Digital Object page**, so you can choose
  an already-uploaded remote file when attaching a digital object.
- **Test Connection** button in settings.

## How to use it

### Upload files

Open **`/ftp-upload`** (surfaced under **Import > FTP Upload**). Drag files (or a
folder) into the upload zone. Each file uploads in chunks with a progress bar and
is transferred to the configured FTP/SFTP destination. The page lists remote
files with size and date, and lets you delete them.

The page prominently displays the path prefix to put in your CSV's
`digitalObjectPath` column for the uploaded files.

### Attach during digital-object add

On any **Add Digital Object** page, an accordion panel **"Select from FTP/SFTP
server"** is injected. Open it to browse the remote files and pick one to attach,
instead of uploading from your local machine.

### Endpoints

| Route | Purpose |
|-------|---------|
| `/ftp-upload` | Upload zone + remote file listing |
| `/ftp-upload/chunk` | Chunked upload receiver (AJAX) |
| `/ftp-upload/list` | List remote files (JSON) |
| `/ftp-upload/delete` | Delete a remote file |
| `/ftp-upload/import-as-upload` | Import a remote file as a digital object |

## Administration / setup

Connection settings are stored in `ahg_settings` and managed in the admin
settings area; use the **Test Connection** button after entering them:

| Setting | Meaning |
|---------|---------|
| `ftp_protocol` | `ftp`, `sftp`, or `local` |
| `ftp_host` / `ftp_port` | Server host and port (default 22 for SFTP, 21 for FTP) |
| `ftp_username` / `ftp_password` | Credentials |
| `ftp_remote_path` | Remote destination directory (default `/uploads`) |
| `ftp_disk_path` | Server-side path the importer reads from |
| `ftp_passive_mode` | FTP passive mode toggle |

SFTP transfers use `sshpass` + `sftp`/`scp` under the hood (the PHP `ssh2`
extension is not required). The plugin depends on `ahgCorePlugin` and
`ahgSettingsPlugin`.

## Tips & FAQ

- **Large files failing?** Uploads are chunked client-side, so browser/PHP
  upload limits are far less likely to bite; check disk space and remote
  permissions if a transfer still fails.
- **Where does my CSV point?** Copy the path prefix shown on the upload page into
  the `digitalObjectPath` column.
- **No FTP server available?** Use `local` mode to write directly into a server
  folder that the importer can read.
- **Test Connection fails?** Re-check host, port, protocol and credentials; for
  SFTP confirm `sshpass` is installed on the server.
