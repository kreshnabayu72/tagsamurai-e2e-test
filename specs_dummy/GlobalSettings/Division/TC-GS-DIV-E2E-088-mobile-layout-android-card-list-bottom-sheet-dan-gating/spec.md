---
id: TC-GS-DIV-E2E-088-mobile-layout-android-card-list-bottom-sheet-dan-gating
title: "Tampilan dan Interaksi Mobile Android: Card List Pengganti Tabel, Tanpa Checkbox/Bulk, Bottom Sheet Toolbar/Dialog, dan Gating Aksi"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-DIV-281
  - TC-GS-DIV-282
  - TC-GS-DIV-283
  - TC-GS-DIV-284
coverage:
  web: automated
---

# Tampilan dan Interaksi Mobile Android: Card List Pengganti Tabel, Tanpa Checkbox/Bulk, Bottom Sheet Toolbar/Dialog, dan Gating Aksi

## Prerequisites

- Mode: mock
- Login sebagai Role: Total Control dan Read Only
- Mode: mock (viewport emulasi Android <768px)
- Aplikasi TAG Samurai Mobile (Android)
- Aplikasi TAG Samurai Mobile (Android) terbuka sebagai Total Control

## Test Steps

### Screening halaman Division pada aplikasi mobile (TC-GS-DIV-281)

1. Buka Global Settings > User > Division
2. Verifikasi Breadcrumb `User > Division`
3. Verifikasi Sub-Tabs Bar horizontal scrollable: `User List | Position | Division (aktif) | Custom Field`
4. Verifikasi Mobile Toolbar: icon `[⋯]` (bottom sheet) dan `[🔍]` (inline search)
5. Verifikasi Tombol `[+ Division]` tetap terlihat di bawah toolbar dan di atas card list
6. Verifikasi Division Card List: tiap card menampilkan Name (tebal), `[⋯]`, lalu `Code · Last Updated` (tanggal mengikuti General Settings)

### Card list mobile tanpa checkbox dan tanpa bulk action (TC-GS-DIV-282)

7. Buka Tab Division
8. Perhatikan card list
9. Verifikasi Tidak ada checkbox seleksi pada card
10. Verifikasi Tidak ada Bulk Action Bar

### Row action card mobile mengikuti gating capability, [⋯] tidak tampil bila semua Hidden (TC-GS-DIV-283)

11. Login sbg Total Control: buka `[⋯]` pada card
12. Login sbg Read Only: perhatikan card
13. Verifikasi Total Control: `[⋯]` memuat `Edit` dan `Delete`
14. Verifikasi Read Only: `Edit` dan `Delete` Hidden sehingga `[⋯]` tidak tampil pada card

### Toolbar, Filter, dan dialog mobile tampil sebagai bottom sheet (TC-GS-DIV-284)

15. Ketuk `[⋯]` pada toolbar
16. Ketuk `Filter`
17. Ketuk `[+ Division]`
18. Verifikasi Bottom sheet `[⋯]` memuat Column Visibility, Filter, Download, dan Changelog
19. Verifikasi Filter Panel tampil sebagai bottom sheet
20. Verifikasi Form Create Division tampil sebagai bottom sheet

## Notes

- Memvalidasi transformasi layout mobile Android: tabel menjadi card list, tanpa checkbox dan tanpa bulk action bar, toolbar/filter/dialog beralih ke bottom sheet, dan menu aksi baris [⋯] mengikuti gating capability (PRD §4.6, prd-conventions.md §13, §39).
- Sumber pemetaan test case granular: TC-GS-DIV-281, TC-GS-DIV-282, TC-GS-DIV-283, TC-GS-DIV-284.
