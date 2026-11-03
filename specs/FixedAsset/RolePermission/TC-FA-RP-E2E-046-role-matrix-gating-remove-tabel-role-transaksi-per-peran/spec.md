---
id: TC-FA-RP-E2E-046-role-matrix-gating-remove-tabel-role-transaksi-per-peran
title: "Role Matrix: gating Remove tabel Role Transaksi per peran"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-RP-160
  - TC-FA-RP-161
  - TC-FA-RP-162
coverage:
  web: automated
---

# Role Matrix: gating Remove tabel Role Transaksi per peran

## Prerequisites

- Mode: FE+BE.
- Login di hook `before` spec ini sebagai Total Control (Siti Rahmawati); halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Role & Permission, Tab Total Control). Hook `after` mengembalikan sesi ke akun default suite (Total Control, `Spectra.env.FA_TC_PASSWORD`).
- Flag Guided Tooltip `guided_tooltip_seen_fa-settings-role-permission`: diatur hook suite (lihat `suite.md`, Hook suite), termasuk untuk semua akun pada tabel Role yang diuji.
- Sesi API aktor dan pemulihan Pre-setup bersama: lihat `suite.md`, Hook suite (Sesi API aktor; Pre-setup bersama).
- Identitas Pre-setup (nama pengguna, group, role) yang dipakai langkah mengacu ke fixture `Fixture.fixedAssetRolePermission` (fixture baru, belum ada di repo, tanpa password; ditandai untuk tim FE).

Role yang diuji (Tabel Data Uji Pre-setup TC):

| TC | Role | Kelompok | Nama user | Email | Env var password |
|---|---|---|---|---|---|
| TC-FA-RP-160 | Total Control | Penuh | Siti Rahmawati (Pre-setup #2) | `totalControl_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_TC_PASSWORD` |
| TC-FA-RP-161 | Manage global user & role (Update) | Manage dengan Update | Hendra Wijaya (Pre-setup #6) | `murGlobal_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_MUR_GLOBAL_PASSWORD` |
| TC-FA-RP-162 | Group Manager (Fajar Nugroho, `IT Infrastructure`) | Group Manager | Fajar Nugroho (Pre-setup #5) | `groupManager_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_GM_PASSWORD` |

Baris target (parameter langkah berulang):

| TC | Detail Role | Baris | Perilaku | Tooltip |
|---|---|---|---|---|
| TC-FA-RP-160 | Tabel Role Transaksi `IT Infrastructure` sub-tab `Disposal` | Admin Utama (Default User) | Disabled | `Default User cannot be modified.` |
| TC-FA-RP-160 | Tabel Role Transaksi `IT Infrastructure` sub-tab `Disposal` | Siti Rahmawati (diri sendiri) | Disabled | `You can't manage your own account from here.` |
| TC-FA-RP-161 | Tabel Role Transaksi `IT Infrastructure` sub-tab `Disposal` | Rina Wulandari (Total Control) | Disabled | `You don't have permission to edit.` |
| TC-FA-RP-161 | Tabel Role Transaksi `IT Infrastructure` sub-tab `Disposal` | Maya Anggraeni (Read Only) | Disabled | `You don't have permission to edit.` |
| TC-FA-RP-162 | Tabel Role Transaksi `IT Infrastructure` sub-tab `Disposal` | Rina Wulandari (Total Control) | Disabled | `You don't have permission to edit.` |
| TC-FA-RP-162 | Tabel Role Transaksi `IT Infrastructure` sub-tab `Disposal` | Maya Anggraeni (Read Only) | Disabled | `You don't have permission to edit.` |

- Data Pre-setup yang dibaca: pohon group #18, seed Role Transaksi #19 (Nadia Putri sebagai target Standard), #3 (Rina Wulandari), dan #12 (Maya Anggraeni). Precondition d: Rina Wulandari, Maya Anggraeni, Siti Rahmawati, dan Admin Utama memegang role pada `IT Infrastructure` sub-tab `Disposal` (Asset Admin atau Monitoring & Report), di-seed hook `before` dan dipulihkan hook `after`. Spec tidak menjalankan Remove; menu baris dibuka lalu ditutup.
- Kemampuan teknis: hover pada elemen Disabled untuk membaca tooltip.
- State global yang diubah: tidak ada selain seed Role Transaksi hook `before` (dipulihkan hook `after`).

## Test Steps

### TC-FA-RP-160: Total Control

1. Klik Tab Transaction Role
2. Klik node `IT Infrastructure` di Sidebar Group Tree
3. Klik sub-tab `Disposal`
4. Untuk setiap baris tabel Baris target dengan TC TC-FA-RP-160 (langkah 5 sampai 8):
5. Klik `⋯` pada baris target
6. Hover `Remove` pada menu baris
7. Verifikasi Aksi `Remove` baris target Disabled dengan tooltip sesuai kolom Tooltip
8. Tutup menu baris dengan Esc
9. Klik `⋯` pada baris Nadia Putri (Standard)
10. Verifikasi Aksi `Remove` baris Nadia Putri Enabled
11. Tutup menu baris dengan Esc

### TC-FA-RP-161: Manage global user & role (Update)

12. Ganti akun: logout, lalu login sebagai Manage global user & role (Update) (Hendra Wijaya)
13. Klik Tab Transaction Role
14. Klik node `IT Infrastructure` di Sidebar Group Tree
15. Klik sub-tab `Disposal`
16. Untuk setiap baris tabel Baris target dengan TC TC-FA-RP-161 (langkah 17 sampai 20):
17. Klik `⋯` pada baris target
18. Hover `Remove` pada menu baris
19. Verifikasi Aksi `Remove` baris target Disabled dengan tooltip sesuai kolom Tooltip
20. Tutup menu baris dengan Esc
21. Klik `⋯` pada baris Nadia Putri (Standard)
22. Verifikasi Aksi `Remove` baris Nadia Putri Enabled
23. Tutup menu baris dengan Esc

### TC-FA-RP-162: Group Manager

24. Ganti akun: logout, lalu login sebagai Group Manager (Fajar Nugroho, `IT Infrastructure`)
25. Klik Tab Transaction Role
26. Klik node `IT Infrastructure` di Sidebar Group Tree
27. Klik sub-tab `Disposal`
28. Untuk setiap baris tabel Baris target dengan TC TC-FA-RP-162 (langkah 29 sampai 32):
29. Klik `⋯` pada baris target
30. Hover `Remove` pada menu baris
31. Verifikasi Aksi `Remove` baris target Disabled dengan tooltip sesuai kolom Tooltip
32. Tutup menu baris dengan Esc
33. Klik `⋯` pada baris Nadia Putri (Standard)
34. Verifikasi Aksi `Remove` baris Nadia Putri Enabled
35. Tutup menu baris dengan Esc

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-role-permission/TestCases/tc-settings-role-permission.md`.
- Spec Role Matrix (bagian 3a konvensi) ditulis per blok role: ganti akun menuntut Step eksplisit (akun pertama login di hook `before`). Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): klik tab (langkah 1, 13 dan 25); membuka menu baris `⋯` (langkah 5, 9, 17, 21, 29 dan 33) dan menutupnya dengan Esc (langkah 8, 11, 20, 23, 32 dan 35); hover untuk membaca tooltip (langkah 6, 18 dan 30); mengulang 5 sampai 8, 17 sampai 20, dan 29 sampai 32 untuk tiap baris target.
- Ganti akun eksplisit (logout lalu login) pada langkah 12 dan 24.
- Asersi Disabled dan Enabled hanya diamati pada baris yang tampil; tidak ada asersi absence.
- Spec melewati sekitar 35 langkah dengan ekspansi (47 langkah; 35 langkah nominal). Semua blok satu kelas harness dan berdiri sendiri: tiap blok role dimulai dengan ganti akun dan membuka sub-tab sendiri, sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna (bagian 3, pemisah butir b); baris target memakai langkah berulang dengan tabel Baris target di Prerequisites (bagian 8b butir 7).
- Kombinasi role dan aksi yang tidak punya TC sumber tidak ditambahkan.
- Temuan untuk QA:
  - TC-FA-RP-160 sampai TC-FA-RP-162 Precondition d menyebut role "Asset Admin atau Monitoring & Report" tanpa menyebut section tiap baris; spec mencari baris lewat nama pada tabel Role Transaksi sub-tab `Disposal`.
  - Target Standard tidak disebut nama; spec memakai Nadia Putri (Asset Admin, seed Pre-setup #19).
  - Tooltip dibaca pada item `Remove` di menu baris; TC tidak menyebut elemen yang di-hover.
  - "Siti Rahmawati/aktor" pada Precondition d TC-FA-RP-161 dan TC-FA-RP-162 menyebut aktor sebagai baris yang memegang role, sedangkan aktor kedua blok itu bukan Siti Rahmawati; spec tidak mengasersi baris Siti Rahmawati pada kedua blok.
