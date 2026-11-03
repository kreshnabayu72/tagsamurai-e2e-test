---
id: TC-AC-DC-E2E-021-role-matrix-positif-delete-delete-only
title: "Role Matrix Positif: Delete Category untuk Delete-Only"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DC-55
  - TC-AC-DC-60
coverage:
  web: automated
---
# Role Matrix Positif: Delete Category untuk Delete-Only

## Prerequisites

- Mode: FE+BE.
- Aktor: Delete-Only (Pre-setup #6); Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Settings > Device > Device Name).

| Role yang diuji | Akun (Pre-setup) | Password |
|---|---|---|
| Delete-Only (Manage device master data: Delete + Read) | #6 `manageDeviceD_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.AC_DC_DELETE_PASSWORD` |

- Data Dinamis (dibuat spec ini lewat API di hook `before` oleh Total Control #1 lewat sesi API aktor, di bawah `Handheld Reader`): node `Pemindai Hapus {runId}-021` (leaf, target Delete TC-AC-DC-55).
- Data Pre-setup: #14 (Pohon Uji Kategori, hanya dibaca; `Smart Fixed Reader` hanya di-hover). Nilai data mengacu ke fixture `settingsDeviceCategory` (belum ada; disediakan tim FE). Nama node Pre-setup #14 ditulis sebagaimana di TC.
- Kemampuan teknis: sesi API aktor (login API password untuk akun yang sama dengan sesi UI, tidak dihitung sebagai sesi web) dan klien HTTP; disediakan tim BE/FE dan dinyatakan di `suite.md`.
- Hook `after`: menghapus semua node (dan Device Name) yang dibuat spec ini, termasuk node hasil aksi UI yang dikenali dari sufiks `{runId}-021`, lewat API dari anak ke induk; cleanup tidak berasumsi seeding berhasil penuh.
- Seeding dan cleanup menambah entri Changelog dan log audit permanen (Create dan Delete atas node bersufiks); entri itu tidak diasersi.
- Env var `AC_TC_PASSWORD` sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example`. Env var `AC_DC_DELETE_PASSWORD` belum terdaftar: perlu didaftarkan tim FE di `spectra.config.ts` (`executionConfig.environmentVariables`) dan `.env.example`.
- Suite berjalan serial (`parallel: false`): pohon Category, Changelog, dan log audit adalah state bersama.

## Test Steps

### TC-AC-DC-60: Delete-Only: node hardcoded perantara tidak menampilkan aksi apa pun

1. Expand `Hardware`
2. Hover node `Smart Fixed Reader`
3. Verifikasi tidak ada aksi pada `Smart Fixed Reader` (Delete tetap Hidden karena hardcoded)

### TC-AC-DC-55: Delete-Only: hanya Delete tampil dan hapus leaf berhasil dieksekusi

4. Expand `Handheld Reader`
5. Hover node `Pemindai Hapus {runId}-021`
6. Verifikasi hanya aksi Delete tampil
7. Verifikasi `+ Subcategory` dan Edit Hidden
8. Klik Delete
9. Klik `[Delete]` pada dialog
10. Verifikasi toast sukses "Success, category has been deleted." tampil
11. Verifikasi node `Pemindai Hapus {runId}-021` hilang dari tree

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-device-category/TestCases/tc-settings-device-category.md`.
- Subjudul `###` memetakan langkah ke id TC granular.
- Spec Role Matrix positif satu role (Delete-Only) untuk aksi Delete; TC-AC-DC-60 (negatif, tanpa menulis data) diletakkan sebelum TC-AC-DC-55 yang menghapus data (S-10). Urutan ini berbeda dari urutan TC sumber.
- Langkah penghubung: langkah 1 dan 4 (expand tree).
- Temuan untuk QA:
  - Target aksi tulis dan hapus memakai node milik spec bersufiks `{runId}-021` (S-06, S-12); TC memakai node literal Pre-setup #14 (`Hapus Daun` pada TC-AC-DC-55) sebagai target. Hasil TC identik karena node milik spec adalah node user-created dengan perilaku yang sama; node literal Pre-setup hanya dibaca.
  - Catatan TC menyebut data destruktif dipulihkan automation baseline sebelum tiap TC; spec ini tidak mengandalkannya. Node hasil Delete sudah terhapus oleh aksi UI, sehingga cleanup node itu di `after` ditulis toleran bila sudah tidak ada.
  - Post Condition TC-AC-DC-55 dan 60 ('-') tidak punya langkah observasi dan tidak diasersi.
