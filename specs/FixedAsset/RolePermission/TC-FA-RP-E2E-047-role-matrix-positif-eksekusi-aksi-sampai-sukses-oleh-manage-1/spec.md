---
id: TC-FA-RP-E2E-047-role-matrix-positif-eksekusi-aksi-sampai-sukses-oleh-manage-1
title: "Role Matrix Positif: eksekusi aksi sampai sukses oleh Manage global user & role (Update) (1/2)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-RP-163
  - TC-FA-RP-164
  - TC-FA-RP-165
  - TC-FA-RP-166
coverage:
  web: automated
---

# Role Matrix Positif: eksekusi aksi sampai sukses oleh Manage global user & role (Update) (1/2)

## Prerequisites

- Mode: FE+BE.
- Login di hook `before` spec ini sebagai Manage global user & role (Update) (Hendra Wijaya); halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Role & Permission, Tab Total Control). Hook `after` mengembalikan sesi ke akun default suite (Total Control, `Spectra.env.FA_TC_PASSWORD`).
- Flag Guided Tooltip `guided_tooltip_seen_fa-settings-role-permission`: diatur hook suite (lihat `suite.md`, Hook suite), termasuk untuk semua akun pada tabel Role yang diuji.
- Sesi API aktor dan pemulihan Pre-setup bersama: lihat `suite.md`, Hook suite (Sesi API aktor; Pre-setup bersama).
- Identitas Pre-setup (nama pengguna, group, role) yang dipakai langkah mengacu ke fixture `Fixture.fixedAssetRolePermission` (fixture baru, belum ada di repo, tanpa password; ditandai untuk tim FE).

Role yang diuji (Tabel Data Uji Pre-setup TC):

| TC | Role | Kelompok | Nama user | Email | Env var password |
|---|---|---|---|---|---|
| TC-FA-RP-163 sampai TC-FA-RP-166 | Manage global user & role (Update) | Manage dengan Update | Hendra Wijaya (Pre-setup #6) | `murGlobal_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_MUR_GLOBAL_PASSWORD` |

- Data Pre-setup yang dibaca dan diubah: pool pengguna #15 (Budi Santoso, Budi Setiawan, Ahmad Fauzi), pohon group #18, seed Role Transaksi #19, dan penugasan #33. Detail Role Global Role `Manage accounting` (assign dan edit CRUD) dan `Manage Open API` (Remove dan Bulk Remove). Seeding ke kondisi Precondition TC dilakukan hook `before` dan lewat langkah penghubung "Seed via API ... hingga ... tersimpan"; hook `after` memulihkan seluruh state yang diubah ke kondisi Tabel Data Uji Pre-setup TC (pengecualian S-06 2026-10-30: target aksi tulis memakai user pool Pre-setup #15; pemulihan dijamin fixture backend yang disediakan tim FE/BE dan dinyatakan di `suite.md`, Hook suite, Pre-setup bersama).
- Kemampuan teknis: seed state Pre-setup lewat API untuk langkah penghubung "Seed via API", disediakan tim FE/BE.
- State global yang diubah: baris peran pool pengguna #15 (dipulihkan hook `after`).

## Test Steps

1. Klik Tab System
2. Klik Role Name `Manage accounting` pada section Global Role

### TC-FA-RP-163: Assign User ke Role Global (`Manage accounting`)

3. Klik `[+ Assign]`
4. Pilih Budi Santoso pada popup Assign
5. Klik `[Assign]`
6. Verifikasi Toast sukses `Success, Manage accounting has been assigned.`
7. Verifikasi Baris Budi Santoso masuk tabel
8. Verifikasi Checkbox Read baris Budi Santoso checked
9. Verifikasi Checkbox Read baris Budi Santoso terkunci (Disabled)
10. Verifikasi Checkbox Create, Update, Delete baris Budi Santoso belum aktif

### TC-FA-RP-164: Edit CRUD sampai sukses

11. Seed via API: Ahmad Fauzi memegang Global Role `Manage accounting` dengan Read aktif dan Create belum aktif hingga tersimpan
12. Muat ulang halaman (F5), lalu buka kembali Detail Role `Manage accounting` (klik Tab System, lalu Role Name `Manage accounting` pada section Global Role)
13. Centang checkbox Create pada baris Ahmad Fauzi
14. Verifikasi Toast sukses `Success, permissions have been updated.`
15. Muat ulang halaman (F5), lalu buka kembali Detail Role `Manage accounting` (klik Tab System, lalu Role Name `Manage accounting` pada section Global Role)
16. Verifikasi Checkbox Create baris Ahmad Fauzi tercentang dan tersimpan setelah muat ulang

### TC-FA-RP-165: Remove baris peran sampai sukses (`Manage Open API`)

17. Seed via API: Budi Santoso dan Budi Setiawan memegang Global Role `Manage Open API` dengan Read aktif hingga tersimpan
18. Muat ulang halaman (F5), lalu buka kembali Detail Role `Manage Open API` (klik Tab System, lalu Role Name `Manage Open API` pada section Global Role)
19. Klik `⋯` pada baris Budi Santoso
20. Klik `Remove`
21. Verifikasi Dialog `Remove User` tampil dengan bullet `Budi S` dan `The role assignment, including its permissions, will be removed permanently.`
22. Klik `[Remove]` pada dialog
23. Verifikasi Toast sukses `Success, user has been removed.`
24. Verifikasi Baris Budi Santoso hilang dari tabel

### TC-FA-RP-166: Bulk Remove dua baris sampai sukses (`Manage Open API`)

25. Seed via API: Budi Santoso memegang Global Role `Manage Open API` dengan Read aktif hingga tersimpan
26. Muat ulang halaman (F5), lalu buka kembali Detail Role `Manage Open API` (klik Tab System, lalu Role Name `Manage Open API` pada section Global Role)
27. Centang baris Budi Santoso
28. Centang baris Budi Setiawan
29. Klik `Bulk Action`
30. Klik `Remove`
31. Verifikasi Dialog `Remove Users` tampil dengan bullet `Budi S` dan `Budi S`
32. Klik `[Remove]` pada dialog
33. Verifikasi Toast sukses `Success, user has been removed.`
34. Verifikasi Kedua baris (Budi Santoso dan Budi Setiawan) hilang dari tabel

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-role-permission/TestCases/tc-settings-role-permission.md`.
- Spec Role Matrix (bagian 3a konvensi) ditulis per blok role: ganti akun menuntut Step eksplisit (akun pertama login di hook `before`). Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): klik tab (langkah 1); seed state precondition lewat API (langkah 11, 17 dan 25) dan memuat ulang halaman lalu membuka kembali Detail Role (langkah 12, 15, 18 dan 26).
- Asersi baris hilang memakai toast sukses yang sudah diasersi sebagai anchor (bagian 8b butir 2).
- Pembagian TC lintas spec: TC-FA-RP-167 sampai TC-FA-RP-170 ada di spec 048.
- Urutan TC mengikuti nomor TC; state tiap TC dibangun ulang lewat seed API sehingga TC tidak bergantung pada hasil TC sebelumnya (S-04, S-06).
- Kombinasi role dan aksi yang tidak punya TC sumber tidak ditambahkan.
- Temuan untuk QA:
  - Precondition d tiap TC menyebut Budi Santoso, Budi Setiawan, dan Ahmad Fauzi "tidak memegang role yang disentuh" tetapi tiap TC menyentuh role berbeda dan beberapa TC (edit CRUD, Remove, Bulk Remove) membutuhkan user itu memegang role; spec men-seed kondisi tiap TC lewat langkah penghubung "Seed via API" sebelum aksi.
  - Mekanisme seed API tidak disebut TC, PRD, atau LLD; ditulis sebagai kemampuan yang disediakan tim FE/BE tanpa endpoint (S-13).
  - Post Condition TC tidak memuat langkah observasi sehingga tidak diasersi; pemulihan state dilakukan hook `after`.
  - Expected b TC-FA-RP-163 "Read checked dan terkunci, C/U/D belum aktif" ditulis sebagai tiga `Verifikasi` (Read checked, Read terkunci, Create, Update, Delete belum aktif).
  - TC-FA-RP-164 dan TC-FA-RP-165 tidak menyebut cara membuka kembali Detail Role setelah muat ulang halaman; spec membukanya dari Tab System (dan memilih node `IT Infrastructure` untuk Group Role).
