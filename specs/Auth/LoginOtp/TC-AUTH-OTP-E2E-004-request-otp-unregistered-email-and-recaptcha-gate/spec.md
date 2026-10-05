---
id: TC-AUTH-OTP-E2E-004-request-otp-unregistered-email-and-recaptcha-gate
title: Validasi email belum terdaftar dan proteksi reCAPTCHA gate belum diselesaikan
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AUTH-OTP-7
  - TC-AUTH-OTP-11
  - TC-AUTH-OTP-71
coverage:
  web: automated
---

# Validasi email belum terdaftar dan proteksi reCAPTCHA gate belum diselesaikan

## Prerequisites

- Browser berada pada status publik (belum login)
- Satu akun email valid yang dipastikan belum pernah terdaftar di sistem (`Fixture.auth.unregisteredUserEmail`)
- Satu akun aktif terdaftar (`Fixture.auth.standardUserEmail`)

## Test Steps

### Email Belum Terdaftar

1. Buka halaman Input Email Login with OTP
2. Masukkan alamat email yang belum terdaftar `Fixture.auth.unregisteredUserEmail`
3. Selesaikan verifikasi reCAPTCHA
4. Klik tombol `[Request OTP]`
5. Verifikasi pengiriman OTP diblokir dan pesan error inline "Email is not registered yet" muncul di bawah field Email
6. Verifikasi kegagalan ini TIDAK menghasilkan entri audit log baru pada surface log (proteksi log pollution)

### Proteksi reCAPTCHA Gate Belum Dicentang

7. Bersihkan field Email dan masukkan email terdaftar `Fixture.auth.standardUserEmail`
8. Biarkan widget reCAPTCHA dalam keadaan kosong / belum dicentang
9. Klik tombol `[Request OTP]`
10. Verifikasi pengiriman OTP diblokir dan notifikasi peringatan "Please verify that you are not a robot" muncul di area reCAPTCHA
11. Verifikasi sistem tidak membuat token OTP baru
12. Menggunakan sesi admin, periksa Activity Log Session
13. Verifikasi kegagalan ini dicatat sebagai status Failed dengan catatan "Captcha not completed"

## Notes

- TAG Samurai menolak request untuk email yang belum terdaftar dan tidak mencatatnya ke audit log untuk mencegah serangan log pollution dari sumber anonim.
- Sebaliknya, upaya submit tanpa menyelesaikan reCAPTCHA dicatat di audit log sebagai indikasi botting/spamming.
