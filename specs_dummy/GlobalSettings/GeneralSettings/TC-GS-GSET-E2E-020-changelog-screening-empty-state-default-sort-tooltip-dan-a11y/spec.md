---
id: TC-GS-GSET-E2E-020-changelog-screening-empty-state-default-sort-tooltip-dan-a11y
title: "Modal Changelog: screening, akses Read Only, empty state, urutan default, tooltip, backdrop, dan focus trap"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-GSET-60
  - TC-GS-GSET-61
  - TC-GS-GSET-63
  - TC-GS-GSET-65
  - TC-GS-GSET-85
  - TC-GS-GSET-86
  - TC-GS-GSET-96
coverage:
  web: automated
---

# Modal Changelog: screening, akses Read Only, empty state, urutan default, tooltip, backdrop, dan focus trap

## Prerequisites

- Login sebagai Role: Total Control
- Changelog General Settings berisi baris riwayat (dinamis) dengan Modified By berformat `Budi S`
- Entitas `Client Baru` tanpa Save General Settings untuk blok empty state

## Test Steps

### Screening Modal

1. Buka Global Settings > General Settings lalu klik icon Changelog di pojok kanan atas halaman
2. Verifikasi Header: Title "Changelog: General Settings"; Toolbar Search (placeholder "Search action, field, or value...") | Filter | Download; klik backdrop tidak menutup modal
3. Verifikasi Body tabel berkolom Date (sortable) | Action (sortable) | Field (sortable) | Old Value (sortable) | New Value (sortable) | Modified By (sortable) | Actions (⋯), urutan default Date descending (Newest First), dan Modified By berformat `[first name lengkap] [huruf pertama last name]` (`Budi S`)
4. Verifikasi Footer: Pagination default 10 baris per halaman

### Akses Read Only

5. Ganti login sebagai Role Read Only, buka Global Settings > General Settings, lalu klik icon Changelog
6. Verifikasi modal terbuka dengan Toolbar Search, Filter, dan Download masing-masing enabled, tabel enam kolom data, dan Pagination

### Empty State

7. Login sebagai staff `Client Baru`, buka Global Settings > General Settings, lalu klik icon Changelog
8. Verifikasi empty state: ilustrasi, title "No changelog yet", description "Activities and changes will appear here."

### Urutan Default

9. Kembali sebagai Total Control dengan data riwayat, buka Modal Changelog, dan amati urutan baris
10. Verifikasi baris terurut Date descending (Newest First): entri terbaru di atas

### Tooltip dan Backdrop

11. Hover icon Changelog di pojok kanan atas halaman
12. Verifikasi tooltip "Changelog"
13. Buka Modal Changelog, hover ikon Search, Filter, dan Download di toolbar
14. Verifikasi tooltip masing-masing "Search", "Filter", "Download"
15. Klik area backdrop di luar modal
16. Verifikasi Modal Changelog tetap terbuka

### Accessibility Focus Trap dan Esc

17. Tekan `Tab` berulang melewati seluruh elemen modal
18. Verifikasi fokus keyboard tetap berada di dalam modal (focus trapped)
19. Tekan `Esc`
20. Verifikasi modal tertutup dan fokus kembali ke halaman General Settings

## Notes

- Menggabungkan TC-GS-GSET-60, 61, 63, 65, 85, 86, dan 96 (screening, akses, empty state, urutan default, tooltip, backdrop, a11y).
