---
id: TC-FA-GRP-E2E-240-tab-assets-filter-category-chip-uncheck-node-dan-kombinasi-category-status
title: "Tab Assets Filter Category: Chip Dihapus via X, Uncheck Node di Tree, dan Kombinasi Category + Status"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-GRP-1162
  - TC-FA-GRP-1163
  - TC-FA-GRP-1164
coverage:
  web: automated
---

# Tab Assets Filter Category: Chip Dihapus via X, Uncheck Node di Tree, dan Kombinasi Category + Status

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup No 1) `totalControlGroups_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Hook suite (flag Guided Tooltip, sesi API aktor, fixture BE, pemulihan state global) mengikuti `suite.md`.
- Data Pre-setup (hanya dibaca, tidak diubah): Warehouse A (Tabel A No 9) berisi 24 aset aktif dengan Category `Laptop` dan `Monitor` (parent `IT Equipment`) serta `Environmental Monitoring Equipment` (parent `Sensors`), dengan Brand, Model/Type, Label, dan Status bervariasi (sedikitnya dua nilai Category distinct, S-11).
- Kolom curated Category ditampilkan lewat Setup Column pada langkah penghubung awal spec (precondition d TC).
- Kemampuan teknis: membaca data aset Warehouse A (Category, Status) untuk menurunkan Status S; disediakan tim FE/BE tanpa endpoint karangan. Status S dipegang sedikitnya satu aset `Laptop`, dan Warehouse A memuat aset `Laptop` dengan status lain.
- State global: konfigurasi kolom Setup Column akun Total Control (kolom Category dicentang dan disimpan). Pemulihan preferensi kolom Setup Column: hook `after` menghapus preferensi kolom di browser (kemampuan disediakan tim FE), bukan `[Reset to Default]`. Filter yang tersisa dibersihkan langkah penghubung.

## Test Steps

### Langkah penghubung: tampilkan kolom curated Category

1. Buka Detail Warehouse A (Tab Assets)
2. Buka Popup Setup Column
3. Centang Category
4. Klik [Save]
5. Verifikasi kolom Category tampil di tabel (precondition TC)

### TC-FA-GRP-1162: Chip filter Category dihapus via (X)

6. Klik icon Filter
7. Klik tombol field Category
8. Centang `Laptop` dan `Monitor`
9. Klik `[Select]`
10. Verifikasi chip `Laptop` dan `Monitor` tampil di field
11. Klik (X) pada chip `Laptop`
12. Verifikasi chip `Laptop` hilang dari field
13. Verifikasi chip `Monitor` tetap ada di field
14. Buka kembali Modal Tree Picker lewat tombol field Category
15. Verifikasi node `Laptop` ter-uncheck
16. Verifikasi node `Monitor` tetap ter-check
17. Klik `[Cancel]`
18. Klik [Apply]
19. Verifikasi sedikitnya satu baris tampil
20. Verifikasi tabel hanya menyaring Category = `Monitor`

### TC-FA-GRP-1163: Uncheck node di Modal Tree Picker menghapus chip

21. Klik icon Filter, hapus chip `Monitor` lewat (X), klik [Apply] (langkah penghubung)
22. Klik icon Filter
23. Klik tombol field Category
24. Centang `Laptop` dan `Monitor`
25. Klik `[Select]`
26. Buka kembali Modal Tree Picker, uncheck `Laptop`, klik `[Select]`
27. Verifikasi chip `Laptop` hilang dari field
28. Verifikasi chip `Monitor` tetap ada di field
29. Klik [Apply]
30. Verifikasi sedikitnya satu baris tampil
31. Verifikasi tabel hanya menyaring Category = `Monitor`

### TC-FA-GRP-1164: Filter kombinasi Category + Status (AND antar-field)

32. Klik icon Filter, hapus chip `Monitor` lewat (X), klik [Apply] (langkah penghubung)
33. Klik icon Filter
34. Pilih node `Laptop` pada field Category lewat Modal Tree Picker
35. Klik `[Select]`
36. Isi Status (Status S, salah satu status aset Laptop)
37. Klik [Apply]
38. Verifikasi sedikitnya satu baris tampil
39. Verifikasi setiap baris yang tampil memenuhi kedua kriteria (Category = `Laptop` dan Status = Status S) (AND antar-field)
40. Klik icon Filter, hapus chip Category dan kosongkan Status, klik [Apply] (langkah penghubung)

## Notes

- Sumber: `fixed-asset/settings-groups/TestCases/tc-settings-groups.md` (Section 4e). Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung awal (S-03): kolom Category dicentang lewat Setup Column dan disimpan untuk membentuk precondition d TC; langkah "hapus chip ..., klik [Apply]" dan `[Cancel]` pada modal mengosongkan state antar-TC (S-09). Modal dibuka ulang pada TC-FA-GRP-1162 hanya untuk mengamati checkbox lalu ditutup dengan `[Cancel]` (TC tidak menyebut cara menutup).
- Spec melewati sekitar 35 langkah: tiga TC tanpa kelas harness (semua fungsional Filter Category pada dataset Warehouse A yang sama), tiap blok berdiri sendiri, dan langkah awal Setup Column serta langkah pemulihan antar-TC menambah panjang tanpa membuka alur baru; kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Temuan untuk QA:
  - TC-FA-GRP-1164: "Isi Status" tidak menyebut nilai; spec memakai Status S, status yang dipegang sedikitnya satu aset `Laptop`, dan Warehouse A juga memuat aset `Laptop` dengan status lain (precondition kurang).
  - TC-FA-GRP-1162: cara menutup modal sesudah pengamatan checkbox tidak disebut TC.
