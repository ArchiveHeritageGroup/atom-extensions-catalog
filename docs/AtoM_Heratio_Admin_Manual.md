# AtoM Heratio — Administrator Manual

**For:** System Administrators, IT Staff, Compliance Officers
**Product:** AtoM Heratio Framework v2.8.2
**Date:** 16 March 2026
**Author:** The Archive and Heritage Group (Pty) Ltd

---

## About This Manual

This manual covers system administration: settings, backup, security, user management, and infrastructure. For end-user workflows (browse, search, records), see the **User Manual**. For development, see the **Technical Manual**.

---

## 1. Admin Panel Overview

**How to get there:** Admin menu in the navbar (requires administrator role)

<div style="overflow-x:auto;margin:1rem 0"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 459 244" style="max-width:100%;height:auto;font-family:ui-monospace,Menlo,Consolas,monospace"><rect x="0.5" y="0.5" width="458" height="243" rx="8" fill="#f7faf9" stroke="#d8e6e3"/><line x1="13.6" y1="34.0" x2="17.2" y2="34.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="26.0" x2="13.6" y2="34.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="34.0" x2="13.6" y2="42.0" stroke="#10373E" stroke-width="1.3"/><line x1="17.2" y1="34.0" x2="20.8" y2="34.0" stroke="#10373E" stroke-width="1.3"/><line x1="20.8" y1="34.0" x2="24.4" y2="34.0" stroke="#10373E" stroke-width="1.3"/><line x1="24.4" y1="34.0" x2="28.0" y2="34.0" stroke="#10373E" stroke-width="1.3"/><line x1="28.0" y1="34.0" x2="31.6" y2="34.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="50.0" x2="17.2" y2="50.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="42.0" x2="13.6" y2="50.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="50.0" x2="13.6" y2="58.0" stroke="#10373E" stroke-width="1.3"/><line x1="17.2" y1="50.0" x2="20.8" y2="50.0" stroke="#10373E" stroke-width="1.3"/><line x1="20.8" y1="50.0" x2="24.4" y2="50.0" stroke="#10373E" stroke-width="1.3"/><line x1="24.4" y1="50.0" x2="28.0" y2="50.0" stroke="#10373E" stroke-width="1.3"/><line x1="28.0" y1="50.0" x2="31.6" y2="50.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="66.0" x2="17.2" y2="66.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="58.0" x2="13.6" y2="66.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="66.0" x2="13.6" y2="74.0" stroke="#10373E" stroke-width="1.3"/><line x1="17.2" y1="66.0" x2="20.8" y2="66.0" stroke="#10373E" stroke-width="1.3"/><line x1="20.8" y1="66.0" x2="24.4" y2="66.0" stroke="#10373E" stroke-width="1.3"/><line x1="24.4" y1="66.0" x2="28.0" y2="66.0" stroke="#10373E" stroke-width="1.3"/><line x1="28.0" y1="66.0" x2="31.6" y2="66.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="82.0" x2="17.2" y2="82.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="74.0" x2="13.6" y2="82.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="82.0" x2="13.6" y2="90.0" stroke="#10373E" stroke-width="1.3"/><line x1="17.2" y1="82.0" x2="20.8" y2="82.0" stroke="#10373E" stroke-width="1.3"/><line x1="20.8" y1="82.0" x2="24.4" y2="82.0" stroke="#10373E" stroke-width="1.3"/><line x1="24.4" y1="82.0" x2="28.0" y2="82.0" stroke="#10373E" stroke-width="1.3"/><line x1="28.0" y1="82.0" x2="31.6" y2="82.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="98.0" x2="17.2" y2="98.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="90.0" x2="13.6" y2="98.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="98.0" x2="13.6" y2="106.0" stroke="#10373E" stroke-width="1.3"/><line x1="17.2" y1="98.0" x2="20.8" y2="98.0" stroke="#10373E" stroke-width="1.3"/><line x1="20.8" y1="98.0" x2="24.4" y2="98.0" stroke="#10373E" stroke-width="1.3"/><line x1="24.4" y1="98.0" x2="28.0" y2="98.0" stroke="#10373E" stroke-width="1.3"/><line x1="28.0" y1="98.0" x2="31.6" y2="98.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="114.0" x2="17.2" y2="114.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="106.0" x2="13.6" y2="114.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="114.0" x2="13.6" y2="122.0" stroke="#10373E" stroke-width="1.3"/><line x1="17.2" y1="114.0" x2="20.8" y2="114.0" stroke="#10373E" stroke-width="1.3"/><line x1="20.8" y1="114.0" x2="24.4" y2="114.0" stroke="#10373E" stroke-width="1.3"/><line x1="24.4" y1="114.0" x2="28.0" y2="114.0" stroke="#10373E" stroke-width="1.3"/><line x1="28.0" y1="114.0" x2="31.6" y2="114.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="130.0" x2="17.2" y2="130.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="122.0" x2="13.6" y2="130.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="130.0" x2="13.6" y2="138.0" stroke="#10373E" stroke-width="1.3"/><line x1="17.2" y1="130.0" x2="20.8" y2="130.0" stroke="#10373E" stroke-width="1.3"/><line x1="20.8" y1="130.0" x2="24.4" y2="130.0" stroke="#10373E" stroke-width="1.3"/><line x1="24.4" y1="130.0" x2="28.0" y2="130.0" stroke="#10373E" stroke-width="1.3"/><line x1="28.0" y1="130.0" x2="31.6" y2="130.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="146.0" x2="17.2" y2="146.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="138.0" x2="13.6" y2="146.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="146.0" x2="13.6" y2="154.0" stroke="#10373E" stroke-width="1.3"/><line x1="17.2" y1="146.0" x2="20.8" y2="146.0" stroke="#10373E" stroke-width="1.3"/><line x1="20.8" y1="146.0" x2="24.4" y2="146.0" stroke="#10373E" stroke-width="1.3"/><line x1="24.4" y1="146.0" x2="28.0" y2="146.0" stroke="#10373E" stroke-width="1.3"/><line x1="28.0" y1="146.0" x2="31.6" y2="146.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="162.0" x2="17.2" y2="162.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="154.0" x2="13.6" y2="162.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="162.0" x2="13.6" y2="170.0" stroke="#10373E" stroke-width="1.3"/><line x1="17.2" y1="162.0" x2="20.8" y2="162.0" stroke="#10373E" stroke-width="1.3"/><line x1="20.8" y1="162.0" x2="24.4" y2="162.0" stroke="#10373E" stroke-width="1.3"/><line x1="24.4" y1="162.0" x2="28.0" y2="162.0" stroke="#10373E" stroke-width="1.3"/><line x1="28.0" y1="162.0" x2="31.6" y2="162.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="178.0" x2="17.2" y2="178.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="170.0" x2="13.6" y2="178.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="178.0" x2="13.6" y2="186.0" stroke="#10373E" stroke-width="1.3"/><line x1="17.2" y1="178.0" x2="20.8" y2="178.0" stroke="#10373E" stroke-width="1.3"/><line x1="20.8" y1="178.0" x2="24.4" y2="178.0" stroke="#10373E" stroke-width="1.3"/><line x1="24.4" y1="178.0" x2="28.0" y2="178.0" stroke="#10373E" stroke-width="1.3"/><line x1="28.0" y1="178.0" x2="31.6" y2="178.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="194.0" x2="17.2" y2="194.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="186.0" x2="13.6" y2="194.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="194.0" x2="13.6" y2="202.0" stroke="#10373E" stroke-width="1.3"/><line x1="17.2" y1="194.0" x2="20.8" y2="194.0" stroke="#10373E" stroke-width="1.3"/><line x1="20.8" y1="194.0" x2="24.4" y2="194.0" stroke="#10373E" stroke-width="1.3"/><line x1="24.4" y1="194.0" x2="28.0" y2="194.0" stroke="#10373E" stroke-width="1.3"/><line x1="28.0" y1="194.0" x2="31.6" y2="194.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="210.0" x2="17.2" y2="210.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="202.0" x2="13.6" y2="210.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="210.0" x2="13.6" y2="218.0" stroke="#10373E" stroke-width="1.3"/><line x1="17.2" y1="210.0" x2="20.8" y2="210.0" stroke="#10373E" stroke-width="1.3"/><line x1="20.8" y1="210.0" x2="24.4" y2="210.0" stroke="#10373E" stroke-width="1.3"/><line x1="24.4" y1="210.0" x2="28.0" y2="210.0" stroke="#10373E" stroke-width="1.3"/><line x1="28.0" y1="210.0" x2="31.6" y2="210.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="226.0" x2="17.2" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="218.0" x2="13.6" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="17.2" y1="226.0" x2="20.8" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="20.8" y1="226.0" x2="24.4" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="24.4" y1="226.0" x2="28.0" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="28.0" y1="226.0" x2="31.6" y2="226.0" stroke="#10373E" stroke-width="1.3"/><text x="10.0" y="22.0" font-size="9.5" fill="#10373E">Admin</text><text x="53.2" y="22.0" font-size="9.5" fill="#10373E">Menu</text><text x="38.8" y="38.0" font-size="9.5" fill="#10373E">Plugins</text><text x="233.2" y="38.0" font-size="9.5" fill="#10373E">—</text><text x="247.6" y="38.0" font-size="9.5" fill="#10373E">Enable/disable</text><text x="355.6" y="38.0" font-size="9.5" fill="#10373E">AHG</text><text x="384.4" y="38.0" font-size="9.5" fill="#10373E">plugins</text><text x="38.8" y="54.0" font-size="9.5" fill="#10373E">Themes</text><text x="233.2" y="54.0" font-size="9.5" fill="#10373E">—</text><text x="247.6" y="54.0" font-size="9.5" fill="#10373E">Theme</text><text x="290.8" y="54.0" font-size="9.5" fill="#10373E">selection</text><text x="38.8" y="70.0" font-size="9.5" fill="#10373E">Settings</text><text x="103.6" y="70.0" font-size="9.5" fill="#10373E">(base</text><text x="146.8" y="70.0" font-size="9.5" fill="#10373E">AtoM)</text><text x="233.2" y="70.0" font-size="9.5" fill="#10373E">—</text><text x="247.6" y="70.0" font-size="9.5" fill="#10373E">Core</text><text x="283.6" y="70.0" font-size="9.5" fill="#10373E">AtoM</text><text x="319.6" y="70.0" font-size="9.5" fill="#10373E">settings</text><text x="38.8" y="86.0" font-size="9.5" fill="#10373E">AHG</text><text x="67.6" y="86.0" font-size="9.5" fill="#10373E">Settings</text><text x="233.2" y="86.0" font-size="9.5" fill="#10373E">—</text><text x="247.6" y="86.0" font-size="9.5" fill="#10373E">21</text><text x="269.2" y="86.0" font-size="9.5" fill="#10373E">sections,</text><text x="341.2" y="86.0" font-size="9.5" fill="#10373E">200</text><text x="377.2" y="86.0" font-size="9.5" fill="#10373E">options</text><text x="38.8" y="102.0" font-size="9.5" fill="#10373E">Users</text><text x="82.0" y="102.0" font-size="9.5" fill="#10373E">&amp;</text><text x="96.4" y="102.0" font-size="9.5" fill="#10373E">Groups</text><text x="233.2" y="102.0" font-size="9.5" fill="#10373E">—</text><text x="247.6" y="102.0" font-size="9.5" fill="#10373E">User</text><text x="283.6" y="102.0" font-size="9.5" fill="#10373E">accounts,</text><text x="355.6" y="102.0" font-size="9.5" fill="#10373E">roles,</text><text x="406.0" y="102.0" font-size="9.5" fill="#10373E">ACL</text><text x="38.8" y="118.0" font-size="9.5" fill="#10373E">Menus</text><text x="233.2" y="118.0" font-size="9.5" fill="#10373E">—</text><text x="247.6" y="118.0" font-size="9.5" fill="#10373E">Navigation</text><text x="326.8" y="118.0" font-size="9.5" fill="#10373E">menu</text><text x="362.8" y="118.0" font-size="9.5" fill="#10373E">management</text><text x="38.8" y="134.0" font-size="9.5" fill="#10373E">Static</text><text x="89.2" y="134.0" font-size="9.5" fill="#10373E">pages</text><text x="233.2" y="134.0" font-size="9.5" fill="#10373E">—</text><text x="247.6" y="134.0" font-size="9.5" fill="#10373E">Static</text><text x="298.0" y="134.0" font-size="9.5" fill="#10373E">page</text><text x="334.0" y="134.0" font-size="9.5" fill="#10373E">content</text><text x="38.8" y="150.0" font-size="9.5" fill="#10373E">Visible</text><text x="96.4" y="150.0" font-size="9.5" fill="#10373E">elements</text><text x="233.2" y="150.0" font-size="9.5" fill="#10373E">—</text><text x="247.6" y="150.0" font-size="9.5" fill="#10373E">Show/hide</text><text x="319.6" y="150.0" font-size="9.5" fill="#10373E">interface</text><text x="391.6" y="150.0" font-size="9.5" fill="#10373E">elements</text><text x="38.8" y="166.0" font-size="9.5" fill="#10373E">Backup</text><text x="89.2" y="166.0" font-size="9.5" fill="#10373E">&amp;</text><text x="103.6" y="166.0" font-size="9.5" fill="#10373E">Restore</text><text x="233.2" y="166.0" font-size="9.5" fill="#10373E">—</text><text x="247.6" y="166.0" font-size="9.5" fill="#10373E">Backup</text><text x="298.0" y="166.0" font-size="9.5" fill="#10373E">management</text><text x="38.8" y="182.0" font-size="9.5" fill="#10373E">Queue</text><text x="233.2" y="182.0" font-size="9.5" fill="#10373E">—</text><text x="247.6" y="182.0" font-size="9.5" fill="#10373E">Background</text><text x="326.8" y="182.0" font-size="9.5" fill="#10373E">job</text><text x="355.6" y="182.0" font-size="9.5" fill="#10373E">queue</text><text x="38.8" y="198.0" font-size="9.5" fill="#10373E">Audit</text><text x="82.0" y="198.0" font-size="9.5" fill="#10373E">Trail</text><text x="233.2" y="198.0" font-size="9.5" fill="#10373E">—</text><text x="247.6" y="198.0" font-size="9.5" fill="#10373E">Activity</text><text x="312.4" y="198.0" font-size="9.5" fill="#10373E">logging</text><text x="38.8" y="214.0" font-size="9.5" fill="#10373E">Reports</text><text x="233.2" y="214.0" font-size="9.5" fill="#10373E">—</text><text x="247.6" y="214.0" font-size="9.5" fill="#10373E">Reporting</text><text x="319.6" y="214.0" font-size="9.5" fill="#10373E">dashboard</text><text x="38.8" y="230.0" font-size="9.5" fill="#10373E">Help</text><text x="74.8" y="230.0" font-size="9.5" fill="#10373E">Center</text><text x="233.2" y="230.0" font-size="9.5" fill="#10373E">—</text><text x="247.6" y="230.0" font-size="9.5" fill="#10373E">Help</text><text x="283.6" y="230.0" font-size="9.5" fill="#10373E">articles</text></svg></div>

---

## 2. AHG Settings

**How to get there:** Admin > AHG Settings

The central configuration hub. Every option is documented below, organized by section.

### How Settings Work

- Settings are stored in the `ahg_settings` database table
- Each setting has a key, value, group, and type
- Changes take effect immediately (no restart needed)
- Some sections only appear when the related plugin is enabled

---

### 2.1 General — Theme Configuration

Controls the visual appearance of the site.

| Setting | Type | Default | Description |
|---------|------|---------|-------------|
| Enable AHG Theme | Toggle | On | Master switch for AHG theme customizations. When off, falls back to base AtoM theme. |
| Custom Logo | Text path | (empty) | Path to a custom logo image relative to web root (e.g., `/uploads/logo.png`). Leave blank for default. |
| Primary Color | Color picker | #1a5f7a | Main brand color used in navbar, headings, and primary buttons. |
| Secondary Color | Color picker | #57837b | Accent color used for hover states and secondary elements. |
| Card Header Background | Color picker | #1a5f2a | Background color for all card headers throughout the site. |
| Card Header Text | Color picker | #ffffff | Text color in card headers. Must contrast with Card Header Background. |
| Button Background | Color picker | #1a5f2a | Primary button background color. |
| Button Text | Color picker | #ffffff | Primary button text color. |
| Link Color | Color picker | #1a5f2a | Color for all hyperlinks. |
| Sidebar Background | Color picker | #f8f9fa | Background color for the left sidebar on two-column pages. |
| Sidebar Text | Color picker | #333333 | Text color in the sidebar. |
| Footer Text | Text | (empty) | Custom text displayed in the site footer. Leave blank to hide footer. |
| Show Branding | Toggle | On | Display "Powered by AtoM Heratio" branding in footer. |
| Custom CSS | Textarea | (empty) | Additional CSS rules injected after the theme stylesheet. Use for institution-specific styling without modifying theme files. |

**Tips:**
- Use a colour contrast checker to ensure text colours meet WCAG AA (4.5:1 ratio)
- Custom CSS is injected with a CSP nonce — inline styles in the textarea are safe

---

### 2.2 Collections Procedures — Collections Management

Controls Collections Procedures.

| Setting | Type | Default | Description |
|---------|------|---------|-------------|
| Enable Collections Procedures | Toggle | On | Master switch. When off, Collections Procedures features are hidden from all menus and record pages. |
| Default Currency | Select | ZAR | Currency for valuation records. Options: ZAR (South African Rand), USD, EUR, GBP. |
| Valuation Reminder | Number (days) | 365 | System will flag items for re-valuation after this many days since last valuation. Range: 30–1825. |
| Default Loan Period | Number (days) | 90 | Default duration for new loan records. Range: 1–365. |
| Condition Check Interval | Number (days) | 180 | Recommended interval between condition checks. Items overdue for a check are flagged. Range: 30–730. |
| Auto-create Movements | Toggle | On | When an object's location is changed, automatically create a movement record in the audit trail. |
| Require Photos | Toggle | Off | When on, condition reports cannot be saved without at least one photo attached. |
| Email Notifications | Toggle | On | Send email notifications when tasks are assigned (e.g., condition check, valuation due). |

---

### 2.3 Media — Media Player

Controls the HTML5 audio/video player behaviour.

| Setting | Type | Default | Description |
|---------|------|---------|-------------|
| Player Type | Select | enhanced | **basic:** minimal HTML5 controls. **enhanced:** waveform display, transcription panel, playback speed. |
| Auto-play | Toggle | Off | Auto-play media when the page loads. Note: most browsers block autoplay with sound. |
| Show Controls | Toggle | On | Display player controls. When off, media plays but user cannot pause/seek. |
| Loop Playback | Toggle | Off | Automatically restart media when it reaches the end. |
| Default Volume | Slider | 0.8 | Initial volume level. Range: 0 (muted) to 1.0 (full). |
| Show Download | Toggle | Off | Display a download button on the player. When off, users must use the record's export options. |

---

### 2.4 Photos — Condition Photo Upload

Controls how condition assessment photos are stored and processed.

| Setting | Type | Default | Description |
|---------|------|---------|-------------|
| Upload Path | Text path | `{atom_root}/uploads/condition_photos` | Absolute filesystem path where condition photos are stored. |
| Max Upload Size | Select | 10 MB | Maximum file size per photo. Options: 5 MB, 10 MB, 20 MB, 50 MB. |
| Create Thumbnails | Toggle | On | Auto-generate thumbnails at three sizes when a photo is uploaded. |
| Thumbnail Small | Pixels | 150 | Maximum dimension for small thumbnails. Range: 50–300. |
| Thumbnail Medium | Pixels | 300 | Maximum dimension for medium thumbnails. Range: 100–600. |
| Thumbnail Large | Pixels | 600 | Maximum dimension for large thumbnails. Range: 300–1200. |
| JPEG Quality | Slider | 85 | Compression quality for generated thumbnails. Range: 60–100. Higher = larger files, better quality. |
| Extract EXIF | Toggle | On | Read camera information (date taken, camera model, GPS) from photo EXIF data. |
| Auto-rotate | Toggle | On | Automatically rotate photos based on EXIF orientation tag. Prevents sideways photos. |

---

### 2.5 Data Protection — Compliance

Controls privacy compliance features.

| Setting | Type | Default | Description |
|---------|------|---------|-------------|
| Enable Module | Toggle | On | Master switch for data protection features. |
| Default Regulation | Select | POPIA | Default privacy regulation. Options: POPIA (South Africa), GDPR (EU), PAIA (South Africa — access), CCPA (California). |
| Notify Overdue | Toggle | On | Send email when a data subject request exceeds the response deadline. |
| Notification Email | Email | (empty) | Recipient for overdue request notifications. |
| POPIA Request Fee | Number (ZAR) | 50 | Standard fee charged for POPIA information requests. |
| Special Category Fee | Number (ZAR) | 140 | Fee for requests involving special categories of personal information. |
| Response Days | Number (days) | 30 | Deadline in days for responding to data subject requests. Range: 1–90. |

---

### 2.6 IIIF — Image Viewer

Controls the high-resolution image viewer.

| Setting | Type | Default | Description |
|---------|------|---------|-------------|
| Enable IIIF | Toggle | On | Master switch. When off, images display as simple `<img>` tags. |
| Viewer Library | Select | OpenSeadragon | **OpenSeadragon:** lightweight, fast. **Mirador:** full-featured with annotations. **Leaflet:** map-style viewer. |
| IIIF Server URL | URL | (empty) | URL of an external IIIF Image API server. Leave blank to use the built-in Cantaloupe server. |
| Show Navigator | Toggle | On | Display a mini-map in the corner for orientation on large images. |
| Enable Rotation | Toggle | On | Show rotation controls in the viewer toolbar. |
| Max Zoom Level | Number | 10 | Maximum zoom level. Range: 1–20. Higher values allow deeper zoom on high-resolution images. |

---

### 2.7 Jobs — Background Processing

Controls the background job system.

| Setting | Type | Default | Description |
|---------|------|---------|-------------|
| Enable Jobs | Toggle | On | Master switch for background job processing. When off, all tasks run synchronously. |
| Max Concurrent | Number | 2 | Maximum jobs running simultaneously. Range: 1–10. Higher values need more server resources. |
| Timeout | Seconds | 3600 | Maximum time a single job can run before being killed. Range: 60–86400 (1 min to 24 hours). |
| Retry Attempts | Number | 3 | How many times a failed job is retried. Range: 0–10. |
| Cleanup After | Days | 30 | Completed jobs are deleted from the database after this many days. Range: 1–365. |
| Notify on Failure | Toggle | On | Send email when a background job fails. |
| Notification Email | Email | (empty) | Recipient for job failure notifications. |

---

### 2.8 Fuseki — RiC Triplestore

Controls the Records in Contexts (RiC) linked data integration.

| Setting | Type | Default | Description |
|---------|------|---------|-------------|
| SPARQL Endpoint | URL | http://localhost:3030/ric | Full URL to the Apache Fuseki SPARQL endpoint. |
| Username | Text | admin | Fuseki authentication username. |
| Password | Password | (hidden) | Fuseki authentication password. Not displayed after saving. |
| Enable Auto Sync | Toggle | On | Master switch for all RiC synchronization. When off, no data flows to Fuseki. |
| Use Async Queue | Toggle | On | Queue sync operations for background processing instead of blocking the user. |
| Sync on Save | Toggle | On | Push record data to Fuseki whenever a record is created or updated. |
| Sync on Delete | Toggle | On | Remove record data from Fuseki when a record is deleted in AtoM. |
| Cascade Delete | Toggle | On | When deleting, also remove triples where the deleted record appears as an object (not just subject). |
| Batch Size | Number | 100 | Records per batch during bulk sync operations. Range: 10–1000. |
| Integrity Schedule | Select | weekly | How often to run integrity checks between AtoM and Fuseki. Options: daily, weekly, monthly, disabled. |
| Orphan Retention | Days | 30 | Orphaned triples (in Fuseki but not AtoM) are kept for this many days before cleanup. Range: 1–365. |

---

### 2.9 Metadata — Extraction Configuration

Controls automatic metadata extraction from uploaded files.

| Setting | Type | Default | Description |
|---------|------|---------|-------------|
| Extract on Upload | Toggle | On | Automatically extract embedded metadata when digital objects are uploaded. |
| Auto-Populate | Toggle | On | Populate AtoM description fields with extracted metadata values. |
| Images | Toggle | On | Extract from image files (EXIF, IPTC, XMP). |
| PDF | Toggle | On | Extract from PDF files (author, title, keywords). |
| Office | Toggle | On | Extract from Office documents (Word, Excel — author, title). |
| Video | Toggle | On | Extract from video files (duration, dimensions, codec). |
| Audio | Toggle | On | Extract from audio files (duration, artist, album). |

**Field Mapping** — configurable per GLAM sector (ISAD, Museum, DAM). Each extracted metadata field can be mapped to a specific AtoM field or set to "none" to skip. Mappable fields: Title, Creator, Keywords, Description, Date Created, Copyright, Technical Data, GPS Location.

---

### 2.10 Faces — Face Detection

| Setting | Type | Default | Description |
|---------|------|---------|-------------|
| Enable | Toggle | Off | **Experimental.** Enable face detection in digital objects. |
| Backend | Select | local | **local:** OpenCV (free, runs on server). **aws:** AWS Rekognition (cloud, paid). **azure:** Azure Face API (cloud, paid). |

---

### 2.11 Ingest — Data Ingest Defaults

Default settings for the 6-step data ingest wizard.

**AI Processing Toggles:**

| Setting | Default | Backend |
|---------|---------|---------|
| Virus Scan | On | ClamAV |
| OCR | Off | Tesseract |
| NER | Off | Python/spaCy |
| Auto-Summarize | Off | Python |
| Spell Check | Off | aspell |
| Format ID | Off | Siegfried/PRONOM |
| Face Detection | Off | OpenCV/AWS/Azure |
| Auto-Translate | Off | Argos Translate |

**Translation/Spellcheck:**

| Setting | Type | Default |
|---------|------|---------|
| Translate from | Select | English |
| Translate to | Select | Afrikaans |
| Spellcheck language | Select | en_ZA |

**Output Defaults:**

| Setting | Type | Default |
|---------|------|---------|
| Create AtoM records | Toggle | On |
| Generate SIP | Toggle | Off |
| Generate AIP | Toggle | Off |
| Generate DIP | Toggle | Off |
| Generate thumbnails | Toggle | On |
| Generate reference images | Toggle | On |
| SIP/AIP/DIP output paths | Text | (empty) |
| Default sector | Select | archive |
| Default standard | Select | ISAD(G) |

A **Service Availability** dashboard shows the status of each backend (installed/available/unavailable).

---

### 2.12 Portable Export

| Setting | Type | Default | Description |
|---------|------|---------|-------------|
| Enable | Toggle | On | Allow creation of offline portable catalogues. |
| Retention | Days | 30 | Auto-delete generated exports after this many days. |
| Include Digital Objects | Toggle | On | Include original digital objects in export. |
| Include Thumbnails | Toggle | On | Include thumbnail images. |
| Include References | Toggle | On | Include reference-size images. |
| Include Masters | Toggle | Off | Include master files (large — significantly increases export size). |
| Default Mode | Select | read_only | **read_only:** browse-only viewer. **editable:** allows local editing. |
| Default Language | Select | en | Language for the portable viewer interface. |
| Max Size (MB) | Number | 2048 | Maximum export file size. Range: 100–10240. |
| Show on Description Pages | Toggle | On | Display "Portable Viewer" button on record export options. |
| Show on Clipboard | Toggle | On | Display "Portable Catalogue" option on clipboard page. |

---

### 2.13 Encryption

| Setting | Type | Default | Description |
|---------|------|---------|-------------|
| Enable Encryption | Toggle | Off | Master switch. **Requires** encryption key at `/etc/atom/encryption.key` (permissions 0600). |
| Encrypt Derivatives | Toggle | On | Also encrypt thumbnail and reference images (not just masters). |
| Contact Details | Toggle | Off | Encrypt email, address, telephone fields. |
| Financial Data | Toggle | Off | Encrypt appraisal values in accession records. |
| Donor Information | Toggle | Off | Encrypt biographical/administrative history. |
| Personal Notes | Toggle | Off | Encrypt internal staff notes. |
| Access Restrictions | Toggle | Off | Encrypt rights notes and restriction details. |

**Algorithm:** XChaCha20-Poly1305 (libsodium, preferred) or AES-256-GCM (OpenSSL fallback).

---

### 2.14 Voice & AI

| Setting | Type | Default | Description |
|---------|------|---------|-------------|
| Enable Voice | Toggle | On | Enable voice command system for all users. |
| Language | Select | en-US | Recognition language. 11 options: en-US, en-GB, af-ZA, zu-ZA, xh-ZA, st-ZA, fr-FR, pt-PT, es-ES, de-DE. |
| Confidence | Slider | 0.4 | Minimum confidence threshold. Lower = more lenient (may misrecognize). Higher = stricter. Range: 0.3–0.95. |
| Speech Rate | Slider | 1.0 | Text-to-speech playback speed. Range: 0.5 (slow) to 2.0 (fast). |
| Continuous Listen | Toggle | Off | Keep microphone active after each command (hands-free mode). |
| Floating Button | Toggle | On | Show floating microphone button on all pages (bottom-right). |
| Hover Read | Toggle | On | Read button/link text aloud when mouse hovers. |
| Hover Delay | Slider | 400ms | Delay before hover-read activates. Range: 100–1000ms. |
| LLM Provider | Select | hybrid | **local:** Ollama only. **cloud:** Anthropic Claude only. **hybrid:** try local, fall back to cloud. |
| Daily Cloud Limit | Number | 50 | Maximum cloud API calls per day. 0 = unlimited. |
| Local LLM URL | URL | http://localhost:11434 | Ollama API endpoint. |
| Local LLM Model | Text | llava:7b | Vision model name (must be pulled in Ollama). |
| Timeout | Seconds | 30 | LLM request timeout. Range: 5–300. |
| Cloud API Key | Password | (hidden) | Anthropic API key. Stored encrypted. |
| Cloud Model | Text | claude-sonnet-4-20250514 | Anthropic model ID for image description. |
| Audit AI Calls | Toggle | On | Log every AI image description request to the audit trail. |

---

### 2.15 Integrity — Verification

| Setting | Type | Default | Description |
|---------|------|---------|-------------|
| Enable | Toggle | On | Master switch for integrity verification. |
| Auto Baselines | Toggle | On | Automatically generate checksum baselines for objects that don't have one. |
| Algorithm | Select | sha256 | **sha256:** faster, sufficient for most use. **sha512:** more secure, slower. |
| Batch Size | Number | 200 | Objects processed per verification run. 0 = unlimited. Range: 0–50000. |
| IO Throttle | Milliseconds | 10 | Pause between objects to reduce disk I/O impact. Range: 0–1000. |
| Max Runtime | Minutes | 120 | Maximum duration for a verification run. Range: 1–1440 (24 hours). |
| Max Memory | MB | 512 | Memory limit per run. Range: 64–4096. |
| Dead Letter | Number | 3 | Consecutive failures on an object before escalation alert. Range: 1–100. |
| Notify on Failure | Toggle | On | Email when a verification run fails. |
| Notify on Mismatch | Toggle | On | Email when a file's checksum doesn't match its baseline. |
| Alert Email | Email | (empty) | Notification recipient. |
| Webhook URL | URL | (empty) | POST notifications to Slack, Teams, or PagerDuty. |

---

### 2.16 Accession — Intake Settings

| Setting | Type | Default | Description |
|---------|------|---------|-------------|
| Numbering Mask | Text | ACC-{YYYY}-{####} | Pattern for auto-generated accession numbers. `{YYYY}` = year, `{####}` = zero-padded sequence. |
| Default Priority | Select | normal | Default for new accessions. Options: low, normal, high, urgent. |
| Auto-Assign | Toggle | Off | Automatically assign new accessions to the creating archivist. |
| Require Donor Agreement | Toggle | Off | Block finalization until a donor agreement is attached. |
| Require Appraisal | Toggle | Off | Block finalization until appraisal is completed. |
| Allow Container Barcodes | Toggle | Off | Enable barcode scanning for accession containers. |
| Rights Inheritance | Toggle | Off | Automatically copy rights from the donor agreement to the accession. |

---

### 2.17 Authority — Authority Records

| Setting | Type | Default | Description |
|---------|------|---------|-------------|
| Wikidata | Toggle | Off | Enable Wikidata entity linking and reconciliation. |
| VIAF | Toggle | Off | Virtual International Authority File linking. |
| Getty ULAN | Toggle | Off | Union List of Artist Names linking. |
| LCNAF | Toggle | Off | Library of Congress Name Authority File. |
| ISNI | Toggle | Off | International Standard Name Identifier. |
| Auto-Verify Wikidata | Toggle | Off | Automatically mark Wikidata identifiers as verified. |
| Auto-Recalculate Completeness | Toggle | On | Recalculate completeness scores when records are saved. |
| Hide Stubs from Public | Toggle | On | Stub-level authority records are hidden from public browse/search. |
| NER Auto-Create Stubs | Toggle | Off | Auto-create authority stubs from NER-extracted entities. |
| NER Confidence Threshold | Number | 0.85 | Minimum NER confidence to auto-create. Range: 0.0–1.0. |
| Require Approval for Merge | Toggle | Off | Merging authorities requires workflow approval. |
| Dedup Threshold | Number | 0.80 | Similarity score for duplicate detection. Range: 0.0–1.0. |
| Function Linking | Toggle | On | Enable ISDF actor-to-function structured linking. |

---

### 2.18 Security — Access Control

| Setting | Type | Default | Description |
|---------|------|---------|-------------|
| Password Expiry | Days | 90 | Force password change after this many days. 0 = never expires. Range: 0–365. |
| Password History | Number | 5 | Remember this many previous passwords (user cannot reuse them). 0 = disabled. Range: 0–24. |
| Expiry Warning | Days | 14 | Show warning this many days before password expires. Range: 0–90. |
| Show Expiry Notification | Toggle | On | Display flash notification on login when password is expiring soon. |
| Force Password Change | Toggle | Off | When on, expired passwords redirect to the change password page. When off, user sees a warning but can continue. |
| Enable Lockout | Toggle | On | Lock accounts after too many failed login attempts. |
| Max Failed Attempts | Number | 5 | Number of consecutive failures before lockout. Range: 1–20. |
| Lockout Duration | Minutes | 15 | How long the account stays locked. Range: 1–1440 (24 hours). |
| Session Timeout | Minutes | 30 | Idle sessions expire after this many minutes. Range: 5–480 (8 hours). |
| Login Attempt Retention | Hours | 24 | Failed login attempt records are kept for this many hours. Range: 1–720 (30 days). |

**Security Status** — displays active protections: Session Fixation Prevention, CSRF Protection, Security Headers, HttpOnly Cookies, Bell-LaPadula MAC, SSRF Protection, XXE Protection.

---

### 2.19 Library — Circulation

| Setting | Type | Default | Description |
|---------|------|---------|-------------|
| Loan Rules | Table | (per type) | Configurable rules per material type and patron type: loan days, renewal days, max renewals, fine per day, fine cap, grace period, loanable flag. |
| Default Loan Period | Days | 14 | Default when no specific rule applies. |
| Default Max Renewals | Number | 2 | Default renewal count. |
| Currency | Text | ZAR | Currency code for fines (3 characters). |
| Auto Fine | Toggle | (varies) | Automatically generate fine records for overdue items. |

---

### 2.20 FTP — File Transfer

| Setting | Type | Default | Description |
|---------|------|---------|-------------|
| Protocol | Select | SFTP | **SFTP** (recommended, encrypted) or **FTP** (unencrypted). |
| Host | Text | (empty) | Server hostname or IP address. |
| Port | Number | 22 | Port number. 22 for SFTP, 21 for FTP. Range: 1–65535. |
| Username | Text | (empty) | Login username. |
| Password | Password | (hidden) | Login password. Leave blank to keep current value. |
| Remote Path | Text | /uploads | Base path as seen by the FTP/SFTP user. |
| Server Disk Path | Text | (empty) | Actual filesystem path where uploaded files are stored. |
| Passive Mode | Toggle | On | Use passive mode for FTP connections. Always on for SFTP. |

---

## 3. Backup & Restore

**How to get there:** Admin > Backup & Restore

### 3.1 Dashboard

<div style="overflow-x:auto;margin:1rem 0"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 445 244" style="max-width:100%;height:auto;font-family:ui-monospace,Menlo,Consolas,monospace"><rect x="0.5" y="0.5" width="444" height="243" rx="8" fill="#f7faf9" stroke="#d8e6e3"/><line x1="13.6" y1="18.0" x2="17.2" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="18.0" x2="13.6" y2="26.0" stroke="#10373E" stroke-width="1.3"/><line x1="17.2" y1="18.0" x2="20.8" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="20.8" y1="18.0" x2="24.4" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="24.4" y1="18.0" x2="28.0" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="28.0" y1="18.0" x2="31.6" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="31.6" y1="18.0" x2="35.2" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="35.2" y1="18.0" x2="38.8" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="38.8" y1="18.0" x2="42.4" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="18.0" x2="46.0" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="46.0" y1="18.0" x2="49.6" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="49.6" y1="18.0" x2="53.2" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="53.2" y1="18.0" x2="56.8" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="56.8" y1="18.0" x2="60.4" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="60.4" y1="18.0" x2="64.0" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="64.0" y1="18.0" x2="67.6" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="67.6" y1="18.0" x2="71.2" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="18.0" x2="74.8" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="74.8" y1="18.0" x2="78.4" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="78.4" y1="18.0" x2="82.0" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="82.0" y1="18.0" x2="85.6" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="85.6" y1="18.0" x2="89.2" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="89.2" y1="18.0" x2="92.8" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="92.8" y1="18.0" x2="96.4" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="96.4" y1="18.0" x2="100.0" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="100.0" y1="18.0" x2="103.6" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="103.6" y1="18.0" x2="107.2" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="107.2" y1="18.0" x2="110.8" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="110.8" y1="18.0" x2="114.4" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="114.4" y1="18.0" x2="118.0" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="118.0" y1="18.0" x2="121.6" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="121.6" y1="18.0" x2="125.2" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="125.2" y1="18.0" x2="128.8" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="128.8" y1="18.0" x2="132.4" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="132.4" y1="18.0" x2="136.0" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="136.0" y1="18.0" x2="139.6" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="139.6" y1="18.0" x2="143.2" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="143.2" y1="18.0" x2="146.8" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="146.8" y1="18.0" x2="150.4" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="150.4" y1="18.0" x2="154.0" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="154.0" y1="18.0" x2="157.6" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="157.6" y1="18.0" x2="161.2" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="161.2" y1="18.0" x2="164.8" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="164.8" y1="18.0" x2="168.4" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="164.8" y1="18.0" x2="164.8" y2="26.0" stroke="#10373E" stroke-width="1.3"/><line x1="168.4" y1="18.0" x2="172.0" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="172.0" y1="18.0" x2="175.6" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="175.6" y1="18.0" x2="179.2" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="179.2" y1="18.0" x2="182.8" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="182.8" y1="18.0" x2="186.4" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="186.4" y1="18.0" x2="190.0" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="190.0" y1="18.0" x2="193.6" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="193.6" y1="18.0" x2="197.2" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="197.2" y1="18.0" x2="200.8" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="200.8" y1="18.0" x2="204.4" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="204.4" y1="18.0" x2="208.0" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="208.0" y1="18.0" x2="211.6" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="211.6" y1="18.0" x2="215.2" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="215.2" y1="18.0" x2="218.8" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="218.8" y1="18.0" x2="222.4" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="222.4" y1="18.0" x2="226.0" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="226.0" y1="18.0" x2="229.6" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="229.6" y1="18.0" x2="233.2" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="233.2" y1="18.0" x2="236.8" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="236.8" y1="18.0" x2="240.4" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="240.4" y1="18.0" x2="244.0" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="244.0" y1="18.0" x2="247.6" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="247.6" y1="18.0" x2="251.2" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="251.2" y1="18.0" x2="254.8" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="254.8" y1="18.0" x2="258.4" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="258.4" y1="18.0" x2="262.0" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="262.0" y1="18.0" x2="265.6" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="265.6" y1="18.0" x2="269.2" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="269.2" y1="18.0" x2="272.8" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="272.8" y1="18.0" x2="276.4" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="276.4" y1="18.0" x2="280.0" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="280.0" y1="18.0" x2="283.6" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="283.6" y1="18.0" x2="287.2" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="287.2" y1="18.0" x2="290.8" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="290.8" y1="18.0" x2="294.4" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="294.4" y1="18.0" x2="298.0" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="298.0" y1="18.0" x2="301.6" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="301.6" y1="18.0" x2="305.2" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="305.2" y1="18.0" x2="308.8" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="308.8" y1="18.0" x2="312.4" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="312.4" y1="18.0" x2="316.0" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="316.0" y1="18.0" x2="319.6" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="319.6" y1="18.0" x2="323.2" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="323.2" y1="18.0" x2="326.8" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="326.8" y1="18.0" x2="330.4" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="330.4" y1="18.0" x2="334.0" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="334.0" y1="18.0" x2="337.6" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="337.6" y1="18.0" x2="341.2" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="341.2" y1="18.0" x2="344.8" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="344.8" y1="18.0" x2="348.4" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="348.4" y1="18.0" x2="352.0" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="352.0" y1="18.0" x2="355.6" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="355.6" y1="18.0" x2="359.2" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="359.2" y1="18.0" x2="362.8" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="362.8" y1="18.0" x2="366.4" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="366.4" y1="18.0" x2="370.0" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="370.0" y1="18.0" x2="373.6" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="373.6" y1="18.0" x2="377.2" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="377.2" y1="18.0" x2="380.8" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="380.8" y1="18.0" x2="384.4" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="384.4" y1="18.0" x2="388.0" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="388.0" y1="18.0" x2="391.6" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="391.6" y1="18.0" x2="395.2" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="395.2" y1="18.0" x2="398.8" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="398.8" y1="18.0" x2="402.4" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="402.4" y1="18.0" x2="406.0" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="406.0" y1="18.0" x2="409.6" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="409.6" y1="18.0" x2="413.2" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="413.2" y1="18.0" x2="416.8" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="416.8" y1="18.0" x2="416.8" y2="26.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="26.0" x2="13.6" y2="34.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="34.0" x2="13.6" y2="42.0" stroke="#10373E" stroke-width="1.3"/><line x1="172.0" y1="26.0" x2="172.0" y2="34.0" stroke="#10373E" stroke-width="1.3"/><line x1="172.0" y1="34.0" x2="172.0" y2="42.0" stroke="#10373E" stroke-width="1.3"/><line x1="424.0" y1="26.0" x2="424.0" y2="34.0" stroke="#10373E" stroke-width="1.3"/><line x1="424.0" y1="34.0" x2="424.0" y2="42.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="42.0" x2="13.6" y2="50.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="50.0" x2="13.6" y2="58.0" stroke="#10373E" stroke-width="1.3"/><line x1="172.0" y1="42.0" x2="172.0" y2="50.0" stroke="#10373E" stroke-width="1.3"/><line x1="172.0" y1="50.0" x2="172.0" y2="58.0" stroke="#10373E" stroke-width="1.3"/><line x1="431.2" y1="42.0" x2="431.2" y2="50.0" stroke="#10373E" stroke-width="1.3"/><line x1="431.2" y1="50.0" x2="431.2" y2="58.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="58.0" x2="13.6" y2="66.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="66.0" x2="13.6" y2="74.0" stroke="#10373E" stroke-width="1.3"/><line x1="172.0" y1="58.0" x2="172.0" y2="66.0" stroke="#10373E" stroke-width="1.3"/><line x1="172.0" y1="66.0" x2="172.0" y2="74.0" stroke="#10373E" stroke-width="1.3"/><line x1="229.6" y1="58.0" x2="229.6" y2="74.0" stroke="#10373E" stroke-width="1.3"/><line x1="280.0" y1="58.0" x2="280.0" y2="74.0" stroke="#10373E" stroke-width="1.3"/><line x1="373.6" y1="58.0" x2="373.6" y2="74.0" stroke="#10373E" stroke-width="1.3"/><line x1="431.2" y1="58.0" x2="431.2" y2="66.0" stroke="#10373E" stroke-width="1.3"/><line x1="431.2" y1="66.0" x2="431.2" y2="74.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="74.0" x2="13.6" y2="82.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="82.0" x2="13.6" y2="90.0" stroke="#10373E" stroke-width="1.3"/><line x1="35.2" y1="82.0" x2="38.8" y2="82.0" stroke="#10373E" stroke-width="1.3"/><line x1="35.2" y1="74.0" x2="35.2" y2="82.0" stroke="#10373E" stroke-width="1.3"/><line x1="35.2" y1="82.0" x2="35.2" y2="90.0" stroke="#10373E" stroke-width="1.3"/><line x1="38.8" y1="82.0" x2="42.4" y2="82.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="82.0" x2="46.0" y2="82.0" stroke="#10373E" stroke-width="1.3"/><line x1="164.8" y1="74.0" x2="164.8" y2="82.0" stroke="#10373E" stroke-width="1.3"/><line x1="164.8" y1="82.0" x2="164.8" y2="90.0" stroke="#10373E" stroke-width="1.3"/><line x1="416.8" y1="74.0" x2="416.8" y2="82.0" stroke="#10373E" stroke-width="1.3"/><line x1="416.8" y1="82.0" x2="416.8" y2="90.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="90.0" x2="13.6" y2="98.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="98.0" x2="13.6" y2="106.0" stroke="#10373E" stroke-width="1.3"/><line x1="35.2" y1="98.0" x2="38.8" y2="98.0" stroke="#10373E" stroke-width="1.3"/><line x1="35.2" y1="90.0" x2="35.2" y2="98.0" stroke="#10373E" stroke-width="1.3"/><line x1="35.2" y1="98.0" x2="35.2" y2="106.0" stroke="#10373E" stroke-width="1.3"/><line x1="38.8" y1="98.0" x2="42.4" y2="98.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="98.0" x2="46.0" y2="98.0" stroke="#10373E" stroke-width="1.3"/><line x1="164.8" y1="90.0" x2="164.8" y2="98.0" stroke="#10373E" stroke-width="1.3"/><line x1="164.8" y1="98.0" x2="164.8" y2="106.0" stroke="#10373E" stroke-width="1.3"/><line x1="416.8" y1="90.0" x2="416.8" y2="98.0" stroke="#10373E" stroke-width="1.3"/><line x1="416.8" y1="98.0" x2="416.8" y2="106.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="106.0" x2="13.6" y2="114.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="114.0" x2="13.6" y2="122.0" stroke="#10373E" stroke-width="1.3"/><line x1="35.2" y1="114.0" x2="38.8" y2="114.0" stroke="#10373E" stroke-width="1.3"/><line x1="35.2" y1="106.0" x2="35.2" y2="114.0" stroke="#10373E" stroke-width="1.3"/><line x1="38.8" y1="114.0" x2="42.4" y2="114.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="114.0" x2="46.0" y2="114.0" stroke="#10373E" stroke-width="1.3"/><line x1="164.8" y1="106.0" x2="164.8" y2="114.0" stroke="#10373E" stroke-width="1.3"/><line x1="164.8" y1="114.0" x2="164.8" y2="122.0" stroke="#10373E" stroke-width="1.3"/><line x1="416.8" y1="106.0" x2="416.8" y2="114.0" stroke="#10373E" stroke-width="1.3"/><line x1="416.8" y1="114.0" x2="416.8" y2="122.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="122.0" x2="13.6" y2="130.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="130.0" x2="13.6" y2="138.0" stroke="#10373E" stroke-width="1.3"/><line x1="164.8" y1="122.0" x2="164.8" y2="130.0" stroke="#10373E" stroke-width="1.3"/><line x1="164.8" y1="130.0" x2="164.8" y2="138.0" stroke="#10373E" stroke-width="1.3"/><line x1="416.8" y1="122.0" x2="416.8" y2="130.0" stroke="#10373E" stroke-width="1.3"/><line x1="416.8" y1="130.0" x2="416.8" y2="138.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="138.0" x2="13.6" y2="146.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="146.0" x2="13.6" y2="154.0" stroke="#10373E" stroke-width="1.3"/><line x1="172.0" y1="138.0" x2="172.0" y2="146.0" stroke="#10373E" stroke-width="1.3"/><line x1="172.0" y1="146.0" x2="172.0" y2="154.0" stroke="#10373E" stroke-width="1.3"/><line x1="424.0" y1="138.0" x2="424.0" y2="146.0" stroke="#10373E" stroke-width="1.3"/><line x1="424.0" y1="146.0" x2="424.0" y2="154.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="154.0" x2="13.6" y2="162.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="162.0" x2="13.6" y2="170.0" stroke="#10373E" stroke-width="1.3"/><line x1="35.2" y1="162.0" x2="38.8" y2="162.0" stroke="#10373E" stroke-width="1.3"/><line x1="35.2" y1="154.0" x2="35.2" y2="162.0" stroke="#10373E" stroke-width="1.3"/><line x1="35.2" y1="162.0" x2="35.2" y2="170.0" stroke="#10373E" stroke-width="1.3"/><line x1="38.8" y1="162.0" x2="42.4" y2="162.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="162.0" x2="46.0" y2="162.0" stroke="#10373E" stroke-width="1.3"/><line x1="164.8" y1="154.0" x2="164.8" y2="162.0" stroke="#10373E" stroke-width="1.3"/><line x1="164.8" y1="162.0" x2="164.8" y2="170.0" stroke="#10373E" stroke-width="1.3"/><line x1="416.8" y1="154.0" x2="416.8" y2="162.0" stroke="#10373E" stroke-width="1.3"/><line x1="416.8" y1="162.0" x2="416.8" y2="170.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="170.0" x2="13.6" y2="178.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="178.0" x2="13.6" y2="186.0" stroke="#10373E" stroke-width="1.3"/><line x1="35.2" y1="178.0" x2="38.8" y2="178.0" stroke="#10373E" stroke-width="1.3"/><line x1="35.2" y1="170.0" x2="35.2" y2="178.0" stroke="#10373E" stroke-width="1.3"/><line x1="35.2" y1="178.0" x2="35.2" y2="186.0" stroke="#10373E" stroke-width="1.3"/><line x1="38.8" y1="178.0" x2="42.4" y2="178.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="178.0" x2="46.0" y2="178.0" stroke="#10373E" stroke-width="1.3"/><line x1="164.8" y1="170.0" x2="164.8" y2="178.0" stroke="#10373E" stroke-width="1.3"/><line x1="164.8" y1="178.0" x2="164.8" y2="186.0" stroke="#10373E" stroke-width="1.3"/><line x1="416.8" y1="170.0" x2="416.8" y2="178.0" stroke="#10373E" stroke-width="1.3"/><line x1="416.8" y1="178.0" x2="416.8" y2="186.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="186.0" x2="13.6" y2="194.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="194.0" x2="13.6" y2="202.0" stroke="#10373E" stroke-width="1.3"/><line x1="35.2" y1="194.0" x2="38.8" y2="194.0" stroke="#10373E" stroke-width="1.3"/><line x1="35.2" y1="186.0" x2="35.2" y2="194.0" stroke="#10373E" stroke-width="1.3"/><line x1="38.8" y1="194.0" x2="42.4" y2="194.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="194.0" x2="46.0" y2="194.0" stroke="#10373E" stroke-width="1.3"/><line x1="164.8" y1="186.0" x2="164.8" y2="194.0" stroke="#10373E" stroke-width="1.3"/><line x1="164.8" y1="194.0" x2="164.8" y2="202.0" stroke="#10373E" stroke-width="1.3"/><line x1="416.8" y1="186.0" x2="416.8" y2="194.0" stroke="#10373E" stroke-width="1.3"/><line x1="416.8" y1="194.0" x2="416.8" y2="202.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="202.0" x2="13.6" y2="210.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="210.0" x2="13.6" y2="218.0" stroke="#10373E" stroke-width="1.3"/><line x1="164.8" y1="202.0" x2="164.8" y2="210.0" stroke="#10373E" stroke-width="1.3"/><line x1="164.8" y1="210.0" x2="164.8" y2="218.0" stroke="#10373E" stroke-width="1.3"/><line x1="416.8" y1="202.0" x2="416.8" y2="210.0" stroke="#10373E" stroke-width="1.3"/><line x1="416.8" y1="210.0" x2="416.8" y2="218.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="226.0" x2="17.2" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="218.0" x2="13.6" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="17.2" y1="226.0" x2="20.8" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="20.8" y1="226.0" x2="24.4" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="24.4" y1="226.0" x2="28.0" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="28.0" y1="226.0" x2="31.6" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="31.6" y1="226.0" x2="35.2" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="35.2" y1="226.0" x2="38.8" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="38.8" y1="226.0" x2="42.4" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="226.0" x2="46.0" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="46.0" y1="226.0" x2="49.6" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="49.6" y1="226.0" x2="53.2" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="53.2" y1="226.0" x2="56.8" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="56.8" y1="226.0" x2="60.4" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="60.4" y1="226.0" x2="64.0" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="64.0" y1="226.0" x2="67.6" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="67.6" y1="226.0" x2="71.2" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="226.0" x2="74.8" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="74.8" y1="226.0" x2="78.4" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="78.4" y1="226.0" x2="82.0" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="82.0" y1="226.0" x2="85.6" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="85.6" y1="226.0" x2="89.2" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="89.2" y1="226.0" x2="92.8" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="92.8" y1="226.0" x2="96.4" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="96.4" y1="226.0" x2="100.0" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="100.0" y1="226.0" x2="103.6" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="103.6" y1="226.0" x2="107.2" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="107.2" y1="226.0" x2="110.8" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="110.8" y1="226.0" x2="114.4" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="114.4" y1="226.0" x2="118.0" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="118.0" y1="226.0" x2="121.6" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="121.6" y1="226.0" x2="125.2" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="125.2" y1="226.0" x2="128.8" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="128.8" y1="226.0" x2="132.4" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="132.4" y1="226.0" x2="136.0" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="136.0" y1="226.0" x2="139.6" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="139.6" y1="226.0" x2="143.2" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="143.2" y1="226.0" x2="146.8" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="146.8" y1="226.0" x2="150.4" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="150.4" y1="226.0" x2="154.0" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="154.0" y1="226.0" x2="157.6" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="157.6" y1="226.0" x2="161.2" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="161.2" y1="226.0" x2="164.8" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="164.8" y1="226.0" x2="168.4" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="164.8" y1="218.0" x2="164.8" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="168.4" y1="226.0" x2="172.0" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="172.0" y1="226.0" x2="175.6" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="175.6" y1="226.0" x2="179.2" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="179.2" y1="226.0" x2="182.8" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="182.8" y1="226.0" x2="186.4" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="186.4" y1="226.0" x2="190.0" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="190.0" y1="226.0" x2="193.6" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="193.6" y1="226.0" x2="197.2" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="197.2" y1="226.0" x2="200.8" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="200.8" y1="226.0" x2="204.4" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="204.4" y1="226.0" x2="208.0" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="208.0" y1="226.0" x2="211.6" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="211.6" y1="226.0" x2="215.2" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="215.2" y1="226.0" x2="218.8" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="218.8" y1="226.0" x2="222.4" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="222.4" y1="226.0" x2="226.0" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="226.0" y1="226.0" x2="229.6" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="229.6" y1="226.0" x2="233.2" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="233.2" y1="226.0" x2="236.8" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="236.8" y1="226.0" x2="240.4" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="240.4" y1="226.0" x2="244.0" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="244.0" y1="226.0" x2="247.6" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="247.6" y1="226.0" x2="251.2" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="251.2" y1="226.0" x2="254.8" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="254.8" y1="226.0" x2="258.4" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="258.4" y1="226.0" x2="262.0" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="262.0" y1="226.0" x2="265.6" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="265.6" y1="226.0" x2="269.2" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="269.2" y1="226.0" x2="272.8" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="272.8" y1="226.0" x2="276.4" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="276.4" y1="226.0" x2="280.0" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="280.0" y1="226.0" x2="283.6" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="283.6" y1="226.0" x2="287.2" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="287.2" y1="226.0" x2="290.8" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="290.8" y1="226.0" x2="294.4" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="294.4" y1="226.0" x2="298.0" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="298.0" y1="226.0" x2="301.6" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="301.6" y1="226.0" x2="305.2" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="305.2" y1="226.0" x2="308.8" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="308.8" y1="226.0" x2="312.4" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="312.4" y1="226.0" x2="316.0" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="316.0" y1="226.0" x2="319.6" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="319.6" y1="226.0" x2="323.2" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="323.2" y1="226.0" x2="326.8" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="326.8" y1="226.0" x2="330.4" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="330.4" y1="226.0" x2="334.0" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="334.0" y1="226.0" x2="337.6" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="337.6" y1="226.0" x2="341.2" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="341.2" y1="226.0" x2="344.8" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="344.8" y1="226.0" x2="348.4" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="348.4" y1="226.0" x2="352.0" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="352.0" y1="226.0" x2="355.6" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="355.6" y1="226.0" x2="359.2" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="359.2" y1="226.0" x2="362.8" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="362.8" y1="226.0" x2="366.4" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="366.4" y1="226.0" x2="370.0" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="370.0" y1="226.0" x2="373.6" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="373.6" y1="226.0" x2="377.2" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="377.2" y1="226.0" x2="380.8" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="380.8" y1="226.0" x2="384.4" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="384.4" y1="226.0" x2="388.0" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="388.0" y1="226.0" x2="391.6" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="391.6" y1="226.0" x2="395.2" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="395.2" y1="226.0" x2="398.8" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="398.8" y1="226.0" x2="402.4" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="402.4" y1="226.0" x2="406.0" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="406.0" y1="226.0" x2="409.6" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="409.6" y1="226.0" x2="413.2" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="413.2" y1="226.0" x2="416.8" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="416.8" y1="218.0" x2="416.8" y2="226.0" stroke="#10373E" stroke-width="1.3"/><text x="31.6" y="38.0" font-size="9.5" fill="#10373E">Database</text><text x="96.4" y="38.0" font-size="9.5" fill="#10373E">Info</text><text x="31.6" y="54.0" font-size="9.5" fill="#10373E">Storage</text><text x="89.2" y="54.0" font-size="9.5" fill="#10373E">Info</text><text x="190.0" y="54.0" font-size="9.5" fill="#10373E">BACKUP</text><text x="240.4" y="54.0" font-size="9.5" fill="#10373E">HISTORY</text><text x="298.0" y="54.0" font-size="9.5" fill="#10373E">TABLE</text><text x="31.6" y="70.0" font-size="9.5" fill="#10373E">Quick</text><text x="74.8" y="70.0" font-size="9.5" fill="#10373E">Actions</text><text x="190.0" y="70.0" font-size="9.5" fill="#10373E">Date</text><text x="240.4" y="70.0" font-size="9.5" fill="#10373E">Type</text><text x="290.8" y="70.0" font-size="9.5" fill="#10373E">Components</text><text x="384.4" y="70.0" font-size="9.5" fill="#10373E">Size</text><text x="53.2" y="86.0" font-size="9.5" fill="#10373E">DB</text><text x="74.8" y="86.0" font-size="9.5" fill="#10373E">Only</text><text x="182.8" y="86.0" font-size="9.5" fill="#10373E">[Restore]</text><text x="254.8" y="86.0" font-size="9.5" fill="#10373E">[Download]</text><text x="334.0" y="86.0" font-size="9.5" fill="#10373E">[Delete]</text><text x="53.2" y="102.0" font-size="9.5" fill="#10373E">Full</text><text x="89.2" y="102.0" font-size="9.5" fill="#10373E">Backup</text><text x="53.2" y="118.0" font-size="9.5" fill="#10373E">Incremental</text><text x="31.6" y="150.0" font-size="9.5" fill="#10373E">Schedules</text><text x="53.2" y="166.0" font-size="9.5" fill="#10373E">[</text><text x="67.6" y="166.0" font-size="9.5" fill="#10373E">]</text><text x="82.0" y="166.0" font-size="9.5" fill="#10373E">Add</text><text x="53.2" y="182.0" font-size="9.5" fill="#10373E">Daily</text><text x="96.4" y="182.0" font-size="9.5" fill="#10373E">DB</text><text x="118.0" y="182.0" font-size="9.5" fill="#10373E">✓</text><text x="53.2" y="198.0" font-size="9.5" fill="#10373E">Weekly</text><text x="103.6" y="198.0" font-size="9.5" fill="#10373E">Full</text><text x="139.6" y="198.0" font-size="9.5" fill="#10373E">✓</text><text x="31.6" y="214.0" font-size="9.5" fill="#10373E">Cron:</text><text x="74.8" y="214.0" font-size="9.5" fill="#10373E">0</text><text x="89.2" y="214.0" font-size="9.5" fill="#10373E">*</text><text x="103.6" y="214.0" font-size="9.5" fill="#10373E">*</text><text x="118.0" y="214.0" font-size="9.5" fill="#10373E">*</text><text x="132.4" y="214.0" font-size="9.5" fill="#10373E">*</text></svg></div>

### 3.2 Creating Backups

**Manual:** Click "Create Backup" and select components (database, uploads, plugins, framework).

**Quick Actions:**
- **Database Only** — fast, database only
- **Full Backup** — all components
- **Incremental** — only changes since last full backup

### 3.3 Scheduled Backups

Click **+** in the Schedules card:

| Field | Description |
|-------|-------------|
| Name | Descriptive label (e.g., "Daily DB Backup") |
| Frequency | Hourly, Daily, Weekly, Monthly |
| Time | When to run (24-hour, e.g., 02:00) |
| Day of Week | For weekly (Sunday–Saturday) |
| Day of Month | For monthly (1–28) |
| Retention | Days to keep old backups |
| Components | Database, Uploads, Plugins, Framework checkboxes |

**Required cron entry:**
```
0 * * * * cd /usr/share/nginx/archive && php symfony backup:run-scheduled >> /var/log/atom/backup-cron.log 2>&1
```

**Recommended strategy:**

| Schedule | Frequency | Components | Retention |
|----------|-----------|-----------|-----------|
| Daily DB | Daily 02:00 | Database only | 30 days |
| Weekly Full | Weekly Sunday 03:00 | All | 90 days |
| Monthly Archive | Monthly 1st 04:00 | All | 365 days |

### 3.4 Restoring

1. Click **Restore** on any backup in the history table
2. Select which components to restore
3. Confirm — system backs up current state first, then restores

### 3.5 Upload Restore

1. Click **Upload Backup**
2. Upload a `.tar.gz`, `.sql.gz`, or `.zip` file
3. System validates and detects components
4. Select what to restore and confirm

### 3.6 Settings

**Admin > Backup & Restore > Settings:**

| Setting | Default | Description |
|---------|---------|-------------|
| Backup Path | /var/backups/atom | Where backups are stored |
| Log Path | /var/log/atom/backup.log | Backup log file |
| Max Backups | 30 | Maximum backups to keep |
| Retention Days | 90 | Delete backups older than this |
| Notification Email | (empty) | Email for success/failure alerts |
| Notify on Success | Off | Email on successful backup |
| Notify on Failure | On | Email on failed backup |

### 3.7 CLI

```bash
php symfony backup:run-scheduled              # Run due schedules
php symfony backup:run-scheduled --dry-run    # Preview what would run
php symfony backup:run-scheduled --force      # Run all active schedules now
```

---

## 4. User Management

**How to get there:** Admin > Users & Groups

### 4.1 Users

- Create, edit, deactivate user accounts
- Assign to groups (editor, contributor, administrator, etc.)
- Set security clearance level (for classified records)
- View login history and audit trail

### 4.2 Groups & ACL

- Define permission groups with granular ACL rules
- Control access per module, per action, per repository
- Inherit permissions from parent groups

---

## 5. Security

### 5.1 Security Classification

Bell-LaPadula mandatory access control:

<div style="overflow-x:auto;margin:1rem 0"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 373 164" style="max-width:100%;height:auto;font-family:ui-monospace,Menlo,Consolas,monospace"><rect x="0.5" y="0.5" width="372" height="163" rx="8" fill="#f7faf9" stroke="#d8e6e3"/><line x1="89.2" y1="18.0" x2="92.8" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="92.8" y1="18.0" x2="96.4" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="96.4" y1="18.0" x2="100.0" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="100.0" y1="18.0" x2="103.6" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="103.6" y1="18.0" x2="107.2" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="107.2" y1="18.0" x2="110.8" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="110.8" y1="18.0" x2="114.4" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="114.4" y1="18.0" x2="118.0" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="118.0" y1="18.0" x2="121.6" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="121.6" y1="18.0" x2="125.2" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="125.2" y1="18.0" x2="128.8" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="128.8" y1="18.0" x2="132.4" y2="18.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="26.0" x2="42.4" y2="34.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="34.0" x2="42.4" y2="42.0" stroke="#10373E" stroke-width="1.3"/><line x1="74.8" y1="50.0" x2="78.4" y2="50.0" stroke="#10373E" stroke-width="1.3"/><line x1="78.4" y1="50.0" x2="82.0" y2="50.0" stroke="#10373E" stroke-width="1.3"/><line x1="82.0" y1="50.0" x2="85.6" y2="50.0" stroke="#10373E" stroke-width="1.3"/><line x1="85.6" y1="50.0" x2="89.2" y2="50.0" stroke="#10373E" stroke-width="1.3"/><line x1="89.2" y1="50.0" x2="92.8" y2="50.0" stroke="#10373E" stroke-width="1.3"/><line x1="92.8" y1="50.0" x2="96.4" y2="50.0" stroke="#10373E" stroke-width="1.3"/><line x1="96.4" y1="50.0" x2="100.0" y2="50.0" stroke="#10373E" stroke-width="1.3"/><line x1="100.0" y1="50.0" x2="103.6" y2="50.0" stroke="#10373E" stroke-width="1.3"/><line x1="103.6" y1="50.0" x2="107.2" y2="50.0" stroke="#10373E" stroke-width="1.3"/><line x1="107.2" y1="50.0" x2="110.8" y2="50.0" stroke="#10373E" stroke-width="1.3"/><line x1="110.8" y1="50.0" x2="114.4" y2="50.0" stroke="#10373E" stroke-width="1.3"/><line x1="114.4" y1="50.0" x2="118.0" y2="50.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="58.0" x2="42.4" y2="66.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="66.0" x2="42.4" y2="74.0" stroke="#10373E" stroke-width="1.3"/><line x1="103.6" y1="82.0" x2="107.2" y2="82.0" stroke="#10373E" stroke-width="1.3"/><line x1="107.2" y1="82.0" x2="110.8" y2="82.0" stroke="#10373E" stroke-width="1.3"/><line x1="110.8" y1="82.0" x2="114.4" y2="82.0" stroke="#10373E" stroke-width="1.3"/><line x1="114.4" y1="82.0" x2="118.0" y2="82.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="90.0" x2="42.4" y2="98.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="98.0" x2="42.4" y2="106.0" stroke="#10373E" stroke-width="1.3"/><line x1="96.4" y1="114.0" x2="100.0" y2="114.0" stroke="#10373E" stroke-width="1.3"/><line x1="100.0" y1="114.0" x2="103.6" y2="114.0" stroke="#10373E" stroke-width="1.3"/><line x1="103.6" y1="114.0" x2="107.2" y2="114.0" stroke="#10373E" stroke-width="1.3"/><line x1="107.2" y1="114.0" x2="110.8" y2="114.0" stroke="#10373E" stroke-width="1.3"/><line x1="110.8" y1="114.0" x2="114.4" y2="114.0" stroke="#10373E" stroke-width="1.3"/><line x1="114.4" y1="114.0" x2="118.0" y2="114.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="122.0" x2="42.4" y2="130.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="130.0" x2="42.4" y2="138.0" stroke="#10373E" stroke-width="1.3"/><line x1="103.6" y1="146.0" x2="107.2" y2="146.0" stroke="#10373E" stroke-width="1.3"/><line x1="107.2" y1="146.0" x2="110.8" y2="146.0" stroke="#10373E" stroke-width="1.3"/><line x1="110.8" y1="146.0" x2="114.4" y2="146.0" stroke="#10373E" stroke-width="1.3"/><line x1="114.4" y1="146.0" x2="118.0" y2="146.0" stroke="#10373E" stroke-width="1.3"/><text x="10.0" y="22.0" font-size="9.5" fill="#10373E">Top</text><text x="38.8" y="22.0" font-size="9.5" fill="#10373E">Secret</text><text x="139.6" y="22.0" font-size="9.5" fill="#10373E">Only</text><text x="175.6" y="22.0" font-size="9.5" fill="#10373E">Top</text><text x="204.4" y="22.0" font-size="9.5" fill="#10373E">Secret</text><text x="254.8" y="22.0" font-size="9.5" fill="#10373E">clearance</text><text x="326.8" y="22.0" font-size="9.5" fill="#10373E">users</text><text x="24.4" y="54.0" font-size="9.5" fill="#10373E">Secret</text><text x="125.2" y="54.0" font-size="9.5" fill="#10373E">Secret</text><text x="175.6" y="54.0" font-size="9.5" fill="#10373E">or</text><text x="197.2" y="54.0" font-size="9.5" fill="#10373E">higher</text><text x="10.0" y="86.0" font-size="9.5" fill="#10373E">Confidential</text><text x="125.2" y="86.0" font-size="9.5" fill="#10373E">Confidential</text><text x="218.8" y="86.0" font-size="9.5" fill="#10373E">or</text><text x="240.4" y="86.0" font-size="9.5" fill="#10373E">higher</text><text x="17.2" y="118.0" font-size="9.5" fill="#10373E">Restricted</text><text x="125.2" y="118.0" font-size="9.5" fill="#10373E">Restricted</text><text x="204.4" y="118.0" font-size="9.5" fill="#10373E">or</text><text x="226.0" y="118.0" font-size="9.5" fill="#10373E">higher</text><text x="10.0" y="150.0" font-size="9.5" fill="#10373E">Unclassified</text><text x="125.2" y="150.0" font-size="9.5" fill="#10373E">Everyone</text></svg></div>

Assign classification to records and clearance to users. The system enforces "no read up, no write down."

### 5.2 Audit Trail

Every create, update, delete operation is logged with:
- Who (user)
- What (entity type, entity ID)
- When (timestamp)
- What changed (field-level diff)

**View:** Admin > Audit Trail

### 5.3 Error Log

**View:** Admin > AHG Settings > Error Log

Application errors logged in `ahg_error_log` table. Resolve errors to clear the log.

---

## 6. Queue Management

**How to get there:** Admin > Queue

Monitor and manage background jobs:

| Column | Description |
|--------|-------------|
| Job ID | Unique identifier |
| Type | Job type (ingest, export, AI, etc.) |
| Status | pending, running, completed, failed |
| Progress | Percentage or step indicator |
| Created | When the job was queued |
| Started | When processing began |
| Duration | Elapsed time |

**Actions:** Retry failed jobs, cancel pending jobs, view error details.

**CLI:**
```bash
php bin/atom queue:work              # Start processing
php bin/atom queue:status            # Show queue status
php bin/atom queue:retry --id=123    # Retry a failed job
php bin/atom queue:failed            # List failed jobs
php bin/atom queue:cleanup           # Remove old completed jobs
```

---

## 7. Reports & Statistics

### 7.1 Reports Dashboard

Pre-built reports on collections, users, compliance status.

### 7.2 Report Builder

Enterprise report builder with:
- Rich text editor (Quill.js)
- SQL query data sources
- Sections and templates
- Export to Word, PDF, XLSX, CSV
- Scheduling and sharing

### 7.3 Statistics

Usage statistics dashboard with:
- Record counts by type, level, repository
- User activity trends
- Digital object statistics
- Search query analytics

---

## 8. Infrastructure

### 8.1 Cache Management

```bash
# Clear all caches
rm -rf /usr/share/nginx/archive/cache/*
php symfony cc
sudo systemctl restart php8.3-fpm
```

### 8.2 Search Index

```bash
# Rebuild Elasticsearch index
php symfony search:populate

# Check index status
php symfony search:status
```

### 8.3 Plugin Management

```bash
php bin/atom extension:discover      # Find new plugins
php bin/atom extension:enable <name> # Enable a plugin
php bin/atom extension:disable <name># Disable a plugin
php bin/atom extension:list          # List all plugins
```

### 8.4 Services

```bash
sudo systemctl restart php8.3-fpm     # PHP
sudo systemctl restart cantaloupe      # IIIF image server
sudo systemctl restart elasticsearch   # Search
```

---

*AtoM Heratio Framework v2.8.2 — The Archive and Heritage Group (Pty) Ltd*
