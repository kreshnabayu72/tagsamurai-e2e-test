---
id: TC-AC-PF-E2E-033-gate-status-entitas-suspended-dan-expired-aksi-tulis
title: Gate Status Entitas - Aktor Distributor Suspended, Partner Expired, dan Client Suspended pada Aksi Tulis
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-PF-24
  - TC-AC-PF-75
  - TC-AC-PF-76
  - TC-AC-PF-77
  - TC-AC-PF-281
coverage:
  web: automated
---

# Gate Status Entitas - Aktor Distributor Suspended, Partner Expired, dan Client Suspended pada Aksi Tulis

## Prerequisites

- Mode: FE+BE
- Role yang diuji (akun aktor pertama login di hook `before`; akun lain lewat langkah Ganti akun eksplisit):

| Role | Akun | Email | Env password | Blok |
|---|---|---|---|---|
| Total Control (Distributor Suspended) | #16 suspendedDistributor | `suspendedDistributor_automated_{namaCompany}@qwertysystem.net` | `AC_PF_DIST_SUSP_PASSWORD` | langkah 1 sampai 15 |
| Total Control (Partner Expired) | #19 expiredPartner | `expiredPartner_automated_{namaCompany}@qwertysystem.net` | `AC_PF_PARTNER_EXP_PASSWORD` | langkah 16 sampai 23 |
| Total Control (Principal) | #1 totalControlPrincipal | `totalControlPrincipal_automated_{namaCompany}@qwertysystem.net` | `AC_TC_PASSWORD` | langkah 24 sampai 35 |

- Login di hook `before` spec ini sebagai #16; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Flag Guided Tooltip mengikuti pernyataan di `suite.md` (hook suite menyetel flag true untuk akun aktor pre-setup).
- Data Pre-setup dan state entitas: Dataset Plan E untuk Distributor aktor (tanpa custom plan; hook `before` mengosongkannya), Dataset Plan X (custom Distributor `Plan Distributor Satu` dan `Plan Distributor Arsip`; custom Partner `Plan Partner Satu`; dipulihkan di langkah 5), Dataset Plan P (`Plan Distributor Satu` dengan client Active berversi lama dan delta upgrade; `Paket Push Susp` dengan client `PT Push Susp` berstatus Client Suspended dan subscription Active v1). Entitas `suspendedDistributor` berstatus Suspended dan `expiredPartner` berstatus Expired (Pre-setup #16 dan #19). Nama literal tanpa suffix memakai pengecualian S-06/S-12 butir A-14 (nilai dirujuk lewat fixture data `fixtures/plans-licensing-plans-features.json` yang belum ada, ditandai di sini sesuai S-12).
- Kemampuan teknis (disediakan tim FE/BE, dinyatakan di `suite.md`): fixture backend untuk mengosongkan dan memulihkan Dataset Plan E dan Dataset Plan X, state client Suspended, dan membaca jumlah entri Changelog Custom Principal (baseline N dicatat di hook `before`, dibaca sebelum aksi pemicu pertama yang diasersi).
- State global: status entitas aktor dan state Dataset (tenant Distributor); suite berjalan serial (`parallel: false`); Dataset dipulihkan di hook `after`.

## Test Steps

### Blok Total Control (Distributor Suspended): TC-AC-PF-24, TC-AC-PF-75, dan TC-AC-PF-76

1. Klik tab Custom.
2. Verifikasi area tabel menampilkan Illustration, Title "No custom plans yet", dan Description "Create a custom plan to configure specific feature sets for clients."
3. Verifikasi area tabel tanpa tombol `[+ Custom Plan]`.
4. Verifikasi toolbar tidak memuat tombol `+ Custom Plan`.
5. Pulihkan Dataset Plan X lewat fixture BE, lalu muat ulang halaman.
6. Verifikasi baris `Plan Distributor Satu` tampil.
7. Verifikasi toolbar tab Custom tanpa `+ Custom Plan`.
8. Buka Overlay Row Action pada baris `Plan Distributor Satu`.
9. Verifikasi Overlay Row Action hanya memuat `Detail` (Hidden, bukan Disabled).
10. Verifikasi ikon Search, Filter, Download, Changelog tampil dan aktif.
11. Buka Plan Detail `Plan Distributor Satu`.
12. Verifikasi header Plan Detail hanya menampilkan ikon Download; `Edit` dan `Archive` Hidden.
13. Klik Tab Assigned Clients.
14. Buka Overlay Row Action pada baris client Active yang Outdated.
15. Verifikasi Overlay Row Action hanya memuat `Detail`; `Push Update` Hidden walau versi client lebih lama dan delta upgrade.

### Blok Total Control (Partner Expired): TC-AC-PF-77

16. Ganti akun: logout, lalu login sebagai Total Control (Partner Expired) (#19).
17. Klik tab Custom.
18. Verifikasi baris `Plan Partner Satu` tampil.
19. Verifikasi toolbar tab Custom tanpa `+ Custom Plan`.
20. Buka Overlay Row Action pada baris `Plan Partner Satu`.
21. Verifikasi Overlay Row Action hanya memuat `Detail`.
22. Buka Plan Detail `Plan Partner Satu`.
23. Verifikasi header Plan Detail hanya menampilkan ikon Download.

### Blok Total Control (Principal): TC-AC-PF-281

24. Ganti akun: logout, lalu login sebagai Total Control (Principal) (#1).
25. Klik tab Custom.
26. Buka Plan Detail `Paket Push Susp`.
27. Klik Tab Assigned Clients.
28. Buka Overlay Row Action pada baris `PT Push Susp`.
29. Klik `Push Update`.
30. Klik `[Push Update]` pada dialog.
31. Verifikasi muncul toast error: "Changes can't be saved while this workspace is suspended or expired."
32. Verifikasi versi `PT Push Susp` pada kolom Plan Version tetap `v1`.
33. Kembali ke tab Custom lewat Breadcrumb.
34. Klik ikon Changelog pada toolbar tab Custom.
35. Verifikasi jumlah entri Changelog sama dengan baseline N (tidak ada entri Changelog baru).

## Notes

- Spec ditulis per blok role karena tiap pergantian akun menuntut Step Ganti akun eksplisit (akun pertama login di hook `before`); langkah 16 dan 24 adalah Ganti akun eksplisit (S-07).
- Langkah penghubung (S-03): langkah 1, 17, 25 (pindah tab), langkah 5 (pemulihan Dataset Plan X lewat fixture BE dan muat ulang antar blok TC), langkah 11, 22, 26 (membuka Plan Detail), langkah 33 (kembali ke list).
- Urutan TC: TC-AC-PF-24 dijalankan pertama karena membutuhkan tenant Distributor tanpa custom plan; sesudahnya Dataset Plan X dipulihkan untuk TC-AC-PF-75 dan TC-AC-PF-76.
- Langkah 6 dan 18 adalah anchor positif untuk langkah 7 dan 19 (absence tombol pada surface yang sudah termuat). Langkah 31 adalah anchor positif untuk langkah 32 dan 35 (respons server sudah diproses).
- P-1: TC-AC-PF-281 Expected b ("tidak ada entri Changelog") ditulis sebagai `Verifikasi` berbaseline (langkah 35) di spec ini karena konteksnya bergantung pada state berat yang dibangun fixture BE (client berstatus Suspended dengan subscription Active v1) dan langkah 30 sampai 31; asersi tidak dipindah ke spec absence.
- Kelas h (state tenant): seluruh blok memverifikasi gate write-lockdown status entitas; tiap blok berdiri sendiri dengan akun dan datanya sendiri.
- Temuan untuk QA:
  - TC-AC-PF-24 precondition memakai "Dataset Plan E" yang di Pre-setup #25 didefinisikan sebagai tenant tanpa default plan, tanpa custom plan, dan tanpa entri Changelog, sedangkan TC mengasersi tab Custom bagi aktor Distributor Suspended. Spec mengosongkan custom plan milik Distributor aktor lewat fixture BE dan tidak menyentuh default plan Principal.
  - TC-AC-PF-76 menyebut "baris client yang Outdated" tanpa nama client; Dataset Plan P hanya menyebut `Plan Distributor Satu` dengan "client eligible dalam jaringan Distributor". Nama client "disediakan tim FE/BE".
  - TC-AC-PF-75 Expected c ("Search, Filter, Download, Changelog dapat dipakai") tidak menyebut hasil terukur; spec memverifikasi ikon tampil dan aktif (langkah 10) dan tidak menjalankan keempat fitur.
  - Post Condition "Tidak ada perubahan data" tanpa langkah observasi tidak diasersi (S-01).
