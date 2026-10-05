---
id: TC-AUTH-MFA-E2E-056-cross-module-reset-password-independence
title: Reset Password modul lain tidak mereset trusted device enrollment maupun first login
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-MFA-117
  - TC-AUTH-MFA-118
coverage:
  web: automated
---

# Reset Password modul lain tidak mereset trusted device enrollment maupun first login

## Prerequisites

- Mode: FE+BE
- User telah memiliki riwayat login sukses (`first_login_at` terisi), trusted device, dan enrollment Authenticator

## Test Steps

1. Lakukan alur Reset Password lengkap hingga berhasil memperbarui password baru
2. Buka halaman Login dan masukkan password baru
3. Periksa status data `trusted_device` dan `authenticator_enrollment` user
4. Verifikasi data trusted device dan status enrollment Authenticator TETAP utuh (tidak ter-reset)
5. Verifikasi user tidak dianggap sebagai "first login" lagi (`first_login_at` tidak dikosongkan)

## Notes

- TC Frontend Ref: `TC-AUTH-MFA-FE-56`
- Merepresentasikan `TC-AUTH-MFA-117` dan `TC-AUTH-MFA-118` (FE Ref: `TC-AUTH-MFA-FE-56`).
