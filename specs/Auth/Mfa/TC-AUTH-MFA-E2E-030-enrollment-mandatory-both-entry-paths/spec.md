---
id: TC-AUTH-MFA-E2E-030-enrollment-mandatory-both-entry-paths
title: Pendaftaran Authenticator wajib dari kedua jalur masuk Choose Method dan Login OTP
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-MFA-56
coverage:
  web: automated
---

# Pendaftaran Authenticator wajib dari kedua jalur masuk Choose Method dan Login OTP

## Prerequisites

- Mode: FE+BE
- User belum pernah mendaftarkan Authenticator app

## Test Steps

### Jalur Masuk dari Password > Choose Method
1. Login Faktor-1 via Password, pilih kartu "Authenticator app" pada Choose Method
2. Verifikasi pengguna diarahkan ke halaman "Set up authenticator app"

### Jalur Masuk dari Login with OTP
3. Login Faktor-1 via OTP pada akun lain yang belum enroll Authenticator
4. Verifikasi pasca verifikasi OTP Faktor-1, pengguna langsung diarahkan ke halaman "Set up authenticator app" yang sama
5. Verifikasi kedua jalur masuk menjamin kepatuhan pendaftaran sebelum verifikasi dapat dilakukan

## Notes

- TC Frontend Ref: `TC-AUTH-MFA-FE-30`
- Merepresentasikan `TC-AUTH-MFA-56` (FE Ref: `TC-AUTH-MFA-FE-30`).
