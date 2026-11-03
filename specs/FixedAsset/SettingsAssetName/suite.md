---
name: Fixed Asset Settings Asset Name
id: suite-fixed-asset-settings-asset-name
description: Spec e2e turunan tc-settings-asset-name.md untuk Fixed Asset > Settings > Asset Master > Asset Name
executionOrder: 1.0
parallel: false
---

# Suite: Fixed Asset Settings Asset Name

Suite ini mencakup tab Asset Name pada Fixed Asset > Settings > Asset Master: tabel utama (Search, Filter, Sort, Pagination, Setup Column, Download, notice dan quick filter Category Locked), Create, Edit beserta dialog dampak (Change Category, TAG Type, Default Addon, Default Label), Delete single dan Bulk Delete, Popup Detail (tab Models per Brand, Linked Custom Fields, Total Assets, progres kepatuhan TAG Type), Modal Tree Picker, Code auto-generate, Modal Changelog, pencatatan log di Changelog, System Log, dan Activity Log, Role Matrix, Asset Name excess pada client downgrade, sinkronisasi lintas modul, defense-in-depth, state tenant, ketahanan terhadap kegagalan server, konflik antar sesi, dan tampilan mobile.

`parallel: false` karena spec mengubah state global (System Limits Selection Limit dan Master Data Count Limit, plan dan status client, Time Zone dan format tanggal General Settings, counter rate limit, jam server) dan men-seed katalog Asset Name yang tampil di tabel bersama. Setiap spec tetap menyiapkan dan membersihkan datanya sendiri lewat hook dan tidak bergantung pada hasil spec lain.

## Hook suite

- `before`: login akun aktor default suite (Total Control, `Spectra.env.FA_TC_PASSWORD`) lewat `seedSession`. Spec yang memakai akun aktor lain login akun aktor pertamanya di `before` spec itu (akun dibaca dari `## Prerequisites`) dan hook `after` mengembalikan sesi ke akun default suite.
- `beforeEach`: membuka Fixed Asset > Settings > Asset Master > Asset Name (tab default); spec yang tidak menguji navigasi tidak mengulang langkah buka di `## Test Steps`.
- `after`: membersihkan data milik spec dan memulihkan state global yang diubah spec (System Limits, Master Data Count Limit, plan dan status client, Time Zone dan format tanggal General Settings, counter rate limit).
- Sesi API aktor: login API (password) untuk akun yang sama dengan sesi UI memakai token yang tidak dihitung sebagai sesi web; kemampuan ini disediakan tim BE/FE. `## Prerequisites` spec merujuknya dengan satu baris.
- Seed API per TC: salinan fixture bernama unik per TC (Tabel Data Uji Dinamis) dan client salinan (`Downgrade Client NNN`) disediakan lewat seed API oleh tim BE/FE. `## Prerequisites` spec menyebut salinan yang dipakai.
- Pemulihan konfigurasi kolom Setup Column: hapus preferensi kolom di browser (bukan `[Reset to Default]`); kemampuan disediakan tim FE. Spec penyimpan konfigurasi kolom pada suite ini (nomor spec): 114, 125-132, 142, 145, 146, 148, 151-155, 161-163, 166-209, 211, 226.
- Seed reset fixture bersama: fixture yang tidak dapat digandakan (Pre-setup #10 `Dell Latitude`, #12 `MacBook Pro`, #14r, #14s, #14u, #16c) dipulihkan lewat seed reset BE/FE (pengecualian S-06, 2026-10-30). Spec terdampak: 064, 073, 075, 078-082, 085, 086, 090, 221, 228, 240, 242, 245.
- Pemulihan client Pre-setup #12e-#12g yang diubah spec 139 dilakukan di hook `after` spec itu lewat seed reset.
- `## Prerequisites` tiap spec merujuk hook ini dengan satu baris dan tidak menulis ulang isinya.
