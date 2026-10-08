---
id: TC-GS-ROLE-E2E-091-client-suspended-blokir-operasi-tulis-detail-dan-bulk-remove
title: "Client Suspended: Pemblokiran Operasi Tulis Assign Role, Edit CRUD, Remove Single, dan Bulk Remove pada Detail"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-GS-ROLE-267
  - TC-GS-ROLE-268
  - TC-GS-ROLE-269
  - TC-GS-ROLE-270
coverage:
  web: automated
---

# Client Suspended: Pemblokiran Operasi Tulis Assign Role, Edit CRUD, Remove Single, dan Bulk Remove pada Detail

## Prerequisites

- Login sebagai Total Control pada tenant Client C berstatus Suspended (Pre-setup #16)
- Data Uji: Pre-setup #16 (Client C suspended)
- Setup Hook: before: setTenantSuspended()
- Login sbg Role: Total Control pada client suspended (Pre-setup #16)

## Test Steps

### Assign Role saat client suspended ditolak (TC-GS-ROLE-267)

1. Detail "Manage TAG" > [+ Assign] > centang Wawan Setiawan > [Assign]
2. Verifikasi Muncul toast error: "Changes can't be saved while this workspace is suspended or expired."
3. Verifikasi Data tidak berubah
4. Verifikasi Tidak ada tampilan khusus suspend di halaman ini

### Edit CRUD saat client suspended ditolak (TC-GS-ROLE-268)

5. Detail "Manage TAG" > centang Update baris Doni Pratama
6. Verifikasi Muncul toast error: "Changes can't be saved while this workspace is suspended or expired."
7. Verifikasi Data tidak berubah
8. Verifikasi Tidak ada tampilan khusus suspend di halaman ini

### Remove baris role saat client suspended ditolak (TC-GS-ROLE-269)

9. Detail "Manage TAG" > Remove baris Doni Pratama > [Remove]
10. Verifikasi Muncul toast error: "Changes can't be saved while this workspace is suspended or expired."
11. Verifikasi Data tidak berubah
12. Verifikasi Tidak ada tampilan khusus suspend di halaman ini

### Bulk Remove saat client suspended ditolak (TC-GS-ROLE-270)

13. Detail "Manage TAG" > centang 2 baris > Bulk Action > Remove > [Remove]
14. Verifikasi Muncul toast error: "Changes can't be saved while this workspace is suspended or expired."
15. Verifikasi Data tidak berubah
16. Verifikasi Tidak ada tampilan khusus suspend di halaman ini

## Notes

- Memvalidasi alur skenario "Client Suspended: Pemblokiran Operasi Tulis Assign Role, Edit CRUD, Remove Single, dan Bulk Remove pada Detail".
- Aturan PRD terkait: global-settings/role/PRD/role.md §9.4.2 Semua aksi tulis D1; foundation/functions/entity-isolation.md §18.8.
- Sumber pemetaan test case granular: TC-GS-ROLE-267, TC-GS-ROLE-268, TC-GS-ROLE-269, TC-GS-ROLE-270.
