---
id: TC-GS-POS-E2E-033-overlay-column-visibility-tabel-utama
title: "Overlay Column Visibility tabel utama: uncheck instant, drag reorder, dan guard kolom terakhir"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-POS-177
  - TC-GS-POS-178
  - TC-GS-POS-179
  - TC-GS-POS-180
coverage:
  web: automated
---

# Overlay Column Visibility tabel utama: uncheck instant, drag reorder, dan guard kolom terakhir

## Prerequisites

- Login sebagai Total Control
- Tabel Position tampil di layar

## Test Steps

### Buka Overlay Column Visibility

1. Klik ikon titik tiga (⋯) pada header kolom paling kanan tabel
2. Verifikasi popover Overlay Column Visibility terbuka menampilkan daftar kolom: "Name" dan "Last Updated", masing-masing dengan checkbox dan drag handle

### Uncheck Instant & Reorder

3. Hapus centang (uncheck) pada checkbox "Last Updated"
4. Verifikasi kolom "Last Updated" langsung menghilang seketika dari tabel tanpa perlu menekan tombol simpan
5. Centang kembali "Last Updated"
6. Lakukan drag handle pada kolom "Last Updated" ke atas kolom "Name"
7. Verifikasi urutan kolom di tabel langsung bertukar tempat secara instan

### Guard Kolom Terakhir (Last Visible Column)

8. Uncheck kolom "Last Updated" sehingga hanya kolom "Name" yang tampil
9. Coba uncheck checkbox kolom "Name"
10. Verifikasi checkbox kolom "Name" berada dalam kondisi disabled (tidak dapat di-uncheck) karena minimal satu kolom data wajib tampil di tabel

## Notes

- Menggabungkan TC-GS-POS-177 s.d. 180.
