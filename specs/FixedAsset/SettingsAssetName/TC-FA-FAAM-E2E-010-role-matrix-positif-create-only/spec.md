---
id: TC-FA-FAAM-E2E-010-role-matrix-positif-create-only
title: "Role Matrix Positif Create-Only: Create Sampai Sukses, Tombol [➕] Default Label, dan Sumber Dropdown"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAM-52
  - TC-FA-FAAM-60
  - TC-FA-FAAM-63
coverage:
  web: automated
---

# Role Matrix Positif Create-Only: Create Sampai Sukses, Tombol [➕] Default Label, dan Sumber Dropdown

## Prerequisites

- Mode: FE+BE (backend nyata).
- Role yang diuji (Pre-setup #4):

| Role | Akun (Pre-setup) | Env password |
|---|---|---|
| Create-Only | `createOnly_automated_{namaCompany}@qwertysystem.net` (#4) | `Spectra.env.FA_CO_PASSWORD` |

- Login akun Create-Only di hook `before` spec ini; halaman Fixed Asset > Settings > Asset Master > Asset Name dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control, `Spectra.env.FA_TC_PASSWORD`). Password tidak ditulis di spec atau fixture. Nama env baru didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`.
- Hook suite (`suite.md`): `before`, `beforeEach`, dan `after` dirujuk apa adanya; seed API per TC tidak dipakai.
- Data Pre-setup (hanya dibaca, dirujuk lewat fixture baru `Fixture.faAssetName.master`): Brand `Dell` (#23), UoM `Unit` (#24), dan pohon kategori dengan leaf `IT Equipment` (#22). Aktor Create-Only tidak memiliki permission pada modul Brand, Measurement, dan Categories (precondition TC-FA-FAAM-63).
- Data Dinamis (suffix `{runId}-010`): Asset Name `Role Create Item {runId}-010` dibuat langkah 17, dihapus hook `after` lewat seed API (aktor Create-Only tidak dapat menghapusnya).
- State global: tidak ada yang diubah. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-FAAM-60: Tombol [➕] Default Label tampil bagi pemegang hak Create di modal Create

1. Klik `[+ Asset Name]`
2. Amati caption field Default Label
3. Verifikasi tombol icon `[➕]` tampil di sebelah caption Default Label
4. Hover tombol `[➕]`
5. Verifikasi tooltip `Create label`

### TC-FA-FAAM-63: Pemegang Create-Only membaca sumber dropdown dan Tree Picker tanpa hak modul sumber

6. Buka dropdown Brand
7. Verifikasi opsi Brand terisi dari master data (opsi `Dell` tampil)
8. Tutup dropdown Brand dengan Esc
9. Buka dropdown UoM
10. Verifikasi opsi UoM terisi dari master data (opsi `Unit` tampil)
11. Tutup dropdown UoM dengan Esc
12. Klik `[Select Category]`
13. Verifikasi Modal Tree Picker memuat pohon kategori (kategori `IT Equipment` tampil)

### TC-FA-FAAM-52: Pemegang Create-Only menyelesaikan Create Asset Name sampai sukses

14. Pilih Category leaf `IT Equipment` pada Modal Tree Picker, klik `[Select]`
15. Isi Asset Name `Role Create Item {runId}-010`
16. Pilih TAG Type `QR`, pilih Brand `Dell`, pilih UoM `Unit`
17. Klik `[Submit]`
18. Verifikasi toast `Success, asset name has been created.`
19. Ketik Search `Role Create Item {runId}-010`, tekan Enter
20. Verifikasi baris `Role Create Item {runId}-010` tampil di List
21. Klik `⋯` baris `Role Create Item {runId}-010`
22. Verifikasi menu `⋯` memuat `Detail`
23. Verifikasi menu `⋯` tidak memuat aksi `Edit` dan `Delete`
24. Tekan Esc untuk menutup menu `⋯`

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-asset-name/TestCases/tc-settings-asset-name.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Urutan TC di spec: 60, 63, 52. Satu pembukaan Modal Create dipakai bersama (bagian 3, halaman yang sama dipakai berulang): TC-60 dan TC-63 hanya membaca, lalu Category yang dipilih lewat Tree Picker TC-63 dipakai melanjutkan TC-52. Pembukaan form (langkah 1) satu kali, penutupan terjadi lewat `[Submit]` sukses pada langkah 17.
- Langkah penghubung (aksi tanpa `Verifikasi`, S-03): langkah 2 (mengamati caption), langkah 8 dan 11 (menutup dropdown), langkah 19 (Search untuk menemukan baris target, R-16), langkah 24 (menutup menu).
- Langkah 22 adalah anchor positif untuk asersi absence `Edit` dan `Delete` pada langkah 23 (bagian 8b butir 2).
- Langkah 14 sampai 16 memakai nilai Data Uji TC-52 (Category `IT Equipment`, TAG Type `QR`, Brand `Dell`, UoM `Unit`); Asset Name diberi suffix `{runId}-010` (S-12).
- Temuan untuk QA:
  - TC-52 Data Uji menulis Asset Name `Role Create Item` tanpa suffix; spec memakai `Role Create Item {runId}-010` supaya run berikutnya tidak bentrok.
  - TC-52 Expected c ("Tidak ada aksi Edit dan Delete pada menu ⋯ baris itu") tidak menyebut apakah menu hanya memuat `Detail`; spec mengasersi `Detail` sebagai anchor dan absence `Edit` dan `Delete`.
  - TC-63 Precondition menyebut aktor tidak memiliki permission pada modul Brand, Measurement, dan Categories tanpa menyebut cara memastikannya; spec mengandalkan konfigurasi akun Pre-setup #4.
