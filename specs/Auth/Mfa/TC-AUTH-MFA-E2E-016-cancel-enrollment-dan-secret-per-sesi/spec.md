---
id: TC-AUTH-MFA-E2E-016-cancel-enrollment-dan-secret-per-sesi
title: "Cancel Enrollment dan Secret Authenticator per Sesi Pre-auth"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AUTH-MFA-114
  - TC-AUTH-MFA-115
  - TC-AUTH-MFA-116
  - TC-AUTH-MFA-117
  - TC-AUTH-MFA-118
coverage:
  web: automated
---

# Cancel Enrollment dan Secret Authenticator per Sesi Pre-auth

## Prerequisites

- Mode: FE+BE.
- Seeding (hook `before`, lewat API oleh akun aktor Total Control (Global Settings) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.GS_TC_PASSWORD`): lima user profil FIRST (Tabel Data Uji Pre-setup #3: Activated, Active ON, belum pernah login di platform mana pun, Authenticator belum terdaftar), password `Spectra.env.MFA_PASSWORD`, email bersuffix per run:
  - TC-AUTH-MFA-114: `Indra Lesmana` (`indralesmana+{runId}-016@qwertysystem.net`)
  - TC-AUTH-MFA-115: `Jessica Tanuwijaya` (`jessicatanuwijaya+{runId}-016@qwertysystem.net`)
  - TC-AUTH-MFA-116: `Krisna Aditya` (`krisnaaditya+{runId}-016@qwertysystem.net`)
  - TC-AUTH-MFA-117: `Lestari Wulan` (`lestariwulan+{runId}-016@qwertysystem.net`)
  - TC-AUTH-MFA-118: `Mario Santoso` (`mariosantoso+{runId}-016@qwertysystem.net`)
- Seeding state BE per user: hanya profil FIRST (Activated, Active ON, belum pernah login di platform mana pun, Authenticator belum terdaftar) yang dibentuk lewat pembuatan user oleh akun aktor; tidak ada state BE lain yang di-seed (trusted device, lokasi dan waktu login terakhir, consent, secret Authenticator). Secret pending dibentuk oleh alur UI spec ini sendiri.
- Hook `after`: hapus kelima user. Pembersihan tidak berasumsi seeding berhasil penuh.
- Akun yang dipakai: tanpa login (halaman publik; tidak ada sesi aktif di browser) untuk semua TC. Tiap TC setelah yang pertama dimulai di jendela privat baru.
- Environment variable: `GS_TC_PASSWORD`, `MFA_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Kemampuan teknis: jendela privat; reCAPTCHA mode uji di environment; mail-catcher lingkungan uji untuk membaca kode OTP login (TC-AUTH-MFA-115); muat ulang halaman (F5); pencatatan secret key (teks) dan gambar QR code yang tampil lalu pembandingannya antar tampilan halaman Enrollment (TC-AUTH-MFA-117, 118). Isi QR code (URI otpauth://) tidak didekode di spec ini; dekode ada di spec Isi QR Code Enrollment.
- Kemampuan teknis, pembacaan state BE: pembacaan status enrollment Authenticator oleh sisi BE untuk Expected TC-AUTH-MFA-114 dan TC-AUTH-MFA-115 butir b serta TC-AUTH-MFA-116 (langkah 11, 23, dan 37); disediakan tim FE/BE karena tidak ada cara cek di UI atau Langkah Uji TC; endpoint/skrip tidak didefinisikan di TC, PRD, atau LLD.
- Semua user berprofil FIRST: login Password maupun login OTP pertama tiap user melewati layar Confirm to Continue. Login ulang user yang sama di TC-AUTH-MFA-118 juga melewati layar Confirm to Continue lagi, karena user belum menyelesaikan login final pada platform web (kondisi Agreement (a) `auth-foundation.md` §11.1).

## Test Steps

### TC-AUTH-MFA-114: Cancel di Enrollment setelah Login with Password kembali ke Choose Verification Method

1. Buka halaman `Auth > Login with Password` di browser → halaman Login with Password tampil
2. Ketik `indralesmana+{runId}-016@qwertysystem.net` pada field Email
3. Ketik `Spectra.env.MFA_PASSWORD` pada field Password
4. Centang widget reCAPTCHA "I'm not a robot"
5. Klik button [Log in] → layar Confirm to Continue tampil
6. Centang checkbox persetujuan, lalu klik [Continue ➔] → halaman `Auth > MFA > Choose Verification Method` tampil
7. Pilih opsi "Authenticator app" pada halaman Choose Verification Method
8. Klik button [Login] → halaman `Auth > MFA > Enrollment Authenticator` tampil
9. Klik button Text [Cancel]
10. Verifikasi Halaman `Auth > MFA > Choose Verification Method` tampil
11. Verifikasi Enrollment tetap belum aktif
12. Verifikasi Tidak ada opsi yang terpilih (kembali ke default)
13. Verifikasi Button [Login] disabled (kembali ke default)

### TC-AUTH-MFA-115: Cancel di Enrollment setelah Login with OTP kembali ke halaman login

14. Tutup jendela user uji dari TC sebelumnya dan hapus sesi login browser terkait (ID device dan jendela sesi akun aktor tetap), lalu buka jendela privat baru (tanpa sesi login)
15. Buka halaman `Auth > Login with OTP > Request OTP` di browser → halaman Request OTP tampil
16. Ketik `jessicatanuwijaya+{runId}-016@qwertysystem.net` pada field Email
17. Centang widget reCAPTCHA "I'm not a robot"
18. Klik button [Request OTP] → halaman Verify OTP tampil
19. Ketik 6 digit kode OTP login dari email `jessicatanuwijaya+{runId}-016@qwertysystem.net` pada kotak digit → layar Confirm to Continue tampil
20. Centang checkbox persetujuan, lalu klik [Continue ➔] → halaman `Auth > MFA > Enrollment Authenticator` tampil
21. Klik button Text [Cancel] pada halaman Enrollment Authenticator
22. Verifikasi Halaman login tampil (bukan Choose Verification Method)
23. Verifikasi Enrollment tetap belum aktif
24. Verifikasi Tidak ada sesi penuh

### TC-AUTH-MFA-116: Setelah Cancel, memilih Authenticator app lagi tetap membuka Enrollment

25. Tutup jendela user uji dari TC sebelumnya dan hapus sesi login browser terkait (ID device dan jendela sesi akun aktor tetap), lalu buka jendela privat baru (tanpa sesi login)
26. Buka halaman `Auth > Login with Password` di browser → halaman Login with Password tampil
27. Ketik `krisnaaditya+{runId}-016@qwertysystem.net` pada field Email
28. Ketik `Spectra.env.MFA_PASSWORD` pada field Password
29. Centang widget reCAPTCHA "I'm not a robot"
30. Klik button [Log in] → layar Confirm to Continue tampil
31. Centang checkbox persetujuan, lalu klik [Continue ➔] → halaman `Auth > MFA > Choose Verification Method` tampil
32. Pilih opsi "Authenticator app" pada halaman Choose Verification Method
33. Klik button [Login] → halaman `Auth > MFA > Enrollment Authenticator` tampil
34. Klik button Text [Cancel] → halaman `Auth > MFA > Choose Verification Method` tampil
35. Pilih opsi "Authenticator app" lalu klik button [Login]
36. Verifikasi Halaman `Auth > MFA > Enrollment Authenticator` tampil lagi
37. Verifikasi Enrollment belum aktif setelah Cancel

### TC-AUTH-MFA-117: Memuat ulang halaman Enrollment pada sesi pre-auth yang sama menampilkan secret yang sama

38. Tutup jendela user uji dari TC sebelumnya dan hapus sesi login browser terkait (ID device dan jendela sesi akun aktor tetap), lalu buka jendela privat baru (tanpa sesi login)
39. Buka halaman `Auth > Login with Password` di browser → halaman Login with Password tampil
40. Ketik `lestariwulan+{runId}-016@qwertysystem.net` pada field Email
41. Ketik `Spectra.env.MFA_PASSWORD` pada field Password
42. Centang widget reCAPTCHA "I'm not a robot"
43. Klik button [Log in] → layar Confirm to Continue tampil
44. Centang checkbox persetujuan, lalu klik [Continue ➔] → halaman `Auth > MFA > Choose Verification Method` tampil
45. Pilih opsi "Authenticator app" pada halaman Choose Verification Method
46. Klik button [Login] → halaman `Auth > MFA > Enrollment Authenticator` tampil
47. Catat secret key dan gambar QR code yang tampil
48. Muat ulang halaman (F5)
49. Bandingkan secret key dan QR code dengan yang dicatat
50. Verifikasi Halaman Enrollment Authenticator menampilkan secret key yang sama dengan sebelumnya
51. Verifikasi QR code mendaftarkan secret yang sama (gambar QR code identik dengan yang dicatat pada langkah 47)

### TC-AUTH-MFA-118: Sesi pre-auth baru memulai enrollment dengan secret baru

52. Tutup jendela user uji dari TC sebelumnya dan hapus sesi login browser terkait (ID device dan jendela sesi akun aktor tetap), lalu buka jendela privat baru (tanpa sesi login)
53. Buka halaman `Auth > Login with Password` di browser → halaman Login with Password tampil
54. Ketik `mariosantoso+{runId}-016@qwertysystem.net` pada field Email
55. Ketik `Spectra.env.MFA_PASSWORD` pada field Password
56. Centang widget reCAPTCHA "I'm not a robot"
57. Klik button [Log in] → layar Confirm to Continue tampil
58. Centang checkbox persetujuan, lalu klik [Continue ➔] → halaman `Auth > MFA > Choose Verification Method` tampil
59. Pilih opsi "Authenticator app" pada halaman Choose Verification Method
60. Klik button [Login] → halaman `Auth > MFA > Enrollment Authenticator` tampil
61. Catat secret key dan gambar QR code yang tampil
62. Klik button Text [Cancel] → halaman `Auth > MFA > Choose Verification Method` tampil
63. Buka halaman `Auth > Login with Password` di browser → halaman Login with Password tampil
64. Ketik `mariosantoso+{runId}-016@qwertysystem.net` pada field Email
65. Ketik `Spectra.env.MFA_PASSWORD` pada field Password
66. Centang widget reCAPTCHA "I'm not a robot"
67. Klik button [Log in] → layar Confirm to Continue tampil (login baru meng-invalidate sesi pre-auth lama)
68. Centang checkbox persetujuan, lalu klik [Continue ➔] → halaman `Auth > MFA > Choose Verification Method` tampil
69. Pilih opsi "Authenticator app" lalu klik button [Login] → halaman `Auth > MFA > Enrollment Authenticator` tampil
70. Bandingkan secret key dengan yang dicatat pada langkah 61
71. Verifikasi Secret key pada sesi pre-auth baru berbeda dari secret key yang dicatat pada langkah 61
72. Verifikasi QR code pada sesi pre-auth baru berbeda dari QR code yang dicatat pada langkah 61

## Notes

- Sumber: `auth/mfa/TestCases/tc-mfa.md`. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Langkah pembuka tiap TC sesudah TC pertama menutup jendela user uji dari TC sebelumnya dan menghapus sesi login browser terkait (ID device dan jendela sesi akun aktor tetap) sebelum jendela baru dibuka; itu langkah penghubung tanpa `Verifikasi` (S-03, S-09).
- Urutan mengikuti urutan TC sumber (114, 115, 116, 117, 118); tidak ada penyimpangan. Tidak ada aksi yang menghabisi data; tiap TC memakai user sendiri.
- Langkah penghubung tanpa awalan `Verifikasi` (buka jendela privat baru di awal tiap TC setelah yang pertama; langkah 34 Cancel menuju Choose Verification Method sebelum memilih ulang; langkah 47, 61 mencatat secret key dan QR code; langkah 49, 70 membandingkan) bukan asersi tambahan (S-03).
- Batas ukuran: langkah prefix login faktor-1 yang identik antar-TC (buka Login with Password sampai klik [Log in]) tidak dihitung ke batas ±35 langkah (bagian 3 konvensi); kelima TC independen dan tiap TC memakai user sendiri, sehingga spec tidak dipecah.
- Perbandingan QR code pada TC-AUTH-MFA-117 butir b dan TC-AUTH-MFA-118 dilakukan pada gambar QR code yang tampil; isi URI `otpauth://` tidak didekode di spec ini karena dekode QR adalah kelas harness eksternal yang dipisah (prinsip 13 butir d) dan ada di spec Isi QR Code Enrollment.
- Temuan untuk QA: (1) Post Condition TC tanpa langkah observasi dan tanpa Expected padanan tidak diasersi di spec ini (S-01): TC-AUTH-MFA-117 "Satu secret pending untuk sesi pre-auth ini"; TC-AUTH-MFA-118 "Secret pending lama tidak berlaku untuk `Mario Santoso`; enrollment belum aktif". Post Condition TC-AUTH-MFA-114 "Sesi pre-auth MFA tetap aktif" teramati sebagai halaman Choose Verification Method tampil (langkah 10), tanpa `Verifikasi` terpisah. Post Condition absence dan pencatatan juga tidak diasersi (S-05): TC-AUTH-MFA-114 dan 115 "tidak ada entri log". QA dapat menambah Expected atau langkah observasi di TC. (1a) TC-AUTH-MFA-114 dan TC-AUTH-MFA-115 butir b serta TC-AUTH-MFA-116 ("enrollment tetap belum aktif" / "belum aktif setelah Cancel") tidak memberi cara cek status enrollment di UI maupun di Langkah Uji; spec membacanya lewat kemampuan pembacaan status enrollment oleh sisi BE yang disediakan tim FE/BE (langkah 11, 23, 37) dan tidak menyebut endpoint. QA perlu menambah langkah observasi atau menyatakan cara cek status itu. (2) TC-AUTH-MFA-118 langkah 9 memuat langkah bersyarat ("bila layar Confirm to Continue tampil"); spec menetapkan layar tampil karena user FIRST belum menyelesaikan login final (kondisi Agreement (a) `auth-foundation.md` §11.1), dan Langkah Uji tidak merinci cara membuka login ulang sehingga spec membuka halaman Login with Password di konteks yang sama. (3) TC-AUTH-MFA-115 Langkah Uji 5 menyebut Confirm to Continue lalu langsung langkah 6 pada halaman Enrollment tanpa langkah menuju halaman itu; langkah 20 menambahkan hasil "halaman Enrollment Authenticator tampil". (4) TC-AUTH-MFA-115 butir a "Halaman login tampil" tidak menyebut halaman login yang mana (Login with Password atau Login with OTP). (5) TC-AUTH-MFA-116 langkah 8 dan TC-AUTH-MFA-118 langkah 9 tidak menyebut hasil Cancel (Choose Verification Method); spec menulisnya sebagai hasil panah pada langkah 34 (TC-AUTH-MFA-116) dan langkah 62 (TC-AUTH-MFA-118, hasil yang juga tidak ada di Langkah Uji). (6) Mekanisme seeding user profil FIRST mengikuti Pre-setup #3 (Create User); tidak ada state BE tambahan yang butuh mekanisme seeding di spec ini.
