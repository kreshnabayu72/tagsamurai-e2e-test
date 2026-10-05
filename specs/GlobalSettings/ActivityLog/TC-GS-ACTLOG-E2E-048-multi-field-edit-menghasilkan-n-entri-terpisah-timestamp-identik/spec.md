---
id: TC-GS-ACTLOG-E2E-048-multi-field-edit-menghasilkan-n-entri-terpisah-timestamp-identik
title: "D9 Multi-field edit dalam satu kali simpan menghasilkan N entri changelog terpisah bertimestamp identik"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-GS-ACTLOG-238
coverage:
  web: automated
---

# D9 Multi-field edit dalam satu kali simpan menghasilkan N entri changelog terpisah bertimestamp identik

## Prerequisites

- Total Control melakukan aksi Edit di modul General Settings yang mengubah 3 field sekaligus dalam 1 kali submit Save

## Test Steps

1. Buka modul General Settings, ubah 3 pengaturan sekaligus (mis. Company Name, Date Format, dan Time Format)
2. Klik `[Save]` untuk menyimpan ketiga perubahan secara bersamaan
3. Buka menu `Global Settings > Activity Log > Tab User Action`
4. Amati baris-baris teratas pada tabel User Action
5. Verifikasi tepat 3 entri changelog baru muncul secara terpisah (satu baris per field yang diubah)
6. Verifikasi ketiga entri tersebut memiliki nilai kolom Date (timestamp) yang sama persis

## Notes

- 1 operasi Save multi-field dipecah menjadi 1 entri log per atribut yang termutasi.
