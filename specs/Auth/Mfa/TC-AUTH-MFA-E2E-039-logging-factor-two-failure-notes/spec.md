---
id: TC-AUTH-MFA-E2E-039-logging-factor-two-failure-notes
title: Pencatatan kegagalan faktor kedua ke kedua surface sesuai enum Note spesifik
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-MFA-79
coverage:
  web: automated
---

# Pencatatan kegagalan faktor kedua ke kedua surface sesuai enum Note spesifik

## Prerequisites

- Mode: FE+BE
- Berbagai kondisi kegagalan pada faktor kedua (OTP / Authenticator)

## Test Steps

1. Picu kegagalan kode salah pada form OTP/Authenticator
2. Verifikasi di kedua surface log tercatat Status "Failed" dengan Note "Incorrect OTP"
3. Picu kegagalan kode kedaluwarsa pada form OTP
4. Verifikasi di kedua surface log tercatat Status "Failed" dengan Note "OTP expired"
5. Picu kegagalan kode kosong melalui tombol fallback
6. Verifikasi di kedua surface log tercatat Status "Failed" dengan Note "Empty OTP"
7. Picu submit kode lama setelah email akun diubah
8. Verifikasi di kedua surface log tercatat Status "Failed" dengan Note "OTP invalid — email changed"

## Notes

- TC Frontend Ref: `TC-AUTH-MFA-FE-39`
- Merepresentasikan `TC-AUTH-MFA-79` (FE Ref: `TC-AUTH-MFA-FE-39`).
