---
id: TC-FA-RP-E2E-266-sinkronisasi-detail-role-dan-tab-role-settings-user-2
title: "Sinkronisasi Detail Role dan Tab Role Settings > User (2/2)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-RP-897
  - TC-FA-RP-898
  - TC-FA-RP-899
  - TC-FA-RP-911
coverage:
  web: automated
---

# Sinkronisasi Detail Role dan Tab Role Settings > User (2/2)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #2, Siti Rahmawati), email `totalControl_automated_{namaCompany}@qwertysystem.net` (`Fixture.fixedAssetRolePermission.akun.totalControl.email`), password `Spectra.env.FA_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Role & Permission, Tab Total Control). Hook `after` mengembalikan sesi ke akun default suite (Total Control, `FA_TC_PASSWORD`).
- Data Pre-setup: #15 (Ahmad Fauzi dan Budi Santoso sebagai Standard tanpa tingkat akses), #3 (Rina Wulandari, Total Control kedua; TC-FA-RP-899), #18 (pohon group Company Alpha: `IT Infrastructure`, `Data Center`), dan #19 (seed Role Transaksi Disposal pada `IT Infrastructure`). Budi Santoso di-seed tidak memegang `Manage Open API` (TC-FA-RP-911).
- Kemampuan teknis: membaca jumlah notifikasi in-app akun Rina Wulandari lewat sesi API akun target (baseline dan hasil TC-FA-RP-899 Expected c) disediakan tim FE/BE; tanpa endpoint karangan.
- Flag Guided Tooltip, halaman awal, sesi API aktor, dan pemulihan Pre-setup bersama: lihat `suite.md` bagian "Hook suite".
- Data Pre-setup dirujuk lewat fixture `Fixture.fixedAssetRolePermission` (berkas `fixtures/fixedAssetRolePermission.json`, belum ada; disediakan tim FE). Email data pengguna berformat `[namalengkaptanpaspasi]@qwertysystem.net`.
- Seeding dan pemulihan: kondisi Precondition tiap TC (tingkat akses, penugasan, group, status pengguna) dibuat lewat seeding API (kemampuan disediakan tim FE/BE, tanpa endpoint karangan) di hook `before` dan sebagai langkah penghubung antar blok TC; Pre-setup yang diubah dipulihkan ke Tabel Data Uji Pre-setup TC di hook `after` (Catatan TC "Pemulihan fixture destruktif"). Spec tidak membuat data Dinamis. Suite berjalan serial (`parallel: false`).
- Pemulihan di hook `after`: Rina Wulandari dikembalikan sebagai Total Control kedua dengan seluruh Global Role CRUD penuh.
- Env var yang dipakai: `FA_TC_PASSWORD`. Didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example` (nama dan arti di `suite.md` bagian "Env password akun aktor"). Password tidak ditulis di spec atau fixture.

## Test Steps

### TC-FA-RP-897: Role Transaksi tersinkron dua arah dengan Tab Role Settings > User sub-tab Transaction Role

1. Buka Fixed Asset > Settings > Role & Permission > Tab Transaction Role
2. Klik node `IT Infrastructure` lalu sub-tab `Disposal`
3. Klik `[+ Assign]` pada section Asset Admin, centang Ahmad Fauzi, klik `[Assign]`
4. Tunggu aksi selesai: popup tertutup
5. Buka Settings > User > Detail Ahmad Fauzi > Tab Role sub-tab Transaction Role
6. Verifikasi penugasan `Disposal` `Asset Admin` pada `IT Infrastructure` tampil pada Tab Role Ahmad Fauzi

### TC-FA-RP-898: Tingkat akses dan Group Manager satu arah: Settings > User hanya menampilkan banner tanpa aksi assign atau remove

7. Buka Tab Total Control
8. Klik `[+ Assign]` di Tab Total Control, centang Ahmad Fauzi, klik `[Assign]` (Assign Total Control ke Ahmad Fauzi)
9. Buka Tab Group Manager
10. Klik `[+ Assign]` di Tab Group Manager, pilih group `Data Center`, centang Budi Santoso, klik `[Assign]` (Assign Group Manager ke Budi Santoso di `Data Center`)
11. Tunggu aksi selesai: popup tertutup
12. Buka Settings > User > Detail Ahmad Fauzi
13. Verifikasi Detail Ahmad Fauzi menampilkan banner status Total Control
14. Verifikasi tidak ada kontrol assign atau remove tingkat akses di Detail Ahmad Fauzi
15. Buka Settings > User > Detail Budi Santoso
16. Verifikasi Detail Budi Santoso menampilkan banner status Group Manager
17. Verifikasi tidak ada kontrol assign atau remove Group Manager di Detail Budi Santoso

### TC-FA-RP-899: Auto-Revert dari origin Tab Role Settings > User: dialog muncul di sana dan hasilnya tampil di Tab Total Control

18. Catat baseline (aksi tanpa `Verifikasi`): jumlah notifikasi in-app Rina Wulandari, dibaca lewat sesi API akun target (kemampuan baca notifikasi disediakan tim FE/BE)
19. Buka Settings > User > Detail Rina Wulandari > Tab Role sub-tab Global Role
20. Matikan switch `Manage Open API`
21. Verifikasi dialog auto-revert Total Control tampil pada Settings > User sebelum perubahan disimpan
22. Konfirmasi dialog auto-revert
23. Tunggu aksi selesai: perubahan tersimpan
24. Buka Fixed Asset > Settings > Role & Permission > Tab Total Control
25. Verifikasi baris Siti Rahmawati (Total Control lain) tampil di Tab Total Control
26. Verifikasi Rina Wulandari tidak lagi ada di Tab Total Control
27. Baca daftar notifikasi in-app Rina Wulandari lewat sesi API akun target
28. Verifikasi notifikasi in-app baru terkirim ke Rina Wulandari (jumlah notifikasi bertambah dari baseline)

### TC-FA-RP-911: Kolom Users Tab System diperbarui setelah Assign dan Remove lintas origin

29. Buka Tab System, lalu catat kolom Users baris `Manage Open API` (baseline)
30. Buka Detail Role `Manage Open API`
31. Klik `[+ Assign]`, centang Budi Santoso, klik `[Assign]` (Assign Budi Santoso ke role itu)
32. Tunggu aksi selesai: popup tertutup
33. Buka Tab System
34. Verifikasi kolom Users baris `Manage Open API` naik satu terhadap baseline
35. Buka Settings > User > Detail Budi Santoso > Tab Role sub-tab Global Role
36. Matikan switch `Manage Open API`
37. Tunggu aksi selesai: perubahan tersimpan
38. Buka kembali Fixed Asset > Settings > Role & Permission > Tab System
39. Verifikasi kolom Users baris `Manage Open API` kembali ke nilai baseline

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-role-permission/TestCases/tc-settings-role-permission.md`. Subjudul `###` memetakan langkah ke id TC granular. Spec ini memuat 39 langkah.
- Urutan blok: TC-FA-RP-897, 898, 899, 911; TC-FA-RP-899 (mencabut Total Control Rina Wulandari lewat switch) sebelum TC-FA-RP-911 yang tidak memakai Rina Wulandari.
- Langkah penghubung (S-03): pencatatan baseline, pembukaan tab, Detail Role, dan Settings > User, serta "Tunggu aksi selesai". Akun aktor pertama sudah login di hook `before` (S-07).
- Notifikasi pada TC-FA-RP-899 Expected c dibaca lewat sesi API akun target (bukan sesi UI kedua) karena notifikasi bukan objek uji TC ini; hal itu dicatat di Prerequisites.
- Spec melewati 35 langkah dengan alasan: seluruh blok satu kelas yang sama (sinkronisasi atau efek lintas modul), tiap blok berdiri sendiri dan punya Expected sendiri (kegagalan satu blok tidak membuat blok lain kehilangan makna); memecahnya menambah login, hook, dan cleanup tanpa manfaat.
- Temuan untuk QA:
  - TC-FA-RP-899 Expected c ("Notifikasi in-app tetap terkirim ke Rina Wulandari") tidak menyebut Title dan Body notifikasi; spec hanya mengasersi bahwa notifikasi baru terkirim (jumlah bertambah dari baseline). Teks dialog auto-revert dan label tombol konfirmasinya tidak disebut di TC-FA-RP-899; spec memakai "Konfirmasi dialog auto-revert".
  - TC-FA-RP-898 menyebut "banner status" tanpa teksnya; spec mengasersi banner Total Control dan Group Manager tanpa teks persis. TC-FA-RP-897 dan 911 tidak punya Post Condition.
  - Precondition TC-FA-RP-911 hanya merujuk Pre-setup #15; spec men-seed Budi Santoso tanpa `Manage Open API` agar Assign mengubah kolom Users.
