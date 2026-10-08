---
id: TC-GS-DIV-E2E-079-user-form-stale-division-deletion-auto-clear
title: "Penanganan Form User & Non-Login User pada Divisi yang Dihapus Pihak Lain: Error Field dan Auto-Clear"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-GS-DIV-254
  - TC-GS-DIV-255
coverage:
  web: automated
---

# Penanganan Form User & Non-Login User pada Divisi yang Dihapus Pihak Lain: Error Field dan Auto-Clear

## Prerequisites

- Login sebagai Role: Total Control
- Buka form Create User dan Non-Login User
- Divisi bebas relasi dipilih di form lalu dihapus oleh admin lain sebelum submit
- User berada di Global Settings > User > Division
- Division `Stale Unit A` (Code `SUA`) bebas relasi dibuat lewat `[+ Division]` (Tabel Data Uji Dinamis D-22)
- Division `Stale Unit B` (Code `SUB`) bebas relasi dibuat lewat `[+ Division]` (Tabel Data Uji Dinamis D-23)

## Test Steps

### Form User dengan Division terpilih yang dihapus pihak lain menampilkan error field dan auto-clear (TC-GS-DIV-254)

1. Admin A membuka form Create User dan memilih Division `Stale Unit A`
2. Admin B menghapus Division `Stale Unit A`
3. Admin A mengisi field wajib lain lalu klik Submit
4. Verifikasi Error level field Division: `This division no longer exists. Please select another.`
5. Verifikasi Field Division dikosongkan otomatis dan daftar opsi di-refresh tanpa mereset field lain

### Form Non-Login User dengan Division terpilih yang dihapus pihak lain menampilkan error field dan auto-clear (TC-GS-DIV-255)

6. Admin A membuka form Create Non-Login User dan memilih Division `Stale Unit B`
7. Admin B menghapus Division `Stale Unit B`
8. Admin A mengisi field wajib lain lalu klik Submit
9. Verifikasi Error level field Division: `This division no longer exists. Please select another.`
10. Verifikasi Field Division dikosongkan otomatis dan daftar opsi di-refresh tanpa mereset field lain

## Notes

- Memvalidasi penanganan breaking change §11 pada form konsumen (User dan Non-Login User): saat divisi terpilih dihapus admin lain sebelum submit, sistem menampilkan error field "This division no longer exists. Please select another.", field otomatis dikosongkan (auto-clear), dan daftar opsi di-refresh tanpa mereset input field lain (PRD §11 Breaking Changes, error-handling-convention.md §5.5).
- Sumber pemetaan test case granular: TC-GS-DIV-254, TC-GS-DIV-255.
