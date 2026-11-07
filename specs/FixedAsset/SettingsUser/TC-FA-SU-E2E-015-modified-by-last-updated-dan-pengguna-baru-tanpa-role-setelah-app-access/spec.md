---
id: TC-FA-SU-E2E-015-modified-by-last-updated-dan-pengguna-baru-tanpa-role-setelah-app-access
title: "Kolom Modified By dan Last Updated serta Pengguna Baru Tanpa Role setelah App Access Diberikan"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-12
  - TC-FA-SU-16
coverage:
  web: automated
---

# Kolom Modified By dan Last Updated serta Pengguna Baru Tanpa Role setelah App Access Diberikan

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control Lina Marlina (Pre-setup #1, `totalControl_automated_{namaCompany}@qwertysystem.net`), password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite. Hook suite dinyatakan di `suite.md`. Langkah 33 memakai satu akun kedua (pengguna dinamis Y) lewat Ganti akun eksplisit; sesi dipulihkan ke akun default suite di hook `after`.
- Data Pre-setup (hanya dibaca): Client `FaUserMain` dengan 25 pengguna (#20) dan Global Settings (#38; App Access FAMS dapat diberikan atau dicabut oleh Principal Automation). Nilai dibaca dari `Fixture.faSettingsUser.preSetup` (fixture belum ada, disediakan tim FE).
- Data Dinamis (di-seed lewat API di hook `before` pada Global Settings tanpa App Access FAMS, dihapus di hook `after`): pengguna X (TC-FA-SU-12) `Pengguna Modified {runId}-015`, email `modified+{runId}-015@qwertysystem.net`; pengguna Y (TC-FA-SU-16) `Pengguna Baru {runId}-015`, email `barutanparole+{runId}-015@qwertysystem.net`.
- Kemampuan teknis: Principal Automation (Pre-setup #12) memberi dan mencabut App Access FAMS lewat sesi API (disediakan tim FE); inbox email asli yang dapat dibaca untuk tautan aktivasi pengguna Y dan password pengguna Y yang diatur lewat env yang disediakan tim FE (Manual Only (c) pada TC-FA-SU-16); pencatatan waktu sesudah aksi; jam server dan jam browser sinkron (asersi Last Updated memakai toleransi satu menit, S-12).
- State global: App Access FAMS pengguna X dan Y serta Last Updated pengguna dinamis; tidak mengubah Pre-setup bersama. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-SU-12: Kolom Modified By dan Last Updated: format nama, hover, format tanggal, dan record tanpa log

1. Verifikasi kolom Modified By tampil dalam format `[First Name] [Last Initial]` (`Ahmad D`, `Budi S`)
2. Hover `Ahmad D` pada kolom Modified By
3. Verifikasi tooltip menampilkan nama lengkap `Ahmad Dahlan`
4. Verifikasi Ahmad Dahlan (Default User, seed) menampilkan Modified By `System`
5. Principal Automation memberi App Access FAMS pada pengguna X lewat sesi API hingga tersimpan, lalu catat waktunya
6. Muat ulang User List
7. Ketik Search email pengguna X, tekan Enter
8. Verifikasi baris pengguna X tampil
9. Verifikasi Modified By pengguna X `System`
10. Verifikasi Last Updated pengguna X sama dengan waktu App Access diberikan (toleransi satu menit)
11. Verifikasi Last Updated mengikuti Date Format dan Time Format General Settings
12. Lakukan Activate pada pengguna X
13. Tunggu aksi selesai
14. Muat ulang User List
15. Verifikasi Modified By pengguna X tidak lagi `System`
16. Verifikasi Last Updated pengguna X berubah dari nilai pada langkah 10
17. Buka Edit Home Group pengguna X tanpa mengubah nilai lalu simpan (Edit No-Op)
18. Tunggu aksi selesai
19. Muat ulang User List
20. Verifikasi Modified By pengguna X tidak berubah dari nilai langkah 15
21. Verifikasi Last Updated pengguna X tidak berubah dari nilai langkah 16

### TC-FA-SU-16: Pengguna baru tanpa role muncul di User List dan setelah login diarahkan ke My Asset

22. Principal Automation memberi App Access FAMS pada pengguna Y lewat sesi API hingga tersimpan
23. Muat ulang User List
24. Ganti isi kotak search dengan email pengguna Y, tekan Enter
25. Verifikasi pengguna Y muncul di User List dengan sakelar Active ON
26. Verifikasi Role pengguna Y `0 roles`
27. Verifikasi pengguna Y menampilkan badge `Pending Activation`
28. Principal Automation mencabut App Access FAMS pengguna Y lewat sesi API hingga tersimpan
29. Principal Automation memberi ulang App Access FAMS pengguna Y lewat sesi API hingga tersimpan
30. Muat ulang User List
31. Verifikasi pengguna Y tampil kembali tanpa peran (`0 roles`)
32. Verifikasi sakelar Active pengguna Y ON
33. Ganti akun: Logout, aktivasi akun pengguna Y dari tautan email, lalu login ke FAMS sebagai pengguna Y
34. Verifikasi pengguna Y diarahkan ke halaman My Asset
35. Verifikasi menu navigasi FAMS pengguna Y tampil
36. Verifikasi tidak ada menu fungsional administratif lain yang dapat diakses pengguna Y

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular.
- Jumlah langkah 36, di atas smell 35 langkah; dua TC berdiri sendiri (kegagalan satu blok tidak membuat blok lain kehilangan makna) dan satu topik (pengguna dinamis di User List); kelebihan berasal dari dua langkah penghubung Tunggu aksi selesai (bagian 8b butir 8).
- Urutan di dalam TC-FA-SU-16: Expected a (langkah 22 sampai 27), c (langkah 28 sampai 32), lalu b (langkah 33 sampai 36), karena b mengganti akun ke pengguna Y dan mengakhiri alur (S-10); urutan Langkah Uji TC adalah a, b, c.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 5, 22, 28, dan 29 (pemicu Principal Automation lewat sesi API tanpa objek asersi UI kedua), langkah 6, 14, 19, 23, dan 30 (muat ulang), langkah 7 dan 24 (Search email pengguna dinamis untuk menemukan baris target, R-16), langkah 13 dan 18 (Tunggu aksi selesai sesudah Activate dan Edit Home Group yang hasilnya tidak diasersi langsung, sebelum muat ulang, bagian 8b butir 8). Langkah 8 dan 25 adalah anchor bahwa baris pengguna ada sebelum asersi kolomnya; langkah 35 adalah anchor bahwa menu navigasi pengguna Y termuat sebelum asersi absence langkah 36 (bagian 8b butir 2).
- Langkah 12: "Lakukan Activate" mengikuti kata TC; lihat Temuan untuk QA.
- Langkah 17 menambah aksi Edit No-Op sebagai pemicu Expected e TC-FA-SU-12 karena Langkah Uji TC tidak memuat aksinya (S-03).
- Pembagian TC lintas spec: kolom Name, Role, dan Home Group (TC-FA-SU-9 sampai 11) ada di spec 004.
- Temuan untuk QA:
  - TC-FA-SU-12 Langkah Uji 4 ("Lakukan Activate pada pengguna itu") tidak menjelaskan caranya: sesudah App Access FAMS diberikan, sakelar Active sudah ON (TC-FA-SU-16 Expected a), sehingga Activate sebagai klik sakelar ambigu. Spec menulis "Lakukan Activate" persis seperti TC dan pelaksana skrip menentukan pemicunya.
  - TC-FA-SU-12 Expected e ("Edit No-Op") tidak punya Langkah Uji; spec menambah langkah 17 (Edit Home Group tanpa perubahan) sebagai penghubung.
  - TC-FA-SU-12 Expected c ("kedua kolom baru berubah") tidak menyebut nilai Modified By sesudah aksi; spec mengasersi bukan lagi `System` dan Last Updated berubah.
  - TC-FA-SU-12 Expected d tidak menyebut nilai Date Format dan Time Format General Settings; spec mengasersi mengikuti pengaturan Client.
  - TC-FA-SU-16 langkah 3 (aktivasi akun dari tautan email) tidak merinci langkah aktivasi (pengaturan password) dan password pengguna baru; kebutuhan ditulis sebagai kemampuan "disediakan tim FE" (S-11).
  - TC-FA-SU-16 Expected c ("Pemberian ulang App Access setelah pencabutan") tidak punya Langkah Uji; spec menambah langkah 28 dan 29 sebagai pemicu.
  - TC-FA-SU-16 Expected b ("tidak ada menu fungsional administratif lain") tidak menyebut daftar menu; spec mengasersi dari sisi menu navigasi FAMS pengguna Y.
