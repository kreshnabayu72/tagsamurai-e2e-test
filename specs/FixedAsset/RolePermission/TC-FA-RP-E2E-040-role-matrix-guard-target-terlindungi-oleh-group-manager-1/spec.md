---
id: TC-FA-RP-E2E-040-role-matrix-guard-target-terlindungi-oleh-group-manager-1
title: "Role Matrix: guard target terlindungi oleh Group Manager (1/2)"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-FA-RP-139
  - TC-FA-RP-140
  - TC-FA-RP-141
coverage:
  web: automated
---

# Role Matrix: guard target terlindungi oleh Group Manager (1/2)

## Prerequisites

- Mode: FE+BE.
- Login di hook `before` spec ini sebagai Group Manager (Fajar Nugroho); halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Role & Permission, Tab Total Control). Hook `after` mengembalikan sesi ke akun default suite (Total Control, `Spectra.env.FA_TC_PASSWORD`).
- Flag Guided Tooltip `guided_tooltip_seen_fa-settings-role-permission`: diatur hook suite (lihat `suite.md`, Hook suite), termasuk untuk semua akun pada tabel Role yang diuji.
- Sesi API aktor dan pemulihan Pre-setup bersama: lihat `suite.md`, Hook suite (Sesi API aktor; Pre-setup bersama).
- Identitas Pre-setup (nama pengguna, group, role) yang dipakai langkah mengacu ke fixture `Fixture.fixedAssetRolePermission` (fixture baru, belum ada di repo, tanpa password; ditandai untuk tim FE).

Role yang diuji (Tabel Data Uji Pre-setup TC):

| TC | Role | Kelompok | Nama user | Email | Env var password |
|---|---|---|---|---|---|
| TC-FA-RP-139 sampai TC-FA-RP-141 | Group Manager (Fajar Nugroho, `IT Infrastructure`) | Group Manager | Fajar Nugroho (Pre-setup #5) | `groupManager_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_GM_PASSWORD` |

Baris target (parameter langkah berulang):

| TC | Detail Role | Node | Baris | Perilaku | Tooltip |
|---|---|---|---|---|---|
| TC-FA-RP-139 | Group Role `Manage files` | `Data Center` | Rina Wulandari (Total Control) | Disabled | `You don't have permission to edit.` |
| TC-FA-RP-140 | Group Role `Manage files` | `Data Center` | Maya Anggraeni (Read Only) | Disabled | `You don't have permission to edit.` |
| TC-FA-RP-141 | Group Role `Manage files` | `Data Center` | Kevin Susanto (Group Manager di node GM-nya) | Disabled | `You don't have permission to edit.` |

- Data Pre-setup yang dibaca: pool pengguna #15, pohon group #18, target #13 (Kevin Susanto), #12 (Maya Anggraeni), #3 (Rina Wulandari), dan penugasan #33. Spec tidak membuat, mengubah, atau menghapus data; menu baris dibuka lalu ditutup tanpa menjalankan Remove.
- Kemampuan teknis: hover pada elemen Disabled untuk membaca tooltip.
- State global yang diubah: tidak ada.

## Test Steps

1. Klik Tab System
2. Klik Role Name `Manage files` pada section Group Role

### TC-FA-RP-139, TC-FA-RP-140, dan TC-FA-RP-141: baris Group Role Disabled

3. Untuk setiap baris tabel Baris target (langkah 4 sampai 12):
4. Klik node sesuai kolom Node di Sidebar Group Tree
5. Hover checkbox Update pada baris target
6. Verifikasi Checkbox Create, Update, Delete baris target Disabled dengan tooltip sesuai kolom Tooltip (tooltip dibaca pada checkbox Update)
7. Klik `⋯` pada baris target
8. Hover `Remove` pada menu baris
9. Verifikasi Aksi `Remove` Disabled dengan tooltip sesuai kolom Tooltip
10. Tutup menu baris dengan Esc
11. Hover checkbox baris target
12. Verifikasi Checkbox baris (multi-select) Disabled dengan tooltip sesuai kolom Tooltip

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-role-permission/TestCases/tc-settings-role-permission.md`.
- Spec Role Matrix (bagian 3a konvensi) ditulis per blok role: ganti akun menuntut Step eksplisit (akun pertama login di hook `before`). Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): klik tab (langkah 1); membuka menu baris `⋯` (langkah 7) dan menutupnya dengan Esc (langkah 10); hover untuk membaca tooltip (langkah 5, 8 dan 11); mengulang langkah 4 sampai 12 untuk tiap baris target.
- Asersi Disabled dan Enabled hanya diamati pada baris yang tampil di tabel Detail Role; tidak ada asersi absence.
- Pembagian TC lintas spec: TC-FA-RP-142 sampai TC-FA-RP-144 ada di spec 041.
- Kombinasi role dan aksi yang tidak punya TC sumber tidak ditambahkan.
- Temuan untuk QA:
  - Tooltip dibaca pada checkbox Update (mewakili Create, Update, Delete), pada item `Remove` di menu baris, dan pada checkbox baris; TC tidak menyebut elemen mana yang di-hover.
  - TC tidak menyebut halaman tempat baris target berada; spec mengasumsikan baris tampil pada halaman pertama tabel Detail Role.
  - TC-FA-RP-139 sampai TC-FA-RP-141 menyebut "Klik node ... sesuai Data Uji" tanpa nilai node di Data Uji; spec memakai node `Data Center` sesuai baris yang disebut di Langkah Uji.
