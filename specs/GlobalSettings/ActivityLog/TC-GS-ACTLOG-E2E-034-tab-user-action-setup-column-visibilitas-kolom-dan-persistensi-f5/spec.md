---
id: TC-GS-ACTLOG-E2E-034-tab-user-action-setup-column-visibilitas-kolom-dan-persistensi-f5
title: "Tab User Action: Pengaturan visibilitas kolom hideable pada Setup Column dan persistensi refresh F5"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ACTLOG-171
  - TC-GS-ACTLOG-173
  - TC-GS-ACTLOG-174
  - TC-GS-ACTLOG-175
  - TC-GS-ACTLOG-176
  - TC-GS-ACTLOG-177
  - TC-GS-ACTLOG-178
coverage:
  web: automated
---

# Tab User Action: Pengaturan visibilitas kolom hideable pada Setup Column dan persistensi refresh F5

## Prerequisites

- Login sebagai Role: Total Control pada Tab User Action di modal Setup Column

## Test Steps

1. Buka modal Setup Column pada Tab User Action
2. Uncheck kolom Date, Object, Name, Field, Old Value, New Value, dan Modified By secara bergantian
3. Verifikasi area Live Preview langsung menyembunyikan kolom yang di-uncheck
4. Klik tombol `[Save]`
5. Verifikasi tabel utama Tab User Action menyembunyikan kolom-kolom yang di-uncheck
6. Lakukan refresh halaman browser (F5)
7. Verifikasi konfigurasi kolom yang tersembunyi tetap bertahan (persist) setelah refresh

## Notes

- Visibilitas kolom Tab User Action terisolasi dan tidak mempengaruhi Tab Session.
