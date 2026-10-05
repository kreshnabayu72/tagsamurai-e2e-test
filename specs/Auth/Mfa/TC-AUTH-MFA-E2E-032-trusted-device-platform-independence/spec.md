---
id: TC-AUTH-MFA-E2E-032-trusted-device-platform-independence
title: Status trusted device dievaluasi secara independen per platform web dan mobile
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-MFA-61
coverage:
  web: automated
---

# Status trusted device dievaluasi secara independen per platform web dan mobile

## Prerequisites

- Mode: FE+BE
- Perangkat fisik yang sama telah terdaftar sebagai trusted device pada platform web

## Test Steps

1. Simulasikan login dari aplikasi mobile pada perangkat fisik tersebut
2. Verifikasi aplikasi mobile mengirimkan `device_id` khusus platform mobile yang berbeda dari web
3. Verifikasi status trust pada web TIDAK otomatis meloloskan platform mobile
4. Verifikasi verifikasi MFA tetap diwajibkan untuk sesi mobile pertama tersebut

## Notes

- TC Frontend Ref: `TC-AUTH-MFA-FE-32`
- Merepresentasikan `TC-AUTH-MFA-61` (FE Ref: `TC-AUTH-MFA-FE-32`).
