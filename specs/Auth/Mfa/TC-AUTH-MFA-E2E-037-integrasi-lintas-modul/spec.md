---
id: TC-AUTH-MFA-E2E-037-integrasi-lintas-modul
title: "Integrasi MFA dengan Reset Password dan Redirect Portal"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-MFA-175
  - TC-AUTH-MFA-176
  - TC-AUTH-MFA-178
coverage:
  web: automated
---

# Integrasi MFA dengan Reset Password dan Redirect Portal

## Prerequisites

- Mode: FE+BE.
- Seeding (hook `before`, lewat API oleh akun aktor Total Control (Global Settings) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.GS_TC_PASSWORD`): tiga user, password awal `Spectra.env.MFA_PASSWORD`, email bersuffix per run:
  - TC-AUTH-MFA-175: `Nur Santoso` (`nursantoso+{runId}-037@qwertysystem.net`), profil NEWDEVE (Tabel Data Uji Pre-setup #5: Activated, Active ON, seperti BASE tetapi ID device browser uji B belum ada di daftar trusted device, Authenticator sudah terdaftar; secret-nya dimuat ke aplikasi authenticator uji)
  - TC-AUTH-MFA-176: `Agus Santoso` (`agussantoso+{runId}-037@qwertysystem.net`), profil BASE (Tabel Data Uji Pre-setup #2: Activated, Active ON, device browser uji A dikenali sebagai trusted device, sudah pernah login sukses, logout web terakhir kurang dari 30 hari, Authenticator sudah terdaftar)
  - TC-AUTH-MFA-178: `Fajar Santoso` (`fajarsantoso+{runId}-037@qwertysystem.net`), profil NEWDEVE
- Hook `after`: hapus ketiga user. Hook ini tetap jalan walau spec gagal di tengah dan tidak berasumsi seeding berhasil penuh.
- Akun yang dipakai: tanpa login (halaman publik; tidak ada sesi aktif di browser) untuk semua TC; tiap TC dimulai di konteks browser baru tanpa sesi login.
- Environment variable: `GS_TC_PASSWORD`, `MFA_PASSWORD` (password awal), `MFA_PASSWORD_NEW` (password baru hasil Reset Password; memenuhi Password Policy). Password tidak ditulis di spec atau fixture.
- Kemampuan teknis:
  - Mail-catcher lingkungan uji untuk membaca email Reset Password dan membuka tautan resetnya (TC-AUTH-MFA-175, 176); alur Reset Password (modul Reset Password: halaman Reset Password, Email Sent!, Setup New Password, Password Reset Successful) tersedia di environment.
  - Aplikasi authenticator uji (TOTP: SHA-1, 6 digit, periode 30 detik) untuk TC-AUTH-MFA-175 dan 178.
  - Browser uji B (ID device belum dikenali), browser uji C (device baru tambahan), dan browser uji A (ID device dikenali untuk `Agus Santoso`) sebagai konteks browser terpisah dengan ID device persisten sendiri; konteks browser uji B dipakai ulang di dalam TC-AUTH-MFA-175.
  - reCAPTCHA mode uji di environment.
  - Seeding state BE per user: trusted device ber-ID device browser uji A (`Agus Santoso`) atau tanpa ID device browser uji B (`Nur Santoso`, `Fajar Santoso`), riwayat login sukses dan waktu logout web terakhir (`Agus Santoso`), dan Authenticator terdaftar dengan secret yang dikenal aplikasi authenticator uji; mekanisme seeding (endpoint/skrip uji) disediakan tim FE/BE karena tidak didefinisikan di TC, PRD, atau LLD.

## Test Steps

### TC-AUTH-MFA-175: Reset Password berhasil tidak memengaruhi trust device dan enrollment MFA

1. Buka browser uji B (ID device belum dikenali) sebagai jendela baru tanpa sesi login
2. Buka halaman `Auth > Login with Password` di browser → halaman Login with Password tampil
3. Ketik `nursantoso+{runId}-037@qwertysystem.net` pada field Email
4. Ketik `Spectra.env.MFA_PASSWORD` pada field Password
5. Centang widget reCAPTCHA "I'm not a robot"
6. Klik button [Log in] → halaman `Auth > MFA > Choose Verification Method` tampil
7. Pilih opsi "Authenticator app" pada halaman Choose Verification Method
8. Klik button [Login] → halaman `Auth > MFA > Authenticator Verification` tampil
9. Ketik 6 digit kode TOTP valid dari aplikasi authenticator uji untuk `nursantoso+{runId}-037@qwertysystem.net` pada kotak digit lalu klik [Login] → Portal — Product Hub tampil
10. Logout dari Portal — Product Hub
11. Buka halaman `Auth > Reset Password` di browser → halaman Reset Password tampil
12. Ketik `nursantoso+{runId}-037@qwertysystem.net` pada field Email
13. Centang widget reCAPTCHA "I'm not a robot"
14. Klik button [Reset Password] → halaman Email Sent! tampil
15. Buka email reset yang masuk ke `nursantoso+{runId}-037@qwertysystem.net` di mail-catcher
16. Klik tautan reset di dalam email → halaman Setup New Password tampil
17. Ketik `Spectra.env.MFA_PASSWORD_NEW` pada field Password dan field Confirm Password
18. Klik button [Reset Password] → halaman Password Reset Successful tampil
19. Buka kembali browser uji B (konteks yang sama dengan langkah 1, ID device sama) dan buka halaman `Auth > Login with Password` → halaman Login with Password tampil
20. Ketik `nursantoso+{runId}-037@qwertysystem.net` pada field Email
21. Ketik `Spectra.env.MFA_PASSWORD_NEW` pada field Password
22. Centang widget reCAPTCHA "I'm not a robot"
23. Klik button [Log in]
24. Amati halaman setelah klik [Log in]
25. Verifikasi Halaman MFA tidak tampil (trust device tetap)
26. Verifikasi Portal — Product Hub tampil
27. Logout dari Portal — Product Hub
28. Tutup jendela user uji dari TC sebelumnya dan hapus sesi login browser terkait (ID device dan jendela sesi akun aktor tetap), lalu buka browser uji C (device baru) sebagai jendela baru tanpa sesi login
29. Buka halaman `Auth > Login with Password` di browser → halaman Login with Password tampil
30. Ketik `nursantoso+{runId}-037@qwertysystem.net` pada field Email
31. Ketik `Spectra.env.MFA_PASSWORD_NEW` pada field Password
32. Centang widget reCAPTCHA "I'm not a robot"
33. Klik button [Log in] → halaman `Auth > MFA > Choose Verification Method` tampil
34. Pilih opsi "Authenticator app" pada halaman Choose Verification Method
35. Klik button [Login]
36. Verifikasi Halaman `Auth > MFA > Authenticator Verification` tampil
37. Verifikasi Halaman Enrollment Authenticator tidak tampil
38. Verifikasi Authenticator `Nur Santoso` tetap terdaftar (teramati dari halaman Authenticator Verification pada langkah 36)

### TC-AUTH-MFA-176: Login pertama setelah Reset Password bukan login pertama bagi user yang sudah pernah login sukses

39. Tutup jendela user uji dari TC sebelumnya dan hapus sesi login browser terkait (ID device dan jendela sesi akun aktor tetap), lalu buka browser uji A (ID device dikenali) sebagai jendela baru tanpa sesi login
40. Buka halaman `Auth > Reset Password` di browser → halaman Reset Password tampil
41. Ketik `agussantoso+{runId}-037@qwertysystem.net` pada field Email
42. Centang widget reCAPTCHA "I'm not a robot"
43. Klik button [Reset Password] → halaman Email Sent! tampil
44. Buka email reset yang masuk ke `agussantoso+{runId}-037@qwertysystem.net` di mail-catcher
45. Klik tautan reset di dalam email → halaman Setup New Password tampil
46. Ketik `Spectra.env.MFA_PASSWORD_NEW` pada field Password dan field Confirm Password
47. Klik button [Reset Password] → halaman Password Reset Successful tampil
48. Buka halaman `Auth > Login with Password` di browser → halaman Login with Password tampil
49. Ketik `agussantoso+{runId}-037@qwertysystem.net` pada field Email
50. Ketik `Spectra.env.MFA_PASSWORD_NEW` pada field Password
51. Centang widget reCAPTCHA "I'm not a robot"
52. Klik button [Log in]
53. Verifikasi Halaman MFA tidak tampil (bukan login pertama; device dikenali)
54. Verifikasi Portal — Product Hub tampil
55. Logout dari Portal — Product Hub

### TC-AUTH-MFA-178: Redirect login final MFA mendarat di Portal — Product Hub bukan Dashboard

56. Tutup jendela user uji dari TC sebelumnya dan hapus sesi login browser terkait (ID device dan jendela sesi akun aktor tetap), lalu buka browser uji B (ID device belum dikenali) sebagai jendela privat baru tanpa sesi login
57. Buka halaman `Auth > Login with Password` di browser → halaman Login with Password tampil
58. Ketik `fajarsantoso+{runId}-037@qwertysystem.net` pada field Email
59. Ketik `Spectra.env.MFA_PASSWORD` pada field Password
60. Centang widget reCAPTCHA "I'm not a robot"
61. Klik button [Log in] → halaman `Auth > MFA > Choose Verification Method` tampil
62. Pilih opsi "Authenticator app" pada halaman Choose Verification Method
63. Klik button [Login] → halaman `Auth > MFA > Authenticator Verification` tampil
64. Ketik 6 digit kode TOTP valid dari aplikasi authenticator uji untuk `fajarsantoso+{runId}-037@qwertysystem.net` pada kotak digit lalu klik [Login]
65. Verifikasi Browser dialihkan ke Portal — Product Hub
66. Verifikasi Halaman yang tampil bukan halaman Dashboard produk

## Notes

- Sumber: `auth/mfa/TestCases/tc-mfa.md`. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Langkah pembuka tiap TC sesudah TC pertama menutup jendela user uji dari TC sebelumnya dan menghapus sesi login browser terkait (ID device dan jendela sesi akun aktor tetap) sebelum jendela baru dibuka; itu langkah penghubung tanpa `Verifikasi` (S-03, S-09).
- Kelas harness d (mail-catcher untuk email Reset Password). Langkah Reset Password (langkah 11-18 dan 40-47) disalin dari `auth/reset-password/TestCases/tc-reset-password.md`: request dari TC-AUTH-RST-12 (langkah 1-5: buka halaman Reset Password, ketik Email, centang reCAPTCHA, klik [Reset Password], buka email di mail-catcher) dan submit password baru dari TC-AUTH-RST-82 (langkah 1-3: buka tautan reset dari email, ketik password baru pada Password dan Confirm Password, klik [Reset Password]). Langkah observasi log TC-AUTH-RST-82 (langkah 4) dan asersi Expected kedua TC itu dimiliki modul Reset Password dan tidak diulang di sini; spec ini hanya memakai halaman antara sebagai penanda alur.
- Urutan mengikuti TC sumber. Tiap TC memakai user sendiri dan konteks browser sendiri, jadi urutan antar TC tidak saling bergantung.
- Langkah penghubung tanpa awalan `Verifikasi` (S-03): logout pada langkah 10, 27, dan 55 mengembalikan konteks browser ke tanpa sesi sebelum langkah berikutnya; langkah 19 membuka kembali konteks browser uji B yang sama dengan langkah 1 agar ID device sama (inti asersi trust device pada langkah 25 dan 26); langkah 24 (amati halaman) mengikuti Langkah Uji 11 TC.
- Melewati ±35 langkah karena alur Reset Password disalin utuh (S-04) di dua TC; ketiga TC independen (user dan konteks browser sendiri) dan langkah prefix login faktor-1 tidak dihitung, jadi spec tidak dipecah.
- Post Condition TC-AUTH-MFA-176 dan 178 "Satu sesi web aktif" tidak diasersi terpisah; sesi web teramati sebagai Portal — Product Hub tampil (langkah 54 dan 65). Post Condition TC-AUTH-MFA-175 "Trust device dan enrollment tidak berubah" terwakili Expected a dan b (langkah 25, 26, dan 36 sampai 38).
- Temuan untuk QA:
  - TC-AUTH-MFA-175, 176, 178 menulis "password valid `Nama User`" dan "password baru" tanpa nilai; spec memakai `Spectra.env.MFA_PASSWORD` untuk password awal dan `Spectra.env.MFA_PASSWORD_NEW` untuk password baru.
  - TC-AUTH-MFA-175 Langkah Uji 12 memakai browser uji C (device baru) setelah Langkah Uji 10 memakai browser uji B; Data Uji hanya menyebut browser uji B. Spec mengikuti Langkah Uji.
  - TC-AUTH-MFA-176 Langkah Uji tidak memuat login awal; kondisi "sudah pernah login sukses" dan trusted device browser uji A di-seed BE (profil BASE).
  - TC-AUTH-MFA-175 dan 176 menulis "Selesaikan Reset Password" tanpa memerinci langkahnya; spec memakai langkah TC-AUTH-RST-12 dan TC-AUTH-RST-82 dari modul Reset Password.
  - Post Condition berupa state BE tidak diasersi (aturan Post Condition): TC-AUTH-MFA-176 dan 178 "Satu sesi web aktif untuk `<user>`", TC-AUTH-MFA-175 "Trust device dan enrollment `Nur Santoso` tidak berubah". Padanan teramati ada di Expected (Portal — Product Hub tampil; halaman MFA tidak tampil; Authenticator Verification tampil bukan Enrollment).
  - Mekanisme seeding state BE (trusted device ber-ID device, Authenticator dengan secret dikenal, riwayat login) belum ada di Pre-setup TC (#20/#21); lihat Kemampuan teknis.
