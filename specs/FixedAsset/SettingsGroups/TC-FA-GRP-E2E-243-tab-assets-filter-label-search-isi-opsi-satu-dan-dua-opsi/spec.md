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

1. Ketik Search `Multi Label Node`, tekan Enter
2. Buka Detail Multi Label Node (Tab Assets)
3. Buka Popup Setup Column
4. Centang Label
5. Klik [Save]
6. Verifikasi kolom Label tampil di tabel (precondition TC)

### TC-FA-GRP-1170: Search kolom Label: substring, case-insensitive, label di balik +N more, tanpa hasil

7. Ketik Search `prior`, tekan Enter
8. Verifikasi aset L1, L2, dan L3 tampil
9. Verifikasi label Priority aset L1 tersembunyi di balik `+1 more`
10. Verifikasi aset L4 dan L5 tidak tampil
11. Ganti isi kotak search dengan `PRIOR`, tekan Enter
12. Verifikasi hasil identik dengan huruf kecil: L1, L2, L3 tampil dan L4, L5 tidak tampil (case-insensitive)
13. Ganti isi kotak search dengan `Fixture.settingsGroups.noMatchText`, tekan Enter
14. Verifikasi empty state Illustration dengan title `No results found` dan body `Try adjusting your search or filter.`
15. Klik `(←)` pada kotak Search (langkah penghubung)

### TC-FA-GRP-1171: Screening isi opsi dropdown Filter Label

16. Klik icon Filter
17. Verifikasi placeholder field Label `All labels`
18. Buka dropdown Label
19. Verifikasi opsi = Finance, Fragile, Priority (nilai Label distinct yang ada di baris tabel saat ini)
20. Verifikasi label katalog yang tidak dipakai aset mana pun tidak menjadi opsi
21. Verifikasi opsi tampil berbadge warna label
22. Verifikasi opsi dapat dicentang lebih dari satu (multi-select)
23. Verifikasi kotak search internal tampil di dalam dropdown
24. Tutup dropdown

### TC-FA-GRP-1172: Filter Label satu opsi, aset berlabel ganda cocok bila salah satu labelnya sama

25. Pilih opsi Fragile pada Label
26. Klik [Apply]
27. Verifikasi aset L1 dan L2 tampil (Fragile adalah salah satu labelnya)
28. Verifikasi aset L3, L4, dan L5 tidak tampil
29. Verifikasi indikator filter aktif tampil pada icon Filter

### TC-FA-GRP-1173: Filter Label dua opsi dalam satu field (OR)

30. Klik icon Filter, kosongkan pilihan Label, klik [Apply] (langkah penghubung)
31. Klik icon Filter
32. Centang Finance dan Priority pada Label
33. Klik [Apply]
34. Verifikasi aset L1, L2, L3, dan L5 tampil (memiliki Finance atau Priority)
35. Verifikasi aset L4 (tanpa label) tidak tampil
36. Klik icon Filter, kosongkan pilihan Label, klik [Apply] (langkah penghubung)

## Notes

- Sumber: `fixed-asset/settings-groups/TestCases/tc-settings-groups.md` (Section 4e). Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): kolom Label dicentang lewat Setup Column dan disimpan untuk membentuk precondition d; "Klik `(←)` pada kotak Search" dan "kosongkan pilihan Label, klik [Apply]" mengosongkan state antar-TC dan di akhir spec (S-09). Search nama node dipakai sebagai langkah penghubung untuk menemukan baris target (client memiliki lebih dari 10 node level 1 dan page size 10, sehingga posisi baris di halaman 1 tidak diandalkan; R-16).
- Spec memiliki 36 langkah, di atas smell 35 langkah. Alasan: satu kelas (fungsional Filter Label), satu dataset (Multi Label Node), tiap blok TC berdiri sendiri dan tidak bergantung pada hasil blok lain; langkah dominan berupa Verifikasi per klausa (S-01).
- Temuan untuk QA:
  - TC-FA-GRP-1171 tidak menyebut precondition d (kolom Label ditampilkan) dan tidak menyebut nama label katalog yang tidak dipakai; spec memakai kolom Label yang sama dan `Fixture.settingsGroups.unusedLabel`.
  - TC-FA-GRP-1170: Expected (a) "L1 yang label Priority-nya tersembunyi di balik `+1 more`" dipecah menjadi satu Verifikasi tersendiri (S-01).
