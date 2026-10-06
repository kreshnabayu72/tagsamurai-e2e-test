---
id: TC-GS-DIV-E2E-065-entitas-suspended-expired-blokir-aksi-tulis
title: "Blokir Aksi Tulis Katalog Division Saat Status Entitas Suspended atau Expired"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-GS-DIV-185
coverage:
  web: automated
---

# Blokir Aksi Tulis Katalog Division Saat Status Entitas Suspended atau Expired

## Prerequisites

- Login sebagai pengguna pada entitas/tenant dengan status Suspended atau Expired

## Test Steps

1. Buka menu Global Settings > User > tab Division
2. Verifikasi tombol '[+ Division]' dinonaktifkan atau disembunyikan
3. Verifikasi menu row action (⋯) tidak menampilkan aksi Edit atau Delete
4. Verifikasi checkbox baris dinonaktifkan / disembunyikan sehingga Bulk Delete tidak dapat dipicu
5. Coba kirimkan request create/update/delete langsung dan verifikasi sistem menolak aksi tulis dengan status 403 Forbidden

## Notes

- Menguji dimensi edge case D1 Entity/Account state suspended/expired sesuai division.md §9.4.1.
