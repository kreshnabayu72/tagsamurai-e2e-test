---
id: TC-AUTH-OTP-E2E-020-request-setelah-perubahan-status-akun
title: "Request OTP Setelah Akun Dinonaktifkan, Dihapus, atau Diaktifkan Kembali di Global Settings"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AUTH-OTP-138
  - TC-AUTH-OTP-139
  - TC-AUTH-OTP-140
  - TC-AUTH-OTP-166
coverage:
  web: automated
---

# Request OTP Setelah Akun Dinonaktifkan, Dihapus, atau Diaktifkan Kembali di Global Settings

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Global Settings), pre-setup `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net`; password dari `Spectra.env.GS_TC_PASSWORD`.
- Environment variable: `GS_TC_PASSWORD` (akun aktor), `OTP_PASSWORD` (password user uji yang dipasang saat seeding). Tidak ada password atau token di spec atau fixture. Nama didaftarkan di `executionConfig.environmentVariables` dan `.env.example`.
- Hook `before` (seeding API) membuat user berikut dengan suffix per run `+{runId}-020`, lalu menghapusnya di hook `after` (tetap jalan walau seeding gagal sebagian atau user sudah dihapus oleh spec):
  - TC-AUTH-OTP-138: `Agus Anggraini` (`agusanggraini+{runId}-020@qwertysystem.net`), profil BASE
  - TC-AUTH-OTP-140: `Hendra Ramadhan` (`hendraramadhan+{runId}-020@qwertysystem.net`), profil BASE
  - TC-AUTH-OTP-166: `Teguh Harahap` (`teguhharahap+{runId}-020@qwertysystem.net`), profil BASE
  - TC-AUTH-OTP-139: `Rina Gunawan` (`rinagunawan+{runId}-020@qwertysystem.net`), profil INACTIVE
  - Profil BASE: Activated, Active ON, sudah login sukses di web pada device uji dalam 30 hari terakhir, persetujuan Privacy Policy versi terbaru ada; Agreement dan MFA tidak terpicu.
  - Profil INACTIVE: Activated, Toggle Global (Active) OFF.
- Kemampuan teknis: dua konteks browser (browser admin dan jendela privat publik); mail-catcher lingkungan uji untuk memeriksa ada tidaknya email OTP per alamat; reCAPTCHA mode uji di environment (centang tanpa tantangan).
- Hook `before` membuka browser admin dan login sebagai akun aktor Total Control (Global Settings); langkah uji hanya berpindah konteks ke browser itu.
- Batas waktu TC-AUTH-OTP-166: langkah 18 sampai 23 (Request OTP pertama, nonaktifkan user di browser admin, Back to Login with Password, Log in with OTP, reCAPTCHA, Request OTP kedua) dijalankan berturut-turut dalam jendela cooldown 60 detik sejak langkah 18, tanpa memajukan jam server maupun jam browser dan tanpa menunggu waktu nyata; bila lebih dari 60 detik, cooldown sudah berakhir dan Expected tidak lagi menguji kasus cooldown.
- State yang berubah: TC-AUTH-OTP-138 dan TC-AUTH-OTP-166 menonaktifkan user, TC-AUTH-OTP-140 menghapus user, dan TC-AUTH-OTP-139 mengaktifkan user; semuanya hanya pada user milik spec ini. Tidak ada TC yang membuat sesi login.

## Test Steps

### TC-AUTH-OTP-138: Akun yang dinonaktifkan di Global Settings diblok pada Request OTP berikutnya

1. Di browser admin (sudah login sebagai akun aktor Total Control (Global Settings) lewat hook `before`), buka `Global Settings > User` dan matikan Toggle Active untuk `Agus Anggraini`
2. Ganti konteks ke jendela privat (tanpa sesi), buka halaman `Auth > Login with OTP > Request OTP`
3. Ketik `agusanggraini+{runId}-020@qwertysystem.net` pada field Email
4. Centang widget reCAPTCHA "I'm not a robot"
5. Klik button [Request OTP]
6. Verifikasi caption error di bawah field Email: "Your account is inactive"
7. Periksa mail-catcher untuk `agusanggraini+{runId}-020@qwertysystem.net`
8. Verifikasi tidak ada email OTP terkirim

### TC-AUTH-OTP-140: Akun yang dihapus di Global Settings diblok pada Request OTP berikutnya

9. Ganti konteks ke browser admin, buka `Global Settings > User`, dan hapus user `Hendra Ramadhan`
10. Ganti konteks ke jendela privat, buka halaman `Auth > Login with OTP > Request OTP`
11. Ketik `hendraramadhan+{runId}-020@qwertysystem.net` pada field Email
12. Centang widget reCAPTCHA "I'm not a robot"
13. Klik button [Request OTP]
14. Verifikasi caption error di bawah field Email: "Email is not registered yet"
15. Periksa mail-catcher untuk `hendraramadhan+{runId}-020@qwertysystem.net`
16. Verifikasi tidak ada email OTP terkirim

### TC-AUTH-OTP-166: Request OTP dalam cooldown pada akun yang baru dinonaktifkan menampilkan caption inactive

17. Di jendela privat, buka halaman `Auth > Login with OTP > Request OTP`
18. Ketik `teguhharahap+{runId}-020@qwertysystem.net` pada field Email, centang widget reCAPTCHA "I'm not a robot", lalu klik button [Request OTP]
19. Ganti konteks ke browser admin, buka `Global Settings > User`, dan matikan Toggle Active untuk `Teguh Harahap`
20. Ganti konteks ke jendela privat dan pada tab Verify OTP klik [Back to Login with Password]
21. Klik tautan [Log in with OTP]
22. Centang widget reCAPTCHA "I'm not a robot"
23. Klik button [Request OTP]
24. Verifikasi caption error di bawah field Email: "Your account is inactive"
25. Verifikasi alert "Too many requests. Please try again later." tidak tampil
26. Periksa mail-catcher untuk `teguhharahap+{runId}-020@qwertysystem.net`
27. Verifikasi tidak ada email OTP baru terkirim selain email dari langkah 18

### TC-AUTH-OTP-139: Akun yang diaktifkan kembali di Global Settings dapat meminta OTP lagi

28. Ganti konteks ke browser admin, buka `Global Settings > User`, dan nyalakan Toggle Active untuk `Rina Gunawan`
29. Ganti konteks ke jendela privat, buka halaman `Auth > Login with OTP > Request OTP`
30. Ketik `rinagunawan+{runId}-020@qwertysystem.net` pada field Email
31. Centang widget reCAPTCHA "I'm not a robot"
32. Klik button [Request OTP]
33. Verifikasi toast sukses "Success, the code has been sent." tampil
34. Verifikasi halaman Verify OTP tampil
35. Verifikasi email OTP diterima di `rinagunawan+{runId}-020@qwertysystem.net`

## Notes

- Mode: FE+BE. Sumber: `auth/login-otp/TestCases/tc-login-otp.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC menyimpang dari TC sumber (138, 139, 140, 166): TC yang menolak Request OTP (138, 140, 166) lebih dulu dan TC-AUTH-OTP-139 (berhasil) terakhir (prinsip 3).
- Asersi absence log TC-AUTH-OTP-140 butir c ("tidak ada entri log baru" di `Global Settings > Activity Log > Session` dan `Global Settings > User > Detail > User Log`, termasuk langkah 6 TC) dipindah ke spec 047 (prinsip 13g, S-05); spec ini hanya memuat asersi fungsional. Pembagian TC dicatat juga di Notes spec 047.
- Langkah ganti konteks (1, 2, 9, 10, 17, 19, 20, 28, 29) adalah langkah penghubung eksplisit antara browser admin dan jendela privat (S-03, S-07).
- Browser admin sebagai konteks kedua memenuhi pengecualian P-2 (`docs/e2e-conventions.md` §3): konteks itu hanya pemicu perubahan state akun (nonaktifkan, hapus, aktifkan) dan bukan objek asersi; yang diasersi adalah caption dan email di jendela privat.
- Langkah 25 menerjemahkan frasa "dan bukan 'Too many requests. Please try again later.'" pada Expected TC-AUTH-OTP-166 butir a menjadi `Verifikasi` tersendiri (S-01, pemecahan klausa).
- Temuan untuk QA: (1) TC-AUTH-OTP-166 langkah 6 menulis "Pada tab Verify OTP" padahal TC tidak membuka tab baru; spec memakai jendela privat yang sama dan menafsirkan "tab" sebagai tab yang sama. (2) TC-AUTH-OTP-138 dan TC-AUTH-OTP-140 bertipe Positive di TC sumber padahal Expected-nya penolakan. `caseType` spec ditetapkan Negative karena alur utama yang dominan adalah penolakan Request OTP (tiga dari empat TC: 138, 140, 166), bukan mengikuti kolom jenis TC sumber (konvensi §8). (3) TC-AUTH-OTP-139 memakai profil INACTIVE dan tidak menyebut apakah Request OTP pertama setelah aktivasi memulai sesi email-request baru; hanya toast, Verify OTP, dan email yang diasersi. (4) Post Condition TC-AUTH-OTP-166 a (Failed `Account is inactive`, detail pada TC Logging) tidak punya langkah observasi di TC, sehingga tidak diasersi di spec ini; pencatatan itu diuji di spec pencatatan Failed Request OTP (TC-AUTH-OTP-118).
