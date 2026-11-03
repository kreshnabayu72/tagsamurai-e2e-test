---
id: TC-FA-LBL-E2E-118-gate-value-asset-value-dan-sel-no-access-sort-filter-search-tooltip-request-langsung-bagian-1-2
title: "Gate-Value: Asset Value dan Sel No access (Sort, Filter, Search, Tooltip, Request Langsung) (bagian 1/2)"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-LBL-546
  - TC-FA-LBL-557
  - TC-FA-LBL-559
  - TC-FA-LBL-576
coverage:
  web: automated
---

# Gate-Value: Asset Value dan Sel No access (Sort, Filter, Search, Tooltip, Request Langsung) (bagian 1/2)

## Prerequisites

- Mode: FE+BE. Backend nyata; tidak ada intercept.
- Akun aktor: Gate-Value (`Company Gate`; Read Manage Asset Master Data; Group Role View asset value pada `Gate HQ`) (Pre-setup #40), `Fixture.assetLabeling.akun.gateValue`, `Spectra.env.FA_GATE_VALUE_PASSWORD`. Login di hook `before` spec ini (menggantikan akun default suite); halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Asset Master > tab Labels). Hook `after` mengembalikan sesi ke akun default suite (Total Control Company Alpha, `Spectra.env.FA_LBL_TC_PASSWORD`).
- Akun aktor: Gate-Purchase (`Company Gate`; Read Manage Asset Master Data; Group Role Manage purchase pada `Gate HQ`) (Pre-setup #41), `Fixture.assetLabeling.akun.gatePurchase`, `Spectra.env.FA_GATE_PURCHASE_PASSWORD`. Dipakai pada langkah Ganti akun.
- Hook suite: Guided Tooltip, pemulihan state global, dan pembukaan Settings > Asset Master > tab Labels mengikuti hook di `suite.md` dan tidak ditulis ulang di sini.
- Data Pre-setup `Company Gate` (#38), hanya dibaca dan dirujuk lewat `Fixture.assetLabeling.gate`: General Settings currency `Rp` (ribuan titik, desimal koma, 2 desimal) dan lisensi `FA-7` aktif; Group `Gate HQ` dengan anak `Gate Branch A`, dan Group `Gate Other` (terpisah); dua buku Asset Value tetap `Commercial` dan `Fiscal` (seluruh nilai Asset Value yang diasersi adalah nilai buku `Commercial`); Asset Name `Gate Item` dan `Gate Plain`; Custom Field Active (Scope Asset Name `Gate Item`): `Gate Note` (General, Text), `Gate Region` (General, Text, Value Type Global, nilai `APAC`), `Purchase PO` (Purchasing, Text), `Cost Center` (Accounting, Text); Custom Field Inactive `Retired Field` (General, Text); label `Gate Label` pada aset Active `Gate Item - 51` (Group `Gate HQ`; Asset Value 1500000; Warranty Expiry 30 Jun 2027; `Gate Note` `Note A`; `Purchase PO` `PO-001`; `Cost Center` `CC-10`), `Gate Item - 52` (Group `Gate HQ > Gate Branch A`; Asset Value 0; Warranty Expiry belum ada; `Purchase PO` dan `Cost Center` belum diisi), `Gate Item - 53` (Group `Gate Other`; Asset Value 2500000; Warranty Expiry 15 Jan 2028; `Purchase PO` `PO-003`; `Cost Center` `CC-30`), dan `Gate Plain - 54` (Group `Gate HQ`; Asset Value dan Warranty Expiry belum ada; di luar Scope seluruh Custom Field); label `Gate Scope` pada `Gate Plain - 55` (Active; Group `Gate Other`; Asset Value 700000; Warranty Expiry 01 Mar 2027; di luar Scope seluruh Custom Field).
- Data Dinamis: tidak ada.
- Fixture `fixtures/asset-labeling.json` (belum ada, disediakan tim FE; hanya identitas data, tanpa rahasia). Kunci yang dipakai spec ini: `Fixture.assetLabeling.akun.gateValue`, `Fixture.assetLabeling.akun.gatePurchase` (email akun masing-masing) dan `Fixture.assetLabeling.gate` (data Pre-setup #38).
- Kemampuan teknis (disediakan tim FE): hapus preferensi kolom Setup Column Drawer di browser (bagian 4).
- State global: konfigurasi kolom Setup Column Drawer Tagged Asset (preferensi browser) diubah dan dipulihkan oleh langkah spec; hook `after` spec ini menghapus preferensi kolom di browser sebagai cadangan, bukan `[Reset to Default]` (bagian 4). Kemampuan menghapus preferensi itu disediakan tim FE. Tidak ada state global lain yang diubah.
- Suite berjalan serial (`parallel: false`).
- Cleanup: spec tidak membuat data. Data Pre-setup hanya dibaca dan tidak diubah (Last Updated tidak berubah).
- Env var: `Spectra.env.FA_GATE_VALUE_PASSWORD`, `Spectra.env.FA_GATE_PURCHASE_PASSWORD`, `Spectra.env.FA_LBL_TC_PASSWORD` terdaftar di `executionConfig.environmentVariables` dan `.env.example`. `FA_LBL_TC_PASSWORD` dipakai hanya oleh hook `after` untuk mengembalikan sesi ke akun default suite.

## Test Steps

### TC-FA-LBL-546: Gerbang Asset Value untuk View asset value pada Gate HQ: nilai, nol pada descendant, No access di luar group, dan —

1. Klik chip `Gate Label` di kolom Label
2. Klik header kolom Actions (⋯) Drawer, klik `Setup Column...`, centang `Asset Value (Commercial)`, lalu klik `[Save]`
3. Verifikasi Total Asset `4` di blok identitas
4. Verifikasi keempat baris `Gate Item - 51`, `Gate Item - 52`, `Gate Item - 53`, dan `Gate Plain - 54` tampil (himpunan baris client-wide)
5. Verifikasi `Gate Item - 51` (`Gate HQ`) menampilkan `Rp 1.500.000,00`
6. Verifikasi `Gate Item - 52` (`Gate Branch A`, descendant) menampilkan `Rp 0,00`
7. Verifikasi `Gate Item - 53` (`Gate Other`, di luar hak) menampilkan `No access`
8. Verifikasi nilai 2500000 `Gate Item - 53` tidak tampil
9. Verifikasi `Gate Plain - 54` (`Gate HQ`, berhak, belum ada nilai) menampilkan `—`

### TC-FA-LBL-557: Sort Drawer kolom Asset Value: numerik, — mengikuti arah sort, dan No access selalu terakhir

10. Klik header kolom `Asset Value (Commercial)` satu kali
11. Verifikasi urutan klik 1: Ascending `Gate Item - 52` (`Rp 0,00`), `Gate Item - 51` (Rp 1.500.000,00), `Gate Plain - 54` (`—`) di akhir kelompok bernilai, lalu `Gate Item - 53` (`No access`) paling akhir
12. Klik header kolom `Asset Value (Commercial)` kedua kali
13. Verifikasi urutan klik 2: Descending `Gate Plain - 54` (`—`) di awal, `Gate Item - 51`, `Gate Item - 52`, lalu `Gate Item - 53` (`No access`) tetap paling akhir
14. Klik header kolom `Asset Value (Commercial)` ketiga kali
15. Verifikasi urutan klik 3 kembali ke default Name A-Z

### TC-FA-LBL-576: Search Drawer kolom Asset Value: nilai tampil pada sel berhak dicari, sel No access tidak cocok

16. Klik icon Search di toolbar Drawer, ketik `Rp 1.500.000,00`, tekan Enter
17. Verifikasi hanya `Gate Item - 51` tampil (Search `Rp 1.500.000,00`)
18. Ganti isi kotak search dengan `Rp 0,00`, tekan Enter
19. Verifikasi hanya `Gate Item - 52` tampil (nilai nol pada descendant yang berhak)
20. Ganti isi kotak search dengan `Rp 2.500.000,00`, tekan Enter
21. Verifikasi empty state `No results found` (nilai asli `Gate Item - 53` tidak dicocokkan karena sel `No access`)
22. Ganti isi kotak search dengan `No access`, tekan Enter
23. Verifikasi empty state `No results found` (teks `No access` tidak dicocokkan)
24. Klik `(←)` pada kotak Search

### TC-FA-LBL-559: Filter Drawer kolom bergerbang: baris No access tidak cocok dengan filter apa pun

25. Klik icon Filter di toolbar Drawer, isi `Asset Value (Commercial)` Min `2.000.000` dan Max `3.000.000`, lalu klik `[Apply]`
26. Verifikasi empty state `No results found` (nilai asli `Gate Item - 53` Rp 2.500.000,00 tidak dicocokkan karena sel `No access`)
27. Buka panel Filter lagi, klik `[Clear Field]`, isi `Asset Value (Commercial)` Min `1.000.000` dan Max `2.000.000`, lalu klik `[Apply]`
28. Verifikasi hanya `Gate Item - 51` tampil
29. Buka panel Filter lagi, klik `[Clear Field]`, lalu tutup panel Filter
30. Pemulihan: klik header kolom Actions (⋯) Drawer, klik `Setup Column...`, hapus centang `Asset Value (Commercial)`, lalu klik `[Save]`
31. Tutup Drawer Tagged Asset
32. Ganti akun: Logout, login sebagai Gate-Purchase `Fixture.assetLabeling.akun.gatePurchase` (`Spectra.env.FA_GATE_PURCHASE_PASSWORD`), buka Fixed Asset > Settings > Asset Master > tab Labels
33. Klik chip `Gate Label` di kolom Label
34. Klik icon Filter di toolbar Drawer, pilih rentang `Warranty Expiry` `01 Jan 2028` sampai `31 Dec 2028`, lalu klik `[Apply]`
35. Verifikasi empty state `No results found` (nilai asli `Gate Item - 53` 15 Jan 2028 tidak dicocokkan karena sel `No access`)
36. Buka panel Filter lagi, klik `[Clear Field]`, pilih rentang `Warranty Expiry` `01 Jun 2027` sampai `30 Jun 2027`, lalu klik `[Apply]`
37. Verifikasi hanya `Gate Item - 51` tampil
38. Buka panel Filter lagi, klik `[Clear Field]`, lalu tutup panel Filter
39. Tutup Drawer Tagged Asset

## Notes

- Sumber: `fixed-asset/settings-asset-labeling/TestCases/tc-settings-asset-labeling.md` section 4c (Drawer Tagged Asset). Subjudul `###` memetakan langkah ke TC granular.
- Penyimpangan urutan (bagian 3): TC-FA-LBL-559 ditaruh paling akhir karena memakai Ganti akun ke Gate-Purchase pada Langkah Uji 4 TC; TC-FA-LBL-546, 557, dan 576 berjalan lebih dulu dengan akun Gate-Value (login di hook `before`). TC-FA-LBL-557 dan 576 memakai kolom `Asset Value (Commercial)` yang tetap tercentang dari TC-FA-LBL-546 (Drawer tetap terbuka).
- Ganti akun: ke Gate-Purchase ditulis eksplisit pada langkah pembuka bagian kedua TC-FA-LBL-559; Setup Column tidak disentuh pada bagian itu karena filter `Warranty Expiry` tidak memerlukan kolom tampil (sesuai TC).
- Langkah penghubung (S-03): `Klik (←) pada kotak Search`, `[Clear Field]` terakhir beserta tutup panel Filter, Pemulihan kolom, dan tutup Drawer memulihkan keadaan awal (S-09).
- Pembagian TC lintas spec: Tooltip No access dan permintaan langsung (TC-FA-LBL-551, 566) ada di spec 119.
- Ukuran spec (39 langkah, di atas smell 35 langkah): keempat TC satu kelas (fungsional, gerbang Asset Value dan Warranty Expiry pada Drawer Gate-Value) pada data Pre-setup #38 yang sama dan tiap blok berdiri sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna; langkah membengkak karena matriks nilai per baris, Sort tiga klik, dan tiap klausa Expected menjadi satu `Verifikasi` (S-01).
- Temuan untuk QA:
  - TC-FA-LBL-557 Expected a menempatkan `Gate Plain - 54` (`—`) "di akhir kelompok bernilai" pada Ascending sedangkan Expected b menempatkannya "di awal" pada Descending; spec mengikuti kedua urutan itu.
  - TC-FA-LBL-559 Langkah Uji 4 hanya menyebut login Gate-Purchase dan membuka Drawer `Gate Label`; kolom `Warranty Expiry` tidak dicentang pada langkah itu sehingga asersi bergantung pada Filter Panel yang memuat field `Warranty Expiry` tanpa kolom tampil.
