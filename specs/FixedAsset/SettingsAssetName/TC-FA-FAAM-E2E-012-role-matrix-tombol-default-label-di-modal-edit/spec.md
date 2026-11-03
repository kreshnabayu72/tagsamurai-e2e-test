---
id: TC-FA-FAAM-E2E-012-role-matrix-tombol-default-label-di-modal-edit
title: "Role Matrix: Tombol [➕] Default Label di Modal Edit (Update-Only Hidden, Total Control Tampil)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAM-61
  - TC-FA-FAAM-62
coverage:
  web: automated
---

# Role Matrix: Tombol [➕] Default Label di Modal Edit (Update-Only Hidden, Total Control Tampil)

## Prerequisites

- Mode: FE+BE (backend nyata).
- Role yang diuji (Pre-setup #5 dan #1):

| Role | Akun (Pre-setup) | Env password | Tombol `[➕]` di Modal Edit |
|---|---|---|---|
| Update-Only | `updateOnly_automated_{namaCompany}@qwertysystem.net` (#5) | `Spectra.env.FA_UO_PASSWORD` | Hidden (tidak dirender) |
| Total Control | `totalControl_automated_{namaCompany}@qwertysystem.net` (#1) | `Spectra.env.FA_TC_PASSWORD` | tampil |

- Login akun pertama (Update-Only) di hook `before` spec ini; halaman Fixed Asset > Settings > Asset Master > Asset Name dibuka hook `beforeEach` suite. Akun kedua (Total Control) login lewat langkah Ganti akun eksplisit (langkah 7). Hook `after` mengembalikan sesi ke akun default suite (Total Control). Password tidak ditulis di spec atau fixture. Nama env baru didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`.
- Hook suite (`suite.md`): `before`, `beforeEach`, dan `after` dirujuk apa adanya.
- Data Pre-setup (hanya dibaca, dirujuk lewat fixture baru `Fixture.faAssetName.catalog`): `Dell Latitude` (#10) hanya dibuka di Modal Edit tanpa Save.
- State global: tidak ada yang diubah. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-FAAM-61: Tombol [➕] Default Label Hidden bagi pemegang Update-Only di modal Edit

1. Ketik Search `Dell Latitude`, tekan Enter
2. Klik `⋯` baris `Dell Latitude` lalu `Edit`
3. Amati caption field Default Label
4. Verifikasi caption field Default Label tampil
5. Verifikasi tombol `[➕]` tidak dirender (Hidden)
6. Klik `✕` pada Modal Edit (tanpa perubahan)

### TC-FA-FAAM-62: Tombol [➕] Default Label tampil bagi Total Control di modal Edit

7. Ganti akun: Logout, login sebagai Total Control (`totalControl_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.FA_TC_PASSWORD`), lalu buka Fixed Asset > Settings > Asset Master > Asset Name
8. Ketik Search `Dell Latitude`, tekan Enter
9. Klik `⋯` baris `Dell Latitude` lalu `Edit`
10. Verifikasi tombol `[➕]` tampil di caption Default Label
11. Klik `✕` pada Modal Edit (tanpa perubahan)

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-asset-name/TestCases/tc-settings-asset-name.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Spec ditulis per blok role karena ganti akun menuntut Step eksplisit (akun pertama login di hook `before`; bagian 3a, keputusan 2026-10-30).
- Urutan TC di spec: 61, 62 (akun hook `before` dipakai lebih dahulu).
- Langkah penghubung (aksi tanpa `Verifikasi`, S-03): langkah 1, 8 (Search untuk menemukan baris target, R-16), langkah 3 (mengamati caption), langkah 6 dan 11 (menutup Modal Edit tanpa perubahan, sehingga tanpa dialog `Unsaved Changes`), langkah 7 (Ganti akun eksplisit).
- Langkah 4 adalah anchor positif untuk asersi `Hidden` pada langkah 5 (bagian 8b butir 2 dan 11); asersi Hidden tombol `[➕]` memakai caption yang sudah termuat sebagai anchor permukaan.
- Langkah 8 dan 9 pada Total Control mengulang pencarian karena sesi login baru membuka tab Asset Name tanpa Search.
- Temuan untuk QA: tidak ada. TC-61 dan TC-62 tidak ambigu; keduanya diasersi sesuai Expected.
