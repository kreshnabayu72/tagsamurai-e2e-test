---
id: TC-GS-USER-E2E-046-user-list-toolbar-search-flow
title: "User List: Toolbar Search interaksi, debounce, exact match, dan clear"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-413
  - TC-GS-USER-414
  - TC-GS-USER-415
  - TC-GS-USER-416
  - TC-GS-USER-417
  - TC-GS-USER-418
  - TC-GS-USER-419
  - TC-GS-USER-420
  - TC-GS-USER-421
  - TC-GS-USER-422
  - TC-GS-USER-1034
coverage:
  web: automated
---

# User List: Toolbar Search interaksi, debounce, exact match, dan clear

## Prerequisites

- Berada di Global Settings > User > User List

## Test Steps

### Pencarian Data

1. Klik ikon Search di toolbar, ketik 'Dewi'
2. Verifikasi tabel otomatis tersaring menampilkan baris Dewi Lestari via debounce
3. Ketik teks status Active (exact match), verifikasi pencarian kolom Active bekerja tepat (TC-1034)
4. Klik tombol [✕] clear pada input pencarian, verifikasi seluruh data tabel kembali tampil utuh

## Notes

- Menggabungkan 11 test case granular (TC-GS-USER-413 s.d. TC-GS-USER-1034).
