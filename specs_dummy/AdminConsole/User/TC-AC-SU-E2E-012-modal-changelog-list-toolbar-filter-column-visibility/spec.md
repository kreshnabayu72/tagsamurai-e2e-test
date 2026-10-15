---
id: TC-AC-SU-E2E-012-modal-changelog-list-toolbar-filter-column-visibility
title: "Modal Changelog User List, Search, Filter Panel, Column Visibility terpisah, dan export CSV"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SU-23
  - TC-AC-SU-24
  - TC-AC-SU-25
  - TC-AC-SU-227
coverage:
  web: automated
---

# Modal Changelog User List, Search, Filter Panel, Column Visibility terpisah, dan export CSV

## Prerequisites

- Login sebagai Role: Total Control
- Terdapat riwayat audit perubahan pengguna di tingkat entitas (aggregate across users)

## Test Steps

### Buka Modal Changelog List-Level & Struktur Kolom
1. Buka halaman `Settings > User`
2. Klik icon `[Changelog]` pada toolbar User List
3. Verifikasi modal terbuka dengan judul `"Changelog: User"`
4. Verifikasi tabel memuat 7 kolom baku: `Date`, `Action`, `User Name`, `Field`, `Old Value`, `New Value`, dan `Modified By`

### Pencarian & Filter Panel Modal Changelog
5. Ketik nama pengguna pada kotak Search di dalam modal
6. Verifikasi baris changelog tersaring hanya untuk pengguna tersebut
7. Klik tombol `[Filter]` di dalam modal changelog
8. Verifikasi opsi dropdown `Action` memuat enum hardcoded (contoh: `Activate`, `Deactivate`, `Assign Global Role`, dll.)
9. Verifikasi opsi dropdown `User Name` dan `Modified By` diisi secara dinamis (*populate DISTINCT*)
10. Terapkan filter Action = `"Activate"` dan verifikasi hanya log aktivasi yang tampil

### Setup Column & Export Modal Changelog
11. Buka `Column Visibility (⋯)` di dalam modal changelog
12. Sembunyikan kolom `Field`
13. Verifikasi kolom Field tersembunyi di modal changelog, dan verifikasi cache preferensi ini terpisah serta tidak mempengaruhi tabel User List utama
14. Klik tombol `[Download]` di dalam modal
15. Verifikasi file terunduh dengan nama default `"Changelog-User.csv"`
16. Tutup modal via icon `[×]` dan verifikasi kembali ke layar User List

## Notes

- Modal Changelog di toolbar User List bersifat aggregate lintas seluruh pengguna entitas.
