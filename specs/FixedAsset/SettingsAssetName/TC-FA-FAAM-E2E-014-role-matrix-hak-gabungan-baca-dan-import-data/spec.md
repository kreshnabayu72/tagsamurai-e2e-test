---
id: TC-FA-FAAM-E2E-014-role-matrix-hak-gabungan-baca-dan-import-data
title: "Role Matrix: Hak Gabungan Create-Delete, Hak Baca Permission Read, dan Import Data"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAM-56
  - TC-FA-FAAM-64
  - TC-FA-FAAM-65
coverage:
  web: automated
---

# Role Matrix: Hak Gabungan Create-Delete, Hak Baca Permission Read, dan Import Data

## Prerequisites

- Mode: FE+BE (backend nyata).
- Role yang diuji (Pre-setup #7, #3, dan #9):

| Role | Akun (Pre-setup) | Env password | Dipakai di |
|---|---|---|---|
| Create-Delete | `createDelete_automated_{namaCompany}@qwertysystem.net` (#7) | `Spectra.env.FA_CD_PASSWORD` | TC-FA-FAAM-56 (akun pertama, login di hook `before`) |
| Permission Read | `permissionRead_automated_{namaCompany}@qwertysystem.net` (#3) | `Spectra.env.FA_PR_PASSWORD` | TC-FA-FAAM-64 (Ganti akun, langkah 7) |
| Import Data | `importData_automated_{namaCompany}@qwertysystem.net` (#9) | `Spectra.env.FA_IMPORT_PASSWORD` | TC-FA-FAAM-65 (Ganti akun, langkah 15) |

- Login akun pertama (Create-Delete) di hook `before` spec ini; halaman Fixed Asset > Settings > Asset Master > Asset Name dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control, `Spectra.env.FA_TC_PASSWORD`). Password tidak ditulis di spec atau fixture. Semua nama env baru didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`.
- Hook suite (`suite.md`): `before`, `beforeEach`, dan `after` dirujuk apa adanya.
- Data Pre-setup (hanya dibaca, dirujuk lewat fixture baru `Fixture.faAssetName.catalog`): `Dell Latitude` (#10).
- Kemampuan teknis: pengunduhan berkas CSV oleh browser dibaca nama berkasnya (langkah 11); tidak ada pembacaan isi berkas (isi berkas kelas f diuji di spec lain).
- State global: tidak ada yang diubah. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-FAAM-56: Pemegang Create-Delete mendapat gabungan hak per kolom tanpa hak Edit

1. Ketik Search `Dell Latitude`, tekan Enter
2. Klik `⋯` baris `Dell Latitude`
3. Verifikasi menu `⋯` baris `Dell Latitude` memuat `Detail` dan `Delete` saja
4. Verifikasi `[+ Asset Name]` tampil di toolbar
5. Verifikasi aksi `Edit` tidak tersedia
6. Tekan Esc untuk menutup menu `⋯`

### TC-FA-FAAM-64: Semua pemegang dengan Read dapat Download dan membuka Changelog

7. Ganti akun: Logout, login sebagai Permission Read (`permissionRead_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.FA_PR_PASSWORD`), lalu buka Fixed Asset > Settings > Asset Master > Asset Name
8. Klik Download
9. Pilih `Download as CSV`
10. Verifikasi tidak ada toast sukses setelah memilih `Download as CSV`
11. Verifikasi berkas `Asset-Names.csv` terunduh
12. Klik icon Changelog
13. Verifikasi Modal `Changelog: Asset Name` terbuka
14. Klik `✕` pada Modal Changelog

### TC-FA-FAAM-65: Pemegang Global Role Import Data tanpa permission modul tidak mendapat aksi tulis di form Asset Name

15. Ganti akun: Logout, login sebagai Import Data (`importData_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.FA_IMPORT_PASSWORD`), lalu buka halaman utama FAMS
16. Verifikasi sedikitnya satu item menu lain pada sidebar FAMS tampil
17. Verifikasi menu `Settings > Asset Master` tidak tampil
18. Verifikasi jalur Create hanya tersedia lewat modul Import

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-asset-name/TestCases/tc-settings-asset-name.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Spec ditulis per blok role karena ganti akun menuntut Step eksplisit (akun pertama login di hook `before`; bagian 3a, keputusan 2026-10-30).
- Urutan TC di spec: 56, 64, 65 (urutan sumber; TC-65 terakhir karena membuka halaman utama FAMS tanpa tab Asset Name).
- Langkah penghubung (aksi tanpa `Verifikasi`, S-03): langkah 1 (Search untuk menemukan baris target, R-16), langkah 6 (menutup menu), langkah 7 dan 15 (Ganti akun eksplisit), langkah 14 (menutup modal).
- Langkah 10 (absence toast) ditulis segera setelah pemicu dan sebelum asersi artefak; pemilihan `Download as CSV` menjadi anchor positif yang buktinya menyusul pada langkah 11 (bagian 8b butir 11).
- Langkah 16 adalah anchor positif untuk absence item menu pada langkah 17.
- Temuan untuk QA:
  - TC-65 Expected b ("Jalur Create hanya tersedia lewat modul Import") tidak memberi Langkah observasi (hanya "Perhatikan sidebar FAMS") dan tidak menyebut nama item menu modul Import; spec menuliskan butir ini sebagai `Verifikasi` dengan teks TC tanpa mengarang elemen UI (langkah 18) dan menyerahkan cara observasinya kepada tahap script.
  - TC-64 Langkah 1 menyebut `Download as CSV` tanpa menyebut opsi format lain; spec hanya memilih opsi CSV.
  - TC-56 Expected a dan c tumpang tindih ("Menu memuat Detail dan Delete saja" dan "Aksi Edit tidak tersedia"); keduanya diasersi terpisah sesuai S-01.
