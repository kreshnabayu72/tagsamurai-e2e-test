---
id: TC-GS-ACTLOG-E2E-028-tab-session-setup-column-urutan-drag-drop-dan-persistensi-f5
title: "Tab Session Setup Column: Reorder Urutan Kolom via Drag-and-Drop dan Persistensi F5"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ACTLOG-97
coverage:
  web: automated
---

# Tab Session Setup Column: Reorder Urutan Kolom via Drag-and-Drop dan Persistensi F5

## Prerequisites

- Login sebagai Role: Total Control Global Settings
- User berada di Tab Session

## Test Steps

### Reorder Kolom & Pratinjau
1. Buka modal Setup Column Tab Session.
2. Seret (drag-and-drop) baris kolom Activity ke posisi paling atas (di atas kolom Date).
3. Verifikasi pada tabel pratinjau kolom Activity berpindah menjadi kolom pertama.
4. Klik tombol [Save].
5. Verifikasi pada tabel utama kolom Activity kini berada di posisi pertama.
### Persistensi & Reset
6. Lakukan refresh halaman browser (F5).
7. Verifikasi urutan kolom yang diubah tetap bertahan.
8. Buka kembali modal Setup Column, klik tombol [Reset to Default].
9. Verifikasi urutan kembali ke susunan bawaan (Date di posisi pertama).
10. Klik [Save], verifikasi tabel kembali ke urutan default.

## Notes

- Urutan kolom fleksibel diatur menggunakan drag-and-drop dan tersimpan secara persisten.
