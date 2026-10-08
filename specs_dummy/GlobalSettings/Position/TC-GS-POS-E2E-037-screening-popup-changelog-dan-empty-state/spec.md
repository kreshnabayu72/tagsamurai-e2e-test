---
id: TC-GS-POS-E2E-037-screening-popup-changelog-dan-empty-state
title: "Screening Popup Changelog: Position, tooltip, dismiss ✕/Esc, backdrop, hover Modified By, dan empty state"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-POS-200
  - TC-GS-POS-201
  - TC-GS-POS-202
  - TC-GS-POS-203
  - TC-GS-POS-204
  - TC-GS-POS-241
  - TC-GS-POS-292
coverage:
  web: automated
---

# Screening Popup Changelog: Position, tooltip, dismiss ✕/Esc, backdrop, hover Modified By, dan empty state

## Prerequisites

- Login sebagai Total Control
- Entitas Client Kosong (untuk empty state) dan entitas aktif dengan riwayat Position

## Test Steps

### Screening Popup Changelog & Aksesibilitas

1. Buka Global Settings > User > Position pada entitas aktif
2. Klik ikon Changelog di Table Tools
3. Verifikasi popup modal "Changelog: Position" terbuka menampilkan:
   - Header: Judul modal dan tombol close `[✕]`
   - Toolbar: Search input (placeholder "Search changelog..."), ikon Filter, ikon Download
   - Body: Kolom Date, Action, Position Name, Field, Old Value, New Value, Modified By, dan header Actions (⋯)
4. Hover toolbar dan header kolom Actions, verifikasi tooltip muncul
5. Hover sel "Modified By" pada salah satu baris riwayat, verifikasi tooltip nama lengkap aktor muncul

### Dismiss & Backdrop Guard

6. Klik area backdrop di luar modal Changelog
7. Verifikasi modal Changelog tidak tertutup (NC-14)
8. Tekan tombol Esc pada keyboard, verifikasi modal tertutup
9. Buka kembali Changelog lalu klik tombol `[✕]`, verifikasi modal tertutup

### Empty State Changelog

10. Buka tab Position pada entitas "Client Kosong" (belum pernah ada riwayat)
11. Buka Popup Changelog
12. Verifikasi tabel menampilkan empty state: "No changelog yet"

## Notes

- Menggabungkan TC-GS-POS-200, 201, 202, 203, 204, 241, dan 292.
