---
id: TC-FA-CAT-E2E-016-role-matrix-negatif-read-only-dan-scope-group-manager
title: "Role Matrix Negatif: Read Only Tanpa Aksi Tulis dan Group Manager Melihat Seluruh Pohon Client"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-CAT-49
  - TC-FA-CAT-57
coverage:
  web: automated
---

# Role Matrix Negatif: Read Only Tanpa Aksi Tulis dan Group Manager Melihat Seluruh Pohon Client

## Prerequisites

- Mode: FE+BE. Backend nyata; tidak ada respons yang dipaksa lewat `Spectra.intercept()`.
- Role yang diuji (bagian 3a; langkah tiap role berbeda sehingga spec ditulis per blok role):

| Role | Pre-setup | Akun | Password | Client |
|---|---|---|---|---|
| Read Only | #2 | `Fixture.settingsCategories.readOnly` (`readOnly_automated_{namaCompany}@qwertysystem.net`) | `Spectra.env.FA_RO_PASSWORD` | CatMain (Pre-setup #20) |
| Group Manager Capability CRUD (Manage Asset Master Data: C, R, U, D) | #9 | `Fixture.settingsCategories.gmCapability` (`gmCapability_automated_{namaCompany}@qwertysystem.net`) | `Spectra.env.FA_GMCAP_PASSWORD` | CatMain (Pre-setup #20) |

- Login di hook `before` spec ini sebagai Read Only; halaman dibuka hook `beforeEach` suite. Ganti akun ke Group Manager Capability CRUD memakai langkah eksplisit. Hook `after` mengembalikan sesi ke akun default suite (Total Control).
- Env var `FA_RO_PASSWORD` dan `FA_GMCAP_PASSWORD` didaftarkan di `executionConfig.environmentVariables` dan `.env.example` (nama usulan; keputusan tim).
- Data Pre-setup: client CatMain (Pre-setup #20) dengan 15 kategori seed; spec hanya membaca. Spec mengandalkan pohon CatMain dalam keadaan seed (tanpa kategori tambahan dari spec lain).
- Spec ini tidak membuat atau mengubah data.
- Seed dan pemulihan lewat API, flag Guided Tooltip, dan hook suite lain: lihat `suite.md`.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-CAT-49: Read Only tidak dapat menjalankan aksi tulis dan tetap dapat membuka Detail dan Changelog

1. Klik elipsis (⋯) baris `Furniture`
2. Verifikasi menu baris memuat Detail
3. Verifikasi Edit, + Add Subcategory, dan Delete Hidden
4. Klik `Detail`
5. Verifikasi popup Category Detail terbuka
6. Klik icon close (✕) pada popup Category Detail
7. Klik icon Changelog
8. Verifikasi modal `Changelog: Category` terbuka
9. Tutup modal `Changelog: Category`

### TC-FA-CAT-57: Aktor pemegang capability melihat seluruh pohon client tanpa scoping group

10. Ganti akun: Logout, lalu login sebagai Group Manager Capability CRUD (Pre-setup #9)
11. Buka Fixed Asset > Settings > Categories
12. Klik toggle expand-all pada sidebar
13. Verifikasi sidebar memuat 15 kategori yang sama dengan Total Control
14. Verifikasi tidak ada node yang disembunyikan karena group aktor: `Default Category`, `Electronics`, `Laptop`, `Monitor`, `Furniture`, `Peripheral`, `Keyboard`, `Mouse`, `Accessory`, `Cable`, `Tools`, `Vehicle`, `Spare Part`, `Bolt`, dan `Bolt M8` tampil

## Notes

- Sumber: `fixed-asset/settings-categories/TestCases/tc-settings-categories.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Spec per blok role dengan langkah ganti akun eksplisit (bagian 3a, KEPUTUSAN 2026-10-30): langkah tiap blok berbeda dan akun pertama login di hook `before`. TC-FA-CAT-57 bersifat positif (pohon tampil penuh) tetapi berada di spec ini karena membahas scope Group Manager yang sama dengan TC-FA-CAT-49 (role tanpa aksi tulis).
- Langkah penghubung (S-03): langkah 6 dan 9 (menutup popup dan modal sebelum langkah berikutnya), langkah 10 dan 11 (ganti akun dan membuka halaman, karena hook `beforeEach` hanya membuka halaman untuk akun pertama).
- Menu baris Read Only diasersi lewat anchor positif Detail (langkah 2) sebelum absence Edit, + Add Subcategory, dan Delete (langkah 3), sesuai 8b butir 2.
- Temuan untuk QA:
  - TC-FA-CAT-57 Expected "sama dengan Total Control" tidak punya langkah login Total Control sebagai pembanding; spec mengasersi 15 nama kategori seed Pre-setup #20 dan tidak membandingkan dengan sesi Total Control.
  - TC-FA-CAT-49 dan TC-FA-CAT-57 menyebut baris seed `Furniture` dan pohon seed; spec hanya membaca sehingga tidak menyentuh S-06.
