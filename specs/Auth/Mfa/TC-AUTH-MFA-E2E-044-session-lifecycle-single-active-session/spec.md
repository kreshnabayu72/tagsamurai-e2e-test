---
id: TC-AUTH-MFA-E2E-044-session-lifecycle-single-active-session
title: Batasan satu sesi pre auth aktif per user dan platform membatalkan sesi lama
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-MFA-86
coverage:
  web: automated
---

# Batasan satu sesi pre auth aktif per user dan platform membatalkan sesi lama

## Prerequisites

- Mode: FE+BE
- User memiliki sesi `mfa_session` aktif di Tab 1

## Test Steps

1. Buka Tab 2 dan lakukan login ulang dari Faktor-1 menggunakan kredensial akun yang sama
2. Verifikasi sistem menerbitkan `mfa_session` baru untuk Tab 2
3. Kembali ke Tab 1 dan coba selesaikan faktor kedua menggunakan sesi lama
4. Verifikasi sesi Tab 1 telah otomatis di-invalidate dan ditolak server
5. Verifikasi hanya ada tepat satu `mfa_session` aktif per kombinasi `(user_id, platform)`

## Notes

- TC Frontend Ref: `TC-AUTH-MFA-FE-44`
- Merepresentasikan `TC-AUTH-MFA-86` (FE Ref: `TC-AUTH-MFA-FE-44`).
