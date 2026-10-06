---
id: TC-GS-DIV-E2E-053-changelog-filter-panel-screening-dan-filter-single
title: "Screening Filter Panel Modal Changelog dan Penerapan Filter Individual"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-DIV-97
  - TC-GS-DIV-98
  - TC-GS-DIV-99
  - TC-GS-DIV-100
  - TC-GS-DIV-101
coverage:
  web: automated
---

# Screening Filter Panel Modal Changelog dan Penerapan Filter Individual

## Prerequisites

- Login sebagai Role: Total Control
- Terdapat riwayat mutasi dengan variasi tanggal, action, divisi, dan actor

## Test Steps

1. Buka Modal Changelog Division lalu klik ikon 'Filter'
2. Verifikasi Filter Panel terbuka menampilkan 5 field filter: 'Date' (Date range picker), 'Action' (multi-select), 'Division Name' (multi-select), 'Field' (multi-select), dan 'Modified By' (multi-select)
3. Pilih rentang tanggal pada filter 'Date' lalu klik '[Apply]' dan verifikasi tabel tersaring berdasarkan tanggal
4. Pilih salah satu Action (misal 'Create') lalu klik '[Apply]' dan verifikasi hanya entri Create yang tampil
5. Pilih salah satu nama pada filter 'Division Name' lalu klik '[Apply]' dan verifikasi hanya divisi terpilih yang tampil
6. Pilih salah satu nama user pada filter 'Modified By' lalu klik '[Apply]' dan verifikasi hanya entri buatan user tersebut yang tampil

## Notes

- Spesifikasi field filter changelog diatur pada division.md §4.2b.
