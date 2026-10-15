---
id: TC-AUTH-LP-E2E-015-lock-recovery-reset-password
title: "Pemulihan Lock lewat Reset Password"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-LP-61
  - TC-AUTH-LP-62
  - TC-AUTH-LP-63
coverage:
  web: automated
---

# Pemulihan Lock lewat Reset Password

## Prerequisites

- Mode: FE+BE.
- Seeding: tiga user subjek dibuat lewat API di hook `before` oleh akun aktor Total Control (Global Settings) `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net` (kredensial `Spectra.env.GS_TC_PASSWORD`) lalu diaktivasi. Semua user dihapus di hook `after`, dan pembersihan tidak berasumsi seeding berhasil penuh.
- Environment variable: `GS_TC_PASSWORD`, `LP_PASSWORD`, `LP_PASSWORD_NEW`, `LP_PASSWORD_WRONG`. `LP_PASSWORD_NEW` memenuhi Password Policy.
- Kemampuan teknis (fixture BE): menaruh user pada status Requires Reset di web (TC-AUTH-LP-61); menaruh user langsung pada keadaan pasca-Reset Password, yaitu hitungan gagal dan tahap lock kembali ke awal, tidak lagi berstatus Requires Reset atau Permanent, dan belum login sesudahnya (TC-AUTH-LP-62 dan TC-AUTH-LP-63). Kotak masuk email uji (mail-catcher) dapat dibaca otomatis dan jumlah email per alamat dapat dihitung, untuk mengambil tautan reset TC-AUTH-LP-61. Alur Reset Password (modul Reset Password) tersedia di environment; reCAPTCHA mode uji; ketiga user tanpa gate Agreement atau MFA.
- TC-AUTH-LP-61: Tanpa login (guest, browser web)
- TC-AUTH-LP-61: User `Doni Prasetyo` (`doniprasetyo+{runId}-015@qwertysystem.net`) berstatus Requires Reset di web, password lama `Spectra.env.LP_PASSWORD` (di-seed oleh fixture BE)
- TC-AUTH-LP-61 data: Password baru `Spectra.env.LP_PASSWORD_NEW`
- TC-AUTH-LP-62: Tanpa login (guest, browser web)
- TC-AUTH-LP-62: User `Putra Anugrah` (`putraanugrah+{runId}-015@qwertysystem.net`) dalam keadaan baru menyelesaikan Reset Password dari status Requires Reset dan belum login sesudahnya (di-seed langsung oleh fixture BE)
- TC-AUTH-LP-62 data: Password salah `Spectra.env.LP_PASSWORD_WRONG`
- TC-AUTH-LP-63: Tanpa login (guest, browser web)
- TC-AUTH-LP-63: User `Panji Kusuma` (`panjikusuma+{runId}-015@qwertysystem.net`) dalam keadaan pernah berstatus Permanent, baru menyelesaikan Reset Password, dan belum login sesudahnya (di-seed langsung oleh fixture BE)
- TC-AUTH-LP-63 data: Password salah `Spectra.env.LP_PASSWORD_WRONG`

## Test Steps

### TC-AUTH-LP-61: Login berhasil setelah Reset Password menyelesaikan status Requires Reset

1. Buka halaman Login with Password
2. Isi Email `doniprasetyo+{runId}-015@qwertysystem.net` dan Password `Spectra.env.LP_PASSWORD`
3. Selesaikan reCAPTCHA
4. Klik [Log in]
5. Verifikasi Alert Danger "Please reset your password" tampil
6. Klik tautan [Reset password] pada Alert
7. Catat jumlah email di kotak masuk `doniprasetyo+{runId}-015@qwertysystem.net` pada mail-catcher (baseline)
8. Selesaikan reCAPTCHA
9. Klik Button [Reset Password]
10. Buka email baru (jumlah email melebihi baseline langkah 7) di mail-catcher, lalu buka tautan reset di dalamnya sampai halaman Setup New Password tampil
11. Isi field Password dan Confirm Password dengan `Spectra.env.LP_PASSWORD_NEW`
12. Klik Button [Reset Password]
13. Kembali ke halaman Login with Password
14. Isi Email `doniprasetyo+{runId}-015@qwertysystem.net` dan Password `Spectra.env.LP_PASSWORD_NEW`
15. Selesaikan reCAPTCHA
16. Klik [Log in]
17. Verifikasi login berhasil dan browser menuju Portal — Product Hub
18. Verifikasi caption lock tidak tampil
19. Logout dari Portal — Product Hub

### TC-AUTH-LP-62: Reset Password mengembalikan hitungan gagal dan tahap lock ke awal

20. Buka halaman Login with Password
21. Isi Email `putraanugrah+{runId}-015@qwertysystem.net` dan Password `Spectra.env.LP_PASSWORD_WRONG`
22. Selesaikan reCAPTCHA
23. Klik [Log in]
24. Verifikasi Alert Danger "Incorrect email or password" tampil di atas Button [Log in]
25. Isi Password `Spectra.env.LP_PASSWORD_WRONG`
26. Selesaikan reCAPTCHA
27. Klik [Log in]
28. Verifikasi Alert Danger "Incorrect email or password" tampil di atas Button [Log in]
29. Isi Password `Spectra.env.LP_PASSWORD_WRONG`
30. Selesaikan reCAPTCHA
31. Klik [Log in]
32. Verifikasi Alert Danger "Too many failed login attempts. Your account is locked for 15 minutes. You can try again at {time}." tampil (lock 15 menit, bukan Requires Reset)

### TC-AUTH-LP-63: Reset Password mengosongkan hitungan hari berturut-turut sehingga tidak langsung Permanent

33. Buka halaman Login with Password
34. Isi Email `panjikusuma+{runId}-015@qwertysystem.net` dan Password `Spectra.env.LP_PASSWORD_WRONG`
35. Selesaikan reCAPTCHA
36. Klik [Log in]
37. Verifikasi Alert Danger "Incorrect email or password" tampil di atas Button [Log in]
38. Verifikasi Alert lock Permanent "For security reasons, your account has been locked. Please reset your password to regain access." tidak tampil

## Notes

- Mode: FE+BE. Sumber: `auth/login-password/TestCases/tc-login-password.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Precondition TC-AUTH-LP-62 dan TC-AUTH-LP-63 ("baru menyelesaikan Reset Password") di-seed langsung oleh fixture BE ke keadaan pasca-reset; alur Reset Password hanya dijalankan di TC-AUTH-LP-61. Progresi lock yang membangun status Requires Reset dan Permanent ada di spec `TC-AUTH-LP-E2E-012-lock-1h-expiry-requires-reset` dan `TC-AUTH-LP-E2E-014-lock-permanent-escalation`.
- Detail field dan label halaman Reset Password dimiliki modul Reset Password; langkah 7 sampai 12 memakai nama elemen dari `auth/reset-password/TestCases/tc-reset-password.md` (field Email, Button [Reset Password], email di mail-catcher, Setup New Password dengan field Password dan Confirm Password).
- Langkah penghubung (S-03): logout dari Portal (langkah 19) mengembalikan sesi ke guest sebelum TC berikutnya; pengisian ulang Password dan reCAPTCHA sebelum tiap submit karena field Password dikosongkan dan reCAPTCHA kembali Unsolved setelah respons.
- Temuan untuk QA (TC-AUTH-LP-61, CAUSE2): Langkah Uji 3 hanya menyebut "selesaikan alur Reset Password (alur modul Reset Password)" tanpa merinci. Langkah 7 sampai 12 disusun dari alur Request Reset dan Setup New Password di TC modul Reset Password. TC-AUTH-LP-61 tidak menyatakan tujuan tautan [Reset password] pada Alert; spec mengikuti TC-AUTH-LP-52 dan TC-AUTH-LP-60 yang menyatakan halaman Reset Password terbuka dengan field Email sudah terisi setelah tautan diklik, sehingga email tidak diketik ulang. Hasil akhir Reset Password (halaman Password Reset Successful) tidak ada di Expected TC-AUTH-LP-61 dan tidak diasersi.
- Temuan untuk QA (TC-AUTH-LP-62 dan TC-AUTH-LP-63): TC tidak menyebut apakah login sesudah Reset Password membutuhkan Agreement atau MFA; spec mengasumsikan tidak ada gate.
- Temuan untuk QA (TC-AUTH-LP-61): Post Condition "Data lock akun kembali ke kondisi tidak terkunci" tidak dapat dibaca lewat UI dan TC tidak memberi langkah observasinya; tidak diasersi (S-01).
- Jumlah langkah 38 (smell, melewati ~35): satu topik (pemulihan lock lewat Reset Password) dengan tiga user terpisah yang di-seed sendiri, sehingga kegagalan satu TC tidak membuat TC sesudahnya kehilangan makna.
