---
id: TC-AC-ACAL-E2E-035-tab-user-action-download-csv-xlsx-filtered-dan-error
title: "Tab User Action — Export CSV/XLSX seluruh data, data terfilter, filter kosong, dan penanganan error"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACAL-203
  - TC-AC-ACAL-204
  - TC-AC-ACAL-205
  - TC-AC-ACAL-206
  - TC-AC-ACAL-208
coverage:
  web: automated
---

# Tab User Action — Export CSV/XLSX seluruh data, data terfilter, filter kosong, dan penanganan error

## Prerequisites

- Login sebagai Role: Principal Total Control
- Tab User Action terisi data riwayat aktivitas

## Test Steps

### Download Seluruh Data (CSV & XLSX)

1. Buka menu `Admin Console > Activity Log` > klik tab `"User Action"`
2. Klik tombol `[Download]` pada toolbar
3. Pilih opsi `"Download as CSV"`
4. Verifikasi file bernama `Activity-Log-User-Action.csv` berhasil diunduh memuat seluruh baris data
5. Klik kembali `[Download]` dan pilih `"Download as XLSX"`
6. Verifikasi file `Activity-Log-User-Action.xlsx` berhasil diunduh

### Download Mengikuti Filter Aktif

7. Buka Filter Panel, pilih Action `"Create"`, lalu klik `[Apply]`
8. Klik `[Download]` > `"Download as CSV"`
9. Verifikasi isi file CSV hanya memuat baris dengan Action Create

### Download Hasil Filter Kosong

10. Masukkan keyword search yang menghasilkan `No results found`
11. Klik `[Download]` > `"Download as CSV"`
12. Verifikasi file CSV terunduh hanya berisi baris header kolom

### Penanganan Error Gagal Download (Mock)

13. Intercept endpoint `/v2/analytics-reporting/change-logs/export` dengan status response error 500
14. Klik `[Download]` > `"Download as CSV"`
15. Verifikasi toast error muncul dengan pesan `"Error, failed to download Activity-Log-User-Action."`

## Notes

- Memverifikasi mekanisme export dan error handling pada Tab User Action.
