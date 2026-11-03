---
id: TC-AC-ACTS-E2E-160-detail-sku-realtime-tab-available-opsi-filter-banner-dan-approval
title: "Detail SKU Realtime: Unit Menjadi In Use, Keputusan Approval, Opsi Dropdown Filter, dan Banner Waiting for Approval Tanpa Reload"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACTS-386
  - TC-AC-ACTS-731
  - TC-AC-ACTS-735
  - TC-AC-ACTS-991
coverage:
  web: automated
---

# Detail SKU Realtime: Unit Menjadi In Use, Keputusan Approval, Opsi Dropdown Filter, dan Banner Waiting for Approval Tanpa Reload

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`.
- Login di hook `before` spec ini sebagai Total Control; halaman dibuka hook `beforeEach` suite (TAG > Stock). Hook `after` memulihkan sesi ke akun default suite (Total Control).
- Flag Guided Tooltip `guided_tooltip_seen_ac-tag-stock` disetel `seen` oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Data Pre-setup: SKU `RFID-ASSET-CORE-R5` (Pre-setup #12; Device Name `RFID Asset Tag`, Brand `Core`, Model `R5`, Object TAG). Unit uji milik spec di-seed di hook `before` pada SKU itu (idempoten) dan dipulihkan fixture BE di hook `after`: 2 unit Available (A, B) dan 2 unit Damaged/Missing (C, D), seluruhnya eligible Audit. Aksi spec mengubah Last Updated SKU Pre-setup; efeknya dipulihkan fixture BE.
- Kemampuan teknis: Sesi API aktor (login API password, token tidak dihitung sebagai sesi web) untuk pelaku kedua yang hanya memicu perubahan state, disediakan tim BE/FE (lihat `suite.md`).
- Kemampuan teknis: Fixture BE (seeding idempoten dan pemulihan SKU, unit, Subject, saldo Stock Ledger, dan sesi log) serta pembacaan state BE yang tidak terlihat di UI disediakan tim FE/BE tanpa endpoint karangan (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`).
- Pelaku kedua (Admin 2) memakai sesi API aktor: Approve dan Reject Subject, aktivasi unit lewat Global Settings > Activate TAG, Add Stock Admin 2 (Sari Dewi), dan Add Stock entitas Distributor lain (PT Karya Utama) dengan identifier yang cocok existing; seluruhnya kemampuan yang disediakan tim FE/BE (aktor dan mekanisme tidak disebut di TC, PRD, atau LLD; S-13). Hasil diasersi di sesi Admin 1 (Total Control).
- Data per blok TC (di-reset fixture BE): unit Available yang akan diaktivasi (TC-AC-ACTS-386); Subject Register Duplicate A dan B pending (TC-AC-ACTS-731); semua record dibuat oleh `Budi S` dan Subject pending hanya dari `PT Maju Bersama` (Distributor) (TC-AC-ACTS-735); satu Subject Register Duplicate pending (TC-AC-ACTS-991, untuk Approve).
- Kemampuan teknis: Pembacaan dropdown Filter tanpa reload halaman pada Tab Available, modal Event Log (Tab Add Stock), dan Approvals > TAG Stock > Tab Active. Hasil realtime diasersi pada halaman yang sudah terbuka tanpa memuat ulang halaman.

## Test Steps

### TC-AC-ACTS-386: Unit yang menjadi In Use hilang dari Tab Available secara realtime

1. Klik row action `Detail` pada SKU `RFID-ASSET-CORE-R5` di Stock List, lalu buka Tab Available
2. Sesi API mengaktivasi satu unit Available lewat Global Settings > Activate TAG hingga status In Use tersimpan
3. Amati Tab Available tanpa memuat ulang halaman
4. Verifikasi baris unit hilang otomatis dari Tab Available tanpa reload
5. Buka Tab In Use
6. Verifikasi unit itu muncul di Tab In Use

### TC-AC-ACTS-731: Tab Available mengikuti keputusan approval secara realtime tanpa reload

7. Reset dataset: Subject Register Duplicate A dan B pending lewat fixture BE, lalu buka Tab Available (unit A dan B belum tampil)
8. Sesi API (Admin 2) meng-Approve Subject A hingga status Approved tersimpan
9. Sesi API (Admin 2) me-Reject Subject B dengan Approval Note terisi hingga status Rejected tersimpan
10. Amati Tab Available tanpa memuat ulang halaman
11. Verifikasi unit A muncul otomatis di Tab Available sebagai Available dengan TAG Code baru
12. Verifikasi unit B tidak muncul di Tab Available (Rejected tidak tampil)
13. Verifikasi tidak ada reload halaman

### TC-AC-ACTS-735: Opsi dropdown Filter bertambah real-time setelah ada record baru

14. Reset dataset: semua record dibuat oleh `Budi S`, Subject pending hanya dari `PT Maju Bersama`
15. Buka Filter Panel Tab Available, buka dropdown `Registered By`, dan catat opsi
16. Buka modal `[Event Log]` (Tab Add Stock), Filter Panel, dropdown `Modified By`, dan catat opsi, lalu tutup modal Event Log
17. Buka Approvals > TAG Stock > Tab Active, Filter Panel, dropdown `Requested By`, dan catat opsi
18. Sesi API (Admin 2, Sari Dewi) Add Stock 1 unit baru pada SKU itu hingga tersimpan
19. Sesi API (PT Karya Utama) Add Stock 1 TAG yang cocok existing hingga Subject baru tersimpan
20. Buka kembali ketiga dropdown tanpa memuat ulang halaman
21. Verifikasi Tab Available: opsi `Registered By` bertambah `Sari D`
22. Verifikasi modal Event Log: opsi `Modified By` bertambah `Sari D`
23. Tutup modal Event Log
24. Verifikasi Approvals Tab Active: opsi `Requested By` bertambah `PT Karya Utama (Distributor)`

### TC-AC-ACTS-991: Banner diperbarui real-time dan hilang setelah unit terakhir di-approve

25. Reset dataset: satu Subject Register Duplicate pending lewat fixture BE, lalu buka Detail SKU `RFID-ASSET-CORE-R5` > Tab Available
26. Verifikasi banner `1 TAG is waiting for approval.` tampil
27. Catat Total Registered pada Summary bar
28. Sesi API (Admin 2) meng-Approve Subject itu hingga status Approved tersimpan
29. Amati Tab Available tanpa memuat ulang halaman
30. Verifikasi banner hilang tanpa reload
31. Verifikasi unit hasil Approve muncul sebagai baris Available dengan TAG Code baru
32. Verifikasi Total Registered bertambah 1 dari nilai yang dicatat sebelum Approve

## Notes

- Alasan di atas smell ~35 langkah: seluruh blok satu kelas harness (d, simulator reader) dengan satu dataset; tiap blok TC berdiri sendiri dan tidak kehilangan makna bila blok lain gagal. Langkah penutup popup (`✕`, dialog Unsaved Changes, `[Leave]`) diulang per blok.
- Langkah penghubung (S-03): langkah 1 (membuka Detail SKU), "Reset dataset", pencatatan opsi dropdown. Langkah "Tutup modal Event Log" menutup modal sebelum pindah surface atau ganti akun (pemulihan state, S-09).
- P-2: pelaku kedua yang hanya memicu perubahan state memakai sesi API aktor; tidak ada konteks UI kedua, sehingga tidak ada butir `P-2` selain pernyataan ini (kelas c ringan; hasil diasersi di sesi Admin 1).
- Temuan untuk QA:
  - Pelaku kedua (Admin 2, Sari Dewi, PT Karya Utama) tidak ada di Pre-setup TC; spec memakai sesi API aktor yang disediakan tim FE/BE.
  - TC-AC-ACTS-735 menyebut "semua record dibuat oleh Budi S"; Data Dinamis #3 memuat `Budi Santoso`, `Sari Dewi`, `Andi Wijaya`, sehingga opsi `Sari D` diasersi persis dari TC.
  - TC-AC-ACTS-386 tidak menyebut apakah unit yang diaktivasi muncul di Tab In Use pada Expected butir selain "muncul di Tab In Use"; spec membuka Tab In Use untuk mengasersinya.
