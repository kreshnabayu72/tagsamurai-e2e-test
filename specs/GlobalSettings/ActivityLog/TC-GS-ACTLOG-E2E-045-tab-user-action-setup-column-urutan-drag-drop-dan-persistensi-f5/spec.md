---
id: TC-GS-ACTLOG-E2E-045-tab-user-action-setup-column-urutan-drag-drop-dan-persistensi-f5
title: "Tab User Action Setup Column: Reorder Urutan Kolom via Drag-and-Drop dan Persistensi F5"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ACTLOG-184
coverage:
  web: automated
---

# Tab User Action Setup Column: Reorder Urutan Kolom via Drag-and-Drop dan Persistensi F5

## Prerequisites

- Login sebagai Role: Total Control Global Settings
- User berada di Tab User Action

## Test Steps

### Reorder Kolom & Pratinjau
1. Buka modal Setup Column Tab User Action.
2. Seret (drag-and-drop) baris kolom Object ke posisi paling atas (di atas kolom Date).
3. Verifikasi pada tabel pratinjau kolom Object berpindah menjadi kolom pertama.
4. Klik tombol [Save].
5. Verifikasi pada tabel utama kolom Object kini berada di posisi pertama.
### Persistensi & Reset
6. Lakukan refresh halaman browser (F5).
7. Verifikasi urutan kolom yang diubah tetap bertahan.
8. Buka kembali modal Setup Column, klik tombol [Reset to Default].
9. Verifikasi urutan kembali ke susunan bawaan (Date di posisi pertama).
10. Klik [Save], verifikasi tabel kembali ke urutan default.

## Notes

- Reorder kolom memungkinkan penyesuaian tata letak audit sesuai kebutuhan investigasi.
