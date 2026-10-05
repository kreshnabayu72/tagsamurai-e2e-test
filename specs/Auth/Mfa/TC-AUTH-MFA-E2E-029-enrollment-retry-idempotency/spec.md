---
id: TC-AUTH-MFA-E2E-029-enrollment-retry-idempotency
title: Retry permintaan enrollment dengan pre auth session sama bersifat idempoten
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AUTH-MFA-55
coverage:
  web: automated
---

# Retry permintaan enrollment dengan pre auth session sama bersifat idempoten

## Prerequisites

- Mode: FE+BE
- Permintaan awal pendaftaran Authenticator sukses diproses di server namun client mengalami timeout

## Test Steps

1. Simulasikan retry permintaan pendaftaran oleh client menggunakan `mfa_session` yang sama
2. Verifikasi server mengembalikan respons QR code dan secret key yang PERSIS SAMA dengan percobaan pertama
3. Verifikasi server tidak membuat secret key baru yang akan membatalkan pairing pengguna sebelumnya

## Notes

- TC Frontend Ref: `TC-AUTH-MFA-FE-29`
- Merepresentasikan `TC-AUTH-MFA-55` (FE Ref: `TC-AUTH-MFA-FE-29`).
