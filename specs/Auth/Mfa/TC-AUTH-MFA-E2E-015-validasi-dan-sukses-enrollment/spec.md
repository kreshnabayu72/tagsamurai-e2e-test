---
id: TC-AUTH-MFA-E2E-015-validasi-dan-sukses-enrollment
title: "Validasi Kode dan Keberhasilan Enrollment Authenticator"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-MFA-110
  - TC-AUTH-MFA-111
  - TC-AUTH-MFA-112
  - TC-AUTH-MFA-11
  - TC-AUTH-MFA-106
  - TC-AUTH-MFA-107
  - TC-AUTH-MFA-108
coverage:
  web: automated
---

# Validasi Kode dan Keberhasilan Enrollment Authenticator

## Prerequisites

- Mode: FE+BE (kondisi jaringan lambat pada TC-AUTH-MFA-11 dipicu lewat intercept respons di atas backend nyata, bagian 6 konvensi).
- Seeding (hook `before`, lewat API oleh akun aktor Total Control (Global Settings) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.GS_TC_PASSWORD`): tujuh user profil FIRST (Tabel Data Uji Pre-setup #3: Activated, Active ON, belum pernah login di platform mana pun, Authenticator belum terdaftar), password `Spectra.env.MFA_PASSWORD`, email bersuffix per run:
  - TC-AUTH-MFA-111: `Fitri Handayani` (`fitrihandayani+{runId}-015@qwertysystem.net`)
  - TC-AUTH-MFA-112: `Guntur Pamungkas` (`gunturpamungkas+{runId}-015@qwertysystem.net`)
  - TC-AUTH-MFA-110: `Erlangga Putra` (`erlanggaputra+{runId}-015@qwertysystem.net`)
  - TC-AUTH-MFA-11: `Dimas Prakoso` (`dimasprakoso+{runId}-015@qwertysystem.net`)
  - TC-AUTH-MFA-106: `Alif Rahman` (`alifrahman+{runId}-015@qwertysystem.net`)
  - TC-AUTH-MFA-107: `Bunga Citra` (`bungacitra+{runId}-015@qwertysystem.net`)
  - TC-AUTH-MFA-108: `Candra Wijaya` (`candrawijaya+{runId}-015@qwertysystem.net`)
- Seeding state BE per user: hanya profil FIRST (Activated, Active ON, belum pernah login di platform mana pun, Authenticator belum terdaftar) yang dibentuk lewat pembuatan user oleh akun aktor; tidak ada state BE lain yang di-seed (trusted device, lokasi dan waktu login terakhir, consent, secret Authenticator). Enrollment aktif pada TC-AUTH-MFA-107 dibentuk oleh alur UI spec ini sendiri (langkah 95–96), bukan oleh seeding.
- Hook `after`: hapus ketujuh user dan hentikan throttle atau intercept jaringan yang dipasang TC-AUTH-MFA-11 (cadangan; TC-AUTH-MFA-11 melepasnya sendiri pada langkah 66 sebelum TC-AUTH-MFA-106). Pembersihan tidak berasumsi seeding berhasil penuh.
- Akun yang dipakai: tanpa login (halaman publik; tidak ada sesi aktif di browser) untuk semua TC. Tiap TC setelah yang pertama dimulai di jendela privat baru. TC-AUTH-MFA-107 memakai browser uji A (device pertama) lalu browser uji B secara berurutan hanya untuk membentuk identitas device (tanpa asersi lintas kedua browser).
- Environment variable: `GS_TC_PASSWORD`, `MFA_PASSWORD`. Password tidak ditulis di spec atau fixture. Input uji kode salah `000000` dan `123` ditulis literal.
- Kemampuan teknis: jendela privat; reCAPTCHA mode uji di environment; aplikasi authenticator uji (TOTP: SHA-1, 6 digit, periode 30 detik, jam tidak digeser) yang dapat mendaftarkan akun dari QR code atau secret key halaman Enrollment dan menghasilkan kode TOTP; akses clipboard browser untuk CopyButton "Copy key" (TC-AUTH-MFA-108); throttle jaringan atau intercept yang menahan respons verifikasi enrollment selama 3 detik (TC-AUTH-MFA-11) beserta pengamatan jumlah request yang terkirim; browser uji A dan browser uji B, masing-masing profil browser terpisah dengan ID device persisten (browser uji A = device pertama, browser uji B = device baru yang belum dikenali, TC-AUTH-MFA-107); pembacaan toast beserta durasi tampilnya (TC-AUTH-MFA-106).
- Kemampuan teknis, pembacaan state BE: pembacaan status enrollment Authenticator oleh sisi BE untuk Expected TC-AUTH-MFA-111 dan TC-AUTH-MFA-112 butir a (langkah 11 dan 25); disediakan tim FE/BE karena tidak ada cara cek di UI atau Langkah Uji TC; endpoint/skrip tidak didefinisikan di TC, PRD, atau LLD.
- Jeda nyata pendek (≤30 detik): langkah 83 menunggu 4 detik (TC-AUTH-MFA-106) sampai toast hilang otomatis. Spec ini tidak mengatur jam server, jam browser, maupun jam aplikasi authenticator uji.
- Semua user berprofil FIRST, jadi login pertama tiap user melewati layar Confirm to Continue sebelum Choose Verification Method.

## Test Steps

### TC-AUTH-MFA-111: Klik [Verify] pada Enrollment tanpa mengisi kode

1. Buka halaman `Auth > Login with Password` di browser → halaman Login with Password tampil
2. Ketik `fitrihandayani+{runId}-015@qwertysystem.net` pada field Email
3. Ketik `Spectra.env.MFA_PASSWORD` pada field Password
4. Centang widget reCAPTCHA "I'm not a robot"
5. Klik button [Log in] → layar Confirm to Continue tampil
6. Centang checkbox persetujuan, lalu klik [Continue ➔] → halaman `Auth > MFA > Choose Verification Method` tampil
7. Pilih opsi "Authenticator app" pada halaman Choose Verification Method
8. Klik button [Login] → halaman `Auth > MFA > Enrollment Authenticator` tampil
9. Klik button [Verify] tanpa mengisi kotak digit
10. Verifikasi Halaman tetap Enrollment Authenticator
11. Verifikasi Enrollment belum aktif
12. Verifikasi Caption error di bawah kotak digit: "Code must not be empty"

### TC-AUTH-MFA-112: Klik [Verify] pada Enrollment sebelum 6 digit terisi

13. Tutup jendela user uji dari TC sebelumnya dan hapus sesi login browser terkait (ID device dan jendela sesi akun aktor tetap), lalu buka jendela privat baru (tanpa sesi login)
14. Buka halaman `Auth > Login with Password` di browser → halaman Login with Password tampil
15. Ketik `gunturpamungkas+{runId}-015@qwertysystem.net` pada field Email
16. Ketik `Spectra.env.MFA_PASSWORD` pada field Password
17. Centang widget reCAPTCHA "I'm not a robot"
18. Klik button [Log in] → layar Confirm to Continue tampil
19. Centang checkbox persetujuan, lalu klik [Continue ➔] → halaman `Auth > MFA > Choose Verification Method` tampil
20. Pilih opsi "Authenticator app" pada halaman Choose Verification Method
21. Klik button [Login] → halaman `Auth > MFA > Enrollment Authenticator` tampil
22. Ketik 3 digit kode `123` pada kotak digit
23. Klik button [Verify]
24. Verifikasi Halaman tetap Enrollment Authenticator
25. Verifikasi Enrollment belum aktif
26. Verifikasi Caption error di bawah kotak digit: "Code must not be empty" (kode parsial didefinisikan sama dengan kosong)

### TC-AUTH-MFA-110: Kode verifikasi enrollment salah pada percobaan 1–4 tetap di halaman Enrollment

27. Tutup jendela user uji dari TC sebelumnya dan hapus sesi login browser terkait (ID device dan jendela sesi akun aktor tetap), lalu buka jendela privat baru (tanpa sesi login)
28. Buka halaman `Auth > Login with Password` di browser → halaman Login with Password tampil
29. Ketik `erlanggaputra+{runId}-015@qwertysystem.net` pada field Email
30. Ketik `Spectra.env.MFA_PASSWORD` pada field Password
31. Centang widget reCAPTCHA "I'm not a robot"
32. Klik button [Log in] → layar Confirm to Continue tampil
33. Centang checkbox persetujuan, lalu klik [Continue ➔] → halaman `Auth > MFA > Choose Verification Method` tampil
34. Pilih opsi "Authenticator app" pada halaman Choose Verification Method
35. Klik button [Login] → halaman `Auth > MFA > Enrollment Authenticator` tampil
36. Catat secret key dan QR code yang tampil
37. Ketik 6 digit kode yang salah `000000` pada kotak digit
38. Klik button [Verify]
39. Verifikasi Caption error di bawah kotak digit: "Invalid code"
40. Verifikasi Halaman tetap Enrollment Authenticator
41. Verifikasi QR code yang tampil sama dengan yang dicatat pada langkah 36
42. Verifikasi Secret key yang tampil sama dengan yang dicatat pada langkah 36
43. Verifikasi Kotak digit dikosongkan
44. Verifikasi Fokus kembali ke kotak 1
45. Ketik digit `1` pada kotak 1
46. Verifikasi Caption error hilang
47. Verifikasi Border error hilang

### TC-AUTH-MFA-11: Button [Verify] di Enrollment berstatus Submitting saat verifikasi berjalan

48. Tutup jendela user uji dari TC sebelumnya dan hapus sesi login browser terkait (ID device dan jendela sesi akun aktor tetap), lalu buka jendela privat baru (tanpa sesi login)
49. Buka halaman `Auth > Login with Password` di browser → halaman Login with Password tampil
50. Ketik `dimasprakoso+{runId}-015@qwertysystem.net` pada field Email
51. Ketik `Spectra.env.MFA_PASSWORD` pada field Password
52. Centang widget reCAPTCHA "I'm not a robot"
53. Klik button [Log in] → layar Confirm to Continue tampil
54. Centang checkbox persetujuan, lalu klik [Continue ➔] → halaman `Auth > MFA > Choose Verification Method` tampil
55. Pilih opsi "Authenticator app" pada halaman Choose Verification Method
56. Klik button [Login] → halaman `Auth > MFA > Enrollment Authenticator` tampil
57. Pindai QR code atau masukkan secret key pada aplikasi authenticator uji
58. Ketik 6 digit kode dari aplikasi authenticator uji pada kotak digit
59. Tahan respons server menggunakan throttle jaringan 3 detik, lalu klik button [Verify]
60. Amati button [Verify] selama request berjalan
61. Verifikasi Selama request berjalan, button [Verify] berstatus disabled
62. Verifikasi Selama request berjalan, button [Verify] menampilkan spinner memutar
63. Klik button [Verify] sekali lagi selama request berjalan
64. Verifikasi Klik tambahan tidak mengirim request kedua
65. Verifikasi Setelah respons diterima, browser dialihkan ke Portal — Product Hub
66. Lepaskan throttle atau intercept jaringan 3 detik yang dipasang pada langkah 59

### TC-AUTH-MFA-106: Enrollment Authenticator berhasil dan langsung menyelesaikan login final

67. Tutup jendela user uji dari TC sebelumnya dan hapus sesi login browser terkait (ID device dan jendela sesi akun aktor tetap), lalu buka jendela privat baru (tanpa sesi login)
68. Buka halaman `Auth > Login with Password` di browser → halaman Login with Password tampil
69. Ketik `alifrahman+{runId}-015@qwertysystem.net` pada field Email
70. Ketik `Spectra.env.MFA_PASSWORD` pada field Password
71. Centang widget reCAPTCHA "I'm not a robot"
72. Klik button [Log in] → layar Confirm to Continue tampil
73. Centang checkbox persetujuan, lalu klik [Continue ➔] → halaman `Auth > MFA > Choose Verification Method` tampil
74. Pilih opsi "Authenticator app" pada halaman Choose Verification Method
75. Klik button [Login] → halaman `Auth > MFA > Enrollment Authenticator` tampil
76. Pindai QR code dengan aplikasi authenticator uji
77. Ketik 6 digit kode dari aplikasi authenticator uji pada kotak digit
78. Klik button [Verify]
79. Verifikasi Browser dialihkan ke Portal — Product Hub
80. Verifikasi Tidak ada layar konfirmasi terpisah sebelum Portal — Product Hub tampil
81. Verifikasi Sesi web aktif untuk `Alif Rahman`
82. Verifikasi Pada Portal — Product Hub muncul toast sukses: "Success, authenticator app has been added."
83. Tunggu 4 detik
84. Verifikasi Toast "Success, authenticator app has been added." hilang otomatis setelah 4 detik
85. Verifikasi Tidak ada toast untuk verifikasi login itu sendiri

### TC-AUTH-MFA-107: Setelah enrollment aktif, MFA berikutnya membuka Authenticator Verification

86. Tutup jendela user uji dari TC sebelumnya dan hapus sesi login browser terkait (ID device dan jendela sesi akun aktor tetap), lalu buka jendela baru di browser uji A (device pertama; tanpa sesi login)
87. Buka halaman `Auth > Login with Password` di browser → halaman Login with Password tampil
88. Ketik `bungacitra+{runId}-015@qwertysystem.net` pada field Email
89. Ketik `Spectra.env.MFA_PASSWORD` pada field Password
90. Centang widget reCAPTCHA "I'm not a robot"
91. Klik button [Log in] → layar Confirm to Continue tampil
92. Centang checkbox persetujuan, lalu klik [Continue ➔] → halaman `Auth > MFA > Choose Verification Method` tampil
93. Pilih opsi "Authenticator app" pada halaman Choose Verification Method
94. Klik button [Login] → halaman `Auth > MFA > Enrollment Authenticator` tampil
95. Pindai QR code dengan aplikasi authenticator uji
96. Ketik 6 digit kode dari aplikasi authenticator uji lalu klik button [Verify] → Portal — Product Hub tampil
97. Logout dari Portal — Product Hub
98. Tutup jendela user uji dari TC sebelumnya dan hapus sesi login browser terkait (ID device dan jendela sesi akun aktor tetap), lalu buka browser uji B (device baru, tanpa sesi login)
99. Buka halaman `Auth > Login with Password` di browser → halaman Login with Password tampil
100. Ketik `bungacitra+{runId}-015@qwertysystem.net` pada field Email
101. Ketik `Spectra.env.MFA_PASSWORD` pada field Password
102. Centang widget reCAPTCHA "I'm not a robot"
103. Klik button [Log in] → halaman `Auth > MFA > Choose Verification Method` tampil
104. Pilih opsi "Authenticator app" lalu klik button [Login]
105. Verifikasi Halaman `Auth > MFA > Authenticator Verification` tampil (bukan Enrollment Authenticator)

### TC-AUTH-MFA-108: Enrollment lewat secret key yang disalin (tanpa scan QR) berhasil

106. Tutup jendela user uji dari TC sebelumnya dan hapus sesi login browser terkait (ID device dan jendela sesi akun aktor tetap), lalu buka jendela privat baru (tanpa sesi login)
107. Buka halaman `Auth > Login with Password` di browser → halaman Login with Password tampil
108. Ketik `candrawijaya+{runId}-015@qwertysystem.net` pada field Email
109. Ketik `Spectra.env.MFA_PASSWORD` pada field Password
110. Centang widget reCAPTCHA "I'm not a robot"
111. Klik button [Log in] → layar Confirm to Continue tampil
112. Centang checkbox persetujuan, lalu klik [Continue ➔] → halaman `Auth > MFA > Choose Verification Method` tampil
113. Pilih opsi "Authenticator app" pada halaman Choose Verification Method
114. Klik button [Login] → halaman `Auth > MFA > Enrollment Authenticator` tampil
115. Klik CopyButton "Copy key"
116. Tempel secret key yang disalin pada aplikasi authenticator uji (input manual)
117. Verifikasi Secret key yang disalin dapat ditempel pada aplikasi authenticator uji
118. Verifikasi Aplikasi authenticator uji menghasilkan kode 6 digit dari secret key itu
119. Ketik 6 digit kode dari aplikasi authenticator uji pada kotak digit
120. Klik button [Verify]
121. Verifikasi Browser dialihkan ke Portal — Product Hub
122. Verifikasi Sesi web aktif untuk `Candra Wijaya`

## Notes

- Sumber: `auth/mfa/TestCases/tc-mfa.md`. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Langkah pembuka tiap TC sesudah TC pertama menutup jendela user uji dari TC sebelumnya dan menghapus sesi login browser terkait (ID device dan jendela sesi akun aktor tetap) sebelum jendela baru dibuka; itu langkah penghubung tanpa `Verifikasi` (S-03, S-09).
- Urutan: TC-AUTH-MFA-111, 112, 110 (validasi yang diblokir) lebih dulu, lalu TC-AUTH-MFA-11, 106, 107, 108 (aksi sukses) sesuai bagian 3 konvensi dan tidak menyimpang dari prinsip urutan. Tiap TC memakai user sendiri, sehingga tidak ada data yang dipakai bersama.
- Langkah penghubung tanpa awalan `Verifikasi` (buka jendela privat baru di awal tiap TC setelah yang pertama; langkah 36 mencatat secret key dan QR code; langkah 45 mengetik digit untuk mengecek hilangnya caption; langkah 63 klik tambahan; langkah 66 melepas throttle atau intercept jaringan TC-AUTH-MFA-11; langkah 83 menunggu 4 detik; langkah 97–104 login ulang dari browser uji B) bukan asersi tambahan (S-03). Langkah 63 dan 45 menurunkan butir Expected TC yang tidak punya langkah aksinya di Langkah Uji (S-14).
- Browser uji A (device pertama) lalu browser uji B pada TC-AUTH-MFA-107 dipakai berurutan hanya untuk membentuk identitas device; tidak ada asersi lintas kedua browser dan tidak ada konteks kedua yang berjalan bersamaan.
- Batas ukuran: langkah prefix login faktor-1 yang identik antar-TC (buka Login with Password sampai klik [Log in]) tidak dihitung ke batas ±35 langkah (bagian 3 konvensi); ketujuh TC independen dan tiap TC memakai user sendiri, sehingga spec tidak dipecah.
- Temuan untuk QA: (1) Post Condition TC tanpa langkah observasi dan tanpa Expected padanan tidak diasersi di spec ini (S-01): TC-AUTH-MFA-110 "Enrollment belum aktif"; TC-AUTH-MFA-111 "percobaan dihitung sebagai satu percobaan salah terhadap batas 5" (diuji di TC batas percobaan, TC-AUTH-MFA-131); TC-AUTH-MFA-11 "Enrollment Authenticator aktif untuk `Dimas Prakoso`; satu sesi web aktif" (sesi teramati sebagai Portal — Product Hub tampil, langkah 65); TC-AUTH-MFA-106 butir a "Enrollment Authenticator `Alif Rahman` berstatus aktif" dan butir b "Satu sesi web aktif" (padanan sesi: langkah 79 dan 81); TC-AUTH-MFA-107 "Sesi pre-auth MFA aktif untuk `Bunga Citra`; enrollment tetap aktif" (sesi pre-auth teramati sebagai halaman Authenticator Verification tampil, langkah 105); TC-AUTH-MFA-108 "Enrollment Authenticator `Candra Wijaya` berstatus aktif". Post Condition absence dan pencatatan juga tidak diasersi (S-05): TC-AUTH-MFA-110, 111, 112 "Tidak ada entri log (kegagalan enrollment tidak dicatat)" dan TC-AUTH-MFA-106 "Enrollment tidak dicatat di surface log; hanya satu entri Success `Login with password`". QA dapat menambah Expected atau langkah observasi di TC. (1a) TC-AUTH-MFA-111 dan TC-AUTH-MFA-112 Expected butir a ("enrollment belum aktif") tidak memberi cara cek status enrollment di UI maupun di Langkah Uji; spec membacanya lewat kemampuan pembacaan status enrollment oleh sisi BE yang disediakan tim FE/BE (langkah 11 dan 25) dan tidak menyebut endpoint. QA perlu menambah langkah observasi atau menyatakan cara cek status itu. (2) TC-AUTH-MFA-110 berjudul "percobaan 1–4" tetapi Langkah Uji hanya satu percobaan salah (`000000`); spec mengikuti Langkah Uji. (3) TC-AUTH-MFA-11 Expected butir a menyebut "klik tambahan tidak mengirim request kedua" tanpa langkah klik tambahan di Langkah Uji; ditambahkan sebagai langkah 63. (4) TC-AUTH-MFA-107 langkah 10 "Logout lalu login ulang dari browser uji B" tidak merinci langkah login ulang dan tidak menyebut layar Confirm to Continue; spec menyalin login faktor-1 lalu Choose Verification Method tampil (user sudah menyelesaikan login pertama, jadi Agreement tidak terpicu). (5) TC-AUTH-MFA-106 butir b menyebut toast hilang otomatis setelah 4 detik; spec memverifikasi dengan menunggu 4 detik (jeda nyata, tercatat di Prerequisites). (6) Mekanisme seeding user profil FIRST mengikuti Pre-setup #3 (Create User); tidak ada state BE tambahan yang butuh mekanisme seeding di spec ini. (7) TC-AUTH-MFA-110 Expected c ("caption dan border error hilang saat digit pertama diketik ulang") tidak punya langkah mengetik ulang digit pertama di Langkah Uji (analog TC-AUTH-MFA-72 dan TC-AUTH-MFA-73 yang sudah memilikinya); ditambahkan sebagai langkah 45. (8) TC-AUTH-MFA-11 Langkah Uji 10 memasang throttle jaringan 3 detik tanpa langkah pelepasan; ditambahkan sebagai langkah 66 supaya TC-AUTH-MFA-106, 107, dan 108 tidak berjalan dengan throttle.
