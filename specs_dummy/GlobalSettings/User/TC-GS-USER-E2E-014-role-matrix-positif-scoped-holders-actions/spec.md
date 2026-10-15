---
id: TC-GS-USER-E2E-014-role-matrix-positif-scoped-holders-actions
title: "Role Matrix Positif: Scoped capability holders (Create-Only, Update-Only, Delete-Only)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-63
  - TC-GS-USER-64
  - TC-GS-USER-65
  - TC-GS-USER-67
  - TC-GS-USER-72
  - TC-GS-USER-73
  - TC-GS-USER-85
  - TC-GS-USER-86
  - TC-GS-USER-87
coverage:
  web: automated
---

# Role Matrix Positif: Scoped capability holders (Create-Only, Update-Only, Delete-Only)

## Prerequisites

- Akun Lestari Ayu (Create-Only), Bayu Saputra (Update-Only), Citra Melati (Delete-Only) tersedia

## Test Steps

### Create-Only Holder

1. Login sebagai Create-Only, verifikasi tombol '[+ User]' enabled dan submit form berhasil
2. Verifikasi opsi Edit dan Delete disabled/hidden pada baris tabel

### Update-Only Holder

3. Login sebagai Update-Only, verifikasi tombol '[+ User]' disabled/hidden
4. Verifikasi opsi Edit dan Toggle Active enabled pada baris user yang berhak diubah

### Delete-Only Holder

5. Login sebagai Delete-Only, verifikasi tombol '[+ User]' dan Edit disabled/hidden
6. Verifikasi opsi Delete enabled pada baris user yang berhak dihapus

## Notes

- Menggabungkan 9 test case granular (TC-GS-USER-63 s.d. TC-GS-USER-87).
