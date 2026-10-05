---
id: TC-AUTH-MFA-E2E-053-security-direct-url-access-guard
title: Akses langsung via URL ke rute faktor kedua tanpa sesi pre auth diredirect ke login
priority: Critical
caseType: Security
status: draft
sourceTc:
  - TC-AUTH-MFA-95
coverage:
  web: automated
---

# Akses langsung via URL ke rute faktor kedua tanpa sesi pre auth diredirect ke login

## Prerequisites

- Mode: FE+BE
- Sesi browser baru tanpa token `mfa_session` (unauthenticated)

## Test Steps

1. Ketikkan URL rute langsung halaman MFA (misalnya `/auth/mfa/choose-method` atau `/auth/mfa/authenticator`)
2. Tekan Enter
3. Verifikasi sistem menolak akses tanpa token pre-auth valid
4. Verifikasi browser seketika di-redirect kembali ke halaman Login awal (`/auth/login`)

## Notes

- TC Frontend Ref: `TC-AUTH-MFA-FE-53`
- Merepresentasikan `TC-AUTH-MFA-95` (FE Ref: `TC-AUTH-MFA-FE-53`).
