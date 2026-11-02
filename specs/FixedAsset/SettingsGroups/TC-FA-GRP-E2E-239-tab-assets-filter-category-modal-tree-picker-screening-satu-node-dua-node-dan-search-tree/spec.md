---
id: TC-FA-GRP-E2E-239-tab-assets-filter-category-modal-tree-picker-screening-satu-node-dua-node-dan-search-tree
title: "Tab Assets Filter Category: Screening Modal Tree Picker, Satu Node Leaf, Dua Node Leaf (OR), dan Search Tree"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-GRP-1158
  - TC-FA-GRP-1159
  - TC-FA-GRP-1160
  - TC-FA-GRP-1161
coverage:
  web: automated
---

# Tab Assets Filter Category: Screening Modal Tree Picker, Satu Node Leaf, Dua Node Leaf (OR), dan Search Tree

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup No 1) `totalControlGroups_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Hook suite (flag Guided Tooltip, sesi API aktor, fixture BE, pemulihan state global) mengikuti `suite.md`.
- Data Pre-setup (hanya dibaca, tidak diubah): Warehouse A (Tabel A No 9) berisi 24 aset aktif dengan Category `Laptop` dan `Monitor` (parent `IT Equipment`) serta `Environmental Monitoring Equipment` (parent `Sensors`), dengan Brand, Model/Type, Label, dan Status bervariasi (sedikitnya dua nilai Category distinct, S-11).
- Kolom curated Category ditampilkan lewat Setup Column pada langkah penghubung awal spec (precondition d TC).
- Kemampuan teknis: membaca Category client; fixture `Fixture.settingsGroups.unusedCategory` (Category client yang tidak dipakai aset Warehouse A; belum ada) dan `Fixture.settingsGroups.noMatchText` (teks yang tidak ada di nama node mana pun; belum ada) disediakan tim FE/BE.
- State global: konfigurasi kolom Setup Column akun Total Control (kolom Category dicentang dan disimpan). Pemulihan preferensi kolom Setup Column: hook `after` menghapus preferensi kolom di browser (kemampuan disediakan tim FE), bukan `[Reset to Default]`. Filter yang tersisa dibersihkan langkah penghubung.

## Test Steps

### Langkah penghubung: tampilkan kolom curated Category

1. Buka Detail Warehouse A (Tab Assets)
2. Buka Popup Setup Column
3. Centang Category
4. Klik [Save]
5. Verifikasi kolom Category tampil di tabel (precondition TC)

### TC-FA-GRP-1158: Screening field Filter Category: tombol pembuka Modal Tree Picker dan isi tree

6. Klik icon Filter
7. Amati field Category
8. Verifikasi field Category berupa tombol dengan placeholder `All categories` (bukan dropdown)
9. Klik tombol field Category
10. Verifikasi Modal Tree Picker multi-select terbuka berisi tree Category client (IT Equipment > Laptop, Monitor; Sensors > Environmental Monitoring Equipment)
11. Verifikasi tree memuat checkbox per node
12. Verifikasi tree memuat kotak Search
13. Verifikasi footer modal berisi `[Cancel]` dan `[Select]`
14. Verifikasi tree memuat Category client yang tidak dipakai aset mana pun di Warehouse A (`Fixture.settingsGroups.unusedCategory`)
15. Klik `[Cancel]` (langkah penghubung)

### TC-FA-GRP-1159: Filter Tab Assets by Category: satu node leaf

16. Klik tombol field Category
17. Centang node `Laptop`
18. Klik `[Select]`
19. Verifikasi field menampilkan chip `Laptop`
20. Klik [Apply]
21. Verifikasi sedikitnya satu baris tampil
22. Verifikasi hanya baris dengan Category = `Laptop` yang tampil
23. Verifikasi indikator filter aktif tampil pada icon Filter

### TC-FA-GRP-1160: Filter Tab Assets by Category: dua node leaf (OR)

24. Klik icon Filter, hapus chip `Laptop` lewat (X), klik [Apply] (langkah penghubung)
25. Klik icon Filter
26. Klik tombol field Category
27. Centang node `Laptop` dan `Environmental Monitoring Equipment`
28. Klik `[Select]`
29. Verifikasi field menampilkan dua chip
30. Klik [Apply]
31. Verifikasi sedikitnya satu baris tampil
32. Verifikasi baris dengan Category = `Laptop` atau `Environmental Monitoring Equipment` tampil (OR di dalam field)
33. Verifikasi baris ber-Category `Monitor` tidak tampil

### TC-FA-GRP-1161: Search di Modal Tree Picker filter Category

34. Klik icon Filter, hapus kedua chip Category lewat (X), klik [Apply] (langkah penghubung)
35. Klik icon Filter
36. Klik tombol field Category
37. Ketik `lap` di kotak Search modal
38. Verifikasi node `Laptop` tampil beserta parent `IT Equipment` (parent tetap tampil karena ada child yang cocok)
39. Verifikasi node yang tidak cocok disembunyikan (`Monitor`, `Sensors`, `Environmental Monitoring Equipment` tidak tampil)
40. Ganti isi kotak Search modal dengan `Fixture.settingsGroups.noMatchText`
41. Verifikasi empty state pencarian standar (§7.1) tampil di area tree
42. Klik `[Cancel]` (langkah penghubung)

## Notes

- Sumber: `fixed-asset/settings-groups/TestCases/tc-settings-groups.md` (Section 4e). Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung awal (S-03): kolom Category dicentang lewat Setup Column dan disimpan untuk membentuk precondition d TC-FA-GRP-1159 sampai TC-FA-GRP-1161; TC-FA-GRP-1158 tidak menyebut precondition itu tetapi berjalan dengan kolom yang sama. Langkah "hapus chip lewat (X), klik [Apply]" dan `[Cancel]` pada modal mengosongkan state antar-TC (S-09).
- Spec melewati sekitar 35 langkah: empat TC tanpa kelas harness (semua fungsional Filter Category pada dataset Warehouse A yang sama), tiap blok berdiri sendiri, dan langkah awal Setup Column serta langkah pemulihan antar-TC menambah panjang tanpa membuka alur baru; kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Temuan untuk QA:
  - TC-FA-GRP-1158: Expected (c) mensyaratkan Category client yang tidak dipakai aset di Warehouse A tetapi tidak menyebut namanya; spec memakai fixture `Fixture.settingsGroups.unusedCategory` (belum ada, disediakan tim FE/BE). Precondition d (kolom Category ditampilkan) tidak ditulis di TC-FA-GRP-1158.
  - TC-FA-GRP-1161: Expected (b) menyebut "empty state pencarian standar (§7.1)" tanpa teks; teks persisnya tidak diasersi di spec ini (bandingkan TC-FA-GRP-1170 yang menulis `No results found` dan `Try adjusting your search or filter.`).
