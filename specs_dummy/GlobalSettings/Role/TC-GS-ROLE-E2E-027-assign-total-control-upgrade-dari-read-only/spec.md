---
id: TC-GS-ROLE-E2E-027-assign-total-control-upgrade-dari-read-only
title: "Peningkatan Hak Akses User dari Read Only Menjadi Total Control: Pemindahan Tab dan Tanpa Duplikasi Log"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ROLE-60
coverage:
  web: automated
---

# Peningkatan Hak Akses User dari Read Only Menjadi Total Control: Pemindahan Tab dan Tanpa Duplikasi Log

## Prerequisites

- Login sebagai Total Control; Siti Nurhaliza berstatus Read Only
- Data Uji: Siti Nurhaliza (Pre-setup #4 / Dinamis #3)
- Setup Hook: before: seedUserRO(Siti Nurhaliza)
- Login sbg Role: Total Control (Ahmad Fauzi)
- User berada di Global Settings > Role & Permission > Total Control
- Siti Nurhaliza Read Only

## Test Steps

### Assign Total Control langsung ke user Read Only (upgrade) (TC-GS-ROLE-60)

1. Klik [+ Assign]
2. Centang Siti Nurhaliza
3. Klik [Assign]
4. Buka Tab Read Only
5. Buka Detail "Manage user and role"
6. Login sebagai Siti Nurhaliza, buka notifikasi
7. Verifikasi Toast sukses: "Success, Total Control has been assigned."
8. Verifikasi Siti Nurhaliza tampil di Tab Total Control dan tidak lagi di Tab Read Only
9. Verifikasi Detail "Manage user and role": Siti Nurhaliza Create, Read, Update, Delete checked
10. Verifikasi Siti Nurhaliza tidak menerima notifikasi "Your Read Only access was removed"

## Notes

- Memvalidasi alur skenario "Peningkatan Hak Akses User dari Read Only Menjadi Total Control: Pemindahan Tab dan Tanpa Duplikasi Log".
- Aturan PRD terkait: global-settings/role/PRD/role.md §4.2 [+ Assign] (Total Control); global-settings/role/PRD/role.md §9.2 [F-ROLE-04] Upsert; global-settings/role/PRD/role.md §8.8.
- Sumber pemetaan test case granular: TC-GS-ROLE-60.
