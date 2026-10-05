---
id: TC-AUTH-MFA-E2E-037-logging-note-factor-one-otp
title: Note login final di kedua surface mencatat Login with OTP saat faktor pertama OTP
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-MFA-75
coverage:
  web: automated
---

# Note login final di kedua surface mencatat Login with OTP saat faktor pertama OTP

## Prerequisites

- Mode: FE+BE
- Faktor-1 login menggunakan Login with OTP
- Faktor-2 diselesaikan menggunakan Authenticator app hingga sukses

## Test Steps

1. Lakukan login Faktor-1 via OTP
2. Pada layar MFA, selesaikan verifikasi Authenticator app hingga sukses mendarat di Portal
3. Buka Global Settings > Activity Log > Session dan User Log
4. Verifikasi entri login final pada kedua surface mencatat Status "Success" dengan Note "Login with OTP" (mengikuti metode Faktor-1, bukan faktor-2 Authenticator)

## Notes

- TC Frontend Ref: `TC-AUTH-MFA-FE-37`
- Merepresentasikan `TC-AUTH-MFA-75` (FE Ref: `TC-AUTH-MFA-FE-37`).
