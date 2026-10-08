---
id: TC-GS-ROLE-E2E-081-sync-dua-arah-dengan-modul-user-detail-tab-role
title: "Sinkronisasi Dua Arah Antara Menu Role & Permission dengan Halaman User Detail Tab Role"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ROLE-231
  - TC-GS-ROLE-232
coverage:
  web: automated
---

# Sinkronisasi Dua Arah Antara Menu Role & Permission dengan Halaman User Detail Tab Role

## Prerequisites

- Login sebagai Total Control
- Data Uji: Pre-setup #10 (Doni Pratama)
- Setup Hook: beforeEach: navigateTo(User Detail / Role Detail)
- Login sbg Role: Total Control (Ahmad Fauzi)

## Test Steps

### Edit CRUD dari Detail tercermin di User Detail Tab Role (TC-GS-ROLE-231)

1. Detail "Manage TAG": centang Update baris Wawan Setiawan
2. Buka Global Settings > User > Wawan Setiawan > Tab Role
3. Verifikasi Baris Manage TAG di Tab Role: Update checked

### Edit dari User Detail Tab Role tercermin di Detail role (TC-GS-ROLE-232)

4. User > Wawan Setiawan > Tab Role: uncheck Update Manage TAG
5. Buka Role & Permission > System > Detail "Manage TAG"
6. Verifikasi Baris Wawan Setiawan: Update unchecked

## Notes

- Memvalidasi alur skenario "Sinkronisasi Dua Arah Antara Menu Role & Permission dengan Halaman User Detail Tab Role".
- Aturan PRD terkait: global-settings/role/PRD/role.md §4.2 Sinkron dengan User Detail; global-settings/user/PRD/user.md §4.1.
- Sumber pemetaan test case granular: TC-GS-ROLE-231, TC-GS-ROLE-232.
