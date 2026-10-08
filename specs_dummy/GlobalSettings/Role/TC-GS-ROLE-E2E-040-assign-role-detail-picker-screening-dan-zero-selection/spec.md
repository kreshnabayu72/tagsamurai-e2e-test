---
id: TC-GS-ROLE-E2E-040-assign-role-detail-picker-screening-dan-zero-selection
title: "Screening Modal Table User Picker Assign Role pada Halaman Detail dan Validasi Seleksi Kosong"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-GS-ROLE-92
  - TC-GS-ROLE-93
coverage:
  web: automated
---

# Screening Modal Table User Picker Assign Role pada Halaman Detail dan Validasi Seleksi Kosong

## Prerequisites

- Login sebagai Total Control
- Data Uji: Detail Manage hardware, Tari Anjani (Pre-setup #18)
- Setup Hook: beforeEach: openModalAssignRole()
- Login sbg Role: Total Control (Ahmad Fauzi)
- User berada di Global Settings > Role & Permission > System > Detail "Manage TAG"
- Doni Pratama punya baris Manage TAG; Wawan Setiawan dan Agus Salim tidak

## Test Steps

### Screening Popup Assign Role dan pool-nya (TC-GS-ROLE-92)

1. Klik [+ Assign]
2. Screening popup dan daftar user
3. Verifikasi Title "Assign Role"; toolbar `Search | Filter`; kolom `Checkbox | Name | Email | Position | Division | Status`; footer `[Cancel] | [Assign]`
4. Verifikasi Tidak tampil: user yang sudah punya baris Manage TAG (Doni Pratama, Budi Santoso, Siti Nurhaliza) dan Ahmad Fauzi (aktor)
5. Verifikasi Tampil: Wawan Setiawan, Tari Anjani (Inactive), Yoga Pratama (Pending Activation) (Pre-setup #18)

### Submit Assign Role tanpa memilih user (TC-GS-ROLE-93)

6. Klik [+ Assign]
7. Klik [Assign]
8. Verifikasi Teks error inline "You must pick a user" (danger) di atas tombol footer
9. Verifikasi Popup tetap terbuka

## Notes

- Memvalidasi alur skenario "Screening Modal Table User Picker Assign Role pada Halaman Detail dan Validasi Seleksi Kosong".
- Aturan PRD terkait: global-settings/role/PRD/role.md §4.2 Page: Detail; global-settings/role/PRD/role.md ROLE-LOGIC-06b; global-settings/role/PRD/role.md ROLE-LOGIC-01c; global-settings/role/PRD/role.md §6 V-09.
- Sumber pemetaan test case granular: TC-GS-ROLE-92, TC-GS-ROLE-93.
