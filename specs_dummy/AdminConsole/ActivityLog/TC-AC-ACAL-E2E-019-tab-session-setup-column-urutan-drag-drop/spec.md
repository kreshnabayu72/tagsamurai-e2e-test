---
id: TC-AC-ACAL-E2E-019-tab-session-setup-column-urutan-drag-drop
title: "Tab Session — Drag and drop reordering urutan 10 kolom dan persistensi reload F5"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACAL-95
  - TC-AC-ACAL-96
  - TC-AC-ACAL-97
  - TC-AC-ACAL-98
  - TC-AC-ACAL-99
  - TC-AC-ACAL-100
  - TC-AC-ACAL-101
  - TC-AC-ACAL-102
  - TC-AC-ACAL-103
  - TC-AC-ACAL-104
coverage:
  web: automated
---

# Tab Session — Drag and drop reordering urutan 10 kolom dan persistensi reload F5

## Prerequisites

- Login sebagai Role: Principal Total Control
- Pengguna berada di `Admin Console > Activity Log` (Tab Session)

## Test Steps

1. Klik header kolom `⋯` > klik `"Setup Column"`
2. Geser (drag) baris kolom `User` ke posisi paling atas (menggeser posisi `Date`)
3. Verifikasi panel Live Preview langsung mengupdate urutan kolom dengan User di posisi pertama
4. Lakukan drag reorder pada kolom-kolom lainnya (`Employee ID`, `Position`, `Division`, `Activity`, `Status`, `Note`, `IP Address`, `Device / Browser`)
5. Klik tombol `[Save]`
6. Verifikasi modal tertutup dan header tabel Tab Session menampilkan urutan kolom baru yang telah disesuaikan
7. Lakukan refresh halaman browser (F5)
8. Verifikasi urutan kolom baru tersebut tetap persisten dan tidak kembali ke urutan default

## Notes

- Memverifikasi interaksi drag-and-drop HTML5 / library UI serta sinkronisasi state order ke tabel.
