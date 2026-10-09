---
id: TC-GS-GSET-E2E-009-mobile-layout-bottom-sheet-tooltip-dan-dialog
title: "Mobile: layout satu kolom, bottom sheet, sticky footer, tooltip ketuk, dan dialog"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-GSET-19
  - TC-GS-GSET-20
  - TC-GS-GSET-21
  - TC-GS-GSET-148
  - TC-GS-GSET-149
coverage:
  web: unsupported
---

# Mobile: layout satu kolom, bottom sheet, sticky footer, tooltip ketuk, dan dialog

## Prerequisites

- Aplikasi TAG Samurai Mobile (Android) dengan backend dan data entitas yang sama
- Login sebagai Role: Total Control; satu blok memakai Role: Read Only
- Record General Settings entitas tersimpan: Currency Code `IDR`, Date Format `dd/MM/yy`, Time Format `HH:mm`, Time Zone `Asia/Jakarta`, Session Idle Timeout `30 minutes`
- Changelog berisi baris riwayat
- `[simbol opsi USD]` = simbol yang tampil pada label opsi untuk kode USD

## Test Steps

### Layout Satu Kolom, Bottom Sheet, dan Sticky Footer

1. Login sebagai Total Control di aplikasi TAG Samurai Mobile, buka Global Settings > General Settings
2. Verifikasi field tersusun satu kolom penuh lebar dalam SectionCard terpisah dengan urutan: Currency Code, Preview Currency, Date Format, Time Format, Time Zone, Preview Date & Time, Session Idle Timeout
3. Ketuk Select "Currency Code", "Time Zone", "Session Idle Timeout", "Date Format", "Time Format" satu per satu
4. Verifikasi kelima Select membuka bottom sheet selector
5. Ketuk Select "Currency Code" lalu pilih `USD`
6. Verifikasi Preview Currency tampil tepat di bawah field Currency Code dan berubah menjadi "[simbol opsi USD] 5.000,00"
7. Verifikasi tombol "Save" berada di sticky footer, icon Changelog tetap terlihat di header, dan tidak ada tombol Cancel

### Tooltip Ketuk dan Read Only

8. Login sebagai Read Only, buka Global Settings > General Settings
9. Ketuk ikon info label "Currency Code"
10. Verifikasi tooltip tampil persis "Currency used to display amounts across all products. Changing it does not convert existing amounts."
11. Ketuk Select "Session Idle Timeout" yang disabled
12. Verifikasi Select disabled menampilkan tooltip "You don't have permission to edit"
13. Verifikasi tombol "Save" Hidden

### Modal sebagai Bottom Sheet

14. Login sebagai Total Control, buka Global Settings > General Settings
15. Ketuk icon Changelog di header
16. Verifikasi Modal Changelog: General Settings tampil sebagai full-height bottom sheet
17. Ketuk header kolom Actions (⋯) lalu item `Setup Column...`
18. Verifikasi Modal Setup Column tampil sebagai full-height bottom sheet

### Dialog Unsaved Changes dan Change Currency

19. Tutup modal, ketuk Select "Session Idle Timeout" lalu pilih `1 hour` pada bottom sheet
20. Ketuk tombol Back
21. Verifikasi dialog muncul: "You have unsaved changes. Are you sure you want to leave?" dengan tombol `[Cancel]` dan `[Leave]`
22. Ketuk `[Cancel]`
23. Verifikasi dialog tertutup, tetap di General Settings dengan Session Idle Timeout `1 hour`
24. Ketuk tombol Back lagi lalu ketuk `[Leave]`
25. Verifikasi keluar dari halaman tanpa menyimpan; setelah dibuka kembali Session Idle Timeout `30 minutes`
26. Ketuk Select "Currency Code" lalu pilih `USD`, ketuk `[Save]`
27. Verifikasi dialog "Change Currency" tampil dengan copy dan perilaku desktop
28. Ketuk `[Cancel]`
29. Verifikasi dialog tertutup dan form tetap unsaved dengan Currency Code `USD`
30. Ketuk `[Save]` lagi lalu ketuk `[Change Currency]`
31. Verifikasi toast sukses "Success, general settings has been saved."

## Notes

- Target platform mobile (Android); `coverage.web: unsupported` sehingga tidak dijalankan di runner web. Menggabungkan TC-GS-GSET-19, TC-GS-GSET-20, TC-GS-GSET-21, TC-GS-GSET-148, dan TC-GS-GSET-149.
