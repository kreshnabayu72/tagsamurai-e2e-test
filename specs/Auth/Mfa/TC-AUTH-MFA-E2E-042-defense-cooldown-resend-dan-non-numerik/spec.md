---
id: TC-AUTH-MFA-E2E-042-defense-cooldown-resend-dan-non-numerik
title: "Defense-in-Depth: Kode Non-Numerik dan Cooldown Resend OTP pada Request Langsung"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AUTH-MFA-85
  - TC-AUTH-MFA-214
  - TC-AUTH-MFA-86
  - TC-AUTH-MFA-104
  - TC-AUTH-MFA-124
coverage:
  web: automated
---

# Defense-in-Depth: Kode Non-Numerik dan Cooldown Resend OTP pada Request Langsung

## Prerequisites

- Mode: FE+BE.
- Seeding (hook `before`, lewat API oleh akun aktor Total Control (Global Settings) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.GS_TC_PASSWORD`), password user `Spectra.env.MFA_PASSWORD`, email bersuffix per run:
  - TC-AUTH-MFA-86: `Ratna Wijaya` (`ratnawijaya+{runId}-042@qwertysystem.net`), profil NEWDEV (Tabel Data Uji Pre-setup #4: Activated, Active ON, device browser uji B belum ada di daftar trusted device, Authenticator belum terdaftar).
  - TC-AUTH-MFA-104: `Dimas Wijaya` (`dimaswijaya+{runId}-042@qwertysystem.net`), profil NEWDEVE (Tabel Data Uji Pre-setup #5: seperti NEWDEV, Authenticator sudah terdaftar).
  - TC-AUTH-MFA-124: `Maya Wijaya` (`mayawijaya+{runId}-042@qwertysystem.net`), profil FIRST (Tabel Data Uji Pre-setup #3: Activated, Active ON, belum pernah login di platform mana pun, Authenticator belum terdaftar).
  - TC-AUTH-MFA-85: `Agus Wijaya` (`aguswijaya+{runId}-042@qwertysystem.net`), profil NEWDEV.
  - TC-AUTH-MFA-214: `Vina Oktaviani` (`vinaoktaviani+{runId}-042@qwertysystem.net`), profil NEWDEV.
- Hook `after`: kembalikan jam server uji ke waktu nyata (TC-AUTH-MFA-214), lalu hapus kelima user. Hook ini tetap jalan walau spec gagal di tengah dan pembersihan tidak berasumsi seeding berhasil penuh.
- Akun yang dipakai: tanpa login (halaman publik; tidak ada sesi aktif di browser) untuk kelima TC. TC-AUTH-MFA-86, TC-AUTH-MFA-104, dan TC-AUTH-MFA-124 memeriksa log lewat jendela sesi akun aktor Total Control (Global Settings) yang dibuka di hook `before` (kredensial `Spectra.env.GS_TC_PASSWORD`). Tiap TC berbrowser dimulai di jendela baru tanpa sesi login: TC-AUTH-MFA-124 di jendela baru browser uji A (konteks bersih; ID device dikenali), lainnya di jendela privat baru browser uji B (ID device belum dikenali).
- Environment variable: `GS_TC_PASSWORD`, `MFA_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Kemampuan teknis:
  - Client HTTP untuk request langsung ke endpoint `POST /v2/iam/auth/mfa/otp/verify` (field `preAuthToken`, `otpCode`), `POST /v2/iam/auth/mfa/authenticator/verify` (`totpCode`), `POST /v2/iam/auth/mfa/authenticator/enroll/verify` (`verifyCode`), dan `POST /v2/iam/auth/mfa/otp/send` (`preAuthToken`); nama endpoint dan field dari `auth/mfa/API/openapi.yaml`.
  - Pembacaan token sesi pre-auth dari respons request faktor-1 yang dikirim browser (alat uji API).
  - Mail-catcher lingkungan uji untuk membaca email OTP faktor-2, menghitung jumlahnya (baseline jumlah email sebelum aksi), dan membaca waktu terbit email pertama (T0) dari penanda waktu email (TC-AUTH-MFA-214).
  - Jam server uji yang dapat diset absolut (dibekukan) ke waktu tertentu dengan presisi satu detik (TC-AUTH-MFA-214), dengan pemulihan ke waktu nyata di hook `after`.
  - Penanda waktu (baseline) Activity Log Session dan User Log yang dicatat sebelum request langsung, supaya asersi entri log hanya membaca baris sesudah penanda dan dicari lewat email bersuffix (TC-AUTH-MFA-86, TC-AUTH-MFA-104, TC-AUTH-MFA-124).
  - Seeding state BE per user: profil NEWDEV/NEWDEVE tanpa ID device browser uji B di daftar trusted device, profil FIRST yang belum pernah login di platform mana pun, dan Authenticator terdaftar untuk profil NEWDEVE (`Dimas Wijaya`); mekanisme seeding (endpoint/skrip uji) disediakan tim FE/BE karena tidak didefinisikan di TC, PRD, atau LLD.
  - reCAPTCHA mode uji di environment.
- Jam (TC-AUTH-MFA-214): yang diatur hanya jam server uji, diset absolut ke T0 + 59 detik lalu ke T0 + 60 detik (T0 = waktu terbit email OTP pertama), bukan digeser relatif. Jam browser/klien tidak diubah: yang diuji adalah penegakan cooldown oleh server atas request langsung, bukan hitung mundur UI, dan hitung mundur UI berjalan di jam klien. Jam server dipulihkan ke waktu nyata sebelum asersi state cooldown pada halaman, dan lagi di akhir TC.
- Jeda nyata: TC-AUTH-MFA-85 menunggu 10 detik nyata sejak pengiriman email OTP pertama (≤30 detik, tanpa pengaturan jam).
- Suite berjalan serial (`parallel: false`) karena spec ini mengubah jam server uji; hook `after` memulihkan jam server uji ke waktu nyata. Spec tidak mengubah geo-IP, email service, atau counter rate limit.

## Test Steps

### TC-AUTH-MFA-86: Server menolak kode OTP non-numerik yang lolos filter FE sebagai kode kosong

1. Buka halaman `Auth > Login with Password` di browser → halaman Login with Password tampil
2. Ketik `ratnawijaya+{runId}-042@qwertysystem.net` pada field Email
3. Ketik `Spectra.env.MFA_PASSWORD` pada field Password
4. Centang widget reCAPTCHA "I'm not a robot"
5. Klik button [Log in] → halaman `Auth > MFA > Choose Verification Method` tampil
6. Catat penanda waktu (baseline) Activity Log Session sebelum request langsung
7. Simpan token sesi pre-auth (alat uji API) dan kirim langsung request `POST /v2/iam/auth/mfa/otp/verify` (client HTTP) dengan `otpCode` `12a456`
8. Verifikasi Request ditolak
9. Verifikasi Tidak ada sesi penuh yang dibuat (halaman tetap pada Choose Verification Method)
10. Verifikasi Pesan error pada respons "OTP must not be empty" (non-numerik diperlakukan seperti kosong)
11. Pindah ke jendela sesi akun aktor Total Control (Global Settings), lalu buka `Global Settings > Activity Log > Session` dan cari entri sesudah penanda waktu untuk `Ratna Wijaya`
12. Verifikasi Tampil tepat satu entri baru sesudah penanda waktu untuk `Ratna Wijaya` dengan Status "Failed" dan Note "Empty OTP" pada Activity Log Session

### TC-AUTH-MFA-104: Server menolak kode TOTP non-numerik yang lolos filter FE sebagai kode kosong

13. Tutup jendela user uji dari TC sebelumnya dan hapus sesi login browser terkait (ID device dan jendela sesi akun aktor tetap), lalu buka jendela privat baru (tanpa sesi login)
14. Buka halaman `Auth > Login with Password` di browser → halaman Login with Password tampil
15. Ketik `dimaswijaya+{runId}-042@qwertysystem.net` pada field Email
16. Ketik `Spectra.env.MFA_PASSWORD` pada field Password
17. Centang widget reCAPTCHA "I'm not a robot"
18. Klik button [Log in] → halaman `Auth > MFA > Choose Verification Method` tampil
19. Catat penanda waktu (baseline) Activity Log Session sebelum request langsung
20. Simpan token sesi pre-auth (alat uji API) dan kirim langsung request `POST /v2/iam/auth/mfa/authenticator/verify` (client HTTP) dengan `totpCode` `12a456`
21. Verifikasi Request ditolak
22. Verifikasi Tidak ada sesi penuh yang dibuat (halaman tetap pada Choose Verification Method)
23. Verifikasi Pesan error pada respons "Code must not be empty"
24. Pindah ke jendela sesi akun aktor Total Control (Global Settings), lalu buka `Global Settings > Activity Log > Session` dan cari entri sesudah penanda waktu untuk `Dimas Wijaya`
25. Verifikasi Tampil tepat satu entri baru sesudah penanda waktu untuk `Dimas Wijaya` dengan Status "Failed" dan Note "Empty OTP" pada Activity Log Session

### TC-AUTH-MFA-124: Server menolak kode enrollment non-numerik yang lolos filter FE tanpa pencatatan

26. Tutup jendela user uji dari TC sebelumnya dan hapus sesi login browser terkait (ID device dan jendela sesi akun aktor tetap), lalu buka jendela baru browser uji A (konteks bersih, tanpa sesi login)
27. Buka halaman `Auth > Login with Password` di browser → halaman Login with Password tampil
28. Ketik `mayawijaya+{runId}-042@qwertysystem.net` pada field Email
29. Ketik `Spectra.env.MFA_PASSWORD` pada field Password
30. Centang widget reCAPTCHA "I'm not a robot"
31. Klik button [Log in] → layar Confirm to Continue tampil
32. Centang checkbox persetujuan, lalu klik [Continue ➔] → halaman `Auth > MFA > Choose Verification Method` tampil
33. Catat penanda waktu (baseline) Activity Log Session dan User Log sebelum request langsung
34. Simpan token sesi pre-auth (alat uji API) dan kirim langsung request `POST /v2/iam/auth/mfa/authenticator/enroll/verify` (client HTTP) dengan `verifyCode` `12a456`
35. Verifikasi Request ditolak
36. Verifikasi Tidak ada sesi penuh yang dibuat (halaman tetap pada Choose Verification Method)
37. Verifikasi Pesan error pada respons "Code must not be empty"
38. Pindah ke jendela sesi akun aktor Total Control (Global Settings), lalu buka `Global Settings > Activity Log > Session` dan cari entri sesudah penanda waktu untuk `Maya Wijaya` (email bersuffix `mayawijaya+{runId}-042@qwertysystem.net`)
39. Verifikasi Tidak ada entri log baru untuk `Maya Wijaya` pada Activity Log Session sesudah penanda waktu (kegagalan enrollment tidak dicatat)
40. Buka `Global Settings > User > Detail > User Log` untuk `Maya Wijaya` dan cari entri sesudah penanda waktu
41. Verifikasi Tidak ada entri log baru untuk `Maya Wijaya` pada User Log sesudah penanda waktu
42. Kembali ke jendela browser uji A (halaman Choose Verification Method)
43. Pilih opsi "Authenticator app", lalu klik button [Login] → halaman `Auth > MFA > Enrollment Authenticator` tampil
44. Verifikasi Enrollment tetap belum aktif (halaman yang tampil Enrollment Authenticator, bukan Authenticator Verification)

### TC-AUTH-MFA-85: Server menolak Resend OTP yang dikirim sebelum cooldown 60 detik selesai

45. Tutup jendela user uji dari TC sebelumnya dan hapus sesi login browser terkait (ID device dan jendela sesi akun aktor tetap), lalu buka jendela privat baru (tanpa sesi login)
46. Buka halaman `Auth > Login with Password` di browser → halaman Login with Password tampil
47. Ketik `aguswijaya+{runId}-042@qwertysystem.net` pada field Email
48. Ketik `Spectra.env.MFA_PASSWORD` pada field Password
49. Centang widget reCAPTCHA "I'm not a robot"
50. Klik button [Log in] → halaman `Auth > MFA > Choose Verification Method` tampil
51. Pilih opsi "OTP via email" pada halaman Choose Verification Method
52. Klik button [Login] → halaman `Auth > MFA > OTP Verification` tampil dan email OTP faktor-2 terkirim ke `aguswijaya+{runId}-042@qwertysystem.net`
53. Catat jumlah email OTP faktor-2 di mail-catcher `aguswijaya+{runId}-042@qwertysystem.net` sebagai baseline (satu email)
54. Simpan token sesi pre-auth (alat uji API)
55. Tunggu sampai 10 detik berlalu sejak pengiriman email OTP pertama, lalu kirim langsung request Resend OTP `POST /v2/iam/auth/mfa/otp/send` (client HTTP) dengan token tersebut
56. Verifikasi Request ditolak (hasil gagal)
57. Periksa mail-catcher `aguswijaya+{runId}-042@qwertysystem.net` dan button Resend pada halaman
58. Verifikasi Tidak ada email OTP baru di mail-catcher (jumlah email OTP faktor-2 sama dengan baseline)
59. Verifikasi Hitungan resend tidak bertambah (jumlah email OTP faktor-2 tetap sama dengan baseline; hitungan hanya dicek lewat jumlah email)
60. Verifikasi Halaman tetap pada state cooldown (button Resend dengan hitung mundur berjalan)
61. Verifikasi Tidak ada toast atau caption baru pada halaman
62. Ketik 6 digit kode OTP pertama dari email pada kotak digit → Portal — Product Hub tampil
63. Verifikasi Kode OTP pertama tetap berlaku (login berhasil dengan kode pertama)

### TC-AUTH-MFA-214: Resend OTP ditolak pada detik ke-59 dan diterima tepat pada detik ke-60 sejak pengiriman terakhir

64. Tutup jendela user uji dari TC sebelumnya dan hapus sesi login browser terkait (ID device dan jendela sesi akun aktor tetap), lalu buka jendela privat baru (tanpa sesi login)
65. Buka halaman `Auth > Login with Password` di browser → halaman Login with Password tampil
66. Ketik `vinaoktaviani+{runId}-042@qwertysystem.net` pada field Email
67. Ketik `Spectra.env.MFA_PASSWORD` pada field Password
68. Centang widget reCAPTCHA "I'm not a robot"
69. Klik button [Log in] → halaman `Auth > MFA > Choose Verification Method` tampil
70. Pilih opsi "OTP via email" pada halaman Choose Verification Method
71. Klik button [Login] → halaman `Auth > MFA > OTP Verification` tampil dan email OTP faktor-2 terkirim ke `vinaoktaviani+{runId}-042@qwertysystem.net`
72. Catat jumlah email OTP faktor-2 di mail-catcher `vinaoktaviani+{runId}-042@qwertysystem.net` sebagai baseline (satu email) dan catat T0 (waktu terbit email OTP pertama)
73. Simpan token sesi pre-auth (alat uji API)
74. Atur jam server uji ke T0 + 59 detik (absolut, dibekukan), lalu kirim langsung request Resend OTP `POST /v2/iam/auth/mfa/otp/send` (client HTTP) dengan token tersebut
75. Verifikasi Request ditolak
76. Periksa mail-catcher `vinaoktaviani+{runId}-042@qwertysystem.net`
77. Verifikasi Tidak ada email OTP baru di mail-catcher (jumlah email OTP faktor-2 sama dengan baseline)
78. Verifikasi Kode pertama tetap berlaku (tidak ada email OTP baru yang menggantikannya; hanya dicek lewat jumlah email)
79. Verifikasi Hitungan resend tidak bertambah (jumlah email OTP faktor-2 tetap sama dengan baseline; hitungan hanya dicek lewat jumlah email)
80. Pulihkan jam server uji ke waktu nyata
81. Periksa button Resend pada halaman OTP Verification
82. Verifikasi Halaman tetap pada state cooldown (button Resend dengan hitung mundur berjalan)
83. Verifikasi Tidak ada toast atau caption baru pada halaman
84. Atur jam server uji ke T0 + 60 detik (absolut, dibekukan), lalu kirim ulang request Resend OTP `POST /v2/iam/auth/mfa/otp/send` (client HTTP) dengan token yang sama
85. Verifikasi Request diterima (cooldown 1 menit genap terlewati)
86. Periksa mail-catcher `vinaoktaviani+{runId}-042@qwertysystem.net`
87. Verifikasi Email OTP kedua terkirim ke `vinaoktaviani+{runId}-042@qwertysystem.net`
88. Verifikasi Kode pada email OTP kedua berbeda dari kode pada email pertama
89. Verifikasi Tepat 2 email OTP faktor-2 total di mail-catcher (baseline + 1)
90. Ketik 6 digit kode OTP pertama pada kotak digit di halaman OTP Verification
91. Verifikasi Kode pertama tidak berlaku lagi (ditolak)
92. Pulihkan jam server uji ke waktu nyata

## Notes

- Sumber: `auth/mfa/TestCases/tc-mfa.md`. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Langkah pembuka tiap TC sesudah TC pertama menutup jendela user uji dari TC sebelumnya dan menghapus sesi login browser terkait (ID device dan jendela sesi akun aktor tetap) sebelum jendela baru dibuka; itu langkah penghubung tanpa `Verifikasi` (S-03, S-09).
- `P-1`: asersi "tidak ada entri log untuk `Maya Wijaya`" (TC-AUTH-MFA-124 Expected c, kegagalan enrollment tidak dicatat) tetap di spec ini sebagai `Verifikasi` dengan baseline penanda waktu sebelum request langsung (S-12, S-05), karena konteksnya adalah sesi pre-auth FIRST yang baru dibangun langkah sebelumnya di TC ini (consent lalu Choose Verification Method). TC-AUTH-MFA-124 tidak masuk `sourceTc` spec absence `TC-AUTH-MFA-E2E-035-absence-pencatatan-log`.
- Kelas harness: TC-AUTH-MFA-214 berkelas a (defense-in-depth), bukan kelas d: yang diuji adalah penegakan cooldown 60 detik oleh server atas request langsung, dan pengaturan jam hanya sarana pemicu batas detik ke-59 dan ke-60.
- Jumlah langkah melewati ±35 karena lima TC independen berprefix login faktor-1 yang identik (langkah prefix tidak dihitung); tiap TC memakai user sendiri dan bagian sesudahnya tetap bermakna bila TC sebelumnya gagal.
- Urutan TC menyimpang dari TC sumber (85, 214, 86, 104, 124): ketiga TC kode non-numerik dipindah ke awal, lalu TC-AUTH-MFA-85, dan TC-AUTH-MFA-214 di akhir karena mengatur jam server (state global) dan ditutup dengan kode pertama dipakai ulang (S-05, S-10).
- Langkah penghubung tanpa awalan `Verifikasi` (buka jendela privat baru di awal tiap TC berbrowser setelah TC pertama, mencatat penanda waktu baseline log, membuka Activity Log dan User Log di jendela aktor dan kembali ke browser uji A pada TC-AUTH-MFA-124, mencatat baseline jumlah email dan T0, memilih "Authenticator app" lalu [Login] pada TC-AUTH-MFA-124, mengetik kode OTP pertama pada TC-AUTH-MFA-85 dan TC-AUTH-MFA-214, memulihkan jam server uji pada TC-AUTH-MFA-214) bukan asersi tambahan (S-03).
- Asersi entri log pada TC-AUTH-MFA-86 dan TC-AUTH-MFA-104 hanya memakai Status dan Note sesuai TC ("Failed", "Empty OTP"); kolom Activity tidak diasersi karena nilainya berasal dari LLD, bukan dari TC.
- Temuan untuk QA: (1) TC-AUTH-MFA-86 dan TC-AUTH-MFA-104 butir b menyebut "caption error pada halaman", tetapi request langsung tidak merender caption pada halaman dan Langkah Uji berhenti di Choose Verification Method; spec mengasersi pesan error pada respons (field `message` openapi yang dirender FE sebagai caption). (2) TC-AUTH-MFA-124 butir a "enrollment tetap belum aktif" tidak punya cara pengecekan di Langkah Uji; spec menambah langkah memilih "Authenticator app" yang harus berujung pada Enrollment Authenticator. (3) Post Condition "percobaan dihitung sebagai satu percobaan salah terhadap batas 5" (TC-AUTH-MFA-86, 104, 124) dan "hitungan resend sesi pre-auth ini 0 atau 1" serta "Hanya satu kode OTP aktif" (TC-AUTH-MFA-85, 214) tidak punya cara pengecekan di Langkah Uji dan tidak diasersi. (4) TC-AUTH-MFA-85 dan TC-AUTH-MFA-214 butir "kode pertama tetap berlaku" tidak punya cara pengecekan; spec memakai kode pertama pada TC-AUTH-MFA-85 dan, pada TC-AUTH-MFA-214, hanya memeriksa tidak adanya email baru (kode pertama baru dipakai setelah Resend kedua diterima untuk memeriksa butir d). (5) TC-AUTH-MFA-124 mencantumkan akun Total Control di Precondition tetapi Langkah Uji 7 tidak menyebut User Log dan tidak menyebut penanda waktu; spec memakai Activity Log > Session dan User Log dengan baseline penanda waktu sebelum request langsung. Mekanisme seeding state BE (trusted device, Authenticator terdaftar, profil FIRST) belum ada di Pre-setup TC (#20/#21). (6) TC-AUTH-MFA-85 butir b dan TC-AUTH-MFA-214 butir b "hitungan resend tidak bertambah" tidak punya cara membaca hitungan di Langkah Uji; spec hanya mengeceknya lewat jumlah email di mail-catcher (sama dengan baseline). (7) TC-AUTH-MFA-214 Post Condition "tidak ada sesi penuh" tidak punya Expected padanan atau langkah observasi di Langkah Uji dan tidak diasersi.
