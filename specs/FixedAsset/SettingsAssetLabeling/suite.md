---
name: Fixed Asset Settings Asset Labeling
id: suite-fixed-asset-settings-asset-labeling
description: Spec e2e turunan PRD settings-asset-labeling.md (sourceRules) untuk Fixed Asset > Settings > Asset Master > Labels
executionOrder: 2.0
parallel: false
---

# Suite: Fixed Asset Settings Asset Labeling

Suite ini mencakup tab Labels pada Settings > Asset Master: screening Labels List dan Changelog, Create (Color Picker, Live Preview, validasi nama dan hex, batas Master Data Count Limit), Edit (validasi, perubahan kapitalisasi, zero-delta), Delete single dan Bulk Delete, provenance label Default dan manual pada aset, Role Matrix, request langsung, race dua admin, state tenant Suspended dan Expired, dan state error di mode mock.

`parallel: false` karena spec mengubah atau menghapus state bersama (katalog Label client, Master Data Count Limit, status client, data aset). Spec Delete (017 sampai 020) dijalankan sesudah spec lain. Setiap spec tetap menyiapkan dan membersihkan datanya sendiri lewat hook dan tidak bergantung pada hasil spec lain.

## Hook suite

- `before`: login akun aktor default suite (Total Control, DU-01) dan membuka Settings > Asset Master > tab Labels.
- `beforeEach`: membuka tab Labels bila spec memakai halaman itu; spec yang berpindah client atau akun membuka halamannya sendiri.
- `after`: memulihkan state global (katalog Label, System Limits, status client) ke nilai awal dan mengembalikan sesi ke akun default suite.
- `## Prerequisites` tiap spec merujuk hook ini dengan satu baris dan tidak menulis ulang isinya.

## Kemampuan teknis suite

- Sesi API aktor (login API password untuk akun yang sama dengan sesi UI, token tidak dihitung sebagai sesi web) dan fixture BE untuk seeding label, aset, Asset Name, dan membaca state; disediakan tim FE/BE tanpa mekanisme karangan.
- Seeding volume: 500 aset berlabel dan katalog Label sampai Master Data Count Limit lewat fixture BE.
- Client khusus: Suspended, Expired, dan di batas katalog (tier biasa dan Enterprise).
- Klien HTTP untuk request langsung ke server (kelas a) dan dua konteks browser (kelas c).
- `Spectra.intercept()` untuk spec `Mode: mock`.

## Env

`FA_TC_EMAIL`, `FA_TC_PASSWORD`, `FA_RO_*`, `FA_CO_*`, `FA_UO_*`, `FA_DO_*`, `FA_NOROLE_*`, `FA_AMDCRUD_*`, `FA_ATUPD_*`, `FA_TC2_*`, `FA_SUSP_TC_*`, `FA_EXP_TC_*`, `FA_LIM_TC_*`, `FA_LIM_ENT_TC_*`. Semua didaftarkan di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`.
