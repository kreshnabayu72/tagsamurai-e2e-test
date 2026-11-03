---
id: TC-FA-GRP-E2E-016-role-matrix-visibilitas-elemen-groups-list-aktor-scoped-region-west
title: "Role Matrix: Visibilitas Elemen Groups List per Role Scoped Region West (Group Manager, Manage Group CRUD, R, R+C, R+U, R+D)"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-GRP-47
  - TC-FA-GRP-48
  - TC-FA-GRP-49
  - TC-FA-GRP-50
  - TC-FA-GRP-51
  - TC-FA-GRP-52
coverage:
  web: automated
---

# Role Matrix: Visibilitas Elemen Groups List per Role Scoped Region West (Group Manager, Manage Group CRUD, R, R+C, R+U, R+D)

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama (langkah 1 sampai 10): Group Manager scope Region West (Pre-setup No 4) `groupManagerGroups_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_GM_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Role yang diuji pada langkah 12 sampai 23 (ganti akun eksplisit; semua scope Region West). Nilai kolom dipakai sebagai parameter `Verifikasi`:

| Role | Akun (Pre-setup) | Password | Kolom Checkbox | Menu (⋯) baris dan sidebar |
|---|---|---|---|---|
| Manage Group CRUD (TC-FA-GRP-48) | No 5 `manageGroupCrud_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_MGCRUD_PASSWORD` | Tampil | Detail, Add Subgroup, Edit, Delete |
| Manage Group R saja (TC-FA-GRP-49) | No 6 `manageGroupRead_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_MGR_PASSWORD` | Hidden | hanya Detail |
| Manage Group R+C (TC-FA-GRP-50) | No 6 `manageGroupCreate_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_MGRC_PASSWORD` | Hidden | Detail, Add Subgroup (Edit dan Delete Hidden) |
| Manage Group R+U (TC-FA-GRP-51) | No 6 `manageGroupUpdate_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_MGRU_PASSWORD` | Hidden | Detail, Edit (Add Subgroup dan Delete Hidden) |
| Manage Group R+D (TC-FA-GRP-52) | No 6 `manageGroupDelete_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_MGRD_PASSWORD` | Tampil (Bulk Delete tersedia) | Detail, Delete (Add Subgroup dan Edit Hidden) |

- Flag Guided Tooltip `fa-settings-groups` disetel `seen` oleh hook suite untuk akun Total Control (lihat `suite.md`); untuk keenam akun scoped flag disetel `seen` di hook `before` spec ini dan dipulihkan di hook `after` (kemampuan disediakan tim FE/BE).
- Data Pre-setup (hanya dibaca, tidak diubah): pohon group baku Tabel A (Pre-setup No 9): Global HQ > Region West > Branch West 1 > Room 301; Region East. Spec ini tidak menjalankan aksi tulis.
- Kemampuan teknis: fixture BE dan sesi API aktor, disediakan tim FE/BE (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`); spec ini tidak mengubah state global.

## Test Steps

### Role Group Manager (TC-FA-GRP-47)

1. Verifikasi menu Settings > Groups tampil, kolom Checkbox tampil, dan tombol [+] Group Hidden
2. Verifikasi sidebar menampilkan Region West, Branch West 1, dan Room 301 beserta ancestor context Global HQ
3. Klik node Region West di sidebar
4. Klik (⋯) pada baris Branch West 1
5. Verifikasi menu baris memuat Detail, Add Subgroup, Edit, Delete
6. Tutup menu dengan Esc
7. Klik (⋯) pada node Region West di sidebar
8. Verifikasi menu sidebar memuat Detail, Add Subgroup, Edit, Delete
9. Tutup menu dengan Esc
10. Verifikasi Search, Filter, Download, Changelog, sort, pagination, dan Column Visibility tampil dan aktif

### Role Manage Group (TC-FA-GRP-48 sampai 52)

11. Untuk setiap baris tabel "Role yang diuji" di Prerequisites, lakukan langkah 12 sampai 23
12. Logout dari akun sebelumnya
13. Login sebagai role pada baris tabel dengan password pada baris yang sama
14. Buka Fixed Asset > Settings > Groups
15. Verifikasi menu Settings > Groups tampil, kolom Checkbox sesuai kolom "Kolom Checkbox" tabel, dan tombol [+] Group Hidden
16. Klik node Region West di sidebar
17. Klik (⋯) pada baris Branch West 1
18. Verifikasi menu baris sesuai kolom "Menu (⋯) baris dan sidebar" tabel
19. Tutup menu dengan Esc
20. Klik (⋯) pada node Region West di sidebar
21. Verifikasi menu sidebar sesuai kolom "Menu (⋯) baris dan sidebar" tabel
22. Tutup menu dengan Esc
23. Verifikasi Search, Filter, Download, Changelog, sort, pagination, dan Column Visibility tampil dan aktif

## Notes

- Spec melewati sekitar 35 langkah setelah ekspansi (10 langkah blok Group Manager ditambah 12 langkah dikali 5 role = 70 langkah): perulangan per role dari tabel Prerequisites (8b butir 7, langkah 12 sampai 23), kelas dan dataset sama (Role Matrix visibilitas Groups List, scope Region West), tiap iterasi berdiri sendiri, dan kegagalan satu role tidak menghilangkan makna role lain. Nominal hanya 23 langkah.
- Blok Group Manager ditulis terpisah dari perulangan karena memuat `Verifikasi` tree sidebar (langkah 2) yang khusus TC-FA-GRP-47.
- Langkah penghubung (S-03): langkah 3 dan 16 (memilih Region West agar baris Branch West 1 tampil, karena Region West bukan node level 1 pada All Groups), langkah 6, 9, 19, 22 (menutup menu), langkah 12 sampai 14 (ganti akun eksplisit dan membuka layar). Hook `after` memulihkan sesi ke akun default suite (S-07).
- Urutan role mengikuti nomor TC (47 sampai 52).
- Temuan untuk QA:
  - TC-FA-GRP-47 sampai 52 menyebut "elipsis baris dan node sidebar" tanpa nama baris; spec memakai baris Branch West 1 dan node Region West.
  - Email akun Manage Group R, R+C, R+U, R+D pada Pre-setup No 6 ditulis dengan elipsis (`manageGroupRead_automated_…`); spec melengkapinya dengan pola `{namaCompany}@qwertysystem.net` seperti baris lain.
  - Nama env password per role (`FA_GM_PASSWORD`, `FA_MGCRUD_PASSWORD`, `FA_MGR_PASSWORD`, `FA_MGRC_PASSWORD`, `FA_MGRU_PASSWORD`, `FA_MGRD_PASSWORD`) adalah nama baru yang didaftarkan di `executionConfig.environmentVariables` dan `.env.example` oleh pemilik script.
  - "Bulk Delete tersedia" hanya disebut TC-FA-GRP-52; spec mengasersinya lewat kolom Checkbox tampil pada baris R+D tanpa aksi hapus.
