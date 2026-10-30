---
name: Global Settings Role
id: suite-global-settings-role
description: Spec e2e turunan tc-role.md untuk Global Settings > Role & Permission
executionOrder: 1.6
parallel: false
---

# Suite: Global Settings Role

Suite ini mencakup halaman Role & Permission pada Global Settings: Tab Total Control, Tab Read Only, Tab System, dan Detail role (Import data, Manage files, Manage hardware, Manage master reference, Manage TAG, Manage user and role). Cakupan: screening, Role Matrix, Popup Assign (Total Control, Read Only, Role), Assign dan Remove access level, Edit CRUD dan Auto-Revert, Remove baris role dan Bulk Remove, Search, Filter, Sort, Pagination, Setup Column, Download, Modal Changelog, pencatatan Changelog, System Log aktor, dan Activity Log, sinkronisasi dengan modul User dan sidebar target, cascade Remove Access Global Settings, notifikasi in-app, Guided Tooltip, state tenant (Client Suspended), defense-in-depth, ketahanan terhadap kegagalan server, konflik antar admin, serta tampilan mobile Android.

`parallel: false` karena spec mengubah state yang dipakai bersama (access level dan baris role user Pre-setup, flag Guided Tooltip, format tanggal General Settings, batas Selection Limit, status Client). Spec yang menghapus data atau mencabut access level dijalankan sesudah spec lain. Setiap spec tetap menyiapkan dan membersihkan datanya sendiri lewat hook dan tidak bergantung pada hasil spec lain.

## Hook suite

- Flag Guided Tooltip `guided_tooltip_seen_gs-role`: hook `before` suite mencatat nilai awal flag lalu menyetelnya `seen` (true) untuk akun aktor yang dipakai suite, dan hook `after` memulihkan nilai awal. Hook ini berlaku untuk setiap akun UI yang dipakai suite, termasuk akun admin kedua, akun target pada spec sinkronisasi, dan akun entitas lain (mis. Client C). Spec yang menguji Guided Tooltip (010, 011) mengatur flag sendiri sesudah hook dan menjelaskan mekanismenya di `## Prerequisites`. `## Prerequisites` spec lain merujuk pernyataan ini dengan satu baris. Kemampuan membaca dan menyetel flag disediakan tim FE/BE. Spec mobile (012, 013, 014) dan spec `Mode: mock` (seluruh API di-mock, tanpa backend untuk hook ini) tidak memakai hook ini; spec mock mengatur flag lewat respons mock yang tertulis di Prerequisites-nya.
- Pre-setup bersama (Ahmad Fauzi, Budi Santoso, Siti Nurhaliza, Rina Putri, Doni Pratama, Agus Salim, Wawan Setiawan, Nina Kartika, dan kandidat fixture Pre-setup #18) dipulihkan ke kondisi Tabel Data Uji Pre-setup TC oleh spec yang mengubahnya (Given di hook `before`, pemulihan di hook `after`), mengikuti catatan "Reset Pre-setup per TC" di `tc-role.md`.
- Admin kedua (Eko Prasetyo, Total Control) memakai env `GS_TC2_PASSWORD`. Aksi admin kedua yang hanya memicu perubahan state memakai sesi API; sesi UI kedua dipakai hanya bila hasil di sesi itu diasersi (P-2, `[KEPUTUSAN 2026-10-21]`).
