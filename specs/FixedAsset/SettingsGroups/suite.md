---
name: Fixed Asset Settings Groups
id: suite-fixed-asset-settings-groups
description: Spec e2e turunan tc-settings-groups.md untuk Fixed Asset > Settings > Groups
executionOrder: 1.0
parallel: false
---

# Suite: Fixed Asset Settings Groups

Suite ini mencakup halaman Fixed Asset > Settings > Groups: Groups List (Sidebar Group Tree, Group Context Header, Search, Filter, Sort, Pagination, Setup Column, Download), Create Group dan Create Subgroup, Edit Group (termasuk Dialog Change Function), Delete dan Bulk Delete, Popup Detail Group (Tab Assets dan Tab Users), Modal Changelog, Wizard dan Alert Group Consolidation, Code auto-generate, Role Matrix (Total Control, Default User, Read Only, Group Manager, Manage Group), Guided Tooltip, pencatatan Changelog, System Log, dan Activity Log, sinkronisasi lintas modul, plan gating dan state tenant, defense-in-depth, ketahanan terhadap kegagalan server, konflik antar admin, serta tampilan mobile Android.

`parallel: false` karena spec mengubah state global dan data yang dipakai bersama: plan tier dan downgrade terjadwal, Master Data Count Limit, Hierarchy Depth Limit, dan Selection Limit, status Client (Suspended, Expired), lisensi FA-7, format tanggal dan Time Zone General Settings, flag Guided Tooltip, serta pohon group Pre-setup (Tabel A). Spec yang menghapus data (Delete, Bulk Delete) dijalankan sesudah spec lain. Setiap spec tetap menyiapkan dan membersihkan datanya sendiri lewat hook dan tidak bergantung pada hasil spec lain.

## Hook suite

- `before`: login akun aktor default suite (Total Control, Pre-setup No 1, `Spectra.env.FA_TC_PASSWORD`; nama env baru yang didaftarkan penulis spec di `executionConfig.environmentVariables` dan `.env.example`) dan menyetel flag Guided Tooltip `fa-settings-groups` menjadi `seen` untuk akun aktor yang dipakai suite, supaya walkthrough otomatis tidak menutupi layar. Mekanisme penyetelan dan pemulihan flag disediakan tim FE/BE. Spec Guided Tooltip (012, 013) dan spec 019 (TC-40) mengatur flag sendiri sesudah hook ini.
- `after`: memulihkan flag Guided Tooltip ke nilai awal tiap akun, memulihkan preferensi kolom Setup Column (Groups List dan Tab Users/Assets) dan preferensi sidebar yang tersimpan di browser ke bawaan (konvensi bagian 4), lalu mengembalikan sesi ke akun default suite.
- `beforeEach`: membuka Fixed Asset > Settings > Groups untuk akun yang sedang login. Spec 017 (role tanpa akses, ditolak server) membuka Dashboard lebih dulu pada langkah awalnya dan tidak bergantung pada hook ini.
- Sesi API aktor: login API (password) untuk akun yang sama dengan sesi UI memakai token yang tidak dihitung sebagai sesi web (bagian 5 konvensi); kemampuan ini, klien HTTP untuk request langsung ke server, dan fixture BE (membaca/mengembalikan state data, status Client, plan, limit platform, hook uji T-0, penulisan Activity Log yang disimulasikan gagal) disediakan tim FE/BE tanpa endpoint karangan. Aksi pelaku kedua yang hanya memicu perubahan state memakai sesi API; sesi UI kedua dipakai hanya bila hasil di sesi itu diasersi (P-2).
- Pemulihan state global (plan, limit platform, Selection Limit, General Settings, status Client, lisensi) dilakukan di hook `after` spec yang mengubahnya. Pohon group Pre-setup (Tabel A) dibaca; fixture "Pre-setup tambahan" (Edit Target, Del Empty, Bulk E1..E16, dan seterusnya) di-seed per spec lewat API di `before` dan dibersihkan di `after`; Value Gate Node A/B/Child (spec 253-268) adalah Pre-setup literal bersama yang hanya dibaca. Custom Field User untuk spec Tab Users (165, 170, 171, 178, 179, 185) di-seed per spec bersuffix `{runId}` dan dihapus di `after`; pemulihan Disposal Yard (spec 058, 071) lewat fixture BE di `after` spec tersebut; pemulihan reader dan kuota pada spec 204 di `after`.
- `## Prerequisites` tiap spec merujuk hook ini dengan satu baris dan tidak menulis ulang isinya. Spec mobile (014, 089) memakai perangkat Android yang disediakan tim FE dan tidak memakai hook web ini.
