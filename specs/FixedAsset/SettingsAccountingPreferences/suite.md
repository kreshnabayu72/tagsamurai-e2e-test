---
name: Fixed Asset Settings Accounting Preferences
id: suite-fixed-asset-settings-accounting-preferences
description: Spec e2e turunan tc-settings-accounting-preferences.md untuk Fixed Asset > Settings > Accounting > Preferences
executionOrder: 1.0
parallel: false
---

# Suite: Fixed Asset Settings Accounting Preferences

Suite ini mencakup tab Preferences pada Settings > Accounting (SectionCard General, Capitalization, Depreciation, Disposal, Chart of Accounts, Journal Export), validasi form (setting wajib, Default Capitalization Threshold, First Accounting Period, akun default), alur Save dengan dialog pratinjau dampak D-01, kunci Fiscal Year Start dan First Accounting Period beserta dialog D-03, dialog Unsaved Changes D-04, modal Changelog (Search, Filter, Sort, Setup Column, paginasi, Download), pencatatan log di tiga surface (Changelog, System Log, Activity Log), sinkronisasi ke Asset Class, Tax Depreciation Class, Accounting Period dan Chart of Accounts, Role Matrix, Guided Tooltip, aksesibilitas dan tampilan Android, gating plan dan state tenant, defense-in-depth, konflik dua sesi, ketahanan terhadap kegagalan server, serta TC `[DEFERRED]` pada modul pemilik dan konsumen yang belum disusun (aktivasi dan job J-01, In-service Date Source, Depreciation in Disposal Month, akun Gain dan Loss, Disposal Documents, Capitalization Offset, Found Asset Credit Account, Journal Grouping pada Export Journal).

`parallel: false` karena spec mengubah atau bergantung pada state global: jam sistem (bulan berjalan menurut Time Zone entitas), plan dan status company (Starter, Suspended, Expired), Run Posted (posting penyusutan pertama) dan Exported through, Preferences company, akun Chart of Accounts, capability role, flag Guided Tooltip, dan konfigurasi kolom Changelog. Setiap spec menyiapkan dan memulihkan datanya sendiri lewat hook; urutan antar-spec tidak diasumsikan dan tidak ada spec yang bergantung pada hasil spec lain.

## Hook suite

- `before`: login akun aktor default suite (Total Control, Pre-setup, company `PT Contoh Konstruksi`, `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, password lewat `Spectra.env`; nama env baru yang didaftarkan penulis spec di `executionConfig.environmentVariables` dan `.env.example`). Spec yang aktor pertamanya akun atau company lain login akun itu di hook `before` spec, dan hook `after` spec mengembalikan sesi ke akun default.
- `beforeEach`: tutup dialog yang terbuka dan buka Fixed Asset > Settings > Accounting > Preferences (layar awal spec). Spec yang membuka layar sendiri (screening kunjungan pertama, Guided Tooltip, akun tanpa capability, plan Starter, aplikasi Android) menulis pengecualian itu di `## Prerequisites`.
- Jaring pengaman form dirty: hook `beforeEach` mengonfirmasi `beforeunload` dan menutup dialog `Unsaved Changes`; ini bukan pengganti langkah pemulihan eksplisit spec (S-09).
- Flag Guided Tooltip halaman Preferences (`guided_tooltip_seen_fa-accounting-preferences`): hook suite `before` men-set flag true untuk setiap akun aktor yang dipakai agar walkthrough tidak menutupi layar, dan `after` memulihkan nilai awal. Mekanisme disediakan tim FE/BE. Spec Guided Tooltip dikecualikan dan menulis pengaturan flag-nya di `## Prerequisites`.
- Sesi API aktor: login API (password) memakai token yang tidak dihitung sebagai sesi web, termasuk untuk akun yang sama dengan sesi UI. Dipakai untuk pelaku kedua yang hanya memicu perubahan state dan untuk request langsung ke server. Kemampuan ini disediakan tim BE/FE; tiap spec yang memakainya memuat satu baris rujukan ke butir ini.
- Seed dan pemulihan lewat API: seed company Pre-setup (PA, PB, PC) dan pemulihan Preferences ke nilai awal, plan, status company, penguncian (Run Posted pertama), versi Tax Depreciation Class ber-Effective From, transaksi bertanggal, pelepasan menunggu posting, Asset Class, dan akun Chart of Accounts disediakan tim FE/BE; tiap spec merujuk butir ini dan hanya menulis fakta spesifik spec.
- Kendali jam sistem (clock): jam server dan jam browser diatur bersama untuk TC bulan berjalan menurut Time Zone entitas dan dipulihkan di hook `after` spec yang memakainya (bagian 6). Kemampuan disediakan tim FE/BE.
- Pemulihan Setup Column Changelog: spec yang menyimpan konfigurasi kolom memulihkannya dengan langkah eksplisit di spec yang sama (8b.13, R-24) dan di hook `after` dengan menghapus preferensi kolom di browser. Kemampuan itu disediakan tim FE.

## Data bersama

- Seri fixture: PA (TC 1-175), PB (TC 176-361), PC (TC 362-631) adalah seed terisolasi; nilai awal Preferences PA-2, PB-1, PC-1 setara. Perubahan Preferences oleh spec dipulihkan ke nilai awal lewat seed sebelum TC berikutnya; target tulis memakai data milik spec (S-06) dan data dinamis (akun baru, entri log) bersuffix `{runId}-<NNN>` bila perlu unik (S-12).
- Pelepasan "belum diposting" atau "menunggu posting" pada fixture (PB-6a, PB-6b, PC-7, PC-18) adalah baris pelepasan berstatus Executed (belum Posted); baris Waiting for Approval dan Waiting for Execution tidak dihitung.
- Fixture `fixtures/settings-accounting-preferences.json` belum ada dan disediakan tim FE; memuat identitas data Pre-setup yang dirujuk Prerequisites (kode akun Chart of Accounts, nama Asset Class, entri Changelog contoh). Nama kunci ditetapkan tim FE.
- Data yang butuh fixture backend (Run Posted, Exported through, versi Tax Depreciation Class, transaksi bertanggal, pelepasan menunggu posting, 105 entri Changelog PB-C2, company tanpa baris Preferences, company plan Starter, entitas Suspended/Expired, perubahan akun) dan modul pemilik/konsumen untuk TC `[DEFERRED]` ditulis di `## Prerequisites` spec sebagai "disediakan tim FE" tanpa endpoint karangan (S-13).
