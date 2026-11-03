---
id: TC-FA-RP-E2E-030-role-matrix-kontrol-tab-transaction-role-per-peran-1
title: "Role Matrix: kontrol Tab Transaction Role per peran (1/2)"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-RP-105
  - TC-FA-RP-106
  - TC-FA-RP-107
  - TC-FA-RP-108
coverage:
  web: automated
---

# Role Matrix: kontrol Tab Transaction Role per peran (1/2)

## Prerequisites

- Mode: FE+BE.
- Login di hook `before` spec ini sebagai Total Control (Siti Rahmawati); halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Role & Permission, Tab Total Control). Hook `after` mengembalikan sesi ke akun default suite (Total Control, `Spectra.env.FA_TC_PASSWORD`).
- Flag Guided Tooltip `guided_tooltip_seen_fa-settings-role-permission`: diatur hook suite (lihat `suite.md`, Hook suite), termasuk untuk semua akun pada tabel Role yang diuji.
- Sesi API aktor dan pemulihan Pre-setup bersama: lihat `suite.md`, Hook suite (Sesi API aktor; Pre-setup bersama).
- Identitas Pre-setup (nama pengguna, group, role) yang dipakai langkah mengacu ke fixture `Fixture.fixedAssetRolePermission` (fixture baru, belum ada di repo, tanpa password; ditandai untuk tim FE).

Role yang diuji (Tabel Data Uji Pre-setup TC):

| TC | Role | Kelompok | Nama user | Email | Env var password |
|---|---|---|---|---|---|
| TC-FA-RP-105 | Total Control | Penuh | Siti Rahmawati (Pre-setup #2) | `totalControl_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_TC_PASSWORD` |
| TC-FA-RP-106 | Read Only | Hanya baca | Dewi Anggraini (Pre-setup #4) | `readOnly_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_RO_PASSWORD` |
| TC-FA-RP-107 | Group Manager (Fajar Nugroho, `IT Infrastructure`) | Group Manager | Fajar Nugroho (Pre-setup #5) | `groupManager_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_GM_PASSWORD` |
| TC-FA-RP-108 | Manage global user & role (Update) | Manage dengan Update | Hendra Wijaya (Pre-setup #6) | `murGlobal_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_MUR_GLOBAL_PASSWORD` |

- Data Pre-setup yang dibaca: pohon group #18 dan seed Role Transaksi #19 pada `IT Infrastructure` sub-tab `Disposal` (Nadia Putri sebagai Asset Admin Standard). Hook `before` menyalakan Require Approval ON pada `IT Infrastructure` sub-tab `Disposal` (Approver Pandu Wijaya dari #19) sesuai Precondition d (toggle `Require Approval for Disposal` diatur ON sebelum TC dijalankan karena Pre-setup #19 berstatus OFF di semua node) dan hook `after` memulihkannya ke OFF. Spec tidak menjalankan Remove atau Assign; menu baris dibuka lalu ditutup.
- Kemampuan teknis: hover pada elemen Disabled untuk membaca tooltip.
- State global yang diubah: Require Approval `Disposal` pada `IT Infrastructure` (dinyalakan hook `before`, dipulihkan hook `after`).

## Test Steps

### TC-FA-RP-105: Total Control

1. Klik Tab Transaction Role
2. Klik node `IT Infrastructure` di Sidebar Group Tree
3. Klik sub-tab `Disposal`
4. Verifikasi `[+ Assign]` pada section Asset Admin, Monitoring & Report, dan Approver tampil (Show) pada node `IT Infrastructure`
5. Klik `⋯` pada baris Nadia Putri (section Asset Admin)
6. Verifikasi Menu baris memuat `Remove` Enabled untuk target Standard (baris Nadia Putri)
7. Tutup menu baris dengan Esc
8. Verifikasi Toggle `Require Approval for Disposal` dan radio `Any approver (OR)` serta `All approvers (AND)` Enabled

### TC-FA-RP-106: Read Only

9. Ganti akun: logout, lalu login sebagai Read Only (Dewi Anggraini)
10. Klik Tab Transaction Role
11. Klik node `IT Infrastructure` di Sidebar Group Tree
12. Klik sub-tab `Disposal`
13. Verifikasi `[+ Assign]` pada seluruh section (Asset Admin, Monitoring & Report, Approver) Hidden
14. Verifikasi Aksi `Remove` pada seluruh section Hidden (baris Nadia Putri tampil)
15. Verifikasi Toggle `Require Approval for Disposal` dan radio OR/AND Disabled
16. Hover toggle `Require Approval for Disposal`
17. Verifikasi Toggle `Require Approval for Disposal` Disabled dengan tooltip `Read Only access cannot modify data.`
18. Hover radio `All approvers (AND)`
19. Verifikasi Radio OR/AND Disabled dengan tooltip `Read Only access cannot modify data.`

### TC-FA-RP-107: Group Manager

20. Ganti akun: logout, lalu login sebagai Group Manager (Fajar Nugroho, `IT Infrastructure`)
21. Klik Tab Transaction Role
22. Klik node `IT Infrastructure` di Sidebar Group Tree
23. Klik sub-tab `Disposal`
24. Verifikasi `[+ Assign]` pada section Asset Admin, Monitoring & Report, dan Approver tampil (Show) dalam cabang `IT Infrastructure` (diamati pada node `IT Infrastructure`)
25. Klik `⋯` pada baris Nadia Putri (section Asset Admin)
26. Verifikasi Menu baris memuat `Remove` Enabled untuk target Standard (baris Nadia Putri)
27. Tutup menu baris dengan Esc
28. Verifikasi Toggle `Require Approval for Disposal` dan radio `Any approver (OR)` serta `All approvers (AND)` Enabled

### TC-FA-RP-108: Manage global user & role (Update)

29. Ganti akun: logout, lalu login sebagai Manage global user & role (Update) (Hendra Wijaya)
30. Klik Tab Transaction Role
31. Klik node `IT Infrastructure` di Sidebar Group Tree
32. Klik sub-tab `Disposal`
33. Verifikasi `[+ Assign]` pada section Asset Admin, Monitoring & Report, dan Approver tampil (Show) pada node `IT Infrastructure`
34. Klik `⋯` pada baris Nadia Putri (section Asset Admin)
35. Verifikasi Menu baris memuat `Remove` Enabled untuk target Standard (baris Nadia Putri)
36. Tutup menu baris dengan Esc
37. Verifikasi Toggle `Require Approval for Disposal` dan radio `Any approver (OR)` serta `All approvers (AND)` Enabled

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-role-permission/TestCases/tc-settings-role-permission.md`.
- Spec Role Matrix (bagian 3a konvensi) ditulis per blok role: langkah tiap role identik tetapi ganti akun menuntut Step eksplisit (akun pertama login di hook `before`), sehingga satu blok per TC. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): klik tab (langkah 1, 10, 21 dan 30); membuka menu baris `⋯` (langkah 5, 25 dan 34) dan menutupnya dengan Esc (langkah 7, 27 dan 36); hover untuk membaca tooltip (langkah 16 dan 18).
- Ganti akun eksplisit (logout lalu login) pada langkah 9, 20, dan 29.
- Asersi `Hidden` memakai halaman yang sudah termuat dengan baris target yang tampil (baris Nadia Putri) sebagai anchor permukaan (bagian 8b butir 2).
- Pembagian TC lintas spec: TC-FA-RP-109 sampai TC-FA-RP-111 ada di spec 031.
- Spec melewati sekitar 35 langkah (37 langkah). Semua blok satu kelas harness (Role Matrix, baca saja) dan berdiri sendiri: tiap blok role dimulai dengan ganti akun dan membuka tab sendiri, sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna (bagian 3, pemisah butir b).
- Kombinasi role dan aksi yang tidak punya TC sumber tidak ditambahkan.
- Temuan untuk QA:
  - TC-FA-RP-107 Expected a menyebut `[+ Assign]` "dalam cabang ... beserta descendant", sedangkan Langkah Uji hanya memilih node `IT Infrastructure`; spec mengasersi pada node itu saja.
  - Target Standard untuk `Remove` tidak disebut nama; spec memakai Nadia Putri (Asset Admin, seed Pre-setup #19).
  - Tooltip toggle dan radio dibaca pada toggle `Require Approval for Disposal` dan radio `All approvers (AND)`; TC tidak menyebut elemen yang di-hover.
