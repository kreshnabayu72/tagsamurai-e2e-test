---
id: TC-AC-DC-E2E-020-role-matrix-positif-edit-update-only
title: "Role Matrix Positif: Edit Category untuk Update-Only"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DC-54
  - TC-AC-DC-59
coverage:
  web: automated
---
# Role Matrix Positif: Edit Category untuk Update-Only

## Prerequisites

- Mode: FE+BE.
- Aktor: Update-Only (Pre-setup #5); Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Settings > Device > Device Name).

| Role yang diuji | Akun (Pre-setup) | Password |
|---|---|---|
| Update-Only (Manage device master data: Update + Read) | #5 `manageDeviceU_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.AC_DC_UPDATE_PASSWORD` |

- Data Dinamis (dibuat spec ini lewat API di hook `before` oleh Total Control #1 lewat sesi API aktor, di bawah `Handheld Reader`): node `Pemindai Ubah {runId}-020` (leaf, target rename TC-AC-DC-54). Nama hasil rename: `Pemindai Ubah Pro {runId}-020`.
- Data Pre-setup: #14 (Pohon Uji Kategori, hanya dibaca; `Handheld Reader` hanya di-hover). Nilai data mengacu ke fixture `settingsDeviceCategory` (belum ada; disediakan tim FE). Nama node Pre-setup #14 ditulis sebagaimana di TC.
- Kemampuan teknis: sesi API aktor (login API password untuk akun yang sama dengan sesi UI, tidak dihitung sebagai sesi web) dan klien HTTP; disediakan tim BE/FE dan dinyatakan di `suite.md`.
- Hook `after`: menghapus semua node (dan Device Name) yang dibuat spec ini, termasuk node hasil aksi UI yang dikenali dari sufiks `{runId}-020`, lewat API dari anak ke induk; cleanup tidak berasumsi seeding berhasil penuh.
- Seeding dan cleanup menambah entri Changelog dan log audit permanen (Create dan Delete atas node bersufiks); entri itu tidak diasersi.
- Env var `AC_TC_PASSWORD` sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example`. Env var `AC_DC_UPDATE_PASSWORD` belum terdaftar: perlu didaftarkan tim FE di `spectra.config.ts` (`executionConfig.environmentVariables`) dan `.env.example`.
- Suite berjalan serial (`parallel: false`): pohon Category, Changelog, dan log audit adalah state bersama.

## Test Steps

### TC-AC-DC-59: Update-Only: node hardcoded perantara tidak menampilkan aksi apa pun

1. Expand `Hardware` lalu `Handheld Reader`
2. Hover node `Handheld Reader`
3. Verifikasi tidak ada aksi pada `Handheld Reader` (Edit tetap Hidden karena hardcoded, `+ Subcategory` Hidden karena tidak punya capability Create)

### TC-AC-DC-54: Update-Only: hanya Edit tampil dan rename berhasil dieksekusi

4. Hover node `Pemindai Ubah {runId}-020`
5. Verifikasi hanya aksi Edit tampil
6. Verifikasi `+ Subcategory` dan Delete Hidden
7. Klik Edit
8. Ubah nama menjadi "Pemindai Ubah Pro {runId}-020"
9. Klik `[Save]`
10. Verifikasi toast sukses "Success, category has been updated." tampil
11. Verifikasi node tampil dengan nama "Pemindai Ubah Pro {runId}-020"

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-device-category/TestCases/tc-settings-device-category.md`.
- Subjudul `###` memetakan langkah ke id TC granular.
- Spec Role Matrix positif satu role (Update-Only) untuk aksi Edit; TC-AC-DC-59 (negatif, tanpa menulis data) diletakkan sebelum TC-AC-DC-54 yang mengubah data (S-10). Urutan ini berbeda dari urutan TC sumber.
- Langkah penghubung: langkah 1 (expand tree).
- Temuan untuk QA:
  - Target aksi tulis dan hapus memakai node milik spec bersufiks `{runId}-020` (S-06, S-12); TC memakai node literal Pre-setup #14 (`Rugged Scanner` yang di-rename menjadi "Rugged Scanner Pro" pada TC-AC-DC-54; nama hasil rename diberi sufiks `{runId}-020`) sebagai target. Hasil TC identik karena node milik spec adalah node user-created dengan perilaku yang sama; node literal Pre-setup hanya dibaca.
  - Catatan TC menyebut data destruktif dipulihkan automation baseline sebelum tiap TC; spec ini tidak mengandalkannya.
  - Post Condition TC-AC-DC-54 dan 59 ('-') tidak punya langkah observasi dan tidak diasersi.
