---
id: TC-AC-ACAL-E2E-014-tab-session-search-dropdown-or-logic-dan-chip-removal
title: "Tab Session — Search dalam dropdown filter, logika OR multi-select, penambahan dan penghapusan chip"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACAL-54
  - TC-AC-ACAL-55
  - TC-AC-ACAL-56
  - TC-AC-ACAL-57
  - TC-AC-ACAL-58
  - TC-AC-ACAL-59
  - TC-AC-ACAL-60
  - TC-AC-ACAL-61
  - TC-AC-ACAL-62
  - TC-AC-ACAL-63
  - TC-AC-ACAL-64
  - TC-AC-ACAL-65
  - TC-AC-ACAL-66
  - TC-AC-ACAL-67
  - TC-AC-ACAL-269
  - TC-AC-ACAL-270
  - TC-AC-ACAL-271
coverage:
  web: automated
---

# Tab Session — Search dalam dropdown filter, logika OR multi-select, penambahan dan penghapusan chip

## Prerequisites

- Login sebagai Role: Principal Total Control
- Tab Session terisi data beragam nama User (minimal 3 nama), Position (minimal 3), dan Division (minimal 3)

## Test Steps

### Search dalam Dropdown Multi-Select

1. Buka menu `Admin Console > Activity Log` > klik `[Filter]`
2. Buka dropdown `User` dan ketik substring nama user di kotak pencarian internal dropdown
3. Verifikasi daftar pilihan menyaring secara real-time menampilkan opsi yang cocok
4. Ulangi hal yang sama untuk dropdown `Position` dan `Division`

### Logika OR Multi-Select & Tampilan Badge Chip

5. Pada dropdown `User`, centang 2 nama user sekaligus (contoh: "John Doe" dan "Jane Smith")
6. Verifikasi dua badge chip muncul di dalam field input `User`
7. Klik tombol `[Apply]`
8. Verifikasi tabel menampilkan gabungan hasil dengan logika OR (baris milik John Doe ATAU Jane Smith tampil)

### Penghapusan Chip via Tombol (X) & Uncheck Dropdown

9. Buka kembali Filter Panel
10. Klik icon `(X)` pada salah satu chip di field User
11. Verifikasi chip tersebut hilang dan checkbox nama terkait di dalam dropdown otomatis ter-uncheck (chip lainnya tetap ada)
12. Buka dropdown `Position`, centang 2 opsi position sehingga menghasilkan 2 chip
13. Buka kembali dropdown `Position` dan uncheck salah satu checkbox
14. Verifikasi chip terkait otomatis hilang dari field input
15. Lakukan pengujian chip add/remove pada field `Division`

### Overflow Chip

16. Centang banyak opsi pada field User hingga melebihi lebar input box
17. Verifikasi penanganan overflow berjalan rapi (menampilkan ringkasan `"+N more"` atau scroll horizontal yang dapat diakses)

## Notes

- Multi-select filter menggunakan logika OR untuk opsi di dalam field yang sama.
