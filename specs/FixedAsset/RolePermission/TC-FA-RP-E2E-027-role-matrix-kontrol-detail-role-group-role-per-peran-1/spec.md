---
id: TC-FA-RP-E2E-027-role-matrix-kontrol-detail-role-group-role-per-peran-1
title: "Role Matrix: kontrol Detail Role Group Role per peran (1/3)"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-RP-98
  - TC-FA-RP-99
  - TC-FA-RP-100
coverage:
  web: automated
---

# Role Matrix: kontrol Detail Role Group Role per peran (1/3)

## Prerequisites

- Mode: FE+BE.
- Login di hook `before` spec ini sebagai Total Control (Siti Rahmawati); halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Role & Permission, Tab Total Control). Hook `after` mengembalikan sesi ke akun default suite (Total Control, `Spectra.env.FA_TC_PASSWORD`).
- Flag Guided Tooltip `guided_tooltip_seen_fa-settings-role-permission`: diatur hook suite (lihat `suite.md`, Hook suite), termasuk untuk semua akun pada tabel Role yang diuji.
- Sesi API aktor dan pemulihan Pre-setup bersama: lihat `suite.md`, Hook suite (Sesi API aktor; Pre-setup bersama).
- Identitas Pre-setup (nama pengguna, group, role) yang dipakai langkah mengacu ke fixture `Fixture.fixedAssetRolePermission` (fixture baru, belum ada di repo, tanpa password; ditandai untuk tim FE).

Role yang diuji (Tabel Data Uji Pre-setup TC):

| TC | Role | Kelompok | Nama user | Email | Env var password |
|---|---|---|---|---|---|
| TC-FA-RP-98 | Total Control | Penuh | Siti Rahmawati (Pre-setup #2) | `totalControl_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_TC_PASSWORD` |
| TC-FA-RP-99 | Read Only | Hanya baca | Dewi Anggraini (Pre-setup #4) | `readOnly_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_RO_PASSWORD` |
| TC-FA-RP-100 | Group Manager (Fajar Nugroho, `IT Infrastructure`) | Group Manager | Fajar Nugroho (Pre-setup #5) | `groupManager_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_GM_PASSWORD` |

- Data Pre-setup yang dibaca: pool pengguna Standard #15 (Ahmad Fauzi sebagai target Standard), pohon group #18 (`Data Center` sebagai node uji), dan penugasan #33. Seeding ke kondisi Tabel Data Uji Pre-setup TC dilakukan hook `before`. Spec tidak membuat, mengubah, atau menghapus data; menu baris dibuka lalu ditutup tanpa menjalankan Remove.
- Kemampuan teknis: hover pada elemen Disabled untuk membaca tooltip.
- State global yang diubah: tidak ada.

## Test Steps

### TC-FA-RP-98: Total Control

1. Klik Tab System
2. Klik Role Name `Manage files` pada section Group Role
3. Klik node `Data Center` di Sidebar Group Tree
4. Verifikasi `[+ Assign]` tampil (Show) pada node `Data Center`
5. Klik `⋯` pada baris Ahmad Fauzi
6. Verifikasi Menu baris memuat `Remove` Enabled untuk target Standard (baris Ahmad Fauzi) pada node `Data Center`
7. Tutup menu baris dengan Esc
8. Verifikasi Kolom Checkbox multi-select dan `Bulk Action` tampil
9. Verifikasi Checkbox Create, Update, Delete baris Ahmad Fauzi Enabled untuk target Standard
10. Hover checkbox Read baris Ahmad Fauzi
11. Verifikasi Checkbox Read Disabled dengan tooltip `Read access is required and can only be removed by removing the role.`

### TC-FA-RP-99: Read Only

12. Ganti akun: logout, lalu login sebagai Read Only (Dewi Anggraini)
13. Buka Fixed Asset > Settings > Role & Permission, lalu klik Tab System
14. Klik Role Name `Manage files` pada section Group Role
15. Klik node `Data Center` di Sidebar Group Tree
16. Verifikasi `[+ Assign]` Hidden
17. Verifikasi Aksi `Remove` Hidden pada baris Ahmad Fauzi
18. Verifikasi Kolom Checkbox multi-select dan `Bulk Action` Hidden
19. Verifikasi Checkbox Create, Update, Delete baris Ahmad Fauzi Disabled
20. Hover checkbox Update baris Ahmad Fauzi
21. Verifikasi Checkbox Create, Update, Delete Disabled dengan tooltip `Read Only access cannot modify data.` (tooltip dibaca pada checkbox Update)
22. Hover checkbox Read baris Ahmad Fauzi
23. Verifikasi Checkbox Read Disabled dengan tooltip `Read access is required and can only be removed by removing the role.`

### TC-FA-RP-100: Group Manager

24. Ganti akun: logout, lalu login sebagai Group Manager (Fajar Nugroho, `IT Infrastructure`)
25. Buka Fixed Asset > Settings > Role & Permission, lalu klik Tab System
26. Klik Role Name `Manage files` pada section Group Role
27. Klik node `Data Center` di Sidebar Group Tree
28. Verifikasi `[+ Assign]` tampil (Show) dalam group cabang `IT Infrastructure` beserta descendant (diamati pada node `Data Center`)
29. Klik `⋯` pada baris Ahmad Fauzi
30. Verifikasi Menu baris memuat `Remove` Enabled untuk target Standard (baris Ahmad Fauzi) dalam group cabang `IT Infrastructure` beserta descendant
31. Tutup menu baris dengan Esc
32. Verifikasi Kolom Checkbox multi-select dan `Bulk Action` tampil
33. Verifikasi Checkbox Create, Update, Delete baris Ahmad Fauzi Enabled untuk target Standard
34. Hover checkbox Read baris Ahmad Fauzi
35. Verifikasi Checkbox Read Disabled dengan tooltip `Read access is required and can only be removed by removing the role.`

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-role-permission/TestCases/tc-settings-role-permission.md`.
- Spec Role Matrix (bagian 3a konvensi) ditulis per blok role: langkah tiap role identik tetapi ganti akun menuntut Step eksplisit (akun pertama login di hook `before`), sehingga satu blok per TC. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): klik tab (langkah 1); membuka halaman Role & Permission setelah ganti akun (langkah 13 dan 25); membuka menu baris `⋯` (langkah 5 dan 29) dan menutupnya dengan Esc (langkah 7 dan 31); hover untuk membaca tooltip (langkah 10, 20, 22 dan 34).
- Ganti akun eksplisit (logout lalu login) pada langkah 12 dan 24.
- Asersi `Hidden` memakai halaman yang sudah termuat dengan baris target yang tampil (baris Ahmad Fauzi) sebagai anchor permukaan (bagian 8b butir 2).
- Pembagian TC lintas spec: TC-FA-RP-101 sampai TC-FA-RP-103 ada di spec 028 dan TC-FA-RP-104 di spec 029 (kontrol Detail Role Group Role untuk role lain).
- Kombinasi role dan aksi yang tidak punya TC sumber tidak ditambahkan.
- Temuan untuk QA:
  - TC-FA-RP-100 Expected a dan b menyebut `[+ Assign]` dan `Remove` "dalam group cabang ... beserta descendant", sedangkan Langkah Uji hanya memilih node `Data Center`; spec mengasersi pada node `Data Center` (descendant `IT Infrastructure`) dan tidak membuktikan cakupan seluruh group cabang.
  - Expected d dan e tidak menyebut checkbox mana yang di-hover untuk tooltip; spec membaca tooltip pada checkbox Update (mewakili Create, Update, Delete) dan pada checkbox Read.
  - TC-FA-RP-98 sampai TC-FA-RP-104 tidak menyebut halaman tempat baris Ahmad Fauzi berada; spec mengasumsikan baris itu ada pada halaman pertama node `Data Center` (Pre-setup #39 mencantumkan Ahmad Fauzi di `Data Center`).
