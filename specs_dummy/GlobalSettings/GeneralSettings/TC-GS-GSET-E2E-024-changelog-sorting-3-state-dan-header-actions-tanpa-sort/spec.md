---
id: TC-GS-GSET-E2E-024-changelog-sorting-3-state-dan-header-actions-tanpa-sort
title: "Sorting Modal Changelog: 3-state kolom teks, kolom Date Oldest/Newest, dan header Actions tanpa ikon sort"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-GSET-82
  - TC-GS-GSET-83
  - TC-GS-GSET-160
coverage:
  web: automated
---

# Sorting Modal Changelog: 3-state kolom teks, kolom Date Oldest/Newest, dan header Actions tanpa ikon sort

## Prerequisites

- Login sebagai Role: Total Control
- Changelog General Settings berisi baris riwayat (dinamis)

## Test Steps

### Sorting 3-State Kolom Teks

1. Buka Modal Changelog; untuk kolom Action klik header sekali, dua kali, tiga kali berurutan dan amati indikator sort serta urutan baris tiap klik
2. Verifikasi Action: klik 1 indikator Ascending, klik 2 Descending, klik 3 netral (urutan default Date descending); karena semua baris bernilai `Edit`, yang diperiksa cukup indikator sort
3. Ulangi tiga klik berurutan untuk kolom Field
4. Verifikasi Field: klik 1 Ascending (A-Z, case-insensitive), klik 2 Descending (Z-A), klik 3 kembali ke default Date descending
5. Ulangi tiga klik berurutan untuk kolom Old Value
6. Verifikasi Old Value: Ascending, Descending, lalu kembali ke default Date descending
7. Ulangi tiga klik berurutan untuk kolom New Value
8. Verifikasi New Value: Ascending, Descending, lalu kembali ke default Date descending
9. Ulangi tiga klik berurutan untuk kolom Modified By
10. Verifikasi Modified By: Ascending, Descending, lalu kembali ke default Date descending

### Sorting Kolom Date

11. Klik header Date sekali
12. Verifikasi Oldest First
13. Klik header Date kedua kali
14. Verifikasi Newest First
15. Klik header Date ketiga kali
16. Verifikasi kembali ke default Date descending

### Header Actions Tanpa Sort

17. Amati header kolom Actions (⋯)
18. Verifikasi header Actions tidak menampilkan ikon sort
19. Klik header kolom Actions (⋯)
20. Verifikasi membuka Panel Column Visibility dan urutan baris tidak berubah

## Notes

- Menggabungkan TC-GS-GSET-82 (3-state kolom teks), 83 (kolom Date), dan 160 (header Actions tanpa sort).
