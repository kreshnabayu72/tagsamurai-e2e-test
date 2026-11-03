---
id: TC-AC-PF-E2E-203-screening-dan-filter-panel-modal-changelog-global-settings
title: Screening modal Changelog Global Settings dan Filter Panel tanpa field Action
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-PF-500
  - TC-AC-PF-501
coverage:
  web: automated
---

# Screening modal Changelog Global Settings dan Filter Panel tanpa field Action

## Prerequisites

- Mode: FE+BE
- Akun aktor: #1 `totalControlPrincipal_automated_{namaCompany}@qwertysystem.net` (nama tampil Andi Wijaya; entitas Principal; Global Role Manage plans & licensing Create, Read, Update, Delete); password `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Env: `AC_TC_PASSWORD` (password Total Control Principal).
- Data Pre-setup: Dataset Log G, Changelog Global Settings lima entri, terbaru dahulu: `30 Jun 26, 11:21` Edit `Max depreciation methods (Multi Depreciation tier)` (Old `3`, New `4`, John D); `30 Jun 26, 11:20` Edit `Max custom fields per asset name` (Old `8`, New `10`, John D); `22 Jun 26, 09:05` Edit `Max custom fields per asset name` (Old `5`, New `8`, Sarah T); `15 Jun 26, 14:40` Edit `Max depreciation methods (Multi Depreciation tier)` (Old `2`, New `3`, Sarah T); `02 Jun 26, 10:00` Edit `Max custom fields per asset name` (Old `3`, New `5`, John D). Nilai data dirujuk lewat `fixtures/plans-licensing-plans-features.json` (belum ada; ditandai untuk tim FE, S-12).
- General Settings akun: Date Format `dd MMM yy`, Time Format 24-hour, Time Zone UTC; tidak diubah spec ini.
- Pengecualian S-06/S-12 butir A-14: dataset memakai nama literal tanpa suffix dari Pre-setup TC. Fixture BE yang disediakan tim FE/BE (idempoten) menyetel Changelog Global Settings Principal tepat sama dengan Dataset Log G di hook `before` dan memulihkannya ke baseline di hook `after`; suite berjalan serial (`parallel: false`). Spec ini hanya membaca data itu.
- Kemampuan teknis (disediakan tim FE/BE): fixture BE penyetel Changelog; sesi API aktor, klien HTTP, dan flag Guided Tooltip sesuai pernyataan di `suite.md`.
- State global: tidak ada yang diubah spec ini.

## Test Steps

### Screening modal Changelog Global Settings (TC-AC-PF-500)

1. Klik tab Global Settings
2. Klik ikon Changelog di pojok kanan atas Card
3. Verifikasi Title modal `Changelog: Plans & Features > Global Settings`
4. Verifikasi Table Tools `Search`, `Filter`, `Download` tampil
5. Verifikasi kolom `Date`, `Action`, `Field`, `Old Value`, `New Value`, `Modified By` bersifat sortable
6. Verifikasi kolom `Column Visibility (⋯)` tampil di ujung kanan header
7. Verifikasi tidak ada kolom Plan Name
8. Verifikasi entri pertama: `30 Jun 26, 11:21` | `Edit` | `Max depreciation methods (Multi Depreciation tier)` | `3` | `4` | `John D`
9. Verifikasi entri kedua: `30 Jun 26, 11:20` | `Edit` | `Max custom fields per asset name` | `8` | `10` | `John D`
10. Verifikasi entri ketiga: `22 Jun 26, 09:05` | `Edit` | `Max custom fields per asset name` | `5` | `8` | `Sarah T`
11. Verifikasi entri keempat: `15 Jun 26, 14:40` | `Edit` | `Max depreciation methods (Multi Depreciation tier)` | `2` | `3` | `Sarah T`
12. Verifikasi entri kelima: `02 Jun 26, 10:00` | `Edit` | `Max custom fields per asset name` | `3` | `5` | `John D`
13. Verifikasi Old Value dan New Value berupa bilangan bulat tanpa pemisah ribuan
14. Tutup modal dengan icon (X)

### Filter Panel tanpa field Action (TC-AC-PF-501)

15. Klik ikon Changelog di pojok kanan atas Card
16. Klik ikon Filter
17. Verifikasi Filter Panel memuat `Date` (`Select date`), `Field` (multi-select searchable, `All fields`), dan `Modified By` (multi-select searchable, `All users`)
18. Verifikasi Filter Panel tidak memuat field Action
19. Tutup Filter Panel
20. Ketik Search `edit`, tekan Enter
21. Verifikasi kelima baris cocok dengan Search `edit` (kolom Action Searchable)

## Notes

- Langkah penghubung (S-03): penutupan modal dengan icon (X) dan penutupan Filter Panel sebelum Search.
- Anchor absence (bagian 8b butir 2): Verifikasi kolom langkah 5 dan 6 mendahului langkah 7; Verifikasi field Filter Panel pada langkah 17 mendahului langkah 18.
- Pembagian TC lintas spec: TC-AC-PF-495 dan TC-AC-PF-496 (modal Changelog Custom) ada di spec 179.
- Temuan untuk QA: TC menetapkan lima entri sebagai seluruh isi Changelog Global Settings. Changelog adalah audit trail permanen (S-12), sehingga asersi ini bergantung pada fixture BE penyetel log yang tidak tertulis di TC, PRD, atau LLD (S-13).
