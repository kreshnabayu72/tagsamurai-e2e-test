---
id: TC-FA-CAT-E2E-187-bulk-delete-baris-excess-ikut-terhapus
title: "Bulk Delete: Baris Excess Dapat Dicentang dan Ikut Terhapus pada Client CatExcess"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CAT-260
coverage:
  web: automated
---

# Bulk Delete: Baris Excess Dapat Dicentang dan Ikut Terhapus pada Client CatExcess

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net` pada client CatExcess (Pre-setup #31), password dari `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite.
- Data Pre-setup #31 (CatExcess, cap 5, 9 kategori): Excess `Heavy Equipment` dan `Vehicle` (Total Asset 0) dihapus oleh spec ini. Kondisi Excess bergantung pada seluruh isi client sehingga tidak dapat dimiliki spec; pemulihan lewat fixture backend yang disediakan tim FE/BE, dijalankan di hook `before` dan `after`; efeknya (Changelog dan Last Updated) dicatat sebagai efek spec ini. Suite berjalan serial (`parallel: false`).
- Seed dan pemulihan client Pre-setup mengikuti butir "Seed dan pemulihan lewat API" di `suite.md`; flag Guided Tooltip mengikuti hook suite.
- Env var `FA_TC_PASSWORD` didaftarkan di `executionConfig.environmentVariables` dan `.env.example`.

## Test Steps

### TC-FA-CAT-260: Baris Excess dapat dicentang dan ikut Bulk Delete

1. Centang checkbox baris `Heavy Equipment` dan `Vehicle`
2. Verifikasi checkbox baris Excess `Heavy Equipment` dan `Vehicle` aktif (tidak disabled)
3. Klik `[Delete]` pada Bulk Action Bar
4. Klik `[Delete]` pada dialog
5. Verifikasi toast `Success, category has been deleted.`

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-categories/TestCases/tc-settings-categories.md`.
- Pembagian TC lintas spec: TC-FA-CAT-260 ada di spec ini karena memakai client CatExcess, sedangkan TC Bulk Delete lain pada seri yang sama memakai client CatMain.
- Temuan untuk QA:
  - Teks dialog Bulk Delete untuk seleksi Excess tidak tertulis di TC-FA-CAT-260; spec hanya meng-assert toast.
  - Expected TC-FA-CAT-260 menyebut keduanya ikut Bulk Delete namun hanya mengasersi toast; spec tidak menambah asersi baris hilang.
