---
id: TC-GS-ROLE-E2E-047-edit-crud-detail-resilience-server-500
title: "Ketahanan Edit CRUD Inline Detail: Pemulihan State Checkbox dan Tombol Retry Pasca-Error Jaringan 500"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-GS-ROLE-109
  - TC-GS-ROLE-110
  - TC-GS-ROLE-111
coverage:
  web: automated
---

# Ketahanan Edit CRUD Inline Detail: Pemulihan State Checkbox dan Tombol Retry Pasca-Error Jaringan 500

## Prerequisites

- Login sebagai Total Control; mock intercept HTTP 500
- Data Uji: Doni Pratama, Maya Anggraini, Wawan Setiawan
- Spectra.intercept aktif untuk penanganan simulasi network/mock response
- Setup Hook: beforeEach: setupMock500()
- Login sbg Role: Total Control (Ahmad Fauzi)
- User berada di Global Settings > Role & Permission > System > Detail "Manage TAG"
- Rudi Hartono Total Control; response Edit CRUD dibuat gagal 5xx
- Doni Pratama punya baris Manage TAG

## Test Steps

### Auto-revert gagal 5xx memakai pesan gagal Edit CRUD (TC-GS-ROLE-109)

1. Uncheck Update baris Rudi Hartono
2. Klik [Remove]
3. Buka Tab Total Control
4. Verifikasi Muncul toast error: "Error, failed to update permissions."
5. Verifikasi Rudi Hartono tetap di Tab Total Control

### Screening overlay row action dan dialog Remove baris target biasa (TC-GS-ROLE-110)

6. Klik (⋯) baris Doni Pratama
7. Klik Remove
8. Screening dialog
9. Verifikasi Overlay hanya berisi `Remove` dengan icon DeleteBin6Line severity danger
10. Verifikasi Title "Remove Access"
11. Verifikasi Body mengikuti template "• [User Name]
12. Verifikasi This will remove [Role Name] access from this user. Are you sure you want to remove it?": "• Doni Pratama" + "This will remove Manage TAG access from this user. Are you sure you want to remove it?"
13. Verifikasi Tombol `[Cancel]` (contrast) | `[Remove]` (danger)

### Cancel dialog Remove baris target biasa (TC-GS-ROLE-111)

14. Klik Remove baris Doni Pratama
15. Klik [Cancel]
16. Verifikasi Dialog tertutup tanpa toast
17. Verifikasi Baris Doni Pratama tetap ada

## Notes

- Memvalidasi alur skenario "Ketahanan Edit CRUD Inline Detail: Pemulihan State Checkbox dan Tombol Retry Pasca-Error Jaringan 500".
- Aturan PRD terkait: global-settings/role/PRD/role.md §7.1 T-07; global-settings/role/PRD/role.md §4.4 D-03; global-settings/role/PRD/role.md §4.1 Row Actions; global-settings/role/PRD/role.md §4.4.
- Sumber pemetaan test case granular: TC-GS-ROLE-109, TC-GS-ROLE-110, TC-GS-ROLE-111.
