---
id: TC-FA-GRP-E2E-233-tab-assets-filter-brand-isi-opsi-satu-dua-opsi-or-dan-search-dropdown
title: "Tab Assets Filter Brand: Isi Opsi, Satu/Dua Opsi OR, dan Search Dropdown"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-GRP-1069
  - TC-FA-GRP-1070
  - TC-FA-GRP-1071
  - TC-FA-GRP-1072
coverage:
  web: automated
---

# Tab Assets Filter Brand: Isi Opsi, Satu/Dua Opsi OR, dan Search Dropdown

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup No 1) `totalControlGroups_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Hook suite (flag Guided Tooltip, sesi API aktor, fixture BE, pemulihan state global) mengikuti `suite.md`.
- Data Pre-setup (hanya dibaca, tidak diubah): Warehouse A (Tabel A No 9) berisi 24 aset aktif dengan sedikitnya tiga nilai Brand distinct dan sedikitnya dua nilai Status distinct (S-11). Brand A dan Brand B adalah dua nilai Brand distinct yang dipakai baris Warehouse A, dibaca lewat kemampuan baca fixture BE sebelum uji. Fixture `Fixture.settingsGroups.noMatchText` (belum ada; teks yang tidak ada di opsi mana pun) dipakai untuk Search dropdown tanpa kecocokan.
- Kemampuan teknis: membaca data aset Warehouse A (Brand, Status) untuk menurunkan Brand A dan Brand B; disediakan tim FE/BE tanpa endpoint karangan.
- State global: tidak ada. Spec tidak menyimpan Setup Column; filter yang tersisa dibersihkan langkah penghubung.

## Test Steps

### TC-FA-GRP-1069: Screening isi opsi dropdown Filter Brand Tab Assets

1. Ketik Search `Warehouse A`, tekan Enter
2. Buka Detail Warehouse A (Tab Assets)
3. Klik icon Filter
4. Buka dropdown Brand
5. Verifikasi opsi sama dengan nilai Brand distinct yang ada di baris tabel Warehouse A saat ini dan tidak memuat nilai yang tidak dipakai baris mana pun
6. Verifikasi opsi dapat dicentang lebih dari satu (multi-select)
7. Verifikasi kotak search internal tampil di dalam dropdown

### TC-FA-GRP-1070: Filter Tab Assets by Brand: satu opsi

8. Pilih 1 opsi pada Brand (Brand A)
9. Klik [Apply]
10. Verifikasi sedikitnya satu baris tampil
11. Verifikasi hanya baris dengan Brand = Brand A yang tampil
12. Verifikasi indikator filter aktif tampil pada icon Filter

### TC-FA-GRP-1071: Filter Tab Assets by Brand: dua opsi dalam satu field (OR)

13. Klik icon Filter, kosongkan pilihan Brand, klik [Apply] (langkah penghubung)
14. Klik icon Filter
15. Centang 2 opsi berbeda pada Brand (Brand A dan Brand B)
16. Klik [Apply]
17. Verifikasi sedikitnya satu baris tampil
18. Verifikasi baris dengan Brand = Brand A atau Brand B tampil (OR di dalam field)
19. Verifikasi baris dengan nilai Brand lain tidak tampil

### TC-FA-GRP-1072: Search internal dropdown Filter Brand Tab Assets

20. Klik icon Filter, kosongkan pilihan Brand, klik [Apply] (langkah penghubung)
21. Klik icon Filter
22. Buka dropdown Brand
23. Ketik potongan nama Brand A dalam huruf kecil di kotak search dropdown
24. Verifikasi daftar opsi menyempit ke opsi yang mengandung substring (case-insensitive) dan memuat Brand A
25. Ganti isi kotak search dropdown dengan `Fixture.settingsGroups.noMatchText`
26. Verifikasi tidak ada opsi yang tampil di daftar opsi
27. Verifikasi teks `No results found` tampil di daftar opsi
28. Verifikasi tidak ada ilustrasi di daftar opsi (teks saja)

## Notes

- Sumber: `fixed-asset/settings-groups/TestCases/tc-settings-groups.md` (Section 4e). Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): "Klik icon Filter, kosongkan pilihan Brand, klik [Apply]" mengembalikan filter ke kosong sebelum TC berikutnya (S-09).
- Layar awal (Groups List) dibuka hook `beforeEach` suite; langkah "Buka Detail Warehouse A (Tab Assets)" adalah bagian TC.
- Baris target dicari lewat Search nama (client memiliki lebih dari 10 node level 1 dan page size 10, sehingga posisi baris di halaman 1 tidak diandalkan). Langkah Search adalah langkah penghubung (S-03, R-16).
- Temuan untuk QA:
  - TC-FA-GRP-1069: Expected "tidak termasuk nilai yang tidak dipakai baris mana pun" tidak menyebut contoh Brand katalog yang tidak dipakai; asersinya dibuktikan lewat kesamaan daftar opsi dengan nilai distinct tabel.
  - TC-FA-GRP-1072: "potongan nama opsi" tidak menyebut panjang potongan; spec memakai Brand A dalam huruf kecil.
  - Nama Brand A dan Brand B tidak tertulis di Tabel Data Uji (TC hanya menyebut "variasi Brand"); dibaca dari data Warehouse A.
