---
id: TC-FA-LBL-E2E-116-gate-full-kolom-custom-field-setup-column-dan-pin-bagian-1-2
title: "Gate-Full: Kolom Custom Field, Setup Column, dan Pin (bagian 1/2)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-LBL-534
  - TC-FA-LBL-535
  - TC-FA-LBL-553
coverage:
  web: automated
---

# Gate-Full: Kolom Custom Field, Setup Column, dan Pin (bagian 1/2)

## Prerequisites

- Mode: FE+BE. Backend nyata; tidak ada intercept.
- Akun aktor: Gate-Full (`Company Gate`; Read Manage Asset Master Data; View asset value dan Manage purchase pada `Gate HQ`; Manage accounting) (Pre-setup #44), `Fixture.assetLabeling.akun.gateFull`, `Spectra.env.FA_GATE_FULL_PASSWORD`. Login di hook `before` spec ini (menggantikan akun default suite); halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Asset Master > tab Labels). Hook `after` mengembalikan sesi ke akun default suite (Total Control Company Alpha, `Spectra.env.FA_LBL_TC_PASSWORD`).
- Hook suite: Guided Tooltip, pemulihan state global, dan pembukaan Settings > Asset Master > tab Labels mengikuti hook di `suite.md` dan tidak ditulis ulang di sini.
- Data Pre-setup `Company Gate` (#38), hanya dibaca dan dirujuk lewat `Fixture.assetLabeling.gate`: General Settings currency `Rp` (ribuan titik, desimal koma, 2 desimal) dan lisensi `FA-7` aktif; Group `Gate HQ` dengan anak `Gate Branch A`, dan Group `Gate Other` (terpisah); dua buku Asset Value tetap `Commercial` dan `Fiscal` (seluruh nilai Asset Value yang diasersi adalah nilai buku `Commercial`); Asset Name `Gate Item` dan `Gate Plain`; Custom Field Active (Scope Asset Name `Gate Item`): `Gate Note` (General, Text), `Gate Region` (General, Text, Value Type Global, nilai `APAC`), `Purchase PO` (Purchasing, Text), `Cost Center` (Accounting, Text); Custom Field Inactive `Retired Field` (General, Text); label `Gate Label` pada aset Active `Gate Item - 51` (Group `Gate HQ`; Asset Value 1500000; Warranty Expiry 30 Jun 2027; `Gate Note` `Note A`; `Purchase PO` `PO-001`; `Cost Center` `CC-10`), `Gate Item - 52` (Group `Gate HQ > Gate Branch A`; Asset Value 0; Warranty Expiry belum ada; `Purchase PO` dan `Cost Center` belum diisi), `Gate Item - 53` (Group `Gate Other`; Asset Value 2500000; Warranty Expiry 15 Jan 2028; `Purchase PO` `PO-003`; `Cost Center` `CC-30`), dan `Gate Plain - 54` (Group `Gate HQ`; Asset Value dan Warranty Expiry belum ada; di luar Scope seluruh Custom Field); label `Gate Scope` pada `Gate Plain - 55` (Active; Group `Gate Other`; Asset Value 700000; Warranty Expiry 01 Mar 2027; di luar Scope seluruh Custom Field).
- Data Dinamis: tidak ada.
- Fixture `fixtures/asset-labeling.json` (belum ada, disediakan tim FE; hanya identitas data, tanpa rahasia). Kunci yang dipakai spec ini: `Fixture.assetLabeling.akun.gateFull` (email akun masing-masing) dan `Fixture.assetLabeling.gate` (data Pre-setup #38).
- Kemampuan teknis (disediakan tim FE): hapus preferensi kolom Setup Column Drawer di browser (bagian 4).
- Kemampuan teknis: mempersempit lebar viewport sampai tabel Drawer dapat di-scroll horizontal dan mengamati kolom membeku (sticky) saat scroll; lebar dan mekanisme observasi ditetapkan tim FE saat script.
- State global: konfigurasi kolom Setup Column Drawer Tagged Asset (preferensi browser) diubah dan dipulihkan oleh langkah spec; hook `after` spec ini menghapus preferensi kolom di browser sebagai cadangan, bukan `[Reset to Default]` (bagian 4). Kemampuan menghapus preferensi itu disediakan tim FE. Lebar viewport dipersempit pada langkah 38 dan dipulihkan pada langkah 48; hook `after` spec ini memulihkan viewport sebagai cadangan. Tidak ada state global lain yang diubah.
- Suite berjalan serial (`parallel: false`).
- Cleanup: spec tidak membuat data. Data Pre-setup hanya dibaca dan tidak diubah (Last Updated tidak berubah).
- Env var: `Spectra.env.FA_GATE_FULL_PASSWORD`, `Spectra.env.FA_LBL_TC_PASSWORD` terdaftar di `executionConfig.environmentVariables` dan `.env.example`. `FA_LBL_TC_PASSWORD` dipakai hanya oleh hook `after` untuk mengembalikan sesi ke akun default suite.

## Test Steps

### TC-FA-LBL-553: Kolom Custom Field: urutan grup, default Hidden, ceklis, dan tidak ada field Filter

1. Klik chip `Gate Label` di kolom Label
2. Klik header kolom Actions (⋯) Drawer, klik `Setup Column...`
3. Verifikasi urutan daftar kolom: `Name`, `Asset ID`, `TAG`, `Brand`, `Model/Type`, `Measurement`, `Category`, `Group`, `Label`, `Status`, `Transactional Policy`, `Last Scanned`, `Asset Value (Commercial)`, `Asset Value (Fiscal)`, `Warranty Expiry`, `Gate Note`, `Gate Region`, `Purchase PO`, `Cost Center`, `Last Updated` (grup General, Purchasing, Accounting, lalu Field Name A-Z dalam grup)
4. Verifikasi keempat kolom Custom Field (`Gate Note`, `Gate Region`, `Purchase PO`, `Cost Center`) tidak tercentang
5. Verifikasi checkbox keempat kolom Custom Field enabled (Curated)
6. Centang `Gate Note`, `Gate Region`, `Purchase PO`, dan `Cost Center`, lalu klik `[Save]`
7. Verifikasi keempat kolom Custom Field tampil di antara `Warranty Expiry` dan `Last Updated`
8. Klik icon Filter di toolbar Drawer dan baca daftar field
9. Verifikasi Filter Panel memuat field `Asset Value (Commercial)`, `Asset Value (Fiscal)`, dan `Warranty Expiry`
10. Verifikasi Filter Panel tidak memuat field untuk keempat Custom Field bertipe Text
11. Tutup panel Filter
12. Pemulihan: klik header kolom Actions (⋯) Drawer, klik `Setup Column...`, hapus centang `Gate Note`, `Gate Region`, `Purchase PO`, dan `Cost Center`, lalu klik `[Save]`
13. Tutup Drawer Tagged Asset

### TC-FA-LBL-534: Setup Column Drawer: drag reorder kolom Curated baru dan Custom Field

14. Klik chip `Gate Label` di kolom Label
15. Klik header kolom Actions (⋯) Drawer, klik `Setup Column...`, lalu centang `Measurement`, `Transactional Policy`, `Last Scanned`, `Asset Value (Commercial)`, `Warranty Expiry`, dan `Gate Note` (tanpa `[Save]`)
16. Seret `Gate Note` ke posisi paling atas daftar
17. Verifikasi `Gate Note` menjadi kolom pertama di Live Preview
18. Seret `Warranty Expiry` ke posisi paling atas
19. Verifikasi `Warranty Expiry` menjadi kolom pertama di Live Preview, diikuti `Gate Note`
20. Seret `Asset Value (Commercial)` ke posisi paling atas
21. Verifikasi `Asset Value (Commercial)` menjadi kolom pertama di Live Preview, diikuti `Warranty Expiry`, `Gate Note`
22. Seret `Last Scanned` ke posisi paling atas
23. Verifikasi `Last Scanned` menjadi kolom pertama di Live Preview, diikuti `Asset Value (Commercial)`, `Warranty Expiry`, `Gate Note`
24. Seret `Transactional Policy` ke posisi paling atas
25. Verifikasi `Transactional Policy` menjadi kolom pertama di Live Preview, diikuti `Last Scanned`, `Asset Value (Commercial)`, `Warranty Expiry`, `Gate Note`
26. Seret `Measurement` ke posisi paling atas
27. Verifikasi `Measurement` menjadi kolom pertama di Live Preview, diikuti `Transactional Policy`, `Last Scanned`, `Asset Value (Commercial)`, `Warranty Expiry`, `Gate Note`
28. Klik `[Save]`, tekan F5, lalu buka Drawer `Gate Label` kembali dengan klik chip `Gate Label` di kolom Label
29. Verifikasi urutan header tabel Drawer `Measurement`, `Transactional Policy`, `Last Scanned`, `Asset Value (Commercial)`, `Warranty Expiry`, `Gate Note`, lalu `Name`, `Asset ID`, `TAG`, `Brand`, `Model/Type`, `Group`, `Status`, `Last Updated`, dan bertahan setelah reload
30. Hapus preferensi kolom Setup Column Drawer di browser (kemampuan disediakan tim FE)
31. Tutup Drawer Tagged Asset

### TC-FA-LBL-535: Setup Column Drawer: pin kolom TAG, Curated baru, dan Custom Field serta batas pin ketiga

32. Klik chip `Gate Label` di kolom Label
33. Klik header kolom Actions (⋯) Drawer, klik `Setup Column...`, lalu centang `Measurement`, `Transactional Policy`, `Last Scanned`, `Asset Value (Commercial)`, `Warranty Expiry`, dan `Gate Note` (tanpa `[Save]`)
34. Klik icon Pin `TAG`, `Measurement`, dan `Transactional Policy` satu per satu
35. Hover icon Pin `Last Scanned`
36. Verifikasi icon Pin `Last Scanned` disabled dengan tooltip `Maximum 3 columns can be pinned at once. Unpin another column first.`
37. Klik `[Save]`
38. Persempit lebar viewport sampai tabel Drawer dapat di-scroll horizontal
39. Scroll tabel horizontal
40. Verifikasi `TAG`, `Measurement`, dan `Transactional Policy` membeku di kiri saat scroll
41. Verifikasi kolom lain ikut bergeser saat scroll
42. Klik header kolom Actions (⋯) Drawer, klik `Setup Column...`, lepas pin `TAG`, `Measurement`, dan `Transactional Policy`, klik icon Pin `Last Scanned`, `Asset Value (Commercial)`, dan `Warranty Expiry`, klik `[Save]`, lalu scroll tabel horizontal
43. Verifikasi `Last Scanned`, `Asset Value (Commercial)`, dan `Warranty Expiry` membeku saat scroll
44. Verifikasi `TAG`, `Measurement`, dan `Transactional Policy` ikut bergeser saat scroll
45. Klik header kolom Actions (⋯) Drawer, klik `Setup Column...`, lepas pin `Last Scanned`, `Asset Value (Commercial)`, dan `Warranty Expiry`, klik icon Pin `Gate Note`, klik `[Save]`, lalu scroll tabel horizontal
46. Verifikasi `Gate Note` membeku saat scroll
47. Verifikasi `Last Scanned`, `Asset Value (Commercial)`, dan `Warranty Expiry` ikut bergeser saat scroll
48. Pulihkan lebar viewport ke ukuran semula
49. Hapus preferensi kolom Setup Column Drawer di browser (kemampuan disediakan tim FE)
50. Tutup Drawer Tagged Asset

## Notes

- Sumber: `fixed-asset/settings-asset-labeling/TestCases/tc-settings-asset-labeling.md` section 4c (Drawer Tagged Asset). Subjudul `###` memetakan langkah ke TC granular.
- Penyimpangan urutan (bagian 3): TC-FA-LBL-553 (daftar kolom dan default Hidden) ditaruh paling awal karena membaca keadaan default Setup Column; TC-FA-LBL-534 lalu 535 sesudahnya, masing-masing diawali preferensi kolom bersih.
- Langkah penghubung (S-03): langkah 38 mempersempit lebar viewport agar tabel Drawer dapat di-scroll horizontal dan langkah 48 memulihkannya (S-09); Pemulihan kolom, `Hapus preferensi kolom Setup Column Drawer di browser`, tutup panel Filter, dan tutup Drawer memulihkan keadaan awal blok berikutnya (S-09); tekan F5 pada TC-FA-LBL-534 tidak meninggalkan form dirty (Setup Column sudah disimpan).
- Pembagian TC lintas spec: Search Custom Field untuk Gate-Full (TC-FA-LBL-560) ada di spec 117.
- Ukuran spec (50 langkah, di atas smell 35 langkah): ketiga TC satu kelas (fungsional, Setup Column Drawer dengan kolom Curated baru dan Custom Field) pada akun Gate-Full dan data Pre-setup #38 yang sama dan tiap blok berdiri sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna; langkah membengkak karena drag enam kali dengan satu `Verifikasi` per langkah TC dan tiap klausa Expected menjadi satu `Verifikasi` (S-01).
- Temuan untuk QA:
  - TC-FA-LBL-534 Expected g menggabungkan urutan header dan "bertahan setelah reload" sebagai satu butir tetapi Langkah Uji 9 hanya mengamati sesudah F5; spec memverifikasi urutan sesudah F5 (satu `Verifikasi`).
  - TC-FA-LBL-535 tidak menyebut lebar viewport 'sempit' secara numerik dan cara mengamati kolom membeku saat scroll; lebar dan mekanisme observasi (posisi sticky) ditetapkan tim FE saat script.
  - TC-FA-LBL-535 Langkah Uji 5 dan 6 menyebut "lepas pin ketiga kolom itu" tanpa menyebut bahwa pin dilepas sebelum Save; spec melepas pin, memasang pin baru, lalu klik `[Save]` sesuai urutan TC.
  - TC-FA-LBL-553 Expected d menyebut daftar field Filter Panel tidak memuat Custom Field Text sambil menyebut field `Asset Value (Commercial)`, `Asset Value (Fiscal)`, dan `Warranty Expiry` ada; spec memverifikasi keberadaan ketiga field itu lebih dulu sebagai anchor absence (bagian 8b butir 2).
