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
coverage:
  web: automated
---

# Export CSV dan XLSX User List, format WYSIWYG kolom terfilter, transformasi representasi teks, dan penanganan error

## Prerequisites

- Login sebagai Role: Total Control
- Tabel User List memiliki data pengguna dengan ragam status, dan filter aktif diterapkan

## Test Steps

### Buka Menu Download & Pilih Format
1. Buka halaman `Settings > User`
2. Terapkan filter divisi `"Finance"` sehingga hanya menampilkan sebagian data
3. Klik tombol `[Download]` pada toolbar
4. Verifikasi muncul popover pilihan format: `"Download as CSV"` dan `"Download as XLSX"`

### Validasi Ekspor CSV (WYSIWYG & Transformasi Teks)
5. Klik opsi `"Download as CSV"`
6. Verifikasi file terunduh dengan nama default `"Users.csv"`
7. Periksa header dan isi file CSV
8. Verifikasi kolom yang diekspor identik dengan kolom yang sedang visible di tabel (prinsip WYSIWYG)
9. Verifikasi baris yang diekspor hanya data yang memenuhi saringan divisi Finance
10. Verifikasi transformasi representasi teks: switch Active diekspor sebagai `"Active"` atau `"Inactive"` (bukan boolean true/false); badge Role diekspor sebagai label teks (contoh: `"Total Control"` atau angka peran); placeholder kosong diekspor sebagai tanda strip `"—"`

### Validasi Ekspor XLSX
11. Klik tombol `[Download]` kembali dan pilih `"Download as XLSX"`
12. Verifikasi file terunduh dengan format spreadsheet `"Users.xlsx"`
13. Verifikasi struktur sheet dan format kolom konsisten dengan versi CSV

## Notes

- Ekspor mencerminkan tampilan tabel yang sedang aktif (kolom visible & baris terfilter).
