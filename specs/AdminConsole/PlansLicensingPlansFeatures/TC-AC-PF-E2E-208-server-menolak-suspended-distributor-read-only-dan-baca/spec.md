---
id: TC-AC-PF-E2E-208-server-menolak-suspended-distributor-read-only-dan-baca
title: "Defense-in-depth: Server Menolak Aksi Tulis Distributor Suspended, Save Global Settings oleh Read Only dan Distributor, serta Baca Global Settings"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AC-PF-562
  - TC-AC-PF-563
  - TC-AC-PF-564
  - TC-AC-PF-646
coverage:
  web: automated
---

# Defense-in-depth: Server Menolak Aksi Tulis Distributor Suspended, Save Global Settings oleh Read Only dan Distributor, serta Baca Global Settings

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Total Control Distributor Suspended `suspendedDistributor_automated_{namaCompany}@qwertysystem.net` (Pre-setup #16, entitas Distributor berstatus Suspended), password dari `Spectra.env.AC_PF_DIST_SUSP_PASSWORD` (TC-AC-PF-562). Akun lain, semuanya lewat sesi API: Read Only Principal `readOnlyPrincipal_automated_{namaCompany}@qwertysystem.net` (Pre-setup #2, nama tampil `Dewi Lestari`), password dari `Spectra.env.AC_PF_RO_PASSWORD` (TC-AC-PF-563 dan TC-AC-PF-646); Total Control Distributor `totalControlDistributor_automated_{namaCompany}@qwertysystem.net` (Pre-setup #10, entitas Active), password dari `Spectra.env.AC_PF_DIST_TC_PASSWORD` (TC-AC-PF-564 dan TC-AC-PF-646). Kelas harness: a defense-in-depth (request langsung ke server, tanpa melewati browser).
- Login akun #16 di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Plans & Licensing > Plans & Features, Default > Active). Tidak ada ganti akun UI di tengah spec; request akun #2 dan #10 memakai sesi API masing-masing (pelaku lain lewat sesi API).
- Data Pre-setup (hook `before`): Dataset Plan X (Pre-setup #36: custom plan Distributor `Plan Distributor Satu`, aktif); nilai Global FAMS Settings tersimpan `5` (Max custom fields per asset name) dan `2` (Max depreciation methods (Multi Depreciation tier)); Changelog Global Settings memuat sedikitnya satu entri.
- Baseline (dicatat di hook `before` lewat kemampuan baca fixture BE sebelum request pertama): Version dan data `Plan Distributor Satu`, jumlah entri Changelog Custom milik Distributor (`N_log_custom_dist`), nilai Max custom fields per asset name (`5`), dan jumlah entri Changelog Global Settings (`N_log_global`). Jumlah entri Changelog tidak diasersi sebagai angka absolut (audit trail permanen).
- Pengecualian S-06/S-12 butir A-14: nama Plan Pre-setup literal tanpa suffix dan nilai Global FAMS Settings Pre-setup dipakai sebagai target request yang ditolak; spec hanya membaca data itu dan tidak mengubahnya. Pemulihan Dataset dan nilai Global Settings lewat fixture BE yang idempoten (disediakan tim FE/BE) dijalankan di hook `before` dan `after`; suite berjalan serial.
- Berkas `fixtures/plans-licensing-plans-features.json` belum ada; nilai data ditulis langsung pada langkah sampai tim FE menyediakannya.
- Flag Guided Tooltip halaman ini disetel true oleh hook `before` suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Kemampuan teknis (disediakan tim FE/BE, lihat `suite.md`): klien HTTP untuk request langsung ke server, sesi API akun #16, #2, dan #10, fixture BE untuk membaca state akhir (data plan, Version, nilai Global FAMS Settings, dan jumlah entri Changelog) dan memulihkan Dataset.
- Env var: `Spectra.env.AC_PF_DIST_SUSP_PASSWORD`, `Spectra.env.AC_PF_RO_PASSWORD`, dan `Spectra.env.AC_PF_DIST_TC_PASSWORD`; ketiganya didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture.

## Test Steps

### TC-AC-PF-562: Aksi tulis dari entitas Distributor Suspended ditolak server walau dikirim langsung

1. Kirim permintaan ubah Group count `Plan Distributor Satu` menjadi `25` langsung ke server dengan sesi API akun Distributor Suspended
2. Verifikasi server menolak permintaan sebagai akses ditolak (forbidden) karena entitas aktor Suspended
3. Verifikasi (dibaca lewat fixture BE) `Plan Distributor Satu` tidak berubah dibanding baseline
4. Verifikasi (dibaca lewat fixture BE) Version `Plan Distributor Satu` tidak naik
5. Verifikasi (dibaca lewat fixture BE) jumlah entri Changelog Custom milik Distributor sama dengan `N_log_custom_dist`

### TC-AC-PF-563: Read Only Principal ditolak server saat Save Global Settings lewat permintaan langsung

6. Kirim permintaan simpan Max custom fields per asset name bernilai `8` langsung ke server dengan sesi API akun Read Only Principal
7. Verifikasi server menolak permintaan
8. Verifikasi (dibaca lewat fixture BE) nilai tersimpan Max custom fields per asset name tetap `5`
9. Verifikasi (dibaca lewat fixture BE) jumlah entri Changelog Global Settings sama dengan `N_log_global`

### TC-AC-PF-564: Distributor Total Control ditolak server saat Save Global Settings lewat permintaan langsung

10. Kirim permintaan simpan Max custom fields per asset name bernilai `8` langsung ke server dengan sesi API akun Distributor Total Control
11. Verifikasi server menolak permintaan karena Global Settings Principal-only
12. Verifikasi (dibaca lewat fixture BE) nilai tersimpan Max custom fields per asset name tetap `5`
13. Verifikasi (dibaca lewat fixture BE) jumlah entri Changelog Global Settings sama dengan `N_log_global`

### TC-AC-PF-646: Permintaan baca langsung Global FAMS Settings dan Changelog-nya oleh Distributor dan oleh Principal Read Only ditolak server

14. Sbg Distributor: kirim permintaan baca Global FAMS Settings langsung ke server dengan sesi API akun Distributor Total Control
15. Verifikasi permintaan ditolak server sebagai akses ditolak (forbidden)
16. Sbg Distributor: kirim permintaan baca Changelog Global Settings langsung ke server dengan sesi API akun Distributor Total Control
17. Verifikasi permintaan ditolak server sebagai akses ditolak (forbidden)
18. Sbg Read Only Principal: kirim permintaan baca Global FAMS Settings langsung ke server dengan sesi API akun Read Only Principal
19. Verifikasi permintaan ditolak server sebagai akses ditolak (forbidden)
20. Sbg Read Only Principal: kirim permintaan baca Changelog Global Settings langsung ke server dengan sesi API akun Read Only Principal
21. Verifikasi permintaan ditolak server sebagai akses ditolak (forbidden)
22. Verifikasi keempat respons tidak mengembalikan nilai setting
23. Verifikasi keempat respons tidak mengembalikan entri Changelog

## Notes

- K-1: keempat TC adalah kelas a dengan Expected berupa respons API dan state data; tetap satu spec FE+BE walau tumpang tindih dengan `tc-plans-licensing-plans-features-backend.md`.
- Bagian 8b butir 1: request langsung tidak melewati browser, sehingga hanya status respons dan state data yang diasersi. Langkah TC "Dengan sesi Principal buka tab Global Settings, amati nilai ..., klik ikon Changelog di Card" dibaca sebagai pembacaan state lewat fixture BE; tampilan UI tidak diasersi di spec ini.
- Expected "tidak ada entri log" diasersi sebagai jumlah entri sama dengan baseline (S-12), bukan sebagai asersi absence; spec ini tidak memuat TC kelas g.
- Temuan untuk QA:
  - TC-AC-PF-562: nilai Group count pada permintaan tidak disebut; spec memakai `25`.
  - TC-AC-PF-646: precondition menyebut "dua akun terpisah" tetapi tidak menyebut akun Read Only Principal yang dipakai; spec memakai Pre-setup #2.
  - TC-AC-PF-564: precondition menyebut sesi B Principal untuk mengamati hasil; pembacaan dilakukan lewat fixture BE sehingga akun Principal tidak dipakai sebagai sesi UI.
