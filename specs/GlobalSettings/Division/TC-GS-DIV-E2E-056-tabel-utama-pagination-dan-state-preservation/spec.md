---
id: TC-GS-DIV-E2E-056-tabel-utama-pagination-dan-state-preservation
title: "Pagination Tabel Utama: Default 10 Data, Pilihan Page Size 10/25/50/100, Kontrol Navigasi Halaman, dan Retensi State Saat Navigasi/Refresh"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-DIV-163
  - TC-GS-DIV-164
  - TC-GS-DIV-165
  - TC-GS-DIV-166
coverage:
  web: automated
---

# Pagination Tabel Utama: Default 10 Data, Pilihan Page Size 10/25/50/100, Kontrol Navigasi Halaman, dan Retensi State Saat Navigasi/Refresh

## Prerequisites

- Login sebagai Role: Total Control
- Tabel terisi >=32 divisi (populasi D-02)
- User berada di Global Settings > User > Division
- Tabel Division terisi 32 baris (TC-GS-DIV-30)
- Last Updated Division Pre-setup lebih lama dari Division Data Uji Dinamis

## Test Steps

### Sort 3-state kolom teks Name dan Code (TC-GS-DIV-163)

1. Klik header Name tiga kali
2. Klik header Code tiga kali
3. Verifikasi Name: klik 1 ascending A-Z tanpa membedakan huruf besar kecil, klik 2 descending Z-A, klik 3 kembali ke default Name A-Z
4. Verifikasi Code: klik 1 ascending A-Z, klik 2 descending Z-A, klik 3 kembali ke default sort tabel (Name A-Z)

### Sort 3-state kolom Last Updated (TC-GS-DIV-164)

5. Klik header Last Updated tiga kali
6. Verifikasi Klik 1: Oldest First (Division Pre-setup di atas)
7. Verifikasi Klik 2: Newest First (Division Data Uji Dinamis di atas)
8. Verifikasi Klik 3: kembali ke default sort Name A-Z

### Kolom checkbox dan Column Visibility tidak memiliki ikon sort (TC-GS-DIV-165)

9. Perhatikan header kolom Checkbox dan kolom Column Visibility (⋯)
10. Verifikasi Header kolom Checkbox tidak memiliki ikon sort
11. Verifikasi Header kolom Column Visibility (⋯) tidak memiliki ikon sort

### Pagination default 10 data per halaman dengan 4 halaman untuk 32 baris (TC-GS-DIV-166)

12. Buka Tab Division
13. Perhatikan footer pagination
14. Verifikasi Halaman 1 menampilkan 10 baris
15. Verifikasi Footer menampilkan 4 halaman dan page size terpilih 10
16. Verifikasi Pilihan page size: 10, 25, 50, 100 (tanpa opsi All)

## Notes

- Memvalidasi kontrol pagination footer, render akurat page size 10/25/50/100, tombol navigasi First/Prev/Next/Last, serta persistensi state saat refresh F5 atau kembali dari menu lain (PRD §5, prd-conventions.md §9.11, §27.1c).
- Sumber pemetaan test case granular: TC-GS-DIV-163, TC-GS-DIV-164, TC-GS-DIV-165, TC-GS-DIV-166.
