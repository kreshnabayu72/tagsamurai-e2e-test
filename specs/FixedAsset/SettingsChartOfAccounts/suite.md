---
name: Fixed Asset Settings Chart of Accounts
id: suite-fixed-asset-settings-chart-of-accounts
description: Spec e2e turunan tc-settings-chart-of-accounts.md untuk Fixed Asset > Settings > Accounting > Chart of Accounts
executionOrder: 1.0
parallel: false
---

# Suite: Fixed Asset Settings Chart of Accounts

Suite ini mencakup halaman Chart of Accounts (tab keempat Settings > Accounting): tabel akun dengan Search, Filter, Sort, Pagination, Setup Column, dan Download; modal Add Account dan Edit Account; Activate dan Deactivate (single dan bulk); Delete (single dan bulk) beserta dialog blok; popup Used By; Modal Changelog dan pencatatan di tiga surface (Changelog, System Log, Activity Log); Role Matrix; Guided Tooltip; tampilan Android; batas jumlah akun dan Selection Limit; state tenant (Suspended, Expired, plan Starter); konflik dua sesi; defense-in-depth; serta ketahanan terhadap kegagalan server.

`parallel: false` karena spec mengubah atau bergantung pada state global: plan dan status client, System Limits (Master Data Count Limit dan Selection Limit), capability role, General Settings (format tanggal, waktu, dan zona waktu), nilai default company di Settings > Accounting > Preferences (SET-05, SET-06, SET-08, SET-09, SET-13), flag Guided Tooltip, serta kumpulan akun bersama per client. Setiap spec menyiapkan dan membersihkan datanya sendiri lewat hook; urutan antar-spec tidak diasumsikan dan tidak ada spec yang bergantung pada hasil spec lain.

## Hook suite

- `before`: login akun aktor default suite (Total Control, `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, password lewat `Spectra.env.FA_TC_PASSWORD`). Spec yang aktor pertamanya akun atau client lain login akun itu di hook `before` spec, dan hook `after` spec mengembalikan sesi ke akun default.
- `beforeEach`: tutup dialog yang terbuka dan buka Fixed Asset > Settings > Accounting > Chart of Accounts (layar awal spec). Spec yang membuka layar sendiri (screening halaman pertama, tabel kosong, Guided Tooltip, akun tanpa capability, Android) menulis pengecualian itu di `## Prerequisites`.
- Jaring pengaman form dirty: hook `beforeEach` mengonfirmasi `beforeunload` dan menutup dialog `Unsaved Changes`; ini bukan pengganti langkah pemulihan eksplisit spec (S-09).
- Flag Guided Tooltip halaman Chart of Accounts: hook suite `before` men-set flag true untuk setiap akun aktor yang dipakai agar tur tidak menutupi layar, dan `after` memulihkan nilai awal. Mekanisme disediakan tim FE/BE. Spec Guided Tooltip dikecualikan dan menulis pengaturan flag-nya di `## Prerequisites`.
- Sesi API aktor: login API (password) memakai token yang tidak dihitung sebagai sesi web, termasuk untuk akun yang sama dengan sesi UI. Dipakai untuk pelaku kedua yang hanya memicu perubahan state (hapus, ubah status, ekspor akun oleh sesi lain). Kemampuan ini disediakan tim BE/FE; tiap spec yang memakainya memuat satu baris rujukan ke butir ini.
- Seed dan pemulihan lewat API: seed akun Pre-setup (P1 sampai P118), client uji (P23 sampai P26, P89, P110, client kosong, client Suspended dan Expired, client plan Starter), Asset Class pemakai akun (Used By), nilai default company di Preferences, serta pemulihan plan, status client, System Limits, dan jalur ekspor Journal J-06 disediakan tim FE/BE; tiap spec merujuk butir ini dan hanya menulis fakta spesifik spec.
- Pemulihan Setup Column: spec yang menyimpan konfigurasi kolom memulihkannya dengan langkah eksplisit di spec yang sama dan di hook `after` dengan menghapus preferensi kolom di browser, bukan lewat `[Reset to Default]`. Kemampuan itu disediakan tim FE.

## Data bersama

- Akun Pre-setup P1 sampai P118: akun P1 sampai P5 hanya dibaca; target tulis, hapus, nonaktifkan, dan ekspor memakai akun sekali pakai tersendiri milik spec (kebijakan fixture TC). Data Dinamis D1 sampai D16 dibuat spec lewat UI dan dibersihkan di `after`.
- Pengecualian A-18 (S-06 dan S-12) `[KEPUTUSAN 2026-11-04]`: akun Pre-setup sekali pakai (P9, P16–P22, P27, P33–P38, P43, P45–P86, P88–P109, P111–P117) boleh menjadi target aksi tulis, hapus, atau ubah status, dan Account Code literal (maksimal 15 karakter) boleh dipakai tanpa suffix `{runId}`. Syarat suite: seed idempotent dan pemulihan ke keadaan awal dijamin fixture backend dari tim FE/BE, dijalankan di hook `before` dan `after` spec yang memakainya; suite serial (`parallel: false`); satu akun Pre-setup dipakai satu spec saja, dan satu Account Code literal dipakai satu spec saja kecuali hanya diketik pada Create yang selalu ditolak atau gagal, atau dipulihkan di `before` dan `after`. Tiap spec yang memakainya menulis satu baris rujukan ke butir ini di `## Prerequisites` (akun milik spec cukup dinyatakan di sana); butir `A-18` di `## Notes` ditulis hanya bila Account Code literal tanpa suffix menjadi objek asersi atau Expected TC, beserta TC pemakainya.
- Fixture `fixtures/settings-chart-of-accounts.json` belum ada dan disediakan tim FE; memuat identitas akun Pre-setup, client uji, dan Asset Class yang dirujuk Prerequisites. Nama kunci ditetapkan tim FE; langkah dan Prerequisites merujuknya dengan satu notasi `Fixture.settingsChartOfAccounts.<kunci>`.
- Data yang butuh fixture backend (client dengan 1000 akun, 999 akun, 101 akun, lebih dari 5.000 akun, Asset Class pemakai akun, nilai default company, jalur ekspor J-06) ditulis di `## Prerequisites` spec sebagai "disediakan tim FE" tanpa endpoint karangan (S-13).
