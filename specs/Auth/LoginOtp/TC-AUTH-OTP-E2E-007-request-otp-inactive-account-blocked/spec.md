---
id: TC-AUTH-OTP-E2E-007-request-otp-inactive-account-blocked
title: Request OTP diblokir untuk akun berstatus Inactive
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AUTH-OTP-24
  - TC-AUTH-OTP-70
coverage:
  web: automated
---

# Request OTP diblokir untuk akun berstatus Inactive

## Prerequisites

- Akun terdaftar berstatus Inactive / dinonaktifkan oleh admin (`is_active = false` / Global Toggle OFF) tersedia di database (`Fixture.auth.inactiveUser`)
- Halaman Login with OTP dapat diakses

## Test Steps

1. Buka halaman Input Email Login with OTP
2. Masukkan alamat email akun inactive (`Fixture.auth.inactiveUser`)
3. Selesaikan verifikasi reCAPTCHA
4. Klik tombol `[Request OTP]`
5. Verifikasi pengiriman OTP diblokir di sisi server
6. Verifikasi toast notifikasi error muncul di pojok kanan bawah dengan teks "Error, your account is inactive. Please contact the administrator to activate your account."
7. Verifikasi halaman tetap berada di Input Email
8. Verifikasi tidak ada email kode OTP yang terkirim
9. Menggunakan sesi admin, periksa Activity Log Session dan User Log
10. Verifikasi percobaan ini dicatat pada Activity Log Session dengan status Failed dan Note "User is inactive"
11. Verifikasi entri serupa juga tercatat pada User Log untuk user tersebut

## Notes

- Akun yang dinonaktifkan oleh administrator ditolak secara tegas dengan pesan yang mengarahkan user menghubungi admin.
