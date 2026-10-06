---
id: TC-GS-DIV-E2E-046-tabel-utama-setup-column-fase-2-popup-modal-live-preview-dan-pin
title: "Setup Column Fase 2: Popup Modal, Live Preview, Toggle Ceklis, Geser, dan Pin Kolom"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-DIV-75
  - TC-GS-DIV-76
  - TC-GS-DIV-77
  - TC-GS-DIV-228
  - TC-GS-DIV-229
  - TC-GS-DIV-230
  - TC-GS-DIV-231
  - TC-GS-DIV-270
  - TC-GS-DIV-271
  - TC-GS-DIV-272
coverage:
  web: automated
---

# Setup Column Fase 2: Popup Modal, Live Preview, Toggle Ceklis, Geser, dan Pin Kolom

## Prerequisites

- Mode: mock
- Login sebagai Role: Total Control

## Test Steps

1. Buka modal Setup Column penuh (size sm ~420px) melalui header Actions (⋯)
2. Verifikasi judul modal 'Setup Column', subtitle 'Manage column visibility, reorder, and freeze columns.', search input, list kolom dengan drag handle, serta tombol footer '[Reset to Default]', '[Cancel]', dan '[Apply]'
3. Coba uncheck seluruh kolom hingga menyisakan 1 kolom dan verifikasi guard minimal 1 kolom visible aktif
4. Lakukan perubahan visibilitas ceklis pada kolom Name, Code, dan Last Updated
5. Lakukan geser (drag-and-drop reorder) pada masing-masing kolom
6. Lakukan klik ikon Pin/Freeze pada salah satu kolom
7. Verifikasi live preview tabel di latar belakang merefleksikan perubahan secara langsung
8. Klik tombol '[Apply]'
9. Verifikasi modal menutup, perubahan tersimpan di local storage (kunci table_columns_gs_division), dan tabel mempertahankan pengaturan baru

## Notes

- Menguji fungsionalitas komprehensif Setup Column Modal Fase 2 per-kolom (division.md §4.2e).
