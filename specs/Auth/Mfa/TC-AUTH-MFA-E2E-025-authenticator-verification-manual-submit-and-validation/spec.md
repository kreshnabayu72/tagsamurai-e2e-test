---
id: TC-AUTH-MFA-E2E-025-authenticator-verification-manual-submit-and-validation
title: Verifikasi kode Authenticator tanpa auto submit validasi kode salah dan login sukses
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-MFA-41
  - TC-AUTH-MFA-42
  - TC-AUTH-MFA-43
  - TC-AUTH-MFA-45
  - TC-AUTH-MFA-47
coverage:
  web: automated
---

# Verifikasi kode Authenticator tanpa auto submit validasi kode salah dan login sukses

## Prerequisites

- Mode: FE+BE
- User telah terdaftar Authenticator app
- Halaman Authenticator Verification terbuka dengan judul "Enter authenticator code"

## Test Steps

### Penolakan Submit Kosong
1. Klik tombol CTA `[Login]` tanpa mengisi digit kode
2. Verifikasi caption error muncul dan di log tercatat Status "Failed", Note "Empty OTP"

### Peniadaan Auto-Submit & Penolakan Kode Salah
3. Ketik 6 digit kode salah (misalnya "123456")
4. Verifikasi sistem TIDAK melakukan auto-submit saat digit ke-6 diisi (pengguna harus klik tombol `[Login]` secara manual)
5. Klik tombol `[Login]`
6. Verifikasi caption error menampilkan "Invalid code", field dikosongkan, dan tercatat Status "Failed", Note "Incorrect OTP"

### Penolakan Kode di Luar Drift Window
7. Masukkan kode TOTP yang sudah kedaluwarsa ≥2 interval waktu (di luar drift window)
8. Klik `[Login]` dan verifikasi kode ditolak dengan caption "Invalid code"

### Verifikasi Kode Benar
9. Masukkan kode TOTP 6 digit yang valid dari aplikasi authenticator
10. Klik tombol `[Login]`
11. Verifikasi login berhasil dan pengguna mendarat di Portal

## Notes

- TC Frontend Ref: `TC-AUTH-MFA-FE-25`
- Merepresentasikan `TC-AUTH-MFA-41`, `42`, `43`, `45`, `47` (FE Ref: `TC-AUTH-MFA-FE-25`).
- Berbeda dari Login OTP, verifikasi TOTP Authenticator tidak menggunakan auto-submit untuk mencegah submission yang tidak disengaja.
