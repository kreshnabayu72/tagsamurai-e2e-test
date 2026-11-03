---
id: TC-AC-PF-E2E-210-invarian-server-default-plan-slot-free-paid-posisi-tier
title: "Defense-in-depth: Invarian Server Default Plan: Slot Free dan Paid, Posisi Tier, Asset Cap, dan Feature Suites Plan Free"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AC-PF-570
  - TC-AC-PF-571
  - TC-AC-PF-572
  - TC-AC-PF-573
  - TC-AC-PF-574
  - TC-AC-PF-575
  - TC-AC-PF-576
  - TC-AC-PF-577
coverage:
  web: automated
---

# Defense-in-depth: Invarian Server Default Plan: Slot Free dan Paid, Posisi Tier, Asset Cap, dan Feature Suites Plan Free

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal `totalControlPrincipal_automated_{namaCompany}@qwertysystem.net` (Pre-setup #1, nama tampil `Andi Wijaya`), password dari `Spectra.env.AC_TC_PASSWORD` (akun default suite). Kelas harness: a defense-in-depth (request langsung ke server, tanpa melewati browser).
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Plans & Licensing > Plans & Features, Default > Active). Tidak ada ganti akun di tengah spec; request langsung memakai sesi API akun #1.
- Data Pre-setup: Dataset Plan A (Pre-setup #21; FAMS penuh: 1 Free `Starter` v2 dan 3 Paid `Growth` v5, `Professional`, `Enterprise`; SAMS belum memiliki default plan) dipakai TC-AC-PF-570 sampai TC-AC-PF-575 dan TC-AC-PF-577. Dataset Plan V (Pre-setup #34; default FAMS dengan 3 Paid aktif dan Free `Starter` sudah archived) dipakai TC-AC-PF-576 dan diterapkan lewat fixture BE pada langkah 29.
- Baseline (dicatat di hook `before` lewat kemampuan baca fixture BE sebelum request pertama): jumlah default plan per Product (FAMS dan SAMS), Version `Growth` dan `Starter`, serta jumlah entri Changelog Default (`N_log_default`). Baseline jumlah entri Changelog diperbarui lewat fixture BE setelah langkah 29. Jumlah entri Changelog tidak diasersi sebagai angka absolut (audit trail permanen).
- Pengecualian S-06/S-12 butir A-14: nama Plan Pre-setup literal tanpa suffix (`Starter`, `Growth`) dipakai sebagai target request yang ditolak; spec hanya membaca data itu dan tidak mengubahnya. Pemulihan Dataset ke Dataset Plan A lewat fixture BE yang idempoten (disediakan tim FE/BE) dijalankan di hook `before` dan `after`; suite berjalan serial.
- Berkas `fixtures/plans-licensing-plans-features.json` belum ada; nilai data ditulis langsung pada langkah sampai tim FE menyediakannya.
- Flag Guided Tooltip halaman ini disetel true oleh hook `before` suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Kemampuan teknis (disediakan tim FE/BE, lihat `suite.md`): klien HTTP untuk request langsung ke server, sesi API akun #1, fixture BE untuk membaca state akhir (daftar plan, Version, dan jumlah entri Changelog) dan memulihkan Dataset.
- Env var: hanya `Spectra.env.AC_TC_PASSWORD`; password tidak ditulis di spec atau fixture.

## Test Steps

### TC-AC-PF-570: Create default plan Free untuk Product yang sudah punya Free ditolak server dengan pesan Invariant #1

1. Kirim permintaan buat default plan FAMS dengan Pricing Type `Free` langsung ke server
2. Verifikasi server menolak dengan pesan "This product already has a free plan."
3. Verifikasi (dibaca lewat fixture BE) tidak ada plan baru: nama dan jumlah default plan FAMS sama dengan baseline
4. Verifikasi (dibaca lewat fixture BE) jumlah entri Changelog Default sama dengan `N_log_default`

### TC-AC-PF-571: Create default plan Paid untuk Product yang sudah mencapai tiga Paid ditolak server dengan pesan Invariant #2

5. Kirim permintaan buat default plan FAMS dengan Pricing Type `Paid` langsung ke server
6. Verifikasi server menolak dengan pesan "This product already has the maximum number of paid plans (3). Archive an existing one first."
7. Verifikasi (dibaca lewat fixture BE) tidak ada plan baru: nama dan jumlah default plan FAMS sama dengan baseline
8. Verifikasi (dibaca lewat fixture BE) jumlah entri Changelog Default sama dengan `N_log_default`

### TC-AC-PF-572: Posisi tier yang dikirim manual pada Create Default Plan ditolak server

9. Kirim permintaan buat default plan SAMS dengan field posisi tier terisi `1` langsung ke server
10. Verifikasi server menolak dengan pesan "Tier position is set by the system and cannot be submitted."
11. Verifikasi (dibaca lewat fixture BE) tidak ada plan SAMS baru: jumlah default plan SAMS sama dengan baseline
12. Verifikasi (dibaca lewat fixture BE) jumlah entri Changelog Default sama dengan `N_log_default`

### TC-AC-PF-573: Posisi tier yang dikirim manual pada Edit Plan ditolak server dan plan tidak berubah

13. Kirim permintaan ubah default plan `Growth` dengan field posisi tier terisi `1` langsung ke server
14. Verifikasi server menolak dengan pesan "Tier position is set by the system and cannot be submitted."
15. Verifikasi (dibaca lewat fixture BE) Version `Growth` tetap `v5`
16. Verifikasi (dibaca lewat fixture BE) jumlah entri Changelog Default sama dengan `N_log_default`

### TC-AC-PF-574: Asset cap yang dikirim untuk default plan Paid ditolak server saat Create

17. Kirim permintaan buat default plan FAMS Paid dengan field Asset cap terisi `25` langsung ke server
18. Verifikasi server menolak dengan pesan "Asset cap does not apply to paid plans." (tidak diabaikan diam-diam)
19. Verifikasi (dibaca lewat fixture BE) tidak ada plan baru: nama dan jumlah default plan FAMS sama dengan baseline
20. Verifikasi (dibaca lewat fixture BE) jumlah entri Changelog Default sama dengan `N_log_default`

### TC-AC-PF-575: Asset cap yang dikirim untuk default plan Paid ditolak server saat Edit

21. Kirim permintaan ubah default plan Paid `Growth` dengan field Asset cap terisi `25` langsung ke server
22. Verifikasi server menolak dengan pesan "Asset cap does not apply to paid plans."
23. Verifikasi (dibaca lewat fixture BE) Version `Growth` tetap `v5`
24. Verifikasi (dibaca lewat fixture BE) jumlah entri Changelog Default sama dengan `N_log_default`

### TC-AC-PF-577: Feature Suites non-None untuk default plan Free ditolak server saat Edit

25. Kirim permintaan ubah default plan Free `Starter` dengan Borrowing `Full` langsung ke server
26. Verifikasi server menolak dengan pesan "Feature suites are not available for the free plan"
27. Verifikasi (dibaca lewat fixture BE) Version `Starter` tetap `v2`
28. Verifikasi (dibaca lewat fixture BE) jumlah entri Changelog Default sama dengan `N_log_default`

### TC-AC-PF-576: Feature Suites non-None untuk default plan Free ditolak server saat Create

29. Terapkan Dataset Plan V lewat fixture BE (FAMS tanpa Free) dan catat ulang baseline jumlah default plan FAMS dan `N_log_default`
30. Kirim permintaan buat default plan FAMS Free dengan Borrowing `Full` langsung ke server
31. Verifikasi server menolak dengan pesan "Feature suites are not available for the free plan"
32. Verifikasi (dibaca lewat fixture BE) tidak ada plan baru: nama dan jumlah default plan FAMS sama dengan baseline
33. Verifikasi (dibaca lewat fixture BE) jumlah entri Changelog Default sama dengan `N_log_default`

## Notes

- K-1: kedelapan TC adalah kelas a dengan Expected berupa respons API dan state data; tetap satu spec FE+BE walau tumpang tindih dengan `tc-plans-licensing-plans-features-backend.md`.
- Bagian 8b butir 1: request langsung tidak melewati browser, sehingga hanya status respons dan state data yang diasersi. Langkah TC "Buka tab Default sub-tab Active, amati daftar plan ... klik ikon Changelog ... amati tidak ada entri baru" dibaca sebagai pembacaan state lewat fixture BE; tampilan UI tidak diasersi di spec ini.
- Expected "Changelog tidak memuat entri baru" diasersi sebagai jumlah entri sama dengan baseline (S-12), bukan sebagai asersi absence; spec ini tidak memuat TC kelas g.
- Penyimpangan urutan (S-10): TC-AC-PF-576 ditulis paling akhir karena memakai Dataset Plan V yang tidak dapat hidup bersamaan dengan Dataset Plan A pada FAMS; langkah 29 adalah langkah penghubung yang mengganti dataset.
- Temuan untuk QA:
  - TC-AC-PF-574: langkah menyebut "default plan FAMS Paid (slot tersedia)", padahal precondition Dataset Plan A menyebut FAMS penuh (1 Free + 3 Paid) sehingga slot Paid tidak tersedia. Spec mengikuti precondition dataset dan mengasersi pesan "Asset cap does not apply to paid plans."; urutan evaluasi invarian server (slot lebih dulu atau Asset cap lebih dulu) tidak ditentukan TC.
  - TC-AC-PF-572, TC-AC-PF-573, TC-AC-PF-574, dan TC-AC-PF-575: nilai field posisi tier dan Asset cap tidak disebut; spec memakai `1` dan `25`.
