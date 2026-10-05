---
id: TC-AUTH-OTP-E2E-021-otp-verification-invalid-code-and-clearing
title: Verifikasi OTP gagal karena kode salah, clearing field, dan reset fokus
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AUTH-OTP-40
  - TC-AUTH-OTP-47
  - TC-AUTH-OTP-69
coverage:
  web: automated
---

# Verifikasi OTP gagal karena kode salah, clearing field, dan reset fokus

## Prerequisites

- Akun aktif terdaftar tersedia di database (`Fixture.auth.standardUserEmail`)
- Halaman Input OTP telah terbuka dengan kode OTP 6 digit aktif

## Test Steps

1. Pada halaman Input OTP, masukkan 6 digit kode yang salah ("111111")
2. Verifikasi auto-submit terpicu secara otomatis begitu digit ke-6 dimasukkan
3. Verifikasi sistem menolak verifikasi dengan menampilkan pesan error inline "Invalid code" di bawah grup field OTP
4. Verifikasi bahwa kode OTP yang benar belum ter-consume (`used=false`) dan sesi belum terkunci
5. Verifikasi bahwa seluruh 6 kotak input dapat dikosongkan (clearable)
6. Verifikasi kursor fokus kembali ke Box 1 untuk pengetikan ulang
7. Menggunakan sesi admin, periksa Activity Log Session dan User Log
8. Verifikasi kegagalan verifikasi ini dicatat di kedua surface log dengan status Failed dan Note "Incorrect OTP"

## Notes

- Kegagalan verifikasi dengan kode salah tidak menghanguskan kode yang valid, user masih diberi kesempatan mencoba ulang selama kode belum expired.
- Kasus kode kedaluwarsa dipisahkan ke `TC-AUTH-OTP-E2E-022`, reuse kode dipisahkan ke `TC-AUTH-OTP-E2E-023`, dan independensi password lock dipisahkan ke `TC-AUTH-OTP-E2E-024`.
