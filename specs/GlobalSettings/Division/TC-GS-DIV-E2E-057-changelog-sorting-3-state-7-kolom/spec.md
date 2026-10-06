---
id: TC-GS-DIV-E2E-057-changelog-sorting-3-state-7-kolom
title: "Sorting 3-State untuk 7 Kolom Modal Changelog (Date Default Newest First)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-DIV-111
  - TC-GS-DIV-112
  - TC-GS-DIV-113
  - TC-GS-DIV-114
  - TC-GS-DIV-115
  - TC-GS-DIV-116
  - TC-GS-DIV-117
coverage:
  web: automated
---

# Sorting 3-State untuk 7 Kolom Modal Changelog (Date Default Newest First)

## Prerequisites

- Login sebagai Role: Total Control
- Tabel Changelog terisi data mutasi bervariasi

## Test Steps

1. Buka Modal Changelog Division
2. Verifikasi default sort tabel Changelog adalah kolom 'Date' Descending (Newest First)
3. Klik header kolom 'Date' untuk beralih ke Oldest First lalu klik kembali untuk reset
4. Klik header kolom 'Action' 1x (A-Z), 2x (Z-A), dan 3x (kembali ke default sort)
5. Lakukan pengujian siklus sort 3-state berturut-turut pada kolom: 'Division Name', 'Field', 'Old Value', 'New Value', dan 'Modified By'
6. Verifikasi pada kolom Old Value dan New Value, nilai kosong ('—') selalu ditempatkan di urutan akhir saat sort Ascending
7. Verifikasi seluruh transisi sorting 7 kolom berjalan mulus tanpa error

## Notes

- Default sort Newest First pada event stream mengikuti aturan pengecualian prd-conventions.md §9.10.
