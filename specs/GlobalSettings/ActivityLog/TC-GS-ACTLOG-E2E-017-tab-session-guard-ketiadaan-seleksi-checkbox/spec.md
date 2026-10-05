---
id: TC-GS-ACTLOG-E2E-017-tab-session-guard-ketiadaan-seleksi-checkbox
title: "Tab Session: Guard ketiadaan checkbox seleksi dan aksi bulk karena modul read-only murni"
priority: Low
caseType: Negative
status: draft
sourceTc:
  - TC-GS-ACTLOG-74
coverage:
  web: automated
---

# Tab Session: Guard ketiadaan checkbox seleksi dan aksi bulk karena modul read-only murni

## Prerequisites

- Login sebagai Role: Total Control pada Tab Session dengan data log aktif

## Test Steps

1. Buka Tab Session
2. Periksa header tabel pada kolom pertama
3. Verifikasi tidak ada checkbox Select All di header tabel
4. Periksa setiap baris data pada tabel
5. Verifikasi tidak ada checkbox seleksi individual di baris mana pun
6. Verifikasi tidak ada toolbar aksi massal (bulk action) yang muncul

## Notes

- Karena Activity Log bersifat read-only tanpa aksi mutasi, kontrol seleksi massal dihilangkan total.
