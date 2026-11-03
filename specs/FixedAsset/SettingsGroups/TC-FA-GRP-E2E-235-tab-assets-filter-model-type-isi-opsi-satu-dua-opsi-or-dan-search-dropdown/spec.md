---
id: TC-FA-GRP-E2E-235-tab-assets-filter-model-type-isi-opsi-satu-dua-opsi-or-dan-search-dropdown
title: "Tab Assets Filter Model/Type: Isi Opsi, Satu/Dua Opsi OR, dan Search Dropdown"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-GRP-1150
  - TC-FA-GRP-1151
  - TC-FA-GRP-1152
  - TC-FA-GRP-1153
coverage:
  web: automated
---

# Tab Assets Filter Model/Type: Isi Opsi, Satu/Dua Opsi OR, dan Search Dropdown

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup No 1) `totalControlGroups_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Hook suite (flag Guided Tooltip, sesi API aktor, fixture BE, pemulihan state global) mengikuti `suite.md`.
- Data Pre-setup (hanya dibaca, tidak diubah): Warehouse A (Tabel A No 9) berisi 24 aset aktif dengan sedikitnya tiga nilai Model/Type distinct dan sedikitnya dua nilai Status distinct (S-11). Model/Type A dan Model/Type B adalah dua nilai Model/Type distinct yang dipakai baris Warehouse A, dibaca lewat kemampuan baca fixture BE sebelum uji. Fixture `Fixture.settingsGroups.noMatchText` (belum ada; teks yang tidak ada di opsi mana pun) dipakai untuk Search dropdown tanpa kecocokan.
- Kemampuan teknis: membaca data aset Warehouse A (Model/Type, Status) untuk menurunkan Model/Type A dan Model/Type B; disediakan tim FE/BE tanpa endpoint karangan.
- State global: tidak ada. Spec tidak menyimpan Setup Column; filter yang tersisa dibersihkan langkah penghubung.

## Test Steps

### TC-FA-GRP-1150: Screening isi opsi dropdown Filter Model/Type Tab Assets

1. Ketik Search `Warehouse A`, tekan Enter
2. Buka Detail Warehouse A (Tab Assets)
3. Klik icon Filter
4. Buka dropdown Model/Type
5. Verifikasi opsi sama dengan nilai Model/Type distinct yang ada di baris tabel Warehouse A saat ini dan tidak memuat nilai yang tidak dipakai baris mana pun
6. Verifikasi opsi dapat dicentang lebih dari satu (multi-select)
7. Verifikasi kotak search internal tampil di dalam dropdown
8. Verifikasi placeholder field Model/Type `All models`

### TC-FA-GRP-1151: Filter Tab Assets by Model/Type: satu opsi

9. Pilih 1 opsi pada Model/Type (Model/Type A)
10. Klik [Apply]
11. Verifikasi sedikitnya satu baris tampil
12. Verifikasi hanya baris dengan Model/Type = Model/Type A yang tampil
13. Verifikasi indikator filter aktif tampil pada icon Filter

### TC-FA-GRP-1152: Filter Tab Assets by Model/Type: dua opsi dalam satu field (OR)

14. Klik icon Filter, kosongkan pilihan Model/Type, klik [Apply] (langkah penghubung)
15. Klik icon Filter
16. Centang 2 opsi berbeda pada Model/Type (Model/Type A dan Model/Type B)
17. Klik [Apply]
18. Verifikasi sedikitnya satu baris tampil
19. Verifikasi baris dengan Model/Type = Model/Type A atau Model/Type B tampil (OR di dalam field)
20. Verifikasi baris dengan nilai Model/Type lain tidak tampil

### TC-FA-GRP-1153: Search internal dropdown Filter Model/Type Tab Assets

21. Klik icon Filter, kosongkan pilihan Model/Type, klik [Apply] (langkah penghubung)
22. Klik icon Filter
23. Buka dropdown Model/Type
24. Ketik potongan nama Model/Type A dalam huruf kecil di kotak search dropdown
25. Verifikasi daftar opsi menyempit ke opsi yang mengandung substring (case-insensitive) dan memuat Model/Type A
26. Ganti isi kotak search dropdown dengan `Fixture.settingsGroups.noMatchText`
27. Verifikasi tidak ada opsi yang tampil di daftar opsi
28. Verifikasi teks `No results found` tampil di daftar opsi
29. Verifikasi tidak ada ilustrasi di daftar opsi (teks saja)

## Notes

- Sumber: `fixed-asset/settings-groups/TestCases/tc-settings-groups.md` (Section 4e). Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): "Klik icon Filter, kosongkan pilihan Model/Type, klik [Apply]" mengembalikan filter ke kosong sebelum TC berikutnya (S-09).
- Layar awal (Groups List) dibuka hook `beforeEach` suite; langkah "Buka Detail Warehouse A (Tab Assets)" adalah bagian TC.
- Baris target dicari lewat Search nama (client memiliki lebih dari 10 node level 1 dan page size 10, sehingga posisi baris di halaman 1 tidak diandalkan). Langkah Search adalah langkah penghubung (S-03, R-16).
- Temuan untuk QA:
  - TC-FA-GRP-1150: Expected "tidak termasuk nilai yang tidak dipakai baris mana pun" tidak menyebut contoh Model/Type katalog yang tidak dipakai; asersinya dibuktikan lewat kesamaan daftar opsi dengan nilai distinct tabel.
  - TC-FA-GRP-1153: "potongan nama opsi" tidak menyebut panjang potongan; spec memakai Model/Type A dalam huruf kecil.
  - Nama Model/Type A dan Model/Type B tidak tertulis di Tabel Data Uji (TC hanya menyebut "variasi Model/Type"); dibaca dari data Warehouse A.
