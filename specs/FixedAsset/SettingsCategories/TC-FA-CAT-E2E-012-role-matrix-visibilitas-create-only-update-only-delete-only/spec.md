---
id: TC-FA-CAT-E2E-012-role-matrix-visibilitas-create-only-update-only-delete-only
title: "Role Matrix: Visibilitas Elemen Categories List (Create-Only, Update-Only, Delete-Only)"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CAT-35
  - TC-FA-CAT-36
  - TC-FA-CAT-37
coverage:
  web: automated
---

# Role Matrix: Visibilitas Elemen Categories List (Create-Only, Update-Only, Delete-Only)

## Prerequisites

- Mode: FE+BE.
- Role yang diuji:

  | TC | Role | Pre-setup | Email | Env var password |
  |---|---|---|---|---|
  | TC-FA-CAT-35 | Create-Only (Manage Asset Master Data: C) | #4 | `createOnly_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_CO_PASSWORD` |
  | TC-FA-CAT-36 | Update-Only (Manage Asset Master Data: U) | #5 | `updateOnly_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_UO_PASSWORD` |
  | TC-FA-CAT-37 | Delete-Only (Manage Asset Master Data: D) | #6 | `deleteOnly_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_DO_PASSWORD` |
- Login akun aktor pertama (Create-Only) di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Pengecualian atas `suite.md`: precondition TC adalah halaman utama FAMS, sehingga hook `beforeEach` membuka halaman utama FAMS (bukan Categories) untuk spec ini. Hook `after` mengembalikan sesi ke akun default suite (Total Control). Ganti akun di tengah spec memakai langkah logout dan login eksplisit.
- Env var `FA_CO_PASSWORD`, `FA_UO_PASSWORD`, `FA_DO_PASSWORD` belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`: didaftarkan tim FE. Password tidak ditulis di spec atau fixture.
- Data: client CatMain (Pre-setup #20, plan Enterprise); baris `Furniture` dan `Tools` dibaca; spec tidak mengubah data.
- Flag Guided Tooltip halaman Categories: hook suite `before` men-set true untuk akun aktor dan `after` memulihkannya (butir "Flag Guided Tooltip" di `suite.md`). Berlaku untuk ketiga akun aktor.
- Seed dan pemulihan client Pre-setup lewat API disediakan tim FE/BE (butir "Seed dan pemulihan lewat API" di `suite.md`).
- Identitas data Pre-setup dibaca dari `fixtures/settings-categories.json` (belum ada; disediakan tim FE, nama kunci ditetapkan tim FE). Nama data Pre-setup ditulis seperti di TC.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-CAT-35: Visibilitas elemen Categories List untuk aktor Create-Only

1. Klik menu `Settings > Categories` pada sidebar navigasi FAMS
2. Verifikasi Create-Only: menu `Settings > Categories` Show
3. Verifikasi Create-Only: halaman Categories terbuka (aktor memiliki Read)
4. Verifikasi Create-Only: sidebar `[+] Category` Show
5. Klik elipsis (⋯) pada baris `Furniture`
6. Verifikasi Create-Only: row action Detail, + Add Subcategory Show pada baris `Furniture`
7. Verifikasi Create-Only: row action Edit, Delete Hidden pada baris `Furniture`
8. Tutup menu row action
9. Verifikasi Create-Only: checkbox baris dan Bulk Action Bar `[Delete]` Hidden
10. Verifikasi Create-Only: Toolbar Search, Filter, Download, Changelog dan Sidebar Category Tree Show

### TC-FA-CAT-36: Visibilitas elemen Categories List untuk aktor Update-Only

11. Logout dari akun Create-Only
12. Login sebagai Update-Only (`updateOnly_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.FA_UO_PASSWORD`)
13. Klik menu `Settings > Categories` pada sidebar navigasi FAMS
14. Verifikasi Update-Only: menu `Settings > Categories` Show
15. Verifikasi Update-Only: halaman Categories terbuka (aktor memiliki Read)
16. Verifikasi Update-Only: sidebar `[+] Category` Hidden
17. Klik elipsis (⋯) pada baris `Furniture`
18. Verifikasi Update-Only: row action Detail, Edit Show pada baris `Furniture`
19. Verifikasi Update-Only: row action + Add Subcategory, Delete Hidden pada baris `Furniture`
20. Tutup menu row action
21. Verifikasi Update-Only: checkbox baris dan Bulk Action Bar `[Delete]` Hidden
22. Verifikasi Update-Only: Toolbar Search, Filter, Download, Changelog dan Sidebar Category Tree Show

### TC-FA-CAT-37: Visibilitas elemen Categories List untuk aktor Delete-Only

23. Logout dari akun Update-Only
24. Login sebagai Delete-Only (`deleteOnly_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.FA_DO_PASSWORD`)
25. Klik menu `Settings > Categories` pada sidebar navigasi FAMS
26. Verifikasi Delete-Only: menu `Settings > Categories` Show
27. Verifikasi Delete-Only: halaman Categories terbuka (aktor memiliki Read)
28. Verifikasi Delete-Only: sidebar `[+] Category` Hidden
29. Klik elipsis (⋯) pada baris `Furniture`
30. Verifikasi Delete-Only: row action Detail, Delete Show pada baris `Furniture`
31. Verifikasi Delete-Only: row action + Add Subcategory, Edit Hidden pada baris `Furniture`
32. Tutup menu row action
33. Verifikasi Delete-Only: checkbox baris Show
34. Centang checkbox baris `Tools`
35. Verifikasi Delete-Only: Bulk Action Bar `[Delete]` Show
36. Hapus centang checkbox baris `Tools`
37. Verifikasi Delete-Only: Toolbar Search, Filter, Download, Changelog dan Sidebar Category Tree Show

## Notes

- Sumber: `fixed-asset/settings-categories/TestCases/tc-settings-categories.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Mode: FE+BE. Spec Role Matrix visibilitas (bagian 3a): satu daftar elemen, banyak role, hasil berbeda per role; polaritas Show dan Hidden dicampur.
- Langkah penghubung (S-03): tiap langkah "Tutup menu row action" dan "Hapus centang checkbox baris `Tools`", serta pasangan logout dan login di awal blok TC-FA-CAT-36 dan TC-FA-CAT-37 (ganti akun eksplisit; akun pertama login di hook `before`, S-07).
- Langkah "Centang checkbox baris `Tools` bila checkbox tampil" pada LK TC ditulis deterministik per role: Delete-Only (Expected: Show) mencentang checkbox; Create-Only dan Update-Only (Expected: Hidden) memverifikasi checkbox dan Bulk Action Bar Hidden. Bulk Action Bar Hidden dikerjakan sebagai satu `Verifikasi` bersama checkbox karena tanpa checkbox tidak ada seleksi yang memunculkan bar (S-03).
- Temuan untuk QA:
  - Nama env var password per role (`FA_CO_PASSWORD`, `FA_UO_PASSWORD`, `FA_DO_PASSWORD`) tidak tertulis di TC; diusulkan spec dan perlu keputusan tim.
- Ukuran spec (37 langkah, melewati sekitar 35): Role Matrix mengulang urutan langkah untuk tiap role (bagian 3a) dan tiap klausa Expected menjadi satu `Verifikasi` (S-01). Spec ditulis per blok role karena ganti akun menuntut Step eksplisit (bagian 3a, keputusan 2026-10-30) dan hasil tiap role berbeda; tiap blok berdiri sendiri (login ulang eksplisit di awal blok) sehingga bagian sesudahnya tetap bermakna walau blok sebelumnya gagal; spec tidak dipecah.
- Spec melewati 35 langkah (37 langkah). Alasan: satu kelas harness dan satu dataset; Expected dipecah per klausa (S-01) dan blok berdiri sendiri; nomor cadangan slice habis sehingga tidak dipecah lebih jauh.
