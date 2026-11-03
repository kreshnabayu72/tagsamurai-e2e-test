---
id: TC-FA-FAAM-E2E-165-changelog-empty-state-client-tanpa-entri
title: "Modal Changelog: Empty State pada Client Tanpa Entri Changelog"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAM-466
coverage:
  web: automated
---

# Modal Changelog: Empty State pada Client Tanpa Entri Changelog

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control pada client tanpa Asset Name, tanpa Changelog, dan tanpa kategori (Pre-setup #16b), dirujuk lewat fixture baru `Fixture.faAssetName.emptyClient`. Email akun ini tidak tertulis di Pre-setup TC (lihat Temuan untuk QA); akun disediakan tim FE. Password `Spectra.env.FA_TC16B_PASSWORD` (nama env baru didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Hook suite: lihat `suite.md` (hook `before`, `beforeEach`, `after`; kemampuan disediakan tim BE/FE).
- State global: tidak ada yang diubah. Client ini tidak dipakai spec lain dan tidak diisi data oleh spec ini. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-FAAM-466: Changelog kosong menampilkan empty state genuinely

1. Klik icon Changelog
2. Verifikasi empty state dengan title `No changelog yet` dan deskripsi `Activities and changes will appear here.`

## Notes

- Pembagian TC lintas spec: TC-FA-FAAM-466 memakai client lain daripada TC Modal Changelog lain, sehingga ia berdiri sendiri; TC Modal Changelog lain ada di spec 147 sampai 156.
- Temuan untuk QA:
  - TC-FA-FAAM-466 memuat ACC `#16` (client `AutoStarter` plan Starter dengan 10 Asset Name), sedangkan Precondition menyebut `#16b` (client tanpa Asset Name dan Changelog). Spec mengikuti Precondition.
  - Email akun Total Control untuk client #16b tidak tertulis di Pre-setup TC.
