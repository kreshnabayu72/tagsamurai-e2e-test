---
id: TC-AC-PF-E2E-206-server-menolak-partner-untuk-create-edit-archive-delete
title: "Defense-in-depth: Server Menolak Partner Total Control untuk Create, Edit, Archive, dan Delete Default Plan"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AC-PF-557
  - TC-AC-PF-656
  - TC-AC-PF-657
  - TC-AC-PF-658
coverage:
  web: automated
---

# Defense-in-depth: Server Menolak Partner Total Control untuk Create, Edit, Archive, dan Delete Default Plan

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Partner `totalControlPartner_automated_{namaCompany}@qwertysystem.net` (Pre-setup #17, entitas Partner Active), password dari `Spectra.env.AC_PF_PARTNER_TC_PASSWORD`. Kelas harness: a defense-in-depth (request langsung ke server, tanpa melewati browser).
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Plans & Licensing > Plans & Features, Default > Active). Tidak ada ganti akun di tengah spec; request langsung memakai sesi API akun #17.
- Data Pre-setup (hook `before`): Dataset Plan A (Pre-setup #21: default `Starter`, `Growth` v5, `Professional`, `Enterprise`) dan Dataset Plan R (Pre-setup #30: default archived `Plan Arsip Lama`, `Plan Arsip Tengah`, `Plan Arsip Baru`, Clients 0).
- Baseline (dicatat di hook `before` lewat kemampuan baca fixture BE sebelum request pertama): jumlah entri Changelog Default (`N_log_default`), jumlah baris default plan sub-tab Active dan Archive, serta Version tiap default plan. Jumlah entri Changelog tidak diasersi sebagai angka absolut (audit trail permanen).
- Pengecualian S-06/S-12 butir A-14: nama Plan Pre-setup literal tanpa suffix (`Growth`, `Enterprise`, `Plan Arsip Lama`) dipakai sebagai target request yang ditolak; spec hanya membaca data itu dan tidak mengubahnya. Pemulihan Dataset lewat fixture BE yang idempoten (disediakan tim FE/BE) dijalankan di hook `before` dan `after`; suite berjalan serial.
- Berkas `fixtures/plans-licensing-plans-features.json` belum ada; nilai data ditulis langsung pada langkah sampai tim FE menyediakannya.
- Flag Guided Tooltip halaman ini disetel true oleh hook `before` suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Kemampuan teknis (disediakan tim FE/BE, lihat `suite.md`): klien HTTP untuk request langsung ke server, sesi API akun #17, fixture BE untuk membaca state akhir (daftar plan, Version, dan jumlah entri Changelog) dan memulihkan Dataset.
- Env var: hanya `Spectra.env.AC_PF_PARTNER_TC_PASSWORD`; nama ini didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture.

## Test Steps

### TC-AC-PF-557: Partner ditolak server untuk membuat default plan lewat permintaan langsung

1. Kirim permintaan buat default plan Paid SAMS langsung ke server dengan sesi API akun Partner Total Control
2. Verifikasi permintaan ditolak karena Entity Gate Principal-only
3. Verifikasi (dibaca lewat fixture BE) tidak ada default plan baru: jumlah baris default plan sama dengan baseline
4. Verifikasi (dibaca lewat fixture BE) jumlah entri Changelog Default sama dengan `N_log_default` (tidak ada entri Create baru)

### TC-AC-PF-656: Partner ditolak server untuk mengubah default plan lewat permintaan langsung

5. Kirim permintaan ubah Group count default plan `Growth` menjadi `25` langsung ke server dengan sesi API akun Partner Total Control
6. Verifikasi permintaan ditolak karena Entity Gate Principal-only
7. Verifikasi (dibaca lewat fixture BE) Version `Growth` tetap `v5`
8. Verifikasi (dibaca lewat fixture BE) jumlah entri Changelog Default sama dengan `N_log_default`

### TC-AC-PF-657: Partner ditolak server untuk meng-archive default plan lewat permintaan langsung

9. Kirim permintaan archive default plan `Enterprise` langsung ke server dengan sesi API akun Partner Total Control
10. Verifikasi permintaan ditolak karena Entity Gate Principal-only
11. Verifikasi (dibaca lewat fixture BE) `Enterprise` tetap di sub-tab Active default plan
12. Verifikasi (dibaca lewat fixture BE) jumlah entri Changelog Default sama dengan `N_log_default` (tidak ada entri Archive baru)

### TC-AC-PF-658: Partner ditolak server untuk menghapus default plan archived lewat permintaan langsung

13. Kirim permintaan delete default plan archived `Plan Arsip Lama` langsung ke server dengan sesi API akun Partner Total Control
14. Verifikasi permintaan ditolak karena Entity Gate Principal-only
15. Verifikasi (dibaca lewat fixture BE) `Plan Arsip Lama` tetap di sub-tab Archive default plan
16. Verifikasi (dibaca lewat fixture BE) jumlah entri Changelog Default sama dengan `N_log_default` (tidak ada entri Delete baru)

## Notes

- K-1: keempat TC adalah kelas a dengan Expected berupa respons API dan state data; tetap satu spec FE+BE walau tumpang tindih dengan `tc-plans-licensing-plans-features-backend.md`.
- Bagian 8b butir 1: request langsung tidak melewati browser, sehingga hanya status respons dan state data yang diasersi. Langkah TC "Dengan sesi Principal buka tab Default ... klik ikon Changelog pada toolbar ... amati entri terbaru" dibaca sebagai pembacaan state lewat fixture BE; tampilan UI tidak diasersi di spec ini.
- Expected "Changelog tidak memuat entri baru" diasersi sebagai jumlah entri sama dengan baseline (S-12), bukan sebagai asersi absence; spec ini tidak memuat TC kelas g.
- Temuan untuk QA:
  - TC-AC-PF-656: nilai Group count pada permintaan tidak disebut; spec memakai `25` (opsi valid yang berbeda dari nilai awal `3`).
  - TC-AC-PF-657: pada Dataset Plan A `Enterprise` memiliki Clients 8; server dapat menolak karena guard subscription selain Entity Gate. Spec mengasersi alasan penolakan sesuai Expected TC (Entity Gate Principal-only).
