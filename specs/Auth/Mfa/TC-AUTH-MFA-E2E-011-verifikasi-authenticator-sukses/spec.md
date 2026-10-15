---
id: TC-AUTH-MFA-E2E-011-verifikasi-authenticator-sukses
title: "Verifikasi Authenticator Faktor Kedua Berhasil"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-MFA-10
  - TC-AUTH-MFA-90
  - TC-AUTH-MFA-91
coverage:
  web: automated
---

# Verifikasi Authenticator Faktor Kedua Berhasil

## Prerequisites

- Mode: FE+BE.
- Seeding (hook `before`, lewat API oleh akun aktor Total Control (Global Settings) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.GS_TC_PASSWORD`): tiga user profil NEWDEVE (Tabel Data Uji Pre-setup #5: Activated, Active ON, sudah pernah login sukses di web dari browser uji A (device dikenali), login terakhir dari IP uji Jakarta (ID), logout web terakhir kurang dari 30 hari, Authenticator sudah terdaftar dengan secret yang diketahui aplikasi authenticator uji), password `Spectra.env.MFA_PASSWORD`, email bersuffix per run:
  - TC-AUTH-MFA-10: `Ratna Sari` (`ratnasari+{runId}-011@qwertysystem.net`)
  - TC-AUTH-MFA-90: `Prita Anindya` (`pritaanindya+{runId}-011@qwertysystem.net`)
  - TC-AUTH-MFA-91: `Qori Ramadani` (`qoriramadani+{runId}-011@qwertysystem.net`)
- Hook `after`: hapus ketiga user, tutup semua jendela privat, hapus sesi browser awal (cadangan langkah 21), dan lepas throttle jaringan bila masih aktif. Pembersihan tidak berasumsi seeding berhasil penuh.
- Akun yang dipakai: tanpa login (halaman publik; tidak ada sesi aktif di browser) untuk semua TC. TC pertama berjalan di browser awal; browser awal dan tiap jendela privat tanpa ID device tersimpan, dikenali sebagai browser uji B. Tiap TC setelah TC pertama dimulai di jendela privat baru. Login dari IP uji Jakarta (ID) hanya memicu MFA karena device baru. Semua user berprofil NEWDEVE, jadi tiap login Password melewati Choose Verification Method tanpa layar Confirm to Continue.
- Environment variable: `GS_TC_PASSWORD`, `MFA_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Kemampuan teknis: jendela privat; reCAPTCHA mode uji di environment; mail-catcher lingkungan uji untuk membaca kode OTP login (TC-AUTH-MFA-91); aplikasi authenticator uji (TOTP: SHA-1, 6 digit, periode 30 detik) yang memegang secret tiap user seeding untuk menghasilkan kode valid; throttle jaringan 3 detik pada respons endpoint verifikasi Authenticator beserta pemantau request jaringan untuk menghitung request (TC-AUTH-MFA-10); pemantau request jaringan untuk memastikan tidak ada request verifikasi sebelum [Login] diklik (TC-AUTH-MFA-90).
- Kemampuan teknis, seeding state BE per user: status Activated dan Active ON, trusted device ber-ID device browser uji A (device dikenali), lokasi dan waktu login terakhir dari IP uji Jakarta (ID), logout web terakhir kurang dari 30 hari, consent sudah disetujui sehingga tanpa layar Confirm to Continue, dan Authenticator terdaftar dengan secret yang diketahui aplikasi authenticator uji. Mekanisme seeding (endpoint atau skrip uji) disediakan tim FE/BE karena tidak didefinisikan di TC, PRD, atau LLD.
- Akhir ketiga TC berupa sesi web aktif: TC-AUTH-MFA-10 berakhir di browser awal dan sesinya dihapus pada langkah 21 (hook `after` sebagai cadangan); TC-AUTH-MFA-90 dan TC-AUTH-MFA-91 berakhir di jendela privat masing-masing dan sesinya dibuang bersama penutupan jendela di hook `after`.

## Test Steps

### TC-AUTH-MFA-10: Button [Login] berstatus Submitting saat verifikasi Authenticator berjalan

1. Buka halaman `Auth > Login with Password` di browser → halaman Login with Password tampil
2. Ketik `ratnasari+{runId}-011@qwertysystem.net` pada field Email
3. Ketik `Spectra.env.MFA_PASSWORD` pada field Password
4. Centang widget reCAPTCHA "I'm not a robot"
5. Klik button [Log in] → halaman `Auth > MFA > Choose Verification Method` tampil
6. Pilih opsi "Authenticator app" pada halaman Choose Verification Method
7. Klik button [Login] → halaman `Auth > MFA > Authenticator Verification` tampil
8. Ketik 6 digit kode TOTP valid dari aplikasi authenticator uji untuk `ratnasari+{runId}-011@qwertysystem.net` pada kotak digit
9. Aktifkan throttle jaringan 3 detik pada respons server (tahan respons verifikasi Authenticator)
10. Klik button [Login]
11. Amati button [Login] selama request berjalan
12. Verifikasi Selama request berjalan button [Login] berstatus disabled
13. Verifikasi Selama request berjalan button [Login] menampilkan spinner memutar
14. Klik button [Login] sekali lagi selama request berjalan
15. Verifikasi Klik tambahan tidak mengirim request kedua (hanya satu request verifikasi yang terkirim)
16. Verifikasi Selama request berjalan browser tidak dialihkan
17. Verifikasi Selama request berjalan UI tidak menampilkan keberhasilan sebelum respons server (update pessimistic)
18. Tunggu respons server diterima
19. Verifikasi Browser dialihkan ke Portal — Product Hub
20. Lepas throttle jaringan
21. Hapus sesi browser awal (cookie dan penyimpanan lokal) supaya sesi web `Ratna Sari` tidak tersisa sebelum TC berikutnya

### TC-AUTH-MFA-90: Verifikasi Authenticator faktor-2 dengan kode benar setelah Login with Password

22. Tutup jendela user uji dari TC sebelumnya dan hapus sesi login browser terkait (ID device dan jendela sesi akun aktor tetap), lalu buka jendela privat baru (tanpa sesi login)
23. Buka halaman `Auth > Login with Password` di browser → halaman Login with Password tampil
24. Ketik `pritaanindya+{runId}-011@qwertysystem.net` pada field Email
25. Ketik `Spectra.env.MFA_PASSWORD` pada field Password
26. Centang widget reCAPTCHA "I'm not a robot"
27. Klik button [Log in] → halaman `Auth > MFA > Choose Verification Method` tampil
28. Pilih opsi "Authenticator app" pada halaman Choose Verification Method
29. Klik button [Login] → halaman `Auth > MFA > Authenticator Verification` tampil
30. Ketik 6 digit kode TOTP valid dari aplikasi authenticator uji untuk `pritaanindya+{runId}-011@qwertysystem.net` pada kotak digit
31. Verifikasi Verifikasi belum berjalan setelah digit ke-6 terisi (tidak ada auto-submit; tidak ada request verifikasi dan halaman tetap Authenticator Verification)
32. Klik button [Login]
33. Verifikasi Browser dialihkan ke Portal — Product Hub
34. Verifikasi Sesi web aktif untuk `Prita Anindya` (teramati dari Portal — Product Hub yang tampil)
35. Verifikasi Tidak ada toast sukses untuk verifikasi

### TC-AUTH-MFA-91: Verifikasi Authenticator faktor-2 dengan kode benar setelah Login with OTP

36. Tutup jendela user uji dari TC sebelumnya dan hapus sesi login browser terkait (ID device dan jendela sesi akun aktor tetap), lalu buka jendela privat baru (tanpa sesi login)
37. Buka halaman `Auth > Login with OTP > Request OTP` di browser → halaman Request OTP tampil
38. Ketik `qoriramadani+{runId}-011@qwertysystem.net` pada field Email
39. Centang widget reCAPTCHA "I'm not a robot"
40. Klik button [Request OTP] → halaman Verify OTP tampil
41. Ketik 6 digit kode OTP login dari email `qoriramadani+{runId}-011@qwertysystem.net` (dibaca lewat mail-catcher) pada kotak digit → halaman `Auth > MFA > Authenticator Verification` tampil
42. Ketik 6 digit kode TOTP valid dari aplikasi authenticator uji untuk `qoriramadani+{runId}-011@qwertysystem.net` pada kotak digit
43. Klik button [Login]
44. Verifikasi Browser dialihkan ke Portal — Product Hub
45. Verifikasi Sesi web aktif untuk `Qori Ramadani` (teramati dari Portal — Product Hub yang tampil)

## Notes

- Sumber: `auth/mfa/TestCases/tc-mfa.md`. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Langkah pembuka tiap TC sesudah TC pertama menutup jendela user uji dari TC sebelumnya dan menghapus sesi login browser terkait (ID device dan jendela sesi akun aktor tetap) sebelum jendela baru dibuka; itu langkah penghubung tanpa `Verifikasi` (S-03, S-09).
- Ketiga TC berakhir pada login sukses di user masing-masing, jadi tidak ada urutan yang bergantung; urutan mengikuti rencana.
- Langkah penghubung tanpa awalan `Verifikasi` (buka jendela privat baru di awal TC kedua dan ketiga; langkah 20 melepas throttle dan langkah 21 menghapus sesi browser awal supaya tidak memengaruhi TC berikutnya) bukan asersi tambahan (S-03, S-09).
- Pencatatan pada Post Condition (satu entri Success login final, Success `Login with password`, Success `Login with OTP`) tidak diasersikan di spec ini; asersi pencatatan berada di spec pencatatan.
- Temuan untuk QA: (1) TC-AUTH-MFA-10 butir a menyatakan "klik tambahan tidak mengirim request kedua" tetapi Langkah Uji tidak memuat klik tambahan; langkah 14 ditambahkan sebagai langkah penghubung agar asersinya dapat dijalankan (S-14, S-15). (2) Post Condition tanpa langkah observasi dan tanpa Expected padanan tidak diasersi dan spec tidak menambah langkah observasi sendiri (S-01): TC-AUTH-MFA-10 "Satu sesi web aktif untuk `Ratna Sari`" (sesi web teramati sebagai Portal tampil pada Expected c) dan TC-AUTH-MFA-90 butir b "Browser uji B tercatat sebagai trusted device `Prita Anindya` untuk platform web"; QA perlu menambah langkah observasi ke TC bila trusted device harus diuji. (3) TC-AUTH-MFA-91 Langkah Uji 5 dan 6 mengetik kode OTP lalu kode TOTP tanpa menyebut transisi antar halaman (tidak ada aksi submit setelah OTP); spec mengasumsikan halaman Authenticator Verification tampil setelah 6 digit OTP terisi, sama seperti TC-AUTH-MFA-06. (4) Pre-setup TC (#20/#21) belum memuat mekanisme seeding state BE per user (trusted device ber-ID device browser A, lokasi dan waktu login terakhir, secret authenticator yang dikenal authenticator uji, consent, logout web terakhir); mekanisme seed disediakan tim FE/BE.
