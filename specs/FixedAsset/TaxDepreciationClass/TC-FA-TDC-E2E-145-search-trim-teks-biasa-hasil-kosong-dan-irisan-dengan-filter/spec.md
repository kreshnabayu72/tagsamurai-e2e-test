---
id: TC-FA-TDC-E2E-145-search-trim-teks-biasa-hasil-kosong-dan-irisan-dengan-filter
title: "Search: Trim, Teks Biasa, Hasil Kosong, dan Irisan dengan Filter"
layer: ui-e2e
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-TDC-498
  - TC-FA-TDC-499
  - TC-FA-TDC-500
  - TC-FA-TDC-501
  - TC-FA-TDC-502
sourceRules: ["§5#b2", "ST-23", "§7.1#p2", "§4.1.1#r4", "§4.1.1#r8", "§4.7#r5", "§5#b6"]
smoke: []
dependsOn: []
trace:
  "§5#b2": [2, 5, 7, 9, 11, 13, 18, 23, 32]
  "ST-23": 15
  "§7.1#p2": 16
  "§4.1.1#r4": [23, 30]
  "§4.1.1#r8": [23, 30]
  "§4.7#r5": [23, 32]
  "§5#b6": [24, 33]
anchor: [3]
coverage:
  web: automated
---

# Search: Trim, Teks Biasa, Hasil Kosong, dan Irisan dengan Filter

## Prerequisites

- Mode: FE+BE.
- Akun: Total Control (company uji Fixed Asset). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Akun dan email disediakan tim FE (email tidak tertulis di TC); password lewat `Spectra.env.FA_TC_PASSWORD`.
- Hook suite, seeding, dan flag Guided Tooltip mengikuti `suite.md`.
- Data Pre-setup (dibaca, tidak diubah; `Fixture.fixedAssetTaxDepreciationClass.exampleData`, disediakan tim FE): sembilan class Example Data PRD (BLD-NP, BLD-P, LAND, NB-1, NB-2, NB-4, NB-KHS, NB-OLD, NB-SL) dengan nilai kolom persis Example Data; tabel muat pada satu halaman. Class Name yang dicari: NB-KHS `Kelompok khusus pernah diposting`, NB-OLD `Kelompok khusus lama`, NB-SL `Kelompok khusus Straight Line`, NB-1 `Bukan bangunan – Kelompok 1`, NB-2 `Bukan bangunan – Kelompok 2`, NB-4 `Bukan bangunan – Kelompok 4`. Asset Type NB-1, NB-2, NB-4, NB-KHS, NB-OLD, NB-SL `Non-building`; Allowed Methods NB-1, NB-2, NB-4, NB-KHS memuat `Declining Balance`.
- Data uji (keyword Search, literal TC): `  NB-1  ` (spasi di awal dan akhir), `Kelompok khusus`, `Kelompok  khusus` (dua spasi di tengah), tiga spasi, `NB-.`, `.*`, `tidak ada class ini`, `Kelompok`; Filter Asset Type `Non-building` dan Allowed Methods `Declining Balance`.
- Data Dinamis: tidak ada.
- Kemampuan teknis: seeding sembilan class Example Data lewat API (`suite.md`); membaca isi input Search.
- State global yang diubah: Search dan Filter pada tabel (dilepas oleh langkah di spec dan oleh `beforeEach` suite).

## Test Steps

### Search men-trim spasi awal dan akhir, spasi tengah dipertahankan (TC-FA-TDC-498)

1. Ketik Search `  NB-1  ` (spasi di awal dan akhir), tekan Enter
2. Verifikasi tabel hanya menampilkan baris NB-1
3. Verifikasi isi input Search di layar tidak berubah (tetap `  NB-1  `)
4. Ganti isi kotak search dengan `Kelompok khusus`, tekan Enter
5. Verifikasi tabel menampilkan tepat tiga baris: NB-KHS, NB-OLD, dan NB-SL
6. Ganti isi kotak search dengan `Kelompok  khusus` (dua spasi di tengah), tekan Enter
7. Verifikasi tabel menampilkan `No results found` karena spasi di tengah tidak disentuh
8. Ganti isi kotak search dengan tiga spasi, tekan Enter
9. Verifikasi query hanya spasi diperlakukan sebagai kosong: tabel menampilkan 9 baris

### Kata kunci Search dicocokkan sebagai teks biasa (TC-FA-TDC-499)

10. Ganti isi kotak search dengan `NB-.`, tekan Enter
11. Verifikasi tabel menampilkan `No results found` (titik tidak dianggap pola)
12. Ganti isi kotak search dengan `.*`, tekan Enter
13. Verifikasi tabel menampilkan `No results found` (`.*` tidak dianggap pola)

### Search tanpa hasil menampilkan Empty State (TC-FA-TDC-500)

14. Ganti isi kotak search dengan `tidak ada class ini`, tekan Enter
15. Verifikasi Illustration tampil dengan Title `No results found` dan Description `Try adjusting your search or filter.`
16. Verifikasi tidak ada tombol aksi pada Empty State

### Alur Search lalu Filter menghasilkan irisan (TC-FA-TDC-501)

17. Ganti isi kotak search dengan `Kelompok`, tekan Enter
18. Verifikasi setelah Search tabel menampilkan tepat enam baris: NB-1, NB-2, NB-4, NB-KHS, NB-OLD, dan NB-SL
19. Klik icon Filter
20. Pilih Asset Type `Non-building`
21. Pilih Allowed Methods `Declining Balance`
22. Klik `[Apply]`
23. Verifikasi setelah Apply tabel menampilkan tepat empat baris: NB-1, NB-2, NB-4, dan NB-KHS
24. Verifikasi keyword Search `Kelompok` tetap tampil di input
25. Klik `[Clear Field]` lalu `[Apply]` pada Filter Panel
26. Klik `(←)` pada kotak Search

### Alur Filter lalu Search menghasilkan irisan yang sama (TC-FA-TDC-502)

27. Pilih Asset Type `Non-building`
28. Pilih Allowed Methods `Declining Balance`
29. Klik `[Apply]`
30. Verifikasi setelah Apply tabel menampilkan tepat empat baris: NB-1, NB-2, NB-4, dan NB-KHS
31. Ketik Search `Kelompok`, tekan Enter
32. Verifikasi setelah Search tabel menampilkan tepat empat baris NB-1, NB-2, NB-4, dan NB-KHS (identik dengan alur Search lalu Filter)
33. Verifikasi kriteria Filter tetap aktif
34. Klik `[Clear Field]` lalu `[Apply]` pada Filter Panel

## Notes

- Langkah penghubung (S-03): langkah 25 dan 26 (melepas Filter dan menutup kotak Search sebelum TC-FA-TDC-502 agar kedua alur mulai dari tabel penuh; S-09), langkah 34 (melepas Filter di akhir spec). Langkah "Kosongkan Search, ketik X" di TC ditulis "ganti isi kotak search dengan X" (8b.9).
- Filter Panel dibuka pada langkah 19 dan tetap terbuka sesudah `[Apply]` (8b.9), sehingga blok TC-FA-TDC-502 langsung memilih Asset Type pada langkah 27 tanpa klik icon Filter (klik icon itu menutup panel).
- Asersi `No results found` langkah 7, 11, dan 13 adalah Empty State hasil Search yang diproses, anchor positif yang sah (8b.2); asersi tanpa tombol aksi langkah 16 didahului anchor langkah 15.
- Temuan untuk QA:
  - TC-FA-TDC-500 Expected "tanpa tombol aksi" tidak menyebut tombol mana yang dimaksud; spec mengasersi tidak ada tombol aksi pada Empty State.
  - TC-FA-TDC-498 Expected a "isi input Search di layar tidak berubah" tidak menyebut nilai pembanding; spec memakai teks yang diketik persis.
  - TC-FA-TDC-501 dan 502 tidak menyebut kriteria Filter yang aktif diamati lewat badge titik atau panel; spec mengasersi "kriteria Filter tetap aktif" apa adanya.
  - Asumsi spec, belum dikonfirmasi FE: Filter Panel tetap terbuka sesudah pelepasan Filter lewat `[Clear Field]` dan `[Apply]` serta klik `(←)` pada kotak Search (langkah 25 dan 26), sehingga langkah 27 memilih Asset Type tanpa klik icon Filter; TC dan PRD tidak menyebutnya (sama dengan asumsi di spec 248). Perlu konfirmasi FE.
  - Email akun Total Control tidak tertulis di TC.
