---
id: TC-GS-DIV-E2E-003-no-result-state-pencarian-tanpa-hasil
title: "Tampilan No-Result State Saat Pencarian Tanpa Data Cocok"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-GS-DIV-04
coverage:
  web: automated
---

# Tampilan No-Result State Saat Pencarian Tanpa Data Cocok

## Prerequisites

- Login sebagai Role: Total Control
- Tabel Division terisi data normal

## Test Steps

1. Buka menu Global Settings > User > tab Division
2. Klik ikon Search pada toolbar TableTools hingga input pencarian terbuka
3. Ketik keyword pencarian 'zzznotfound' lalu tekan Enter
4. Verifikasi tabel menampilkan ilustrasi empty state berukuran 100x100 dengan judul 'No results found' dan deskripsi 'Try adjusting your search or filter.'
5. Verifikasi tidak muncul pesan error sistem atau crash pada komponen tabel

## Notes

- Copywriting empty state filtered mengacu pada matriks kanonikal division.md §7.1.
