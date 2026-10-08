---
id: TC-GS-ROLE-E2E-005-badge-kondisional-pending-activation-lintas-surface
title: "Tampilan Badge Kondisional Pending Activation di Sebelah Name pada Tab Total Control, Detail, dan Picker"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ROLE-12
  - TC-GS-ROLE-13
coverage:
  web: automated
---

# Tampilan Badge Kondisional Pending Activation di Sebelah Name pada Tab Total Control, Detail, dan Picker

## Prerequisites

- Login sebagai Role: Total Control (Ahmad Fauzi)
- Data Uji: Rudi Hartono (Pending Activation, Total Control & Manage TAG)
- Setup Hook: before: seedUser(Pending Activation, Total Control)
- Login sbg Role: Total Control (Ahmad Fauzi)
- User berada di Global Settings > Role & Permission > Total Control
- Rudi Hartono (Pending Activation) sudah di-assign Total Control
- Rudi Hartono (Pending Activation) punya baris role Manage TAG

## Test Steps

### Badge Pending Activation di sebelah Name pada Tab Total Control (TC-GS-ROLE-12)

1. Amati sel Name dan Status baris Rudi Hartono
2. Verifikasi Badge "Pending Activation" (warning) tampil di sebelah Name
3. Verifikasi Kolom Status menampilkan Active/Inactive sesuai status user, bukan "Pending Activation"

### Badge Pending Activation di sebelah Name pada Detail dan Table User Picker (TC-GS-ROLE-13)

4. Buka Detail "Manage TAG"
5. Amati sel Name baris Rudi Hartono
6. Verifikasi Detail "Manage TAG": badge "Pending Activation" (warning) tampil di sebelah Name Rudi Hartono
7. Verifikasi Popup Assign Role pada Detail role yang belum dipegang Rudi Hartono: badge "Pending Activation" tampil di sebelah Name

## Notes

- Memvalidasi alur skenario "Tampilan Badge Kondisional Pending Activation di Sebelah Name pada Tab Total Control, Detail, dan Picker".
- Aturan PRD terkait: global-settings/role/PRD/role.md §4.1.1 Status; global-settings/role/PRD/role.md §4.1.4; global-settings/role/PRD/role.md §4.1.5.
- Sumber pemetaan test case granular: TC-GS-ROLE-12, TC-GS-ROLE-13.
