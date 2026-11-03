---
id: TC-FA-RP-E2E-031-role-matrix-kontrol-tab-transaction-role-per-peran-2
title: "Role Matrix: kontrol Tab Transaction Role per peran (2/2)"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-FA-RP-109
  - TC-FA-RP-110
  - TC-FA-RP-111
coverage:
  web: automated
---

# Role Matrix: kontrol Tab Transaction Role per peran (2/2)

## Prerequisites

- Mode: FE+BE.
- Login di hook `before` spec ini sebagai Manage user & role (Group, Update) (Gita Maharani); halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Role & Permission, Tab Total Control). Hook `after` mengembalikan sesi ke akun default suite (Total Control, `Spectra.env.FA_TC_PASSWORD`).
- Flag Guided Tooltip `guided_tooltip_seen_fa-settings-role-permission`: diatur hook suite (lihat `suite.md`, Hook suite), termasuk untuk semua akun pada tabel Role yang diuji.
- Sesi API aktor dan pemulihan Pre-setup bersama: lihat `suite.md`, Hook suite (Sesi API aktor; Pre-setup bersama).
- Identitas Pre-setup (nama pengguna, group, role) yang dipakai langkah mengacu ke fixture `Fixture.fixedAssetRolePermission` (fixture baru, belum ada di repo, tanpa password; ditandai untuk tim FE).

Role yang diuji (Tabel Data Uji Pre-setup TC):

| TC | Role | Kelompok | Nama user | Email | Env var password |
|---|---|---|---|---|---|
| TC-FA-RP-109 | Manage user & role (Group, Update, `IT Infrastructure`) | Manage dengan Update | Gita Maharani (Pre-setup #7) | `murGroup_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_MUR_GROUP_PASSWORD` |
| TC-FA-RP-110 | Manage global user & role tanpa Update | Manage tanpa Update | Bayu Prakoso (Pre-setup #8) | `murReadOnlyGate_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_MUR_GLOBAL_RO_PASSWORD` |
| TC-FA-RP-111 | Manage user & role tanpa Update (Group, `IT Infrastructure`) | Manage tanpa Update | Wulan Sari (Pre-setup #9) | `murGroupReadOnly_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_MUR_GROUP_RO_PASSWORD` |

- Data Pre-setup yang dibaca: pohon group #18 dan seed Role Transaksi #19 pada `IT Infrastructure` sub-tab `Disposal` (Nadia Putri sebagai Asset Admin Standard). Hook `before` menyalakan Require Approval ON pada `IT Infrastructure` sub-tab `Disposal` (Approver Pandu Wijaya dari #19) sesuai Precondition d (toggle `Require Approval for Disposal` diatur ON sebelum TC dijalankan karena Pre-setup #19 berstatus OFF di semua node) dan hook `after` memulihkannya ke OFF. Spec tidak menjalankan Remove atau Assign; menu baris dibuka lalu ditutup.
- Kemampuan teknis: hover pada elemen Disabled untuk membaca tooltip.
- State global yang diubah: Require Approval `Disposal` pada `IT Infrastructure` (dinyalakan hook `before`, dipulihkan hook `after`).

## Test Steps

### TC-FA-RP-109: Manage user & role (Group, Update)

1. Klik Tab Transaction Role
2. Klik node `IT Infrastructure` di Sidebar Group Tree
3. Klik sub-tab `Disposal`
4. Verifikasi `[+ Assign]` pada section Asset Admin, Monitoring & Report, dan Approver tampil (Show) dalam group yang di-assign beserta descendant (diamati pada node `IT Infrastructure`)
5. Klik `⋯` pada baris Nadia Putri (section Asset Admin)
6. Verifikasi Menu baris memuat `Remove` Enabled untuk target Standard (baris Nadia Putri)
7. Tutup menu baris dengan Esc
8. Verifikasi Toggle `Require Approval for Disposal` dan radio `Any approver (OR)` serta `All approvers (AND)` Enabled

### TC-FA-RP-110: Manage global user & role tanpa Update

9. Ganti akun: logout, lalu login sebagai Manage global user & role tanpa Update (Bayu Prakoso)
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

### TC-FA-RP-111: Manage user & role tanpa Update (Group)

20. Ganti akun: logout, lalu login sebagai Manage user & role tanpa Update (Group, `IT Infrastructure`) (Wulan Sari)
21. Klik Tab Transaction Role
22. Klik node `IT Infrastructure` di Sidebar Group Tree
23. Klik sub-tab `Disposal`
24. Verifikasi `[+ Assign]` pada seluruh section (Asset Admin, Monitoring & Report, Approver) Hidden
25. Verifikasi Aksi `Remove` pada seluruh section Hidden (baris Nadia Putri tampil)
26. Verifikasi Toggle `Require Approval for Disposal` dan radio OR/AND Disabled
27. Hover toggle `Require Approval for Disposal`
28. Verifikasi Toggle `Require Approval for Disposal` Disabled dengan tooltip `Read Only access cannot modify data.`
29. Hover radio `All approvers (AND)`
30. Verifikasi Radio OR/AND Disabled dengan tooltip `Read Only access cannot modify data.`

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-role-permission/TestCases/tc-settings-role-permission.md`.
- Spec Role Matrix (bagian 3a konvensi) ditulis per blok role: langkah tiap role identik tetapi ganti akun menuntut Step eksplisit (akun pertama login di hook `before`), sehingga satu blok per TC. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): klik tab (langkah 1, 10 dan 21); membuka menu baris `⋯` (langkah 5) dan menutupnya dengan Esc (langkah 7); hover untuk membaca tooltip (langkah 16, 18, 27 dan 29).
- Ganti akun eksplisit (logout lalu login) pada langkah 9 dan 20.
- Asersi `Hidden` memakai halaman yang sudah termuat dengan baris target yang tampil (baris Nadia Putri) sebagai anchor permukaan (bagian 8b butir 2).
- Pembagian TC lintas spec: TC-FA-RP-105 sampai TC-FA-RP-108 ada di spec 030.
- Kombinasi role dan aksi yang tidak punya TC sumber tidak ditambahkan.
- Temuan untuk QA:
  - Expected a menyebut `[+ Assign]` "pada seluruh group" atau "dalam cabang ... beserta descendant", sedangkan Langkah Uji hanya memilih node `IT Infrastructure`; spec mengasersi pada node itu saja.
  - Target Standard untuk `Remove` tidak disebut nama; spec memakai Nadia Putri (Asset Admin, seed Pre-setup #19).
  - Tooltip toggle dan radio dibaca pada toggle `Require Approval for Disposal` dan radio `All approvers (AND)`; TC tidak menyebut elemen yang di-hover.
  - `caseType` Negative karena dua dari tiga TC sumber menguji kontrol yang Hidden atau Disabled.
