---
id: TC-GS-GSET-E2E-026-changelog-download-overlay-csv-xlsx-filter-dan-unhide
title: "Download Changelog: overlay CSV/XLSX, cakupan seluruh baris, mengikuti Search/kolom, format tanggal, dan kolom ter-unhide ikut ter-export"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-GSET-97
  - TC-GS-GSET-98
  - TC-GS-GSET-99
  - TC-GS-GSET-100
  - TC-GS-GSET-159
coverage:
  web: automated
---

# Download Changelog: overlay CSV/XLSX, cakupan seluruh baris, mengikuti Search/kolom, format tanggal, dan kolom ter-unhide ikut ter-export

## Prerequisites

- Login sebagai Role: Total Control
- Changelog General Settings berisi baris riwayat (dinamis); untuk blok cakupan seluruh baris, Changelog berisi ≥11 baris
- Date Format dan Time Format tersimpan: `dd/MM/yy` dan `HH:mm`

## Test Steps

### Overlay Download

1. Buka Modal Changelog, klik Download di toolbar
2. Verifikasi overlay memuat dua pilihan: `Download as CSV` dan `Download as XLSX`

### Download CSV Seluruh Baris

3. Klik Download, pilih `Download as CSV`
4. Verifikasi file terunduh bernama `Changelog-General-Settings.csv`
5. Verifikasi tidak ada toast sukses
6. Buka file dan verifikasi memuat seluruh baris riwayat (lebih dari 10 baris halaman aktif)
7. Verifikasi kolom Date memakai Date Format dan Time Format yang tersimpan saat Download

### Download XLSX

8. Klik Download, pilih `Download as XLSX`
9. Verifikasi file terunduh bernama `Changelog-General-Settings.xlsx` dan tidak ada toast sukses

### Mengikuti Search dan Kolom Tampil

10. Search "Session Idle" lalu `Enter`
11. Buka Setup Column via header Actions (⋯) > `Setup Column...`, uncheck kolom Modified By, klik `[Save]`
12. Klik Download, pilih `Download as CSV`
13. Verifikasi file hanya memuat baris yang cocok dengan Search dan tanpa kolom Modified By

### Kolom Ter-unhide Ikut Ter-export

14. Buka Setup Column, uncheck kolom Modified By, klik `[Save]`
15. Buka Setup Column, check kolom Modified By, klik `[Save]`
16. Klik Download, pilih `Download as CSV`, lalu buka file
17. Verifikasi file memuat kolom Modified By (kolom yang sudah di-unhide kembali ikut ter-export)

## Notes

- Menggabungkan TC-GS-GSET-97, 98, 99, 100, dan 159 (Download Changelog).
