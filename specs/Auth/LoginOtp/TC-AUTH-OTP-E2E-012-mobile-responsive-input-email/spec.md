---
id: TC-AUTH-OTP-E2E-012-mobile-responsive-input-email
title: Tampilan mobile responsive halaman Input Email dan peniadaan reCAPTCHA
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-OTP-2
  - TC-AUTH-OTP-13
  - TC-AUTH-OTP-98
coverage:
  web: automated
---

# Tampilan mobile responsive halaman Input Email dan peniadaan reCAPTCHA

## Prerequisites

- Mode: mock (pengujian tampilan responsive dan emulasi perangkat mobile)
- Konfigurasi viewport mobile app / layar kecil (375x812 atau setara)
- User aktif normal (`Fixture.auth.standardUserEmail`)

## Test Steps

1. Atur viewport browser ke ukuran mobile (contoh: 375x812)
2. Buka halaman Input Email Login with OTP dengan parameter emulasi platform mobile
3. Verifikasi layout halaman berorientasi vertikal penuh (full-screen vertical stack)
4. Verifikasi widget reCAPTCHA TIDAK ditampilkan sama sekali pada platform mobile (Must NOT)
5. Masukkan email valid tanpa token reCAPTCHA lalu klik tombol `[Request OTP]`
6. Verifikasi submit diproses tanpa ditolak oleh validasi captcha
7. Verifikasi proses berhasil berpindah ke halaman Input OTP

## Notes

- Sesuai spesifikasi PRD F-AUTHOTP-01 & F-AUTHOTP-09, widget reCAPTCHA hanya berlaku di web dan dilarang muncul pada aplikasi mobile.
- Pengujian tampilan mobile pada halaman Input OTP, numeric keyboard inputmode, dan tap target >= 44px dipisahkan ke `TC-AUTH-OTP-E2E-018`.
