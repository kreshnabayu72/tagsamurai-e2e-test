---
id: TC-AUTH-MFA-E2E-020-pemicu-mfa-login-pertama
title: "Pemicu MFA pada Login Pertama"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-MFA-24
  - TC-AUTH-MFA-25
  - TC-AUTH-MFA-149
coverage:
  web: automated
---

# Pemicu MFA pada Login Pertama

## Prerequisites

- Mode: FE+BE.
- Seeding (hook `before`, lewat API oleh akun aktor Total Control (Global Settings) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.GS_TC_PASSWORD`): tiga user profil FIRST (Tabel Data Uji Pre-setup #3: Activated, Active ON, belum pernah menyelesaikan login di platform mana pun, Authenticator belum terdaftar, tanpa trusted device), password `Spectra.env.MFA_PASSWORD`, email bersuffix per run:
  - TC-AUTH-MFA-24: `Sari Utami` (`sariutami+{runId}-020@qwertysystem.net`)
  - TC-AUTH-MFA-25: `Joko Susilo` (`jokosusilo+{runId}-020@qwertysystem.net`)
  - TC-AUTH-MFA-149: `Melati Wangi` (`melatiwangi+{runId}-020@qwertysystem.net`)
- Hook `after`: hapus ketiga user. Pembersihan tidak berasumsi seeding berhasil penuh.
- Akun yang dipakai: tanpa login (halaman publik; tidak ada sesi aktif di browser) untuk semua TC. Tiap TC setelah yang pertama dimulai di jendela baru browser uji A tanpa sesi login; TC pertama berjalan di browser awal.
- Environment variable: `GS_TC_PASSWORD`, `MFA_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Kemampuan teknis:
  - Browser uji A: konteks browser dengan cookie ID device persisten yang belum ada di daftar trusted device user (belum pernah login); setiap TC memakai konteks baru. IP uji tidak diubah selama spec (IP uji yang sama pada semua login, termasuk dua login `Melati Wangi`).
  - Mail-catcher lingkungan uji untuk membaca kode OTP login (TC-AUTH-MFA-25) dan memastikan tidak ada email alert "New sign-in to your TAG Samurai account". Asersi email memakai baseline jumlah email alert untuk alamat user yang dicatat sebelum login.
  - Aplikasi authenticator uji (TOTP: SHA-1, 6 digit, periode 30 detik) yang dapat memindai QR code Enrollment dan menghasilkan kode (TC-AUTH-MFA-149); jam aplikasi authenticator uji sama dengan jam server uji.
  - reCAPTCHA mode uji di environment.
- Semua user berprofil FIRST, jadi login pertama melewati layar Confirm to Continue sebelum halaman MFA.

## Test Steps

### TC-AUTH-MFA-24: Login pertama via Login with Password mewajibkan MFA tanpa email alert

1. Catat jumlah email dengan subject "New sign-in to your TAG Samurai account" di mail-catcher untuk `sariutami+{runId}-020@qwertysystem.net` sebagai baseline
2. Buka halaman `Auth > Login with Password` di browser uji A → halaman Login with Password tampil
3. Ketik `sariutami+{runId}-020@qwertysystem.net` pada field Email
4. Ketik `Spectra.env.MFA_PASSWORD` pada field Password
5. Centang widget reCAPTCHA "I'm not a robot"
6. Klik button [Log in] → layar Confirm to Continue tampil
7. Centang checkbox persetujuan, lalu klik [Continue ➔]
8. Amati halaman setelah klik [Continue ➔]
9. Verifikasi Halaman `Auth > MFA > Choose Verification Method` tampil (MFA wajib karena login pertama)
10. Periksa mail-catcher lingkungan uji untuk `sariutami+{runId}-020@qwertysystem.net`
11. Verifikasi Tidak ada email alert "New sign-in to your TAG Samurai account" di mail-catcher untuk `sariutami+{runId}-020@qwertysystem.net` (jumlah sama dengan baseline langkah 1; login pertama tidak dievaluasi sebagai login tak biasa)

### TC-AUTH-MFA-25: Login pertama via Login with OTP mewajibkan MFA langsung ke Enrollment tanpa email alert

12. Tutup jendela user uji dari TC sebelumnya dan hapus sesi login browser terkait (ID device dan jendela sesi akun aktor tetap), lalu buka jendela baru browser uji A (konteks bersih tanpa sesi login)
13. Catat jumlah email dengan subject "New sign-in to your TAG Samurai account" di mail-catcher untuk `jokosusilo+{runId}-020@qwertysystem.net` sebagai baseline
14. Buka halaman `Auth > Login with OTP > Request OTP` di browser uji A → halaman Request OTP tampil
15. Ketik `jokosusilo+{runId}-020@qwertysystem.net` pada field Email
16. Centang widget reCAPTCHA "I'm not a robot"
17. Klik button [Request OTP] → halaman Verify OTP tampil
18. Ketik 6 digit kode OTP login dari email `jokosusilo+{runId}-020@qwertysystem.net` pada kotak digit → layar Confirm to Continue tampil
19. Centang checkbox persetujuan, lalu klik [Continue ➔]
20. Amati halaman setelah klik [Continue ➔]
21. Verifikasi Halaman Choose Verification Method tidak tampil
22. Verifikasi Halaman `Auth > MFA > Enrollment Authenticator` tampil langsung (login pertama, Authenticator belum terdaftar)
23. Periksa mail-catcher lingkungan uji untuk `jokosusilo+{runId}-020@qwertysystem.net`
24. Verifikasi Tidak ada email alert "New sign-in to your TAG Samurai account" di mail-catcher untuk `jokosusilo+{runId}-020@qwertysystem.net` (jumlah sama dengan baseline langkah 13)

### TC-AUTH-MFA-149: Setelah login final pertama, user tidak lagi dianggap login pertama

25. Tutup jendela user uji dari TC sebelumnya dan hapus sesi login browser terkait (ID device dan jendela sesi akun aktor tetap), lalu buka jendela baru browser uji A (konteks bersih tanpa sesi login)
26. Buka halaman `Auth > Login with Password` di browser uji A → halaman Login with Password tampil
27. Ketik `melatiwangi+{runId}-020@qwertysystem.net` pada field Email
28. Ketik `Spectra.env.MFA_PASSWORD` pada field Password
29. Centang widget reCAPTCHA "I'm not a robot"
30. Klik button [Log in] → layar Confirm to Continue tampil
31. Centang checkbox persetujuan, lalu klik [Continue ➔] → halaman `Auth > MFA > Choose Verification Method` tampil
32. Pilih opsi "Authenticator app" pada halaman Choose Verification Method
33. Klik button [Login] → halaman `Auth > MFA > Enrollment Authenticator` tampil
34. Pindai QR code dengan aplikasi authenticator uji
35. Ketik kode TOTP valid dari aplikasi authenticator uji pada kotak digit
36. Klik button [Verify] → Portal — Product Hub tampil
37. Logout dari akun `Melati Wangi`
38. Buka halaman `Auth > Login with Password` di browser uji A → halaman Login with Password tampil
39. Ketik `melatiwangi+{runId}-020@qwertysystem.net` pada field Email
40. Ketik `Spectra.env.MFA_PASSWORD` pada field Password
41. Centang widget reCAPTCHA "I'm not a robot"
42. Klik button [Log in]
43. Amati halaman setelah klik [Log in]
44. Verifikasi Halaman MFA tidak tampil
45. Verifikasi Portal — Product Hub tampil (bukan login pertama; browser uji A di-trust)

## Notes

- Sumber: `auth/mfa/TestCases/tc-mfa.md`. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Langkah pembuka tiap TC sesudah TC pertama menutup jendela user uji dari TC sebelumnya dan menghapus sesi login browser terkait (ID device dan jendela sesi akun aktor tetap) sebelum jendela baru dibuka; itu langkah penghubung tanpa `Verifikasi` (S-03, S-09).
- Langkah penghubung tanpa awalan `Verifikasi` (buka jendela baru browser uji A, catat baseline email, logout pada TC-AUTH-MFA-149) bukan asersi tambahan (S-03). Langkah 1 dan 13 mencatat baseline jumlah email alert (S-12) supaya "tidak ada email alert" diasersi sebagai tidak bertambah.
- Penggantian langkah amati (S-15): langkah 8 (TC-AUTH-MFA-24) dan langkah 20 (TC-AUTH-MFA-25) mengamati halaman setelah klik [Continue ➔], bukan "setelah klik [Log in]" atau "setelah digit ke-6 terisi" seperti Langkah Uji TC, karena pada titik itu yang tampil adalah layar Confirm to Continue (lihat Temuan untuk QA 1).
- Urutan TC mengikuti TC sumber; TC-AUTH-MFA-149 ditaruh terakhir karena membuat sesi penuh dan trusted device (S-10).
- Sesi teramati lewat halaman yang tampil: sesi pre-auth MFA = halaman MFA (Choose Verification Method atau Enrollment Authenticator) tampil. Post Condition sesi tidak diasersi terpisah.
- Post Condition TC-AUTH-MFA-149 ("`Melati Wangi` ditandai pernah login sukses di platform web") dibuktikan lewat Expected (login ulang tanpa MFA), tidak diasersi terpisah.
- Temuan untuk QA:
  1. TC-AUTH-MFA-24 dan 25 Langkah Uji menaruh "amati halaman setelah klik [Log in]" (24) atau "digit ke-6 terisi" (25) sebelum/di luar layar Confirm to Continue; spec mengamati halaman setelah klik [Continue ➔] (langkah 8 dan 20).
  2. TC-AUTH-MFA-149 tidak menyebut IP uji untuk kedua login; spec memakai IP uji yang sama.
  3. TC-AUTH-MFA-149 tidak menyebut layar Confirm to Continue pada login ulang; spec mengikuti Expected (langsung ke Portal).
  4. Post Condition berupa state BE tidak diasersi (S-01, S-15): TC-AUTH-MFA-24 "Sesi pre-auth MFA aktif untuk `Sari Utami`; tidak ada sesi penuh" dan TC-AUTH-MFA-25 "Sesi pre-auth MFA aktif untuk `Joko Susilo`; enrollment belum aktif" (sesi pre-auth teramati lewat halaman MFA tampil pada Expected; "tidak ada sesi penuh" dan "enrollment belum aktif" tanpa langkah observasi di TC). QA menambah Expected atau langkah observasi di TC bila Post Condition itu harus diuji.
