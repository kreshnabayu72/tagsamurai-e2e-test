---
id: TC-GS-USER-E2E-012-role-matrix-positif-full-crud-holder-actions
title: "Role Matrix Positif: Capability holder Full CRUD mengelola user Normal dan sesama holder"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-54
  - TC-GS-USER-55
  - TC-GS-USER-59
coverage:
  web: automated
---

# Role Matrix Positif: Capability holder Full CRUD mengelola user Normal dan sesama holder

## Prerequisites

- Login sebagai Fajar Nugroho (Manage user and role Full CRUD)
- Target Normal dan target sesama holder tersedia

## Test Steps

### Aksi Pengelolaan oleh Full CRUD Holder

1. Buka Global Settings > User > User List
2. Verifikasi tombol '[+ User]' tampil enabled dan modal Create User dapat dibuka
3. Pada baris user Normal dan sesama holder, verifikasi opsi Edit, Toggle Active, dan Delete dapat diakses

## Notes

- Menggabungkan 3 test case granular (TC-GS-USER-54 s.d. TC-GS-USER-59).
