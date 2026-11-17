---
id: TC-FA-TDC-E2E-251-popup-changelog-setup-column-ceklis-dan-unceklis-tujuh-kolom-default
title: "Popup Changelog Setup Column: Ceklis dan Unceklis Tujuh Kolom Default"
layer: ui-e2e
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TDC-642
sourceRules: ["§4.1.1#r25", "§4.1.1#r26", "§4.1.1#r27", "§4.1.1#r28", "§4.1.1#r29", "§4.1.1#r30", "§4.1.1#r31", "§5#b9"]
smoke: []
dependsOn: []
trace:
  "§4.1.1#r25": [5, 15]
  "§4.1.1#r26": [5, 15]
  "§4.1.1#r27": [5, 15]
  "§4.1.1#r28": [5, 15]
  "§4.1.1#r29": [5, 15]
  "§4.1.1#r30": [5, 15]
  "§4.1.1#r31": [5, 15]
  "§5#b9": [7, 10]
coverage:
  web: automated
---

# Popup Changelog Setup Column: Ceklis dan Unceklis Tujuh Kolom Default

## Prerequisites

- Mode: FE+BE.
- Akun: Total Control (company uji Fixed Asset). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Akun dan email disediakan tim FE (email tidak tertulis di TC); password lewat `Spectra.env.FA_TC_PASSWORD`.
- Hook suite, seeding, dan flag Guided Tooltip mengikuti `suite.md`.
- Data Pre-setup (dibaca, tidak diubah; disediakan tim FE): `Fixture.fixedAssetTaxDepreciationClass.exampleData` berisi sembilan class Example Data PRD (BLD-NP, BLD-P, LAND, NB-1, NB-2, NB-4, NB-KHS, NB-OLD, NB-SL); `Fixture.fixedAssetTaxDepreciationClass.exampleDataChangelog` berisi 16 entri Popup Changelog sesuai Example Data Modal Changelog PRD. Konfigurasi kolom Popup Changelog dalam keadaan default (tujuh kolom tampil). Data Dinamis: tidak ada.
- Tabel "Kolom yang diuji" (parameter langkah 2 sampai 15, TC-FA-TDC-642):

  | Iterasi | Kolom |
  |---|---|
  | 1 | Date |
  | 2 | Action |
  | 3 | Class Code |
  | 4 | Field |
  | 5 | Old Value |
  | 6 | New Value |
  | 7 | Modified By |

- Kemampuan teknis: riwayat Changelog diatur ke 16 entri Example Data lewat Fixture BE (disediakan tim FE/BE; mekanismenya tidak disebut TC, PRD, atau LLD); Popup Setup Column dengan Live Preview pada Popup Changelog; konfigurasi kolom Popup Changelog tersimpan di browser dan dibaca ulang setelah muat ulang halaman; pemulihan lewat langkah eksplisit (8b.14, R-24).
- State global yang diubah: konfigurasi kolom Popup Changelog. Tiap iterasi mengembalikan kolom yang disembunyikan (langkah 12 sampai 14). Hook `after` menghapus preferensi kolom di browser sebagai cadangan.

## Test Steps

### TC-FA-TDC-642: Ceklis dan unceklis di Popup Setup Column Popup Changelog

1. Klik icon Changelog

Untuk setiap baris tabel "Kolom yang diuji" (langkah 2 sampai 15), dengan `{kolom}` = nilai kolom Kolom pada iterasi itu:

2. Klik icon `⋯` pada header kolom Actions
3. Klik `Setup Column...`
4. Hapus centang kolom `{kolom}`
5. Verifikasi kolom `{kolom}` hilang dari Live Preview setelah uncheck
6. Klik `[Save]`
7. Verifikasi kolom `{kolom}` hilang dari tabel setelah Save
8. Muat ulang halaman (F5)
9. Klik icon Changelog untuk membuka kembali Popup Changelog
10. Verifikasi kolom `{kolom}` tetap hilang dari tabel setelah F5
11. Klik icon `⋯` pada header kolom Actions
12. Klik `Setup Column...`
13. Centang kolom `{kolom}`
14. Klik `[Save]`
15. Verifikasi kolom `{kolom}` tampil kembali di tabel setelah check ulang dan Save

16. Tutup Popup Changelog lewat ikon Close `(X)`

## Notes

- Langkah berulang (8b.7): langkah 2 sampai 15 diulang tujuh kali (satu iterasi per baris tabel "Kolom yang diuji"); parameter tiap iterasi hanya `{kolom}`, tanpa langkah bersyarat, dan `Verifikasi` tetap satu per klausa (S-01). Dengan ekspansi spec ini 100 langkah (1 langkah pembuka, 7 x 14 langkah ulangan, dan 1 langkah penutup).
- Alasan lebih dari sekitar 35 langkah (dengan ekspansi): satu TC, satu topik (ceklis dan unceklis Setup Column Popup Changelog), satu kelas harness; tiap iterasi berdiri sendiri sehingga kegagalan satu iterasi tidak menghapus makna iterasi lain, dan pengulangan per kolom berasal dari TC-FA-TDC-642 ("Untuk tiap kolom").
- Interpretasi TC-FA-TDC-642: langkah 4 TC dijalankan per kolom lalu dipulihkan (langkah 13 dan 14) sebelum kolom berikutnya, karena menyembunyikan ketujuh kolom sekaligus tidak mungkin akibat guard satu kolom tersisa (TC-FA-TDC-647). Muat ulang halaman (langkah 8) menutup Popup Changelog sehingga dibuka kembali (langkah 9). Pemulihan Setup Column dilakukan di langkah 12 sampai 14 (8b.14, R-24).
- Langkah penghubung (S-03): langkah 8 dan 9 (muat ulang dan membuka kembali Popup), langkah 12 sampai 14 (check ulang kolom), langkah 16 (menutup Popup Changelog).
- Temuan untuk QA:
  - Email akun Total Control tidak tertulis di TC.
  - TC-FA-TDC-642 langkah 4 dan 5 tidak menyatakan apakah kolom dipulihkan per iterasi; langkah 6 menyebut "check kolom yang disembunyikan" tanpa mengatakan kapan. Spec memakai pemulihan per iterasi.
  - TC-FA-TDC-642 menyebut header kolom `Actions`, sedangkan TC-FA-TDC-613 menyebut `Column Visibility (⋯)`.
  - TC-FA-TDC-642 tidak menyatakan keadaan Popup Changelog sesudah muat ulang halaman; spec membukanya kembali.
