---
id: TC-GS-USER-E2E-040-reset-authenticator-mfa-flow
title: "Reset Authenticator: Reset MFA dari User Detail, dialog konfirmasi, dan guard status"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-325
  - TC-GS-USER-326
  - TC-GS-USER-327
  - TC-GS-USER-328
  - TC-GS-USER-329
  - TC-GS-USER-330
  - TC-GS-USER-331
  - TC-GS-USER-332
  - TC-GS-USER-333
  - TC-GS-USER-334
coverage:
  web: automated
---

# Reset Authenticator: Reset MFA dari User Detail, dialog konfirmasi, dan guard status

## Prerequisites

- Login sebagai Role: Total Control
- User John Doe berstatus MFA Enrolled tersedia

## Test Steps

### Reset Authenticator User Enrolled

1. Buka User Detail John Doe
2. Verifikasi badge Authenticator berstatus Enrolled
3. Klik tombol '[Reset Authenticator]'
4. Verifikasi dialog konfirmasi muncul dengan peringatan pembatalan akses MFA
5. Klik tombol konfirmasi reset
6. Verifikasi toast sukses 'Authenticator reset successfully.' tampil dan status Authenticator berubah menjadi Not Enrolled

## Notes

- Menggabungkan 10 test case granular (TC-GS-USER-325 s.d. TC-GS-USER-334).
