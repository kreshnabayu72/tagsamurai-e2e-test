---
id: TC-FA-TDC-E2E-179-popup-changelog-setup-column-geser-urutan-kolom
title: "Popup Changelog Setup Column: Geser Urutan Kolom"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TDC-643
coverage:
  web: automated
---

# Popup Changelog Setup Column: Geser Urutan Kolom

## Prerequisites

- Mode: FE+BE.
- Akun: Total Control (company uji Fixed Asset). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Akun dan email disediakan tim FE (email tidak tertulis di TC); password lewat `Spectra.env.FA_TC_PASSWORD`.
- Hook suite, seeding, dan flag Guided Tooltip mengikuti `suite.md`.
- Data Pre-setup (dibaca, tidak diubah; disediakan tim FE): `Fixture.fixedAssetTaxDepreciationClass.exampleData` berisi sembilan class Example Data PRD (BLD-NP, BLD-P, LAND, NB-1, NB-2, NB-4, NB-KHS, NB-OLD, NB-SL); `Fixture.fixedAssetTaxDepreciationClass.exampleDataChangelog` berisi 16 entri Popup Changelog sesuai Example Data Modal Changelog PRD. Konfigurasi kolom Popup Changelog dalam keadaan default (urutan `Date | Action | Class Code | Field | Old Value | New Value | Modified By`). Data Dinamis: tidak ada.
- Tabel "Kolom yang diuji" (parameter langkah 2 sampai 14, TC-FA-TDC-643):

  | Iterasi | Kolom | Posisi semula |
  |---|---|---|
  | 1 | Date | 1 |
  | 2 | Action | 2 |
  | 3 | Class Code | 3 |
  | 4 | Field | 4 |
  | 5 | Old Value | 5 |
  | 6 | New Value | 6 |
  | 7 | Modified By | 7 |

- Kemampuan teknis: riwayat Changelog diatur ke 16 entri Example Data lewat Fixture BE (disediakan tim FE/BE; mekanismenya tidak disebut TC, PRD, atau LLD); Popup Setup Column dengan drag handle dan Live Preview pada Popup Changelog; konfigurasi kolom Popup Changelog tersimpan di browser dan dibaca ulang setelah muat ulang halaman; pemulihan lewat langkah eksplisit (8b.14, R-24).
- State global yang diubah: urutan kolom Popup Changelog. Tiap iterasi mengembalikan kolom ke posisi semula (langkah 11 sampai 14). Hook `after` menghapus preferensi kolom di browser sebagai cadangan.

## Test Steps

### TC-FA-TDC-643: Geser urutan kolom di Popup Setup Column Popup Changelog

1. Klik icon Changelog

Untuk setiap baris tabel "Kolom yang diuji" (langkah 2 sampai 14), dengan `{kolom}` = nilai kolom Kolom dan `{posisi}` = nilai kolom Posisi semula pada iterasi itu:

2. Klik icon `⋯` pada header kolom Actions
3. Klik `Setup Column...`
4. Seret kolom `{kolom}` ke posisi paling atas daftar
5. Verifikasi Live Preview menempatkan `{kolom}` sebagai kolom pertama
6. Klik `[Save]`
7. Verifikasi urutan tabel sama dengan Live Preview dengan `{kolom}` sebagai kolom pertama
8. Muat ulang halaman (F5)
9. Klik icon Changelog untuk membuka kembali Popup Changelog
10. Verifikasi urutan tabel tetap dengan `{kolom}` sebagai kolom pertama setelah F5
11. Klik icon `⋯` pada header kolom Actions
12. Klik `Setup Column...`
13. Seret kolom `{kolom}` kembali ke posisi `{posisi}` daftar
14. Klik `[Save]`

15. Tutup Popup Changelog lewat ikon Close `(X)`

## Notes

- Langkah berulang (8b.7): langkah 2 sampai 14 diulang tujuh kali (satu iterasi per baris tabel "Kolom yang diuji"); parameter tiap iterasi hanya `{kolom}` dan `{posisi}`, tanpa langkah bersyarat, dan `Verifikasi` tetap satu per klausa (S-01). Dengan ekspansi spec ini 93 langkah (1 langkah pembuka, 7 x 13 langkah ulangan, dan 1 langkah penutup).
- Alasan lebih dari sekitar 35 langkah (dengan ekspansi): satu TC, satu topik (geser urutan kolom Setup Column Popup Changelog), satu kelas harness; tiap iterasi berdiri sendiri sehingga kegagalan satu iterasi tidak menghapus makna iterasi lain, dan pengulangan per kolom berasal dari TC-FA-TDC-643 ("Untuk tiap kolom").
- Interpretasi TC-FA-TDC-643: langkah 4 TC dijalankan per kolom lalu urutan dipulihkan (langkah 13 dan 14) sebelum kolom berikutnya agar tiap iterasi dimulai dari urutan default. Pada iterasi 1 (Date) menyeret ke posisi paling atas tidak mengubah urutan; langkah 5, 7, dan 10 tetap mengasersi Date sebagai kolom pertama. Muat ulang halaman (langkah 8) menutup Popup Changelog sehingga dibuka kembali (langkah 9). Pemulihan urutan dilakukan di langkah 13 dan 14 (8b.14, R-24).
- Langkah penghubung (S-03): langkah 8 dan 9 (muat ulang dan membuka kembali Popup), langkah 11 sampai 14 (mengembalikan urutan kolom), langkah 15 (menutup Popup).
- Temuan untuk QA:
  - Email akun Total Control tidak tertulis di TC.
  - TC-FA-TDC-643 tidak menyatakan pemulihan urutan di antara iterasi; spec memulihkan per iterasi.
  - TC-FA-TDC-643 menyebut header kolom `Actions`, sedangkan TC-FA-TDC-613 menyebut `Column Visibility (⋯)`.
  - TC-FA-TDC-643 butir a (Date) menyeret kolom yang sudah berada di posisi pertama sehingga tidak mengubah urutan.
