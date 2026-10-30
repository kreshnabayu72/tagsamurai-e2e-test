---
name: Global Settings Division
id: suite-global-settings-division
description: Spec e2e turunan tc-division.md untuk Global Settings > User > Division
executionOrder: 1.4
parallel: false
---

# Suite: Global Settings Division

Suite ini mencakup tab Division pada Global Settings > User: tabel (Search, Filter, Sort, Pagination, Setup Column, Download), Create (validasi Name dan Code, auto-generate Code, Stay on this form, Master Data Count Limit), Edit, Delete single dan Bulk Delete (guard in-use, Selection Limit), Modal Changelog, Role Matrix, Guided Tooltip, pencatatan log di Changelog, Tab System Log aktor, dan Activity Log Global Settings, sinkronisasi ke form User, Non-Login User, dan Import, defense-in-depth, state tenant, ketahanan terhadap kegagalan server, konflik antar admin, serta tampilan mobile Android.

`parallel: false` karena spec mengubah state global (batas Master Data Count Limit dan Selection Limit, plan dan status Client, format tanggal General Settings, flag Guided Tooltip) dan men-seed Population D-02 dengan nama literal. Spec yang menghapus data (Delete, Bulk Delete) dijalankan sesudah spec lain. Setiap spec tetap menyiapkan dan membersihkan datanya sendiri lewat hook dan tidak bergantung pada hasil spec lain.

## Hook suite

- Flag Guided Tooltip `guided_tooltip_seen_gs-division`: hook `before` suite mencatat nilai awal flag lalu menyetelnya `seen` (true) untuk akun aktor yang dipakai suite, dan hook `after` memulihkan nilai awal. Hook ini berlaku untuk setiap akun UI yang dipakai suite, termasuk akun admin kedua dan akun entitas lain (mis. Client C); spec yang mengatur flag sendiri (001 sampai 010) menjelaskan mekanismenya di Prerequisites sendiri. Kemampuan membaca dan menyetel flag disediakan tim FE/BE. Spec yang menguji Guided Tooltip (004, 005, 006) dan spec yang sudah mengatur flag sendiri mengatur flag sesudah hook; `## Prerequisites` spec lain merujuk pernyataan ini dengan satu baris. Spec mobile (079, 080) dan spec `Mode: mock` (seluruh API di-mock, tanpa backend untuk hook ini) tidak memakai hook ini; spec mock mengatur flag lewat respons mock yang tertulis di Prerequisites-nya.
- Population D-02 (26 Division), D-03 (Name 120 karakter), dan Name literal penentu hasil auto-generate Code memakai nama literal (pengecualian S-12 `[KEPUTUSAN 2026-10-21]`): seeding idempotent di hook `before` spec yang membutuhkannya, spec 018 menghapus sisa Population lewat API lebih dulu, cleanup hanya menghapus yang dibuat spec itu, dan suite berjalan serial.
- Baris Pre-setup (`Finance`, `Human Resources`, `Legal`, `Operations`, `Compliance`, `Treasury`) tidak diubah atau dihapus spec mana pun; Last Updated keenamnya identik (Tabel Data Uji Pre-setup TC).
