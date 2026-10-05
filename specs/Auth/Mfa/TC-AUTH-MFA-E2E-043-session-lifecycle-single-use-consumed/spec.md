---
id: TC-AUTH-MFA-E2E-043-session-lifecycle-single-use-consumed
title: Sesi pre auth MFA yang telah digunakan tidak dapat dipakai ulang untuk login kedua
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AUTH-MFA-85
coverage:
  web: automated
---

# Sesi pre auth MFA yang telah digunakan tidak dapat dipakai ulang untuk login kedua

## Prerequisites

- Mode: FE+BE
- Sesi MFA telah sukses diselesaikan pada Tab 1 (`mfa_session.is_consumed = true`)

## Test Steps

1. Buka Tab 2 yang masih menampilkan form verifikasi dengan `mfa_session` yang sama
2. Masukkan kode verifikasi valid pada Tab 2 dan submit
3. Verifikasi server menolak permintaan karena sesi pre-auth telah di-consume
4. Verifikasi tidak ada sesi login kedua atau entri log ganda yang tercipta

## Notes

- TC Frontend Ref: `TC-AUTH-MFA-FE-43`
- Merepresentasikan `TC-AUTH-MFA-85` (FE Ref: `TC-AUTH-MFA-FE-43`).
