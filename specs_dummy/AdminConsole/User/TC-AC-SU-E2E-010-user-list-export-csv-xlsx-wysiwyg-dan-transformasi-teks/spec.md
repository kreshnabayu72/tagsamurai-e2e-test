---
id: TC-AC-SU-E2E-010-user-list-export-csv-xlsx-wysiwyg-dan-transformasi-teks
title: "Export CSV dan XLSX User List, format WYSIWYG kolom terfilter, transformasi representasi teks, dan penanganan error"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SU-22
  - TC-AC-SU-277
  - TC-AC-SU-278
  - TC-AC-SU-279
  - TC-AC-SU-280
coverage:
  web: automated
---

# Export CSV dan XLSX User List, format WYSIWYG kolom terfilter, transformasi representasi teks, dan penanganan error

## Prerequisites

- Login sebagai Role: Principal Total Control
- Terdapat data pengguna terfilter dan setidaknya 1 kolom di-hide via Setup Column

## Test Steps

### Export CSV & XLSX dengan Scope Saringan Aktif

1. Buka halaman User List, terapkan kata kunci pencarian dan filter tertentu
2. Sembunyikan 1 kolom (contoh: Employee ID) via Setup Column
3. Klik tombol `[Download]` di toolbar lalu pilih opsi `CSV`
4. Verifikasi file terunduh dengan nama `Users.csv`
5. Buka file `Users.csv`, verifikasi isi file hanya memuat baris data yang cocok dengan kriteria filter aktif (bukan seluruh database)
6. Verifikasi file export mengikuti prinsip WYSIWYG (kolom yang disembunyikan tidak ikut diekspor)
7. Klik tombol `[Download]` lalu pilih opsi `XLSX`
8. Verifikasi file terunduh dengan nama `Users.xlsx`

### Transformasi Representasi Teks dan Error Handling

1. Periksa isi file export: verifikasi nilai switch Active tertransformasi menjadi teks `"Active"` / `"Inactive"`, badge status menjadi teks polos, boolean Temporary User menjadi `"Yes"` / `"No"`, dan sel kosong menjadi placeholder eksplisit `"—"`
2. Konfigurasikan mock error pada endpoint download backend
3. Klik tombol `[Download]`
4. Verifikasi toast error muncul: `"Error, failed to download User."`

## Notes

- Fitur download mengekspor representasi data yang tampak di layar.
