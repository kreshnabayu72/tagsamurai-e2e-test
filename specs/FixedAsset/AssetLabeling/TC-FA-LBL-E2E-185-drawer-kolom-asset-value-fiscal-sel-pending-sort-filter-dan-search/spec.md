---
id: TC-FA-LBL-E2E-185-drawer-kolom-asset-value-fiscal-sel-pending-sort-filter-dan-search
title: "Drawer Tagged Asset: Kolom Asset Value (Fiscal) dengan Sel Pending, Sort Tepat Sebelum No access, Tidak Cocok Filter dan Search"
priority: High
caseType: Boundary
status: draft
sourceTc:
  - TC-FA-LBL-597
coverage:
  web: automated
---

# Drawer Tagged Asset: Kolom Asset Value (Fiscal) dengan Sel Pending, Sort Tepat Sebelum No access, Tidak Cocok Filter dan Search

## Prerequisites

- Mode: FE+BE. Backend nyata; tidak ada intercept.
- Akun aktor: Gate-Value (`Company Gate`; Read Manage Asset Master Data; Group Role View asset value pada `Gate HQ`) (Pre-setup #40), `Fixture.assetLabeling.akun.gateValue`, `Spectra.env.FA_GATE_VALUE_PASSWORD`. Login di hook `before` spec ini (menggantikan akun default suite); halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Asset Master > tab Labels). Hook `after` mengembalikan sesi ke akun default suite (Total Control Company Alpha, `Spectra.env.FA_LBL_TC_PASSWORD`).
- Hook suite: Guided Tooltip, pemulihan state global, dan pembukaan Settings > Asset Master > tab Labels mengikuti hook di `suite.md` dan tidak ditulis ulang di sini.
- Data Dinamis: tidak ada.
- Fixture `fixtures/asset-labeling.json` (belum ada, disediakan tim FE; hanya identitas data, tanpa rahasia). Kunci yang dipakai spec ini: `Fixture.assetLabeling.akun.gateValue` (email akun) dan `Fixture.assetLabeling.gate` (data Pre-setup #38).
- Data Pre-setup `Company Gate` (#38), hanya dibaca: General Settings currency `Rp` (ribuan titik, desimal koma, 2 desimal) dan lisensi `FA-7` aktif; Group `Gate HQ` dengan anak `Gate Branch A`, dan Group `Gate Other` (terpisah); label `Gate Label` pada aset Active `Gate Item - 51` (Group `Gate HQ`), `Gate Item - 52` (Group `Gate HQ > Gate Branch A`), `Gate Item - 53` (Group `Gate Other`; di luar hak Gate-Value sehingga `No access`), dan `Gate Plain - 54` (Group `Gate HQ`; Asset Value `Pending` karena belum ada Purchase Cost, tooltip `Purchase cost has not been set.`).
- Kemampuan teknis (disediakan tim FE): hapus preferensi kolom Setup Column Drawer di browser (bagian 4).
- State global: konfigurasi kolom Setup Column Drawer Tagged Asset (preferensi browser) diubah dan dipulihkan oleh langkah spec; hook `after` spec ini menghapus preferensi kolom di browser sebagai cadangan, bukan `[Reset to Default]` (bagian 4). Tidak ada state global lain yang diubah.
- Suite berjalan serial (`parallel: false`).
- Cleanup: spec tidak membuat data. Data Pre-setup hanya dibaca dan tidak diubah.
- Env var: `Spectra.env.FA_GATE_VALUE_PASSWORD` dan `Spectra.env.FA_LBL_TC_PASSWORD` terdaftar di `executionConfig.environmentVariables` dan `.env.example`. `FA_LBL_TC_PASSWORD` dipakai hanya oleh hook `after`.

## Test Steps

### TC-FA-LBL-597: Kolom Asset Value (Fiscal) dengan sel Pending: Sort tepat sebelum No access, tidak cocok Filter dan Search

1. Klik chip `Gate Label` di kolom Label
2. Klik header kolom Actions (⋯) Drawer, klik `Setup Column...`, centang `Asset Value (Fiscal)`, lalu klik `[Save]`
3. Klik header kolom `Asset Value (Fiscal)` satu kali
4. Verifikasi klik 1 (Ascending): `Gate Plain - 54` (`Pending`) tepat sebelum `Gate Item - 53` (`No access`) yang paling akhir
5. Klik header kolom `Asset Value (Fiscal)` kedua kali
6. Verifikasi klik 2 (Descending): `Gate Plain - 54` (`Pending`) tetap tepat sebelum `Gate Item - 53` (`No access`) yang tetap paling akhir
7. Klik icon Filter di toolbar Drawer, isi `Asset Value (Fiscal)` Min `0` dan Max `99.999.999`, lalu klik `[Apply]`
8. Verifikasi `Gate Plain - 54` (`Pending`) dan `Gate Item - 53` (`No access`) tidak tampil
9. Buka panel Filter lagi, klik `[Clear Field]`, lalu tutup panel Filter
10. Klik icon Search di toolbar Drawer, ketik `Pending`, tekan Enter
11. Verifikasi empty state `No results found` (sel `Pending` tidak dicocokkan teksnya)
12. Klik `(←)` pada kotak Search
13. Hover sel `Pending` `Gate Plain - 54` pada kolom `Asset Value (Fiscal)`
14. Verifikasi tooltip `Purchase cost has not been set.`
15. Pemulihan: klik header kolom Actions (⋯) Drawer, klik `Setup Column...`, hapus centang `Asset Value (Fiscal)`, lalu klik `[Save]`
16. Tutup Drawer Tagged Asset

## Notes

- Sumber: `fixed-asset/settings-asset-labeling/TestCases/tc-settings-asset-labeling.md` section 4c (Drawer Tagged Asset). Subjudul `###` memetakan langkah ke TC granular.
- Langkah penghubung (S-03): langkah 9 (membersihkan Filter dan menutup panel Filter, panel tetap terbuka sesudah `[Apply]`), langkah 12 (`(←)` pada kotak Search), langkah 15 dan 16 (pemulihan kolom dan tutup Drawer).
- Temuan untuk QA:
  - TC-FA-LBL-597 Expected a menyatakan urutan baris bernilai di depan `Pending` tidak diasersikan; spec mengikuti dan hanya mengasersi posisi `Pending` dan `No access`.
  - TC-FA-LBL-597 Langkah Uji 5 menyebut `[Clear Field]` lalu Search tanpa menyebut tombol penutup panel Filter; spec menambah penutupan panel sebagai langkah penghubung.
  - Expected e (hover sel `Pending` menampilkan tooltip) tidak punya langkah hover di TC; spec menambah langkah hover 13.
  - Post Condition TC tidak disebut; tidak diasersi.
