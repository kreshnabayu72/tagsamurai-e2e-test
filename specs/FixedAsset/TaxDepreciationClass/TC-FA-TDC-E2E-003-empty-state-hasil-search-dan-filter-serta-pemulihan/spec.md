---
id: TC-FA-TDC-E2E-003-empty-state-hasil-search-dan-filter-serta-pemulihan
title: "Empty State Hasil Search dan Filter serta Pemulihan Tabel"
layer: ui-e2e
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-TDC-9
  - TC-FA-TDC-10
  - TC-FA-TDC-11
  - TC-FA-TDC-12
sourceRules: ["ST-23", "FATDC-LOGIC-02k", "§7.1#p2", "§5#b2", "FATDC-LOGIC-02a", "§4.1.1#b7"]
smoke: []
dependsOn: []
trace:
  "ST-23": [2, 4, 7, 17, 24]
  "FATDC-LOGIC-02k": [3, 18]
  "§7.1#p2": [3, 18]
  "§5#b2": 10
  "FATDC-LOGIC-02a": [12, 26]
  "§4.1.1#b7": [19, 27]
anchor: [9]
coverage:
  web: automated
---

# Empty State Hasil Search dan Filter serta Pemulihan Tabel

## Prerequisites

- Mode: FE+BE.
- Akun: Total Control (company uji Fixed Asset). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Akun dan email disediakan tim FE (email tidak tertulis di TC); password lewat `Spectra.env.FA_TC_PASSWORD`.
- Hook suite, seeding, dan flag Guided Tooltip mengikuti `suite.md`.
- Data Pre-setup (dibaca, tidak diubah; `Fixture.fixedAssetTaxDepreciationClass.seedClasses`, disediakan tim FE): tujuh class seed bawaan NB-1, NB-2, NB-3, NB-4, BLD-P, BLD-NP, LAND belum diubah; tabel muat pada satu halaman. Data uji: kata kunci Search `zzzz`; Filter Used By Min `99` dan Max `100` (tidak ada class yang cocok). Data Dinamis: tidak ada.
- Kemampuan teknis: seeding tujuh class seed lewat API (`suite.md`).
- State global yang diubah: Search dan Filter pada tabel (dikosongkan oleh langkah di spec dan oleh `beforeEach` suite).

## Test Steps

### Search kosong tanpa tombol Restore (TC-FA-TDC-9)

1. Ketik Search `zzzz`, tekan Enter
2. Verifikasi Illustration tampil dengan Title `No results found` dan Description `Try adjusting your search or filter.`
3. Verifikasi tombol `Restore default classes` tidak tampil
4. Verifikasi tidak ada baris data

### Pemulihan setelah Search dikosongkan (TC-FA-TDC-11)

5. Klik `(←)` pada kotak Search
6. Ketik Search `zzzz`, tekan Enter
7. Verifikasi tabel menampilkan `No results found`
8. Klik icon `(✕)` pada input Search
9. Verifikasi input Search kosong
10. Verifikasi tabel masih menampilkan `No results found`
11. Tekan Enter pada input yang kosong
12. Verifikasi 7 baris seed tampil kembali

### Filter kosong tanpa tombol Restore dan dengan chip Clear all (TC-FA-TDC-10)

13. Klik `(←)` pada kotak Search
14. Klik icon Filter
15. Isi Used By Min `99` dan Max `100`
16. Klik `[Apply]`
17. Verifikasi Illustration tampil dengan Title `No results found` dan Description `Try adjusting your search or filter.`
18. Verifikasi tombol `Restore default classes` tidak tampil
19. Verifikasi chip filter aktif dan `Clear all` tampil di atas tabel

### Pemulihan dengan Clear all (TC-FA-TDC-12)

20. Klik `Clear all` pada chip filter
21. Klik icon Filter
22. Isi Used By Min `99` dan Max `100`
23. Klik `[Apply]`
24. Verifikasi tabel menampilkan `No results found`
25. Klik `Clear all` pada chip filter
26. Verifikasi 7 baris seed tampil kembali
27. Verifikasi chip filter hilang

## Notes

- Urutan TC dalam spec: TC-FA-TDC-9, 11, 10, 12 (kasus Search dahulu, lalu kasus Filter) supaya state Search dan Filter tidak bercampur.
- Langkah penghubung (S-03): langkah 5 (menutup input Search lewat `(←)` sehingga tabel kembali penuh sebelum TC berikutnya), langkah 13 (menutup input Search sebelum Filter), dan langkah 20 (menghapus filter TC-FA-TDC-10 sebelum TC-FA-TDC-12 menerapkannya lagi; S-09).
- Asersi absence langkah 3, 4, dan 18 punya anchor positif pada `Verifikasi` Empty State langkah 2 dan 17; asersi chip hilang langkah 27 didahului anchor langkah 26 (butir 8b.2).
- Temuan untuk QA:
  - TC-FA-TDC-11 tidak menyebut apa yang tampil pada kotak Search sesudah `(✕)` selain "input kosong"; spec mengikuti TC.
  - Email akun Total Control tidak tertulis di TC.
