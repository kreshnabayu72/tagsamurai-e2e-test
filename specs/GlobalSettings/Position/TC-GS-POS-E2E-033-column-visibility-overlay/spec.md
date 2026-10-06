---
id: TC-GS-POS-E2E-033-column-visibility-overlay
title: Overlay Column Visibility — Struktur, Hideable, Guard Minimal 1 Kolom, Drag, Persist
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-POS-68
  - TC-GS-POS-117
  - TC-GS-POS-118
  - TC-GS-POS-131
  - TC-GS-POS-132
coverage:
  web: automated
---

# Overlay Column Visibility — Struktur, Hideable, Guard Minimal 1 Kolom, Drag, Persist

## Prerequisites

- Aktor `Fixture.globalSettingsPosition.actors.totalControl`.
- Tabel terisi data.
- Kolom default: Name (posisi 1), Last Updated (posisi 2). Keduanya Hideable.

## Test Steps

### A. Screening Overlay Column Visibility

1. Klik header kolom Actions `(⋯)` → buka Overlay Column Visibility.
2. Verifikasi tombol `[Setup Column]` tampil di bagian atas overlay.
3. Verifikasi daftar kolom & status checkbox default:
   - Name (posisi 1): ☑ Hideable — checkbox checked & enabled, drag handle aktif
   - Last Updated (posisi 2): ☑ Hideable — checkbox checked & enabled, drag handle aktif
4. Tutup overlay.

### B. Last Updated — Ceklis/Unceklis (persist)

5. Buka Overlay Column Visibility.
6. Uncheck `Last Updated`.
7. Verifikasi kolom `Last Updated` langsung hilang dari tabel (tanpa reload).
8. Refresh browser (F5).
9. Verifikasi kolom `Last Updated` tetap tersembunyi setelah refresh.
10. Buka overlay kembali, centang `Last Updated`.
11. Verifikasi kolom `Last Updated` muncul kembali.
12. Refresh (F5), verifikasi tetap muncul.

### C. Name — Guard minimal 1 kolom visible

13. Buka Overlay Column Visibility. Sembunyikan `Last Updated` hingga hanya `Name` yang visible (jika belum).
14. Amati checkbox baris `Name`.
15. Coba uncheck checkbox `Name` (satu-satunya kolom visible tersisa).
16. Verifikasi checkbox `Name` disabled, tidak dapat di-uncheck + tooltip `"At least one column must remain visible."`.

### D. Drag reorder di Overlay

17. Kembalikan kondisi default (kedua kolom visible).
18. Buka Overlay Column Visibility.
19. Drag baris `Name` ke bawah `Last Updated`.
20. Verifikasi urutan kolom berubah (Last Updated di posisi pertama) dan tabel utama mengikuti urutan baru.
21. Buka kembali overlay, drag baris `Last Updated` ke atas `Name` (atau kembali ke urutan semula).
22. Verifikasi pergeseran berhasil dan tabel mengikuti.

### E. Persist urutan & visibilitas

23. Lakukan perubahan urutan/visibilitas, lalu logout/login.
24. Buka halaman Position, verifikasi konfigurasi Column Visibility & urutan tetap utuh.

## Notes

- B menegaskan perubahan langsung (seketika) dan persist setelah refresh.
- C menerapkan guard generik minimal 1 kolom visible (sesuai §9.3).
- D menguji drag handle aktif dan sinkronisasi tabel↔overlay.
