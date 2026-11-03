---
id: TC-AC-PF-E2E-034-capability-tunggal-principal-create-only-membuat-custom
title: Capability Tunggal Principal Create-Only - Membuat Custom Plan dan Default Plan
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-PF-80
  - TC-AC-PF-84
coverage:
  web: automated
---

# Capability Tunggal Principal Create-Only - Membuat Custom Plan dan Default Plan

## Prerequisites

- Mode: FE+BE
- Akun aktor: #3 `createOnlyPrincipal_automated_{namaCompany}@qwertysystem.net` (Create-Only, Principal: Manage plans & licensing Read dan Create; password dari env `AC_PF_CO_PASSWORD`).
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Flag Guided Tooltip mengikuti pernyataan di `suite.md` (hook suite menyetel flag true untuk akun aktor pre-setup).
- Data Pre-setup: Dataset Plan A (template `Growth` pada Product FAMS), Dataset Plan T (Product SAMS dengan 3 Paid aktif `Supply Tiga A`, `Supply Tiga B`, `Supply Tiga C` dan tanpa Free). Spec mengubah state default plan SAMS (slot Free terisi plan buatan spec); nama literal Pre-setup memakai pengecualian S-06/S-12 butir A-14, dan pemulihan Dataset Plan T dijamin fixture backend (disediakan tim FE/BE, idempoten) di hook `before` dan `after`.
- Data Dinamis (bersuffix per run): custom plan `Paket Create Only {runId}-034` (Product FAMS, Template Growth) dan default plan `Supply Gratis {runId}-034` (Product SAMS, Pricing Type Free). Keduanya dibuang di hook `after` lewat fixture BE (archive lalu Delete) bila ada.
- Kemampuan teknis (disediakan tim FE/BE, dinyatakan di `suite.md`): fixture backend untuk pemulihan Dataset Plan T dan penghapusan plan buatan spec. Fixture data `fixtures/plans-licensing-plans-features.json` belum ada (S-12).
- State global: slot default plan SAMS dan entri Changelog Default dan Custom (permanen); suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AC-PF-80: Create-Only Principal membuat custom plan

1. Klik tab Custom.
2. Klik `+ Custom Plan`.
3. Pilih Product `FAMS`.
4. Pilih Template `Growth`.
5. Isi Plan Name `Paket Create Only {runId}-034`.
6. Klik `[Submit]`.
7. Verifikasi muncul toast sukses: "Success, custom plan has been created."
8. Verifikasi halaman Plans & Licensing > Plans & Features > Custom > Active > Detail untuk `Paket Create Only {runId}-034` terbuka dengan judul `Paket Create Only {runId}-034 – v1`.

### TC-AC-PF-84: Create-Only Principal membuat default plan Free SAMS

9. Kembali ke list lewat Breadcrumb.
10. Klik tab Default.
11. Klik `+ Default Plan`.
12. Pilih Product `SAMS`.
13. Isi Plan Name `Supply Gratis {runId}-034`.
14. Pilih Pricing Type `Free`.
15. Klik `[Submit]`.
16. Verifikasi muncul toast sukses: "Success, default plan has been created."
17. Verifikasi halaman Plans & Licensing > Plans & Features > Default > Active > Detail untuk `Supply Gratis {runId}-034` terbuka dengan judul `Supply Gratis {runId}-034 – v1`.

## Notes

- Langkah penghubung (S-03): langkah 1 dan 10 (pindah tab) dan langkah 9 (kembali ke list).
- Plan Name memakai suffix `{runId}-034` (S-12); nilai Expected judul TC (`Paket Create Only – v1`, `Supply Gratis – v1`) ditulis dengan nama bersuffix yang sama.
- Temuan untuk QA:
  - TC-AC-PF-84 precondition "Dataset Plan T tersedia (SAMS tanpa plan Free)" dan Pre-setup #31 (Dataset Plan S memuat `Supply Starter` Free SAMS) mendefinisikan state SAMS yang berbeda; spec memakai Dataset Plan T dengan pemulihan fixture BE.
  - Post Condition TC-AC-PF-80 dan TC-AC-PF-84 tanpa langkah observasi tidak diasersi (S-01).
