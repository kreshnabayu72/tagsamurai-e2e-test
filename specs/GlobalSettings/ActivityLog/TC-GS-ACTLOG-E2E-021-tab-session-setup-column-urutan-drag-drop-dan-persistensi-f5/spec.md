---
id: TC-GS-ACTLOG-E2E-021-tab-session-setup-column-urutan-drag-drop-dan-persistensi-f5
title: "Tab Session: Pengaturan urutan kolom tabel via drag-and-drop Setup Column dan persistensi refresh F5"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ACTLOG-98
  - TC-GS-ACTLOG-99
  - TC-GS-ACTLOG-100
  - TC-GS-ACTLOG-101
  - TC-GS-ACTLOG-102
  - TC-GS-ACTLOG-103
  - TC-GS-ACTLOG-104
  - TC-GS-ACTLOG-105
  - TC-GS-ACTLOG-106
  - TC-GS-ACTLOG-107
coverage:
  web: automated
---

# Tab Session: Pengaturan urutan kolom tabel via drag-and-drop Setup Column dan persistensi refresh F5

## Prerequisites

- Login sebagai Role: Total Control pada Tab Session di modal Setup Column

## Test Steps

1. Buka modal Setup Column pada Tab Session
2. Drag baris kolom Date ke urutan ketiga
3. Drag baris kolom User ke urutan pertama
4. Drag baris kolom Employee ID, Position, Division, Activity, Status, Note, IP Address, dan Device/Browser ke posisi kustom
5. Verifikasi urutan kolom pada Live Preview langsung berubah mengikuti hasil drag
6. Klik tombol `[Save]`
7. Verifikasi urutan kolom pada tabel utama Tab Session berubah sesuai susunan baru
8. Lakukan refresh halaman browser (F5)
9. Verifikasi urutan kolom kustom tetap bertahan (persist) setelah refresh

## Notes

- Drag and drop reordering berlaku interaktif dengan feedback visual langsung pada Live Preview.
