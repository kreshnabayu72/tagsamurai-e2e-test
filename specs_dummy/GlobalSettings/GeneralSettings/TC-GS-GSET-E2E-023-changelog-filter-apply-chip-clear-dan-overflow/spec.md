---
id: TC-GS-GSET-E2E-023-changelog-filter-apply-chip-clear-dan-overflow
title: "Filter Changelog: Apply per field, kombinasi AND/OR, chip (X)/(uncheck), Clear Field, panel discard, +N more, dan independensi kolom"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-GS-GSET-73
  - TC-GS-GSET-74
  - TC-GS-GSET-76
  - TC-GS-GSET-77
  - TC-GS-GSET-78
  - TC-GS-GSET-79
  - TC-GS-GSET-81
  - TC-GS-GSET-158
  - TC-GS-GSET-175
  - TC-GS-GSET-176
  - TC-GS-GSET-179
coverage:
  web: automated
---

# Filter Changelog: Apply per field, kombinasi AND/OR, chip (X)/(uncheck), Clear Field, panel discard, +N more, dan independensi kolom

## Prerequisites

- Login sebagai Role: Total Control
- Changelog General Settings berisi baris riwayat (dinamis) dengan Field `Session Idle Timeout`, `Time Zone`, dan Modified By `Budi S` dan `Andi W`
- Changelog memuat baris untuk kelima Field (Currency Code, Time Zone, Date Format, Time Format, Session Idle Timeout)
- Viewport desktop lebar 1280 px untuk blok overflow chip

## Test Steps

### Filter Field Tunggal dan OR dalam Satu Field

1. Buka Modal Changelog, klik Filter, pilih Field `Session Idle Timeout`, lalu klik `[Apply]`
2. Verifikasi tabel hanya menampilkan baris Field `Session Idle Timeout`
3. Buka Filter, pilih Field `Session Idle Timeout` dan `Time Zone`, lalu klik `[Apply]`
4. Verifikasi tabel menampilkan baris Field `Session Idle Timeout` ATAU `Time Zone`; kedua chip tampil di dalam field filter

### Filter Modified By dan Date Range

5. Buka Filter, pilih Modified By `Budi S`, lalu klik `[Apply]`
6. Verifikasi tabel hanya menampilkan baris Modified By `Budi S`
7. Buka Filter, pilih rentang tanggal hari ini pada field Date, lalu klik `[Apply]`
8. Verifikasi tabel menampilkan baris yang dibuat hari ini dan teks tanggal input mengikuti Date Format General Settings tersimpan
9. Pilih rentang tanggal kemarin saja lalu klik `[Apply]`
10. Verifikasi empty state "No results found" + "Try adjusting your search or filter."

### Kombinasi Field dan Modified By (AND antar field)

11. Buka Filter, pilih Field `Session Idle Timeout` dan Modified By `Budi S`, lalu klik `[Apply]`
12. Verifikasi tabel menampilkan irisan: hanya baris Field `Session Idle Timeout` dengan Modified By `Budi S`

### Hapus Chip via (X) dan via Uncheck

13. Buka Filter, pilih Field `Session Idle Timeout` dan `Time Zone`, lalu klik `(X)` pada chip `Time Zone`
14. Verifikasi chip `Time Zone` hilang, checkbox `Time Zone` ter-uncheck, dan chip `Session Idle Timeout` tetap
15. Buka Filter, pilih Field `Session Idle Timeout` dan `Time Zone`; buka dropdown Field dan uncheck `Session Idle Timeout`; klik `[Apply]`
16. Verifikasi chip `Session Idle Timeout` hilang, chip `Time Zone` tetap, dan tabel hanya memuat baris Field `Time Zone`
17. Buka Filter, pilih Modified By `Budi S` dan `Andi W`; buka dropdown Modified By dan uncheck `Andi W`; klik `[Apply]`
18. Verifikasi chip `Andi W` hilang, chip `Budi S` tetap, dan tabel hanya memuat baris Field `Time Zone` dengan Modified By `Budi S`

### Clear Field Tanpa Melepas Search

19. Search "Edit" lalu `Enter`
20. Buka Filter, pilih Field `Session Idle Timeout`, klik `[Apply]`
21. Buka Filter, klik `[Clear Field]`, lalu klik `[Apply]`
22. Verifikasi kriteria Field dilepas dan keyword Search "Edit" tetap aktif menyaring tabel

### Menutup Panel Tanpa Apply

23. Buka Filter, pilih Field `Time Zone`, lalu klik area di luar Filter Panel
24. Verifikasi Filter Panel menutup dan tabel tidak berubah
25. Buka Filter lagi dan verifikasi field Field kosong (placeholder "All fields") karena belum ada nilai ter-Apply

### Overflow Chip +N More

26. Buka Filter, pilih kelima opsi Field: `Currency Code`, `Time Zone`, `Date Format`, `Time Format`, `Session Idle Timeout`
27. Verifikasi chip ditampilkan sebanyak yang muat pada lebar field, sisanya diringkas dalam satu chip `+N more` (jumlah chip tampil + N = 5), field tidak melebar keluar panel dan tidak digulir horizontal

### Filter Independen dari Visibilitas Kolom

28. Buka Filter, pilih Field `Session Idle Timeout`, klik `[Apply]`
29. Buka Setup Column via header Actions (⋯) > `Setup Column...`, uncheck kolom Field, klik `[Save]`
30. Verifikasi tabel tetap hanya memuat baris Field `Session Idle Timeout` (filter ter-Apply tetap berlaku)
31. Buka Filter dan verifikasi field Field tetap memuat chip `Session Idle Timeout`
32. Buka Setup Column lagi, check kolom Field, klik `[Save]`
33. Verifikasi kolom Field tampil kembali dan filter tetap aktif

## Notes

- Menggabungkan TC-GS-GSET-73, 74, 76, 77, 78, 79, 81, 158, 175, 176, dan 179 (Filter Changelog). Ini salah satu spec terbesar; bila step > 35, pecah blok Overflow Chip ke spec terpisah.
