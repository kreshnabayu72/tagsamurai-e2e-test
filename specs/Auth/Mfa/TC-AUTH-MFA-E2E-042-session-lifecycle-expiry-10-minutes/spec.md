---
id: TC-AUTH-MFA-E2E-042-session-lifecycle-expiry-10-minutes
title: Sesi pre auth MFA kedaluwarsa setelah 10 menit membatalkan sesi dan redirect login
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AUTH-MFA-84
coverage:
  web: automated
---

# Sesi pre auth MFA kedaluwarsa setelah 10 menit membatalkan sesi dan redirect login

## Prerequisites

- Mode: FE+BE
- Pre-auth session `mfa_session` telah dibuat >10 menit yang lalu (TTL 10 menit terlewati)

## Test Steps

1. Buka kembali halaman verifikasi MFA yang telah dibiarkan idle selama >10 menit
2. Masukkan kode verifikasi valid dan submit
3. Verifikasi server menolak request dengan kode `MFA_SESSION_EXPIRED`
4. Verifikasi pengguna diredirect kembali ke halaman Login awal
5. Verifikasi pengguna diwajibkan mengulang proses login dari Faktor-1

## Notes

- TC Frontend Ref: `TC-AUTH-MFA-FE-42`
- Merepresentasikan `TC-AUTH-MFA-84` (FE Ref: `TC-AUTH-MFA-FE-42`).
