---
id: TC-AC-DC-E2E-018-role-matrix-visibilitas-aksi-per-role
title: "Role Matrix: Visibilitas Aksi Node Category untuk Total Control, Default User, dan Full CRUD"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DC-43
  - TC-AC-DC-50
  - TC-AC-DC-51
  - TC-AC-DC-56
coverage:
  web: automated
---
# Role Matrix: Visibilitas Aksi Node Category untuk Total Control, Default User, dan Full CRUD

## Prerequisites

- Mode: FE+BE.
- Aktor pertama: Total Control (Pre-setup #1); Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Settings > Device > Device Name). Ganti akun eksplisit di tengah spec ke Default User (#2), lalu ke Full CRUD (#7). Hook `after` mengembalikan sesi ke akun default suite.

| Role yang diuji | Akun (Pre-setup) | Password |
|---|---|---|
| Total Control (`Budi Santoso`) | #1 `totalControlDevCat_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.AC_TC_PASSWORD` |
| Default User (`Dewi Lestari`) | #2 `defaultUserDevCat_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.AC_DC_DEFAULT_PASSWORD` |
| Full CRUD (Manage device master data: Create + Update + Delete + Read, role custom) | #7 `manageDeviceCUD_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.AC_DC_CUD_PASSWORD` |

- Data Pre-setup: #14 (Pohon Uji Kategori, hanya dibaca; node `Rugged Scanner` hanya di-hover). Nilai data mengacu ke fixture `settingsDeviceCategory` (belum ada; disediakan tim FE). Nama node Pre-setup #14 ditulis sebagaimana di TC.
- Spec ini tidak membuat data; tidak ada seeding dan cleanup data.
- Env var `AC_TC_PASSWORD` sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example`. Env var `AC_DC_CUD_PASSWORD`, `AC_DC_DEFAULT_PASSWORD` belum terdaftar: perlu didaftarkan tim FE di `spectra.config.ts` (`executionConfig.environmentVariables`) dan `.env.example`.
- Suite berjalan serial (`parallel: false`): pohon Category, Changelog, dan log audit adalah state bersama.

## Test Steps

### TC-AC-DC-43: Principal dengan capability Manage device master data dapat mengakses tree dan Changelog

1. Verifikasi tree Category tampil penuh dengan seluruh node
2. Klik ikon Changelog pada header sidebar
3. Verifikasi modal "Changelog: Category" terbuka
4. Tutup modal Changelog

### TC-AC-DC-50: Total Control: node user-created menyediakan + Subcategory, Edit, dan Delete berurutan

5. Expand `Hardware` lalu `Handheld Reader`
6. Hover node `Rugged Scanner`
7. Verifikasi tersedia tepat tiga aksi: `+ Subcategory`, Edit, Delete
8. Verifikasi urutan aksi: `+ Subcategory`, Edit, lalu Delete
9. Verifikasi Delete bergaya danger
10. Verifikasi ikon Changelog pada header sidebar tampil

### TC-AC-DC-51: Default User: akses penuh sama dengan Total Control pada node user-created

11. Logout dari akun Total Control
12. Login sebagai Default User (`defaultUserDevCat_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.AC_DC_DEFAULT_PASSWORD`)
13. Buka halaman `Settings > Device > Device Name`
14. Expand `Hardware` lalu `Handheld Reader`
15. Hover node `Rugged Scanner`
16. Verifikasi tersedia `+ Subcategory`, Edit, dan Delete pada node user-created
17. Verifikasi ikon Changelog tampil
18. Klik ikon Changelog pada header sidebar
19. Verifikasi modal Changelog dapat dibuka: modal "Changelog: Category" terbuka
20. Tutup modal Changelog

### TC-AC-DC-56: Role custom Create Update Delete: ketiga aksi tampil pada node user-created

21. Logout dari akun Default User
22. Login sebagai Full CRUD (`manageDeviceCUD_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.AC_DC_CUD_PASSWORD`)
23. Buka halaman `Settings > Device > Device Name`
24. Expand `Hardware` lalu `Handheld Reader`
25. Hover node `Rugged Scanner`
26. Verifikasi `+ Subcategory`, Edit, dan Delete tampil
27. Verifikasi ikon Changelog tampil

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-device-category/TestCases/tc-settings-device-category.md`.
- Subjudul `###` memetakan langkah ke id TC granular.
- Matriks visibilitas aksi per role ditulis per blok akun karena ganti akun menuntut Step eksplisit dan akun pertama login di hook `before` (bagian 3a, KEPUTUSAN 2026-10-30). Langkah tiap blok serupa tetapi tidak identik (TC-AC-DC-43 dan TC-AC-DC-50 menguji Changelog dan urutan aksi).
- Pembagian TC lintas spec: TC-AC-DC-52 (Read Only, visibilitas aksi) dan TC-AC-DC-283 (kontrol baca modal Changelog Read Only) ada di spec 091 (`TC-AC-DC-E2E-091-role-matrix-visibilitas-read-only`).
- Langkah penghubung: langkah 4 dan 20 (menutup modal Changelog), 5, 14, 24 (expand tree agar node terlihat), 11 dan 21 (ganti akun eksplisit, S-07), 13 dan 23 (membuka halaman setelah ganti akun, karena hook `beforeEach` hanya berjalan di awal spec), 18 (klik ikon Changelog untuk membuktikan klausa "modal Changelog dapat dibuka" pada Expected b TC-AC-DC-51 yang langkah TC-nya tidak mengkliknya).
- Halaman Device Name sudah dibuka hook `beforeEach` suite pada akun pertama, sehingga langkah "Buka halaman `Settings > Device > Device Name`" TC-AC-DC-43 dan TC-AC-DC-50 tidak diulang.
- Temuan untuk QA:
  - TC-AC-DC-43 Expected a ("tree tampil penuh dengan seluruh node") tidak merinci node yang dihitung; asersi mengikuti kalimat TC.
  - Pemakaian node literal `Rugged Scanner` hanya untuk hover (baca saja); tidak ada aksi tulis pada node Pre-setup di spec ini.
  - Post Condition TC-AC-DC-43, 50, 51, dan 56 ('-') tidak punya langkah observasi dan tidak diasersi.
