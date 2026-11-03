---
id: TC-FA-RP-E2E-039-role-matrix-guard-target-terlindungi-oleh-manage-global-user-2
title: "Role Matrix: guard target terlindungi oleh Manage global user & role (Update) (2/2)"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-FA-RP-134
  - TC-FA-RP-135
  - TC-FA-RP-136
  - TC-FA-RP-137
  - TC-FA-RP-138
coverage:
  web: automated
---

# Role Matrix: guard target terlindungi oleh Manage global user & role (Update) (2/2)

## Prerequisites

- Mode: FE+BE.
- Login di hook `before` spec ini sebagai Manage global user & role (Update) (Hendra Wijaya); halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Role & Permission, Tab Total Control). Hook `after` mengembalikan sesi ke akun default suite (Total Control, `Spectra.env.FA_TC_PASSWORD`).
- Flag Guided Tooltip `guided_tooltip_seen_fa-settings-role-permission`: diatur hook suite (lihat `suite.md`, Hook suite), termasuk untuk semua akun pada tabel Role yang diuji.
- Sesi API aktor dan pemulihan Pre-setup bersama: lihat `suite.md`, Hook suite (Sesi API aktor; Pre-setup bersama).
- Identitas Pre-setup (nama pengguna, group, role) yang dipakai langkah mengacu ke fixture `Fixture.fixedAssetRolePermission` (fixture baru, belum ada di repo, tanpa password; ditandai untuk tim FE).

Role yang diuji (Tabel Data Uji Pre-setup TC):

| TC | Role | Kelompok | Nama user | Email | Env var password |
|---|---|---|---|---|---|
| TC-FA-RP-134 sampai TC-FA-RP-138 | Manage global user & role (Update) | Manage dengan Update | Hendra Wijaya (Pre-setup #6) | `murGlobal_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_MUR_GLOBAL_PASSWORD` |

Baris target (parameter langkah berulang):

| TC | Detail Role | Node | Baris | Perilaku | Tooltip |
|---|---|---|---|---|---|
| TC-FA-RP-135 | Group Role `Manage files` | `Data Center` | Rina Wulandari (Total Control) | Disabled | `You don't have permission to edit.` |
| TC-FA-RP-136 | Group Role `Manage files` | `Data Center` | Maya Anggraeni (Read Only) | Disabled | `You don't have permission to edit.` |
| TC-FA-RP-137 | Group Role `Manage files` | `Data Center` | Kevin Susanto (Group Manager di node GM-nya) | Disabled | `You don't have permission to edit.` |
| TC-FA-RP-138 | Group Role `Manage files` | `Helpdesk` | Kevin Susanto (Group Manager, node lain) | Enabled | - |

- Data Pre-setup yang dibaca: pool pengguna #15, pohon group #18, target #13 (Kevin Susanto: Group Role `Manage files` CRUD di `Data Center`, Read dan Delete di `Helpdesk`), #12 (Maya Anggraeni), #3 (Rina Wulandari), dan penugasan #33; TC-FA-RP-134 memakai Gita Maharani yang memegang Global Role `Manage accounting` (seed hook `before`). Spec tidak membuat, mengubah, atau menghapus data; menu baris dibuka lalu ditutup tanpa menjalankan Remove.
- Kemampuan teknis: hover pada elemen Disabled untuk membaca tooltip.
- State global yang diubah: tidak ada.

## Test Steps

1. Klik Tab System
2. Klik Role Name `Manage accounting` pada section Global Role

### TC-FA-RP-134: sesama pemegang Manage user & role pada Global Role

3. Verifikasi Checkbox Create, Update, Delete baris Global Role Gita Maharani Enabled
4. Klik `⋯` pada baris Global Role Gita Maharani
5. Verifikasi Aksi `Remove` baris Global Role Gita Maharani Enabled
6. Tutup menu baris dengan Esc
7. Verifikasi Checkbox baris (multi-select) baris Global Role Gita Maharani Enabled

### TC-FA-RP-135, TC-FA-RP-136, dan TC-FA-RP-137: baris Group Role Disabled

8. Klik Tab System
9. Klik Role Name `Manage files` pada section Group Role
10. Untuk setiap baris tabel Baris target dengan Perilaku Disabled (langkah 11 sampai 19):
11. Klik node sesuai kolom Node di Sidebar Group Tree
12. Hover checkbox Update pada baris target
13. Verifikasi Checkbox Create, Update, Delete baris target Disabled dengan tooltip sesuai kolom Tooltip (tooltip dibaca pada checkbox Update)
14. Klik `⋯` pada baris target
15. Hover `Remove` pada menu baris
16. Verifikasi Aksi `Remove` Disabled dengan tooltip sesuai kolom Tooltip
17. Tutup menu baris dengan Esc
18. Hover checkbox baris target
19. Verifikasi Checkbox baris (multi-select) Disabled dengan tooltip sesuai kolom Tooltip

### TC-FA-RP-138: baris Group Manager pada node lain (tidak terkunci)

20. Klik node `Helpdesk` di Sidebar Group Tree
21. Verifikasi Checkbox Create, Update, Delete baris Group Role Kevin Susanto di `Helpdesk` Enabled
22. Klik `⋯` pada baris Group Role Kevin Susanto di `Helpdesk`
23. Verifikasi Aksi `Remove` baris Group Role Kevin Susanto di `Helpdesk` Enabled
24. Tutup menu baris dengan Esc
25. Verifikasi Checkbox baris (multi-select) baris Group Role Kevin Susanto di `Helpdesk` Enabled

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-role-permission/TestCases/tc-settings-role-permission.md`.
- Spec Role Matrix (bagian 3a konvensi) ditulis per blok role: ganti akun menuntut Step eksplisit (akun pertama login di hook `before`). Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): klik tab (langkah 1 dan 8); membuka menu baris `⋯` (langkah 4, 14 dan 22) dan menutupnya dengan Esc (langkah 6, 17 dan 24); hover untuk membaca tooltip (langkah 12, 15 dan 18); mengulang langkah 11 sampai 19 untuk tiap baris Disabled, kembali ke Tab System lalu membuka Detail Role `Manage files` (langkah 8).
- Asersi Disabled dan Enabled hanya diamati pada baris yang tampil di tabel Detail Role; tidak ada asersi absence.
- Pembagian TC lintas spec: TC-FA-RP-129 sampai TC-FA-RP-133 ada di spec 038; urutan TC pada spec ini mengelompokkan baris Disabled (TC-FA-RP-135 sampai TC-FA-RP-137) dalam satu langkah berulang.
- Spec melewati sekitar 35 langkah dengan ekspansi (43 langkah; 25 langkah nominal). Semua blok satu kelas harness (Role Matrix guard, baca saja) dan berdiri sendiri: tiap baris target diuji dengan langkah yang sama dan kegagalan satu baris tidak membuat baris lain kehilangan makna; langkah berulang memakai tabel Baris target di Prerequisites (bagian 8b butir 7).
- Kombinasi role dan aksi yang tidak punya TC sumber tidak ditambahkan.
- Temuan untuk QA:
  - Tooltip dibaca pada checkbox Update (mewakili Create, Update, Delete), pada item `Remove` di menu baris, dan pada checkbox baris; TC tidak menyebut elemen mana yang di-hover.
  - TC tidak menyebut halaman tempat baris target berada; spec mengasumsikan baris tampil pada halaman pertama tabel Detail Role.
  - TC-FA-RP-135 sampai TC-FA-RP-137 menyebut "Klik node pada Sidebar Group Tree sesuai Data Uji" dan Data Uji hanya menyebut baris di `Data Center`; spec mengklik node `Data Center` untuk ketiga baris dan `Helpdesk` untuk TC-FA-RP-138.
  - TC-FA-RP-134 Precondition d menyebut Gita Maharani memegang `Manage accounting`; Pre-setup #7 tidak menyebut Global Role itu, sehingga seed dilakukan hook `before`.
