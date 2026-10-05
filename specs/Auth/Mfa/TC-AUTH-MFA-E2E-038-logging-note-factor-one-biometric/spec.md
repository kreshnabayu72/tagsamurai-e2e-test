---
id: TC-AUTH-MFA-E2E-038-logging-note-factor-one-biometric
title: Note login final di kedua surface mencatat Login with biometric saat relogin mobile
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-MFA-76
coverage:
  web: automated
---

# Note login final di kedua surface mencatat Login with biometric saat relogin mobile

## Prerequisites

- Mode: FE+BE
- Faktor-1 menggunakan Biometric Re-login pada platform mobile dan memicu MFA

## Test Steps

1. Simulasikan keberhasilan Biometric Re-login (Faktor-1)
2. Verifikasi sebelum MFA tuntas, log Success belum ditulis
3. Selesaikan verifikasi faktor kedua hingga tuntas
4. Periksa Activity Log Session dan User Log
5. Verifikasi tercatat tepat 1 entri Success dengan Note "Login with biometric" yang ditulis oleh MFA setelah faktor kedua tuntas

## Notes

- TC Frontend Ref: `TC-AUTH-MFA-FE-38`
- Merepresentasikan `TC-AUTH-MFA-76` (FE Ref: `TC-AUTH-MFA-FE-38`).
