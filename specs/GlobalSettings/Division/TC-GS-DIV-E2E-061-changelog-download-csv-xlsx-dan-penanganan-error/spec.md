---
id: TC-GS-DIV-E2E-061-changelog-download-csv-xlsx-dan-penanganan-error
title: "Ekspor Download Changelog CSV/XLSX dan Penanganan Kegagalan Server"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-DIV-129
  - TC-GS-DIV-130
coverage:
  web: automated
---

# Ekspor Download Changelog CSV/XLSX dan Penanganan Kegagalan Server

## Prerequisites

- Login sebagai Role: Total Control
- Modal Changelog memuat riwayat mutasi

## Test Steps

1. Buka Modal Changelog Division
2. Klik tombol 'Download' pada toolbar Changelog
3. Pilih opsi 'Download CSV' dan verifikasi berkas CSV riwayat mutasi divisi berhasil diunduh
4. Pilih opsi 'Download XLSX' dan verifikasi berkas Excel berhasil diunduh
5. Kondisikan endpoint ekspor changelog mengalami kegagalan 500
6. Klik kembali download dan verifikasi muncul toast notifikasi error ekspor

## Notes

- Menguji ekspor riwayat audit trail divisi ke format CSV dan XLSX (division.md §4.1 item 12).
