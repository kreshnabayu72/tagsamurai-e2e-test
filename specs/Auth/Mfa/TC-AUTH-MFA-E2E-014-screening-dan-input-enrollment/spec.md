---
id: TC-AUTH-MFA-E2E-014-screening-dan-input-enrollment
title: "Screening dan Input Kotak Digit Halaman Enrollment Authenticator"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-MFA-07
  - TC-AUTH-MFA-16
  - TC-AUTH-MFA-113
  - TC-AUTH-MFA-121
  - TC-AUTH-MFA-122
  - TC-AUTH-MFA-123
coverage:
  web: automated
---

# Screening dan Input Kotak Digit Halaman Enrollment Authenticator

## Prerequisites

- Mode: FE+BE.
- Seeding (hook `before`, lewat API oleh akun aktor Total Control (Global Settings) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.GS_TC_PASSWORD`): enam user profil FIRST (Tabel Data Uji Pre-setup #3: Activated, Active ON, belum pernah login di platform mana pun, Authenticator belum terdaftar), password `Spectra.env.MFA_PASSWORD`, email bersuffix per run:
  - TC-AUTH-MFA-07: `Agus Setiawan` (`agussetiawan+{runId}-014@qwertysystem.net`)
  - TC-AUTH-MFA-16: `Yuni Astuti` (`yuniastuti+{runId}-014@qwertysystem.net`)
  - TC-AUTH-MFA-113: `Hesti Rahmadani` (`hestirahmadani+{runId}-014@qwertysystem.net`)
  - TC-AUTH-MFA-121: `Yuni Rahmawati` (`yunirahmawati+{runId}-014@qwertysystem.net`)
  - TC-AUTH-MFA-123: `Wulan Rahmawati` (`wulanrahmawati+{runId}-014@qwertysystem.net`)
  - TC-AUTH-MFA-122: `Bayu Rahmawati` (`bayurahmawati+{runId}-014@qwertysystem.net`)
- Seeding state BE per user: hanya profil FIRST (Activated, Active ON, belum pernah login di platform mana pun, Authenticator belum terdaftar) yang dibentuk lewat pembuatan user oleh akun aktor; tidak ada state BE lain yang di-seed (trusted device, lokasi dan waktu login terakhir, consent, secret Authenticator). Secret pending dan enrollment dibentuk oleh alur UI spec ini sendiri.
- Hook `after`: hapus keenam user. Pembersihan tidak berasumsi seeding berhasil penuh.
- Akun yang dipakai: tanpa login (halaman publik; tidak ada sesi aktif di browser) untuk semua TC. Tiap TC setelah yang pertama dimulai di jendela privat baru.
- Environment variable: `GS_TC_PASSWORD`, `MFA_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Kemampuan teknis: jendela privat; reCAPTCHA mode uji di environment; aplikasi authenticator uji (TOTP: SHA-1, 6 digit, periode 30 detik, jam tidak digeser) yang dapat mendaftarkan akun dari QR code atau secret key halaman Enrollment dan menghasilkan kode TOTP (TC-AUTH-MFA-113, 122); akses clipboard browser untuk menyalin kode dan menempelnya dengan Ctrl+V (TC-AUTH-MFA-122); navigasi keyboard (tombol Tab, Backspace) dan indikator fokus (TC-AUTH-MFA-16, 121); pengamatan request jaringan untuk memastikan tidak ada request verifikasi yang berjalan (TC-AUTH-MFA-113, 121, 122).
- Jeda nyata pendek (≤30 detik): langkah 53 menunggu 5 detik (TC-AUTH-MFA-113) untuk memastikan tidak ada auto-submit. Spec ini tidak mengatur jam server, jam browser, maupun jam aplikasi authenticator uji.
- Semua user berprofil FIRST, jadi tiap login melewati layar Confirm to Continue sebelum Choose Verification Method.

## Test Steps

### TC-AUTH-MFA-07: Screening halaman Enrollment Authenticator

1. Buka halaman `Auth > Login with Password` di browser → halaman Login with Password tampil
2. Ketik `agussetiawan+{runId}-014@qwertysystem.net` pada field Email
3. Ketik `Spectra.env.MFA_PASSWORD` pada field Password
4. Centang widget reCAPTCHA "I'm not a robot"
5. Klik button [Log in] → layar Confirm to Continue tampil
6. Centang checkbox persetujuan, lalu klik [Continue ➔] → halaman `Auth > MFA > Choose Verification Method` tampil
7. Pilih opsi "Authenticator app" pada halaman Choose Verification Method
8. Klik button [Login] → halaman `Auth > MFA > Enrollment Authenticator` tampil
9. Susuri halaman dari atas ke bawah tanpa mengklik apa pun
10. Verifikasi **Header**: Card `Elevated` terpusat
11. Verifikasi Title: "Set up authenticator app"
12. Verifikasi Subtitle: "Secure your account with an authenticator app. You only need to scan the QR code once — after that, just enter the 6-digit code from the app whenever you're asked to verify."
13. Verifikasi **Body**: tiga langkah tampil sekaligus dalam satu card
14. Verifikasi Body: tidak ada stepper
15. Verifikasi Step 1 berjudul "Download an authenticator app"
16. Verifikasi Step 1 berdeskripsi: "We recommend Google Authenticator if you don't have one yet. Authy also works."
17. Verifikasi Step 2 berjudul "Scan the QR code or copy the key"
18. Verifikasi Step 2 berdeskripsi: "Scan the QR code with your authenticator app, or copy the secret key below and enter it manually."
19. Verifikasi Step 2 menampilkan gambar QR code di tengah
20. Verifikasi Step 2 menampilkan secret key bergrup spasi
21. Verifikasi Step 2 menampilkan secret key dalam huruf monospace
22. Verifikasi Step 2 menampilkan CopyButton berlabel "Copy key"
23. Verifikasi Step 3 berjudul "Enter the 6-digit code"
24. Verifikasi Step 3 berdeskripsi: "Your authenticator app will generate a 6-digit code. Enter it below to finish setup."
25. Verifikasi Step 3 menampilkan SegmentedInput 6 kotak digit kosong
26. Verifikasi Step 3: kursor berada di kotak 1
27. Verifikasi **Footer**: Button Text [Cancel] (severity contrast)
28. Verifikasi Footer: Button [Verify] (severity primary)
29. Verifikasi Footer: Tidak ada tautan recovery code

### TC-AUTH-MFA-16: Accessibility — seluruh input dan tombol halaman Enrollment Authenticator dapat dijangkau dengan tombol Tab

30. Tutup jendela user uji dari TC sebelumnya dan hapus sesi login browser terkait (ID device dan jendela sesi akun aktor tetap), lalu buka jendela privat baru (tanpa sesi login)
31. Buka halaman `Auth > Login with Password` di browser → halaman Login with Password tampil
32. Ketik `yuniastuti+{runId}-014@qwertysystem.net` pada field Email
33. Ketik `Spectra.env.MFA_PASSWORD` pada field Password
34. Centang widget reCAPTCHA "I'm not a robot"
35. Klik button [Log in] → layar Confirm to Continue tampil
36. Centang checkbox persetujuan, lalu klik [Continue ➔] → halaman `Auth > MFA > Choose Verification Method` tampil
37. Pilih opsi "Authenticator app" pada halaman Choose Verification Method
38. Klik button [Login] → halaman `Auth > MFA > Enrollment Authenticator` tampil
39. Tekan tombol Tab berulang dari awal halaman sampai fokus melewati elemen terakhir
40. Verifikasi Fokus berpindah berurutan melalui: CopyButton "Copy key", kotak digit, button [Cancel], lalu button [Verify]
41. Verifikasi Setiap elemen yang menerima fokus menampilkan indikator fokus yang terlihat

### TC-AUTH-MFA-113: Enrollment tidak auto-submit saat digit ke-6 terisi

42. Tutup jendela user uji dari TC sebelumnya dan hapus sesi login browser terkait (ID device dan jendela sesi akun aktor tetap), lalu buka jendela privat baru (tanpa sesi login)
43. Buka halaman `Auth > Login with Password` di browser → halaman Login with Password tampil
44. Ketik `hestirahmadani+{runId}-014@qwertysystem.net` pada field Email
45. Ketik `Spectra.env.MFA_PASSWORD` pada field Password
46. Centang widget reCAPTCHA "I'm not a robot"
47. Klik button [Log in] → layar Confirm to Continue tampil
48. Centang checkbox persetujuan, lalu klik [Continue ➔] → halaman `Auth > MFA > Choose Verification Method` tampil
49. Pilih opsi "Authenticator app" pada halaman Choose Verification Method
50. Klik button [Login] → halaman `Auth > MFA > Enrollment Authenticator` tampil
51. Pindai QR code dengan aplikasi authenticator uji
52. Ketik 6 digit kode dari aplikasi authenticator uji pada kotak digit
53. Tunggu 5 detik tanpa mengklik apa pun
54. Verifikasi Tidak ada request verifikasi yang berjalan
55. Verifikasi Halaman tetap Enrollment Authenticator sampai button [Verify] diklik

### TC-AUTH-MFA-121: Mengetik angka memajukan kursor dan Backspace mengembalikan fokus ke kotak sebelumnya di Enrollment

56. Tutup jendela user uji dari TC sebelumnya dan hapus sesi login browser terkait (ID device dan jendela sesi akun aktor tetap), lalu buka jendela privat baru (tanpa sesi login)
57. Buka halaman `Auth > Login with Password` di browser → halaman Login with Password tampil
58. Ketik `yunirahmawati+{runId}-014@qwertysystem.net` pada field Email
59. Ketik `Spectra.env.MFA_PASSWORD` pada field Password
60. Centang widget reCAPTCHA "I'm not a robot"
61. Klik button [Log in] → layar Confirm to Continue tampil
62. Centang checkbox persetujuan, lalu klik [Continue ➔] → halaman `Auth > MFA > Choose Verification Method` tampil
63. Pilih opsi "Authenticator app" pada halaman Choose Verification Method
64. Klik button [Login] → halaman `Auth > MFA > Enrollment Authenticator` tampil
65. Ketik digit `1`, `2`, `3` berurutan pada kotak digit Step 3
66. Verifikasi Kotak 1 sampai 3 berisi `1`, `2`, `3`
67. Verifikasi Fokus berada di kotak 4
68. Klik kotak 3 yang berisi `3`
69. Tekan tombol Backspace satu kali
70. Verifikasi Kotak 3 dikosongkan
71. Verifikasi Fokus kembali ke kotak 2
72. Tekan tombol Backspace satu kali lagi
73. Verifikasi Kotak 2 dikosongkan
74. Verifikasi Fokus kembali ke kotak 1
75. Verifikasi Tidak ada verifikasi yang berjalan

### TC-AUTH-MFA-123: Karakter selain angka tidak dapat diketik pada kotak digit Enrollment

76. Tutup jendela user uji dari TC sebelumnya dan hapus sesi login browser terkait (ID device dan jendela sesi akun aktor tetap), lalu buka jendela privat baru (tanpa sesi login)
77. Buka halaman `Auth > Login with Password` di browser → halaman Login with Password tampil
78. Ketik `wulanrahmawati+{runId}-014@qwertysystem.net` pada field Email
79. Ketik `Spectra.env.MFA_PASSWORD` pada field Password
80. Centang widget reCAPTCHA "I'm not a robot"
81. Klik button [Log in] → layar Confirm to Continue tampil
82. Centang checkbox persetujuan, lalu klik [Continue ➔] → halaman `Auth > MFA > Choose Verification Method` tampil
83. Pilih opsi "Authenticator app" pada halaman Choose Verification Method
84. Klik button [Login] → halaman `Auth > MFA > Enrollment Authenticator` tampil
85. Ketik huruf `a` dan simbol `-` pada kotak 1
86. Verifikasi Huruf `a` dan simbol `-` tidak masuk ke kotak 1 dan kotak 1 tetap kosong
87. Verifikasi Tidak ada caption error pada kotak digit
88. Ketik digit `5` pada kotak 1
89. Verifikasi Digit `5` masuk ke kotak 1
90. Verifikasi Fokus berpindah ke kotak 2

### TC-AUTH-MFA-122: Menempel 6 digit sekaligus memecah karakter ke enam kotak Enrollment tanpa auto-submit

91. Tutup jendela user uji dari TC sebelumnya dan hapus sesi login browser terkait (ID device dan jendela sesi akun aktor tetap), lalu buka jendela privat baru (tanpa sesi login)
92. Buka halaman `Auth > Login with Password` di browser → halaman Login with Password tampil
93. Ketik `bayurahmawati+{runId}-014@qwertysystem.net` pada field Email
94. Ketik `Spectra.env.MFA_PASSWORD` pada field Password
95. Centang widget reCAPTCHA "I'm not a robot"
96. Klik button [Log in] → layar Confirm to Continue tampil
97. Centang checkbox persetujuan, lalu klik [Continue ➔] → halaman `Auth > MFA > Choose Verification Method` tampil
98. Pilih opsi "Authenticator app" pada halaman Choose Verification Method
99. Klik button [Login] → halaman `Auth > MFA > Enrollment Authenticator` tampil
100. Pindai QR code, salin 6 digit kode dari aplikasi authenticator uji ke clipboard
101. Klik kotak 1 lalu tempel dengan Ctrl+V
102. Verifikasi Keenam kotak terisi satu digit per kotak
103. Verifikasi Tidak ada verifikasi otomatis berjalan
104. Klik button [Verify]
105. Verifikasi Browser dialihkan ke Portal — Product Hub
106. Verifikasi Sesi web aktif untuk `Bayu Rahmawati`

## Notes

- Sumber: `auth/mfa/TestCases/tc-mfa.md`. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Langkah pembuka tiap TC sesudah TC pertama menutup jendela user uji dari TC sebelumnya dan menghapus sesi login browser terkait (ID device dan jendela sesi akun aktor tetap) sebelum jendela baru dibuka; itu langkah penghubung tanpa `Verifikasi` (S-03, S-09).
- Penyimpangan urutan (S-05): urutan TC sumber 07, 16, 113, 121, 122, 123; TC-AUTH-MFA-122 dipindah ke akhir karena satu-satunya TC yang berakhir dengan [Verify] sukses dan sesi penuh (aksi sukses terakhir, bagian 3 konvensi). Tiap TC memakai user sendiri, jadi perpindahan tidak mengubah data.
- Langkah penghubung tanpa awalan `Verifikasi` (buka jendela privat baru di awal tiap TC setelah yang pertama) bukan asersi tambahan (S-03).
- Batas ukuran: langkah prefix login faktor-1 yang identik antar-TC (buka Login with Password sampai klik [Log in]) tidak dihitung ke batas ±35 langkah (bagian 3 konvensi); keenam TC independen dan tiap TC memakai user sendiri, sehingga spec tidak dipecah.
- Butir c Expected TC-AUTH-MFA-123 ("Server menolak kode non-numerik yang lolos filter FE") menunjuk TC terpisah (kelas defense-in-depth): TC-AUTH-MFA-124 di spec `TC-AUTH-MFA-E2E-042-defense-cooldown-resend-dan-non-numerik`; tidak ditulis di spec ini.
- Temuan untuk QA: (1) Post Condition TC tanpa langkah observasi dan tanpa Expected padanan tidak diasersi di spec ini (S-01): TC-AUTH-MFA-07 butir a "Secret Authenticator pending untuk sesi pre-auth ini dibuat dan belum aktif" dan butir b "Tidak ada entri log untuk pembukaan halaman Enrollment" (absence dan pencatatan, S-05); TC-AUTH-MFA-113 "Enrollment belum aktif; tidak ada sesi"; TC-AUTH-MFA-121 dan TC-AUTH-MFA-123 "Enrollment belum aktif". QA dapat menambah Expected atau langkah observasi di TC. (2) TC-AUTH-MFA-122 Langkah Uji "Pindai QR code, salin 6 digit kode ... ke clipboard" memuat dua aksi tanpa langkah penyalinan eksplisit; kemampuan clipboard ditulis di Prerequisites (S-11). (3) Mekanisme seeding user profil FIRST mengikuti Pre-setup #3 (Create User); tidak ada state BE tambahan yang butuh mekanisme seeding di spec ini.
