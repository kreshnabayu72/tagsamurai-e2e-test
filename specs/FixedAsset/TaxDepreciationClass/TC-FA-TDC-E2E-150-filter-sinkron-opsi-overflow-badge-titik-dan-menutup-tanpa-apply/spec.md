---
id: TC-FA-TDC-E2E-150-filter-sinkron-opsi-overflow-badge-titik-dan-menutup-tanpa-apply
title: "Filter: Sinkron Chip Opsi, Overflow +N more, Badge Titik, dan Menutup Panel Tanpa Apply"
layer: ui-e2e
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TDC-522
  - TC-FA-TDC-523
  - TC-FA-TDC-524
  - TC-FA-TDC-525
sourceRules: ["§4.1.1#r4", "§4.1.1#b7", "§4.4#r9", "§9.5#r2", "§5#b6"]
smoke: []
dependsOn: []
trace:
  "§4.1.1#r4": [5, 6, 8]
  "§4.1.1#b7": [12, 13, 14]
  "§4.4#r9": [16, 17, 18]
  "§9.5#r2": 18
  "§5#b6": [23, 25]
anchor: [31, 32, 33, 34]
coverage:
  web: automated
---

# Filter: Sinkron Chip Opsi, Overflow +N more, Badge Titik, dan Menutup Panel Tanpa Apply

## Prerequisites

- Mode: FE+BE.
- Akun: Total Control (company uji Fixed Asset). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Akun dan email disediakan tim FE (email tidak tertulis di TC); password lewat `Spectra.env.FA_TC_PASSWORD`.
- Hook suite, seeding, dan flag Guided Tooltip mengikuti `suite.md`.
- Data Pre-setup (`Fixture.fixedAssetTaxDepreciationClass.exampleData`, disediakan tim FE), dua isi tabel berurutan:
  - Isi tabel A (TC-FA-TDC-522, 524, 525; dibaca, tidak diubah): sembilan class Example Data PRD (BLD-NP, BLD-P, LAND, NB-1, NB-2, NB-4, NB-KHS, NB-OLD, NB-SL) dengan nilai kolom persis Example Data; tabel muat pada satu halaman. Asset Type BLD-NP dan BLD-P `Building`, LAND `Land`, class lain `Non-building`.
  - Isi tabel B (TC-FA-TDC-523, kunci `sixModifiedBy`): isi tabel A dengan enam user berbeda tercatat sebagai Modified By (nama user disediakan tim FE). Isi tabel diubah lewat seeding API pada langkah 28 dan dikembalikan ke isi tabel A pada langkah 35; Last Updated class Example Data berubah sebagai efeknya (spec ini tidak mengasersi Last Updated). Pemulihan dijamin fixture BE yang disediakan tim FE/BE dan dijalankan juga di hook `after`.
- Data uji (literal TC): Asset Type `Land`, `Building`, `Non-building`; enam opsi dropdown Modified By.
- Data Dinamis: tidak ada.
- Kemampuan teknis: seeding dan penggantian isi tabel lewat API (`suite.md`); membaca chip opsi pada field multi-select; membaca badge titik pada icon Filter (komponen Badge varian Standalone Dot, selector belum ada, perlu dikonfirmasi tim FE); mengklik di luar panel.
- State global yang diubah: Filter pada tabel (dilepas oleh langkah di spec dan oleh `beforeEach` suite) dan Modified By class (isi tabel B, dipulihkan langkah 35 dan hook `after`); suite berjalan serial (`parallel: false`).

## Test Steps

### Uncheck opsi di dalam dropdown menyinkronkan chip (TC-FA-TDC-522)

1. Klik icon Filter
2. Pilih Asset Type `Land` dan `Building`
3. Buka dropdown Asset Type
4. Uncheck `Land` di dalam dropdown
5. Verifikasi chip `Building` tetap ada
6. Verifikasi chip `Land` hilang dari field
7. Klik `[Apply]`
8. Verifikasi tabel menampilkan tepat dua baris: BLD-NP dan BLD-P

### Badge titik pada ikon Filter muncul saat filter ter-Apply dan hilang saat filter dilepas (TC-FA-TDC-524)

9. Klik `[Clear Field]` pada Filter Panel
10. Pilih Asset Type `Land`
11. Klik `[Apply]`
12. Verifikasi icon Filter menampilkan badge titik
13. Verifikasi badge titik tanpa angka
14. Verifikasi tidak ada chip atau tombol pelepas filter di atas tabel
15. Klik `[Clear Field]`
16. Klik `[Apply]`
17. Verifikasi badge titik pada icon Filter hilang
18. Verifikasi tabel menampilkan 9 baris

### Menutup Filter Panel tanpa Apply membuang perubahan (TC-FA-TDC-525)

19. Pilih Asset Type `Land`
20. Klik `[Apply]`
21. Ubah Asset Type menjadi `Non-building` (hapus `Land`, pilih `Non-building`) tanpa `[Apply]`
22. Klik di luar panel
23. Verifikasi tabel tetap menampilkan hanya baris LAND setelah panel ditutup
24. Buka kembali Filter Panel
25. Verifikasi panel menampilkan nilai ter-Apply terakhir: Asset Type `Land`
26. Klik `[Clear Field]`
27. Klik `[Apply]`

### Overflow banyak chip diringkas menjadi +N more (TC-FA-TDC-523)

28. Ganti isi tabel menjadi isi tabel B (enam user berbeda tercatat sebagai Modified By) lewat seeding API, lalu muat ulang halaman
29. Buka Filter Panel
30. Pilih keenam opsi pada dropdown Modified By
31. Verifikasi field menampilkan chip sebanyak yang muat
32. Verifikasi sisanya diringkas dalam satu chip `+N more`
33. Verifikasi field tidak melebar keluar panel
34. Verifikasi field tidak digulir horizontal
35. Kembalikan isi tabel menjadi isi tabel A (sembilan class Example Data) lewat seeding API

## Notes

- Urutan TC dalam spec: TC-FA-TDC-522, 524, 525, 523. TC-FA-TDC-523 diletakkan terakhir karena butuh isi tabel B (enam user Modified By); TC lain memakai isi tabel A.
- Langkah penghubung (S-03, S-09): langkah 9 (melepas Filter Building lewat `[Clear Field]` sebelum TC-FA-TDC-524), langkah 26 dan 27 (melepas Filter Land sebelum TC-FA-TDC-523; muat ulang tidak melepas Filter), langkah 28 dan 35 (mengganti dan mengembalikan isi tabel lewat seeding API). Langkah "Klik di luar panel" (22) adalah aksi TC-FA-TDC-525.
- Asersi chip hilang langkah 6 dan asersi badge titik hilang langkah 17 didahului anchor positif: chip `Building` tetap ada (langkah 5 pada field yang sama) dan badge titik tampil sebelum `[Clear Field]` (langkah 12).
- Filter Panel dibuka pada langkah 1 dan tetap terbuka sesudah `[Apply]` (8b.9): langkah 10 (blok TC-FA-TDC-524) dan langkah 19 sampai 21 (blok TC-FA-TDC-525) langsung memilih opsi atau mengubahnya tanpa klik icon Filter (klik icon itu menutup panel). Panel ditutup oleh langkah 22 (klik di luar panel), sehingga langkah 24 membukanya kembali; langkah 29 membuka panel sesudah muat ulang.
- Spec ini 35 langkah.
- Temuan untuk QA:
  - TC-FA-TDC-523 mensyaratkan enam user berbeda tercatat sebagai Modified By, padahal Example Data hanya memuat `Rina P` dan `System`; spec mengganti isi tabel (isi tabel B) lewat seeding API yang disediakan tim FE/BE, dan "N" pada `+N more` bergantung lebar field.
  - TC-FA-TDC-524 Expected a "tanpa angka" dan hilangnya badge titik diamati lewat komponen Badge Standalone Dot pada icon Filter; selector badge titik belum ada di repo (belum ada page-object Tax Depreciation Class), perlu dikonfirmasi tim FE.
  - TC-FA-TDC-522 Expected a/b ditulis sesudah Apply pada TC, sedangkan chip diamati di field sebelum Apply; spec mengasersi chip sebelum `[Apply]` dan tabel sesudahnya.
  - Email akun Total Control dan nama enam user Modified By tidak tertulis di TC.
