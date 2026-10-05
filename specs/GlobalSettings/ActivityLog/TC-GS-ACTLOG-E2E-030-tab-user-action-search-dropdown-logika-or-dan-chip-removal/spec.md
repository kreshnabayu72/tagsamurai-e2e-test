---
id: TC-GS-ACTLOG-E2E-030-tab-user-action-search-dropdown-logika-or-dan-chip-removal
title: "Tab User Action: Search internal dropdown, logika OR dalam satu field, dan siklus chip seleksi 2-arah"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ACTLOG-145
  - TC-GS-ACTLOG-146
  - TC-GS-ACTLOG-147
  - TC-GS-ACTLOG-148
  - TC-GS-ACTLOG-149
  - TC-GS-ACTLOG-150
  - TC-GS-ACTLOG-151
  - TC-GS-ACTLOG-223
coverage:
  web: automated
---

# Tab User Action: Search internal dropdown, logika OR dalam satu field, dan siklus chip seleksi 2-arah

## Prerequisites

- Login sebagai Role: Total Control pada Tab User Action dengan Filter Panel terbuka

## Test Steps

1. Buka dropdown Modified By di Filter Panel dan ketik sebagian nama pada pencarian internal dropdown
2. Verifikasi daftar opsi menyempit sesuai keyword pencarian
3. Centang opsi "Create" dan "Delete" dalam field Action yang sama lalu klik `[Apply]`
4. Verifikasi hasil filter menggabungkan data secara OR (entri Create ATAU Delete tampil)
5. Buka kembali Filter, centang opsi pertama pada field Action dan verifikasi chip muncul di field
6. Centang opsi kedua dan verifikasi chip kedua muncul berdampingan
7. Klik icon `(X)` pada salah satu chip dan verifikasi chip hilang serta checkbox terkait otomatis ter-uncheck
8. Buka dropdown Action, uncheck salah satu checkbox, dan verifikasi chip terkait langsung terhapus dari field
9. Pilih ≥6 Action sekaligus dan verifikasi tampilan overflow `+N more` tampil rapi
10. Pilih tanggal pada date picker dan verifikasi format tanggal di input terformat presisi sesuai Date Format
11. Verifikasi perilaku chip 2-arah dan overflow berlaku simetris pada field Object dan Modified By

## Notes

- Multiselect dropdown chip berlaku seragam di seluruh form filter platform.
