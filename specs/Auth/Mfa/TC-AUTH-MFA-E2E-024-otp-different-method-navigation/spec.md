---
id: TC-AUTH-MFA-E2E-024-otp-different-method-navigation
title: Navigasi Use a different method kembali ke Choose Method dan invalidate OTP aktif
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-MFA-40
coverage:
  web: automated
---

# Navigasi Use a different method kembali ke Choose Method dan invalidate OTP aktif

## Prerequisites

- Mode: FE+BE
- Halaman Verifikasi OTP (MFA) terbuka dengan kode aktif

## Test Steps

1. Klik tautan "Use a different method"
2. Verifikasi pengguna dialihkan kembali ke layar "Choose verification method"
3. Verifikasi kode OTP sebelumnya langsung dinyatakan tidak valid (invalidated)
4. Verifikasi tidak ada field untuk mengedit alamat email (alamat email OTP MFA terikat kuat pada akun dan tidak dapat diketik ulang)

## Notes

- TC Frontend Ref: `TC-AUTH-MFA-FE-24`
- Merepresentasikan `TC-AUTH-MFA-40` (FE Ref: `TC-AUTH-MFA-FE-24`).
