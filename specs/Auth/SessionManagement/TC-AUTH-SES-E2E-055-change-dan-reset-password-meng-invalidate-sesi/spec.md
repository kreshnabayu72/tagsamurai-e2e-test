---
id: TC-AUTH-SES-E2E-055-change-dan-reset-password-meng-invalidate-sesi
title: "Change Password dan Reset Password Meng-invalidate Sesi Aktif Lintas Web dan Mobile"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-SES-182
  - TC-AUTH-SES-183
  - TC-AUTH-SES-184
  - TC-AUTH-SES-185
  - TC-AUTH-SES-186
  - TC-AUTH-SES-187
  - TC-AUTH-SES-188
  - TC-AUTH-SES-264
coverage:
  web: automated
  mobile: automated
---

# Change Password dan Reset Password Meng-invalidate Sesi Aktif Lintas Web dan Mobile

## Prerequisites

- Mode: FE+BE.
- Seeding (hook `before`, lewat API oleh akun aktor Total Control (Global Settings) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.GS_TC_PASSWORD`; scope Client Alpha Logistik: Tabel Data Uji Pre-setup #1, scope Client Q2 untuk user milik Client Q2: Tabel Data Uji Pre-setup #26): delapan user profil BASE (Tabel Data Uji Pre-setup #5 dan #12: Activated, Active ON, MFA dan Agreement tidak terpicu), password `Spectra.env.SES_PASSWORD`, email bersuffix per run. Sesi web aktif dibuat lewat login API di konteks Browser A (Chrome on Windows) dan sesi mobile aktif lewat login mobile pada perangkat Android uji A (Tabel Data Uji Pre-setup #10; cara menyiapkan: Pre-setup #28), semuanya berstatus Active:
  - TC-AUTH-SES-186: `Hendra Wulandari` (`hendrawulandari+{runId}-055@qwertysystem.net`), Client Alpha Logistik; sesi web dan sesi mobile
  - TC-AUTH-SES-187: `Maya Hidayat` (`mayahidayat+{runId}-055@qwertysystem.net`), Client Alpha Logistik; sesi mobile; link reset password milik user ini kedaluwarsa, disediakan BE uji (precondition c TC-AUTH-SES-187; Tabel Data Uji Pre-setup #18), dan tautannya terbaca di mail-catcher (Tabel Data Uji Pre-setup #19)
  - TC-AUTH-SES-182: `Rizky Permata` (`rizkypermata+{runId}-055@qwertysystem.net`), Client Alpha Logistik; sesi web dan sesi mobile
  - TC-AUTH-SES-183: `Nur Lestari` (`nurlestari+{runId}-055@qwertysystem.net`), Client Alpha Logistik; sesi web dan sesi mobile (langkah dependensi TC-AUTH-SES-182 disalin di spec)
  - TC-AUTH-SES-188: `Fajar Utami` (`fajarutami+{runId}-055@qwertysystem.net`), Client Alpha Logistik; sesi web dan sesi mobile
  - TC-AUTH-SES-185: `Rina Ramadhan` (`rinaramadhan+{runId}-055@qwertysystem.net`), Client Q2 (Tabel Data Uji Pre-setup #12: subscription Fixed Asset dan Supply Asset Active, kuota 2) dengan App Access Fixed Asset dan Supply Asset; sesi web, sesi mobile, dan sesi-produk Fixed Asset Active yang dipakai sesi mobile (seat terpakai 1)
  - TC-AUTH-SES-184: `Agus Pratama` (`aguspratama+{runId}-055@qwertysystem.net`), Client Alpha Logistik; sesi web dan sesi mobile; Browser C belum login
  - TC-AUTH-SES-264: `Galih Saputra` (`galihsaputra+{runId}-055@qwertysystem.net`), Client Q2 dengan App Access Fixed Asset dan Supply Asset; sesi mobile dan sesi-produk Fixed Asset Active yang dipakai sesi mobile
- Konteks dan akun (dibuka di hook `before`, login pertama tiap konteks ada di hook):
  - Browser Admin: akun aktor Total Control (Global Settings) dengan scope Client Q2 (Tabel Data Uji Pre-setup #26; user yang log-nya dibaca, `Rina Ramadhan` dan `Galih Saputra`, milik Client Q2), dipakai membaca `Global Settings > Activity Log > Session`, `Activity Log > Session` milik Fixed Asset, dan `Global Settings > User > Detail > User Log`.
  - Browser License: akun aktor `manageGlobalLicenseFixedAsset_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup #2 dan #33: Global Role Manage Global License, scope Client Q2 dan Client Alpha), kredensial `Spectra.env.FA_MGL_PASSWORD`, dipakai membaca `PLATFORM SETTINGS > License > Concurrent User` (Fixed Asset).
  - Browser A (sesi web user uji; memuat sesi web seed milik user TC yang sedang berjalan), Browser C (konteks bersih tanpa login, halaman publik), dan perangkat Android uji A (aplikasi mobile TAG Samurai).
- Password: password lama user uji `Spectra.env.SES_PASSWORD`; password baru hasil Change Password atau Reset Password `Spectra.env.SES_PASSWORD_NEW`. Input Current Password yang salah pada TC-AUTH-SES-186 adalah literal uji karena submit-nya ditolak.
- Hook `after`: akhiri semua sesi seed (web, mobile, sesi-produk), tutup konteks Browser A, Browser C, Browser License, dan Browser Admin, hapus kedelapan user, dan bersihkan token reset seed milik `Maya Hidayat`. Pembersihan tidak berasumsi seeding berhasil penuh.
- Environment variable: `GS_TC_PASSWORD`, `FA_MGL_PASSWORD`, `SES_PASSWORD`, `SES_PASSWORD_NEW`. Password tidak ditulis di spec atau fixture.
- Suite berjalan serial (`parallel: false`); state global yang diubah: seat Fixed Asset Client Q2 (kuota 2) diisi sesi-produk seed (`Rina Ramadhan` dan `Galih Saputra`, masing-masing 1 seat), dipulihkan di hook `after`; perangkat fisik Android uji A dipakai bersama oleh user antar-TC.
- Kemampuan teknis: tiga konteks browser tambahan bersamaan dengan Browser A (Browser C, Browser License, Browser Admin); driver otomasi Android (aplikasi native) pada perangkat Android uji A yang dipakai bergantian oleh user antar-TC (tiap TC memuat sesi mobile milik user TC itu di aplikasi); mail-catcher lingkungan uji untuk membaca email reset password; link reset password kedaluwarsa yang disediakan BE uji tanpa menggeser jam server (jam server tidak digeser di spec ini karena idle sesi mobile ikut berubah); reCAPTCHA mode uji di environment (halaman Reset Password).
- Akun yang dipakai: user uji masing-masing TC (bukan akun aktor) di Browser A, Browser C, dan perangkat Android uji A; akun aktor di Browser Admin dan Browser License.

## Test Steps

### TC-AUTH-SES-186: Change Password gagal tidak meng-invalidate sesi lain

1. Tutup konteks Browser A sebelumnya dan buka konteks baru Browser A dengan memuat sesi web seed milik `Hendra Wulandari`
2. Di Browser A (sesi web Active `Hendra Wulandari`) buka `Global Settings > My Profile > Change Password` → modal Change Password tampil
3. Ketik `Salah#Password1` pada field Current Password
4. Ketik `Spectra.env.SES_PASSWORD_NEW` pada field New Password
5. Ketik `Spectra.env.SES_PASSWORD_NEW` pada field Confirm New Password
6. Klik [Save]
7. Verifikasi Change Password ditolak oleh modul My Profile
8. Klik [Cancel] pada modal Change Password
9. Tutup aplikasi sebelumnya di perangkat Android uji A dan buka aplikasi dengan memuat sesi mobile seed milik `Hendra Wulandari`
10. Di perangkat Android uji A (aplikasi memuat sesi mobile Active `Hendra Wulandari`) ketuk layar
11. Verifikasi Sesi mobile tetap Active
12. Verifikasi Tidak ada dialog di perangkat A
13. Di Browser A amati halaman tanpa interaksi
14. Verifikasi Sesi web tetap Active

### TC-AUTH-SES-187: Reset Password gagal karena link kedaluwarsa tidak meng-invalidate sesi aktif

15. Di Browser C buka link reset yang kedaluwarsa milik `Maya Hidayat` (dari mail-catcher) dan coba kirim password baru `Spectra.env.SES_PASSWORD_NEW`
16. Verifikasi Reset Password ditolak
17. Tutup aplikasi sebelumnya di perangkat Android uji A dan buka aplikasi dengan memuat sesi mobile seed milik `Maya Hidayat`
18. Di perangkat Android uji A (aplikasi memuat sesi mobile Active `Maya Hidayat`) ketuk layar
19. Verifikasi Sesi mobile tetap Active
20. Verifikasi Tidak ada dialog di perangkat A

### TC-AUTH-SES-182: Change Password sukses meng-invalidate sesi lain dan sesi pemicu tetap aktif

21. Tutup konteks Browser A sebelumnya dan buka konteks baru Browser A dengan memuat sesi web seed milik `Rizky Permata`
22. Di Browser A (sesi web Active `Rizky Permata`, Chrome on Windows) buka `Global Settings > My Profile > Change Password` → modal Change Password tampil
23. Ketik `Spectra.env.SES_PASSWORD` pada field Current Password
24. Ketik `Spectra.env.SES_PASSWORD_NEW` pada field New Password
25. Ketik `Spectra.env.SES_PASSWORD_NEW` pada field Confirm New Password
26. Klik [Save] → password berhasil diubah
27. Di Browser A klik menu lain
28. Verifikasi Sesi web di Browser A tetap Active
29. Tutup aplikasi sebelumnya di perangkat Android uji A dan buka aplikasi dengan memuat sesi mobile seed milik `Rizky Permata`
30. Di perangkat Android uji A (aplikasi memuat sesi mobile Active `Rizky Permata`) ketuk layar → Dialog muncul
31. Verifikasi Sesi mobile berstatus Force Logged Out
32. Verifikasi Perangkat A menampilkan Dialog Password Changed

### TC-AUTH-SES-183: OK pada Dialog Password Changed langsung mengarah ke Login tanpa cek ulang sesi

33. Tutup konteks Browser A sebelumnya dan buka konteks baru Browser A dengan memuat sesi web seed milik `Nur Lestari`
34. Di Browser A (sesi web Active `Nur Lestari`) buka `Global Settings > My Profile > Change Password` → modal Change Password tampil
35. Ketik `Spectra.env.SES_PASSWORD` pada field Current Password
36. Ketik `Spectra.env.SES_PASSWORD_NEW` pada field New Password
37. Ketik `Spectra.env.SES_PASSWORD_NEW` pada field Confirm New Password
38. Klik [Save] → password berhasil diubah
39. Tutup aplikasi sebelumnya di perangkat Android uji A dan buka aplikasi dengan memuat sesi mobile seed milik `Nur Lestari`
40. Di perangkat Android uji A (aplikasi memuat sesi mobile Active `Nur Lestari`) ketuk layar → Dialog Password Changed tampil
41. Ketuk [OK]
42. Verifikasi App diarahkan ke halaman Login penuh
43. Verifikasi Tanpa pengecekan sesi ulang (bukan perilaku Refresh)
44. Verifikasi Screen biometric sign-in tidak tampil karena token lokal dihapus saat Dialog Password Changed tampil

### TC-AUTH-SES-188: Change Password dua kali berturut-turut bersifat idempotent terhadap sesi lain

45. Tutup konteks Browser A sebelumnya dan buka konteks baru Browser A dengan memuat sesi web seed milik `Fajar Utami`
46. Di Browser A (sesi web Active `Fajar Utami`) buka `Global Settings > My Profile > Change Password` → modal Change Password tampil
47. Ketik `Spectra.env.SES_PASSWORD` pada field Current Password
48. Ketik `Spectra.env.SES_PASSWORD_NEW` pada field New Password
49. Ketik `Spectra.env.SES_PASSWORD_NEW` pada field Confirm New Password
50. Klik [Save] → password berhasil diubah
51. Segera buka lagi `Global Settings > My Profile > Change Password` → modal Change Password tampil
52. Ketik `Spectra.env.SES_PASSWORD_NEW` pada field Current Password
53. Ketik `Spectra.env.SES_PASSWORD` pada field New Password
54. Ketik `Spectra.env.SES_PASSWORD` pada field Confirm New Password
55. Klik [Save] → password berhasil diubah
56. Tutup aplikasi sebelumnya di perangkat Android uji A dan buka aplikasi dengan memuat sesi mobile seed milik `Fajar Utami`
57. Di perangkat Android uji A (aplikasi memuat sesi mobile Active `Fajar Utami`) ketuk layar → Dialog muncul
58. Verifikasi Sesi mobile berstatus Force Logged Out satu kali
59. Verifikasi Tidak ada error tambahan di Browser A maupun di perangkat A
60. Verifikasi Sesi web di Browser A tetap Active

### TC-AUTH-SES-185: Sesi-produk anak dari sesi yang di-invalidate ikut berakhir dan seat dilepas

61. Di Browser License buka `PLATFORM SETTINGS > License > Concurrent User` (Fixed Asset) dan catat hitungan seat aktif serta keberadaan baris `Rina Ramadhan`
62. Tutup konteks Browser A sebelumnya dan buka konteks baru Browser A dengan memuat sesi web seed milik `Rina Ramadhan`
63. Di Browser A (sesi web Active `Rina Ramadhan`) buka `Global Settings > My Profile > Change Password` → modal Change Password tampil
64. Ketik `Spectra.env.SES_PASSWORD` pada field Current Password
65. Ketik `Spectra.env.SES_PASSWORD_NEW` pada field New Password
66. Ketik `Spectra.env.SES_PASSWORD_NEW` pada field Confirm New Password
67. Klik [Save] → password berhasil diubah
68. Di Browser License muat ulang `PLATFORM SETTINGS > License > Concurrent User` (Fixed Asset) dan periksa daftar sesi aktif serta hitungan seat
69. Verifikasi Sesi-produk Fixed Asset `Rina Ramadhan` berstatus Ended
70. Verifikasi Seat Sesi-produk Fixed Asset `Rina Ramadhan` dilepas
71. Verifikasi Di `PLATFORM SETTINGS > License > Concurrent User` (Fixed Asset) baris `Rina Ramadhan` hilang
72. Verifikasi Hitungan seat aktif berkurang 1 dibanding hitungan yang dicatat di langkah 61
73. Di Browser Admin buka `Global Settings > Activity Log > Session` dan cari entri `Rina Ramadhan` yang dibuat sesudah langkah 63 dimulai
74. Verifikasi Tercatat `Logged out (password changed)` untuk sesi platform yang berakhir
75. Di Browser Admin buka `Activity Log > Session` milik Fixed Asset dan cari entri `Rina Ramadhan` yang dibuat sesudah langkah 63 dimulai
76. Verifikasi Tercatat `Session ended` untuk sesi-produk anak di `Activity Log > Session` milik Fixed Asset
77. Buka `Global Settings > User > Detail > User Log` milik `Rina Ramadhan` dan cari entri yang dibuat sesudah langkah 63 dimulai
78. Verifikasi Tercatat `Session ended (Fixed Asset)` untuk sesi-produk anak di `Global Settings > User > Detail > User Log`

### TC-AUTH-SES-184: Reset Password dari device yang belum login meng-invalidate semua sesi aktif

79. Tutup konteks Browser C TC sebelumnya (hapus sesi login browser), buka konteks baru Browser C (belum login)
80. Di Browser C buka halaman `Auth > Reset Password` → halaman Reset Password (Request) tampil
81. Ketik `aguspratama+{runId}-055@qwertysystem.net` pada field Email
82. Centang widget reCAPTCHA "I'm not a robot"
83. Klik [Reset Password] → halaman Email Sent! tampil
84. Buka mail-catcher, ambil email reset untuk `aguspratama+{runId}-055@qwertysystem.net`, lalu klik tautan reset → halaman Setup New Password tampil
85. Ketik `Spectra.env.SES_PASSWORD_NEW` pada field New Password
86. Ketik `Spectra.env.SES_PASSWORD_NEW` pada field Confirm Password
87. Klik [Reset Password] → Password Reset Successful tampil
88. Tutup konteks Browser A sebelumnya dan buka konteks baru Browser A dengan memuat sesi web seed milik `Agus Pratama`
89. Di Browser A (sesi web Active `Agus Pratama`) klik menu apa pun → Dialog muncul
90. Verifikasi Sesi web berstatus Force Logged Out
91. Verifikasi Browser A menampilkan Dialog "Password Changed"
92. Tutup aplikasi sebelumnya di perangkat Android uji A dan buka aplikasi dengan memuat sesi mobile seed milik `Agus Pratama`
93. Di perangkat Android uji A (aplikasi memuat sesi mobile Active `Agus Pratama`) ketuk layar → Dialog muncul
94. Verifikasi Sesi mobile berstatus Force Logged Out
95. Verifikasi Perangkat A menampilkan Dialog "Password Changed"
96. Verifikasi Tidak ada sesi yang dikecualikan: sesi web dan sesi mobile sama-sama berstatus Force Logged Out

### TC-AUTH-SES-264: Reset Password mencatat Logged out (password changed) per sesi platform dan Session ended per sesi-produk anak

97. Di Browser License buka `PLATFORM SETTINGS > License > Concurrent User` (Fixed Asset), lalu catat bahwa baris `Galih Saputra` ada di daftar sesi aktif dan catat hitungan seat aktif
98. Tutup konteks Browser C TC sebelumnya (hapus sesi login browser), buka konteks baru Browser C (belum login)
99. Di Browser C buka halaman `Auth > Reset Password` → halaman Reset Password (Request) tampil
100. Ketik `galihsaputra+{runId}-055@qwertysystem.net` pada field Email
101. Centang widget reCAPTCHA "I'm not a robot"
102. Klik [Reset Password] → halaman Email Sent! tampil
103. Buka mail-catcher, ambil email reset untuk `galihsaputra+{runId}-055@qwertysystem.net`, lalu klik tautan reset → halaman Setup New Password tampil
104. Ketik `Spectra.env.SES_PASSWORD_NEW` pada field New Password
105. Ketik `Spectra.env.SES_PASSWORD_NEW` pada field Confirm Password
106. Klik [Reset Password] → Password Reset Successful tampil
107. Di Browser Admin buka `Global Settings > Activity Log > Session` dan cari entri `Galih Saputra` yang dibuat sesudah langkah 99 dimulai
108. Verifikasi Dicatat `Logged out (password changed)` untuk sesi platform yang berakhir
109. Di Browser Admin buka `Activity Log > Session` milik Fixed Asset dan cari entri `Galih Saputra` yang dibuat sesudah langkah 99 dimulai
110. Verifikasi Dicatat `Session ended` untuk sesi-produk anak
111. Buka `Global Settings > User > Detail > User Log` milik `Galih Saputra` dan cari entri yang dibuat sesudah langkah 99 dimulai
112. Verifikasi User Log memuat `Logged out (password changed)`
113. Verifikasi User Log memuat `Session ended (Fixed Asset)`
114. Di Browser License buka `PLATFORM SETTINGS > License > Concurrent User` (Fixed Asset) dan periksa daftar sesi aktif serta hitungan seat
115. Verifikasi Seat dilepas: baris `Galih Saputra` tidak ada di daftar sesi aktif dan hitungan seat aktif berkurang 1 dibanding hitungan yang dicatat di langkah 97

## Notes

- Sumber: `auth/session-management/TestCases/tc-session-management.md`. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Kelas harness: multi-konteks (Browser A, Browser C, Browser License, Browser Admin, perangkat Android) dengan mail-catcher untuk Reset Password. Seluruh TC batch ini satu kelas harness multi-sesi.
- Penyimpangan urutan (S-05, S-10): urutan di spec ini 186, 187, 182, 183, 188, 185, 184, 264 (urutan TC sumber 182–188 lalu 264). Penolakan (186, 187) ditaruh sebelum aksi sukses; 185, 184, dan 264 yang melepas seat dan memerlukan pembacaan di Browser License/Admin ditaruh paling akhir. Tiap TC memakai user sendiri, jadi urutan tidak membuat TC saling bergantung.
- Pembagian TC lintas spec (prinsip 10): pencatatan `Logged out (password changed)` yang menjadi fokus TC-AUTH-SES-208 diuji di spec `TC-AUTH-SES-E2E-057-pencatatan-akun-akses-force-logout-dan-password`. Pembacaan log di TC-AUTH-SES-185 (Expected butir b) dan TC-AUTH-SES-264 dipertahankan di spec ini sesuai TC sumber.
- TC-AUTH-SES-182 berdependensi pada TC-AUTH-SES-5 (Change Password lalu Dialog Password Changed di perangkat A); langkah 22–30 menyalin langkah dependensi itu (S-04). Screening isi Dialog diuji di spec screening, bukan di sini. TC-AUTH-SES-183 berdependensi pada TC-AUTH-SES-182; langkah 34–40 menyalin alurnya, kecuali langkah 2 TC-AUTH-SES-182 ("Di Browser A klik menu lain", langkah 27) yang sengaja tidak disalin karena hanya melayani Expected butir a TC-AUTH-SES-182 (sesi web tetap Active), sedangkan Expected TC-AUTH-SES-183 hanya menyangkut Dialog Password Changed di perangkat A. TC-AUTH-SES-264 berdependensi pada TC-AUTH-SES-184 ([DEFERRED]); langkah 99–106 menyalin alur Reset Password-nya.
- Langkah penghubung tanpa awalan `Verifikasi` (S-03): menutup modal Change Password dengan [Cancel] (langkah 8), menutup konteks Browser C TC sebelumnya (langkah 79 dan 98, S-09), perpindahan antar konteks dan perangkat, mencatat baris dan hitungan seat sebelum aksi (langkah 61, dasar pembanding langkah 72; langkah 97, dasar pembanding langkah 115), dan memuat ulang halaman Concurrent User (langkah 68).
- Detail halaman Reset Password (field Email, reCAPTCHA, Email Sent!, Setup New Password dengan field New Password dan Confirm Password, Password Reset Successful) dan modal Change Password (Current Password, New Password, Confirm New Password, [Save], [Cancel]) mengikuti `auth/reset-password/TestCases/tc-reset-password.md` dan PRD My Profile karena TC sumber hanya menulis "jalankan Forgot Password" dan "ubah password".
- Teks `Session ended (Fixed Asset)` pada entri User Log (langkah 78 dan 113) mengikuti Expected TC-AUTH-SES-132 dan TC-AUTH-SES-141, tempat User Log menampilkan `Session ended (Fixed Asset)`; Expected butir b TC-AUTH-SES-185 dan butir b TC-AUTH-SES-264 hanya menulis `Session ended`. Entri yang sama di `Activity Log > Session` milik Fixed Asset (langkah 76 dan 110) tetap `Session ended`.
- Temuan untuk QA:
  - TC-AUTH-SES-184 dan TC-AUTH-SES-264 menulis "Forgot Password" tanpa menyebut layar awalnya; TC modul Reset Password memakai dua jalur berbeda ([Forgot password?] di TC-AUTH-RST-143 dan tautan [Reset here] di TC-AUTH-RST-04); spec membuka halaman Reset Password langsung.
  - TC-AUTH-SES-187 Langkah Uji "coba kirim password baru" tidak menjelaskan bentuk penolakan; TC modul Reset Password menampilkan halaman 404 "Reset Link Expired" untuk tautan kedaluwarsa sehingga form kirim password baru mungkin tidak tersedia. Spec hanya menasersi "Reset Password ditolak".
  - TC-AUTH-SES-188 menulis "data valid yang lain" tanpa nilai; spec memakai `Spectra.env.SES_PASSWORD` sebagai password baru kedua (kembali ke password awal). Bila kebijakan password melarang memakai ulang password lama, diperlukan env password valid ketiga.
  - TC-AUTH-SES-185 Expected butir c merujuk pembacaan daftar `fixed-asset/license/PRD/license.md` §3.2; spec memakai akun #2 dengan Global Role Manage Global License di Client Q2 sesuai TC-AUTH-SES-133, dan user Rina Ramadhan berada di Client Q2.
  - TC-AUTH-SES-182, 184, 185, dan 188 menulis sesi "Force Logged Out" atau "Ended" tanpa cara baca di UI selain dialog atau hilangnya baris; spec mengasersinya di langkah 31, 58, 69, 90, 94, dan 96 dan bukti terlihatnya perlu ditentukan pemilik TC.
  - TC-AUTH-SES-185 Langkah Uji tidak memuat pembacaan License sebelum aksi, padahal Expected "hitungan berkurang 1"; spec menambah langkah 61 sebagai langkah penghubung (S-03).
  - TC-AUTH-SES-264 Langkah Uji menyebut pembacaan di Browser Admin, tetapi Expected butir c ("Seat dilepas") tidak punya langkah pembacaan; spec menambah langkah 114 di Browser License (S-14) dan langkah 97 sebagai pembacaan awal baris dan hitungan seat (S-12, S-14).
- Langkah penghubung ganti akun (S-03, S-07): tiap TC membuka konteks baru Browser A dan memuat sesi mobile seed di perangkat Android uji A untuk user TC itu, karena Browser A dan perangkat A dipakai bergantian oleh user antar-TC; langkah ini tanpa awalan `Verifikasi`.
- Ukuran spec: melewati sekitar 35 langkah walau blok baca-log tidak dihitung, karena delapan TC password berbagi harness yang sama (Browser A, Browser C, Browser License, Browser Admin, dan perangkat Android uji A). Tiap subjudul TC memakai user dan sesi seed sendiri sehingga bagian sesudahnya tetap bermakna bila bagian sebelumnya gagal (konvensi bagian 3, batas ukuran).
- TC-AUTH-SES-185 langkah 3 membaca tiga surface (GS Activity Log, `Activity Log > Session` milik Fixed Asset, User Log); spec membaca ketiganya (langkah 73 sampai 78) sesuai Expected butir b.
