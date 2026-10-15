---
id: TC-AUTH-MFA-E2E-028-batas-5-percobaan-salah
title: "Batas 5 Percobaan Salah Faktor-2 Meng-invalidate Sesi Pre-auth"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AUTH-MFA-129
  - TC-AUTH-MFA-130
  - TC-AUTH-MFA-131
  - TC-AUTH-MFA-133
  - TC-AUTH-MFA-134
  - TC-AUTH-MFA-135
  - TC-AUTH-MFA-132
coverage:
  web: automated
---

# Batas 5 Percobaan Salah Faktor-2 Meng-invalidate Sesi Pre-auth

## Prerequisites

- Mode: FE+BE.
- Seeding (hook `before`, lewat API oleh akun aktor Total Control (Global Settings) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.GS_TC_PASSWORD`): tujuh user Activated, Active ON, password `Spectra.env.MFA_PASSWORD`, email bersuffix per run. Kondisi BE yang di-seed per profil:
  - Profil NEWDEV (Tabel Data Uji Pre-setup #4): seperti BASE, yaitu sudah pernah login sukses di web dari browser uji A (ID device browser uji A tercatat sebagai trusted device), login terakhir dari IP uji Jakarta (ID), logout web terakhir kurang dari 30 hari; Authenticator belum terdaftar. Login dilakukan dari browser uji B (ID device belum ada di daftar trusted device) sehingga MFA terpicu.
  - Profil NEWDEVE (Tabel Data Uji Pre-setup #5): seperti NEWDEV tetapi Authenticator sudah terdaftar (secret TOTP dipegang aplikasi authenticator uji).
  - Profil FIRST (Tabel Data Uji Pre-setup #3): belum pernah menyelesaikan login di platform mana pun; Authenticator belum terdaftar.
  - TC-AUTH-MFA-129: `Tomi Hermawan` (`tomihermawan+{runId}-028@qwertysystem.net`), NEWDEV
  - TC-AUTH-MFA-130: `Ulfa Rahmi` (`ulfarahmi+{runId}-028@qwertysystem.net`), NEWDEVE
  - TC-AUTH-MFA-131: `Vicky Alamsyah` (`vickyalamsyah+{runId}-028@qwertysystem.net`), FIRST
  - TC-AUTH-MFA-133: `Yanti Susanti` (`yantisusanti+{runId}-028@qwertysystem.net`), NEWDEVE
  - TC-AUTH-MFA-134: `Zaki Firdaus` (`zakifirdaus+{runId}-028@qwertysystem.net`), NEWDEVE
  - TC-AUTH-MFA-135: `Anggi Permana` (`anggipermana+{runId}-028@qwertysystem.net`), NEWDEVE
  - TC-AUTH-MFA-132: `Wahyu Nugroho` (`wahyunugroho+{runId}-028@qwertysystem.net`), NEWDEV
- Hook `after`: hapus ketujuh user. Pembersihan tidak berasumsi seeding berhasil penuh.
- Akun yang dipakai: tanpa login (halaman publik; tidak ada sesi aktif di browser) untuk semua TC. Browser uji B = jendela privat baru (ID device belum dikenali) untuk semua TC kecuali TC-AUTH-MFA-131 yang memakai browser uji A (profil browser reguler dengan ID device persisten).
- Environment variable: `GS_TC_PASSWORD`, `MFA_PASSWORD`. Password tidak ditulis di spec atau fixture. Kode salah `000001` sampai `000005` adalah input uji literal.
- Kemampuan teknis: seeding state BE per user (trusted device ber-ID device browser uji A, lokasi dan waktu login terakhir Jakarta, logout web terakhir kurang dari 30 hari, Authenticator terdaftar dengan secret yang dikenal aplikasi authenticator uji untuk profil NEWDEVE, belum pernah login dan persetujuan Privacy Policy belum ada untuk profil FIRST); mekanisme seeding (endpoint/skrip uji) disediakan tim FE/BE karena tidak didefinisikan di TC, PRD, atau LLD; jendela privat dan browser uji A; reCAPTCHA mode uji di environment; mail-catcher lingkungan uji untuk membaca email OTP faktor-2 (TC-AUTH-MFA-129); aplikasi authenticator uji (TOTP: SHA-1, 6 digit, periode 30 detik) untuk kode TOTP valid user NEWDEVE (TC-AUTH-MFA-130, 134); tombol Back browser (TC-AUTH-MFA-129, 130); pembacaan status enrollment Authenticator user oleh sisi BE (TC-AUTH-MFA-131, langkah 76; disediakan tim FE/BE karena tidak ada cara cek di UI atau di Langkah Uji TC; endpoint/skrip tidak didefinisikan di TC, PRD, atau LLD).
- State global: tidak ada yang diubah spec ini (jam server dan counter rate limit tidak disentuh).

## Test Steps

### TC-AUTH-MFA-129: Lima percobaan OTP salah meng-invalidate sesi pre-auth dan mengalihkan ke login

1. Buka halaman `Auth > Login with Password` di browser uji B → halaman Login with Password tampil
2. Ketik `tomihermawan+{runId}-028@qwertysystem.net` pada field Email
3. Ketik `Spectra.env.MFA_PASSWORD` pada field Password
4. Centang widget reCAPTCHA "I'm not a robot"
5. Klik button [Log in] → halaman `Auth > MFA > Choose Verification Method` tampil
6. Pilih opsi "OTP via email" pada halaman Choose Verification Method
7. Klik button [Login] → halaman `Auth > MFA > OTP Verification` tampil dan email OTP faktor-2 terkirim ke `tomihermawan+{runId}-028@qwertysystem.net`
8. Ketik `000001` pada kotak digit (percobaan 1)
9. Verifikasi Percobaan 1: caption "Invalid code" tampil
10. Verifikasi Percobaan 1: halaman tetap OTP Verification
11. Ketik `000002` pada kotak digit (percobaan 2)
12. Verifikasi Percobaan 2: caption "Invalid code" tampil
13. Verifikasi Percobaan 2: halaman tetap OTP Verification
14. Ketik `000003` pada kotak digit (percobaan 3)
15. Verifikasi Percobaan 3: caption "Invalid code" tampil
16. Verifikasi Percobaan 3: halaman tetap OTP Verification
17. Ketik `000004` pada kotak digit (percobaan 4)
18. Verifikasi Percobaan 4: caption "Invalid code" tampil
19. Verifikasi Percobaan 4: halaman tetap OTP Verification
20. Ketik `000005` pada kotak digit (percobaan 5)
21. Verifikasi Percobaan 5: halaman Login with Password tampil (sesi pre-auth di-invalidate)
22. Tanpa login ulang, tekan tombol Back browser untuk kembali ke halaman OTP Verification
23. Ketik 6 digit kode OTP yang benar dari email `tomihermawan+{runId}-028@qwertysystem.net` (dibaca dari mail-catcher) pada kotak digit
24. Verifikasi Kode benar ditolak karena sesi pre-auth sudah tidak berlaku
25. Verifikasi Halaman login tampil
26. Verifikasi Tidak ada sesi penuh untuk `Tomi Hermawan`

### TC-AUTH-MFA-130: Lima percobaan TOTP salah meng-invalidate sesi pre-auth dan mengalihkan ke login

27. Tutup jendela user uji dari TC sebelumnya dan hapus sesi login browser terkait (ID device dan jendela sesi akun aktor tetap), lalu buka jendela privat baru (tanpa sesi login)
28. Buka halaman `Auth > Login with Password` di browser uji B → halaman Login with Password tampil
29. Ketik `ulfarahmi+{runId}-028@qwertysystem.net` pada field Email
30. Ketik `Spectra.env.MFA_PASSWORD` pada field Password
31. Centang widget reCAPTCHA "I'm not a robot"
32. Klik button [Log in] → halaman `Auth > MFA > Choose Verification Method` tampil
33. Pilih opsi "Authenticator app" pada halaman Choose Verification Method
34. Klik button [Login] → halaman `Auth > MFA > Authenticator Verification` tampil
35. Ketik `000001` pada kotak digit lalu klik button [Login] (percobaan 1)
36. Verifikasi Percobaan 1: caption "Invalid code" tampil
37. Verifikasi Percobaan 1: halaman tetap Authenticator Verification
38. Ketik `000002` pada kotak digit lalu klik button [Login] (percobaan 2)
39. Verifikasi Percobaan 2: caption "Invalid code" tampil
40. Verifikasi Percobaan 2: halaman tetap Authenticator Verification
41. Ketik `000003` pada kotak digit lalu klik button [Login] (percobaan 3)
42. Verifikasi Percobaan 3: caption "Invalid code" tampil
43. Verifikasi Percobaan 3: halaman tetap Authenticator Verification
44. Ketik `000004` pada kotak digit lalu klik button [Login] (percobaan 4)
45. Verifikasi Percobaan 4: caption "Invalid code" tampil
46. Verifikasi Percobaan 4: halaman tetap Authenticator Verification
47. Ketik `000005` pada kotak digit lalu klik button [Login] (percobaan 5)
48. Verifikasi Percobaan 5: halaman Login with Password tampil
49. Tanpa login ulang, tekan tombol Back browser untuk kembali ke halaman Authenticator Verification
50. Ketik 6 digit kode TOTP valid dari aplikasi authenticator uji untuk `ulfarahmi+{runId}-028@qwertysystem.net` pada kotak digit
51. Verifikasi Kode benar ditolak karena sesi pre-auth tidak berlaku
52. Verifikasi Halaman login tampil

### TC-AUTH-MFA-131: Lima kode enrollment salah meng-invalidate sesi pre-auth dan mengalihkan ke login

53. Tutup jendela user uji dari TC sebelumnya dan hapus sesi login browser terkait (ID device dan jendela sesi akun aktor tetap), lalu buka jendela baru di browser uji A (tanpa sesi login)
54. Buka halaman `Auth > Login with Password` di browser uji A → halaman Login with Password tampil
55. Ketik `vickyalamsyah+{runId}-028@qwertysystem.net` pada field Email
56. Ketik `Spectra.env.MFA_PASSWORD` pada field Password
57. Centang widget reCAPTCHA "I'm not a robot"
58. Klik button [Log in] → layar Confirm to Continue tampil
59. Centang checkbox persetujuan, lalu klik [Continue ➔] → halaman `Auth > MFA > Choose Verification Method` tampil
60. Pilih opsi "Authenticator app" pada halaman Choose Verification Method
61. Klik button [Login] → halaman `Auth > MFA > Enrollment Authenticator` tampil
62. Ketik `000001` pada kotak digit lalu klik button [Verify] (percobaan 1)
63. Verifikasi Percobaan 1: caption "Invalid code" tampil
64. Verifikasi Percobaan 1: halaman tetap Enrollment Authenticator
65. Ketik `000002` pada kotak digit lalu klik button [Verify] (percobaan 2)
66. Verifikasi Percobaan 2: caption "Invalid code" tampil
67. Verifikasi Percobaan 2: halaman tetap Enrollment Authenticator
68. Ketik `000003` pada kotak digit lalu klik button [Verify] (percobaan 3)
69. Verifikasi Percobaan 3: caption "Invalid code" tampil
70. Verifikasi Percobaan 3: halaman tetap Enrollment Authenticator
71. Ketik `000004` pada kotak digit lalu klik button [Verify] (percobaan 4)
72. Verifikasi Percobaan 4: caption "Invalid code" tampil
73. Verifikasi Percobaan 4: halaman tetap Enrollment Authenticator
74. Ketik `000005` pada kotak digit lalu klik button [Verify] (percobaan 5)
75. Verifikasi Percobaan 5: halaman Login with Password tampil (sesi pre-auth di-invalidate)
76. Verifikasi Enrollment Authenticator `Vicky Alamsyah` tetap belum aktif (Authenticator belum terdaftar)

### TC-AUTH-MFA-133: Verify dengan kode kosong dihitung sebagai percobaan salah

77. Tutup jendela user uji dari TC sebelumnya dan hapus sesi login browser terkait (ID device dan jendela sesi akun aktor tetap), lalu buka jendela privat baru (tanpa sesi login)
78. Buka halaman `Auth > Login with Password` di browser uji B → halaman Login with Password tampil
79. Ketik `yantisusanti+{runId}-028@qwertysystem.net` pada field Email
80. Ketik `Spectra.env.MFA_PASSWORD` pada field Password
81. Centang widget reCAPTCHA "I'm not a robot"
82. Klik button [Log in] → halaman `Auth > MFA > Choose Verification Method` tampil
83. Pilih opsi "Authenticator app" pada halaman Choose Verification Method
84. Klik button [Login] → halaman `Auth > MFA > Authenticator Verification` tampil
85. Klik button [Login] tanpa mengisi kode (percobaan 1)
86. Klik button [Login] tanpa mengisi kode (percobaan 2)
87. Klik button [Login] tanpa mengisi kode (percobaan 3)
88. Klik button [Login] tanpa mengisi kode (percobaan 4)
89. Klik button [Login] tanpa mengisi kode (percobaan 5)
90. Verifikasi Pada klik ke-5: halaman Login with Password tampil
91. Verifikasi Sesi pre-auth MFA `Yanti Susanti` tidak berlaku (kode kosong ikut dihitung sebagai percobaan salah)

### TC-AUTH-MFA-134: Percobaan ke-5 yang benar setelah 4 salah berhasil

92. Tutup jendela user uji dari TC sebelumnya dan hapus sesi login browser terkait (ID device dan jendela sesi akun aktor tetap), lalu buka jendela privat baru (tanpa sesi login)
93. Buka halaman `Auth > Login with Password` di browser uji B → halaman Login with Password tampil
94. Ketik `zakifirdaus+{runId}-028@qwertysystem.net` pada field Email
95. Ketik `Spectra.env.MFA_PASSWORD` pada field Password
96. Centang widget reCAPTCHA "I'm not a robot"
97. Klik button [Log in] → halaman `Auth > MFA > Choose Verification Method` tampil
98. Pilih opsi "Authenticator app" pada halaman Choose Verification Method
99. Klik button [Login] → halaman `Auth > MFA > Authenticator Verification` tampil
100. Ketik `000001` pada kotak digit lalu klik button [Login] (percobaan 1)
101. Ketik `000002` pada kotak digit lalu klik button [Login] (percobaan 2)
102. Ketik `000003` pada kotak digit lalu klik button [Login] (percobaan 3)
103. Ketik `000004` pada kotak digit lalu klik button [Login] (percobaan 4)
104. Ketik 6 digit kode TOTP valid dari aplikasi authenticator uji untuk `zakifirdaus+{runId}-028@qwertysystem.net` pada kotak digit lalu klik button [Login] (percobaan 5, benar)
105. Verifikasi Faktor-2 berhasil pada percobaan ke-5
106. Verifikasi Browser dialihkan ke Portal — Product Hub
107. Verifikasi Sesi web aktif untuk `Zaki Firdaus` (satu sesi web aktif)

### TC-AUTH-MFA-135: Login ulang setelah sesi pre-auth di-invalidate menghasilkan hitungan percobaan baru

108. Tutup jendela user uji dari TC sebelumnya dan hapus sesi login browser terkait (ID device dan jendela sesi akun aktor tetap), lalu buka jendela privat baru (tanpa sesi login)
109. Buka halaman `Auth > Login with Password` di browser uji B → halaman Login with Password tampil
110. Ketik `anggipermana+{runId}-028@qwertysystem.net` pada field Email
111. Ketik `Spectra.env.MFA_PASSWORD` pada field Password
112. Centang widget reCAPTCHA "I'm not a robot"
113. Klik button [Log in] → halaman `Auth > MFA > Choose Verification Method` tampil
114. Pilih opsi "Authenticator app" pada halaman Choose Verification Method
115. Klik button [Login] → halaman `Auth > MFA > Authenticator Verification` tampil
116. Ketik `000001` pada kotak digit lalu klik button [Login] (percobaan 1)
117. Ketik `000002` pada kotak digit lalu klik button [Login] (percobaan 2)
118. Ketik `000003` pada kotak digit lalu klik button [Login] (percobaan 3)
119. Ketik `000004` pada kotak digit lalu klik button [Login] (percobaan 4)
120. Ketik `000005` pada kotak digit lalu klik button [Login] (percobaan 5) → halaman Login with Password tampil
121. Ketik `anggipermana+{runId}-028@qwertysystem.net` pada field Email
122. Ketik `Spectra.env.MFA_PASSWORD` pada field Password
123. Centang widget reCAPTCHA "I'm not a robot"
124. Klik button [Log in] → halaman `Auth > MFA > Choose Verification Method` tampil
125. Pilih opsi "Authenticator app" pada halaman Choose Verification Method
126. Klik button [Login]
127. Verifikasi Login ulang berhasil sampai halaman `Auth > MFA > Authenticator Verification`
128. Ketik `000006` pada kotak digit lalu klik button [Login]
129. Verifikasi Satu kode salah baru menampilkan caption "Invalid code" (hitungan dimulai dari 1)
130. Verifikasi Halaman tetap Authenticator Verification

### TC-AUTH-MFA-132: Batas 5 percobaan salah berlaku gabungan lintas OTP, TOTP, dan enrollment

131. Tutup jendela user uji dari TC sebelumnya dan hapus sesi login browser terkait (ID device dan jendela sesi akun aktor tetap), lalu buka jendela privat baru (tanpa sesi login)
132. Buka halaman `Auth > Login with Password` di browser uji B → halaman Login with Password tampil
133. Ketik `wahyunugroho+{runId}-028@qwertysystem.net` pada field Email
134. Ketik `Spectra.env.MFA_PASSWORD` pada field Password
135. Centang widget reCAPTCHA "I'm not a robot"
136. Klik button [Log in] → halaman `Auth > MFA > Choose Verification Method` tampil
137. Pilih opsi "OTP via email" pada halaman Choose Verification Method
138. Klik button [Login] → halaman `Auth > MFA > OTP Verification` tampil
139. Ketik `000001` pada kotak digit (OTP, percobaan 1)
140. Klik button Text [Use a different method] → halaman Choose Verification Method tampil
141. Pilih opsi "Authenticator app", lalu klik button [Login] → halaman `Auth > MFA > Enrollment Authenticator` tampil
142. Ketik `000002` pada kotak digit lalu klik button [Verify] (enrollment, percobaan 2)
143. Ketik `000003` pada kotak digit lalu klik button [Verify] (enrollment, percobaan 3)
144. Klik button [Cancel] → halaman Choose Verification Method tampil
145. Pilih opsi "OTP via email", lalu klik button [Login] → halaman OTP Verification tampil
146. Ketik `000004` pada kotak digit lalu klik button [Login] (OTP, percobaan 4)
147. Ketik `000005` pada kotak digit lalu klik button [Login] (OTP, percobaan 5)
148. Verifikasi Setelah percobaan ke-5 (gabungan 1 OTP + 2 enrollment + 2 OTP): halaman Login with Password tampil
149. Verifikasi Sesi pre-auth tidak berlaku
150. Verifikasi Hitungan percobaan tidak ter-reset oleh ganti metode (sesi habis pada percobaan ke-5 gabungan walau hanya 2 kode salah pada metode terakhir)

## Notes

- Sumber: `auth/mfa/TestCases/tc-mfa.md`. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. Kelas harness: batas percobaan di sesi pre-auth (tanpa jam server, tanpa multi-konteks).
- Langkah pembuka tiap TC sesudah TC pertama menutup jendela user uji dari TC sebelumnya dan menghapus sesi login browser terkait (ID device dan jendela sesi akun aktor tetap) sebelum jendela baru dibuka; itu langkah penghubung tanpa `Verifikasi` (S-03, S-09).
- Urutan: TC-AUTH-MFA-132 (gabungan lintas OTP, TOTP, dan enrollment; di TC sumber berada sebelum 133) ditaruh paling akhir karena memakai ketiga halaman faktor-2 dan jalur terpanjang (S-05, S-10). Urutan lain mengikuti TC sumber; tiap TC memakai user sendiri sehingga tidak saling bergantung.
- Langkah penghubung tanpa awalan `Verifikasi` (buka jendela baru di awal tiap TC; klik [Login] atau [Verify] untuk mengirim kode pada TC-AUTH-MFA-130, 131, 133, 134, 135 dan pada langkah 142, 143, 146, 147 TC-AUTH-MFA-132; tombol Back browser pada TC-AUTH-MFA-129 dan 130) bukan asersi tambahan (S-03). Langkah 138 tidak mengasersi pengiriman email OTP faktor-2 karena TC-AUTH-MFA-132 tidak punya Expected untuk email itu dan tidak membaca isinya.
- Asersi tambahan (S-03): langkah 25 dan 52 (`Verifikasi Halaman login tampil` sesudah kode benar dikirim pada TC-AUTH-MFA-129 dan 130) tidak ada di Expected TC, yang hanya menyatakan kode benar ditolak karena sesi pre-auth tidak berlaku; langkah itu menjadi penanda penolakan yang teramati di UI, dengan dasar NC-05 TC (keputusan 2026-10-06: kode benar sesudah percobaan ke-5 ditolak dengan redirect ke login).
- Post Condition "Tidak ada sesi penuh" (TC-AUTH-MFA-130, 132) dan "Sesi pre-auth MFA baru aktif" (TC-AUTH-MFA-135) tidak diasersi terpisah: sesi pre-auth teramati sebagai halaman MFA tampil (langkah 127 dan 129 sampai 130) dan ketiadaan sesi sebagai halaman Login with Password tampil (langkah 48, 52, 148); sesi penuh yang ditolak pada TC-AUTH-MFA-129 tetap diasersi karena Expected butir c menyebutnya (langkah 26).
- Melewati ±35 langkah (±115 netto setelah langkah prefix login faktor-1 tidak dihitung) karena tujuh TC independen; tiap TC memakai user dan jendela baru sendiri sehingga bagian sesudahnya tetap bermakna walau bagian sebelumnya gagal, dan spec tidak dipecah.
- Post Condition pencatatan (entri log) tidak diasersi di spec ini; lihat Temuan untuk QA butir 8.
- Temuan untuk QA: (1) Cara mengirim kode berbeda antar TC: TC-AUTH-MFA-129 langkah 8–11 dan TC-AUTH-MFA-130 langkah 11 hanya menyebut mengetik kode tanpa klik [Login], dan TC-AUTH-MFA-132 langkah 8 hanya menyebut mengetik kode, sedangkan TC-AUTH-MFA-130 langkah 8, TC-AUTH-MFA-131 langkah 8, TC-AUTH-MFA-133, 134, dan 135 menyebut klik [Login] atau [Verify]; spec mengikuti teks Langkah Uji tiap TC apa adanya: hanya mengetik pada langkah 8, 11, 14, 17, 20, 23, 50, dan 139 (TC tidak menyebut klik), dan mengetik lalu klik tombol halaman itu pada langkah yang TC-nya menyebut klik, termasuk langkah 146 dan 147 TC-AUTH-MFA-132 yang berada di halaman OTP Verification yang sama dengan langkah 139. Ketidakseragaman yang sama ada pada TC-AUTH-MFA-207 ("ketik kode OTP yang salah lima kali berturut-turut" tanpa klik) serta TC-AUTH-MFA-75 dan 161 ("ketik 6 digit kode OTP" tanpa klik); QA perlu menyeragamkan apakah pengiriman kode memerlukan klik [Login] atau [Verify]. (2) TC-AUTH-MFA-129 dan 130 langkah 11 ("ketik kode benar tanpa login ulang") tidak menjelaskan cara mencapai kotak digit setelah user dialihkan ke halaman login; spec memakai tombol Back browser sebagai langkah penghubung. (3) TC-AUTH-MFA-131 Expected butir c ("Enrollment tetap belum aktif") tidak punya cara pengecekan di Langkah Uji; dibaca dari sisi BE (Prerequisites). (4) TC-AUTH-MFA-133 klik 1–4 tidak punya Expected; spec hanya mengasersi klik ke-5. (5) TC-AUTH-MFA-132 dan 133 berlabel Manual Only tetapi seluruh langkahnya dapat dijalankan lewat UI; tetap masuk spec. (6) TC-AUTH-MFA-132 langkah 11 menyebut button [Cancel] di Enrollment Authenticator; label ini dipakai apa adanya dari TC. (7) Mekanisme seeding state BE profil NEWDEV, NEWDEVE, dan FIRST (trusted device ber-ID device, lokasi login terakhir, secret Authenticator yang dikenal authenticator uji) belum ada di Pre-setup TC (#20/#21 hanya memuat sebagian) dan tidak didefinisikan di PRD atau LLD; spec tidak menyebut endpoint seeding. (8) Post Condition berupa entri log (TC-AUTH-MFA-129 dan 130 "lima entri Failed `Incorrect OTP`", TC-AUTH-MFA-133 "lima entri Failed `Empty OTP`", TC-AUTH-MFA-131 "tidak ada entri log") tidak punya langkah observasi dan tidak punya Expected padanan di TC; spec pencatatan (`TC-AUTH-MFA-E2E-033`, `034`) dan spec absence (`TC-AUTH-MFA-E2E-035`) tidak memuat TC-AUTH-MFA-129 sampai 135 sehingga belum ada spec yang mengasersinya; QA perlu menambah Expected atau langkah observasi, atau TC pencatatan atau absence, atau menghapus Post Condition itu.
