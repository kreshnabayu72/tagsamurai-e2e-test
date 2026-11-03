---
id: TC-FA-PREF-E2E-018-helper-peringatan-akun-default-inactive
title: "Helper peringatan akun default Inactive pada keempat Select akun"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-PREF-91
  - TC-FA-PREF-92
  - TC-FA-PREF-93
  - TC-FA-PREF-94
  - TC-FA-PREF-95
coverage:
  web: automated
---

# Helper peringatan akun default Inactive pada keempat Select akun

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup PA-4), email `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, company `PT Contoh Konstruksi` (PA-1), password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Env var `FA_TC_PASSWORD` belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`: didaftarkan tim FE. Password tidak ditulis di spec atau fixture.
- Data awal (seed di hook `before`): Chart of Accounts sesuai PA-3 (akun Active dan Inactive); Preferences company sesuai PA-21: Default Gain on Disposal `4-9200 – Laba Lama`, Default Loss on Disposal `5-9200 – Rugi Lama`, Default Capitalization Offset `1-2950 – Biaya Lama`, Found Asset Credit Account `4-1600 – Pendapatan Lama`; keempat akun berstatus Inactive. Dipakai TC-FA-PREF-91 sampai 94.
- Data blok TC-FA-PREF-95 (seed lewat API oleh langkah penghubung): Preferences sesuai PA-22 (Default Gain on Disposal `4-9100 – Laba Pelepasan Aset`, akun Active; setting lain PA-2). Hook `after` memulihkan Preferences ke PA-2.
- Flag Guided Tooltip halaman Preferences: hook suite `before` men-set true untuk akun aktor dan `after` memulihkannya (butir "Flag Guided Tooltip" di `suite.md`).
- Seed dan pemulihan lewat API disediakan tim FE/BE (butir "Seed dan pemulihan lewat API" di `suite.md`).
- Identitas data Pre-setup dibaca dari `fixtures/settings-accounting-preferences.json` (belum ada; disediakan tim FE, nama kunci ditetapkan tim FE).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-PREF-91: Default Gain on Disposal, akun tersimpan Inactive

1. Verifikasi Select Default Gain on Disposal tetap menampilkan nilai "4-9200 – Laba Lama"
2. Verifikasi helper berseverity warning tampil di bawah Select Default Gain on Disposal: "This account is inactive. Journals using it are held at export."

### TC-FA-PREF-92: Default Loss on Disposal, akun tersimpan Inactive

3. Verifikasi Select Default Loss on Disposal tetap menampilkan nilai "5-9200 – Rugi Lama"
4. Verifikasi helper berseverity warning tampil di bawah Select Default Loss on Disposal: "This account is inactive. Journals using it are held at export."

### TC-FA-PREF-93: Default Capitalization Offset, akun tersimpan Inactive

5. Verifikasi Select Default Capitalization Offset tetap menampilkan nilai "1-2950 – Biaya Lama"
6. Verifikasi helper berseverity warning tampil di bawah Select Default Capitalization Offset: "This account is inactive. Journals using it are held at export."

### TC-FA-PREF-94: Found Asset Credit Account, akun tersimpan Inactive

7. Verifikasi Select Found Asset Credit Account tetap menampilkan nilai "4-1600 – Pendapatan Lama"
8. Verifikasi helper berseverity warning tampil di bawah Select Found Asset Credit Account: "This account is inactive. Journals using it are held at export."

### TC-FA-PREF-95: Helper tidak tampil saat akun tersimpan Active

9. Seed ulang Preferences company ke PA-22 lewat API lalu buka ulang Fixed Asset > Settings > Accounting > Preferences
10. Verifikasi Select Default Gain on Disposal menampilkan nilai "4-9100 – Laba Pelepasan Aset"
11. Verifikasi helper "This account is inactive. Journals using it are held at export." tidak tampil

## Notes

- Sumber: `fixed-asset/settings-accounting-preferences/TestCases/tc-settings-accounting-preferences.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): langkah 9 (seed ulang PA-22 dan buka ulang halaman). Keempat TC Inactive memakai satu seed PA-21 karena precondition-nya sama dan form hanya dibaca.
- Asersi absence helper pada langkah 11 didahului langkah 10 (nilai Select tampil pada surface yang sama sebagai anchor positif, 8b butir 2).
- Temuan untuk QA:
  - TC-FA-PREF-91 sampai 95 tidak menyebut nama env var password; nama `FA_TC_PASSWORD` diusulkan spec dan perlu keputusan tim.
