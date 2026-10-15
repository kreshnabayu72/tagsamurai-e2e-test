---
id: TC-AUTH-MFA-E2E-013-admin-reset-authenticator
title: "Admin Reset Authenticator Saat Login MFA"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-MFA-100
  - TC-AUTH-MFA-105
coverage:
  web: automated
---

# Admin Reset Authenticator Saat Login MFA

## Prerequisites

- Mode: FE+BE.
- Seeding (hook `before`, lewat API oleh akun aktor Total Control (Global Settings) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.GS_TC_PASSWORD`): dua user profil NEWDEVE (Tabel Data Uji Pre-setup #5: Activated, Active ON, sudah pernah login sukses di web dari browser uji A (device dikenali), login terakhir dari IP uji Jakarta (ID), logout web terakhir kurang dari 30 hari, Authenticator sudah terdaftar (status Enrolled) dengan secret yang diketahui aplikasi authenticator uji dan dicatat sebagai secret lama), password `Spectra.env.MFA_PASSWORD`, email bersuffix per run:
  - TC-AUTH-MFA-100: `Zahra Pertiwi` (`zahrapertiwi+{runId}-013@qwertysystem.net`)
  - TC-AUTH-MFA-105: `Yuni Wijaya` (`yuniwijaya+{runId}-013@qwertysystem.net`)
- Hook `before` juga login sebagai Total Control (Global Settings) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (`Spectra.env.GS_TC_PASSWORD`) di jendela admin; jendela ini dipakai untuk Reset Authenticator di `Global Settings > User > Detail` dan tetap terbuka sepanjang spec.
- Hook `after`: tutup semua jendela privat, hapus kedua user, dan kembalikan sesi jendela admin ke akun default suite.
- Akun yang dipakai: Total Control (Global Settings) di jendela admin untuk Reset Authenticator; tanpa login (halaman publik; tidak ada sesi aktif di browser) di jendela privat untuk alur user. Pergantian akun dilakukan eksplisit dengan beralih antara jendela admin dan jendela privat. Jendela privat tanpa ID device tersimpan sehingga dikenali sebagai browser uji B (ID device belum dikenali), dan login dari IP uji Jakarta (ID) hanya memicu MFA karena device baru. Semua user berprofil NEWDEVE, jadi tiap login Password melewati Choose Verification Method tanpa layar Confirm to Continue.
- Environment variable: `GS_TC_PASSWORD`, `MFA_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Kemampuan teknis: dua jendela browser bersamaan (jendela admin dan jendela privat); reCAPTCHA mode uji di environment; aplikasi authenticator uji (TOTP: SHA-1, 6 digit, periode 30 detik) yang memegang secret lama user seeding untuk menghasilkan kode (TC-AUTH-MFA-105) dan nilai secret lama itu terbaca automation untuk dibandingkan dengan secret key pada Enrollment (TC-AUTH-MFA-100).
- Kemampuan teknis, pembacaan hitungan percobaan salah sesi pre-auth oleh sisi BE (TC-AUTH-MFA-105 butir b; langkah 28 dan 36): mekanisme baca disediakan tim FE/BE karena hitungan itu tidak terlihat di UI dan tidak didefinisikan sebagai endpoint baca di TC, PRD, atau LLD.
- Kemampuan teknis, seeding state BE per user: status Activated dan Active ON, trusted device ber-ID device browser uji A (device dikenali), lokasi dan waktu login terakhir dari IP uji Jakarta (ID), logout web terakhir kurang dari 30 hari, consent sudah disetujui sehingga tanpa layar Confirm to Continue, dan Authenticator terdaftar (status Enrolled) dengan secret yang diketahui aplikasi authenticator uji. Mekanisme seeding (endpoint atau skrip uji) disediakan tim FE/BE karena tidak didefinisikan di TC, PRD, atau LLD.

## Test Steps

### TC-AUTH-MFA-100: Setelah admin reset Authenticator, pilihan Authenticator berikutnya membuka Enrollment

1. Di jendela admin (sesi Total Control Global Settings dari hook `before`), buka halaman `Global Settings > User > Detail` untuk `Zahra Pertiwi` (dicari lewat email bersuffix `zahrapertiwi+{runId}-013@qwertysystem.net` pada daftar User) → sub-section Authenticator (MFA) menampilkan status Enrolled dan button [Reset Authenticator]
2. Klik button [Reset Authenticator] → dialog konfirmasi tampil
3. Klik button [Reset] pada dialog konfirmasi
4. Verifikasi Reset Authenticator oleh admin berhasil: toast "Success, authenticator has been reset for Zahra Pertiwi."
5. Buka jendela privat baru (tanpa sesi login) untuk alur user
6. Buka halaman `Auth > Login with Password` di browser → halaman Login with Password tampil
7. Ketik `zahrapertiwi+{runId}-013@qwertysystem.net` pada field Email
8. Ketik `Spectra.env.MFA_PASSWORD` pada field Password
9. Centang widget reCAPTCHA "I'm not a robot"
10. Klik button [Log in] → halaman `Auth > MFA > Choose Verification Method` tampil
11. Pilih opsi "Authenticator app" pada halaman Choose Verification Method
12. Klik button [Login] → halaman `Auth > MFA > Enrollment Authenticator` tampil
13. Verifikasi Halaman `Auth > MFA > Enrollment Authenticator` tampil (bukan Authenticator Verification)
14. Verifikasi QR code tampil pada halaman Enrollment Authenticator
15. Verifikasi Secret key pada halaman Enrollment Authenticator berbeda dari secret lama

### TC-AUTH-MFA-105: Admin Reset Authenticator saat user sudah di Authenticator Verification diperlakukan seperti kode salah

16. Tutup jendela user uji dari TC sebelumnya dan hapus sesi login browser terkait (ID device dan jendela sesi akun aktor tetap), lalu buka jendela privat baru (tanpa sesi login) untuk alur user
17. Buka halaman `Auth > Login with Password` di browser → halaman Login with Password tampil
18. Ketik `yuniwijaya+{runId}-013@qwertysystem.net` pada field Email
19. Ketik `Spectra.env.MFA_PASSWORD` pada field Password
20. Centang widget reCAPTCHA "I'm not a robot"
21. Klik button [Log in] → halaman `Auth > MFA > Choose Verification Method` tampil
22. Pilih opsi "Authenticator app" pada halaman Choose Verification Method
23. Klik button [Login] → halaman `Auth > MFA > Authenticator Verification` tampil
24. Beralih ke jendela admin (sesi Total Control Global Settings) dan buka halaman `Global Settings > User > Detail` untuk `Yuni Wijaya` (dicari lewat email bersuffix `yuniwijaya+{runId}-013@qwertysystem.net` pada daftar User)
25. Klik button [Reset Authenticator] → dialog konfirmasi tampil
26. Klik button [Reset] pada dialog konfirmasi
27. Catat penanda waktu P1 sebagai waktu saat ini (setelah Reset selesai, sebelum kode diketik)
28. Catat hitungan percobaan salah sesi pre-auth `Yuni Wijaya` sebagai baseline (dibaca lewat kemampuan baca BE)
29. Beralih kembali ke jendela privat pada halaman Authenticator Verification
30. Ketik 6 digit kode TOTP valid dari aplikasi authenticator uji (kode dari secret lama) untuk `yuniwijaya+{runId}-013@qwertysystem.net` pada kotak digit
31. Klik button [Login]
32. Verifikasi Caption error di bawah kotak digit: "Invalid code"
33. Verifikasi Tidak ada sesi yang dibuat
34. Beralih ke jendela admin, buka `Global Settings > Activity Log > Session`, cari `yuniwijaya+{runId}-013@qwertysystem.net` pada kolom pencarian, dan lihat entri dengan waktu sesudah penanda P1
35. Verifikasi Tampil entri baru untuk `Yuni Wijaya` pada Activity Log Session dengan Status `Failed` dan Note `Incorrect OTP`
36. Verifikasi Percobaan tersebut dihitung sebagai percobaan salah: hitungan percobaan salah sesi pre-auth `Yuni Wijaya` bertambah satu dari baseline
37. Beralih kembali ke jendela privat pada halaman Authenticator Verification
38. Klik button Text [Use a different method] → halaman Choose Verification Method tampil
39. Pilih opsi "Authenticator app" pada halaman Choose Verification Method
40. Klik button [Login] → halaman `Auth > MFA > Enrollment Authenticator` tampil
41. Verifikasi Halaman `Auth > MFA > Enrollment Authenticator` tampil (enrollment sudah di-reset)

## Notes

- Sumber: `auth/mfa/TestCases/tc-mfa.md`. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Langkah pembuka tiap TC sesudah TC pertama menutup jendela user uji dari TC sebelumnya dan menghapus sesi login browser terkait (ID device dan jendela sesi akun aktor tetap) sebelum jendela baru dibuka; itu langkah penghubung tanpa `Verifikasi` (S-03, S-09).
- Pergantian akun: sesi Total Control Global Settings berada di jendela admin sejak hook `before` (login aktor pertama, S-07); alur user berjalan di jendela privat tanpa sesi login. Jendela admin hanya memicu Reset Authenticator pada user target dan bukan objek asersi (bukan konteks kedua). Langkah 5, 16, 24, 29, 34, dan 37 beralih jendela secara eksplisit.
- Langkah penghubung tanpa awalan `Verifikasi` (membuka Detail, klik [Reset] pada dialog, mencatat penanda waktu P1 dan baseline hitungan percobaan salah, beralih jendela) bukan asersi tambahan (S-03, S-12). Teks toast pada langkah 4 mengikuti `global-settings/user/PRD/user.md` (T-27), bukan kolom TC.
- `P-1` (state berat): asersi log TC-AUTH-MFA-105 butir b (langkah 34-36) tetap di spec ini karena bergantung pada state handoff MFA yang dibangun langkah 17-26 (sesi pre-auth user di Authenticator Verification dengan enrollment yang di-reset admin pada langkah 26). Tidak ada spec pencatatan yang menampung TC-AUTH-MFA-105: spec pencatatan Failed faktor kedua hanya memuat TC-AUTH-MFA-159, 163, dan 164.
- Baseline (S-12): asersi log memakai penanda waktu P1 (langkah 27, sebelum kode diketik) dan pencarian lewat email bersuffix pada kolom pencarian Activity Log > Session. TC-AUTH-MFA-105 butir b tidak menyebut User Log, sehingga hanya Activity Log > Session yang dibaca, dan hanya Status serta Note yang diasersi: kolom Activity tidak diasersi karena Expected butir b tidak menyebutnya. Asersi hitungan percobaan salah (langkah 36) memakai baseline yang dicatat pada langkah 28 dan kemampuan baca BE di Prerequisites.
- Temuan untuk QA: (1) TC-AUTH-MFA-100 Langkah Uji 1 dan TC-AUTH-MFA-105 Langkah Uji 8 menyebut "lakukan Reset Authenticator" tanpa merinci dialog konfirmasi dan toast hasilnya; spec menambah klik [Reset] pada dialog berdasarkan alur di `global-settings/user/PRD/user.md` (S-15). (2) TC-AUTH-MFA-100 butir b ("QR code dan secret key baru") tidak menyebut pembanding "baru"; spec membandingkan secret key dengan secret lama yang di-seed. (3) TC-AUTH-MFA-105 butir b ("dicatat Failed `Incorrect OTP` dan dihitung sebagai percobaan salah", detail "pada TC Logging"): bagian pencatatan Failed `Incorrect OTP` diasersi pada langkah 34-35; klausa "dihitung sebagai percobaan salah" tidak memberi cara cek di UI Auth maupun log dan TC tidak menyebut langkah observasinya, sehingga diasersi pada langkah 36 lewat kemampuan baca BE (hitungan percobaan salah sesi pre-auth) yang disediakan tim FE/BE tanpa endpoint karangan; QA perlu menambah Expected yang teramati di UI atau menetapkan cara baca hitungan itu. (4) Post Condition tanpa langkah observasi dan tanpa Expected padanan tidak diasersi dan spec tidak menambah langkah observasi sendiri (S-01): TC-AUTH-MFA-100 "Enrollment Authenticator `Zahra Pertiwi` belum aktif sampai kode verifikasi dimasukkan" dan TC-AUTH-MFA-105 "Enrollment Authenticator `Yuni Wijaya` belum aktif sampai kode verifikasi enrollment dimasukkan"; QA perlu menambah Expected atau langkah observasi ke TC bila status itu harus diuji. (5) Pre-setup TC (#20/#21) belum memuat mekanisme seeding state BE per user (trusted device ber-ID device browser A, lokasi dan waktu login terakhir, enrollment Authenticator dengan secret yang dikenal authenticator uji, consent, logout web terakhir); mekanisme seed disediakan tim FE/BE.
