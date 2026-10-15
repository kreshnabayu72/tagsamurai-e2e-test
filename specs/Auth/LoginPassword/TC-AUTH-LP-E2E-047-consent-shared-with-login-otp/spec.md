---
id: TC-AUTH-LP-E2E-047-consent-shared-with-login-otp
title: "Persetujuan Privacy Policy dari Login with Password Berlaku pada Login with OTP"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-LP-159
coverage:
  web: automated
---

# Persetujuan Privacy Policy dari Login with Password Berlaku pada Login with OTP

## Prerequisites

- Mode: FE+BE.
- Seeding: user dibuat lewat API di hook `before` oleh akun aktor Total Control (Global Settings) `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup baris 1; kredensial `Spectra.env.GS_TC_PASSWORD`), lalu dihapus di hook `after`; pembersihan tidak berasumsi seeding berhasil penuh.
- Environment variable: `GS_TC_PASSWORD`, `LP_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Kemampuan teknis: fixture BE untuk user Bimo berupa device terpercaya, tanpa gate MFA, bukan login pertama, dan tidak idle; kotak masuk email akun user dapat dibaca penguji (mail-catcher lingkungan uji); reCAPTCHA mode uji di environment; versi Privacy Policy aktif lebih baru dari versi yang disetujui user (fixture BE).
- TC-AUTH-LP-159: User `Bimo Setiawan` (`bimosetiawan+{runId}-047@qwertysystem.net`) berstatus Activated dan Active; versi Privacy Policy aktif lebih baru dari versi terakhir yang disetujui akun ini; device terpercaya; bukan login pertama dan tidak idle; tidak memicu MFA; tanpa login (guest) di browser web
- TC-AUTH-LP-159 data: Email `bimosetiawan+{runId}-047@qwertysystem.net`; Password `Spectra.env.LP_PASSWORD`

## Test Steps

### TC-AUTH-LP-159: Persetujuan Privacy Policy dari Login with Password berlaku pada Login with OTP

1. Buka halaman Login with Password
2. Ketik "bimosetiawan+{runId}-047@qwertysystem.net" di field Email
3. Ketik nilai `Spectra.env.LP_PASSWORD` di field Password
4. Selesaikan reCAPTCHA
5. Klik [Log in] sampai layar Confirm to Continue tampil
6. Centang checkbox persetujuan
7. Klik [Continue ➔] sampai Portal — Product Hub tampil
8. Verifikasi browser menuju Portal — Product Hub
9. Logout dari Portal — Product Hub
10. Buka halaman Login with OTP
11. Ketik "bimosetiawan+{runId}-047@qwertysystem.net" di field Email
12. Centang widget reCAPTCHA "I'm not a robot"
13. Klik button [Request OTP]
14. Buka kotak masuk email `bimosetiawan+{runId}-047@qwertysystem.net` dan ambil kode OTP 6 digit
15. Ketik 6 digit kode OTP pada kotak digit sampai verifikasi diproses
16. Verifikasi layar Confirm to Continue tidak tampil
17. Verifikasi browser menuju Portal — Product Hub

## Notes

- Sumber: `auth/login-password/TestCases/tc-login-password.md`. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Satu spec sendiri karena topiknya alur Login with OTP (Request OTP, kode dari email, kotak digit) yang berbeda dari alur biometric re-login pada spec `TC-AUTH-LP-E2E-048-consent-shared-with-biometric-relogin`, yang berjalan di platform lain. Membaca mail-catcher untuk kode OTP adalah langkah rutin dan bukan kelas harness d (konvensi §3 prinsip 13d).
- Langkah penghubung (S-03): logout pada langkah 9 hanya mengakhiri sesi Login with Password agar login berikutnya lewat OTP (S-09). Langkah 10 sampai 15 disalin dari alur Login with OTP (halaman Request OTP, [Request OTP], kotak digit dengan auto-submit) sebagai dependensi (S-04).
- Temuan untuk QA:
  - TC-AUTH-LP-159 langkah 5 menyebut "minta kode OTP, isi kode OTP dari kotak masuk email lalu verifikasi" tanpa merinci tombol; spec memakai nama dari modul Login with OTP (`[Request OTP]`, widget reCAPTCHA "I'm not a robot", kotak digit dengan auto-submit tanpa tombol terpisah). Kotak digit memicu verifikasi otomatis; tombol [Verify] tidak diklik.
  - TC-AUTH-LP-159 Post Condition menyebut persetujuan tersimpan untuk versi aktif, tetapi tidak ada langkah yang mengamatinya selain tidak tampilnya layar Confirm to Continue.
