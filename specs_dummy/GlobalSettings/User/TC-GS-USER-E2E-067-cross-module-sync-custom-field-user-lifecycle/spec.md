---
id: TC-GS-USER-E2E-067-cross-module-sync-custom-field-user-lifecycle
title: "Cross-Module Sync: Siklus hidup Custom Field User (Create, Deactivate, Delete) ke form dan Detail"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-950
  - TC-GS-USER-951
  - TC-GS-USER-952
  - TC-GS-USER-953
  - TC-GS-USER-954
  - TC-GS-USER-955
coverage:
  web: automated
---

# Cross-Module Sync: Siklus hidup Custom Field User (Create, Deactivate, Delete) ke form dan Detail

## Prerequisites

- Berada di tab Custom Field User

## Test Steps

### Sinkronisasi Custom Fields

1. Buat Custom Field baru di tab Custom Field
2. Buka modal Create User, verifikasi field baru langsung muncul
3. Deaktivasi custom field, verifikasi field tersembunyi dari form dan Detail
4. Hapus custom field permanen, verifikasi field dan nilainya hilang dari sistem

## Notes

- Menggabungkan 6 test case granular (TC-GS-USER-950 s.d. TC-GS-USER-955).
