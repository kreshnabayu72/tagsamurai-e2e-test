---
id: TC-GS-USER-E2E-158-tab-role-toggle-active-role
title: Switch Active di Tab Role memberi dan mencabut role individual
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-617
coverage:
  web: automated
---

# Switch Active di Tab Role memberi dan mencabut role individual

## Prerequisites

- Login sebagai Role: Total Control biasa (`totalControl2_automated_qaTeam1`), entity Client
- User "Doni Pratama" adalah User Basic (bukan Total Control atau Read Only) dan role "Manage TAG" berstatus OFF
- Spec ini mengubah lalu mengembalikan role, jadi data kembali seperti semula

## Test Steps

1. Buka User Detail "Doni Pratama" > Tab Role
2. Hidupkan Switch Active pada baris "Manage TAG"
3. Verifikasi auto-save tanpa tombol Save, toast "Success, permissions have been updated.", dan kolom CRUD baris itu menjadi editable
4. Buka Role & Permission dan verifikasi "Doni Pratama" ter-assign pada "Manage TAG"
5. Kembali ke Tab Role dan matikan Switch Active baris yang sama
6. Verifikasi toast yang sama, baris kembali OFF dengan CRUD disabled dan tidak tercentang
7. Buka Modal Changelog User > Role dan verifikasi ada entri "Assign" lalu "Remove" untuk "Manage TAG" pada Field "Access"

## Notes

- Melengkapi `TC-GS-USER-E2E-054` yang hanya mengedit checkbox CRUD. Gate aksi ini belum tegas, lihat `GAP-296`.
- Spec dijalankan oleh Total Control biasa saja.
