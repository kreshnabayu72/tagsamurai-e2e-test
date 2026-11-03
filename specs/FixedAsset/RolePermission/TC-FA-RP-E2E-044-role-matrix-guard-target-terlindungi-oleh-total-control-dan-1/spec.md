---
id: TC-FA-RP-E2E-044-role-matrix-guard-target-terlindungi-oleh-total-control-dan-1
title: "Role Matrix: guard target terlindungi oleh Total Control dan Default User (1/2)"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-FA-RP-151
  - TC-FA-RP-152
  - TC-FA-RP-153
  - TC-FA-RP-154
  - TC-FA-RP-155
coverage:
  web: automated
---

# Role Matrix: guard target terlindungi oleh Total Control dan Default User (1/2)

## Prerequisites

- Mode: FE+BE.
- Login di hook `before` spec ini sebagai Total Control (Siti Rahmawati); halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Role & Permission, Tab Total Control). Hook `after` mengembalikan sesi ke akun default suite (Total Control, `Spectra.env.FA_TC_PASSWORD`).
- Flag Guided Tooltip `guided_tooltip_seen_fa-settings-role-permission`: diatur hook suite (lihat `suite.md`, Hook suite), termasuk untuk semua akun pada tabel Role yang diuji.
- Sesi API aktor dan pemulihan Pre-setup bersama: lihat `suite.md`, Hook suite (Sesi API aktor; Pre-setup bersama).
- Identitas Pre-setup (nama pengguna, group, role) yang dipakai langkah mengacu ke fixture `Fixture.fixedAssetRolePermission` (fixture baru, belum ada di repo, tanpa password; ditandai untuk tim FE).

Role yang diuji (Tabel Data Uji Pre-setup TC):

| TC | Role | Kelompok | Nama user | Email | Env var password |
|---|---|---|---|---|---|
| TC-FA-RP-151 sampai TC-FA-RP-155 | Total Control | Penuh | Siti Rahmawati (Pre-setup #2) | `totalControl_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_TC_PASSWORD` |

Baris target (parameter langkah berulang):

| TC | Detail Role | Baris | Perilaku | Tooltip |
|---|---|---|---|---|
| TC-FA-RP-151 | Global Role `Manage accounting` | Admin Utama (Default User) | Disabled | `Default User cannot be modified.` |
| TC-FA-RP-152 | Global Role `Manage accounting` | Siti Rahmawati (diri sendiri) | Disabled | `You can't manage your own account from here.` |
| TC-FA-RP-153 | Global Role `Manage accounting` | Rina Wulandari (Total Control lain) | Enabled | - |
| TC-FA-RP-154 | Global Role `Manage accounting` | Maya Anggraeni (Read Only) | Enabled | - |
| TC-FA-RP-155 | Group Role `Manage files` pada node `Data Center` | Kevin Susanto (Group Manager di node GM-nya) | Enabled | - |

- Data Pre-setup yang dibaca: pool pengguna #15, pohon group #18, target #13 (Kevin Susanto), #12 (Maya Anggraeni), #3 (Rina Wulandari), dan penugasan #33. Spec tidak membuat, mengubah, atau menghapus data; menu baris dibuka lalu ditutup tanpa menjalankan Remove.
- Kemampuan teknis: hover pada elemen Disabled untuk membaca tooltip.
- State global yang diubah: tidak ada.

## Test Steps

1. Klik Tab System
2. Klik Role Name `Manage accounting` pada section Global Role

### TC-FA-RP-151 dan TC-FA-RP-152: baris Disabled (Default User dan diri sendiri)

3. Untuk setiap baris tabel Baris target dengan Perilaku Disabled (langkah 4 sampai 11):
4. Hover checkbox Update pada baris target
5. Verifikasi Checkbox Create, Update, Delete baris target Disabled dengan tooltip sesuai kolom Tooltip (tooltip dibaca pada checkbox Update)
6. Klik `⋯` pada baris target
7. Hover `Remove` pada menu baris
8. Verifikasi Aksi `Remove` Disabled dengan tooltip sesuai kolom Tooltip
9. Tutup menu baris dengan Esc
10. Hover checkbox baris target
11. Verifikasi Checkbox baris (multi-select) Disabled dengan tooltip sesuai kolom Tooltip

### TC-FA-RP-153 dan TC-FA-RP-154: baris Enabled (Total Control lain dan Read Only)

12. Untuk setiap baris tabel Baris target dengan Perilaku Enabled (langkah 13 sampai 17):
13. Verifikasi Checkbox Create, Update, Delete baris target Enabled
14. Klik `⋯` pada baris target
15. Verifikasi Aksi `Remove` baris target Enabled
16. Tutup menu baris dengan Esc
17. Verifikasi Checkbox baris (multi-select) baris target Enabled

### TC-FA-RP-155: baris Group Manager pada Group Role di node GM-nya

18. Klik Tab System
19. Klik Role Name `Manage files` pada section Group Role
20. Klik node `Data Center` di Sidebar Group Tree
21. Verifikasi Checkbox Create, Update, Delete baris Kevin Susanto di `Data Center` Enabled
22. Klik `⋯` pada baris Kevin Susanto di `Data Center`
23. Verifikasi Aksi `Remove` baris Kevin Susanto di `Data Center` Enabled
24. Tutup menu baris dengan Esc
25. Verifikasi Checkbox baris (multi-select) baris Kevin Susanto di `Data Center` Enabled

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-role-permission/TestCases/tc-settings-role-permission.md`.
- Spec Role Matrix (bagian 3a konvensi) ditulis per blok role: ganti akun menuntut Step eksplisit (akun pertama login di hook `before`). Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): klik tab (langkah 1 dan 18); membuka menu baris `⋯` (langkah 6, 14 dan 22) dan menutupnya dengan Esc (langkah 9, 16 dan 24); hover untuk membaca tooltip (langkah 4, 7 dan 10); mengulang langkah 4 sampai 11 (baris Disabled) dan langkah 13 sampai 17 (baris Enabled), serta kembali ke Tab System untuk membuka Detail Role Group Role (langkah 18).
- Asersi Disabled dan Enabled hanya diamati pada baris yang tampil di tabel Detail Role; tidak ada asersi absence.
- Pembagian TC lintas spec: TC-FA-RP-156 sampai TC-FA-RP-159 ada di spec 045; urutan TC pada spec ini mengelompokkan baris Disabled lebih dulu lalu baris Enabled supaya langkah berulang tidak bersyarat.
- Spec melewati sekitar 35 langkah dengan ekspansi (38 langkah; 25 langkah nominal). Semua blok satu kelas harness (Role Matrix guard, baca saja) dan berdiri sendiri: tiap baris target diuji dengan langkah yang sama dan kegagalan satu baris tidak membuat baris lain kehilangan makna; langkah berulang memakai tabel Baris target di Prerequisites (bagian 8b butir 7).
- Kombinasi role dan aksi yang tidak punya TC sumber tidak ditambahkan.
- Temuan untuk QA:
  - Tooltip dibaca pada checkbox Update (mewakili Create, Update, Delete), pada item `Remove` di menu baris, dan pada checkbox baris; TC tidak menyebut elemen mana yang di-hover.
  - TC tidak menyebut halaman tempat baris target berada; spec mengasumsikan baris tampil pada halaman pertama tabel Detail Role.
  - TC-FA-RP-151 sampai TC-FA-RP-154 tidak menyebut bahwa Admin Utama, Siti Rahmawati, Rina Wulandari, dan Maya Anggraeni memegang `Manage accounting`; spec mengasumsikan baris itu tampil.
