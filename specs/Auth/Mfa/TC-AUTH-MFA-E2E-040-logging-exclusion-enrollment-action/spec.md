---
id: TC-AUTH-MFA-E2E-040-logging-exclusion-enrollment-action
title: Peniadaan pencatatan log audit untuk aksi pendaftaran atau aktivasi Authenticator
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AUTH-MFA-80
coverage:
  web: automated
---

# Peniadaan pencatatan log audit untuk aksi pendaftaran atau aktivasi Authenticator

## Prerequisites

- Mode: FE+BE
- User menyelesaikan setup pendaftaran Authenticator

## Test Steps

1. Selesaikan proses pendaftaran Authenticator Step 1 dan Step 2 dengan kode valid
2. Buka Global Settings > Activity Log > Session dan User Log
3. Verifikasi TIDAK ADA entri log baru yang mencatat aktivitas setup pendaftaran itu sendiri (sesuai aturan kanonikal §10)

## Notes

- TC Frontend Ref: `TC-AUTH-MFA-FE-40`
- Merepresentasikan `TC-AUTH-MFA-80` (FE Ref: `TC-AUTH-MFA-FE-40`).
