---
id: TC-AUTH-MFA-E2E-033-pencatatan-failed-faktor-kedua
title: "Pencatatan Failed pada Verifikasi Faktor Kedua MFA"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AUTH-MFA-158
  - TC-AUTH-MFA-159
  - TC-AUTH-MFA-162
  - TC-AUTH-MFA-163
  - TC-AUTH-MFA-164
coverage:
  web: automated
---

# Pencatatan Failed pada Verifikasi Faktor Kedua MFA

## Prerequisites

- Mode: FE+BE.
- Seeding (hook `before`, lewat API oleh akun aktor Total Control (Global Settings) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.GS_TC_PASSWORD`): lima user, password `Spectra.env.MFA_PASSWORD`, email bersuffix per run:
  - TC-AUTH-MFA-158: `Prabu Anggoro` (`prabuanggoro+{runId}-033@qwertysystem.net`), profil NEWDEV (Tabel Data Uji Pre-setup #4: Activated, Active ON, seperti BASE tetapi ID device browser uji B belum ada di daftar trusted device, Authenticator belum terdaftar)
  - TC-AUTH-MFA-159: `Quin Safitri` (`quinsafitri+{runId}-033@qwertysystem.net`), profil NEWDEV
  - TC-AUTH-MFA-162: `Tantri Wulandari` (`tantriwulandari+{runId}-033@qwertysystem.net`), profil NEWDEVE (Tabel Data Uji Pre-setup #5: seperti NEWDEV tetapi Authenticator sudah terdaftar; secret-nya dimuat ke aplikasi authenticator uji)
  - TC-AUTH-MFA-163: `Ucok Siregar` (`ucoksiregar+{runId}-033@qwertysystem.net`), profil NEWDEVE
  - TC-AUTH-MFA-164: `Vivi Anjani` (`vivianjani+{runId}-033@qwertysystem.net`), profil NEWDEVE
- Aktor observer log: akun aktor Total Control (Global Settings) di atas login di browser kedua pada hook `before` dan membaca `Global Settings > Activity Log > Session` serta `Global Settings > User > Detail > User Log`. Browser pertama dipakai sebagai user uji tanpa login (halaman publik) dan dibuka di jendela privat baru tiap TC.
- Suite berjalan serial (`parallel: false`) karena spec ini mengubah jam server uji dan jam aplikasi authenticator uji (dibekukan pada TC-AUTH-MFA-164); hook `after` memulihkan kedua jam itu ke waktu nyata.
- Hook `after`: hapus kelima user, pulihkan jam server uji dan jam aplikasi authenticator uji ke waktu nyata, dan tutup browser kedua. Hook ini tetap jalan walau spec gagal di tengah dan tidak berasumsi seeding berhasil penuh.
- Environment variable: `GS_TC_PASSWORD`, `MFA_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Kemampuan teknis: dua sesi browser bersamaan; browser uji B (ID device belum dikenali) dan browser uji C (device baru tambahan; TC-AUTH-MFA-164) sebagai konteks browser terpisah dengan ID device persisten sendiri; aplikasi authenticator uji (TOTP: SHA-1, 6 digit, periode 30 detik) yang memegang secret user profil NEWDEVE, dengan jam yang dapat dibekukan dan dipulihkan, bersama jam server uji, agar kode TOTP yang sama dapat dipakai dua kali dalam periode yang sama (TC-AUTH-MFA-164); IP uji yang dikenal untuk asersi kolom IP Address; reCAPTCHA mode uji di environment.
- Seeding state BE per user: login sukses sebelumnya dari browser uji A (device dikenali), lokasi dan waktu login terakhir, ID device browser uji B belum ada di daftar trusted device, dan (profil NEWDEVE) Authenticator terdaftar dengan secret yang dikenal aplikasi authenticator uji; mekanisme seeding (endpoint/skrip uji) disediakan tim FE/BE karena tidak didefinisikan di TC, PRD, atau LLD.
- Semua user berprofil NEWDEV atau NEWDEVE (bukan login pertama), jadi tiap login langsung menuju Choose Verification Method tanpa layar Confirm to Continue.

## Test Steps

### TC-AUTH-MFA-158: Pencatatan OTP faktor-2 kosong dicatat Failed Empty OTP

1. Buka jendela privat baru di browser pertama (tanpa sesi login)
2. Buka halaman `Auth > Login with Password` di browser → halaman Login with Password tampil
3. Ketik `prabuanggoro+{runId}-033@qwertysystem.net` pada field Email
4. Ketik `Spectra.env.MFA_PASSWORD` pada field Password
5. Centang widget reCAPTCHA "I'm not a robot"
6. Klik button [Log in] → halaman `Auth > MFA > Choose Verification Method` tampil
7. Pilih opsi "OTP via email" pada halaman Choose Verification Method
8. Klik button [Login] → halaman `Auth > MFA > OTP Verification` tampil dan email OTP faktor-2 terkirim ke `prabuanggoro+{runId}-033@qwertysystem.net`
9. Klik button [Login] tanpa mengisi kode
10. Pindah ke browser kedua (sesi Total Control Global Settings), buka `Global Settings > Activity Log > Session`, dan cari entri untuk `Prabu Anggoro` yang dibuat sesudah langkah 1 dimulai
11. Verifikasi Tampil satu entri baru untuk `Prabu Anggoro`: Activity `Login`, Status `Failed`, Note `Empty OTP`, IP Address berisi IP uji, tanggal dan waktu percobaan
12. Verifikasi Percobaan ini menghasilkan tepat satu entri pada `Global Settings > Activity Log > Session` (tidak ada entri log tambahan)
13. Buka `Global Settings > User > Detail > User Log` untuk `Prabu Anggoro` dan cari entri yang dibuat sesudah langkah 1 dimulai
14. Verifikasi Tampil satu entri baru dengan Activity `Login`, Status `Failed`, Note `Empty OTP`, dan IP Address yang sama
15. Verifikasi Percobaan ini menghasilkan tepat satu entri pada `Global Settings > User > Detail > User Log` (tidak ada entri log tambahan)

### TC-AUTH-MFA-159: Pencatatan OTP faktor-2 salah dicatat Failed Incorrect OTP

16. Tutup jendela user uji dari TC sebelumnya dan hapus sesi login browser terkait (ID device dan jendela sesi akun aktor tetap), lalu pindah ke browser pertama dan buka jendela privat baru (tanpa sesi login)
17. Buka halaman `Auth > Login with Password` di browser → halaman Login with Password tampil
18. Ketik `quinsafitri+{runId}-033@qwertysystem.net` pada field Email
19. Ketik `Spectra.env.MFA_PASSWORD` pada field Password
20. Centang widget reCAPTCHA "I'm not a robot"
21. Klik button [Log in] → halaman `Auth > MFA > Choose Verification Method` tampil
22. Pilih opsi "OTP via email" pada halaman Choose Verification Method
23. Klik button [Login] → halaman `Auth > MFA > OTP Verification` tampil dan email OTP faktor-2 terkirim ke `quinsafitri+{runId}-033@qwertysystem.net`
24. Ketik 6 digit kode yang salah `000000` pada kotak digit
25. Pindah ke browser kedua, buka `Global Settings > Activity Log > Session`, dan cari entri untuk `Quin Safitri` yang dibuat sesudah langkah 16 dimulai
26. Verifikasi Tampil satu entri baru untuk `Quin Safitri`: Activity `Login`, Status `Failed`, Note `Incorrect OTP`, IP Address berisi IP uji, tanggal dan waktu percobaan
27. Verifikasi Percobaan ini menghasilkan tepat satu entri pada `Global Settings > Activity Log > Session` (tidak ada entri log tambahan)
28. Buka `Global Settings > User > Detail > User Log` untuk `Quin Safitri` dan cari entri yang dibuat sesudah langkah 16 dimulai
29. Verifikasi Tampil satu entri baru dengan Activity `Login`, Status `Failed`, Note `Incorrect OTP`, dan IP Address yang sama
30. Verifikasi Percobaan ini menghasilkan tepat satu entri pada `Global Settings > User > Detail > User Log` (tidak ada entri log tambahan)

### TC-AUTH-MFA-162: Pencatatan kode Authenticator kosong dicatat Failed Empty OTP

31. Tutup jendela user uji dari TC sebelumnya dan hapus sesi login browser terkait (ID device dan jendela sesi akun aktor tetap), lalu pindah ke browser pertama dan buka jendela privat baru (tanpa sesi login)
32. Buka halaman `Auth > Login with Password` di browser → halaman Login with Password tampil
33. Ketik `tantriwulandari+{runId}-033@qwertysystem.net` pada field Email
34. Ketik `Spectra.env.MFA_PASSWORD` pada field Password
35. Centang widget reCAPTCHA "I'm not a robot"
36. Klik button [Log in] → halaman `Auth > MFA > Choose Verification Method` tampil
37. Pilih opsi "Authenticator app" pada halaman Choose Verification Method
38. Klik button [Login] → halaman `Auth > MFA > Authenticator Verification` tampil
39. Klik button [Login] tanpa mengisi kode
40. Pindah ke browser kedua, buka `Global Settings > Activity Log > Session`, dan cari entri untuk `Tantri Wulandari` yang dibuat sesudah langkah 31 dimulai
41. Verifikasi Tampil satu entri baru untuk `Tantri Wulandari`: Activity `Login`, Status `Failed`, Note `Empty OTP`, IP Address berisi IP uji, tanggal dan waktu percobaan
42. Verifikasi Percobaan ini menghasilkan tepat satu entri pada `Global Settings > Activity Log > Session` (tidak ada entri log tambahan)
43. Buka `Global Settings > User > Detail > User Log` untuk `Tantri Wulandari` dan cari entri yang dibuat sesudah langkah 31 dimulai
44. Verifikasi Tampil satu entri baru dengan Activity `Login`, Status `Failed`, Note `Empty OTP`, dan IP Address yang sama
45. Verifikasi Percobaan ini menghasilkan tepat satu entri pada `Global Settings > User > Detail > User Log` (tidak ada entri log tambahan)

### TC-AUTH-MFA-163: Pencatatan kode Authenticator salah dicatat Failed Incorrect OTP

46. Tutup jendela user uji dari TC sebelumnya dan hapus sesi login browser terkait (ID device dan jendela sesi akun aktor tetap), lalu pindah ke browser pertama dan buka jendela privat baru (tanpa sesi login)
47. Buka halaman `Auth > Login with Password` di browser → halaman Login with Password tampil
48. Ketik `ucoksiregar+{runId}-033@qwertysystem.net` pada field Email
49. Ketik `Spectra.env.MFA_PASSWORD` pada field Password
50. Centang widget reCAPTCHA "I'm not a robot"
51. Klik button [Log in] → halaman `Auth > MFA > Choose Verification Method` tampil
52. Pilih opsi "Authenticator app" pada halaman Choose Verification Method
53. Klik button [Login] → halaman `Auth > MFA > Authenticator Verification` tampil
54. Ketik 6 digit kode TOTP yang salah `000000` pada kotak digit lalu klik [Login]
55. Pindah ke browser kedua, buka `Global Settings > Activity Log > Session`, dan cari entri untuk `Ucok Siregar` yang dibuat sesudah langkah 46 dimulai
56. Verifikasi Tampil satu entri baru untuk `Ucok Siregar`: Activity `Login`, Status `Failed`, Note `Incorrect OTP`, IP Address berisi IP uji, tanggal dan waktu percobaan
57. Verifikasi Percobaan ini menghasilkan tepat satu entri pada `Global Settings > Activity Log > Session` (tidak ada entri log tambahan)
58. Buka `Global Settings > User > Detail > User Log` untuk `Ucok Siregar` dan cari entri yang dibuat sesudah langkah 46 dimulai
59. Verifikasi Tampil satu entri baru dengan Activity `Login`, Status `Failed`, Note `Incorrect OTP`, dan IP Address yang sama
60. Verifikasi Percobaan ini menghasilkan tepat satu entri pada `Global Settings > User > Detail > User Log` (tidak ada entri log tambahan)

### TC-AUTH-MFA-164: Pencatatan kode TOTP yang dipakai ulang dicatat Failed Incorrect OTP

61. Pindah ke browser kedua, buka `Global Settings > Activity Log > Session`, dan catat jumlah entri berstatus `Failed` untuk `Vivi Anjani` sebagai baseline (jam server masih nyata)
62. Buka `Global Settings > User > Detail > User Log` untuk `Vivi Anjani` dan catat jumlah entri berstatus `Failed` sebagai baseline
63. Tutup jendela user uji dari TC sebelumnya dan hapus sesi login browser terkait (ID device dan jendela sesi akun aktor tetap), lalu pindah ke browser pertama dan buka browser uji B (ID device belum dikenali) sebagai jendela privat baru (tanpa sesi login)
64. Buka halaman `Auth > Login with Password` di browser → halaman Login with Password tampil
65. Ketik `vivianjani+{runId}-033@qwertysystem.net` pada field Email
66. Ketik `Spectra.env.MFA_PASSWORD` pada field Password
67. Centang widget reCAPTCHA "I'm not a robot"
68. Klik button [Log in] → halaman `Auth > MFA > Choose Verification Method` tampil
69. Pilih opsi "Authenticator app" pada halaman Choose Verification Method
70. Klik button [Login] → halaman `Auth > MFA > Authenticator Verification` tampil
71. Bekukan jam server uji dan jam aplikasi authenticator uji pada waktu yang sama (T0), supaya kode TOTP yang dihasilkan tetap berada di periode 30 detik yang sama sampai jam dipulihkan
72. Ketik 6 digit kode TOTP valid dari aplikasi authenticator uji untuk `vivianjani+{runId}-033@qwertysystem.net` pada kotak digit lalu klik [Login] → Portal — Product Hub tampil
73. Logout dari Portal — Product Hub
74. Tutup jendela user uji dari TC sebelumnya dan hapus sesi login browser terkait (ID device dan jendela sesi akun aktor tetap), lalu buka browser uji C (device baru) sebagai jendela baru tanpa sesi login
75. Buka halaman `Auth > Login with Password` di browser → halaman Login with Password tampil
76. Ketik `vivianjani+{runId}-033@qwertysystem.net` pada field Email
77. Ketik `Spectra.env.MFA_PASSWORD` pada field Password
78. Centang widget reCAPTCHA "I'm not a robot"
79. Klik button [Log in] → halaman `Auth > MFA > Choose Verification Method` tampil
80. Pilih opsi "Authenticator app" pada halaman Choose Verification Method
81. Klik button [Login] → halaman `Auth > MFA > Authenticator Verification` tampil
82. Ketik 6 digit kode TOTP yang sama dengan langkah 72 (dalam periode TOTP yang sama) pada kotak digit lalu klik [Login]
83. Pulihkan jam server uji dan jam aplikasi authenticator uji ke waktu nyata (sebelum akun aktor membuka Activity Log atau User Log)
84. Pindah ke browser kedua, muat ulang `Global Settings > Activity Log > Session`, dan cari entri berstatus `Failed` untuk `Vivi Anjani` di atas baseline langkah 61
85. Verifikasi Tampil satu entri baru untuk `Vivi Anjani`: Activity `Login`, Status `Failed`, Note `Incorrect OTP`, IP Address berisi IP uji, tanggal dan waktu percobaan
86. Verifikasi Percobaan ini menghasilkan tepat satu entri pada `Global Settings > Activity Log > Session` (jumlah entri berstatus `Failed` bertambah tepat satu dari baseline langkah 61, tidak ada entri log tambahan untuk percobaan ini)
87. Buka `Global Settings > User > Detail > User Log` untuk `Vivi Anjani` dan cari entri berstatus `Failed` di atas baseline langkah 62
88. Verifikasi Tampil satu entri baru dengan Activity `Login`, Status `Failed`, Note `Incorrect OTP`, dan IP Address yang sama
89. Verifikasi Percobaan ini menghasilkan tepat satu entri pada `Global Settings > User > Detail > User Log` (jumlah entri berstatus `Failed` bertambah tepat satu dari baseline langkah 62, tidak ada entri log tambahan untuk percobaan ini)

## Notes

- Sumber: `auth/mfa/TestCases/tc-mfa.md`. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Langkah pembuka tiap TC sesudah TC pertama menutup jendela user uji dari TC sebelumnya dan menghapus sesi login browser terkait (ID device dan jendela sesi akun aktor tetap) sebelum jendela baru dibuka; itu langkah penghubung tanpa `Verifikasi` (S-03, S-09).
- Kelas harness: pencatatan Failed (Status/Note spesifik) dibaca lewat akun aktor di browser kedua; asersi absence ada di spec `TC-AUTH-MFA-E2E-035`. Asersi Expected butir c ("tepat satu entri per surface") adalah asersi jumlah, bukan absence, sehingga tetap di spec ini.
- Melewati ±35 langkah (±54 netto setelah langkah prefix login faktor-1 tidak dihitung) karena lima TC pencatatan yang tiap TC-nya independen (user dan jendela privat sendiri, baseline penanda waktu sendiri) dan membaca dua surface log; TC-AUTH-MFA-164 yang membekukan jam ditaruh paling akhir dan memulihkannya di langkah terakhirnya, sehingga bagian sesudahnya tetap bermakna walau bagian sebelumnya gagal dan spec tidak dipecah.
- Urutan mengikuti TC sumber. TC-AUTH-MFA-164 ditaruh paling akhir karena berisi login sukses dan logout yang membentuk dua trusted device. Memakai ulang kode TOTP lewat UI di browser uji C hanya memicu kegagalan yang dicatat; objek ujinya pencatatan Failed `Incorrect OTP`, bukan manipulasi server, sehingga bukan kelas a.
- Langkah penghubung tanpa awalan `Verifikasi` (S-03): buka jendela privat baru dan perpindahan antar browser pertama dan kedua di awal tiap TC; langkah 71 dan 83 (bekukan dan pulihkan jam) serta 73 (Logout) dan 74 (membuka browser uji C) dari Langkah Uji 9 TC-AUTH-MFA-164, dan langkah 61 dan 62 (baseline log, dicatat sebelum jam dibekukan). Entri "baru" dibedakan dari entri seeding lewat penanda waktu (S-12): hanya entri yang dibuat sesudah langkah pembuka jendela privat TC itu dimulai yang dihitung. Pengecualian TC-AUTH-MFA-164: jam server dibekukan sehingga penanda waktu tidak dapat dipakai, dan jam dipulihkan (langkah 83) sebelum akun aktor membuka Activity Log atau User Log (S-09), jadi baseline berupa jumlah entri berstatus `Failed` untuk `Vivi Anjani` yang dicatat pada langkah 61 dan 62 sebelum jam dibekukan, dan asersi hanya entri `Failed` di atas baseline itu (entri Success dari login pertama langkah 72 bukan entri percobaan ke-2 dan tidak dihitung).
- Temuan untuk QA:
  - TC-AUTH-MFA-158 hingga 164 menulis "password valid `Nama User`" pada Langkah Uji; spec memakai `Spectra.env.MFA_PASSWORD` sebagai password valid user seeding.
  - TC-AUTH-MFA-164: Data Uji menyebut browser uji B untuk seluruh TC, sedangkan Langkah Uji 9 memakai browser uji C setelah logout; spec mengikuti Langkah Uji. Kode TOTP yang sama hanya dapat dipakai dua kali bila kedua langkah jatuh dalam periode 30 detik yang sama; TC tidak menyebut cara menjamin ini; spec membekukan jam server uji dan jam aplikasi authenticator uji sebelum kode dipakai pertama (langkah 71) dan memulihkannya sesudah pemakaian kedua dan sebelum log dibaca (langkah 83 dan hook `after`), dicatat sebagai kemampuan teknis di Prerequisites.
  - Mekanisme seeding state BE per user (login sebelumnya dari browser uji A, lokasi dan waktu login terakhir, Authenticator terdaftar dengan secret yang dikenal authenticator uji) belum ada di Pre-setup (#20/#21) TC.
  - TC-AUTH-MFA-164 Post Condition "trust device tidak diperbarui" tidak dicek di Langkah Uji; tidak diasersi. TC ini juga menghasilkan entri Success dari login pertama; "satu entri baru" pada Expected diartikan sebagai satu entri Failed baru dari percobaan ke-2.
  - Cara mengirim kode: TC-AUTH-MFA-159 langkah 8 hanya menyebut mengetik kode salah dan tidak menyebut klik [Login], sedangkan TC-AUTH-MFA-158, 162, 163, dan 164 menyebut klik [Login]; spec mengikuti teks TC dan hanya mengetik pada TC-AUTH-MFA-159 (langkah 24), padahal PRD FI-04 (auto-submit pada digit ke-6) berlaku untuk halaman OTP Verification.
  - Expected TC tidak menyebut caption atau toast UI untuk kode kosong atau salah; spec hanya mengasersi pencatatan log.
