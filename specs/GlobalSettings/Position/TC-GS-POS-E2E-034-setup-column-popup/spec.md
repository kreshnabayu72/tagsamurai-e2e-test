---
id: TC-GS-POS-E2E-034-setup-column-popup
title: Popup Setup Column — Screening, Ceklis/Geser/Pin, Reset to Default, Cancel/X, Persist
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-POS-120
  - TC-GS-POS-133
  - TC-GS-POS-134
  - TC-GS-POS-135
  - TC-GS-POS-136
  - TC-GS-POS-137
  - TC-GS-POS-130
  - TC-GS-POS-176
  - TC-GS-POS-121
coverage:
  web: automated
---

# Popup Setup Column — Screening, Ceklis/Geser/Pin, Reset to Default, Cancel/X, Persist

## Prerequisites

- Aktor `Fixture.globalSettingsPosition.actors.totalControl`.
- Tabel terisi data.
- Kolom default: Name, Last Updated (keduanya Hideable).
- Popup Setup Column tersedia via `[Setup Column]` di Overlay Column Visibility.

## Test Steps

### A. Screening Popup Setup Column & Preview

1. Klik header kolom Actions `(⋯)` → klik `[Setup Column]`.
2. Verifikasi header popup: title `"Setup Column"`, info `"Drag and drop to reorder columns, check/uncheck to show/hide, or pin columns."`, tombol Close `(X)`.
3. Verifikasi section daftar kolom & status, section live preview table, footer `[Cancel]` `[Save]` `[Reset to Default]`.
4. Tutup popup via `(X)` atau Cancel.

### B. Name — Ceklis/Unceklis & Persist

5. Buka Popup Setup Column.
6. Uncheck `Name`, amati preview & efek.
7. Klik `[Save]`, verifikasi popup tertutup & kolom `Name` hilang dari tabel.
8. Refresh (F5), verifikasi persist.
9. Buka kembali Setup Column, centang `Name`, Save, verifikasi muncul kembali.

### C. Last Updated — Ceklis/Unceklis & Persist

10. Buka Popup Setup Column.
11. Uncheck `Last Updated`, amati live preview.
12. Klik `[Save]`, verifikasi kolom `Last Updated` hilang dari tabel.
13. Refresh (F5), verifikasi persist.
14. Centang kembali & Save.

### D. Reorder di Popup

15. Buka Popup Setup Column.
16. Drag baris `Name` ke bawah `Last Updated` di daftar kolom.
17. Verifikasi header preview & tabel utama mengikuti urutan baru (`Last Updated` → `Name`).
18. Klik `[Save]`, refresh (F5), verifikasi urutan persist.
19. Kembalikan urutan default (`Name` → `Last Updated`).

### E. Geser Last Updated ke atas Name — ditolak (edge case)

20. Buka Popup Setup Column.
21. Coba drag baris `Last Updated` ke atas `Name`.
22. Verifikasi pergeseran ke atas ditolak; preview & tabel tetap `Name` → `Last Updated`.
23. Klik `[Save]`, refresh (F5), verifikasi tetap konsisten.

### F. Pin kolom di Popup

24. Buka Popup Setup Column.
25. Klik icon Pin pada baris `Name`.
26. Verifikasi indikator Pin aktif.
27. Klik `[Save]`.
28. Scroll tabel utama secara horizontal (viewport sempit).
29. Verifikasi kolom `Name` membeku (sticky freeze) di kiri saat scroll horizontal.
30. Refresh (F5), verifikasi status Pin `Name` tetap bertahan.
31. Ulangi untuk `Last Updated` (Pin/Unpin) sesuai TC-121 untuk memastikan kedua kolom dapat di-pin & persist.
32. Unpin kembali jika perlu.

### G. Reset to Default

33. Ubah konfigurasi (sembunyikan/ubah urutan/pin) agar berbeda dari default.
34. Buka Popup Setup Column.
35. Klik `[Reset to Default]`.
36. Verifikasi preview kembali ke susunan awal (`Name` & `Last Updated` checked, urutan default, unpinned).
37. Klik `[Save]`.
38. Refresh (F5), verifikasi tabel kembali ke layout default dan tersimpan.

### H. Cancel & X — discard changes

39. Ubah konfigurasi di dalam popup (mis. uncheck `Last Updated`), amati preview berubah.
40. Klik `[Cancel]` (atau `(X)` kanan atas).
41. Verifikasi popup tertutup seketika.
42. Verifikasi seluruh perubahan di-discard, tabel utama tetap seperti sebelum buka popup.
43. Refresh (F5), verifikasi konfigurasi tersimpan tidak berubah.

## Notes

- Live preview membuktikan sinkronisasi saat edit sebelum Save.
- Cancel/X wajib discard; Save wajib persist (localStorage).
- Guard minimal 1 kolom tetap berlaku (jika hanya 1 visible, checkbox disabled).
