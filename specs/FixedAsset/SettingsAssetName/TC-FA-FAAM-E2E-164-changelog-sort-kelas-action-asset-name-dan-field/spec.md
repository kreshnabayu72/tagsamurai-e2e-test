---
id: TC-FA-FAAM-E2E-164-changelog-sort-kelas-action-asset-name-dan-field
title: "Modal Changelog: Sort Kelas Action, Asset Name, dan Field"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAM-481
coverage:
  web: automated
---

# Modal Changelog: Sort Kelas Action, Asset Name, dan Field

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD` (nama env baru didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Data Pre-setup (hanya dibaca, dirujuk lewat fixture baru `Fixture.faAssetName.changelogSeed`): Changelog contoh PRD §4.1 (Pre-setup #28), entri Create, Edit, dan Delete bertanggal berbeda-beda dalam `changelogSeed.dateRange`, dengan sedikitnya dua nilai distinct pada kolom Action, Asset Name, dan Field (S-11). Halaman teramati dibatasi Filter Date rentang seed (S-14), sehingga entri baru dari spec lain tidak memengaruhi urutan.
- Tabel "Kolom teks" (dipakai langkah 4 sampai 9):

  | Kolom |
  |---|
  | Action |
  | Asset Name |
  | Field |

- Hook suite: lihat `suite.md` (hook `before`, `beforeEach`, `after`; seed API per TC dan sesi API aktor disediakan tim BE/FE).
- State global: tidak ada yang diubah. Spec ini tidak menyimpan konfigurasi kolom. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-FAAM-481: Sort Changelog kelas Action, Asset Name, Field

1. Klik icon Changelog
2. Batasi tabel pada entri seed: klik icon Filter, pilih rentang tanggal `Fixture.faAssetName.changelogSeed.dateRange`, klik `[Apply]`
3. Untuk setiap kolom pada tabel "Kolom teks" (langkah 4 sampai 9):
4. Klik header kolom
5. Verifikasi Klik 1: A-Z tanpa membedakan huruf besar-kecil
6. Klik header kolom
7. Verifikasi Klik 2: Z-A
8. Klik header kolom
9. Verifikasi Klik 3: kembali netral (default Date Newest First)

## Notes

- Langkah penghubung (aksi tanpa `Verifikasi`): Filter Date rentang seed supaya halaman teramati memuat entri seed dengan nilai distinct (langkah 2, S-14).
- Langkah 4 sampai 9 diulang untuk Action, Asset Name, lalu Field (bagian 8b butir 7); jumlah langkah dengan ekspansi 21. Tiap iterasi dimulai dari sort netral (hasil langkah 9).
- Pembagian TC lintas spec: sort kelas Date, Old Value, New Value, dan Modified By (TC-FA-FAAM-480, 482, 483) ada di spec 150.
- Temuan untuk QA: Pre-setup #28 tidak menjamin sedikitnya dua nilai distinct pada kolom Asset Name dan Field; asersi sort A-Z dan Z-A baru bermakna bila seed menyediakannya (S-11), sehingga spec mengandalkan seed dari tim BE.
