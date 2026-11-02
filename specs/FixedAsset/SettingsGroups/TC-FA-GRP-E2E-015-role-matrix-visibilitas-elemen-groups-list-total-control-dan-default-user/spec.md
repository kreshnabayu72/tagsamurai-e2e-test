---
id: TC-FA-GRP-E2E-015-role-matrix-visibilitas-elemen-groups-list-total-control-dan-default-user
title: "Role Matrix: Visibilitas Elemen Groups List per Role (Total Control dan Default User)"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-GRP-44
  - TC-FA-GRP-45
coverage:
  web: automated
---

# Role Matrix: Visibilitas Elemen Groups List per Role (Total Control dan Default User)

## Prerequisites

- Mode: FE+BE.
- Role yang diuji:

| Role | Akun (Pre-setup) | Password | Blok langkah |
|---|---|---|---|
| Total Control | No 1 `totalControlGroups_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_TC_PASSWORD` | langkah 1 sampai 12 |
| Default User | No 2 `defaultUserGroups_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_DU_PASSWORD` | langkah 13 sampai 27 |

- Login di hook `before` spec ini sebagai Total Control; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Flag Guided Tooltip `fa-settings-groups` disetel `seen` oleh hook suite untuk akun Total Control (lihat `suite.md`); untuk akun Default User flag disetel `seen` di hook `before` spec ini dan dipulihkan di hook `after` (kemampuan disediakan tim FE/BE).
- Data Pre-setup (hanya dibaca, tidak diubah): pohon group baku Tabel A (Pre-setup No 9) dengan Warehouse A, Warehouse B, Head Office, Global HQ, dan Region East. Spec ini tidak menjalankan Delete.
- Kemampuan teknis: fixture BE dan sesi API aktor, disediakan tim FE/BE (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`); spec ini tidak mengubah state global.

## Test Steps

### Role Total Control (TC-FA-GRP-44)

1. Verifikasi menu Settings > Groups tampil pada navigasi, kolom Checkbox tampil, dan tombol [+] Group tampil
2. Klik (⋯) pada baris Warehouse A
3. Verifikasi menu baris memuat Detail, Add Subgroup, Edit, Delete
4. Tutup menu dengan Esc
5. Klik (⋯) pada node Warehouse A di sidebar
6. Verifikasi menu sidebar memuat Detail, Add Subgroup, Edit, Delete
7. Tutup menu dengan Esc
8. Centang baris Warehouse A
9. Verifikasi Bulk Action Bar memuat Delete sehingga Bulk Delete tersedia
10. Hapus centang baris Warehouse A dengan Unselect All
11. Verifikasi sidebar menampilkan seluruh tree client (Head Office, Warehouse A, Warehouse B, Global HQ, dan Region East)
12. Verifikasi Search, Filter, Download, Changelog, sort, pagination, dan Column Visibility tampil dan aktif

### Role Default User (TC-FA-GRP-45)

13. Logout dari akun Total Control
14. Login sebagai Default User dengan `Spectra.env.FA_DU_PASSWORD`
15. Buka Fixed Asset > Settings > Groups
16. Verifikasi menu Settings > Groups tampil pada navigasi, kolom Checkbox tampil, dan tombol [+] Group tampil
17. Klik (⋯) pada baris Warehouse A
18. Verifikasi menu baris memuat Detail, Add Subgroup, Edit, Delete
19. Tutup menu dengan Esc
20. Klik (⋯) pada node Warehouse A di sidebar
21. Verifikasi menu sidebar memuat Detail, Add Subgroup, Edit, Delete
22. Tutup menu dengan Esc
23. Centang baris Warehouse A
24. Verifikasi Bulk Action Bar memuat Delete sehingga Bulk Delete tersedia
25. Hapus centang baris Warehouse A dengan Unselect All
26. Verifikasi sidebar menampilkan seluruh tree client (Head Office, Warehouse A, Warehouse B, Global HQ, dan Region East)
27. Verifikasi Search, Filter, Download, Changelog, sort, pagination, dan Column Visibility tampil dan aktif

## Notes

- Spec ditulis per blok role karena ganti akun memerlukan langkah eksplisit (akun pertama login di hook `before`); langkah tiap blok identik (bagian 3a).
- Langkah penghubung (S-03): langkah 4, 7, 19, 22 (menutup menu), langkah 10 dan 25 (Unselect All, S-09), langkah 13 sampai 15 (ganti akun dan membuka layar, karena hook `beforeEach` hanya berlaku untuk akun aktor pertama). Hook `after` memulihkan sesi ke akun default suite (S-07).
- Pembagian TC lintas spec: Role Read Only (TC-FA-GRP-46 dan 78) ada di spec 278. Role Group Manager dan Manage Group (TC-FA-GRP-47 sampai 52) ada di spec 016.
- Temuan untuk QA:
  - TC-FA-GRP-44 dan 45 tidak menyebut baris yang dibuka elipsis-nya; spec memakai Warehouse A.
  - Expected "seluruh tree client" tidak menyebut daftar node; spec memakai node Tabel A yang tampil di sidebar.
  - "Tetap Show & aktif" untuk sort, pagination, dan Column Visibility tidak menyebut cara cek aktif; spec mengasersi tampil dan dapat dipakai.
