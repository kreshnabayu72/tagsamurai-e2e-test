---
id: TC-GS-ACTLOG-E2E-014-tab-session-populate-opsi-filter-dari-data-log
title: "Tab Session: Sumber opsi dropdown filter terpopulasi dari data log aktual dan penanganan stale reference"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ACTLOG-50
  - TC-GS-ACTLOG-51
  - TC-GS-ACTLOG-52
  - TC-GS-ACTLOG-53
  - TC-GS-ACTLOG-54
  - TC-GS-ACTLOG-56
  - TC-GS-ACTLOG-57
  - TC-GS-ACTLOG-58
coverage:
  web: automated
---

# Tab Session: Sumber opsi dropdown filter terpopulasi dari data log aktual dan penanganan stale reference

## Prerequisites

- Login sebagai Role: Total Control pada Tab Session dengan subset data log aktif

## Test Steps

1. Buka Filter Panel pada Tab Session
2. Buka dropdown User saat opsi sedang di-fetch dan verifikasi indikator skeleton/loading tampil di dropdown
3. Amati daftar opsi dropdown User dan verifikasi opsi hanya memuat user yang genuinely pernah tercatat di log entitas ini
4. Buka dropdown Position dan verifikasi opsi hanya memuat Position yang ada di entri log (posisi lain di master data yang belum pernah login tidak muncul)
5. Buka dropdown Division dan verifikasi hal yang sama berlaku untuk Division
6. Buka dropdown Activity saat log hanya berisi Login, Logout, dan Session
7. Verifikasi dropdown Activity hanya memuat ketiga opsi tersebut dan opsi yang belum pernah muncul di log tidak tampil
8. Buka dropdown Status saat log hanya memuat Success
9. Verifikasi opsi Failed tidak muncul di dropdown Status
10. Terapkan filter User untuk "Budi Santoso", simulasikan akun tersebut dihapus di modul User
11. Verifikasi filter tetap berjalan sebagai snapshot dan entri lama milik "Budi Santoso" tetap tampil

## Notes

- Prinsip populate-scope universal: dropdown filter hanya memuat nilai yang benar-benar ada di riwayat data log.
