---
id: TC-AUTH-OTP-E2E-001-request-otp-email-screening
title: Screening form Input Email Login with OTP
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-OTP-1
  - TC-AUTH-OTP-97
coverage:
  web: automated
---

# Screening form Input Email Login with OTP

## Prerequisites

- Browser berada pada status publik (belum login / unauthenticated session)
- Halaman Login with Password dapat diakses

## Test Steps

1. Buka halaman Login with Password
2. Klik link "Log in with OTP"
3. Verifikasi browser berpindah ke halaman Input Email Login with OTP
4. Verifikasi judul halaman menampilkan teks "Login with OTP"
5. Verifikasi terdapat field Email kosong dengan placeholder "Enter your email"
6. Verifikasi field Email memiliki atribut `inputmode="email"`
7. Verifikasi widget reCAPTCHA tampil di bawah field Email
8. Verifikasi tombol `[Request OTP]` dalam status enabled
9. Verifikasi link "Use password instead" tampil di bawah tombol submit
10. Verifikasi tidak ada checkbox Agreement (kebijakan privasi) dalam bentuk apa pun pada halaman ini

## Notes

- Sesuai koreksi arsitektur 2026-07-28, checkbox Agreement tidak pernah muncul di halaman Input Email, melainkan baru dievaluasi pada layar "Confirm to Continue" setelah verifikasi OTP sukses.
- Validasi field email dipisahkan ke `TC-AUTH-OTP-E2E-003`, dan alur navigasi bolak-balik dipisahkan ke `TC-AUTH-OTP-E2E-002`.
