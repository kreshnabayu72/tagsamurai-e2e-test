---
id: TC-GS-DIV-E2E-051-changelog-search-per-kolom-dan-guard-date
title: "Pencarian Modal Changelog pada 6 Kolom Teks dan Guard Kolom Date Non-Searchable"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-DIV-89
  - TC-GS-DIV-90
  - TC-GS-DIV-91
  - TC-GS-DIV-92
  - TC-GS-DIV-93
  - TC-GS-DIV-94
  - TC-GS-DIV-95
  - TC-GS-DIV-273
coverage:
  web: automated
---

# Pencarian Modal Changelog pada 6 Kolom Teks dan Guard Kolom Date Non-Searchable

## Prerequisites

- Login sebagai Role: Total Control
- Modal Changelog terisi riwayat mutasi Create, Edit (Name dan Code), dan Delete

## Test Steps

1. Buka Modal Changelog Division
2. Ketik keyword pencarian 'Create' lalu tekan Enter dan verifikasi hasil tersaring berdasarkan kolom Action
3. Ketik nama divisi yang ada di riwayat lalu tekan Enter dan verifikasi tersaring berdasarkan kolom Division Name
4. Ketik keyword 'Code' lalu tekan Enter dan verifikasi baris dengan Field = 'Code' (hasil edit kode divisi) tampil di tabel
5. Ketik nilai lama (Old Value) dan nilai baru (New Value) lalu verifikasi pencarian bekerja akurat
6. Ketik nama pengguna pemodifikasi (Modified By) lalu verifikasi baris terkait tampil
7. Ketik format tanggal dari kolom Date lalu tekan Enter
8. Verifikasi muncul empty state 'No results found' (membuktikan kolom Date tidak searchable melalui search box)

## Notes

- Pencarian Changelog mencakup 6 kolom teks; filter tanggal diakses melalui Filter Panel (division.md §4.2b).
