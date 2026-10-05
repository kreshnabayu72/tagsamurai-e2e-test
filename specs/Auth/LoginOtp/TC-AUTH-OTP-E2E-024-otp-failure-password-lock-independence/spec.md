---
id: TC-AUTH-OTP-E2E-024-otp-failure-password-lock-independence
title: Kegagalan verifikasi OTP berulang tidak memengaruhi lock progression pada Login Password
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AUTH-OTP-45
  - TC-AUTH-OTP-102
coverage:
  web: automated
---

# Kegagalan verifikasi OTP berulang tidak memengaruhi lock progression pada Login Password
## Prerequisites

- Akun aktif terdaftar (`Fixture.auth.dualTrackUser`)
- Counter kegagalan login password pada database berada pada nilai 0 (`failed_login_attempts = 0`)

## Test Steps

1. Buka halaman Login with OTP untuk user `Fixture.auth.dualTrackUser`
2. Minta OTP hingga halaman Input OTP terbuka
3. Masukkan 6 digit kode salah ("000000") sebanyak 3 kali berturut-turut
4. Verifikasi setiap submission kode salah menampilkan pesan error inline "Invalid code"
5. Periksa status counter kegagalan password pada database
6. Verifikasi counter kegagalan password (`failed_login_attempts`) TETAP bernilai 0 dan akun TIDAK mengalami lock progression pada jalur Password
7. Buka tab browser baru dan akses halaman Login with Password (`/login-password`)
8. Masukkan email dan password yang benar untuk user `Fixture.auth.dualTrackUser`
9. Verifikasi login via password langsung berhasil tanpa terhalang banner akun terkunci maupun delay proteksi password

## Notes

- TAG Samurai memisahkan secara tegas metrik keamanan antara jalur Login Password (yang memiliki lock progression bertahap 1m/5m/10m) dan jalur Login OTP (yang hanya membatasi resend). Kegagalan verifikasi kode OTP tidak boleh memicu penguncian akun pada alur Password.
- Kebalikannya, akun yang sedang terkunci di alur Password tetap bisa login via OTP diuji pada `TC-AUTH-OTP-E2E-025`.
