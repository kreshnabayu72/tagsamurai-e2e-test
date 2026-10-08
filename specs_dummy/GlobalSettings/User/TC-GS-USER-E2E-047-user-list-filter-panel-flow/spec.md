---
id: TC-GS-USER-E2E-047-user-list-filter-panel-flow
title: "User List: Filter panel multi-select, rentang tanggal, apply, dan clear filter"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-423
  - TC-GS-USER-424
  - TC-GS-USER-425
  - TC-GS-USER-426
  - TC-GS-USER-427
  - TC-GS-USER-428
  - TC-GS-USER-429
  - TC-GS-USER-430
  - TC-GS-USER-431
  - TC-GS-USER-432
  - TC-GS-USER-433
  - TC-GS-USER-434
coverage:
  web: automated
---

# User List: Filter panel multi-select, rentang tanggal, apply, dan clear filter

## Prerequisites

- Berada di Global Settings > User > User List

## Test Steps

### Filter Panel Interaksi

1. Klik ikon Filter di toolbar, verifikasi panel filter terbuka
2. Pilih filter Status 'Active', Division 'Finance', dan rentang tanggal Last Update
3. Klik tombol '[Apply]'
4. Verifikasi tabel tersaring sesuai kriteria dan badge indikator filter aktif muncul
5. Buka kembali filter panel, klik tombol '[Clear All]', verifikasi seluruh filter ter-reset

## Notes

- Menggabungkan 12 test case granular (TC-GS-USER-423 s.d. TC-GS-USER-434).
