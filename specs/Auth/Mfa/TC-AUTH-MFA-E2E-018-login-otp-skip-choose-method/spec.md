---
id: TC-AUTH-MFA-E2E-018-login-otp-skip-choose-method
title: Login Faktor-1 via OTP melewati layar Choose Method langsung ke Authenticator
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AUTH-MFA-27
coverage:
  web: automated
---

# Login Faktor-1 via OTP melewati layar Choose Method langsung ke Authenticator

## Prerequisites

- Mode: FE+BE
- User login menggunakan metode Login with OTP sebagai Faktor-1
- Login terpicu kondisi MFA

## Test Steps

1. Selesaikan verifikasi kode OTP pada alur Login with OTP (Faktor-1)
2. Verifikasi sistem mengevaluasi bahwa Faktor-1 sudah merupakan OTP
3. Verifikasi layar "Choose verification method" DILEWATI (tidak ditampilkan)
4. Verifikasi pengguna langsung diarahkan ke Authenticator Verification (atau Setup Authenticator jika belum enrolled) untuk menjamin prinsip autentikasi multifaktor ortogonal

## Notes

- TC Frontend Ref: `TC-AUTH-MFA-FE-18`
- Merepresentasikan `TC-AUTH-MFA-27` (FE Ref: `TC-AUTH-MFA-FE-18`).
- Menjamin kepatuhan aturan bahwa faktor kedua tidak boleh menawarkan kembali faktor yang identik dengan faktor pertama.
