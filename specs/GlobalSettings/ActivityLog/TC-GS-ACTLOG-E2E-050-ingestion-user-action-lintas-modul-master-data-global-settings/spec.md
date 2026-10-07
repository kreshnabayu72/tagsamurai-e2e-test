---
id: TC-GS-ACTLOG-E2E-050-ingestion-user-action-lintas-modul-master-data-global-settings
title: "Ingestion User Action dari Mutasi Master Data 9 Modul Global Settings, Hardware, dan TAG Registry"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ACTLOG-199
  - TC-GS-ACTLOG-200
  - TC-GS-ACTLOG-201
  - TC-GS-ACTLOG-202
  - TC-GS-ACTLOG-203
  - TC-GS-ACTLOG-204
  - TC-GS-ACTLOG-205
  - TC-GS-ACTLOG-206
  - TC-GS-ACTLOG-207
  - TC-GS-ACTLOG-208
coverage:
  web: automated
---

# Ingestion User Action dari Mutasi Master Data 9 Modul Global Settings, Hardware, dan TAG Registry

## Prerequisites

- Login sebagai Role: Total Control Global Settings
- Terdapat aksi mutasi yang dieksekusi oleh admin 'Hendra Pratama' pada modul-modul Global Settings

## Test Steps

### Ingestion Modul Inti GS
1. Buka Tab User Action di Global Settings > Activity Log.
2. Cari entri mutasi dari masing-masing modul berikut:
   a. Modul User (Create User 'John Doe') -> Object: 'User'
   b. Modul Role & Permission (Assign role) -> Object: 'Role & Permission'
   c. Modul General Settings (Edit Timezone) -> Object: 'General Settings'
   d. Modul Brand (Create Brand 'Acme Corp') -> Object: 'Brand'
   e. Modul Measurement (Create Unit 'Pieces') -> Object: 'Measurement'
   f. Modul Position (Create Position 'Warehouse Staff') -> Object: 'Position'
   g. Modul Division (Create Division 'Finance') -> Object: 'Division'
   h. Modul Non-Login User (Create NLU 'Budi Kurniawan') -> Object: 'Non-Login User'
### Ingestion Hardware & TAG Registry
3. Cari entri aktivasi gateway pada modul Hardware:
   - Verifikasi Object: 'Hardware' / 'BLE Gateway', Action: 'Activate'.
4. Cari entri audit tag pada modul TAG Registry:
   - Verifikasi Object: 'TAG Registry' / 'All TAGs', Action: 'Audit'.
5. Verifikasi pada setiap baris: Date akurat, Old/New Value memuat diff perubahan, dan Modified By menampilkan 'Hendra P'.

## Notes

- Seluruh modul operasional di bawah Global Settings menyalurkan event mutasi ke audit trail secara konsisten.
