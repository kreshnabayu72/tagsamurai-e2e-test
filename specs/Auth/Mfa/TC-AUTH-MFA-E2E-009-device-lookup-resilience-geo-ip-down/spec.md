---
id: TC-AUTH-MFA-E2E-009-device-lookup-resilience-geo-ip-down
title: Deteksi device baru tidak fail open saat layanan Geo-IP eksternal down
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AUTH-MFA-12
coverage:
  web: automated
---

# Deteksi device baru tidak fail open saat layanan Geo-IP eksternal down

## Prerequisites

- Mode: FE+BE
- Device baru (`device_id` belum terdaftar)
- Layanan resolusi Geo-IP eksternal mengalami gangguan (down / 500 / timeout)

## Test Steps

1. Simulasikan kegagalan pada penyedia layanan Geo-IP eksternal
2. Lakukan login dari perangkat dengan `device_id` baru
3. Klik tombol `[Login]`
4. Verifikasi lookup device lokal ke tabel internal `trusted_device` tetap dieksekusi
5. Verifikasi MFA tetap wajib karena dimensi device adalah lookup database internal dan TIDAK fail-open

## Notes

- TC Frontend Ref: `TC-AUTH-MFA-FE-09`
- Merepresentasikan `TC-AUTH-MFA-12` (FE Ref: `TC-AUTH-MFA-FE-09`).
