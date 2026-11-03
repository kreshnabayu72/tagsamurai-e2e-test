---
id: TC-AC-PF-E2E-182-filter-modal-changelog-default-screening-dan-multi-select
title: Filter modal Changelog Default screening Filter Panel, multi-select, dan rentang Date inklusif
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-PF-464
  - TC-AC-PF-465
  - TC-AC-PF-466
  - TC-AC-PF-467
coverage:
  web: automated
---

# Filter modal Changelog Default screening Filter Panel, multi-select, dan rentang Date inklusif

## Prerequisites

- Mode: FE+BE
- Akun aktor: #1 `totalControlPrincipal_automated_{namaCompany}@qwertysystem.net` (nama tampil Andi Wijaya; entitas Principal; Global Role Manage plans & licensing Create, Read, Update, Delete); password `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Env: `AC_TC_PASSWORD` (password Total Control Principal).
- Data Pre-setup: Dataset Log D, Changelog Default Principal lima entri, terbaru dahulu: `12 Aug 26, 09:00` Create `Enterprise` (Plan Name, Old `—`, New `Enterprise`, Jane S); `01 Aug 26, 08:00` Archive `Growth Plus (old)` (Status, Old `Active`, New `Archived`, Jane S); `20 Jul 26, 10:00` Push Update `PT Wahana Nusantara` (Plan Version, Old `v1`, New `v5`, Sarah T); `10 Jul 26, 12:00` Delete `Pilot Default` (Plan Name, Old `Pilot Default`, New `—`, John D); `05 Jun 26, 15:40` Edit `Growth` (Group count, Old `3`, New `5`, Jane S). Modified By Jane S = Jane Smith. Nilai data dirujuk lewat `fixtures/plans-licensing-plans-features.json` (belum ada; ditandai untuk tim FE, S-12).
- General Settings akun: Date Format `dd MMM yy`, Time Format 24-hour, Time Zone UTC; tidak diubah spec ini.
- Pengecualian S-06/S-12 butir A-14: dataset memakai nama literal tanpa suffix dari Pre-setup TC. Fixture BE yang disediakan tim FE/BE (idempoten) menyetel Changelog Principal tepat sama dengan Dataset Log D di hook `before` dan memulihkannya ke baseline di hook `after`; suite berjalan serial (`parallel: false`). Spec ini hanya membaca data itu.
- Kemampuan teknis (disediakan tim FE/BE): fixture BE penyetel Changelog; sesi API aktor, klien HTTP, dan flag Guided Tooltip sesuai pernyataan di `suite.md`.
- State global: tidak ada yang diubah spec ini.

## Test Steps

### Screening Filter Panel (TC-AC-PF-464)

1. Klik ikon Changelog pada toolbar tab Default
2. Klik ikon Filter
3. Verifikasi Filter Panel memuat `Date` (date range picker, placeholder `Select date`), `Action` (multi-select searchable, `All actions`), `Plan Name` (multi-select searchable, `All plans`), `Field` (multi-select searchable, `All fields`), dan `Modified By` (multi-select searchable, `All users`)
4. Verifikasi tombol `[Clear Field]` dan `[Apply]` tampil

### Filter Action multi-select (TC-AC-PF-465)

5. Pilih Action `Archive`, klik `[Apply]`
6. Verifikasi satu baris `Growth Plus (old)`
7. Buka Filter Panel, tambahkan Action `Delete`, klik `[Apply]`
8. Verifikasi dua baris `Growth Plus (old)` dan `Pilot Default` (logika OR)

### Filter Plan Name, Field, dan Modified By (TC-AC-PF-466)

9. Buka Filter Panel, klik `[Clear Field]`, pilih Plan Name `Growth`, klik `[Apply]`
10. Verifikasi baris `Edit Growth`
11. Buka Filter Panel, klik `[Clear Field]`, pilih Field `Plan Version`, klik `[Apply]`
12. Verifikasi baris `Push Update`
13. Buka Filter Panel, klik `[Clear Field]`, pilih Modified By `Jane Smith`, klik `[Apply]`
14. Verifikasi tiga baris (`Create`, `Archive`, `Edit`)

### Filter Date inklusif (TC-AC-PF-467)

15. Buka Filter Panel, klik `[Clear Field]`, pilih rentang `10 Jul 26` sampai `01 Aug 26`, klik `[Apply]`
16. Verifikasi tiga entri `Archive` (01 Aug), `Push Update` (20 Jul), dan `Delete` (10 Jul) dengan batas inklusif

## Notes

- Langkah penghubung (S-03): `[Clear Field]` pada langkah 9, 11, 13, dan 15 mengganti filter sebelumnya sehingga "ganti ke" pada TC-AC-PF-466 tidak menumpuk dengan filter blok sebelumnya.
- Temuan untuk QA: TC menetapkan lima baris sebagai seluruh isi Changelog Default. Changelog adalah audit trail permanen (S-12), sehingga asersi bergantung pada fixture BE penyetel log yang tidak tertulis di TC, PRD, atau LLD (S-13).
