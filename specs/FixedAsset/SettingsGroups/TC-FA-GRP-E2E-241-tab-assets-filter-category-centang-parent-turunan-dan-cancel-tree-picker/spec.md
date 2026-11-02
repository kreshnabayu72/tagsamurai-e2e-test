---
id: TC-FA-GRP-E2E-241-tab-assets-filter-category-centang-parent-turunan-dan-cancel-tree-picker
title: "Tab Assets Filter Category: Centang Parent Mencentang Turunan dan [Cancel] Membuang Pilihan Pending"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-GRP-1187
  - TC-FA-GRP-1188
coverage:
  web: automated
---

# Tab Assets Filter Category: Centang Parent Mencentang Turunan dan [Cancel] Membuang Pilihan Pending

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup No 1) `totalControlGroups_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Hook suite (flag Guided Tooltip, sesi API aktor, fixture BE, pemulihan state global) mengikuti `suite.md`.
- Data Pre-setup (hanya dibaca, tidak diubah): Warehouse A (Tabel A No 9) berisi 24 aset aktif dengan Category `Laptop` dan `Monitor` (parent `IT Equipment`) serta `Environmental Monitoring Equipment` (parent `Sensors`), dengan Brand, Model/Type, Label, dan Status bervariasi (sedikitnya dua nilai Category distinct, S-11).
- Kolom curated Category ditampilkan lewat Setup Column pada langkah penghubung awal spec (precondition d TC).
- Kemampuan teknis: tidak ada tambahan; data Category dibaca dari Warehouse A.
- State global: konfigurasi kolom Setup Column akun Total Control (kolom Category dicentang dan disimpan). Pemulihan preferensi kolom Setup Column: hook `after` menghapus preferensi kolom di browser (kemampuan disediakan tim FE), bukan `[Reset to Default]`. Filter yang tersisa dibersihkan langkah penghubung.

## Test Steps

### Langkah penghubung: tampilkan kolom curated Category

1. Buka Detail Warehouse A (Tab Assets)
2. Buka Popup Setup Column
3. Centang Category
4. Klik [Save]
5. Verifikasi kolom Category tampil di tabel (precondition TC)

### TC-FA-GRP-1187: Centang parent mencentang semua turunan dan menyaring seluruh turunan

6. Klik icon Filter
7. Klik tombol field Category
8. Centang node parent `IT Equipment`
9. Amati checkbox `Laptop` dan `Monitor`
10. Verifikasi checkbox `Laptop` ter-check
11. Verifikasi checkbox `Monitor` ter-check
12. Klik `[Select]`
13. Klik [Apply]
14. Verifikasi sedikitnya satu baris tampil
15. Verifikasi baris ber-Category `Laptop` atau `Monitor` tampil
16. Verifikasi baris ber-Category `Environmental Monitoring Equipment` tidak tampil
17. Verifikasi Filter Panel tertutup setelah [Apply]
18. Klik icon Filter
19. Buka kembali Modal Tree Picker lewat tombol field Category
20. Uncheck `Monitor`
21. Verifikasi `Monitor` ter-uncheck dan `Laptop` tetap ter-check
22. Verifikasi parent `IT Equipment` tidak lagi ter-check penuh
23. Klik `[Cancel]`

### TC-FA-GRP-1188: [Cancel] membuang pilihan pending

24. Klik icon Filter, hapus chip Category lewat (X), klik [Apply] (langkah penghubung)
25. Klik icon Filter
26. Klik tombol field Category
27. Centang `Laptop`
28. Klik `[Select]`
29. Buka kembali Modal Tree Picker lewat tombol field Category
30. Centang `Monitor`
31. Klik `[Cancel]`
32. Verifikasi modal tertutup
33. Verifikasi field menampilkan chip `Laptop` saja
34. Klik [Apply]
35. Verifikasi sedikitnya satu baris tampil
36. Verifikasi tabel hanya menyaring Category = `Laptop`
37. Klik icon Filter, hapus chip `Laptop` lewat (X), klik [Apply] (langkah penghubung)

## Notes

- Spec 37 langkah, di atas smell 35 langkah. Alasan: seluruh blok satu topik dan satu dataset tanpa kelas harness lain; tiap blok berdiri sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna.

- Sumber: `fixed-asset/settings-groups/TestCases/tc-settings-groups.md` (Section 4e). Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): kolom Category dicentang lewat Setup Column dan disimpan untuk membentuk precondition d TC; "hapus chip ..., klik [Apply]" mengosongkan filter antar-TC dan di akhir spec (S-09); "Klik icon Filter" membuka kembali Filter Panel yang sudah tertutup sesudah [Apply] (TC-1187, sesuai langkah 8 TC); `[Cancel]` menutup modal setelah pengamatan pada TC-FA-GRP-1187 (TC tidak menyebut cara menutup).
- Temuan untuk QA:
  - TC-FA-GRP-1187: langkah 8 (uncheck `Monitor`) tidak diikuti `[Select]` atau `[Cancel]` di TC; Expected (c) hanya menyebut keadaan checkbox, sehingga spec menutup modal dengan `[Cancel]` sebagai langkah penghubung.
