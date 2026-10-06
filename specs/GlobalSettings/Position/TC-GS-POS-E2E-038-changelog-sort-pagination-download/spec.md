---
id: TC-GS-POS-E2E-038-changelog-sort-pagination-download
title: Popup Changelog — Sort, Pagination Page Size 25/50/100, Download
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-POS-178
  - TC-GS-POS-179
  - TC-GS-POS-180
  - TC-GS-POS-181
  - TC-GS-POS-182
  - TC-GS-POS-183
  - TC-GS-POS-184
  - TC-GS-POS-213
  - TC-GS-POS-214
  - TC-GS-POS-246
coverage:
  web: automated
---

# Popup Changelog — Sort, Pagination Page Size 25/50/100, Download

## Prerequisites

- Aktor `Fixture.globalSettingsPosition.actors.totalControl`.
- Popup Changelog berisi ≥100 entri log mutasi agar page size 100 teruji.
- Semua kolom data sortable (Date/Action/Name/Field/Old/New Value/Modified By), kolom Actions unsortable (header = Setup Column).

## Test Steps

### A. Sort pada kolom Changelog

1. Buka Popup Changelog, default sort Date descending (Newest First).
2. Uji sort siklus/arah pada kolom Action → urutan sesuai alfabetis case-insensitive.
3. Uji sort pada kolom Name → A–Z/Z–A case-insensitive.
4. Uji sort pada kolom Field → A–Z/Z–A.
5. Uji sort pada kolom Old Value, New Value, Modified By → sesuai konvensi (case-insensitive, null-last jika ada).
6. Uji transisi antar kolom sort (kolom sebelumnya kembali Netral saat berpindah kolom).

### B. Pagination page size 25/50/100

7. Popup Changelog terbuka (default 10/page).
8. Ubah page size ke 25 → tepat 25 baris tampil.
9. Ubah page size ke 50 → tepat 50 baris tampil.
10. Ubah page size ke 100 → tepat 100 baris tampil, 100 maksimum tanpa opsi "All".
11. Verifikasi tidak ada duplikasi/menghilang baris, total & info pagination konsisten.
12. Kembalikan ke 10.

### C. Kombinasi Search + Multi-Filter + Sort + Pagination

13. Terapkan Search + Multi-Filter + ubah sort + ubah page size → seluruh state berlaku bersamaan, tidak saling menimpa.
14. Navigasi halaman → state konsisten.

### D. Download Popup Changelog

15. Klik icon Download di toolbar Popup Changelog (tanpa filter) → file terunduh sesuai nama file Changelog-Position (sesuai konvensi §9.9), tidak ada toast sukses.
16. Terapkan filter aktif → download → isi sesuai kondisi ter-filter.
17. Simulasikan backend down saat download → tampil toast error `"Error, failed to download Changelog-Position."`.

## Notes

- Sort berlaku pada seluruh dataset yang sedang tersaring (client/server pagination konsisten).
- Download popup Changelog menggunakan nama file khusus (beda dari tabel utama `"Position"`).
