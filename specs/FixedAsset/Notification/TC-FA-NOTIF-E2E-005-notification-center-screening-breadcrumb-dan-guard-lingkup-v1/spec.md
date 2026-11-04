---
id: TC-FA-NOTIF-E2E-005-notification-center-screening-breadcrumb-dan-guard-lingkup-v1
title: "Notification Center: Screening, Breadcrumb, dan Guard Lingkup V1"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-NOTIF-20
  - TC-FA-NOTIF-21
  - TC-FA-NOTIF-22
  - TC-FA-NOTIF-29
  - TC-FA-NOTIF-30
  - TC-FA-NOTIF-31
coverage:
  web: automated
---

# Notification Center: Screening, Breadcrumb, dan Guard Lingkup V1

## Prerequisites

- Mode: FE+BE. Platform: web, Fixed Asset > Dashboard, Dropdown Panel, dan Notification Center.
- Akun aktor: Total Control Pre-setup #1 (`totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`; nama env usulan, belum terdaftar di `executionConfig.environmentVariables` dan `.env.example`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Data: seed notifikasi N-01 sampai N-07 (Pre-setup #17) milik akun aktor: N-01 dan N-02 Unread actionable, N-03, N-04, N-05 Unread view-only, N-06 Read view-only, N-07 Read actionable. Spec hanya membaca data; fixture BE pemulih seed dijalankan di hook `before` dan `after`. Nilai dibaca dari `Fixture.fixedAssetNotification.<kunci>`; fixture `fixtures/fixedAssetNotification.json` belum ada dan disediakan tim FE.
- Hook suite yang berlaku (rujukan ke `suite.md`): flag Guided Tooltip (akun #1 sudah true) dan fixture BE pemulih seed notifikasi.

## Test Steps

### TC-FA-NOTIF-31: Guard lingkup V1: tidak ada halaman kelola notifikasi atau pengaturan preferensi

1. Verifikasi item menu `Dashboard` tampil pada sidebar FAMS
2. Verifikasi sidebar tidak memuat menu atau halaman untuk mengelola notifikasi, mengirim broadcast, atau mengatur preferensi/mute notifikasi
3. Klik Bell icon
4. Verifikasi Dropdown Panel tampil dengan Header `Notifications`
5. Verifikasi Dropdown Panel tidak memuat kontrol untuk mengelola notifikasi, mengirim broadcast, atau mengatur preferensi/mute notifikasi

### TC-FA-NOTIF-20: Dropdown Panel: [Show All] membuka Notification Center

6. Klik `[Show All]`
7. Verifikasi halaman Notification Center terbuka
8. Verifikasi Breadcrumb `Notification Center`

### TC-FA-NOTIF-31 (lanjutan): Notification Center

9. Verifikasi Notification Center tidak memuat kontrol untuk mengelola notifikasi, mengirim broadcast, atau mengatur preferensi/mute notifikasi
10. Verifikasi hanya Bell icon, Dropdown Panel, dan Notification Center yang tersedia sebagai permukaan notifikasi

### TC-FA-NOTIF-21: Screening Notification Center: Header, Body, Footer

11. Verifikasi Header memuat Breadcrumb `Notification Center`
12. Verifikasi Header memuat Tab `All` (aktif) dan `Unread`
13. Verifikasi Header memuat Table Tools `Search | Filter | Sort Newest`
14. Verifikasi Body berupa list kartu item berurutan terbaru ke terlama (N-01 sampai N-07)
15. Verifikasi tiap item menampilkan icon, Title, Body, timestamp relatif, dan dot
16. Verifikasi tombol `[Mark as Read]` tampil pada item view-only Unread, tombol `[Detail]` tampil pada item actionable Unread, dan item Read tanpa tombol
17. Verifikasi Footer tidak memuat pagination bernomor dan tidak memuat `[Load More]`

### TC-FA-NOTIF-22: Breadcrumb Notification Center satu segmen dan tidak dapat diklik

18. Verifikasi Breadcrumb hanya satu segmen `Notification Center` sebagai label statis
19. Klik teks Breadcrumb `Notification Center`
20. Verifikasi klik tidak memicu navigasi dan halaman tetap Notification Center

### TC-FA-NOTIF-29: Guard Toolbar Notification Center: tidak ada Download, Changelog, Column Visibility

21. Verifikasi Table Tools hanya memuat Search, Filter, dan toggle Sort `Newest`
22. Verifikasi tidak ada icon Download, icon Changelog, maupun trigger Column Visibility `(⋯)`

### TC-FA-NOTIF-30: Guard Notification Center: tidak ada Mark All as Read dan kolom checkbox

23. Verifikasi tombol `[Mark as Read]` tampil pada item N-03 (item view-only Unread)
24. Verifikasi tidak ada kontrol `Mark All as Read`
25. Verifikasi tidak ada checkbox seleksi pada setiap item

## Notes

- Sumber: `fixed-asset/notification/TestCases/tc-notification.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Urutan blok: TC-31 (bagian sidebar dan Dropdown Panel) dan TC-20 di awal karena keduanya berangkat dari Fixed Asset > Dashboard; TC-31 bagian Notification Center (langkah 9 dan 10) memakai halaman yang dibuka TC-20; TC-21, 22, 29, 30 memakai halaman yang sama tanpa membukanya lagi (langkah "Buka Notification Center" tiap TC itu sudah terpenuhi oleh langkah 6). Urutan menyimpang dari urutan nomor TC.
- Asersi tambahan sebagai anchor positif (S-03; 8b butir 2): langkah 1 (item menu `Dashboard` sebelum asersi absence menu), langkah 4 (Header Dropdown Panel sebelum asersi absence kontrol), langkah 8 (Breadcrumb sebelum asersi absence di Notification Center), langkah 21 (Table Tools yang tampil sebelum asersi absence icon, sesuai anchor positif pada Expected TC-29), langkah 23 (tombol `[Mark as Read]` sebelum asersi absence kontrol, sesuai anchor positif pada Expected TC-30). Urutan asersi TC-30 menyimpang dari Expected TC (butir b sebelum butir a) karena alasan yang sama.
- Langkah 21 dan 22 adalah asersi absence elemen UI (TC-29), bukan absence log.
- Temuan untuk QA:
  - TC-31 tidak menyebut menu sidebar yang dipakai sebagai pembanding asersi absence; spec memakai item `Dashboard` karena pengguna berada di Fixed Asset > Dashboard.
