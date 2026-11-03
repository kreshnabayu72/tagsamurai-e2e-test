---
id: TC-FA-LBL-E2E-122-gate-none-pemegang-view-tagged-assets-tanpa-hak-nilai-bagian-1-2
title: "Gate-None: Pemegang View Tagged Assets tanpa Hak Nilai (bagian 1/2)"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-FA-LBL-547
  - TC-FA-LBL-554
coverage:
  web: automated
---

# Gate-None: Pemegang View Tagged Assets tanpa Hak Nilai (bagian 1/2)

## Prerequisites

- Mode: FE+BE. Backend nyata; tidak ada intercept.
- Akun aktor: Gate-None (`Company Gate`; capability Read Manage Asset Master Data; tanpa View asset value, Manage purchase, dan Manage accounting) (Pre-setup #39), `Fixture.assetLabeling.akun.gateNone`, `Spectra.env.FA_GATE_NONE_PASSWORD`. Login di hook `before` spec ini (menggantikan akun default suite); halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Asset Master > tab Labels). Hook `after` mengembalikan sesi ke akun default suite (Total Control Company Alpha, `Spectra.env.FA_LBL_TC_PASSWORD`).
- Akun aktor: Gate-Purchase (`Company Gate`; Read Manage Asset Master Data; Group Role Manage purchase pada `Gate HQ`) (Pre-setup #41), `Fixture.assetLabeling.akun.gatePurchase`, `Spectra.env.FA_GATE_PURCHASE_PASSWORD`. Dipakai pada langkah Ganti akun.
- Hook suite: Guided Tooltip, pemulihan state global, dan pembukaan Settings > Asset Master > tab Labels mengikuti hook di `suite.md` dan tidak ditulis ulang di sini.
- Data Pre-setup `Company Gate` (#38), hanya dibaca dan dirujuk lewat `Fixture.assetLabeling.gate`: General Settings currency `Rp` (ribuan titik, desimal koma, 2 desimal) dan lisensi `FA-7` aktif; Group `Gate HQ` dengan anak `Gate Branch A`, dan Group `Gate Other` (terpisah); dua buku Asset Value tetap `Commercial` dan `Fiscal` (seluruh nilai Asset Value yang diasersi adalah nilai buku `Commercial`); Asset Name `Gate Item` dan `Gate Plain`; Custom Field Active (Scope Asset Name `Gate Item`): `Gate Note` (General, Text), `Gate Region` (General, Text, Value Type Global, nilai `APAC`), `Purchase PO` (Purchasing, Text), `Cost Center` (Accounting, Text); Custom Field Inactive `Retired Field` (General, Text); label `Gate Label` pada aset Active `Gate Item - 51` (Group `Gate HQ`; Asset Value 1500000; Warranty Expiry 30 Jun 2027; `Gate Note` `Note A`; `Purchase PO` `PO-001`; `Cost Center` `CC-10`), `Gate Item - 52` (Group `Gate HQ > Gate Branch A`; Asset Value 0; Warranty Expiry belum ada; `Purchase PO` dan `Cost Center` belum diisi), `Gate Item - 53` (Group `Gate Other`; Asset Value 2500000; Warranty Expiry 15 Jan 2028; `Purchase PO` `PO-003`; `Cost Center` `CC-30`), dan `Gate Plain - 54` (Group `Gate HQ`; Asset Value dan Warranty Expiry belum ada; di luar Scope seluruh Custom Field); label `Gate Scope` pada `Gate Plain - 55` (Active; Group `Gate Other`; Asset Value 700000; Warranty Expiry 01 Mar 2027; di luar Scope seluruh Custom Field).
- Data Dinamis: tidak ada.
- Fixture `fixtures/asset-labeling.json` (belum ada, disediakan tim FE; hanya identitas data, tanpa rahasia). Kunci yang dipakai spec ini: `Fixture.assetLabeling.akun.gateNone`, `Fixture.assetLabeling.akun.gatePurchase` (email akun masing-masing) dan `Fixture.assetLabeling.gate` (data Pre-setup #38).
- Kemampuan teknis (disediakan tim FE): hapus preferensi kolom Setup Column Drawer di browser (bagian 4).
- State global: konfigurasi kolom Setup Column Drawer Tagged Asset (preferensi browser) diubah dan dipulihkan oleh langkah spec; hook `after` spec ini menghapus preferensi kolom di browser sebagai cadangan, bukan `[Reset to Default]` (bagian 4). Kemampuan menghapus preferensi itu disediakan tim FE. Tidak ada state global lain yang diubah.
- Suite berjalan serial (`parallel: false`).
- Cleanup: spec tidak membuat data. Data Pre-setup hanya dibaca dan tidak diubah (Last Updated tidak berubah).
- Env var: `Spectra.env.FA_GATE_NONE_PASSWORD`, `Spectra.env.FA_GATE_PURCHASE_PASSWORD`, `Spectra.env.FA_LBL_TC_PASSWORD` terdaftar di `executionConfig.environmentVariables` dan `.env.example`. `FA_LBL_TC_PASSWORD` dipakai hanya oleh hook `after` untuk mengembalikan sesi ke akun default suite.
- Role yang diuji (bagian 3a):

  | No | Role | Pre-setup | Akun (Fixture) | Env password | TC |
  |---|---|---|---|---|---|
  | 1 | Gate-None | #39 | `Fixture.assetLabeling.akun.gateNone` | `FA_GATE_NONE_PASSWORD` | TC-FA-LBL-554, 547 |
  | 2 | Gate-Purchase | #41 | `Fixture.assetLabeling.akun.gatePurchase` | `FA_GATE_PURCHASE_PASSWORD` | TC-FA-LBL-547 |

## Test Steps

### Blok Gate-None (Pre-setup #39): TC-FA-LBL-554 dan TC-FA-LBL-547

1. Klik chip `Gate Label` di kolom Label
2. Klik header kolom Actions (⋯) Drawer, klik `Setup Column...`, centang `Gate Note` dan `Gate Region`, lalu klik `[Save]`
3. Verifikasi `Gate Item - 51`: `Gate Note` `Note A`, `Gate Region` `APAC`
4. Verifikasi `Gate Item - 52` dan `Gate Item - 53`: `Gate Note` `—` (nilai belum diisi), `Gate Region` `APAC` (nilai Global sama seperti nilai per aset)
5. Verifikasi `Gate Plain - 54` (Asset Name di luar Scope kedua field): `Gate Note` dan `Gate Region` `—`
6. Klik header kolom Actions (⋯) Drawer, klik `Setup Column...`
7. Verifikasi kolom `Asset Value (Commercial)` tersedia di Setup Column (Curated, tidak tercentang) bagi Gate-None
8. Centang `Asset Value (Commercial)`, lalu klik `[Save]`
9. Verifikasi keempat baris tampil dengan sel `Name`, `Group`, dan `Status` terisi
10. Verifikasi sel `Asset Value (Commercial)` semua baris menampilkan `No access`, termasuk `Gate Plain - 54` (tidak berhak, bukan `—`)
11. Pemulihan: klik header kolom Actions (⋯) Drawer, klik `Setup Column...`, hapus centang `Gate Note`, `Gate Region`, dan `Asset Value (Commercial)`, lalu klik `[Save]`
12. Tutup Drawer Tagged Asset

### Blok Gate-Purchase (Pre-setup #41): TC-FA-LBL-547 (aktor kedua)

13. Ganti akun: Logout, login sebagai Gate-Purchase `Fixture.assetLabeling.akun.gatePurchase` (`Spectra.env.FA_GATE_PURCHASE_PASSWORD`), buka Fixed Asset > Settings > Asset Master > tab Labels
14. Klik chip `Gate Label` di kolom Label
15. Klik header kolom Actions (⋯) Drawer, klik `Setup Column...`
16. Verifikasi kolom `Asset Value (Commercial)` tersedia di Setup Column (Curated, tidak tercentang) bagi Gate-Purchase
17. Centang `Asset Value (Commercial)`, lalu klik `[Save]`
18. Verifikasi keempat baris tampil dengan sel `Name`, `Group`, dan `Status` terisi
19. Verifikasi sel `Asset Value (Commercial)` semua baris menampilkan `No access`, termasuk `Gate Plain - 54` (tidak berhak, bukan `—`; Manage purchase tidak memberi hak atas Asset Value (Commercial))
20. Pemulihan: klik header kolom Actions (⋯) Drawer, klik `Setup Column...`, hapus centang `Asset Value (Commercial)`, lalu klik `[Save]`
21. Tutup Drawer Tagged Asset

## Notes

- Sumber: `fixed-asset/settings-asset-labeling/TestCases/tc-settings-asset-labeling.md` section 4c (Drawer Tagged Asset). Subjudul `###` memetakan langkah ke TC granular.
- Susunan role (bagian 3a, `[KEPUTUSAN 2026-10-30]`): spec ditulis per blok role karena Ganti akun menuntut Step eksplisit (akun pertama login di hook `before`). TC-FA-LBL-554 hanya memakai Gate-None; TC-FA-LBL-547 memakai Gate-None dan Gate-Purchase (aktor kedua) sehingga ditulis pada dua blok sesuai Langkah Uji 4 TC.
- Penyimpangan urutan (bagian 3): TC-FA-LBL-554 ditaruh sebelum TC-FA-LBL-547 supaya seluruh langkah Gate-None berurutan sebelum Ganti akun; Setup Column TC-FA-LBL-554 (`Gate Note`, `Gate Region`) dipulihkan bersama kolom `Asset Value (Commercial)` pada akhir blok Gate-None.
- Langkah penghubung (S-03): Pemulihan kolom dan tutup Drawer memulihkan keadaan awal (S-09).
- Pembagian TC lintas spec: TC-FA-LBL-550 (Gate-None dengan role lain) di spec 172 dan TC-FA-LBL-552 di spec 181; TC-FA-LBL-561 (baris client-wide Gate-None) di spec 123. Ketiganya memakai Company Gate (Pre-setup #38).
- Temuan untuk QA:
  - TC-FA-LBL-547 Expected d ("Manage purchase tidak memberi hak atas Asset Value (Commercial)") adalah kesimpulan dari Expected c untuk Gate-Purchase dan tidak teramati terpisah; spec menuliskannya dalam satu `Verifikasi` bersama Expected c (S-03).
  - TC-FA-LBL-547 Expected a ("tersedia di Setup Column bagi kedua aktor") dan Expected b ("keempat baris tampil") diverifikasi untuk tiap aktor pada bloknya masing-masing.
