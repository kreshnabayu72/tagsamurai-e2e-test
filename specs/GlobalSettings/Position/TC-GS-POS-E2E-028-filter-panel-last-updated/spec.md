---
id: TC-GS-POS-E2E-028-filter-panel-last-updated
title: Filter Panel Last Updated — Screening, Rentang, Single-day, Persist saat Kolom Disembunyikan, Clear Field
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-POS-116
  - TC-GS-POS-65
  - TC-GS-POS-247
  - TC-GS-POS-252
  - TC-GS-POS-72
coverage:
  web: automated
---

# Filter Panel Last Updated — Screening, Rentang, Single-day, Persist saat Kolom Disembunyikan, Clear Field

## Prerequisites

- Aktor adalah `Fixture.globalSettingsPosition.actors.totalControl`.
- `Fixture.globalSettingsPosition.captions.filter.panel.label` = `Last Updated`.
- `Fixture.globalSettingsPosition.captions.filter.panel.placeholder` = `Select date range`.
- `Fixture.globalSettingsPosition.captions.filter.panel.actions.clear` = `Clear Field`.
- `Fixture.globalSettingsPosition.captions.filter.panel.actions.apply` = `Apply`.
- `Fixture.globalSettingsPosition.data.filterRange.stale` dan `Fixture.globalSettingsPosition.data.filterRange.recency` tersedia.
- `Fixture.globalSettingsPosition.data.searchPartialMatch` tersedia untuk menguji `Clear Field` tidak mereset search/sort.
- PRD §5 dan §9.8: Filter Panel hanya punya field Last Updated (date range), filter baru berlaku saat `Apply`. Filter independen dari visibilitas kolom.
- Konvensi: `Clear Field` tidak mereset keyword search dan arah sort yang sedang aktif.

## Test Steps

### A. Screening Filter Panel

1. Buka halaman `Global Settings > User > Position` dengan kondisi tanpa filter aktif.
2. Klik tombol Filter pada toolbar untuk membuka Filter Panel.
3. Verifikasi Filter Panel menampilkan field Last Updated dengan label `Fixture.globalSettingsPosition.captions.filter.panel.label`.
4. Verifikasi date range picker menampilkan placeholder `Fixture.globalSettingsPosition.captions.filter.panel.placeholder`.
5. Verifikasi tombol `Clear Field` dan `Apply` tampil.
6. Verifikasi hanya ada satu field di Filter Panel.

### B. Filter by Last Updated (date range)

7. Pilih rentang `Fixture.globalSettingsPosition.data.filterRange.stale` pada date range picker.
8. Verifikasi tabel belum berubah sebelum `Apply` ditekan.
9. Klik tombol `Apply`.
10. Verifikasi Filter Panel tertutup setelah `Apply`.
11. Verifikasi hanya baris dengan Last Updated dalam rentang `stale` yang tampil.

### C. Single-day (start == end)

12. Kosongkan filter dengan membuka Filter Panel, klik `Clear Field`, lalu `Apply`.
13. Buka Filter Panel kembali.
14. Pilih satu tanggal target (start == end) pada date range picker.
15. Klik `Apply`.
16. Verifikasi field terisi tanggal tersebut.
17. Verifikasi hanya baris dengan `Last Updated` = tanggal target yang tampil (exact match).

### D. Filter persist saat kolom Last Updated disembunyikan

18. Pastikan filter tanggal target masih aktif (dari langkah 15–17).
19. Klik header kolom Actions `(⋯)` → Overlay Column Visibility.
20. Uncheck kolom `Last Updated`.
21. Verifikasi kolom `Last Updated` langsung hilang dari tabel.
22. Verifikasi indikator filter aktif masih terlihat pada toolbar (filter tetap aktif).
23. Buka kembali Filter Panel.
24. Verifikasi kriteria filter Last Updated masih terisi sesuai filter yang terakhir di-Apply.
25. Centang kembali kolom `Last Updated` via Overlay Column Visibility.

### E. Clear Field tidak mereset Search & Sort

26. Ketik `Fixture.globalSettingsPosition.data.searchPartialMatch` lalu tekan Enter (aktifkan search).
27. Klik header kolom Name hingga arah sort aktif (Ascending/Descending teramati).
28. Catat state search+sort aktif.
29. Buka Filter Panel, klik `Clear Field`, lalu `Apply`.
30. Verifikasi kriteria filter Last Updated dilepas.
31. Verifikasi keyword search tetap terisi.
32. Verifikasi arah sort tabel tetap dipertahankan.
33. Verifikasi tabel menampilkan hasil sesuai keyword tanpa pembatasan rentang tanggal.

## Notes

- Langkah 8 menegaskan filter baru berlaku saat `Apply` (bukan saat memilih tanggal).
- Langkah 17 menegaskan single-day = exact match (start==end).
- D–E menegaskan independensi filter vs visibilitas kolom dan vs search/sort.
