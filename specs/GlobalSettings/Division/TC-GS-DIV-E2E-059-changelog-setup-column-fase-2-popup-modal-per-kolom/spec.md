---
id: TC-GS-DIV-E2E-059-changelog-setup-column-fase-2-popup-modal-per-kolom
title: "Setup Column Modal Changelog Fase 2: Popup Modal Visibilitas, Urutan, dan Pin 7 Kolom"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-DIV-123
  - TC-GS-DIV-124
  - TC-GS-DIV-125
  - TC-GS-DIV-232
  - TC-GS-DIV-233
  - TC-GS-DIV-234
  - TC-GS-DIV-235
  - TC-GS-DIV-236
  - TC-GS-DIV-237
  - TC-GS-DIV-238
  - TC-GS-DIV-239
  - TC-GS-DIV-240
  - TC-GS-DIV-241
  - TC-GS-DIV-242
  - TC-GS-DIV-243
  - TC-GS-DIV-244
  - TC-GS-DIV-245
  - TC-GS-DIV-246
  - TC-GS-DIV-247
  - TC-GS-DIV-248
  - TC-GS-DIV-249
  - TC-GS-DIV-250
coverage:
  web: automated
---

# Setup Column Modal Changelog Fase 2: Popup Modal Visibilitas, Urutan, dan Pin 7 Kolom

## Prerequisites

- Mode: mock
- Login sebagai Role: Total Control

## Test Steps

1. Buka popup modal Setup Column penuh pada tabel Changelog
2. Verifikasi modal memuat 7 kolom data: Date, Action, Division Name, Field, Old Value, New Value, dan Modified By
3. Verifikasi guard 'minimal 1 kolom visible tersisa' mencegah uncheck pada kolom terakhir yang tersisa
4. Lakukan pengujian ceklis/unceklis, drag reorder, dan pin/unpin pada masing-masing dari 7 kolom data Changelog
5. Verifikasi live preview tabel merefleksikan perubahan status kolom
6. Klik tombol '[Apply]'
7. Verifikasi modal menutup dan konfigurasi kolom tersimpan rapi pada preferensi pengguna

## Notes

- Mencakup granularitas 4+3N per-kolom untuk seluruh kolom tabel changelog sesuai standar interim platform.
