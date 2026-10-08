---
id: TC-GS-ROLE-E2E-048-remove-role-assignment-single-happy-path-dan-dialog
title: "Pencabutan Baris Role Assignment Single: Dialog D-03, Pembatalan Cancel, Eksekusi MUR, dan Double-Click Debounce"
priority: Critical
caseType: Edge
status: draft
sourceTc:
  - TC-GS-ROLE-112
  - TC-GS-ROLE-113
  - TC-GS-ROLE-119
coverage:
  web: automated
---

# Pencabutan Baris Role Assignment Single: Dialog D-03, Pembatalan Cancel, Eksekusi MUR, dan Double-Click Debounce

## Prerequisites

- Login sebagai Total Control lalu Hendra Wijaya
- Data Uji: Doni Pratama, Wawan Setiawan
- Setup Hook: beforeEach: navigateTo(Detail)
- Login sbg Role: Total Control (Ahmad Fauzi)
- User berada di Global Settings > Role & Permission > System > Detail "Manage TAG"
- Login sbg Role: Manage user and role C/R/U/D (Hendra Wijaya)
- User berada di Global Settings > Role & Permission > System > Detail "Manage files"
- User berada di Global Settings > Role & Permission > System > Detail "Manage hardware"

## Test Steps

### Remove baris role target biasa oleh Total Control (TC-GS-ROLE-112)

1. Klik Remove baris Doni Pratama
2. Klik [Remove]
3. Buka Tab System
4. Buka Detail "Manage files"
5. Verifikasi Muncul toast sukses: "Success, user has been removed."
6. Verifikasi Baris Doni Pratama hilang dari Detail "Manage TAG"
7. Verifikasi Users "Manage TAG" berkurang 1
8. Verifikasi Baris Doni Pratama di Detail "Manage files" tetap ada

### Remove baris role oleh aktor Manage user and role dengan Update (TC-GS-ROLE-113)

9. Klik Remove baris Nina Kartika
10. Klik [Remove]
11. Verifikasi Toast sukses: "Success, user has been removed."
12. Verifikasi Baris Nina Kartika hilang

### Klik ganda [Remove] dialog Remove baris role (TC-GS-ROLE-119)

13. Klik Remove baris Wawan Setiawan
14. Klik [Remove] dua kali cepat
15. Verifikasi Satu toast sukses: "Success, user has been removed."
16. Verifikasi Changelog "Manage hardware" memuat tepat 1 entry Remove untuk Wawan Setiawan

## Notes

- Memvalidasi alur skenario "Pencabutan Baris Role Assignment Single: Dialog D-03, Pembatalan Cancel, Eksekusi MUR, dan Double-Click Debounce".
- Aturan PRD terkait: global-settings/role/PRD/role.md §9.2 [F-ROLE-07]; global-settings/role/PRD/role.md §7.1 T-08; global-settings/role/PRD/role.md §9.2 [F-ROLE-07] Idempotent.
- Sumber pemetaan test case granular: TC-GS-ROLE-112, TC-GS-ROLE-113, TC-GS-ROLE-119.
