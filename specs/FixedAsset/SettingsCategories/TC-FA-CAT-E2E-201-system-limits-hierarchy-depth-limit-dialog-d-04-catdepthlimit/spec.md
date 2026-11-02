---
id: TC-FA-CAT-E2E-201-system-limits-hierarchy-depth-limit-dialog-d-04-catdepthlimit
title: "System Limits: Dialog D-04 Hierarchy Depth Limit Tercapai pada Client CatDepthLimit"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-CAT-127
coverage:
  web: automated
---

# System Limits: Dialog D-04 Hierarchy Depth Limit Tercapai pada Client CatDepthLimit

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net` pada client CatDepthLimit (Pre-setup #30, plan Enterprise, Hierarchy Depth Limit 5, rantai `Depth 1` sampai `Depth 5`), password dari `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (CatMain). Tidak ada ganti akun di tengah spec.
- Env var `FA_TC_PASSWORD` didaftarkan di `executionConfig.environmentVariables` dan `.env.example` (nama usulan, lihat Temuan untuk QA).
- Data Pre-setup #30 (CatDepthLimit), dibaca: rantai `Depth 1` > `Depth 2` > `Depth 3` > `Depth 4` > `Depth 5` (depth ke-5, sama dengan Hierarchy Depth Limit). Base limit client CatDepthLimit adalah 5 (Pre-setup #30); spec 044 memakai varian limit 6 hanya untuk TC-FA-CAT-529 dan memulihkannya ke 5, tetapi urutan spec tidak dijamin. Karena itu hook `before` spec ini menyetel Hierarchy Depth Limit CatDepthLimit ke 5 lewat fixture atau kemampuan System Limits yang disediakan tim FE/BE (tanpa endpoint karangan), sehingga dialog D-04 selalu muncul. Spec tidak mengubah data lain.
- Flag Guided Tooltip halaman Categories: hook suite `before` men-set true untuk akun aktor dan `after` memulihkannya (butir "Flag Guided Tooltip" di `suite.md`).
- Fixture `fixtures/settings-categories.json` disediakan tim FE.

## Test Steps

### TC-FA-CAT-127: Hierarchy Depth Limit tercapai, dialog D-04

1. Expand rantai `Depth 1` sampai `Depth 5` di Sidebar Category Tree dan klik node `Depth 4`
2. Klik elipsis (⋯) pada baris `Depth 5` (depth ke-5) > `+ Add Subcategory`
3. Verifikasi dialog 🔒 `Cannot Add Category` dengan body `You've reached the platform limit of 5 levels. Contact support if you need a higher limit.` dan tombol `[OK]` tampil
4. Verifikasi dialog tanpa CTA upgrade
5. Klik `[OK]`

## Notes

- Data ringan (rantai depth 5 pada client CatDepthLimit), satu TC, berdiri sendiri dengan login client sendiri dan penyetelan Hierarchy Depth Limit 5 di hook `before`. Limit sudah 5 sesuai Pre-setup #30, sehingga tidak ada pemulihan tambahan.
- Langkah penghubung (S-03): langkah 1 (expand rantai dan memilih node induk) dan langkah 5 (menutup dialog).
- Temuan untuk QA:
  - TC-127 tidak menyebut akun dan client login; spec memakai Total Control pada client CatDepthLimit sesuai Pre-setup #30.
  - Nama env var password aktor tidak tertulis di TC; `FA_TC_PASSWORD` adalah usulan.
