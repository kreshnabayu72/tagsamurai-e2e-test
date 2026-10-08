---
id: TC-GS-USER-E2E-169-pool-assign-prasyarat-global-settings
title: User baru muncul di pool Assign Role & Permission setelah akses Global Settings dicentang
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-629
coverage:
  web: automated
---

# User baru muncul di pool Assign Role & Permission setelah akses Global Settings dicentang

## Prerequisites

- Login sebagai Role: Total Control biasa (`totalControl2_automated_qaTeam1`), entity Client
- User "Sinta Produk" punya Access `[Fixed Asset]` saja
- User "Tegar Settings" punya Access `[Global Settings]`
- Spec ini mengubah Access "Sinta Produk", jadi data di-seed ulang setelah run

## Test Steps

1. Buka Role & Permission lalu klik `[+ Assign]`
2. Cari "Tegar Settings" dan "Sinta Produk"
3. Verifikasi "Tegar Settings" muncul sebagai kandidat dan "Sinta Produk" tidak
4. Buka Modal Edit "Sinta Produk", centang `Global Settings`, klik `[Save]`
5. Ulangi pencarian "Sinta Produk" di `[+ Assign]` dan verifikasi kini muncul sebagai kandidat
6. Buka Tab Role "Sinta Produk" dan verifikasi masih User Basic (tidak ada banner Total Control atau Read Only dan tidak ada role aktif)

## Notes

- Sumber `user.md` §9.2 [F-USER-02] (catatan Global Settings). Arah Affected dari modul User ke Role & Permission.
