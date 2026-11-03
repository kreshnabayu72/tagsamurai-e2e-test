---
id: TC-FA-LIC-E2E-015-screening-tab-concurrent-user-metric-summary-bar-kolom
title: "Screening Tab Concurrent User: Metric Summary Bar, Kolom, Isi Baris, Fokus Keyboard, dan Online Users"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-LIC-63
  - TC-FA-LIC-64
  - TC-FA-LIC-65
  - TC-FA-LIC-66
  - TC-FA-LIC-67
  - TC-FA-LIC-70
  - TC-FA-LIC-85
  - TC-FA-LIC-298
coverage:
  web: automated
---

# Screening Tab Concurrent User: Metric Summary Bar, Kolom, Isi Baris, Fokus Keyboard, dan Online Users

## Prerequisites

- Mode: FE+BE
- Akun aktor: Total Control Pre-setup #1 `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net` (client PT Sejahtera, plan Professional (Paid), `License allocation per group` ON; General Settings `dd/MM/yy`, `HH:mm`; kredensial `Spectra.env.FA_TC_PASSWORD`). Login di hook `before` spec ini; halaman Fixed Asset > License dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Data Pre-setup #14: 18 sesi aktif, seat 25; cuplikan Rudi Hartono (rudi@example.co.id, Position `Staff Gudang`, Division `Divisi Logistik`, IP `198.51.100.33`, `iOS`, `Safari`, Login Time 29/09/26 09:20, Last Activity 29/09/26 09:38), Dewi Lestari, Andi Pratama (tanpa Position dan Division), Siti Rahma, Budi Santoso (Position `Supervisor Gudang`, Division `Divisi Logistik`, IP `192.0.2.45`, `Windows`, `Chrome`, Login Time 29/09/26 06:40, Last Activity 29/09/26 07:05). Data Pre-setup #26: lima sesi cuplikan yang sama, Online Users 5/25, salah satunya milik user tanpa foto profil. Nilai dibaca dari `Fixture.fixedAssetLicense.*`; berkas fixture belum ada, disediakan tim FE.
- State yang diubah spec dan dipulihkan: Position Rudi Hartono diubah ke `Kepala Gudang` (TC-FA-LIC-67, langkah 27) dan dipulihkan pada langkah 30; tabel sesi dipulihkan ke Pre-setup #26 (langkah 31); ledger Concurrent User diubah ke Total 10 dengan 12 sesi grandfathered (TC-FA-LIC-70, langkah 36). Hook `after` memulihkan Pre-setup #14 dan #26. Fixture BE penyetel dan pemulih sesi, profil user, dan ledger disediakan tim FE/BE.
- Hook dan kemampuan suite (flag Guided Tooltip seen, sesi API aktor, fixture BE, pemulihan preferensi kolom): dinyatakan sekali di suite.md.
- Suite serial: `parallel: false` (lihat suite.md).

## Test Steps

### TC-FA-LIC-63: Metric Summary Bar, toolbar, dan kolom default

1. Klik Tab `Concurrent User`
2. Verifikasi Metric Summary Bar satu metrik: `Online Users: 18/25`
3. Verifikasi Toolbar: `Search | Filter | Changelog`
4. Verifikasi tidak ada ikon Download pada toolbar
5. Verifikasi Kolom default: `User Name (sortable) | Email (sortable) | Position (sortable) | Division (sortable) | IP Address (sortable) | Device / OS (sortable) | Browser (sortable) | Login Time (sortable) | Last Activity (sortable) | Column Visibility (⋯)`
6. Verifikasi kolom Actions berisi tombol `[Force Logout]`
7. Verifikasi paginasi default 10 per halaman
8. Verifikasi tidak ada checkbox seleksi

### TC-FA-LIC-64: Kolom Curated Hidden secara default

9. Verifikasi kolom `Activation Status`, `Temporary User`, `Temporary Until`, `TAG`, dan Custom Field aktif tidak tampil di tabel
10. Klik header kolom Actions `⋯`
11. Klik `Setup Column...`
12. Verifikasi pada Column Visibility kelima kolom itu tampil dengan checkbox tidak tercentang
13. Verifikasi sembilan kolom default tercentang
14. Tutup popup Setup Column dengan `×`

### TC-FA-LIC-65: Isi baris Active Sessions

15. Verifikasi baris Rudi Hartono: avatar + `Rudi Hartono`, rudi@example.co.id, Position `Staff Gudang`, Division `Divisi Logistik`, IP `198.51.100.33`, Device / OS `iOS`, Browser `Safari`, Login Time 29/09/26 09:20, Last Activity 29/09/26 09:38
16. Verifikasi baris Budi Santoso: Position `Supervisor Gudang`, Division `Divisi Logistik`, IP `192.0.2.45`, Device / OS `Windows`, Browser `Chrome`, Login Time 29/09/26 06:40, Last Activity 29/09/26 07:05
17. Arahkan kursor ke nama `Rudi Hartono`
18. Verifikasi tooltip nama lengkap `Rudi Hartono` tampil

### TC-FA-LIC-66: Sesi user tanpa Position atau Division

19. Verifikasi baris Andi Pratama: Position `—` dan Division `—`
20. Verifikasi tombol `[Force Logout]` tampil pada baris Andi Pratama

### TC-FA-LIC-85: Baris DataTables dan Force Logout memakai tema standar dan fokus keyboard

21. Tekan Tab hingga fokus mencapai tombol `[Force Logout]` pada baris pertama
22. Verifikasi tombol `[Force Logout]` menerima fokus keyboard dengan fokus ring
23. Arahkan kursor ke tombol `[Force Logout]`
24. Verifikasi tombol berseverity danger
25. Verifikasi label tooltip `Force Logout` tampil saat hover atau fokus

### TC-FA-LIC-67: Position dibaca live dari profil user

26. Catat Position Rudi Hartono di Tab `Concurrent User`
27. Ubah Position Rudi Hartono menjadi `Kepala Gudang` lewat fixture BE
28. Muat ulang Tab `Concurrent User`
29. Verifikasi Position Rudi Hartono di tabel berubah menjadi `Kepala Gudang` tanpa perubahan di data sesi
30. Pulihkan Position Rudi Hartono lewat fixture BE

### TC-FA-LIC-298: Avatar dan nama lengkap User Name

31. Pulihkan tabel sesi ke Pre-setup #26 (lima sesi, Online Users 5/25) lewat fixture BE, lalu muat ulang Tab `Concurrent User`
32. Verifikasi setiap sel kolom User Name menampilkan `[Avatar] Full Name`
33. Verifikasi user tanpa foto profil menampilkan ikon user generik
34. Arahkan kursor ke nama user
35. Verifikasi tooltip nama lengkap tampil

### TC-FA-LIC-70: Online Users saat Used melebihi Total

36. Setel ledger Concurrent User Total 10 dengan 12 sesi grandfathered lewat fixture BE, lalu muat ulang Tab `Concurrent User`
37. Verifikasi Metric Summary Bar `Online Users: 12/10`

## Notes

- Sumber: `fixed-asset/license/TestCases/tc-license.md` (TC-FA-LIC-63, 64, 65, 66, 67, 70, 85, 298). Tidak ada TC hanya-BE di spec ini.
- Urutan TC diubah dari urutan nomor: blok pada dataset #14 (TC-63 sampai 66, 85) di awal, TC-67 (mengubah profil) sesudahnya, lalu blok dataset #26 (TC-298) dan TC-70 (mengubah ledger) di akhir (S-10).
- Spec di atas 35 langkah (37 langkah): seluruh blok satu topik (tabel Active Sessions pada Tab Concurrent User) dan berdiri sendiri; kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Langkah penghubung (aksi tanpa `Verifikasi`, bukan dari langkah TC): langkah 1 (klik Tab), langkah 14 (menutup popup Setup Column), langkah 30 dan 31 (pemulihan). Langkah 27 memakai fixture BE sebagai pemicu perubahan Position (pengganti Global Settings > User; pemicu, bukan objek uji).
- Temuan untuk QA:
  - TC-65 meminta "Hover nama menampilkan nama lengkap sebagai tooltip" tanpa menyebut nama yang di-hover; langkah 17 memakai `Rudi Hartono`.
  - TC-67 mengubah Position lewat Global Settings > User; spec memakai fixture BE.
  - TC-298 Precondition "Satu sesi milik user tanpa foto profil" tidak menyebut user mana di Pre-setup #26; langkah 33 mengasersi pada user mana pun tanpa foto profil.
