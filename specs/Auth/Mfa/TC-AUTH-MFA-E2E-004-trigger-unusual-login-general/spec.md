---
id: TC-AUTH-MFA-E2E-004-trigger-unusual-login-general
title: Deteksi anomali login memicu MFA dan pengiriman email alert
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-MFA-5
coverage:
  web: automated
---

# Deteksi anomali login memicu MFA dan pengiriman email alert

## Prerequisites

- Mode: FE+BE
- Akun aktif yang login dari salah satu kondisi anomali §5 (device baru, lokasi baru >100km, atau negara baru)

## Test Steps

1. Buka halaman Login dari environment anomali (misalnya browser dengan user agent / device id baru)
2. Masukkan email dan password valid, lalu klik `[Login]`
3. Verifikasi sistem mendeteksi anomali login dan mewajibkan verifikasi faktor kedua (MFA)
4. Verifikasi pengguna dialihkan ke alur verifikasi MFA
5. Verifikasi sistem memicu pengiriman email alert Unusual Login ke alamat email akun secara asinkron
6. Verifikasi `mfa_session` terbentuk dengan konteks `mfaReason = 'unusual_login'`

## Notes

- TC Frontend Ref: `TC-AUTH-MFA-FE-04`
- Merepresentasikan `TC-AUTH-MFA-5` (FE Ref: `TC-AUTH-MFA-FE-04`).
