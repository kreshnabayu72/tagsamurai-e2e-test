---
id: TC-AUTH-MFA-E2E-034-email-alert-reset-password-navigation
title: Tombol Reset Password pada email alert mengarah ke form request reset normal
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-MFA-70
coverage:
  web: automated
---

# Tombol Reset Password pada email alert mengarah ke form request reset normal

## Prerequisites

- Mode: FE+BE
- Email alert Unusual Login diterima di mailbox pengguna

## Test Steps

1. Buka email alert Unusual Login yang diterima
2. Klik tombol aksi `[Reset Password]` di dalam body email
3. Verifikasi tautan mengarahkan browser ke halaman request Reset Password publik (`/reset-password/`)
4. Verifikasi pengguna TIDAK langsung diarahkan ke form set password baru (pengguna tetap diwajibkan memvalidasi kepemilikan email melalui alur baku)

## Notes

- TC Frontend Ref: `TC-AUTH-MFA-FE-34`
- Merepresentasikan `TC-AUTH-MFA-70` (FE Ref: `TC-AUTH-MFA-FE-34`).
