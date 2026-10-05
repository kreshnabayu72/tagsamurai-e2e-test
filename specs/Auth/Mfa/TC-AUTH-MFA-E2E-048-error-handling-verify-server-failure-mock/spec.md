---
id: TC-AUTH-MFA-E2E-048-error-handling-verify-server-failure-mock
title: Penanganan kegagalan server 500 saat verifikasi faktor kedua dan toast error retry
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AUTH-MFA-91
coverage:
  web: automated
---

# Penanganan kegagalan server 500 saat verifikasi faktor kedua dan toast error retry

## Prerequisites

- Mode: mock
- Mode: mock (intersep endpoint verifikasi faktor kedua mengembalikan status HTTP 500)

## Test Steps

1. Masukkan kode verifikasi valid pada form faktor kedua
2. Konfigurasikan mock agar endpoint verify mengembalikan error 500
3. Lakukan submit
4. Verifikasi muncul toast notifikasi "Error, failed to log in."
5. Verifikasi pengguna tetap berada di halaman verifikasi faktor kedua dan dapat mencoba ulang saat server pulih
6. Verifikasi kegagalan server teknis ini TIDAK dicatat di Activity Log Session

## Notes

- TC Frontend Ref: `TC-AUTH-MFA-FE-48`
- Merepresentasikan `TC-AUTH-MFA-91` (FE Ref: `TC-AUTH-MFA-FE-48`).
