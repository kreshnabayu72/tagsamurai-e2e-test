---
id: TC-AC-PF-E2E-202-pagination-modal-changelog-global-settings-dan-archive
title: Pagination modal Changelog Global Settings, Default Archive, Custom Archive, dan modal Changelog Custom
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-PF-516
  - TC-AC-PF-629
coverage:
  web: automated
---

# Pagination modal Changelog Global Settings, Default Archive, Custom Archive, dan modal Changelog Custom

## Prerequisites

- Mode: FE+BE
- Akun aktor: #1 `totalControlPrincipal_automated_{namaCompany}@qwertysystem.net` (nama tampil Andi Wijaya; entitas Principal; Global Role Manage plans & licensing Create, Read, Update, Delete); password `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Env: `AC_TC_PASSWORD` (password Total Control Principal).
- Data Pre-setup: Dataset Log GBig (Changelog Global Settings Principal 30 entri); Dataset Plan AR (12 default plan FAMS Paid archived tidak pernah dipakai `Arsip Default 01` sampai `Arsip Default 12`, dan 12 custom plan archived milik Principal tidak pernah dipakai `Arsip Kustom 01` sampai `Arsip Kustom 12`); Dataset Log C12 (Changelog Custom Principal 12 entri). Nilai data dirujuk lewat `fixtures/plans-licensing-plans-features.json` (belum ada; ditandai untuk tim FE, S-12).
- General Settings akun: Date Format `dd MMM yy`, Time Format 24-hour, Time Zone UTC; tidak diubah spec ini.
- Pengecualian S-06/S-12 butir A-14: dataset memakai nama literal tanpa suffix dari Pre-setup TC. Fixture BE yang disediakan tim FE/BE (idempoten) menyetel Changelog Global Settings Principal tepat sama dengan Dataset Log GBig, Changelog Custom Principal tepat sama dengan Dataset Log C12, dan menyediakan Dataset Plan AR di hook `before`, dan memulihkan semuanya ke baseline di hook `after`; suite berjalan serial (`parallel: false`). Spec ini hanya membaca data itu.
- Kemampuan teknis (disediakan tim FE/BE): fixture BE penyetel Changelog dan penyedia Dataset Plan AR; sesi API aktor, klien HTTP, dan flag Guided Tooltip sesuai pernyataan di `suite.md`.
- State global: tidak ada yang diubah spec ini.

## Test Steps

### Pagination modal Changelog Global Settings (TC-AC-PF-516)

1. Klik tab Global Settings
2. Klik ikon Changelog di pojok kanan atas Card
3. Verifikasi footer `Showing 1–10 of 30 entries`
4. Klik Next
5. Verifikasi footer `Showing 11–20 of 30 entries`
6. Buka Overlay Page Size
7. Verifikasi Overlay Page Size memuat `10`, `25`, `50`, `100`
8. Tutup Overlay Page Size, lalu tutup modal dengan icon (X)

### Pagination Default Archive (TC-AC-PF-629 butir a)

9. Klik tab Default, lalu klik sub-tab Archive
10. Verifikasi footer halaman 1 `Showing 1–10 of 12 entries`
11. Klik Next
12. Verifikasi footer `Showing 11–12 of 12 entries`
13. Buka Overlay Page Size
14. Verifikasi Overlay Page Size memuat `10`, `25`, `50`, `100`

### Pagination Custom Archive (TC-AC-PF-629 butir b)

15. Tutup Overlay Page Size, lalu klik tab Custom dan sub-tab Archive
16. Verifikasi footer halaman 1 `Showing 1–10 of 12 entries`
17. Klik Next
18. Verifikasi footer `Showing 11–12 of 12 entries`
19. Buka Overlay Page Size
20. Verifikasi Overlay Page Size memuat `10`, `25`, `50`, `100`

### Pagination modal Changelog Custom (TC-AC-PF-629 butir c)

21. Tutup Overlay Page Size, lalu klik ikon Changelog pada toolbar
22. Verifikasi footer halaman 1 `Showing 1–10 of 12 entries`
23. Klik Next
24. Verifikasi footer `Showing 11–12 of 12 entries`
25. Buka Overlay Page Size
26. Verifikasi Overlay Page Size memuat `10`, `25`, `50`, `100`

## Notes

- Langkah penghubung (S-03): langkah 8, 15, dan 21 menutup Overlay Page Size (dan modal pada langkah 8) sebelum blok berikutnya.
- TC-AC-PF-629 mencakup tiga surface; seluruhnya ada di spec ini.
- Temuan untuk QA:
  - TC-AC-PF-516 dan TC-AC-PF-629 menetapkan 30 dan 12 entri sebagai seluruh isi Changelog. Changelog adalah audit trail permanen (S-12), sehingga asersi bergantung pada fixture BE penyetel log yang tidak tertulis di TC, PRD, atau LLD (S-13).
  - Dataset Log GBig, Log C12, dan Dataset Plan AR dipakai bersama pada spec ini dengan state Changelog Principal yang berbeda dari spec lain; hook `before` dan `after` fixture menjadi satu-satunya penjamin isolasi antar spec.
