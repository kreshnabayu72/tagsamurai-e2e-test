---
id: TC-FA-RP-E2E-045-role-matrix-guard-target-terlindungi-oleh-total-control-dan-2
title: "Role Matrix: guard target terlindungi oleh Total Control dan Default User (2/2)"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-FA-RP-156
  - TC-FA-RP-157
  - TC-FA-RP-158
  - TC-FA-RP-159
coverage:
  web: automated
---

# Role Matrix: guard target terlindungi oleh Total Control dan Default User (2/2)

## Prerequisites

- Mode: FE+BE.
- Login di hook `before` spec ini sebagai Total Control (Siti Rahmawati); halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Role & Permission, Tab Total Control). Hook `after` mengembalikan sesi ke akun default suite (Total Control, `Spectra.env.FA_TC_PASSWORD`).
- Flag Guided Tooltip `guided_tooltip_seen_fa-settings-role-permission`: diatur hook suite (lihat `suite.md`, Hook suite), termasuk untuk semua akun pada tabel Role yang diuji.
- Sesi API aktor dan pemulihan Pre-setup bersama: lihat `suite.md`, Hook suite (Sesi API aktor; Pre-setup bersama).
- Identitas Pre-setup (nama pengguna, group, role) yang dipakai langkah mengacu ke fixture `Fixture.fixedAssetRolePermission` (fixture baru, belum ada di repo, tanpa password; ditandai untuk tim FE).

Role yang diuji (Tabel Data Uji Pre-setup TC):

| TC | Role | Kelompok | Nama user | Email | Env var password |
|---|---|---|---|---|---|
| TC-FA-RP-156 | Total Control | Penuh | Siti Rahmawati (Pre-setup #2) | `totalControl_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_TC_PASSWORD` |
| TC-FA-RP-157, TC-FA-RP-158, TC-FA-RP-159 | Default User | Penuh | Admin Utama (Pre-setup #1) | `defaultUser_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_DU_PASSWORD` |

Baris target (parameter langkah berulang):

| TC | Detail Role | Baris | Perilaku | Tooltip |
|---|---|---|---|---|
| TC-FA-RP-156 | Global Role `Manage accounting` | Ahmad Fauzi (Standard), aktor Total Control | Enabled | - |
| TC-FA-RP-157 | Global Role `Manage accounting` | Admin Utama (diri sendiri sebagai Default User) | Disabled | `Default User cannot be modified.` |
| TC-FA-RP-158 | Global Role `Manage accounting` | Rina Wulandari (Total Control), aktor Default User | Enabled | - |
| TC-FA-RP-159 | Global Role `Manage accounting` | Ahmad Fauzi (Standard), aktor Default User | Enabled | - |

- Data Pre-setup yang dibaca: pool pengguna #15 (Ahmad Fauzi), pohon group #18, target #13, #12, #3, dan penugasan #33. Spec tidak membuat, mengubah, atau menghapus data; menu baris dibuka lalu ditutup tanpa menjalankan Remove.
- Kemampuan teknis: hover pada elemen Disabled untuk membaca tooltip.
- State global yang diubah: tidak ada. Hook `after` mengembalikan sesi dari Default User ke akun default suite (Total Control).

## Test Steps

1. Klik Tab System
2. Klik Role Name `Manage accounting` pada section Global Role

### TC-FA-RP-156: Total Control atas target Standard

3. Verifikasi Checkbox Create, Update, Delete baris Ahmad Fauzi (Standard) Enabled
4. Klik `⋯` pada baris Ahmad Fauzi (Standard)
5. Verifikasi Aksi `Remove` baris Ahmad Fauzi (Standard) Enabled
6. Tutup menu baris dengan Esc
7. Verifikasi Checkbox baris (multi-select) baris Ahmad Fauzi (Standard) Enabled

### TC-FA-RP-157: Default User atas diri sendiri

8. Ganti akun: logout, lalu login sebagai Default User (Admin Utama)
9. Buka Fixed Asset > Settings > Role & Permission, lalu klik Tab System
10. Klik Role Name `Manage accounting` pada section Global Role
11. Hover checkbox Update pada baris Admin Utama (diri sendiri sebagai Default User)
12. Verifikasi Checkbox Create, Update, Delete baris Admin Utama (diri sendiri sebagai Default User) Disabled dengan tooltip `Default User cannot be modified.` (tooltip dibaca pada checkbox Update)
13. Klik `⋯` pada baris Admin Utama (diri sendiri sebagai Default User)
14. Hover `Remove` pada menu baris
15. Verifikasi Aksi `Remove` baris Admin Utama (diri sendiri sebagai Default User) Disabled dengan tooltip `Default User cannot be modified.`
16. Tutup menu baris dengan Esc
17. Hover checkbox baris Admin Utama (diri sendiri sebagai Default User)
18. Verifikasi Checkbox baris (multi-select) baris Admin Utama (diri sendiri sebagai Default User) Disabled dengan tooltip `Default User cannot be modified.`

### TC-FA-RP-158 dan TC-FA-RP-159: Default User atas target Total Control dan Standard

19. Untuk setiap baris tabel Baris target dengan Perilaku Enabled (langkah 20 sampai 24):
20. Verifikasi Checkbox Create, Update, Delete baris target Enabled
21. Klik `⋯` pada baris target
22. Verifikasi Aksi `Remove` baris target Enabled
23. Tutup menu baris dengan Esc
24. Verifikasi Checkbox baris (multi-select) baris target Enabled

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-role-permission/TestCases/tc-settings-role-permission.md`.
- Spec Role Matrix (bagian 3a konvensi) ditulis per blok role: ganti akun menuntut Step eksplisit (akun pertama login di hook `before`). Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): klik tab (langkah 1); membuka halaman Role & Permission setelah ganti akun (langkah 9); membuka menu baris `⋯` (langkah 4, 13 dan 21) dan menutupnya dengan Esc (langkah 6, 16 dan 23); hover untuk membaca tooltip (langkah 11, 14 dan 17); mengulang langkah 20 sampai 24 untuk baris Enabled aktor Default User.
- Ganti akun eksplisit (logout lalu login) pada langkah 8.
- Asersi Disabled dan Enabled hanya diamati pada baris yang tampil di tabel Detail Role; tidak ada asersi absence.
- Pembagian TC lintas spec: TC-FA-RP-151 sampai TC-FA-RP-155 ada di spec 044.
- Kombinasi role dan aksi yang tidak punya TC sumber tidak ditambahkan.
- Temuan untuk QA:
  - Tooltip dibaca pada checkbox Update (mewakili Create, Update, Delete), pada item `Remove` di menu baris, dan pada checkbox baris; TC tidak menyebut elemen mana yang di-hover.
  - TC tidak menyebut halaman tempat baris target berada; spec mengasumsikan baris tampil pada halaman pertama tabel Detail Role.
  - TC-FA-RP-157 sampai TC-FA-RP-159 menyebut Default User tetapi Pre-setup #1 memberi nama akun Admin Utama; spec memakai Admin Utama sebagai baris diri sendiri.
  - TC-FA-RP-157 sampai TC-FA-RP-159 mencantumkan Total Control sebagai tingkat akses Default User permanen; spec mengikuti Langkah Uji dan tidak menambah asersi.
