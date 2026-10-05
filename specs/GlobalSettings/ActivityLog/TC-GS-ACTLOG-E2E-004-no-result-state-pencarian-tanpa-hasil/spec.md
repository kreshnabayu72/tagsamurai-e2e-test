---
id: TC-GS-ACTLOG-E2E-004-no-result-state-pencarian-tanpa-hasil
title: "Tampilan no-result state saat pencarian atau penyaringan tidak menghasilkan data"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ACTLOG-08
  - TC-GS-ACTLOG-09
coverage:
  web: automated
---

# Tampilan no-result state saat pencarian atau penyaringan tidak menghasilkan data

## Prerequisites

- Login sebagai Role: Total Control
- Terdapat data riwayat aktivitas pada Tab Session dan Tab User Action

## Test Steps

1. Buka Tab Session
2. Masukkan keyword "zzznotfound" pada kotak Search Toolbar lalu tekan Enter
3. Verifikasi tabel menampilkan judul "No results found" dan subtitle "Try adjusting your search or filter."
4. Kosongkan kotak Search lalu tekan Enter untuk memulihkan tampilan data
5. Klik tab "User Action"
6. Masukkan keyword "zzznotfound" pada kotak Search Toolbar lalu tekan Enter
7. Verifikasi tabel menampilkan judul "No results found" dan subtitle "Try adjusting your search or filter."

## Notes

- Tampilan no-result state memuat subtitle pemulihan untuk memandu user menghapus kriteria pencarian.
