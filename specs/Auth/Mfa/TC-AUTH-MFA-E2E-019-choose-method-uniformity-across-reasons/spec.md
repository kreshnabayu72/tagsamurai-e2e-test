---
id: TC-AUTH-MFA-E2E-019-choose-method-uniformity-across-reasons
title: Keseragaman tampilan layar Choose Method lintas berbagai pemicu MFA
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-MFA-32
  - TC-AUTH-MFA-33
coverage:
  web: automated
---

# Keseragaman tampilan layar Choose Method lintas berbagai pemicu MFA

## Prerequisites

- Mode: FE+BE
- User dipicu oleh variasi alasan: `first_login`, `idle_30d`, atau `unusual_login`

## Test Steps

1. Simulasikan pembukaan layar Choose Method untuk kondisi pemicu `first_login`
2. Catat opsi dan teks yang tampil
3. Ulangi untuk kondisi pemicu `idle_30d` dan `unusual_login`
4. Verifikasi tampilan antarmuka dan opsi kartu (OTP vs Authenticator) identik di ketiga kondisi
5. Verifikasi field `mfaReason` bersifat informational-only (hanya digunakan untuk template email alert, bukan untuk membatasi opsi metode)

## Notes

- TC Frontend Ref: `TC-AUTH-MFA-FE-19`
- Merepresentasikan `TC-AUTH-MFA-32` dan `TC-AUTH-MFA-33` (FE Ref: `TC-AUTH-MFA-FE-19`).
