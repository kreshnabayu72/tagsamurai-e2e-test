---
id: TC-GS-DIV-E2E-049-tabel-utama-pagination-navigasi-dan-render-page-size
title: "Pagination Navigasi Halaman dan Render Presisi Page Size 10/25/50/100"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-DIV-84
  - TC-GS-DIV-85
  - TC-GS-DIV-274
coverage:
  web: automated
---

# Pagination Navigasi Halaman dan Render Presisi Page Size 10/25/50/100

## Prerequisites

- Login sebagai Role: Total Control
- Tersedia dataset divisi lebih dari 25 record

## Test Steps

1. Buka menu Global Settings > User > tab Division
2. Verifikasi paginasi default menampilkan 10 record per halaman
3. Klik tombol navigasi 'Next' (>) dan verifikasi halaman berpindah ke page 2
4. Klik tombol 'Previous' (<) dan verifikasi kembali ke page 1
5. Buka dropdown page size lalu pilih opsi '25'
6. Verifikasi tabel me-render tepat 25 baris data per halaman tanpa duplikasi
7. Pilih opsi '50' dan '100' lalu verifikasi jumlah baris yang dirender presisi sesuai angka opsi
8. Lakukan refresh browser (F5) dan verifikasi pilihan page size 25 tetap bertahan (persistensi state pagination)

## Notes

- Memvalidasi rendering pagination page size sesuai sitasi TC-GS-DIV-274 dan prd-conventions.md §9.11.
