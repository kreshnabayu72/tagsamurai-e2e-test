---
id: TC-AUTH-OTP-E2E-010-error-handling-recaptcha-timeout-mock
title: Penanganan provider reCAPTCHA down/timeout dan retry request OTP
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AUTH-OTP-14
  - TC-AUTH-OTP-76
coverage:
  web: automated
---

# Penanganan provider reCAPTCHA down/timeout dan retry request OTP

## Prerequisites

- Mode: mock (intersep HTTP pada endpoint verifikasi captcha dan request OTP)
- Akun aktif terdaftar (`Fixture.auth.standardUserEmail`)

## Test Steps

### Provider reCAPTCHA Timeout / Down

1. Buka halaman Input Email Login with OTP
2. Konfigurasikan intersep jaringan agar respons verifikasi reCAPTCHA mengalami timeout atau status HTTP 5xx
3. Masukkan email valid dan coba klik tombol `[Request OTP]`
4. Verifikasi sistem memperlakukan kondisi ini sebagai gangguan jaringan dengan memunculkan toast error retry
5. Verifikasi sistem TIDAK meloloskan request OTP tanpa token captcha yang terverifikasi

### Retry Request OTP Setelah Timeout Client

6. Buka kembali halaman Input Email dengan reCAPTCHA normal
7. Selesaikan reCAPTCHA, lalu klik `[Request OTP]`
8. Konfigurasikan response request pertama mengalami timeout jaringan di sisi client saat server sebenarnya berhasil menerbitkan kode
9. Lakukan retry request dari client dengan parameter yang sama
10. Verifikasi server menerbitkan kode baru dan meng-invalidate kode sebelumnya tanpa error tak konsisten

## Notes

- Penanganan kegagalan server HTTP 500 dan IP rate limit HTTP 429 pada Input Email dipisahkan ke `TC-AUTH-OTP-E2E-011`.
- Penanganan kegagalan server pada verifikasi OTP dipisahkan ke `TC-AUTH-OTP-E2E-026`.
