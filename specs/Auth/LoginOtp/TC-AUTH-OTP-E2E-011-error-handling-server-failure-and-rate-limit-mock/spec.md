---
id: TC-AUTH-OTP-E2E-011-error-handling-server-failure-and-rate-limit-mock
title: Penanganan kegagalan server 500 dan HTTP 429 IP rate limit pada halaman Input Email
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AUTH-OTP-27
  - TC-AUTH-OTP-72
  - TC-AUTH-OTP-79
coverage:
  web: automated
---

# Penanganan kegagalan server 500 dan HTTP 429 IP rate limit pada halaman Input Email

## Prerequisites

- Mode: mock (intersep HTTP pada endpoint `POST /v2/iam/auth/otp/request`)
- Akun aktif terdaftar (`Fixture.auth.standardUserEmail`)

## Test Steps

### Kegagalan Pengiriman OTP (HTTP 500 / Email Service Down)

1. Buka halaman Input Email Login with OTP
2. Konfigurasikan intersep endpoint `POST /v2/iam/auth/otp/request` untuk mengembalikan status HTTP 500
3. Masukkan email valid, selesaikan reCAPTCHA, lalu klik `[Request OTP]`
4. Verifikasi toast notifikasi error muncul dengan teks "Error, failed to send the code."
5. Verifikasi halaman tetap berada di Input Email (tidak berpindah ke halaman OTP)
6. Verifikasi tidak ada kode OTP baru yang dibuat dan tidak ada entri audit log baru yang tertulis

### IP Rate Limiting Terlampaui (HTTP 429 Too Many Requests)

7. Simulasikan pengiriman request berulang dari IP yang sama melebihi batas toleransi rate limit sehingga endpoint `POST /v2/iam/auth/otp/request` mengembalikan status HTTP 429
8. Klik tombol `[Request OTP]`
9. Verifikasi sistem menampilkan pesan inline atau toast error yang mengindikasikan rate limit ("Too many requests. Please wait a moment before trying again.")
10. Verifikasi tidak ada kode OTP yang terkirim dan kegagalan rate limit transport ini TIDAK dicatat ke Activity Log Session

## Notes

- TAG Samurai memproteksi endpoint request OTP dari brute force / DoS berbasis IP menggunakan HTTP 429.
- Kegagalan teknis transport server 500 maupun HTTP 429 tidak dicatat di surface audit log (hanya kegagalan bisnis otentikasi yang dicatat).
