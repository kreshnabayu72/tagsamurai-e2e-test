---
id: TC-GS-USER-E2E-068-cross-module-sync-produk-fams-dan-admin-console
title: "Cross-Module Sync: Integrasi user ke Fixed Asset, Admin Console, My Profile, dan File Manager"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-958
  - TC-GS-USER-959
  - TC-GS-USER-960
  - TC-GS-USER-961
  - TC-GS-USER-962
  - TC-GS-USER-963
  - TC-GS-USER-964
coverage:
  web: automated
---

# Cross-Module Sync: Integrasi user ke Fixed Asset, Admin Console, My Profile, dan File Manager

## Prerequisites

- Akses multi-modul (Fixed Asset, Admin Console, File Manager) aktif

## Test Steps

### Sinkronisasi Lintas Modul

1. Deaktivasi user di User List, verifikasi user hilang dari pilihan peminjam/approver di Fixed Asset
2. Buat user dengan Access Fixed Asset, verifikasi user muncul di Fixed Asset > Settings > User
3. Ubah foto profil di User Detail, verifikasi foto terupdate di File Manager

## Notes

- Menggabungkan 7 test case granular (TC-GS-USER-958 s.d. TC-GS-USER-964).
