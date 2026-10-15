---
id: TC-AUTH-LP-E2E-018-mobile-login-screening-and-success
title: "Screening Layar Login Mobile Tanpa reCAPTCHA dan Login Berhasil"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-LP-06
  - TC-AUTH-LP-70
coverage:
  mobile: automated
---

# Screening Layar Login Mobile Tanpa reCAPTCHA dan Login Berhasil

## Prerequisites

- Seeding: user subjek dibuat lewat API di hook `before` oleh akun aktor Total Control (Global Settings) `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net` (kredensial `Spectra.env.GS_TC_PASSWORD`): Create User lalu aktivasi dengan password `Spectra.env.LP_PASSWORD`. User dihapus di hook `after`, dan pembersihan tidak berasumsi seeding berhasil penuh.
- Environment variable: `GS_TC_PASSWORD`, `LP_PASSWORD`. Password akun tidak ditulis di spec atau fixture.
- Kemampuan teknis: aplikasi native Android TAG Samurai Mobile (perangkat atau emulator); fixture BE untuk device terpercaya di mobile dan penandaan tanpa gate Agreement dan MFA di mobile.
- Mode: FE+BE.
- TC-AUTH-LP-06: User belum login; aplikasi native Android TAG Samurai Mobile
- TC-AUTH-LP-70: User `Budi Santoso` (`budisantoso+{runId}-018@qwertysystem.net`) berstatus Activated dan Active; device terpercaya di mobile; tidak ada gate Agreement dan MFA di mobile; aplikasi native Android TAG Samurai Mobile
- TC-AUTH-LP-70 data: Email `budisantoso+{runId}-018@qwertysystem.net`; Password nilai `Spectra.env.LP_PASSWORD`

## Test Steps

### TC-AUTH-LP-06: Screening layar Login with Password di aplikasi mobile tidak merender reCAPTCHA

1. Buka layar Login with Password di aplikasi
2. Susuri layar dari atas ke bawah tanpa klik apa pun
3. Verifikasi Logo TAG Samurai tampil
4. Verifikasi Title "Login with Password" tampil
5. Verifikasi Subtitle "Sign in and start managing your assets" tampil
6. Verifikasi field Email tampil
7. Verifikasi field Password tampil
8. Verifikasi toggle intip pada field Password tampil
9. Verifikasi Button [Log in] lebar penuh tampil
10. Verifikasi link [Log in with OTP] tampil
11. Verifikasi link "Forgot your password? " [Reset here] tampil
12. Verifikasi **Must NOT**: widget reCAPTCHA tidak dirender
13. Verifikasi **Must NOT**: caption "Please verify that you are not a robot" tidak dirender

### TC-AUTH-LP-70: Login berhasil di aplikasi mobile tanpa reCAPTCHA menuju Portal — Product Hub

14. Buka layar Login with Password di aplikasi
15. Ketik email `budisantoso+{runId}-018@qwertysystem.net` di field Email
16. Ketik password nilai `Spectra.env.LP_PASSWORD` di field Password
17. Ketuk [Log in] tanpa langkah reCAPTCHA
18. Verifikasi login berhasil: aplikasi menuju Portal — Product Hub
19. Logout dari aplikasi

## Notes

- Mode: FE+BE. Sumber: `auth/login-password/TestCases/tc-login-password.md`.
- Screening (TC-AUTH-LP-06) di awal spec, sebelum aksi login (prinsip 2 dan 3).
- Langkah 19 (logout) adalah langkah penghubung tanpa awalan `Verifikasi` (S-03).
- Alasan penggabungan screening (TC-AUTH-LP-06, tampilan murni) dengan seeding dan login (TC-AUTH-LP-70) dalam satu spec: keduanya memakai platform mobile yang sama, layar Login with Password yang sama (screening dahulu, lalu login di layar itu), sesi guest yang sama, dan tidak butuh harness lain; seeding user di hook `before` hanya dipakai TC-AUTH-LP-70 dan tidak mengubah layar yang di-screening.
