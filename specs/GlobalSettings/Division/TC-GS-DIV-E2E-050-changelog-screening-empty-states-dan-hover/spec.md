---
id: TC-GS-DIV-E2E-050-changelog-screening-empty-states-dan-hover
title: "Screening Modal Changelog Division, Tampilan Empty State, dan Hover Tooltip"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-DIV-86
  - TC-GS-DIV-87
  - TC-GS-DIV-88
  - TC-GS-DIV-118
  - TC-GS-DIV-119
  - TC-GS-DIV-202
coverage:
  web: automated
---

# Screening Modal Changelog Division, Tampilan Empty State, dan Hover Tooltip

## Prerequisites

- Login sebagai Role: Total Control

## Test Steps

1. Buka menu Global Settings > User > tab Division
2. Klik ikon 'Changelog' (⏱) pada toolbar TableTools
3. Verifikasi modal dialog 'Changelog: Division' (size lg ~800px) terbuka dengan header judul, icon close '[✕]', dan tabel T-DIV-02
4. Verifikasi kolom tabel Changelog terurut: Date (sortable), Action (sortable), Division Name (sortable), Field (sortable), Old Value (sortable), New Value (sortable), Modified By (sortable), dan Actions (⋯) (unsortable, read-only)
5. Verifikasi sel pada kolom Actions (⋯) per baris berstatus kosong murni tanpa tombol aksi atau menu popover
6. Jika entitas baru belum memiliki riwayat mutasi, verifikasi muncul empty state dengan judul 'No changelog yet' dan deskripsi 'Activities and changes will appear here.'
7. Ketik keyword pencarian 'zzznotfound' di search bar Changelog dan verifikasi muncul ilustrasi 'No results found'
8. Arahkan kursor mouse ke teks nama staf pada kolom Modified By dan verifikasi muncul hover tooltip nama lengkap / email
9. Arahkan kursor ke ikon Filter dan Download pada toolbar Changelog dan verifikasi muncul tooltip masing-masing
10. Verifikasi kolom Old Value dan New Value menerapkan aturan hug content (tampil penuh / wrap natural tanpa pemotongan kaku)

## Notes

- Tabel Modal Changelog adalah tabel read-only tanpa row action (division.md §4.1 item 12 dan §4.2b).
