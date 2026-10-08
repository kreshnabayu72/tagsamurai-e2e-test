---
id: TC-GS-POS-E2E-029-sort-siklus-3-state
title: Sort Siklus 3-State — Name & Last Updated, Null-last, Transisi Antar Kolom
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-POS-69
  - TC-GS-POS-70
coverage:
  web: automated
---

# Sort Siklus 3-State — Name & Last Updated, Null-last, Transisi Antar Kolom

## Prerequisites

- Aktor `Fixture.globalSettingsPosition.actors.totalControl`.
- Tabel berisi ≥3 Position dengan variasi nama (case-insensitive) dan ≥2 dengan tanggal berbeda.
- Konvensi platform §9.7: Siklus Klik Sort 3-Tahap (Ascending → Descending → Netral).
- Netral mengembalikan ke default sort tabel (initial default). PRD Position: default sort Last Updated Newest First (lihat 001).
- Null-last: nilai kosong selalu ditempatkan terakhir baik ascending maupun descending. Karena Position selalu punya Last Updated, aturan ini dibuktikan implisit; tetap dicatat.
- Transisi kolom: klik kolom B saat kolom A aktif → kolom A kembali Netral, kolom B mulai Klik #1 Ascending.

## Test Steps

### A. Name — Siklus 3-State

1. Pastikan tidak ada sort aktif pada kolom lain (kondisi awal netral) atau amati state.
2. Klik header kolom Name (Klik #1) → Ascending A–Z (case-insensitive).
3. Verifikasi indikator panah naik aktif pada header Name.
4. Verifikasi urutan baris A–Z (case-insensitive).
5. Klik header kolom Name (Klik #2) → Descending Z–A (case-insensitive).
6. Verifikasi indikator panah turun aktif pada header Name.
7. Verifikasi urutan baris Z–A (case-insensitive).
8. Klik header kolom Name (Klik #3) → Netral.
9. Verifikasi indikator panah pada kolom Name hilang/non-aktif.
10. Verifikasi susunan tabel kembali ke default sort tabel (sesuai 001).

### B. Last Updated — Siklus 3-State

11. Klik header kolom Last Updated (Klik #1) → Oldest First (↑).
12. Verifikasi indikator panah naik aktif pada header Last Updated.
13. Verifikasi data terurut tanggal terlama → terbaru.
14. Klik header kolom Last Updated (Klik #2) → Newest First (↓).
15. Verifikasi indikator panah turun aktif pada header Last Updated.
16. Verifikasi data terurut tanggal terbaru → terlama.
17. Klik header kolom Last Updated (Klik #3) → Netral.
18. Verifikasi indikator panah hilang dan tabel kembali ke default sort.

### C. Transisi antar kolom

19. Klik header kolom Name (Klik #1) → Ascending aktif pada Name.
20. Klik header kolom Last Updated → kolom Name kembali Netral, kolom Last Updated langsung Ascending (Klik #1).
21. Verifikasi indikator sort berpindah ke Last Updated (↑), indikator Name non-aktif.
22. Klik header kolom Name → kolom Last Updated kembali Netral, kolom Name Ascending (Klik #1).

## Notes

- Transisi kolom membuktikan sort single-column dan Netral diterapkan ke kolom sebelumnya.
- Netral kembali ke initial default sort tabel, bukan mempertahankan urutan acak.
