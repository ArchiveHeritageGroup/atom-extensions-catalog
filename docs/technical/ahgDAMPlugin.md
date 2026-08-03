# ahgDAMPlugin - Technical Documentation

> **Version:** 1.3.14
> **Last Updated:** 2026-01-20
> **Category:** Sector-Specific
> **Dependencies:** ahgThemeB5Plugin (required)

---

## Overview

The ahgDAMPlugin provides Digital Asset Management functionality for born-digital and digitized materials including photographs, videos, audio files, documents, and 3D models. It includes specialized metadata fields for film/video heritage materials.

---

## Database Schema

### Core Tables

#### dam_iptc_metadata
Stores IPTC and technical metadata for digital assets.

```sql
CREATE TABLE dam_iptc_metadata (
    id BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    object_id INT NOT NULL UNIQUE,

    -- IPTC Core
    headline VARCHAR(255),
    description TEXT,
    keywords TEXT,
    creator VARCHAR(255),
    credit_line VARCHAR(255),

    -- Location
    city VARCHAR(100),
    province_state VARCHAR(100),
    country VARCHAR(100),
    country_code CHAR(3),
    gps_latitude DECIMAL(10, 8),
    gps_longitude DECIMAL(11, 8),
    gps_altitude DECIMAL(10, 2),

    -- Production (Film/Video)
    duration_minutes INT UNSIGNED,
    production_country VARCHAR(100),
    production_country_code CHAR(3),

    -- Rights
    copyright_notice TEXT,
    rights_usage_terms TEXT,
    license_type VARCHAR(50),
    license_url VARCHAR(500),
    license_expiry DATE,

    -- Technical
    asset_type VARCHAR(50),
    file_format VARCHAR(50),
    mime_type VARCHAR(100),
    file_size BIGINT UNSIGNED,

    -- Timestamps
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,

    INDEX idx_dam_iptc_object (object_id),
    INDEX idx_dam_iptc_asset_type (asset_type)
);
```

#### dam_version_links
Tracks alternative language versions, formats, restorations, and edits.

```sql
CREATE TABLE dam_version_links (
    id BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    object_id INT NOT NULL,
    related_object_id INT NULL,
    version_type ENUM('language', 'format', 'restoration',
                      'directors_cut', 'censored', 'other') NOT NULL DEFAULT 'language',
    title VARCHAR(255) NOT NULL,
    language_code CHAR(3) NULL,
    language_name VARCHAR(50) NULL,
    year VARCHAR(10) NULL,
    notes TEXT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,

    INDEX idx_dam_version_object (object_id),
    INDEX idx_dam_version_related (related_object_id),
    INDEX idx_dam_version_type (version_type)
);
```

#### dam_format_holdings
Documents physical formats held at institutions.

```sql
CREATE TABLE dam_format_holdings (
    id BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    object_id INT NOT NULL,
    format_type ENUM(
        '35mm', '16mm', '8mm', 'Super8',
        'VHS', 'Betacam', 'U-matic', 'DV',
        'DVD', 'Blu-ray', 'LaserDisc',
        'Digital_File', 'DCP', 'ProRes',
        'Nitrate', 'Safety', 'Polyester',
        'Audio_Reel', 'Audio_Cassette', 'Vinyl', 'CD',
        'Other'
    ) NOT NULL,
    format_details VARCHAR(255) NULL,
    holding_institution VARCHAR(255) NOT NULL,
    holding_location VARCHAR(255) NULL,
    accession_number VARCHAR(100) NULL,
    condition_status ENUM('excellent', 'good', 'fair',
                          'poor', 'deteriorating', 'unknown') DEFAULT 'unknown',
    access_status ENUM('available', 'restricted', 'preservation_only',
                       'digitized_available', 'on_request',
                       'staff_only', 'unknown') DEFAULT 'unknown',
    access_url VARCHAR(500) NULL,
    access_notes TEXT NULL,
    is_primary TINYINT(1) DEFAULT 0,
    verified_date DATE NULL,
    notes TEXT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,

    INDEX idx_dam_holdings_object (object_id),
    INDEX idx_dam_holdings_institution (holding_institution),
    INDEX idx_dam_holdings_format (format_type),
    INDEX idx_dam_holdings_access (access_status)
);
```

#### dam_external_links
Stores links to ESAT, IMDb, Wikipedia, and other external databases.

```sql
CREATE TABLE dam_external_links (
    id BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    object_id INT NOT NULL,
    link_type ENUM(
        'ESAT', 'IMDb', 'SAFILM', 'NFVSA',
        'Wikipedia', 'Wikidata', 'VIAF',
        'YouTube', 'Vimeo', 'Archive_org',
        'BFI', 'AFI', 'Letterboxd', 'MUBI',
        'Filmography', 'Review', 'Academic', 'Press',
        'Other'
    ) NOT NULL,
    url VARCHAR(500) NOT NULL,
    title VARCHAR(255) NULL,
    description TEXT NULL,
    person_name VARCHAR(255) NULL,
    person_role VARCHAR(100) NULL,
    verified_date DATE NULL,
    is_primary TINYINT(1) DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,

    INDEX idx_dam_links_object (object_id),
    INDEX idx_dam_links_type (link_type),
    INDEX idx_dam_links_person (person_name)
);
```

---

## Module Structure

<div style="overflow-x:auto;margin:1rem 0"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 430 388" style="max-width:100%;height:auto;font-family:ui-monospace,Menlo,Consolas,monospace"><rect x="0.5" y="0.5" width="429" height="387" rx="8" fill="#f7faf9" stroke="#d8e6e3"/><line x1="13.6" y1="34.0" x2="17.2" y2="34.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="26.0" x2="13.6" y2="34.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="34.0" x2="13.6" y2="42.0" stroke="#10373E" stroke-width="1.3"/><line x1="17.2" y1="34.0" x2="20.8" y2="34.0" stroke="#10373E" stroke-width="1.3"/><line x1="20.8" y1="34.0" x2="24.4" y2="34.0" stroke="#10373E" stroke-width="1.3"/><line x1="24.4" y1="34.0" x2="28.0" y2="34.0" stroke="#10373E" stroke-width="1.3"/><line x1="28.0" y1="34.0" x2="31.6" y2="34.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="42.0" x2="13.6" y2="50.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="50.0" x2="13.6" y2="58.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="50.0" x2="46.0" y2="50.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="42.0" x2="42.4" y2="50.0" stroke="#10373E" stroke-width="1.3"/><line x1="46.0" y1="50.0" x2="49.6" y2="50.0" stroke="#10373E" stroke-width="1.3"/><line x1="49.6" y1="50.0" x2="53.2" y2="50.0" stroke="#10373E" stroke-width="1.3"/><line x1="53.2" y1="50.0" x2="56.8" y2="50.0" stroke="#10373E" stroke-width="1.3"/><line x1="56.8" y1="50.0" x2="60.4" y2="50.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="66.0" x2="17.2" y2="66.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="58.0" x2="13.6" y2="66.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="66.0" x2="13.6" y2="74.0" stroke="#10373E" stroke-width="1.3"/><line x1="17.2" y1="66.0" x2="20.8" y2="66.0" stroke="#10373E" stroke-width="1.3"/><line x1="20.8" y1="66.0" x2="24.4" y2="66.0" stroke="#10373E" stroke-width="1.3"/><line x1="24.4" y1="66.0" x2="28.0" y2="66.0" stroke="#10373E" stroke-width="1.3"/><line x1="28.0" y1="66.0" x2="31.6" y2="66.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="74.0" x2="13.6" y2="82.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="82.0" x2="13.6" y2="90.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="82.0" x2="46.0" y2="82.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="74.0" x2="42.4" y2="82.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="82.0" x2="42.4" y2="90.0" stroke="#10373E" stroke-width="1.3"/><line x1="46.0" y1="82.0" x2="49.6" y2="82.0" stroke="#10373E" stroke-width="1.3"/><line x1="49.6" y1="82.0" x2="53.2" y2="82.0" stroke="#10373E" stroke-width="1.3"/><line x1="53.2" y1="82.0" x2="56.8" y2="82.0" stroke="#10373E" stroke-width="1.3"/><line x1="56.8" y1="82.0" x2="60.4" y2="82.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="90.0" x2="13.6" y2="98.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="98.0" x2="13.6" y2="106.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="98.0" x2="46.0" y2="98.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="90.0" x2="42.4" y2="98.0" stroke="#10373E" stroke-width="1.3"/><line x1="46.0" y1="98.0" x2="49.6" y2="98.0" stroke="#10373E" stroke-width="1.3"/><line x1="49.6" y1="98.0" x2="53.2" y2="98.0" stroke="#10373E" stroke-width="1.3"/><line x1="53.2" y1="98.0" x2="56.8" y2="98.0" stroke="#10373E" stroke-width="1.3"/><line x1="56.8" y1="98.0" x2="60.4" y2="98.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="106.0" x2="13.6" y2="114.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="114.0" x2="13.6" y2="122.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="114.0" x2="74.8" y2="114.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="106.0" x2="71.2" y2="114.0" stroke="#10373E" stroke-width="1.3"/><line x1="74.8" y1="114.0" x2="78.4" y2="114.0" stroke="#10373E" stroke-width="1.3"/><line x1="78.4" y1="114.0" x2="82.0" y2="114.0" stroke="#10373E" stroke-width="1.3"/><line x1="82.0" y1="114.0" x2="85.6" y2="114.0" stroke="#10373E" stroke-width="1.3"/><line x1="85.6" y1="114.0" x2="89.2" y2="114.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="130.0" x2="17.2" y2="130.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="122.0" x2="13.6" y2="130.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="130.0" x2="13.6" y2="138.0" stroke="#10373E" stroke-width="1.3"/><line x1="17.2" y1="130.0" x2="20.8" y2="130.0" stroke="#10373E" stroke-width="1.3"/><line x1="20.8" y1="130.0" x2="24.4" y2="130.0" stroke="#10373E" stroke-width="1.3"/><line x1="24.4" y1="130.0" x2="28.0" y2="130.0" stroke="#10373E" stroke-width="1.3"/><line x1="28.0" y1="130.0" x2="31.6" y2="130.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="138.0" x2="13.6" y2="146.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="146.0" x2="13.6" y2="154.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="146.0" x2="46.0" y2="146.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="138.0" x2="42.4" y2="146.0" stroke="#10373E" stroke-width="1.3"/><line x1="46.0" y1="146.0" x2="49.6" y2="146.0" stroke="#10373E" stroke-width="1.3"/><line x1="49.6" y1="146.0" x2="53.2" y2="146.0" stroke="#10373E" stroke-width="1.3"/><line x1="53.2" y1="146.0" x2="56.8" y2="146.0" stroke="#10373E" stroke-width="1.3"/><line x1="56.8" y1="146.0" x2="60.4" y2="146.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="154.0" x2="13.6" y2="162.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="162.0" x2="13.6" y2="170.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="162.0" x2="74.8" y2="162.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="154.0" x2="71.2" y2="162.0" stroke="#10373E" stroke-width="1.3"/><line x1="74.8" y1="162.0" x2="78.4" y2="162.0" stroke="#10373E" stroke-width="1.3"/><line x1="78.4" y1="162.0" x2="82.0" y2="162.0" stroke="#10373E" stroke-width="1.3"/><line x1="82.0" y1="162.0" x2="85.6" y2="162.0" stroke="#10373E" stroke-width="1.3"/><line x1="85.6" y1="162.0" x2="89.2" y2="162.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="178.0" x2="17.2" y2="178.0" stroke="#10373E" stroke-width="1.3"/><line x1="13.6" y1="170.0" x2="13.6" y2="178.0" stroke="#10373E" stroke-width="1.3"/><line x1="17.2" y1="178.0" x2="20.8" y2="178.0" stroke="#10373E" stroke-width="1.3"/><line x1="20.8" y1="178.0" x2="24.4" y2="178.0" stroke="#10373E" stroke-width="1.3"/><line x1="24.4" y1="178.0" x2="28.0" y2="178.0" stroke="#10373E" stroke-width="1.3"/><line x1="28.0" y1="178.0" x2="31.6" y2="178.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="194.0" x2="46.0" y2="194.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="186.0" x2="42.4" y2="194.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="194.0" x2="42.4" y2="202.0" stroke="#10373E" stroke-width="1.3"/><line x1="46.0" y1="194.0" x2="49.6" y2="194.0" stroke="#10373E" stroke-width="1.3"/><line x1="49.6" y1="194.0" x2="53.2" y2="194.0" stroke="#10373E" stroke-width="1.3"/><line x1="53.2" y1="194.0" x2="56.8" y2="194.0" stroke="#10373E" stroke-width="1.3"/><line x1="56.8" y1="194.0" x2="60.4" y2="194.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="202.0" x2="42.4" y2="210.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="210.0" x2="42.4" y2="218.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="210.0" x2="74.8" y2="210.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="202.0" x2="71.2" y2="210.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="210.0" x2="71.2" y2="218.0" stroke="#10373E" stroke-width="1.3"/><line x1="74.8" y1="210.0" x2="78.4" y2="210.0" stroke="#10373E" stroke-width="1.3"/><line x1="78.4" y1="210.0" x2="82.0" y2="210.0" stroke="#10373E" stroke-width="1.3"/><line x1="82.0" y1="210.0" x2="85.6" y2="210.0" stroke="#10373E" stroke-width="1.3"/><line x1="85.6" y1="210.0" x2="89.2" y2="210.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="218.0" x2="42.4" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="226.0" x2="42.4" y2="234.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="218.0" x2="71.2" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="226.0" x2="71.2" y2="234.0" stroke="#10373E" stroke-width="1.3"/><line x1="100.0" y1="226.0" x2="103.6" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="100.0" y1="218.0" x2="100.0" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="100.0" y1="226.0" x2="100.0" y2="234.0" stroke="#10373E" stroke-width="1.3"/><line x1="103.6" y1="226.0" x2="107.2" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="107.2" y1="226.0" x2="110.8" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="110.8" y1="226.0" x2="114.4" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="114.4" y1="226.0" x2="118.0" y2="226.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="234.0" x2="42.4" y2="242.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="242.0" x2="42.4" y2="250.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="234.0" x2="71.2" y2="242.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="242.0" x2="71.2" y2="250.0" stroke="#10373E" stroke-width="1.3"/><line x1="100.0" y1="242.0" x2="103.6" y2="242.0" stroke="#10373E" stroke-width="1.3"/><line x1="100.0" y1="234.0" x2="100.0" y2="242.0" stroke="#10373E" stroke-width="1.3"/><line x1="103.6" y1="242.0" x2="107.2" y2="242.0" stroke="#10373E" stroke-width="1.3"/><line x1="107.2" y1="242.0" x2="110.8" y2="242.0" stroke="#10373E" stroke-width="1.3"/><line x1="110.8" y1="242.0" x2="114.4" y2="242.0" stroke="#10373E" stroke-width="1.3"/><line x1="114.4" y1="242.0" x2="118.0" y2="242.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="250.0" x2="42.4" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="258.0" x2="42.4" y2="266.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="258.0" x2="74.8" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="250.0" x2="71.2" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="74.8" y1="258.0" x2="78.4" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="78.4" y1="258.0" x2="82.0" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="82.0" y1="258.0" x2="85.6" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="85.6" y1="258.0" x2="89.2" y2="258.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="266.0" x2="42.4" y2="274.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="274.0" x2="42.4" y2="282.0" stroke="#10373E" stroke-width="1.3"/><line x1="100.0" y1="274.0" x2="103.6" y2="274.0" stroke="#10373E" stroke-width="1.3"/><line x1="100.0" y1="266.0" x2="100.0" y2="274.0" stroke="#10373E" stroke-width="1.3"/><line x1="100.0" y1="274.0" x2="100.0" y2="282.0" stroke="#10373E" stroke-width="1.3"/><line x1="103.6" y1="274.0" x2="107.2" y2="274.0" stroke="#10373E" stroke-width="1.3"/><line x1="107.2" y1="274.0" x2="110.8" y2="274.0" stroke="#10373E" stroke-width="1.3"/><line x1="110.8" y1="274.0" x2="114.4" y2="274.0" stroke="#10373E" stroke-width="1.3"/><line x1="114.4" y1="274.0" x2="118.0" y2="274.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="282.0" x2="42.4" y2="290.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="290.0" x2="42.4" y2="298.0" stroke="#10373E" stroke-width="1.3"/><line x1="100.0" y1="290.0" x2="103.6" y2="290.0" stroke="#10373E" stroke-width="1.3"/><line x1="100.0" y1="282.0" x2="100.0" y2="290.0" stroke="#10373E" stroke-width="1.3"/><line x1="103.6" y1="290.0" x2="107.2" y2="290.0" stroke="#10373E" stroke-width="1.3"/><line x1="107.2" y1="290.0" x2="110.8" y2="290.0" stroke="#10373E" stroke-width="1.3"/><line x1="110.8" y1="290.0" x2="114.4" y2="290.0" stroke="#10373E" stroke-width="1.3"/><line x1="114.4" y1="290.0" x2="118.0" y2="290.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="306.0" x2="46.0" y2="306.0" stroke="#10373E" stroke-width="1.3"/><line x1="42.4" y1="298.0" x2="42.4" y2="306.0" stroke="#10373E" stroke-width="1.3"/><line x1="46.0" y1="306.0" x2="49.6" y2="306.0" stroke="#10373E" stroke-width="1.3"/><line x1="49.6" y1="306.0" x2="53.2" y2="306.0" stroke="#10373E" stroke-width="1.3"/><line x1="53.2" y1="306.0" x2="56.8" y2="306.0" stroke="#10373E" stroke-width="1.3"/><line x1="56.8" y1="306.0" x2="60.4" y2="306.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="322.0" x2="74.8" y2="322.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="314.0" x2="71.2" y2="322.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="322.0" x2="71.2" y2="330.0" stroke="#10373E" stroke-width="1.3"/><line x1="74.8" y1="322.0" x2="78.4" y2="322.0" stroke="#10373E" stroke-width="1.3"/><line x1="78.4" y1="322.0" x2="82.0" y2="322.0" stroke="#10373E" stroke-width="1.3"/><line x1="82.0" y1="322.0" x2="85.6" y2="322.0" stroke="#10373E" stroke-width="1.3"/><line x1="85.6" y1="322.0" x2="89.2" y2="322.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="330.0" x2="71.2" y2="338.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="338.0" x2="71.2" y2="346.0" stroke="#10373E" stroke-width="1.3"/><line x1="100.0" y1="338.0" x2="103.6" y2="338.0" stroke="#10373E" stroke-width="1.3"/><line x1="100.0" y1="330.0" x2="100.0" y2="338.0" stroke="#10373E" stroke-width="1.3"/><line x1="103.6" y1="338.0" x2="107.2" y2="338.0" stroke="#10373E" stroke-width="1.3"/><line x1="107.2" y1="338.0" x2="110.8" y2="338.0" stroke="#10373E" stroke-width="1.3"/><line x1="110.8" y1="338.0" x2="114.4" y2="338.0" stroke="#10373E" stroke-width="1.3"/><line x1="114.4" y1="338.0" x2="118.0" y2="338.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="354.0" x2="74.8" y2="354.0" stroke="#10373E" stroke-width="1.3"/><line x1="71.2" y1="346.0" x2="71.2" y2="354.0" stroke="#10373E" stroke-width="1.3"/><line x1="74.8" y1="354.0" x2="78.4" y2="354.0" stroke="#10373E" stroke-width="1.3"/><line x1="78.4" y1="354.0" x2="82.0" y2="354.0" stroke="#10373E" stroke-width="1.3"/><line x1="82.0" y1="354.0" x2="85.6" y2="354.0" stroke="#10373E" stroke-width="1.3"/><line x1="85.6" y1="354.0" x2="89.2" y2="354.0" stroke="#10373E" stroke-width="1.3"/><line x1="100.0" y1="370.0" x2="103.6" y2="370.0" stroke="#10373E" stroke-width="1.3"/><line x1="100.0" y1="362.0" x2="100.0" y2="370.0" stroke="#10373E" stroke-width="1.3"/><line x1="103.6" y1="370.0" x2="107.2" y2="370.0" stroke="#10373E" stroke-width="1.3"/><line x1="107.2" y1="370.0" x2="110.8" y2="370.0" stroke="#10373E" stroke-width="1.3"/><line x1="110.8" y1="370.0" x2="114.4" y2="370.0" stroke="#10373E" stroke-width="1.3"/><line x1="114.4" y1="370.0" x2="118.0" y2="370.0" stroke="#10373E" stroke-width="1.3"/><text x="10.0" y="22.0" font-size="9.5" fill="#10373E">ahgDAMPlugin/</text><text x="38.8" y="38.0" font-size="9.5" fill="#10373E">config/</text><text x="67.6" y="54.0" font-size="9.5" fill="#10373E">ahgDAMPluginConfiguration.class.php</text><text x="38.8" y="70.0" font-size="9.5" fill="#10373E">data/</text><text x="67.6" y="86.0" font-size="9.5" fill="#10373E">install.sql</text><text x="67.6" y="102.0" font-size="9.5" fill="#10373E">migrations/</text><text x="96.4" y="118.0" font-size="9.5" fill="#10373E">2026_01_20_dam_film_metadata.sql</text><text x="38.8" y="134.0" font-size="9.5" fill="#10373E">lib/</text><text x="67.6" y="150.0" font-size="9.5" fill="#10373E">model/</text><text x="96.4" y="166.0" font-size="9.5" fill="#10373E">DamIptcMetadata.class.php</text><text x="38.8" y="182.0" font-size="9.5" fill="#10373E">modules/</text><text x="67.6" y="198.0" font-size="9.5" fill="#10373E">ahgDAMPlugin/</text><text x="240.4" y="198.0" font-size="9.5" fill="#10373E">#</text><text x="254.8" y="198.0" font-size="9.5" fill="#10373E">Sector</text><text x="305.2" y="198.0" font-size="9.5" fill="#10373E">view/edit</text><text x="377.2" y="198.0" font-size="9.5" fill="#10373E">module</text><text x="96.4" y="214.0" font-size="9.5" fill="#10373E">actions/</text><text x="125.2" y="230.0" font-size="9.5" fill="#10373E">indexAction.class.php</text><text x="125.2" y="246.0" font-size="9.5" fill="#10373E">editAction.class.php</text><text x="96.4" y="262.0" font-size="9.5" fill="#10373E">templates/</text><text x="125.2" y="278.0" font-size="9.5" fill="#10373E">indexSuccess.php</text><text x="125.2" y="294.0" font-size="9.5" fill="#10373E">editSuccess.php</text><text x="67.6" y="310.0" font-size="9.5" fill="#10373E">ahgDam/</text><text x="247.6" y="310.0" font-size="9.5" fill="#10373E">#</text><text x="262.0" y="310.0" font-size="9.5" fill="#10373E">Dashboard</text><text x="334.0" y="310.0" font-size="9.5" fill="#10373E">and</text><text x="362.8" y="310.0" font-size="9.5" fill="#10373E">admin</text><text x="96.4" y="326.0" font-size="9.5" fill="#10373E">actions/</text><text x="125.2" y="342.0" font-size="9.5" fill="#10373E">actions.class.php</text><text x="96.4" y="358.0" font-size="9.5" fill="#10373E">templates/</text><text x="125.2" y="374.0" font-size="9.5" fill="#10373E">dashboardSuccess.php</text></svg></div>

---

## Key Classes

### editAction.class.php

Main edit action for DAM assets. Handles:

- Core AtoM fields (title, dates, creators, subjects)
- IPTC metadata
- Version links (saveVersionLinks)
- Format holdings (saveFormatHoldings)
- External links (saveExternalLinks)
- Location data (saveItemLocation)

**Key Methods:**

```php
protected function saveIptcMetadataDirectly()
// Saves IPTC fields including duration_minutes, production_country

protected function saveVersionLinks()
// Saves to dam_version_links table

protected function saveFormatHoldings()
// Saves to dam_format_holdings table with all fields:
// format_type, format_details, holding_institution, holding_location,
// accession_number, condition_status, access_status, access_url,
// access_notes, verified_date, is_primary, notes

protected function saveExternalLinks()
// Saves to dam_external_links table with all fields:
// link_type, url, title, description, person_name, person_role,
// verified_date, is_primary
```

---

## Routes

| Route | Module | Action | Description |
|-------|--------|--------|-------------|
| `/dam/:slug` | ahgDAMPlugin | index | View DAM asset |
| `/dam/:slug/edit` | ahgDAMPlugin | edit | Edit DAM asset |
| `/dam/dashboard` | ahgDam | dashboard | DAM dashboard |
| `/dam/browse` | ahgDam | browse | Browse DAM assets |

---

## Template Variables

### indexSuccess.php (View)

| Variable | Type | Description |
|----------|------|-------------|
| `$resource` | QubitInformationObject | The AtoM resource |
| `$rawResource` | stdClass | Raw database record |
| `$iptc` | stdClass | IPTC metadata record |
| `$versionLinks` | Collection | Alternative versions |
| `$formatHoldings` | Collection | Format holdings |
| `$externalLinks` | Collection | External links |

### editSuccess.php (Edit)

Same variables plus:

| Variable | Type | Description |
|----------|------|-------------|
| `$form` | sfForm | Symfony form object |

---

## Asset Types

Supported asset type values:

| Value | Label |
|-------|-------|
| `photograph` | Photograph |
| `film` | Film |
| `video` | Video |
| `documentary` | Documentary |
| `audio` | Audio Recording |
| `podcast` | Podcast |
| `speech` | Speech/Lecture |
| `document` | Document |
| `manuscript` | Manuscript |
| `artwork` | Artwork |
| `map` | Map |
| `model_3d` | 3D Model |
| `dataset` | Dataset |
| `software` | Software |
| `website` | Website |

---

## Integration Points

### Loan Plugin Integration

The DAM module integrates with ahgLoanPlugin if enabled:

```php
<?php if (in_array('ahgLoanPlugin', sfProjectConfiguration::getActive()->getPlugins())): ?>
  <a href="<?php echo url_for(['module' => 'loan', 'action' => 'add',
      'type' => 'out', 'sector' => 'dam', 'object_id' => $rawResource->id]); ?>">
    New Loan
  </a>
<?php endif; ?>
```

### Preservation Plugin Integration

Compatible with ahgPreservationPlugin for:
- Checksum verification
- Format identification (PRONOM)
- SIP/AIP/DIP workflows

### Cart Plugin Integration

Integrates with ahgCartPlugin for ordering copies.

---

## Form Field Names

### IPTC Fields (Single Values)
- `duration_minutes`
- `production_country`
- `production_country_code`

### Version Links (Arrays)
- `version_id[]`
- `version_title[]`
- `version_type[]`
- `version_language[]`
- `version_language_code[]`
- `version_year[]`
- `version_notes[]`

### Format Holdings (Arrays)
- `holding_id[]`
- `holding_format[]`
- `holding_format_details[]`
- `holding_institution[]`
- `holding_location[]`
- `holding_accession[]`
- `holding_condition[]`
- `holding_access[]`
- `holding_url[]`
- `holding_access_notes[]`
- `holding_verified[]`
- `holding_primary[]`
- `holding_notes[]`

### External Links (Arrays)
- `link_id[]`
- `link_type[]`
- `link_url[]`
- `link_title[]`
- `link_description[]`
- `link_person[]`
- `link_role[]`
- `link_verified[]`
- `link_primary[]`

---

## CLI Commands

```bash
# Import DAM assets from CSV
php symfony dam:import /path/to/file.csv

# Export DAM metadata
php symfony dam:export --format=csv

# Regenerate thumbnails
php symfony dam:regenerate-derivatives
```

---

## Changelog

### v1.3.14 (2026-01-20)
- Added film/video metadata fields:
  - Running time (duration_minutes)
  - Production country
  - Alternative versions (dam_version_links)
  - Format holdings (dam_format_holdings)
  - External links (dam_external_links)
- Fixed "New License" to "New Loan" terminology
- Updated user guide with film metadata documentation

### v1.3.13
- Initial stable release
- IPTC metadata support
- GPS coordinates
- Asset type classification

---

*Part of the AtoM AHG Framework*
