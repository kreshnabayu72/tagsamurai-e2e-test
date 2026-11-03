---
id: TC-AC-DC-E2E-019-role-matrix-positif-add-create-only
title: "Role Matrix Positif: Add Subcategory untuk Create-Only"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DC-53
  - TC-AC-DC-61
coverage:
  web: automated
---
# Role Matrix Positif: Add Subcategory untuk Create-Only

## Prerequisites

- Mode: FE+BE.
- Aktor: Create-Only (Pre-setup #4); Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Settings > Device > Device Name).

| Role yang diuji | Akun (Pre-setup) | Password |
|---|---|---|
| Create-Only (Manage device master data: Create + Read) | #4 `manageDeviceC_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.AC_DC_CREATE_PASSWORD` |

- Data Dinamis (dibuat spec ini lewat API di hook `before` oleh Total Control #1 lewat sesi API aktor, di bawah `Handheld Reader`): node `Pemindai Uji {runId}-019` (leaf, target TC-AC-DC-53). Nama node yang dibuat aksi UI: `Wearable Scanner {runId}-019` dan `Pemindai Genggam Baru {runId}-019`.
- Data Pre-setup: #14 (Pohon Uji Kategori, hanya dibaca). Nilai data mengacu ke fixture `settingsDeviceCategory` (belum ada; disediakan tim FE). Nama node Pre-setup #14 ditulis sebagaimana di TC.
- Kemampuan teknis: sesi API aktor (login API password untuk akun yang sama dengan sesi UI, tidak dihitung sebagai sesi web) dan klien HTTP; disediakan tim BE/FE dan dinyatakan di `suite.md`.
- Hook `after`: menghapus semua node (dan Device Name) yang dibuat spec ini, termasuk node hasil aksi UI yang dikenali dari sufiks `{runId}-019`, lewat API dari anak ke induk; cleanup tidak berasumsi seeding berhasil penuh.
- Seeding dan cleanup menambah entri Changelog dan log audit permanen (Create dan Delete atas node bersufiks); entri itu tidak diasersi.
- Env var `AC_TC_PASSWORD` sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example`. Env var `AC_DC_CREATE_PASSWORD` belum terdaftar: perlu didaftarkan tim FE di `spectra.config.ts` (`executionConfig.environmentVariables`) dan `.env.example`.
- Suite berjalan serial (`parallel: false`): pohon Category, Changelog, dan log audit adalah state bersama.

## Test Steps

### TC-AC-DC-53: Create-Only: hanya + Subcategory tampil dan Add berhasil dieksekusi

1. Expand `Hardware` lalu `Handheld Reader`
2. Hover node `Pemindai Uji {runId}-019`
3. Verifikasi aksi `+ Subcategory` tampil
4. Verifikasi aksi Edit dan Delete Hidden
5. Klik `+ Subcategory`
6. Ketik "Wearable Scanner {runId}-019"
7. Klik `[Submit]`
8. Verifikasi toast sukses "Success, category has been created." tampil
9. Verifikasi node `Wearable Scanner {runId}-019` muncul di bawah `Pemindai Uji {runId}-019`
10. Verifikasi tree tetap tampil
11. Verifikasi ikon Changelog tetap tampil
12. Tunggu toast sebelumnya hilang otomatis

### TC-AC-DC-61: Create-Only: node hardcoded perantara menampilkan + Subcategory dan Add berhasil

13. Hover node `Handheld Reader`
14. Verifikasi hanya aksi `+ Subcategory` tampil pada `Handheld Reader`
15. Klik `+ Subcategory`
16. Ketik "Pemindai Genggam Baru {runId}-019"
17. Klik `[Submit]`
18. Verifikasi toast sukses "Success, category has been created." tampil
19. Verifikasi node `Pemindai Genggam Baru {runId}-019` muncul di bawah `Handheld Reader`

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-device-category/TestCases/tc-settings-device-category.md`.
- Subjudul `###` memetakan langkah ke id TC granular.
- Spec Role Matrix positif satu role (Create-Only) untuk aksi Add (bagian 3a).
- Langkah penghubung: langkah 1 (expand tree) dan 12 (menunggu toast TC-AC-DC-53 hilang sebelum toast serupa TC-AC-DC-61 diasersi, R-12).
- Temuan untuk QA:
  - Target aksi tulis dan hapus memakai node milik spec bersufiks `{runId}-019` (S-06, S-12); TC memakai node literal Pre-setup #14 (`Rugged Scanner` pada TC-AC-DC-53 dan nama "Wearable Scanner" serta "Pemindai Genggam Baru" pada Data Uji; nama yang diketik diberi sufiks `{runId}-019`) sebagai target. Hasil TC identik karena node milik spec adalah node user-created dengan perilaku yang sama; node literal Pre-setup hanya dibaca.
  - Catatan TC menyebut data destruktif dipulihkan automation baseline sebelum tiap TC; spec ini tidak mengandalkannya dan membersihkan datanya sendiri di `after`.
  - Post Condition TC-AC-DC-53 dan 61 ('-') tidak punya langkah observasi dan tidak diasersi.
