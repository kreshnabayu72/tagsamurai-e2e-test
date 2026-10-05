---
id: TC-GS-ACTLOG-E2E-020-tab-session-setup-column-visibilitas-kolom-dan-persistensi-f5
title: "Tab Session: Pengaturan visibilitas kolom hideable pada Setup Column dan persistensi refresh F5"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ACTLOG-88
  - TC-GS-ACTLOG-90
  - TC-GS-ACTLOG-91
  - TC-GS-ACTLOG-92
  - TC-GS-ACTLOG-93
  - TC-GS-ACTLOG-94
  - TC-GS-ACTLOG-95
  - TC-GS-ACTLOG-96
  - TC-GS-ACTLOG-97
coverage:
  web: automated
---

# Tab Session: Pengaturan visibilitas kolom hideable pada Setup Column dan persistensi refresh F5

## Prerequisites

- Login sebagai Role: Total Control pada Tab Session di modal Setup Column

## Test Steps

1. Buka modal Setup Column pada Tab Session
2. Uncheck kolom Date, Employee ID, Position, Division, Activity, Status, Note, IP Address, dan Device/Browser secara bergantian
3. Verifikasi area Live Preview langsung menyembunyikan kolom yang di-uncheck
4. Klik tombol `[Save]`
5. Verifikasi tabel utama Tab Session menyembunyikan kolom-kolom yang di-uncheck
6. Lakukan refresh halaman browser (F5)
7. Verifikasi konfigurasi kolom yang tersembunyi tetap bertahan (persist) setelah refresh

## Notes

- Konfigurasi Setup Column disimpan di browser storage pengguna dan terisolasi per tab.
