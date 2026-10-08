---
id: TC-GS-ACTLOG-E2E-052-integritas-ingestion-atomik-rollback-transaksi-gagal
title: "Atomic Rollback Ingestion: Ketiadaan Pencatatan Log pada Operasi Database yang Gagal (Zero Phantom Log)"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-GS-ACTLOG-212
coverage:
  web: automated
---

# Atomic Rollback Ingestion: Ketiadaan Pencatatan Log pada Operasi Database yang Gagal (Zero Phantom Log)

## Prerequisites

- Login sebagai Role: Total Control Global Settings
- Instrumentasi simulasi kegagalan database / 5xx pada endpoint mutasi (misal Create Brand 'Rollback Test')

## Test Steps

### Simulasi Kegagalan Mutasi
1. Picu kegagalan transaksi database (injeksi HTTP 500 / rollback) saat mengeksekusi Create Brand 'Rollback Test'.
2. Verifikasi sistem menampilkan indikator kegagalan operasi pada modul Brand.
### Verifikasi Zero Phantom Log di Activity Log
3. Buka menu Global Settings > Activity Log > Tab User Action.
4. Masukkan keyword 'Rollback Test' pada Search box lalu tekan Enter.
5. Verifikasi tabel menampilkan 'No results found'.
6. Periksa filter Object = 'Brand' dan Action = 'Create', verifikasi tidak ada entri audit palsu (*phantom log*) yang tercipta untuk transaksi yang gagal di-commit.

## Notes

- Log audit wajib atomik dengan commit transaksi database sumber; rollback transaksi menjamin zero phantom log.
