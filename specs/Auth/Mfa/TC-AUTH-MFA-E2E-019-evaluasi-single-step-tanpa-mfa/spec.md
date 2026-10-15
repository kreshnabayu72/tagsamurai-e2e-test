---
id: TC-AUTH-MFA-E2E-019-evaluasi-single-step-tanpa-mfa
title: "Evaluasi Single-Step Tanpa Pemicu MFA"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-MFA-22
  - TC-AUTH-MFA-23
  - TC-AUTH-MFA-34
  - TC-AUTH-MFA-148
coverage:
  web: automated
---

# Evaluasi Single-Step Tanpa Pemicu MFA

## Prerequisites

- Mode: FE+BE.
- Suite berjalan serial (`parallel: false`) karena spec ini mengubah IP uji (lokasi koneksi login ke Jakarta, Bekasi, dan Subang); hook `after` memulihkan IP uji ke IP default lingkungan uji.
- Seeding (hook `before`, lewat API oleh akun aktor Total Control (Global Settings) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.GS_TC_PASSWORD`): empat user berpassword `Spectra.env.MFA_PASSWORD`, email bersuffix per run. Kondisi yang di-seed BE untuk semua user: Activated, Active ON, sudah pernah login sukses di web dari browser uji A (ID device browser uji A terdaftar sebagai trusted device web), login terakhir dari IP uji Jakarta (ID), logout web terakhir kurang dari 30 hari, Authenticator sudah terdaftar, persetujuan Privacy Policy versi terbaru sudah tersimpan:
  - TC-AUTH-MFA-22: `Intan Maharani` (`intanmaharani+{runId}-019@qwertysystem.net`), profil BASE (Tabel Data Uji Pre-setup #2).
  - TC-AUTH-MFA-23: `Gilang Ramadhan` (`gilangramadhan+{runId}-019@qwertysystem.net`), profil BASE.
  - TC-AUTH-MFA-34: `Dian Puspita` (`dianpuspita+{runId}-019@qwertysystem.net`), profil NEAR (Tabel Data Uji Pre-setup #8; seperti BASE).
  - TC-AUTH-MFA-148: `Luthfi Hakim` (`luthfihakim+{runId}-019@qwertysystem.net`), profil BASE.
- Hook `after`: kembalikan IP uji ke IP default lingkungan uji, lalu hapus keempat user. Pembersihan tidak berasumsi seeding berhasil penuh.
- Akun yang dipakai: tanpa login (halaman publik; tidak ada sesi aktif di browser) untuk semua TC. Tiap TC setelah yang pertama dimulai di jendela baru browser uji A tanpa sesi login; TC pertama berjalan di browser awal.
- Environment variable: `GS_TC_PASSWORD`, `MFA_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Kemampuan teknis:
  - Seeding state BE per user: trusted device (ID device browser uji A), lokasi dan waktu login terakhir (Jakarta (ID)), `last_logout_at` kurang dari 30 hari, Authenticator terdaftar, dan persetujuan Privacy Policy; mekanisme seeding (endpoint/skrip uji) disediakan tim FE/BE karena tidak didefinisikan di TC, PRD, atau LLD.
  - Browser uji A: konteks browser dengan cookie ID device persisten; setiap TC memakai konteks baru dengan ID device yang didaftarkan sebagai trusted device user TC itu.
  - IP uji: IP sumber permintaan login dapat ditetapkan ke IP uji geo-IP Jakarta (ID), Bekasi (ID), atau Subang (ID) (Tabel Data Uji Pre-setup #19).
  - Mail-catcher lingkungan uji untuk membaca email OTP login (TC-AUTH-MFA-23) dan memastikan tidak ada email alert "New sign-in to your TAG Samurai account" (TC-AUTH-MFA-22, 23, 34). Asersi email memakai baseline jumlah email alert untuk alamat user yang dicatat sebelum login.
  - reCAPTCHA mode uji di environment.

## Test Steps

### TC-AUTH-MFA-22: Login with Password tanpa pemicu MFA berakhir single-step

1. Atur IP uji ke Jakarta (ID)
2. Catat jumlah email dengan subject "New sign-in to your TAG Samurai account" di mail-catcher untuk `intanmaharani+{runId}-019@qwertysystem.net` sebagai baseline
3. Buka halaman `Auth > Login with Password` di browser uji A → halaman Login with Password tampil
4. Ketik `intanmaharani+{runId}-019@qwertysystem.net` pada field Email
5. Ketik `Spectra.env.MFA_PASSWORD` pada field Password
6. Centang widget reCAPTCHA "I'm not a robot"
7. Klik button [Log in]
8. Amati halaman setelah klik [Log in]
9. Verifikasi Halaman Choose Verification Method, OTP Verification, Authenticator Verification, dan Enrollment tidak tampil
10. Verifikasi Browser dialihkan ke Portal — Product Hub
11. Verifikasi Sesi web aktif untuk `Intan Maharani` (teramati dari Portal — Product Hub yang tampil untuk akun ini)
12. Periksa mail-catcher lingkungan uji untuk `intanmaharani+{runId}-019@qwertysystem.net`
13. Verifikasi Tidak ada email alert "New sign-in to your TAG Samurai account" di mail-catcher untuk `intanmaharani+{runId}-019@qwertysystem.net` (jumlah sama dengan baseline langkah 2)

### TC-AUTH-MFA-23: Login with OTP tanpa pemicu MFA berakhir single-step

14. Tutup jendela user uji dari TC sebelumnya dan hapus sesi login browser terkait (ID device dan jendela sesi akun aktor tetap), lalu buka jendela baru browser uji A (konteks bersih tanpa sesi login)
15. Atur IP uji ke Jakarta (ID)
16. Catat jumlah email dengan subject "New sign-in to your TAG Samurai account" di mail-catcher untuk `gilangramadhan+{runId}-019@qwertysystem.net` sebagai baseline
17. Buka halaman `Auth > Login with OTP > Request OTP` di browser uji A → halaman Request OTP tampil
18. Ketik `gilangramadhan+{runId}-019@qwertysystem.net` pada field Email
19. Centang widget reCAPTCHA "I'm not a robot"
20. Klik button [Request OTP] → halaman Verify OTP tampil
21. Ketik 6 digit kode OTP login dari email `gilangramadhan+{runId}-019@qwertysystem.net` pada kotak digit
22. Amati halaman setelah digit ke-6 terisi
23. Verifikasi Halaman MFA tidak tampil
24. Verifikasi Browser dialihkan ke Portal — Product Hub
25. Verifikasi Sesi web aktif untuk `Gilang Ramadhan` (teramati dari Portal — Product Hub yang tampil untuk akun ini)
26. Periksa mail-catcher lingkungan uji untuk `gilangramadhan+{runId}-019@qwertysystem.net`
27. Verifikasi Tidak ada email alert "New sign-in to your TAG Samurai account" di mail-catcher untuk `gilangramadhan+{runId}-019@qwertysystem.net` (jumlah sama dengan baseline langkah 16)

### TC-AUTH-MFA-34: Login dari lokasi kurang dari 100 km dengan negara sama tidak memicu MFA

28. Tutup jendela user uji dari TC sebelumnya dan hapus sesi login browser terkait (ID device dan jendela sesi akun aktor tetap), lalu buka jendela baru browser uji A (konteks bersih tanpa sesi login)
29. Atur IP uji ke Bekasi (ID)
30. Catat jumlah email dengan subject "New sign-in to your TAG Samurai account" di mail-catcher untuk `dianpuspita+{runId}-019@qwertysystem.net` sebagai baseline
31. Buka halaman `Auth > Login with Password` di browser uji A → halaman Login with Password tampil
32. Ketik `dianpuspita+{runId}-019@qwertysystem.net` pada field Email
33. Ketik `Spectra.env.MFA_PASSWORD` pada field Password
34. Centang widget reCAPTCHA "I'm not a robot"
35. Klik button [Log in]
36. Amati halaman setelah klik [Log in]
37. Verifikasi Halaman MFA tidak tampil
38. Verifikasi Browser dialihkan ke Portal — Product Hub
39. Periksa mail-catcher lingkungan uji untuk `dianpuspita+{runId}-019@qwertysystem.net`
40. Verifikasi Tidak ada email alert "New sign-in to your TAG Samurai account" di mail-catcher untuk `dianpuspita+{runId}-019@qwertysystem.net` (jumlah sama dengan baseline langkah 30)

### TC-AUTH-MFA-148: Login single-step yang berhasil memperbarui lokasi login terakhir tanpa menambah trusted device

41. Tutup jendela user uji dari TC sebelumnya dan hapus sesi login browser terkait (ID device dan jendela sesi akun aktor tetap), lalu buka jendela baru browser uji A (konteks bersih tanpa sesi login)
42. Atur IP uji ke Jakarta (ID)
43. Buka halaman `Auth > Login with Password` di browser uji A → halaman Login with Password tampil
44. Ketik `luthfihakim+{runId}-019@qwertysystem.net` pada field Email
45. Ketik `Spectra.env.MFA_PASSWORD` pada field Password
46. Centang widget reCAPTCHA "I'm not a robot"
47. Klik button [Log in] → Portal — Product Hub tampil
48. Logout dari akun `Luthfi Hakim`
49. Atur IP uji ke Bekasi (ID, kurang dari 100 km dari Jakarta)
50. Buka halaman `Auth > Login with Password` di browser uji A → halaman Login with Password tampil
51. Ketik `luthfihakim+{runId}-019@qwertysystem.net` pada field Email
52. Ketik `Spectra.env.MFA_PASSWORD` pada field Password
53. Centang widget reCAPTCHA "I'm not a robot"
54. Klik button [Log in] → Portal — Product Hub tampil (single-step)
55. Logout dari akun `Luthfi Hakim`
56. Atur IP uji ke Subang (ID, sekitar 92 km dari Bekasi dan sekitar 114 km dari Jakarta)
57. Buka halaman `Auth > Login with Password` di browser uji A → halaman Login with Password tampil
58. Ketik `luthfihakim+{runId}-019@qwertysystem.net` pada field Email
59. Ketik `Spectra.env.MFA_PASSWORD` pada field Password
60. Centang widget reCAPTCHA "I'm not a robot"
61. Klik button [Log in]
62. Amati halaman setelah klik [Log in]
63. Verifikasi Halaman MFA tidak tampil
64. Verifikasi Portal — Product Hub tampil (jarak Subang dihitung terhadap Bekasi, lokasi login terakhir yang diperbarui oleh login single-step; Subang-Jakarta lebih dari 100 km tetapi tidak dipakai sebagai baseline)

## Notes

- Sumber: `auth/mfa/TestCases/tc-mfa.md`. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Langkah pembuka tiap TC sesudah TC pertama menutup jendela user uji dari TC sebelumnya dan menghapus sesi login browser terkait (ID device dan jendela sesi akun aktor tetap) sebelum jendela baru dibuka; itu langkah penghubung tanpa `Verifikasi` (S-03, S-09).
- Langkah penghubung tanpa awalan `Verifikasi` (buka jendela baru browser uji A, atur IP uji, catat baseline email, logout pada TC-AUTH-MFA-148) bukan asersi tambahan (S-03). Langkah 47 dan 54 memakai panah hasil (Portal tampil) sebagai kondisi perantara yang dinyatakan Langkah Uji TC, bukan asersi baru. Langkah 2, 16, dan 30 mencatat baseline jumlah email alert (S-12) supaya "tidak ada email alert" diasersi sebagai tidak bertambah, bukan sekadar daftar kosong.
- Sesi teramati lewat halaman yang tampil: sesi web aktif = Portal — Product Hub tampil (langkah 11 dan 25 merinci klausa "sesi web aktif untuk user" pada Expected b TC-AUTH-MFA-22 dan 23); tidak adanya sesi pre-auth = halaman MFA tidak tampil. Post Condition sesi tidak diasersi terpisah.
- Jumlah langkah melewati ±35 karena empat TC independen dengan prefix login faktor-1 yang identik (tidak dihitung) dan TC-AUTH-MFA-148 yang berisi tiga login berurutan; spec tidak dipecah.
- Temuan untuk QA:
  1. TC-AUTH-MFA-148 Langkah Uji tidak menyebut IP uji login pertama; spec memakai Jakarta (ID) sesuai Data Uji ("IP uji berurutan: Jakarta, Bekasi, Subang") dan profil BASE.
  2. Post Condition berupa state BE tidak diasersi (S-01, S-15): TC-AUTH-MFA-22 dan TC-AUTH-MFA-34 "Satu sesi web aktif ...; tidak ada sesi pre-auth MFA" (teramati lewat Expected: Portal tampil dan halaman MFA tidak tampil), TC-AUTH-MFA-22 butir b "Entri Success `Login with password` ditulis oleh faktor-1 (modul login-password), bukan oleh MFA" dan TC-AUTH-MFA-23 "Satu sesi web aktif; entri Success `Login with OTP` ditulis oleh faktor-1 (modul login-otp)" (asersi pencatatan lintas surface log tanpa Expected padanan maupun langkah observasi di TC), TC-AUTH-MFA-148 "Daftar trusted device `Luthfi Hakim` tidak bertambah dari login single-step" (tanpa langkah observasi di TC maupun surface UI yang dinyatakan). QA menambah Expected atau langkah observasi di TC bila Post Condition itu harus diuji.
  3. TC-AUTH-MFA-22 dan 23 tidak menyebut kondisi persetujuan Privacy Policy; spec menganggap sudah tersimpan karena Expected langsung ke Portal.
  4. Mekanisme seeding state BE (trusted device ber-ID device browser uji A, lokasi dan waktu login terakhir, `last_logout_at`, Authenticator terdaftar, consent) belum ada di Tabel Data Uji Pre-setup (#20 dan #21 hanya memuat manipulasi jam server dan seed `last_logout_at`, pasangan negara, `first_login_at`, serta failure injection); tim FE/BE menyediakan dan QA melengkapi Pre-setup.
