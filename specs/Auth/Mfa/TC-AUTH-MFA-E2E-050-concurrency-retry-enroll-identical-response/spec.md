---
id: TC-AUTH-MFA-E2E-050-concurrency-retry-enroll-identical-response
title: Retry permintaan pendaftaran Authenticator mengembalikan respons QR dan rahasia identik
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AUTH-MFA-93
coverage:
  web: automated
---

# Retry permintaan pendaftaran Authenticator mengembalikan respons QR dan rahasia identik

## Prerequisites

- Mode: FE+BE
- Permintaan awal pendaftaran Authenticator aktif

## Test Steps

1. Kirim permintaan pendaftaran Authenticator
2. Catat secret key dan URI QR code yang dihasilkan
3. Lakukan retry permintaan dengan token `mfa_session` yang sama
4. Verifikasi nilai secret key dan QR code yang dikembalikan persis sama tanpa menghasilkan secret baru

## Notes

- TC Frontend Ref: `TC-AUTH-MFA-FE-50`
- Merepresentasikan `TC-AUTH-MFA-93` (FE Ref: `TC-AUTH-MFA-FE-50`).
