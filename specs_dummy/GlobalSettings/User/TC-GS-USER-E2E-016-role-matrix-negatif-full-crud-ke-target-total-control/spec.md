---
id: TC-GS-USER-E2E-016-role-matrix-negatif-full-crud-ke-target-total-control
title: "Role Matrix Negatif: Capability holder Full CRUD dilarang mengubah target Total Control"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-GS-USER-58
  - TC-GS-USER-979
coverage:
  web: automated
---

# Role Matrix Negatif: Capability holder Full CRUD dilarang mengubah target Total Control

## Prerequisites

- Login sebagai Fajar Nugroho (Manage user and role Full CRUD)
- Target Andi Wijaya (Total Control) ada di User List

## Test Steps

### Proteksi Target Total Control terhadap Holder Biasa

1. Buka Global Settings > User > User List
2. Temukan baris Andi Wijaya (Total Control)
3. Hover opsi Edit, toggle Active, dan Delete di baris Andi Wijaya
4. Verifikasi kontrol tersebut disabled dengan tooltip proteksi tier
5. Kirim request edit langsung via API tampering, verifikasi respons 403 Forbidden

## Notes

- Menggabungkan 2 test case granular (TC-GS-USER-58 s.d. TC-GS-USER-979).
