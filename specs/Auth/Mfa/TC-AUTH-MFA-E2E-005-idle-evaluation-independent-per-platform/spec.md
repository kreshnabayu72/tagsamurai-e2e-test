---
id: TC-AUTH-MFA-E2E-005-idle-evaluation-independent-per-platform
title: Evaluasi idle 30 hari dihitung secara independen per platform web dan mobile
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-MFA-6
coverage:
  web: automated
---

# Evaluasi idle 30 hari dihitung secara independen per platform web dan mobile

## Prerequisites

- Mode: FE+BE
- User memiliki riwayat `last_logout_at` pada platform web ≥30 hari yang lalu
- User aktif login dan bertransaksi di platform mobile 7 hari yang lalu

## Test Steps

1. Simulasikan request login pada platform mobile menggunakan kredensial akun tersebut
2. Verifikasi evaluasi dimensi idle pada platform mobile membaca histori platform mobile sendiri (<30 hari)
3. Verifikasi MFA TIDAK terpicu pada platform mobile oleh dimensi idle
4. Buka browser web dan lakukan login dengan akun yang sama
5. Verifikasi evaluasi dimensi idle pada platform web membaca histori web (≥30 hari) sehingga MFA terpicu di web

## Notes

- TC Frontend Ref: `TC-AUTH-MFA-FE-05`
- Merepresentasikan `TC-AUTH-MFA-6` (FE Ref: `TC-AUTH-MFA-FE-05`).
- State idle terisolasi per platform (web vs mobile) sesuai arsitektur sesi TAG Samurai.
