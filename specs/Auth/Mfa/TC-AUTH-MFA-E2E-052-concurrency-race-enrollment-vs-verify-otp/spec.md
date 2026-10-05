---
id: TC-AUTH-MFA-E2E-052-concurrency-race-enrollment-vs-verify-otp
title: Kondisi balapan simultan verifikasi setup enrollment Tab A vs verifikasi OTP Tab B
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AUTH-MFA-122
coverage:
  web: automated
---

# Kondisi balapan simultan verifikasi setup enrollment Tab A vs verifikasi OTP Tab B

## Prerequisites

- Mode: FE+BE
- Tab A berada di layar setup enrollment Authenticator
- Tab B berada di layar verifikasi OTP MFA dengan `mfa_session` yang sama

## Test Steps

1. Submit kode verifikasi setup pada Tab A bersamaan dengan auto-submit OTP pada Tab B
2. Simulasikan OTP Tab B berhasil diverifikasi terlebih dahulu
3. Verifikasi verifikasi setup enrollment Tab A ditolak dan status `is_active` enrollment tetap bernilai `false`
4. Verifikasi sesi tidak berada dalam status campuran

## Notes

- TC Frontend Ref: `TC-AUTH-MFA-FE-52`
- Merepresentasikan `TC-AUTH-MFA-122` (FE Ref: `TC-AUTH-MFA-FE-52`).
