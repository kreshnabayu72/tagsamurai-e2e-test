---
id: TC-GS-POS-E2E-035-download-csv-xlsx-tabel-utama
title: "Binary Buffer: Download CSV dan XLSX tabel utama, kesesuaian query, dan pengecualian kolom tersembunyi"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-POS-192
  - TC-GS-POS-193
  - TC-GS-POS-194
  - TC-GS-POS-195
  - TC-GS-POS-196
  - TC-GS-POS-197
  - TC-GS-POS-198
coverage:
  web: automated
---

# Binary Buffer: Download CSV dan XLSX tabel utama, kesesuaian query, dan pengecualian kolom tersembunyi

## Prerequisites

- Login sebagai Total Control
- Tabel Position terisi data

## Test Steps

### Screening Overlay Download

1. Klik ikon Download pada Table Tools
2. Verifikasi overlay Download muncul dengan opsi "Download as CSV" dan "Download as XLSX" (sesuai konvensi NC-17)

### Download Penuh Tanpa Filter

3. Klik opsi "Download as CSV"
4. Verifikasi file CSV terunduh dan memuat seluruh data baris Position lintas halaman
5. Klik opsi "Download as XLSX"
6. Verifikasi file XLSX terunduh dengan struktur yang valid

### Download Mengikuti Query Aktif & Kolom Tersembunyi

7. Terapkan kata kunci Search "Manager" pada tabel
8. Sembunyikan kolom "Last Updated" via Setup Column
9. Lakukan download CSV
10. Verifikasi isi file CSV hanya memuat baris yang mengandung "Manager" dan kolom Last Updated tidak disertakan di dalam file
11. Tampilkan kembali kolom Last Updated, lakukan download, verifikasi kolom Last Updated kembali muncul di file

## Notes

- Menggabungkan pengujian file export dari TC-GS-POS-192 s.d. 198 dalam kelas harness Binary Buffer.
