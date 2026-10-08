---
id: TC-GS-USER-E2E-010-role-matrix-read-only-ui-restrictions
title: "Role Matrix: Pembatasan kontrol UI halaman User List untuk aktor Read Only"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-GS-USER-47
  - TC-GS-USER-48
  - TC-GS-USER-66
coverage:
  web: automated
---

# Role Matrix: Pembatasan kontrol UI halaman User List untuk aktor Read Only

## Prerequisites

- Login sebagai Role: Read Only
- Dataset Pre-setup tersedia di User List

## Test Steps

### Pembatasan Tombol dan Toggle

1. Buka Global Settings > User > User List
2. Hover tombol '[+ User]', verifikasi tombol disabled dengan tooltip permission
3. Hover switch toggle Active pada setiap baris user, verifikasi toggle disabled dengan tooltip permission
4. Centang baris tabel, verifikasi Bulk Action Bar tidak muncul / disabled untuk Read Only

## Notes

- Menggabungkan 3 test case granular (TC-GS-USER-47 s.d. TC-GS-USER-66).
