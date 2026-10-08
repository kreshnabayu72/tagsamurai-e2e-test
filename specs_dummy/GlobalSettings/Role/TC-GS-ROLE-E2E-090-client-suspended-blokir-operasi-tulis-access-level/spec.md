---
id: TC-GS-ROLE-E2E-090-client-suspended-blokir-operasi-tulis-access-level
title: "Client Suspended: Pemblokiran Operasi Tulis Assign dan Remove Total Control Serta Read Only"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-GS-ROLE-263
  - TC-GS-ROLE-264
  - TC-GS-ROLE-265
  - TC-GS-ROLE-266
coverage:
  web: automated
---

# Client Suspended: Pemblokiran Operasi Tulis Assign dan Remove Total Control Serta Read Only

## Prerequisites

- Login sebagai Total Control pada tenant Client C berstatus Suspended (Pre-setup #16)
- Data Uji: Pre-setup #16 (Client C suspended)
- Setup Hook: before: setTenantSuspended()
- Login sbg Role: Total Control pada client suspended (Pre-setup #16)

## Test Steps

### Assign Total Control saat client suspended ditolak (TC-GS-ROLE-263)

1. Tab Total Control > [+ Assign] > centang Wawan Setiawan > [Assign]
2. Verifikasi Muncul toast error: "Changes can't be saved while this workspace is suspended or expired."
3. Verifikasi Data tidak berubah
4. Verifikasi Tidak ada tampilan khusus suspend di halaman ini

### Assign Read Only saat client suspended ditolak (TC-GS-ROLE-264)

5. Tab Read Only > [+ Assign] > centang Wawan Setiawan > [Assign]
6. Verifikasi Muncul toast error: "Changes can't be saved while this workspace is suspended or expired."
7. Verifikasi Data tidak berubah
8. Verifikasi Tidak ada tampilan khusus suspend di halaman ini

### Remove Total Control saat client suspended ditolak (TC-GS-ROLE-265)

9. Tab Total Control > Remove baris Maya Anggraini > [Remove]
10. Verifikasi Muncul toast error: "Changes can't be saved while this workspace is suspended or expired."
11. Verifikasi Data tidak berubah
12. Verifikasi Tidak ada tampilan khusus suspend di halaman ini

### Remove Read Only saat client suspended ditolak (TC-GS-ROLE-266)

13. Tab Read Only > Remove baris Rina Putri > [Remove]
14. Verifikasi Muncul toast error: "Changes can't be saved while this workspace is suspended or expired."
15. Verifikasi Data tidak berubah
16. Verifikasi Tidak ada tampilan khusus suspend di halaman ini

## Notes

- Memvalidasi alur skenario "Client Suspended: Pemblokiran Operasi Tulis Assign dan Remove Total Control Serta Read Only".
- Aturan PRD terkait: global-settings/role/PRD/role.md §9.4.2 Semua aksi tulis D1; foundation/functions/entity-isolation.md §18.8.
- Sumber pemetaan test case granular: TC-GS-ROLE-263, TC-GS-ROLE-264, TC-GS-ROLE-265, TC-GS-ROLE-266.
