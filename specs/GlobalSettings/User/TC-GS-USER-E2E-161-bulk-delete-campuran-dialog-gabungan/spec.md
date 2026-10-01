---
id: TC-GS-USER-E2E-161-bulk-delete-campuran-dialog-gabungan
title: Bulk Delete campuran aset dan approval memakai satu dialog warn gabungan
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-621
coverage:
  web: automated
---

# Bulk Delete campuran aset dan approval memakai satu dialog warn gabungan

## Prerequisites

- Login sebagai Role: Total Control biasa (`totalControl2_automated_qaTeam1`), entity Client
- User "Lukman Aset" punya Borrowed Asset aktif
- User "Mira Approver" punya Pending Approval
- User "Nanda Bersih" tanpa keterikatan data
- Spec ini menghapus ketiga user, jadi data dibuat ulang oleh seeding

## Test Steps

1. Centang baris "Lukman Aset", "Mira Approver", dan "Nanda Bersih" di User List
2. Klik bulk action `Delete`
3. Verifikasi satu dialog warn gabungan yang menyebut dampak aset dan approval
4. Klik `[Delete]`
5. Verifikasi toast "Success, user has been deleted." dan ketiga user hilang dari List
6. Verifikasi snapshot transaksi "Lukman Aset" dan "Mira Approver" di Fixed Asset tetap tersimpan

## Notes

- Sumber `user.md` §4.1 dan §9.2 [F-USER-06]. Melengkapi `TC-GS-USER-E2E-005` (Delete) dan spec Bulk Delete.
