---
id: TC-GS-DIV-E2E-005-hover-tooltip-toolbar-table-tools
title: "Hover Tooltip Icon Toolbar Table Tools (Search, Filter, Download, Changelog)"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-DIV-2
coverage:
  web: automated
---

# Hover Tooltip Icon Toolbar Table Tools (Search, Filter, Download, Changelog)

## Prerequisites

- Mode: mock
- Login sebagai Role: Total Control
- Tabel Division terisi data
- User berada di Global Settings > User > Division

## Test Steps

1. Hover icon Search
2. Hover icon Filter
3. Hover icon Download
4. Hover icon Changelog
5. Verifikasi Hover icon Search menampilkan tooltip `Search`
6. Verifikasi Hover icon Filter menampilkan tooltip `Filter`
7. Verifikasi Hover icon Download menampilkan tooltip `Download`
8. Verifikasi Hover icon Changelog menampilkan tooltip `Changelog`

## Notes

- Memvalidasi kemunculan tooltip teks kanonikal saat kursor melayang di atas icon toolbar Table Tools: "Search", "Filter", "Download", dan "Changelog" (PRD §4.2, prd-conventions.md §9.1).
- Sumber pemetaan test case granular: TC-GS-DIV-2.
