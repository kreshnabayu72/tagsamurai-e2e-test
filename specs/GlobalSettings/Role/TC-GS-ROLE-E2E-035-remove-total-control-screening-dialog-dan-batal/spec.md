---
id: TC-GS-ROLE-E2E-035-remove-total-control-screening-dialog-dan-batal
title: "Screening Dialog Konfirmasi Remove Total Control (D-01) dan Pembatalan via Tombol Cancel"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-GS-ROLE-84
  - TC-GS-ROLE-85
coverage:
  web: automated
---

# Screening Dialog Konfirmasi Remove Total Control (D-01) dan Pembatalan via Tombol Cancel

## Prerequisites

- Login sebagai Total Control
- Data Uji: Dewi Lestari (Pre-setup #3)
- Setup Hook: beforeEach: navigateTo(Tab Total Control)
- Login sbg Role: Total Control (Ahmad Fauzi)
- User berada di Global Settings > Role & Permission > Total Control
- Sari Wulandari Total Control

## Test Steps

### Screening dialog Remove Total Control (TC-GS-ROLE-84)

1. Klik (⋯) baris Sari Wulandari
2. Klik Remove
3. Screening dialog
4. Verifikasi Title "Remove Total Control"
5. Verifikasi Body "• Sari Wulandari" lalu "This will remove Total Control from this user. Their individual permissions will be reset and they will have no access assigned. Are you sure you want to remove it?"
6. Verifikasi Tombol `[Cancel]` (contrast) | `[Remove]` (danger)

### Cancel dialog Remove Total Control (TC-GS-ROLE-85)

7. Klik Remove baris Sari Wulandari
8. Klik [Cancel]
9. Verifikasi Dialog tertutup, tidak ada toast
10. Verifikasi Sari Wulandari tetap di Tab Total Control dan baris role-nya tetap

## Notes

- Memvalidasi alur skenario "Screening Dialog Konfirmasi Remove Total Control (D-01) dan Pembatalan via Tombol Cancel".
- Aturan PRD terkait: global-settings/role/PRD/role.md §4.4 D-01; global-settings/role/PRD/role.md §9.2 [F-ROLE-05].
- Sumber pemetaan test case granular: TC-GS-ROLE-84, TC-GS-ROLE-85.
