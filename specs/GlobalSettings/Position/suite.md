---
name: Global Settings Position
id: suite-global-settings-position
description: Spec e2e turunan tc-position.md untuk Global Settings > User > Position
executionOrder: 1.0
parallel: false
---

# Suite: Global Settings Position

Suite ini mencakup tab Position pada Global Settings > User: tabel (Search, Filter, Sort, Pagination, Setup Column, Download), Create, Edit, Delete single dan Bulk Delete, Popup Changelog, Role Matrix, Guided Tooltip, pencatatan log di tiga surface (Changelog, Activity Log, System Log aktor), sinkronisasi ke form User dan Non-Login User, batas Master Data Count Limit dan Selection Limit, state tenant, konkurensi dua admin, serta ketahanan terhadap kegagalan server.

`parallel: false` karena spec mengubah state global (plan dan status Client, format tanggal General Settings, capability role, flag Guided Tooltip, Master Data Count Limit dan Selection Limit di Admin Console). Spec yang menghapus data (Delete single dan Bulk Delete) dijalankan sesudah spec lain. Flag Guided Tooltip halaman Position (`guided_tooltip_seen_gs-position`): hook suite `before` men-set flag itu true untuk setiap akun aktor yang dipakai spec dalam suite (nilai awal tiap akun dicatat) supaya walkthrough otomatis tidak menutupi layar, dan hook suite `after` memulihkan nilai awal. Mekanisme penyetelan flag disediakan tim FE/BE. Spec 005 dan 006 menguji flag itu sendiri sehingga dikecualikan dan menulis pengaturan flag-nya di `## Prerequisites` masing-masing; tiap spec lain memuat satu baris rujukan ke pernyataan ini.

Setiap spec tetap menyiapkan dan membersihkan datanya sendiri lewat hook dan tidak bergantung pada hasil spec lain.
