---
id: TC-FA-GRP-E2E-236-tab-assets-filter-model-type-chip-opsi-dan-kombinasi-model-type-status
title: "Tab Assets Filter Model/Type: Chip Opsi dan Kombinasi Model/Type + Status (AND)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-GRP-1154
  - TC-FA-GRP-1155
  - TC-FA-GRP-1156
coverage:
  web: automated
---

# Tab Assets Filter Model/Type: Chip Opsi dan Kombinasi Model/Type + Status (AND)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup No 1) `totalControlGroups_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Hook suite (flag Guided Tooltip, sesi API aktor, fixture BE, pemulihan state global) mengikuti `suite.md`.
- Data Pre-setup (hanya dibaca, tidak diubah): Warehouse A (Tabel A No 9) berisi 24 aset aktif dengan sedikitnya tiga nilai Model/Type distinct dan sedikitnya dua nilai Status distinct (S-11). Model/Type A dan Model/Type B adalah dua nilai Model/Type distinct yang dipakai baris Warehouse A. Status S adalah status yang dipegang sedikitnya satu aset ber-Model/Type A; Warehouse A juga memuat aset ber-Model/Type A dengan status lain dan aset ber-Status S dengan Model/Type lain, sehingga kombinasi AND membedakan hasil dari filter satu field. Nilai dibaca lewat kemampuan baca fixture BE sebelum uji.
- Kemampuan teknis: membaca data aset Warehouse A (Model/Type, Status); disediakan tim FE/BE tanpa endpoint karangan.
- State global: tidak ada. Spec tidak menyimpan Setup Column; filter yang tersisa dibersihkan langkah penghubung.

## Test Steps

### TC-FA-GRP-1154: Chip opsi Filter Model/Type: muncul dan dihapus via (X)

1. Ketik Search `Warehouse A`, tekan Enter
2. Buka Detail Warehouse A (Tab Assets)
3. Klik icon Filter
4. Centang opsi A (Model/Type A) lalu opsi B (Model/Type B) pada Model/Type
5. Tutup dropdown
6. Verifikasi chip Model/Type A tampil di dalam field
7. Verifikasi chip Model/Type B tampil di dalam field dan tidak menggantikan chip Model/Type A
8. Klik (X) pada chip Model/Type A
9. Verifikasi chip Model/Type A hilang dari field
10. Buka dropdown Model/Type
11. Verifikasi checkbox Model/Type A di dropdown ter-uncheck
12. Verifikasi chip Model/Type B tetap ada di field
13. Tutup dropdown
14. Klik [Apply]
15. Verifikasi sedikitnya satu baris tampil
16. Verifikasi tabel hanya menyaring Model/Type = Model/Type B

### TC-FA-GRP-1155: Chip opsi Filter Model/Type: dihapus via uncheck di dalam dropdown

17. Klik icon Filter, kosongkan pilihan Model/Type, klik [Apply] (langkah penghubung)
18. Klik icon Filter
19. Centang opsi A (Model/Type A) lalu opsi B (Model/Type B) pada Model/Type
20. Buka lagi dropdown Model/Type dan uncheck opsi A dari dalam dropdown
21. Verifikasi chip Model/Type A hilang dari field
22. Verifikasi chip Model/Type B tetap ada di field
23. Klik [Apply]
24. Verifikasi sedikitnya satu baris tampil
25. Verifikasi tabel hanya menyaring Model/Type = Model/Type B

### TC-FA-GRP-1156: Filter Tab Assets kombinasi Model/Type + Status (AND antar-field)

26. Klik icon Filter, kosongkan pilihan Model/Type, klik [Apply] (langkah penghubung)
27. Klik icon Filter
28. Isi Model/Type (Model/Type A) dan Status (Status S)
29. Klik [Apply]
30. Verifikasi sedikitnya satu baris tampil
31. Verifikasi setiap baris yang tampil memenuhi kedua kriteria (Model/Type = Model/Type A dan Status = Status S) (AND antar-field)
32. Klik icon Filter, kosongkan pilihan Model/Type dan Status, klik [Apply] (langkah penghubung)

## Notes

- Sumber: `fixed-asset/settings-groups/TestCases/tc-settings-groups.md` (Section 4e). Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): "Klik icon Filter, kosongkan pilihan ..., klik [Apply]" mengosongkan filter sebelum TC berikutnya dan di akhir spec (S-09); "Tutup dropdown" dan buka dropdown ulang adalah bagian pengamatan chip.
- Baris target dicari lewat Search nama (client memiliki lebih dari 10 node level 1 dan page size 10, sehingga posisi baris di halaman 1 tidak diandalkan). Langkah Search adalah langkah penghubung (S-03, R-16).
- Temuan untuk QA:
  - TC-FA-GRP-1154: "opsi A" dan "opsi B" tidak ditentukan; spec memakai Model/Type A dan Model/Type B dari data Warehouse A.
  - TC-FA-GRP-1156: "Isi Model/Type dan Status" tidak menyebut nilai; spec memakai Model/Type A dan Status S yang membentuk irisan tidak kosong (precondition kurang).
