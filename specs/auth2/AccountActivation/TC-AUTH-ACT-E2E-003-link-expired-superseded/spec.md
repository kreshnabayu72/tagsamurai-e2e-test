---
id: TC-AUTH-ACT-E2E-003-link-expired-superseded
title: Link expired dan superseded mengarah ke 404 "Activation Link Expired"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AUTH-ACT-11
  - TC-AUTH-ACT-13
coverage:
  web: automated
---

# Link expired dan superseded mengarah ke 404 "Activation Link Expired"

## Prerequisites

- Token `active` expired (>24 jam) tersedia.
- Token `superseded` (di-invalidasi oleh resend, umur < 24 jam) tersedia untuk user terkait.

## Test Steps

### A. Token expired

1. Buka `/activate?token={expiredToken}` untuk token `active` namun `now > expires_at`.
2. Verifikasi halaman 404 dirender.
3. Verifikasi title halaman 404 adalah `"Activation Link Expired"`.
4. Verifikasi body halaman sesuai copy varian Expired (tanpa CTA).

### B. Token superseded (invalidated by resend)

5. Buka `/activate?token={supersededToken}` (link lama sebelum resend).
6. Verifikasi halaman 404 dirender dengan title `"Activation Link Expired"` (bukan varian "Used") sesuai mapping spesifikasi.

## Notes

- Token superseded walau umur < 24 jam harus mengarah ke 404 varian "Expired".
