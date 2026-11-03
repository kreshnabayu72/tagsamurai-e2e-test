---
name: Fixed Asset Asset Labeling
id: suite-fixed-asset-asset-labeling
description: Spec e2e turunan tc-settings-asset-labeling.md untuk Fixed Asset > Settings > Asset Master > Labels
executionOrder: 2.0
parallel: false
---

# Suite: Fixed Asset Asset Labeling

Suite ini mencakup tab Labels pada Settings > Asset Master: Labels List (Search, Filter, Sort, Pagination, Setup Column, Download), Create (Color Picker, Live Preview, validasi, batas Master Data Count Limit), Edit (zero-delta), Delete single dan Bulk Delete (dialog D-01 sampai D-06), Modal Changelog: Labels, Drawer Tagged Asset (kolom baru dan gerbang akses sel), Role Matrix, pencatatan log di Changelog, System Log, dan Activity Log, sinkronisasi ke modul konsumen (Asset List, Asset Detail, Reports, Asset Transactional Policy, Asset Name), defense-in-depth, state tenant, konkurensi dua sesi, ketahanan terhadap kegagalan server, dan layar mobile.

`parallel: false` karena spec mengubah state global (Master Data Count Limit dan Selection Limit di System Limits, format tanggal General Settings, plan dan status Client, jam server dan jam browser, lisensi FA-7, capability role) dan memakai Company khusus dengan Population nama literal (Company Alpha 9 label Pre-setup #12). Spec yang menghapus data (Delete, Bulk Delete) dijalankan sesudah spec lain. Setiap spec tetap menyiapkan dan membersihkan datanya sendiri lewat hook dan tidak bergantung pada hasil spec lain.

## Hook suite

- `before`: login akun aktor default suite (Total Control Company Alpha, `Spectra.env.FA_LBL_TC_PASSWORD`) dan membuka Settings > Asset Master > tab Labels; menyetel flag Guided Tooltip menjadi `seen` bila ada. Mekanisme penyetelan disediakan tim FE/BE.
- `beforeEach`: membuka tab Labels bila spec memakai halaman itu (spec yang berpindah Company atau akun membuka halamannya sendiri).
- `after`: memulihkan state global (System Limits, General Settings, plan dan status Client, jam server dan browser, konfigurasi Setup Column) ke nilai awal dan mengembalikan sesi ke akun default suite.
- `## Prerequisites` tiap spec merujuk hook ini dengan satu baris dan tidak menulis ulang isinya.

## Kemampuan teknis suite

- Sesi API aktor (login API password untuk akun yang sama dengan sesi UI, token tidak dihitung sebagai sesi web) dan fixture BE untuk seeding label, aset, Asset Name, entri log, dan membaca state (bagian 5, 2026-10-30). Spec yang memakainya merujuk satu baris di Prerequisites.
- Seeding Company khusus dan Population: Pre-setup #10 (120 label), #11 (Master Data Count Limit 1000), #15 Suspended, #16 Expired, #17 Changelog, #18 (500 aset), #21 Kosong, #24 (5.001 label), #36, #37 Probe, #38 Gate, #49 Gate Grace/Lapsed, #50 Fields, #51 Warranty, #53/#55 Depreciation.
- Pengaturan jam server dan jam browser (bagian 6) dan pemulihannya di `after`; `Spectra.intercept()` untuk 5xx, timeout, dan menahan respons.
- Dua konteks browser (spec kelas c), pembaca CSV/XLSX untuk spec kelas f, aplikasi mobile Fixed Asset Android (dua spec mobile).

## Env

`FA_LBL_TC_PASSWORD`, `FA_TC2_PASSWORD`, `FA_RO_PASSWORD`, `FA_CREATEONLY_PASSWORD`, `FA_UPDATEONLY_PASSWORD`, `FA_DELETEONLY_PASSWORD`, `FA_READCAP_PASSWORD`, `FA_FULLCRUD_PASSWORD`, `FA_NOROLE_PASSWORD`, `FA_POLICYREAD_PASSWORD`, `FA_ASSETTAGUPDATE_PASSWORD`, `FA_DEFAULTUSER_PASSWORD`, `FA_GMNOCAP_PASSWORD`, `FA_TC_<COMPANY>_PASSWORD` per Company khusus, `FA_GATE_<ROLE>_PASSWORD` per aktor Gate, `FA_WARRANTYNOPURCHASE_PASSWORD`, `FA_DEPVALUE_PASSWORD`, `FA_RO_CHANGELOG_PASSWORD`, `FA_TC_EXTRA_PASSWORD` (Company Extra, Pre-setup #56; nama env pilihan spec, nilai dan akun disediakan tim FE), `FA_TC_SORTCHANGELOG_PASSWORD`. Semua didaftarkan di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`.
