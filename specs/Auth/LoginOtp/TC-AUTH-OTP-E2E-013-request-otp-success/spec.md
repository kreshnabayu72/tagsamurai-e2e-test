---
id: TC-AUTH-OTP-E2E-013-request-otp-success
title: Request OTP sukses, proteksi double-submit, dan toast notifikasi pengiriman
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-OTP-12
  - TC-AUTH-OTP-25
  - TC-AUTH-OTP-30
coverage:
  web: automated
---

# Request OTP sukses, proteksi double-submit, dan toast notifikasi pengiriman

## Prerequisites

- Browser berada pada status publik (belum login)
- Akun aktif terdaftar (`Fixture.auth.standardUserEmail`)
- Layanan pengiriman email testing aktif dan dapat diinspeksi

## Test Steps

1. Buka halaman Input Email Login with OTP
2. Masukkan email valid `Fixture.auth.standardUserEmail`
3. Selesaikan verifikasi reCAPTCHA hingga tercentang
4. Klik tombol `[Request OTP]` dua kali secara cepat untuk menguji proteksi double-submit
5. Verifikasi hanya 1 permintaan HTTP request yang dikirimkan ke server dan tombol langsung disabled/loading selama proses berjalan
6. Verifikasi toast notifikasi muncul di pojok kanan bawah dengan teks "Success, the code has been sent."
7. Verifikasi browser otomatis diarahkan ke halaman Input OTP
8. Verifikasi email notifikasi dengan subjek "Your TAG Samurai one-time password (OTP)" terkirim ke kotak masuk `Fixture.auth.standardUserEmail`
9. Verifikasi kode OTP 6 digit diterbitkan dengan masa berlaku 5 menit (`expires_at = now + 5m`)

## Notes

- Screening elemen halaman Input OTP dipisahkan ke `TC-AUTH-OTP-E2E-016`.
- Aksesibilitas keyboard 6 field OTP dipisahkan ke `TC-AUTH-OTP-E2E-017`.
- Pengujian boundary email 120 karakter dipisahkan ke `TC-AUTH-OTP-E2E-005`.
