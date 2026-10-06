---
id: TC-AC-ACAL-E2E-021-tab-session-download-csv-xlsx-filtered-dan-error
title: "Tab Session — Export CSV/XLSX seluruh data, data terfilter, filter kosong, dan penanganan error"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACAL-118
  - TC-AC-ACAL-119
  - TC-AC-ACAL-120
  - TC-AC-ACAL-121
  - TC-AC-ACAL-123
coverage:
  web: automated
---

# Tab Session — Export CSV/XLSX seluruh data, data terfilter, filter kosong, dan penanganan error

## Prerequisites

- Login sebagai Role: Principal Total Control
- Tab Session terisi data riwayat aktivitas

## Test Steps

### Download Seluruh Data (CSV & XLSX)

1. Buka menu `Admin Console > Activity Log` (Tab Session)
2. Klik tombol `[Download]` pada toolbar
3. Pilih opsi `"Download as CSV"`
4. Verifikasi file bernama `Activity-Log-Session.csv` berhasil diunduh memuat seluruh baris data (tanpa toast sukses berlebih)
5. Klik kembali `[Download]` dan pilih `"Download as XLSX"`
6. Verifikasi file `Activity-Log-Session.xlsx` berhasil diunduh

### Download Mengikuti Filter Aktif

7. Buka Filter Panel, terapkan filter Division tertentu (contoh: `"Finance"`), lalu klik `[Apply]`
8. Klik `[Download]` > `"Download as CSV"`
9. Verifikasi isi file CSV hanya memuat data dengan Division Finance

### Download Hasil Filter Kosong

10. Masukkan keyword search yang menghasilkan `No results found`
11. Klik `[Download]` > `"Download as CSV"`
12. Verifikasi file CSV terunduh hanya berisi baris header kolom (bukan pesan error)

### Penanganan Error Gagal Download (Mock)

13. Intercept endpoint `/v2/analytics-reporting/session-logs/export` dengan response error status 500
14. Klik `[Download]` > `"Download as CSV"`
15. Verifikasi toast error muncul dengan pesan `"Error, failed to download Activity-Log-Session."`

## Notes

- Menjamin konsistensi payload hasil download terhadap filter yang sedang aktif di UI.
