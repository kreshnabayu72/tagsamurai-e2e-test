---
id: TC-FA-LBL-E2E-123-gate-none-pemegang-view-tagged-assets-tanpa-hak-nilai-bagian-2-2
title: "Gate-None: Pemegang View Tagged Assets tanpa Hak Nilai (bagian 2/2)"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-LBL-561
coverage:
  web: automated
---

# Gate-None: Pemegang View Tagged Assets tanpa Hak Nilai (bagian 2/2)

## Prerequisites

- Mode: FE+BE. Backend nyata; tidak ada intercept.
- Akun aktor: Gate-None (`Company Gate`; capability Read Manage Asset Master Data; tanpa View asset value, Manage purchase, dan Manage accounting) (Pre-setup #39), `Fixture.assetLabeling.akun.gateNone`, `Spectra.env.FA_GATE_NONE_PASSWORD`. Login di hook `before` spec ini (menggantikan akun default suite); halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Asset Master > tab Labels). Hook `after` mengembalikan sesi ke akun default suite (Total Control Company Alpha, `Spectra.env.FA_LBL_TC_PASSWORD`).
- Hook suite: Guided Tooltip, pemulihan state global, dan pembukaan Settings > Asset Master > tab Labels mengikuti hook di `suite.md` dan tidak ditulis ulang di sini.
- Data Pre-setup `Company Gate` (#38), hanya dibaca dan dirujuk lewat `Fixture.assetLabeling.gate`: General Settings currency `Rp` (ribuan titik, desimal koma, 2 desimal) dan lisensi `FA-7` aktif; Group `Gate HQ` dengan anak `Gate Branch A`, dan Group `Gate Other` (terpisah); dua buku Asset Value tetap `Commercial` dan `Fiscal` (seluruh nilai Asset Value yang diasersi adalah nilai buku `Commercial`); Asset Name `Gate Item` dan `Gate Plain`; Custom Field Active (Scope Asset Name `Gate Item`): `Gate Note` (General, Text), `Gate Region` (General, Text, Value Type Global, nilai `APAC`), `Purchase PO` (Purchasing, Text), `Cost Center` (Accounting, Text); Custom Field Inactive `Retired Field` (General, Text); label `Gate Label` pada aset Active `Gate Item - 51` (Group `Gate HQ`; Asset Value 1500000; Warranty Expiry 30 Jun 2027; `Gate Note` `Note A`; `Purchase PO` `PO-001`; `Cost Center` `CC-10`), `Gate Item - 52` (Group `Gate HQ > Gate Branch A`; Asset Value 0; Warranty Expiry belum ada; `Purchase PO` dan `Cost Center` belum diisi), `Gate Item - 53` (Group `Gate Other`; Asset Value 2500000; Warranty Expiry 15 Jan 2028; `Purchase PO` `PO-003`; `Cost Center` `CC-30`), dan `Gate Plain - 54` (Group `Gate HQ`; Asset Value dan Warranty Expiry belum ada; di luar Scope seluruh Custom Field); label `Gate Scope` pada `Gate Plain - 55` (Active; Group `Gate Other`; Asset Value 700000; Warranty Expiry 01 Mar 2027; di luar Scope seluruh Custom Field).
- Data Dinamis: tidak ada.
- Fixture `fixtures/asset-labeling.json` (belum ada, disediakan tim FE; hanya identitas data, tanpa rahasia). Kunci yang dipakai spec ini: `Fixture.assetLabeling.akun.gateNone` (email akun masing-masing) dan `Fixture.assetLabeling.gate` (data Pre-setup #38).
- Kemampuan teknis (disediakan tim FE): hapus preferensi kolom Setup Column Drawer di browser (bagian 4).
- State global: konfigurasi kolom Setup Column Drawer Tagged Asset (preferensi browser) diubah dan dipulihkan oleh langkah spec; hook `after` spec ini menghapus preferensi kolom di browser sebagai cadangan, bukan `[Reset to Default]` (bagian 4). Kemampuan menghapus preferensi itu disediakan tim FE. Tidak ada state global lain yang diubah.
- Suite berjalan serial (`parallel: false`).
- Cleanup: spec tidak membuat data. Data Pre-setup hanya dibaca dan tidak diubah (Last Updated tidak berubah).
- Env var: `Spectra.env.FA_GATE_NONE_PASSWORD`, `Spectra.env.FA_LBL_TC_PASSWORD` terdaftar di `executionConfig.environmentVariables` dan `.env.example`. `FA_LBL_TC_PASSWORD` dipakai hanya oleh hook `after` untuk mengembalikan sesi ke akun default suite.

## Test Steps

### TC-FA-LBL-561: Drawer menampilkan baris client-wide bagi pemegang View Tagged Assets tanpa hak nilai, hanya sel bergerbang No access

1. Klik chip `Gate Label` di kolom Label
2. Verifikasi Total Asset `4` di blok identitas
3. Verifikasi empat baris tampil dengan default sort Name A-Z: `Gate Item - 51`, `Gate Item - 52`, `Gate Item - 53`, `Gate Plain - 54`
4. Klik header kolom Actions (⋯) Drawer, klik `Setup Column...`, centang `Asset Value (Commercial)` dan `Warranty Expiry`, lalu klik `[Save]`
5. Verifikasi sel `Name`, `Asset ID`, `Group`, dan `Status` terisi normal pada semua baris, termasuk `Gate Item - 53` di group `Gate Other`
6. Verifikasi sel `Asset Value (Commercial)` semua baris menampilkan `No access`
7. Verifikasi sel `Warranty Expiry` semua baris menampilkan `No access`
8. Pemulihan: klik header kolom Actions (⋯) Drawer, klik `Setup Column...`, hapus centang `Asset Value (Commercial)` dan `Warranty Expiry`, lalu klik `[Save]`
9. Tutup Drawer Tagged Asset

## Notes

- Sumber: `fixed-asset/settings-asset-labeling/TestCases/tc-settings-asset-labeling.md` section 4c (Drawer Tagged Asset). Subjudul `###` memetakan langkah ke TC granular.
- Langkah penghubung (S-03): Pemulihan kolom dan tutup Drawer memulihkan keadaan awal.
- Pembagian TC lintas spec: TC-FA-LBL-547 dan 554 (Gate-None) di spec 122 dan TC-FA-LBL-550 di spec 172 dan TC-FA-LBL-552 di spec 181; semuanya Company Gate (Pre-setup #38).
- Temuan untuk QA:
  - TC-FA-LBL-561 Langkah Uji 2 mengamati blok identitas dan keempat baris sebelum kolom bergerbang dicentang; kolom `Asset Value (Commercial)` dan `Warranty Expiry` dicentang pada Langkah Uji 3 TC sehingga Expected c diverifikasi sesudahnya.
