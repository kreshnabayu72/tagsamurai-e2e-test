---
id: TC-GS-DIV-E2E-045-tabel-utama-setup-column-fase-1-overlay-quick-panel
title: "Setup Column Fase 1: Screening Overlay, Toggle Kolom Hideable, dan Drag Reorder"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-DIV-72
  - TC-GS-DIV-73
  - TC-GS-DIV-74
coverage:
  web: automated
---

# Setup Column Fase 1: Screening Overlay, Toggle Kolom Hideable, dan Drag Reorder

## Prerequisites

- Mode: mock
- Login sebagai Role: Total Control

## Test Steps

1. Buka menu Global Settings > User > tab Division
2. Klik header kolom Actions (⋯)
3. Verifikasi Setup Column Quick Panel / Overlay terbuka menampilkan daftar kolom: Name, Code, dan Last Updated
4. Verifikasi seluruh kolom data berstatus Hideable (tidak ada kolom Locked)
5. Hapus centang (uncheck) pada kolom 'Code'
6. Verifikasi kolom 'Code' seketika menghilang dari tampilan tabel utama
7. Hapus centang pada kolom 'Last Updated'
8. Verifikasi checkbox kolom terakhir 'Name' menjadi disabled dengan tooltip 'Minimal 1 kolom visible tersisa'
9. Lakukan drag-and-drop untuk menukar posisi urutan kolom
10. Verifikasi urutan kolom pada tabel utama langsung mengikuti susunan baru

## Notes

- Mengikuti aturan Setup Column Fase 1 dan model Hideable-only tanpa kolom Locked (prd-conventions.md §9.3).
