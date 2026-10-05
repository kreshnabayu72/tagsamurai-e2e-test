---
id: TC-AUTH-MFA-E2E-007-device-detection-exact-match
title: Pencocokan device exact match bukan similarity score
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AUTH-MFA-10
coverage:
  web: automated
---

# Pencocokan device exact match bukan similarity score

## Prerequisites

- Mode: FE+BE
- User memiliki perangkat tepercaya dengan `device_id` A
- Request login dikirimkan dengan `device_id` B yang memiliki kemiripan string tinggi (hanya beda 1 karakter)

## Test Steps

1. Konfigurasikan browser/klien dengan `device_id` B (mirip identifier A namun tidak identik)
2. Buka halaman Login dan masukkan kredensial valid akun
3. Klik tombol `[Login]`
4. Verifikasi sistem menolak kemiripan (tanpa fuzzy matching / similarity scoring) dan menganggapnya sebagai device baru
5. Verifikasi alur verifikasi faktor kedua (MFA) diwajibkan

## Notes

- TC Frontend Ref: `TC-AUTH-MFA-FE-07`
- Merepresentasikan `TC-AUTH-MFA-10` (FE Ref: `TC-AUTH-MFA-FE-07`).
- TAG Samurai menerapkan strict exact-match pada hardware/browser fingerprint.
