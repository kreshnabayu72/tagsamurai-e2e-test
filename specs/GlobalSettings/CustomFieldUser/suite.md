---
name: Global Settings Custom Field User
id: suite-global-settings-custom-field-user
description: Spec e2e turunan tc-custom-field-user.md untuk Global Settings > User > Custom Field
executionOrder: 1.0
parallel: false
---

# Suite: Global Settings Custom Field User

Suite ini mencakup tab Custom Field pada Global Settings > User: tabel (Search, Filter, Sort, Pagination, Setup Column, Download), Create, Edit (termasuk ganti Data Type, Decimal Places terkunci, dan Value Dropdown), Delete single dan Bulk Delete, Toggle Active single dan Bulk Activate/Deactivate, Popup Changelog, Role Matrix, Guided Tooltip, pencatatan log di tiga surface (Changelog, Activity Log, System Log aktor), input Custom Field pada form User, sinkronisasi ke modul lain (Detail User, My Profile, Fixed Asset, Admin Console, Import), format tanggal dan Time Zone General Settings, batas Master Data Count Limit dan Selection Limit, state tenant (Suspended, Expired, plan), konkurensi dua admin, serta ketahanan terhadap kegagalan server.

`parallel: false` karena spec mengubah state global (plan dan status Client, format tanggal dan Time Zone General Settings, capability role, flag Guided Tooltip, Master Data Count Limit dan Selection Limit di Admin Console). Spec yang menghapus data (Delete single, Bulk Delete, Select All) dijalankan sesudah spec lain dalam urutan folder.

## Hook suite

- **Login:** hook `before` login sekali per akun aktor yang dipakai spec (password lewat `Spectra.env.*`, tidak ditulis di spec atau fixture). Spec yang berganti akun mencantumkan akunnya di `## Prerequisites`.
- **Guided Tooltip:** flag halaman Custom Field (`guided_tooltip_seen_gs-custom-field-user`): hook suite `before` men-set flag itu true untuk setiap akun aktor yang dipakai spec dalam suite (nilai awal tiap akun dicatat) supaya walkthrough otomatis tidak menutupi layar, dan hook suite `after` memulihkan nilai awal. Mekanisme penyetelan flag disediakan tim FE/BE. Spec 005 dan 006 menguji flag itu sendiri (akun First Visit A sampai E) sehingga akun First Visit dikecualikan dari penyetelan dan flag-nya ditulis di `## Prerequisites` kedua spec itu; tiap spec lain memuat satu baris rujukan ke pernyataan ini.
- **Population:** hook `before` men-seed 14 field awal Client A secara idempotent (dilewati bila sudah ada): 6 field Pre-setup (`Cost Center`, `Employee Grade`, `Job Description`, `Bonus`, `Office Phone`, `Joining Date`, hanya dibaca) dan 8 field Population D-01 (`Blood Type`, `Shirt Size`, `Emergency Phone`, `Birth Date`, `Tax ID`, `Work Notes`, `Annual Target`, `badge number`). Nama Population literal tanpa suffix karena asersi urutan A-Z dan jumlah 14. Field Pre-setup hanya dibaca dan tidak diubah atau dihapus spec mana pun. Field Population di-seed per spec secara idempotent dan dihapus hanya oleh spec yang membuatnya di hook `after` (spec 001, 002, 003, 007, dan 018; spec 018 membangun Population lewat UI untuk TC-GS-UCF-1 dan menghapus sisanya di `before`). Mekanisme seeding disediakan tim FE/BE.
- **Field sisa Client A:** hook `before` suite menghapus lewat API field Client A sisa run sebelumnya, yaitu field bersuffix `{runId}` dan field non-Pre-setup, non-Population yang tidak dimiliki spec mana pun, supaya asersi "tepat 14 field" tidak bergantung pada kebersihan run sebelumnya. Mekanisme penghapusan disediakan tim FE/BE.
- **D-158 (Custom Field Required Yes):** hook `before` suite Client A menonaktifkan atau menghapus lewat API setiap Custom Field Required Yes berstatus Active selain `Cost Center`, `Office Phone`, dan `Tax ID` (kondisi D-158), sebelum spec Form User berjalan, dan mencatat status awal tiap field yang diubah. Hook `after` suite memulihkan field yang dinonaktifkan ke status awal (field yang dihapus dibuat ulang dengan atribut yang tercatat). Spec yang membuat field Required Yes sendiri tetap menghapusnya di hook `after` spec itu; spec Form User (021 sampai 025, 026, 041, 042, 044) merujuk butir ini sebagai jaminan D-158. Mekanisme penonaktifan, penghapusan, dan pemulihan disediakan tim FE/BE.
- **Cleanup:** tiap spec menyiapkan dan membersihkan data miliknya sendiri lewat hook (`before` dan `after`), data bernama bersuffix `{runId}-<NNN>`. Hook `after` menghapus data `{runId}` sisa yang dibuat spec dan memulihkan state global yang diubahnya (capability role, format tanggal, limit, flag Guided Tooltip).

Setiap spec tetap menyiapkan dan membersihkan datanya sendiri dan tidak bergantung pada hasil spec lain. Layar awal dibuka oleh hook `beforeEach` per spec sesuai `## Prerequisites` masing-masing.
