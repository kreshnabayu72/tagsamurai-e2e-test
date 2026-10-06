---
id: TC-GS-DIV-E2E-048-tabel-utama-download-csv-xlsx-dan-penanganan-error
title: "Ekspor Download CSV dan XLSX Mengikuti Filter Aktif Serta Penanganan Error"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-DIV-81
  - TC-GS-DIV-82
  - TC-GS-DIV-83
coverage:
  web: automated
---

# Ekspor Download CSV dan XLSX Mengikuti Filter Aktif Serta Penanganan Error

## Prerequisites

- Login sebagai Role: Total Control
- Tabel Division berisi data aktif

## Test Steps

1. Buka menu Global Settings > User > tab Division
2. Klik ikon 'Download' pada toolbar TableTools
3. Verifikasi popover download terbuka menampilkan opsi 'Download CSV' dan 'Download XLSX'
4. Klik opsi 'Download CSV'
5. Verifikasi file CSV berhasil diunduh dengan penamaan default 'Division.csv'
6. Terapkan filter pencarian nama tertentu di tabel
7. Klik kembali ikon 'Download' lalu klik 'Download XLSX'
8. Verifikasi file Excel terunduh hanya memuat baris data yang cocok dengan filter aktif
9. Kondisikan endpoint ekspor disimulasikan error
10. Klik download dan verifikasi muncul toast error: 'Error, failed to download Division.'

## Notes

- Spesifikasi download dan format nama berkas mengacu pada division.md §4.1 item 13, §5, dan §6.
