---
id: TC-AC-PF-E2E-007-breadcrumb-plan-detail-tab-default-sub-tab-active-dan-archive
title: "Breadcrumb Plan Detail Tab Default Sub-tab Active dan Archive"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-PF-28
  - TC-AC-PF-29
coverage:
  web: automated
---

# Breadcrumb Plan Detail Tab Default Sub-tab Active dan Archive

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal `totalControlPrincipal_automated_{namaCompany}@qwertysystem.net` (nama tampil `Andi Wijaya`, Pre-setup #1), password dari `Spectra.env.AC_TC_PASSWORD` (akun default suite).
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Plans & Licensing > Plans & Features, Default > Active). Tidak ada ganti akun di tengah spec.
- Data Pre-setup (hook `before`): Dataset Plan A (Pre-setup #21): default aktif `Growth` (FAMS, Paid, v5) dan default archived `Growth Plus (old)` (FAMS, Paid, v3). General Settings: Date Format `dd MMM yy`, Time Format 24-hour, Time Zone UTC (Pre-setup #44).
- Pengecualian S-06/S-12 butir A-14: nama Plan Pre-setup literal tanpa suffix (`Growth`, `Growth Plus (old)`) dipakai karena menjadi target klik yang diasersi; spec hanya membaca data itu dan tidak mengubahnya. Pemulihan Dataset ke keadaan awal lewat fixture BE yang idempoten (disediakan tim FE/BE) dijalankan di hook `before` dan `after`; suite berjalan serial.
- Berkas `fixtures/plans-licensing-plans-features.json` belum ada; nilai data ditulis langsung pada langkah sampai tim FE menyediakannya.
- Flag Guided Tooltip halaman ini disetel true oleh hook `before` suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Kemampuan teknis: fixture BE (pemulihan Dataset Pre-setup) dan sesi API aktor, disediakan tim FE/BE (lihat `suite.md`).
- Env var: hanya `Spectra.env.AC_TC_PASSWORD`; password tidak ditulis di spec atau fixture.

## Test Steps

### TC-AC-PF-28: Breadcrumb Plan Detail Default Active mengikuti tab dan sub-tab plan dan segmen tengah dapat diklik

1. Klik teks `Growth` pada kolom Plan Name untuk membuka Plan Detail `Growth`
2. Verifikasi Breadcrumb `Plans & Licensing > Plans & Features > Default > Active > Detail`
3. Verifikasi segmen `Plans & Licensing` dan `Detail` statis
4. Klik segmen `Default` pada breadcrumb
5. Verifikasi tab Default terbuka pada sub-tab default `Active`
6. Ketik Search `Growth`, tekan Enter
7. Klik teks `Growth` pada kolom Plan Name untuk membuka Plan Detail `Growth`
8. Klik segmen `Active` pada breadcrumb
9. Verifikasi sub-tab Active pada tab Default terbuka
10. Verifikasi state list dipertahankan: Search `Growth` masih terpasang
11. Klik teks `Growth` pada kolom Plan Name untuk membuka Plan Detail `Growth`
12. Klik segmen `Plans & Features` pada breadcrumb
13. Verifikasi halaman Plans & Licensing > Plans & Features > Default > Active terbuka

### TC-AC-PF-29: Breadcrumb Plan Detail Default Archive mengikuti tab dan sub-tab plan dan segmen tengah dapat diklik

14. Klik menu Plans & Licensing > Plans & Features di sidebar
15. Klik sub-tab Archive
16. Klik teks `Growth Plus (old)` pada kolom Plan Name untuk membuka Plan Detail `Growth Plus (old)`
17. Verifikasi Breadcrumb `Plans & Licensing > Plans & Features > Default > Archive > Detail`
18. Verifikasi segmen `Plans & Licensing` dan `Detail` statis
19. Klik segmen `Default` pada breadcrumb
20. Verifikasi tab Default terbuka pada sub-tab default `Active`
21. Klik sub-tab Archive
22. Ketik Search `Growth Plus`, tekan Enter
23. Klik teks `Growth Plus (old)` pada kolom Plan Name untuk membuka Plan Detail `Growth Plus (old)`
24. Klik segmen `Archive` pada breadcrumb
25. Verifikasi sub-tab Archive pada tab Default terbuka
26. Verifikasi state list dipertahankan: Search `Growth Plus` masih terpasang
27. Klik teks `Growth Plus (old)` pada kolom Plan Name untuk membuka Plan Detail `Growth Plus (old)`
28. Klik segmen `Plans & Features` pada breadcrumb
29. Verifikasi halaman Plans & Licensing > Plans & Features > Default > Active terbuka

## Notes

- Langkah penghubung (S-03): langkah 6 dan 22 memasang Search sebagai state list yang kemudian diasersi pada langkah 10 dan 26; langkah 7, 11, 16, 23, dan 27 membuka kembali Plan Detail sesuai langkah TC ("Buka kembali Plan Detail"); langkah 14 (klik menu sidebar) mereset Search, Sort, dan Filter sebelum TC berikutnya (S-09); langkah 15 dan 21 mengarahkan layar ke sub-tab yang disyaratkan TC.
- Search pada langkah 6 dan 22 ditambahkan karena Expected TC menyebut "state list dipertahankan" tanpa state yang diatur (S-14, S-03); asersi pada langkah 10 dan 26 hanya mengamati Search yang dipasang spec.
- TC-AC-PF-30 dan TC-AC-PF-31 (tab Custom) ada di spec 008.
- Temuan untuk QA:
  - TC-AC-PF-28 dan TC-AC-PF-29: Expected c menyebut "state list dipertahankan" tetapi langkah TC tidak mengatur state apa pun (Search, Sort, Filter, halaman) sebelum Plan Detail dibuka sehingga asersi tidak dapat gagal; spec memasang Search `Growth` dan `Growth Plus` sebagai state pengamatan.
