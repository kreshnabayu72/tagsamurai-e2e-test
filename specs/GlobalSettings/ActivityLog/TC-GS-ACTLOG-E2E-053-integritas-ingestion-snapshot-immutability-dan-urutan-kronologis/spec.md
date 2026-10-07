---
id: TC-GS-ACTLOG-E2E-053-integritas-ingestion-snapshot-immutability-dan-urutan-kronologis
title: "Snapshot Immutability Modified By dan Pengurutan Kronologis Berdasarkan Waktu Date untuk Event Out-of-Order"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-GS-ACTLOG-213
  - TC-GS-ACTLOG-214
coverage:
  web: automated
---

# Snapshot Immutability Modified By dan Pengurutan Kronologis Berdasarkan Waktu Date untuk Event Out-of-Order

## Prerequisites

- Login sebagai Role: Total Control Global Settings
- Admin 'Wulan Sari' memiliki riwayat mutasi lama, kemudian namanya diubah menjadi 'Wulan Sari Dewi' di modul User
- Dua event audit tiba out-of-order di server (event A jam 10:00 tiba setelah event B jam 10:05)

## Test Steps

### Snapshot Immutability Modified By
1. Buka Tab User Action di Global Settings > Activity Log.
2. Cari entri mutasi lama yang dibuat oleh admin 'Wulan Sari' sebelum namanya diubah.
3. Verifikasi kolom Modified By pada entri historis tersebut tetap menampilkan 'Wulan S' (hover 'Wulan Sari') dan tidak berubah menjadi 'Wulan Sari Dewi'.
### Pengurutan Kronologis Out-of-Order Ingestion
4. Tinjau dua event yang di-ingest ke server dengan jeda kedatangan terbalik (event A timestamp 10:00 tiba di database setelah event B timestamp 10:05).
5. Amati susunan tabel Tab User Action.
6. Verifikasi baris berstempel 10:05 tetap berada di atas baris berstempel 10:00 (tabel diurutkan murni berdasarkan kolom Date aksi, bukan waktu kedatangan data di server).

## Notes

- Audit log menjaga integritas snapshot historis dan urutan kronologis absolut.
