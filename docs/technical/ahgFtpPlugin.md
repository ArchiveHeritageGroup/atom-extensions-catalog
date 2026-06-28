# ahgFtpPlugin - Technical Documentation

> Auto-generated from plugin code (2026-06-27). Browser-based FTP/SFTP upload for CSV import digital objects. Provides drag-and-drop upload interface under Import > FTP Upload so users can place files on the server without external FTP client software. Prominently shows the path to use in CSV digitalObjectPath column.

## Overview

- **Name:** FTP / SFTP Upload
- **Machine name:** `ahgFtpPlugin`
- **Version:** 1.0.0
- **Category:** import
- **Dependencies:** `ahgCorePlugin`, `ahgSettingsPlugin`
- **License:** AGPL-3.0

### Features

- Browser-based drag-and-drop file upload to FTP/SFTP server
- Multi-file upload with per-file progress bars
- Remote file listing with size, date, and delete
- Prominent CSV path warning showing exact digitalObjectPath prefix
- Admin-configurable FTP/SFTP connection settings
- Test Connection button in settings
- Supports FTP (active/passive) and SFTP protocols

## Routes

| Route name | URL | Action |
|---|---|---|
| `ftp_upload_index` | `/ftp-upload` | index |
| `ftp_upload_do` | `/ftp-upload/upload` | upload |
| `ftp_upload_chunk` | `/ftp-upload/chunk` | uploadChunk |
| `ftp_upload_list` | `/ftp-upload/list` | listFiles |
| `ftp_upload_delete` | `/ftp-upload/delete` | deleteFile |
| `ftp_upload_import` | `/ftp-upload/import-as-upload` | importAsUpload |

## Module actions

**`ftpUpload`** — `index`, `uploadChunk`, `upload`, `listFiles`, `importAsUpload`, `deleteFile`, `clearAll`

## Service layer

### `FtpService`  
`lib/Services/FtpService.php`

Public methods: `fromSettings()`, `isConfigured()`, `testConnection()`, `upload()`, `listFiles()`, `deleteFile()`, `disconnect()`, `getRemotePath()`, `clearAll()`, `formatBytes()`

## Standards & conventions

- Laravel Query Builder (Illuminate Capsule) for data access; base AtoM (Qubit) tables are read-only.
- Routes registered via `AtomFramework\Routing\RouteLoader` in the plugin config class.
- No MySQL ENUM (controlled values via `ahg_dropdown`); CSP nonce on inline scripts/styles.
