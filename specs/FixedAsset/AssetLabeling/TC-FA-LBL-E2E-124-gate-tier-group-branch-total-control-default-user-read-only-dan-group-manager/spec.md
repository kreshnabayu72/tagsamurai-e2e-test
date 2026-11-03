---
id: TC-FA-LBL-E2E-124-gate-tier-group-branch-total-control-default-user-read-only-dan-group-manager
title: "Gate Tier: Group Branch, Total Control, Default User, Read Only, dan Group Manager"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-LBL-548
  - TC-FA-LBL-568
  - TC-FA-LBL-569
coverage:
  web: automated
---

# Gate Tier: Group Branch, Total Control, Default User, Read Only, dan Group Manager

## Prerequisites

- Mode: FE+BE. Backend nyata; tidak ada intercept.
- Akun aktor: Gate-Branch (`Company Gate`; Read Manage Asset Master Data; Group Role View asset value dan Manage purchase pada `Gate Branch A` saja) (Pre-setup #43), `Fixture.assetLabeling.akun.gateBranch`, `Spectra.env.FA_GATE_BRANCH_PASSWORD`. Login di hook `before` spec ini (menggantikan akun default suite); halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Asset Master > tab Labels). Hook `after` mengembalikan sesi ke akun default suite (Total Control Company Alpha, `Spectra.env.FA_LBL_TC_PASSWORD`).
- Akun aktor: Gate-TotalControl (`Company Gate`; Total Control) (Pre-setup #45), `Fixture.assetLabeling.akun.gateTotalControl`, `Spectra.env.FA_GATE_TOTALCONTROL_PASSWORD`. Dipakai pada langkah Ganti akun.
- Akun aktor: Gate-DefaultUser (`Company Gate`; Default User) (Pre-setup #46), `Fixture.assetLabeling.akun.gateDefaultUser`, `Spectra.env.FA_GATE_DEFAULTUSER_PASSWORD`. Dipakai pada langkah Ganti akun.
- Akun aktor: Gate-ReadOnly (`Company Gate`; Read Only) (Pre-setup #47), `Fixture.assetLabeling.akun.gateReadOnly`, `Spectra.env.FA_GATE_READONLY_PASSWORD`. Dipakai pada langkah Ganti akun.
- Akun aktor: Gate-GroupManager (`Company Gate`; tier Group Manager pada `Gate HQ`; capability Read Manage Asset Master Data) (Pre-setup #48), `Fixture.assetLabeling.akun.gateGroupManager`, `Spectra.env.FA_GATE_GROUPMANAGER_PASSWORD`. Dipakai pada langkah Ganti akun.
- Hook suite: Guided Tooltip, pemulihan state global, dan pembukaan Settings > Asset Master > tab Labels mengikuti hook di `suite.md` dan tidak ditulis ulang di sini.
- Data Pre-setup `Company Gate` (#38), hanya dibaca dan dirujuk lewat `Fixture.assetLabeling.gate`: General Settings currency `Rp` (ribuan titik, desimal koma, 2 desimal) dan lisensi `FA-7` aktif; Group `Gate HQ` dengan anak `Gate Branch A`, dan Group `Gate Other` (terpisah); dua buku Asset Value tetap `Commercial` dan `Fiscal` (seluruh nilai Asset Value yang diasersi adalah nilai buku `Commercial`); Asset Name `Gate Item` dan `Gate Plain`; Custom Field Active (Scope Asset Name `Gate Item`): `Gate Note` (General, Text), `Gate Region` (General, Text, Value Type Global, nilai `APAC`), `Purchase PO` (Purchasing, Text), `Cost Center` (Accounting, Text); Custom Field Inactive `Retired Field` (General, Text); label `Gate Label` pada aset Active `Gate Item - 51` (Group `Gate HQ`; Asset Value 1500000; Warranty Expiry 30 Jun 2027; `Gate Note` `Note A`; `Purchase PO` `PO-001`; `Cost Center` `CC-10`), `Gate Item - 52` (Group `Gate HQ > Gate Branch A`; Asset Value 0; Warranty Expiry belum ada; `Purchase PO` dan `Cost Center` belum diisi), `Gate Item - 53` (Group `Gate Other`; Asset Value 2500000; Warranty Expiry 15 Jan 2028; `Purchase PO` `PO-003`; `Cost Center` `CC-30`), dan `Gate Plain - 54` (Group `Gate HQ`; Asset Value dan Warranty Expiry belum ada; di luar Scope seluruh Custom Field); label `Gate Scope` pada `Gate Plain - 55` (Active; Group `Gate Other`; Asset Value 700000; Warranty Expiry 01 Mar 2027; di luar Scope seluruh Custom Field).
- Data Dinamis: tidak ada.
- Fixture `fixtures/asset-labeling.json` (belum ada, disediakan tim FE; hanya identitas data, tanpa rahasia). Kunci yang dipakai spec ini: `Fixture.assetLabeling.akun.gateBranch`, `Fixture.assetLabeling.akun.gateTotalControl`, `Fixture.assetLabeling.akun.gateDefaultUser`, `Fixture.assetLabeling.akun.gateReadOnly`, `Fixture.assetLabeling.akun.gateGroupManager` (email akun masing-masing) dan `Fixture.assetLabeling.gate` (data Pre-setup #38).
- Kemampuan teknis (disediakan tim FE): hapus preferensi kolom Setup Column Drawer di browser (bagian 4).
- State global: konfigurasi kolom Setup Column Drawer Tagged Asset (preferensi browser) diubah dan dipulihkan oleh langkah spec; hook `after` spec ini menghapus preferensi kolom di browser sebagai cadangan, bukan `[Reset to Default]` (bagian 4). Kemampuan menghapus preferensi itu disediakan tim FE. Tidak ada state global lain yang diubah.
- Suite berjalan serial (`parallel: false`).
- Cleanup: spec tidak membuat data. Data Pre-setup hanya dibaca dan tidak diubah (Last Updated tidak berubah).
- Env var: `Spectra.env.FA_GATE_BRANCH_PASSWORD`, `Spectra.env.FA_GATE_TOTALCONTROL_PASSWORD`, `Spectra.env.FA_GATE_DEFAULTUSER_PASSWORD`, `Spectra.env.FA_GATE_READONLY_PASSWORD`, `Spectra.env.FA_GATE_GROUPMANAGER_PASSWORD`, `Spectra.env.FA_LBL_TC_PASSWORD` terdaftar di `executionConfig.environmentVariables` dan `.env.example`. `FA_LBL_TC_PASSWORD` dipakai hanya oleh hook `after` untuk mengembalikan sesi ke akun default suite.
- Role yang diuji (bagian 3a), parameter langkah ulang TC-FA-LBL-568:

  | No | Role | Pre-setup | Akun (Fixture) | Env password |
  |---|---|---|---|---|
  | 1 | Gate-TotalControl | #45 | `Fixture.assetLabeling.akun.gateTotalControl` | `FA_GATE_TOTALCONTROL_PASSWORD` |
  | 2 | Gate-DefaultUser | #46 | `Fixture.assetLabeling.akun.gateDefaultUser` | `FA_GATE_DEFAULTUSER_PASSWORD` |
  | 3 | Gate-ReadOnly | #47 | `Fixture.assetLabeling.akun.gateReadOnly` | `FA_GATE_READONLY_PASSWORD` |

## Test Steps

### TC-FA-LBL-548: Gerbang hak sempit pada Gate Branch A: hak group anak tidak naik ke group induk

1. Klik chip `Gate Label` di kolom Label
2. Klik header kolom Actions (⋯) Drawer, klik `Setup Column...`, centang `Asset Value (Commercial)` dan `Warranty Expiry`, lalu klik `[Save]`
3. Verifikasi `Asset Value (Commercial)`: `Gate Item - 52` menampilkan `Rp 0,00`
4. Verifikasi `Asset Value (Commercial)`: `Gate Item - 51`, `Gate Item - 53`, dan `Gate Plain - 54` menampilkan `No access`
5. Verifikasi `Warranty Expiry`: `Gate Item - 52` menampilkan `—` (berhak, belum ada nilai)
6. Verifikasi `Warranty Expiry`: `Gate Item - 51`, `Gate Item - 53`, dan `Gate Plain - 54` menampilkan `No access`
7. Pemulihan: klik header kolom Actions (⋯) Drawer, klik `Setup Column...`, hapus centang `Asset Value (Commercial)` dan `Warranty Expiry`, lalu klik `[Save]`
8. Tutup Drawer Tagged Asset

### TC-FA-LBL-568: Gerbang kolom bergerbang untuk tier Total Control, Default User, dan Read Only: seluruh sel bernilai client-wide

9. Untuk setiap baris tabel 'Role yang diuji' (berurutan dari baris pertama; langkah 9 sampai 20): Ganti akun: Logout, login sebagai role pada baris itu (`Fixture.assetLabeling.akun.<kunci>`, `Spectra.env.<NAMA>` pada tabel), buka Fixed Asset > Settings > Asset Master > tab Labels
10. Klik chip `Gate Label` di kolom Label
11. Klik header kolom Actions (⋯) Drawer, klik `Setup Column...`
12. Verifikasi kolom `Purchase PO` dan `Cost Center` tersedia di Setup Column bagi role itu
13. Centang `Asset Value (Commercial)`, `Warranty Expiry`, `Purchase PO`, dan `Cost Center`, lalu klik `[Save]`
14. Verifikasi `Asset Value (Commercial)`: `Gate Item - 51` `Rp 1.500.000,00`, `Gate Item - 52` `Rp 0,00`, `Gate Item - 53` `Rp 2.500.000,00` (group `Gate Other`), `Gate Plain - 54` `—`
15. Verifikasi `Warranty Expiry`: `30 Jun 2027`, `—`, `15 Jan 2028`, `—` berurutan pada keempat baris
16. Verifikasi `Purchase PO`: `PO-001`, `—`, `PO-003`, `—` berurutan pada keempat baris
17. Verifikasi `Cost Center`: `CC-10`, `—`, `CC-30`, `—` berurutan pada keempat baris
18. Verifikasi tidak ada sel `No access` pada keempat kolom
19. Pemulihan: klik header kolom Actions (⋯) Drawer, klik `Setup Column...`, hapus centang `Asset Value (Commercial)`, `Warranty Expiry`, `Purchase PO`, dan `Cost Center`, lalu klik `[Save]`
20. Tutup Drawer Tagged Asset

### TC-FA-LBL-569: Gerbang kolom bergerbang untuk tier Group Manager: hak pada group yang di-assign beserta descendant, tanpa Custom Field Accounting

21. Ganti akun: Logout, login sebagai Gate-GroupManager `Fixture.assetLabeling.akun.gateGroupManager` (`Spectra.env.FA_GATE_GROUPMANAGER_PASSWORD`), buka Fixed Asset > Settings > Asset Master > tab Labels
22. Klik chip `Gate Label` di kolom Label
23. Klik header kolom Actions (⋯) Drawer, klik `Setup Column...` dan baca daftar kolom
24. Verifikasi kolom `Purchase PO` tersedia
25. Verifikasi kolom `Cost Center` tidak tersedia
26. Tutup Setup Column dengan `[✕]`
27. Klik header kolom Actions (⋯) Drawer, klik `Setup Column...`, centang `Asset Value (Commercial)`, `Warranty Expiry`, dan `Purchase PO`, lalu klik `[Save]`
28. Verifikasi `Asset Value (Commercial)`: `Gate Item - 51` `Rp 1.500.000,00`, `Gate Item - 52` `Rp 0,00`, `Gate Item - 53` `No access`, `Gate Plain - 54` `—`
29. Verifikasi `Warranty Expiry`: `Gate Item - 51` `30 Jun 2027`, `Gate Item - 52` `—`, `Gate Item - 53` `No access`, `Gate Plain - 54` `—`
30. Verifikasi `Purchase PO`: `Gate Item - 51` `PO-001`, `Gate Item - 52` `—`, `Gate Item - 53` `No access`, `Gate Plain - 54` `—`
31. Pemulihan: klik header kolom Actions (⋯) Drawer, klik `Setup Column...`, hapus centang `Asset Value (Commercial)`, `Warranty Expiry`, dan `Purchase PO`, lalu klik `[Save]`
32. Tutup Drawer Tagged Asset

## Notes

- Sumber: `fixed-asset/settings-asset-labeling/TestCases/tc-settings-asset-labeling.md` section 4c (Drawer Tagged Asset). Subjudul `###` memetakan langkah ke TC granular.
- Susunan role (bagian 3a, `[KEPUTUSAN 2026-10-30]`): spec ditulis per blok role karena Ganti akun menuntut Step eksplisit; akun pertama (Gate-Branch, TC-FA-LBL-548) login di hook `before`. Langkah TC-FA-LBL-568 identik untuk tiga tier sehingga memakai langkah ulang atas tabel 'Role yang diuji' (langkah 9 sampai 20, tiga iterasi); Ganti akun menjadi langkah pertama iterasi.
- Langkah ulang (bagian 8b butir 7): jumlah langkah 32 dihitung nominal; ekspansi 56 langkah (blok TC-FA-LBL-568 dua belas langkah dikali tiga iterasi).
- Penyimpangan urutan (bagian 3): TC-FA-LBL-548 (Gate-Branch) dulu, lalu TC-FA-LBL-568 (tiga tier client-wide), lalu TC-FA-LBL-569 (Group Manager) mengikuti nomor TC.
- Langkah penghubung (S-03): Pemulihan kolom dan tutup Drawer sesudah tiap blok memulihkan keadaan awal (S-09).
- Ukuran spec (di atas smell 35 langkah dengan ekspansi): ketiga TC satu kelas (role matrix tier, gerbang kolom Drawer) pada Company Gate (Pre-setup #38) yang sama dan tiap blok berdiri sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna; langkah membengkak karena ekspansi tiga tier dan tiap klausa Expected menjadi satu `Verifikasi` (S-01).
- Temuan untuk QA:
  - TC-FA-LBL-568 Expected b sampai e menyatakan nilai empat baris dalam satu butir per kolom; spec menulis satu `Verifikasi` per kolom dengan daftar nilai keempat baris utuh.
  - TC-FA-LBL-568 Expected a ("kolom `Purchase PO` dan `Cost Center` tersedia bagi ketiga tier") diverifikasi di Setup Column pada tiap iterasi sebelum kolom dicentang.
