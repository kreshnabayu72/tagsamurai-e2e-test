---
name: Fixed Asset Tax Depreciation Class
id: suite-fixed-asset-tax-depreciation-class
description: Spec e2e turunan tc-tax-depreciation-class.md untuk Fixed Asset > Settings > Accounting > Tax Depreciation Class
executionOrder: 1.0
parallel: false
---

# Suite: Fixed Asset Tax Depreciation Class

Suite ini mencakup tab Tax Depreciation Class pada Settings > Accounting: tampilan tabel dan kolom, Empty State, Search, Filter, Sort, Setup Column, Pagination, Download, popup Used By, Versions, dan Changelog; Drawer Create dan Edit beserta validasi field dan perhitungan rate; versioning dengan Effective From (dialog Save Changes D-09, guard persempit D-08, Cancel Scheduled Version D-10, versi Current, Scheduled, dan Cancelled); aksi Activate, Deactivate, Delete, dan bulk beserta dialog konfirmasi dan blok (Guard 1 dan Guard 2); Restore default classes (D-12) dan seed; batas Master Data Count Limit (D-07) dan Selection Limit; job J-01, J-02, dan J-03; Role Matrix capability Manage accounting; gating plan dan state tenant (Starter, Suspended, Expired); pencatatan log di tiga surface (Changelog, System Log, Activity Log); sinkronisasi ke Asset Class, Preferences (Fiscal Year Start), General Settings, dan Accounting Period; Guided Tooltip; aksesibilitas; tampilan Android; konflik dua sesi; serta defense-in-depth (request langsung dan injeksi).

`parallel: false` karena spec mengubah atau bergantung pada state global: jam server dan browser (tanggal sistem uji, Time Zone entitas), plan dan status company (Starter, Suspended, Expired), Master Data Count Limit dan Selection Limit, Fiscal Year Start dan periode Accounting Period (Closed), General Settings (format tanggal, jam, zona waktu), job latar J-01, J-02, J-03, flag Guided Tooltip, dan konfigurasi Setup Column. Setiap spec menyiapkan dan memulihkan datanya sendiri lewat hook; urutan antar-spec tidak diasumsikan dan tidak ada spec yang bergantung pada hasil spec lain.

Pernyataan hook dan kemampuan suite (dinyatakan sekali di sini; `## Prerequisites` tiap spec merujuknya dengan satu baris):

- `before`: login akun aktor default suite (Total Control, company uji Fixed Asset; identitas akun dan nama env password ditetapkan tim FE di fixture; nama env baru didaftarkan penulis spec di `executionConfig.environmentVariables` dan `.env.example`). Spec yang aktor pertamanya akun lain (Read Only, Read, Create-Only, Update-Only, Delete-Only, Default User, atau company lain) login akun itu di hook `before` spec, dan hook `after` spec mengembalikan sesi ke akun default.
- `beforeEach`: tutup dialog yang terbuka dan buka Fixed Asset > Settings > Accounting > Tax Depreciation Class (layar awal spec). Spec yang membuka layar sendiri (Empty State, kunjungan pertama Guided Tooltip, akun tanpa capability, plan Starter, aplikasi Android, tab Asset Class atau Preferences) menulis pengecualian itu di `## Prerequisites`.
- Jaring pengaman form dirty: hook `beforeEach` mengonfirmasi `beforeunload` dan menutup dialog `Unsaved Changes`; ini bukan pengganti langkah pemulihan eksplisit spec (S-09).
- Flag Guided Tooltip halaman ini: hook suite `before` menyetel flag seen true untuk setiap akun aktor agar walkthrough tidak menutupi layar, dan `after` memulihkannya. Nama kunci flag dan mekanismenya disediakan tim FE/BE. Spec Guided Tooltip dikecualikan dan menulis pengaturan flag-nya di `## Prerequisites`.
- Sesi API aktor: login API (password) memakai token yang tidak dihitung sebagai sesi web, termasuk untuk akun yang sama dengan sesi UI. Dipakai untuk pelaku kedua yang hanya memicu perubahan state dan untuk request langsung ke server. Kemampuan ini disediakan tim BE/FE; tiap spec yang memakainya memuat satu baris rujukan ke butir ini.
- Seed dan pemulihan lewat API: seed 7 class bawaan, 9 class Example Data PRD (BLD-NP, BLD-P, LAND, NB-1, NB-2, NB-4, NB-KHS, NB-OLD, NB-SL), class berkunci (Last Posted Tax Year terisi), Used By lewat Asset Class pemakai, versi Scheduled/Current/Cancelled, tabel 21, 25, dan 26 class, tabel tanpa class, periode Accounting Period Closed/Soft Closed/Open, plan company (Starter, Growth, Professional, Enterprise), status company (Suspended, Expired), Master Data Count Limit (1000) dengan 999 class, Selection Limit, dua client (Client A dan B), dan perubahan capability role disediakan tim FE/BE; tiap spec merujuk butir ini dan hanya menulis fakta spesifik spec. Endpoint tidak dikarang (S-13).
- Kendali jam sistem (clock): jam server dan jam browser diatur bersama (tanggal sistem uji dan Time Zone entitas) dan dipulihkan di hook `after` spec yang memakainya (bagian 6); batas eksak memakai waktu absolut. Kemampuan ini dan penahanan/penjalanan job J-01, J-02, J-03 disediakan tim FE/BE.
- Pemulihan Setup Column: spec yang menyimpan konfigurasi kolom (tabel utama, Used By, Changelog) memulihkannya dengan langkah eksplisit di spec yang sama (8b.14, R-24) dan di hook `after` dengan menghapus preferensi kolom di browser. Kemampuan itu disediakan tim FE.
- Aplikasi Android: spec kelas mobile berjalan di perangkat atau emulator Android dengan aplikasi native Fixed Asset terpasang (`coverage.mobile`); disediakan tim FE.

## Data bersama

- Data uji tiap TC ada di kolom Precondition dan Data Uji TC, bukan di tabel Data Uji terpisah. Fixture `fixtures/fixedAssetTaxDepreciationClass.json` belum ada dan disediakan tim FE; memuat identitas data Pre-setup yang dirujuk Prerequisites (kode class seed dan Example Data, nama Asset Class pemakai, periode Closed). Nama kunci ditetapkan tim FE.
- Class milik spec memakai kode `KHS-*` dari TC dan data dinamis bersuffix `{runId}-<NNN>` bila perlu unik (S-12); target aksi tulis atau hapus memakai data milik spec (S-06).
