---
id: TC-AUTH-MFA-E2E-014-country-trust-independence-from-device
title: Status trust negara tidak otomatis meloloskan anomali device baru atau jarak jauh
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AUTH-MFA-25
coverage:
  web: automated
---

# Status trust negara tidak otomatis meloloskan anomali device baru atau jarak jauh

## Prerequisites

- Mode: FE+BE
- Pasangan negara A↔B sudah berstatus `is_trusted = true` untuk pengguna ini
- Login kali ini dilakukan dari perangkat baru (`device_id` baru)

## Test Steps

1. Buka halaman Login dari perangkat baru di negara yang sudah berstatus trusted
2. Masukkan email dan password valid, lalu klik `[Login]`
3. Verifikasi dimensi negara tidak memicu anomali
4. Verifikasi sistem tetap mewajibkan MFA karena terpicu oleh dimensi DEVICE BARU yang independen
5. Verifikasi pengguna dialihkan ke alur MFA

## Notes

- TC Frontend Ref: `TC-AUTH-MFA-FE-14`
- Merepresentasikan `TC-AUTH-MFA-25` (FE Ref: `TC-AUTH-MFA-FE-14`).
