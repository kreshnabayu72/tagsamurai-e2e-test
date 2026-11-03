---
id: TC-AC-PF-E2E-024-screening-plans-list-tab-custom-dan-urutan-default
title: "Screening Plans List Tab Custom Sub-tab Active dan Archive serta Urutan Default"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-PF-3
  - TC-AC-PF-4
  - TC-AC-PF-7
  - TC-AC-PF-8
coverage:
  web: automated
---

# Screening Plans List Tab Custom Sub-tab Active dan Archive serta Urutan Default

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal `totalControlPrincipal_automated_{namaCompany}@qwertysystem.net` (nama tampil `Andi Wijaya`, Pre-setup #1), password dari `Spectra.env.AC_TC_PASSWORD` (akun default suite).
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Plans & Licensing > Plans & Features, Default > Active). Tidak ada ganti akun di tengah spec.
- Data awal (hook `before`): Dataset Plan A (Pre-setup #21): Custom Principal aktif `Growth Tier` (FAMS, Paid, v20, Clients 1, 28 Jun 26 16:00), Custom Principal archived `Enterprise Reseller` (FAMS, Paid, v3, Clients 6, 10 Jun 26 09:15). Dataset Plan C (Pre-setup #23: custom aktif `alpha Tier`, `Beta Pro`, `Growth Tier`, `Zeta Max`; archived `Arsip Custom Satu` 02 Mar 26 10:00 dan `Arsip Custom Dua` 11 May 26 10:00) ditambahkan oleh langkah penghubung sebelum blok TC yang memakainya. General Settings: Date Format `dd MMM yy`, Time Format 24-hour, Time Zone UTC (Pre-setup #44).
- Pengecualian S-06/S-12 butir A-14: nama Plan Pre-setup literal tanpa suffix (`Growth Tier`, `Enterprise Reseller`, `alpha Tier`, `Beta Pro`, `Zeta Max`, `Arsip Custom Satu`, `Arsip Custom Dua`) dipakai karena menentukan asersi urutan, jumlah, dan teks; spec hanya membaca data itu dan tidak mengubahnya. Pemulihan semua Dataset ke keadaan awal lewat fixture BE yang idempoten (disediakan tim FE/BE) dijalankan di hook `before` dan `after` serta pada langkah penghubung; suite berjalan serial.
- Berkas `fixtures/plans-licensing-plans-features.json` belum ada; nilai data ditulis langsung pada langkah sampai tim FE menyediakannya.
- Flag Guided Tooltip halaman ini disetel true oleh hook `before` suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Kemampuan teknis: fixture BE (pemulihan dan penambahan Dataset Pre-setup) dan sesi API aktor, disediakan tim FE/BE (lihat `suite.md`).
- State global: Dataset Plan C yang ditambahkan spec ini dikembalikan ke baseline oleh hook `after` lewat fixture BE.
- Env var: hanya `Spectra.env.AC_TC_PASSWORD`; password tidak ditulis di spec atau fixture.

## Test Steps

### TC-AC-PF-3: Screening Plans List tab Custom sub-tab Active milik Principal saat Dataset Plan A tersedia

1. Klik tab Custom
2. Susuri halaman dari atas ke bawah tanpa mengklik apa pun
3. Verifikasi Header: Breadcrumb `Plans & Licensing > Plans & Features > Custom > Active`
4. Verifikasi Header: Tab `Default | Custom (aktif) | Global Settings`
5. Verifikasi Header: Sub-tab `Active (aktif) | Archive`
6. Verifikasi Header: Table Tools `Search | Filter | Download | Changelog | [+ Custom Plan]`
7. Verifikasi Body: kolom tampil `Plan Name (sortable) | Product (sortable) | Pricing Type (sortable) | Version (sortable) | Clients (sortable) | Last Modified (sortable) | Column Visibility (⋯) (unsortable — header klik = buka Overlay Column Visibility, body per baris = row action menu)`
8. Verifikasi Body: kolom Created By tidak tampil secara default (Curated, unchecked)
9. Verifikasi Body: baris `Growth Tier` | `FAMS` | `Paid` | `v20` | `1` | `28 Jun 26, 16:00`
10. Verifikasi Footer: teks `Showing 1–1 of 1 entries` dan `Rows per page: 10`

### TC-AC-PF-4: Screening Plans List tab Custom sub-tab Archive milik Principal saat Dataset Plan A tersedia

11. Klik sub-tab Archive
12. Susuri halaman dari atas ke bawah tanpa mengklik apa pun
13. Verifikasi Header: Breadcrumb `Plans & Licensing > Plans & Features > Custom > Archive`
14. Verifikasi Header: Sub-tab `Active | Archive (aktif)`
15. Verifikasi Header: Table Tools `Search | Filter | Download | Changelog`
16. Verifikasi Header: tombol `+ Custom Plan` tidak tampil di Table Tools
17. Verifikasi Body: baris `Enterprise Reseller` | `FAMS` | `Paid` | `v3` | `6` | `10 Jun 26, 09:15`
18. Verifikasi Body: kolom sama dengan sub-tab Active
19. Verifikasi Footer: teks `Showing 1–1 of 1 entries`

### Penghubung: tambahkan Dataset Plan C

20. Tambahkan Dataset Plan C lewat fixture BE hingga tersimpan
21. Muat ulang halaman dengan F5
22. Klik sub-tab Active

### TC-AC-PF-7: Urutan default tab Custom sub-tab Active: Plan Name A-Z tidak peka huruf besar-kecil

23. Verifikasi urutan baris dari atas `alpha Tier`, `Beta Pro`, `Growth Tier`, `Zeta Max` (huruf kecil `alpha` tetap di atas `Beta`)

### TC-AC-PF-8: Urutan default tab Custom sub-tab Archive: Last Modified Newest First

24. Klik sub-tab Archive
25. Verifikasi baris `Arsip Custom Dua` (11 May 26, 10:00) tampil di atas baris `Arsip Custom Satu` (02 Mar 26, 10:00)

## Notes

- Langkah penghubung (S-03): langkah 20 sampai 22 menambahkan Dataset Plan C yang dibutuhkan precondition TC-AC-PF-7 dan TC-AC-PF-8 tetapi tidak boleh ada saat TC-AC-PF-3 dan TC-AC-PF-4 mengasersi jumlah baris (`Showing 1–1 of 1 entries`); muat ulang (F5) dan klik sub-tab Active mengembalikan layar ke Custom > Active. Langkah 24 membuka sub-tab Archive untuk TC-AC-PF-8.
- Langkah "Susuri halaman dari atas ke bawah" adalah langkah observasi TC; asersi tiap bagian halaman ditulis sebagai `Verifikasi` terpisah per klausa (S-01).
- TC-AC-PF-1, TC-AC-PF-2, TC-AC-PF-5, dan TC-AC-PF-6 (tab Default) ada di spec 001.
- Temuan untuk QA:
  - TC-AC-PF-8: Expected menyebut urutan hanya dua baris Dataset Plan C, padahal Dataset Plan A juga memuat `Enterprise Reseller` (10 Jun 26, 09:15) di Custom Archive, yang lebih baru dari kedua baris itu. Spec mengasersi urutan relatif `Arsip Custom Dua` di atas `Arsip Custom Satu`; mohon QA menegaskan apakah `Enterprise Reseller` boleh ikut tampil.
  - Dataset Plan A dan Dataset Plan C memberi dua nilai berbeda untuk `Growth Tier` (Last Modified `28 Jun 26, 16:00` pada A, `22 Jun 26, 08:00` pada C). Spec mengasersi baris `Growth Tier` hanya pada TC-AC-PF-3 (Dataset Plan A) dan hanya urutan namanya pada TC-AC-PF-7.
