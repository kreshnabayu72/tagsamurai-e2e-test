---
id: TC-FA-LBL-E2E-121-gate-accounting-asset-value-dan-custom-field-accounting
title: "Gate-Accounting: Asset Value dan Custom Field Accounting"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-LBL-545
  - TC-FA-LBL-556
coverage:
  web: automated
---

# Gate-Accounting: Asset Value dan Custom Field Accounting

## Prerequisites

- Mode: FE+BE. Backend nyata; tidak ada intercept.
- Akun aktor: Gate-Accounting (`Company Gate`; Read Manage Asset Master Data; Global Role Manage accounting) (Pre-setup #42), `Fixture.assetLabeling.akun.gateAccounting`, `Spectra.env.FA_GATE_ACCOUNTING_PASSWORD`. Login di hook `before` spec ini (menggantikan akun default suite); halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Asset Master > tab Labels). Hook `after` mengembalikan sesi ke akun default suite (Total Control Company Alpha, `Spectra.env.FA_LBL_TC_PASSWORD`).
- Hook suite: Guided Tooltip, pemulihan state global, dan pembukaan Settings > Asset Master > tab Labels mengikuti hook di `suite.md` dan tidak ditulis ulang di sini.
- Data Pre-setup `Company Gate` (#38), hanya dibaca dan dirujuk lewat `Fixture.assetLabeling.gate`: General Settings currency `Rp` (ribuan titik, desimal koma, 2 desimal) dan lisensi `FA-7` aktif; Group `Gate HQ` dengan anak `Gate Branch A`, dan Group `Gate Other` (terpisah); dua buku Asset Value tetap `Commercial` dan `Fiscal` (seluruh nilai Asset Value yang diasersi adalah nilai buku `Commercial`); Asset Name `Gate Item` dan `Gate Plain`; Custom Field Active (Scope Asset Name `Gate Item`): `Gate Note` (General, Text), `Gate Region` (General, Text, Value Type Global, nilai `APAC`), `Purchase PO` (Purchasing, Text), `Cost Center` (Accounting, Text); Custom Field Inactive `Retired Field` (General, Text); label `Gate Label` pada aset Active `Gate Item - 51` (Group `Gate HQ`; Asset Value 1500000; Warranty Expiry 30 Jun 2027; `Gate Note` `Note A`; `Purchase PO` `PO-001`; `Cost Center` `CC-10`), `Gate Item - 52` (Group `Gate HQ > Gate Branch A`; Asset Value 0; Warranty Expiry belum ada; `Purchase PO` dan `Cost Center` belum diisi), `Gate Item - 53` (Group `Gate Other`; Asset Value 2500000; Warranty Expiry 15 Jan 2028; `Purchase PO` `PO-003`; `Cost Center` `CC-30`), dan `Gate Plain - 54` (Group `Gate HQ`; Asset Value `Pending` karena belum ada Purchase Cost, tooltip `Purchase cost has not been set.`; Warranty Expiry belum ada; di luar Scope seluruh Custom Field); label `Gate Scope` pada `Gate Plain - 55` (Active; Group `Gate Other`; Asset Value 700000; Warranty Expiry 01 Mar 2027; di luar Scope seluruh Custom Field).
- Data Dinamis: tidak ada.
- Fixture `fixtures/asset-labeling.json` (belum ada, disediakan tim FE; hanya identitas data, tanpa rahasia). Kunci yang dipakai spec ini: `Fixture.assetLabeling.akun.gateAccounting` (email akun masing-masing) dan `Fixture.assetLabeling.gate` (data Pre-setup #38).
- Kemampuan teknis (disediakan tim FE): hapus preferensi kolom Setup Column Drawer di browser (bagian 4).
- State global: konfigurasi kolom Setup Column Drawer Tagged Asset (preferensi browser) diubah dan dipulihkan oleh langkah spec; hook `after` spec ini menghapus preferensi kolom di browser sebagai cadangan, bukan `[Reset to Default]` (bagian 4). Kemampuan menghapus preferensi itu disediakan tim FE. Tidak ada state global lain yang diubah.
- Suite berjalan serial (`parallel: false`).
- Cleanup: spec tidak membuat data. Data Pre-setup hanya dibaca dan tidak diubah (Last Updated tidak berubah).
- Env var: `Spectra.env.FA_GATE_ACCOUNTING_PASSWORD`, `Spectra.env.FA_LBL_TC_PASSWORD` terdaftar di `executionConfig.environmentVariables` dan `.env.example`. `FA_LBL_TC_PASSWORD` dipakai hanya oleh hook `after` untuk mengembalikan sesi ke akun default suite.

## Test Steps

### TC-FA-LBL-545: Kolom Asset Value: default Hidden, format currency, nilai nol, dan Pending bila Purchase Cost belum ada (Manage accounting)

1. Klik chip `Gate Label` di kolom Label
2. Verifikasi kolom `Asset Value (Commercial)` tidak tampil
3. Klik header kolom Actions (⋯) Drawer, klik `Setup Column...`, centang `Asset Value (Commercial)`, lalu klik `[Save]`
4. Verifikasi `Gate Item - 51` menampilkan `Rp 1.500.000,00` (currency 2 desimal)
5. Verifikasi sel `Gate Item - 51` rata kanan
6. Verifikasi `Gate Item - 52` menampilkan `Rp 0,00` (bukan `—` dan bukan `No access`; currency nol sesuai General Settings)
7. Verifikasi `Gate Item - 53` menampilkan `Rp 2.500.000,00` (Manage accounting berlaku client-wide)
8. Verifikasi `Gate Plain - 54` menampilkan `Pending` (berhak, Purchase Cost belum ada), bukan `—`
9. Hover sel `Pending` pada `Gate Plain - 54`
10. Verifikasi tooltip `Purchase cost has not been set.`
11. Pemulihan: klik header kolom Actions (⋯) Drawer, klik `Setup Column...`, hapus centang `Asset Value (Commercial)`, lalu klik `[Save]`
12. Tutup Drawer Tagged Asset

### TC-FA-LBL-556: Custom Field Accounting: nilai client-wide, —, dan — untuk Asset Name di luar Scope

13. Klik chip `Gate Label` di kolom Label
14. Klik header kolom Actions (⋯) Drawer, klik `Setup Column...`, centang `Cost Center`, lalu klik `[Save]`
15. Verifikasi `Gate Item - 51` menampilkan `CC-10`
16. Verifikasi `Gate Item - 52` menampilkan `—` (belum diisi)
17. Verifikasi `Gate Item - 53` (`Gate Other`) menampilkan `CC-30` (Manage accounting berlaku client-wide)
18. Verifikasi `Gate Plain - 54` menampilkan `—` (Asset Name di luar Scope)
19. Verifikasi tidak ada sel `No access` pada kolom `Cost Center`
20. Pemulihan: klik header kolom Actions (⋯) Drawer, klik `Setup Column...`, hapus centang `Cost Center`, lalu klik `[Save]`
21. Tutup Drawer Tagged Asset

## Notes

- Sumber: `fixed-asset/settings-asset-labeling/TestCases/tc-settings-asset-labeling.md` section 4c (Drawer Tagged Asset). Subjudul `###` memetakan langkah ke TC granular.
- Langkah penghubung (S-03): Pemulihan kolom dan tutup Drawer sesudah TC-FA-LBL-545 memulihkan keadaan awal (S-09).
- Temuan untuk QA:
  - TC-FA-LBL-545 Expected b menyebut "currency 2 desimal, rata kanan" dalam satu butir; spec memecahnya menjadi dua `Verifikasi` (teks nilai dan perataan).
