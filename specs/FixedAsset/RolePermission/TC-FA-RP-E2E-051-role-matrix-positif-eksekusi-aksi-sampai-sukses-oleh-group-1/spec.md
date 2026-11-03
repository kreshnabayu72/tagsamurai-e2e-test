---
id: TC-FA-RP-E2E-051-role-matrix-positif-eksekusi-aksi-sampai-sukses-oleh-group-1
title: "Role Matrix Positif: eksekusi aksi sampai sukses oleh Group Manager (1/2)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-RP-179
  - TC-FA-RP-180
  - TC-FA-RP-181
  - TC-FA-RP-182
coverage:
  web: automated
---

# Role Matrix Positif: eksekusi aksi sampai sukses oleh Group Manager (1/2)

## Prerequisites

- Mode: FE+BE.
- Login di hook `before` spec ini sebagai Group Manager (Fajar Nugroho, `IT Infrastructure`) (Fajar Nugroho); halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Role & Permission, Tab Total Control). Hook `after` mengembalikan sesi ke akun default suite (Total Control, `Spectra.env.FA_TC_PASSWORD`).
- Flag Guided Tooltip `guided_tooltip_seen_fa-settings-role-permission`: diatur hook suite (lihat `suite.md`, Hook suite), termasuk untuk semua akun pada tabel Role yang diuji.
- Sesi API aktor dan pemulihan Pre-setup bersama: lihat `suite.md`, Hook suite (Sesi API aktor; Pre-setup bersama).
- Identitas Pre-setup (nama pengguna, group, role) yang dipakai langkah mengacu ke fixture `Fixture.fixedAssetRolePermission` (fixture baru, belum ada di repo, tanpa password; ditandai untuk tim FE).

Role yang diuji (Tabel Data Uji Pre-setup TC):

| TC | Role | Kelompok | Nama user | Email | Env var password |
|---|---|---|---|---|---|
| TC-FA-RP-179 sampai TC-FA-RP-182 | Group Manager (Fajar Nugroho, `IT Infrastructure`) | Group Manager | Fajar Nugroho (Pre-setup #5) | `groupManager_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_GM_PASSWORD` |

- Data Pre-setup yang dibaca dan diubah: pool pengguna #15 (Budi Santoso, Budi Setiawan, Ahmad Fauzi), pohon group #18, seed Role Transaksi #19, dan penugasan #33. Detail Role Group Role `Manage files` pada node `IT Infrastructure`. Seeding ke kondisi Precondition TC dilakukan hook `before` dan lewat langkah penghubung "Seed via API ... hingga ... tersimpan"; hook `after` memulihkan seluruh state yang diubah ke kondisi Tabel Data Uji Pre-setup TC (pengecualian S-06 2026-10-30: target aksi tulis memakai user pool Pre-setup #15; pemulihan dijamin fixture backend yang disediakan tim FE/BE dan dinyatakan di `suite.md`, Hook suite, Pre-setup bersama).
- Kemampuan teknis: seed state Pre-setup lewat API untuk langkah penghubung "Seed via API", disediakan tim FE/BE.
- State global yang diubah: baris peran pool pengguna #15 (dipulihkan hook `after`).

## Test Steps

1. Klik Tab System
2. Klik Role Name `Manage files` pada section Group Role
3. Klik node `IT Infrastructure` di Sidebar Group Tree

### TC-FA-RP-179: Assign User ke Role Group (`Manage files`)

4. Klik `[+ Assign]`
5. Pilih Budi Santoso pada popup Assign dengan field Group `IT Infrastructure`
6. Klik `[Assign]`
7. Verifikasi Toast sukses `Success, Manage files has been assigned.`
8. Verifikasi Baris Budi Santoso masuk tabel
9. Verifikasi Checkbox Read baris Budi Santoso checked
10. Verifikasi Checkbox Read baris Budi Santoso terkunci (Disabled)
11. Verifikasi Checkbox Create, Update, Delete baris Budi Santoso belum aktif

### TC-FA-RP-180: Edit CRUD sampai sukses

12. Seed via API: Ahmad Fauzi memegang Group Role `Manage files` di `IT Infrastructure` dengan Read aktif dan Delete belum aktif hingga tersimpan
13. Muat ulang halaman (F5), lalu buka kembali Detail Role `Manage files` (klik Tab System, Role Name `Manage files` pada section Group Role, lalu node `IT Infrastructure`)
14. Centang checkbox Delete pada baris Ahmad Fauzi
15. Verifikasi Toast sukses `Success, permissions have been updated.`
16. Muat ulang halaman (F5), lalu buka kembali Detail Role `Manage files` (klik Tab System, Role Name `Manage files` pada section Group Role, lalu node `IT Infrastructure`)
17. Verifikasi Checkbox Delete baris Ahmad Fauzi tercentang dan tersimpan setelah muat ulang

### TC-FA-RP-181: Remove baris peran sampai sukses

18. Seed via API: Budi Santoso memegang Group Role `Manage files` di `IT Infrastructure` dengan Read aktif hingga tersimpan
19. Muat ulang halaman (F5), lalu buka kembali Detail Role `Manage files` (klik Tab System, Role Name `Manage files` pada section Group Role, lalu node `IT Infrastructure`)
20. Klik `⋯` pada baris Budi Santoso
21. Klik `Remove`
22. Verifikasi Dialog `Remove User` tampil dengan bullet `Budi S` dan `The role assignment, including its permissions, will be removed permanently.`
23. Klik `[Remove]` pada dialog
24. Verifikasi Toast sukses `Success, user has been removed.`
25. Verifikasi Baris Budi Santoso hilang dari tabel

### TC-FA-RP-182: Bulk Remove dua baris sampai sukses

26. Seed via API: Budi Santoso dan Budi Setiawan memegang Group Role `Manage files` di `IT Infrastructure` dengan Read aktif hingga tersimpan
27. Muat ulang halaman (F5), lalu buka kembali Detail Role `Manage files` (klik Tab System, Role Name `Manage files` pada section Group Role, lalu node `IT Infrastructure`)
28. Centang baris Budi Santoso
29. Centang baris Budi Setiawan
30. Klik `Bulk Action`
31. Klik `Remove`
32. Verifikasi Dialog `Remove Users` tampil dengan bullet `Budi S` dan `Budi S`
33. Klik `[Remove]` pada dialog
34. Verifikasi Toast sukses `Success, user has been removed.`
35. Verifikasi Kedua baris (Budi Santoso dan Budi Setiawan) hilang dari tabel

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-role-permission/TestCases/tc-settings-role-permission.md`.
- Spec Role Matrix (bagian 3a konvensi) ditulis per blok role: ganti akun menuntut Step eksplisit (akun pertama login di hook `before`). Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): klik tab (langkah 1); seed state precondition lewat API (langkah 12, 18 dan 26) dan memuat ulang halaman lalu membuka kembali Detail Role (langkah 13, 16, 19 dan 27).
- Asersi baris hilang memakai toast sukses yang sudah diasersi sebagai anchor (bagian 8b butir 2).
- Pembagian TC lintas spec: TC-FA-RP-183 sampai TC-FA-RP-186 ada di spec 052.
- Urutan TC mengikuti nomor TC; state tiap TC dibangun ulang lewat seed API sehingga TC tidak bergantung pada hasil TC sebelumnya (S-04, S-06).
- Kombinasi role dan aksi yang tidak punya TC sumber tidak ditambahkan.
- Temuan untuk QA:
  - Precondition d tiap TC menyebut Budi Santoso, Budi Setiawan, dan Ahmad Fauzi "tidak memegang role yang disentuh" tetapi tiap TC menyentuh role berbeda dan beberapa TC (edit CRUD, Remove, Bulk Remove) membutuhkan user itu memegang role; spec men-seed kondisi tiap TC lewat langkah penghubung "Seed via API" sebelum aksi.
  - Mekanisme seed API tidak disebut TC, PRD, atau LLD; ditulis sebagai kemampuan yang disediakan tim FE/BE tanpa endpoint (S-13).
  - Post Condition TC tidak memuat langkah observasi sehingga tidak diasersi; pemulihan state dilakukan hook `after`.
  - Expected b TC-FA-RP-179 "Read checked dan terkunci, C/U/D belum aktif" ditulis sebagai tiga `Verifikasi` (Read checked, Read terkunci, Create, Update, Delete belum aktif).
  - TC-FA-RP-180 dan TC-FA-RP-181 tidak menyebut cara membuka kembali Detail Role setelah muat ulang halaman; spec membukanya dari Tab System (dan memilih node `IT Infrastructure` untuk Group Role).
  - TC-FA-RP-179 menyebut "field Group `IT Infrastructure`" pada popup Assign tanpa menyebut apakah field terisi otomatis dari node atau dipilih; spec menulis field Group `IT Infrastructure` sebagai bagian langkah memilih user.
