---
id: TC-GS-ACTLOG-E2E-026-tab-user-action-search-per-kolom-dan-multi-kolom
title: "Tab User Action: Pencarian per kolom untuk 7 kolom teks, guard Date, dan pencarian multi-kolom"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ACTLOG-123
  - TC-GS-ACTLOG-124
  - TC-GS-ACTLOG-125
  - TC-GS-ACTLOG-126
  - TC-GS-ACTLOG-127
  - TC-GS-ACTLOG-128
  - TC-GS-ACTLOG-129
  - TC-GS-ACTLOG-130
  - TC-GS-ACTLOG-131
coverage:
  web: automated
---

# Tab User Action: Pencarian per kolom untuk 7 kolom teks, guard Date, dan pencarian multi-kolom

## Prerequisites

- Login sebagai Role: Total Control pada Tab User Action dengan data changelog bervariasi

## Test Steps

1. Buka Tab User Action
2. Masukkan keyword Action "Edit" pada search box lalu tekan Enter, verifikasi entri yang cocok ditampilkan
3. Masukkan keyword Object "Brand" lalu tekan Enter, verifikasi entri yang cocok ditampilkan
4. Masukkan nama entitas pada kolom Name lalu tekan Enter, verifikasi entri yang cocok ditampilkan
5. Masukkan nama field pada kolom Field lalu tekan Enter, verifikasi entri yang cocok ditampilkan
6. Masukkan nilai Old Value lalu tekan Enter, verifikasi entri yang cocok ditampilkan
7. Masukkan nilai New Value lalu tekan Enter, verifikasi entri yang cocok ditampilkan
8. Masukkan nama admin pada kolom Modified By lalu tekan Enter, verifikasi entri yang cocok ditampilkan
9. Masukkan keyword yang cocok di ≥2 kolom berbeda (mis. "Finance" cocok di Object dan Old Value) lalu tekan Enter
10. Verifikasi seluruh entri yang cocok di kolom mana pun ditampilkan pada hasil pencarian
11. Masukkan teks tanggal kalender pada search box lalu tekan Enter
12. Verifikasi tidak ada pencarian yang dicocokkan berdasarkan kolom Date (guard Date wajib via Filter Panel)

## Notes

- Pencarian di Tab User Action mencakup seluruh kolom metadata perubahan kecuali Date.
