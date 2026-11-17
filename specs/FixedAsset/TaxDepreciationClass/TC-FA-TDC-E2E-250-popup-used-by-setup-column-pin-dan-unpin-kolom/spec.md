---
id: TC-FA-TDC-E2E-250-popup-used-by-setup-column-pin-dan-unpin-kolom
title: "Popup Used By Setup Column: Pin dan Unpin Kolom"
layer: ui-e2e
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TDC-599
sourceRules: []
smoke: []
dependsOn: []
trace:
anchor: [7, 11, 17]
coverage:
  web: automated
---

# Popup Used By Setup Column: Pin dan Unpin Kolom

## Prerequisites

- Mode: FE+BE.
- Akun: Total Control (company uji Fixed Asset). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Akun dan email disediakan tim FE (email tidak tertulis di TC); password lewat `Spectra.env.FA_TC_PASSWORD`.
- Hook suite, seeding, dan flag Guided Tooltip mengikuti `suite.md`.
- Data Pre-setup (dibaca, tidak diubah; disediakan tim FE lewat seeding API, `Fixture.fixedAssetTaxDepreciationClass`, fixture belum ada), kunci `exampleData` ditambah pemakai NB-1: sembilan class Example Data PRD (BLD-NP, BLD-P, LAND, NB-1, NB-2, NB-4, NB-KHS, NB-OLD, NB-SL) dengan nilai kolom persis Example Data; NB-1 dipakai 5 Asset Class: `AC-01 – Mesin Produksi` (Straight Line, 12 Asset Name), `AC-02 – Peralatan Kantor` (Straight Line, 30), `AC-03 – Kendaraan Operasional` (Declining Balance, 7), `AC-04 – Komputer` (Declining Balance, 25), `AC-05 – Furnitur` (Straight Line, 18). Tidak ada kolom yang di-pin pada keadaan awal.
- Tabel "Kolom yang diuji" (parameter langkah 2 sampai 17):

  | Iterasi | Kolom |
  |---|---|
  | 1 | Asset Class |
  | 2 | Tax Method |
  | 3 | Asset Names |

- Kemampuan teknis: Popup Setup Column pada Popup Used By; icon Pin; scroll horizontal tabel Popup Used By (viewport atau lebar popup yang membuat tabel dapat di-scroll horizontal disediakan tim FE); konfigurasi kolom Popup Used By tersimpan di browser dan dibaca ulang setelah muat ulang halaman; pemulihan lewat langkah eksplisit (8b.14, R-24).
- State global yang diubah: Pin kolom Popup Used By. Tiap iterasi langkah 2 sampai 17 meng-unpin kolom yang di-pin (langkah 13 sampai 15). Hook `after` menghapus preferensi kolom di browser sebagai cadangan.

## Test Steps

### TC-FA-TDC-599: Pin dan unpin kolom di Popup Setup Column Popup Used By: 3 kolom default

1. Klik angka `5` pada baris NB-1 untuk membuka Popup Used By

Untuk setiap baris tabel "Kolom yang diuji" (langkah 2 sampai 17), dengan `{kolom}` = nilai kolom Kolom pada iterasi itu:

2. Klik icon `⋯` pada header kolom Actions
3. Klik `Setup Column...`
4. Klik icon Pin pada baris kolom `{kolom}`
5. Klik `[Save]`
6. Scroll tabel Popup Used By secara horizontal
7. Verifikasi kolom `{kolom}` membeku (sticky) saat tabel di-scroll horizontal
8. Muat ulang halaman (F5)
9. Klik angka `5` pada baris NB-1 untuk membuka kembali Popup Used By
10. Scroll tabel Popup Used By secara horizontal
11. Verifikasi kolom `{kolom}` tetap membeku setelah F5
12. Klik icon `⋯` pada header kolom Actions
13. Klik `Setup Column...`
14. Klik icon Pin pada baris kolom `{kolom}` (Unpin)
15. Klik `[Save]`
16. Scroll tabel Popup Used By secara horizontal
17. Verifikasi kolom `{kolom}` ikut bergeser saat tabel di-scroll setelah Unpin

18. Tutup Popup Used By lewat ikon Close `(X)`

## Notes

- Langkah berulang (8b.7): langkah 2 sampai 17 diulang tiga kali (satu iterasi per baris tabel "Kolom yang diuji"); parameter tiap iterasi hanya `{kolom}`, tanpa langkah bersyarat, dan `Verifikasi` tetap satu per klausa (S-01). Dengan ekspansi spec ini 50 langkah (1 langkah pembuka, 3 x 16 langkah berulang, dan 1 langkah penutup).
- Alasan lebih dari sekitar 35 langkah (dengan ekspansi): satu topik (Pin kolom Popup Used By), satu kelas harness, dan tiap iterasi berdiri sendiri sehingga kegagalan satu iterasi tidak menghapus makna iterasi lain; pengulangan per kolom berasal dari TC-FA-TDC-599 ("Untuk tiap kolom") dan hanya satu TC.
- Interpretasi TC-FA-TDC-599: langkah 4 dan 5 TC dijalankan per kolom (Pin, Save, scroll, F5, lalu Unpin dan Save) sebelum kolom berikutnya sehingga tiap iterasi mulai tanpa kolom ter-pin. Scroll horizontal ditambahkan sesudah muat ulang (langkah 10) dan sesudah Unpin (langkah 16) karena "membeku" dan "ikut bergeser" hanya teramati saat tabel di-scroll.
- Langkah penghubung (S-03): langkah 8 dan 9 (muat ulang dan membuka kembali popup), langkah 12 sampai 15 (Unpin yang sekaligus memulihkan Setup Column; 8b.14, R-24), langkah 18 (menutup popup). Tabel utama memuat sembilan baris pada satu halaman; baris NB-1 tidak perlu dicari lewat Search (8b.13).
- Temuan untuk QA:
  - TC-FA-TDC-599 tidak menyebut lebar viewport atau popup yang membuat tabel Popup Used By (tiga kolom) dapat di-scroll horizontal; tanpa itu "membeku saat scroll horizontal" tidak teramati.
  - TC-FA-TDC-599 tidak menyatakan apakah kolom yang di-pin dipulihkan di antara kolom; spec meng-unpin tiap kolom dalam iterasinya.
  - Email akun Total Control tidak tertulis di TC.
