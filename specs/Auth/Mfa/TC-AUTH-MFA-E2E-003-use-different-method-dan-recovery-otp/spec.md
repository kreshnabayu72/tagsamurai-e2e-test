---
id: TC-AUTH-MFA-E2E-003-use-different-method-dan-recovery-otp
title: "Use a Different Method dan Recovery OTP"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-MFA-62
  - TC-AUTH-MFA-63
  - TC-AUTH-MFA-64
coverage:
  web: automated
---

# Use a Different Method dan Recovery OTP

## Prerequisites

- Mode: FE+BE.
- Seeding (hook `before`, lewat API oleh akun aktor Total Control (Global Settings) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.GS_TC_PASSWORD`): tiga user, password `Spectra.env.MFA_PASSWORD`, email bersuffix per run. Semua user sudah pernah login sukses di web (tanpa layar Confirm to Continue); TC pertama berjalan di browser awal; browser awal dan tiap jendela privat tanpa ID device tersimpan, dikenali sebagai browser uji B; login dari browser uji B memicu MFA karena ID device belum ada di daftar trusted device.
  - Profil NEWDEV (Tabel Data Uji Pre-setup #4: Activated, Active ON, Authenticator belum terdaftar):
    - TC-AUTH-MFA-62: `Bima Satria` (`bimasatria+{runId}-003@qwertysystem.net`)
  - Profil NEWDEVE (Tabel Data Uji Pre-setup #5: seperti NEWDEV, Authenticator sudah terdaftar):
    - TC-AUTH-MFA-63: `Elsa Fadilah` (`elsafadilah+{runId}-003@qwertysystem.net`)
    - TC-AUTH-MFA-64: `Ilham Prakasa` (`ilhamprakasa+{runId}-003@qwertysystem.net`), enrollment Authenticator aktif
- Hook `after`: hapus ketiga user. Pembersihan tidak berasumsi seeding berhasil penuh.
- Akun yang dipakai: tanpa login (halaman publik; tidak ada sesi aktif di browser) untuk semua TC. Tiap TC setelah TC pertama dimulai di jendela privat baru.
- Environment variable: `GS_TC_PASSWORD`, `MFA_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Kemampuan teknis:
  - Jendela privat; reCAPTCHA mode uji di environment.
  - Mail-catcher lingkungan uji untuk membaca kode OTP faktor-2 (TC-AUTH-MFA-64).
  - Seeding state BE per user: riwayat login web sukses dengan trusted device ber-ID device browser uji A untuk ketiga user, dan enrollment Authenticator aktif untuk kedua user profil NEWDEVE; mekanisme seeding (endpoint/skrip uji) disediakan tim FE/BE karena tidak didefinisikan di TC, PRD, atau LLD.

## Test Steps

### TC-AUTH-MFA-62: Use a different method di OTP Verification kembali ke Choose Verification Method

1. Buka halaman `Auth > Login with Password` di browser → halaman Login with Password tampil
2. Ketik `bimasatria+{runId}-003@qwertysystem.net` pada field Email
3. Ketik `Spectra.env.MFA_PASSWORD` pada field Password
4. Centang widget reCAPTCHA "I'm not a robot"
5. Klik button [Log in] → halaman `Auth > MFA > Choose Verification Method` tampil
6. Pilih opsi "OTP via email" pada halaman Choose Verification Method
7. Klik button [Login] → halaman `Auth > MFA > OTP Verification` tampil dan email OTP faktor-2 terkirim ke `bimasatria+{runId}-003@qwertysystem.net`
8. Klik button Text [Use a different method]
9. Verifikasi Halaman `Auth > MFA > Choose Verification Method` tampil
10. Verifikasi Tidak ada opsi yang terpilih
11. Verifikasi Button [Login] disabled (kembali ke default)

### TC-AUTH-MFA-63: Use a different method di Authenticator Verification kembali ke Choose Verification Method

12. Tutup jendela user uji dari TC sebelumnya dan hapus sesi login browser terkait (ID device dan jendela sesi akun aktor tetap), lalu buka jendela privat baru (tanpa sesi login)
13. Buka halaman `Auth > Login with Password` di browser → halaman Login with Password tampil
14. Ketik `elsafadilah+{runId}-003@qwertysystem.net` pada field Email
15. Ketik `Spectra.env.MFA_PASSWORD` pada field Password
16. Centang widget reCAPTCHA "I'm not a robot"
17. Klik button [Log in] → halaman `Auth > MFA > Choose Verification Method` tampil
18. Pilih opsi "Authenticator app" pada halaman Choose Verification Method
19. Klik button [Login] → halaman `Auth > MFA > Authenticator Verification` tampil
20. Klik button Text [Use a different method]
21. Verifikasi Halaman `Auth > MFA > Choose Verification Method` tampil
22. Verifikasi Tidak ada opsi yang terpilih
23. Verifikasi Button [Login] disabled (kembali ke default)

### TC-AUTH-MFA-64: User dengan Authenticator yang hilang menyelesaikan MFA lewat OTP via email

24. Tutup jendela user uji dari TC sebelumnya dan hapus sesi login browser terkait (ID device dan jendela sesi akun aktor tetap), lalu buka jendela privat baru (tanpa sesi login)
25. Buka halaman `Auth > Login with Password` di browser → halaman Login with Password tampil
26. Ketik `ilhamprakasa+{runId}-003@qwertysystem.net` pada field Email
27. Ketik `Spectra.env.MFA_PASSWORD` pada field Password
28. Centang widget reCAPTCHA "I'm not a robot"
29. Klik button [Log in] → halaman `Auth > MFA > Choose Verification Method` tampil
30. Pilih opsi "OTP via email" pada halaman Choose Verification Method
31. Klik button [Login] → halaman `Auth > MFA > OTP Verification` tampil dan email OTP faktor-2 terkirim ke `ilhamprakasa+{runId}-003@qwertysystem.net`
32. Ketik 6 digit kode OTP faktor-2 dari email `ilhamprakasa+{runId}-003@qwertysystem.net` pada kotak digit
33. Verifikasi Verifikasi berhasil pada digit ke-6 walau user memiliki enrollment Authenticator aktif
34. Verifikasi Browser dialihkan ke Portal — Product Hub dengan sesi web aktif untuk `Ilham Prakasa` (sesi web teramati sebagai Portal tampil)

## Notes

- Sumber: `auth/mfa/TestCases/tc-mfa.md`. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Langkah pembuka tiap TC sesudah TC pertama menutup jendela user uji dari TC sebelumnya dan menghapus sesi login browser terkait (ID device dan jendela sesi akun aktor tetap) sebelum jendela baru dibuka; itu langkah penghubung tanpa `Verifikasi` (S-03, S-09).
- Langkah penghubung tanpa awalan `Verifikasi` (buka jendela privat baru di awal tiap TC setelah TC pertama) bukan asersi tambahan (S-03).
- Urutan mengikuti TC sumber: dua jalur kembali ke Choose Verification Method (TC-AUTH-MFA-62, 63) lebih dulu, TC-AUTH-MFA-64 yang berujung login sukses paling akhir (S-10).
- Browser/jendela privat berbeda dipakai berurutan hanya untuk membentuk identitas device (browser uji B), tanpa asersi lintas jendela; bukan konteks kedua (tidak butuh butir P-2).
- Temuan untuk QA: (1) Post Condition TC-AUTH-MFA-62 "kode OTP faktor-2 yang terkirim masih berlaku selama belum expired" tidak punya langkah pengecekan di Langkah Uji; tidak diasersi di spec ini. (2) Post Condition tanpa langkah observasi dan tanpa Expected padanan tidak diasersi di spec (S-01, S-15): TC-AUTH-MFA-62 dan 63 "Sesi pre-auth MFA tetap aktif" (teramati sebagai halaman Choose Verification Method tampil, sudah menjadi `Verifikasi` Expected a); TC-AUTH-MFA-64 "Enrollment Authenticator `Ilham Prakasa` tetap aktif; satu sesi web aktif" (sesi web teramati sebagai Portal tampil, sudah menjadi `Verifikasi` Expected b; enrollment tetap aktif tidak punya cara pengecekan). Perlu Expected atau langkah observasi di TC bila Post itu hendak diasersi. (3) TC-AUTH-MFA-64 berjudul "Authenticator yang hilang" tetapi Langkah Uji hanya memilih OTP via email; tidak ada langkah yang membuat Authenticator hilang, enrollment tetap aktif (sesuai Post Condition). (4) Mekanisme seed state BE (trusted device ber-ID device browser uji A, enrollment Authenticator aktif) belum ada di Pre-setup (#20/#21); spec tidak menyebut endpoint karangan (S-11, S-13).
