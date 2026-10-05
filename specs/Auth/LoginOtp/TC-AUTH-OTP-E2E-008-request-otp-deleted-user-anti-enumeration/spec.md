---
id: TC-AUTH-OTP-E2E-008-request-otp-deleted-user-anti-enumeration
title: Request OTP untuk akun terhapus diblokir dengan proteksi anti-enumeration
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AUTH-OTP-101
  - TC-AUTH-OTP-71
coverage:
  web: automated
---

# Request OTP untuk akun terhapus diblokir dengan proteksi anti-enumeration

## Prerequisites

- Akun yang sebelumnya terdaftar namun telah dihapus (soft-deleted / `deleted_at IS NOT NULL`) di database (`Fixture.auth.deletedUser`)
- Halaman Login with OTP dapat diakses

## Test Steps

1. Buka halaman Input Email Login with OTP
2. Masukkan alamat email akun yang sudah dihapus (`Fixture.auth.deletedUser`)
3. Selesaikan verifikasi reCAPTCHA
4. Klik tombol `[Request OTP]`
5. Verifikasi pengiriman OTP diblokir
6. Verifikasi pesan error yang muncul persis sama dengan pesan untuk email yang belum pernah terdaftar: "Email is not registered yet" (anti-enumeration protection)
7. Verifikasi sistem TIDAK membocorkan status bahwa akun ini pernah ada atau telah dihapus
8. Menggunakan sesi admin, periksa Activity Log Session dan User Log
9. Verifikasi bahwa percobaan ini TIDAK menghasilkan entri audit log baru sama sekali (perlindungan zero log)

## Notes

- TAG Samurai menerapkan prinsip proteksi anti-enumeration untuk mencegah penyerang memetakan keberadaan akun lama yang telah dihapus.
