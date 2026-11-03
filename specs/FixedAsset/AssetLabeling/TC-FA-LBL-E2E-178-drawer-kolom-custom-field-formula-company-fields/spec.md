---
id: TC-FA-LBL-E2E-178-drawer-kolom-custom-field-formula-company-fields
title: "Drawer Kolom Custom Field Formula (Company Fields)"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-FA-LBL-581
coverage:
  web: automated
---

# Drawer Kolom Custom Field Formula (Company Fields)

## Prerequisites

- Mode: FE+BE. Backend nyata; tidak ada intercept.
- Akun aktor: Total Control `Company Fields` (Pre-setup #50), `Fixture.assetLabeling.akun.totalControlFields`, `Spectra.env.FA_TC_FIELDS_PASSWORD`. Login di hook `before` spec ini (menggantikan akun default suite); halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Asset Master > tab Labels). Hook `after` mengembalikan sesi ke akun default suite (Total Control Company Alpha, `Spectra.env.FA_LBL_TC_PASSWORD`).
- Hook suite: Guided Tooltip, pemulihan state global, dan pembukaan Settings > Asset Master > tab Labels mengikuti hook di `suite.md` dan tidak ditulis ulang di sini.
- Data Pre-setup `Company Fields` (#50), hanya dibaca dan dirujuk lewat `Fixture.assetLabeling.fields`: Asset Name `Field Item`; Custom Field Active grup General (Scope `Field Item`): `Field Tier` (Dropdown; opsi `Gold`, `Silver`), `Field Qty` (Numeric), `Field Calc` (Formula: `Field Qty` dikali 2); label `Field Label` pada aset Active `Field Item - 61` (Asset ID `FAS-061`; Tier `Gold`; Qty 5), `Field Item - 62` (`FAS-062`; Tier `Silver`; Qty 20), dan `Field Item - 63` (`FAS-063`; seluruh nilai belum diisi).
- Data Dinamis: tidak ada.
- Fixture `fixtures/asset-labeling.json` (belum ada, disediakan tim FE; hanya identitas data, tanpa rahasia). Kunci yang dipakai spec ini: `Fixture.assetLabeling.akun.totalControlFields` (email akun Total Control `Company Fields`) dan `Fixture.assetLabeling.fields` (data Pre-setup #50).
- Kemampuan teknis (disediakan tim FE): hapus preferensi kolom Setup Column Drawer di browser (bagian 4).
- State global: konfigurasi kolom Setup Column Drawer Tagged Asset (preferensi browser) diubah dan dipulihkan oleh langkah spec; hook `after` spec ini menghapus preferensi kolom di browser sebagai cadangan, bukan `[Reset to Default]` (bagian 4). Kemampuan menghapus preferensi itu disediakan tim FE. Tidak ada state global lain yang diubah.
- Suite berjalan serial (`parallel: false`).
- Cleanup: spec tidak membuat data. Data Pre-setup hanya dibaca dan tidak diubah (Last Updated tidak berubah).
- Env var: `Spectra.env.FA_TC_FIELDS_PASSWORD`, `Spectra.env.FA_LBL_TC_PASSWORD` terdaftar di `executionConfig.environmentVariables` dan `.env.example`. `FA_LBL_TC_PASSWORD` dipakai hanya oleh hook `after` untuk mengembalikan sesi ke akun default suite.

## Test Steps

### TC-FA-LBL-581: Kolom Custom Field Formula di Drawer: tanpa Search, Sort, dan Filter

1. Klik chip `Field Label` di kolom Label
2. Klik header kolom Actions (⋯) Drawer, klik `Setup Column...`, centang `Field Calc`, lalu klik `[Save]`
3. Perhatikan header kolom `Field Calc`, lalu klik header itu
4. Verifikasi header `Field Calc` tanpa ikon sort
5. Verifikasi klik header `Field Calc` tidak mengubah urutan baris
6. Klik icon Search, ketik nilai yang tampil pada sel `Field Calc` baris `Field Item - 62` (hasil `Field Qty` 20 dikali 2), tekan Enter
7. Verifikasi empty state `No results found` (kolom Formula tidak dicari)
8. Klik `(←)` pada kotak Search
9. Klik icon Filter di toolbar Drawer dan baca daftar field
10. Verifikasi Filter Panel memuat field `Field Tier` (anchor: panel sudah termuat)
11. Verifikasi Filter Panel tidak memuat field `Field Calc`
12. Tutup panel Filter
13. Pemulihan: klik header kolom Actions (⋯) Drawer, klik `Setup Column...`, hapus centang `Field Calc`, lalu klik `[Save]`
14. Tutup Drawer Tagged Asset

## Notes

- Sumber: `fixed-asset/settings-asset-labeling/TestCases/tc-settings-asset-labeling.md` section 4c (Drawer Tagged Asset).
- Langkah penghubung (S-03): `Klik (←) pada kotak Search`, tutup panel Filter, Pemulihan kolom, dan tutup Drawer memulihkan keadaan awal (S-09).
- Asersi tambahan (S-03): `Verifikasi Filter Panel memuat field Field Tier` ditulis sebagai anchor positif untuk asersi absence field (bagian 8b butir 2); `Field Tier` dipilih karena TC-FA-LBL-577 menetapkan field itu ada di Filter Panel.
- Pembagian TC lintas spec: Custom Field Dropdown, Multi-Dropdown, Date, dan DateTime (TC-FA-LBL-577, 578) ada di spec 110; Custom Field Numeric, Currency, Percentage, Text, Email, dan Phone (TC-FA-LBL-579, 580) di spec 111.
- Temuan untuk QA:
  - TC-FA-LBL-581 Langkah Uji 4 menyebut "ketik nilai yang tampil pada sel `Field Calc`" tanpa nilai konkret; spec menurunkannya dari Pre-setup #50 (`Field Qty` 20 dikali 2) tanpa menuliskan angka hasil.
