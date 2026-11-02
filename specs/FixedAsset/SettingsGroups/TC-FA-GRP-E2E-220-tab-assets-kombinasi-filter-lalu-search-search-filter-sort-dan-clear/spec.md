---
id: TC-FA-GRP-E2E-220-tab-assets-kombinasi-filter-lalu-search-search-filter-sort-dan-clear
title: "Tab Assets Kombinasi: Filter lalu Search, Search + Filter + Sort, serta Clear Filter/Search Saat Lainnya Aktif"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-GRP-694
  - TC-FA-GRP-699
  - TC-FA-GRP-700
  - TC-FA-GRP-701
coverage:
  web: automated
---

# Tab Assets Kombinasi: Filter lalu Search, Search + Filter + Sort, serta Clear Filter/Search Saat Lainnya Aktif

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup No 1) `totalControlGroups_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite.
- Hook suite (`suite.md`) berlaku: login default, flag Guided Tooltip `seen`, sesi API aktor, klien HTTP, dan fixture BE disediakan tim FE/BE.
- Data Pre-setup (hanya dibaca, tidak diubah): Warehouse A (Tabel A No 9: 24 aset aktif variasi status + 2 Disposed). Nilai variasi (Name, Asset ID, Status, Brand, Model/Type, Category, Last Updated; sedikitnya dua nilai distinct per kolom yang dipakai Search, Filter, dan Sort, S-11) dan nilai fixture acuan `Fixture.settingsGroups.<kunci>` disediakan tim FE/BE; Tabel Data Uji TC tidak memuat nilai konkret (lihat Temuan untuk QA).
- Keyword Search Fixture.settingsGroups.searchKeywordKombinasi (potongan nilai kolom Name yang cocok dengan sebagian baris yang lolos filter) dan Filter Status Fixture.settingsGroups.statusA; nilai field Filter Panel beririsan Fixture.settingsGroups.irisanSemuaField untuk TC-694. Sort kolom Name memerlukan sedikitnya dua nilai Name distinct pada himpunan irisan (S-11).

## Test Steps

### TC-FA-GRP-694: Filter lalu Search (irisan)

1. Klik angka Total Asset Warehouse A untuk membuka Popup Detail Group, Tab Assets
2. Klik icon Filter, isi seluruh field Filter Panel dengan nilai `Fixture.settingsGroups.irisanSemuaField`, klik [Apply]
3. Ketik Search `Fixture.settingsGroups.searchKeywordKombinasi`, tekan Enter
4. Verifikasi sedikitnya satu baris tampil
5. Verifikasi setiap baris yang tampil memenuhi Filter dan Search (irisan)
6. Verifikasi kriteria filter tetap aktif setelah search (indikator filter aktif tampil pada icon Filter)

### TC-FA-GRP-699: Search + Filter + Sort

7. Klik icon Filter, klik [Clear Field], klik [Apply]; klik `(←)` pada kotak Search (langkah penghubung)
8. Ketik Search `Fixture.settingsGroups.searchKeywordKombinasi`, tekan Enter
9. Klik icon Filter, pilih `Fixture.settingsGroups.statusA` pada Status, klik [Apply]
10. Klik header Name satu kali, klik header Name untuk kedua kali (Descending)
11. Verifikasi sedikitnya satu baris tampil
12. Verifikasi seluruh baris yang tampil memenuhi Search dan Filter tanpa saling reset
13. Verifikasi urutan Name Descending Z→A pada himpunan irisan

### TC-FA-GRP-700: Clear Filter saat Search dan Sort aktif

14. Klik icon Filter, klik [Clear Field]
15. Klik [Apply]
16. Verifikasi sedikitnya satu baris tampil
17. Verifikasi keyword Search `Fixture.settingsGroups.searchKeywordKombinasi` tetap terpasang di kotak Search
18. Verifikasi urutan Name Descending Z→A tetap berlaku
19. Verifikasi baris yang cocok Search tetapi berstatus selain `Fixture.settingsGroups.statusA` tampil (kriteria filter terlepas)

### TC-FA-GRP-701: Clear Search saat Filter dan Sort aktif

20. Klik icon Filter, pilih `Fixture.settingsGroups.statusA` pada Status, klik [Apply] (langkah penghubung untuk mengaktifkan kembali Filter)
21. Klik icon (✕) pada kotak Search, tekan Enter pada input kosong
22. Verifikasi sedikitnya satu baris tampil
23. Verifikasi setiap baris yang tampil berstatus `Fixture.settingsGroups.statusA` (kriteria filter tetap berlaku)
24. Verifikasi urutan Name Descending Z→A tetap berlaku
25. Verifikasi baris yang tidak cocok keyword Search `Fixture.settingsGroups.searchKeywordKombinasi` tetapi berstatus `Fixture.settingsGroups.statusA` tampil (keyword terlepas)

## Notes

- Langkah penghubung (S-03): langkah 1 membuka Popup Detail Group Tab Assets; [Clear Field], [Apply], dan `(←)` mengosongkan Filter dan Search antar-TC (S-09); langkah pengaktifan ulang Filter pada TC-701 membentuk precondition "Search, Filter, Sort aktif".
- Temuan untuk QA:
  - TC-694: "isi semua field filter" tidak merinci nilai per field; nilai dibaca dari fixture yang disediakan tim FE/BE.
  - TC-700 dan TC-701: precondition "Search K, filter aktif, sort aktif" tidak menyebut nilai konkret; spec memakai nilai yang sama dengan TC-699.
  - TC-699: arah sort "Name Desc" dilakukan dengan dua klik header (Ascending lalu Descending) sesuai siklus sort platform.
