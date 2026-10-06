---
id: TC-GS-ROLE-E2E-048-changelog-total-control-sorting-setup-column-dan-download
title: "Sorting 3-State 7 Kolom, Setup Column 7 Kolom, dan Ekspor Download Modal Changelog Total Control"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ROLE-206
  - TC-GS-ROLE-207
  - TC-GS-ROLE-208
  - TC-GS-ROLE-210
  - TC-GS-ROLE-289
  - TC-GS-ROLE-290
  - TC-GS-ROLE-291
  - TC-GS-ROLE-292
  - TC-GS-ROLE-293
  - TC-GS-ROLE-294
  - TC-GS-ROLE-295
  - TC-GS-ROLE-296
  - TC-GS-ROLE-297
  - TC-GS-ROLE-298
  - TC-GS-ROLE-299
  - TC-GS-ROLE-300
  - TC-GS-ROLE-301
  - TC-GS-ROLE-302
  - TC-GS-ROLE-303
  - TC-GS-ROLE-304
  - TC-GS-ROLE-305
  - TC-GS-ROLE-306
  - TC-GS-ROLE-307
  - TC-GS-ROLE-308
  - TC-GS-ROLE-309
  - TC-GS-ROLE-310
  - TC-GS-ROLE-311
  - TC-GS-ROLE-312
coverage:
  web: automated
---

# Sorting 3-State 7 Kolom, Setup Column 7 Kolom, dan Ekspor Download Modal Changelog Total Control

## Prerequisites

- Mode: mock
- Login sebagai Role: Total Control
- Data log tersedia di modal Changelog Total Control

## Test Steps

1. Buka Modal Changelog Total Control
2. Verifikasi default sort kolom Date adalah Newest First (Desc)
3. Uji sorting 3-state untuk 7 kolom: Date, Action, User Name, Field, Old Value, New Value, Modified By
4. Buka Setup Column pada modal Changelog (Quick Overlay dan Modal Penuh)
5. Uji toggle uncheck, drag geser urutan, dan pin kolom untuk 7 kolom Changelog
6. Uji guard minimal 1 kolom tersisa serta tombol [Reset to Default] dan [Cancel]
7. Klik tombol Download pada toolbar modal Changelog
8. Verifikasi file Changelog-Role-Permission-Total-Control.csv berhasil diunduh tanpa toast sukses

## Notes

- Setup Column dan download pada modal Changelog Total Control mengelola 7 kolom data riwayat audit (role.md §8.1).
