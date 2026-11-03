---
id: TC-FA-LBL-E2E-115-warranty-expiry-hari-ini-mengikuti-time-zone-general-settings
title: "Warranty Expiry: Hari Ini Mengikuti Time Zone General Settings"
priority: Medium
caseType: Edge
status: draft
sourceTc:
  - TC-FA-LBL-586
coverage:
  web: automated
---

# Warranty Expiry: Hari Ini Mengikuti Time Zone General Settings

## Prerequisites

- Mode: FE+BE. Backend nyata; tidak ada intercept. Jam server dan jam browser diatur lewat kemampuan suite (bagian 6).
- Akun aktor: Total Control `Company Warranty` (Pre-setup #51, Time Zone General Settings GMT+7), `Fixture.assetLabeling.akun.totalControlWarranty`, `Spectra.env.FA_TC_WARRANTY_PASSWORD`. Login di hook `before` spec ini (menggantikan akun default suite); halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Asset Master > tab Labels). Hook `after` mengembalikan sesi ke akun default suite (Total Control Company Alpha, `Spectra.env.FA_LBL_TC_PASSWORD`).
- Hook suite: Guided Tooltip, pemulihan state global, dan pembukaan Settings > Asset Master > tab Labels mengikuti hook di `suite.md` dan tidak ditulis ulang di sini.
- Data Pre-setup `Company Warranty` (#51), dirujuk lewat `Fixture.assetLabeling.warranty`: label `Warranty Tint` pada aset Active `Warranty Asset - 77` (Warranty Expiry 10 Nov 2026); Time Zone General Settings GMT+7.
- Data Dinamis: tidak ada.
- Fixture `fixtures/asset-labeling.json` (belum ada, disediakan tim FE; hanya identitas data, tanpa rahasia). Kunci yang dipakai spec ini: `Fixture.assetLabeling.akun.totalControlWarranty` (email akun Total Control `Company Warranty`) dan `Fixture.assetLabeling.warranty` (data Pre-setup #51).
- Kemampuan teknis (disediakan tim FE): hapus preferensi kolom Setup Column Drawer di browser (bagian 4). Pengaturan jam server dan jam browser dan pemulihannya (disediakan tim FE/BE; bagian 6).
- State global: jam server dan jam browser diatur di hook `before` setelah login ke 10 Nov 2026 18:00 UTC (11 Nov 2026 01:00 GMT+7) dan dibekukan; keduanya dipulihkan di hook `after` yang tetap jalan walau spec gagal di tengah. Konfigurasi kolom Setup Column Drawer diubah dan dipulihkan oleh langkah spec; hook `after` menghapus preferensi kolom di browser sebagai cadangan (bagian 4). Suite berjalan serial (`parallel: false`) karena state global jam.
- Cleanup: spec tidak membuat data. Data Pre-setup hanya dibaca dan tidak diubah.
- Env var: `Spectra.env.FA_TC_WARRANTY_PASSWORD`, `Spectra.env.FA_LBL_TC_PASSWORD` terdaftar di `executionConfig.environmentVariables` dan `.env.example`. `FA_LBL_TC_PASSWORD` dipakai hanya oleh hook `after` untuk mengembalikan sesi ke akun default suite.

## Test Steps

### TC-FA-LBL-586: Warranty Expiry: hari ini mengikuti Time Zone General Settings client

1. Klik chip `Warranty Tint` di kolom Label
2. Klik header kolom Actions (⋯) Drawer, klik `Setup Column...`, centang `Warranty Expiry`, lalu klik `[Save]`
3. Verifikasi tanggal `Warranty Asset - 77` `10 Nov 2026` berkelas danger (bukan warning seperti bila memakai UTC)
4. Hover tanggal `Warranty Asset - 77`
5. Verifikasi tooltip `Warranty expired`
6. Pemulihan: klik header kolom Actions (⋯) Drawer, klik `Setup Column...`, hapus centang `Warranty Expiry`, lalu klik `[Save]`
7. Tutup Drawer Tagged Asset

## Notes

- Sumber: `fixed-asset/settings-asset-labeling/TestCases/tc-settings-asset-labeling.md` section 4c (Drawer Tagged Asset). Subjudul `###` memetakan langkah ke TC granular.
- Jam sistem uji (precondition d TC) diatur di hook `before` dan dipulihkan di hook `after` (S-09, R-08); jam diatur absolut, tanpa langkah "Tunggu".
- Langkah penghubung (S-03): Pemulihan kolom `Warranty Expiry` dan tutup Drawer memulihkan keadaan awal.
- Pembagian TC lintas spec: TC-FA-LBL-582 sampai 585 dan 587 (penanda masa garansi dengan jam nyata) ada di spec 114.
- Temuan untuk QA:
  - TC-FA-LBL-586 precondition d menyebut hanya "jam sistem uji" tanpa menyebut jam server atau jam browser; spec mengatur keduanya bersama sesuai bagian 6.
