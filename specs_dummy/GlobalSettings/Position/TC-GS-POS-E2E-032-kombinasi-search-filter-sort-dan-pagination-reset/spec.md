---
id: TC-GS-POS-E2E-032-kombinasi-search-filter-sort-dan-pagination-reset
title: "Sort 3-klik Name & Last Updated, kombinasi Search + Filter + Sort, dan reset pagination"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-POS-165
  - TC-GS-POS-166
  - TC-GS-POS-167
  - TC-GS-POS-168
  - TC-GS-POS-169
  - TC-GS-POS-170
  - TC-GS-POS-171
  - TC-GS-POS-172
  - TC-GS-POS-173
  - TC-GS-POS-174
coverage:
  web: automated
---

# Sort 3-klik Name & Last Updated, kombinasi Search + Filter + Sort, dan reset pagination

## Prerequisites

- Login sebagai Total Control
- Tabel Position berisi ≥15 record

## Test Steps

### Siklus Sort 3-Klik Kolom Name & Last Updated

1. Klik header kolom Name ke-1x, verifikasi terurut Ascending (A-Z) dengan ikon panah ke atas
2. Klik header kolom Name ke-2x, verifikasi terurut Descending (Z-A) dengan ikon panah ke bawah
3. Klik header kolom Name ke-3x, verifikasi kembali ke urutan default tanpa panah sort
4. Klik header Last Updated ke-1x, verifikasi terurut Oldest First
5. Klik header Last Updated ke-2x, verifikasi terurut Newest First
6. Klik header Name 1x, verifikasi sort berpindah ke Name dan sort Last Updated dinonaktifkan

### Kombinasi Search, Filter, dan Sort

7. Masukkan keyword Search "o"
8. Buka Filter Panel, pilih rentang tanggal, klik "[Apply]"
9. Klik sort Name Z-A
10. Verifikasi tabel menampilkan irisan data yang cocok dengan ketiga kriteria tersebut
11. Bersihkan filter via Filter Panel, verifikasi search dan sort tetap aktif
12. Bersihkan search, verifikasi sort tetap aktif

### Reset Pagination ke Halaman 1

13. Pindah ke halaman 2 via kontrol pagination
14. Ketik keyword baru pada Search lalu tekan Enter
15. Verifikasi pagination otomatis di-reset kembali ke halaman 1

## Notes

- Menggabungkan interaksi gabungan query dan sort tabel dari TC-GS-POS-165 s.d. 174.
