---
id: TC-GS-DIV-E2E-058-tabel-utama-setup-column-modal-fase-2
title: "Setup Column Tabel Utama Fase 2: Modal Dialog Setup Column, Pencarian Kolom, Drag-and-Drop Reorder, dan Pin/Unpin Kolom"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-DIV-170
  - TC-GS-DIV-171
  - TC-GS-DIV-172
  - TC-GS-DIV-173
  - TC-GS-DIV-174
coverage:
  web: automated
---

# Setup Column Tabel Utama Fase 2: Modal Dialog Setup Column, Pencarian Kolom, Drag-and-Drop Reorder, dan Pin/Unpin Kolom

## Prerequisites

- Mode: mock
- Login sebagai Role: Total Control
- Buka Modal Setup Column via CTA "Setup Column..." di panel overlay
- User berada di Global Settings > User > Division
- Tabel Division terisi 32 baris (TC-GS-DIV-30)

## Test Steps

### Muat ulang halaman (F5) mempertahankan Search, Sort, Filter, dan halaman (TC-GS-DIV-170)

1. Cari `a` lalu Enter
2. Klik header Name sampai descending
3. Pindah ke halaman 2
4. Tekan F5
5. Verifikasi Setelah F5 keyword `a`, sort Name descending, dan halaman 2 tetap seperti sebelum refresh

### Screening Overlay Column Visibility tabel Division (TC-GS-DIV-171)

6. Klik header kolom Column Visibility (⋯)
7. Verifikasi Overlay tampil tanpa backdrop
8. Verifikasi Daftar kolom berurutan: `Name`, `Code`, `Last Updated`, masing-masing tercentang (Hideable checked dan enabled) dengan drag handle
9. Verifikasi Item `Setup Column...` di bagian bawah

### Screening Popup Setup Column tabel Division (TC-GS-DIV-172)

10. Klik header Column Visibility (⋯)
11. Klik `[Setup Column]`
12. Verifikasi Title `Setup Column`
13. Verifikasi Subtitle `Manage column visibility, reorder, and freeze columns.`
14. Verifikasi Icon close `[✕]`
15. Verifikasi Search input `Search column name...`
16. Verifikasi Daftar kolom `Name`, `Code`, `Last Updated` masing-masing tercentang dengan drag handle `⠿` dan icon pin
17. Verifikasi Preview tabel merefleksikan susunan kolom
18. Verifikasi Tombol `[Reset to Default]` (text, primary) dan `[Save]` (filled, success)

### Setup Column: hide dan unhide tiap kolom lewat popup lalu Save (TC-GS-DIV-173)

19. Buka Popup Setup Column
20. Hilangkan centang `Name` (kolom lain tetap tercentang), klik `[Save]`, lihat tabel, lalu buka kembali popup dan centang kembali `Name`
21. Hilangkan centang `Code` (kolom lain tetap tercentang), klik `[Save]`, lihat tabel, lalu buka kembali popup dan centang kembali `Code`
22. Hilangkan centang `Last Updated` (kolom lain tetap tercentang), klik `[Save]`, lihat tabel, lalu buka kembali popup dan centang kembali `Last Updated`
23. Setelah kolom terakhir diuji, muat ulang halaman (F5)
24. Verifikasi Name: setelah Save kolom `Name` tidak tampil di tabel dan tampil kembali setelah dicentang ulang dan di-Save
25. Verifikasi Code: setelah Save kolom `Code` tidak tampil di tabel dan tampil kembali setelah dicentang ulang dan di-Save
26. Verifikasi Last Updated: setelah Save kolom `Last Updated` tidak tampil di tabel dan tampil kembali setelah dicentang ulang dan di-Save
27. Verifikasi Setelah F5 konfigurasi terakhir tetap tersimpan

### Setup Column: reorder tiap kolom lewat drag lalu Save (TC-GS-DIV-174)

28. Buka Popup Setup Column
29. Seret `Name` ke posisi pertama, klik `[Save]`, lihat tabel
30. Seret `Code` ke posisi pertama, klik `[Save]`, lihat tabel
31. Seret `Last Updated` ke posisi pertama, klik `[Save]`, lihat tabel
32. Verifikasi Name: setelah Save kolom `Name` berada di posisi pertama tabel
33. Verifikasi Code: setelah Save kolom `Code` berada di posisi pertama tabel
34. Verifikasi Last Updated: setelah Save kolom `Last Updated` berada di posisi pertama tabel
35. Verifikasi Setelah F5 urutan terakhir tetap tersimpan

## Notes

- Memvalidasi Fase 2 Setup Column: modal size sm, pencarian field kolom, interaksi drag handle [⠿] untuk mengubah urutan kolom, dan fitur pin/unpin kolom (PRD §4.2e).
- Sumber pemetaan test case granular: TC-GS-DIV-170, TC-GS-DIV-171, TC-GS-DIV-172, TC-GS-DIV-173, TC-GS-DIV-174.
