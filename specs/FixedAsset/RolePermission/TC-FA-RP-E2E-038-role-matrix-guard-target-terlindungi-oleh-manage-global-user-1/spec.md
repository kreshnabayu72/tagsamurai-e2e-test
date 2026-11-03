---
id: TC-FA-RP-E2E-038-role-matrix-guard-target-terlindungi-oleh-manage-global-user-1
title: "Role Matrix: guard target terlindungi oleh Manage global user & role (Update) (1/2)"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-FA-RP-129
  - TC-FA-RP-130
  - TC-FA-RP-131
  - TC-FA-RP-132
  - TC-FA-RP-133
coverage:
  web: automated
---

# Role Matrix: guard target terlindungi oleh Manage global user & role (Update) (1/2)

## Prerequisites

- Mode: FE+BE.
- Login di hook `before` spec ini sebagai Manage global user & role (Update) (Hendra Wijaya); halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Role & Permission, Tab Total Control). Hook `after` mengembalikan sesi ke akun default suite (Total Control, `Spectra.env.FA_TC_PASSWORD`).
- Flag Guided Tooltip `guided_tooltip_seen_fa-settings-role-permission`: diatur hook suite (lihat `suite.md`, Hook suite), termasuk untuk semua akun pada tabel Role yang diuji.
- Sesi API aktor dan pemulihan Pre-setup bersama: lihat `suite.md`, Hook suite (Sesi API aktor; Pre-setup bersama).
- Identitas Pre-setup (nama pengguna, group, role) yang dipakai langkah mengacu ke fixture `Fixture.fixedAssetRolePermission` (fixture baru, belum ada di repo, tanpa password; ditandai untuk tim FE).

Role yang diuji (Tabel Data Uji Pre-setup TC):

| TC | Role | Kelompok | Nama user | Email | Env var password |
|---|---|---|---|---|---|
| TC-FA-RP-129 sampai TC-FA-RP-133 | Manage global user & role (Update) | Manage dengan Update | Hendra Wijaya (Pre-setup #6) | `murGlobal_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_MUR_GLOBAL_PASSWORD` |

Baris target (parameter langkah berulang):

| TC | Detail Role | Baris | Perilaku | Tooltip |
|---|---|---|---|---|
| TC-FA-RP-129 | Global Role `Manage accounting` | Rina Wulandari (Total Control) | Disabled | `You don't have permission to edit.` |
| TC-FA-RP-130 | Global Role `Manage accounting` | Maya Anggraeni (Read Only) | Disabled | `You don't have permission to edit.` |
| TC-FA-RP-132 | Global Role `Manage accounting` | Admin Utama (Default User) | Disabled | `Default User cannot be modified.` |
| TC-FA-RP-133 | Global Role `Manage accounting` | Hendra Wijaya (diri sendiri) | Disabled | `You can't manage your own account from here.` |
| TC-FA-RP-131 | Global Role `Manage accounting` | Kevin Susanto (Group Manager) | Enabled | - |

- Data Pre-setup yang dibaca: pool pengguna #15, pohon group #18, target #13 (Kevin Susanto), #12 (Maya Anggraeni), #3 (Rina Wulandari), dan penugasan #33; Precondition d TC-FA-RP-131 dan TC-FA-RP-133: Gita Maharani, Hendra Wijaya, dan Kevin Susanto memegang Global Role `Manage accounting` (seed hook `before`). Spec tidak membuat, mengubah, atau menghapus data; menu baris dibuka lalu ditutup tanpa menjalankan Remove.
- Kemampuan teknis: hover pada elemen Disabled untuk membaca tooltip.
- State global yang diubah: tidak ada.

## Test Steps

1. Klik Tab System
2. Klik Role Name `Manage accounting` pada section Global Role

### TC-FA-RP-129, TC-FA-RP-130, TC-FA-RP-132, dan TC-FA-RP-133: baris Disabled

3. Untuk setiap baris tabel Baris target dengan Perilaku Disabled (langkah 4 sampai 11):
4. Hover checkbox Update pada baris target
5. Verifikasi Checkbox Create, Update, Delete baris target Disabled dengan tooltip sesuai kolom Tooltip (tooltip dibaca pada checkbox Update)
6. Klik `⋯` pada baris target
7. Hover `Remove` pada menu baris
8. Verifikasi Aksi `Remove` Disabled dengan tooltip sesuai kolom Tooltip
9. Tutup menu baris dengan Esc
10. Hover checkbox baris target
11. Verifikasi Checkbox baris (multi-select) Disabled dengan tooltip sesuai kolom Tooltip

### TC-FA-RP-131: baris Group Manager pada Global Role (tidak terkunci)

12. Verifikasi Checkbox Create, Update, Delete baris Global Role Kevin Susanto Enabled
13. Klik `⋯` pada baris Global Role Kevin Susanto
14. Verifikasi Aksi `Remove` baris Global Role Kevin Susanto Enabled
15. Tutup menu baris dengan Esc
16. Verifikasi Checkbox baris (multi-select) baris Global Role Kevin Susanto Enabled

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-role-permission/TestCases/tc-settings-role-permission.md`.
- Spec Role Matrix (bagian 3a konvensi) ditulis per blok role: ganti akun menuntut Step eksplisit (akun pertama login di hook `before`). Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): klik tab (langkah 1); membuka menu baris `⋯` (langkah 6 dan 13) dan menutupnya dengan Esc (langkah 9 dan 15); hover untuk membaca tooltip (langkah 4, 7 dan 10); mengulang langkah 4 sampai 11 untuk tiap baris Disabled, dengan pembukaan Detail Role lewat Role Name sebagai langkah TC.
- Asersi Disabled dan Enabled hanya diamati pada baris yang tampil di tabel Detail Role; tidak ada asersi absence.
- Pembagian TC lintas spec: TC-FA-RP-134 sampai TC-FA-RP-138 ada di spec 039; urutan TC pada spec ini mengelompokkan baris Disabled (TC-FA-RP-129, TC-FA-RP-130, TC-FA-RP-132, TC-FA-RP-133) sebelum baris Enabled (TC-FA-RP-131) supaya langkah berulang tidak bersyarat.
- Spec melewati sekitar 35 langkah dengan ekspansi (40 langkah; 16 langkah nominal). Semua blok satu kelas harness (Role Matrix guard, baca saja) dan berdiri sendiri: tiap baris target diuji dengan langkah yang sama dan kegagalan satu baris tidak membuat baris lain kehilangan makna; langkah berulang memakai tabel Baris target di Prerequisites (bagian 8b butir 7).
- Kombinasi role dan aksi yang tidak punya TC sumber tidak ditambahkan.
- Temuan untuk QA:
  - Tooltip dibaca pada checkbox Update (mewakili Create, Update, Delete), pada item `Remove` di menu baris, dan pada checkbox baris; TC tidak menyebut elemen mana yang di-hover.
  - TC tidak menyebut halaman tempat baris target berada; spec mengasumsikan baris tampil pada halaman pertama tabel Detail Role.
  - TC-FA-RP-129, TC-FA-RP-130, dan TC-FA-RP-132 tidak menyebut bahwa Rina Wulandari, Maya Anggraeni, dan Admin Utama memegang `Manage accounting`; spec mengasumsikan baris itu tampil (Pre-setup #3 dan #12 memuat Global Role, Default User Total Control permanen).
