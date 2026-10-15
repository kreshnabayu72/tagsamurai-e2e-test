---
id: TC-AUTH-MFA-E2E-030-user-dinonaktifkan-atau-dihapus-saat-mfa
title: "User Dinonaktifkan atau Dihapus Saat MFA Berlangsung"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AUTH-MFA-138
  - TC-AUTH-MFA-140
  - TC-AUTH-MFA-141
  - TC-AUTH-MFA-217
  - TC-AUTH-MFA-142
  - TC-AUTH-MFA-139
coverage:
  web: automated
---

# User Dinonaktifkan atau Dihapus Saat MFA Berlangsung

## Prerequisites

- Mode: FE+BE.
- Seeding (hook `before`, lewat API oleh akun aktor Total Control (Global Settings) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.GS_TC_PASSWORD`): enam user Activated, Active ON, password `Spectra.env.MFA_PASSWORD`, email bersuffix per run. Kondisi BE yang di-seed per profil:
  - Profil NEWDEV (Tabel Data Uji Pre-setup #4): seperti BASE, yaitu sudah pernah login sukses di web dari browser uji A (ID device browser uji A tercatat sebagai trusted device), login terakhir dari IP uji Jakarta (ID), logout web terakhir kurang dari 30 hari; Authenticator belum terdaftar. Login dilakukan dari browser uji B (ID device belum ada di daftar trusted device) sehingga MFA terpicu.
  - Profil NEWDEVE (Tabel Data Uji Pre-setup #5): seperti NEWDEV tetapi Authenticator sudah terdaftar (secret TOTP dipegang aplikasi authenticator uji).
  - Profil FIRST (Tabel Data Uji Pre-setup #3): belum pernah menyelesaikan login di platform mana pun; Authenticator belum terdaftar.
  - TC-AUTH-MFA-138: `Dwi Cahyono` (`dwicahyono+{runId}-030@qwertysystem.net`), NEWDEVE
  - TC-AUTH-MFA-140: `Farhan Akbar` (`farhanakbar+{runId}-030@qwertysystem.net`), NEWDEV
  - TC-AUTH-MFA-141: `Putri Wijaya` (`putriwijaya+{runId}-030@qwertysystem.net`), NEWDEV
  - TC-AUTH-MFA-217: `Rizal Hakim` (`rizalhakim+{runId}-030@qwertysystem.net`), NEWDEV
  - TC-AUTH-MFA-142: `Fajar Wijaya` (`fajarwijaya+{runId}-030@qwertysystem.net`), FIRST
  - TC-AUTH-MFA-139: `Ega Prakoso` (`egaprakoso+{runId}-030@qwertysystem.net`), NEWDEVE
- Aktor Total Control (Global Settings) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (`Spectra.env.GS_TC_PASSWORD`) login satu kali di hook `before` pada browser kedua (konteks browser terpisah dari browser user uji) dan sesinya dipakai sepanjang spec untuk Deactivate, Delete, dan membaca `Global Settings > Activity Log > Session` serta `Global Settings > User > Detail > User Log` (TC-AUTH-MFA-138). Login akun aktor tidak memicu MFA. Browser kedua tidak memegang sesi user uji; fungsinya hanya mengubah state user target dan membaca log.
- Hook `after`: pulihkan jam server uji dan jam browser uji ke waktu nyata; hapus semua user yang dibuat spec ini (termasuk yang berstatus Inactive; `Ega Prakoso` sudah terhapus oleh TC-AUTH-MFA-139); tutup browser kedua. Hook ini tetap jalan walau spec gagal di tengah dan tidak berasumsi seeding atau langkah spec berhasil penuh.
- Akun yang dipakai: user uji tanpa login (halaman publik; tidak ada sesi aktif di browser) di jendela baru browser pertama; akun aktor Total Control (Global Settings) di browser kedua. Browser uji B = jendela privat baru (ID device belum dikenali) untuk semua TC kecuali TC-AUTH-MFA-142 yang memakai browser uji A (profil browser reguler dengan ID device persisten).
- Environment variable: `GS_TC_PASSWORD`, `MFA_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Kemampuan teknis: dua konteks browser terpisah (browser pertama untuk user uji, browser kedua untuk akun aktor); browser uji A (profil reguler) dan browser uji B (jendela privat baru); mail-catcher lingkungan uji untuk email OTP faktor-2 (TC-AUTH-MFA-140, 141, 217); aplikasi authenticator uji (TOTP: SHA-1, 6 digit, periode 30 detik) untuk kode TOTP valid dan pemindaian QR Enrollment; pengaturan jam server uji dan jam browser uji (dimajukan N detik lalu dipulihkan; TC-AUTH-MFA-217); reCAPTCHA mode uji di environment; pembacaan status enrollment Authenticator user oleh sisi BE (TC-AUTH-MFA-142; disediakan tim FE/BE karena tidak ada cara cek di UI atau di Langkah Uji TC). Seeding state BE per user: trusted device ber-ID device browser uji A, lokasi dan waktu login terakhir, logout web terakhir, authenticator terdaftar dengan secret yang dikenal authenticator uji, dan penanda belum pernah login (profil FIRST); mekanisme seeding (endpoint/skrip uji) disediakan tim FE/BE karena tidak didefinisikan di TC, PRD, atau LLD.
- State global: jam server uji dan jam browser uji (hanya TC-AUTH-MFA-217; dipulihkan di akhir TC itu dan di hook `after`). Suite berjalan serial (`parallel: false`) karena spec ini mengubah jam server uji dan jam browser uji; hook `after` memulihkan jam server uji dan jam browser uji. Selain itu hanya data user milik spec ini yang diubah.

## Test Steps

### TC-AUTH-MFA-138: User dinonaktifkan saat MFA berlangsung: faktor-2 diblok dan diarahkan ke login dengan caption Your account is inactive

1. Buka jendela privat baru di browser pertama (tanpa sesi login)
2. Buka halaman `Auth > Login with Password` di browser uji B → halaman Login with Password tampil
3. Ketik `dwicahyono+{runId}-030@qwertysystem.net` pada field Email
4. Ketik `Spectra.env.MFA_PASSWORD` pada field Password
5. Centang widget reCAPTCHA "I'm not a robot"
6. Klik button [Log in] → halaman `Auth > MFA > Choose Verification Method` tampil
7. Pilih opsi "Authenticator app" pada halaman Choose Verification Method
8. Klik button [Login] → halaman `Auth > MFA > Authenticator Verification` tampil
9. Beralih ke browser kedua (sesi Total Control Global Settings) lalu buka `Global Settings > User` dan cari `dwicahyono+{runId}-030@qwertysystem.net` pada User List
10. Klik switch Active baris `Dwi Cahyono` (Toggle Active OFF) → dialog Deactivate User tampil
11. Klik button [Deactivate] pada dialog
12. Catat penanda waktu sesudah Deactivate selesai sebagai acuan entri log baru untuk `Dwi Cahyono`
13. Beralih ke browser pertama (halaman Authenticator Verification)
14. Ketik 6 digit kode TOTP valid dari aplikasi authenticator uji untuk `dwicahyono+{runId}-030@qwertysystem.net` pada kotak digit lalu klik button [Login]
15. Verifikasi Halaman Login with Password tampil
16. Verifikasi Caption "Your account is inactive" tampil pada halaman Login with Password
17. Verifikasi Tidak ada sesi penuh yang dibuat untuk `Dwi Cahyono`
18. Beralih ke browser kedua, buka `Global Settings > Activity Log > Session`, dan cari entri untuk `Dwi Cahyono` dengan email bersuffix `dwicahyono+{runId}-030@qwertysystem.net` yang dibuat sesudah penanda waktu langkah 12
19. Verifikasi Tidak ada entri log baru untuk kegagalan karena status akun `Dwi Cahyono` pada Activity Log > Session sesudah penanda waktu langkah 12
20. Buka `Global Settings > User > Detail > User Log` untuk `Dwi Cahyono` dan cari entri yang dibuat sesudah penanda waktu langkah 12
21. Verifikasi Tidak ada entri log baru untuk kegagalan karena status akun pada User Log `Dwi Cahyono` sesudah penanda waktu langkah 12

### TC-AUTH-MFA-140: User dinonaktifkan saat OTP faktor-2 menunggu: Verify diblok dan diarahkan ke login

22. Tutup jendela user uji dari TC sebelumnya dan hapus sesi login browser terkait (ID device dan jendela sesi akun aktor tetap), lalu pindah ke browser pertama dan buka jendela privat baru (tanpa sesi login)
23. Buka halaman `Auth > Login with Password` di browser uji B → halaman Login with Password tampil
24. Ketik `farhanakbar+{runId}-030@qwertysystem.net` pada field Email
25. Ketik `Spectra.env.MFA_PASSWORD` pada field Password
26. Centang widget reCAPTCHA "I'm not a robot"
27. Klik button [Log in] → halaman `Auth > MFA > Choose Verification Method` tampil
28. Pilih opsi "OTP via email" pada halaman Choose Verification Method
29. Klik button [Login] → halaman `Auth > MFA > OTP Verification` tampil dan email OTP faktor-2 terkirim ke `farhanakbar+{runId}-030@qwertysystem.net`
30. Beralih ke browser kedua (sesi Total Control Global Settings) lalu buka `Global Settings > User` dan cari `farhanakbar+{runId}-030@qwertysystem.net` pada User List
31. Klik switch Active baris `Farhan Akbar` (Toggle Active OFF) → dialog Deactivate User tampil
32. Klik button [Deactivate] pada dialog
33. Beralih ke browser pertama (halaman OTP Verification)
34. Ketik 6 digit kode OTP faktor-2 dari email `farhanakbar+{runId}-030@qwertysystem.net` (dibaca dari mail-catcher) pada kotak digit
35. Verifikasi Halaman Login with Password tampil
36. Verifikasi Caption "Your account is inactive" tampil pada halaman Login with Password
37. Verifikasi Tidak ada sesi penuh yang dibuat untuk `Farhan Akbar`

### TC-AUTH-MFA-141: User dinonaktifkan sebelum memilih OTP via email: pengiriman OTP ditolak dan diarahkan ke login

38. Tutup jendela user uji dari TC sebelumnya dan hapus sesi login browser terkait (ID device dan jendela sesi akun aktor tetap), lalu pindah ke browser pertama dan buka jendela privat baru (tanpa sesi login)
39. Buka halaman `Auth > Login with Password` di browser uji B → halaman Login with Password tampil
40. Ketik `putriwijaya+{runId}-030@qwertysystem.net` pada field Email
41. Ketik `Spectra.env.MFA_PASSWORD` pada field Password
42. Centang widget reCAPTCHA "I'm not a robot"
43. Klik button [Log in] → halaman `Auth > MFA > Choose Verification Method` tampil
44. Beralih ke browser kedua (sesi Total Control Global Settings) lalu buka `Global Settings > User` dan cari `putriwijaya+{runId}-030@qwertysystem.net` pada User List
45. Klik switch Active baris `Putri Wijaya` (Toggle Active OFF) → dialog Deactivate User tampil
46. Klik button [Deactivate] pada dialog
47. Beralih ke browser pertama (halaman Choose Verification Method)
48. Periksa mail-catcher lingkungan uji untuk `putriwijaya+{runId}-030@qwertysystem.net` dan catat jumlah email OTP faktor-2 sebagai acuan
49. Pilih opsi "OTP via email" lalu klik button [Login]
50. Verifikasi Halaman Login with Password tampil
51. Verifikasi Caption "Your account is inactive" tampil pada halaman Login with Password
52. Periksa mail-catcher lingkungan uji untuk `putriwijaya+{runId}-030@qwertysystem.net`
53. Verifikasi Tidak ada email OTP faktor-2 baru di mail-catcher `putriwijaya+{runId}-030@qwertysystem.net` (jumlah email OTP faktor-2 sama dengan acuan)
54. Verifikasi Tidak ada sesi penuh yang dibuat untuk `Putri Wijaya`

### TC-AUTH-MFA-217: User dinonaktifkan saat OTP faktor-2 menunggu: Resend ditolak dan diarahkan ke login

55. Tutup jendela user uji dari TC sebelumnya dan hapus sesi login browser terkait (ID device dan jendela sesi akun aktor tetap), lalu pindah ke browser pertama dan buka jendela privat baru (tanpa sesi login)
56. Buka halaman `Auth > Login with Password` di browser uji B → halaman Login with Password tampil
57. Ketik `rizalhakim+{runId}-030@qwertysystem.net` pada field Email
58. Ketik `Spectra.env.MFA_PASSWORD` pada field Password
59. Centang widget reCAPTCHA "I'm not a robot"
60. Klik button [Log in] → halaman `Auth > MFA > Choose Verification Method` tampil
61. Pilih opsi "OTP via email" lalu klik button [Login] → halaman `Auth > MFA > OTP Verification` tampil dan email OTP faktor-2 terkirim ke `rizalhakim+{runId}-030@qwertysystem.net`
62. Beralih ke browser kedua (sesi Total Control Global Settings) lalu buka `Global Settings > User` dan cari `rizalhakim+{runId}-030@qwertysystem.net` pada User List
63. Klik switch Active baris `Rizal Hakim` (Toggle Active OFF) → dialog Deactivate User tampil
64. Klik button [Deactivate] pada dialog
65. Beralih ke browser pertama (halaman OTP Verification)
66. Majukan jam server uji dan jam browser uji 61 detik sehingga hitung mundur cooldown Resend 1 menit selesai dan button Text [Resend code] aktif
67. Periksa mail-catcher lingkungan uji untuk `rizalhakim+{runId}-030@qwertysystem.net` dan catat jumlah email OTP faktor-2 sebagai acuan
68. Klik button Text [Resend code]
69. Pulihkan jam server uji dan jam browser uji ke waktu nyata
70. Verifikasi Halaman Login with Password tampil
71. Verifikasi Caption "Your account is inactive" tampil pada halaman Login with Password
72. Periksa mail-catcher lingkungan uji untuk `rizalhakim+{runId}-030@qwertysystem.net`
73. Verifikasi Tidak ada email OTP faktor-2 kedua di mail-catcher `rizalhakim+{runId}-030@qwertysystem.net` (jumlah email OTP faktor-2 sama dengan acuan)
74. Verifikasi Tidak ada sesi penuh yang dibuat untuk `Rizal Hakim`

### TC-AUTH-MFA-142: User dinonaktifkan saat Enrollment: verifikasi ditolak dan enrollment tidak aktif

75. Tutup jendela user uji dari TC sebelumnya dan hapus sesi login browser terkait (ID device dan jendela sesi akun aktor tetap), lalu pindah ke browser pertama dan buka jendela baru di browser uji A (tanpa sesi login)
76. Buka halaman `Auth > Login with Password` di browser uji A → halaman Login with Password tampil
77. Ketik `fajarwijaya+{runId}-030@qwertysystem.net` pada field Email
78. Ketik `Spectra.env.MFA_PASSWORD` pada field Password
79. Centang widget reCAPTCHA "I'm not a robot"
80. Klik button [Log in] → layar Confirm to Continue tampil
81. Centang checkbox persetujuan, lalu klik [Continue ➔] → halaman `Auth > MFA > Choose Verification Method` tampil
82. Pilih opsi "Authenticator app" pada halaman Choose Verification Method
83. Klik button [Login] → halaman `Auth > MFA > Enrollment Authenticator` tampil
84. Beralih ke browser kedua (sesi Total Control Global Settings) lalu buka `Global Settings > User` dan cari `fajarwijaya+{runId}-030@qwertysystem.net` pada User List
85. Klik switch Active baris `Fajar Wijaya` (Toggle Active OFF) → dialog Deactivate User tampil
86. Klik button [Deactivate] pada dialog
87. Beralih ke browser pertama (halaman Enrollment Authenticator)
88. Pindai QR code dengan aplikasi authenticator uji
89. Ketik 6 digit kode valid dari aplikasi authenticator uji pada kotak digit lalu klik button [Verify]
90. Verifikasi Halaman Login with Password tampil
91. Verifikasi Caption "Your account is inactive" tampil pada halaman Login with Password
92. Verifikasi Enrollment Authenticator `Fajar Wijaya` tidak aktif
93. Verifikasi Tidak ada sesi penuh yang dibuat untuk `Fajar Wijaya`

### TC-AUTH-MFA-139: User dihapus saat MFA berlangsung: faktor-2 diblok dan diarahkan ke login tanpa caption

94. Tutup jendela user uji dari TC sebelumnya dan hapus sesi login browser terkait (ID device dan jendela sesi akun aktor tetap), lalu pindah ke browser pertama dan buka jendela privat baru (tanpa sesi login)
95. Buka halaman `Auth > Login with Password` di browser uji B → halaman Login with Password tampil
96. Ketik `egaprakoso+{runId}-030@qwertysystem.net` pada field Email
97. Ketik `Spectra.env.MFA_PASSWORD` pada field Password
98. Centang widget reCAPTCHA "I'm not a robot"
99. Klik button [Log in] → halaman `Auth > MFA > Choose Verification Method` tampil
100. Pilih opsi "Authenticator app" pada halaman Choose Verification Method
101. Klik button [Login] → halaman `Auth > MFA > Authenticator Verification` tampil
102. Beralih ke browser kedua (sesi Total Control Global Settings) lalu buka `Global Settings > User` dan cari `egaprakoso+{runId}-030@qwertysystem.net` pada User List
103. Klik (⋯) baris `Ega Prakoso` → `Delete` → dialog Delete tampil
104. Klik button [Delete] pada dialog
105. Beralih ke browser pertama (halaman Authenticator Verification)
106. Ketik 6 digit kode TOTP valid dari aplikasi authenticator uji untuk `egaprakoso+{runId}-030@qwertysystem.net` pada kotak digit lalu klik button [Login]
107. Verifikasi Halaman Login with Password tampil
108. Verifikasi Tidak ada caption pada halaman Login with Password
109. Verifikasi Tidak ada sesi penuh yang dibuat untuk `Ega Prakoso`

## Notes

- Sumber: `auth/mfa/TestCases/tc-mfa.md`. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. Akun aktor Total Control login satu kali di hook `before` di browser kedua dan hanya memicu perubahan state user target (Toggle Active, Delete) serta membaca log; ini bukan konteks kedua yang menjadi objek asersi, sehingga tidak butuh butir `P-2`. Pembacaan email di mail-catcher dan pengaturan jam adalah langkah rutin spec fungsional (bukan kelas harness tersendiri).
- Langkah pembuka tiap TC sesudah TC pertama menutup jendela user uji dari TC sebelumnya dan menghapus sesi login browser terkait (ID device dan jendela sesi akun aktor tetap) sebelum jendela baru dibuka; itu langkah penghubung tanpa `Verifikasi` (S-03, S-09).
- `P-1`: asersi absence TC-AUTH-MFA-138 Expected c ("tidak ada entri log untuk kegagalan karena status akun") tetap di spec ini karena konteksnya bergantung pada state berat yang baru dibangun langkah sebelumnya di spec (handoff MFA: sesi pre-auth Authenticator Verification, user Inactive). Asersinya memakai baseline penanda waktu (S-12) dan mencakup entri kegagalan login karena status akun; entri pencatatan aksi Deactivate itu sendiri berada di luar asersi. Langkah Uji TC-AUTH-MFA-138 tidak punya langkah observasi log; spec menambahkan langkah 12 (penanda waktu) dan langkah 18 sampai 21 (baca Activity Log > Session dan User Log) sebagai dasar Expected c. Spec absence `TC-AUTH-MFA-E2E-035-absence-pencatatan-log` tidak memuat TC-AUTH-MFA-138.
- Melewati ±35 langkah (±73 netto setelah langkah prefix login faktor-1 tidak dihitung) karena enam TC independen; tiap TC memakai user sendiri dan jendela privat baru, aksi Deactivate memakai user milik TC itu, dan TC Delete (TC-AUTH-MFA-139) ditaruh paling akhir, sehingga bagian sesudahnya tetap bermakna walau bagian sebelumnya gagal dan spec tidak dipecah.
- Pembagian lintas spec: TC-AUTH-MFA-75 dan 161 (ganti email saat OTP faktor-2) berada di spec `TC-AUTH-MFA-E2E-055-ganti-email-saat-otp-mfa` karena topik aksinya berbeda (prinsip 1); spec ini hanya memuat Deactivate dan Delete.
- Urutan: sumber TC memuat TC-AUTH-MFA-139 (menghapus user) di urutan kedua; di spec ini TC-AUTH-MFA-139 ditaruh paling akhir, sesudah semua TC Deactivate (138, 140, 141, 217, 142), karena aksi yang menghabisi data di akhir spec (S-10). TC-AUTH-MFA-217 ditaruh sebelum TC-AUTH-MFA-142 (di TC sumber 217 berada sesudah 142) supaya TC faktor-2 OTP (140, 141, 217) yang sama-sama memakai mail-catcher, browser uji B, dan user NEWDEV berurutan, dan jam server uji serta jam browser uji yang dimajukan pada TC-AUTH-MFA-217 sudah dipulihkan sebelum TC Enrollment (142, browser uji A, profil FIRST) berjalan (S-05). Aksi ini memakai user milik sendiri sehingga tidak memengaruhi TC lain, dan baris `Ega Prakoso` memang sudah terhapus saat cleanup.
- Langkah penghubung tanpa awalan `Verifikasi` (buka jendela baru di awal tiap TC; beralih antara browser pertama dan kedua; cari user pada User List; catat penanda waktu dan acuan jumlah email; majukan dan pulihkan jam pada TC-AUTH-MFA-217; pindai QR pada TC-AUTH-MFA-142; tanpa klik tambahan setelah mengetik kode OTP pada TC-AUTH-MFA-140) bukan asersi tambahan (S-03). Pencarian user memakai email bersuffix karena nama user yang sama dipakai spec lain dalam satu run. Jam server uji dan jam browser uji dimajukan bersama pada TC-AUTH-MFA-217 karena hitung mundur Resend berjalan di jam klien; keduanya dipulihkan segera setelah [Resend code] diklik.
- Temuan untuk QA: (1) TC-AUTH-MFA-140 langkah 9 hanya menyebut mengetik kode OTP dan tidak menyebut klik [Login], sedangkan TC-AUTH-MFA-138, 139, dan 142 menyebut klik [Login] atau [Verify] secara eksplisit; spec mengikuti teks TC-AUTH-MFA-140 dan hanya mengetik (langkah 34). (2) TC-AUTH-MFA-138 sampai 142 dan 217 menyebut "nonaktifkan" tanpa langkah di Global Settings; spec memakai alur switch Active lalu `[Deactivate]` dari TC `global-settings/user`. (3) TC-AUTH-MFA-139 menyebut "hapus" tanpa langkah; spec memakai (⋯) lalu `Delete` dan `[Delete]` dari TC `global-settings/user`. (4) TC-AUTH-MFA-217 langkah 8 "tunggu sampai button Resend aktif" tidak menyebut durasi atau cara; spec memakai cooldown 1 menit dari PRD yang dipenuhi dengan memajukan jam server uji dan jam browser uji 61 detik; mekanisme mengatur jam tidak didefinisikan di TC, PRD, atau LLD. (5) TC-AUTH-MFA-142 memakai kode "valid" Enrollment padahal user sudah dinonaktifkan; spec menuliskannya sebagai kode dari aplikasi authenticator uji sesuai TC. (6) Post Condition tanpa langkah observasi dan tanpa Expected padanan tidak diasersi di spec ini: TC-AUTH-MFA-138 "Sesi pre-auth MFA `Dwi Cahyono` di-invalidate"; TC-AUTH-MFA-139, 140, 141, 142, dan 217 "Sesi pre-auth MFA ... di-invalidate; tidak ada entri log" (sesi pre-auth teramati sebagai halaman Login with Password tampil). QA dapat menambah Expected atau langkah observasi di TC bila perlu. (7) Post "tidak ada entri log" TC-AUTH-MFA-139, 140, 141, 142, dan 217 tidak diasersi di spec mana pun (spec 035 tidak memuatnya); hanya TC-AUTH-MFA-138 yang punya Expected untuk itu dan diasersi di sini (`P-1`). (8) TC-AUTH-MFA-142 Expected b ("Enrollment Authenticator tidak aktif") tidak punya cara cek di Langkah Uji; spec mengasersinya lewat pembacaan status enrollment oleh sisi BE (langkah 92; Prerequisites) dan Langkah Uji TC-AUTH-MFA-142 tidak punya langkah observasi untuk itu. (9) Mekanisme seeding state BE per user (trusted device ber-ID device, lokasi dan waktu login terakhir, authenticator terdaftar dengan secret yang dikenal authenticator uji, penanda belum pernah login) belum ada di Pre-setup (#20/#21) TC; spec tidak menyebut endpoint.
