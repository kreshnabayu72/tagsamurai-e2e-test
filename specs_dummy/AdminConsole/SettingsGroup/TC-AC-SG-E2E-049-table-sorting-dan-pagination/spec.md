---
id: TC-AC-SG-E2E-049-table-sorting-dan-pagination
title: "Default sorting Group A-Z dan kontrol paginasi tabel utama (rows per page, page jump, independensi filter)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SG-94
  - TC-AC-SG-178
coverage:
  web: automated
---

# Default sorting Group A-Z dan kontrol paginasi tabel utama (rows per page, page jump, independensi filter)

## Prerequisites

- Login sebagai Role: Total Control
- Tersedia > 25 data group dengan variasi abjad besar dan kecil

## Test Steps

### Verifikasi Default Sorting A-Z
1. Buka `Settings > Group` tanpa mengubah parameter sort
2. Amati urutan baris pada kolom Group
3. Verifikasi baris terurut secara alfabetis A-Z case-insensitive
### Kontrol Paginasi & Page Jump
4. Amati footer paginasi tabel utama, verifikasi default page size adalah 10 baris per halaman
5. Buka dropdown rows-per-page, verifikasi opsi yang tersedia adalah `10`, `25`, `50`, dan `100` (tanpa opsi "All")
6. Pilih opsi `25`, verifikasi tabel seketika merender hingga 25 baris
7. Ketik angka halaman `"2"` langsung pada kotak input nomor halaman lalu tekan Enter
8. Verifikasi tabel melompat menampilkan data halaman 2
### Independensi Paginasi dari Filter
9. Terapkan kata kunci pencarian pada toolbar Search
10. Pindah antar halaman paginasi, verifikasi kata kunci pencarian dan filter aktif tidak pernah ter-reset

## Notes

- Paginasi tidak mereset filter dan search aktif di tabel (prd-conventions.md §9.11).
