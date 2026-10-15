---
id: TC-AUTH-RST-E2E-043-absence-not-logged
title: "Absence: Aksi Reset Password yang Tidak Boleh Dicatat pada Activity Log Session dan User Log"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AUTH-RST-104
  - TC-AUTH-RST-105
  - TC-AUTH-RST-137
coverage:
  web: automated
---

# Absence: Aksi Reset Password yang Tidak Boleh Dicatat pada Activity Log Session dan User Log

## Prerequisites

- Mode: FE+BE (kelas g: asersi absence log). Spec ini adalah tempat asersi "tidak ada entri log" untuk modul Reset Password; spec lain merujuk ke sini.
- Seeding: user subjek dibuat lewat API di hook `before` oleh akun aktor Total Control (Global Settings) `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net` (kredensial `Spectra.env.GS_TC_PASSWORD`), Activated dan Active dengan password aktif `Spectra.env.RST_PASSWORD`, kecuali dinyatakan lain. Token pada user `Eko Santoso` diterbitkan di hook `before` lewat API Request (entri log Success dari seeding terjadi sebelum baseline). User `Joko Susilo` (Deleted) dibuat dengan cara yang sama lalu dihapus di hook `before` oleh akun aktor yang sama (fixture BE). User `Gita Pratama` dibuat dengan cara yang sama (data milik spec ini, email bersuffix unik) dan token aktifnya diterbitkan di hook `before` lewat API Request sebelum baseline. User `Farah Wulandari` dan `Galih Prakoso` dibuat dengan cara yang sama (data milik spec ini, email bersuffix unik, Active tanpa Request sebelumnya). Perubahan email `Linda Sari` ke email baru pending konfirmasi disiapkan di hook `before` lewat fixture BE. User dihapus di hook `after`; pembersihan tidak berasumsi seeding berhasil penuh.
- Environment variable: `GS_TC_PASSWORD`, `RST_PASSWORD`, `RST_PASSWORD_NEW`, `RST_PASSWORD_ALT`.
- Kemampuan teknis: fixture BE untuk counter Request per IP penguji (20 dalam 1 jam); klien API untuk mengirim request langsung ke POST /v2/iam/auth/reset-password/request, POST /v2/iam/auth/reset-password/resend, dan POST /v2/iam/auth/reset-password/confirm; mail-catcher dengan pembacaan jumlah email per alamat (membaca email konfirmasi perubahan email dan tautan reset); akun aktor Total Control yang mengubah email dan menghapus user di Global Settings > User; reCAPTCHA mode uji; jendela guest dan jendela admin terpisah (admin membaca Global Settings > Activity Log > Session dan Global Settings > User > Detail > User Log); pengaturan jam server dan jam browser bersama (countdown [Resend email] berjalan di jam klien, cooldown ditegakkan di server); pembekuan jam server selama bagian aksi endpoint langsung; fixture BE untuk user Active tanpa Request sebelumnya (Kiki Anggraini).
- State global yang diubah: counter Request per IP penguji, jam server, dan jam browser. Suite berjalan serial (`parallel: false`). Jam dipulihkan ke waktu nyata dengan langkah aksi sebelum admin membuka Activity Log Session atau User Log; pembekuan jam server selalu dimulai dari jam nyata. Pemulihan cadangan: counter IP penguji, pembekuan jam server, dan kedua jam dipulihkan di hook `after` (tetap berjalan walau spec gagal di tengah).
- Counter rate limit per IP penguji direset oleh hook `beforeEach` suite (lihat `suite.md`); mekanisme reset disediakan tim FE/BE. Spec ini mengatur counter itu sendiri sesudah reset pada langkah 38, 41, 138, dan 141 (fixture BE).
- Cara membuktikan absence: sebelum tiap kelompok aksi, admin mencatat jumlah entri Activity Log Session (Filter Activity = "Reset Password") dan User Log user terkait sebagai baseline; setelah aksi, memuat ulang dan memverifikasi jumlah entri sama. Spec ini menggeser jam server sehingga entri yang dibuat saat jam digeser bercap waktu di masa depan; karena itu asersi memakai selisih jumlah entri terhadap baseline, dan entri yang diharapkan baru dicari berdasarkan Status, Note, dan email, bukan posisi teratas (S-12).
- Data: Budi Santoso `budisantoso+{runId}-043a@qwertysystem.net` (Active); Joko Susilo `jokosusilo+{runId}-043b@qwertysystem.net` (Deleted); Linda Sari `lindasari+{runId}-043c@qwertysystem.net` dengan email baru `lindasari.baru+{runId}-043c@qwertysystem.net` pending; Citra Dewi `citradewi+{runId}-043d@qwertysystem.net` (Active); Dewi Lestari `dewilestari+{runId}-043e@qwertysystem.net` (Active); Eko Santoso `ekosantoso+{runId}-043f@qwertysystem.net` (Active dengan token aktif); Hana Nugroho `hananugroho+{runId}-043g@qwertysystem.net` (Active tanpa Request sebelumnya); Indra Wijaya `indrawijaya+{runId}-043i@qwertysystem.net` (Active tanpa Request sebelumnya); Kiki Anggraini `kikianggraini+{runId}-043j@qwertysystem.net` (Active tanpa Request sebelumnya); Gita Pratama `gitapratama+{runId}-043h@qwertysystem.net` (Active dengan token aktif, email baru `gitapratama.baru+{runId}-043h@qwertysystem.net`); Farah Wulandari `farahwulandari+{runId}-043k@qwertysystem.net` (Active tanpa Request sebelumnya); Galih Prakoso `galihprakoso+{runId}-043l@qwertysystem.net` (Active tanpa Request sebelumnya, dihapus oleh spec pada langkah 148); email tidak terdaftar `belumterdaftar+{runId}-043@qwertysystem.net`.

## Test Steps

### Persiapan konteks

1. Buka jendela privat guest (tanpa sesi login) dan jendela privat admin; di jendela admin login sebagai akun aktor Total Control (Global Settings) `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net` dengan password `Spectra.env.GS_TC_PASSWORD` (selesaikan reCAPTCHA), lalu buka Global Settings > Activity Log > Session dengan Filter Activity = "Reset Password"

### TC-AUTH-RST-104: Email kosong, format salah, dan reCAPTCHA kosong tidak dicatat

2. Pindah ke jendela admin, muat ulang Activity Log Session (Filter Activity = "Reset Password"), buka User Log user "Budi Santoso", lalu catat jumlah entri kedua surface sebagai baseline B1
3. Pindah ke jendela guest, buka halaman Reset Password (Request), selesaikan reCAPTCHA (centang "I'm not a robot") dengan Email kosong, lalu klik Button [Reset Password]
4. Ketik `budisantoso+{runId}-043a@qwertysystem` (format salah), selesaikan reCAPTCHA, lalu klik Button [Reset Password]
5. Muat ulang halaman Reset Password (Request) agar widget reCAPTCHA kembali kosong
6. Ketik `budisantoso+{runId}-043a@qwertysystem.net` pada field Email tanpa menyelesaikan reCAPTCHA, lalu klik Button [Reset Password]
7. Pindah ke jendela admin, muat ulang Activity Log Session (Filter Activity = "Reset Password") dan User Log user "Budi Santoso"
8. Verifikasi tidak ada entri baru dari ketiga aksi pada Activity Log Session: jumlah entri sama dengan B1
9. Verifikasi tidak ada entri baru dari ketiga aksi pada User Log "Budi Santoso": jumlah entri sama dengan B1

### TC-AUTH-RST-105: Email tidak terdaftar, akun dihapus, email pending, dan Resend akun dihapus tidak dicatat

10. Muat ulang Activity Log Session (Filter Activity = "Reset Password"), lalu catat jumlah entri sebagai baseline B2
11. Pindah ke jendela guest lalu Request dengan `belumterdaftar+{runId}-043@qwertysystem.net` (selesaikan reCAPTCHA)
12. Verifikasi caption "Email is not registered yet" tampil
13. Request dengan `jokosusilo+{runId}-043b@qwertysystem.net` (akun dihapus)
14. Verifikasi caption "Email is not registered yet" tampil
15. Request dengan `lindasari.baru+{runId}-043c@qwertysystem.net` (email pending)
16. Verifikasi caption "Email is not registered yet" tampil
17. Pindah ke jendela admin dan muat ulang Activity Log Session (Filter Activity = "Reset Password")
18. Verifikasi tidak ada entri baru dari ketiga Request: jumlah entri sama dengan B2
19. Pindah ke jendela guest, Request dengan `budisantoso+{runId}-043a@qwertysystem.net` (selesaikan reCAPTCHA) sampai halaman Email Sent! tampil
20. Pindah ke jendela admin, hapus user `budisantoso+{runId}-043a@qwertysystem.net` di Global Settings > User, muat ulang Activity Log Session (Filter Activity = "Reset Password"), lalu catat jumlah entri sebagai baseline B3 (sudah memuat entri Success dari Request; diambil sebelum jam dimajukan)
21. Pindah ke jendela guest lalu majukan jam server dan jam browser 61 detik sampai Button [Resend email] tampil
22. Klik [Resend email]
23. Verifikasi toast sukses muncul: "Success, email has been sent to budisantoso+{runId}-043a@qwertysystem.net."
24. Pulihkan jam server dan jam browser ke waktu nyata
25. Pindah ke jendela admin dan muat ulang Activity Log Session (Filter Activity = "Reset Password")
26. Verifikasi tidak ada entri baru dari Resend untuk akun dihapus: jumlah entri sama dengan B3

### TC-AUTH-RST-137: Resend sukses, cooldown, per IP, token tidak dikenal, dan kesalahan password/confirm tidak dicatat

27. Pindah ke jendela guest, Request dengan `dewilestari+{runId}-043e@qwertysystem.net` (selesaikan reCAPTCHA) sampai halaman Email Sent! tampil
28. Pindah ke jendela admin, muat ulang Activity Log Session (Filter Activity = "Reset Password"), buka User Log user "Eko Santoso", "Dewi Lestari", dan "Citra Dewi", lalu catat jumlah entri Activity Log Session dan ketiga User Log sebagai baseline B4 (Activity Log Session sudah memuat entri Success dari Request `dewilestari`, User Log "Dewi Lestari" juga; User Log "Citra Dewi" belum memuat Request pertama `citradewi`; semua diambil sebelum jam dimajukan)
29. Pindah ke jendela guest lalu majukan jam server dan jam browser 61 detik sampai Button [Resend email] tampil
30. Klik [Resend email]
31. Verifikasi toast sukses muncul: "Success, email has been sent to dewilestari+{runId}-043e@qwertysystem.net."
32. Buka halaman Reset Password (Request) lalu Request dengan `citradewi+{runId}-043d@qwertysystem.net` (selesaikan reCAPTCHA) sampai Email Sent! tampil
33. Buka kembali halaman Reset Password (Request) dari halaman Email Sent! lalu di dalam 60 detik Request lagi dengan email yang sama (selesaikan reCAPTCHA; no-op cooldown)
34. Verifikasi halaman Email Sent! tampil
35. Verifikasi tidak ada toast pada halaman Email Sent!
36. Pulihkan jam server dan jam browser ke waktu nyata
37. Pindah ke jendela admin, muat ulang Activity Log Session (Filter Activity = "Reset Password"), lalu catat jumlah entri sebagai baseline B5 (sudah memuat entri Success dari Request pertama `citradewi`)
38. Atur counter IP penguji menjadi 20 Request dalam 1 jam terakhir (fixture BE)
39. Pindah ke jendela guest lalu Request dengan `dewilestari+{runId}-043e@qwertysystem.net` (selesaikan reCAPTCHA)
40. Verifikasi Alert Danger "Too many requests. Please try again later." tampil
41. Pulihkan counter IP penguji (fixture BE)
42. Kirim request langsung ke POST /v2/iam/auth/reset-password/confirm dengan token acak "tokentidakpernahada", password `Spectra.env.RST_PASSWORD_NEW`, dan confirmPassword `Spectra.env.RST_PASSWORD_NEW`
43. Verifikasi request ditolak
44. Buka tautan reset milik `ekosantoso+{runId}-043f@qwertysystem.net` dari mail-catcher sehingga Setup New Password tampil
45. Klik Button [Reset Password] dengan Password dan Confirm Password kosong
46. Verifikasi caption "Password must not be empty" tampil
47. Verifikasi caption "Confirm password must not be empty" tampil
48. Ketik `Spectra.env.RST_PASSWORD_NEW` pada Password dan `Spectra.env.RST_PASSWORD_ALT` pada Confirm Password lalu klik Button [Reset Password]
49. Verifikasi caption "Passwords do not match" tampil
50. Pindah ke jendela admin dan muat ulang Activity Log Session (Filter Activity = "Reset Password")
51. Verifikasi tidak ada entri baru dari Resend sukses dan Request cooldown: jumlah Activity Log Session bertambah tepat satu dibanding B4 (hanya entri Success dari Request pertama `citradewi`)
52. Verifikasi tidak ada entri baru dari penolakan per IP, Confirm token tidak dikenal, dan kesalahan password/confirm (langkah 39 sampai 49): jumlah entri Activity Log Session sama dengan B5
53. Muat ulang User Log user "Eko Santoso", "Dewi Lestari", dan "Citra Dewi"
54. Verifikasi jumlah entri User Log "Eko Santoso" sama dengan B4 (tidak ada entri baru dari aksi pada user itu)
55. Verifikasi jumlah entri User Log "Dewi Lestari" sama dengan B4 (tidak ada entri baru dari Resend sukses dan Request ditolak per IP)
56. Verifikasi jumlah entri User Log "Citra Dewi" bertambah tepat satu dibanding B4 (hanya entri Success dari Request pertama, bukan dari Request cooldown)

### Aksi endpoint langsung dan validasi UI (rujukan: TC-AUTH-RST-119, 120, 121, 124, 125, 128, 156)

57. Pindah ke jendela admin, muat ulang Activity Log Session (Filter Activity = "Reset Password") lalu catat jumlah entri sebagai baseline B6 (belum memuat Request pertama `hananugroho`; jam nyata)
58. Buka User Log user "Citra Dewi", "Eko Santoso", "Hana Nugroho", dan "Linda Sari" lalu catat jumlah entri masing-masing sebagai baseline B7, B8, B9, dan B10 (belum memuat Request pertama `hananugroho`)
59. Pindah ke jendela guest dan bekukan jam server dari jam nyata
60. Buka halaman Reset Password (Request), ketik `hananugroho+{runId}-043g@qwertysystem.net`, selesaikan reCAPTCHA, lalu klik Button [Reset Password] sampai halaman Email Sent! tampil (Request pertama)
61. Catat jumlah email di mail-catcher untuk `hananugroho+{runId}-043g@qwertysystem.net`, `citradewi+{runId}-043d@qwertysystem.net`, dan `lindasari.baru+{runId}-043c@qwertysystem.net` sebagai baseline M1, M2, dan M3 (sebelum aksi langkah 62 sampai 70)
62. Kirim request langsung ke POST /v2/iam/auth/reset-password/request dengan email "bukan-email" dan token reCAPTCHA valid tanpa melalui halaman Reset Password (rujukan TC-AUTH-RST-119)
63. Kirim request langsung ke POST /v2/iam/auth/reset-password/request dengan email `citradewi+{runId}-043d@qwertysystem.net`, tanpa identifier klien native dan tanpa token reCAPTCHA (rujukan TC-AUTH-RST-120)
64. Kirim request langsung ke POST /v2/iam/auth/reset-password/request dengan email `citradewi+{runId}-043d@qwertysystem.net` dan token reCAPTCHA berisi teks acak "invalid-token" (rujukan TC-AUTH-RST-121)
65. Kirim request langsung ke POST /v2/iam/auth/reset-password/confirm dengan token milik `ekosantoso+{runId}-043f@qwertysystem.net`, password `Spectra.env.RST_PASSWORD_NEW`, dan confirmPassword kosong (rujukan TC-AUTH-RST-124)
66. Kirim request langsung ke POST /v2/iam/auth/reset-password/confirm dengan token yang sama, password `Spectra.env.RST_PASSWORD_NEW`, dan confirmPassword `Spectra.env.RST_PASSWORD_ALT` (rujukan TC-AUTH-RST-124)
67. Kirim request langsung ke POST /v2/iam/auth/reset-password/resend untuk `hananugroho+{runId}-043g@qwertysystem.net` di dalam cooldown 60 detik setelah Request pertama (jam server masih dibekukan) (rujukan TC-AUTH-RST-125)
68. Kirim request langsung ke POST /v2/iam/auth/reset-password/resend untuk `lindasari.baru+{runId}-043c@qwertysystem.net` (email pending) (rujukan TC-AUTH-RST-156)
69. Buka halaman Reset Password (Request), ketik "' OR '1'='1" pada field Email, selesaikan reCAPTCHA, lalu klik Button [Reset Password] (rujukan TC-AUTH-RST-128)
70. Ganti isi field Email dengan "<script>alert(1)</script>" lalu klik Button [Reset Password] (rujukan TC-AUTH-RST-128)
71. Lepaskan pembekuan jam server
72. Periksa mail-catcher
73. Verifikasi tidak ada email baru untuk ketiga alamat uji: jumlah email sama dengan baseline M1, M2, dan M3
74. Pindah ke jendela admin dan muat ulang Activity Log Session (Filter Activity = "Reset Password")
75. Verifikasi jumlah Activity Log Session bertambah tepat satu dibanding baseline B6
76. Verifikasi satu-satunya entri baru pada Activity Log Session adalah entri Success dari Request pertama `hananugroho` (dicari lewat Status Success dan email `hananugroho+{runId}-043g@qwertysystem.net`, bukan lewat posisi teratas), bukan dari aksi langkah 62 sampai 70
77. Muat ulang User Log user "Citra Dewi", "Eko Santoso", "Hana Nugroho", dan "Linda Sari"
78. Verifikasi tidak ada entri baru pada User Log "Citra Dewi", "Eko Santoso", dan "Linda Sari": jumlah entri masing-masing sama dengan B7, B8, dan B10
79. Verifikasi User Log "Hana Nugroho" bertambah tepat satu dibanding B9 (entri Success dari Request pertama)

### Perubahan email dikonfirmasi meng-invalidate token reset aktif (rujukan: TC-AUTH-RST-114 Post Condition b)

80. Pindah ke jendela admin, muat ulang Activity Log Session (Filter Activity = "Reset Password") dan buka User Log user "Gita Pratama", lalu catat jumlah entri dengan Activity `Reset Password` pada kedua surface sebagai baseline B11
81. Pada jendela admin, buka Global Settings > User > Edit untuk user `gitapratama+{runId}-043h@qwertysystem.net` (cari lewat email) lalu ubah email menjadi `gitapratama.baru+{runId}-043h@qwertysystem.net`
82. Pemilik email baru mengonfirmasi perubahan email lewat tautan konfirmasi di mail-catcher
83. Pindah ke jendela guest lalu buka tautan reset dari email lama `gitapratama+{runId}-043h@qwertysystem.net`
84. Verifikasi Halaman 404 tampil dengan Title "Reset Link Expired"
85. Verifikasi Halaman 404 tampil dengan Message "This password reset link has expired. Reset links are valid for 24 hours."
86. Pindah ke jendela admin, muat ulang Activity Log Session (Filter Activity = "Reset Password") dan User Log user "Gita Pratama"
87. Verifikasi tidak ada entri baru dengan Activity `Reset Password` pada Activity Log Session: jumlah entri sama dengan B11
88. Verifikasi tidak ada entri baru dengan Activity `Reset Password` pada User Log "Gita Pratama": jumlah entri dengan Activity `Reset Password` sama dengan B11

### Link Log in with password, Back to Login, dan tautan valid dua kali (rujukan: TC-AUTH-RST-05, 45, 54)

89. Pindah ke jendela admin, muat ulang Activity Log Session (Filter Activity = "Reset Password"), buka User Log user "Citra Dewi", lalu catat jumlah entri kedua surface sebagai baseline B12
90. Pindah ke jendela guest, buka halaman Reset Password (Request) lalu ketik `citradewi+{runId}-043d@qwertysystem.net` pada field Email (rujukan TC-AUTH-RST-05)
91. Klik link "Log in with password"
92. Verifikasi browser menuju halaman Login with Password
93. Pindah ke jendela admin, muat ulang Activity Log Session (Filter Activity = "Reset Password") dan User Log user "Citra Dewi"
94. Verifikasi tidak ada entri baru pada Activity Log Session: jumlah entri sama dengan B12
95. Verifikasi tidak ada entri baru pada User Log "Citra Dewi": jumlah entri sama dengan B12
96. Pindah ke jendela guest, buka halaman Reset Password (Request), ketik `indrawijaya+{runId}-043i@qwertysystem.net`, selesaikan reCAPTCHA (centang "I'm not a robot"), lalu klik Button [Reset Password] sampai halaman Email Sent! tampil (rujukan TC-AUTH-RST-45)
97. Pindah ke jendela admin, muat ulang Activity Log Session (Filter Activity = "Reset Password"), buka User Log user "Indra Wijaya", lalu catat jumlah entri kedua surface sebagai baseline B13 (sudah memuat entri Success dari Request)
98. Pindah ke jendela guest lalu klik Button [Back to Login]
99. Verifikasi browser menuju halaman Login with Password
100. Pindah ke jendela admin, muat ulang Activity Log Session (Filter Activity = "Reset Password") dan User Log user "Indra Wijaya"
101. Verifikasi tidak ada entri baru pada Activity Log Session: jumlah entri sama dengan B13
102. Verifikasi tidak ada entri baru pada User Log "Indra Wijaya": jumlah entri sama dengan B13
103. Pindah ke jendela admin, muat ulang Activity Log Session (Filter Activity = "Reset Password"), buka User Log user "Eko Santoso", lalu catat jumlah entri kedua surface sebagai baseline B14
104. Pindah ke jendela guest lalu buka tautan reset milik `ekosantoso+{runId}-043f@qwertysystem.net` dari mail-catcher (rujukan TC-AUTH-RST-54)
105. Verifikasi halaman Setup New Password tampil dengan Subtitle "Set a new password to log in for ekosantoso+{runId}-043f@qwertysystem.net."
106. Tutup halaman lalu buka tautan yang sama sekali lagi
107. Verifikasi halaman Setup New Password tampil dengan Subtitle "Set a new password to log in for ekosantoso+{runId}-043f@qwertysystem.net."
108. Pindah ke jendela admin, muat ulang Activity Log Session (Filter Activity = "Reset Password") dan User Log user "Eko Santoso"
109. Verifikasi tidak ada entri baru pada Activity Log Session: jumlah entri sama dengan B14
110. Verifikasi tidak ada entri baru pada User Log "Eko Santoso": jumlah entri sama dengan B14

### Request email pending diperlakukan sebagai tidak terdaftar (rujukan: TC-AUTH-RST-155)

111. Pindah ke jendela admin, muat ulang Activity Log Session (Filter Activity = "Reset Password"), buka User Log user "Linda Sari", lalu catat jumlah entri kedua surface sebagai baseline B15
112. Pindah ke jendela guest lalu catat jumlah email di mail-catcher untuk `lindasari.baru+{runId}-043c@qwertysystem.net` sebagai baseline M4
113. Buka halaman Reset Password (Request), ketik `lindasari.baru+{runId}-043c@qwertysystem.net` pada field Email, selesaikan reCAPTCHA (centang "I'm not a robot"), lalu klik Button [Reset Password]
114. Verifikasi caption "Email is not registered yet" tampil di bawah field Email
115. Verifikasi browser tetap di halaman Reset Password
116. Periksa mail-catcher
117. Verifikasi tidak ada email reset di mail-catcher: jumlah email untuk `lindasari.baru+{runId}-043c@qwertysystem.net` sama dengan baseline M4
118. Pindah ke jendela admin, muat ulang Activity Log Session (Filter Activity = "Reset Password") dan User Log user "Linda Sari"
119. Verifikasi tidak ada entri baru pada Activity Log Session: jumlah entri sama dengan B15
120. Verifikasi tidak ada entri baru pada User Log "Linda Sari": jumlah entri sama dengan B15

### Request ulang di dalam cooldown 60 detik (rujukan: TC-AUTH-RST-29)

121. Pindah ke jendela admin, muat ulang Activity Log Session (Filter Activity = "Reset Password"), buka User Log user "Kiki Anggraini", lalu catat jumlah entri kedua surface sebagai baseline B16 (belum memuat Request pertama `kikianggraini`; jam nyata)
122. Pindah ke jendela guest dan bekukan jam server dari jam nyata
123. Buka halaman Reset Password (Request), ketik `kikianggraini+{runId}-043j@qwertysystem.net`, selesaikan reCAPTCHA (centang "I'm not a robot"), lalu klik Button [Reset Password] sampai halaman Email Sent! tampil (Request pertama)
124. Periksa mail-catcher, simpan tautan dari email pertama, dan catat jumlah email untuk `kikianggraini+{runId}-043j@qwertysystem.net` sebagai baseline M5
125. Buka halaman Reset Password (Request), ketik `kikianggraini+{runId}-043j@qwertysystem.net` pada field Email, selesaikan reCAPTCHA, lalu klik Button [Reset Password] (Request kedua di dalam cooldown 60 detik; jam server masih dibekukan)
126. Verifikasi halaman Email Sent! tampil
127. Verifikasi tidak ada toast pada halaman Email Sent!
128. Periksa mail-catcher
129. Verifikasi tidak ada email baru di mail-catcher: jumlah email sama dengan baseline M5 (hanya email dari Request pertama)
130. Buka tautan dari email pertama
131. Verifikasi halaman Setup New Password tampil dengan Subtitle "Set a new password to log in for kikianggraini+{runId}-043j@qwertysystem.net."
132. Lepaskan pembekuan jam server
133. Pindah ke jendela admin, muat ulang Activity Log Session (Filter Activity = "Reset Password") dan User Log user "Kiki Anggraini"
134. Verifikasi jumlah Activity Log Session bertambah tepat satu dibanding baseline B16 (entri Success dari Request pertama, bukan dari Request kedua)
135. Verifikasi jumlah User Log "Kiki Anggraini" bertambah tepat satu dibanding baseline B16 (entri Success dari Request pertama, bukan dari Request kedua)

### Request ke-21 dalam 1 jam dari IP yang sama ditolak 429 (rujukan: TC-AUTH-RST-35)

136. Pindah ke jendela admin, muat ulang Activity Log Session (Filter Activity = "Reset Password"), buka User Log user "Farah Wulandari", lalu catat jumlah entri kedua surface sebagai baseline B17 (belum ada Request untuk `farahwulandari`)
137. Pindah ke jendela guest lalu catat jumlah email di mail-catcher untuk `farahwulandari+{runId}-043k@qwertysystem.net` sebagai baseline M6
138. Atur counter IP penguji menjadi 20 Request dalam 1 jam terakhir (fixture BE)
139. Buka halaman Reset Password (Request), ketik `farahwulandari+{runId}-043k@qwertysystem.net` pada field Email, selesaikan reCAPTCHA (centang "I'm not a robot"), lalu klik Button [Reset Password]
140. Verifikasi Alert Danger "Too many requests. Please try again later." tampil
141. Pulihkan counter IP penguji (fixture BE)
142. Periksa mail-catcher
143. Verifikasi tidak ada email baru: jumlah email untuk `farahwulandari+{runId}-043k@qwertysystem.net` sama dengan baseline M6
144. Pindah ke jendela admin, muat ulang Activity Log Session (Filter Activity = "Reset Password") dan User Log user "Farah Wulandari"
145. Verifikasi tidak ada entri baru pada Activity Log Session: jumlah entri sama dengan B17
146. Verifikasi tidak ada entri baru pada User Log "Farah Wulandari": jumlah entri sama dengan B17

### Resend untuk akun yang dihapus setelah Request menampilkan toast sukses tanpa email dan tanpa entri log (rujukan: TC-AUTH-RST-48)

147. Pindah ke jendela guest, Request dengan `galihprakoso+{runId}-043l@qwertysystem.net` (selesaikan reCAPTCHA) sampai halaman Email Sent! tampil
148. Pindah ke jendela admin, hapus user `galihprakoso+{runId}-043l@qwertysystem.net` di Global Settings > User, muat ulang Activity Log Session (Filter Activity = "Reset Password"), lalu catat jumlah entri sebagai baseline B18 (sudah memuat entri Success dari Request; diambil sebelum jam dimajukan)
149. Pindah ke jendela guest lalu catat jumlah email di mail-catcher untuk `galihprakoso+{runId}-043l@qwertysystem.net` sebagai baseline M7
150. Majukan jam server dan jam browser 61 detik sampai Button [Resend email] tampil
151. Klik [Resend email]
152. Verifikasi toast sukses muncul: "Success, email has been sent to galihprakoso+{runId}-043l@qwertysystem.net."
153. Pulihkan jam server dan jam browser ke waktu nyata
154. Periksa mail-catcher
155. Verifikasi tidak ada email baru: jumlah email untuk `galihprakoso+{runId}-043l@qwertysystem.net` sama dengan baseline M7
156. Pindah ke jendela admin dan muat ulang Activity Log Session (Filter Activity = "Reset Password")
157. Verifikasi tidak ada entri baru dari Resend untuk akun dihapus: jumlah entri Activity Log Session sama dengan B18

## Notes

- Sumber: `auth/reset-password/TestCases/tc-reset-password.md`. Asersi absence dari spec lain diuji di sini lewat aksi nyata yang sama jenisnya dengan baseline log sendiri (prinsip 10, S-05): TC-AUTH-RST-15, 16, 19 (kelompok TC-AUTH-RST-104); TC-AUTH-RST-23, 24 (kelompok TC-AUTH-RST-105); TC-AUTH-RST-36, 42, 73, 74, 126 (kelompok TC-AUTH-RST-137).
- Rujukan tanpa `sourceTc` (id TC tetap milik spec asalnya; aksi nyata dengan baseline sendiri, rujukan dicatat di Notes kedua spec, S-05): bagian "Aksi endpoint langsung dan validasi UI" memicu aksi nyata TC-AUTH-RST-119, 120, 121, 128 (milik `TC-AUTH-RST-E2E-038-defense-request-endpoint`) serta TC-AUTH-RST-124, 125, 156 (milik `TC-AUTH-RST-E2E-039-defense-confirm-resend-endpoint`). Bagian "Request email pending diperlakukan sebagai tidak terdaftar" memicu aksi nyata TC-AUTH-RST-155 dengan baseline B15 dan M4 (milik `TC-AUTH-RST-E2E-008-unregistered-deleted-pending-email`); bagian "Request ulang di dalam cooldown 60 detik" memicu aksi nyata TC-AUTH-RST-29 dengan baseline B16 dan M5 (milik `TC-AUTH-RST-E2E-011-request-cooldown-60s`). Bagian "Link Log in with password, Back to Login, dan tautan valid dua kali" memicu aksi nyata TC-AUTH-RST-05 (milik `TC-AUTH-RST-E2E-002-navigation-login-email-carry`), TC-AUTH-RST-45 (milik `TC-AUTH-RST-E2E-016-screening-email-sent-countdown`), dan TC-AUTH-RST-54 (milik `TC-AUTH-RST-E2E-019-valid-link-idempotent-superseded`). Bagian "Request ke-21 dalam 1 jam dari IP yang sama ditolak 429" memicu aksi nyata TC-AUTH-RST-35 dengan baseline B17 dan M6 pada kedua surface (milik `TC-AUTH-RST-E2E-014-ip-rate-limit-429`); bagian "Resend untuk akun yang dihapus setelah Request" memicu aksi nyata TC-AUTH-RST-48 dengan baseline B18 dan M7 (milik `TC-AUTH-RST-E2E-018-resend-rejections`). Bagian-bagian itu membuktikan Expected "tidak ada entri log" TC tersebut (TC-AUTH-RST-155, 29, 35, dan 48 tidak dimasukkan ke `sourceTc` spec ini); user TC-AUTH-RST-35 dan 48 adalah data milik spec ini yang bersuffix unik; hasil aksi itu sendiri diasersi di spec asal. TC-AUTH-RST-48 memeriksa Activity Log Session saja karena User Log user yang sudah dihapus tidak dapat dibuka.
- Post Condition "tidak ada entri log" TC-AUTH-RST-17, 20, 22, 58, 59, 71, 72 tidak punya langkah observasi di TC sehingga tidak diasersi di spec ini; catatannya ada di "Temuan untuk QA" spec asalnya (S-01, S-05, S-15).
- Temuan untuk QA: TC-AUTH-RST-137 menggabungkan lima aksi tidak dicatat dalam satu precondition; untuk "Resend sukses" dan "cooldown" diperlukan Request awal yang dicatat Success, sehingga baseline diambil sesudahnya (S-15).
- Temuan untuk QA: Post Condition TC-AUTH-RST-119 sampai 121, 124, 125, 156 dan Post Condition "Tidak ada token baru" TC-AUTH-RST-35 dan 48 (tidak ada token baru, token dan counter tidak berubah) tidak punya langkah observasi di TC sehingga tidak diasersi (S-01, S-15).
- Langkah penghubung (S-03): pindah antar jendela admin dan guest, langkah 5 (muat ulang halaman Request agar widget reCAPTCHA kosong, S-14), langkah 21 dan 29 (jam dimajukan menggantikan menunggu 61 detik, konvensi bagian 6), langkah 24 dan 36 (jam dipulihkan sebelum admin membuka log, S-09), langkah 59 sampai 71 dan 122 sampai 132 (jam server dibekukan dari jam nyata agar Resend atau Request langsung tetap dalam cooldown; baseline log B6 sampai B10 dan B16 diambil sebelum pembekuan, sehingga admin tidak membaca log saat jam beku), langkah 150 dan 153 (jam dimajukan lalu dipulihkan sebelum admin membuka log), serta langkah 38, 41, 138, dan 141 (counter IP). Counter IP dan pembekuan jam dipulihkan di hook `after` sebagai cadangan.
- Asersi tambahan di luar Expected TC (S-03, S-12): baseline B1 sampai B18 dan M1 sampai M7 ditambahkan agar "tidak ada entri baru" dan "tidak ada email baru" terbukti; langkah 12, 14, 16, 23, 31, 34, 35, 40, 46, 47, 49, 92, 99, 105, 107, 114, 115, 126, 127, 131, 140, dan 152 adalah observasi bahwa aksi benar-benar terjadi sebelum absence diasersi.
- Ukuran: 157 langkah, melewati smell 35. Satu kelas (g, asersi absence) dengan baseline log tersendiri per kelompok; kelompok TC-AUTH-RST-104, 105, 137, aksi endpoint langsung, dan bagian TC-AUTH-RST-05, 45, 54, 155, 29, 35, 48 tidak saling bergantung data. Dapat dipecah per kelompok bila perlu.
- Absence TC-AUTH-RST-114 Post Condition b ("Tidak ada entri log di modul ini untuk invalidasi tersebut") diasersi pada langkah 80 sampai 88 lewat aksi nyata perubahan email yang dikonfirmasi; id TC-AUTH-RST-114 tetap milik spec `TC-AUTH-RST-E2E-023-email-change-invalidates-token` (TC-AUTH-RST-137 Precondition b memuat aksi ini). Langkah 84 dan 85 adalah observasi bahwa token benar-benar ter-invalidate sebelum absence diasersi (S-12); baseline B11 diambil sebelum perubahan email.
- Langkah 87 dan 88 hanya membandingkan entri ber-Activity `Reset Password`, sehingga entri perubahan email dari modul Global Settings (bila ada di User Log "Gita Pratama") tidak memengaruhi asersi; TC-AUTH-RST-114 Post Condition b hanya menyebut modul Reset Password.
