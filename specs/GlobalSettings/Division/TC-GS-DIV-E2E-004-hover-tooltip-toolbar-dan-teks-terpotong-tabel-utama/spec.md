---
id: TC-GS-DIV-E2E-004-hover-tooltip-toolbar-dan-teks-terpotong-tabel-utama
title: "Hover Tooltip pada Table Tools dan Nama Divisi Panjang yang Terpotong"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-DIV-200
  - TC-GS-DIV-201
coverage:
  web: automated
---

# Hover Tooltip pada Table Tools dan Nama Divisi Panjang yang Terpotong

## Prerequisites

- Mode: mock
- Login sebagai Role: Total Control
- Terdapat data divisi dengan nama panjang yang melampaui lebar kolom (truncated)

## Test Steps

1. Buka menu Global Settings > User > tab Division
2. Arahkan kursor mouse (hover) ke ikon Search pada toolbar dan verifikasi muncul tooltip 'Search'
3. Arahkan kursor mouse ke ikon Filter pada toolbar dan verifikasi muncul tooltip 'Filter'
4. Arahkan kursor mouse ke ikon Download pada toolbar dan verifikasi muncul tooltip 'Download'
5. Arahkan kursor mouse ke ikon Changelog pada toolbar dan verifikasi muncul tooltip 'Changelog'
6. Arahkan kursor mouse ke header kolom Actions (⋯) dan verifikasi muncul tooltip 'Setup Column'
7. Arahkan kursor mouse ke teks nama divisi yang mengalami pemotongan teks (ellipsis) pada baris data
8. Verifikasi muncul tooltip native/popover yang menampilkan string nama divisi lengkap tanpa terpotong

## Notes

- Hover tooltip mengikuti standar UI design system platform untuk komponen tabel (division.md §4.2a).
