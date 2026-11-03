---
name: Global Settings Non-Login User
id: suite-global-settings-non-login-user
description: Spec e2e turunan tc-non-login-user.md untuk Global Settings > User > User List > sub-tab Non-Login User
executionOrder: 1.0
parallel: false
---

# Suite: Global Settings Non-Login User

Suite ini mencakup sub-tab Non-Login User pada Global Settings > User > User List: tabel (Search, Filter, Sort, Pagination, Setup Column, Download), Create, Popup Select User (Represented By), Edit, Delete, Toggle Active dan Reactivate Temporary User, Bulk Action (Activate, Deactivate, Convert to Login User), Convert to Login User, halaman Detail (General Information, Tab Changelog, Tab Responsibilities dengan sub-tab Borrowed Assets dan Assigned Assets), Modal Changelog agregat, Role Matrix per capability, Guided Tooltip, pencatatan log di tiga surface (Changelog, Activity Log, System Log aktor), sinkronisasi dengan Login User, master data, Custom Field, Import, dan Fixed Asset, batas Storage, Master Data Count Limit dan Selection Limit, state tenant (Suspended, Expired, plan), konkurensi dua admin, serta ketahanan terhadap kegagalan server.

`parallel: false` karena spec mengubah state global (plan dan status Client, format tanggal General Settings, capability role, flag Guided Tooltip, Master Data Count Limit dan Selection Limit di Admin Console, status Custom Field). Setiap spec tetap menyiapkan dan membersihkan datanya sendiri lewat hook dan tidak bergantung pada hasil spec lain.

## Hook suite

- **Login:** hook `before` tiap spec login sekali sebagai akun aktor pertama spec itu (akun dan env var dibaca dari `## Prerequisites`; password lewat `Spectra.env.*`, tidak ditulis di spec atau fixture), dan hook `after` mengembalikan sesi ke akun default suite (Total Control, `GS_TC_PASSWORD`). Halaman awal (Global Settings > User > User List > sub-tab Non-Login User) dibuka hook `beforeEach`. Langkah login di `## Test Steps` hanya untuk ganti akun.
- **Guided Tooltip:** flag `guided_tooltip_seen_gs-non-login-user`: hook suite `before` men-set flag itu true untuk setiap akun aktor yang dipakai spec dalam suite (nilai awal tiap akun dicatat) supaya walkthrough otomatis tidak menutupi layar, dan hook suite `after` memulihkan nilai awal. Mekanisme penyetelan flag disediakan tim FE/BE. Spec 006 dan 007 menguji flag itu sendiri (akun First Visit) sehingga dikecualikan dan menulis pengaturan flag-nya di `## Prerequisites` masing-masing; tiap spec lain memuat satu baris rujukan ke pernyataan ini.
- **Sesi API aktor:** login API (password) untuk akun yang sama dengan sesi UI memakai token yang tidak dihitung sebagai sesi web, sehingga sesi UI tidak diusir. Kemampuan itu disediakan tim BE/FE; pelaku kedua yang hanya memicu perubahan state (menghapus, meng-Convert, membuat Login User) memakai sesi API ini, dan `## Prerequisites` spec merujuknya dengan satu baris.
- **Pre-setup:** data Pre-setup No. 9 sampai 13 (Position, Division, pool Login User Represented By, Non-Login User dasar, Custom Field dasar Blood Type, Emergency Phone, Badge Note) hanya dibaca dan tidak diubah atau dihapus spec mana pun. Target aksi tulis atau hapus selalu data milik spec (Non-Login User bersuffix `{runId}-<NNN>`) yang di-seed hook `before` lewat API dan dibersihkan hook `after`. Mekanisme seeding dan penghapusan disediakan tim FE/BE.
- **Setup Column:** spec yang menyimpan konfigurasi kolom (039, 040, 077, 079, 082, 083, 084, 085, 088, 093, 094, 097, 098, 102, 103, 105, 106, 107, 129) memulihkannya di hook `after` dengan menghapus preferensi kolom di browser, bukan `[Reset to Default]`; kemampuan disediakan tim FE.
- **Custom Field uji:** Custom Field khusus uji (Blood Type Uji, Emergency Phone Uji, Badge Note Uji, Badge Required, Skor Uji, Tanggal Uji) dibuat dan diaktifkan hook `before` spec yang memakainya lalu dinonaktifkan atau dihapus di hook `after`, sehingga spec lain hanya melihat tiga field dasar.
- **State global:** spec yang mengubah format tanggal General Settings, Master Data Count Limit, Selection Limit, Storage client, atau capability role menulis pengaturan awal dan pemulihannya di `## Prerequisites` dan memulihkannya di hook `after`. Akun pelaku perubahan limit, plan, dan Storage tidak disebut TC, PRD, atau LLD sehingga ditulis 'disediakan tim FE'.
- **Cleanup:** hook `after` menghapus data `{runId}` sisa yang dibuat spec dan memulihkan state global yang diubahnya.

Layar awal dibuka oleh hook `beforeEach` per spec sesuai `## Prerequisites` masing-masing.
