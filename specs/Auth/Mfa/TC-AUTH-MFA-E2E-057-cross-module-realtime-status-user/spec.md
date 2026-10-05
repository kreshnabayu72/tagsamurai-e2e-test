---
id: TC-AUTH-MFA-E2E-057-cross-module-realtime-status-user
title: Status keaktifan user dibaca secara real time saat verifikasi faktor kedua
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AUTH-MFA-119
coverage:
  web: automated
---

# Status keaktifan user dibaca secara real time saat verifikasi faktor kedua

## Prerequisites

- Mode: FE+BE
- `mfa_session` user sedang aktif
- Akun user di-deactivate tepat sebelum faktor kedua disubmit

## Test Steps

1. Buka layar verifikasi faktor kedua
2. Nonaktifkan user pada modul Global Settings > User
3. Lakukan submit kode verifikasi faktor kedua
4. Verifikasi status user dibaca ulang secara real-time dari database (bukan mengandalkan cache saat sesi pre-auth dibuat)
5. Verifikasi transaksi verifikasi ditolak dan pengguna dialihkan keluar

## Notes

- TC Frontend Ref: `TC-AUTH-MFA-FE-57`
- Merepresentasikan `TC-AUTH-MFA-119` (FE Ref: `TC-AUTH-MFA-FE-57`).
