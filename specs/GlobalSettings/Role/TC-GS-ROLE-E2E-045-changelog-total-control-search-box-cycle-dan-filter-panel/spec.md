---
id: TC-GS-ROLE-E2E-045-changelog-total-control-search-box-cycle-dan-filter-panel
title: "Pola Interaksi Search Box dan Filter Panel Modal Changelog Total Control (Termasuk Filter Date 1 Hari & Range)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ROLE-85
  - TC-GS-ROLE-187
  - TC-GS-ROLE-188
  - TC-GS-ROLE-189
  - TC-GS-ROLE-190
  - TC-GS-ROLE-191
  - TC-GS-ROLE-192
  - TC-GS-ROLE-341
  - TC-GS-ROLE-342
coverage:
  web: automated
---

# Pola Interaksi Search Box dan Filter Panel Modal Changelog Total Control (Termasuk Filter Date 1 Hari & Range)

## Prerequisites

- Login sebagai Role: Total Control
- Tersedia beragam entri riwayat log di modal Changelog Total Control

## Test Steps

1. Buka Modal Changelog dari Tab Total Control
2. Klik icon Search pada toolbar modal Changelog
3. Ketik keyword teks (User Name, Field, atau Modified By) lalu tekan Enter
4. Verifikasi tabel Changelog memfilter baris yang sesuai dengan keyword pencarian
5. Klik icon Filter pada toolbar modal Changelog
6. Verifikasi Filter Panel Changelog memuat filter: Action, User Name, Modified By, dan Date
7. Pilih filter Date untuk 1 hari spesifik (start=end sama) lalu klik [Apply]
8. Verifikasi tabel Changelog menyaring log yang tercatat tepat pada tanggal tersebut
9. Atur filter Date ke rentang beberapa hari lalu klik [Apply]
10. Verifikasi tabel Changelog menampilkan seluruh log dalam rentang tanggal tersebut
11. Uji penerapan filter Action (Assign, Remove, Edit), User Name, dan Modified By secara terpisah

## Notes

- Filter Panel modal Changelog Total Control mencakup filter Date (1 hari / range) serta dropdown Action, User Name, dan Modified By (role.md §8.1, §4.2).
