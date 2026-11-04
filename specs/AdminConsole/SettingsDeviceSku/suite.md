---
name: Admin Console Settings Device SKU
id: suite-admin-console-settings-device-sku
description: Spec e2e turunan tc-settings-device-sku.md untuk Admin Console > Settings > Device > Device SKU
executionOrder: 1.0
parallel: false
---

# Suite: Admin Console Settings Device SKU

Suite ini mencakup halaman Settings > Device > Device SKU: List (Search, Filter, Sort, Setup Column, Pagination, Download), Sidebar Category, popup Register dan Edit SKU, Delete single dan Bulk Delete, modal Changelog, popup Device SKU Detail (Usage by Company), tampilan mobile Android, Role Matrix dan scope Principal/Distributor, pencatatan log di Changelog, System Log, dan Activity Log, sinkronisasi lintas modul, defense-in-depth, state tenant, konkurensi, dan ketahanan terhadap kegagalan server.

`parallel: false` karena spec mengubah state global (Date Format dan Time Zone General Settings, Selection Limit, capability role, Local Registration) dan data SKU bersama. Setiap spec tetap menyiapkan dan memulihkan datanya sendiri lewat hook.

## Hook suite

- `before`: login akun aktor default suite (Total Control Principal, `Spectra.env.AC_DS_TC_PASSWORD`).
- `beforeEach`: membuka Settings > Device > Device SKU.
- `after`: memulihkan state global dan mengembalikan sesi ke akun default suite.
- Sesi API aktor (login API password, tidak dihitung sebagai sesi web) disediakan tim BE/FE; Prerequisites spec merujuknya dengan satu baris.
- `## Prerequisites` tiap spec merujuk hook ini dengan satu baris.
- Guided Tooltip: hook `before` suite menyetel flag Guided Tooltip halaman Device SKU menjadi true untuk setiap akun aktor yang dipakai spec dalam suite (nilai awal tiap akun dicatat) lewat API agar walkthrough otomatis tidak menutupi layar, dan hook `after` memulihkan nilai awal tiap akun. Nama flag dan mekanisme penyetelan disediakan tim FE/BE (`guided_tooltip_seen_<page_key>`, konvensi §4). `## Prerequisites` tiap spec memuat satu baris rujukan ke butir ini.
- Fixture tunggal `Fixture.settingsDeviceSku` merujuk berkas `fixtures/settings-device-sku.json` yang belum ada dan disediakan tim FE; memuat email akun, URL halaman, dan data Pre-setup yang dirujuk Prerequisites tiap spec. Nama kunci ditetapkan tim FE.
- Fixture backend pemulih Pre-setup (disediakan tim FE/BE, idempotent; S-06 2026-10-30): mengembalikan SKU Principal dan Distributor Pre-setup (#29 sampai #31, #33) ke keadaan awal termasuk Last Modified, dan menghapus entri Changelog buatan test bila memungkinkan. Dijalankan di hook `before` dan `after` spec yang mengubah data Pre-setup. Suite berjalan serial.
- Pengecualian S-12 butir A-11 (`docs/e2e-conventions.md` Lampiran A): nama literal tanpa suffix `{runId}` untuk Population Pre-setup Device SKU (SKU Principal inti, `SEED-001` sampai `SEED-119`, `LOC-NOR-01` sampai `LOC-NOR-03`, Device Name, Brand, Category terkait, dan seed Changelog 35 entri). Dinyatakan di sini sekali untuk seluruh suite; spec yang memakainya menyebut "pengecualian S-12 A-11" di `## Notes`. Data yang dibuat spec sendiri tetap bersuffix `{runId}`; spec 062, 063, 064, dan 065 memakai SKU milik spec bersuffix untuk Save, bukan SKU Pre-setup. Total entri audit trail seed tetap relatif (baseline atau Filter Date 01/09/26 sampai 03/10/26).
- Preferensi Setup Column dihapus di hook `after` (kemampuan disediakan tim FE, bukan lewat `[Reset to Default]`): konfigurasi kolom popup Usage by Company (spec 137 sampai 141, juga di hook `before` agar kolom pada konfigurasi bawaan), konfigurasi kolom tabel List lewat Overlay Column Visibility dan popup Setup Column (spec 005, 018, 044, 067, 087, 088, 094, 099, 101 sampai 106, 109, dan 176 untuk kolom Hardware Type, Range Type, dan TAG Type), serta konfigurasi kolom modal Changelog (spec 124 sampai 127 dan 192). Spec yang mengubah konfigurasi kolom juga memulihkannya dengan langkah eksplisit di akhir spec (tanpa `Verifikasi`); hook `after` menjadi cadangan.
- Pengecualian `beforeEach` untuk spec role-negatif 016 dan 017 (akun tanpa akses halaman Device SKU): membuka Settings > Device > Device SKU memunculkan toast 403 dari `beforeEach`, sehingga spec menutup toast itu sebelum asersi, atau `beforeEach` tidak membuka halaman untuk akun tersebut. Pilihan teknis ditetapkan tim FE; langkah spec tidak bergantung pada halaman yang terbuka.
- Env `AC_DS_*` (`AC_DS_TC_PASSWORD`, `AC_DS_TC2_PASSWORD`, `AC_DS_RO_PASSWORD`, `AC_DS_C_PASSWORD`, `AC_DS_U_PASSWORD`, `AC_DS_D_PASSWORD`, `AC_DS_CUD_PASSWORD`, `AC_DS_NOCAP_PASSWORD`, `AC_DS_GM_PASSWORD`, `AC_DS_PARTNER_PASSWORD`, `AC_DS_DIST_PASSWORD`, `AC_DS_DIST_C_PASSWORD`, `AC_DS_DIST_U_PASSWORD`, `AC_DS_DIST_D_PASSWORD`, `AC_DS_DIST_RO_PASSWORD`, `AC_DS_DISTOFF_PASSWORD`, `AC_DS_DISTEXP_PASSWORD`, `AC_DS_DISTSUSP_PASSWORD`, `AC_DS_PRIEXP_PASSWORD`, `AC_DS_FRESH_PASSWORD`, `AC_DS_BIG_PASSWORD`, `AC_DS_BIG5K_PASSWORD`) disediakan tim FE; belum terdaftar di `executionConfig.environmentVariables` dan `.env.example`.
