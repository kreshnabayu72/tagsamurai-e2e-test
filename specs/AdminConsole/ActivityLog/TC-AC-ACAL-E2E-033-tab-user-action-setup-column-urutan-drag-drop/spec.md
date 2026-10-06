---
id: TC-AC-ACAL-E2E-033-tab-user-action-setup-column-urutan-drag-drop
title: "Tab User Action — Drag and drop reordering urutan 8 kolom dan persistensi reload F5"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACAL-184
  - TC-AC-ACAL-185
  - TC-AC-ACAL-186
  - TC-AC-ACAL-187
  - TC-AC-ACAL-188
  - TC-AC-ACAL-189
  - TC-AC-ACAL-190
  - TC-AC-ACAL-191
coverage:
  web: automated
---

# Tab User Action — Drag and drop reordering urutan 8 kolom dan persistensi reload F5

## Prerequisites

- Login sebagai Role: Principal Total Control
- Pengguna berada di `Admin Console > Activity Log` (Tab User Action)

## Test Steps

1. Klik header kolom `⋯` > klik `"Setup Column"`
2. Geser (drag) baris kolom `Action` ke posisi paling atas (menggeser posisi `Date`)
3. Verifikasi panel Live Preview langsung mengupdate urutan kolom dengan Action di posisi pertama
4. Lakukan drag reorder pada kolom-kolom lainnya (`Object`, `Name`, `Field`, `Old Value`, `New Value`, `Modified By`)
5. Klik tombol `[Save]`
6. Verifikasi modal tertutup dan header tabel Tab User Action menampilkan urutan kolom baru yang telah disesuaikan
7. Lakukan refresh halaman browser (F5)
8. Verifikasi urutan kolom baru tersebut tetap persisten dan tidak kembali ke urutan default

## Notes

- Memverifikasi sinkronisasi reorder kolom drag-and-drop pada Tab User Action.
