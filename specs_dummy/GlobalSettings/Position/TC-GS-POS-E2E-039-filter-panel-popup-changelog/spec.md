---
id: TC-GS-POS-E2E-039-filter-panel-popup-changelog
title: "Filter Panel Changelog: Date, multi-select (Action, Name, Modified By), chip sync, loading, dan logika AND/OR"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-POS-211
  - TC-GS-POS-212
  - TC-GS-POS-213
  - TC-GS-POS-214
  - TC-GS-POS-215
  - TC-GS-POS-216
  - TC-GS-POS-217
  - TC-GS-POS-218
  - TC-GS-POS-219
  - TC-GS-POS-220
  - TC-GS-POS-288
  - TC-GS-POS-289
  - TC-GS-POS-290
coverage:
  web: automated
---

# Filter Panel Changelog: Date, multi-select (Action, Name, Modified By), chip sync, loading, dan logika AND/OR

## Prerequisites

- Login sebagai Total Control
- Popup Changelog terbuka

## Test Steps

### Screening Filter Panel & Multi-Select Dropdown

1. Klik ikon Filter pada toolbar Popup Changelog
2. Verifikasi Filter Panel terbuka menampilkan kontrol filter: Date, Action, Position Name, dan Modified By
3. Buka dropdown Action, centang opsi "Create" dan "Edit"
4. Verifikasi logika OR berlaku untuk opsi di dalam dropdown yang sama (menampilkan riwayat Create atau Edit)
5. Verifikasi chip filter muncul di Filter Panel

### Sinkronisasi Chip Filter

6. Klik ikon `[✕]` pada salah satu chip filter Action
7. Verifikasi centang pada dropdown Action otomatis terhapus
8. Buka dropdown Position Name, ketik nama jabatan di input cari internal dropdown
9. Centang opsi jabatan tersebut, verifikasi chip ditambahkan

### Logika AND Antar Field Filter & Filter Date

10. Pilih rentang tanggal pada filter Date
11. Klik tombol "[Apply]"
12. Verifikasi sistem menerapkan logika AND (tanggal cocok DAN Action cocok DAN Position cocok)
13. Buka kembali Filter Panel, klik "[Clear Field]", verifikasi seluruh filter terhapus dan data kembali penuh

## Notes

- Menggabungkan seluruh skenario filter popup changelog dari TC-GS-POS-211 s.d. 220, 288, 289, dan 290.
