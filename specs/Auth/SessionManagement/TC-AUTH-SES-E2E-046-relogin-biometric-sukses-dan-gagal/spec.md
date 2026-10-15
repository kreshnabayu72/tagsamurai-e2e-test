---
id: TC-AUTH-SES-E2E-046-relogin-biometric-sukses-dan-gagal
title: "Re-login Biometric Android: Screen Sign In, Kegagalan, Fallback Password, dan Sukses"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AUTH-SES-152
  - TC-AUTH-SES-153
  - TC-AUTH-SES-154
  - TC-AUTH-SES-155
  - TC-AUTH-SES-156
  - TC-AUTH-SES-157
  - TC-AUTH-SES-158
  - TC-AUTH-SES-159
  - TC-AUTH-SES-160
coverage:
  web: automated
  mobile: automated
---

# Re-login Biometric Android: Screen Sign In, Kegagalan, Fallback Password, dan Sukses

## Prerequisites

- Mode: FE+BE.
- Platform: aplikasi mobile TAG Samurai (Android) terpasang di perangkat Android uji B (Tabel Data Uji Pre-setup #10: hardware biometric, sidik jari terdaftar di OS). Semua TC memakai perangkat yang sama.
- Seeding (hook `before`, lewat API oleh akun aktor Total Control (Global Settings) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.GS_TC_PASSWORD`): sembilan user profil BIO milik Client `Alpha Logistik` (Tabel Data Uji Pre-setup #9 dan #5: batas idle 15 menit; subscription Fixed Asset dan Supply Asset Active, kuota 5; user Activated, Active ON; MFA dan Agreement tidak terpicu; belum pernah enroll biometric), password `Spectra.env.SES_PASSWORD`, email bersuffix per run:
  - TC-AUTH-SES-153: `Nur Saputra` (`nursaputra+{runId}-046@qwertysystem.net`)
  - TC-AUTH-SES-154: `Agus Firmansyah` (`agusfirmansyah+{runId}-046@qwertysystem.net`)
  - TC-AUTH-SES-156: `Hendra Rahayu` (`hendrarahayu+{runId}-046@qwertysystem.net`)
  - TC-AUTH-SES-157: `Maya Anggraini` (`mayaanggraini+{runId}-046@qwertysystem.net`)
  - TC-AUTH-SES-158: `Fajar Wibowo` (`fajarwibowo+{runId}-046@qwertysystem.net`)
  - TC-AUTH-SES-159: `Lestari Nugroho` (`lestarinugroho+{runId}-046@qwertysystem.net`)
  - TC-AUTH-SES-160: `Dimas Maulana` (`dimasmaulana+{runId}-046@qwertysystem.net`)
  - TC-AUTH-SES-155: `Rina Damayanti` (`rinadamayanti+{runId}-046@qwertysystem.net`)
  - TC-AUTH-SES-152: `Rizky Puspita` (`rizkypuspita+{runId}-046@qwertysystem.net`)
- Kondisi awal tiap TC "sudah enroll biometric di perangkat Android uji B; tidak ada sesi platform aktif" dibuat di dalam TC dengan menyalin langkah enroll TC-AUTH-SES-145 (hapus data aplikasi, login, [Enable], lulus sidik jari, hapus app dari recent apps), lalu mengakhiri sesi platform hasil login enroll lewat API yang disediakan tim BE tanpa menghapus token biometric lokal (cara menyiapkan mengikuti Tabel Data Uji Pre-setup #29), karena token biometric lokal dan status "sudah ditawari" disimpan di perangkat dan hanya dapat dibuat oleh aplikasi.
- Kondisi di-seed BE: kredensial biometric `Dimas Maulana` di-revoke di server (TC-AUTH-SES-160). Sesi mobile `Nur Saputra` berakhir karena idle (TC-AUTH-SES-153) lewat pergeseran jam server dan jam browser/perangkat bersama pada langkah.
- Browser Admin: konteks browser terpisah dengan akun aktor Total Control (Global Settings) di atas, login di hook `before`, untuk membaca `Global Settings > Activity Log > Session` (TC-AUTH-SES-152).
- Suite berjalan serial (`parallel: false`), juga karena perangkat Android uji B dipakai bersama; state global yang diubah: jam server dan jam browser/perangkat (diatur bersama, TC-AUTH-SES-153), dipulihkan setelah TC-AUTH-SES-153 dan dicadangkan di hook `after`.
- Hook `after`: kembalikan jam server uji ke waktu nyata, hapus data aplikasi pada perangkat Android uji B, tutup Browser Admin, akhiri semua sesi seed, lalu hapus kesembilan user. Pembersihan tetap jalan walau spec gagal di tengah dan tidak berasumsi seeding berhasil penuh.
- Akun yang dipakai: user uji masing-masing TC pada aplikasi mobile; akun aktor Total Control hanya di Browser Admin (TC-AUTH-SES-152).
- Environment variable: `GS_TC_PASSWORD`, `SES_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Kemampuan teknis (kelas harness d: hardware biometrik dan time-travel): driver otomasi Android (aplikasi native); simulasi sensor sidik jari pada OS biometric prompt (sidik jari terdaftar lulus, sidik jari tidak terdaftar gagal) dan pembatalan OS biometric prompt; menghapus data aplikasi dan menghapus app dari recent apps lalu membukanya kembali; jam server dan jam browser/perangkat dapat diatur bersama dan dipulihkan ke waktu nyata; proxy jaringan (Tabel Data Uji Pre-setup #18) untuk mengamati respons 401 dari request relogin (TC-AUTH-SES-160); pembacaan status sesi dan status kredensial biometric user oleh akun aktor, serta pembacaan penyimpanan token biometric lokal (langkah 40 dan 93) dan API untuk mengakhiri sesi platform mobile user uji tanpa menghapus token biometric lokal (langkah sesudah tiap enroll), disediakan tim FE/BE; reCAPTCHA mode uji di environment untuk login web (halaman Login with Password).

## Test Steps

### TC-AUTH-SES-153: App dibuka setelah sesi mobile idle expired menampilkan Screen biometric sign-in

1. Hapus data aplikasi di perangkat Android uji B lalu buka aplikasi mobile → halaman Login tampil
2. Ketik `nursaputra+{runId}-046@qwertysystem.net` pada field Email
3. Ketik `Spectra.env.SES_PASSWORD` pada field Password
4. Klik [Login] → Prompt Enable Biometric muncul
5. Ketuk [Enable] → OS biometric prompt muncul
6. Lulus verifikasi sidik jari yang terdaftar pada OS biometric prompt → app masuk Portal — Product Hub
7. Majukan jam server dan jam browser/perangkat bersama 16 menit tanpa aktivitas di app sehingga sesi mobile berakhir karena idle
8. Hapus app dari recent apps
9. Buka aplikasi mobile di perangkat Android uji B
10. Verifikasi Screen "Sign in with Face ID / Touch ID" tampil menggantikan form Login
11. Verifikasi OS biometric prompt muncul otomatis
12. Pulihkan jam server dan jam browser/perangkat ke waktu nyata

### TC-AUTH-SES-154: Biometric gagal pertama menampilkan tombol Try Again

13. Hapus data aplikasi di perangkat Android uji B lalu buka aplikasi mobile → halaman Login tampil
14. Ketik `agusfirmansyah+{runId}-046@qwertysystem.net` pada field Email
15. Ketik `Spectra.env.SES_PASSWORD` pada field Password
16. Klik [Login] → Prompt Enable Biometric muncul
17. Ketuk [Enable] → OS biometric prompt muncul
18. Lulus verifikasi sidik jari yang terdaftar pada OS biometric prompt
19. Hapus app dari recent apps
20. Akhiri sesi platform mobile `agusfirmansyah+{runId}-046@qwertysystem.net` hasil login enroll lewat API yang disediakan tim BE, tanpa menghapus token biometric lokal
21. Buka aplikasi mobile di perangkat Android uji B → Screen biometric sign-in tampil dan OS biometric prompt muncul otomatis
22. Tempelkan sidik jari yang tidak terdaftar pada OS biometric prompt
23. Verifikasi Tombol [Try Again] (variant solid, severity primary) tampil sebagai aksi utama
24. Verifikasi Tidak ada sesi yang dibuat untuk `Agus Firmansyah`
25. Verifikasi Tautan "Sign in with password instead" belum tampil setelah kegagalan pertama

### TC-AUTH-SES-156: Biometric gagal kedua menampilkan tautan Sign in with password instead

26. Hapus data aplikasi di perangkat Android uji B lalu buka aplikasi mobile → halaman Login tampil
27. Ketik `hendrarahayu+{runId}-046@qwertysystem.net` pada field Email
28. Ketik `Spectra.env.SES_PASSWORD` pada field Password
29. Klik [Login] → Prompt Enable Biometric muncul
30. Ketuk [Enable] → OS biometric prompt muncul
31. Lulus verifikasi sidik jari yang terdaftar pada OS biometric prompt
32. Hapus app dari recent apps
33. Akhiri sesi platform mobile `hendrarahayu+{runId}-046@qwertysystem.net` hasil login enroll lewat API yang disediakan tim BE, tanpa menghapus token biometric lokal
34. Buka aplikasi mobile di perangkat Android uji B → Screen biometric sign-in tampil dan OS biometric prompt muncul otomatis
35. Tempelkan sidik jari yang tidak terdaftar pada OS biometric prompt (kegagalan pertama)
36. Ketuk [Try Again]
37. Tempelkan sidik jari yang tidak terdaftar pada OS biometric prompt (kegagalan kedua)
38. Verifikasi Tautan teks sekunder "Sign in with password instead" tampil di bawah posisi [Try Again]
39. Verifikasi [Try Again] tetap tampil bersama tautan setelah kegagalan kedua
40. Verifikasi Refresh token biometric tetap tersimpan

### TC-AUTH-SES-157: Cancel pada OS biometric prompt memunculkan tautan Sign in with password instead

41. Hapus data aplikasi di perangkat Android uji B lalu buka aplikasi mobile → halaman Login tampil
42. Ketik `mayaanggraini+{runId}-046@qwertysystem.net` pada field Email
43. Ketik `Spectra.env.SES_PASSWORD` pada field Password
44. Klik [Login] → Prompt Enable Biometric muncul
45. Ketuk [Enable] → OS biometric prompt muncul
46. Lulus verifikasi sidik jari yang terdaftar pada OS biometric prompt
47. Hapus app dari recent apps
48. Akhiri sesi platform mobile `mayaanggraini+{runId}-046@qwertysystem.net` hasil login enroll lewat API yang disediakan tim BE, tanpa menghapus token biometric lokal
49. Buka aplikasi mobile di perangkat Android uji B → Screen biometric sign-in tampil dan OS biometric prompt muncul otomatis
50. Batalkan (cancel) OS biometric prompt pada percobaan pertama
51. Verifikasi Tautan teks sekunder "Sign in with password instead" tampil
52. Verifikasi [Try Again] tetap tampil bersama tautan setelah cancel

### TC-AUTH-SES-158: Tautan Sign in with password instead membuka Login penuh dan token tetap tersimpan

53. Hapus data aplikasi di perangkat Android uji B lalu buka aplikasi mobile → halaman Login tampil
54. Ketik `fajarwibowo+{runId}-046@qwertysystem.net` pada field Email
55. Ketik `Spectra.env.SES_PASSWORD` pada field Password
56. Klik [Login] → Prompt Enable Biometric muncul
57. Ketuk [Enable] → OS biometric prompt muncul
58. Lulus verifikasi sidik jari yang terdaftar pada OS biometric prompt
59. Hapus app dari recent apps
60. Akhiri sesi platform mobile `fajarwibowo+{runId}-046@qwertysystem.net` hasil login enroll lewat API yang disediakan tim BE, tanpa menghapus token biometric lokal
61. Buka aplikasi mobile di perangkat Android uji B → Screen biometric sign-in tampil dan OS biometric prompt muncul otomatis
62. Batalkan (cancel) OS biometric prompt pada percobaan pertama → tautan "Sign in with password instead" tampil
63. Ketuk tautan "Sign in with password instead"
64. Verifikasi Halaman Login penuh tampil setelah tautan diketuk
65. Hapus app dari recent apps
66. Buka kembali app
67. Verifikasi Screen "Sign in with Face ID / Touch ID" tampil lagi karena refresh token tetap tersimpan

### TC-AUTH-SES-159: OS biometric prompt tidak menerima passcode perangkat sebagai pengganti

68. Hapus data aplikasi di perangkat Android uji B lalu buka aplikasi mobile → halaman Login tampil
69. Ketik `lestarinugroho+{runId}-046@qwertysystem.net` pada field Email
70. Ketik `Spectra.env.SES_PASSWORD` pada field Password
71. Klik [Login] → Prompt Enable Biometric muncul
72. Ketuk [Enable] → OS biometric prompt muncul
73. Lulus verifikasi sidik jari yang terdaftar pada OS biometric prompt
74. Hapus app dari recent apps
75. Akhiri sesi platform mobile `lestarinugroho+{runId}-046@qwertysystem.net` hasil login enroll lewat API yang disediakan tim BE, tanpa menghapus token biometric lokal
76. Buka aplikasi mobile di perangkat Android uji B → Screen biometric sign-in tampil dan OS biometric prompt muncul otomatis
77. Pada OS biometric prompt coba pakai opsi PIN atau passcode perangkat
78. Verifikasi Hanya biometric yang diterima; passcode perangkat tidak mengotentikasi sesi
79. Verifikasi Tidak ada sesi yang dibuat untuk `Lestari Nugroho`

### TC-AUTH-SES-160: Token biometric tidak valid menghapus token lokal dan fallback ke Login penuh tanpa log

80. Hapus data aplikasi di perangkat Android uji B lalu buka aplikasi mobile → halaman Login tampil
81. Ketik `dimasmaulana+{runId}-046@qwertysystem.net` pada field Email
82. Ketik `Spectra.env.SES_PASSWORD` pada field Password
83. Klik [Login] → Prompt Enable Biometric muncul
84. Ketuk [Enable] → OS biometric prompt muncul
85. Lulus verifikasi sidik jari yang terdaftar pada OS biometric prompt
86. Hapus app dari recent apps
87. Akhiri sesi platform mobile `dimasmaulana+{runId}-046@qwertysystem.net` hasil login enroll lewat API yang disediakan tim BE, tanpa menghapus token biometric lokal
88. Cabut (revoke) kredensial biometric `Dimas Maulana` di server (kondisi di-seed BE)
89. Buka aplikasi mobile di perangkat Android uji B → Screen biometric sign-in tampil dan OS biometric prompt muncul otomatis
90. Lulus verifikasi sidik jari yang terdaftar pada OS biometric prompt
91. Verifikasi Server menolak request relogin (401 token tidak valid)
92. Verifikasi Token lokal dihapus
93. Verifikasi Halaman Login penuh tampil

### TC-AUTH-SES-155: Try Again berhasil setelah gagal pertama membuat sesi baru

94. Hapus data aplikasi di perangkat Android uji B lalu buka aplikasi mobile → halaman Login tampil
95. Ketik `rinadamayanti+{runId}-046@qwertysystem.net` pada field Email
96. Ketik `Spectra.env.SES_PASSWORD` pada field Password
97. Klik [Login] → Prompt Enable Biometric muncul
98. Ketuk [Enable] → OS biometric prompt muncul
99. Lulus verifikasi sidik jari yang terdaftar pada OS biometric prompt
100. Hapus app dari recent apps
101. Akhiri sesi platform mobile `rinadamayanti+{runId}-046@qwertysystem.net` hasil login enroll lewat API yang disediakan tim BE, tanpa menghapus token biometric lokal
102. Buka aplikasi mobile di perangkat Android uji B → Screen biometric sign-in tampil dan OS biometric prompt muncul otomatis
103. Tempelkan sidik jari yang tidak terdaftar pada OS biometric prompt (satu kegagalan)
104. Ketuk [Try Again]
105. Lulus verifikasi sidik jari yang terdaftar pada OS biometric prompt
106. Verifikasi App masuk Portal — Product Hub
107. Verifikasi Sesi mobile baru Active untuk `Rina Damayanti`

### TC-AUTH-SES-152: Re-login biometric sukses membuat sesi baru, masuk Portal, dan mencatat Login with biometric

108. Di Browser Admin buka `Auth > Login with Password`, ketik email `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` dan password `Spectra.env.GS_TC_PASSWORD`, lalu klik [Log in] (sesi Browser Admin sebelumnya melewati batas idle); buka `Global Settings > Activity Log > Session` dan catat baseline jumlah entri `Login with biometric` `Rizky Puspita`
109. Hapus data aplikasi di perangkat Android uji B lalu buka aplikasi mobile → halaman Login tampil
110. Ketik `rizkypuspita+{runId}-046@qwertysystem.net` pada field Email
111. Ketik `Spectra.env.SES_PASSWORD` pada field Password
112. Klik [Login] → Prompt Enable Biometric muncul
113. Ketuk [Enable] → OS biometric prompt muncul
114. Lulus verifikasi sidik jari yang terdaftar pada OS biometric prompt
115. Hapus app dari recent apps
116. Akhiri sesi platform mobile `rizkypuspita+{runId}-046@qwertysystem.net` hasil login enroll lewat API yang disediakan tim BE, tanpa menghapus token biometric lokal
117. Buka aplikasi mobile di perangkat Android uji B → Screen biometric sign-in tampil dan OS biometric prompt muncul otomatis
118. Lulus verifikasi sidik jari yang terdaftar pada OS biometric prompt
119. Verifikasi App masuk Portal — Product Hub
120. Verifikasi Sesi platform mobile baru berstatus Active untuk `Rizky Puspita`
121. Pindah ke Browser Admin (akun aktor Total Control sudah login di hook)
122. Buka `Global Settings > Activity Log > Session`
123. Verifikasi Entri `Login with biometric` untuk `Rizky Puspita` (dicari berdasarkan Note dan email) bertambah 1 dari baseline

## Notes

- Sumber: `auth/session-management/TestCases/tc-session-management.md`. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Penyimpangan urutan (S-05, S-10): urutan di spec ini TC-AUTH-SES-153, 154, 156, 157, 158, 159, 160, 155, 152 (urutan TC sumber 152, 153, 154, 155, 156, 157, 158, 159, 160). Screen biometric sign-in (153) didahulukan sebagai screening, penolakan dan kegagalan (154, 156, 157, 158, 159, 160) sebelum login sukses (155, 152); TC-AUTH-SES-160 mencabut kredensial miliknya sendiri sehingga tidak memengaruhi TC lain.
- Dependensi (S-04): TC-AUTH-SES-153, 154, 156, 157, 158, 159, 160, 155, 152 bergantung pada TC-AUTH-SES-145 (enroll) dan sebagian pada TC-AUTH-SES-15 (membuka app sampai Screen biometric sign-in), TC-AUTH-SES-154 (TC-AUTH-SES-156 dan 155) serta TC-AUTH-SES-157 (TC-AUTH-SES-158). Langkah enroll disalin di awal tiap TC (hapus data aplikasi sampai hapus app dari recent apps); langkah TC-AUTH-SES-154 disalin pada langkah 34–35 dan 102–103, dan langkah TC-AUTH-SES-157 pada langkah 61–62. Sesudah "hapus app dari recent apps" pada enroll tiap TC (kecuali TC-AUTH-SES-153 yang sesinya berakhir karena idle), sesi platform hasil login enroll diakhiri lewat API yang disediakan tim BE tanpa menghapus token biometric lokal (Pre-setup #29), bukan lewat Log Out UI, supaya kondisi "tidak ada sesi platform aktif" terpenuhi.
- Langkah penghubung tanpa awalan `Verifikasi` (S-03): "Hapus data aplikasi" mengosongkan status "sudah ditawari" dan token biometric lokal di awal tiap TC (S-09); perpindahan ke Browser Admin; majukan jam server dan jam browser/perangkat bersama 16 menit pada TC-AUTH-SES-153 untuk membuat kondisi "sesi sebelumnya berakhir karena idle" (batas idle Client `Alpha Logistik` 15 menit), lalu pulihkan jam di langkah 12 sebelum TC berikutnya dan sebelum Browser Admin membuka Activity Log; langkah login ulang Browser Admin (awal TC-AUTH-SES-152) karena sesi Browser Admin melewati batas idle akibat pergeseran jam.
- Pembagian TC lintas spec: asersi "tidak ada pencatatan" (TC-AUTH-SES-154 Expected b, TC-AUTH-SES-160 Expected c yang merujuk TC-AUTH-SES-211) tidak ditulis di spec ini; ia berada di spec absence `TC-AUTH-SES-E2E-070-absence-biometric` (kelas g, S-05). Pencatatan `Login with biometric` (TC-AUTH-SES-152 Expected c) diasersi di sini; detail kolom log ada di spec pencatatan (TC-AUTH-SES-209).
- Jumlah langkah (123) melewati sekitar 35 karena sembilan TC, masing-masing dengan user dan sesi sendiri, menyalin prefix enroll (hapus data aplikasi sampai mengakhiri sesi hasil enroll) per TC (S-04); tiap TC berdiri sendiri sehingga bagian sesudahnya tetap bermakna walau bagian di atasnya gagal. Blok enroll tidak dihitung ke batas ±35.
- Temuan untuk QA: (1) TC sumber menulis login/enroll tanpa menyebut field dan tombol; spec menguraikannya menjadi ketik email, ketik password, klik [Login] (label tombol login mobile tidak disebut TC). (2) TC-AUTH-SES-153 menyebut "sesi sebelumnya berakhir karena idle" tanpa cara; spec memajukan jam server dan jam browser/perangkat bersama 16 menit. (3) TC-AUTH-SES-159 "coba pakai opsi PIN atau passcode perangkat bila ada" kondisional; spec menulisnya sebagai satu langkah tanpa percabangan (PRD menyatakan prompt biometric-only). (4) TC-AUTH-SES-156 Expected c ("refresh token tetap tersimpan") dan TC-AUTH-SES-160 Expected a ("401 token tidak valid") tidak menyebut cara mengamatinya; spec mengasersinya sebagaimana tertulis dan mengandalkan proxy jaringan untuk 401. (5) TC-AUTH-SES-152/155 ("sesi mobile baru Active") tidak menyebut cara membaca status sesi; spec mengasersinya langsung. (7) Pre-setup #29 tidak menyebut API untuk mengakhiri sesi platform hasil login enroll; spec menuliskannya sebagai kemampuan yang disediakan tim BE tanpa endpoint karangan. (6) TC-AUTH-SES-160 menyebut kredensial "sudah di-revoke di server" tanpa cara; spec memakai langkah revoke yang di-seed BE.
- Baseline log (S-12): jumlah entri `Login with biometric` `Rizky Puspita` dicatat di langkah 108 sebelum aksi; asersi mencari entri berdasarkan Note dan email dan mengasersi selisih jumlah. Asersi hanya kemunculan entri (Expected c TC-AUTH-SES-152 menyatakan "Dicatat `Login with biometric`"); kolom Activity, Status, dan Note diasersi di spec pencatatan (TC-AUTH-SES-209).
