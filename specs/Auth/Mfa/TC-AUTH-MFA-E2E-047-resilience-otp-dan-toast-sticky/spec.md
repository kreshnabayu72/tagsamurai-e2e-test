---
id: TC-AUTH-MFA-E2E-047-resilience-otp-dan-toast-sticky
title: "Resilience Kegagalan Server pada Login, OTP, dan Authenticator serta Toast Error Sticky"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AUTH-MFA-83
  - TC-AUTH-MFA-84
  - TC-AUTH-MFA-198
  - TC-AUTH-MFA-199
  - TC-AUTH-MFA-200
  - TC-AUTH-MFA-201
coverage:
  web: automated
---

# Resilience Kegagalan Server pada Login, OTP, dan Authenticator serta Toast Error Sticky

## Prerequisites

- Mode: FE+BE (backend nyata; sebagian respons dipaksa lewat `Spectra.intercept()`, bukan seluruh API di-mock).
- Suite berjalan serial (`parallel: false`) karena spec ini mengubah jam server uji dan jam browser uji; hook `after` memulihkan jam server uji dan jam browser uji ke waktu nyata.
- Seeding (hook `before`, lewat API oleh akun aktor Total Control (Global Settings) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.GS_TC_PASSWORD`), password user `Spectra.env.MFA_PASSWORD`, email bersuffix per run:
  - TC-AUTH-MFA-83: `Nabila Zahra` (`nabilazahra+{runId}-047@qwertysystem.net`), profil NEWDEV (Tabel Data Uji Pre-setup #4: Activated, Active ON, device browser uji B belum ada di daftar trusted device, Authenticator belum terdaftar).
  - TC-AUTH-MFA-84: `Oky Febrianto` (`okyfebrianto+{runId}-047@qwertysystem.net`), profil NEWDEV.
  - TC-AUTH-MFA-198: `Fajar Rahmawati` (`fajarrahmawati+{runId}-047@qwertysystem.net`), profil NEWDEV.
  - TC-AUTH-MFA-199: `Ratna Rahmawati` (`ratnarahmawati+{runId}-047@qwertysystem.net`), profil NEWDEV.
  - TC-AUTH-MFA-200: `Dimas Rahmawati` (`dimasrahmawati+{runId}-047@qwertysystem.net`), profil NEWDEV.
  - TC-AUTH-MFA-201: `Maya Rahmawati` (`mayarahmawati+{runId}-047@qwertysystem.net`), profil NEWDEVE (Tabel Data Uji Pre-setup #5: seperti NEWDEV, Authenticator sudah terdaftar dengan secret yang dikenali aplikasi authenticator uji).
- Hook `after`: lepas semua aturan intercept yang masih aktif, pulihkan jam server uji dan jam browser uji ke waktu nyata, lalu hapus keenam user. Hook ini tetap jalan walau spec gagal di tengah dan pembersihan tidak berasumsi seeding berhasil penuh.
- Akun yang dipakai: tanpa login (halaman publik; tidak ada sesi aktif di browser) untuk keenam TC. Tiap TC dimulai di jendela privat baru (browser uji B, ID device belum dikenali).
- Environment variable: `GS_TC_PASSWORD`, `MFA_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Kemampuan teknis:
  - `Spectra.intercept()` parsial atas backend nyata. Respons HTTP 500 menggantikan respons backend (request tidak diteruskan ke backend) untuk: `POST /v2/iam/auth/mfa/otp/send` (TC-AUTH-MFA-83 pengiriman awal dan TC-AUTH-MFA-84 Resend), `POST /v2/iam/auth/login` (request faktor-1 yang mengevaluasi MFA, TC-AUTH-MFA-198), `POST /v2/iam/auth/mfa/otp/verify` (TC-AUTH-MFA-199), dan `POST /v2/iam/auth/mfa/authenticator/verify` (TC-AUTH-MFA-201). Untuk TC-AUTH-MFA-200, request `POST /v2/iam/auth/mfa/otp/send` ditahan tanpa respons sampai melewati batas timeout klien (tidak diteruskan ke backend). Nama endpoint `otp/send`, `otp/verify`, dan `authenticator/verify` dari `auth/mfa/API/openapi.yaml`; nama endpoint `POST /v2/iam/auth/login` dari `auth/login-password/API/openapi.yaml`.
  - Pengaturan jam: jam server uji dan jam browser uji (klien) dimajukan bersama N detik, lalu dipulihkan ke waktu nyata. Keduanya diatur bersama karena hitung mundur Resend 60 detik berjalan di jam klien dan cooldown dihitung server. Dipakai untuk TC-AUTH-MFA-84 dan TC-AUTH-MFA-200 (menggantikan menunggu hitung mundur 60 detik). Mekanisme pengaturan jam disediakan tim FE/BE karena tidak didefinisikan di TC, PRD, atau LLD.
  - Mail-catcher lingkungan uji untuk membaca email OTP faktor-2 dan menghitung jumlahnya (baseline jumlah email sebelum aksi; TC-AUTH-MFA-83 dan TC-AUTH-MFA-200).
  - Seeding state BE per user: profil NEWDEV tanpa ID device browser uji B di daftar trusted device (TC-AUTH-MFA-83, 84, 198, 199, 200) dan profil NEWDEVE dengan Authenticator terdaftar dengan secret yang dikenal aplikasi authenticator uji (TC-AUTH-MFA-201); mekanisme seeding (endpoint/skrip uji) disediakan tim FE/BE karena tidak didefinisikan di TC, PRD, atau LLD.
  - Aplikasi authenticator uji (TOTP: SHA-1, 6 digit, periode 30 detik) untuk kode TOTP valid (TC-AUTH-MFA-201).
  - Pengamatan toast selama 10 detik dan dismiss toast manual lewat tombol tutup toast.
  - Jeda nyata: pengamatan toast 10 detik (TC-AUTH-MFA-83, 84, 198, 199, 201) dan penahanan request Resend sampai timeout klien (TC-AUTH-MFA-200; durasi timeout klien belum didefinisikan di TC, lihat Temuan untuk QA).
  - reCAPTCHA mode uji di environment.
- Pemulihan state global: aturan intercept dilepas di hook `after` (dan dilepas pada langkah tiap TC yang memintanya). Jam server uji dan jam browser uji dipulihkan pada langkah terakhir TC-AUTH-MFA-84 dan TC-AUTH-MFA-200, dan di hook `after`. Spec tidak mengubah geo-IP, email service, atau counter rate limit.

## Test Steps

### TC-AUTH-MFA-83: Pengiriman awal OTP gagal 5xx dari Choose Verification Method

1. Buka halaman `Auth > Login with Password` di browser → halaman Login with Password tampil
2. Ketik `nabilazahra+{runId}-047@qwertysystem.net` pada field Email
3. Ketik `Spectra.env.MFA_PASSWORD` pada field Password
4. Centang widget reCAPTCHA "I'm not a robot"
5. Klik button [Log in] → halaman `Auth > MFA > Choose Verification Method` tampil
6. Pilih opsi "OTP via email" pada halaman Choose Verification Method
7. Catat jumlah email OTP di mail-catcher `nabilazahra+{runId}-047@qwertysystem.net` sebagai baseline sebelum aksi
8. Aktifkan intercept respons 5xx pada pengiriman OTP (`POST /v2/iam/auth/mfa/otp/send`), lalu klik button [Login]
9. Verifikasi Toast error: "Error, failed to send the code." tampil
10. Verifikasi Toast tampil di kanan bawah
11. Amati toast selama 10 detik
12. Verifikasi Toast tetap tampil dan tidak hilang otomatis sampai di-dismiss
13. Verifikasi Halaman tetap Choose Verification Method
14. Verifikasi Tidak ada email OTP terkirim ke `nabilazahra+{runId}-047@qwertysystem.net` di mail-catcher (jumlah email OTP sama dengan baseline)
15. Dismiss toast manual
16. Hentikan intercept 5xx dan klik button [Login] lagi
17. Verifikasi Halaman `Auth > MFA > OTP Verification` tampil
18. Verifikasi Email OTP terkirim ke `nabilazahra+{runId}-047@qwertysystem.net` (jumlah email OTP bertambah satu dari baseline)

### TC-AUTH-MFA-84: Resend OTP gagal 5xx

19. Tutup jendela user uji dari TC sebelumnya dan hapus sesi login browser terkait (ID device dan jendela sesi akun aktor tetap), lalu buka jendela privat baru (tanpa sesi login)
20. Buka halaman `Auth > Login with Password` di browser → halaman Login with Password tampil
21. Ketik `okyfebrianto+{runId}-047@qwertysystem.net` pada field Email
22. Ketik `Spectra.env.MFA_PASSWORD` pada field Password
23. Centang widget reCAPTCHA "I'm not a robot"
24. Klik button [Log in] → halaman `Auth > MFA > Choose Verification Method` tampil
25. Pilih opsi "OTP via email" pada halaman Choose Verification Method
26. Klik button [Login] → halaman `Auth > MFA > OTP Verification` tampil dan email OTP faktor-2 terkirim ke `okyfebrianto+{runId}-047@qwertysystem.net`
27. Majukan jam server uji dan jam browser uji 60 detik → hitung mundur Resend selesai
28. Aktifkan intercept respons 5xx pada Resend (`POST /v2/iam/auth/mfa/otp/send`), lalu klik button [Resend code]
29. Verifikasi Halaman tetap OTP Verification
30. Verifikasi Toast error: "Error, failed to send the code." tampil
31. Verifikasi Toast tampil di kanan bawah
32. Amati toast selama 10 detik
33. Verifikasi Toast tetap tampil dan tidak hilang otomatis sampai di-dismiss
34. Dismiss toast manual dan hentikan intercept 5xx
35. Ketik 6 digit kode OTP pertama dari email pada kotak digit → Portal — Product Hub tampil
36. Verifikasi Kode OTP pertama tetap berlaku (belum expired): login berhasil dengan kode pertama
37. Pulihkan jam server uji dan jam browser uji ke waktu nyata

### TC-AUTH-MFA-198: Evaluasi MFA gagal 5xx saat login: toast error dan retry manual tanpa perubahan keputusan

38. Tutup jendela user uji dari TC sebelumnya dan hapus sesi login browser terkait (ID device dan jendela sesi akun aktor tetap), lalu buka jendela privat baru (tanpa sesi login)
39. Buka halaman `Auth > Login with Password` di browser → halaman Login with Password tampil
40. Ketik `fajarrahmawati+{runId}-047@qwertysystem.net` pada field Email
41. Ketik `Spectra.env.MFA_PASSWORD` pada field Password
42. Centang widget reCAPTCHA "I'm not a robot"
43. Aktifkan intercept respons 5xx pada request faktor-1 yang mengevaluasi MFA (`POST /v2/iam/auth/login`), lalu klik button [Log in]
44. Verifikasi Toast error: "Error, failed to log in." tampil
45. Verifikasi Toast tampil di kanan bawah
46. Amati toast selama 10 detik
47. Verifikasi Toast tetap tampil dan tidak hilang otomatis sampai di-dismiss
48. Verifikasi Halaman tetap Login with Password
49. Verifikasi Tidak ada sesi pre-auth MFA yang tampil (halaman MFA tidak tampil)
50. Dismiss toast manual
51. Hentikan intercept 5xx dan klik button [Log in] lagi
52. Verifikasi Halaman `Auth > MFA > Choose Verification Method` tampil (keputusan MFA tidak berubah)

### TC-AUTH-MFA-199: Verifikasi OTP faktor-2 gagal 5xx lalu retry berhasil tanpa efek ganda

53. Tutup jendela user uji dari TC sebelumnya dan hapus sesi login browser terkait (ID device dan jendela sesi akun aktor tetap), lalu buka jendela privat baru (tanpa sesi login)
54. Buka halaman `Auth > Login with Password` di browser → halaman Login with Password tampil
55. Ketik `ratnarahmawati+{runId}-047@qwertysystem.net` pada field Email
56. Ketik `Spectra.env.MFA_PASSWORD` pada field Password
57. Centang widget reCAPTCHA "I'm not a robot"
58. Klik button [Log in] → halaman `Auth > MFA > Choose Verification Method` tampil
59. Pilih opsi "OTP via email" pada halaman Choose Verification Method
60. Klik button [Login] → halaman `Auth > MFA > OTP Verification` tampil dan email OTP faktor-2 terkirim ke `ratnarahmawati+{runId}-047@qwertysystem.net`
61. Aktifkan intercept respons 5xx pada verifikasi OTP (`POST /v2/iam/auth/mfa/otp/verify`), lalu ketik 6 digit kode OTP faktor-2 dari email pada kotak digit
62. Verifikasi Toast error: "Error, failed to log in." tampil
63. Verifikasi Toast tampil di kanan bawah
64. Amati toast selama 10 detik
65. Verifikasi Toast tetap tampil dan tidak hilang otomatis sampai di-dismiss
66. Verifikasi Halaman tetap OTP Verification
67. Verifikasi Tidak ada sesi yang dibuat (Portal — Product Hub tidak tampil)
68. Verifikasi Keenam kotak digit tetap terisi (digit dipertahankan)
69. Dismiss toast manual
70. Hentikan intercept 5xx dan klik button [Login] dengan kode yang sama
71. Verifikasi Verifikasi berhasil
72. Verifikasi Portal — Product Hub tampil
73. Verifikasi Kode OTP faktor-2 masih valid (belum terpakai): login berhasil dengan kode yang sama

### TC-AUTH-MFA-200: Retry setelah timeout pada Resend OTP dihitung sebagai resend baru dan kode lama tetap berlaku

74. Tutup jendela user uji dari TC sebelumnya dan hapus sesi login browser terkait (ID device dan jendela sesi akun aktor tetap), lalu buka jendela privat baru (tanpa sesi login)
75. Buka halaman `Auth > Login with Password` di browser → halaman Login with Password tampil
76. Ketik `dimasrahmawati+{runId}-047@qwertysystem.net` pada field Email
77. Ketik `Spectra.env.MFA_PASSWORD` pada field Password
78. Centang widget reCAPTCHA "I'm not a robot"
79. Klik button [Log in] → halaman `Auth > MFA > Choose Verification Method` tampil
80. Pilih opsi "OTP via email" pada halaman Choose Verification Method
81. Klik button [Login] → halaman `Auth > MFA > OTP Verification` tampil dan email OTP faktor-2 terkirim ke `dimasrahmawati+{runId}-047@qwertysystem.net`
82. Majukan jam server uji dan jam browser uji 60 detik → hitung mundur Resend selesai
83. Catat jumlah email OTP di mail-catcher `dimasrahmawati+{runId}-047@qwertysystem.net` sebagai baseline
84. Aktifkan intercept timeout pada request Resend (`POST /v2/iam/auth/mfa/otp/send` ditahan sampai timeout klien), lalu klik button [Resend code]
85. Verifikasi Toast error: "Error, failed to send the code." tampil setelah timeout
86. Verifikasi Kode OTP pertama tetap berlaku (belum expired): tidak ada email OTP baru di mail-catcher `dimasrahmawati+{runId}-047@qwertysystem.net` (jumlah email OTP sama dengan baseline)
87. Dismiss toast manual dan hentikan intercept timeout
88. Majukan jam server uji dan jam browser uji 60 detik → hitung mundur Resend selesai
89. Klik button [Resend code] lagi sampai berhasil
90. Verifikasi Toast sukses: "Success, the code has been sent." tampil
91. Verifikasi Email OTP kedua terkirim ke `dimasrahmawati+{runId}-047@qwertysystem.net` (resend baru yang diproses server; jumlah email OTP bertambah satu dari baseline)
92. Pulihkan jam server uji dan jam browser uji ke waktu nyata

### TC-AUTH-MFA-201: Toast error T-01 tidak hilang otomatis sampai di-dismiss manual

93. Tutup jendela user uji dari TC sebelumnya dan hapus sesi login browser terkait (ID device dan jendela sesi akun aktor tetap), lalu buka jendela privat baru (tanpa sesi login)
94. Buka halaman `Auth > Login with Password` di browser → halaman Login with Password tampil
95. Ketik `mayarahmawati+{runId}-047@qwertysystem.net` pada field Email
96. Ketik `Spectra.env.MFA_PASSWORD` pada field Password
97. Centang widget reCAPTCHA "I'm not a robot"
98. Klik button [Log in] → halaman `Auth > MFA > Choose Verification Method` tampil
99. Pilih opsi "Authenticator app" pada halaman Choose Verification Method
100. Klik button [Login] → halaman `Auth > MFA > Authenticator Verification` tampil
101. Ketik 6 digit kode TOTP valid dari aplikasi authenticator uji untuk `mayarahmawati+{runId}-047@qwertysystem.net` pada kotak digit
102. Aktifkan intercept respons 5xx pada verifikasi Authenticator (`POST /v2/iam/auth/mfa/authenticator/verify`), lalu klik button [Login]
103. Amati toast selama 10 detik
104. Verifikasi Toast error: "Error, failed to log in." tampil
105. Verifikasi Toast tampil di kanan bawah
106. Verifikasi Toast tetap tampil selama 10 detik
107. Dismiss toast manual
108. Verifikasi Toast hilang hanya setelah di-dismiss manual
109. Hentikan intercept 5xx

## Notes

- Sumber: `auth/mfa/TestCases/tc-mfa.md`. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Langkah pembuka tiap TC sesudah TC pertama menutup jendela user uji dari TC sebelumnya dan menghapus sesi login browser terkait (ID device dan jendela sesi akun aktor tetap) sebelum jendela baru dibuka; itu langkah penghubung tanpa `Verifikasi` (S-03, S-09).
- Langkah penghubung tanpa awalan `Verifikasi` (buka jendela privat baru di awal tiap TC setelah TC pertama, mengamati toast, dismiss toast, melepas intercept, mengetik kode OTP pertama pada TC-AUTH-MFA-84, mencatat baseline jumlah email OTP pada TC-AUTH-MFA-83 dan TC-AUTH-MFA-200) bukan asersi tambahan (S-03).
- Pengaturan jam menggantikan "Tunggu hitung mundur selesai" pada TC-AUTH-MFA-84 langkah 8 dan TC-AUTH-MFA-200 langkah 8 dan 10: jam server uji dan jam browser uji dimajukan bersama 60 detik (K§6). Langkah memulihkan jam (langkah 37 dan 92) adalah aksi tanpa `Verifikasi` (S-09); hook `after` menjadi cadangan.
- Langkah 91 (Email OTP kedua terkirim, jumlah email OTP bertambah satu dari baseline; TC-AUTH-MFA-200) adalah padanan Expected b TC-AUTH-MFA-200 ("dihitung sebagai resend baru terhadap batas 5×"): hitungan resend tidak terbaca langsung, sehingga dicek lewat jumlah email di mail-catcher, seperti TC-AUTH-MFA-85 dan TC-AUTH-MFA-214 di spec `TC-AUTH-MFA-E2E-042-defense-cooldown-resend-dan-non-numerik`.
- Jumlah langkah 109; langkah prefix login faktor-1 yang identik (langkah 1-5, 20-24, 39-42, 54-58, 75-79, 94-98) tidak dihitung sehingga ±80 langkah, melewati smell ±35. Keenam TC independen (user, intercept, dan pengaturan jam sendiri), bagian sesudahnya tetap bermakna bila TC sebelumnya gagal, dan satu spec menghemat login, hook, dan cleanup; pengaturan jam hanya melewati cooldown Resend sebagai prasyarat kegagalan yang diintercept, bukan objek asersi, sehingga spec tidak dipecah.
- Temuan untuk QA: (1) TC-AUTH-MFA-83, 84, 198, dan 199 menulis "tidak hilang otomatis sampai di-dismiss" tanpa durasi pengamatan; spec memakai 10 detik seperti TC-AUTH-MFA-201. (2) TC-AUTH-MFA-84 butir a "kode OTP pertama tetap berlaku" tidak punya cara pengecekan di Langkah Uji; spec memakai kode pertama untuk login di akhir TC. (3) TC-AUTH-MFA-200 butir a "kode OTP pertama tetap berlaku" tidak dapat dicek tanpa memakai kode (Resend berikutnya menggantikan kode pertama); spec memeriksa tidak adanya email OTP baru setelah timeout. (4) TC-AUTH-MFA-200 butir b "dihitung sebagai resend baru terhadap batas 5×" tidak punya cara membaca hitungan di Langkah Uji; spec memakai jumlah email di mail-catcher (langkah 91, bertambah satu dari baseline) sebagai padanan butir b dan tidak membaca hitungan terhadap batas 5×, sedangkan Post Condition hitungan resend tidak diasersi. (5) TC-AUTH-MFA-200 tidak menyebut apakah request yang timeout diteruskan ke backend; spec memakai penahanan tanpa diteruskan, selaras dengan butir a. (6) TC-AUTH-MFA-200 langkah 9 ("paksa timeout") tidak mendefinisikan nilai timeout klien; spec menahan request sampai timeout klien tercapai dengan jeda nyata yang durasinya belum diketahui. (7) TC-AUTH-MFA-198 Post Condition "Satu sesi pre-auth MFA aktif untuk `Fajar Rahmawati`; tidak ada email alert ganda" tidak punya Expected padanan atau langkah observasi di TC (jumlah pasti email alert juga tidak disebut) dan tidak diasersi. (8) TC-AUTH-MFA-199 Post Condition "Satu sesi web aktif untuk `Ratna Rahmawati`; Tepat satu entri Success login final; tidak ada entri Failed untuk 5xx" tidak punya langkah observasi di TC dan tidak diasersi; Precondition TC-AUTH-MFA-199 juga tidak mencantumkan akun Total Control untuk membaca log. (9) TC-AUTH-MFA-201 Post Condition "Tidak ada sesi yang dibuat" tidak punya Expected padanan atau langkah observasi di TC dan tidak diasersi. (10) TC-AUTH-MFA-83 Post Condition "Tidak ada entri log untuk kegagalan kirim", TC-AUTH-MFA-84 Post Condition "Tidak ada entri log untuk kegagalan Resend", dan TC-AUTH-MFA-199 Post Condition "tidak ada entri Failed untuk 5xx" tidak punya Expected padanan maupun langkah observasi di Langkah Uji, sehingga tidak diasersi dan spec tidak menambah langkah pembacaan log. (11) Mekanisme seeding state BE per user (profil NEWDEV/NEWDEVE: trusted device, Authenticator dengan secret dikenal) belum ada di Pre-setup TC (#20/#21).
