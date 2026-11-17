---
id: TC-FA-TDC-E2E-168-popup-used-by-setup-column-ceklis-unceklis-dan-guard-satu-kolom-tersisa
title: "Popup Used By Setup Column: Ceklis dan Unceklis serta Guard Satu Kolom Tersisa"
layer: ui-e2e
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TDC-597
  - TC-FA-TDC-602
sourceRules: ["§4.1.6#r1", "§4.1.6#r2", "§4.1.6#r3"]
smoke: []
dependsOn: []
trace:
  "§4.1.6#r1": [5, 7, 10, 15]
  "§4.1.6#r2": [5, 7, 10, 15]
  "§4.1.6#r3": [5, 7, 10, 15]
anchor: [21, 22, 28, 29]
coverage:
  web: automated
---

# Popup Used By Setup Column: Ceklis dan Unceklis serta Guard Satu Kolom Tersisa

## Prerequisites

- Mode: FE+BE.
- Akun: Total Control (company uji Fixed Asset). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Akun dan email disediakan tim FE (email tidak tertulis di TC); password lewat `Spectra.env.FA_TC_PASSWORD`.
- Hook suite, seeding, dan flag Guided Tooltip mengikuti `suite.md`.
- Data Pre-setup (dibaca, tidak diubah; disediakan tim FE lewat seeding API, `Fixture.fixedAssetTaxDepreciationClass`, fixture belum ada), kunci `exampleData` ditambah pemakai NB-1: sembilan class Example Data PRD (BLD-NP, BLD-P, LAND, NB-1, NB-2, NB-4, NB-KHS, NB-OLD, NB-SL) dengan nilai kolom persis Example Data; NB-1 dipakai 5 Asset Class: `AC-01 – Mesin Produksi` (Straight Line, 12 Asset Name), `AC-02 – Peralatan Kantor` (Straight Line, 30), `AC-03 – Kendaraan Operasional` (Declining Balance, 7), `AC-04 – Komputer` (Declining Balance, 25), `AC-05 – Furnitur` (Straight Line, 18).
- Tabel "Kolom yang diuji" (parameter langkah 2 sampai 15, TC-FA-TDC-597):

  | Iterasi | Kolom |
  |---|---|
  | 1 | Asset Class |
  | 2 | Tax Method |
  | 3 | Asset Names |

- Kemampuan teknis: Popup Setup Column dan Overlay Column Visibility pada Popup Used By; hover untuk tooltip; konfigurasi kolom Popup Used By tersimpan di browser dan dibaca ulang setelah muat ulang halaman; pemulihan lewat langkah eksplisit (8b.14, R-24).
- State global yang diubah: konfigurasi kolom Popup Used By. Tiap iterasi langkah 2 sampai 15 mengembalikan kolom yang disembunyikan (langkah 13 dan 14), dan langkah 30 serta 31 mengembalikan kolom yang disembunyikan lewat Overlay. Hook `after` menghapus preferensi kolom di browser sebagai cadangan.

## Test Steps

### TC-FA-TDC-597: Ceklis dan unceklis di Popup Setup Column Popup Used By: 3 kolom default

1. Klik angka `5` pada baris NB-1 untuk membuka Popup Used By

Untuk setiap baris tabel "Kolom yang diuji" (langkah 2 sampai 15), dengan `{kolom}` = nilai kolom Kolom pada iterasi itu:

2. Klik icon `⋯` pada header kolom Actions
3. Klik `Setup Column...`
4. Hapus centang kolom `{kolom}`
5. Verifikasi kolom `{kolom}` hilang dari Live Preview setelah uncheck
6. Klik `[Save]`
7. Verifikasi kolom `{kolom}` hilang dari tabel setelah Save
8. Muat ulang halaman (F5)
9. Klik angka `5` pada baris NB-1 untuk membuka kembali Popup Used By
10. Verifikasi kolom `{kolom}` tetap hilang dari tabel setelah F5
11. Klik icon `⋯` pada header kolom Actions
12. Klik `Setup Column...`
13. Centang kolom `{kolom}`
14. Klik `[Save]`
15. Verifikasi kolom `{kolom}` tampil kembali di tabel setelah check ulang dan Save

### TC-FA-TDC-602: Guard satu kolom tersisa pada Popup Used By: checkbox terakhir tidak dapat di-uncheck

16. Klik icon `⋯` pada header kolom Actions
17. Klik `Setup Column...`
18. Hapus centang kolom Asset Class
19. Hapus centang kolom Tax Method
20. Arahkan kursor ke checkbox Asset Names pada Popup Setup Column
21. Verifikasi checkbox Asset Names pada Popup Setup Column Disabled (tetap tampil)
22. Verifikasi tooltip `At least one column must remain visible.` pada checkbox Asset Names Popup Setup Column
23. Tutup Popup Setup Column tanpa `[Save]` lewat `(X)`
24. Klik icon `⋯` pada header kolom Actions untuk membuka Overlay Column Visibility
25. Hapus centang kolom Asset Class pada Overlay
26. Hapus centang kolom Tax Method pada Overlay
27. Arahkan kursor ke checkbox Asset Names pada Overlay
28. Verifikasi checkbox Asset Names pada Overlay Disabled (tetap tampil)
29. Verifikasi tooltip `At least one column must remain visible.` pada checkbox Asset Names Overlay
30. Centang kembali kolom Asset Class pada Overlay
31. Centang kembali kolom Tax Method pada Overlay
32. Tutup Overlay Column Visibility
33. Tutup Popup Used By lewat ikon Close `(X)`

## Notes

- Langkah berulang (8b.7): langkah 2 sampai 15 diulang tiga kali (satu iterasi per baris tabel "Kolom yang diuji"); parameter tiap iterasi hanya `{kolom}`, tanpa langkah bersyarat, dan `Verifikasi` tetap satu per klausa (S-01). Dengan ekspansi spec ini 61 langkah (1 langkah pembuka, 3 x 14 langkah berulang, dan 18 langkah TC-FA-TDC-602).
- Alasan lebih dari sekitar 35 langkah (dengan ekspansi): satu topik (Setup Column Popup Used By), satu kelas harness, dan tiap iterasi berdiri sendiri sehingga kegagalan satu iterasi tidak menghapus makna iterasi lain; pengulangan langkah per kolom berasal dari TC-FA-TDC-597 ("Untuk tiap kolom") dan tidak dapat dipecah tanpa mengulang pembukaan popup yang sama di spec lain.
- Interpretasi TC-FA-TDC-597: langkah 4 TC dijalankan per kolom lalu dipulihkan (check ulang, langkah 13 dan 14) sebelum kolom berikutnya, karena menyembunyikan ketiga kolom sekaligus tidak mungkin akibat guard satu kolom tersisa (TC-FA-TDC-602). Langkah F5 (langkah 8) menutup Popup Used By sehingga dibuka kembali (langkah 9). Pemulihan Setup Column dilakukan di langkah 13 sampai 14 (8b.14, R-24).
- Langkah penghubung (S-03): langkah 8 dan 9 (muat ulang dan membuka kembali popup), langkah 13 dan 14 (check ulang kolom), langkah 30 sampai 33 (pemulihan Overlay Column Visibility dan menutup popup). Tabel utama memuat sembilan baris pada satu halaman; baris NB-1 tidak perlu dicari lewat Search (8b.13).
- Temuan untuk QA:
  - TC-FA-TDC-597 langkah 4 dan 5 tidak menyatakan apakah kolom dipulihkan per iterasi; langkah 6 menyebut "check kolom yang disembunyikan" (tunggal/jamak) tanpa mengatakan kapan. Spec memakai pemulihan per iterasi.
  - TC-FA-TDC-597 Expected d menyebut check ulang dan Save untuk "butir a sampai c"; spec mengasersi tiap kolom tampil kembali per iterasi.
  - TC-FA-TDC-602 langkah 2 meminta "uncheck semua kolom kecuali Asset Names" pada Popup Setup Column dan langkah 4 mengulang pada Overlay; TC tidak menyatakan keadaan Overlay setelah Popup ditutup tanpa Save. Spec mengembalikan kolom pada langkah 30 dan 31.
  - Email akun Total Control tidak tertulis di TC.
