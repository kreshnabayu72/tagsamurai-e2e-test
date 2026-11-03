---
id: TC-FA-RP-E2E-262-multi-konteks-notifikasi-in-app-ke-akun-target-1
title: "Multi-konteks: notifikasi in-app ke akun target (1/3)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-RP-875
  - TC-FA-RP-876
  - TC-FA-RP-877
  - TC-FA-RP-878
  - TC-FA-RP-879
coverage:
  web: automated
---

# Multi-konteks: notifikasi in-app ke akun target (1/3)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #2, Siti Rahmawati), email `totalControl_automated_{namaCompany}@qwertysystem.net` (`Fixture.fixedAssetRolePermission.akun.totalControl.email`), password `Spectra.env.FA_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Role & Permission, Tab Total Control). Hook `after` mengembalikan sesi ke akun default suite (Total Control, `FA_TC_PASSWORD`).
- Data Pre-setup: #15 (Ahmad Fauzi sebagai Total Control pada TC-FA-RP-875), #12 (Maya Anggraeni: Read Only), #43 dan #18 (Kevin Susanto Group Manager di `Data Center`), #3 (Rina Wulandari, Total Control kedua), dan #13 (Kevin Susanto dengan Group Role eksplisit di `Data Center`).
- Sesi UI kedua: konteks browser terpisah yang login sebagai akun target dan menjadi objek asersi notifikasi (P-2 tidak berlaku karena sesi kedua adalah objek asersi, bukan pemicu); ditutup di akhir tiap blok TC (S-09). Akun login target (Ahmad Fauzi, Maya Anggraeni, Kevin Susanto, Rina Wulandari, Budi Santoso, Dimas Pranata, Gunawan Halim sesuai TC) tidak tertulis di Pre-setup TC; email dan password disediakan tim FE (lihat Temuan untuk QA).
- Format [Date] pada Body notifikasi mengikuti General Settings (Pre-setup #34, Date Format); nilai [Date] adalah tanggal aksi pemicu.
- Notifikasi: pola Title dan Body mengikuti TC (katalog notifikasi `fixed-asset/notification/PRD/notification.md §5.1f` dirujuk TC). Overlay Notifikasi dibuka dari lonceng navbar.
- Flag Guided Tooltip, halaman awal, sesi API aktor, dan pemulihan Pre-setup bersama: lihat `suite.md` bagian "Hook suite".
- Data Pre-setup dirujuk lewat fixture `Fixture.fixedAssetRolePermission` (berkas `fixtures/fixedAssetRolePermission.json`, belum ada; disediakan tim FE). Email data pengguna berformat `[namalengkaptanpaspasi]@qwertysystem.net`.
- Seeding dan pemulihan: kondisi Precondition tiap TC (tingkat akses, penugasan, group, status pengguna) dibuat lewat seeding API (kemampuan disediakan tim FE/BE, tanpa endpoint karangan) di hook `before` dan sebagai langkah penghubung antar blok TC; Pre-setup yang diubah dipulihkan ke Tabel Data Uji Pre-setup TC di hook `after` (Catatan TC "Pemulihan fixture destruktif"). Spec tidak membuat data Dinamis. Suite berjalan serial (`parallel: false`).
- Env var yang dipakai: `FA_TC_PASSWORD`. Didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example` (nama dan arti di `suite.md` bagian "Env password akun aktor"). Password tidak ditulis di spec atau fixture.

## Test Steps

### TC-FA-RP-875: Notifikasi in-app ke target: Remove Total Control

1. Klik `[⋯]` baris Ahmad Fauzi lalu `Remove`, klik `[Remove]`
2. Tunggu aksi selesai: dialog tertutup
3. Buka sesi UI kedua, login sebagai Ahmad Fauzi, lalu buka Overlay Notifikasi lonceng navbar
4. Verifikasi notifikasi baru Title `Your Total Control access was removed` dengan Body `Siti Rahmawati removed your Total Control access on [Date].` tampil, [Date] terformat sesuai General Settings
5. Verifikasi Action tier view-only: hanya tombol `[Mark as Read]` tanpa tombol navigasi atau CTA lain
6. Verifikasi Body mengikuti pola katalog `[Admin Name] removed your Total Control access on [Date].`
7. Tutup sesi UI kedua

### TC-FA-RP-876: Notifikasi in-app ke target: Remove Read Only

8. Buka Tab Read Only
9. Klik `[⋯]` baris Maya Anggraeni lalu `Remove`, klik `[Remove]`
10. Tunggu aksi selesai: dialog tertutup
11. Buka sesi UI kedua, login sebagai Maya Anggraeni, lalu buka Overlay Notifikasi lonceng navbar
12. Verifikasi notifikasi baru Title `Your Read Only access was removed` dengan Body `Siti Rahmawati removed your Read Only access on [Date].` tampil, [Date] terformat sesuai General Settings
13. Verifikasi Action tier view-only: hanya tombol `[Mark as Read]` tanpa tombol navigasi atau CTA lain
14. Verifikasi Body mengikuti pola katalog `[Admin Name] removed your Read Only access on [Date].`
15. Tutup sesi UI kedua

### TC-FA-RP-877: Notifikasi in-app ke target: Remove Group Manager

16. Buka Tab Group Manager
17. Klik `[⋯]` baris Kevin Susanto di `Data Center` lalu `Remove`, klik `[Remove]`
18. Tunggu aksi selesai: dialog tertutup
19. Buka sesi UI kedua, login sebagai Kevin Susanto, lalu buka Overlay Notifikasi lonceng navbar
20. Verifikasi notifikasi baru Title `You are no longer Group Manager for Data Center` dengan Body `Siti Rahmawati removed your Group Manager status for Data Center on [Date].` tampil, [Date] terformat sesuai General Settings
21. Verifikasi Action tier view-only: hanya tombol `[Mark as Read]` tanpa tombol navigasi atau CTA lain
22. Verifikasi tidak ada notifikasi tambahan untuk baris Group Role yang ikut dihapus (hanya satu notifikasi pelepasan Group Manager yang baru)
23. Verifikasi pola Title katalog `You are no longer Group Manager for [Group Name]` dan pola Body `[Admin Name] removed your Group Manager status for [Group Name] on [Date].`
24. Tutup sesi UI kedua

### TC-FA-RP-878: Notifikasi in-app ke target: Auto-Revert Total Control pemicu Edit CRUD

25. Buka Tab System, lalu Detail Role `Manage accounting`
26. Hapus centang Delete pada baris Rina Wulandari lalu klik `[Remove]` pada dialog
27. Tunggu aksi selesai: perubahan tersimpan
28. Buka sesi UI kedua, login sebagai Rina Wulandari, lalu buka Overlay Notifikasi lonceng navbar
29. Verifikasi notifikasi baru Title `Your Total Control access was removed` dengan Body `Siti Rahmawati removed your Total Control access on [Date].` tampil, [Date] terformat sesuai General Settings
30. Verifikasi Action tier view-only: hanya tombol `[Mark as Read]` tanpa tombol navigasi atau CTA lain
31. Verifikasi Body mengikuti pola katalog `[Admin Name] removed your Total Control access on [Date].`
32. Tutup sesi UI kedua

### TC-FA-RP-879: Notifikasi in-app ke target: Auto-Revert Read Only pemicu Edit CRUD

33. Pulihkan Maya Anggraeni sebagai Read Only lewat seeding API hingga tersimpan, lalu buka Tab System dan Detail Role `Manage accounting`
34. Centang Create pada baris Maya Anggraeni lalu klik `[Remove]` pada dialog
35. Tunggu aksi selesai: perubahan tersimpan
36. Buka sesi UI kedua, login sebagai Maya Anggraeni, lalu buka Overlay Notifikasi lonceng navbar
37. Verifikasi notifikasi baru Title `Your Read Only access was removed` dengan Body `Siti Rahmawati removed your Read Only access on [Date].` tampil, [Date] terformat sesuai General Settings
38. Verifikasi Action tier view-only: hanya tombol `[Mark as Read]` tanpa tombol navigasi atau CTA lain
39. Verifikasi Body mengikuti pola katalog `[Admin Name] removed your Read Only access on [Date].`
40. Tutup sesi UI kedua

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-role-permission/TestCases/tc-settings-role-permission.md`. Subjudul `###` memetakan langkah ke id TC granular. Spec ini memuat 40 langkah.
- Kelas c (multi-konteks): sesi UI kedua akun target menjadi objek asersi notifikasi in-app. Aktor pemicu tetap Total Control pada sesi utama. Urutan blok: TC-FA-RP-875 sampai 879 mengikuti TC sumber; Maya Anggraeni dipulihkan sebagai Read Only sebelum TC-FA-RP-879 karena TC-FA-RP-876 telah mencabut Read Only-nya.
- Langkah penghubung (S-03): pembukaan tab dan Detail Role, "Tunggu aksi selesai" sebelum berpindah sesi (bagian 8b butir 8), pemulihan lewat seeding API, dan penutupan sesi UI kedua (S-09). Akun aktor pertama sudah login di hook `before` (S-07).
- Notifikasi "baru": notifikasi dicari berdasarkan Title dan Body yang memuat tanggal aksi; N audit trail notifikasi tidak diasersi sebagai angka absolut (S-12).
- Spec melewati 35 langkah dengan alasan: seluruh blok satu kelas yang sama, tiap blok punya baseline dan pemicu sendiri dan berdiri sendiri (kegagalan satu blok tidak membuat blok lain kehilangan makna); memecahnya menambah login, hook, dan cleanup tanpa manfaat.
- Temuan untuk QA:
  - Akun login target (Ahmad Fauzi, Maya Anggraeni, Kevin Susanto, Rina Wulandari) tidak tertulis di Pre-setup TC; TC hanya menyebut "memiliki akun login". Email dan password disediakan tim FE.
  - TC-FA-RP-879 mendeskripsikan aksi "Centang Create pada baris Maya Anggraeni lalu klik `[Remove]` pada dialog"; spec mengikuti TC apa adanya. Pre-setup #12 menyebut Maya Anggraeni hanya Read pada seluruh Global Role, sehingga mencentang Create memicu Auto-Revert Read Only.
  - TC-FA-RP-875 dan 878 mensyaratkan Ahmad Fauzi (#15) dan Rina Wulandari (#3) sebagai Total Control; Precondition TC-FA-RP-878 merujuk #3 tetapi baris `Manage accounting` Rina Wulandari tidak tertulis eksplisit selain "seluruh Global Role CRUD penuh" pada #3.
  - TC-FA-RP-875 sampai 879 memiliki Post Condition "Log dan notifikasi dikirim dalam satu transaksi dengan aksi pemicu" tanpa langkah observasi; tidak diasersi (atomisitas satu transaksi diuji sebagai tes backend per Catatan TC).
