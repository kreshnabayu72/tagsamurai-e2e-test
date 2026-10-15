---
id: TC-AUTH-SES-E2E-070-absence-biometric
title: "Absence Pencatatan Biometric: Kondisi Re-login, Enroll, dan Disable yang Tidak Menulis Session Log Entry"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AUTH-SES-154
  - TC-AUTH-SES-160
  - TC-AUTH-SES-162
  - TC-AUTH-SES-170
  - TC-AUTH-SES-173
  - TC-AUTH-SES-175
  - TC-AUTH-SES-176
  - TC-AUTH-SES-177
  - TC-AUTH-SES-212
  - TC-AUTH-SES-257
  - TC-AUTH-SES-258
  - TC-AUTH-SES-325
  - TC-AUTH-SES-328
coverage:
  web: automated
  mobile: automated
---

# Absence Pencatatan Biometric: Kondisi Re-login, Enroll, dan Disable yang Tidak Menulis Session Log Entry

## Prerequisites

- Mode: FE+BE.
- Platform: aplikasi mobile TAG Samurai (Android) terpasang di perangkat Android uji B (Tabel Data Uji Pre-setup #10: hardware biometric, sidik jari terdaftar di OS) sebagai perangkat biometric re-login untuk semua TC kecuali TC-AUTH-SES-257 dan 258 (hanya request langsung) dan perangkat Android uji A sebagai perangkat sesi mobile lain (TC-AUTH-SES-328). Browser Admin (web) hanya sebagai pengamat log.
- Seeding (hook `before`, lewat API oleh akun aktor Total Control (Global Settings) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.GS_TC_PASSWORD`): tiga belas user profil BIO milik Client `Alpha Logistik` (Tabel Data Uji Pre-setup #5 dan #9: batas idle 15 menit; subscription Fixed Asset dan Supply Asset Active, kuota 5; user Activated, Active ON; MFA dan Agreement tidak terpicu; belum pernah enroll biometric), password `Spectra.env.SES_PASSWORD`, email bersuffix per run, tiap user hanya dipakai satu TC:
  - TC-AUTH-SES-257: `Citra Lestari` (`citralestari+{runId}-070@qwertysystem.net`)
  - TC-AUTH-SES-258: `Yoga Pratama` (`yogapratama+{runId}-070@qwertysystem.net`)
  - TC-AUTH-SES-154: `Agus Firmansyah` (`agusfirmansyah+{runId}-070@qwertysystem.net`)
  - TC-AUTH-SES-160: `Dimas Maulana` (`dimasmaulana+{runId}-070@qwertysystem.net`)
  - TC-AUTH-SES-162: `Eko Setiawan` (`ekosetiawan+{runId}-070@qwertysystem.net`), profil BIOPOL (Tabel Data Uji Pre-setup #22)
  - TC-AUTH-SES-170: `Taufik Hidayat` (`taufikhidayat+{runId}-070@qwertysystem.net`)
  - TC-AUTH-SES-176: `Irfan Rahayu` (`irfanrahayu+{runId}-070@qwertysystem.net`)
  - TC-AUTH-SES-177: `Tari Anggraini` (`tarianggraini+{runId}-070@qwertysystem.net`)
  - TC-AUTH-SES-328: `Nadia Pratama` (`nadiapratama+{runId}-070@qwertysystem.net`)
  - TC-AUTH-SES-325: `Bayu Kusuma` (`bayukusuma+{runId}-070@qwertysystem.net`), profil BIOPOL
  - TC-AUTH-SES-173: `Sari Saputra` (`sarisaputra+{runId}-070@qwertysystem.net`)
  - TC-AUTH-SES-175: `Nadia Damayanti` (`nadiadamayanti+{runId}-070@qwertysystem.net`)
  - TC-AUTH-SES-212: `Rizky Wibowo` (`rizkywibowo+{runId}-070@qwertysystem.net`)
- Kondisi di-seed BE (disediakan tim BE, tanpa endpoint karangan): (a) kredensial biometric Active milik `Citra Lestari` dan `Yoga Pratama` pada ID device perangkat Android uji B, dengan `refreshToken` plaintext diserahkan ke alat uji; (b) pencabutan (revoke) kredensial biometric `Dimas Maulana` pada langkah TC-AUTH-SES-160; (c) kondisi profil BIOPOL untuk `Eko Setiawan` dan `Bayu Kusuma`, diterapkan sesudah enroll; (d) versi Privacy Policy aktif tidak ter-resolve atau belum ada versi terpublikasi (fixture BE) pada langkah TC-AUTH-SES-325.
- Kondisi awal tiap TC yang memakai perangkat Android uji B ("sudah enroll biometric di perangkat Android uji B; tidak ada sesi platform aktif") dibuat di dalam TC mengikuti cara Tabel Data Uji Pre-setup #29: menyalin langkah enroll TC-AUTH-SES-145 (hapus data aplikasi, login, [Enable], lulus sidik jari, hapus app dari recent apps), lalu mengakhiri sesi platform hasil login enroll lewat API yang disediakan tim BE tanpa menghapus token biometric lokal dan tanpa Log Out lewat UI. Token biometric lokal dan status "sudah ditawari" disimpan di perangkat dan hanya dapat dibuat oleh aplikasi. Pada TC-AUTH-SES-177 dan TC-AUTH-SES-212 tidak ada langkah "hapus app dari recent apps" dan akhiri sesi karena TC mensyaratkan sesi mobile aktif. Pada TC-AUTH-SES-328 sesi mobile aktif di perangkat Android uji A dibuat sesudah enroll di perangkat B (login nyata di perangkat A dengan [Not now], Tabel Data Uji Pre-setup #28).
- Konteks dan akun (dibuka di hook `before`, login pertama tiap konteks ada di hook):
  - Browser Admin: akun aktor Total Control (Global Settings) di atas, dipakai membaca `Global Settings > Activity Log > Session` dan `Global Settings > User > Detail > User Log` (semua TC) serta mematikan Toggle Active `Irfan Rahayu` di `Global Settings > User` (TC-AUTH-SES-176).
  - Perangkat Android uji B (semua TC kecuali 257 dan 258) dan perangkat Android uji A (TC-AUTH-SES-328: login `Nadia Pratama` di perangkat A tanpa mengaktifkan biometric, sehingga sesi mobile aktif di A).
- Suite berjalan serial (`parallel: false`); state global yang diubah dan pemulihannya di hook `after` (tetap jalan walau spec gagal di tengah): (a) jam server dan jam browser/perangkat (diatur bersama, dimajukan 91 hari pada TC-AUTH-SES-173; keduanya dikembalikan ke waktu nyata); (b) counter IP rate limit relogin biometric dari IP alat uji dan perangkat (TC-AUTH-SES-175; nilai awal nol, di-reset ke nol oleh kemampuan reset counter di hook `before` dan `after`, disediakan tim FE/BE, tanpa menunggu jendela berakhir); (c) versi Privacy Policy aktif (TC-AUTH-SES-325; dipulihkan ke versi terpublikasi); (d) status Active user `Irfan Rahayu` (TC-AUTH-SES-176; user dihapus); (e) sesi Browser Admin dapat kedaluwarsa oleh pergeseran jam TC-AUTH-SES-173, sehingga akun aktor login ulang sesudah jam dipulihkan.
- Hook `before`: reset counter IP rate limit relogin biometric ke nol.
- Hook `after`: pulihkan keempat state global di atas (termasuk reset counter IP rate limit ke nol), hapus data aplikasi pada perangkat Android uji A dan B, cabut kredensial biometric seed, akhiri semua sesi seed, tutup Browser Admin, lalu hapus ketiga belas user. Pembersihan tetap jalan walau spec gagal di tengah dan tidak berasumsi seeding berhasil penuh.
- Environment variable: `GS_TC_PASSWORD`, `SES_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Kemampuan teknis (kelas harness g, dengan pemicu kelas d: hardware biometrik dan time-travel; kelas a dan b: request langsung dan rate limit): driver otomasi Android (aplikasi native) untuk dua perangkat; simulasi sensor sidik jari pada OS biometric prompt (sidik jari terdaftar lulus, sidik jari tidak terdaftar gagal); menghapus data aplikasi dan menghapus app dari recent apps lalu membukanya kembali; API untuk mengakhiri sesi platform hasil login enroll tanpa menghapus token biometric lokal (disediakan tim BE); reset counter IP rate limit ke nol (disediakan tim FE/BE); REST client alat uji yang dapat mengirim request langsung ke `POST /v2/iam/auth/biometric/relogin` (body `deviceId` dan `refreshToken`; sumber: `auth/session-management/API/openapi.yaml`); alat uji dan perangkat Android uji B keluar dari IP yang sama sehingga memakai kunci IP rate limit yang sama (Tabel Data Uji Pre-setup #18: threshold IP rate limit lingkungan uji diketahui); pengatur waktu server uji (Tabel Data Uji Pre-setup #18) yang dapat dimajukan 91 hari dan dikembalikan; fixture BE untuk versi Privacy Policy aktif tidak ter-resolve dan untuk kondisi profil BIOPOL; pembacaan jumlah entri dan stempel waktu entri log untuk membedakan entri baru dari entri seeding (termasuk entri bersetempel jam server yang dimajukan pada TC-AUTH-SES-173, dibandingkan sebagai selisih jumlah terhadap baseline); reCAPTCHA mode uji di environment untuk login web (halaman Login with Password).
- Akun yang dipakai: user uji masing-masing TC pada aplikasi mobile atau request langsung; akun aktor Total Control hanya di Browser Admin.

## Test Steps

### TC-AUTH-SES-257 (bagian absence, Expected b): Biometric re-login dengan ID device yang tidak cocok tidak dicatat

1. Kirim request relogin (`POST /v2/iam/auth/biometric/relogin`) dengan `refreshToken` valid milik `Citra Lestari` dan `deviceId` milik perangkat lain (bukan perangkat Android uji B) → server menolak
2. Pindah ke Browser Admin, buka `Global Settings > Activity Log > Session`, dan cari entri untuk `Citra Lestari` yang dibuat sesudah langkah 1 dimulai
3. Verifikasi Tidak ada entri baru untuk `Citra Lestari` di `Global Settings > Activity Log > Session` untuk kondisi Biometric re-login dengan ID device yang tidak cocok
4. Buka `Global Settings > User > Detail > User Log` milik `Citra Lestari` dan cari entri yang dibuat sesudah langkah 1 dimulai
5. Verifikasi Tidak ada entri baru di `Global Settings > User > Detail > User Log` untuk kondisi Biometric re-login dengan ID device yang tidak cocok

### TC-AUTH-SES-258 (bagian absence, Expected b): Biometric re-login dengan token yang tidak ditemukan di server tidak dicatat

6. Kirim request relogin (`POST /v2/iam/auth/biometric/relogin`) dengan `refreshToken` acak yang tidak pernah diterbitkan dan `deviceId` perangkat Android uji B → server menolak
7. Pindah ke Browser Admin, buka `Global Settings > Activity Log > Session`, dan cari entri untuk `Yoga Pratama` yang dibuat sesudah langkah 6 dimulai
8. Verifikasi Tidak ada entri baru untuk `Yoga Pratama` di `Global Settings > Activity Log > Session` untuk kondisi Biometric re-login dengan token yang tidak ditemukan di server
9. Buka `Global Settings > User > Detail > User Log` milik `Yoga Pratama` dan cari entri yang dibuat sesudah langkah 6 dimulai
10. Verifikasi Tidak ada entri baru di `Global Settings > User > Detail > User Log` untuk kondisi Biometric re-login dengan token yang tidak ditemukan di server

### TC-AUTH-SES-154 (bagian absence, Expected b): Biometric gagal pertama tidak dicatat

11. Hapus data aplikasi di perangkat Android uji B lalu buka aplikasi mobile → halaman Login tampil
12. Ketik `agusfirmansyah+{runId}-070@qwertysystem.net` pada field Email
13. Ketik `Spectra.env.SES_PASSWORD` pada field Password
14. Klik [Login] → Prompt Enable Biometric muncul
15. Ketuk [Enable] → OS biometric prompt muncul
16. Lulus verifikasi sidik jari yang terdaftar pada OS biometric prompt
17. Hapus app dari recent apps
18. Akhiri sesi platform `Agus Firmansyah` hasil login enroll lewat API yang disediakan tim BE (tanpa menghapus token biometric lokal dan tanpa Log Out lewat UI; Tabel Data Uji Pre-setup #29) → perangkat Android uji B tanpa sesi platform aktif
19. Buka aplikasi mobile di perangkat Android uji B → Screen biometric sign-in tampil dan OS biometric prompt muncul otomatis
20. Tempelkan sidik jari yang tidak terdaftar pada OS biometric prompt → tombol [Try Again] tampil
21. Pindah ke Browser Admin, buka `Global Settings > Activity Log > Session`, dan cari entri untuk `Agus Firmansyah` yang dibuat sesudah langkah 19 dimulai
22. Verifikasi Tidak ada entri baru untuk `Agus Firmansyah` di `Global Settings > Activity Log > Session` untuk kondisi Biometric gagal pertama
23. Buka `Global Settings > User > Detail > User Log` milik `Agus Firmansyah` dan cari entri yang dibuat sesudah langkah 19 dimulai
24. Verifikasi Tidak ada entri baru di `Global Settings > User > Detail > User Log` untuk kondisi Biometric gagal pertama

### TC-AUTH-SES-160 (bagian absence, Expected c): Token biometric tidak valid dan fallback ke Login penuh tidak dicatat

25. Hapus data aplikasi di perangkat Android uji B lalu buka aplikasi mobile → halaman Login tampil
26. Ketik `dimasmaulana+{runId}-070@qwertysystem.net` pada field Email
27. Ketik `Spectra.env.SES_PASSWORD` pada field Password
28. Klik [Login] → Prompt Enable Biometric muncul
29. Ketuk [Enable] → OS biometric prompt muncul
30. Lulus verifikasi sidik jari yang terdaftar pada OS biometric prompt
31. Hapus app dari recent apps
32. Akhiri sesi platform `Dimas Maulana` hasil login enroll lewat API yang disediakan tim BE (tanpa menghapus token biometric lokal dan tanpa Log Out lewat UI; Tabel Data Uji Pre-setup #29) → perangkat Android uji B tanpa sesi platform aktif
33. Cabut (revoke) kredensial biometric `Dimas Maulana` di server (kondisi di-seed BE)
34. Buka aplikasi mobile di perangkat Android uji B → Screen biometric sign-in tampil dan OS biometric prompt muncul otomatis
35. Lulus verifikasi sidik jari yang terdaftar pada OS biometric prompt → server menolak (401 token tidak valid), token lokal dihapus, dan halaman Login penuh tampil
36. Pindah ke Browser Admin, buka `Global Settings > Activity Log > Session`, dan cari entri untuk `Dimas Maulana` yang dibuat sesudah langkah 34 dimulai
37. Verifikasi Tidak ada entri baru untuk `Dimas Maulana` di `Global Settings > Activity Log > Session` untuk kondisi token biometric tidak valid
38. Buka `Global Settings > User > Detail > User Log` milik `Dimas Maulana` dan cari entri yang dibuat sesudah langkah 34 dimulai
39. Verifikasi Tidak ada entri baru di `Global Settings > User > Detail > User Log` untuk kondisi token biometric tidak valid

### TC-AUTH-SES-162 (bagian absence, Expected c): Persetujuan Agreement pada biometric re-login tidak dicatat tersendiri

40. Hapus data aplikasi di perangkat Android uji B lalu buka aplikasi mobile → halaman Login tampil
41. Ketik `ekosetiawan+{runId}-070@qwertysystem.net` pada field Email
42. Ketik `Spectra.env.SES_PASSWORD` pada field Password
43. Klik [Login] → Prompt Enable Biometric muncul
44. Ketuk [Enable] → OS biometric prompt muncul
45. Lulus verifikasi sidik jari yang terdaftar pada OS biometric prompt
46. Hapus app dari recent apps
47. Akhiri sesi platform `Eko Setiawan` hasil login enroll lewat API yang disediakan tim BE (tanpa menghapus token biometric lokal dan tanpa Log Out lewat UI; Tabel Data Uji Pre-setup #29) → perangkat Android uji B tanpa sesi platform aktif
48. Terapkan kondisi profil BIOPOL untuk `Eko Setiawan` (versi Privacy Policy aktif lebih baru dari yang terakhir disetujui; di-seed BE)
49. Buka aplikasi mobile di perangkat Android uji B → Screen biometric sign-in tampil dan OS biometric prompt muncul otomatis
50. Lulus verifikasi sidik jari yang terdaftar pada OS biometric prompt → Screen Confirm to Continue tampil
51. Centang checkbox "I have read and agree to the Privacy Policy *" lalu ketuk [Continue ➔] → app masuk Portal — Product Hub
52. Pindah ke Browser Admin, buka `Global Settings > Activity Log > Session`, dan cari entri untuk `Eko Setiawan` yang dibuat sesudah langkah 49 dimulai
53. Verifikasi Tidak ada entri tersendiri untuk persetujuan Agreement: entri baru untuk `Eko Setiawan` di `Global Settings > Activity Log > Session` hanya `Login with biometric` untuk kondisi persetujuan Agreement pada biometric re-login
54. Buka `Global Settings > User > Detail > User Log` milik `Eko Setiawan` dan cari entri yang dibuat sesudah langkah 49 dimulai
55. Verifikasi Tidak ada entri tersendiri untuk persetujuan Agreement: entri baru untuk `Eko Setiawan` di `Global Settings > User > Detail > User Log` hanya `Login with biometric` untuk kondisi persetujuan Agreement pada biometric re-login

### TC-AUTH-SES-170 (bagian absence, Expected b): Kegagalan biometric tidak menambah entri kegagalan password

56. Hapus data aplikasi di perangkat Android uji B lalu buka aplikasi mobile → halaman Login tampil
57. Ketik `taufikhidayat+{runId}-070@qwertysystem.net` pada field Email
58. Ketik `Spectra.env.SES_PASSWORD` pada field Password
59. Klik [Login] → Prompt Enable Biometric muncul
60. Ketuk [Enable] → OS biometric prompt muncul
61. Lulus verifikasi sidik jari yang terdaftar pada OS biometric prompt
62. Hapus app dari recent apps
63. Akhiri sesi platform `Taufik Hidayat` hasil login enroll lewat API yang disediakan tim BE (tanpa menghapus token biometric lokal dan tanpa Log Out lewat UI; Tabel Data Uji Pre-setup #29) → perangkat Android uji B tanpa sesi platform aktif
64. Buka aplikasi mobile di perangkat Android uji B → Screen biometric sign-in tampil dan OS biometric prompt muncul otomatis
65. Tempelkan sidik jari yang tidak terdaftar pada OS biometric prompt (kegagalan biometric ke-1)
66. Ketuk [Try Again]
67. Tempelkan sidik jari yang tidak terdaftar pada OS biometric prompt (kegagalan biometric ke-2)
68. Ketuk tautan "Sign in with password instead"
69. Hapus app dari recent apps
70. Buka aplikasi mobile di perangkat Android uji B → Screen biometric sign-in tampil dan OS biometric prompt muncul otomatis
71. Tempelkan sidik jari yang tidak terdaftar pada OS biometric prompt (kegagalan biometric ke-3)
72. Ketuk [Try Again]
73. Tempelkan sidik jari yang tidak terdaftar pada OS biometric prompt (kegagalan biometric ke-4)
74. Ketuk [Try Again]
75. Tempelkan sidik jari yang tidak terdaftar pada OS biometric prompt (kegagalan biometric ke-5)
76. Ketuk tautan "Sign in with password instead" → halaman Login penuh tampil
77. Ketik `taufikhidayat+{runId}-070@qwertysystem.net` pada field Email
78. Ketik `Spectra.env.SES_PASSWORD` pada field Password
79. Klik [Login] → app masuk Portal — Product Hub
80. Pindah ke Browser Admin, buka `Global Settings > Activity Log > Session`, dan cari entri untuk `Taufik Hidayat` yang dibuat sesudah langkah 64 dimulai
81. Verifikasi Tidak ada entri baru untuk `Taufik Hidayat` di `Global Settings > Activity Log > Session` dengan Note `Incorrect password` untuk kondisi kegagalan biometric
82. Verifikasi Tidak ada entri baru untuk `Taufik Hidayat` di `Global Settings > Activity Log > Session` dengan Note `Locked` untuk kondisi kegagalan biometric
83. Buka `Global Settings > User > Detail > User Log` milik `Taufik Hidayat` dan cari entri yang dibuat sesudah langkah 64 dimulai
84. Verifikasi Tidak ada entri baru untuk `Taufik Hidayat` di `Global Settings > User > Detail > User Log` dengan Note `Incorrect password` untuk kondisi kegagalan biometric
85. Verifikasi Tidak ada entri baru untuk `Taufik Hidayat` di `Global Settings > User > Detail > User Log` dengan Note `Locked` untuk kondisi kegagalan biometric

### TC-AUTH-SES-176 (bagian absence, Expected b): Token biometric ditolak karena akun dinonaktifkan tidak dicatat

86. Hapus data aplikasi di perangkat Android uji B lalu buka aplikasi mobile → halaman Login tampil
87. Ketik `irfanrahayu+{runId}-070@qwertysystem.net` pada field Email
88. Ketik `Spectra.env.SES_PASSWORD` pada field Password
89. Klik [Login] → Prompt Enable Biometric muncul
90. Ketuk [Enable] → OS biometric prompt muncul
91. Lulus verifikasi sidik jari yang terdaftar pada OS biometric prompt
92. Hapus app dari recent apps
93. Akhiri sesi platform `Irfan Rahayu` hasil login enroll lewat API yang disediakan tim BE (tanpa menghapus token biometric lokal dan tanpa Log Out lewat UI; Tabel Data Uji Pre-setup #29) → perangkat Android uji B tanpa sesi platform aktif
94. Pindah ke Browser Admin (akun aktor Total Control sudah login di hook)
95. Matikan Toggle Active `Irfan Rahayu` di `Global Settings > User`
96. Buka aplikasi mobile di perangkat Android uji B → Screen biometric sign-in tampil dan OS biometric prompt muncul otomatis
97. Lulus verifikasi sidik jari yang terdaftar pada OS biometric prompt → re-login ditolak, token lokal dihapus, dan halaman Login penuh tampil
98. Pindah ke Browser Admin, buka `Global Settings > Activity Log > Session`, dan cari entri untuk `Irfan Rahayu` yang dibuat sesudah langkah 96 dimulai
99. Verifikasi Tidak ada entri baru untuk `Irfan Rahayu` di `Global Settings > Activity Log > Session` untuk kondisi token biometric Active ditolak karena akun dinonaktifkan
100. Buka `Global Settings > User > Detail > User Log` milik `Irfan Rahayu` dan cari entri yang dibuat sesudah langkah 96 dimulai
101. Verifikasi Tidak ada entri baru di `Global Settings > User > Detail > User Log` untuk kondisi token biometric Active ditolak karena akun dinonaktifkan

### TC-AUTH-SES-177 (bagian absence, Expected c): Disable biometric lewat toggle Settings > Security tidak dicatat

102. Hapus data aplikasi di perangkat Android uji B lalu buka aplikasi mobile → halaman Login tampil
103. Ketik `tarianggraini+{runId}-070@qwertysystem.net` pada field Email
104. Ketik `Spectra.env.SES_PASSWORD` pada field Password
105. Klik [Login] → Prompt Enable Biometric muncul
106. Ketuk [Enable] → OS biometric prompt muncul
107. Lulus verifikasi sidik jari yang terdaftar pada OS biometric prompt
108. Buka Settings > Security di aplikasi mobile perangkat Android uji B (sesi mobile aktif di Portal — Product Hub)
109. Matikan toggle "Face ID / Touch ID" → toggle dinonaktifkan dan toast sukses tampil
110. Pindah ke Browser Admin, buka `Global Settings > Activity Log > Session`, dan cari entri untuk `Tari Anggraini` yang dibuat sesudah langkah 109 dimulai
111. Verifikasi Tidak ada entri baru untuk `Tari Anggraini` di `Global Settings > Activity Log > Session` untuk kondisi Disable biometric lewat toggle Settings > Security
112. Buka `Global Settings > User > Detail > User Log` milik `Tari Anggraini` dan cari entri yang dibuat sesudah langkah 109 dimulai
113. Verifikasi Tidak ada entri baru di `Global Settings > User > Detail > User Log` untuk kondisi Disable biometric lewat toggle Settings > Security

### TC-AUTH-SES-328 (bagian absence, Expected b): Cancel pada Dialog Duplicate Login Attempt dari biometric re-login tidak dicatat

114. Hapus data aplikasi di perangkat Android uji B lalu buka aplikasi mobile → halaman Login tampil
115. Ketik `nadiapratama+{runId}-070@qwertysystem.net` pada field Email
116. Ketik `Spectra.env.SES_PASSWORD` pada field Password
117. Klik [Login] → Prompt Enable Biometric muncul
118. Ketuk [Enable] → OS biometric prompt muncul
119. Lulus verifikasi sidik jari yang terdaftar pada OS biometric prompt
120. Hapus app dari recent apps
121. Akhiri sesi platform `Nadia Pratama` hasil login enroll lewat API yang disediakan tim BE (tanpa menghapus token biometric lokal dan tanpa Log Out lewat UI; Tabel Data Uji Pre-setup #29) → perangkat Android uji B tanpa sesi platform aktif
122. Di perangkat Android uji A login dengan `nadiapratama+{runId}-070@qwertysystem.net` dan password `Spectra.env.SES_PASSWORD`, ketuk [Not now] pada Prompt Enable Biometric → app masuk Portal — Product Hub (sesi mobile aktif di perangkat A)
123. Buka aplikasi mobile di perangkat Android uji B → Screen biometric sign-in tampil dan OS biometric prompt muncul otomatis
124. Lulus verifikasi sidik jari yang terdaftar pada OS biometric prompt → Dialog Duplicate Login Attempt muncul
125. Ketuk [Cancel]
126. Pindah ke Browser Admin, buka `Global Settings > Activity Log > Session`, dan cari entri untuk `Nadia Pratama` yang dibuat sesudah langkah 123 dimulai
127. Verifikasi Tidak ada entri `Login with biometric` baru untuk `Nadia Pratama` di `Global Settings > Activity Log > Session` untuk kondisi Cancel pada Dialog Duplicate Login Attempt dari biometric re-login
128. Verifikasi Tidak ada entri `Logged out (new device login)` baru untuk `Nadia Pratama` di `Global Settings > Activity Log > Session` untuk kondisi Cancel pada Dialog Duplicate Login Attempt dari biometric re-login
129. Buka `Global Settings > User > Detail > User Log` milik `Nadia Pratama` dan cari entri yang dibuat sesudah langkah 123 dimulai
130. Verifikasi Tidak ada entri `Login with biometric` baru untuk `Nadia Pratama` di `Global Settings > User > Detail > User Log` untuk kondisi Cancel pada Dialog Duplicate Login Attempt dari biometric re-login
131. Verifikasi Tidak ada entri `Logged out (new device login)` baru untuk `Nadia Pratama` di `Global Settings > User > Detail > User Log` untuk kondisi Cancel pada Dialog Duplicate Login Attempt dari biometric re-login

### TC-AUTH-SES-325 (bagian absence, Expected c): Biometric re-login diblok karena versi Privacy Policy tidak dapat ditentukan tidak dicatat

132. Hapus data aplikasi di perangkat Android uji B lalu buka aplikasi mobile → halaman Login tampil
133. Ketik `bayukusuma+{runId}-070@qwertysystem.net` pada field Email
134. Ketik `Spectra.env.SES_PASSWORD` pada field Password
135. Klik [Login] → Prompt Enable Biometric muncul
136. Ketuk [Enable] → OS biometric prompt muncul
137. Lulus verifikasi sidik jari yang terdaftar pada OS biometric prompt
138. Hapus app dari recent apps
139. Akhiri sesi platform `Bayu Kusuma` hasil login enroll lewat API yang disediakan tim BE (tanpa menghapus token biometric lokal dan tanpa Log Out lewat UI; Tabel Data Uji Pre-setup #29) → perangkat Android uji B tanpa sesi platform aktif
140. Terapkan kondisi profil BIOPOL untuk `Bayu Kusuma` (versi Privacy Policy aktif lebih baru dari yang terakhir disetujui; di-seed BE)
141. Atur versi Privacy Policy aktif menjadi tidak ter-resolve atau belum ada versi terpublikasi (fixture BE)
142. Buka aplikasi mobile di perangkat Android uji B → Screen biometric sign-in tampil dan OS biometric prompt muncul otomatis
143. Lulus verifikasi sidik jari yang terdaftar pada OS biometric prompt → toast gagal tampil dan Screen Confirm to Continue tidak tampil
144. Pindah ke Browser Admin, buka `Global Settings > Activity Log > Session`, dan cari entri untuk `Bayu Kusuma` yang dibuat sesudah langkah 142 dimulai
145. Verifikasi Tidak ada entri baru untuk `Bayu Kusuma` di `Global Settings > Activity Log > Session` untuk kondisi Biometric re-login diblok karena versi Privacy Policy aktif tidak dapat ditentukan
146. Buka `Global Settings > User > Detail > User Log` milik `Bayu Kusuma` dan cari entri yang dibuat sesudah langkah 142 dimulai
147. Verifikasi Tidak ada entri baru di `Global Settings > User > Detail > User Log` untuk kondisi Biometric re-login diblok karena versi Privacy Policy aktif tidak dapat ditentukan
148. Pulihkan versi Privacy Policy aktif sehingga dapat ditentukan (fixture BE)

### TC-AUTH-SES-173 (bagian absence, Expected b): Token biometric kedaluwarsa lebih dari 90 hari tidak dicatat

149. Hapus data aplikasi di perangkat Android uji B lalu buka aplikasi mobile → halaman Login tampil
150. Ketik `sarisaputra+{runId}-070@qwertysystem.net` pada field Email
151. Ketik `Spectra.env.SES_PASSWORD` pada field Password
152. Klik [Login] → Prompt Enable Biometric muncul
153. Ketuk [Enable] → OS biometric prompt muncul
154. Lulus verifikasi sidik jari yang terdaftar pada OS biometric prompt
155. Hapus app dari recent apps
156. Akhiri sesi platform `Sari Saputra` hasil login enroll lewat API yang disediakan tim BE (tanpa menghapus token biometric lokal dan tanpa Log Out lewat UI; Tabel Data Uji Pre-setup #29) → perangkat Android uji B tanpa sesi platform aktif
157. Di Browser Admin buka `Global Settings > Activity Log > Session` dan `Global Settings > User > Detail > User Log` milik `Sari Saputra`, lalu catat baseline: jumlah entri `Sari Saputra` (dicari lewat Note dan email `sarisaputra+{runId}-070@qwertysystem.net`) dan stempel waktu entri terbaru di kedua surface
158. Majukan jam server dan jam browser/perangkat bersama 91 hari
159. Buka aplikasi mobile di perangkat Android uji B → Screen biometric sign-in tampil dan OS biometric prompt muncul otomatis
160. Lulus verifikasi sidik jari yang terdaftar pada OS biometric prompt → server menolak karena masa berlaku lewat, token lokal dihapus, dan halaman Login penuh tampil
161. Pulihkan jam server dan jam browser/perangkat ke waktu nyata
162. Di Browser Admin login ulang dengan akun aktor Total Control (Global Settings) dan password `Spectra.env.GS_TC_PASSWORD` (jam digeser melewati batas idle)
163. Pindah ke Browser Admin, buka `Global Settings > Activity Log > Session`, dan hitung entri `Sari Saputra` lewat Note dan email `sarisaputra+{runId}-070@qwertysystem.net` (termasuk entri bercap jam server yang dimajukan), lalu bandingkan dengan baseline langkah 157
164. Verifikasi Tidak ada entri baru untuk `Sari Saputra` di `Global Settings > Activity Log > Session` untuk kondisi token biometric yang tidak dipakai lebih dari 90 hari: jumlah entri sama dengan baseline langkah 157
165. Buka `Global Settings > User > Detail > User Log` milik `Sari Saputra` dan hitung entri lewat Note dan email, lalu bandingkan dengan baseline langkah 157
166. Verifikasi Tidak ada entri baru di `Global Settings > User > Detail > User Log` untuk kondisi token biometric yang tidak dipakai lebih dari 90 hari: jumlah entri sama dengan baseline langkah 157

### TC-AUTH-SES-175 (bagian absence, Expected b): Biometric re-login yang melampaui IP rate limit tidak dicatat

167. Hapus data aplikasi di perangkat Android uji B lalu buka aplikasi mobile → halaman Login tampil
168. Ketik `nadiadamayanti+{runId}-070@qwertysystem.net` pada field Email
169. Ketik `Spectra.env.SES_PASSWORD` pada field Password
170. Klik [Login] → Prompt Enable Biometric muncul
171. Ketuk [Enable] → OS biometric prompt muncul
172. Lulus verifikasi sidik jari yang terdaftar pada OS biometric prompt
173. Hapus app dari recent apps
174. Akhiri sesi platform `Nadia Damayanti` hasil login enroll lewat API yang disediakan tim BE (tanpa menghapus token biometric lokal dan tanpa Log Out lewat UI; Tabel Data Uji Pre-setup #29) → perangkat Android uji B tanpa sesi platform aktif
175. Kirim request relogin biometric (`POST /v2/iam/auth/biometric/relogin`) dengan `refreshToken` acak yang tidak pernah diterbitkan dan `deviceId` perangkat Android uji B, berulang dari IP yang sama sampai batas IP rate limit terlampaui
176. Buka aplikasi mobile di perangkat Android uji B → Screen biometric sign-in tampil dan OS biometric prompt muncul otomatis
177. Lulus verifikasi sidik jari yang terdaftar pada OS biometric prompt → toast error tampil (satu request relogin lagi dari IP yang sama)
178. Pindah ke Browser Admin, buka `Global Settings > Activity Log > Session`, dan cari entri untuk `Nadia Damayanti` yang dibuat sesudah langkah 175 dimulai
179. Verifikasi Tidak ada entri baru untuk `Nadia Damayanti` di `Global Settings > Activity Log > Session` untuk kondisi Biometric re-login yang melampaui IP rate limit
180. Buka `Global Settings > User > Detail > User Log` milik `Nadia Damayanti` dan cari entri yang dibuat sesudah langkah 175 dimulai
181. Verifikasi Tidak ada entri baru di `Global Settings > User > Detail > User Log` untuk kondisi Biometric re-login yang melampaui IP rate limit

### TC-AUTH-SES-212 (seluruhnya absence): Biometric Enroll dan Disable tidak dicatat

182. Hapus data aplikasi di perangkat Android uji B lalu buka aplikasi mobile (tanpa sesi platform aktif dan tanpa token biometric lokal) → halaman Login tampil
183. Ketik `rizkywibowo+{runId}-070@qwertysystem.net` pada field Email
184. Ketik `Spectra.env.SES_PASSWORD` pada field Password
185. Klik [Login] → Prompt Enable Biometric muncul
186. Ketuk [Enable] → OS biometric prompt muncul
187. Lulus verifikasi sidik jari yang terdaftar pada OS biometric prompt → app masuk Portal — Product Hub
188. Buka Settings > Security di aplikasi mobile perangkat Android uji B dan matikan toggle "Face ID / Touch ID"
189. Pindah ke Browser Admin, buka `Global Settings > Activity Log > Session`, dan cari entri untuk `Rizky Wibowo` yang dibuat sesudah langkah 185 dimulai
190. Verifikasi Tidak ada entri baru untuk Enroll dan Disable biometric di `Global Settings > Activity Log > Session` untuk `Rizky Wibowo` (entri baru satu-satunya adalah login dengan password pada langkah 185)
191. Buka `Global Settings > User > Detail > User Log` milik `Rizky Wibowo` dan cari entri yang dibuat sesudah langkah 185 dimulai
192. Verifikasi Tidak ada entri baru untuk Enroll dan Disable biometric di `Global Settings > User > Detail > User Log` milik `Rizky Wibowo` (entri baru satu-satunya adalah login dengan password pada langkah 185)

## Notes

- Sumber: `auth/session-management/TestCases/tc-session-management.md`. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. Spec ini memuat klausa absence (kelas g, "tidak ada entri log / tidak dicatat") dari TC biometric; asersi fungsional (dialog, toast, status sesi, token lokal dihapus, Screen yang tampil) tidak diulang dan tetap di spec asal. TC-AUTH-SES-212 seluruhnya asersi absence dan tidak punya spec asal lain; Expected butir c TC-AUTH-SES-145 (spec asal `TC-AUTH-SES-E2E-044`) dipenuhi lewat TC-AUTH-SES-212 di spec ini; asersi pencatatan presence biometric (TC-AUTH-SES-209, 210, 267) ada di spec `TC-AUTH-SES-E2E-059-pencatatan-biometric`.
- Spec ini memuat 192 langkah karena tiga belas TC absence biometric masing-masing membutuhkan blok enroll sendiri (hapus data aplikasi, login, [Enable], sidik jari, akhiri sesi enroll) dan pembacaan dua surface log; blok enroll dan pembacaan log tidak dihitung terhadap batas sekitar 35 langkah. Tiap TC memakai user dan baseline sendiri sehingga bagian sesudahnya tetap bermakna walau TC sebelumnya gagal.
- Pembagian TC lintas spec (prinsip 10): tiap TC selain TC-AUTH-SES-212 punya spec asal yang memegang asersi fungsional dan merujuk spec ini di Expected butir absence-nya (S-05).
- TC-AUTH-SES-212: langkah 182–188 disalin dari TC-AUTH-SES-145 (login, [Enable], lulus sidik jari; langkah 4 tidak disalin karena memicu Re-login biometric yang menulis entri `Login with biometric` dan mengotori asersi absence) dan TC-AUTH-SES-177 (matikan toggle). Baseline entri (S-12): hanya entri yang dibuat sesudah langkah 185 dihitung, dibedakan dari entri seeding lewat stempel waktu; satu-satunya entri baru yang diharapkan adalah login dengan password (Success, Note `Login with password`).
- TC-AUTH-SES-173 (langkah 157 sampai 166): jam server digeser 91 hari sehingga entri yang dibuat selama pergeseran bisa bercap waktu di masa depan dan jatuh di bawah penanda waktu biasa. Baseline jumlah entri `Sari Saputra` dan stempel entri terbaru di kedua surface dicatat sebelum jam digeser (langkah 157); sesudah jam dipulihkan dan akun aktor login ulang, absence diasersi sebagai jumlah entri yang tidak berubah terhadap baseline, dengan entri dicari lewat Note dan email, bukan posisi teratas (S-12).
- Temuan untuk QA (TC-AUTH-SES-212): precondition "profil BIO" tidak menyebut sudah atau belum enroll, sedangkan dependensi TC-AUTH-SES-145 mensyaratkan belum pernah enroll dan TC-AUTH-SES-177 mensyaratkan sudah enroll serta "tidak ada sesi platform aktif" bersamaan dengan "sesi mobile aktif"; spec memakai urutan enroll lalu disable dalam satu sesi mobile aktif. TC tidak menyebut entri `Login with password` yang tertulis pada login langkah 185; spec mengecualikannya dari asersi "tidak ada entri baru" dan menyebutnya eksplisit.
- Temuan untuk QA (TC-AUTH-SES-257 dan 258): TC-257 Data Uji menyebut `refreshToken` plaintext diserahkan ke alat uji oleh seed BE saat enroll lewat API (plaintext hanya dikembalikan sekali saat enroll, sehingga tidak dapat dibaca dari perangkat); TC-258 tidak menyebut cara menyiapkan enroll dan memakai token acak. Spec memakai seed BE yang disediakan tim BE untuk `Citra Lestari` dan `Yoga Pratama` (Prerequisites).
- Temuan untuk QA (TC-AUTH-SES-162 dan 325): kondisi profil BIOPOL diterapkan BE sesudah enroll (langkah "Terapkan kondisi") supaya login password saat enroll tidak memicu Agreement; TC hanya menyebut profil BIOPOL tanpa urutan terhadap enroll.
- Temuan untuk QA (TC-AUTH-SES-175): TC menyebut "Threshold: belum ditetapkan" dan tidak menyebut mekanisme reset counter IP rate limit maupun nilai awalnya; spec mengandalkan kemampuan reset counter ke nol di hook `before` dan `after` (disediakan tim FE/BE) dan mengasumsikan nilai awal nol.
- Langkah penghubung tanpa awalan `Verifikasi` (S-03): login user uji dan enroll biometric di perangkat Android uji B (hapus data aplikasi, ketik email dan password, [Login], [Enable], lulus verifikasi sidik jari); menghapus app dari recent apps lalu membukanya kembali; mengakhiri sesi platform hasil login enroll lewat API BE (langkah 18, 32, 47, 63, 93, 121, 139, 156, dan 174); mencabut kredensial biometric `Dimas Maulana` (langkah 33); menerapkan kondisi profil BIOPOL (langkah 48 dan 140); mengatur versi Privacy Policy aktif tidak ter-resolve (langkah 141) dan memulihkannya (langkah 148); mencentang checkbox Privacy Policy (langkah 51); memajukan dan memulihkan jam server dan jam browser/perangkat (langkah 158 dan 161); login ulang akun aktor di Browser Admin (langkah 162); berpindah ke Browser Admin dan mencari entri di `Global Settings > Activity Log > Session` dan `Global Settings > User > Detail > User Log` (termasuk pencatatan baseline pada langkah 157); mematikan Toggle Active `Irfan Rahayu` (langkah 94 dan 95).
- Pengecualian `P-5` (a): pemicu biometrik (perangkat Android, pergeseran jam, penolakan server) hanya membentuk kondisi yang diasersi tidak tercatat dan bukan objek uji; tiap TC memakai user dan baseline sendiri.
