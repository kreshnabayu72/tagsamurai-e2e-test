---
name: Admin Console Settings Role Permission
id: suite-admin-console-settings-role-permission
description: Spec e2e turunan tc-settings-role-permission.md untuk Admin Console > Settings > Role & Permission
executionOrder: 1.1
parallel: false
---

# Suite: Admin Console Settings Role Permission

Suite ini mencakup halaman Settings > Role & Permission pada Admin Console untuk entitas Principal, Distributor, dan Partner (Client tanpa akses): Tab Total Control, Read Only, Group Manager (dengan sidebar Group Tree), dan System, Role Detail Global Role dan Group Role, Approvers Section dan Approval Settings. Cakupan: screening, Role Matrix (akses menu, visibilitas elemen, gating checkbox CRUD dan Remove), Assign dan Remove Total Control, Read Only, Group Manager, Assign User to Role, Edit CRUD autosave dan auto-revert, Remove baris dan Bulk Remove, Additional Approver, toggle Require Approval, Table User Picker, Search, Filter, Sort, Setup Column, Pagination, Download, Modal Changelog, pencatatan Changelog, System Log, dan Activity Log, notifikasi in-app (DEFERRED), sinkronisasi dengan Settings > User dan Settings > Group, modul konsumen (Device Allocation, Approvals, Wallet), defense-in-depth, state tenant (Suspended dan Expired), target berubah atau hilang sejak render, konkurensi, ketahanan terhadap kegagalan server, serta tampilan mobile Android.

`parallel: false` karena spec mengubah state yang dipakai bersama: tingkat akses dan penugasan user Pre-setup (Total Control, Read Only, Group Manager, peran individual), approver dan toggle Require Approval per group, Selection Limit, status entitas (Suspended, Expired), flag Guided Tooltip, dan perangkat Android bersama. Setiap spec tetap menyiapkan dan memulihkan datanya sendiri lewat hook dan tidak bergantung pada hasil spec lain.

## Hook suite

- `before`: login akun aktor pertama spec (akun dan env dibaca dari `## Prerequisites` spec); `after` mengembalikan sesi ke akun default suite (Siti Nurhaliza, Total Control Principal). `beforeEach` membuka halaman `Settings > Role & Permission`, kecuali untuk spec 021 yang aktornya akun Client tanpa akses halaman itu (spec dimulai dari landing Admin Console).
- Flag Guided Tooltip `guided_tooltip_seen_role-permission`: hook `before` suite menyetel flag `true` untuk akun aktor yang dipakai suite dan hook `after` memulihkannya. Spec Guided Tooltip mengatur flag sendiri sesudah hook. `## Prerequisites` spec lain merujuk pernyataan ini dengan satu baris. Kemampuan membaca dan menyetel flag disediakan tim FE/BE.
- Pemulihan baseline automation: data Pre-setup yang diubah spec (tingkat akses, penugasan GM, approver, toggle; group Pre-setup beserta rename atau hapus group, penugasan GM, approver, toggle, dan penempatan entitas; pemindahan entitas antar group; Activation Status atau status aktif user) dipulihkan ke kondisi Tabel Data Uji Pre-setup TC lewat kemampuan reset yang disediakan tim FE/BE, dijalankan di hook `before` dan `after` spec yang mengubahnya serta sebagai langkah penghubung antar blok TC; efek pada Last Updated dan audit trail dicatat di `## Prerequisites` spec. Pengecualian S-06 diterima untuk data Pre-setup ini karena TC menguji tepat group, user, dan penugasan Pre-setup bernama literal yang sudah terhubung ke data lain di tenant, sehingga tidak dapat digantikan data Dinamis milik spec; pemulihannya hanya lewat kemampuan reset ini.
- Baca jumlah entri audit trail: kemampuan membaca jumlah entri Changelog dan log (System Log, Activity Log, Changelog: User) pada surface yang disebut spec, dipakai mencatat baseline sebelum aksi dan mengasersi selisih sesudahnya tanpa angka absolut (S-12). Dipakai spec yang mencatat baseline jumlah entri, lihat `## Prerequisites` spec. Kemampuan disediakan tim FE.
- Pemulihan Setup Column: spec yang menyimpan konfigurasi kolom menghapus preferensi kolom di browser pada hook `after` (bukan `[Reset to Default]`); kemampuan disediakan tim FE.
- Sesi API aktor: login API (password) untuk akun yang sama dengan sesi UI memakai token yang tidak dihitung sebagai sesi web; dipakai untuk aksi Admin B yang hanya memicu perubahan state dan untuk request langsung spec defense-in-depth. Kemampuan disediakan tim BE/FE.
