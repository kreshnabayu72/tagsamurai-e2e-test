---
id: TC-AUTH-MFA-E2E-022-otp-invalid-after-email-changed
title: Kode OTP MFA lama invalid setelah alamat email akun diubah pada sesi lain
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AUTH-MFA-38
coverage:
  web: automated
---

# Kode OTP MFA lama invalid setelah alamat email akun diubah pada sesi lain

## Prerequisites

- Mode: FE+BE
- Sesi OTP MFA sedang menunggu input kode di Tab A
- Pada Tab B / sesi lain, email akun diubah via My Profile > Change Email

## Test Steps

1. Masukkan kode OTP yang diterbitkan sebelum email akun diubah ke form pada Tab A
2. Tunggu proses auto-submit mengevaluasi kode
3. Verifikasi sistem menolak kode tersebut dengan caption "Invalid code"
4. Verifikasi entri tercatat di kedua surface log dengan Status "Failed" dan Note "OTP invalid — email changed"

## Notes

- TC Frontend Ref: `TC-AUTH-MFA-FE-22`
- Merepresentasikan `TC-AUTH-MFA-38` (FE Ref: `TC-AUTH-MFA-FE-22`).
