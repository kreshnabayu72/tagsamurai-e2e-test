---
id: TC-FA-FAAM-E2E-138-notice-category-locked-bentuk-tunggal
title: "Notice Category Locked: Bentuk Tunggal dan Show only this"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAM-688
  - TC-FA-FAAM-692
coverage:
  web: automated
---

# Notice Category Locked: Bentuk Tunggal dan Show only this

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control client `AutoLocked1` (Pre-setup #12d); email akun tidak tertulis di Pre-setup TC (lihat Temuan untuk QA); password `Spectra.env.FA_TC_LOCKED1_PASSWORD` (nama env baru didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Data Pre-setup (client `AutoLocked1`, Pre-setup #12d; tidak diubah spec ini; `Fixture.faSettingsAssetName.autoLocked1`, fixture baru belum ada): tepat 1 Asset Name Category Locked `Solo Locked Item` (Category internal `Electronics`, Total Asset 0); hitungan Needs Update 1.
- Hook suite: lihat `suite.md` (hook `before`, `beforeEach`, `after`, sesi API aktor, dan seed API per TC; kemampuan disediakan tim BE/FE).
- State global: tidak ada yang diubah spec ini. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-FAAM-688: Notice Category Locked bentuk tunggal untuk satu Asset Name
1. Perhatikan notice di atas tabel
2. Verifikasi Alert Warning dengan teks `1 asset name needs a category update.`
3. Verifikasi aksi tautan `Show only this`
### TC-FA-FAAM-692: Show only this memasang quick filter untuk satu Asset Name Category Locked
4. Klik `Show only this` pada notice
5. Verifikasi tabel hanya memuat `Solo Locked Item`
6. Verifikasi chip `Needs Update` dengan `✕` tampil
7. Verifikasi notice berubah menjadi `Showing 1 asset name that needs a category update.`
8. Verifikasi notice memuat aksi `Clear filter`
9. Klik `Clear filter`

## Notes

- Langkah penghubung (aksi tanpa `Verifikasi`): `Clear filter` terakhir yang melepas quick filter.
- Temuan untuk QA: Pre-setup #12d berupa client tanpa baris akun Total Control (email tidak tertulis).
