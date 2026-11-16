---
id: TC-FA-FAAC-E2E-133-filter-capitalization-threshold-nominal-berdesimal
title: "Filter Tabel Asset Class: Min dan Max pada Capitalization Threshold Membandingkan Nilai Tersimpan Termasuk Bagian Desimal"
layer: ui-e2e
priority: Medium
caseType: Edge
status: draft
sourceTc:
  - TC-FA-FAAC-706
sourceRules: ["§5#b2", "§4.1.1#r6", "§5#b3", "ST-23", "§4.1.1#r17", "§4.1.1#r19"]
smoke: []
dependsOn: []
trace:
  "§5#b2": 2
  "§4.1.1#r6": [5, 6, 9, 13, 14]
  "§5#b3": [5, 6, 9, 13, 14]
  "ST-23": 9
  "§4.1.1#r17": 14
  "§4.1.1#r19": 14
coverage:
  web: automated
---

# Filter Tabel Asset Class: Min dan Max pada Capitalization Threshold Membandingkan Nilai Tersimpan Termasuk Bagian Desimal

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (tab Asset Class pada Settings > Accounting). Hook `after` mengembalikan sesi ke akun default suite.
- Flag Guided Tooltip `guided_tooltip_seen_fa-asset-class` disetel true oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Data Pre-setup (hanya dibaca, tidak diubah): sembilan Asset Class contoh Example Data PRD §4.1.1 dengan nama literal dari Tabel Data Uji Pre-setup TC, termasuk HEAVY-EQ (Capitalization Threshold 5,000,000) dan IT-EQ (2,000,000).
- Data milik spec (seed di hook `before`, cleanup di hook `after`): Asset Class B-DEC (Class Name `Decimal Fixture`, Method Straight Line, Useful Life 60, Residual Value unit Amount 2500000.99, Tax Depreciation Class `Bukan bangunan – Kelompok 3`, Tax Method `Declining Balance`, Capitalization Threshold 1500.99, tampil `1,500.99`) dan B-DECZ (Class Name `Decimal Zero Fixture`, field lain sama, Residual Value Amount 2000000.00, Capitalization Threshold 3000000.00, tampil `3,000,000`). Precondition TC menyebutnya hasil pembuatan pada TC-FA-FAAC-704; spec membuat keduanya lewat seeding API sebagai precondition, tidak diasersi pembuatannya. Seed dan pembersihan disediakan tim FE/BE (lihat `suite.md`).
- Populasi tabel nyata: tabel Asset Class memuat lebih dari 25 baris (sembilan kelas contoh ditambah seed lain seperti `B-*`, `PMP-01`, `B-PAGE01` sampai `B-PAGE11`, `TEMP-EQ`, dan seed spec lain), sehingga sembilan kelas contoh tidak dijamin berada bersama pada halaman 1 dan baris seed lain dapat menyela atau ikut tampil. Asersi spec ini dibatasi pada keanggotaan dan urutan RELATIF antar baris contoh (atau pada baris yang dikenali lewat Search kode); baris seed lain tidak diasersi.
- Suite berjalan serial (`parallel: false`); spec ini tidak mengubah state global.

## Test Steps

### TC-FA-FAAC-706: Filter Min dan Max pada Capitalization Threshold membandingkan nilai tersimpan termasuk bagian desimal

1. Ketik Search `B-DEC`, tekan Enter
2. Verifikasi baris B-DEC dan B-DECZ tampil
3. Klik icon Filter untuk membuka Filter Panel
4. Isi Capitalization Threshold Min `1501`, klik `[Apply]`
5. Verifikasi baris B-DECZ tampil
6. Verifikasi baris B-DEC tidak tampil karena nilai tersimpan 1500.99 kurang dari 1501
7. Klik `[Clear Field]`, lalu `[Apply]`
8. Isi Capitalization Threshold Max `1500`, klik `[Apply]`
9. Verifikasi empty state `No results found` tampil dan baris B-DEC tidak tampil karena nilai tersimpan 1500.99 lebih dari 1500
10. Klik `[Clear Field]`, lalu `[Apply]`
11. Klik `(←)` pada kotak Search untuk menutup input dan mereset tabel
12. Isi Capitalization Threshold Min `1500` dan Max `1501`, klik `[Apply]`
13. Verifikasi baris B-DEC tampil
14. Verifikasi HEAVY-EQ, IT-EQ, dan B-DECZ tidak tampil
15. Klik `[Clear Field]`, lalu `[Apply]`

## Notes

- Langkah penghubung (S-03): langkah 1 (Search `B-DEC` untuk membatasi tabel pada dua baris milik spec sehingga asersi absence punya anchor positif pada surface yang sama, 8b butir 2; R-16), langkah 7 dan 10 (melepas filter antar kasus, S-09; sesuai langkah TC), langkah 11 (menutup Search sebelum kasus Min `1500` dan Max `1501` supaya kasus itu menguji Filter, bukan Search), langkah 15 (melepas filter di akhir spec, S-09).
- Langkah 1 dan 2 tidak ada di TC; Search membatasi tabel pada B-DEC dan B-DECZ untuk kasus Min `1501` dan Max `1500` (langkah 4 sampai 9), dengan baris B-DEC dan B-DECZ (langkah 2) serta B-DECZ (langkah 5) sebagai anchor positif. Search ditutup pada langkah 11 sehingga kasus Min `1500` dan Max `1501` (langkah 12 sampai 14) menguji Filter pada seluruh tabel: HEAVY-EQ dan IT-EQ (5,000,000 dan 2,000,000) tidak tampil karena di luar rentang, dengan baris B-DEC (langkah 13) sebagai anchor positif sebelum asersi absence.
- Nama literal B-DEC dan B-DECZ dipakai tanpa suffix `{runId}` karena asersi bergantung pada nilai tampil persis; keduanya milik spec ini dan dibersihkan di hook `after`. Kode literal yang sama dibuat lewat UI oleh spec 131 (suite serial; tiap spec membersihkan kelas yang dibuatnya; S-06, S-12).
- Temuan untuk QA: TC-FA-FAAC-706 memakai B-DEC dan B-DECZ sebagai "hasil TC pembuatan" pada TC-FA-FAAC-704; spec menyiapkannya lewat seeding API karena spec tidak boleh menumpang hasil spec lain (S-06). TC tidak menyebut hasil tabel untuk Max `1500` (diasumsikan kosong pada tabel yang dibatasi Search `B-DEC`).
