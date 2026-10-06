---
id: TC-AC-ACAL-E2E-038-sinkronisasi-real-time-sse-kedua-tab
title: "Sinkronisasi Real-time SSE — Entri baru otomatis muncul di atas tabel dan filter guard"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACAL-18
  - TC-AC-ACAL-19
  - TC-AC-ACAL-82
  - TC-AC-ACAL-173
coverage:
  web: automated
---

# Sinkronisasi Real-time SSE — Entri baru otomatis muncul di atas tabel dan filter guard

## Prerequisites

- Login sebagai Role: Principal Total Control
- Pengguna membuka halaman `Admin Console > Activity Log` di sesi browser utama

## Test Steps

### Real-Time SSE Tab Session

1. Buka Tab Session di browser utama
2. Di sesi browser sekunder (atau API trigger), lakukan login staff Admin Console baru
3. Amati tabel Tab Session di browser utama tanpa melakukan reload/refresh
4. Verifikasi baris log baru `"Session started"` otomatis muncul di posisi paling atas tabel secara real-time tanpa mengubah posisi scroll

### Real-Time SSE Tab User Action

5. Klik tab `"User Action"` di browser utama
6. Di sesi browser sekunder, lakukan aksi write pada salah satu modul Admin Console (misal: Create Distributor)
7. Amati tabel Tab User Action di browser utama tanpa reload
8. Verifikasi baris log mutasi data baru otomatis muncul di urutan paling atas

### Real-Time SSE dengan Filter Aktif (Filter Guard)

9. Di Tab User Action, terapkan filter Object = `"Distributor"`
10. Di sesi sekunder, lakukan aksi write pada modul Partner (Object = `"Partner"`)
11. Amati tabel Tab User Action di browser utama
12. Verifikasi entri baru Partner TIDAK muncul di tampilan tabel yang sedang terfilter Distributor (SSE menghormati kriteria filter aktif)

## Notes

- TAG Samurai menerapkan Tier 1 Server-Sent Events (SSE) untuk sinkronisasi live data audit trail secara silent tanpa menampilkan dialog popup mengganggu.
