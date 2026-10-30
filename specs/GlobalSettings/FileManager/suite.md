---
name: Global Settings File Manager
id: suite-global-settings-file-manager
description: Spec e2e turunan tc-file-manager.md untuk Global Settings > File Manager
executionOrder: 1.7
parallel: false
---

# Suite: Global Settings File Manager

Suite ini mencakup halaman File Manager pada Global Settings: tabel utama File Manager (isi sel, Search, Filter, Sort, Pagination, Setup Column, Download CSV/XLSX), modal Recycle Bin dan modal Changelog, aksi Delete (single dan Bulk Delete), Permanently Delete (single dan bulk), Open File dan Download File di web, File Preview mobile (Android), kartu Storage Usage, pengaturan Lifecycle Settings (retensi, Selection Limit), auto-transition foto profil, auto-purge dan cascade purge, pencatatan log di tiga surface, Role Matrix per capability Manage files, state tenant (Suspended/Expired, plan tier), Guided Tooltip, ketahanan terhadap kegagalan server, serta request langsung dan isolasi Client.

`parallel: false` karena spec mengubah state global dan menghapus data. Setiap spec tetap men-seed dan membersihkan datanya sendiri lewat hook (seed idempotent per hook `before`) dan tidak bergantung pada hasil spec lain. Hitungan baris tetap ("33 records", 16 baris Recycle Bin) hanya valid bila suite berjalan serial dan dataset di-seed ulang per spec. Changelog tidak dapat di-seed ulang atau dibersihkan (audit trail permanen, tiap spec menambah entri), sehingga hitungan entri Changelog tidak diasersi sebagai total absolut (S-12): spec membatasi dengan Filter Date rentang Tabel A4 (`23/08/26` sampai `14/09/26`) atau memakai baseline sebelum dan sesudah aksi. Spec yang menghapus data (Delete, Bulk Delete, Permanently Delete, cascade purge) sebaiknya berjalan sesudah spec baca-saja bila runner mengikuti nomor spec; urutan itu belum terbukti.

## Hook Guided Tooltip

Hook `before` suite menyetel flag `guided_tooltip_seen_gs-file-manager` menjadi `true` agar walkthrough Guided Tooltip tidak menutupi layar spec lain; hook `after` memulihkan flag ke nilai semula. Pengecualian: spec 012 (TC-267, Guided Tooltip mobile) dan spec 070 (flag seen, replay, dan navigasi keluar) mengelola flag sendiri lewat API sesi akun aktor (menghapus flag sebelum asersi dan memulihkannya sesudahnya).

## State global yang dipulihkan hook `after`

- Lifecycle Settings: retensi Recycle Bin dan Selection Limit.
- General Settings: format tanggal.
- Client: status (Active/Suspended/Expired) dan tier plan (Starter, Growth, Professional, Enterprise).
- Jam (server dan browser/klien) bila spec mengaturnya.
- Capability role/akun (Manage files) yang diubah untuk spec konflik dan Role Matrix.
- Laporan Storage (kartu Storage Usage) dan kuota yang di-seed.
- Flag Guided Tooltip (lihat di atas) dan data bersufiks `{runId}-<NNN>` milik spec.

## Kemampuan teknis yang dibutuhkan (disediakan tim FE/BE)

Mekanisme dan endpoint tidak disebut di TC, PRD, maupun LLD yang dibaca tahap ini; spec menulisnya sebagai kemampuan dan tahap script wajib melengkapinya dari `openapi.yaml`.

- Seed 33 file aktif, Recycle Bin (16 baris), dan Changelog (14 entri Tabel A4 dengan tanggal tetap; entri baru dari spec lain tetap menumpuk dan tidak dibersihkan) secara idempotent di hook `before` tiap spec.
- Pemicu job auto-purge dan cascade purge, serta job dijeda atau jam dibekukan di environment e2e.
- Penyimpanan file tidak terjangkau (kegagalan soft-delete/storage), laporan Storage per app dan kuota, client uji tanpa data.
- Ubah Lifecycle Settings, format tanggal General Settings, status Client, tier plan, dan capability role lewat sesi API.
- Intercept jaringan (500, timeout, respons lambat) di atas backend nyata.
- Aplikasi Android (emulator atau perangkat) untuk spec mobile (010 sampai 012).
- Membaca berkas unduhan CSV/XLSX (BOM, sheet, tipe sel).
- Klien HTTP untuk request langsung ke server (spec 071) dan dua sesi (dua konteks browser atau sesi API).
- Akun klon milik spec (nama dan capability sama seperti aktor Pre-setup) dan akun Total Control pada client tanpa data.

## Kredensial

Password aktor lewat `Spectra.env`: `GS_TC_PASSWORD` (Total Control `totalControlGlobalSettings_automated_{namaCompany}`), `GS_RO_PASSWORD` (Read Only), `GS_FILES_READ_PASSWORD` (Manage files: Read), `GS_FILES_DELETE_PASSWORD` (Manage files: Delete), `GS_NOACCESS_PASSWORD` (tanpa akses File Manager), `GS_FILES_DELETE_CLONE_PASSWORD` (akun klon spec 008), `GS_TC_EMPTY_PASSWORD` (client tanpa data, spec 003). Didaftarkan di `spectra.config.ts` dan `.env.example`.
