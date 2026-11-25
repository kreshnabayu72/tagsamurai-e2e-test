---
id: TC-FA-TDC-E2E-028-aktor-read-membuka-mencari-memfilter-mengunduh-dan-popup
title: "Aktor Read: Membuka Tab, Mencari, Memfilter, Mengunduh, dan Membuka Popup"
layer: ui-e2e
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TDC-91
  - TC-FA-TDC-92
  - TC-FA-TDC-93
  - TC-FA-TDC-94
  - TC-FA-TDC-95
  - TC-FA-TDC-96
  - TC-FA-TDC-97
sourceRules: ["§4.2a#p2", "§4.1.1#r16", "§4.1.1#r17", "§4.1.1#r18", "§4.1.1#r19", "§4.1.1#r20", "§4.1.1#r21", "§4.1.1#r22", "§4.1.1#r23", "§4.1.1#r24", "§5#b2", "§5#b3", "§4.1.1#b7", "T-11a", "§5#b7", "§5#b8", "§4.1.1#p9", "§4.1.6#p1", "FATDC-LOGIC-11d.1", "§4.1.6#p5", "F-FATDC-03.k9"]
smoke: []
dependsOn: []
trace:
  "§4.2a#p2": 4
  "§4.1.1#r16": 5
  "§4.1.1#r17": 5
  "§4.1.1#r18": 5
  "§4.1.1#r19": 5
  "§4.1.1#r20": 5
  "§4.1.1#r21": 5
  "§4.1.1#r22": [5, 7]
  "§4.1.1#r23": 5
  "§4.1.1#r24": 5
  "§5#b2": 7
  "§5#b3": 12
  "§4.1.1#b7": 13
  "T-11a": 17
  "§5#b7": 18
  "§5#b8": 20
  "§4.1.1#p9": 21
  "§4.1.6#p1": 24
  "FATDC-LOGIC-11d.1": 25
  "§4.1.6#p5": 29
  "F-FATDC-03.k9": 30
coverage:
  web: automated
---

# Aktor Read: Membuka Tab, Mencari, Memfilter, Mengunduh, dan Membuka Popup

## Prerequisites

- Mode: FE+BE.
- Role yang diuji:

| Role | Akun | Password (env) | Blok langkah |
|---|---|---|---|
| Read (Manage accounting) | disediakan tim FE (tidak ada nomor Pre-setup di TC) | `Spectra.env.FA_READ_PASSWORD` | langkah 1 sampai 32 |

- Login di hook `before` spec ini sebagai Read (Manage accounting). Spec ini membuka layar sendiri: TC-FA-TDC-91 dimulai dari halaman utama aplikasi Fixed Asset, sehingga layar awal spec adalah halaman utama dan hook `beforeEach` suite tidak membuka tab Tax Depreciation Class. Hook `after` mengembalikan sesi ke akun default suite (Total Control).
- Kemampuan teknis (disediakan tim FE/BE, lihat `suite.md`): seed dan pemulihan data lewat API (class, versi, Used By, tabel tanpa class), akun per role, dan perubahan capability role. Endpoint tidak dikarang (S-13).
- Data Pre-setup dirujuk lewat fixture `fixtures/fixedAssetTaxDepreciationClass.json` (belum ada; disediakan tim FE, nama kunci ditetapkan tim FE): kode dan nilai kolom class Example Data. Nama env password di tabel "Role yang diuji" belum terdaftar di `executionConfig.environmentVariables` dan `.env.example`; penulis script mendaftarkannya.
- Data (kondisi awal): tabel berisi 9 class sesuai Example Data PRD (BLD-NP, BLD-P, LAND, NB-1, NB-2, NB-4, NB-KHS, NB-OLD, NB-SL) dengan nilai kolom persis Example Data; 9 baris berada dalam satu halaman Pagination (10 baris per halaman), sehingga baris target tidak dicari lewat Search. Hook `before` spec ini menyeed ulang kondisi itu lewat API dan hook `after` memulihkannya; Class Code dibatasi 15 karakter sehingga kode class memakai literal TC tanpa suffix `{runId}-<NNN>` (lihat Temuan untuk QA).
- Akun aktor sudah tersedia dan memiliki akses tab (Read) ke Settings > Accounting > Tax Depreciation Class.
- Kebutuhan data: NB-1 memiliki Used By 5 (Popup Used By, TC-FA-TDC-96); BLD-NP memiliki satu versi Scheduled (Popup Versions, TC-FA-TDC-97); class LAND memiliki Class Name yang memuat `Tanah` dan Asset Type `Land` (TC-FA-TDC-92 dan 93). Unduhan berkas (TC-FA-TDC-94) memerlukan kemampuan browser menangkap unduhan, disediakan tim FE; isi berkas tidak diasersi di spec ini.
- Flag Guided Tooltip halaman ini disetel `seen` oleh hook suite untuk setiap akun aktor (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`) sesuai `suite.md`; spec ini tidak mengubah state global kecuali yang tertulis di bawah.

## Test Steps

1. Buka halaman utama aplikasi Fixed Asset

### Membuka tab (TC-FA-TDC-91)

2. Klik menu sidebar `Accounting`
3. Klik tab `Tax Depreciation Class`
4. Verifikasi tab terbuka dengan Breadcrumb `Settings > Accounting > Tax Depreciation Class`
5. Verifikasi tabel menampilkan 9 baris Example Data

### Search (TC-FA-TDC-92)

6. Ketik Search `Tanah`, tekan Enter
7. Verifikasi baris LAND tampil dan tabel hanya menampilkan baris LAND
8. Klik `(←)` pada kotak Search untuk menutup input dan mereset tabel

### Filter Panel (TC-FA-TDC-93)

9. Klik icon Filter
10. Pilih Asset Type `Land`
11. Klik `[Apply]`
12. Verifikasi baris LAND tampil dan tabel hanya menampilkan baris LAND
13. Verifikasi icon Filter menampilkan badge titik tanpa angka
14. Klik `[Clear Field]` lalu `[Apply]` pada Filter Panel

### Download CSV (TC-FA-TDC-94)

15. Klik icon Download
16. Klik `Download as CSV`
17. Verifikasi tidak ada toast sukses
18. Verifikasi berkas `Tax-Depreciation-Class.csv` terunduh

### Popup Changelog (TC-FA-TDC-95)

19. Klik icon Changelog
20. Verifikasi Popup `Changelog: Tax Depreciation Class` terbuka
21. Verifikasi entri Changelog tampil
22. Tutup Popup Changelog

### Popup Used By (TC-FA-TDC-96)

23. Klik angka `5` pada baris NB-1
24. Verifikasi Popup `Used By` terbuka dengan teks `NB-1 – Bukan bangunan – Kelompok 1` di bawah judul
25. Verifikasi tabel Asset Class pemakai tampil
26. Tutup Popup Used By

### Popup Versions (TC-FA-TDC-97)

27. Klik Class Code BLD-NP
28. Klik `View versions`
29. Verifikasi Popup `Versions` terbuka dengan teks `BLD-NP – Bangunan tidak permanen` di bawah judul
30. Verifikasi tabel Popup Versions tanpa kolom Action
31. Tutup Popup `Versions`
32. Tutup Drawer dengan `[×]`

## Notes

- Satu aktor (Read) untuk seluruh spec; login di hook `before`, tidak ada ganti akun. Langkah 1 (membuka halaman utama) adalah langkah penghubung untuk TC-FA-TDC-91 yang berprasyarat halaman utama.
- Langkah penghubung (S-03): `(←)` pada Search dan `[Clear Field]` lalu `[Apply]` memulihkan tabel penuh sebelum TC berikutnya (S-09); menutup Popup dan Drawer. Search `Tanah` adalah isi TC-FA-TDC-92, bukan pencarian baris target; tabel 9 baris satu halaman (R-16).
- Pembagian TC lintas spec: unduhan CSV hanya diasersi nama berkas dan terunduh; isi berkas diasersi di spec kelas berkas.
- Absence "tidak ada toast sukses" ditulis tepat sesudah klik `Download as CSV` (8b.11); klik itu adalah anchor positif yang buktinya menyusul pada Verifikasi berkas terunduh.
- Temuan untuk QA:
  - Akun per role tidak punya nomor Pre-setup, email, atau company di TC; Prerequisites menandainya "disediakan tim FE" dan nama env password adalah usulan.
  - TC tidak memiliki tabel Data Uji Pre-setup dan Dinamis; data ditulis di kolom Precondition tiap TC dan disalin ke Prerequisites.
  - Class Code dibatasi 15 karakter (TC-136, 137), sehingga suffix `{runId}-<NNN>` tidak dapat dipasang pada kode class (S-12); spec memakai kode literal Example Data dan menyeed ulang data milik spec di hook `before` serta memulihkannya di hook `after`. Perlu konfirmasi QA.
  - TC-91 tidak menyebut bahwa tab terbuka dengan Search/Filter kosong; tabel 9 baris diasersi dari Precondition.
  - TC-92 tidak menyebut nama kolom yang dicari (`Tanah` diasumsikan ada pada Class Name LAND).
