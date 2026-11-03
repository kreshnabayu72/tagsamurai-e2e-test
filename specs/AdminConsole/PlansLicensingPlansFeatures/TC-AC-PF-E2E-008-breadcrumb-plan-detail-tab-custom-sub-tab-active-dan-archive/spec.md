---
id: TC-AC-PF-E2E-008-breadcrumb-plan-detail-tab-custom-sub-tab-active-dan-archive
title: "Breadcrumb Plan Detail Tab Custom Sub-tab Active dan Archive"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-PF-30
  - TC-AC-PF-31
coverage:
  web: automated
---

# Breadcrumb Plan Detail Tab Custom Sub-tab Active dan Archive

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal `totalControlPrincipal_automated_{namaCompany}@qwertysystem.net` (nama tampil `Andi Wijaya`, Pre-setup #1), password dari `Spectra.env.AC_TC_PASSWORD` (akun default suite).
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Plans & Licensing > Plans & Features, Default > Active). Tidak ada ganti akun di tengah spec.
- Data Pre-setup (hook `before`): Dataset Plan A (Pre-setup #21): custom Principal aktif `Growth Tier` (FAMS, Paid, v20) dan custom Principal archived `Enterprise Reseller` (FAMS, Paid, v3). General Settings: Date Format `dd MMM yy`, Time Format 24-hour, Time Zone UTC (Pre-setup #44).
- Pengecualian S-06/S-12 butir A-14: nama Plan Pre-setup literal tanpa suffix (`Growth Tier`, `Enterprise Reseller`) dipakai karena menjadi target klik yang diasersi; spec hanya membaca data itu dan tidak mengubahnya. Pemulihan Dataset ke keadaan awal lewat fixture BE yang idempoten (disediakan tim FE/BE) dijalankan di hook `before` dan `after`; suite berjalan serial.
- Berkas `fixtures/plans-licensing-plans-features.json` belum ada; nilai data ditulis langsung pada langkah sampai tim FE menyediakannya.
- Flag Guided Tooltip halaman ini disetel true oleh hook `before` suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Kemampuan teknis: fixture BE (pemulihan Dataset Pre-setup) dan sesi API aktor, disediakan tim FE/BE (lihat `suite.md`).
- Env var: hanya `Spectra.env.AC_TC_PASSWORD`; password tidak ditulis di spec atau fixture.

## Test Steps

### TC-AC-PF-30: Breadcrumb Plan Detail Custom Active mengikuti tab dan sub-tab plan dan segmen tengah dapat diklik

1. Klik tab Custom
2. Klik teks `Growth Tier` pada kolom Plan Name untuk membuka Plan Detail `Growth Tier`
3. Verifikasi Breadcrumb `Plans & Licensing > Plans & Features > Custom > Active > Detail`
4. Verifikasi segmen `Plans & Licensing` dan `Detail` statis
5. Klik segmen `Custom` pada breadcrumb
6. Verifikasi tab Custom terbuka pada sub-tab default `Active`
7. Ketik Search `Growth Tier`, tekan Enter
8. Klik teks `Growth Tier` pada kolom Plan Name untuk membuka Plan Detail `Growth Tier`
9. Klik segmen `Active` pada breadcrumb
10. Verifikasi sub-tab Active pada tab Custom terbuka
11. Verifikasi state list dipertahankan: Search `Growth Tier` masih terpasang
12. Klik teks `Growth Tier` pada kolom Plan Name untuk membuka Plan Detail `Growth Tier`
13. Klik segmen `Plans & Features` pada breadcrumb
14. Verifikasi halaman Plans & Licensing > Plans & Features > Default > Active terbuka

### TC-AC-PF-31: Breadcrumb Plan Detail Custom Archive mengikuti tab dan sub-tab plan dan segmen tengah dapat diklik

15. Klik tab Custom
16. Klik sub-tab Archive
17. Klik teks `Enterprise Reseller` pada kolom Plan Name untuk membuka Plan Detail `Enterprise Reseller`
18. Verifikasi Breadcrumb `Plans & Licensing > Plans & Features > Custom > Archive > Detail`
19. Verifikasi segmen `Plans & Licensing` dan `Detail` statis
20. Klik segmen `Custom` pada breadcrumb
21. Verifikasi tab Custom terbuka pada sub-tab default `Active`
22. Klik sub-tab Archive
23. Ketik Search `Enterprise Reseller`, tekan Enter
24. Klik teks `Enterprise Reseller` pada kolom Plan Name untuk membuka Plan Detail `Enterprise Reseller`
25. Klik segmen `Archive` pada breadcrumb
26. Verifikasi sub-tab Archive pada tab Custom terbuka
27. Verifikasi state list dipertahankan: Search `Enterprise Reseller` masih terpasang
28. Klik teks `Enterprise Reseller` pada kolom Plan Name untuk membuka Plan Detail `Enterprise Reseller`
29. Klik segmen `Plans & Features` pada breadcrumb
30. Verifikasi halaman Plans & Licensing > Plans & Features > Default > Active terbuka

## Notes

- Langkah penghubung (S-03): langkah 7 dan 23 memasang Search sebagai state list yang kemudian diasersi pada langkah 11 dan 27; langkah 8, 12, 24, 28 membuka kembali Plan Detail sesuai langkah TC ("Buka kembali Plan Detail"); klik tab dan sub-tab pada langkah 1, 15, 16, dan 22 mengarahkan layar ke tab yang disyaratkan TC.
- Search pada langkah 7 dan 23 ditambahkan karena Expected TC menyebut "state list dipertahankan" tanpa state yang diatur (S-14, S-03); asersi pada langkah 11 dan 27 hanya mengamati Search yang dipasang spec.
- TC-AC-PF-28 dan TC-AC-PF-29 (tab Default) ada di spec 007.
- Temuan untuk QA:
  - TC-AC-PF-30 dan TC-AC-PF-31: Expected c menyebut "state list dipertahankan" tetapi langkah TC tidak mengatur state apa pun sebelum Plan Detail dibuka sehingga asersi tidak dapat gagal; spec memasang Search sebagai state pengamatan.
  - TC-AC-PF-30 dan TC-AC-PF-31: Expected d menyebut klik `Plans & Features` pada Plan Detail Custom membuka Default > Active (bukan tab Custom), mengikuti TC; mohon QA mengonfirmasi tujuan segmen itu untuk plan Custom.
