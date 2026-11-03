---
id: TC-AC-PF-E2E-001-screening-plans-list-tab-default-dan-urutan-default
title: "Screening Plans List Tab Default Sub-tab Active dan Archive serta Urutan Default"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-PF-1
  - TC-AC-PF-2
  - TC-AC-PF-5
  - TC-AC-PF-6
coverage:
  web: automated
---

# Screening Plans List Tab Default Sub-tab Active dan Archive serta Urutan Default

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal `totalControlPrincipal_automated_{namaCompany}@qwertysystem.net` (nama tampil `Andi Wijaya`, Pre-setup #1), password dari `Spectra.env.AC_TC_PASSWORD` (akun default suite).
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Plans & Licensing > Plans & Features, Default > Active). Tidak ada ganti akun di tengah spec.
- Data awal (hook `before`): Dataset Plan A (Pre-setup #21): Default Active Starter, Growth, Professional, Enterprise, SIEM; Default Archive `Growth Plus (old)`; Custom Principal `Growth Tier` aktif dan `Enterprise Reseller` archived. Dataset Plan S (Pre-setup #31: `Supply Starter` Free, `Supply Pro` Paid, Product SAMS) dan Dataset Plan R (Pre-setup #30: `Plan Arsip Lama`, `Plan Arsip Tengah`, `Plan Arsip Baru`, Clients 0) ditambahkan oleh langkah penghubung sebelum blok TC yang memakainya. General Settings: Date Format `dd MMM yy`, Time Format 24-hour, Time Zone UTC (Pre-setup #44).
- Pengecualian S-06/S-12 butir A-14: nama Plan Pre-setup literal tanpa suffix (`Starter`, `Growth`, `Professional`, `Enterprise`, `SIEM`, `Supply Starter`, `Supply Pro`, `Plan Arsip Lama`, `Plan Arsip Tengah`, `Plan Arsip Baru`) dipakai karena menentukan asersi urutan, jumlah, dan teks; spec hanya membaca data itu dan tidak mengubahnya. Pemulihan semua Dataset ke keadaan awal lewat fixture BE yang idempoten (disediakan tim FE/BE) dijalankan di hook `before` dan `after` serta pada langkah penghubung; suite berjalan serial.
- Berkas `fixtures/plans-licensing-plans-features.json` belum ada; nilai data ditulis langsung pada langkah sampai tim FE menyediakannya.
- Flag Guided Tooltip halaman ini disetel true oleh hook `before` suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Kemampuan teknis: fixture BE (pemulihan dan penambahan Dataset Pre-setup) dan sesi API aktor, disediakan tim FE/BE (lihat `suite.md`).
- State global: Dataset Plan S dan Dataset Plan R yang ditambahkan spec ini dikembalikan ke baseline oleh hook `after` lewat fixture BE.
- Env var: hanya `Spectra.env.AC_TC_PASSWORD`; password tidak ditulis di spec atau fixture.

## Test Steps

### TC-AC-PF-1: Screening Plans List tab Default sub-tab Active saat Dataset Plan A tersedia

1. Klik menu Plans & Licensing > Plans & Features di sidebar
2. Susuri halaman dari atas ke bawah tanpa mengklik apa pun
3. Verifikasi Header: Breadcrumb `Plans & Licensing > Plans & Features > Default > Active`
4. Verifikasi Header: segmen pertama dan terakhir Breadcrumb statis, sedangkan `Plans & Features` dan `Default` dapat diklik
5. Verifikasi Header: Tab `Default (aktif) | Custom | Global Settings`
6. Verifikasi Header: Sub-tab `Active (aktif) | Archive`
7. Verifikasi Header: Table Tools `Search | Filter | Download | Changelog | [+ Default Plan]`
8. Verifikasi Body: kolom `Plan Name (sortable) | Product (sortable) | Pricing Type (sortable) | Version (sortable) | Clients (sortable) | Last Modified (sortable) | Column Visibility (⋯) (unsortable — header klik = buka Overlay Column Visibility, body per baris = row action menu)`
9. Verifikasi Body: baris berurutan dari atas `Starter` | `FAMS` | `Free` | `v2` | `12` | `15 Jun 26, 10:00`; `Growth` | `FAMS` | `Paid` | `v5` | `47` | `15 Jun 26, 10:00`; `Professional` | `FAMS` | `Paid` | `v3` | `23` | `15 Jun 26, 10:00`; `Enterprise` | `FAMS` | `Paid` | `v1` | `8` | `12 Aug 26, 09:00`; `SIEM` | `SIEM` | `Paid` | `v1` | `5` | `09 Jul 26, 11:00`
10. Verifikasi Body: tidak ada kolom Type, Status, Base Plan, maupun Rank, dan tidak ada kolom checkbox
11. Verifikasi Footer: teks `Showing 1–5 of 5 entries` dan `Rows per page: 10`
12. Verifikasi Footer: kontrol `Prev`, input nomor halaman, dan `Next`

### TC-AC-PF-2: Screening Plans List tab Default sub-tab Archive saat Dataset Plan A tersedia

13. Klik sub-tab Archive
14. Susuri halaman dari atas ke bawah tanpa mengklik apa pun
15. Verifikasi Header: Breadcrumb `Plans & Licensing > Plans & Features > Default > Archive`
16. Verifikasi Header: Tab `Default (aktif) | Custom | Global Settings`
17. Verifikasi Header: Sub-tab `Active | Archive (aktif)`
18. Verifikasi Header: Table Tools `Search | Filter | Download | Changelog`
19. Verifikasi Header: tombol `+ Default Plan` tidak tampil di Table Tools
20. Verifikasi Body: kolom `Plan Name (sortable) | Product (sortable) | Pricing Type (sortable) | Version (sortable) | Clients (sortable) | Last Modified (sortable) | Column Visibility (⋯) (unsortable — header klik = buka Overlay Column Visibility, body per baris = row action menu)`
21. Verifikasi Body: baris `Growth Plus (old)` | `FAMS` | `Paid` | `v3` | `31` | `01 Aug 26, 08:00`
22. Verifikasi Footer: teks `Showing 1–1 of 1 entries` dan `Rows per page: 10`

### Penghubung: tambahkan Dataset Plan S dan Dataset Plan R

23. Tambahkan Dataset Plan S dan Dataset Plan R lewat fixture BE hingga tersimpan
24. Muat ulang halaman dengan F5
25. Klik sub-tab Active

### TC-AC-PF-5: Urutan default tab Default sub-tab Active: Product A-Z lalu urutan tier dengan Free lebih dulu

26. Verifikasi urutan baris dari atas `Starter`, `Growth`, `Professional`, `Enterprise` (Product `FAMS`, Free lebih dulu lalu Paid menurut tier naik), `Supply Starter`, `Supply Pro` (Product `SAMS`), `SIEM` (Product `SIEM`)
27. Verifikasi tidak ada header kolom yang menampilkan panah sort aktif

### TC-AC-PF-6: Urutan default tab Default sub-tab Archive: Last Modified Newest First

28. Klik sub-tab Archive
29. Verifikasi baris `Plan Arsip Baru` (20 Aug 26, 08:00), `Plan Arsip Tengah` (15 Jul 26, 08:00), dan `Plan Arsip Lama` (01 Jun 26, 08:00) tampil berurutan dari atas ke bawah

## Notes

- Langkah penghubung (S-03): langkah 23 sampai 25 menambahkan Dataset Plan S dan Dataset Plan R yang dibutuhkan precondition TC-AC-PF-5 dan TC-AC-PF-6 tetapi tidak boleh ada saat TC-AC-PF-1 dan TC-AC-PF-2 mengasersi jumlah baris (`Showing 1–5 of 5 entries`, `Showing 1–1 of 1 entries`); muat ulang (F5) dan klik sub-tab Active mengembalikan layar ke Default > Active. Langkah 28 membuka sub-tab Archive untuk TC-AC-PF-6.
- Langkah "Susuri halaman dari atas ke bawah" adalah langkah observasi TC; asersi tiap bagian halaman ditulis sebagai `Verifikasi` terpisah per klausa (S-01).
- TC-AC-PF-3, TC-AC-PF-4, TC-AC-PF-7, dan TC-AC-PF-8 (tab Custom) ada di spec 024.
- Temuan untuk QA:
  - TC-AC-PF-6: Expected menyebut urutan hanya tiga baris Dataset Plan R, padahal Dataset Plan A juga memuat `Growth Plus (old)` (01 Aug 26, 08:00) di Default Archive dan jatuh di antara `Plan Arsip Baru` dan `Plan Arsip Tengah`. Spec mengasersi urutan relatif ketiga baris yang disebut TC; mohon QA menegaskan apakah baris `Growth Plus (old)` boleh ikut tampil.
  - TC-AC-PF-1 dan TC-AC-PF-2 mengasersi jumlah baris yang hanya benar bila Dataset Plan S dan Dataset Plan R belum ada, sedangkan TC-AC-PF-5 dan TC-AC-PF-6 membutuhkannya; TC tidak menyebut urutan penambahan data, sehingga spec menambahkannya lewat langkah penghubung.
  - TC-AC-PF-1 baris Clients `47` pada `Growth` berbeda dari Dataset Plan D (`Growth` memiliki 9 client); spec mengikuti TC-AC-PF-1 (Dataset Plan A).
