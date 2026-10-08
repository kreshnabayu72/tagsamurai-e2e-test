---
id: TC-GS-ROLE-E2E-042-assign-role-detail-resilience-server-500-dan-double-submit
title: "Ketahanan Form Assign Role Detail: Penanganan Error Server 500 dan Guard Klik Ganda Cepat"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-GS-ROLE-97
  - TC-GS-ROLE-98
coverage:
  web: automated
---

# Ketahanan Form Assign Role Detail: Penanganan Error Server 500 dan Guard Klik Ganda Cepat

## Prerequisites

- Login sebagai Total Control; intercept respons 500
- Data Uji: Wawan Setiawan (Pre-setup #18)
- Spectra.intercept aktif untuk penanganan simulasi network/mock response
- Setup Hook: beforeEach: openModalAssignRole()
- Login sbg Role: Total Control (Ahmad Fauzi)
- User berada di Global Settings > Role & Permission > System > Detail "Manage hardware"
- Response Assign Role dibuat gagal 5xx

## Test Steps

### Assign Role gagal 5xx (TC-GS-ROLE-97)

1. Klik [+ Assign]
2. Centang Wawan Setiawan
3. Klik [Assign]
4. Verifikasi Muncul toast error: "Error, failed to assign role."
5. Verifikasi Popup tetap terbuka dengan seleksi dipertahankan
6. Verifikasi Tidak ada baris baru

### Klik ganda [Assign] Popup Assign Role (TC-GS-ROLE-98)

7. Klik [+ Assign]
8. Centang Wawan Setiawan
9. Klik [Assign] dua kali cepat
10. Verifikasi Satu toast sukses: "Success, role has been assigned."
11. Verifikasi Detail memuat tepat 1 baris Wawan Setiawan

## Notes

- Memvalidasi alur skenario "Ketahanan Form Assign Role Detail: Penanganan Error Server 500 dan Guard Klik Ganda Cepat".
- Aturan PRD terkait: global-settings/role/PRD/role.md §7.1 T-06; global-settings/role/PRD/role.md §9.6 Assign Role; global-settings/role/PRD/role.md §9.6 Delta modul ini; global-settings/role/PRD/role.md §9.6; global-settings/role/PRD/role.md §9.4.3 Must NOT.
- Sumber pemetaan test case granular: TC-GS-ROLE-97, TC-GS-ROLE-98.
