---
id: TC-GS-USER-E2E-066-cross-module-sync-master-data-position-dan-division
title: "Cross-Module Sync: Refleksi perubahan master data Position dan Division ke dropdown User"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-944
  - TC-GS-USER-945
  - TC-GS-USER-946
  - TC-GS-USER-947
  - TC-GS-USER-948
  - TC-GS-USER-949
coverage:
  web: automated
---

# Cross-Module Sync: Refleksi perubahan master data Position dan Division ke dropdown User

## Prerequisites

- Berada di modul Global Settings > Position dan Division

## Test Steps

### Sinkronisasi Master Data

1. Buat Position baru 'Procurement Officer' di tab Position
2. Buka tab User List > modal '[+ User]', verifikasi 'Procurement Officer' muncul di opsi dropdown Position
3. Rename Position di tab Position, verifikasi sel Position pada user terkait di User List terupdate
4. Hapus Position yang tidak dipakai, verifikasi hilang dari dropdown modal User
5. Lakukan pengujian yang sama untuk entitas Division

## Notes

- Menggabungkan 6 test case granular (TC-GS-USER-944 s.d. TC-GS-USER-949).
