---
name: Fixed Asset Asset Class
id: suite-fixed-asset-asset-class
description: Spec e2e turunan tc-asset-class.md untuk Fixed Asset > Settings > Accounting > Asset Class
executionOrder: 7.0
parallel: false
---

# Suite: Fixed Asset Asset Class

Suite ini mencakup tab Asset Class pada halaman Settings > Accounting: tabel Asset Class (Search, Filter, Sort, Setup Column, paginasi, Download, Bulk Action Bar, toggle Active), Halaman Detail mode Create dan Edit (tab General, Depreciation, Accounts, Asset Names, Clear Field, Unsaved Changes), Duplicate, Use Recommended Classes, Assign, Move, dan Unassign Asset Name (termasuk Effective From dan pratinjau dampak), Delete dan guard bisnis, Apply Changes dan versi Scheduled, kunci Class Code dan reklasifikasi Reclassify Balances, Modal Changelog, Alert dependensi akun dan banner Asset Name tanpa Asset Class, Guided Tooltip, Role Matrix, batas plan dan Master Data Count Limit, pencatatan log di Changelog, System Log, dan Activity Log, sinkronisasi ke modul Chart of Accounts, Tax Depreciation Class, dan Asset Name, state tenant, konflik dua sesi, defense-in-depth, serta ketahanan terhadap kegagalan server.

`parallel: false` karena banyak spec mengubah atau bergantung pada state global: plan dan status client (Suspended/Expired), Master Data Count Limit dan Selection Limit, capability role akun aktor, Chart of Accounts dan Tax Depreciation Class bersama per client, keanggotaan Asset Name tanpa Asset Class (banner dan D-23), General Settings (format tanggal dan zona waktu), periode akuntansi dan Last Posted/Last Exported Period, job penerapan versi Scheduled, dan flag Guided Tooltip. Setiap spec menyiapkan dan membersihkan datanya sendiri lewat hook; urutan antar-spec tidak diasumsikan dan tidak ada spec yang bergantung pada hasil spec lain.

## Hook suite

- `before`: login akun aktor default suite (Total Control, `totalControl_automated_{namaCompany}@qwertysystem.net`, password lewat `Spectra.env`). Spec yang aktor pertamanya akun role lain atau client lain login akun itu di hook `before` spec, dan hook `after` spec mengembalikan sesi ke akun default.
- `beforeEach`: tutup dialog yang terbuka dan buka Fixed Asset > Settings > Accounting > tab Asset Class (layar awal spec). Spec yang membuka layar sendiri (screening halaman pertama, Guided Tooltip, akun tanpa capability, plan Starter) menulis pengecualian itu di `## Prerequisites`.
- Jaring pengaman form dirty: hook `beforeEach` mengonfirmasi `beforeunload` dan menutup dialog `Unsaved Changes`; ini bukan pengganti langkah pemulihan eksplisit spec (S-09).
- Flag Guided Tooltip halaman ini (`guided_tooltip_seen_fa-asset-class`): hook suite `before` men-set flag true untuk setiap akun aktor yang dipakai agar walkthrough tidak menutupi layar, dan `after` memulihkan nilai awal. Spec Guided Tooltip (TC-46 s.d. 55) dikecualikan dan menulis pengaturan flag di `## Prerequisites` masing-masing. Mekanisme disediakan tim FE/BE.
- Sesi API aktor: login API (password) memakai token yang tidak dihitung sebagai sesi web, termasuk untuk akun yang sama dengan sesi UI. Dipakai sebagai pelaku kedua yang hanya memicu perubahan state. Kemampuan ini disediakan tim BE/FE; tiap spec yang memakainya memuat satu baris rujukan ke butir ini.
- Seed dan pemulihan lewat API/fixture BE: sembilan Asset Class contoh Pre-setup, Asset Class bertanda `B-*` per TC, Asset Name dengan dan tanpa aset aktif, Chart of Accounts, Tax Depreciation Class, entri Changelog contoh, Last Posted/Last Exported Period, versi Scheduled, plan client, status entitas, Master Data Count Limit, Selection Limit, dan volume besar disediakan tim FE/BE; tiap spec merujuk butir ini dan hanya menulis fakta spesifik spec.
- Pemulihan Setup Column: spec yang menyimpan konfigurasi kolom memulihkannya di hook `after` dengan menghapus preferensi kolom di browser, bukan lewat `[Reset to Default]`. Kemampuan disediakan tim FE.

## Data bersama

- Fixture `fixtures/fixed-asset-asset-class.json` belum ada dan disediakan tim FE; memuat identitas data Pre-setup yang dirujuk Prerequisites. Nama kunci ditetapkan tim FE.
- Target aksi tulis dan hapus memakai data milik spec bila TC tidak mewajibkan baris seed tertentu (S-06, S-12); baris seed bernama literal yang asersinya bergantung pada nama, urutan, atau jumlah dicatat di `## Prerequisites` dan Notes (lihat plan, Pertanyaan terbuka nomor 1).
