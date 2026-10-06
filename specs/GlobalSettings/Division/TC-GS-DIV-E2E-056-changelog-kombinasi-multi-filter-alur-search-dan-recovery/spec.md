---
id: TC-GS-DIV-E2E-056-changelog-kombinasi-multi-filter-alur-search-dan-recovery
title: "Kombinasi Multi-Filter Changelog, Alur Search dan Filter, Serta Pemulihan Empty State"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-DIV-102
  - TC-GS-DIV-103
  - TC-GS-DIV-104
  - TC-GS-DIV-105
  - TC-GS-DIV-106
  - TC-GS-DIV-107
  - TC-GS-DIV-108
  - TC-GS-DIV-109
  - TC-GS-DIV-110
  - TC-GS-DIV-275
coverage:
  web: automated
---

# Kombinasi Multi-Filter Changelog, Alur Search dan Filter, Serta Pemulihan Empty State

## Prerequisites

- Login sebagai Role: Total Control
- Terdapat dataset riwayat mutasi yang kaya

## Test Steps

1. Buka Modal Changelog Division
2. Terapkan filter Action = 'Edit' DAN Modified By = user tertentu (logika AND antar-field)
3. Verifikasi tabel menampilkan irisan log yang cocok dengan kedua filter
4. Masukkan keyword pencarian pada search box Changelog di atas hasil filter
5. Verifikasi data terfilter lebih lanjut secara presisi
6. Ubah page size Changelog menjadi 25/50/100 dan verifikasi pagination menampilkan jumlah baris yang presisi
7. Klik '[Clear Field]' pada Filter Panel dan verifikasi kriteria filter terlepas tanpa mereset search
8. Hapus teks search box dan verifikasi search terlepas tanpa mereset status sort
9. Terapkan filter hingga menghasilkan 0 data, lalu ubah kriteria filter
10. Verifikasi tabel Changelog pulih menampilkan data riwayat yang cocok

## Notes

- Menguji kombinasi penuh kontrol tabel sekunder pada modal changelog (division.md §4.2b).
