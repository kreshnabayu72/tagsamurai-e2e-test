---
id: TC-GS-GSET-E2E-024-filter-field-modified-by-multi-select
title: Filter Field & Modified By multi-select, chip, overflow
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-GSET-53
  - TC-GS-GSET-54
  - TC-GS-GSET-61
  - TC-GS-GSET-62
  - TC-GS-GSET-63
  - TC-GS-GSET-64
  - TC-GS-GSET-65
  - TC-GS-GSET-66
  - TC-GS-GSET-67
  - TC-GS-GSET-156
coverage:
  web: automated
---

# Filter Field & Modified By: multi-select, OR, chip, overflow, dropdown

## Prerequisites

- Sudah login sebagai admin Total Control (`Fixture.globalSettingsGeneralSettings.actors.totalControl`).
- Data changelog: baris Field `Currency Code` oleh `Olivia`, Field `Time Zone` oleh `Liam`,
  Field `Date Format` oleh `Olivia`.

## Test Steps

### Pilihan pertama & chip tampil

1. Buka Modal Changelog; buka Filter
2. Pada grup `Field`, pilih `Currency Code`
3. Verifikasi chip/filter pill tampil menunjukkan `Currency Code`
4. Klik `[Apply]`; verifikasi hanya baris dari `Currency Code` yang tampil

### Multi-select & OR antar pilihan

5. Buka kembali Filter; tambahkan pilihan `Time Zone` pada `Field`
6. Verifikasi chip kedua tampil (multi-select)
7. Klik `[Apply]`
8. Verifikasi baris `Currency Code` dan `Time Zone` tampil (logika OR) dan baris `Date Format` tidak
   tampil

### Hapus satu pilihan dari chip

9. Buka Filter; hapus chip `Currency` (klik ✕ pada chip) sehingga hanya `Time Zone` tersisa
10. Klik `[Apply]`
11. Verifikasi hanya baris `Time Zone` yang tampil

### Overflow label panjang pada chip

12. Pilih nilai `Modified By = Olivia` dan `Modified By = Liam` bersamaan, plus `Field`
    `Currency Code`, `Time Zone`, dan `Date Format`
13. Verifikasi deretan chip pada area filter & tombol Apply tetap terbaca: chip yang melebihi lebar
    tampil ringkas/elipsis atau masuk area "View more"
14. Verifikasi tidak ada chip yang terpotong hilang dari representasi (jumlah chip tetap tampil)

### Dropdown multi-select memiliki search-dalam-dropdown

15. Buka dropdown `Modified By`
16. Ketik teks di dalam dropdown (misal `Oli`); verifikasi daftar opsi ter-filter ke pencarian
    (nomor TC-GS-GSET-67)
17. Pilih `Olivia`; klik `[Apply]`
18. Verifikasi hanya baris `Modified By = Olivia` tampil

### Statis: dropdown Field tetap berisi kelima field walau kolom hidden

19. Pada Setup Column, sembunyikan kolom `Field` (langkah uji di spec 029)
20. Buka Filter, buka dropdown `Field`
21. Verifikasi kontrol dropdown `Field` tetap ada di Filter Panel (statis) dan opsi berfungsi valid
    meskipun kolomnya tersembunyi; pilih opsi `Session Idle Timeout`, klik `[Apply]`
22. Verifikasi tabel memfilter hanya baris `Session Idle Timeout` dengan kolom `Field` tetap hidden
23. Kembalikan kolom `Field` lewat Setup Column

## Notes

- Select filter selalu membaca daftar field independen dari visibilitas kolom Setup Column.