---
id: TC-FA-RP-E2E-041-role-matrix-guard-target-terlindungi-oleh-group-manager-2
title: "Role Matrix: guard target terlindungi oleh Group Manager (2/2)"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-FA-RP-142
  - TC-FA-RP-143
  - TC-FA-RP-144
coverage:
  web: automated
---

# Role Matrix: guard target terlindungi oleh Group Manager (2/2)

## Prerequisites

- Mode: FE+BE.
- Login di hook `before` spec ini sebagai Group Manager (Fajar Nugroho); halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Role & Permission, Tab Total Control). Hook `after` mengembalikan sesi ke akun default suite (Total Control, `Spectra.env.FA_TC_PASSWORD`).
- Flag Guided Tooltip `guided_tooltip_seen_fa-settings-role-permission`: diatur hook suite (lihat `suite.md`, Hook suite), termasuk untuk semua akun pada tabel Role yang diuji.
- Sesi API aktor dan pemulihan Pre-setup bersama: lihat `suite.md`, Hook suite (Sesi API aktor; Pre-setup bersama).
- Identitas Pre-setup (nama pengguna, group, role) yang dipakai langkah mengacu ke fixture `Fixture.fixedAssetRolePermission` (fixture baru, belum ada di repo, tanpa password; ditandai untuk tim FE).

Role yang diuji (Tabel Data Uji Pre-setup TC):

| TC | Role | Kelompok | Nama user | Email | Env var password |
|---|---|---|---|---|---|
| TC-FA-RP-142 sampai TC-FA-RP-144 | Group Manager (Fajar Nugroho, `IT Infrastructure`) | Group Manager | Fajar Nugroho (Pre-setup #5) | `groupManager_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_GM_PASSWORD` |

- Data Pre-setup yang dibaca: pool pengguna #15, pohon group #18, target #13 (Kevin Susanto: Group Role `Manage files` Read dan Delete di `Helpdesk`), #12, #3, dan penugasan #33; Precondition d TC-FA-RP-144: Gita Maharani (Pre-setup #7) memegang Group Role `Manage files` di `IT Infrastructure` (seed hook `before`). Spec tidak membuat, mengubah, atau menghapus data; menu baris dibuka lalu ditutup tanpa menjalankan Remove.
- Kemampuan teknis: hover pada elemen Disabled untuk membaca tooltip.
- State global yang diubah: tidak ada.

## Test Steps

1. Klik Tab System
2. Klik Role Name `Manage files` pada section Group Role

### TC-FA-RP-143: diri sendiri pada node `IT Infrastructure`

3. Klik node `IT Infrastructure` di Sidebar Group Tree
4. Hover checkbox Update pada baris milik aktor (Fajar Nugroho) di `IT Infrastructure`
5. Verifikasi Checkbox Create, Update, Delete baris milik aktor (Fajar Nugroho) di `IT Infrastructure` Disabled dengan tooltip `You can't manage your own account from here.` (tooltip dibaca pada checkbox Update)
6. Klik `⋯` pada baris milik aktor (Fajar Nugroho) di `IT Infrastructure`
7. Hover `Remove` pada menu baris
8. Verifikasi Aksi `Remove` baris milik aktor (Fajar Nugroho) di `IT Infrastructure` Disabled dengan tooltip `You can't manage your own account from here.`
9. Tutup menu baris dengan Esc
10. Hover checkbox baris milik aktor (Fajar Nugroho) di `IT Infrastructure`
11. Verifikasi Checkbox baris (multi-select) baris milik aktor (Fajar Nugroho) di `IT Infrastructure` Disabled dengan tooltip `You can't manage your own account from here.`

### TC-FA-RP-144: sesama pemegang Manage user & role pada node `IT Infrastructure`

12. Verifikasi Checkbox Create, Update, Delete baris Gita Maharani pada `Manage files` di `IT Infrastructure` Enabled
13. Klik `⋯` pada baris Gita Maharani pada `Manage files` di `IT Infrastructure`
14. Verifikasi Aksi `Remove` baris Gita Maharani pada `Manage files` di `IT Infrastructure` Enabled
15. Tutup menu baris dengan Esc
16. Verifikasi Checkbox baris (multi-select) baris Gita Maharani pada `Manage files` di `IT Infrastructure` Enabled

### TC-FA-RP-142: baris Group Manager pada node lain (tidak terkunci)

17. Klik node `Helpdesk` di Sidebar Group Tree
18. Verifikasi Checkbox Create, Update, Delete baris Kevin Susanto di `Helpdesk` Enabled
19. Klik `⋯` pada baris Kevin Susanto di `Helpdesk`
20. Verifikasi Aksi `Remove` baris Kevin Susanto di `Helpdesk` Enabled
21. Tutup menu baris dengan Esc
22. Verifikasi Checkbox baris (multi-select) baris Kevin Susanto di `Helpdesk` Enabled

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-role-permission/TestCases/tc-settings-role-permission.md`.
- Spec Role Matrix (bagian 3a konvensi) ditulis per blok role: ganti akun menuntut Step eksplisit (akun pertama login di hook `before`). Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): klik tab (langkah 1); membuka menu baris `⋯` (langkah 6, 13 dan 19) dan menutupnya dengan Esc (langkah 9, 15 dan 21); hover untuk membaca tooltip (langkah 4, 7 dan 10).
- Asersi Disabled dan Enabled hanya diamati pada baris yang tampil di tabel Detail Role; tidak ada asersi absence.
- Pembagian TC lintas spec: TC-FA-RP-139 sampai TC-FA-RP-141 ada di spec 040; urutan TC pada spec ini mengikuti node (`IT Infrastructure` lebih dulu, `Helpdesk` sesudahnya): TC-FA-RP-143, TC-FA-RP-144, lalu TC-FA-RP-142.
- Kombinasi role dan aksi yang tidak punya TC sumber tidak ditambahkan.
- Temuan untuk QA:
  - Tooltip dibaca pada checkbox Update (mewakili Create, Update, Delete), pada item `Remove` di menu baris, dan pada checkbox baris; TC tidak menyebut elemen mana yang di-hover.
  - TC tidak menyebut halaman tempat baris target berada; spec mengasumsikan baris tampil pada halaman pertama tabel Detail Role.
  - TC-FA-RP-143 menyebut "baris milik aktor di `IT Infrastructure`" pada `Manage files` tanpa Precondition yang menyatakan Fajar Nugroho memegang `Manage files` di sana; spec mengasumsikan baris eksplisit CRUD penuh Pre-setup #5 mencakup `Manage files`.
