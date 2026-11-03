---
id: TC-FA-RP-E2E-264-multi-konteks-notifikasi-in-app-ke-akun-target-3
title: "Multi-konteks: notifikasi in-app ke akun target (3/3)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-RP-885
  - TC-FA-RP-886
  - TC-FA-RP-887
  - TC-FA-RP-888
coverage:
  web: automated
---

# Multi-konteks: notifikasi in-app ke akun target (3/3)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #2, Siti Rahmawati), email `totalControl_automated_{namaCompany}@qwertysystem.net` (`Fixture.fixedAssetRolePermission.akun.totalControl.email`), password `Spectra.env.FA_TC_PASSWORD`.
- Akun ganti (TC-FA-RP-888): Manage global user & role dengan Update (Pre-setup #6, Hendra Wijaya), email `murGlobal_automated_{namaCompany}@qwertysystem.net` (`Fixture.fixedAssetRolePermission.akun.murGlobal.email`), password `Spectra.env.FA_MUR_GLOBAL_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Role & Permission, Tab Total Control). Hook `after` mengembalikan sesi ke akun default suite (Total Control, `FA_TC_PASSWORD`).
- Data Pre-setup: #12 (Maya Anggraeni: Read Only; TC-FA-RP-885 dan 887), #43 dan #18 (Kevin Susanto Group Manager di `Data Center` dan `Helpdesk`; TC-FA-RP-886), #3 (Rina Wulandari, Total Control kedua; TC-FA-RP-887), #17 (Gunawan Halim, Home Group `Data Center`, memegang `Manage files` di `Helpdesk`; TC-FA-RP-888), dan #3 serta #12 sebagai pemegang `Manage Open API` pada TC-FA-RP-887.
- Sesi UI kedua: konteks browser terpisah yang login sebagai akun target dan menjadi objek asersi notifikasi (P-2 tidak berlaku karena sesi kedua adalah objek asersi, bukan pemicu); ditutup di akhir tiap blok TC (S-09). Akun login target (Ahmad Fauzi, Maya Anggraeni, Kevin Susanto, Rina Wulandari, Budi Santoso, Dimas Pranata, Gunawan Halim sesuai TC) tidak tertulis di Pre-setup TC; email dan password disediakan tim FE (lihat Temuan untuk QA).
- Kemampuan teknis: membaca jumlah notifikasi in-app akun target sebelum aksi (baseline TC-FA-RP-885 dan 888, S-12) disediakan tim FE/BE; tanpa endpoint karangan.
- Format [Date] pada Body notifikasi mengikuti General Settings (Pre-setup #34, Date Format); nilai [Date] adalah tanggal aksi pemicu.
- Notifikasi: pola Title dan Body mengikuti TC (katalog notifikasi `fixed-asset/notification/PRD/notification.md §5.1f` dirujuk TC). Overlay Notifikasi dibuka dari lonceng navbar.
- Flag Guided Tooltip, halaman awal, sesi API aktor, dan pemulihan Pre-setup bersama: lihat `suite.md` bagian "Hook suite".
- Data Pre-setup dirujuk lewat fixture `Fixture.fixedAssetRolePermission` (berkas `fixtures/fixedAssetRolePermission.json`, belum ada; disediakan tim FE). Email data pengguna berformat `[namalengkaptanpaspasi]@qwertysystem.net`.
- Seeding dan pemulihan: kondisi Precondition tiap TC (tingkat akses, penugasan, group, status pengguna) dibuat lewat seeding API (kemampuan disediakan tim FE/BE, tanpa endpoint karangan) di hook `before` dan sebagai langkah penghubung antar blok TC; Pre-setup yang diubah dipulihkan ke Tabel Data Uji Pre-setup TC di hook `after` (Catatan TC "Pemulihan fixture destruktif"). Spec tidak membuat data Dinamis. Suite berjalan serial (`parallel: false`).
- Env var yang dipakai: `FA_TC_PASSWORD` dan `FA_MUR_GLOBAL_PASSWORD`. Didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example` (nama dan arti di `suite.md` bagian "Env password akun aktor"). Password tidak ditulis di spec atau fixture.

## Test Steps

### TC-FA-RP-885: Upgrade Read Only ke Total Control tidak memicu notifikasi Remove Read Only

1. Catat baseline (aksi tanpa `Verifikasi`): jumlah notifikasi in-app Maya Anggraeni dengan Title `Your Read Only access was removed`
2. Klik `[+ Assign]` di Tab Total Control, centang Maya Anggraeni, klik `[Assign]` (Assign Total Control ke Maya Anggraeni)
3. Tunggu aksi selesai: popup tertutup
4. Buka sesi UI kedua, login sebagai Maya Anggraeni, lalu buka Overlay Notifikasi lonceng navbar
5. Verifikasi Overlay Notifikasi Maya Anggraeni tampil dengan jumlah notifikasi yang terbaca
6. Verifikasi jumlah notifikasi `Your Read Only access was removed` sama dengan baseline (tidak ada notifikasi baru)
7. Tutup sesi UI kedua

### TC-FA-RP-886: Assign Total Control ke Group Manager mengirim satu notifikasi per group yang dilepas

8. Pulihkan Kevin Susanto sebagai Group Manager di `Data Center` dan `Helpdesk` lewat seeding API hingga tersimpan
9. Klik `[+ Assign]` di Tab Total Control, centang Kevin Susanto, klik `[Assign]` (Assign Total Control ke Kevin Susanto)
10. Tunggu aksi selesai: popup tertutup
11. Buka sesi UI kedua, login sebagai Kevin Susanto, lalu buka Overlay Notifikasi lonceng navbar
12. Verifikasi dua notifikasi baru tampil: Title `You are no longer Group Manager for Data Center` dan Title `You are no longer Group Manager for Helpdesk`
13. Verifikasi Body `Siti Rahmawati removed your Group Manager status for Data Center on [Date].` dan versi `Helpdesk`, [Date] terformat sesuai General Settings
14. Tutup sesi UI kedua

### TC-FA-RP-887: Bulk Remove dengan baris bertier mengirim satu notifikasi per user terdampak

15. Pulihkan Rina Wulandari sebagai Total Control dan Maya Anggraeni sebagai Read Only, keduanya memegang `Manage Open API`, lewat seeding API hingga tersimpan, lalu buka Tab System dan Detail Role `Manage Open API`
16. Centang baris Rina Wulandari dan Maya Anggraeni, klik `Bulk Action` > `Remove` > `[Remove]`
17. Verifikasi toast bulk tidak memuat informasi auto-revert: `Success, user has been removed.`
18. Tunggu aksi selesai: dialog tertutup
19. Buka sesi UI kedua, login sebagai Rina Wulandari, lalu buka Overlay Notifikasi lonceng navbar
20. Verifikasi Rina Wulandari menerima satu notifikasi Total Control baru
21. Tutup sesi UI kedua, lalu buka sesi UI kedua dan login sebagai Maya Anggraeni, lalu buka Overlay Notifikasi lonceng navbar
22. Verifikasi Maya Anggraeni menerima satu notifikasi Read Only baru
23. Tutup sesi UI kedua

### TC-FA-RP-888: Pencabutan Group Role akibat Home Group constraint tidak mengirim notifikasi ke target

24. Ganti akun: logout dari Siti Rahmawati lalu login sebagai Manage global user & role (Update) (Pre-setup #6, Hendra Wijaya)
25. Catat baseline (aksi tanpa `Verifikasi`): jumlah notifikasi in-app Gunawan Halim
26. Tetapkan Home Group constraint `Data Center` untuk Gunawan Halim dan konfirmasi `[Revoke]`
27. Tunggu aksi selesai: dialog tertutup
28. Buka sesi UI kedua, login sebagai Gunawan Halim, lalu buka Overlay Notifikasi lonceng navbar
29. Verifikasi Overlay Notifikasi Gunawan Halim tampil dengan jumlah notifikasi yang terbaca
30. Verifikasi jumlah notifikasi Gunawan Halim sama dengan baseline (tidak ada notifikasi tentang pencabutan assignment)
31. Tutup sesi UI kedua

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-role-permission/TestCases/tc-settings-role-permission.md`. Subjudul `###` memetakan langkah ke id TC granular. Spec ini memuat 31 langkah.
- Kelas c (multi-konteks): sesi UI kedua akun target menjadi objek asersi notifikasi in-app. Ganti akun ke Hendra Wijaya pada TC-FA-RP-888 memakai Step eksplisit (S-07); hook `after` mengembalikan sesi ke akun default suite.
- Langkah penghubung (S-03): pencatatan baseline, pembukaan tab dan Detail Role, "Tunggu aksi selesai" sebelum berpindah sesi (bagian 8b butir 8), pemulihan lewat seeding API, dan penutupan sesi UI kedua (S-09).
- Absence notifikasi (TC-FA-RP-885 dan 888, state sementara): ditulis segera sesudah pembukaan Overlay Notifikasi (bagian 8b butir 11) dengan Verifikasi Overlay tampil sebagai anchor; baseline jumlah sebelum aksi (S-12). Pemicunya adalah aksi sukses, bukan penolakan, sehingga asersi jumlah dengan baseline boleh berada di spec ini (bukan kelas g).
- TC-FA-RP-888: Home Group constraint ditetapkan oleh Hendra Wijaya sesuai Precondition TC (Login sbg Role: Manage global user & role (Update)).
- Temuan untuk QA:
  - Akun login target (Maya Anggraeni, Kevin Susanto, Rina Wulandari, Gunawan Halim) tidak tertulis di Pre-setup TC; email dan password disediakan tim FE.
  - TC-FA-RP-888 tidak menyebut lokasi UI penetapan Home Group constraint; spec memakai kalimat TC apa adanya.
  - TC-FA-RP-887 memiliki dua Expected (a dan b); spec mengasersi b (toast) segera sesudah aksi dan a sesudah pindah sesi sesuai urutan state (bagian 8b butir 5). TC-FA-RP-885 dan 886 tidak memuat Post Condition.
