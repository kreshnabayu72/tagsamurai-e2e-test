---
id: TC-FA-TDC-E2E-164-popup-used-by-search-sort-pagination-dan-empty-state-hasil
title: "Popup Used By: Search, Sort, Pagination, dan Empty State Hasil"
layer: ui-e2e
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TDC-583
  - TC-FA-TDC-584
  - TC-FA-TDC-585
  - TC-FA-TDC-587
  - TC-FA-TDC-588
sourceRules: ["§4.1.6#p1", "ST-25", "§4.1.6#p2", "§4.1.6#r2", "§4.4#r10", "§4.1.6#r3"]
smoke: []
dependsOn: []
trace:
  "§4.1.6#p1": [3, 5, 25, 26, 28, 30]
  "ST-25": [7, 9]
  "§4.1.6#p2": [11, 21]
  "§4.1.6#r2": [13, 15]
  "§4.4#r10": [13, 15, 17, 19, 21]
  "§4.1.6#r3": [17, 19]
coverage:
  web: automated
---

# Popup Used By: Search, Sort, Pagination, dan Empty State Hasil

## Prerequisites

- Mode: FE+BE.
- Akun: Total Control (company uji Fixed Asset). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Akun dan email disediakan tim FE (email tidak tertulis di TC); password lewat `Spectra.env.FA_TC_PASSWORD`.
- Hook suite, seeding, dan flag Guided Tooltip mengikuti `suite.md`.
- Data Pre-setup (dibaca, tidak diubah; disediakan tim FE lewat seeding API, `Fixture.fixedAssetTaxDepreciationClass`, fixture belum ada), dua isi pemakai berurutan:
  - Isi pemakai A (TC-FA-TDC-583, 584, 585, 587), kunci `exampleData` ditambah pemakai NB-1: sembilan class Example Data PRD (BLD-NP, BLD-P, LAND, NB-1, NB-2, NB-4, NB-KHS, NB-OLD, NB-SL) dengan nilai kolom persis Example Data; NB-1 dipakai 5 Asset Class: `AC-01 – Mesin Produksi` (Straight Line, 12 Asset Name), `AC-02 – Peralatan Kantor` (Straight Line, 30), `AC-03 – Kendaraan Operasional` (Declining Balance, 7), `AC-04 – Komputer` (Declining Balance, 25), `AC-05 – Furnitur` (Straight Line, 18).
  - Isi pemakai B (TC-FA-TDC-588): class BLD-NP dipakai 12 Asset Class (jumlah Asset Class pemakai lebih dari 10; nama dan Tax Method tidak disebut TC). Isi pemakai B diterapkan lewat seeding API pada langkah 23.
- Kemampuan teknis: seeding pemakai class lewat API; Search, sort header, dan Pagination popup.
- State global yang diubah: tidak ada state yang disimpan oleh sort atau Search popup. Pemakai BLD-NP dikembalikan ke isi pemakai A (BLD-NP tanpa pemakai) lewat seeding API di hook `after`.

## Test Steps

### TC-FA-TDC-583: Search di Popup Used By: kolom Asset Class dan Tax Method

1. Klik angka `5` pada baris NB-1 untuk membuka Popup Used By
2. Ketik Search `mesin` pada Search popup, tekan Enter
3. Verifikasi hasil Search kolom Asset Class hanya `AC-01 – Mesin Produksi` (baris `AC-02 – Peralatan Kantor` tidak tampil)
4. Ganti isi kotak search dengan `declining`, tekan Enter
5. Verifikasi hasil Search kolom Tax Method berisi `AC-03 – Kendaraan Operasional` dan `AC-04 – Komputer` (baris `AC-01 – Mesin Produksi` tidak tampil)

### TC-FA-TDC-584: Guard Popup Used By: kolom Asset Names tidak dicari

6. Ganti isi kotak search dengan `12`, tekan Enter
7. Verifikasi Popup menampilkan `No results found` walau AC-01 bernilai Asset Names `12`

### TC-FA-TDC-585: Popup Used By: hasil Search kosong

8. Ganti isi kotak search dengan `zzzz`, tekan Enter
9. Verifikasi Illustration dengan Title `No results found` dan Description `Try adjusting your search or filter.`
10. Klik `(←)` pada kotak Search

### TC-FA-TDC-587: Sort kolom Popup Used By: Asset Class (default), Tax Method, dan Asset Names

11. Verifikasi urutan awal default Asset Class A-Z: AC-01, AC-02, AC-03, AC-04, AC-05
12. Klik header Tax Method satu kali
13. Verifikasi Tax Method Ascending: AC-03, AC-04 (`Declining Balance`) lalu AC-01, AC-02, AC-05 (`Straight Line`), baris bernilai sama mengikuti Asset Class A-Z
14. Klik header Tax Method kedua kali
15. Verifikasi Tax Method Descending: AC-01, AC-02, AC-05 (`Straight Line`) lalu AC-03, AC-04 (`Declining Balance`), baris bernilai sama mengikuti Asset Class A-Z
16. Klik header Asset Names satu kali
17. Verifikasi Asset Names Ascending: AC-03 (7), AC-01 (12), AC-05 (18), AC-04 (25), AC-02 (30)
18. Klik header Asset Names kedua kali
19. Verifikasi Asset Names Descending: AC-02 (30), AC-04 (25), AC-05 (18), AC-01 (12), AC-03 (7)
20. Klik header Asset Names ketiga kali
21. Verifikasi urutan kembali ke default Asset Class A-Z

### TC-FA-TDC-588: Pagination Popup Used By

22. Tutup Popup Used By lewat ikon Close `(X)`
23. Ganti pemakai BLD-NP menjadi 12 Asset Class (isi pemakai B) lewat seeding API, lalu muat ulang halaman
24. Klik angka `12` pada baris BLD-NP untuk membuka Popup Used By
25. Verifikasi halaman 1 menampilkan 10 baris dengan page size default 10
26. Verifikasi footer menampilkan opsi page size `10`, `25`, `50`, `100`
27. Klik halaman berikutnya
28. Verifikasi halaman 2 menampilkan 2 baris
29. Ganti page size menjadi 25
30. Verifikasi page size 25 menampilkan 12 baris di halaman 1
31. Tutup Popup Used By lewat ikon Close `(X)`

## Notes

- Urutan TC dalam spec: TC-FA-TDC-583, 584, 585, 587, 588. Empat TC pertama memakai Popup Used By NB-1 yang sama sehingga dibuka sekali (langkah 1); TC-FA-TDC-588 memakai BLD-NP dengan 12 pemakai sehingga diletakkan paling akhir. TC-FA-TDC-586 ada di spec lain.
- Langkah penghubung (S-03): langkah 10 (mengosongkan Search sebelum sort; 8b.9, R-16), langkah 22 dan 31 (menutup popup), langkah 23 (seeding API pemakai BLD-NP). Tabel utama memuat sembilan baris pada satu halaman; baris NB-1 dan BLD-NP tidak perlu dicari lewat Search (8b.13).
- Langkah 3 dan 5 adalah asersi "hanya": baris yang diharapkan tampil dan satu baris pembanding yang dijamin ada pada tabel yang sama (AC-02 atau AC-01) tidak tampil (8b.2).
- Temuan untuk QA:
  - TC-FA-TDC-583 langkah 3 menulis "Kosongkan Search" tanpa aksi; spec memakai "ganti isi kotak search dengan `declining`" (8b.9).
  - TC-FA-TDC-583 butir b menyebut dua hasil tanpa kata "hanya"; spec mengasersi kedua baris tampil dan satu baris Straight Line tidak tampil.
  - TC-FA-TDC-587 menyebut klik header Tax Method hanya dua kali dan header Asset Names tiga kali; spec mengasersi tiap klik sesuai Expected b dan c. Descending Tax Method dan Asset Names ditulis sebagai urutan eksplisit hasil kebalikan Ascending.
  - TC-FA-TDC-588 precondition d (BLD-NP dipakai 12 Asset Class) bertentangan dengan baris BLD-NP Example Data (Used By 0) pada precondition c; spec menerapkan isi pemakai B lewat seeding. Nama dan Tax Method 12 Asset Class tidak disebut TC.
  - Email akun Total Control tidak tertulis di TC.
