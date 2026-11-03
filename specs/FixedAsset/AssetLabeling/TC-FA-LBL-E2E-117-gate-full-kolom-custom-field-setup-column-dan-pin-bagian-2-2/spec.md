---
id: TC-FA-LBL-E2E-117-gate-full-kolom-custom-field-setup-column-dan-pin-bagian-2-2
title: "Gate-Full: Kolom Custom Field, Setup Column, dan Pin (bagian 2/2)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-LBL-560
coverage:
  web: automated
---

# Gate-Full: Kolom Custom Field, Setup Column, dan Pin (bagian 2/2)

## Prerequisites

- Mode: FE+BE. Backend nyata; tidak ada intercept.
- Akun aktor: Gate-Full (`Company Gate`; Read Manage Asset Master Data; View asset value dan Manage purchase pada `Gate HQ`; Manage accounting) (Pre-setup #44), `Fixture.assetLabeling.akun.gateFull`, `Spectra.env.FA_GATE_FULL_PASSWORD`. Login di hook `before` spec ini (menggantikan akun default suite); halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Asset Master > tab Labels). Hook `after` mengembalikan sesi ke akun default suite (Total Control Company Alpha, `Spectra.env.FA_LBL_TC_PASSWORD`).
- Hook suite: Guided Tooltip, pemulihan state global, dan pembukaan Settings > Asset Master > tab Labels mengikuti hook di `suite.md` dan tidak ditulis ulang di sini.
- Data Pre-setup `Company Gate` (#38), hanya dibaca dan dirujuk lewat `Fixture.assetLabeling.gate`: General Settings currency `Rp` (ribuan titik, desimal koma, 2 desimal) dan lisensi `FA-7` aktif; Group `Gate HQ` dengan anak `Gate Branch A`, dan Group `Gate Other` (terpisah); dua buku Asset Value tetap `Commercial` dan `Fiscal` (seluruh nilai Asset Value yang diasersi adalah nilai buku `Commercial`); Asset Name `Gate Item` dan `Gate Plain`; Custom Field Active (Scope Asset Name `Gate Item`): `Gate Note` (General, Text), `Gate Region` (General, Text, Value Type Global, nilai `APAC`), `Purchase PO` (Purchasing, Text), `Cost Center` (Accounting, Text); Custom Field Inactive `Retired Field` (General, Text); label `Gate Label` pada aset Active `Gate Item - 51` (Group `Gate HQ`; Asset Value 1500000; Warranty Expiry 30 Jun 2027; `Gate Note` `Note A`; `Purchase PO` `PO-001`; `Cost Center` `CC-10`), `Gate Item - 52` (Group `Gate HQ > Gate Branch A`; Asset Value 0; Warranty Expiry belum ada; `Purchase PO` dan `Cost Center` belum diisi), `Gate Item - 53` (Group `Gate Other`; Asset Value 2500000; Warranty Expiry 15 Jan 2028; `Purchase PO` `PO-003`; `Cost Center` `CC-30`), dan `Gate Plain - 54` (Group `Gate HQ`; Asset Value dan Warranty Expiry belum ada; di luar Scope seluruh Custom Field); label `Gate Scope` pada `Gate Plain - 55` (Active; Group `Gate Other`; Asset Value 700000; Warranty Expiry 01 Mar 2027; di luar Scope seluruh Custom Field).
- Data Dinamis: tidak ada.
- Fixture `fixtures/asset-labeling.json` (belum ada, disediakan tim FE; hanya identitas data, tanpa rahasia). Kunci yang dipakai spec ini: `Fixture.assetLabeling.akun.gateFull` (email akun masing-masing) dan `Fixture.assetLabeling.gate` (data Pre-setup #38).
- Kemampuan teknis (disediakan tim FE): hapus preferensi kolom Setup Column Drawer di browser (bagian 4).
- State global: konfigurasi kolom Setup Column Drawer Tagged Asset (preferensi browser) diubah dan dipulihkan oleh langkah spec; hook `after` spec ini menghapus preferensi kolom di browser sebagai cadangan, bukan `[Reset to Default]` (bagian 4). Kemampuan menghapus preferensi itu disediakan tim FE. Tidak ada state global lain yang diubah.
- Suite berjalan serial (`parallel: false`).
- Cleanup: spec tidak membuat data. Data Pre-setup hanya dibaca dan tidak diubah (Last Updated tidak berubah).
- Env var: `Spectra.env.FA_GATE_FULL_PASSWORD`, `Spectra.env.FA_LBL_TC_PASSWORD` terdaftar di `executionConfig.environmentVariables` dan `.env.example`. `FA_LBL_TC_PASSWORD` dipakai hanya oleh hook `after` untuk mengembalikan sesi ke akun default suite.

## Test Steps

### TC-FA-LBL-560: Search Drawer kolom Custom Field: nilai dicari, nilai dan teks No access tidak dicari

1. Klik chip `Gate Label` di kolom Label
2. Klik header kolom Actions (⋯) Drawer, klik `Setup Column...`, centang `Gate Note`, `Purchase PO`, dan `Cost Center`, lalu klik `[Save]`
3. Klik icon Search di toolbar Drawer, ketik `PO-001`, tekan Enter
4. Verifikasi hanya `Gate Item - 51` tampil (Search `PO-001`)
5. Ganti isi kotak search dengan `PO-003`, tekan Enter
6. Verifikasi empty state `No results found` (nilai sel `No access` pada `Gate Item - 53` tidak dicari)
7. Ganti isi kotak search dengan `No access`, tekan Enter
8. Verifikasi empty state `No results found` (teks `No access` tidak dicari)
9. Ganti isi kotak search dengan `Note A`, tekan Enter
10. Verifikasi hanya `Gate Item - 51` tampil (Search `Note A`)
11. Ganti isi kotak search dengan `CC-30`, tekan Enter
12. Verifikasi hanya `Gate Item - 53` tampil (Manage accounting berlaku client-wide)
13. Klik `(←)` pada kotak Search
14. Pemulihan: klik header kolom Actions (⋯) Drawer, klik `Setup Column...`, hapus centang `Gate Note`, `Purchase PO`, dan `Cost Center`, lalu klik `[Save]`
15. Tutup Drawer Tagged Asset

## Notes

- Sumber: `fixed-asset/settings-asset-labeling/TestCases/tc-settings-asset-labeling.md` section 4c (Drawer Tagged Asset). Subjudul `###` memetakan langkah ke TC granular.
- Langkah penghubung (S-03): `Klik (←) pada kotak Search`, Pemulihan kolom, dan tutup Drawer memulihkan keadaan awal.
- Pembagian TC lintas spec: Setup Column dan Pin Gate-Full (TC-FA-LBL-534, 535, 553) ada di spec 116.
- Temuan untuk QA: tidak ada temuan TC sumber untuk TC-FA-LBL-560; asersi empty state pada Search `PO-003`, `No access` didahului anchor positif Search `PO-001` yang menampilkan `Gate Item - 51`.
