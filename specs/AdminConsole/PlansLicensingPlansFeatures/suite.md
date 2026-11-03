---
name: Admin Console Plans Licensing Plans Features
id: suite-admin-console-plans-licensing-plans-features
description: Spec e2e turunan tc-plans-licensing-plans-features.md untuk Admin Console > Plans & Licensing > Plans & Features
executionOrder: 1.0
parallel: false
---

# Suite: Admin Console Plans Licensing Plans Features

Suite ini mencakup halaman Plans & Licensing > Plans & Features: Plans List (tab Default dan Custom, sub-tab Active dan Archive; Search, Filter, Sort, Pagination, Setup Column, Download), Plan Detail (Tab Overview dan Tab Assigned Clients), Create dan Edit Custom Plan serta Default Plan, Archive, Delete, Push Update per client, tab Global Settings (Global FAMS Settings), tiga modal Changelog (Default, Custom, Global Settings), Guided Tooltip, Role Matrix, scope data per entitas dan masking Group Role, pencatatan log di tiga surface, efek lintas modul, defense-in-depth sisi server, konkurensi dua admin, aksesibilitas, serta ketahanan terhadap kegagalan server.

`parallel: false` karena spec memakai state global bersama: Dataset Pre-setup default plan (slot Free dan Paid per Product terbatas sehingga tidak dapat dimiliki satu spec), Dataset E yang mengosongkan tenant, Global FAMS Settings (singleton), format tanggal, zona waktu, dan format jam General Settings, flag Guided Tooltip, status entitas aktor, serta capability role. Spec yang mengubah Pre-setup bersama (Archive dan Delete default plan, Edit Growth, Edit Starter, Push Update) memulihkannya ke keadaan awal lewat fixture backend yang disediakan tim FE/BE (idempoten), dijalankan di hook `before` dan `after` spec serta sebagai langkah penghubung antar blok TC; efeknya (Last Updated dan entri Changelog) dicatat di `## Prerequisites` spec yang bersangkutan. Spec yang menghapus data dan spec yang mengosongkan tenant (Dataset E) dijalankan sesudah spec lain.

Hook suite `beforeEach` membuka halaman Plans & Licensing > Plans & Features sesudah akun aktor pertama login di hook `before` tiap spec. Hook suite juga menjadi jaring pengaman dengan mengonfirmasi dialog `beforeunload` dan menutup dialog `Unsaved Changes` bila masih terbuka; itu bukan pengganti langkah pemulihan form dirty di spec.

Sesi API aktor: login API (password) untuk akun aktor yang sama dengan sesi UI memakai token yang tidak dihitung sebagai sesi web, sehingga batas satu sesi web tidak terpengaruh dan sesi UI tidak diusir. Kemampuan itu, klien HTTP untuk request langsung ke server, fixture backend (pemulihan Dataset Pre-setup, status entitas aktor, akun dihapus atau dinonaktifkan, flag Guided Tooltip, pengaturan General Settings, dan state client Expired, Suspended, serta term Trial) disediakan tim FE/BE; `## Prerequisites` spec merujuknya dengan satu baris.

Flag Guided Tooltip halaman ini (`guided_tooltip_seen_ac-plans-features`): hook suite `before` men-set flag itu true untuk setiap akun aktor pre-setup (nilai awal dicatat) supaya tur tidak menutupi layar, dan hook suite `after` memulihkan nilai awal. Spec Guided Tooltip memakai akun tanpa flag dan menulis kebutuhan itu di `## Prerequisites`-nya sendiri; tiap spec lain memuat satu baris rujukan ke pernyataan ini.

Password akun aktor memakai env var `<APP>_<ROLE>_PASSWORD` (bagian 5 konvensi): Total Control Principal `AC_TC_PASSWORD`; akun lain memakai nama berkode modul `AC_PF_<ROLE>_PASSWORD` yang didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`.

Setiap spec tetap menyiapkan dan membersihkan datanya sendiri lewat hook dan tidak bergantung pada hasil spec lain.

Preferensi Setup Column: spec yang mengubah atau menyimpan konfigurasi kolom Plans List (Setup Column, Unpin, Apply) mengembalikannya ke default di hook `after` spec itu lewat penghapusan preferensi kolom akun aktor pada browser, kemampuan yang disediakan tim FE; `## Prerequisites` spec merujuknya dengan satu baris.
