---
id: TC-GS-DIV-E2E-058-changelog-setup-column-fase-1-overlay-quick-panel
title: "Setup Column Modal Changelog Fase 1: Screening Overlay dan Drag Reorder"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-DIV-120
  - TC-GS-DIV-121
  - TC-GS-DIV-122
coverage:
  web: automated
---

# Setup Column Modal Changelog Fase 1: Screening Overlay dan Drag Reorder

## Prerequisites

- Mode: mock
- Login sebagai Role: Total Control

## Test Steps

1. Buka Modal Changelog Division
2. Klik header kolom Actions (⋯) pada tabel Changelog
3. Verifikasi Setup Column Quick Overlay terbuka menampilkan seluruh 7 kolom data Changelog berstatus Hideable
4. Hapus centang pada salah satu kolom (misal 'Field') dan verifikasi kolom seketika tersembunyi dari tabel
5. Lakukan drag-and-drop untuk menukar posisi kolom
6. Verifikasi urutan kolom tabel Changelog langsung berubah secara visual

## Notes

- Memvalidasi interaksi cepat Setup Column pada modal changelog (division.md §4.2b).
