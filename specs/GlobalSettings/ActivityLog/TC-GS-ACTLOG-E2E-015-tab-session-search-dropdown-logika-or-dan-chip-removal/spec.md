---
id: TC-GS-ACTLOG-E2E-015-tab-session-search-dropdown-logika-or-dan-chip-removal
title: "Tab Session: Search internal dropdown, logika OR dalam satu field, dan siklus chip seleksi 2-arah"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ACTLOG-59
  - TC-GS-ACTLOG-60
  - TC-GS-ACTLOG-61
  - TC-GS-ACTLOG-62
  - TC-GS-ACTLOG-63
  - TC-GS-ACTLOG-64
  - TC-GS-ACTLOG-65
  - TC-GS-ACTLOG-222
coverage:
  web: automated
---

# Tab Session: Search internal dropdown, logika OR dalam satu field, dan siklus chip seleksi 2-arah

## Prerequisites

- Login sebagai Role: Total Control pada Tab Session dengan Filter Panel terbuka

## Test Steps

1. Buka dropdown User di Filter Panel dan ketik sebagian nama pada kotak pencarian internal dropdown
2. Verifikasi daftar opsi menyempit sesuai substring pencarian
3. Centang opsi "Login" dan "Logout" dalam field Activity yang sama lalu klik `[Apply]`
4. Verifikasi hasil filter menggabungkan data secara OR (entri Login ATAU Logout tampil)
5. Buka kembali Filter, centang opsi pertama pada field User dan verifikasi chip muncul di dalam kotak field
6. Centang opsi kedua dan verifikasi chip kedua muncul berdampingan
7. Klik icon `(X)` pada salah satu chip dan verifikasi chip terhapus serta checkbox terkait di dropdown otomatis ter-uncheck
8. Buka dropdown User, uncheck checkbox yang sudah tercentang, dan verifikasi chip terkait langsung terhapus dari field
9. Pilih ≥6 user sekaligus dan verifikasi tampilan overflow `+N more` tampil rapi tanpa memotong field
10. Pilih tanggal pada date picker dan verifikasi format tanggal di dalam kotak input terformat presisi sesuai Date Format
11. Verifikasi perilaku chip 2-arah dan overflow berlaku simetris pada field Position, Division, dan Status

## Notes

- Siklus chip dua arah menjamin sinkronisasi instan antara elemen chip di luar dengan daftar checkbox di dalam dropdown.
