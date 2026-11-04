---
id: TC-FA-TDC-E2E-252-popup-changelog-setup-column-pin-dan-unpin-tujuh-kolom-default
title: "Popup Changelog Setup Column: Pin dan Unpin Tujuh Kolom Default"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TDC-644
coverage:
  web: automated
---

# Popup Changelog Setup Column: Pin dan Unpin Tujuh Kolom Default

## Prerequisites

- Mode: FE+BE.
- Akun: Total Control (company uji Fixed Asset). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Akun dan email disediakan tim FE (email tidak tertulis di TC); password lewat `Spectra.env.FA_TC_PASSWORD`.
- Hook suite, seeding, dan flag Guided Tooltip mengikuti `suite.md`.
- Data Pre-setup (dibaca, tidak diubah; disediakan tim FE): `Fixture.fixedAssetTaxDepreciationClass.exampleData` berisi sembilan class Example Data PRD (BLD-NP, BLD-P, LAND, NB-1, NB-2, NB-4, NB-KHS, NB-OLD, NB-SL); `Fixture.fixedAssetTaxDepreciationClass.exampleDataChangelog` berisi 16 entri Popup Changelog sesuai Example Data Modal Changelog PRD. Konfigurasi kolom Popup Changelog dalam keadaan default (tujuh kolom tampil, tanpa kolom di-Pin). Data Dinamis: tidak ada.
- Tabel "Kolom yang diuji" (parameter langkah 2 sampai 17, TC-FA-TDC-644):

  | Iterasi | Kolom |
  |---|---|
  | 1 | Date |
  | 2 | Action |
  | 3 | Class Code |
  | 4 | Field |
  | 5 | Old Value |
  | 6 | New Value |
  | 7 | Modified By |

- Kemampuan teknis: riwayat Changelog diatur ke 16 entri Example Data lewat Fixture BE (disediakan tim FE/BE; mekanismenya tidak disebut TC, PRD, atau LLD); Popup Setup Column dengan icon Pin pada Popup Changelog; ukuran viewport yang membuat tabel Popup Changelog dapat di-scroll horizontal (disediakan tim FE; lihat Temuan untuk QA); konfigurasi kolom Popup Changelog tersimpan di browser dan dibaca ulang setelah muat ulang halaman; pemulihan lewat langkah eksplisit (8b.14, R-24).
- State global yang diubah: Pin kolom Popup Changelog. Tiap iterasi melakukan Unpin kolom yang di-Pin (langkah 12 sampai 15). Hook `after` menghapus preferensi kolom di browser sebagai cadangan.

## Test Steps

### TC-FA-TDC-644: Pin dan unpin kolom di Popup Setup Column Popup Changelog

1. Klik icon Changelog

Untuk setiap baris tabel "Kolom yang diuji" (langkah 2 sampai 17), dengan `{kolom}` = nilai kolom Kolom pada iterasi itu:

2. Klik icon `⋯` pada header kolom Actions
3. Klik `Setup Column...`
4. Klik icon Pin pada baris kolom `{kolom}`
5. Klik `[Save]`
6. Scroll tabel secara horizontal
7. Verifikasi kolom `{kolom}` membeku (sticky) saat tabel di-scroll horizontal setelah Pin dan Save
8. Muat ulang halaman (F5)
9. Klik icon Changelog untuk membuka kembali Popup Changelog
10. Scroll tabel secara horizontal
11. Verifikasi kolom `{kolom}` tetap membeku (sticky) saat tabel di-scroll horizontal setelah F5
12. Klik icon `⋯` pada header kolom Actions
13. Klik `Setup Column...`
14. Klik icon Pin pada baris kolom `{kolom}` (Unpin)
15. Klik `[Save]`
16. Scroll tabel secara horizontal
17. Verifikasi kolom `{kolom}` ikut bergeser saat tabel di-scroll horizontal setelah Unpin

18. Tutup Popup Changelog lewat ikon Close `(X)`

## Notes

- Langkah berulang (8b.7): langkah 2 sampai 17 diulang tujuh kali (satu iterasi per baris tabel "Kolom yang diuji"); parameter tiap iterasi hanya `{kolom}`, tanpa langkah bersyarat, dan `Verifikasi` tetap satu per klausa (S-01). Dengan ekspansi spec ini 114 langkah (1 langkah pembuka, 7 x 16 langkah ulangan, dan 1 langkah penutup).
- Alasan lebih dari sekitar 35 langkah (dengan ekspansi): satu TC, satu topik (Pin dan Unpin Setup Column Popup Changelog), satu kelas harness; tiap iterasi berdiri sendiri sehingga kegagalan satu iterasi tidak menghapus makna iterasi lain, dan pengulangan per kolom berasal dari TC-FA-TDC-644 ("Untuk tiap kolom").
- Interpretasi TC-FA-TDC-644: langkah 4 dan 5 TC dijalankan per kolom; Unpin (langkah 14 dan 15) dilakukan pada iterasi yang sama sehingga tiap iterasi dimulai tanpa kolom di-Pin. Muat ulang halaman (langkah 8) menutup Popup Changelog sehingga dibuka kembali (langkah 9). Scroll horizontal diulang sebelum tiap `Verifikasi` sticky (S-14). Pemulihan Pin dilakukan di langkah 14 dan 15 (8b.14, R-24).
- Langkah penghubung (S-03): langkah 8 dan 9 (muat ulang dan membuka kembali Popup), langkah 6, 10, dan 16 (scroll tabel horizontal sebelum `Verifikasi` sticky), langkah 18 (menutup Popup Changelog).
- Temuan untuk QA:
  - Email akun Total Control tidak tertulis di TC.
  - TC-FA-TDC-644 tidak menyebut viewport yang membuat tabel Popup Changelog dapat di-scroll horizontal; dengan tujuh kolom default pada viewport lebar, Pin tidak teramati.
  - TC-FA-TDC-644 tidak menyatakan Unpin per iterasi; spec memakai Unpin per iterasi.
  - TC-FA-TDC-644 menyebut header kolom `Actions`, sedangkan TC-FA-TDC-613 menyebut `Column Visibility (⋯)`.
