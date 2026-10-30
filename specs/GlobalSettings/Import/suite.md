---
name: Global Settings Import
id: suite-global-settings-import
description: Spec e2e turunan tc-import.md untuk Global Settings > Import
executionOrder: 1.0
parallel: false
---

# Suite: Global Settings Import

Suite ini mencakup halaman Import pada Global Settings: layar awal dan state belum ada draft, Unsaved Banner, Guided Tooltip, rute per tab, akses role dan capability, Upload dan Column Mapping, validasi berkas dan sel, Staging Table (Metric Cards, Callout, Edit, Duplicate, Remove, Bulk Delete, Append, Discard), sesi edit dan kunci, saran AI (Field Shortening dan Reference Suggestion), Create Missing, commit dan notifikasi, Download Template, Changelog, pencatatan log, Custom Field, plan gating dan status tenant, batas Master Data Count Limit dan Selection Limit, konkurensi dua admin, ketahanan terhadap kegagalan server, serta Android.

`parallel: false` karena spec mengubah state global: jam server dan hook umur draft, kontrol worker commit, mode mock layanan AI, plan dan status Client, flag Guided Tooltip `gs-import`, seed Master Data Count Limit dan Selection Limit, serta Custom Field Client A dan C. Draft Import dibagikan ke seluruh admin satu client sehingga dua spec pada client yang sama tidak boleh berjalan bersamaan. Spec yang menghapus data atau menjalankan commit dijalankan sesudah spec lain.

Hook suite:

- `before`: men-set flag Guided Tooltip halaman Import (`guided_tooltip_seen_gs-import`) true untuk setiap akun aktor yang dipakai spec dalam suite, kecuali akun Total Control Tooltip Baru Client A (nilai awal tiap akun dicatat), supaya walkthrough otomatis tidak menutupi layar. Mekanisme penyetelan flag disediakan tim FE/BE. Spec yang menguji flag itu sendiri (akun Tooltip Baru dan Tooltip Selesai) menulis pengaturan flag-nya di `## Prerequisites` masing-masing; tiap spec lain memuat satu baris rujukan ke pernyataan ini.
- `after`: memulihkan nilai awal flag Guided Tooltip tiap akun dan mengembalikan sesi ke akun default suite (Total Control Client A).
- `beforeEach`: mereset client dan draft sesuai Kontrak Fixture R1 dan R2 `tc-import.md` (client bersih direset ke tanpa draft; draft dasar Client A dipulihkan ke kondisi Population; mutasi master data, Custom Field, dan produk organisasi dipulihkan ke kondisi Pre-setup). Skrip reset tidak didefinisikan di TC, PRD, atau LLD; mekanismenya disediakan tim FE/BE (S-13) dan dicatat di "Temuan untuk QA" tiap spec yang bergantung padanya, bukan sebagai endpoint karangan. Sesudah reset, hook membuka layar awal sesuai baris "Layar awal" di `## Prerequisites` tiap spec (termasuk sub-tab; tab bawaan adalah Brand; hook ini disediakan tim FE) pada Global Settings > Import untuk akun aktor spec. `beforeEach` hanya menyiapkan keadaan dasar tersebut; data lain yang dibutuhkan sebuah spec (draft selain draft dasar Client A, umur draft D-76, seed Changelog D-60, notifikasi, master data, mock layanan, status tenant) disiapkan oleh langkah pembuka eksplisit di `## Test Steps` spec itu dan tidak dititipkan ke hook `before`, karena `beforeEach` mereset client dan draft sesudahnya.

Sesi API aktor: login API (password) untuk akun yang sama dengan sesi UI memakai token yang tidak dihitung sebagai sesi web, sehingga sesi UI tidak diusir; pelaku kedua lewat sesi API bukan konteks kedua. Kemampuan ini disediakan tim BE/FE; `## Prerequisites` spec merujuknya dengan satu baris.

Spec yang menyimpan konfigurasi kolom Setup Column: spec 199 (Changelog Import dan Staging Table) dan spec 180 (modal Changelog). Pemulihannya di hook `after` adalah menghapus preferensi kolom di browser (kemampuan disediakan tim FE).

Skrip fixture (reset, pembuangan draft, pemulihan data, penyetelan umur draft, kontrol worker) berjalan sinkron: satu langkah fixture selesai sebelum langkah berikutnya dijalankan, sehingga spec tidak menulis penanda tunggu per langkah fixture. Sesudah reset fixture yang membuang atau mengganti draft, halaman yang sudah terbuka menampilkan keadaan lama; langkah berikutnya yang membutuhkan keadaan baru didahului "Muat ulang halaman ...".

Setiap spec tetap menyiapkan dan membersihkan datanya sendiri lewat hook dan tidak bergantung pada hasil spec lain.
