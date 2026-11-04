---
id: TC-GS-USER-E2E-149-user-log-note-lock-change-password-dan-account-locked
title: "Tab User Log: Note Lock Change Password 15 Menit, 1 Jam, Perlu Reset, dan Account locked"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-1083
  - TC-GS-USER-1084
  - TC-GS-USER-1085
  - TC-GS-USER-1086
coverage:
  web: automated
---

# Tab User Log: Note Lock Change Password 15 Menit, 1 Jam, Perlu Reset, dan Account locked

## Prerequisites

- Mode: FE+BE (kelas d: manipulasi jam server dan jam browser; counter lock Change Password).
- Hook suite: flag Guided Tooltip `gs-user` = seen (lihat `suite.md`).
- Akun aktor pertama: Total Control (Siti Nurhaliza) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup No. 2; kredensial `Spectra.env.GS_TC_PASSWORD`). Login sekali di hook `before`; hook `after` mengembalikan sesi ke akun default suite (Total Control). Password tidak ditulis di spec atau fixture.
- Env var: `GS_TC_PASSWORD`, `USER_PASSWORD` (password login user uji; memenuhi policy password), `USER_PASSWORD_NEW` (New Password dan Confirm New Password yang memenuhi policy; tidak pernah tersimpan karena Change Password tidak pernah berhasil di spec ini), `USER_PASSWORD_WRONG` (nilai Current Password salah; bukan password user mana pun), semuanya didaftarkan di `executionConfig.environmentVariables`.
- Data Pre-setup (hanya dibaca): akun aktor Siti Nurhaliza (No. 2) di jendela akun aktor. User Pre-setup Dewi Lestari (No. 12) tidak dipakai karena counter lock Change Password-nya diubah spec ini (S-06).
- Data Dinamis milik spec, di-seed lewat API di hook `before` (HK1) dan dihapus di hook `after`, keduanya Activated, MFA Enrolled, Division `Finance`, Access `Global Settings`, password `Spectra.env.USER_PASSWORD`, tanpa riwayat Change Password:
  - `Dewi Lestari {runId}-149`, Email `dewilestari+{runId}-149@qwertysystem.net`: dipakai berurutan oleh TC-GS-USER-1083, 1084, dan 1085 (satu user karena state lock dibangun berurutan, P-3).
  - `Dewi Lestari B {runId}-149`, Email `dewilestarib+{runId}-149@qwertysystem.net`: dipakai TC-GS-USER-1086 (tidak boleh berada pada tier wajib-reset, sehingga tidak memakai user di atas).
- Dua jendela: jendela akun aktor (Total Control, hanya membaca Tab User Log) dan jendela user uji (jendela privat berisi sesi user uji). Jendela user uji ditutup dan sesi login browser terkait dihapus sebelum jendela user uji berikutnya dibuka (S-09).
- Kemampuan teknis, disediakan tim FE/BE (TC, PRD, dan LLD tidak menyebut cara atau endpoint): (1) sesi login user seed yang memenuhi MFA (kode authenticator); (2) reCAPTCHA pada Login with Password dapat diselesaikan di environment automation; (3) manipulasi jam: jam server dan jam browser diatur bersama ke nilai absolut atau dibekukan, dan dipulihkan ke waktu nyata; (4) seeding user lewat API tanpa riwayat Change Password; (5) membaca jumlah baris hasil Search Tab User Log (`{nCPA0}`, `{nCPB0}`, dan jumlah pada asersi selisih) dari indikator jumlah baris pada footer pagination Tab User Log; bila footer tidak menampilkan total, kemampuan baca jumlah entri log per user dan Note lewat BE disediakan tim FE/BE (TC, PRD, dan LLD tidak menyebut cara). Sumber baca yang sama dipakai untuk baseline dan asersi (langkah 3, 19, 39, 59, 65, 104).
- Jam dan lock (PRD `auth-foundation.md` §3 dan §9.1 Tabel G, PRD My Profile `PROFILE-LOGIC-07`): counter Current Password salah dipisah dari counter Login; percobaan salah ke-3 menghasilkan lock 15 menit, ke-6 lock 1 jam, ke-9 lock wajib reset; hitungan per hari yang sama kecuali tier wajib-reset; bila 7 hari berturut-turut mencapai lock 1 jam, percobaan salah pertama hari ke-8 langsung menghasilkan Note `Account locked (change password)`. Jam dibekukan pada nilai absolut sebelum percobaan pertama tiap tahap sehingga waktu lock sama dengan nilai beku. Nilai awal TC-GS-USER-1083: `{tA1}` = 09:00 zona waktu server pada tanggal besok (menghindari batas hari saat tahap berjalan); tahap berikutnya: `{tA2}` = `{tA1}` + 15 menit + 60 detik, `{tA3}` = `{tA2}` + 60 menit + 60 detik. Margin 60 detik di atas masa lock (di bawah 5 menit) dihitung dari nilai beku tahap sebelumnya, bukan dari waktu hook. TC-GS-USER-1086: hari ke-d (d = 1 sampai 7) dimulai pada `{Dd}` = 09:00 zona waktu server pada tanggal hari ini + d hari, tahap kedua hari itu pada `{Dd}` + 15 menit + 60 detik; hari ke-8 pada `{D8}` = 09:00 zona waktu server pada tanggal hari ini + 8 hari. Batas hari mengikuti zona waktu server (sumber tidak menyebut zona waktu hitungan harian).
- Jam server dan jam browser dipulihkan ke waktu nyata lewat langkah aksi sebelum jendela akun aktor membuka Tab User Log (S-09); hook `after` memulihkan jam sebagai cadangan. Log yang dibuat saat jam digeser bercap waktu masa depan, sehingga asersi memakai selisih jumlah baris terhadap baseline dan pencarian Note, bukan posisi teratas (S-12).
- State global yang diubah: jam server dan jam browser; counter dan lock Change Password dua user uji. Suite berjalan serial (`suite.md`). Hook `after` memulihkan jam, menutup jendela user uji, dan menghapus kedua user uji.
- Baris log dikenali lewat Search Note pada Tab User Log user seed bersuffix `{runId}-149` yang unik per run dan tanpa riwayat Change Password (baseline nol), bukan lewat penanda waktu (S-12). Jumlah baris `Incorrect current password` TC-GS-USER-1083 sampai 1085 bersifat kumulatif pada satu user (2, 4, lalu 6); baseline jumlah baris Activity `Change Password` (`{nCPA0}` dan `{nCPB0}`) dicatat dari Tab User Log user uji sebelum aksi untuk asersi selisih.
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus lewat API kedua user uji bersuffix `{runId}-149`. Hook `before` menghapus sisa user bersuffix `-149` dari run lama. Entri log bersifat immutable dan tidak dihapus.

## Test Steps

### Pembukaan layar dan baseline TC-GS-USER-1083

1. Di jendela akun aktor, buka Global Settings > User > User List (sub-tab Login User)
2. Di jendela akun aktor, buka Global Settings > User > User List, klik icon Search, ketik `Dewi Lestari {runId}-149`, tekan Enter, klik Name `Dewi Lestari {runId}-149`, buka Tab User Log, klik icon Search, ketik `Change Password`, tekan Enter
3. Catat jumlah baris hasil Search (dibaca dari footer pagination atau kemampuan baca yang disediakan tim FE/BE, lihat Prerequisites) sebagai `{nCPA0}`

### TC-GS-USER-1083: Note Locked 15 minutes (change password)

4. Atur jam server dan jam browser bersama ke nilai absolut `{tA1}` = 09:00 zona waktu server pada tanggal besok (dibekukan)
5. Buka jendela user uji (jendela privat), buka Login with Password, isi Email `dewilestari+{runId}-149@qwertysystem.net` dan Password `Spectra.env.USER_PASSWORD`, selesaikan reCAPTCHA, klik [Log in]
6. Selesaikan verifikasi MFA user uji (kode authenticator disediakan tim FE/BE)
7. Tunggu aksi selesai (Portal - Product Hub tampil)
8. Di jendela user uji, buka Global Settings > My Profile, klik [Change Password]
9. Isi Current Password `Spectra.env.USER_PASSWORD_WRONG` (salah; bukan password aktif), New Password `Spectra.env.USER_PASSWORD_NEW`, dan Confirm New Password `Spectra.env.USER_PASSWORD_NEW`
10. Klik [Save] (percobaan salah ke-1)
11. Tunggu aksi selesai (modal Change Password tetap terbuka)
12. Klik [Save] (percobaan salah ke-2)
13. Tunggu aksi selesai (modal Change Password tetap terbuka)
14. Klik [Save] (percobaan salah ke-3, lock 15 menit)
15. Tunggu aksi selesai (modal Change Password tetap terbuka)
16. Tutup jendela user uji dan hapus sesi login browser terkait
17. Pulihkan jam server dan jam browser ke waktu nyata
18. Di jendela akun aktor, buka Global Settings > User > User List, klik icon Search, ketik `Dewi Lestari {runId}-149`, tekan Enter, klik Name `Dewi Lestari {runId}-149`, buka Tab User Log, klik icon Search, ketik `Change Password`, tekan Enter
19. Verifikasi hasil Search `Change Password` pada Tab User Log `Dewi Lestari {runId}-149`: jumlah baris Activity `Change Password` bertambah tepat 3 dari `{nCPA0}` (selisih terhadap baseline)
20. Ganti isi kotak search dengan `Locked 15 minutes (change password)`
21. Verifikasi Tab User Log `Dewi Lestari {runId}-149` memuat baris dengan Activity `Change Password`, Status `Failed`, Note `Locked 15 minutes (change password)`
22. Ganti isi kotak search dengan `Incorrect current password`
23. Verifikasi hasil Search `Incorrect current password` pada Tab User Log `Dewi Lestari {runId}-149` memuat tepat 2 baris (percobaan sebelum lock); event lock tidak diganti menjadi Note `Incorrect current password`

### TC-GS-USER-1084: Note Locked 1 hour (change password)

24. Atur jam server dan jam browser bersama ke nilai absolut `{tA2}` = `{tA1}` + 15 menit + 60 detik (dibekukan)
25. Buka jendela user uji (jendela privat), buka Login with Password, isi Email `dewilestari+{runId}-149@qwertysystem.net` dan Password `Spectra.env.USER_PASSWORD`, selesaikan reCAPTCHA, klik [Log in]
26. Selesaikan verifikasi MFA user uji (kode authenticator disediakan tim FE/BE)
27. Tunggu aksi selesai (Portal - Product Hub tampil)
28. Di jendela user uji, buka Global Settings > My Profile, klik [Change Password]
29. Isi Current Password `Spectra.env.USER_PASSWORD_WRONG` (salah; bukan password aktif), New Password `Spectra.env.USER_PASSWORD_NEW`, dan Confirm New Password `Spectra.env.USER_PASSWORD_NEW`
30. Klik [Save] (percobaan salah ke-4)
31. Tunggu aksi selesai (modal Change Password tetap terbuka)
32. Klik [Save] (percobaan salah ke-5)
33. Tunggu aksi selesai (modal Change Password tetap terbuka)
34. Klik [Save] (percobaan salah ke-6, lock 1 jam)
35. Tunggu aksi selesai (modal Change Password tetap terbuka)
36. Tutup jendela user uji dan hapus sesi login browser terkait
37. Pulihkan jam server dan jam browser ke waktu nyata
38. Di jendela akun aktor, buka Global Settings > User > User List, klik icon Search, ketik `Dewi Lestari {runId}-149`, tekan Enter, klik Name `Dewi Lestari {runId}-149`, buka Tab User Log, klik icon Search, ketik `Change Password`, tekan Enter
39. Verifikasi hasil Search `Change Password` pada Tab User Log `Dewi Lestari {runId}-149`: jumlah baris Activity `Change Password` bertambah tepat 6 dari `{nCPA0}` (selisih terhadap baseline)
40. Ganti isi kotak search dengan `Locked 1 hour (change password)`
41. Verifikasi Tab User Log `Dewi Lestari {runId}-149` memuat baris dengan Activity `Change Password`, Status `Failed`, Note `Locked 1 hour (change password)`
42. Ganti isi kotak search dengan `Incorrect current password`
43. Verifikasi hasil Search `Incorrect current password` pada Tab User Log `Dewi Lestari {runId}-149` memuat tepat 4 baris (percobaan sebelum lock); event lock tidak diganti menjadi Note `Incorrect current password`

### TC-GS-USER-1085: Note Locked requires reset (change password)

44. Atur jam server dan jam browser bersama ke nilai absolut `{tA3}` = `{tA2}` + 60 menit + 60 detik (dibekukan)
45. Buka jendela user uji (jendela privat), buka Login with Password, isi Email `dewilestari+{runId}-149@qwertysystem.net` dan Password `Spectra.env.USER_PASSWORD`, selesaikan reCAPTCHA, klik [Log in]
46. Selesaikan verifikasi MFA user uji (kode authenticator disediakan tim FE/BE)
47. Tunggu aksi selesai (Portal - Product Hub tampil)
48. Di jendela user uji, buka Global Settings > My Profile, klik [Change Password]
49. Isi Current Password `Spectra.env.USER_PASSWORD_WRONG` (salah; bukan password aktif), New Password `Spectra.env.USER_PASSWORD_NEW`, dan Confirm New Password `Spectra.env.USER_PASSWORD_NEW`
50. Klik [Save] (percobaan salah ke-7)
51. Tunggu aksi selesai (modal Change Password tetap terbuka)
52. Klik [Save] (percobaan salah ke-8)
53. Tunggu aksi selesai (modal Change Password tetap terbuka)
54. Klik [Save] (percobaan salah ke-9, lock wajib reset)
55. Tunggu aksi selesai (modal Change Password tetap terbuka)
56. Tutup jendela user uji dan hapus sesi login browser terkait
57. Pulihkan jam server dan jam browser ke waktu nyata
58. Di jendela akun aktor, buka Global Settings > User > User List, klik icon Search, ketik `Dewi Lestari {runId}-149`, tekan Enter, klik Name `Dewi Lestari {runId}-149`, buka Tab User Log, klik icon Search, ketik `Change Password`, tekan Enter
59. Verifikasi hasil Search `Change Password` pada Tab User Log `Dewi Lestari {runId}-149`: jumlah baris Activity `Change Password` bertambah tepat 9 dari `{nCPA0}` (selisih terhadap baseline)
60. Ganti isi kotak search dengan `Locked requires reset (change password)`
61. Verifikasi Tab User Log `Dewi Lestari {runId}-149` memuat baris dengan Activity `Change Password`, Status `Failed`, Note `Locked requires reset (change password)`
62. Ganti isi kotak search dengan `Incorrect current password`
63. Verifikasi hasil Search `Incorrect current password` pada Tab User Log `Dewi Lestari {runId}-149` memuat tepat 6 baris (percobaan sebelum lock); event lock tidak diganti menjadi Note `Incorrect current password`

### TC-GS-USER-1086: Note Account locked (change password) setelah 7 hari berturut-turut mencapai lock 1 jam

64. Di jendela akun aktor, buka Global Settings > User > User List, klik icon Search, ketik `Dewi Lestari B {runId}-149`, tekan Enter, klik Name `Dewi Lestari B {runId}-149`, buka Tab User Log, klik icon Search, ketik `Change Password`, tekan Enter
65. Catat jumlah baris hasil Search (sumber baca sama dengan langkah 3, lihat Prerequisites) sebagai `{nCPB0}`
66. Atur jam server dan jam browser bersama ke nilai absolut `{Dd}` = 09:00 zona waktu server pada tanggal hari ini + d hari (d = 1 untuk hari ke-1) (dibekukan)
67. Buka jendela user uji (jendela privat), buka Login with Password, isi Email `dewilestarib+{runId}-149@qwertysystem.net` dan Password `Spectra.env.USER_PASSWORD`, selesaikan reCAPTCHA, klik [Log in]
68. Selesaikan verifikasi MFA user uji (kode authenticator disediakan tim FE/BE)
69. Tunggu aksi selesai (Portal - Product Hub tampil)
70. Di jendela user uji, buka Global Settings > My Profile, klik [Change Password]
71. Isi Current Password `Spectra.env.USER_PASSWORD_WRONG` (salah; bukan password aktif), New Password `Spectra.env.USER_PASSWORD_NEW`, dan Confirm New Password `Spectra.env.USER_PASSWORD_NEW`
72. Klik [Save] (percobaan salah ke-1 hari ke-d)
73. Tunggu aksi selesai (modal Change Password tetap terbuka)
74. Klik [Save] (percobaan salah ke-2 hari ke-d)
75. Tunggu aksi selesai (modal Change Password tetap terbuka)
76. Klik [Save] (percobaan salah ke-3 hari ke-d, lock 15 menit)
77. Tunggu aksi selesai (modal Change Password tetap terbuka)
78. Tutup jendela user uji dan hapus sesi login browser terkait
79. Atur jam server dan jam browser bersama ke nilai absolut `{Dd}` + 15 menit + 60 detik (dibekukan)
80. Buka jendela user uji (jendela privat), buka Login with Password, isi Email `dewilestarib+{runId}-149@qwertysystem.net` dan Password `Spectra.env.USER_PASSWORD`, selesaikan reCAPTCHA, klik [Log in]
81. Selesaikan verifikasi MFA user uji (kode authenticator disediakan tim FE/BE)
82. Tunggu aksi selesai (Portal - Product Hub tampil)
83. Di jendela user uji, buka Global Settings > My Profile, klik [Change Password]
84. Isi Current Password `Spectra.env.USER_PASSWORD_WRONG` (salah; bukan password aktif), New Password `Spectra.env.USER_PASSWORD_NEW`, dan Confirm New Password `Spectra.env.USER_PASSWORD_NEW`
85. Klik [Save] (percobaan salah ke-4 hari ke-d)
86. Tunggu aksi selesai (modal Change Password tetap terbuka)
87. Klik [Save] (percobaan salah ke-5 hari ke-d)
88. Tunggu aksi selesai (modal Change Password tetap terbuka)
89. Klik [Save] (percobaan salah ke-6 hari ke-d, lock 1 jam)
90. Tunggu aksi selesai (modal Change Password tetap terbuka)
91. Tutup jendela user uji dan hapus sesi login browser terkait
92. Ulangi langkah 66 sampai 91 untuk hari ke-2 sampai hari ke-7 (d = 2 sampai 7), satu hari berurutan setelah hari sebelumnya
93. Atur jam server dan jam browser bersama ke nilai absolut `{D8}` = 09:00 zona waktu server pada tanggal hari ini + 8 hari (dibekukan)
94. Buka jendela user uji (jendela privat), buka Login with Password, isi Email `dewilestarib+{runId}-149@qwertysystem.net` dan Password `Spectra.env.USER_PASSWORD`, selesaikan reCAPTCHA, klik [Log in]
95. Selesaikan verifikasi MFA user uji (kode authenticator disediakan tim FE/BE)
96. Tunggu aksi selesai (Portal - Product Hub tampil)
97. Di jendela user uji, buka Global Settings > My Profile, klik [Change Password]
98. Isi Current Password `Spectra.env.USER_PASSWORD_WRONG` (salah; bukan password aktif), New Password `Spectra.env.USER_PASSWORD_NEW`, dan Confirm New Password `Spectra.env.USER_PASSWORD_NEW`
99. Klik [Save] (percobaan salah pertama hari ke-8)
100. Tunggu aksi selesai (modal Change Password tetap terbuka)
101. Tutup jendela user uji dan hapus sesi login browser terkait
102. Pulihkan jam server dan jam browser ke waktu nyata
103. Di jendela akun aktor, buka Global Settings > User > User List, klik icon Search, ketik `Dewi Lestari B {runId}-149`, tekan Enter, klik Name `Dewi Lestari B {runId}-149`, buka Tab User Log, klik icon Search, ketik `Change Password`, tekan Enter
104. Verifikasi hasil Search `Change Password` pada Tab User Log `Dewi Lestari B {runId}-149`: jumlah baris Activity `Change Password` bertambah tepat 43 dari `{nCPB0}` (7 hari x 6 percobaan, ditambah 1 percobaan hari ke-8)
105. Ganti isi kotak search dengan `Account locked (change password)`
106. Verifikasi Tab User Log `Dewi Lestari B {runId}-149` memuat tepat 1 baris dengan Activity `Change Password`, Status `Failed`, Note `Account locked (change password)`
107. Ganti isi kotak search dengan `Incorrect current password`
108. Verifikasi hasil Search `Incorrect current password` pada Tab User Log `Dewi Lestari B {runId}-149` memuat tepat 28 baris (4 percobaan per hari selama 7 hari); percobaan hari ke-8 tidak diganti menjadi Note `Incorrect current password`

## Notes

- Mode: FE+BE. Sumber: `global-settings/user/TestCases/tc-user.md`, `auth/_foundation/auth-foundation.md` §3 dan §9.1 Tabel G, `global-settings/my-profile/PRD/my-profile.md` `PROFILE-LOGIC-07`.
- P-3 (user berurutan): TC-GS-USER-1083, 1084, dan 1085 memakai satu user karena lock 15 menit, 1 jam, dan wajib reset dibangun berurutan dari counter yang sama dan tidak dapat diulang tanpa biaya besar. TC-GS-USER-1086 memakai user kedua karena tier wajib-reset pada user pertama menahan counter lintas hari.
- Urutan TC di spec: 1083, 1084, 1085, 1086 (urutan sumber).
- TC sumber menulis "Fixture User Log" berisi event Auth; TC dan PRD tidak menyebut mekanisme fixture. Spec membangun event yang sama lewat alur Auth yang menghasilkannya: Change Password dengan Current Password salah berulang pada jam yang dibekukan (progression: `auth-foundation.md` §3; Note: Tabel G). Sumber event tetap pemilik Auth; Tab User Log hanya diamati.
- Blok hari TC-GS-USER-1086 ditulis sekali dan diulang untuk hari ke-2 sampai hari ke-7 (langkah pengulangan menyebut rentang langkah); satu hari berisi enam percobaan salah di dua tahap (lock 15 menit lalu lock 1 jam). Jumlah akhir 43 baris = 7 x 6 + 1; 28 baris `Incorrect current password` = 7 x 4.
- Asersi Expected Result "tidak diganti menjadi Incorrect current password" ditulis sebagai jumlah baris `Incorrect current password` (hanya percobaan sebelum lock), karena baris lock tidak boleh menjadi salah satunya.
- Langkah penghubung (aksi tanpa `Verifikasi`): pencatatan jumlah baris baseline, pembekuan dan pemulihan jam, membuka dan menutup jendela user uji, Login with Password dan MFA, My Profile > [Change Password] dan pengisian field, [Save] percobaan salah dan "Tunggu aksi selesai" (8b butir 8), serta pembukaan Tab User Log beserta Search di jendela akun aktor. Hasil tiap percobaan (inline error, toast lock) tidak diasersi karena bukan Expected Result TC.
- Spec melewati sekitar 35 langkah karena empat TC berada dalam satu kelas harness (d: manipulasi jam), satu pola (membangun lock lalu membaca Tab User Log), dan blok TC-GS-USER-1086 butuh tujuh hari berturut-turut; blok 1083 sampai 1085 bergantung berurutan pada satu user (P-3), sedangkan blok 1086 berdiri sendiri. Memecahnya melipatgandakan hook seeding, login MFA, dan pembekuan jam tanpa mengubah makna.
- Sumber pembacaan jumlah baris (baseline langkah 3 dan 65, asersi selisih langkah 19, 39, 59, 104, dan jumlah tepat langkah 23, 43, 63, 108) satu: indikator jumlah baris pada footer pagination Tab User Log, atau kemampuan baca yang disediakan tim FE/BE bila footer tidak menampilkan total; spec tidak mengandaikan kemampuan UI baru.
- Temuan untuk QA:
  - TC-GS-USER-1083 sampai 1086: Langkah Uji 3 menyebut "Method" sedangkan kolom Tab User Log bernama "Activity" (PRD `user.md` §4.1.7); spec memakai nama kolom Activity.
  - TC-GS-USER-1083 sampai 1086: Precondition "Fixture User Log ... IP dan device metadata sesuai pemilik Auth" tidak menyebut mekanisme fixture; nilai IP Address dan Device / Browser event tidak diasersi karena bukan Expected Result.
  - TC-GS-USER-1086: kondisi "Account locked" butuh 7 hari berturut-turut mencapai lock 1 jam (`auth-foundation.md` §3, eskalasi 7 hari) yang tidak disebut TC; zona waktu hitungan harian tidak disebut sumber, spec memakai zona waktu server.
  - TC-GS-USER-1083 sampai 1086: Post Condition "Tidak ada mutasi log" tidak punya langkah observasi di TC sehingga tidak diasersi.
  - TC-GS-USER-1083 sampai 1086: Precondition "Login sebagai Total Control di entitas Dewi Lestari" hanya berlaku untuk jendela akun aktor; aksi user uji dilakukan di jendela terpisah yang tidak disebut TC.
