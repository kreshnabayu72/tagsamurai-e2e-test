---
id: TC-GS-POS-E2E-041-download-csv-xlsx-popup-changelog
title: "Binary Buffer: Download CSV dan XLSX Popup Changelog mengikuti filter dan kolom tampil"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-POS-237
  - TC-GS-POS-238
  - TC-GS-POS-239
coverage:
  web: automated
---

# Binary Buffer: Download CSV dan XLSX Popup Changelog mengikuti filter dan kolom tampil

## Prerequisites

- Login sebagai Total Control
- Popup Changelog terbuka

## Test Steps

### Download CSV dan XLSX Changelog

1. Klik ikon Download pada toolbar Popup Changelog
2. Klik opsi "Download as CSV"
3. Verifikasi file CSV riwayat terunduh dan memuat data changelog
4. Klik opsi "Download as XLSX"
5. Verifikasi file XLSX terunduh dengan benar

### Download Mengikuti Filter & Kolom Aktif

6. Terapkan filter Action "Create" pada Changelog
7. Sembunyikan kolom "Field" via Setup Column
8. Lakukan unduh file CSV
9. Verifikasi isi file CSV hanya memuat baris Action "Create" dan kolom "Field" tidak disertakan

## Notes

- Menggabungkan TC-GS-POS-237, 238, dan 239 dalam kelas harness Binary Buffer.
