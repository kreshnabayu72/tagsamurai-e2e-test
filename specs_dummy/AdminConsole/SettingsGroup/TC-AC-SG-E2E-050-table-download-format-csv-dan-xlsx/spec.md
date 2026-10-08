---
id: TC-AC-SG-E2E-050-table-download-format-csv-dan-xlsx
title: "Ekspor data tabel utama ke format CSV dan XLSX"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SG-97
coverage:
  web: automated
---

# Ekspor data tabel utama ke format CSV dan XLSX

## Prerequisites

- Login sebagai Role: Total Control
- Terdapat data group di tabel utama

## Test Steps

### Unduh Format CSV
1. Klik icon `[⬇ Download]` pada toolbar tabel utama
2. Pada overlay pilihan format, klik `"Download as CSV"`
3. Verifikasi file terunduh ke perangkat lokal dengan format nama `"Groups.csv"`
4. Verifikasi tidak ada toast sukses pasca-unduh (sesuai konvensi ekspor file)
### Unduh Format XLSX
5. Klik kembali icon `[⬇ Download]` lalu pilih `"Download as XLSX"`
6. Verifikasi file terunduh dengan format nama `"Groups.xlsx"`

## Notes

- Nama file unduhan tabel utama adalah Groups tanpa penambahan tanggal.
