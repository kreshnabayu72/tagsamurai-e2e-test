---
id: TC-AUTH-MFA-E2E-028-enrollment-race-two-devices
title: Penanganan kondisi balapan enrollment dari dua perangkat secara simultan
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AUTH-MFA-53
coverage:
  web: automated
---

# Penanganan kondisi balapan enrollment dari dua perangkat secara simultan

## Prerequisites

- Mode: FE+BE
- User membuka halaman pendaftaran Authenticator di dua perangkat/tab browser secara bersamaan

## Test Steps

1. Buka layar setup enrollment pada Perangkat A dan Perangkat B dengan `mfa_session` yang sama
2. Lakukan submit kode verifikasi di Perangkat A dan Perangkat B dalam waktu hampir bersamaan
3. Verifikasi hanya satu transaksi setup yang berhasil disetujui (kebijakan last-write-wins pada secret)
4. Verifikasi perangkat yang kalah menerima notifikasi penolakan (caption error)
5. Verifikasi hanya tepat satu entri pendaftaran aktif di database (`is_active = true`)

## Notes

- TC Frontend Ref: `TC-AUTH-MFA-FE-28`
- Merepresentasikan `TC-AUTH-MFA-53` (FE Ref: `TC-AUTH-MFA-FE-28`).
