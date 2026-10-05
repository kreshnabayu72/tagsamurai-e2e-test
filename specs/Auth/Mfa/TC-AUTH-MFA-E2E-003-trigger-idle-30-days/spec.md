---
id: TC-AUTH-MFA-E2E-003-trigger-idle-30-days
title: Pemicu MFA karena idle 30 hari atau lebih sejak logout terakhir
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-MFA-3
coverage:
  web: automated
---

# Pemicu MFA karena idle 30 hari atau lebih sejak logout terakhir

## Prerequisites

- Mode: FE+BE
- Akun terdaftar dengan data riwayat `last_logout_at` pada platform web tercatat ≥30 hari lalu

## Test Steps

1. Buka halaman Login TAG Samurai
2. Masukkan email dan password akun yang telah idle ≥30 hari, lalu klik `[Login]`
3. Verifikasi sistem mengevaluasi dimensi inaktivitas login dan mendeteksi kondisi idle ≥30 hari
4. Verifikasi pengguna dialihkan ke alur verifikasi faktor kedua (MFA)
5. Verifikasi `mfa_session` aktif terbentuk dengan konteks `mfaReason = 'idle_30d'`

## Notes

- TC Frontend Ref: `TC-AUTH-MFA-FE-03`
- Merepresentasikan `TC-AUTH-MFA-3` (FE Ref: `TC-AUTH-MFA-FE-03`).
- Pengguna yang tidak login selama satu bulan kalender wajib membuktikan kepemilikan faktor kedua.
