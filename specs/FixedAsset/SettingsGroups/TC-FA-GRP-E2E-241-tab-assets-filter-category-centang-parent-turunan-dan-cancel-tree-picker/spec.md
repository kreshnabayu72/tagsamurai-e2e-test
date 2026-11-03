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

1. Ketik Search `Warehouse A`, tekan Enter
2. Buka Detail Warehouse A (Tab Assets)
3. Buka Popup Setup Column
4. Centang Category
5. Klik [Save]
6. Verifikasi kolom Category tampil di tabel (precondition TC)

### TC-FA-GRP-1187: Centang parent mencentang semua turunan dan menyaring seluruh turunan

7. Klik icon Filter
8. Klik tombol field Category
9. Centang node parent `IT Equipment`
10. Amati checkbox `Laptop` dan `Monitor`
11. Verifikasi checkbox `Laptop` ter-check
12. Verifikasi checkbox `Monitor` ter-check
13. Klik `[Select]`
14. Klik [Apply]
15. Verifikasi sedikitnya satu baris tampil
16. Verifikasi baris ber-Category `Laptop` atau `Monitor` tampil
17. Verifikasi baris ber-Category `Environmental Monitoring Equipment` tidak tampil
18. Verifikasi Filter Panel tertutup setelah [Apply]
19. Klik icon Filter
20. Buka kembali Modal Tree Picker lewat tombol field Category
21. Uncheck `Monitor`
22. Verifikasi `Monitor` ter-uncheck dan `Laptop` tetap ter-check
23. Verifikasi parent `IT Equipment` tidak lagi ter-check penuh
24. Klik `[Cancel]`

### TC-FA-GRP-1188: [Cancel] membuang pilihan pending

25. Hapus chip Category lewat (X), klik [Apply] (langkah penghubung)
26. Klik icon Filter
27. Klik tombol field Category
28. Centang `Laptop`
29. Klik `[Select]`
30. Buka kembali Modal Tree Picker lewat tombol field Category
31. Centang `Monitor`
32. Klik `[Cancel]`
33. Verifikasi modal tertutup
34. Verifikasi field menampilkan chip `Laptop` saja
35. Klik [Apply]
36. Verifikasi sedikitnya satu baris tampil
37. Verifikasi tabel hanya menyaring Category = `Laptop`
38. Klik icon Filter, hapus chip `Laptop` lewat (X), klik [Apply] (langkah penghubung)

## Notes

- Spec 38 langkah, di atas smell 35 langkah. Alasan: seluruh blok satu topik dan satu dataset tanpa kelas harness lain; tiap blok berdiri sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna.

- Sumber: `fixed-asset/settings-groups/TestCases/tc-settings-groups.md` (Section 4e). Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): kolom Category dicentang lewat Setup Column dan disimpan untuk membentuk precondition d TC; "hapus chip ..., klik [Apply]" mengosongkan filter antar-TC dan di akhir spec (S-09); pada langkah 25 Filter Panel masih terbuka sesudah `[Cancel]` langkah 24, sehingga tidak ada klik icon Filter (klik icon akan menutup panel), sedangkan pada langkah 38 panel sudah tertutup sesudah [Apply] langkah 35 sehingga didahului klik icon Filter; "Klik icon Filter" membuka kembali Filter Panel yang sudah tertutup sesudah [Apply] (TC-1187, sesuai langkah 8 TC); `[Cancel]` menutup modal setelah pengamatan pada TC-FA-GRP-1187 (TC tidak menyebut cara menutup).
- Baris target dicari lewat Search nama (client memiliki lebih dari 10 node level 1 dan page size 10, sehingga posisi baris di halaman 1 tidak diandalkan). Langkah Search adalah langkah penghubung (S-03, R-16).
- Temuan untuk QA:
  - TC-FA-GRP-1187: langkah 9 (uncheck `Monitor`) tidak diikuti `[Select]` atau `[Cancel]` di TC; Expected (c) hanya menyebut keadaan checkbox, sehingga spec menutup modal dengan `[Cancel]` sebagai langkah penghubung.
