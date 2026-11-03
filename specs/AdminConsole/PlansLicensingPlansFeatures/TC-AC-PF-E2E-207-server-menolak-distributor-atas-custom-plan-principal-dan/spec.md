---
id: TC-AC-PF-E2E-207-server-menolak-distributor-atas-custom-plan-principal-dan
title: "Defense-in-depth: Server Menolak Distributor atas Custom Plan Milik Principal dan Principal atas Custom Plan Milik Distributor"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AC-PF-558
  - TC-AC-PF-559
  - TC-AC-PF-560
  - TC-AC-PF-561
coverage:
  web: automated
---

# Defense-in-depth: Server Menolak Distributor atas Custom Plan Milik Principal dan Principal atas Custom Plan Milik Distributor

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Distributor `totalControlDistributor_automated_{namaCompany}@qwertysystem.net` (Pre-setup #10), password dari `Spectra.env.AC_PF_DIST_TC_PASSWORD` (aktor TC-AC-PF-558 sampai TC-AC-PF-560). Akun kedua: Total Control Principal `totalControlPrincipal_automated_{namaCompany}@qwertysystem.net` (Pre-setup #1), password dari `Spectra.env.AC_TC_PASSWORD` (aktor TC-AC-PF-561). Kelas harness: a defense-in-depth (request langsung ke server, tanpa melewati browser).
- Login akun #10 di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Plans & Licensing > Plans & Features, Default > Active). Tidak ada ganti akun UI di tengah spec; request akun #1 memakai sesi API akun #1 (pelaku kedua lewat sesi API).
- Data Pre-setup (hook `before`): Dataset Plan X (Pre-setup #36): custom plan Principal `Plan Principal Satu` (aktif) dan `Plan Principal Arsip` (archived); custom plan Distributor `Plan Distributor Satu` (aktif) dan `Plan Distributor Arsip` (archived, tidak pernah dipakai); custom plan Partner `Plan Partner Satu` (aktif).
- Baseline (dicatat di hook `before` lewat kemampuan baca fixture BE sebelum request pertama): Version dan data baris `Plan Principal Satu` dan `Plan Principal Arsip`, serta jumlah entri Changelog Custom Principal (`N_log_custom`). Jumlah entri Changelog tidak diasersi sebagai angka absolut (audit trail permanen).
- Pengecualian S-06/S-12 butir A-14: nama Plan Pre-setup literal tanpa suffix dipakai sebagai target request yang ditolak; spec hanya membaca data itu dan tidak mengubahnya. Pemulihan Dataset lewat fixture BE yang idempoten (disediakan tim FE/BE) dijalankan di hook `before` dan `after`; suite berjalan serial.
- Berkas `fixtures/plans-licensing-plans-features.json` belum ada; nilai data ditulis langsung pada langkah sampai tim FE menyediakannya.
- Flag Guided Tooltip halaman ini disetel true oleh hook `before` suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Kemampuan teknis (disediakan tim FE/BE, lihat `suite.md`): klien HTTP untuk request langsung ke server, sesi API akun #10 dan #1, fixture BE untuk membaca state akhir (data plan, Version, dan jumlah entri Changelog Custom) dan memulihkan Dataset.
- Env var: `Spectra.env.AC_PF_DIST_TC_PASSWORD` dan `Spectra.env.AC_TC_PASSWORD`; `AC_PF_DIST_TC_PASSWORD` didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture.

## Test Steps

### TC-AC-PF-558: Distributor ditolak server saat mengubah custom plan milik Principal lewat permintaan langsung

1. Kirim permintaan ubah Group count custom plan `Plan Principal Satu` menjadi `25` langsung ke server dengan sesi API akun Distributor Total Control
2. Verifikasi server menolak permintaan karena custom plan bukan milik entitas aktor
3. Verifikasi (dibaca lewat fixture BE) data `Plan Principal Satu` tidak berubah: Group count sama dengan baseline
4. Verifikasi (dibaca lewat fixture BE) Version `Plan Principal Satu` sama dengan baseline
5. Verifikasi (dibaca lewat fixture BE) jumlah entri Changelog Custom Principal sama dengan `N_log_custom`

### TC-AC-PF-559: Distributor ditolak server saat meng-archive custom plan milik Principal lewat permintaan langsung

6. Kirim permintaan meng-archive custom plan `Plan Principal Satu` langsung ke server dengan sesi API akun Distributor Total Control
7. Verifikasi server menolak permintaan karena custom plan bukan milik entitas aktor
8. Verifikasi (dibaca lewat fixture BE) `Plan Principal Satu` masih ada di sub-tab Active custom plan dengan data sama dengan baseline
9. Verifikasi (dibaca lewat fixture BE) Version `Plan Principal Satu` sama dengan baseline
10. Verifikasi (dibaca lewat fixture BE) jumlah entri Changelog Custom Principal sama dengan `N_log_custom`

### TC-AC-PF-560: Distributor ditolak server saat menghapus (archived) custom plan milik Principal lewat permintaan langsung

11. Kirim permintaan menghapus custom plan archived `Plan Principal Arsip` langsung ke server dengan sesi API akun Distributor Total Control
12. Verifikasi server menolak permintaan karena custom plan bukan milik entitas aktor
13. Verifikasi (dibaca lewat fixture BE) `Plan Principal Arsip` masih ada di sub-tab Archive custom plan dengan data sama dengan baseline
14. Verifikasi (dibaca lewat fixture BE) Version `Plan Principal Arsip` sama dengan baseline
15. Verifikasi (dibaca lewat fixture BE) jumlah entri Changelog Custom Principal sama dengan `N_log_custom`

### TC-AC-PF-561: Principal tidak dapat membaca custom plan milik Distributor lewat permintaan detail langsung

16. Kirim permintaan baca detail custom plan `Plan Distributor Satu` langsung ke server dengan sesi API akun Principal Total Control
17. Verifikasi server menolak permintaan karena plan di luar scope entitas Principal
18. Verifikasi respons permintaan tidak mengembalikan data plan `Plan Distributor Satu`

## Notes

- K-1: keempat TC adalah kelas a dengan Expected berupa respons API dan state data; tetap satu spec FE+BE walau tumpang tindih dengan `tc-plans-licensing-plans-features-backend.md`.
- Bagian 8b butir 1: request langsung tidak melewati browser, sehingga hanya status respons dan state data yang diasersi. Langkah TC "Dengan sesi Principal buka tab Custom ... amati kolom Version ... klik ikon Changelog ... amati entri terbaru" dibaca sebagai pembacaan state lewat fixture BE; tampilan UI tidak diasersi di spec ini.
- Expected "tidak ada entri log" diasersi sebagai jumlah entri sama dengan baseline (S-12), bukan sebagai asersi absence; spec ini tidak memuat TC kelas g.
- Temuan untuk QA:
  - TC-AC-PF-558: nilai Group count pada permintaan tidak disebut; spec memakai `25`.
  - TC-AC-PF-558 sampai TC-AC-PF-560: Expected "data dan versi tidak berubah" tidak menyebut field data yang diperiksa; spec mengasersi Group count (558) dan baris plan (559, 560) terhadap baseline.
  - TC-AC-PF-561: Changelog bukan bagian Expected; tidak ada asersi log pada TC ini.
