---
id: TC-GS-ROLE-E2E-050-remove-role-assignment-single-resilience-server-500
title: "Ketahanan Pencabutan Baris Role Single: Penanganan Kegagalan Server 500 pada Target Biasa dan TC/RO"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-GS-ROLE-117
  - TC-GS-ROLE-118
coverage:
  web: automated
---

# Ketahanan Pencabutan Baris Role Single: Penanganan Kegagalan Server 500 pada Target Biasa dan TC/RO

## Prerequisites

- Login sebagai Total Control; mock intercept HTTP 500
- Data Uji: Doni Pratama, Rudi Hartono
- Spectra.intercept aktif untuk penanganan simulasi network/mock response
- Setup Hook: beforeEach: setupMock500()
- Login sbg Role: Total Control (Ahmad Fauzi)
- User berada di Global Settings > Role & Permission > System > Detail "Manage files"
- Response Remove dibuat gagal 5xx
- Siti Nurhaliza Total Control; response Remove gagal 5xx

## Test Steps

### Remove baris role gagal 5xx (TC-GS-ROLE-117)

1. Klik Remove baris Wawan Setiawan
2. Klik [Remove]
3. Verifikasi Muncul toast error: "Error, failed to remove user."
4. Verifikasi Baris Wawan Setiawan tetap ada

### Remove baris role target Total Control gagal 5xx (TC-GS-ROLE-118)

5. Klik Remove baris Siti Nurhaliza
6. Klik [Remove]
7. Verifikasi Muncul toast error: "Error, failed to remove user."
8. Verifikasi Baris tetap ada dan Siti Nurhaliza tetap di Tab Total Control

## Notes

- Memvalidasi alur skenario "Ketahanan Pencabutan Baris Role Single: Penanganan Kegagalan Server 500 pada Target Biasa dan TC/RO".
- Aturan PRD terkait: global-settings/role/PRD/role.md §7.1 T-08; global-settings/role/PRD/role.md §9.6; global-settings/role/PRD/role.md §7.1 T-09.
- Sumber pemetaan test case granular: TC-GS-ROLE-117, TC-GS-ROLE-118.
