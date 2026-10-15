---
id: TC-AUTH-MFA-E2E-021-pemicu-mfa-idle-30-hari
title: "Pemicu MFA Setelah Idle 30 Hari"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-MFA-26
  - TC-AUTH-MFA-27
  - TC-AUTH-MFA-28
  - TC-AUTH-MFA-59
  - TC-AUTH-MFA-52
coverage:
  web: automated
---

# Pemicu MFA Setelah Idle 30 Hari

## Prerequisites

- Mode: FE+BE.
- Suite berjalan serial (`parallel: false`) karena spec ini mengubah jam server uji (dibekukan di T0) dan IP uji (lokasi koneksi login ditetapkan ke Jakarta (ID)); hook `after` memulihkan jam server uji ke waktu nyata dan IP uji ke IP default lingkungan uji.
- Seeding (hook `before`, lewat API oleh akun aktor Total Control (Global Settings) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.GS_TC_PASSWORD`): lima user profil IDLE (Tabel Data Uji Pre-setup #6: seperti BASE, yaitu Activated, Active ON, sudah pernah login sukses di web dari browser uji A, login terakhir dari IP uji Jakarta (ID), Authenticator sudah terdaftar), password `Spectra.env.MFA_PASSWORD`, email bersuffix per run. Waktu logout web terakhir (`last_logout_at`) di-seed relatif terhadap T0, yaitu waktu jam server uji saat dibekukan di hook `before`:
  - TC-AUTH-MFA-26: `Nia Kurnia` (`niakurnia+{runId}-021@qwertysystem.net`), logout web terakhir T0 - 31 hari; ID device browser uji A trusted.
  - TC-AUTH-MFA-27: `Rudi Hartono` (`rudihartono+{runId}-021@qwertysystem.net`), logout web terakhir T0 - 30 hari tepat; ID device browser uji A trusted.
  - TC-AUTH-MFA-28: `Tari Handayani` (`tarihandayani+{runId}-021@qwertysystem.net`), logout web terakhir T0 - 29 hari; ID device browser uji A trusted.
  - TC-AUTH-MFA-59: `Tika Amelia` (`tikaamelia+{runId}-021@qwertysystem.net`), logout web terakhir T0 - 31 hari; ID device browser uji A trusted.
  - TC-AUTH-MFA-52: `Rizky Wijaya` (`rizkywijaya+{runId}-021@qwertysystem.net`), logout web terakhir T0 - 31 hari; ID device browser uji B tidak ada di daftar trusted device.
- Hook `before`: bekukan jam server uji pada T0 sebelum seeding, sehingga usia logout web terakhir tidak bergeser selama spec berjalan (batas tepat 30 hari pada TC-AUTH-MFA-27), lalu tetapkan IP uji ke Jakarta (ID) untuk semua TC (tidak diatur ulang per TC). Hook `after`: lepaskan pembekuan dan kembalikan jam server uji ke waktu nyata, kembalikan IP uji ke IP default lingkungan uji, lalu hapus kelima user. Hook `after` tetap jalan walau spec gagal di tengah.
- Jam yang diatur hanya jam server uji. Jam browser/klien tidak diubah: usia logout web terakhir dan ambang 30 hari dihitung murni di server dan tidak diamati lewat UI (tidak ada countdown pada layar yang diuji).
- Akun yang dipakai: tanpa login (halaman publik; tidak ada sesi aktif di browser) untuk semua TC. Tiap TC setelah yang pertama dimulai di jendela baru browser uji tanpa sesi login; TC pertama berjalan di browser awal.
- Environment variable: `GS_TC_PASSWORD`, `MFA_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Kemampuan teknis:
  - Manipulasi jam server uji (bekukan di T0 dan lepaskan) serta seeding `last_logout_at` per user.
  - Seeding state BE per user: trusted device (ID device browser uji A trusted untuk TC-AUTH-MFA-26, 27, 28, 59; ID device browser uji B tidak terdaftar untuk TC-AUTH-MFA-52), lokasi dan waktu login terakhir (Jakarta (ID)), `last_logout_at`, Authenticator terdaftar, dan persetujuan Privacy Policy; mekanisme seeding (endpoint/skrip uji) disediakan tim FE/BE karena tidak didefinisikan di TC, PRD, atau LLD.
  - Browser uji A (ID device terdaftar trusted untuk user TC itu) dan browser uji B (ID device belum dikenali): konteks browser dengan cookie ID device persisten; setiap TC memakai konteks baru. IP uji Jakarta (ID) tetap untuk semua TC (Tabel Data Uji Pre-setup #19).
  - Mail-catcher lingkungan uji untuk memastikan ada atau tidak adanya email alert "New sign-in to your TAG Samurai account". Asersi email memakai baseline jumlah email alert untuk alamat user yang dicatat sebelum login.
  - reCAPTCHA mode uji di environment.
- TC-AUTH-MFA-26, 27, 52, 59: Langkah Uji TC melewati layar Confirm to Continue sebelum halaman MFA karena idle 30 hari atau lebih memicu Agreement (kondisi (b), `auth/_foundation/auth-foundation.md` §11.1); TC-AUTH-MFA-28 (29 hari) tidak memenuhi kondisi itu sehingga tidak melewati layar tersebut.

## Test Steps

### TC-AUTH-MFA-26: Login setelah idle 31 hari sejak logout web terakhir mewajibkan MFA

1. Catat jumlah email dengan subject "New sign-in to your TAG Samurai account" di mail-catcher untuk `niakurnia+{runId}-021@qwertysystem.net` sebagai baseline
2. Buka halaman `Auth > Login with Password` di browser uji A → halaman Login with Password tampil
3. Ketik `niakurnia+{runId}-021@qwertysystem.net` pada field Email
4. Ketik `Spectra.env.MFA_PASSWORD` pada field Password
5. Centang widget reCAPTCHA "I'm not a robot"
6. Klik button [Log in] → layar Confirm to Continue tampil
7. Centang checkbox persetujuan, lalu klik [Continue ➔]
8. Amati halaman setelah klik [Continue ➔]
9. Verifikasi Halaman `Auth > MFA > Choose Verification Method` tampil (MFA wajib karena idle 30 hari atau lebih)
10. Verifikasi Pilihan dan tampilan halaman identik dengan alasan MFA lain: opsi "OTP via email" dan "Authenticator app"
11. Periksa mail-catcher lingkungan uji untuk `niakurnia+{runId}-021@qwertysystem.net`
12. Verifikasi Tidak ada email alert "New sign-in to your TAG Samurai account" di mail-catcher untuk `niakurnia+{runId}-021@qwertysystem.net` (jumlah sama dengan baseline langkah 1; device dikenali, lokasi dan negara sama)

### TC-AUTH-MFA-27: Login tepat 30 hari setelah logout web terakhir mewajibkan MFA (batas 30 hari)

13. Tutup jendela user uji dari TC sebelumnya dan hapus sesi login browser terkait (ID device dan jendela sesi akun aktor tetap), lalu buka jendela baru browser uji A (konteks bersih tanpa sesi login)
14. Buka halaman `Auth > Login with Password` di browser uji A → halaman Login with Password tampil
15. Ketik `rudihartono+{runId}-021@qwertysystem.net` pada field Email
16. Ketik `Spectra.env.MFA_PASSWORD` pada field Password
17. Centang widget reCAPTCHA "I'm not a robot"
18. Klik button [Log in] → layar Confirm to Continue tampil
19. Centang checkbox persetujuan, lalu klik [Continue ➔]
20. Amati halaman setelah klik [Continue ➔]
21. Verifikasi Halaman `Auth > MFA > Choose Verification Method` tampil (MFA wajib; 30 hari termasuk idle 30 hari atau lebih)

### TC-AUTH-MFA-28: Login 29 hari setelah logout web terakhir tidak memicu MFA

22. Tutup jendela user uji dari TC sebelumnya dan hapus sesi login browser terkait (ID device dan jendela sesi akun aktor tetap), lalu buka jendela baru browser uji A (konteks bersih tanpa sesi login)
23. Buka halaman `Auth > Login with Password` di browser uji A → halaman Login with Password tampil
24. Ketik `tarihandayani+{runId}-021@qwertysystem.net` pada field Email
25. Ketik `Spectra.env.MFA_PASSWORD` pada field Password
26. Centang widget reCAPTCHA "I'm not a robot"
27. Klik button [Log in]
28. Amati halaman setelah klik [Log in]
29. Verifikasi Halaman MFA tidak tampil
30. Verifikasi Browser dialihkan ke Portal — Product Hub
31. Verifikasi Sesi web aktif untuk `Tari Handayani` (teramati dari Portal — Product Hub yang tampil untuk akun ini)

### TC-AUTH-MFA-59: Pilihan Choose Verification Method identik saat alasan MFA adalah idle 30 hari atau lebih

32. Tutup jendela user uji dari TC sebelumnya dan hapus sesi login browser terkait (ID device dan jendela sesi akun aktor tetap), lalu buka jendela baru browser uji A (konteks bersih tanpa sesi login)
33. Buka halaman `Auth > Login with Password` di browser uji A → halaman Login with Password tampil
34. Ketik `tikaamelia+{runId}-021@qwertysystem.net` pada field Email
35. Ketik `Spectra.env.MFA_PASSWORD` pada field Password
36. Centang widget reCAPTCHA "I'm not a robot"
37. Klik button [Log in] → layar Confirm to Continue tampil
38. Centang checkbox persetujuan, lalu klik [Continue ➔] → halaman `Auth > MFA > Choose Verification Method` tampil
39. Verifikasi Opsi "OTP via email" dan "Authenticator app" tampil sama dengan alasan MFA lain
40. Verifikasi Title "Choose verification method" sama dengan alasan MFA lain
41. Verifikasi Subtitle "Select how you'd like to verify your identity" sama dengan alasan MFA lain
42. Verifikasi Tidak ada teks atau opsi yang menyebut alasan MFA (idle 30 hari atau lebih)

### TC-AUTH-MFA-52: Alert login tak biasa tetap dikirim saat idle 30 hari atau lebih terjadi bersamaan dengan device baru

43. Tutup jendela user uji dari TC sebelumnya dan hapus sesi login browser terkait (ID device dan jendela sesi akun aktor tetap), lalu buka jendela baru browser uji B (konteks bersih tanpa sesi login; ID device belum dikenali)
44. Catat jumlah email dengan subject "New sign-in to your TAG Samurai account" di mail-catcher untuk `rizkywijaya+{runId}-021@qwertysystem.net` sebagai baseline
45. Buka halaman `Auth > Login with Password` di browser uji B → halaman Login with Password tampil
46. Ketik `rizkywijaya+{runId}-021@qwertysystem.net` pada field Email
47. Ketik `Spectra.env.MFA_PASSWORD` pada field Password
48. Centang widget reCAPTCHA "I'm not a robot"
49. Klik button [Log in] → layar Confirm to Continue tampil
50. Centang checkbox persetujuan, lalu klik [Continue ➔]
51. Amati halaman setelah klik [Continue ➔]
52. Verifikasi Halaman `Auth > MFA > Choose Verification Method` tampil (MFA wajib)
53. Periksa mail-catcher lingkungan uji untuk `rizkywijaya+{runId}-021@qwertysystem.net`
54. Verifikasi Email alert dengan subject "New sign-in to your TAG Samurai account" diterima di mail-catcher untuk `rizkywijaya+{runId}-021@qwertysystem.net` (jumlah bertambah dibanding baseline langkah 44; device dan lokasi tetap dievaluasi walau idle 30 hari atau lebih sudah terpenuhi)

## Notes

- Sumber: `auth/mfa/TestCases/tc-mfa.md`. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Langkah pembuka tiap TC sesudah TC pertama menutup jendela user uji dari TC sebelumnya dan menghapus sesi login browser terkait (ID device dan jendela sesi akun aktor tetap) sebelum jendela baru dibuka; itu langkah penghubung tanpa `Verifikasi` (S-03, S-09).
- Kelas harness d (time-travel / manipulasi jam server): seluruh TC spec ini bergantung pada usia `last_logout_at`. Jam server uji dibekukan di T0 sekali di hook `before` dan IP uji Jakarta (ID) ditetapkan di hook yang sama, sehingga tidak ada langkah pengaturan jam atau IP per TC; usia tepat 30 hari (TC-AUTH-MFA-27) tidak bergeser selama run.
- Langkah penghubung tanpa awalan `Verifikasi` (buka jendela baru browser uji, catat baseline email) bukan asersi tambahan (S-03). Langkah 1 dan 44 mencatat baseline jumlah email alert (S-12) supaya "tidak ada email alert" diasersi sebagai tidak bertambah dan "email alert diterima" sebagai bertambah.
- Penggantian langkah amati (S-15): Langkah Uji TC-AUTH-MFA-26, 27, dan 52 (Langkah 6) menulis "amati halaman setelah klik [Log in]" pada langkah yang sama dengan klik [Continue ➔]; spec mengamati halaman setelah klik [Continue ➔] (langkah 8, 20, dan 51) karena setelah klik [Log in] yang tampil adalah layar Confirm to Continue.
- Urutan TC mengikuti TC sumber; TC-AUTH-MFA-52 ditaruh terakhir karena memakai browser uji B (device baru) (S-10).
- Sesi teramati lewat halaman yang tampil: sesi pre-auth MFA = halaman Choose Verification Method tampil; sesi web aktif = Portal — Product Hub tampil (langkah 31 merinci klausa "sesi web aktif" pada Expected b TC-AUTH-MFA-28). Post Condition sesi tidak diasersi terpisah.
- Jumlah langkah melewati ±35 karena lima TC independen dengan prefix login faktor-1 yang identik (tidak dihitung); spec tidak dipecah.
- Temuan untuk QA:
  1. TC-AUTH-MFA-26, 27, 52, dan 59 melewati layar Confirm to Continue pada Langkah Uji, tetapi Precondition tidak menyatakan penyebabnya; dasarnya `auth/_foundation/auth-foundation.md` §11.1 kondisi (b) (idle 30 hari atau lebih memicu Agreement), sedangkan TC-AUTH-MFA-28 (29 hari) tidak memicunya. QA menambah penjelasan itu di Precondition TC (lihat juga profil POLICY, Tabel Data Uji Pre-setup #12, yang menyatakan layar Confirm terpicu karena Privacy Policy baru).
  2. TC-AUTH-MFA-26, 27, 28, 59, 52 tidak menyebut IP uji; spec memakai Jakarta (ID) sesuai profil IDLE/BASE.
  3. TC-AUTH-MFA-27 Data Uji menyebut "Idle: 30 hari" tanpa menyatakan apakah jam server dibekukan; spec membekukan jam agar batas tepat 30 hari deterministik.
  4. TC-AUTH-MFA-59 Expected butir a menyebut Title dan Subtitle "sama" tanpa menulis teksnya; spec memakai teks dari halaman Choose Verification Method (TC-AUTH-MFA-01).
  5. Post Condition berupa state BE tidak diasersi (S-01, S-15): "Sesi pre-auth MFA aktif untuk <user>" pada TC-AUTH-MFA-26, 27, 59, dan 52 (teramati lewat halaman Choose Verification Method tampil pada Expected) serta "Satu sesi web aktif ...; tidak ada sesi pre-auth MFA" pada TC-AUTH-MFA-28 (teramati lewat Portal tampil dan halaman MFA tidak tampil). QA menambah Expected atau langkah observasi di TC bila ada yang harus diuji lebih jauh.
  6. Mekanisme seeding state BE (trusted device per ID device, lokasi dan waktu login terakhir, consent) belum ada di Tabel Data Uji Pre-setup; #20 hanya memuat manipulasi jam server dan seed `last_logout_at`, pasangan negara, `first_login_at`. Tim FE/BE menyediakan dan QA melengkapi Pre-setup.
