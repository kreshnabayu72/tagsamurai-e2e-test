---
id: TC-GS-GSET-E2E-025-changelog-setup-column-panel-modal-pin-hide-reorder-reset-dan-discard
title: "Setup Column Changelog: panel Column Visibility, modal screening, Pin/Unpin, search, hide/unhide, reorder, guard 1 kolom, Reset to Default, dan discard"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-GSET-84
  - TC-GS-GSET-87
  - TC-GS-GSET-88
  - TC-GS-GSET-89
  - TC-GS-GSET-90
  - TC-GS-GSET-91
  - TC-GS-GSET-92
  - TC-GS-GSET-93
  - TC-GS-GSET-94
  - TC-GS-GSET-95
coverage:
  web: automated
---

# Setup Column Changelog: panel Column Visibility, modal screening, Pin/Unpin, search, hide/unhide, reorder, guard 1 kolom, Reset to Default, dan discard

## Prerequisites

- Login sebagai Role: Total Control
- Changelog General Settings berisi baris riwayat (dinamis)
- Viewport dapat dipersempit agar tabel Changelog dapat di-scroll horizontal

## Test Steps

### Panel Column Visibility

1. Buka Modal Changelog, hover header kolom Actions (⋯)
2. Verifikasi tooltip header "Column Visibility"
3. Klik header kolom Actions (⋯)
4. Verifikasi panel dropdown tampil: daftar kolom (Date, Action, Field, Old Value, New Value, Modified By) dengan show/hide dan reorder cepat; item `Setup Column...` di bagian bawah

### Modal Screening Setup Column

5. Klik item `Setup Column...` di panel dan amati modal
6. Verifikasi Header: Title "Setup Column", info text "Manage column visibility, reorder, and freeze columns.", tombol `[✕]`
7. Verifikasi Body: Search Input (placeholder "Search column name..."); 6 baris kolom (Date, Action, Field, Old Value, New Value, Modified By) semua checkbox Hideable checked dan enabled, drag handle, kontrol Pin/Unpin per baris; Live Preview tabel Changelog
8. Verifikasi Footer: `[Reset to Default]` dan `[Save]`, tanpa `[Cancel]`

### Pin dan Unpin Kolom

9. Klik icon Pin pada baris kolom Date dan amati Live Preview
10. Verifikasi Live Preview menandai kolom Date beku (freeze)
11. Klik `[Save]`
12. Persempit lebar viewport hingga tabel dapat di-scroll horizontal lalu scroll ke kanan
13. Verifikasi kolom Date tetap terlihat saat tabel di-scroll horizontal
14. Refresh (F5); verifikasi status pin bertahan
15. Buka Setup Column, klik icon Unpin pada kolom Date, klik `[Save]`
16. Verifikasi kolom Date ikut bergeser saat di-scroll

### Pencarian Nama Kolom

17. Buka Setup Column, ketik "Modified" di Search Input "Search column name..."
18. Verifikasi daftar kolom menyempit ke `Modified By`
19. Hapus kata kunci dan verifikasi keenam kolom tampil kembali

### Hide dan Unhide Kolom

20. Buka Setup Column, uncheck kolom Action, Old Value, dan New Value, lalu amati Live Preview
21. Verifikasi Live Preview menyembunyikan ketiga kolom
22. Klik `[Save]`, refresh (F5), dan verifikasi ketiga kolom tidak tampil serta tetap tersembunyi
23. Buka Setup Column, check kembali ketiganya, klik `[Save]`; verifikasi ketiga kolom tampil kembali

### Reorder Kolom

24. Buka Setup Column, drag kolom Modified By ke posisi pertama, amati Live Preview
25. Klik `[Save]`, lalu refresh (F5)
26. Verifikasi Modified By berada di urutan pertama pada Live Preview dan tabel serta bertahan setelah F5

### Guard Minimal Satu Kolom

27. Buka Setup Column, uncheck kolom satu per satu hingga tersisa satu kolom
28. Hover checkbox kolom terakhir dan coba uncheck
29. Verifikasi checkbox kolom terakhir disabled (tetap tampil), tidak dapat di-uncheck, dan tooltip "At least one column must remain visible."

### Reset to Default

30. Uncheck kolom Action dan geser Modified By ke posisi pertama, klik `[Save]`
31. Buka Setup Column lagi, klik `[Reset to Default]`, lalu amati Live Preview
32. Verifikasi Live Preview kembali ke 6 kolom default urutan Date | Action | Field | Old Value | New Value | Modified By
33. Klik `[Save]` dan refresh (F5); verifikasi urutan default bertahan

### Discard Perubahan Belum Disimpan

34. Buka Setup Column, uncheck kolom Field, klik `[✕]`
35. Verifikasi modal tertutup tanpa konfirmasi dan kolom Field tetap tampil
36. Buka Setup Column lagi, uncheck kolom Field, lalu tekan `Esc`
37. Verifikasi modal tertutup tanpa konfirmasi dan kolom Field tetap tampil
38. Buka Setup Column, uncheck kolom Field, klik `[Save]`; buka lagi, klik `[Reset to Default]`, lalu klik `[✕]`
39. Verifikasi setelah ditutup tanpa Save, tabel tetap memakai konfigurasi tersimpan (kolom Field tidak tampil)

## Notes

- Menggabungkan TC-GS-GSET-84, 87, 88, 89, 90, 91, 92, 93, 94, dan 95 (Setup Column Changelog). Spec terbesar; bila step > 35, pecah blok Pin/Reorder/Reset ke spec terpisah.
