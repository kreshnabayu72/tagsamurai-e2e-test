---
id: TC-GS-USER-E2E-015-role-matrix-negatif-proteksi-default-user-dan-self
title: "Role Matrix Negatif: Proteksi terhadap baris Default User dan akun sendiri (Self-Protection)"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-GS-USER-50
  - TC-GS-USER-51
  - TC-GS-USER-56
  - TC-GS-USER-57
  - TC-GS-USER-1029
  - TC-GS-USER-1030
coverage:
  web: automated
---

# Role Matrix Negatif: Proteksi terhadap baris Default User dan akun sendiri (Self-Protection)

## Prerequisites

- Login sebagai Total Control atau Full CRUD
- Baris Default User dan baris login user sendiri terlihat di tabel

## Test Steps

### Proteksi Baris Default User

1. Buka Global Settings > User > User List
2. Temukan baris Default User (Hendra Gunawan)
3. Hover checkbox dan toggle Active, verifikasi keduanya disabled dengan tooltip proteksi Default User
4. Buka menu (⋯), verifikasi opsi Delete disabled dengan tooltip proteksi Default User

### Proteksi Baris Akun Sendiri

5. Temukan baris user aktor yang sedang login
6. Hover toggle Active, verifikasi toggle disabled dengan tooltip proteksi akun sendiri (tidak dapat menonaktifkan akun sendiri)
7. Buka menu (⋯), verifikasi opsi Delete disabled dengan tooltip akun sendiri
8. Verifikasi aksi Resend Email dan Pair TAG pada akun sendiri dibatasi sesuai aturan kanonikal

## Notes

- Menggabungkan 6 test case granular (TC-GS-USER-50 s.d. TC-GS-USER-1030).
