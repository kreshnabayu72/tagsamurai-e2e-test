---
id: TC-FA-TDC-E2E-166-popup-used-by-download-opsi-nama-berkas-dan-isi-berkas
title: "Popup Used By Download: Opsi, Nama Berkas, dan Isi Berkas"
layer: ui-e2e
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TDC-591
  - TC-FA-TDC-592
  - TC-FA-TDC-593
  - TC-FA-TDC-929
sourceRules: ["§4.1.6#p3", "T-11e", "§4.1.6#p1", "§4.1.6#r1", "§4.1.6#r2", "§4.1.6#r3", "§4.1.6#p2"]
smoke: []
dependsOn: []
trace:
  "§4.1.6#p3": [3, 5, 6, 9, 10, 13, 14, 22, 23, 33, 35, 36, 37]
  "T-11e": [5, 9, 13]
  "§4.1.6#p1": 15
  "§4.1.6#r1": [23, 33]
  "§4.1.6#r2": [23, 33]
  "§4.1.6#r3": 33
  "§4.1.6#p2": 34
coverage:
  web: automated
---

# Popup Used By Download: Opsi, Nama Berkas, dan Isi Berkas

## Prerequisites

- Mode: FE+BE.
- Akun: Total Control (company uji Fixed Asset). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Akun dan email disediakan tim FE (email tidak tertulis di TC); password lewat `Spectra.env.FA_TC_PASSWORD`.
- Hook suite, seeding, dan flag Guided Tooltip mengikuti `suite.md`.
- Data Pre-setup (dibaca, tidak diubah; disediakan tim FE lewat seeding API, `Fixture.fixedAssetTaxDepreciationClass`, fixture belum ada), dua isi pemakai berurutan:
  - Isi pemakai A (TC-FA-TDC-591, 593, 592), kunci `exampleData` ditambah pemakai NB-1: sembilan class Example Data PRD (BLD-NP, BLD-P, LAND, NB-1, NB-2, NB-4, NB-KHS, NB-OLD, NB-SL) dengan nilai kolom persis Example Data; NB-1 dipakai 5 Asset Class: `AC-01 – Mesin Produksi` (Straight Line, 12 Asset Name), `AC-02 – Peralatan Kantor` (Straight Line, 30), `AC-03 – Kendaraan Operasional` (Declining Balance, 7), `AC-04 – Komputer` (Declining Balance, 25), `AC-05 – Furnitur` (Straight Line, 18).
  - Isi pemakai B (TC-FA-TDC-929), kunci `exampleData` ditambah pemakai NB-SL: NB-SL (hanya Straight Line) dipakai 4 Asset Class: `AC-11 – Mesin Cetak` (Straight Line, 6 Asset Name), `AC-12 – Mesin Potong` (Straight Line, 9), `AC-13 – Mesin Press` (Straight Line, 4), dan `AC-14 – Mesin Bor` (Straight Line, 11). Isi pemakai B diterapkan lewat seeding API pada langkah 29.
- Kemampuan teknis: membuka berkas unduhan CSV (baris, kolom, karakter sel) disediakan tim FE; Overlay Download dan Overlay Column Visibility popup; pemulihan Setup Column dengan langkah eksplisit (8b.14, R-24).
- State global yang diubah: kolom Asset Names popup disembunyikan lalu ditampilkan kembali (langkah 17 sampai 19 dan 24 sampai 26), Search popup dikosongkan (langkah 27). Pemakai NB-SL dikembalikan ke isi pemakai A lewat seeding API di hook `after`.

## Test Steps

### TC-FA-TDC-591: Download di Popup Used By: opsi dan nama berkas

1. Klik angka `5` pada baris NB-1 untuk membuka Popup Used By
2. Klik Download pada toolbar Popup
3. Verifikasi Overlay memuat `Download as CSV` dan `Download as XLSX`
4. Klik `Download as CSV`
5. Verifikasi tidak ada toast
6. Verifikasi berkas `Tax-Depreciation-Class-Used-By.csv` terunduh
7. Klik Download pada toolbar Popup
8. Klik `Download as XLSX`
9. Verifikasi tidak ada toast
10. Verifikasi berkas `Tax-Depreciation-Class-Used-By.xlsx` terunduh

### TC-FA-TDC-593: Download Used By berhasil tanpa toast sukses

11. Klik icon Download pada toolbar Popup
12. Klik `Download as CSV`
13. Verifikasi tidak ada toast sukses
14. Verifikasi berkas `Tax-Depreciation-Class-Used-By.csv` terunduh
15. Verifikasi Popup Used By tetap terbuka

### TC-FA-TDC-592: Download Used By mengikuti Search popup dan kolom yang tampil

16. Ketik Search `declining` pada Search popup, tekan Enter
17. Klik header kolom Actions `⋯`
18. Hapus centang kolom Asset Names
19. Tutup Overlay Column Visibility
20. Klik icon Download pada toolbar Popup
21. Klik `Download as CSV` lalu buka berkas
22. Verifikasi berkas hanya memuat 2 baris data: `AC-03 – Kendaraan Operasional` dan `AC-04 – Komputer`
23. Verifikasi berkas hanya memuat kolom Asset Class dan Tax Method
24. Klik header kolom Actions `⋯`
25. Centang kolom Asset Names
26. Tutup Overlay Column Visibility
27. Klik `(←)` pada kotak Search

### TC-FA-TDC-929: Berkas Download Used By memuat kolom data Asset Class, Tax Method, dan Asset Names

28. Tutup Popup Used By lewat ikon Close `(X)`
29. Ganti pemakai NB-SL menjadi isi pemakai B (empat Asset Class) lewat seeding API, lalu muat ulang halaman
30. Klik angka `4` pada baris NB-SL untuk membuka Popup Used By
31. Klik icon Download pada toolbar Popup
32. Klik `Download as CSV` lalu buka berkas `Tax-Depreciation-Class-Used-By.csv`
33. Verifikasi berkas memuat baris header `Asset Class`, `Tax Method`, `Asset Names`
34. Verifikasi berkas memuat 4 baris data urut Asset Class A-Z
35. Verifikasi baris pertama berkas: `AC-11 – Mesin Cetak`, `Straight Line`, `6`
36. Verifikasi sel Asset Class hanya berisi `[Class Code] – [Class Name]` tanpa karakter tambahan
37. Verifikasi tidak ada kolom tambahan
38. Tutup Popup Used By lewat ikon Close `(X)`

## Notes

- Urutan TC dalam spec: TC-FA-TDC-591, 593, 592, 929. TC-FA-TDC-591, 593, dan 592 memakai Popup Used By NB-1 yang sama dan dibuka sekali (langkah 1); TC-FA-TDC-929 memakai NB-SL dengan empat pemakai berbeda sehingga diletakkan paling akhir. TC-FA-TDC-593 mendahului TC-FA-TDC-592 supaya perubahan Search dan kolom TC-FA-TDC-592 tidak memengaruhinya (S-09).
- Alasan lebih dari sekitar 35 langkah (38 langkah): satu topik (Download popup Used By), satu kelas harness (isi berkas), dan tiap blok TC berdiri sendiri sehingga kegagalan satu blok tidak menghapus makna blok lain.
- Asersi tidak ada toast pada langkah 5, 9, 13 diletakkan segera setelah pemicu sebelum asersi berkas terunduh yang menjadi anchor positif (8b.11).
- Langkah penghubung (S-03): langkah 17 sampai 19 dan 24 sampai 26 (menyembunyikan dan menampilkan kembali kolom Asset Names; pemulihan Setup Column 8b.14, R-24; TC tidak menyebut `[Save]`), langkah 27 (mengosongkan Search; 8b.9), langkah 28 dan 38 (menutup popup), langkah 29 (seeding API). Langkah 17 memakai label header "Actions ⋯" sesuai TC-FA-TDC-595 walau header yang sama disebut `Column Visibility (⋯)` pada TC-FA-TDC-579.
- Temuan untuk QA:
  - TC-FA-TDC-591 butir b dan c serta TC-FA-TDC-593 butir a dan b mengasersi hal yang sama untuk CSV (nama berkas, tanpa toast); spec menulis keduanya karena tiap TC tepat satu spec.
  - TC-FA-TDC-592 tidak menyebut cara menyembunyikan kolom Asset Names; spec memakai Overlay Column Visibility lewat header kolom Actions `⋯`.
  - TC-FA-TDC-929 butir a menyebut baris header `Asset Class`, `Tax Method`, `Asset Names`; kolom Column Visibility `⋯` tidak masuk berkas menurut TC.
  - Email akun Total Control tidak tertulis di TC.
