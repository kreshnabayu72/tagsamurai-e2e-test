---
id: TC-AUTH-MFA-E2E-041-logging-exclusion-otp-resend-action
title: Peniadaan pencatatan log audit untuk aksi resend OTP dalam konteks MFA
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AUTH-MFA-81
coverage:
  web: automated
---

# Peniadaan pencatatan log audit untuk aksi resend OTP dalam konteks MFA

## Prerequisites

- Mode: FE+BE
- Halaman verifikasi OTP MFA terbuka

## Test Steps

1. Klik tombol "Resend code" setelah cooldown 60 detik selesai
2. Verifikasi kode baru dikirimkan ke email
3. Periksa Activity Log Session dan User Log
4. Verifikasi NIHIL entri baru yang mencatat pengiriman ulang kode OTP tersebut

## Notes

- TC Frontend Ref: `TC-AUTH-MFA-FE-41`
- Merepresentasikan `TC-AUTH-MFA-81` (FE Ref: `TC-AUTH-MFA-FE-41`).
