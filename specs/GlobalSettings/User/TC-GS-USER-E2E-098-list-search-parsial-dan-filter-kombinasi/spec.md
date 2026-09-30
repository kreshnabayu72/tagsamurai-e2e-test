---
id: TC-GS-USER-E2E-098-list-search-parsial-dan-filter-kombinasi
title: 'Search parsial, case-insensitive, dan Filter Division dengan Active'
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-140
  - TC-GS-USER-141
  - TC-GS-USER-142
coverage:
  web: automated
---

# Search parsial, case-insensitive, dan Filter Division dengan Active

## Prerequisites

- Login sebagai Role: Total Control biasa (`totalControl2_automated_qaTeam1`), entity Client
- User "Agus Setiawan" dan "Maya Putri" ada, dengan Division dan status Active yang bervariasi
- Spec ini tidak mengubah data

## Test Steps

1. Cari "Agus" di Search dan tekan `Enter`
2. Verifikasi hanya "Agus Setiawan" yang muncul
3. Kosongkan Search, lalu cari "MAYA"
4. Verifikasi "Maya Putri" tetap muncul (tidak peka huruf besar)
5. Kosongkan Search, buka Filter Panel, lalu pilih Division `Finance` dan Status `Active`, klik `[Apply Filter]`
6. Verifikasi hanya baris yang cocok dengan kedua kriteria yang tampil (AND, bukan OR)

## Notes

- Sumber `user.md` bagian 4.4 dan `prd-conventions.md` bagian 9.6.
