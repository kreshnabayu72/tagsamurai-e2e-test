---
id: TC-FA-FAAM-E2E-011-role-matrix-positif-update-only-edit
title: "Role Matrix Positif Update-Only: Edit Sampai Sukses dan Edit Category Locked"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAM-53
  - TC-FA-FAAM-59
coverage:
  web: automated
---

# Role Matrix Positif Update-Only: Edit Sampai Sukses dan Edit Category Locked

## Prerequisites

- Mode: FE+BE (backend nyata).
- Role yang diuji (Pre-setup #5):

| Role | Akun (Pre-setup) | Env password |
|---|---|---|
| Update-Only | `updateOnly_automated_{namaCompany}@qwertysystem.net` (#5) | `Spectra.env.FA_UO_PASSWORD` |

- Login akun Update-Only di hook `before` spec ini; halaman Fixed Asset > Settings > Asset Master > Asset Name dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control, `Spectra.env.FA_TC_PASSWORD`). Password tidak ditulis di spec atau fixture. Nama env baru didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`.
- Hook suite (`suite.md`): `before`, `beforeEach`, dan `after` dirujuk apa adanya.
- Data Pre-setup (hanya dibaca): `MacBook Pro` (#12, Category internal `Electronics` sehingga Category Locked) hanya dibuka di Modal Edit tanpa Save, dirujuk lewat fixture baru `Fixture.faAssetName.catalog`.
- Data Dinamis (suffix `{runId}-011` pada nama, seed API idempotent di hook `before`, dihapus hook `after`): `Warehouse Pallet {runId}-011` ber-Code `PLT-WH011` (salinan fixture #13 yang diedit TC-FA-FAAM-53). Code diubah ke `PLT-U1-011` pada langkah 8. Code tetap tanpa `{runId}` karena batas Code 15 karakter; hook `before` dan `after` menghapus lewat API record ber-Code `PLT-WH011` dan `PLT-U1-011` bila masih ada (suite serial).
- State global: tidak ada yang diubah. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-FAAM-59: Pemegang Update-Only dapat mengedit Asset Name ber-Category Locked

1. Ketik Search `MacBook Pro`, tekan Enter
2. Klik `⋯` baris `MacBook Pro` lalu `Edit`
3. Verifikasi Modal `Edit Asset Name` terbuka
4. Verifikasi Category terisi `Electronics`
5. Klik `✕` pada Modal Edit (tanpa perubahan)

### TC-FA-FAAM-53: Pemegang Update-Only menyelesaikan Edit Asset Name sampai sukses

6. Ganti isi kotak search dengan `Warehouse Pallet {runId}-011`, tekan Enter
7. Klik `⋯` baris `Warehouse Pallet {runId}-011` lalu `Edit`
8. Ubah Code dari `PLT-WH011` menjadi `PLT-U1-011`
9. Klik `[Save]`
10. Verifikasi toast `Success, asset name has been updated.`
11. Verifikasi baris `Warehouse Pallet {runId}-011` menampilkan Code `PLT-U1-011`

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-asset-name/TestCases/tc-settings-asset-name.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Urutan TC di spec: 59, 53 (pembacaan tanpa Save lebih dahulu, aksi sukses kemudian, S-10).
- Langkah penghubung (aksi tanpa `Verifikasi`, S-03): langkah 1, 6 (Search untuk menemukan baris target, R-16), langkah 5 (menutup Modal Edit tanpa perubahan, sehingga tanpa dialog `Unsaved Changes`).
- TC-59 tidak mengubah data sehingga Last Updated `MacBook Pro` tidak berubah (S-06).
- Temuan untuk QA:
  - TC-53 memakai salinan `Warehouse Pallet 53` (Code `PLT-WH53`) dan Code baru `PLT-U1` tanpa suffix per run; spec memakai suffix `{runId}-011` pada nama (S-12) dan Code tetap `PLT-WH011` dan `PLT-U1-011` tanpa `{runId}` karena batas Code 15 karakter.
  - TC-59 tidak menyebut apakah Modal Edit dapat disimpan; spec hanya mengasersi Modal terbuka dan Category terisi sesuai Expected.
