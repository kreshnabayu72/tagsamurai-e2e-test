---
id: TC-AUTH-MFA-E2E-029-ttl-sesi-pre-auth-10-menit
title: "TTL Sesi Pre-auth MFA 10 Menit"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AUTH-MFA-125
  - TC-AUTH-MFA-126
  - TC-AUTH-MFA-127
  - TC-AUTH-MFA-128
  - TC-AUTH-MFA-212
  - TC-AUTH-MFA-213
coverage:
  web: automated
---

# TTL Sesi Pre-auth MFA 10 Menit

## Prerequisites

- Mode: FE+BE.
- Suite berjalan serial (`parallel: false`) karena spec ini mengubah jam server uji, jam browser uji (klien), dan jam aplikasi authenticator uji; hook `after` memulihkan ketiganya ke waktu nyata dan melepas pembekuan jam server.
- Seeding (hook `before`, lewat API oleh akun aktor Total Control (Global Settings) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.GS_TC_PASSWORD`): enam user Activated, Active ON, password `Spectra.env.MFA_PASSWORD`, email bersuffix per run. Kondisi BE yang di-seed per profil:
  - Profil NEWDEV (Tabel Data Uji Pre-setup #4): seperti BASE, yaitu sudah pernah login sukses di web dari browser uji A (ID device browser uji A tercatat sebagai trusted device), login terakhir dari IP uji Jakarta (ID), logout web terakhir kurang dari 30 hari; Authenticator belum terdaftar. Login dilakukan dari browser uji B (ID device belum ada di daftar trusted device) sehingga MFA terpicu.
  - Profil NEWDEVE (Tabel Data Uji Pre-setup #5): seperti NEWDEV tetapi Authenticator sudah terdaftar (secret TOTP dipegang aplikasi authenticator uji).
  - Profil FIRST (Tabel Data Uji Pre-setup #3): belum pernah menyelesaikan login di platform mana pun; Authenticator belum terdaftar.
  - TC-AUTH-MFA-125: `Putra Kencana` (`putrakencana+{runId}-029@qwertysystem.net`), NEWDEVE
  - TC-AUTH-MFA-126: `Queen Anggun` (`queenanggun+{runId}-029@qwertysystem.net`), NEWDEV
  - TC-AUTH-MFA-127: `Rendi Pratama` (`rendipratama+{runId}-029@qwertysystem.net`), NEWDEV
  - TC-AUTH-MFA-128: `Santi Maulina` (`santimaulina+{runId}-029@qwertysystem.net`), FIRST
  - TC-AUTH-MFA-212: `Sinta Larasati` (`sintalarasati+{runId}-029@qwertysystem.net`), NEWDEVE
  - TC-AUTH-MFA-213: `Teddy Gunawan` (`teddygunawan+{runId}-029@qwertysystem.net`), NEWDEVE
- Hook `after`: lepas pembekuan jam server uji, kembalikan jam server uji, jam browser uji, dan jam aplikasi authenticator uji ke waktu nyata, lalu hapus keenam user. Hook ini tetap jalan walau spec gagal di tengah dan tidak berasumsi seeding berhasil penuh. Tiap TC juga memulihkan jam di langkah terakhirnya; hook `after` hanya cadangan.
- Akun yang dipakai: tanpa login (halaman publik; tidak ada sesi aktif di browser) untuk semua TC. Browser uji B = jendela privat baru (ID device belum dikenali) untuk semua TC kecuali TC-AUTH-MFA-128 yang memakai browser uji A (profil browser reguler dengan ID device persisten).
- Environment variable: `GS_TC_PASSWORD`, `MFA_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Kemampuan teknis (kelas harness d: time-travel):
  - Seeding state BE per user: trusted device ber-ID device browser uji A (NEWDEV, NEWDEVE), lokasi dan waktu login terakhir Jakarta, logout web terakhir kurang dari 30 hari, Authenticator terdaftar dengan secret yang dikenal aplikasi authenticator uji (NEWDEVE), belum pernah login dan persetujuan Privacy Policy belum ada (FIRST); mekanisme seeding (endpoint/skrip uji) disediakan tim FE/BE karena tidak didefinisikan di TC, PRD, atau LLD.
  - Jam server uji dapat dimajukan dengan presisi detik (hanya maju), dapat dibekukan pada waktu tertentu (jam tidak berjalan), dan dapat diset ke waktu absolut di depan waktu beku. Pembekuan dan pengaturan absolut dipakai untuk batas eksak TC-AUTH-MFA-212 dan 213.
  - Jam browser uji (klien) dapat dimajukan bersama jam server uji (TC-AUTH-MFA-127: hitung mundur cooldown Resend berjalan di jam klien, sehingga memajukan jam server saja tidak mengaktifkan button Text [Resend code]). TC lain menghitung umur sesi pre-auth murni di server dan tidak mengamatinya lewat UI, sehingga cukup jam server.
  - Jam aplikasi authenticator uji (TOTP: SHA-1, 6 digit, periode 30 detik) dapat disamakan dengan jam server uji sehingga kode TOTP valid pada waktu server yang digeser; aplikasi authenticator uji dapat memindai QR code Enrollment (TC-AUTH-MFA-128).
  - Mail-catcher lingkungan uji untuk membaca email OTP faktor-2 dan jumlah email per alamat tujuan (TC-AUTH-MFA-126, 127). Asersi "tidak ada email baru" memakai baseline jumlah email sebelum aksi.
  - Pembacaan status enrollment Authenticator user oleh sisi BE (TC-AUTH-MFA-128, langkah 65; disediakan tim FE/BE karena tidak ada cara cek di UI atau di Langkah Uji TC; endpoint/skrip tidak didefinisikan di TC, PRD, atau LLD).
  - Jendela privat dan browser uji A; reCAPTCHA mode uji di environment.
- State global yang diubah: jam server uji, jam browser uji (TC-AUTH-MFA-127), dan jam aplikasi authenticator uji. Pemulihan di langkah terakhir tiap TC dan di hook `after`.
- Jeda nyata: tidak ada; semua penantian waktu dipenuhi dengan mengatur jam.
- Titik waktu: "faktor-1 lolos" = saat klik [Log in] di halaman Login with Password berhasil dan sesi pre-auth dibuat; tiap TC mengukur usia sesi pre-auth dari titik itu pada TC-nya sendiri. Pada TC-AUTH-MFA-212 dan 213, jam server dibekukan pada waktu T0 sebelum klik [Log in], sehingga faktor-1 lolos tepat pada T0.

## Test Steps

### TC-AUTH-MFA-125: Sesi pre-auth yang habis (10 menit) mengalihkan ke halaman login pada aksi berikutnya

1. Buka halaman `Auth > Login with Password` di browser uji B → halaman Login with Password tampil
2. Ketik `putrakencana+{runId}-029@qwertysystem.net` pada field Email
3. Ketik `Spectra.env.MFA_PASSWORD` pada field Password
4. Centang widget reCAPTCHA "I'm not a robot"
5. Klik button [Log in] → halaman `Auth > MFA > Choose Verification Method` tampil
6. Pilih opsi "Authenticator app" pada halaman Choose Verification Method
7. Klik button [Login] → halaman `Auth > MFA > Authenticator Verification` tampil
8. Majukan jam server uji sehingga 10 menit 30 detik berlalu sejak faktor-1 lolos
9. Samakan jam aplikasi authenticator uji dengan jam server uji
10. Ketik 6 digit kode TOTP valid dari aplikasi authenticator uji untuk `putrakencana+{runId}-029@qwertysystem.net` pada kotak digit
11. Klik button [Login]
12. Verifikasi Halaman Login with Password tampil (user harus login ulang dari faktor-1)
13. Verifikasi Tidak ada caption pada halaman login
14. Verifikasi Tidak ada sesi penuh yang dibuat untuk `Putra Kencana`
15. Verifikasi Tidak ada toast, caption, atau pesan lain yang menyertai pengalihan
16. Pulihkan jam server uji dan jam aplikasi authenticator uji ke waktu nyata

### TC-AUTH-MFA-126: Sesi pre-auth habis saat memilih OTP via email mengalihkan ke halaman login tanpa kirim email

17. Tutup jendela user uji dari TC sebelumnya dan hapus sesi login browser terkait (ID device dan jendela sesi akun aktor tetap), lalu buka jendela privat baru (tanpa sesi login)
18. Buka halaman `Auth > Login with Password` di browser uji B → halaman Login with Password tampil
19. Ketik `queenanggun+{runId}-029@qwertysystem.net` pada field Email
20. Ketik `Spectra.env.MFA_PASSWORD` pada field Password
21. Centang widget reCAPTCHA "I'm not a robot"
22. Klik button [Log in] → halaman `Auth > MFA > Choose Verification Method` tampil
23. Catat jumlah email di mail-catcher untuk `queenanggun+{runId}-029@qwertysystem.net` (baseline sesudah faktor-1 lolos, sebelum memilih OTP via email)
24. Majukan jam server uji sehingga 10 menit 30 detik berlalu sejak faktor-1 lolos
25. Pilih opsi "OTP via email" lalu klik button [Login]
26. Verifikasi Halaman Login with Password tampil
27. Verifikasi Tidak ada caption pada halaman login
28. Periksa mail-catcher lingkungan uji untuk `queenanggun+{runId}-029@qwertysystem.net`
29. Verifikasi Tidak ada email OTP faktor-2 baru di mail-catcher `queenanggun+{runId}-029@qwertysystem.net` dibanding baseline langkah 23
30. Pulihkan jam server uji ke waktu nyata

### TC-AUTH-MFA-127: TTL sesi pre-auth bersifat absolut: Resend dan ganti metode tidak memperpanjangnya

31. Tutup jendela user uji dari TC sebelumnya dan hapus sesi login browser terkait (ID device dan jendela sesi akun aktor tetap), lalu buka jendela privat baru (tanpa sesi login)
32. Buka halaman `Auth > Login with Password` di browser uji B → halaman Login with Password tampil
33. Ketik `rendipratama+{runId}-029@qwertysystem.net` pada field Email
34. Ketik `Spectra.env.MFA_PASSWORD` pada field Password
35. Centang widget reCAPTCHA "I'm not a robot"
36. Klik button [Log in] → halaman `Auth > MFA > Choose Verification Method` tampil
37. Pilih opsi "OTP via email" pada halaman Choose Verification Method
38. Klik button [Login] → halaman `Auth > MFA > OTP Verification` tampil dan email OTP faktor-2 terkirim ke `rendipratama+{runId}-029@qwertysystem.net`
39. Majukan jam server uji dan jam browser uji bersama 4 menit (4 menit sejak faktor-1 lolos)
40. Klik button Text [Use a different method] → halaman Choose Verification Method tampil
41. Pilih opsi "OTP via email", lalu klik button [Login] → halaman OTP Verification tampil
42. Majukan jam server uji dan jam browser uji bersama 4 menit lagi (8 menit sejak faktor-1 lolos) sehingga hitung mundur cooldown 1 menit selesai dan button Text [Resend code] aktif
43. Klik button Text [Resend code]
44. Majukan jam server uji dan jam browser uji bersama sampai 10 menit 30 detik sejak faktor-1 lolos
45. Ketik 6 digit kode OTP faktor-2 terbaru dari email `rendipratama+{runId}-029@qwertysystem.net` (dibaca dari mail-catcher) pada kotak digit
46. Verifikasi Aksi ditolak (TTL tidak diperpanjang oleh pindah metode maupun Resend; sesi habis pada menit ke-10 sejak faktor-1 lolos)
47. Verifikasi Halaman Login with Password tampil
48. Verifikasi Tidak ada sesi penuh yang dibuat untuk `Rendi Pratama`
49. Pulihkan jam server uji dan jam browser uji ke waktu nyata

### TC-AUTH-MFA-128: Enrollment tidak memperpanjang TTL sesi pre-auth dan sesi habis saat enrollment membuang progres

50. Tutup jendela user uji dari TC sebelumnya dan hapus sesi login browser terkait (ID device dan jendela sesi akun aktor tetap), lalu buka jendela baru di browser uji A (tanpa sesi login)
51. Buka halaman `Auth > Login with Password` di browser uji A → halaman Login with Password tampil
52. Ketik `santimaulina+{runId}-029@qwertysystem.net` pada field Email
53. Ketik `Spectra.env.MFA_PASSWORD` pada field Password
54. Centang widget reCAPTCHA "I'm not a robot"
55. Klik button [Log in] → layar Confirm to Continue tampil
56. Centang checkbox persetujuan, lalu klik [Continue ➔] → halaman `Auth > MFA > Choose Verification Method` tampil
57. Pilih opsi "Authenticator app" pada halaman Choose Verification Method
58. Klik button [Login] → halaman `Auth > MFA > Enrollment Authenticator` tampil
59. Pindai QR code dengan aplikasi authenticator uji
60. Majukan jam server uji sehingga 10 menit 30 detik berlalu sejak faktor-1 lolos
61. Samakan jam aplikasi authenticator uji dengan jam server uji
62. Ketik 6 digit kode dari aplikasi authenticator uji pada kotak digit lalu klik button [Verify]
63. Verifikasi Halaman Login with Password tampil
64. Verifikasi Tidak ada sesi penuh yang dibuat untuk `Santi Maulina`
65. Verifikasi Enrollment Authenticator tidak aktif karena verifikasi ditolak (sesi habis)
66. Pulihkan jam server uji dan jam aplikasi authenticator uji ke waktu nyata

### TC-AUTH-MFA-212: Sesi pre-auth berumur 9 menit 59 detik masih berlaku (satu detik sebelum batas)

67. Tutup jendela user uji dari TC sebelumnya dan hapus sesi login browser terkait (ID device dan jendela sesi akun aktor tetap), lalu buka jendela privat baru (tanpa sesi login)
68. Buka halaman `Auth > Login with Password` di browser uji B → halaman Login with Password tampil
69. Ketik `sintalarasati+{runId}-029@qwertysystem.net` pada field Email
70. Ketik `Spectra.env.MFA_PASSWORD` pada field Password
71. Centang widget reCAPTCHA "I'm not a robot"
72. Bekukan jam server uji pada waktu T0 (jam server tidak berjalan sampai diatur ulang)
73. Klik button [Log in] → halaman `Auth > MFA > Choose Verification Method` tampil (faktor-1 lolos tepat pada T0)
74. Pilih opsi "Authenticator app" pada halaman Choose Verification Method
75. Klik button [Login] → halaman `Auth > MFA > Authenticator Verification` tampil
76. Atur jam server uji (tetap beku) ke waktu absolut T0 + 9 menit 59 detik
77. Samakan jam aplikasi authenticator uji dengan jam server uji
78. Ketik 6 digit kode TOTP valid dari aplikasi authenticator uji untuk `sintalarasati+{runId}-029@qwertysystem.net` pada kotak digit
79. Klik button [Login]
80. Verifikasi Faktor-2 berhasil (sesi pre-auth valid selama kurang dari 10 menit)
81. Verifikasi Browser dialihkan ke Portal — Product Hub
82. Verifikasi Satu sesi web aktif untuk `Sinta Larasati`
83. Lepas pembekuan jam server uji, lalu pulihkan jam server uji dan jam aplikasi authenticator uji ke waktu nyata

### TC-AUTH-MFA-213: Sesi pre-auth berumur tepat 10 menit 00 detik sudah tidak berlaku (batas eksklusif)

84. Tutup jendela user uji dari TC sebelumnya dan hapus sesi login browser terkait (ID device dan jendela sesi akun aktor tetap), lalu buka jendela privat baru (tanpa sesi login)
85. Buka halaman `Auth > Login with Password` di browser uji B → halaman Login with Password tampil
86. Ketik `teddygunawan+{runId}-029@qwertysystem.net` pada field Email
87. Ketik `Spectra.env.MFA_PASSWORD` pada field Password
88. Centang widget reCAPTCHA "I'm not a robot"
89. Bekukan jam server uji pada waktu T0 (jam server tidak berjalan sampai diatur ulang)
90. Klik button [Log in] → halaman `Auth > MFA > Choose Verification Method` tampil (faktor-1 lolos tepat pada T0)
91. Pilih opsi "Authenticator app" pada halaman Choose Verification Method
92. Klik button [Login] → halaman `Auth > MFA > Authenticator Verification` tampil
93. Atur jam server uji (tetap beku) ke waktu absolut T0 + 10 menit 00 detik
94. Samakan jam aplikasi authenticator uji dengan jam server uji
95. Ketik 6 digit kode TOTP valid dari aplikasi authenticator uji untuk `teddygunawan+{runId}-029@qwertysystem.net` pada kotak digit
96. Klik button [Login]
97. Verifikasi Halaman Login with Password tampil (user harus login ulang dari faktor-1)
98. Verifikasi Tidak ada caption pada halaman login
99. Verifikasi Tidak ada sesi penuh yang dibuat untuk `Teddy Gunawan`
100. Verifikasi Tidak ada toast, caption, atau pesan lain yang menyertai pengalihan
101. Lepas pembekuan jam server uji, lalu pulihkan jam server uji dan jam aplikasi authenticator uji ke waktu nyata

## Notes

- Sumber: `auth/mfa/TestCases/tc-mfa.md`. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. Kelas harness d (time-travel).
- Langkah pembuka tiap TC sesudah TC pertama menutup jendela user uji dari TC sebelumnya dan menghapus sesi login browser terkait (ID device dan jendela sesi akun aktor tetap) sebelum jendela baru dibuka; itu langkah penghubung tanpa `Verifikasi` (S-03, S-09).
- Pengaturan jam (konvensi bagian 6): umur sesi pre-auth dihitung murni di server dan tidak diamati lewat UI, sehingga TC-AUTH-MFA-125, 126, 128, 212, dan 213 cukup mengatur jam server uji (jam aplikasi authenticator uji disamakan untuk kode TOTP). TC-AUTH-MFA-127 mengamati hitung mundur cooldown Resend di UI yang berjalan di jam klien, sehingga jam server dan jam browser uji dimajukan bersama pada seluruh TC itu. Batas eksak TC-AUTH-MFA-212 (9 menit 59 detik) dan 213 (10 menit 00 detik) memakai jam server yang dibekukan pada T0 sebelum klik [Log in] lalu diatur absolut ke T0 + 9:59 atau T0 + 10:00, bukan digeser relatif, supaya detik nyata antara klik [Log in] dan klik [Login] faktor-2 tidak mengubah usia sesi.
- Pemulihan jam: langkah 16, 30, 49, 66, 83, dan 101 memulihkan jam (aksi tanpa `Verifikasi`) di akhir tiap TC, sehingga jam yang digeser satu TC tidak terbawa ke TC berikutnya. Hook `after` menjadi cadangan.
- TC sumber TC-AUTH-MFA-125, 126, 127, dan 128 menulis "Tunggu 10 menit 30 detik" (dan "Tunggu 4 menit" pada 127); spec menuliskannya sebagai "Majukan jam server uji" supaya satu mekanisme waktu dipakai di seluruh spec (konsisten dengan TC-AUTH-MFA-212 dan 213). Pada TC-AUTH-MFA-127 hitung mundur cooldown Resend 1 menit dipenuhi dengan memajukan jam server dan jam browser bersama, bukan menunggu nyata.
- Langkah penghubung tanpa awalan `Verifikasi` (buka jendela baru di awal tiap TC; samakan jam aplikasi authenticator uji dengan jam server uji; periksa mail-catcher; catat baseline email; bekukan, atur, dan pulihkan jam) bukan asersi tambahan (S-03).
- Baseline email (S-12): langkah 23 mencatat jumlah email setelah faktor-1 lolos (email alert device baru sudah masuk hitungan); asersi langkah 29 hanya menghitung email OTP faktor-2 sesudah baseline itu.
- Post Condition "Sesi pre-auth MFA tidak berlaku" (TC-AUTH-MFA-125, 127, 213) tidak diasersi terpisah: sesi pre-auth yang habis teramati sebagai halaman Login with Password tampil (langkah 12, 47, 97), yang sudah menjadi Expected.
- Urutan mengikuti TC sumber; tiap TC memakai user sendiri sehingga tidak saling bergantung.
- Melewati ±35 langkah (±65 netto setelah langkah prefix login faktor-1 tidak dihitung) karena enam TC time-travel yang berdiri sendiri; tiap TC memakai user dan konteks browser sendiri serta memulihkan jam di akhir TC-nya, sehingga bagian sesudahnya tetap bermakna walau bagian sebelumnya gagal dan spec tidak dipecah.
- Temuan untuk QA: (1) TC-AUTH-MFA-127 langkah 10 "klik [Resend code] jika aktif" bersyarat; spec memajukan jam server dan jam browser bersama sehingga cooldown pasti selesai dan tombol aktif. (2) TC-AUTH-MFA-127 langkah 11 tidak menyebut kode OTP mana yang diketik setelah Resend dan tidak menyebut klik [Login]; spec memakai kode terbaru dari email dan hanya mengetik (langkah 45), sedangkan TC-AUTH-MFA-125 langkah 10 dan 212/213 langkah 10 menyebut klik [Login] secara eksplisit. (3) TC-AUTH-MFA-125, 128, 212, dan 213 memakai kode TOTP pada waktu server yang digeser, tetapi TC tidak menyebut sinkronisasi jam aplikasi authenticator uji; spec menambah langkah penghubung dan kebutuhannya dicatat di Prerequisites. (4) TC-AUTH-MFA-212 dan 213 memakai batas presisi detik tetapi TC hanya menulis "Majukan jam server sehingga ... berlalu sejak faktor-1 lolos"; spec membekukan jam server pada T0 sebelum klik [Log in] dan mengaturnya absolut. (5) Post Condition "Tidak ada entri log (bukan upaya autentikasi)" pada TC-AUTH-MFA-125, 126, 128, dan 213 tidak punya langkah observasi di TC dan tidak diasersi di spec ini; spec `TC-AUTH-MFA-E2E-035-absence-pencatatan-log` tidak memuat TC-AUTH-MFA-125, 126, 128, dan 213 sehingga belum ada spec yang mengasersinya; QA perlu menambah Expected atau TC absence, atau menghapus Post Condition itu. (6) Mekanisme seeding state BE profil NEWDEV, NEWDEVE, dan FIRST (trusted device ber-ID device, lokasi login terakhir, secret Authenticator yang dikenal authenticator uji) belum ada di Pre-setup TC (#20/#21 hanya memuat sebagian) dan tidak didefinisikan di PRD atau LLD; spec tidak menyebut endpoint seeding. (7) TC-AUTH-MFA-128 Expected b ("Enrollment Authenticator tidak aktif") tidak punya cara cek di UI dan Langkah Uji TC tidak memberi cara cek status enrollment; spec memakai kemampuan pembacaan status enrollment oleh sisi BE (langkah 65) yang disediakan tim FE/BE tanpa endpoint karangan; QA perlu menambah langkah observasi di TC atau menyatakan cara cek lain.
