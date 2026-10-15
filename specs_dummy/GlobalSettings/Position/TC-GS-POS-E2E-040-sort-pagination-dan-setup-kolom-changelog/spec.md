---
id: TC-GS-POS-E2E-040-sort-pagination-dan-setup-kolom-changelog
title: "Sort 3-klik Date/teks/Modified By, pagination, Overlay Visibility, dan Setup Column Changelog (7 kolom)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-POS-221
  - TC-GS-POS-222
  - TC-GS-POS-223
  - TC-GS-POS-224
  - TC-GS-POS-225
  - TC-GS-POS-226
  - TC-GS-POS-227
  - TC-GS-POS-228
  - TC-GS-POS-229
  - TC-GS-POS-230
  - TC-GS-POS-231
  - TC-GS-POS-232
  - TC-GS-POS-233
  - TC-GS-POS-234
  - TC-GS-POS-235
  - TC-GS-POS-236
coverage:
  web: automated
---

# Sort 3-klik Date/teks/Modified By, pagination, Overlay Visibility, dan Setup Column Changelog (7 kolom)

## Prerequisites

- Login sebagai Total Control
- Popup Changelog terbuka dengan riwayat >10 baris

## Test Steps

### Sort Kolom Changelog

1. Klik header kolom Date 1x, verifikasi terurut Oldest First; klik 2x, verifikasi Newest First
2. Klik header kolom Action, Position Name, dan Modified By, verifikasi pengurutan alfabetis
3. Uji sort kolom Old Value dan New Value, verifikasi penanganan baris dengan nilai kosong ("—")

### Pagination Changelog

4. Verifikasi pagination di footer Popup Changelog menampilkan 10 baris per halaman
5. Pindah ke halaman 2 via navigasi pagination, verifikasi baris terusan tampil

### Overlay Visibility & Setup Column Changelog

6. Klik ikon ⋯ pada header kolom tabel Changelog
7. Verifikasi Overlay Column Visibility menampilkan ke-7 kolom kelas Hideable: Date, Action, Position Name, Field, Old Value, New Value, Modified By
8. Klik "Setup Column..." pada overlay
9. Verifikasi modal Setup Column Changelog terbuka tanpa tombol Cancel di footer
10. Sembunyikan kolom "Old Value" dan lakukan pin pada kolom "Date" (maksimal 3 pin)
11. Klik "[Save]", verifikasi perubahan diterapkan di tabel Changelog
12. Buka kembali Setup Column, klik "[Reset to Default]", lalu klik "[Save]"
13. Verifikasi seluruh 7 kolom kembali tampil ke posisi awal

## Notes

- Menggabungkan sort, pagination, dan pengelolaan kolom pada Popup Changelog (TC-GS-POS-221 s.d. 236).
