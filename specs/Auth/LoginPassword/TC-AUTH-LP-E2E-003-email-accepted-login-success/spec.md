---
id: TC-AUTH-LP-E2E-003-email-accepted-login-success
title: "Email Diterima dan Login Berhasil: Spasi, Plus-Addressing, dan Kapitalisasi Campuran"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-LP-18
  - TC-AUTH-LP-27
  - TC-AUTH-LP-156
coverage:
  web: automated
---

# Email Diterima dan Login Berhasil: Spasi, Plus-Addressing, dan Kapitalisasi Campuran

## Prerequisites

- Mode: FE+BE.
- Seeding: setiap user subjek dibuat lewat API di hook `before` oleh akun aktor Total Control (Global Settings) `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net` (kredensial `Spectra.env.GS_TC_PASSWORD`) dengan status Activated dan Active. User dihapus di hook `after`, dan pembersihan tidak berasumsi seeding berhasil penuh.
- Email user memakai suffix per run `+{runId}-003` (contoh `budisantoso+{runId}-003@qwertysystem.net`); asersi teks yang memuat email memakai nilai bersuffix yang sama.
- Environment variable: `GS_TC_PASSWORD`, `LP_PASSWORD`. Password akun tidak ditulis di spec atau fixture.
- Kemampuan teknis (fixture BE): setiap user bertanda device terpercaya, lokasi sama seperti login sebelumnya, pernah login dan logout kurang dari 30 hari lalu, dan versi Privacy Policy terakhir yang disetujui sama dengan versi aktif, sehingga tidak ada gate Agreement dan MFA; reCAPTCHA mode uji di environment.
- Pemulihan: sesi login yang dibuat spec ditutup lewat logout di akhir tiap TC; hook `after` menutup sesi yang tersisa bila spec gagal di tengah.
- TC-AUTH-LP-18: Tanpa login (guest); browser web
- TC-AUTH-LP-18: User `Budi Santoso` (`budisantoso+{runId}-003@qwertysystem.net`) berstatus Activated dan Active (di-seed lewat API di hook `before`; kondisi fixture BE di atas)
- TC-AUTH-LP-18 data: Email: ` budisantoso+{runId}-003@qwertysystem.net ` (spasi awal dan akhir); Password: nilai `Spectra.env.LP_PASSWORD`
- TC-AUTH-LP-27: Tanpa login (guest); browser web
- TC-AUTH-LP-27: User `Budi Santoso QA` (`budisantoso+qa+{runId}-003@qwertysystem.net`) berstatus Activated dan Active dengan alamat plus-addressing (di-seed lewat API di hook `before`; kondisi fixture BE di atas)
- TC-AUTH-LP-27 data: Email: `budisantoso+qa+{runId}-003@qwertysystem.net`; Password: nilai `Spectra.env.LP_PASSWORD`
- TC-AUTH-LP-156: Tanpa login (guest); browser web
- TC-AUTH-LP-156: User `Budi Santoso` (`budisantoso+{runId}-003@qwertysystem.net`, sama seperti TC-AUTH-LP-18) berstatus Activated dan Active
- TC-AUTH-LP-156 data: Email: `BudiSantoso+{runId}-003@QwertySystem.net` (kapitalisasi campuran); Password: nilai `Spectra.env.LP_PASSWORD`

## Test Steps

### TC-AUTH-LP-18: Email dengan spasi di awal dan akhir tetap cocok ke akun

1. Buka halaman Login with Password
2. Ketik Email " budisantoso+{runId}-003@qwertysystem.net " (spasi di awal dan di akhir) di field Email
3. Verifikasi selama diketik, field Email menampilkan spasi apa adanya
4. Isi field Password dengan nilai `Spectra.env.LP_PASSWORD`
5. Selesaikan reCAPTCHA
6. Klik [Log in]
7. Verifikasi login berhasil: browser menuju Portal — Product Hub
8. Logout dari Portal — Product Hub

### TC-AUTH-LP-27: Submit dengan Email plus-addressing diterima dan login diproses

9. Buka halaman Login with Password
10. Isi field Email dengan "budisantoso+qa+{runId}-003@qwertysystem.net" dan field Password dengan nilai `Spectra.env.LP_PASSWORD`
11. Selesaikan reCAPTCHA
12. Klik [Log in]
13. Verifikasi caption "Email format is incorrect" tidak tampil
14. Verifikasi login diproses seperti email biasa
15. Verifikasi browser dialihkan ke Portal — Product Hub
16. Logout dari Portal — Product Hub

### TC-AUTH-LP-156: Submit dengan kapitalisasi email campuran login ke akun yang sama

17. Buka halaman Login with Password
18. Isi field Email dengan "BudiSantoso+{runId}-003@QwertySystem.net" dan field Password dengan nilai `Spectra.env.LP_PASSWORD`
19. Selesaikan reCAPTCHA
20. Klik [Log in]
21. Verifikasi caption "Email is not registered yet" tidak tampil
22. Verifikasi login berhasil dan browser dialihkan ke Portal — Product Hub
23. Verifikasi sesi yang aktif milik user `budisantoso+{runId}-003@qwertysystem.net`
24. Logout dari Portal — Product Hub

## Notes

- Mode: FE+BE. Sumber: `auth/login-password/TestCases/tc-login-password.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Tiga login berhasil dalam satu spec dipisah oleh logout (langkah penghubung, S-03 dan S-09) supaya tiap TC dimulai dari guest sesuai precondition TC.
- Email plus-addressing TC-AUTH-LP-27 berbentuk `budisantoso+qa+{runId}-003@...` karena suffix per run juga memakai tanda `+` (bagian 5 konvensi); tujuan TC (tanda `+` diterima validasi format) tetap terjaga.
- Temuan untuk QA: TC-AUTH-LP-156 Expected butir b menyebut "sesi milik `budisantoso@qwertysystem.net`" tanpa menyebut elemen UI atau cara memverifikasi identitas pemilik sesi di Portal — Product Hub; langkah 23 menulis asersi sesuai bunyi TC dan cara pembacaan identitas perlu ditentukan saat tahap script.
