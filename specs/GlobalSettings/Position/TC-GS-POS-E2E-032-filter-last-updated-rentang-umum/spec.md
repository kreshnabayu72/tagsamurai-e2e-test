---
id: TC-GS-POS-E2E-032-filter-last-updated-rentang-umum
title: Filter Last Updated — Rentang Umum & Interaksi dengan Search/Sort/Paginasi
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-POS-73
coverage:
  web: automated
---

# Filter Last Updated — Rentang Umum & Interaksi dengan Search/Sort/Paginasi

## Prerequisites

- Aktor `Fixture.globalSettingsPosition.actors.totalControl`.
- ≥2 Position dengan tanggal update berbeda.
- Search partial match tersedia.
- Data cukup untuk paginasi (>1 halaman saat ter-filter atau saat tidak).

## Test Steps

### A. Filter by Last Updated (date)

1. Buka halaman tanpa filter.
2. Buka Filter Panel, pilih rentang `Fixture.globalSettingsPosition.data.filterRange.recency`, klik `Apply`.
3. Verifikasi hanya baris dengan Last Updated dalam rentang `recency` yang tampil.
4. Kosongkan filter (Clear Field + Apply) dan kembali ke kondisi semula.

### B. Interaksi filter + search + sort + paginasi

5. Terapkan filter `recency` (Apply).
6. Ketik `Fixture.globalSettingsPosition.data.searchPartialMatch` lalu Enter (irisan filter∩search).
7. Klik header kolom Name untuk mengaktifkan sort Ascending (atau Descending).
8. Pindah ke halaman 2 via Next.
9. Verifikasi hasil tetap ter-filter dan terurut sesuai sort aktif, keyword search tetap terisi.
10. Kembali ke halaman 1.
11. Verifikasi state konsisten.

### C. Clear Field tidak mereset search & sort

12. Dengan filter+search+sort aktif, buka Filter Panel → `Clear Field` → `Apply`.
13. Verifikasi filter dilepas, keyword search tetap terisi, sort tetap aktif.
14. Verifikasi tabel menampilkan hasil keyword saja.

### D. Refresh mempertahankan state filter+sort+paginasi (konsistensi)

15. Kembalikan kombinasi state (mis. filter aktif + sort aktif + halaman >1) lalu refresh F5.
16. Verifikasi filter masih aktif (indikator toolbar), sort masih aktif, halaman tetap >1 sesuai state terakhir.

## Notes

- B–C menguatkan aturan: filter ∩ search; menghapus filter tidak mereset search/sort.
- D konsisten dengan preservasi state lintas kontrol tabel.
