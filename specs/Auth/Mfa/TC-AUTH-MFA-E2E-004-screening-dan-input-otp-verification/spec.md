---
id: TC-AUTH-MFA-E2E-004-screening-dan-input-otp-verification
title: "Screening dan Input Kotak Digit OTP Verification"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-MFA-04
  - TC-AUTH-MFA-14
  - TC-AUTH-MFA-67
  - TC-AUTH-MFA-69
  - TC-AUTH-MFA-87
  - TC-AUTH-MFA-88
  - TC-AUTH-MFA-89
coverage:
  web: automated
---

# Screening dan Input Kotak Digit OTP Verification

## Prerequisites

- Mode: FE+BE.
- Seeding (hook `before`, lewat API oleh akun aktor Total Control (Global Settings) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.GS_TC_PASSWORD`): tujuh user, password `Spectra.env.MFA_PASSWORD`, email bersuffix per run:
  - Profil FIRST (Tabel Data Uji Pre-setup #3: Activated, Active ON, belum pernah login di platform mana pun, Authenticator belum terdaftar; tiap login melewati layar Confirm to Continue sebelum Choose Verification Method):
    - TC-AUTH-MFA-04: `Dewi Lestari` (`dewilestari+{runId}-004@qwertysystem.net`)
    - TC-AUTH-MFA-14: `Lina Marlina` (`linamarlina+{runId}-004@qwertysystem.net`)
  - Profil NEWDEV (Tabel Data Uji Pre-setup #4: Activated, Active ON, sudah pernah login sukses di web, Authenticator belum terdaftar; TC pertama berjalan di browser awal; browser awal dan tiap jendela privat tanpa ID device tersimpan, dikenali sebagai browser uji B; login dari browser uji B memicu MFA karena ID device belum dikenali; tanpa layar Confirm to Continue):
    - TC-AUTH-MFA-67: `Yulia Rahayu` (`yuliarahayu+{runId}-004@qwertysystem.net`)
    - TC-AUTH-MFA-69: `Nanda Safira` (`nandasafira+{runId}-004@qwertysystem.net`)
    - TC-AUTH-MFA-87: `Hendra Wijaya` (`hendrawijaya+{runId}-004@qwertysystem.net`)
    - TC-AUTH-MFA-88: `Lina Wijaya` (`linawijaya+{runId}-004@qwertysystem.net`)
    - TC-AUTH-MFA-89: `Teguh Wijaya` (`teguhwijaya+{runId}-004@qwertysystem.net`)
- Hook `after`: hapus ketujuh user. Pembersihan tidak berasumsi seeding berhasil penuh.
- Akun yang dipakai: tanpa login (halaman publik; tidak ada sesi aktif di browser) untuk semua TC. Tiap TC setelah TC pertama dimulai di jendela privat baru.
- Environment variable: `GS_TC_PASSWORD`, `MFA_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Kemampuan teknis:
  - Jendela privat; reCAPTCHA mode uji di environment.
  - Navigasi keyboard (tombol Tab) dan indikator fokus (TC-AUTH-MFA-14); pengisian clipboard dan tempel dengan Ctrl+V (TC-AUTH-MFA-88, 89).
  - Seeding state BE per user: riwayat login web sukses dengan trusted device ber-ID device browser uji A untuk kelima user profil NEWDEV (profil FIRST tidak butuh state tambahan); mekanisme seeding (endpoint/skrip uji) disediakan tim FE/BE karena tidak didefinisikan di TC, PRD, atau LLD.

## Test Steps

### TC-AUTH-MFA-04: Screening halaman OTP Verification (MFA) setelah memilih OTP via email

1. Buka halaman `Auth > Login with Password` di browser → halaman Login with Password tampil
2. Ketik `dewilestari+{runId}-004@qwertysystem.net` pada field Email
3. Ketik `Spectra.env.MFA_PASSWORD` pada field Password
4. Centang widget reCAPTCHA "I'm not a robot"
5. Klik button [Log in] → layar Confirm to Continue tampil
6. Centang checkbox persetujuan, lalu klik [Continue ➔] → halaman `Auth > MFA > Choose Verification Method` tampil
7. Pilih opsi "OTP via email" pada halaman Choose Verification Method
8. Klik button [Login] → halaman `Auth > MFA > OTP Verification` tampil dan email OTP faktor-2 terkirim ke `dewilestari+{runId}-004@qwertysystem.net`
9. Susuri halaman dari atas ke bawah tanpa mengklik apa pun
10. Verifikasi **Header**: Card `Elevated` terpusat
11. Verifikasi Logo TAG Samurai di bagian atas card
12. Verifikasi Title "Enter verification code"
13. Verifikasi Subtitle "We sent a code to dewilestari+{runId}-004@qwertysystem.net"
14. Verifikasi Alamat email `dewilestari+{runId}-004@qwertysystem.net` pada Subtitle tampil tanpa di-mask
15. Verifikasi **Body**: SegmentedInput 6 kotak digit dalam dua grup tiga kotak
16. Verifikasi Keenam kotak digit kosong
17. Verifikasi Kursor aktif di kotak 1
18. Verifikasi Slot alert error di bawah kotak digit kosong
19. Verifikasi Button Text [Resend code in Ns] disabled
20. Verifikasi Hitung mundur berada di dalam label tombol (N maksimal 60)
21. Verifikasi **Footer**: Button [Login] full-width (severity primary) tampil
22. Verifikasi Button [Login] enabled
23. Verifikasi Button Text [Use a different method] di tengah
24. Verifikasi Tidak ada tautan [Edit email]

### TC-AUTH-MFA-14: Accessibility — seluruh input dan tombol halaman OTP Verification dapat dijangkau dengan tombol Tab

25. Tutup jendela user uji dari TC sebelumnya dan hapus sesi login browser terkait (ID device dan jendela sesi akun aktor tetap), lalu buka jendela privat baru (tanpa sesi login)
26. Buka halaman `Auth > Login with Password` di browser → halaman Login with Password tampil
27. Ketik `linamarlina+{runId}-004@qwertysystem.net` pada field Email
28. Ketik `Spectra.env.MFA_PASSWORD` pada field Password
29. Centang widget reCAPTCHA "I'm not a robot"
30. Klik button [Log in] → layar Confirm to Continue tampil
31. Centang checkbox persetujuan, lalu klik [Continue ➔] → halaman `Auth > MFA > Choose Verification Method` tampil
32. Pilih opsi "OTP via email" pada halaman Choose Verification Method
33. Klik button [Login] → halaman `Auth > MFA > OTP Verification` tampil dan email OTP faktor-2 terkirim ke `linamarlina+{runId}-004@qwertysystem.net`
34. Tekan tombol Tab berulang dari awal halaman sampai fokus melewati elemen terakhir
35. Verifikasi Fokus berpindah berurutan melalui: kotak digit, button [Resend code], button [Login], lalu button [Use a different method]
36. Verifikasi Setiap elemen yang menerima fokus menampilkan indikator fokus yang terlihat

### TC-AUTH-MFA-67: Mengetik angka memajukan kursor dan Backspace mengembalikan fokus ke kotak sebelumnya

37. Tutup jendela user uji dari TC sebelumnya dan hapus sesi login browser terkait (ID device dan jendela sesi akun aktor tetap), lalu buka jendela privat baru (tanpa sesi login)
38. Buka halaman `Auth > Login with Password` di browser → halaman Login with Password tampil
39. Ketik `yuliarahayu+{runId}-004@qwertysystem.net` pada field Email
40. Ketik `Spectra.env.MFA_PASSWORD` pada field Password
41. Centang widget reCAPTCHA "I'm not a robot"
42. Klik button [Log in] → halaman `Auth > MFA > Choose Verification Method` tampil
43. Pilih opsi "OTP via email" pada halaman Choose Verification Method
44. Klik button [Login] → halaman `Auth > MFA > OTP Verification` tampil dan email OTP faktor-2 terkirim ke `yuliarahayu+{runId}-004@qwertysystem.net`
45. Ketik digit `1`, `2`, `3` berurutan pada kotak digit
46. Verifikasi Kotak 1 sampai 3 berisi `1`, `2`, `3`
47. Verifikasi Fokus berada di kotak 4
48. Klik kotak 3 yang berisi `3`
49. Tekan tombol Backspace satu kali
50. Verifikasi Kotak 3 dikosongkan
51. Verifikasi Fokus kembali ke kotak 2
52. Tekan tombol Backspace satu kali lagi
53. Verifikasi Kotak 2 dikosongkan
54. Verifikasi Fokus kembali ke kotak 1
55. Verifikasi Tidak ada verifikasi yang berjalan

### TC-AUTH-MFA-69: Karakter selain angka tidak dapat diketik pada kotak digit OTP

56. Tutup jendela user uji dari TC sebelumnya dan hapus sesi login browser terkait (ID device dan jendela sesi akun aktor tetap), lalu buka jendela privat baru (tanpa sesi login)
57. Buka halaman `Auth > Login with Password` di browser → halaman Login with Password tampil
58. Ketik `nandasafira+{runId}-004@qwertysystem.net` pada field Email
59. Ketik `Spectra.env.MFA_PASSWORD` pada field Password
60. Centang widget reCAPTCHA "I'm not a robot"
61. Klik button [Log in] → halaman `Auth > MFA > Choose Verification Method` tampil
62. Pilih opsi "OTP via email" pada halaman Choose Verification Method
63. Klik button [Login] → halaman `Auth > MFA > OTP Verification` tampil dan email OTP faktor-2 terkirim ke `nandasafira+{runId}-004@qwertysystem.net`
64. Ketik huruf `a` dan simbol `-` pada kotak 1
65. Verifikasi Huruf `a` dan simbol `-` tidak masuk ke kotak 1 dan kotak tetap kosong
66. Verifikasi Tidak ada caption error
67. Ketik digit `5` pada kotak 1
68. Verifikasi Digit `5` masuk ke kotak 1
69. Verifikasi Fokus berpindah ke kotak 2

### TC-AUTH-MFA-87: Backspace pada kotak kosong mengosongkan kotak kiri dan memindahkan fokus ke sana

70. Tutup jendela user uji dari TC sebelumnya dan hapus sesi login browser terkait (ID device dan jendela sesi akun aktor tetap), lalu buka jendela privat baru (tanpa sesi login)
71. Buka halaman `Auth > Login with Password` di browser → halaman Login with Password tampil
72. Ketik `hendrawijaya+{runId}-004@qwertysystem.net` pada field Email
73. Ketik `Spectra.env.MFA_PASSWORD` pada field Password
74. Centang widget reCAPTCHA "I'm not a robot"
75. Klik button [Log in] → halaman `Auth > MFA > Choose Verification Method` tampil
76. Pilih opsi "OTP via email" pada halaman Choose Verification Method
77. Klik button [Login] → halaman `Auth > MFA > OTP Verification` tampil dan email OTP faktor-2 terkirim ke `hendrawijaya+{runId}-004@qwertysystem.net`
78. Ketik digit `1`, `2`, `3` berurutan pada kotak digit (fokus berada di kotak 4 yang kosong)
79. Tekan tombol Backspace satu kali
80. Verifikasi Kotak 3 dikosongkan
81. Verifikasi Fokus berpindah ke kotak 3
82. Verifikasi Kotak 1 dan 2 tetap berisi `1` dan `2`
83. Verifikasi Tidak ada verifikasi yang berjalan

### TC-AUTH-MFA-88: Paste 6 digit mulai dari kotak 3 mengisi sampai kotak 6, membuang digit berlebih, dan tidak memverifikasi otomatis

84. Tutup jendela user uji dari TC sebelumnya dan hapus sesi login browser terkait (ID device dan jendela sesi akun aktor tetap), lalu buka jendela privat baru (tanpa sesi login)
85. Buka halaman `Auth > Login with Password` di browser → halaman Login with Password tampil
86. Ketik `linawijaya+{runId}-004@qwertysystem.net` pada field Email
87. Ketik `Spectra.env.MFA_PASSWORD` pada field Password
88. Centang widget reCAPTCHA "I'm not a robot"
89. Klik button [Log in] → halaman `Auth > MFA > Choose Verification Method` tampil
90. Pilih opsi "OTP via email" pada halaman Choose Verification Method
91. Klik button [Login] → halaman `Auth > MFA > OTP Verification` tampil dan email OTP faktor-2 terkirim ke `linawijaya+{runId}-004@qwertysystem.net`
92. Salin teks `123456` ke clipboard
93. Klik kotak 3
94. Tempel `123456` dengan Ctrl+V
95. Verifikasi Kotak 3, 4, 5, dan 6 berisi `1`, `2`, `3`, `4`
96. Verifikasi Digit `5` dan `6` dari clipboard dibuang
97. Verifikasi Kotak 1 dan 2 tetap kosong
98. Verifikasi Tidak ada verifikasi otomatis berjalan (keenam kotak belum terisi)

### TC-AUTH-MFA-89: Paste yang berisi karakter non-digit mengabaikan karakter tersebut

99. Tutup jendela user uji dari TC sebelumnya dan hapus sesi login browser terkait (ID device dan jendela sesi akun aktor tetap), lalu buka jendela privat baru (tanpa sesi login)
100. Buka halaman `Auth > Login with Password` di browser → halaman Login with Password tampil
101. Ketik `teguhwijaya+{runId}-004@qwertysystem.net` pada field Email
102. Ketik `Spectra.env.MFA_PASSWORD` pada field Password
103. Centang widget reCAPTCHA "I'm not a robot"
104. Klik button [Log in] → halaman `Auth > MFA > Choose Verification Method` tampil
105. Pilih opsi "OTP via email" pada halaman Choose Verification Method
106. Klik button [Login] → halaman `Auth > MFA > OTP Verification` tampil dan email OTP faktor-2 terkirim ke `teguhwijaya+{runId}-004@qwertysystem.net`
107. Salin teks `12a4` ke clipboard
108. Klik kotak 1
109. Tempel `12a4` dengan Ctrl+V
110. Verifikasi Kotak 1, 2, dan 3 berisi `1`, `2`, `4`
111. Verifikasi Karakter `a` diabaikan
112. Verifikasi Kotak 4 sampai 6 kosong
113. Verifikasi Tidak ada verifikasi otomatis berjalan

## Notes

- Sumber: `auth/mfa/TestCases/tc-mfa.md`. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Langkah pembuka tiap TC sesudah TC pertama menutup jendela user uji dari TC sebelumnya dan menghapus sesi login browser terkait (ID device dan jendela sesi akun aktor tetap) sebelum jendela baru dibuka; itu langkah penghubung tanpa `Verifikasi` (S-03, S-09).
- Langkah penghubung tanpa awalan `Verifikasi` (buka jendela privat baru di awal tiap TC setelah TC pertama; menyalin teks `123456` dan `12a4` ke clipboard pada TC-AUTH-MFA-88 dan 89) bukan asersi tambahan (S-03). Penyalinan ke clipboard mewujudkan Data Uji "Clipboard" milik TC.
- Urutan mengikuti TC sumber: screening (TC-AUTH-MFA-04, 14) lebih dulu, lalu perilaku input kotak digit. Spec tidak memuat aksi sukses, penolakan server, atau pembuatan sesi, jadi tidak ada penyimpangan urutan (S-10).
- Browser/jendela privat berbeda dipakai berurutan hanya untuk membentuk identitas device (browser uji B), tanpa asersi lintas jendela; bukan konteks kedua (tidak butuh butir P-2).
- Pembagian TC lintas spec: TC-AUTH-MFA-69 butir c ("Server menolak kode non-numerik yang lolos filter FE") menunjuk TC terpisah (TC-AUTH-MFA-86, defense-in-depth) dan tidak diasersi di spec ini.
- Ukuran spec (smell sekitar 35 langkah): spec ini sekitar 78 langkah setelah langkah prefix login faktor-1 yang identik (buka Login with Password sampai klik [Log in]) tidak dihitung. Tidak dipecah karena ketujuh TC independen: tiap TC memakai user dan jendela privat sendiri, sehingga bagian sesudahnya tetap bermakna bila bagian sebelumnya gagal.
- Temuan untuk QA: (1) TC-AUTH-MFA-14 Expected a menyebut fokus melalui button [Resend code], tetapi button itu disabled selama cooldown 60 detik dan lazimnya tidak menerima fokus; TC tidak menyebut apakah Tab ditekan setelah cooldown selesai. Spec tetap mengikuti TC (S-15). (2) TC-AUTH-MFA-87 Expected a berbunyi "Kotak 3 dikosongkan dan fokus berpindah ke kotak 3"; diikuti apa adanya. (3) Precondition c (email uji dapat dibaca lewat mail-catcher) tidak dipakai oleh Langkah Uji atau Expected TC di spec ini, jadi mail-catcher tidak dicantumkan di Kemampuan teknis. (4) Post Condition TC-AUTH-MFA-04 "Email OTP faktor-2 terkirim ke `dewilestari@qwertysystem.net`; sesi pre-auth MFA aktif" tidak punya Expected padanan maupun langkah observasi (email hanya disebut sebagai penjelasan hasil Langkah 7); tidak diasersi di spec (S-01, S-15). Sesi pre-auth teramati sebagai halaman OTP Verification tampil. (5) Post Condition "Tidak ada entri log" pada TC-AUTH-MFA-67, 69, 87, 88, 89 tidak punya Expected padanan maupun langkah observasi di TC, dan TC itu tidak masuk spec absence; tidak diasersi di spec (S-01, S-05, S-15). QA perlu menambah Expected atau langkah observasi ke TC bila ketiadaan entri log itu harus diuji. (6) Mekanisme seed state BE (trusted device ber-ID device browser uji A) belum ada di Pre-setup (#20/#21); spec tidak menyebut endpoint karangan (S-11, S-13).
