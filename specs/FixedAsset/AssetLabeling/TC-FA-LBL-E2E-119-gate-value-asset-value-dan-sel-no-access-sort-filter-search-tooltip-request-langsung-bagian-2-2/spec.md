---
id: TC-FA-LBL-E2E-119-gate-value-asset-value-dan-sel-no-access-sort-filter-search-tooltip-request-langsung-bagian-2-2
title: "Gate-Value: Asset Value dan Sel No access (Sort, Filter, Search, Tooltip, Request Langsung) (bagian 2/2)"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-FA-LBL-551
  - TC-FA-LBL-566
coverage:
  web: automated
---

# Gate-Value: Asset Value dan Sel No access (Sort, Filter, Search, Tooltip, Request Langsung) (bagian 2/2)

## Prerequisites

- Mode: FE+BE. Backend nyata; tidak ada intercept.
- Akun aktor: Gate-Value (`Company Gate`; Read Manage Asset Master Data; Group Role View asset value pada `Gate HQ`) (Pre-setup #40), `Fixture.assetLabeling.akun.gateValue`, `Spectra.env.FA_GATE_VALUE_PASSWORD`. Login di hook `before` spec ini (menggantikan akun default suite); halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Asset Master > tab Labels). Hook `after` mengembalikan sesi ke akun default suite (Total Control Company Alpha, `Spectra.env.FA_LBL_TC_PASSWORD`).
- Akun aktor: Gate-Purchase (`Company Gate`; Read Manage Asset Master Data; Group Role Manage purchase pada `Gate HQ`) (Pre-setup #41), `Fixture.assetLabeling.akun.gatePurchase`, `Spectra.env.FA_GATE_PURCHASE_PASSWORD`. Dipakai pada langkah Ganti akun.
- Hook suite: Guided Tooltip, pemulihan state global, dan pembukaan Settings > Asset Master > tab Labels mengikuti hook di `suite.md` dan tidak ditulis ulang di sini.
- Data Pre-setup `Company Gate` (#38), hanya dibaca dan dirujuk lewat `Fixture.assetLabeling.gate`: General Settings currency `Rp` (ribuan titik, desimal koma, 2 desimal) dan lisensi `FA-7` aktif; Group `Gate HQ` dengan anak `Gate Branch A`, dan Group `Gate Other` (terpisah); dua buku Asset Value tetap `Commercial` dan `Fiscal` (seluruh nilai Asset Value yang diasersi adalah nilai buku `Commercial`); Asset Name `Gate Item` dan `Gate Plain`; Custom Field Active (Scope Asset Name `Gate Item`): `Gate Note` (General, Text), `Gate Region` (General, Text, Value Type Global, nilai `APAC`), `Purchase PO` (Purchasing, Text), `Cost Center` (Accounting, Text); Custom Field Inactive `Retired Field` (General, Text); label `Gate Label` pada aset Active `Gate Item - 51` (Group `Gate HQ`; Asset Value 1500000; Warranty Expiry 30 Jun 2027; `Gate Note` `Note A`; `Purchase PO` `PO-001`; `Cost Center` `CC-10`), `Gate Item - 52` (Group `Gate HQ > Gate Branch A`; Asset Value 0; Warranty Expiry belum ada; `Purchase PO` dan `Cost Center` belum diisi), `Gate Item - 53` (Group `Gate Other`; Asset Value 2500000; Warranty Expiry 15 Jan 2028; `Purchase PO` `PO-003`; `Cost Center` `CC-30`), dan `Gate Plain - 54` (Group `Gate HQ`; Asset Value dan Warranty Expiry belum ada; di luar Scope seluruh Custom Field); label `Gate Scope` pada `Gate Plain - 55` (Active; Group `Gate Other`; Asset Value 700000; Warranty Expiry 01 Mar 2027; di luar Scope seluruh Custom Field).
- Data Dinamis: tidak ada.
- Fixture `fixtures/asset-labeling.json` (belum ada, disediakan tim FE; hanya identitas data, tanpa rahasia). Kunci yang dipakai spec ini: `Fixture.assetLabeling.akun.gateValue`, `Fixture.assetLabeling.akun.gatePurchase` (email akun masing-masing) dan `Fixture.assetLabeling.gate` (data Pre-setup #38).
- Kemampuan teknis (disediakan tim FE): hapus preferensi kolom Setup Column Drawer di browser (bagian 4). Klien HTTP untuk permintaan langsung ke server (TC-FA-LBL-566) dengan sesi API aktor Gate-Value (login API password, token tidak dihitung sebagai sesi web; dinyatakan di `suite.md`).
- State global: konfigurasi kolom Setup Column Drawer Tagged Asset (preferensi browser) diubah dan dipulihkan oleh langkah spec; hook `after` spec ini menghapus preferensi kolom di browser sebagai cadangan, bukan `[Reset to Default]` (bagian 4). Kemampuan menghapus preferensi itu disediakan tim FE. Tidak ada state global lain yang diubah.
- Suite berjalan serial (`parallel: false`).
- Cleanup: spec tidak membuat data. Data Pre-setup hanya dibaca dan tidak diubah (Last Updated tidak berubah).
- Env var: `Spectra.env.FA_GATE_VALUE_PASSWORD`, `Spectra.env.FA_GATE_PURCHASE_PASSWORD`, `Spectra.env.FA_LBL_TC_PASSWORD` terdaftar di `executionConfig.environmentVariables` dan `.env.example`. `FA_LBL_TC_PASSWORD` dipakai hanya oleh hook `after` untuk mengembalikan sesi ke akun default suite.

## Test Steps

### TC-FA-LBL-551: Tooltip sel No access: Asset Value, Warranty Expiry, dan Custom Field Purchasing

1. Klik chip `Gate Label` di kolom Label
2. Klik header kolom Actions (⋯) Drawer, klik `Setup Column...`, centang `Asset Value (Commercial)`, lalu klik `[Save]`
3. Hover sel `No access` pada `Gate Item - 53`
4. Verifikasi tooltip Asset Value (Commercial) `Requires View asset value access in this group.`
5. Pemulihan: klik header kolom Actions (⋯) Drawer, klik `Setup Column...`, hapus centang `Asset Value (Commercial)`, lalu klik `[Save]`
6. Tutup Drawer Tagged Asset
7. Ganti akun: Logout, login sebagai Gate-Purchase `Fixture.assetLabeling.akun.gatePurchase` (`Spectra.env.FA_GATE_PURCHASE_PASSWORD`), buka Fixed Asset > Settings > Asset Master > tab Labels
8. Klik chip `Gate Label` di kolom Label
9. Klik header kolom Actions (⋯) Drawer, klik `Setup Column...`, centang `Warranty Expiry` dan `Purchase PO`, lalu klik `[Save]`
10. Hover sel `No access` kolom `Warranty Expiry` pada `Gate Item - 53`
11. Verifikasi tooltip Warranty Expiry `Requires Manage purchase access in this group.`
12. Hover sel `No access` kolom `Purchase PO` pada `Gate Item - 53`
13. Verifikasi tooltip Purchase PO `Requires Manage purchase access in this group.`
14. Pemulihan: klik header kolom Actions (⋯) Drawer, klik `Setup Column...`, hapus centang `Warranty Expiry` dan `Purchase PO`, lalu klik `[Save]`
15. Tutup Drawer Tagged Asset

### TC-FA-LBL-566: Permintaan langsung ke server tidak mengirim nilai sel No access

16. Kirim permintaan langsung ke server dengan sesi API Gate-Value (`Fixture.assetLabeling.akun.gateValue`, `Spectra.env.FA_GATE_VALUE_PASSWORD`): ambil daftar Tagged Assets label `Gate Label` dengan kolom `Asset Value (Commercial)` dan `Warranty Expiry` diminta
17. Verifikasi sel `Asset Value (Commercial)` `Gate Item - 53` pada respons berstatus `No access` tanpa nilai
18. Verifikasi nilai 2500000 tidak ada di respons
19. Verifikasi sel `Asset Value (Commercial)` `Gate Item - 51` pada respons memuat nilai 1500000
20. Verifikasi sel `Asset Value (Commercial)` `Gate Item - 52` pada respons memuat nilai nol
21. Verifikasi sel `Warranty Expiry` semua baris respons (`Gate Item - 51` sampai `Gate Plain - 54`) berstatus `No access` tanpa nilai
22. Verifikasi nilai 15 Jan 2028 dan 30 Jun 2027 tidak ada di respons

## Notes

- Sumber: `fixed-asset/settings-asset-labeling/TestCases/tc-settings-asset-labeling.md` section 4c (Drawer Tagged Asset). Subjudul `###` memetakan langkah ke TC granular.
- Penyimpangan urutan (bagian 3): TC-FA-LBL-551 dulu (Ganti akun ke Gate-Purchase ditulis eksplisit pada Langkah Uji 4 TC), lalu TC-FA-LBL-566 (request langsung) dengan sesi API Gate-Value; sesi API tidak bergantung pada akun UI aktif.
- Langkah penghubung (S-03): Pemulihan kolom dan tutup Drawer memulihkan keadaan awal.
- P-5 (b): TC-FA-LBL-566 (kelas a defense-in-depth, request langsung ke server) adalah satu-satunya objek-uji ringan kelas a di spec ini; ia berada di spec fungsional gerbang Drawer yang permukaannya sama (Drawer Tagged Asset Gate-Value). Asersinya hanya isi respons server (8b butir 1); perilaku FE untuk sel `No access` diasersi di langkah TC-FA-LBL-551 dan spec 118.
- K-1: TC-FA-LBL-566 berkelas a dengan Expected berupa isi respons API dan state data; TC tetap masuk spec FE+BE walau tumpang tindih dengan `tc-settings-asset-labeling-backend.md`, karena TC granular tetap sumber dan tiap TC tepat satu spec.
- Pembagian TC lintas spec: sort, filter, search, dan tampilan Asset Value Gate-Value (TC-FA-LBL-546, 557, 559, 576) ada di spec 118.
- Temuan untuk QA:
  - TC-FA-LBL-566 Langkah Uji 1 menyebut "mengambil daftar Tagged Assets label `Gate Label`" tanpa menyebut endpoint atau parameter permintaan; spec tidak mengarang endpoint (S-13) dan menyerahkan bentuk permintaan sebagai kemampuan klien HTTP yang disediakan tim FE/BE.
  - TC-FA-LBL-566 Expected b dan c ("memuat nilai 1500000", "`No access` tanpa nilai") tidak menyebut bentuk representasi status `No access` pada respons.
