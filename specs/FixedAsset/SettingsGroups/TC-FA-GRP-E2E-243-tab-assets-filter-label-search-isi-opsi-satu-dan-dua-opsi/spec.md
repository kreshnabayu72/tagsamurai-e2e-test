---
id: TC-FA-GRP-E2E-243-tab-assets-filter-label-search-isi-opsi-satu-dan-dua-opsi
title: "Tab Assets Label: Search Kolom Label (+N more), Isi Opsi Filter, Satu Opsi (Berlabel Ganda), dan Dua Opsi OR"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-GRP-1170
  - TC-FA-GRP-1171
  - TC-FA-GRP-1172
  - TC-FA-GRP-1173
coverage:
  web: automated
---

# Tab Assets Label: Search Kolom Label (+N more), Isi Opsi Filter, Satu Opsi (Berlabel Ganda), dan Dua Opsi OR

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup No 1) `totalControlGroups_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Hook suite (flag Guided Tooltip, sesi API aktor, fixture BE, pemulihan state global) mengikuti `suite.md`.
- Data Pre-setup (hanya dibaca, tidak diubah): Multi Label Node (Tabel B No 9, Assignable, level 1) berisi hanya 5 aset aktif: L1 (Finance, Fragile, Priority), L2 (Fragile, Priority), L3 (Priority), L4 (tanpa label), L5 (Finance); status aset bervariasi. Tiga nilai Label distinct memenuhi syarat search/filter (S-11). Fixture "Pre-setup tambahan" ini di-seed tim FE/BE dan tidak diubah spec. Katalog Label client memuat sedikitnya satu label yang tidak dipakai aset mana pun (`Fixture.settingsGroups.unusedLabel`, belum ada; disediakan tim FE/BE). Fixture `Fixture.settingsGroups.noMatchText` (belum ada; teks yang tidak ada di data) dipakai untuk Search tanpa hasil.
- Kolom curated Label tersembunyi secara default dan ditampilkan oleh langkah penghubung awal spec (precondition d TC-FA-GRP-1170, 1172, 1173).
- Kemampuan teknis: menghapus preferensi kolom Setup Column di browser (disediakan tim FE); membaca data aset (tim FE/BE).
- State global: konfigurasi kolom Setup Column akun Total Control (kolom Label dicentang dan disimpan). Pemulihan preferensi kolom Setup Column: hook `after` menghapus preferensi kolom di browser (kemampuan disediakan tim FE), bukan `[Reset to Default]`. Filter dan Search yang tersisa dibersihkan langkah penghubung.

## Test Steps

### Langkah penghubung: tampilkan kolom curated Label

1. Buka Detail Multi Label Node (Tab Assets)
2. Buka Popup Setup Column
3. Centang Label
4. Klik [Save]
5. Verifikasi kolom Label tampil di tabel (precondition TC)

### TC-FA-GRP-1170: Search kolom Label: substring, case-insensitive, label di balik +N more, tanpa hasil

6. Ketik Search `prior`, tekan Enter
7. Verifikasi aset L1, L2, dan L3 tampil
8. Verifikasi label Priority aset L1 tersembunyi di balik `+1 more`
9. Verifikasi aset L4 dan L5 tidak tampil
10. Ganti isi kotak search dengan `PRIOR`, tekan Enter
11. Verifikasi hasil identik dengan huruf kecil: L1, L2, L3 tampil dan L4, L5 tidak tampil (case-insensitive)
12. Ganti isi kotak search dengan `Fixture.settingsGroups.noMatchText`, tekan Enter
13. Verifikasi empty state Illustration dengan title `No results found` dan body `Try adjusting your search or filter.`
14. Klik `(←)` pada kotak Search (langkah penghubung)

### TC-FA-GRP-1171: Screening isi opsi dropdown Filter Label

15. Klik icon Filter
16. Verifikasi placeholder field Label `All labels`
17. Buka dropdown Label
18. Verifikasi opsi = Finance, Fragile, Priority (nilai Label distinct yang ada di baris tabel saat ini)
19. Verifikasi label katalog yang tidak dipakai aset mana pun tidak menjadi opsi
20. Verifikasi opsi tampil berbadge warna label
21. Verifikasi opsi dapat dicentang lebih dari satu (multi-select)
22. Verifikasi kotak search internal tampil di dalam dropdown
23. Tutup dropdown

### TC-FA-GRP-1172: Filter Label satu opsi, aset berlabel ganda cocok bila salah satu labelnya sama

24. Pilih opsi Fragile pada Label
25. Klik [Apply]
26. Verifikasi aset L1 dan L2 tampil (Fragile adalah salah satu labelnya)
27. Verifikasi aset L3, L4, dan L5 tidak tampil
28. Verifikasi indikator filter aktif tampil pada icon Filter

### TC-FA-GRP-1173: Filter Label dua opsi dalam satu field (OR)

29. Klik icon Filter, kosongkan pilihan Label, klik [Apply] (langkah penghubung)
30. Klik icon Filter
31. Centang Finance dan Priority pada Label
32. Klik [Apply]
33. Verifikasi aset L1, L2, L3, dan L5 tampil (memiliki Finance atau Priority)
34. Verifikasi aset L4 (tanpa label) tidak tampil
35. Klik icon Filter, kosongkan pilihan Label, klik [Apply] (langkah penghubung)

## Notes

- Sumber: `fixed-asset/settings-groups/TestCases/tc-settings-groups.md` (Section 4e). Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): kolom Label dicentang lewat Setup Column dan disimpan untuk membentuk precondition d; "Klik `(←)` pada kotak Search" dan "kosongkan pilihan Label, klik [Apply]" mengosongkan state antar-TC dan di akhir spec (S-09). Search untuk menemukan baris target tidak dipakai di luar TC.
- Temuan untuk QA:
  - TC-FA-GRP-1171 tidak menyebut precondition d (kolom Label ditampilkan) dan tidak menyebut nama label katalog yang tidak dipakai; spec memakai kolom Label yang sama dan `Fixture.settingsGroups.unusedLabel`.
  - TC-FA-GRP-1170: Expected (a) "L1 yang label Priority-nya tersembunyi di balik `+1 more`" dipecah menjadi satu Verifikasi tersendiri (S-01).
