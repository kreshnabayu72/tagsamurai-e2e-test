---
id: TC-AUTH-MFA-E2E-058-plan-gating-identical-across-tiers
title: Fitur MFA berlaku identik di seluruh tier lisensi plan tanpa opsi penonaktifan
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-MFA-120
coverage:
  web: automated
---

# Fitur MFA berlaku identik di seluruh tier lisensi plan tanpa opsi penonaktifan

## Prerequisites

- Mode: FE+BE
- Akun uji pada berbagai tier lisensi plan (Starter, Growth, Professional, Enterprise)

## Test Steps

1. Lakukan pengujian pemicu MFA pada akun dengan plan Starter
2. Verifikasi MFA berfungsi normal dan tidak dapat dinonaktifkan
3. Ulangi pengujian pada akun dengan plan Growth, Professional, dan Enterprise
4. Verifikasi seluruh fungsionalitas deteksi anomali, opsi verifikasi, dan logging berlaku seragam tanpa diskriminasi plan

## Notes

- TC Frontend Ref: `TC-AUTH-MFA-FE-58`
- Merepresentasikan `TC-AUTH-MFA-120` (FE Ref: `TC-AUTH-MFA-FE-58`).
