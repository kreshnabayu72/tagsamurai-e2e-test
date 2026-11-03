---
id: TC-AC-PF-E2E-205-server-menolak-distributor-untuk-create-edit-archive
title: "Defense-in-depth: Server Menolak Distributor Total Control untuk Create, Edit, Archive, dan Delete Default Plan"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AC-PF-553
  - TC-AC-PF-554
  - TC-AC-PF-555
  - TC-AC-PF-556
coverage:
  web: automated
---

# Defense-in-depth: Server Menolak Distributor Total Control untuk Create, Edit, Archive, dan Delete Default Plan

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Distributor `totalControlDistributor_automated_{namaCompany}@qwertysystem.net` (Pre-setup #10, entitas Distributor berstatus Active, capability Create, Update, Delete aktif), password dari `Spectra.env.AC_PF_DIST_TC_PASSWORD`. Kelas harness: a defense-in-depth (request langsung ke server, tanpa melewati browser).
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Plans & Licensing > Plans & Features, Default > Active). Tidak ada ganti akun di tengah spec; request langsung memakai sesi API akun #10.
- Data Pre-setup (hook `before`): Dataset Plan A (Pre-setup #21: default `Starter`, `Growth` v5, `Professional`, `Enterprise`), Dataset Plan R (Pre-setup #30: default archived `Plan Arsip Lama`, `Plan Arsip Tengah`, `Plan Arsip Baru`, Clients 0), dan Dataset Plan Y (Pre-setup #37: default FAMS tanpa subscription: `Starter`, `Growth`, `Professional`, `Enterprise`).
- Baseline (dicatat di hook `before` lewat kemampuan baca fixture BE sebelum request pertama): jumlah entri Changelog Default (`N_log_default`), jumlah baris default plan sub-tab Active dan Archive, serta Version tiap default plan. Asersi "tidak berubah" membandingkan state akhir dengan baseline ini; jumlah entri Changelog tidak diasersi sebagai angka absolut (audit trail permanen).
- Pengecualian S-06/S-12 butir A-14: nama Plan Pre-setup literal tanpa suffix (`Growth`, `Enterprise`, `Plan Arsip Lama`) dipakai sebagai target request yang ditolak; spec hanya membaca data itu dan tidak mengubahnya. Pemulihan semua Dataset lewat fixture BE yang idempoten (disediakan tim FE/BE) dijalankan di hook `before` dan `after`; suite berjalan serial.
- Berkas `fixtures/plans-licensing-plans-features.json` belum ada; nilai data ditulis langsung pada langkah sampai tim FE menyediakannya.
- Flag Guided Tooltip halaman ini disetel true oleh hook `before` suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Kemampuan teknis (disediakan tim FE/BE, lihat `suite.md`): klien HTTP untuk request langsung ke server, sesi API akun #10, fixture BE untuk membaca state akhir (daftar plan, Version, dan jumlah entri Changelog) dan memulihkan Dataset.
- Env var: hanya `Spectra.env.AC_PF_DIST_TC_PASSWORD`; nama ini didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture.

## Test Steps

### TC-AC-PF-553: Distributor Total Control ditolak server saat membuat default plan lewat permintaan langsung

1. Kirim permintaan buat default plan Paid SAMS langsung ke server dengan sesi API akun Distributor Total Control
2. Verifikasi server menolak permintaan karena Entity Gate Principal-only
3. Verifikasi (dibaca lewat fixture BE) data default plan tidak berubah: tidak ada default plan SAMS Paid baru dan jumlah baris default plan sama dengan baseline
4. Verifikasi (dibaca lewat fixture BE) Version seluruh default plan sama dengan baseline
5. Verifikasi (dibaca lewat fixture BE) jumlah entri Changelog Default sama dengan `N_log_default`

### TC-AC-PF-554: Distributor Total Control ditolak server saat mengubah default plan lewat permintaan langsung

6. Kirim permintaan ubah Group count default plan `Growth` menjadi `25` langsung ke server dengan sesi API akun Distributor Total Control
7. Verifikasi server menolak permintaan karena Entity Gate Principal-only
8. Verifikasi (dibaca lewat fixture BE) data default plan `Growth` tidak berubah: Group count tetap `3`
9. Verifikasi (dibaca lewat fixture BE) Version `Growth` tetap `v5`
10. Verifikasi (dibaca lewat fixture BE) jumlah entri Changelog Default sama dengan `N_log_default`

### TC-AC-PF-555: Distributor Total Control ditolak server saat meng-archive default plan lewat permintaan langsung

11. Kirim permintaan archive default plan `Enterprise` (tanpa subscription penahan) langsung ke server dengan sesi API akun Distributor Total Control
12. Verifikasi server menolak permintaan karena Entity Gate Principal-only
13. Verifikasi (dibaca lewat fixture BE) `Enterprise` masih ada di sub-tab Active default plan
14. Verifikasi (dibaca lewat fixture BE) Version `Enterprise` sama dengan baseline
15. Verifikasi (dibaca lewat fixture BE) jumlah entri Changelog Default sama dengan `N_log_default`

### TC-AC-PF-556: Distributor Total Control ditolak server saat menghapus default plan archived lewat permintaan langsung

16. Kirim permintaan delete default plan archived `Plan Arsip Lama` langsung ke server dengan sesi API akun Distributor Total Control
17. Verifikasi server menolak permintaan karena Entity Gate Principal-only
18. Verifikasi (dibaca lewat fixture BE) `Plan Arsip Lama` masih ada di sub-tab Archive default plan
19. Verifikasi (dibaca lewat fixture BE) Version `Plan Arsip Lama` sama dengan baseline
20. Verifikasi (dibaca lewat fixture BE) jumlah entri Changelog Default sama dengan `N_log_default`

## Notes

- K-1: keempat TC adalah kelas a dengan Expected berupa respons API dan state data; tetap satu spec FE+BE walau tumpang tindih dengan `tc-plans-licensing-plans-features-backend.md`.
- Bagian 8b butir 1: request langsung tidak melewati browser, sehingga hanya status respons dan state data yang diasersi. Langkah TC "Dengan sesi Principal buka tab Default ... klik ikon Changelog ... amati entri terbaru" dibaca sebagai pembacaan state lewat fixture BE; tampilan UI tidak diasersi di spec ini.
- Expected "Changelog tidak berubah" diasersi sebagai jumlah entri sama dengan baseline (S-12), bukan sebagai asersi absence; spec ini tidak memuat TC kelas g.
- Temuan untuk QA:
  - TC-AC-PF-553 sampai TC-AC-PF-556: precondition menyebut Dataset Plan A, R, dan Y bersamaan, padahal Dataset Plan A (Enterprise Clients 8) dan Dataset Plan Y (default FAMS tanpa subscription) mendefinisikan default FAMS yang sama dengan jumlah Clients berbeda. Spec memakai baseline hasil seeding hook `before` dan hanya mengasersi bahwa state tidak berubah.
  - TC-AC-PF-554: nilai Group count pada permintaan tidak disebut; spec memakai `25` (opsi valid yang berbeda dari nilai awal `3`).
  - TC-AC-PF-555: "tanpa subscription penahan" hanya berlaku pada Dataset Plan Y; pada Dataset Plan A `Enterprise` memiliki Clients 8.
