---
id: TC-FA-RP-E2E-263-multi-konteks-notifikasi-in-app-ke-akun-target-2
title: "Multi-konteks: notifikasi in-app ke akun target (2/3)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-RP-880
  - TC-FA-RP-881
  - TC-FA-RP-882
  - TC-FA-RP-883
  - TC-FA-RP-884
coverage:
  web: automated
---

# Multi-konteks: notifikasi in-app ke akun target (2/3)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #2, Siti Rahmawati), email `totalControl_automated_{namaCompany}@qwertysystem.net` (`Fixture.fixedAssetRolePermission.akun.totalControl.email`), password `Spectra.env.FA_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Role & Permission, Tab Total Control). Hook `after` mengembalikan sesi ke akun default suite (Total Control, `FA_TC_PASSWORD`).
- Data Pre-setup: #13 dan #18 (Kevin Susanto: Group Manager di `Data Center` dengan Group Role eksplisit `Manage group`), #3 (Rina Wulandari, Total Control kedua), #12 (Maya Anggraeni: Read Only), dan #15 (Ahmad Fauzi, Budi Santoso, dan Dimas Pranata sebagai Standard untuk TC-FA-RP-884).
- Sesi UI kedua: konteks browser terpisah yang login sebagai akun target dan menjadi objek asersi notifikasi (P-2 tidak berlaku karena sesi kedua adalah objek asersi, bukan pemicu); ditutup di akhir tiap blok TC (S-09). Akun login target (Ahmad Fauzi, Maya Anggraeni, Kevin Susanto, Rina Wulandari, Budi Santoso, Dimas Pranata, Gunawan Halim sesuai TC) tidak tertulis di Pre-setup TC; email dan password disediakan tim FE (lihat Temuan untuk QA).
- Kemampuan teknis: membaca jumlah notifikasi in-app akun target sebelum aksi (baseline TC-FA-RP-884, S-12) disediakan tim FE/BE; tanpa endpoint karangan.
- Format [Date] pada Body notifikasi mengikuti General Settings (Pre-setup #34, Date Format); nilai [Date] adalah tanggal aksi pemicu.
- Notifikasi: pola Title dan Body mengikuti TC (katalog notifikasi `fixed-asset/notification/PRD/notification.md §5.1f` dirujuk TC). Overlay Notifikasi dibuka dari lonceng navbar.
- Flag Guided Tooltip, halaman awal, sesi API aktor, dan pemulihan Pre-setup bersama: lihat `suite.md` bagian "Hook suite".
- Data Pre-setup dirujuk lewat fixture `Fixture.fixedAssetRolePermission` (berkas `fixtures/fixedAssetRolePermission.json`, belum ada; disediakan tim FE). Email data pengguna berformat `[namalengkaptanpaspasi]@qwertysystem.net`.
- Seeding dan pemulihan: kondisi Precondition tiap TC (tingkat akses, penugasan, group, status pengguna) dibuat lewat seeding API (kemampuan disediakan tim FE/BE, tanpa endpoint karangan) di hook `before` dan sebagai langkah penghubung antar blok TC; Pre-setup yang diubah dipulihkan ke Tabel Data Uji Pre-setup TC di hook `after` (Catatan TC "Pemulihan fixture destruktif"). Spec tidak membuat data Dinamis. Suite berjalan serial (`parallel: false`).
- Env var yang dipakai: `FA_TC_PASSWORD`. Didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example` (nama dan arti di `suite.md` bagian "Env password akun aktor"). Password tidak ditulis di spec atau fixture.

## Test Steps

### TC-FA-RP-880: Notifikasi in-app ke target: Auto-Revert Group Manager pemicu Edit CRUD

1. Buka Tab System, lalu Detail Role `Manage group` dan pilih node `Data Center`
2. Hapus centang Delete pada baris Kevin Susanto lalu klik `[Remove]` pada dialog
3. Tunggu aksi selesai: perubahan tersimpan
4. Buka sesi UI kedua, login sebagai Kevin Susanto, lalu buka Overlay Notifikasi lonceng navbar
5. Verifikasi notifikasi baru Title `You are no longer Group Manager for Data Center` dengan Body `Siti Rahmawati removed your Group Manager status for Data Center on [Date].` tampil, [Date] terformat sesuai General Settings
6. Verifikasi Action tier view-only: hanya tombol `[Mark as Read]` tanpa tombol navigasi atau CTA lain
7. Verifikasi Body mengikuti pola katalog `[Admin Name] removed your Group Manager status for [Group Name] on [Date].`
8. Tutup sesi UI kedua

### TC-FA-RP-881: Notifikasi in-app ke target: Auto-Revert Total Control pemicu Remove baris peran

9. Buka Tab System, lalu Detail Role `Manage Open API`
10. Klik `[⋯]` baris Rina Wulandari lalu `Remove`, klik `[Remove]`
11. Tunggu aksi selesai: dialog tertutup
12. Buka sesi UI kedua, login sebagai Rina Wulandari, lalu buka Overlay Notifikasi lonceng navbar
13. Verifikasi notifikasi baru Title `Your Total Control access was removed` dengan Body `Siti Rahmawati removed your Total Control access on [Date].` tampil, [Date] terformat sesuai General Settings
14. Verifikasi Action tier view-only: hanya tombol `[Mark as Read]` tanpa tombol navigasi atau CTA lain
15. Verifikasi Body mengikuti pola katalog `[Admin Name] removed your Total Control access on [Date].`
16. Tutup sesi UI kedua

### TC-FA-RP-882: Notifikasi in-app ke target: Auto-Revert Read Only pemicu Remove baris peran

17. Buka Tab System, lalu Detail Role `Manage Open API`
18. Klik `[⋯]` baris Maya Anggraeni lalu `Remove`, klik `[Remove]`
19. Tunggu aksi selesai: dialog tertutup
20. Buka sesi UI kedua, login sebagai Maya Anggraeni, lalu buka Overlay Notifikasi lonceng navbar
21. Verifikasi notifikasi baru Title `Your Read Only access was removed` dengan Body `Siti Rahmawati removed your Read Only access on [Date].` tampil, [Date] terformat sesuai General Settings
22. Verifikasi Action tier view-only: hanya tombol `[Mark as Read]` tanpa tombol navigasi atau CTA lain
23. Verifikasi Body mengikuti pola katalog `[Admin Name] removed your Read Only access on [Date].`
24. Tutup sesi UI kedua

### TC-FA-RP-883: Notifikasi in-app ke target: Auto-Revert Group Manager pemicu Remove baris Group Role

25. Pulihkan Kevin Susanto sebagai Group Manager di `Data Center` dengan Group Role eksplisit `Manage group` lewat seeding API hingga tersimpan, lalu buka Tab System dan Detail Role `Manage group` dan pilih node `Data Center`
26. Klik `[⋯]` baris Kevin Susanto lalu `Remove`, klik `[Remove]`
27. Tunggu aksi selesai: dialog tertutup
28. Buka sesi UI kedua, login sebagai Kevin Susanto, lalu buka Overlay Notifikasi lonceng navbar
29. Verifikasi notifikasi baru Title `You are no longer Group Manager for Data Center` dengan Body `Siti Rahmawati removed your Group Manager status for Data Center on [Date].` tampil, [Date] terformat sesuai General Settings
30. Verifikasi Action tier view-only: hanya tombol `[Mark as Read]` tanpa tombol navigasi atau CTA lain
31. Tutup sesi UI kedua

### TC-FA-RP-884: Assign Total Control, Read Only, dan Group Manager tidak memicu notifikasi

32. Catat baseline (aksi tanpa `Verifikasi`): jumlah notifikasi in-app Ahmad Fauzi, Budi Santoso, dan Dimas Pranata
33. Buka Tab Total Control
34. Klik `[+ Assign]` di Tab Total Control, centang Ahmad Fauzi, klik `[Assign]` (Assign Total Control ke Ahmad Fauzi)
35. Buka Tab Read Only
36. Klik `[+ Assign]` di Tab Read Only, centang Budi Santoso, klik `[Assign]` (Assign Read Only ke Budi Santoso)
37. Buka Tab Group Manager
38. Klik `[+ Assign]` di Tab Group Manager, pilih group `Data Center`, centang Dimas Pranata, klik `[Assign]` (Assign Group Manager ke Dimas Pranata di `Data Center`)
39. Tunggu aksi selesai: popup tertutup
40. Buka sesi UI kedua, login sebagai Ahmad Fauzi, lalu buka Overlay Notifikasi lonceng navbar
41. Verifikasi Overlay Notifikasi Ahmad Fauzi tampil dengan jumlah notifikasi yang terbaca
42. Verifikasi jumlah notifikasi Ahmad Fauzi sama dengan baseline (tidak ada notifikasi baru terkait penambahan akses)
43. Tutup sesi UI kedua, lalu buka sesi UI kedua dan login sebagai Budi Santoso, lalu buka Overlay Notifikasi lonceng navbar
44. Verifikasi Overlay Notifikasi Budi Santoso tampil dengan jumlah notifikasi yang terbaca
45. Verifikasi jumlah notifikasi Budi Santoso sama dengan baseline (tidak ada notifikasi baru terkait penambahan akses)
46. Tutup sesi UI kedua, lalu buka sesi UI kedua dan login sebagai Dimas Pranata, lalu buka Overlay Notifikasi lonceng navbar
47. Verifikasi Overlay Notifikasi Dimas Pranata tampil dengan jumlah notifikasi yang terbaca
48. Verifikasi jumlah notifikasi Dimas Pranata sama dengan baseline (tidak ada notifikasi baru terkait penambahan akses)
49. Tutup sesi UI kedua

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-role-permission/TestCases/tc-settings-role-permission.md`. Subjudul `###` memetakan langkah ke id TC granular. Spec ini memuat 49 langkah.
- Kelas c (multi-konteks): sesi UI kedua akun target menjadi objek asersi notifikasi in-app. TC-FA-RP-883 tidak punya butir pola katalog pada Expected (hanya a dan b), sehingga blok itu memuat dua Verifikasi. Maya Anggraeni (TC-FA-RP-882), Rina Wulandari (TC-FA-RP-881), dan Kevin Susanto (TC-FA-RP-883, dipulihkan) dipulihkan lewat seeding API di antara blok bila diperlukan; TC-FA-RP-880 dan 883 memakai Kevin Susanto yang sama sehingga 883 didahului pemulihan.
- Langkah penghubung (S-03): pembukaan tab dan Detail Role, "Tunggu aksi selesai" sebelum berpindah sesi (bagian 8b butir 8), pemulihan lewat seeding API, pencatatan baseline, dan penutupan sesi UI kedua (S-09). Akun aktor pertama sudah login di hook `before` (S-07).
- Absence notifikasi TC-FA-RP-884 (state sementara): ditulis segera sesudah pembukaan Overlay Notifikasi tiap target (bagian 8b butir 11) dengan Verifikasi Overlay tampil sebagai anchor; pemicunya adalah tiga Assign yang sukses, sehingga asersi jumlah dengan baseline boleh berada di spec ini (bukan kelas g).
- Spec melewati 35 langkah dengan alasan: seluruh blok satu kelas yang sama, tiap blok punya baseline dan pemicu sendiri dan berdiri sendiri (kegagalan satu blok tidak membuat blok lain kehilangan makna); memecahnya menambah login, hook, dan cleanup tanpa manfaat.
- Temuan untuk QA:
  - Akun login target (Kevin Susanto, Rina Wulandari, Maya Anggraeni, Ahmad Fauzi, Budi Santoso, Dimas Pranata) tidak tertulis di Pre-setup TC; email dan password disediakan tim FE.
  - TC-FA-RP-884 Expected tidak menyebut baseline; spec memakai jumlah notifikasi sebelum aksi (S-12). TC-FA-RP-884 tidak merujuk Pre-setup #43 untuk Group Manager di `Data Center` padahal Dimas Pranata di #38 berstatus Pending Activation pada `Rack A1`; spec memakai Dimas Pranata dari kolam #15 (Standard) sesuai precondition #15.
  - Post Condition "Log dan notifikasi dikirim dalam satu transaksi dengan aksi pemicu" pada TC-FA-RP-880 sampai 883 tanpa langkah observasi; tidak diasersi.
