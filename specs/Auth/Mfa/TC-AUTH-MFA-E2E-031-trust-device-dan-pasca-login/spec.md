---
id: TC-AUTH-MFA-E2E-031-trust-device-dan-pasca-login
title: "Trust Device dan Pencatatan Pasca Login Final MFA"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-MFA-143
  - TC-AUTH-MFA-144
  - TC-AUTH-MFA-145
  - TC-AUTH-MFA-147
  - TC-AUTH-MFA-150
  - TC-AUTH-MFA-151
coverage:
  web: automated
---

# Trust Device dan Pencatatan Pasca Login Final MFA

## Prerequisites

- Mode: FE+BE.
- Seeding (hook `before`, lewat API oleh akun aktor Total Control (Global Settings) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.GS_TC_PASSWORD`): enam user Activated, Active ON, profil NEWDEVE (Tabel Data Uji Pre-setup #5), password `Spectra.env.MFA_PASSWORD`, email bersuffix per run. Kondisi BE yang di-seed: seperti BASE, yaitu sudah pernah login sukses di web dari browser uji A (ID device browser uji A tercatat sebagai trusted device), login terakhir dari IP uji Jakarta (ID), logout web terakhir kurang dari 30 hari; Authenticator sudah terdaftar (secret TOTP dipegang aplikasi authenticator uji). Login dari browser uji B (ID device belum ada di daftar trusted device) memicu MFA.
  - TC-AUTH-MFA-143: `Grace Natalia` (`gracenatalia+{runId}-031@qwertysystem.net`)
  - TC-AUTH-MFA-144: `Haikal Azzam` (`haikalazzam+{runId}-031@qwertysystem.net`)
  - TC-AUTH-MFA-145: `Ines Maharani` (`inesmaharani+{runId}-031@qwertysystem.net`)
  - TC-AUTH-MFA-147: `Kartika Sari` (`kartikasari+{runId}-031@qwertysystem.net`)
  - TC-AUTH-MFA-150: `Nazar Hidayat` (`nazarhidayat+{runId}-031@qwertysystem.net`)
  - TC-AUTH-MFA-151: `Olivia Gunawan` (`oliviagunawan+{runId}-031@qwertysystem.net`)
- Aktor Total Control (Global Settings) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (`Spectra.env.GS_TC_PASSWORD`) login satu kali di hook `before` pada browser kedua (konteks browser terpisah dari browser user uji) dan sesinya dipakai untuk membaca `Global Settings > Activity Log > Session` pada TC-AUTH-MFA-150 dan 151. Login akun aktor tidak memicu MFA. Browser kedua tidak memegang sesi user uji; fungsinya hanya membaca log.
- Hook `after`: kembalikan IP uji ke IP default lingkungan uji, hapus keenam user, dan tutup browser kedua. Hook ini tetap jalan walau spec gagal di tengah dan tidak berasumsi seeding berhasil penuh.
- Akun yang dipakai: user uji tanpa login (halaman publik; tidak ada sesi aktif di browser) di jendela baru browser pertama; akun aktor Total Control (Global Settings) di browser kedua. Browser uji B = jendela privat baru (ID device belum dikenali) untuk semua TC; browser uji A = profil browser reguler dengan ID device persisten yang didaftarkan seeding sebagai trusted device (TC-AUTH-MFA-147).
- Suite berjalan serial (`parallel: false`) karena spec ini mengubah IP uji (lokasi koneksi login ke Jakarta, ID, pada TC-AUTH-MFA-143 dan 147); hook `after` memulihkan IP uji ke IP default lingkungan uji.
- Environment variable: `GS_TC_PASSWORD`, `MFA_PASSWORD`. Password tidak ditulis di spec atau fixture. Kode salah `000001` sampai `000005` adalah input uji literal.
- Kemampuan teknis: browser uji A dan browser uji B; dua konteks browser terpisah (browser pertama untuk user uji, browser kedua untuk akun aktor); tab baru dan tombol Back browser (TC-AUTH-MFA-144, 150); mail-catcher lingkungan uji untuk membaca email alert login tak biasa (TC-AUTH-MFA-143, 144); aplikasi authenticator uji (TOTP: SHA-1, 6 digit, periode 30 detik); reCAPTCHA mode uji di environment; IP uji: IP sumber permintaan login dapat ditetapkan ke IP uji geo-IP Jakarta (ID) (Tabel Data Uji Pre-setup #19) dan dikembalikan ke IP default lingkungan uji (TC-AUTH-MFA-143, 147). Seeding state BE per user: trusted device ber-ID device browser uji A, lokasi dan waktu login terakhir, logout web terakhir, dan authenticator terdaftar dengan secret yang dikenal authenticator uji; mekanisme seeding (endpoint/skrip uji) disediakan tim FE/BE karena tidak didefinisikan di TC, PRD, atau LLD. Pembacaan jumlah sesi aktif user oleh sisi BE (TC-AUTH-MFA-150, langkah 109; disediakan tim FE/BE karena tidak ada cara cek di UI atau di Langkah Uji TC; endpoint/skrip tidak didefinisikan di TC, PRD, atau LLD).
- State global yang diubah: IP uji (TC-AUTH-MFA-143 dan 147; dipulihkan di langkah terakhir tiap TC itu dan di hook `after`). Selain itu hanya data user milik spec ini.

## Test Steps

### TC-AUTH-MFA-143: Setelah MFA sukses, login berikutnya dari browser yang sama dan lokasi dekat berakhir single-step

1. Buka jendela privat baru di browser pertama (tanpa sesi login)
2. Atur IP uji ke Jakarta (ID)
3. Buka halaman `Auth > Login with Password` di browser uji B → halaman Login with Password tampil
4. Ketik `gracenatalia+{runId}-031@qwertysystem.net` pada field Email
5. Ketik `Spectra.env.MFA_PASSWORD` pada field Password
6. Centang widget reCAPTCHA "I'm not a robot"
7. Klik button [Log in] → halaman `Auth > MFA > Choose Verification Method` tampil
8. Pilih opsi "Authenticator app" pada halaman Choose Verification Method
9. Klik button [Login] → halaman `Auth > MFA > Authenticator Verification` tampil
10. Ketik 6 digit kode TOTP valid dari aplikasi authenticator uji untuk `gracenatalia+{runId}-031@qwertysystem.net` pada kotak digit lalu klik button [Login] → Portal — Product Hub tampil
11. Verifikasi Login pertama: MFA selesai
12. Verifikasi Portal — Product Hub tampil
13. Periksa mail-catcher lingkungan uji untuk `gracenatalia+{runId}-031@qwertysystem.net` dan catat jumlah email alert login tak biasa sebagai acuan
14. Logout dari akun `Grace Natalia`
15. Buka halaman `Auth > Login with Password` di browser yang sama → halaman Login with Password tampil
16. Ketik `gracenatalia+{runId}-031@qwertysystem.net` pada field Email
17. Ketik `Spectra.env.MFA_PASSWORD` pada field Password
18. Centang widget reCAPTCHA "I'm not a robot"
19. Klik button [Log in]
20. Amati halaman setelah klik [Log in]
21. Verifikasi Login berikutnya: halaman MFA tidak tampil
22. Verifikasi Browser dialihkan langsung ke Portal — Product Hub (device dan lokasi di-trust)
23. Periksa mail-catcher lingkungan uji untuk `gracenatalia+{runId}-031@qwertysystem.net`
24. Verifikasi Tidak ada email alert baru pada login berikutnya (jumlah email alert sama dengan acuan setelah login pertama)
25. Kembalikan IP uji ke IP default lingkungan uji

### TC-AUTH-MFA-144: Device tidak di-trust sebelum login final berhasil

26. Tutup jendela user uji dari TC sebelumnya dan hapus sesi login browser terkait (ID device dan jendela sesi akun aktor tetap), lalu buka jendela privat baru di browser pertama (tanpa sesi login)
27. Buka halaman `Auth > Login with Password` di browser uji B → halaman Login with Password tampil
28. Ketik `haikalazzam+{runId}-031@qwertysystem.net` pada field Email
29. Ketik `Spectra.env.MFA_PASSWORD` pada field Password
30. Centang widget reCAPTCHA "I'm not a robot"
31. Klik button [Log in] → halaman `Auth > MFA > Choose Verification Method` tampil
32. Pilih opsi "Authenticator app" pada halaman Choose Verification Method
33. Klik button [Login] → halaman `Auth > MFA > Authenticator Verification` tampil
34. Ketik `000001` pada kotak digit lalu klik button [Login]
35. Periksa mail-catcher lingkungan uji untuk `haikalazzam+{runId}-031@qwertysystem.net` dan catat jumlah email alert login tak biasa sebagai acuan (setelah login pertama)
36. Biarkan halaman tanpa menyelesaikan MFA, lalu buka tab baru di jendela privat yang sama
37. Buka halaman `Auth > Login with Password` pada tab baru → halaman Login with Password tampil
38. Ketik `haikalazzam+{runId}-031@qwertysystem.net` pada field Email
39. Ketik `Spectra.env.MFA_PASSWORD` pada field Password
40. Centang widget reCAPTCHA "I'm not a robot"
41. Klik button [Log in]
42. Verifikasi Login ulang tetap memicu MFA pada tab baru: halaman `Auth > MFA > Choose Verification Method` tampil
43. Periksa mail-catcher lingkungan uji untuk `haikalazzam+{runId}-031@qwertysystem.net`
44. Verifikasi Email alert login tak biasa diterima kembali untuk `haikalazzam+{runId}-031@qwertysystem.net` (jumlah email alert bertambah dari acuan setelah login pertama)
45. Tutup tab baru

### TC-AUTH-MFA-145: Kegagalan faktor-2 tidak memperbarui trust device dan lokasi

46. Tutup jendela user uji dari TC sebelumnya dan hapus sesi login browser terkait (ID device dan jendela sesi akun aktor tetap), lalu buka jendela privat baru di browser pertama (tanpa sesi login)
47. Buka halaman `Auth > Login with Password` di browser uji B → halaman Login with Password tampil
48. Ketik `inesmaharani+{runId}-031@qwertysystem.net` pada field Email
49. Ketik `Spectra.env.MFA_PASSWORD` pada field Password
50. Centang widget reCAPTCHA "I'm not a robot"
51. Klik button [Log in] → halaman `Auth > MFA > Choose Verification Method` tampil
52. Pilih opsi "Authenticator app" pada halaman Choose Verification Method
53. Klik button [Login] → halaman `Auth > MFA > Authenticator Verification` tampil
54. Ketik `000001` pada kotak digit lalu klik button [Login] (percobaan 1)
55. Ketik `000002` pada kotak digit lalu klik button [Login] (percobaan 2)
56. Ketik `000003` pada kotak digit lalu klik button [Login] (percobaan 3)
57. Ketik `000004` pada kotak digit lalu klik button [Login] (percobaan 4)
58. Ketik `000005` pada kotak digit lalu klik button [Login] (percobaan 5) → halaman Login with Password tampil
59. Ketik `inesmaharani+{runId}-031@qwertysystem.net` pada field Email
60. Ketik `Spectra.env.MFA_PASSWORD` pada field Password
61. Centang widget reCAPTCHA "I'm not a robot"
62. Klik button [Log in]
63. Amati halaman setelah klik [Log in]
64. Verifikasi Halaman `Auth > MFA > Choose Verification Method` tampil lagi (browser uji B belum di-trust)

### TC-AUTH-MFA-147: User dengan beberapa trusted device: masing-masing device dikenali pada login berikutnya

65. Tutup jendela user uji dari TC sebelumnya dan hapus sesi login browser terkait (ID device dan jendela sesi akun aktor tetap), lalu buka jendela privat baru di browser pertama (tanpa sesi login)
66. Atur IP uji ke Jakarta (ID)
67. Buka halaman `Auth > Login with Password` di browser uji B → halaman Login with Password tampil
68. Ketik `kartikasari+{runId}-031@qwertysystem.net` pada field Email
69. Ketik `Spectra.env.MFA_PASSWORD` pada field Password
70. Centang widget reCAPTCHA "I'm not a robot"
71. Klik button [Log in] → halaman `Auth > MFA > Choose Verification Method` tampil
72. Pilih opsi "Authenticator app" pada halaman Choose Verification Method
73. Klik button [Login] → halaman `Auth > MFA > Authenticator Verification` tampil
74. Ketik 6 digit kode TOTP valid dari aplikasi authenticator uji untuk `kartikasari+{runId}-031@qwertysystem.net` pada kotak digit lalu klik button [Login] → Portal — Product Hub tampil
75. Logout dari akun `Kartika Sari` di browser uji B
76. Beralih ke browser uji A (device lama dikenali) lalu buka halaman `Auth > Login with Password` → halaman Login with Password tampil
77. Ketik `kartikasari+{runId}-031@qwertysystem.net` pada field Email
78. Ketik `Spectra.env.MFA_PASSWORD` pada field Password
79. Centang widget reCAPTCHA "I'm not a robot"
80. Klik button [Log in]
81. Amati halaman setelah klik [Log in]
82. Verifikasi Browser uji A: single-step ke Portal — Product Hub
83. Logout dari akun `Kartika Sari` di browser uji A
84. Beralih kembali ke browser uji B lalu buka halaman `Auth > Login with Password` → halaman Login with Password tampil
85. Ketik `kartikasari+{runId}-031@qwertysystem.net` pada field Email
86. Ketik `Spectra.env.MFA_PASSWORD` pada field Password
87. Centang widget reCAPTCHA "I'm not a robot"
88. Klik button [Log in]
89. Amati halaman setelah klik [Log in]
90. Verifikasi Browser uji B: single-step ke Portal — Product Hub (kedua device masuk daftar trusted)
91. Kembalikan IP uji ke IP default lingkungan uji

### TC-AUTH-MFA-150: Sesi pre-auth MFA tidak menghasilkan sesi penuh dan dikonsumsi setelah login final

92. Tutup jendela user uji dari TC sebelumnya dan hapus sesi login browser terkait (ID device dan jendela sesi akun aktor tetap), lalu buka jendela privat baru di browser pertama (tanpa sesi login)
93. Buka halaman `Auth > Login with Password` di browser uji B → halaman Login with Password tampil
94. Ketik `nazarhidayat+{runId}-031@qwertysystem.net` pada field Email
95. Ketik `Spectra.env.MFA_PASSWORD` pada field Password
96. Centang widget reCAPTCHA "I'm not a robot"
97. Klik button [Log in] → halaman `Auth > MFA > Choose Verification Method` tampil
98. Pilih opsi "Authenticator app" pada halaman Choose Verification Method
99. Klik button [Login] → halaman `Auth > MFA > Authenticator Verification` tampil
100. Sebelum verifikasi, buka tab baru lalu buka alamat Portal — Product Hub langsung di browser
101. Verifikasi Portal — Product Hub tidak dapat diakses tanpa sesi penuh (user tidak masuk)
102. Tutup tab baru
103. Catat penanda waktu sebelum login final sebagai acuan entri log baru untuk `Nazar Hidayat`
104. Ketik 6 digit kode TOTP valid dari aplikasi authenticator uji untuk `nazarhidayat+{runId}-031@qwertysystem.net` pada kotak digit lalu klik button [Login]
105. Verifikasi Login final berhasil
106. Verifikasi Portal — Product Hub tampil
107. Tekan tombol Back browser
108. Ketik ulang kode TOTP yang sama pada kotak digit di halaman Authenticator Verification lalu klik button [Login]
109. Verifikasi Pengiriman ulang tidak membuat sesi kedua untuk `Nazar Hidayat`
110. Beralih ke browser kedua (sesi Total Control Global Settings), buka `Global Settings > Activity Log > Session`, lalu cari entri `Nazar Hidayat` dengan email bersuffix `nazarhidayat+{runId}-031@qwertysystem.net` yang dibuat sesudah penanda waktu langkah 103
111. Verifikasi Tidak ada entri Success ganda untuk `Nazar Hidayat` (tepat satu entri Success login final sesudah penanda waktu langkah 103)

### TC-AUTH-MFA-151: Faktor-1 tidak menulis Success saat MFA terpicu dan hanya MFA yang menulis setelah faktor-2

112. Tutup jendela user uji dari TC sebelumnya dan hapus sesi login browser terkait (ID device dan jendela sesi akun aktor tetap), lalu pindah ke browser pertama dan buka jendela privat baru (tanpa sesi login)
113. Buka halaman `Auth > Login with Password` di browser uji B → halaman Login with Password tampil
114. Ketik `oliviagunawan+{runId}-031@qwertysystem.net` pada field Email
115. Ketik `Spectra.env.MFA_PASSWORD` pada field Password
116. Centang widget reCAPTCHA "I'm not a robot"
117. Klik button [Log in] → halaman `Auth > MFA > Choose Verification Method` tampil
118. Pilih opsi "Authenticator app" pada halaman Choose Verification Method
119. Klik button [Login] → halaman `Auth > MFA > Authenticator Verification` tampil
120. Beralih ke browser kedua (sesi Total Control Global Settings), buka `Global Settings > Activity Log > Session`, lalu cari entri `Olivia Gunawan` dengan email bersuffix `oliviagunawan+{runId}-031@qwertysystem.net` dan catat penanda waktu sebagai acuan entri log baru
121. Beralih ke browser pertama (halaman Authenticator Verification)
122. Ketik 6 digit kode TOTP valid dari aplikasi authenticator uji untuk `oliviagunawan+{runId}-031@qwertysystem.net` pada kotak digit lalu klik button [Login]
123. Beralih ke browser kedua (sesi Total Control Global Settings)
124. Muat ulang `Global Settings > Activity Log > Session` lalu cari entri `Olivia Gunawan` yang dibuat sesudah penanda waktu langkah 120
125. Verifikasi Tepat satu entri Success `Login with password` untuk `Olivia Gunawan` sesudah penanda waktu langkah 120

## Notes

- Sumber: `auth/mfa/TestCases/tc-mfa.md`. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. Akun aktor Total Control login satu kali di hook `before` di browser kedua dan hanya membaca log (TC-AUTH-MFA-150 dan 151), sehingga bukan konteks kedua yang menjadi objek asersi dan tidak butuh butir `P-2` untuknya. Browser uji A dan B dipakai berurutan hanya untuk membentuk identitas device (TC-AUTH-MFA-147, tanpa asersi lintas keduanya) dan tidak butuh butir `P-2`. Pembacaan email di mail-catcher adalah langkah rutin spec fungsional.
- Langkah pembuka tiap TC sesudah TC pertama menutup jendela user uji dari TC sebelumnya dan menghapus sesi login browser terkait (ID device dan jendela sesi akun aktor tetap) sebelum jendela baru dibuka; itu langkah penghubung tanpa `Verifikasi` (S-03, S-09).
- `P-2`: tab baru pada TC-AUTH-MFA-144 hanya berfungsi sebagai pemicu login ulang untuk membangun state yang diuji (device belum di-trust sehingga MFA terpicu lagi dan email alert diterima kembali); objek asersinya halaman Choose Verification Method pada tab baru dan email alert, bukan perilaku tab pertama. Tab baru ditutup di akhir TC (S-09).
- `P-2`: TC-AUTH-MFA-150 menguji siklus sesi pre-auth (dikonsumsi setelah login final). Membuka alamat Portal — Product Hub sebelum verifikasi (Expected a) dan mengirim ulang kode TOTP yang sama setelah Back (Expected c) dilakukan lewat UI hanya untuk mengamati bahwa sesi pre-auth belum menghasilkan sesi penuh dan sudah habis; keduanya bukan serangan langsung ke server sehingga bukan kelas a (defense-in-depth).
- Urutan mengikuti TC sumber; tiap TC memakai user sendiri sehingga tidak saling bergantung.
- Melewati ±35 langkah (±85 netto setelah langkah prefix login faktor-1 tidak dihitung) karena enam TC independen; tiap TC memakai user dan konteks browser sendiri dan IP uji dipulihkan di akhir TC yang mengubahnya, sehingga bagian sesudahnya tetap bermakna walau bagian sebelumnya gagal dan spec tidak dipecah.
- Pembagian lintas spec: TC-AUTH-MFA-151 terbelah dengan spec `TC-AUTH-MFA-E2E-035-absence-pencatatan-log`. Butir a (belum ada entri Success `Login with password` untuk `Olivia Gunawan` saat faktor-1 lolos dan MFA terpicu) adalah asersi absence dan diasersikan di spec 035 (prinsip 10, S-05), bukan di spec ini. Butir b (tepat satu entri Success setelah faktor-2) diasersikan di spec ini dengan baseline penanda waktu sesudah langkah 120. Langkah membuka Activity Log sebelum faktor-2 (pencatatan penanda waktu) ditulis sebagai langkah penghubung.
- Langkah penghubung tanpa awalan `Verifikasi` (buka jendela baru di awal tiap TC; beralih antara browser pertama dan kedua; periksa mail-catcher dan catat acuan jumlah email alert pada TC-AUTH-MFA-143 dan 144; catat penanda waktu pada TC-AUTH-MFA-150 dan 151; atur dan kembalikan IP uji pada TC-AUTH-MFA-143 dan 147 (langkah 2, 25, 66, 91); tab baru dan tutup tab pada TC-AUTH-MFA-144 dan 150; klik [Login] untuk mengirim kode salah) bukan asersi tambahan (S-03). Tab baru pada TC-AUTH-MFA-150 dipakai untuk membuka alamat Portal — Product Hub supaya halaman Authenticator Verification pada tab pertama tidak ditinggalkan.
- Temuan untuk QA: (1) TC-AUTH-MFA-150 Expected butir c ("tidak ada entri Success ganda") memerlukan pembacaan Activity Log oleh akun Total Control Global Settings, tetapi Precondition TC tidak memuat akun tersebut; spec menambahkannya di Prerequisites (login di hook `before`). (2) TC-AUTH-MFA-150 langkah 10 tidak menjelaskan halaman yang tampil setelah tombol Back dan hasil pengiriman ulang kode di UI; spec hanya mengasersi bahwa tidak ada sesi kedua (langkah 109, memakai kemampuan pembacaan jumlah sesi aktif oleh sisi BE yang disediakan tim FE/BE) dan tidak ada entri Success ganda. TC-AUTH-MFA-150 Expected butir c tidak memberi cara cek jumlah sesi di UI maupun di Langkah Uji; QA perlu menambah langkah observasi atau menyatakan cara cek lain. (3) TC-AUTH-MFA-143 dan 144 Expected butir c ("tidak ada email alert baru" dan "email alert diterima kembali") tidak punya acuan jumlah email sebelumnya; spec mencatat jumlah email alert setelah login pertama sebagai pembanding. (4) TC-AUTH-MFA-144 Expected memuat "email alert diterima kembali" tanpa langkah pengecekan mail-catcher; ditambahkan sebagai langkah penghubung. (5) TC-AUTH-MFA-147 langkah 9–10 "Logout" tidak menyebut cara dan browser yang dipakai; spec menuliskan logout eksplisit di browser yang sedang dipakai. (6) TC-AUTH-MFA-144 dan 145 tidak menyebut IP uji; spec tidak menetapkan IP khusus untuk kedua TC itu (IP default lingkungan uji, karena IP uji dipulihkan di akhir TC-AUTH-MFA-143). (7) Post Condition tanpa langkah observasi dan tanpa Expected padanan tidak diasersi di spec ini: TC-AUTH-MFA-144 "Browser uji B belum masuk daftar trusted device `Haikal Azzam`"; TC-AUTH-MFA-145 "Daftar trusted device `Ines Maharani` tidak bertambah" (belum ada cara membaca daftar trusted device lewat UI di TC); TC-AUTH-MFA-143, 147, dan 150 "Satu sesi web aktif" (teramati sebagai Portal — Product Hub tampil); TC-AUTH-MFA-150 "Sesi pre-auth MFA `Nazar Hidayat` tidak berlaku lagi"; TC-AUTH-MFA-151 "Satu entri Success login final" sudah menjadi Expected butir b. QA dapat menambah Expected atau langkah observasi di TC bila perlu. (8) Mekanisme seeding state BE per user (trusted device ber-ID device, lokasi dan waktu login terakhir, authenticator terdaftar dengan secret yang dikenal authenticator uji) belum ada di Pre-setup (#20/#21) TC; spec tidak menyebut endpoint.
