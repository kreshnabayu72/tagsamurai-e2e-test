---
id: TC-AUTH-MFA-E2E-060-mobile-responsive-layout-and-numeric-keyboard
title: Tampilan mobile responsive halaman MFA layout vertikal dan keyboard angka
priority: Medium
caseType: Edge
status: draft
sourceTc:
  - TC-AUTH-MFA-114
  - TC-AUTH-MFA-115
coverage:
  web: automated
---

# Tampilan mobile responsive halaman MFA layout vertikal dan keyboard angka

## Prerequisites

- Mode: mock
- Mode: mock (viewport browser disesuaikan ke resolusi mobile 375x667)

## Test Steps

1. Atur viewport browser ke ukuran mobile (375x667)
2. Buka halaman Choose Method, OTP Verification, dan Authenticator Verification
3. Verifikasi layout tersaji secara full-screen vertikal dengan tap target minimal 44px
4. Verifikasi field input kode 6 digit memiliki atribut `inputmode="numeric"` untuk memunculkan keyboard angka secara otomatis di perangkat mobile

## Notes

- TC Frontend Ref: `— (Manual di FE doc)`
- Merepresentasikan `TC-AUTH-MFA-114` dan `TC-AUTH-MFA-115`.
