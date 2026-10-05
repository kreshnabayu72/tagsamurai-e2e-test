---
id: TC-AUTH-OTP-E2E-006-request-otp-pending-activation-blocked
title: Request OTP diblokir untuk akun berstatus Pending Activation
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AUTH-OTP-23
  - TC-AUTH-OTP-70
coverage:
  web: automated
---

# Request OTP diblokir untuk akun berstatus Pending Activation

## Prerequisites

- Akun terdaftar berstatus "Pending Activation" (belum pernah aktivasi via email undangan) tersedia di database (`Fixture.auth.pendingActivationUser`)
- Halaman Login with OTP dapat diakses

## Test Steps

1. Buka halaman Input Email Login with OTP
2. Masukkan alamat email user berstatus Pending Activation (`Fixture.auth.pendingActivationUser`)
3. Selesaikan verifikasi reCAPTCHA
4. Klik tombol `[Request OTP]`
5. Verifikasi pengiriman OTP diblokir di sisi server
6. Verifikasi toast notifikasi error muncul di pojok kanan bawah dengan teks "Error, your account is not activated yet. Please activate your account first."
7. Verifikasi halaman tidak berpindah ke halaman Input OTP (tetap di halaman Input Email)
8. Verifikasi tidak ada email kode OTP yang terkirim
9. Menggunakan sesi admin, periksa Activity Log Session dan User Log
10. Verifikasi percobaan ini dicatat pada Activity Log Session dengan status Failed dan Note "User not activated"
11. Verifikasi entri log serupa juga tercatat pada User Log untuk user terkait

## Notes

- TAG Samurai memblokir seluruh mekanisme login (Password maupun OTP) sebelum pengguna melakukan aktivasi akun.
- Kegagalan ini teridentifikasi akunnya sehingga wajib dicatat ke audit log dengan status Failed.
