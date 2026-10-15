---
id: TC-AUTH-MFA-E2E-035-absence-pencatatan-log
title: "Tidak Ada Pencatatan Log untuk Aksi Non-Autentikasi pada MFA"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AUTH-MFA-168
  - TC-AUTH-MFA-169
  - TC-AUTH-MFA-170
  - TC-AUTH-MFA-171
  - TC-AUTH-MFA-207
  - TC-AUTH-MFA-151
  - TC-AUTH-MFA-48
coverage:
  web: automated
---

# Tidak Ada Pencatatan Log untuk Aksi Non-Autentikasi pada MFA

## Prerequisites

- Mode: FE+BE (TC-AUTH-MFA-171 memakai intercept parsial di atas backend nyata).
- Suite berjalan serial (`parallel: false`) karena spec ini mengubah jam server uji, jam browser uji, dan jam aplikasi authenticator uji (TC-AUTH-MFA-169 dan 170); hook `after` memulihkan ketiga jam itu ke waktu nyata dan melepas intercept respons 5xx (TC-AUTH-MFA-171).
- Principal `principalSettingsPrivacyPolicy_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup #22, kredensial `Spectra.env.AC_PRINCIPAL_PP_PASSWORD`) sudah mempublikasikan versi Privacy Policy di `Admin Console > Settings > Privacy Policy` sebagai prasyarat environment (profil POLICY, TC-AUTH-MFA-48). Hook `before` hanya memverifikasi (pembacaan lewat API oleh akun Principal) bahwa versi terbitan itu sudah ada sebelum seeding user; hook tidak mem-publish, mengubah, atau menghapus Privacy Policy. Bila versi terbitan belum ada, spec berhenti karena prasyarat environment tidak terpenuhi.
- Seeding (hook `before`, lewat API oleh akun aktor Total Control (Global Settings) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.GS_TC_PASSWORD`): tujuh user, password `Spectra.env.MFA_PASSWORD`, email bersuffix per run:
  - TC-AUTH-MFA-168: `Ario Bimantara` (`ariobimantara+{runId}-035@qwertysystem.net`), profil FIRST (Tabel Data Uji Pre-setup #3: Activated, Active ON, belum pernah menyelesaikan login di platform mana pun, Authenticator belum terdaftar)
  - TC-AUTH-MFA-169: `Bintang Safira` (`bintangsafira+{runId}-035@qwertysystem.net`), profil NEWDEV (Tabel Data Uji Pre-setup #4: Activated, Active ON, seperti BASE tetapi ID device browser uji B belum ada di daftar trusted device, Authenticator belum terdaftar)
  - TC-AUTH-MFA-207: `Lukman Hakim` (`lukmanhakim+{runId}-035@qwertysystem.net`), profil NEWDEV
  - TC-AUTH-MFA-171: `Dewa Putu` (`dewaputu+{runId}-035@qwertysystem.net`), profil NEWDEVE (Tabel Data Uji Pre-setup #5: seperti NEWDEV tetapi Authenticator sudah terdaftar; secret-nya dimuat ke aplikasi authenticator uji)
  - TC-AUTH-MFA-170: `Chandra Gunadi` (`chandragunadi+{runId}-035@qwertysystem.net`), profil NEWDEVE
  - TC-AUTH-MFA-48 (langkah 8, absence log saja): `Desi Natalia` (`desinatalia+{runId}-035@qwertysystem.net`), profil POLICY (Tabel Data Uji Pre-setup #12: seperti FIRST, tetapi Principal sudah mempublish versi Privacy Policy sehingga layar Confirm to Continue terpicu; state ini di-seed di hook `before`), browser uji A (belum pernah login)
  - TC-AUTH-MFA-151 (butir a saja): `Olivia Gunawan` (`oliviagunawan+{runId}-035@qwertysystem.net`), profil NEWDEVE
- Aktor observer log: akun aktor Total Control (Global Settings) di atas login di browser kedua pada hook `before` dan membaca `Global Settings > Activity Log > Session` serta `Global Settings > User > Detail > User Log`. Browser pertama dipakai sebagai user uji tanpa login (halaman publik). TC-AUTH-MFA-168 dan 48 memakai browser uji A (profil browser reguler dengan cookie ID device persisten, bukan jendela privat; jendela baru tanpa sesi login untuk user itu); TC lain dibuka di jendela privat baru tiap TC (browser uji B, ID device belum dikenali).
- Hook `after`: kembalikan jam server uji, jam browser uji, dan jam aplikasi authenticator uji ke waktu nyata, lepas intercept respons 5xx bila masih terpasang, hapus ketujuh user, dan tutup browser kedua. Versi Privacy Policy terbitan Principal tidak diubah atau dihapus oleh spec ini. Hook ini tetap jalan walau spec gagal di tengah dan tidak berasumsi seeding berhasil penuh.
- Environment variable: `GS_TC_PASSWORD`, `AC_PRINCIPAL_PP_PASSWORD`, `MFA_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Kemampuan teknis:
  - Dua sesi browser bersamaan.
  - Aplikasi authenticator uji (TOTP: SHA-1, 6 digit, periode 30 detik) dengan jam yang mengikuti jam server uji, dan kemampuan memindai QR code atau membaca secret enrollment dari halaman Enrollment Authenticator (TC-AUTH-MFA-168).
  - Jam server uji dan jam browser uji yang dapat dimajukan lalu dipulihkan bersama (TC-AUTH-MFA-169: hitung mundur Resend berjalan di jam browser; countdown 60 detik diganti pengaturan jam, bukan menunggu); jam server uji yang dapat dimajukan (TC-AUTH-MFA-170: TTL sesi pre-auth dihitung di server).
  - `Spectra.intercept()` untuk memaksa respons 5xx pada `POST /v2/iam/auth/mfa/authenticator/verify` (TC-AUTH-MFA-171, endpoint dari `auth/mfa/API/openapi.yaml`).
  - Seeding state BE per user: profil FIRST, NEWDEV, NEWDEVE, dan POLICY (login sukses sebelumnya dari browser uji A, lokasi dan waktu login terakhir, ID device browser uji B belum ada di daftar trusted device, Authenticator terdaftar dengan secret yang dikenal aplikasi authenticator uji, dan persetujuan Privacy Policy versi terbitan belum ada untuk profil POLICY); mekanisme seeding (endpoint/skrip uji) disediakan tim FE/BE karena tidak didefinisikan di TC, PRD, atau LLD.
  - reCAPTCHA mode uji di environment.

## Test Steps

### TC-AUTH-MFA-168: Aktivasi enrollment Authenticator tidak dicatat dan kegagalan kode enrollment tidak dicatat

1. Buka jendela baru browser uji A di browser pertama (tanpa sesi login untuk `Ario Bimantara`)
2. Buka halaman `Auth > Login with Password` di browser → halaman Login with Password tampil
3. Ketik `ariobimantara+{runId}-035@qwertysystem.net` pada field Email
4. Ketik `Spectra.env.MFA_PASSWORD` pada field Password
5. Centang widget reCAPTCHA "I'm not a robot"
6. Klik button [Log in] → layar Confirm to Continue tampil
7. Centang checkbox persetujuan, lalu klik [Continue ➔] → halaman `Auth > MFA > Choose Verification Method` tampil
8. Pilih opsi "Authenticator app" pada halaman Choose Verification Method
9. Klik button [Login] → halaman `Auth > MFA > Enrollment Authenticator` tampil
10. Ketik 6 digit kode salah `000000` lalu klik [Verify] (kegagalan enrollment)
11. Pindai QR code dengan aplikasi authenticator uji, ketik 6 digit kode benar dari aplikasi tersebut lalu klik [Verify] → Portal — Product Hub tampil
12. Pindah ke browser kedua (sesi Total Control Global Settings), buka `Global Settings > Activity Log > Session`, dan cari entri untuk `Ario Bimantara` yang dibuat sesudah langkah 1 dimulai
13. Verifikasi Hanya ada satu entri baru untuk `Ario Bimantara` pada `Global Settings > Activity Log > Session`: Status `Success`, Note `Login with password`
14. Verifikasi Tidak ada entri Failed untuk kode enrollment salah dan tidak ada entri untuk aktivasi atau enrollment Authenticator pada `Global Settings > Activity Log > Session`
15. Buka `Global Settings > User > Detail > User Log` untuk `Ario Bimantara` dan cari entri yang dibuat sesudah langkah 1 dimulai
16. Verifikasi Hanya ada satu entri baru pada `Global Settings > User > Detail > User Log`: Status `Success`, Note `Login with password`
17. Verifikasi Tidak ada entri Failed untuk kode enrollment salah dan tidak ada entri untuk aktivasi atau enrollment Authenticator pada `Global Settings > User > Detail > User Log`

### TC-AUTH-MFA-169: Resend OTP, pilih metode, email alert, dan hasil bukan upaya autentikasi tidak dicatat

18. Tutup jendela user uji dari TC sebelumnya dan hapus sesi login browser terkait (ID device dan jendela sesi akun aktor tetap), lalu pindah ke browser pertama dan buka jendela privat baru (tanpa sesi login)
19. Buka halaman `Auth > Login with Password` di browser → halaman Login with Password tampil
20. Ketik `bintangsafira+{runId}-035@qwertysystem.net` pada field Email
21. Ketik `Spectra.env.MFA_PASSWORD` pada field Password
22. Centang widget reCAPTCHA "I'm not a robot"
23. Klik button [Log in] → halaman `Auth > MFA > Choose Verification Method` tampil
24. Pilih opsi "OTP via email" pada halaman Choose Verification Method
25. Klik button [Login] → halaman `Auth > MFA > OTP Verification` tampil dan email OTP faktor-2 terkirim ke `bintangsafira+{runId}-035@qwertysystem.net`
26. Majukan jam server uji dan jam browser uji sebesar 60 detik → label button berubah dari "Resend code in Ns" menjadi "Resend code"
27. Klik button [Resend code]
28. Klik button Text [Use a different method] → halaman Choose Verification Method tampil
29. Pilih opsi "OTP via email", lalu klik button [Login]
30. Pulihkan jam server uji dan jam browser uji ke waktu nyata
31. Pindah ke browser kedua, buka `Global Settings > Activity Log > Session`, dan cari entri untuk `Bintang Safira` yang dibuat sesudah langkah 18 dimulai
32. Verifikasi Tidak ada entri baru untuk `Bintang Safira` pada `Global Settings > Activity Log > Session` (Resend OTP, pemilihan metode, dan email alert tidak dicatat)
33. Buka `Global Settings > User > Detail > User Log` untuk `Bintang Safira` dan cari entri yang dibuat sesudah langkah 18 dimulai
34. Verifikasi Tidak ada entri baru pada `Global Settings > User > Detail > User Log` untuk `Bintang Safira`

### TC-AUTH-MFA-171: Kegagalan 5xx saat verifikasi faktor-2 tidak dicatat dan tidak mengubah state

35. Tutup jendela user uji dari TC sebelumnya dan hapus sesi login browser terkait (ID device dan jendela sesi akun aktor tetap), lalu pindah ke browser pertama dan buka jendela privat baru (tanpa sesi login)
36. Buka halaman `Auth > Login with Password` di browser → halaman Login with Password tampil
37. Ketik `dewaputu+{runId}-035@qwertysystem.net` pada field Email
38. Ketik `Spectra.env.MFA_PASSWORD` pada field Password
39. Centang widget reCAPTCHA "I'm not a robot"
40. Klik button [Log in] → halaman `Auth > MFA > Choose Verification Method` tampil
41. Pilih opsi "Authenticator app" pada halaman Choose Verification Method
42. Klik button [Login] → halaman `Auth > MFA > Authenticator Verification` tampil
43. Ketik 6 digit kode TOTP valid dari aplikasi authenticator uji untuk `dewaputu+{runId}-035@qwertysystem.net` pada kotak digit
44. Pasang intercept yang memaksa respons 5xx pada `POST /v2/iam/auth/mfa/authenticator/verify`, lalu klik button [Login]
45. Verifikasi Toast error "Error, failed to log in." tampil
46. Verifikasi Tidak ada sesi yang dibuat (halaman tetap Authenticator Verification dan Portal — Product Hub tidak tampil)
47. Lepas intercept respons 5xx
48. Pindah ke browser kedua, buka `Global Settings > Activity Log > Session`, dan cari entri untuk `Dewa Putu` yang dibuat sesudah langkah 35 dimulai
49. Verifikasi Tidak ada entri baru untuk `Dewa Putu` pada `Global Settings > Activity Log > Session`
50. Buka `Global Settings > User > Detail > User Log` untuk `Dewa Putu` dan cari entri yang dibuat sesudah langkah 35 dimulai
51. Verifikasi Tidak ada entri baru untuk `Dewa Putu` pada `Global Settings > User > Detail > User Log`

### TC-AUTH-MFA-207: Percobaan OTP salah ke-5 dicatat Failed walau sesi pre-auth berakhir, percobaan enrollment ke-5 tidak dicatat

52. Tutup jendela user uji dari TC sebelumnya dan hapus sesi login browser terkait (ID device dan jendela sesi akun aktor tetap), lalu pindah ke browser pertama dan buka jendela privat baru (tanpa sesi login)
53. Buka halaman `Auth > Login with Password` di browser → halaman Login with Password tampil
54. Ketik `lukmanhakim+{runId}-035@qwertysystem.net` pada field Email
55. Ketik `Spectra.env.MFA_PASSWORD` pada field Password
56. Centang widget reCAPTCHA "I'm not a robot"
57. Klik button [Log in] → halaman `Auth > MFA > Choose Verification Method` tampil
58. Pilih opsi "OTP via email" pada halaman Choose Verification Method
59. Klik button [Login] → halaman `Auth > MFA > OTP Verification` tampil
60. Ketik kode OTP yang salah `000000` pada kotak digit; lakukan lima kali berturut-turut
61. Verifikasi Halaman login tampil (sesi pre-auth di-invalidate)
62. Verifikasi Tidak ada caption pada halaman login
63. Pindah ke browser kedua, buka `Global Settings > Activity Log > Session`, dan hitung entri Failed untuk `Lukman Hakim` yang dibuat sesudah langkah 52 dimulai
64. Verifikasi Tampil 5 entri Failed baru untuk `Lukman Hakim` pada `Global Settings > Activity Log > Session`
65. Verifikasi Entri ke-5 memiliki Note "Incorrect OTP"
66. Pindah ke browser pertama (halaman login), ketik `lukmanhakim+{runId}-035@qwertysystem.net` pada field Email
67. Ketik `Spectra.env.MFA_PASSWORD` pada field Password
68. Centang widget reCAPTCHA "I'm not a robot"
69. Klik button [Log in] → halaman `Auth > MFA > Choose Verification Method` tampil
70. Pilih opsi "Authenticator app" pada halaman Choose Verification Method
71. Klik button [Login] → halaman `Auth > MFA > Enrollment Authenticator` tampil
72. Ketik kode verifikasi enrollment yang salah `111111` pada kotak digit; lakukan lima kali berturut-turut
73. Pindah ke browser kedua, muat ulang `Global Settings > Activity Log > Session`, dan hitung entri Failed untuk `Lukman Hakim` yang dibuat sesudah langkah 66 dimulai
74. Verifikasi Tidak ada entri Failed baru dari percobaan enrollment

### TC-AUTH-MFA-170: Sesi pre-auth habis dan user dinonaktifkan atau dihapus saat MFA tidak dicatat

75. Tutup jendela user uji dari TC sebelumnya dan hapus sesi login browser terkait (ID device dan jendela sesi akun aktor tetap), lalu pindah ke browser pertama dan buka jendela privat baru (tanpa sesi login)
76. Buka halaman `Auth > Login with Password` di browser → halaman Login with Password tampil
77. Ketik `chandragunadi+{runId}-035@qwertysystem.net` pada field Email
78. Ketik `Spectra.env.MFA_PASSWORD` pada field Password
79. Centang widget reCAPTCHA "I'm not a robot"
80. Klik button [Log in] → halaman `Auth > MFA > Choose Verification Method` tampil
81. Pilih opsi "Authenticator app" pada halaman Choose Verification Method
82. Klik button [Login] → halaman `Auth > MFA > Authenticator Verification` tampil
83. Majukan jam server uji sebesar 10 menit 30 detik (jam aplikasi authenticator uji mengikuti jam server)
84. Ketik 6 digit kode TOTP valid dari aplikasi authenticator uji untuk `chandragunadi+{runId}-035@qwertysystem.net` pada kotak digit lalu klik [Login]
85. Verifikasi Halaman login tampil
86. Kembalikan jam server uji dan jam aplikasi authenticator uji ke waktu nyata (sebelum akun aktor membuka Activity Log atau User Log)
87. Pindah ke browser kedua, buka `Global Settings > Activity Log > Session`, dan cari entri untuk `Chandra Gunadi` yang dibuat sesudah langkah 75 dimulai
88. Verifikasi Tidak ada entri baru untuk `Chandra Gunadi` pada `Global Settings > Activity Log > Session` (sesi pre-auth habis bukan upaya autentikasi)
89. Buka `Global Settings > User > Detail > User Log` untuk `Chandra Gunadi` dan cari entri yang dibuat sesudah langkah 75 dimulai
90. Verifikasi Tidak ada entri baru untuk `Chandra Gunadi` pada `Global Settings > User > Detail > User Log`

### TC-AUTH-MFA-151 (bagian absence, butir a): Faktor-1 tidak menulis Success saat MFA terpicu

91. Tutup jendela user uji dari TC sebelumnya dan hapus sesi login browser terkait (ID device dan jendela sesi akun aktor tetap), lalu pindah ke browser pertama dan buka jendela privat baru (tanpa sesi login)
92. Buka halaman `Auth > Login with Password` di browser → halaman Login with Password tampil
93. Ketik `oliviagunawan+{runId}-035@qwertysystem.net` pada field Email
94. Ketik `Spectra.env.MFA_PASSWORD` pada field Password
95. Centang widget reCAPTCHA "I'm not a robot"
96. Klik button [Log in] → halaman `Auth > MFA > Choose Verification Method` tampil
97. Pilih opsi "Authenticator app" pada halaman Choose Verification Method
98. Klik button [Login] → halaman `Auth > MFA > Authenticator Verification` tampil
99. Pindah ke browser kedua, buka `Global Settings > Activity Log > Session`, dan cari entri `Olivia Gunawan` yang dibuat sesudah langkah 91 dimulai
100. Verifikasi Belum ada entri Success `Login with password` untuk `Olivia Gunawan` pada `Global Settings > Activity Log > Session` (faktor-1 tidak menulis Success saat MFA terpicu)

### TC-AUTH-MFA-48 (bagian absence, langkah 8): Attempt yang menolak Agreement tidak menulis entri log

101. Tutup jendela user uji dari TC sebelumnya dan hapus sesi login browser terkait (ID device dan jendela sesi akun aktor tetap), lalu pindah ke browser pertama dan buka jendela baru browser uji A (tanpa sesi login untuk `Desi Natalia`; user belum pernah login)
102. Buka halaman `Auth > Login with Password` di browser → halaman Login with Password tampil
103. Ketik `desinatalia+{runId}-035@qwertysystem.net` pada field Email
104. Ketik `Spectra.env.MFA_PASSWORD` pada field Password
105. Centang widget reCAPTCHA "I'm not a robot"
106. Klik button [Log in] → layar Confirm to Continue tampil
107. Tinggalkan layar Confirm to Continue tanpa klik [Continue] (kembali ke halaman Login with Password)
108. Pindah ke browser kedua, buka `Global Settings > Activity Log > Session`, dan cari entri untuk `Desi Natalia` yang dibuat sesudah langkah 101 dimulai
109. Verifikasi Tidak ada entri untuk `Desi Natalia` pada `Global Settings > Activity Log > Session`
110. Buka `Global Settings > User > Detail > User Log` untuk `Desi Natalia` dan cari entri yang dibuat sesudah langkah 101 dimulai
111. Verifikasi Tidak ada entri untuk `Desi Natalia` pada `Global Settings > User > Detail > User Log`

## Notes

- Sumber: `auth/mfa/TestCases/tc-mfa.md`. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Langkah pembuka tiap TC sesudah TC pertama menutup jendela user uji dari TC sebelumnya dan menghapus sesi login browser terkait (ID device dan jendela sesi akun aktor tetap) sebelum jendela baru dibuka; itu langkah penghubung tanpa `Verifikasi` (S-03, S-09).
- Kelas harness g (asersi absence), dipisah dari spec pencatatan `TC-AUTH-MFA-E2E-033` dan `034`. Asersi absence dari TC fungsional lain (Post Condition "tidak ada entri log untuk pengiriman email" pada TC-AUTH-MFA-65 dan 152) dirujuk di Notes spec `TC-AUTH-MFA-E2E-032`.
- P-1 (state berat): TC-AUTH-MFA-207 adalah TC campuran: butir a dan b (5 entri Failed, entri ke-5 `Incorrect OTP`) adalah asersi pencatatan, butir c (tidak ada entri Failed dari percobaan enrollment) adalah absence. Seluruh TC tetap di spec ini karena butir c bergantung pada state berat yang dibangun langkah sebelumnya (lima OTP salah lalu login ulang menuju Enrollment Authenticator pada user yang sama) dan memakai alur login yang sama; memisahkan butir a dan b menduplikasi state itu.
- P-2 (pemicu bukan objek uji): TC-AUTH-MFA-171 memaksa respons 5xx (kelas b) hanya sebagai pemicu; objek asersinya adalah tidak adanya entri log (absence); toast error dan tidak adanya sesi (Expected a dan c) adalah akibat langsung pemicu itu sehingga TC-AUTH-MFA-171 tetap di spec ini, bukan di spec resilience. Intercept dilepas segera setelah pemicu selesai (langkah 47).
- TC-AUTH-MFA-169 (jam server dan jam browser dimajukan 60 detik), TC-AUTH-MFA-170 (jam server dimajukan 10 menit 30 detik), dan TC-AUTH-MFA-168 (pemindaian QR code untuk menyelesaikan enrollment) memakai harness waktu atau QR sebagai langkah rutin pemicu atau penyelesaian alur, bukan objek uji; TTL dan teknologi bantu bukan yang diasersi, sehingga tidak butuh pemisahan kelas d.
- TC-AUTH-MFA-151 terbelah lintas spec (prinsip 10): butir a (absence, langkah 91–100) diasersikan di spec ini; butir b (tepat satu entri Success setelah faktor-2) diasersikan di spec `TC-AUTH-MFA-E2E-031-trust-device-dan-pasca-login`. User di spec ini berbeda (`+{runId}-035`) dan sengaja tidak menyelesaikan faktor-2.
- TC-AUTH-MFA-48 terbelah lintas spec (prinsip 10): tampilan layar Confirm to Continue, tidak adanya halaman MFA, email OTP, dan email alert, serta tidak adanya sesi diuji di spec `TC-AUTH-MFA-E2E-027-sekuensialitas-agreement-dan-mfa`; asersi absence log (langkah 8 TC sumber) diuji di spec ini dengan user terpisah (`+{runId}-035`).
- Penyimpangan urutan (S-05): urutan di spec ini 168, 169, 171, 207, 170 (urutan TC sumber 168, 169, 170, 171, 207). TC-AUTH-MFA-170 ditaruh paling akhir di antara TC yang memajukan jam server; state global itu dipulihkan di langkah 86 (sebelum akun aktor membuka Activity Log dan User Log, S-09) dan hook `after`, dan tidak boleh memengaruhi TC lain. Jam TC-AUTH-MFA-169 dipulihkan di langkah 30.
- Asersi tambahan (S-03): langkah 85 (`Verifikasi Halaman login tampil` pada TC-AUTH-MFA-170) hanya ada di Langkah Uji TC-AUTH-MFA-170 langkah 8 (dalam kurung), tidak di Expected; langkah itu menjadi penanda sesi pre-auth habis yang teramati di UI sebelum asersi absence log.
- Melewati ±35 langkah (±68 netto setelah langkah prefix login faktor-1 tidak dihitung) karena tujuh TC absence yang masing-masing memakai user dan konteks browser sendiri, membaca log lewat akun observer yang login sekali di hook `before`, dan memulihkan jam atau intercept di akhir TC yang mengubahnya; bagian sesudahnya tetap bermakna walau bagian sebelumnya gagal, sehingga spec tidak dipecah.
- Langkah penghubung tanpa awalan `Verifikasi` (S-03): buka jendela privat baru (atau jendela baru browser uji A untuk TC-AUTH-MFA-168 dan 48) dan perpindahan antar browser pertama dan kedua di awal tiap TC; langkah 47 (lepas intercept), 30 dan 86 (pulihkan jam; keduanya sebelum akun aktor membaca log). Entri "baru" dibedakan dari entri yang sudah ada lewat penanda waktu (S-12): hanya entri yang dibuat sesudah langkah pembuka TC itu dimulai yang dihitung, tanpa baris log awal buatan seeding.
- Temuan untuk QA:
  - TC-AUTH-MFA-48: kolom Expected tidak menyebut kondisi kedua surface log padahal Langkah Uji 8 memeriksanya; spec menulis asersi absence berdasarkan PRD `AUTHMFA-LOGIC-01b` (Agreement yang ditolak bukan upaya autentikasi yang selesai).
  - Seluruh TC di spec ini menulis "password valid `Nama User`" pada Langkah Uji; spec memakai `Spectra.env.MFA_PASSWORD` sebagai password valid user seeding.
  - TC-AUTH-MFA-168, 169, 170, 171, 48 mencantumkan Precondition mail-catcher yang tidak dipakai Langkah Uji; spec tidak mencantumkannya di Prerequisites.
  - TC-AUTH-MFA-170: judul menyebut "user dinonaktifkan atau dihapus", sedangkan Langkah Uji dan Expected hanya memuat sesi pre-auth habis (jeda 10 menit 30 detik). Spec hanya mengikuti kasus sesi pre-auth habis. TC memakai "Tunggu 10 menit 30 detik"; spec memajukan jam server sesuai kemampuan teknis (jam server uji) dan kode TOTP dihasilkan pada jam yang sama.
  - TC-AUTH-MFA-171: Langkah Uji 9 ("Paksa respons 5xx") tidak menyebut endpoint; spec memakai `POST /v2/iam/auth/mfa/authenticator/verify` dari OpenAPI. Post Condition "trust device tidak diperbarui" tidak dapat dicek lewat UI dan tidak diasersi; "Tidak ada sesi yang dibuat" diasersi lewat halaman tetap Authenticator Verification.
  - TC-AUTH-MFA-168: tidak disebut cara memindai QR code oleh harness; kemampuan ini dicatat di Prerequisites. Post Condition "Tepat satu entri pada tiap surface log" sama dengan butir a.
  - TC-AUTH-MFA-207 langkah 2 dan 5 ("ketik kode OTP yang salah lima kali berturut-turut", "ketik kode verifikasi enrollment yang salah lima kali") tidak menyebut klik [Login] atau [Verify]; spec mengikuti teks TC dan hanya mengetik (langkah 60 dan 72), sedangkan TC-AUTH-MFA-168 langkah 8 menyebut klik [Verify] secara eksplisit.
  - TC-AUTH-MFA-207: Expected butir b tidak menyebut Note entri ke-1 hingga ke-4, dan tidak menyebut apakah login ulang pada Langkah Uji 5 dibatasi setelah 5 OTP salah; Post Condition "Tidak ada sesi aktif" tidak punya langkah cek dan tidak diasersi.
  - TC-AUTH-MFA-169: Langkah Uji 8 "Tunggu hitung mundur selesai" tidak menyebut durasi (PRD §9.2 F-AUTHMFA-04 menyebut 1 menit sejak pengiriman terakhir); spec memajukan jam server dan jam browser 60 detik sampai label menjadi "Resend code", lalu memulihkannya.
  - Mekanisme seeding state BE per user (login sebelumnya dari browser uji A, lokasi dan waktu login terakhir, Authenticator terdaftar dengan secret yang dikenal authenticator uji, persetujuan Privacy Policy belum ada untuk profil POLICY) belum ada di Pre-setup (#20/#21) TC.
