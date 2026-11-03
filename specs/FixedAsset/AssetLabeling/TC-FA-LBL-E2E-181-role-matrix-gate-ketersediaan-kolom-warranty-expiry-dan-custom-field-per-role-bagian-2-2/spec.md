---
id: TC-FA-LBL-E2E-181-role-matrix-gate-ketersediaan-kolom-warranty-expiry-dan-custom-field-per-role-bagian-2-2
title: "Role Matrix Gate: Ketersediaan Kolom Warranty Expiry dan Custom Field per Role (bagian 2/2)"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-LBL-552
coverage:
  web: automated
---

# Role Matrix Gate: Ketersediaan Kolom Warranty Expiry dan Custom Field per Role (bagian 2/2)

## Prerequisites

- Mode: FE+BE. Backend nyata; tidak ada intercept.
- Akun aktor: Gate-None (`Company Gate`; capability Read Manage Asset Master Data; tanpa View asset value, Manage purchase, dan Manage accounting) (Pre-setup #39), `Fixture.assetLabeling.akun.gateNone`, `Spectra.env.FA_GATE_NONE_PASSWORD`. Login di hook `before` spec ini (menggantikan akun default suite); halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Asset Master > tab Labels). Hook `after` mengembalikan sesi ke akun default suite (Total Control Company Alpha, `Spectra.env.FA_LBL_TC_PASSWORD`).
- Akun aktor: Gate-Value (`Company Gate`; Read Manage Asset Master Data; Group Role View asset value pada `Gate HQ`) (Pre-setup #40), `Fixture.assetLabeling.akun.gateValue`, `Spectra.env.FA_GATE_VALUE_PASSWORD`. Dipakai pada langkah Ganti akun.
- Akun aktor: Gate-Purchase (`Company Gate`; Read Manage Asset Master Data; Group Role Manage purchase pada `Gate HQ`) (Pre-setup #41), `Fixture.assetLabeling.akun.gatePurchase`, `Spectra.env.FA_GATE_PURCHASE_PASSWORD`. Dipakai pada langkah Ganti akun.
- Akun aktor: Gate-Accounting (`Company Gate`; Read Manage Asset Master Data; Global Role Manage accounting) (Pre-setup #42), `Fixture.assetLabeling.akun.gateAccounting`, `Spectra.env.FA_GATE_ACCOUNTING_PASSWORD`. Dipakai pada langkah Ganti akun.
- Akun aktor: Gate-Full (`Company Gate`; Read Manage Asset Master Data; View asset value dan Manage purchase pada `Gate HQ`; Manage accounting) (Pre-setup #44), `Fixture.assetLabeling.akun.gateFull`, `Spectra.env.FA_GATE_FULL_PASSWORD`. Dipakai pada langkah Ganti akun.
- Hook suite: Guided Tooltip, pemulihan state global, dan pembukaan Settings > Asset Master > tab Labels mengikuti hook di `suite.md` dan tidak ditulis ulang di sini.
- Data Pre-setup `Company Gate` (#38), hanya dibaca dan dirujuk lewat `Fixture.assetLabeling.gate`: lisensi `FA-7` aktif; dua buku Asset Value tetap `Commercial` dan `Fiscal`; Asset Name `Gate Item`; Custom Field Active (Scope Asset Name `Gate Item`): `Gate Note` (General, Text), `Gate Region` (General, Text, Value Type Global), `Purchase PO` (Purchasing, Text), `Cost Center` (Accounting, Text); Custom Field Inactive `Retired Field` (General, Text); label `Gate Label` pada aset Active `Gate Item - 51`, `Gate Item - 52`, dan `Gate Item - 53`.
- Data Dinamis: tidak ada.
- Fixture `fixtures/asset-labeling.json` (belum ada, disediakan tim FE; hanya identitas data, tanpa rahasia). Kunci yang dipakai spec ini: `Fixture.assetLabeling.akun.gateNone`, `Fixture.assetLabeling.akun.gateValue`, `Fixture.assetLabeling.akun.gatePurchase`, `Fixture.assetLabeling.akun.gateAccounting`, `Fixture.assetLabeling.akun.gateFull` (email akun masing-masing) dan `Fixture.assetLabeling.gate` (data Pre-setup #38).
- State global: tidak ada yang diubah selain sesi login; spec hanya membuka dan menutup Setup Column tanpa menyimpan konfigurasi.
- Suite berjalan serial (`parallel: false`).
- Cleanup: spec tidak membuat data. Data Pre-setup hanya dibaca dan tidak diubah (Last Updated tidak berubah).
- Env var: `Spectra.env.FA_GATE_NONE_PASSWORD`, `Spectra.env.FA_GATE_VALUE_PASSWORD`, `Spectra.env.FA_GATE_PURCHASE_PASSWORD`, `Spectra.env.FA_GATE_ACCOUNTING_PASSWORD`, `Spectra.env.FA_GATE_FULL_PASSWORD`, `Spectra.env.FA_LBL_TC_PASSWORD` terdaftar di `executionConfig.environmentVariables` dan `.env.example`. `FA_LBL_TC_PASSWORD` dipakai hanya oleh hook `after` untuk mengembalikan sesi ke akun default suite.
- Role yang diuji (bagian 3a):

  | No | Role | Pre-setup | Akun (Fixture) | Env password | TC |
  |---|---|---|---|---|---|
  | 1 | Gate-None | #39 | `Fixture.assetLabeling.akun.gateNone` | `FA_GATE_NONE_PASSWORD` | TC-FA-LBL-552 |
  | 2 | Gate-Value | #40 | `Fixture.assetLabeling.akun.gateValue` | `FA_GATE_VALUE_PASSWORD` | TC-FA-LBL-552 |
  | 3 | Gate-Purchase | #41 | `Fixture.assetLabeling.akun.gatePurchase` | `FA_GATE_PURCHASE_PASSWORD` | TC-FA-LBL-552 |
  | 4 | Gate-Accounting | #42 | `Fixture.assetLabeling.akun.gateAccounting` | `FA_GATE_ACCOUNTING_PASSWORD` | TC-FA-LBL-552 |
  | 5 | Gate-Full | #44 | `Fixture.assetLabeling.akun.gateFull` | `FA_GATE_FULL_PASSWORD` | TC-FA-LBL-552 |

## Test Steps

### Blok Gate-None (Pre-setup #39): TC-FA-LBL-552

1. Klik chip `Gate Label` di kolom Label
2. Klik header kolom Actions (⋯) Drawer, klik `Setup Column...` dan baca daftar kolom
3. Verifikasi kolom `Asset Value (Commercial)`, `Asset Value (Fiscal)`, dan `Warranty Expiry` tersedia di Setup Column bagi Gate-None
4. Verifikasi kolom `Gate Note` dan `Gate Region` tersedia bagi Gate-None
5. Verifikasi kolom `Purchase PO` dan `Cost Center` tidak tersedia bagi Gate-None
6. Verifikasi kolom `Retired Field` (Custom Field Inactive) tidak tersedia bagi Gate-None
7. Tutup Setup Column dengan `[✕]`
8. Tutup Drawer Tagged Asset

### Blok Gate-Value (Pre-setup #40): TC-FA-LBL-552

9. Ganti akun: Logout, login sebagai Gate-Value `Fixture.assetLabeling.akun.gateValue` (`Spectra.env.FA_GATE_VALUE_PASSWORD`), buka Fixed Asset > Settings > Asset Master > tab Labels
10. Klik chip `Gate Label` di kolom Label
11. Klik header kolom Actions (⋯) Drawer, klik `Setup Column...` dan baca daftar kolom
12. Verifikasi kolom `Asset Value (Commercial)`, `Asset Value (Fiscal)`, dan `Warranty Expiry` tersedia di Setup Column bagi Gate-Value
13. Verifikasi kolom `Gate Note` dan `Gate Region` tersedia bagi Gate-Value
14. Verifikasi kolom `Purchase PO` dan `Cost Center` tidak tersedia bagi Gate-Value
15. Verifikasi kolom `Retired Field` (Custom Field Inactive) tidak tersedia bagi Gate-Value
16. Tutup Setup Column dengan `[✕]`
17. Tutup Drawer Tagged Asset

### Blok Gate-Purchase (Pre-setup #41): TC-FA-LBL-552

18. Ganti akun: Logout, login sebagai Gate-Purchase `Fixture.assetLabeling.akun.gatePurchase` (`Spectra.env.FA_GATE_PURCHASE_PASSWORD`), buka Fixed Asset > Settings > Asset Master > tab Labels
19. Klik chip `Gate Label` di kolom Label
20. Klik header kolom Actions (⋯) Drawer, klik `Setup Column...` dan baca daftar kolom
21. Verifikasi kolom `Asset Value (Commercial)`, `Asset Value (Fiscal)`, dan `Warranty Expiry` tersedia di Setup Column bagi Gate-Purchase
22. Verifikasi kolom `Gate Note` dan `Gate Region` tersedia bagi Gate-Purchase
23. Verifikasi kolom `Purchase PO` tersedia bagi Gate-Purchase
24. Verifikasi kolom `Cost Center` tidak tersedia bagi Gate-Purchase
25. Verifikasi kolom `Retired Field` (Custom Field Inactive) tidak tersedia bagi Gate-Purchase
26. Tutup Setup Column dengan `[✕]`
27. Tutup Drawer Tagged Asset

### Blok Gate-Accounting (Pre-setup #42): TC-FA-LBL-552

28. Ganti akun: Logout, login sebagai Gate-Accounting `Fixture.assetLabeling.akun.gateAccounting` (`Spectra.env.FA_GATE_ACCOUNTING_PASSWORD`), buka Fixed Asset > Settings > Asset Master > tab Labels
29. Klik chip `Gate Label` di kolom Label
30. Klik header kolom Actions (⋯) Drawer, klik `Setup Column...` dan baca daftar kolom
31. Verifikasi kolom `Asset Value (Commercial)`, `Asset Value (Fiscal)`, dan `Warranty Expiry` tersedia di Setup Column bagi Gate-Accounting
32. Verifikasi kolom `Gate Note` dan `Gate Region` tersedia bagi Gate-Accounting
33. Verifikasi kolom `Cost Center` tersedia bagi Gate-Accounting
34. Verifikasi kolom `Purchase PO` tidak tersedia bagi Gate-Accounting
35. Verifikasi kolom `Retired Field` (Custom Field Inactive) tidak tersedia bagi Gate-Accounting
36. Tutup Setup Column dengan `[✕]`
37. Tutup Drawer Tagged Asset

### Blok Gate-Full (Pre-setup #44): TC-FA-LBL-552

38. Ganti akun: Logout, login sebagai Gate-Full `Fixture.assetLabeling.akun.gateFull` (`Spectra.env.FA_GATE_FULL_PASSWORD`), buka Fixed Asset > Settings > Asset Master > tab Labels
39. Klik chip `Gate Label` di kolom Label
40. Klik header kolom Actions (⋯) Drawer, klik `Setup Column...` dan baca daftar kolom
41. Verifikasi kolom `Asset Value (Commercial)`, `Asset Value (Fiscal)`, dan `Warranty Expiry` tersedia di Setup Column bagi Gate-Full
42. Verifikasi kolom `Gate Note` dan `Gate Region` tersedia bagi Gate-Full
43. Verifikasi kolom `Purchase PO` dan `Cost Center` tersedia bagi Gate-Full
44. Verifikasi kolom `Retired Field` (Custom Field Inactive) tidak tersedia bagi Gate-Full
45. Tutup Setup Column dengan `[✕]`
46. Tutup Drawer Tagged Asset

## Notes

- Sumber: `fixed-asset/settings-asset-labeling/TestCases/tc-settings-asset-labeling.md` section 4c (Drawer Tagged Asset). Subjudul `###` memetakan langkah ke TC granular.
- Susunan role (bagian 3a, `[KEPUTUSAN 2026-10-30]`): spec ditulis per blok role karena Ganti akun menuntut Step eksplisit (akun pertama login di hook `before`; langkah Ganti akun 9, 18, 28, dan 38). TC-FA-LBL-552 memakai kelima role; langkah tiap role identik tetapi Expected-nya berbeda per role sehingga tiap blok ditulis eksplisit.
- Langkah penghubung (S-03): `Tutup Setup Column dengan [✕]` (TC-FA-LBL-552 Langkah Uji 3) dan tutup Drawer memulihkan keadaan awal blok berikutnya (S-09).
- Pembagian TC lintas spec: TC-FA-LBL-550 (gerbang Warranty Expiry per role) ada di spec 172; TC-FA-LBL-547 dan 554 (Gate-None, Gate-Purchase) di spec 122; TC-FA-LBL-561 di spec 123.
- Ukuran spec (46 langkah, di atas smell 35 langkah): satu TC (TC-FA-LBL-552) dengan lima role pada Company Gate (Pre-setup #38) yang sama; TC tidak dipotong lintas spec, tiap blok role berdiri sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna, dan langkah membengkak karena lima role dan tiap klausa Expected menjadi satu `Verifikasi` (S-01).
- Temuan untuk QA:
  - TC-FA-LBL-552 Expected c sampai f menyatakan ketersediaan `Purchase PO` dan `Cost Center` per role; spec menulis satu `Verifikasi` per kolom per role dan memakai anchor positif ketersediaan kolom lain pada Setup Column yang sama (bagian 8b butir 2).
