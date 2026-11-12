---
id: TC-FA-LBL-E2E-120-gate-purchase-warranty-expiry-dan-custom-field-purchasing
title: "Gate-Purchase: Warranty Expiry dan Custom Field Purchasing"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-LBL-549
  - TC-FA-LBL-555
  - TC-FA-LBL-558
  - TC-FA-LBL-562
  - TC-FA-LBL-570
coverage:
  web: automated
---

# Gate-Purchase: Warranty Expiry dan Custom Field Purchasing

## Prerequisites

- Mode: FE+BE. Backend nyata; tidak ada intercept.
- Akun aktor: Gate-Purchase (`Company Gate`; Read Manage Asset Master Data; Group Role Manage purchase pada `Gate HQ`) (Pre-setup #41), `Fixture.assetLabeling.akun.gatePurchase`, `Spectra.env.FA_GATE_PURCHASE_PASSWORD`. Login di hook `before` spec ini (menggantikan akun default suite); halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Asset Master > tab Labels). Hook `after` mengembalikan sesi ke akun default suite (Total Control Company Alpha, `Spectra.env.FA_LBL_TC_PASSWORD`).
- Hook suite: Guided Tooltip, pemulihan state global, dan pembukaan Settings > Asset Master > tab Labels mengikuti hook di `suite.md` dan tidak ditulis ulang di sini.
- Data Pre-setup `Company Gate` (#38), hanya dibaca dan dirujuk lewat `Fixture.assetLabeling.gate`: General Settings currency `Rp` (ribuan titik, desimal koma, 2 desimal) dan lisensi `FA-7` aktif; Group `Gate HQ` dengan anak `Gate Branch A`, dan Group `Gate Other` (terpisah); dua buku Asset Value tetap `Commercial` dan `Fiscal` (seluruh nilai Asset Value yang diasersi adalah nilai buku `Commercial`); Asset Name `Gate Item` dan `Gate Plain`; Custom Field Active (Scope Asset Name `Gate Item`): `Gate Note` (General, Text), `Gate Region` (General, Text, Value Type Global, nilai `APAC`), `Purchase PO` (Purchasing, Text), `Cost Center` (Accounting, Text); Custom Field Inactive `Retired Field` (General, Text); label `Gate Label` pada aset Active `Gate Item - 51` (Group `Gate HQ`; Asset Value 1500000; Warranty Expiry 30 Jun 2027; `Gate Note` `Note A`; `Purchase PO` `PO-001`; `Cost Center` `CC-10`), `Gate Item - 52` (Group `Gate HQ > Gate Branch A`; Asset Value 0; Warranty Expiry belum ada; `Purchase PO` dan `Cost Center` belum diisi), `Gate Item - 53` (Group `Gate Other`; Asset Value 2500000; Warranty Expiry 15 Jan 2028; `Purchase PO` `PO-003`; `Cost Center` `CC-30`), dan `Gate Plain - 54` (Group `Gate HQ`; Asset Value `Pending` karena belum ada Purchase Cost, tooltip `Purchase cost has not been set.`; Warranty Expiry belum ada; di luar Scope seluruh Custom Field); label `Gate Scope` pada `Gate Plain - 55` (Active; Group `Gate Other`; Asset Value 700000; Warranty Expiry 01 Mar 2027; di luar Scope seluruh Custom Field).
- Data Dinamis: tidak ada.
- Fixture `fixtures/asset-labeling.json` (belum ada, disediakan tim FE; hanya identitas data, tanpa rahasia). Kunci yang dipakai spec ini: `Fixture.assetLabeling.akun.gatePurchase` (email akun masing-masing) dan `Fixture.assetLabeling.gate` (data Pre-setup #38).
- Kemampuan teknis (disediakan tim FE): hapus preferensi kolom Setup Column Drawer di browser (bagian 4).
- State global: konfigurasi kolom Setup Column Drawer Tagged Asset (preferensi browser) diubah dan dipulihkan oleh langkah spec; hook `after` spec ini menghapus preferensi kolom di browser sebagai cadangan, bukan `[Reset to Default]` (bagian 4). Kemampuan menghapus preferensi itu disediakan tim FE. Tidak ada state global lain yang diubah.
- Suite berjalan serial (`parallel: false`).
- Cleanup: spec tidak membuat data. Data Pre-setup hanya dibaca dan tidak diubah (Last Updated tidak berubah).
- Env var: `Spectra.env.FA_GATE_PURCHASE_PASSWORD`, `Spectra.env.FA_LBL_TC_PASSWORD` terdaftar di `executionConfig.environmentVariables` dan `.env.example`. `FA_LBL_TC_PASSWORD` dipakai hanya oleh hook `after` untuk mengembalikan sesi ke akun default suite.

## Test Steps

### TC-FA-LBL-549: Gerbang Warranty Expiry untuk Manage purchase pada Gate HQ: nilai, —, dan No access

1. Klik chip `Gate Label` di kolom Label
2. Klik header kolom Actions (⋯) Drawer, klik `Setup Column...`
3. Verifikasi kolom `Warranty Expiry` tersedia di Setup Column dan tidak tercentang (default Hidden)
4. Centang `Warranty Expiry`, lalu klik `[Save]`
5. Verifikasi `Gate Item - 51` menampilkan `30 Jun 2027` sesuai format General Settings
6. Verifikasi `Gate Item - 52` (`Gate Branch A`, descendant, belum ada nilai) menampilkan `—`
7. Verifikasi `Gate Item - 53` (`Gate Other`) menampilkan `No access`
8. Verifikasi nilai 15 Jan 2028 `Gate Item - 53` tidak tampil
9. Verifikasi `Gate Plain - 54` menampilkan `—`

### TC-FA-LBL-555: Custom Field Purchasing: nilai, —, No access, dan — untuk Asset Name di luar Scope

10. Klik header kolom Actions (⋯) Drawer, klik `Setup Column...`, centang `Purchase PO`, lalu klik `[Save]`
11. Verifikasi `Gate Item - 51` menampilkan `PO-001`
12. Verifikasi `Gate Item - 52` (berhak, belum diisi) menampilkan `—`
13. Verifikasi `Gate Item - 53` (`Gate Other`, di luar hak) menampilkan `No access`
14. Verifikasi `PO-003` tidak tampil
15. Verifikasi `Gate Plain - 54` (berhak, Asset Name di luar Scope field) menampilkan `—`

### TC-FA-LBL-558: Sort Drawer kolom Warranty Expiry dan Custom Field Purchasing: No access selalu terakhir

16. Klik header kolom `Warranty Expiry` satu kali
17. Verifikasi urutan klik 1 Warranty Expiry (Oldest First): `Gate Item - 51` (30 Jun 2027), lalu `Gate Item - 52` dan `Gate Plain - 54` (`—`, urut default Name), lalu `Gate Item - 53` (`No access`) paling akhir
18. Klik header kolom `Warranty Expiry` kedua kali
19. Verifikasi urutan klik 2 Warranty Expiry (Newest First): `Gate Item - 52` dan `Gate Plain - 54` (`—`) di awal, lalu `Gate Item - 51`, lalu `Gate Item - 53` (`No access`) tetap paling akhir
20. Klik header kolom `Warranty Expiry` ketiga kali
21. Verifikasi urutan klik 3 Warranty Expiry kembali ke default Name A-Z
22. Klik header kolom `Purchase PO` satu kali
23. Verifikasi urutan klik 1 Purchase PO (A-Z): `Gate Item - 51` (`PO-001`), lalu `Gate Item - 52` dan `Gate Plain - 54` (`—`), lalu `Gate Item - 53` (`No access`) paling akhir
24. Klik header kolom `Purchase PO` kedua kali
25. Verifikasi urutan klik 2 Purchase PO (Z-A): `Gate Item - 52` dan `Gate Plain - 54` (`—`) di awal, lalu `Gate Item - 51`, lalu `Gate Item - 53` (`No access`) tetap paling akhir
26. Klik header kolom `Purchase PO` ketiga kali
27. Verifikasi urutan klik 3 Purchase PO kembali ke default

### TC-FA-LBL-562: Guard: kolom Warranty Expiry tidak ikut dicari di Drawer

28. Verifikasi kolom `Warranty Expiry` tampil dan `Gate Item - 51` bernilai `30 Jun 2027`
29. Klik icon Search di toolbar Drawer, ketik `30 Jun 2027`, tekan Enter
30. Verifikasi empty state `No results found` (kolom `Warranty Expiry` tidak ikut dicari walau tampil dan bernilai)
31. Klik `(←)` pada kotak Search
32. Pemulihan: klik header kolom Actions (⋯) Drawer, klik `Setup Column...`, hapus centang `Warranty Expiry` dan `Purchase PO`, lalu klik `[Save]`
33. Tutup Drawer Tagged Asset

### TC-FA-LBL-570: Keadaan — menang atas No access: field tidak berlaku bagi Asset Name aset tampil — apa pun hak

34. Klik chip `Gate Scope` di kolom Label
35. Klik header kolom Actions (⋯) Drawer, klik `Setup Column...`, centang `Asset Value (Commercial)`, `Warranty Expiry`, dan `Purchase PO`, lalu klik `[Save]`
36. Verifikasi `Purchase PO` pada `Gate Plain - 55` menampilkan `—` (field tidak berlaku bagi Asset Name aset), bukan `No access`, walau group `Gate Other` di luar hak
37. Verifikasi `Warranty Expiry` pada `Gate Plain - 55` menampilkan `No access` (field berlaku bagi semua aset dan pemanggil tidak berhak atas baris itu)
38. Verifikasi `Asset Value (Commercial)` pada `Gate Plain - 55` menampilkan `No access`
39. Pemulihan: klik header kolom Actions (⋯) Drawer, klik `Setup Column...`, hapus centang `Asset Value (Commercial)`, `Warranty Expiry`, dan `Purchase PO`, lalu klik `[Save]`
40. Tutup Drawer Tagged Asset

## Notes

- Sumber: `fixed-asset/settings-asset-labeling/TestCases/tc-settings-asset-labeling.md` section 4c (Drawer Tagged Asset). Subjudul `###` memetakan langkah ke TC granular.
- Penyimpangan urutan (bagian 3): kolom `Warranty Expiry` (TC-FA-LBL-549) dan `Purchase PO` (TC-FA-LBL-555) dicentang sekali pada blok pertamanya dan tetap tampil sampai TC-FA-LBL-562 (Drawer tetap terbuka); langkah klik chip dan mencentang kolom pada TC-FA-LBL-558 dan 562 tidak ditulis ulang karena keadaan yang dibutuhkannya sudah terpenuhi dan tidak ada Expected yang bergantung pada keadaan Hidden. Kolom dipulihkan sebelum TC-FA-LBL-570 (label `Gate Scope`).
- Langkah penghubung (S-03): `Klik (←) pada kotak Search`, Pemulihan kolom, dan tutup Drawer memulihkan keadaan awal (S-09).
- Ukuran spec (40 langkah, di atas smell 35 langkah): kelima TC satu kelas (fungsional, gerbang Warranty Expiry dan Custom Field Purchasing untuk Gate-Purchase) pada akun dan data Pre-setup #38 yang sama dan tiap blok berdiri sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna; langkah membengkak karena matriks nilai per baris, Sort enam klik, dan tiap klausa Expected menjadi satu `Verifikasi` (S-01).
- Temuan untuk QA:
  - TC-FA-LBL-558 klik 3 Purchase PO tidak menyebut baris yang diharapkan ("kembali ke default"); spec memverifikasi urutan default Name A-Z.
  - TC-FA-LBL-562 Expected a mensyaratkan kolom `Warranty Expiry` "tampil dan bernilai"; spec menambahkan `Verifikasi` kolom tampil dan `Gate Item - 51` bernilai sebagai anchor positif sebelum Search (bagian 8b butir 2).
