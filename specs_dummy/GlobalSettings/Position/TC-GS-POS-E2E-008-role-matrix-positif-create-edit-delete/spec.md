---
id: TC-GS-POS-E2E-008-role-matrix-positif-create-edit-delete
title: "Role Matrix Positif: Eksekusi Create, Edit, Delete, dan Bulk Delete oleh aktor capability spesifik"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-POS-32
  - TC-GS-POS-33
  - TC-GS-POS-34
  - TC-GS-POS-35
coverage:
  web: automated
---

# Role Matrix Positif: Eksekusi Create, Edit, Delete, dan Bulk Delete oleh aktor capability spesifik

## Prerequisites

- Akun Aktor C-Only (Sari Dewi), U-Only, dan D-Only tersedia
- Master data Position untuk uji coba tersedia

## Test Steps

### Create oleh Aktor C-Only

1. Login sebagai Aktor C-Only
2. Buka Global Settings > User > Position
3. Klik "[+ Position]", isi Position Name "Junior Tester", lalu klik "[Submit]"
4. Verifikasi toast sukses muncul dan "Junior Tester" terdaftar di tabel

### Edit oleh Aktor U-Only

5. Login sebagai Aktor U-Only
6. Buka menu ⋯ pada baris "Junior Tester", klik "Edit"
7. Ubah nama menjadi "Middle Tester", lalu klik "[Save]"
8. Verifikasi toast sukses muncul dan nama di tabel terbarukan

### Delete Single & Bulk Delete oleh Aktor D-Only

9. Login sebagai Aktor D-Only
10. Buka menu ⋯ pada baris "Middle Tester", klik "Delete"
11. Pada dialog konfirmasi Delete Position, klik "[Delete]"
12. Verifikasi toast sukses muncul dan record terhapus dari tabel
13. Centang 2 record bebas relasi lainnya pada tabel
14. Klik tombol "[Delete]" pada Bulk Action Bar, lalu konfirmasi Delete
15. Verifikasi kedua record terhapus dan toast sukses Bulk Delete muncul

## Notes

- Menggabungkan TC-GS-POS-32, 33, 34, dan 35.
