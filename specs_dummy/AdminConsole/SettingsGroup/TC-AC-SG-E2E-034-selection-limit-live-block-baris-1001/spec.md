---
id: TC-AC-SG-E2E-034-selection-limit-live-block-baris-1001
title: "Selection Limit: Live-block seleksi manual saat checkbox ke-1001 dicentang"
priority: Medium
caseType: Edge
status: draft
sourceTc:
  - TC-AC-SG-151
coverage:
  web: automated
---

# Selection Limit: Live-block seleksi manual saat checkbox ke-1001 dicentang

## Prerequisites

- Mode: mock
- Login sebagai Role: Total Control
- Dataset terisi ≥ 1001 baris grup (mock dataset / pagination besar)

## Test Steps

### Seleksi Manual Mencapai Limit 1000
1. Buka `Settings > Group` dengan dataset > 1000 baris
2. Lakukan seleksi checkbox satu per satu hingga mencapai baris ke-1000
3. Amati status checkbox pada baris ke-1001
4. Verifikasi checkbox pada baris ke-1001 (dan baris setelahnya) berstatus disabled
5. Hover pada checkbox baris ke-1001
6. Verifikasi muncul tooltip 🔖 `"You've reached the maximum selection of 1000 rows."` (prd-conventions.md)
7. Verifikasi 1000 baris yang telah dicentang sebelumnya tetap terpilih
8. Verifikasi Bulk Action Bar tetap aktif dan dapat digunakan untuk 1000 baris tersebut

## Notes

- Selection Limit 1000 baris adalah aturan baku platform-wide.
