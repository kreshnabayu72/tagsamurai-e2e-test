---
id: TC-GS-USER-E2E-073-multi-konteks-konkurensi-dua-admin-dan-limit
title: "Multi-Konteks: Konkurensi dua admin toggle user bersamaan dan batas Master Data Limit"
priority: Medium
caseType: Edge
status: draft
sourceTc:
  - TC-GS-USER-985
  - TC-GS-USER-986
  - TC-GS-USER-987
coverage:
  web: automated
---

# Multi-Konteks: Konkurensi dua admin toggle user bersamaan dan batas Master Data Limit

## Prerequisites

- Dua sesi browser admin terbuka bersamaan

## Test Steps

### Konkurensi Dua Admin

1. Admin A menonaktifkan Dewi Lestari
2. Admin B (tanpa refresh) mencoba mengubah toggle Dewi Lestari
3. Verifikasi dialog 'Data has changed' muncul meminta refresh
4. Simulasikan pembuatan user pada slot limit terakhir secara bersamaan, verifikasi salah satu request ditolak dialog Limit Reached

## Notes

- Menggabungkan 3 test case granular (TC-GS-USER-985 s.d. TC-GS-USER-987).
