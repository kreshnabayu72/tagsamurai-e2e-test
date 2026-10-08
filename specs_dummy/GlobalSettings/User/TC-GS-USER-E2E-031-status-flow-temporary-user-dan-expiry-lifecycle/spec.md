---
id: TC-GS-USER-E2E-031-status-flow-temporary-user-dan-expiry-lifecycle
title: "Status Flow: Siklus hidup Temporary User, tanggal kedaluwarsa, dan auto-deactivate"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-251
  - TC-GS-USER-252
  - TC-GS-USER-253
  - TC-GS-USER-254
  - TC-GS-USER-255
  - TC-GS-USER-256
  - TC-GS-USER-257
  - TC-GS-USER-258
  - TC-GS-USER-259
  - TC-GS-USER-260
  - TC-GS-USER-1012
  - TC-GS-USER-1013
  - TC-GS-USER-1014
  - TC-GS-USER-1039
coverage:
  web: automated
---

# Status Flow: Siklus hidup Temporary User, tanggal kedaluwarsa, dan auto-deactivate

## Prerequisites

- Login sebagai Role: Total Control
- User Fikri Ramadhan dengan Temporary Until

## Test Steps

### Pengaturan dan Perpanjangan Masa Aktif

1. Buka modal Edit user temporary, verifikasi tanggal Temporary Until terlihat
2. Perpanjang tanggal Temporary Until ke tanggal di masa depan, klik '[Save]'
3. Verifikasi pembaruan tanggal berhasil
4. Simulasikan kedaluwarsa waktu (melewati Temporary Until), verifikasi status user otomatis menjadi Inactive (auto-deactivate)

## Notes

- Menggabungkan 14 test case granular (TC-GS-USER-251 s.d. TC-GS-USER-1039).
