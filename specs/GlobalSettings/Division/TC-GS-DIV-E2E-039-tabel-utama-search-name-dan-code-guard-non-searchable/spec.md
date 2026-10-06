---
id: TC-GS-DIV-E2E-039-tabel-utama-search-name-dan-code-guard-non-searchable
title: "Pencarian Tabel Utama Berdasarkan Name dan Code serta Guard Kolom Tanggal"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-DIV-54
  - TC-GS-DIV-55
  - TC-GS-DIV-56
  - TC-GS-DIV-268
coverage:
  web: automated
---

# Pencarian Tabel Utama Berdasarkan Name dan Code serta Guard Kolom Tanggal

## Prerequisites

- Login sebagai Role: Total Control
- Terdapat divisi dengan variasi Name dan Code (misal: 'Human Resources' dengan Code 'HR')

## Test Steps

1. Buka menu Global Settings > User > tab Division
2. Klik ikon Search pada toolbar TableTools
3. Ketik substring nama 'human' (huruf kecil) lalu tekan Enter
4. Verifikasi tabel tersaring hanya menampilkan baris yang mengandung 'Human' (pencarian substring case-insensitive)
5. Ketik keyword kode 'hr' lalu tekan Enter
6. Verifikasi tabel menampilkan baris dengan Code 'HR'
7. Ketik keyword berupa format tanggal '2026' atau bulan dari kolom Last Updated lalu tekan Enter
8. Verifikasi tabel menampilkan empty state 'No results found' (membuktikan kolom Last Updated tidak ikut tersaring di search box utama)

## Notes

- Kolom yang dapat dicari di tabel utama adalah Name dan Code; Last Updated bukan kolom searchable (division.md §4.2a).
