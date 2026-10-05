---
id: TC-AUTH-OTP-E2E-025-login-otp-password-locked-account-resilience
title: Akun yang sedang mengalami lock aktif di jalur Password tetap dapat login sukses via OTP
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-OTP-103
coverage:
  web: automated
---

# Akun yang sedang mengalami lock aktif di jalur Password tetap dapat login sukses via OTP

## Prerequisites

- Akun aktif terdaftar yang sedang dalam status terkunci aktif (locked out) akibat salah memasukkan password berulang kali pada alur Login with Password (`Fixture.auth.passwordLockedUser`)
- Status lock akun terverifikasi aktif pada database (`locked_until > now`)

## Test Steps

1. Buka halaman Login with Password dan coba submit password untuk `Fixture.auth.passwordLockedUser`
2. Verifikasi sistem menolak dengan pesan lock aktif ("Your account is locked due to too many failed attempts")
3. Dari halaman login, klik link "Log in with OTP"
4. Masukkan email user `Fixture.auth.passwordLockedUser` ke dalam form Input Email OTP
5. Selesaikan verifikasi reCAPTCHA dan klik `[Request OTP]`
6. Verifikasi request OTP diloloskan oleh sistem (tidak terblokir oleh lock status password)
7. Ambil kode OTP yang dikirimkan ke email user dan masukkan 6 digit kode yang benar ke halaman Input OTP
8. Verifikasi auto-submit terpicu dan verifikasi berhasil
9. Verifikasi browser sukses masuk ke Product Hub (login tuntas)

## Notes

- TAG Samurai sengaja mendesain Login with OTP sebagai jalur pemulihan (resilience/recovery track) bagi pengguna yang terblokir sementara di jalur password, selama kepemilikan email dapat dibuktikan melalui verifikasi OTP.
