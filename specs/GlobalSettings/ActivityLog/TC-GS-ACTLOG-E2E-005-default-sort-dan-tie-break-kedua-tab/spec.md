---
id: TC-GS-ACTLOG-E2E-005-default-sort-dan-tie-break-kedua-tab
title: "Default Sort Date Descending dan Tie-Break Timestamp Identik di Kedua Tab"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-GS-ACTLOG-10
  - TC-GS-ACTLOG-11
coverage:
  web: automated
---

# Default Sort Date Descending dan Tie-Break Timestamp Identik di Kedua Tab

## Prerequisites

- Login sebagai Role: Total Control Global Settings
- Terdapat entri Session dengan stempel waktu identik (misal 14 Jul 2026, 08:10) dengan variasi Activity dan User
- Terdapat entri User Action dengan stempel waktu identik (misal 14 Jun 2026, 14:05) dengan variasi Action dan Field

## Test Steps

### Default Sort & Tie-Break Tab Session
1. Buka Tab Session tanpa mengubah konfigurasi sorting.
2. Verifikasi entri tersusun secara default dari tanggal terbaru ke terlama (Date descending).
3. Pada kelompok entri dengan timestamp identik, verifikasi urutan tie-break diurutkan berdasarkan Activity A-Z.
4. Jika Activity sama pada timestamp identik, verifikasi urutan tie-break dilanjutkan berdasarkan User A-Z (menurut nama lengkap).
### Default Sort & Tie-Break Tab User Action
5. Klik tab 'User Action' tanpa mengubah konfigurasi sorting.
6. Verifikasi entri tersusun secara default dari tanggal terbaru ke terlama (Date descending).
7. Pada kelompok entri dengan timestamp identik, verifikasi urutan tie-break diurutkan berdasarkan Action A-Z.
8. Jika Action sama pada timestamp identik, verifikasi urutan tie-break dilanjutkan berdasarkan Field A-Z.

## Notes

- Tie-break deterministik menjamin konsistensi urutan tampilan ketika beberapa event terjadi pada detik yang sama.
