---
id: TC-FA-LBL-E2E-172-role-matrix-gate-ketersediaan-kolom-warranty-expiry-dan-custom-field-per-role
title: "Role Matrix Gate: Ketersediaan Kolom Warranty Expiry dan Custom Field per Role (bagian 1/2)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-LBL-550
coverage:
  web: automated
---

# Role Matrix Gate: Ketersediaan Kolom Warranty Expiry dan Custom Field per Role (bagian 1/2)

## Prerequisites

- Mode: FE+BE. Backend nyata; tidak ada intercept.
- Akun aktor: Gate-None (`Company Gate`; capability Read Manage Asset Master Data; tanpa View asset value, Manage purchase, dan Manage accounting) (Pre-setup #39), `Fixture.assetLabeling.akun.gateNone`, `Spectra.env.FA_GATE_NONE_PASSWORD`. Login di hook `before` spec ini (menggantikan akun default suite); halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Asset Master > tab Labels). Hook `after` mengembalikan sesi ke akun default suite (Total Control Company Alpha, `Spectra.env.FA_LBL_TC_PASSWORD`).
- Akun aktor: Gate-Value (`Company Gate`; Read Manage Asset Master Data; Group Role View asset value pada `Gate HQ`) (Pre-setup #40), `Fixture.assetLabeling.akun.gateValue`, `Spectra.env.FA_GATE_VALUE_PASSWORD`. Dipakai pada langkah Ganti akun.
- Akun aktor: Gate-Accounting (`Company Gate`; Read Manage Asset Master Data; Global Role Manage accounting) (Pre-setup #42), `Fixture.assetLabeling.akun.gateAccounting`, `Spectra.env.FA_GATE_ACCOUNTING_PASSWORD`. Dipakai pada langkah Ganti akun.
- Hook suite: Guided Tooltip, pemulihan state global, dan pembukaan Settings > Asset Master > tab Labels mengikuti hook di `suite.md` dan tidak ditulis ulang di sini.
- Data Pre-setup `Company Gate` (#38), hanya dibaca dan dirujuk lewat `Fixture.assetLabeling.gate`: lisensi `FA-7` aktif; Group `Gate HQ` dengan anak `Gate Branch A`, dan Group `Gate Other` (terpisah); Asset Name `Gate Item`; label `Gate Label` pada aset Active `Gate Item - 51` (Group `Gate HQ`; Warranty Expiry 30 Jun 2027), `Gate Item - 52` (Group `Gate HQ > Gate Branch A`; Warranty Expiry belum ada), dan `Gate Item - 53` (Group `Gate Other`; Warranty Expiry 15 Jan 2028).
- Data Dinamis: tidak ada.
- Fixture `fixtures/asset-labeling.json` (belum ada, disediakan tim FE; hanya identitas data, tanpa rahasia). Kunci yang dipakai spec ini: `Fixture.assetLabeling.akun.gateNone`, `Fixture.assetLabeling.akun.gateValue`, `Fixture.assetLabeling.akun.gateAccounting` (email akun masing-masing) dan `Fixture.assetLabeling.gate` (data Pre-setup #38).
- Kemampuan teknis (disediakan tim FE): hapus preferensi kolom Setup Column Drawer di browser (bagian 4).
- State global: konfigurasi kolom Setup Column Drawer Tagged Asset (preferensi browser) diubah dan dipulihkan oleh langkah spec; hook `after` spec ini menghapus preferensi kolom di browser sebagai cadangan, bukan `[Reset to Default]` (bagian 4). Kemampuan menghapus preferensi itu disediakan tim FE. Tidak ada state global lain yang diubah.
- Suite berjalan serial (`parallel: false`).
- Cleanup: spec tidak membuat data. Data Pre-setup hanya dibaca dan tidak diubah (Last Updated tidak berubah).
- Env var: `Spectra.env.FA_GATE_NONE_PASSWORD`, `Spectra.env.FA_GATE_VALUE_PASSWORD`, `Spectra.env.FA_GATE_ACCOUNTING_PASSWORD`, `Spectra.env.FA_LBL_TC_PASSWORD` terdaftar di `executionConfig.environmentVariables` dan `.env.example`. `FA_LBL_TC_PASSWORD` dipakai hanya oleh hook `after` untuk mengembalikan sesi ke akun default suite.
- Role yang diuji (bagian 3a):

  | No | Role | Pre-setup | Akun (Fixture) | Env password | TC |
  |---|---|---|---|---|---|
  | 1 | Gate-None | #39 | `Fixture.assetLabeling.akun.gateNone` | `FA_GATE_NONE_PASSWORD` | TC-FA-LBL-550 |
  | 2 | Gate-Value | #40 | `Fixture.assetLabeling.akun.gateValue` | `FA_GATE_VALUE_PASSWORD` | TC-FA-LBL-550 |
  | 3 | Gate-Accounting | #42 | `Fixture.assetLabeling.akun.gateAccounting` | `FA_GATE_ACCOUNTING_PASSWORD` | TC-FA-LBL-550 |

## Test Steps

### Blok Gate-None (Pre-setup #39): TC-FA-LBL-550

1. Klik chip `Gate Label` di kolom Label
2. Klik header kolom Actions (⋯) Drawer, klik `Setup Column...`
3. Verifikasi kolom `Warranty Expiry` tersedia di Setup Column
4. Centang `Warranty Expiry`, lalu klik `[Save]`
5. Verifikasi sel `Warranty Expiry` semua baris menampilkan `No access`, termasuk `Gate Item - 51` yang bernilai
6. Pemulihan: klik header kolom Actions (⋯) Drawer, klik `Setup Column...`, hapus centang `Warranty Expiry`, lalu klik `[Save]`
7. Tutup Drawer Tagged Asset

### Blok Gate-Value (Pre-setup #40): TC-FA-LBL-550

8. Ganti akun: Logout, login sebagai Gate-Value `Fixture.assetLabeling.akun.gateValue` (`Spectra.env.FA_GATE_VALUE_PASSWORD`), buka Fixed Asset > Settings > Asset Master > tab Labels
9. Klik chip `Gate Label` di kolom Label
10. Klik header kolom Actions (⋯) Drawer, klik `Setup Column...`
11. Verifikasi kolom `Warranty Expiry` tersedia di Setup Column
12. Centang `Warranty Expiry`, lalu klik `[Save]`
13. Verifikasi sel `Warranty Expiry` semua baris menampilkan `No access`, termasuk `Gate Item - 51` yang bernilai
14. Pemulihan: klik header kolom Actions (⋯) Drawer, klik `Setup Column...`, hapus centang `Warranty Expiry`, lalu klik `[Save]`
15. Tutup Drawer Tagged Asset

### Blok Gate-Accounting (Pre-setup #42): TC-FA-LBL-550

16. Ganti akun: Logout, login sebagai Gate-Accounting `Fixture.assetLabeling.akun.gateAccounting` (`Spectra.env.FA_GATE_ACCOUNTING_PASSWORD`), buka Fixed Asset > Settings > Asset Master > tab Labels
17. Klik chip `Gate Label` di kolom Label
18. Klik header kolom Actions (⋯) Drawer, klik `Setup Column...`
19. Verifikasi kolom `Warranty Expiry` tersedia di Setup Column
20. Centang `Warranty Expiry`, lalu klik `[Save]`
21. Verifikasi sel `Warranty Expiry` semua baris menampilkan `No access`, termasuk `Gate Item - 51` yang bernilai
22. Pemulihan: klik header kolom Actions (⋯) Drawer, klik `Setup Column...`, hapus centang `Warranty Expiry`, lalu klik `[Save]`
23. Tutup Drawer Tagged Asset

## Notes

- Sumber: `fixed-asset/settings-asset-labeling/TestCases/tc-settings-asset-labeling.md` section 4c (Drawer Tagged Asset). Subjudul `###` memetakan langkah ke TC granular.
- Susunan role (bagian 3a, `[KEPUTUSAN 2026-10-30]`): spec ditulis per blok role karena Ganti akun menuntut Step eksplisit (akun pertama login di hook `before`; langkah Ganti akun 8 dan 16). TC-FA-LBL-550 memakai Gate-None, Gate-Value, dan Gate-Accounting; langkah tiap role identik tetapi tiap blok ditulis eksplisit.
- Langkah penghubung (S-03): Pemulihan kolom `Warranty Expiry` dan tutup Drawer memulihkan keadaan awal blok berikutnya (S-09).
- Pembagian TC lintas spec: TC-FA-LBL-552 (ketersediaan kolom per role pada Setup Column) ada di spec 181; TC-FA-LBL-547 dan 554 (Gate-None, Gate-Purchase) di spec 122; TC-FA-LBL-561 di spec 123.
- Temuan untuk QA:
  - TC-FA-LBL-550 Expected b menyatakan `No access` untuk "semua baris" termasuk `Gate Item - 51` bernilai; spec memverifikasi seluruh baris dengan satu `Verifikasi` per role.
