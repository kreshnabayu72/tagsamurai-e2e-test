---
id: TC-FA-PREF-E2E-016-banner-setup-incomplete-hilang-setelah-setting-wajib-disimpan
title: "Banner Setup Incomplete hilang setelah setting wajib terakhir disimpan dan memuat setting kosong menurut urutan SectionCard"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-PREF-80
  - TC-FA-PREF-397
  - TC-FA-PREF-398
coverage:
  web: automated
---

# Banner Setup Incomplete hilang setelah setting wajib terakhir disimpan dan memuat setting kosong menurut urutan SectionCard

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup PA-4), email `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, company `PT Contoh Konstruksi` (PA-1), password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Env var `FA_TC_PASSWORD` belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`: didaftarkan tim FE. Password tidak ditulis di spec atau fixture.
- Data awal blok TC-FA-PREF-80 (seed di hook `before`): Preferences company sesuai PA-7 (hanya In-service Date Source kosong; setting lain bernilai awal).
- Data blok TC-FA-PREF-397 (seed lewat API oleh langkah penghubung): Preferences company sesuai PC-12 varian In-service Date Source tersimpan kosong sedangkan setting wajib lain terisi. Nilai kosong tidak dapat dibuat lewat Save UI, sehingga dibentuk lewat seed.
- Data blok TC-FA-PREF-398 (seed lewat API oleh langkah penghubung): Preferences company sesuai PC-12 varian First Accounting Period, Default Capitalization Threshold, dan Depreciation in Disposal Month tersimpan kosong; setting wajib lain terisi.
- Hook `after` memulihkan Preferences ke nilai awal (PA-2). Seri fixture PA dan PC dipakai berurutan dengan seed ulang di antara blok.
- Flag Guided Tooltip halaman Preferences: hook suite `before` men-set true untuk akun aktor dan `after` memulihkannya (butir "Flag Guided Tooltip" di `suite.md`).
- Seed dan pemulihan lewat API disediakan tim FE/BE (butir "Seed dan pemulihan lewat API" di `suite.md`).
- Identitas data Pre-setup dibaca dari `fixtures/settings-accounting-preferences.json` (belum ada; disediakan tim FE, nama kunci ditetapkan tim FE).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-PREF-80: Banner hilang setelah setting wajib terakhir yang kosong disimpan

1. Verifikasi banner awal tampil dengan teks "Accounting setup is incomplete: In-service Date Source. Depreciation and journal export are blocked until completed."
2. Pilih "Activation date" pada Select In-service Date Source
3. Klik `[Save changes]`
4. Verifikasi dialog "Save Changes" tidak tampil
5. Verifikasi toast sukses "Success, accounting preferences have been saved." tampil
6. Verifikasi banner Setup Incomplete hilang
7. Verifikasi judul SectionCard Capitalization tampil
8. Verifikasi tidak ada titik peringatan pada judul SectionCard Capitalization

### TC-FA-PREF-397: Banner hilang setelah setting wajib terisi dan disimpan

9. Seed ulang Preferences company ke PC-12 (In-service Date Source tersimpan kosong; setting wajib lain terisi) lewat API lalu buka ulang Fixed Asset > Settings > Accounting > Preferences
10. Verifikasi banner (Alert severity danger, tidak dapat ditutup) tampil dengan teks "Accounting setup is incomplete: In-service Date Source. Depreciation and journal export are blocked until completed."
11. Pilih "Activation date" pada Select In-service Date Source
12. Klik `[Save changes]`
13. Verifikasi dialog "Save Changes" tidak tampil
14. Verifikasi toast "Success, accounting preferences have been saved." tampil
15. Verifikasi banner Setup Incomplete tidak tampil lagi

### TC-FA-PREF-398: Banner memuat semua setting wajib kosong menurut urutan SectionCard

16. Seed ulang Preferences company ke PC-12 (First Accounting Period, Default Capitalization Threshold, dan Depreciation in Disposal Month tersimpan kosong; setting wajib lain terisi) lewat API lalu buka ulang Fixed Asset > Settings > Accounting > Preferences
17. Verifikasi banner Setup Incomplete tampil dengan teks "Accounting setup is incomplete: First Accounting Period, Default Capitalization Threshold, Depreciation in Disposal Month. Depreciation and journal export are blocked until completed."
18. Verifikasi daftar setting dipisah koma dan spasi menurut urutan SectionCard General, Capitalization, Depreciation tanpa dipotong

## Notes

- Sumber: `fixed-asset/settings-accounting-preferences/TestCases/tc-settings-accounting-preferences.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): langkah 9 dan 16 (seed ulang Preferences dan buka ulang halaman). Langkah 7 (anchor positif judul SectionCard Capitalization sebelum absence titik peringatan, 8b butir 2) adalah asersi tambahan di luar Expected TC, dicatat beserta alasannya.
- Asersi absence dialog "Save Changes" (langkah 4 dan 13) diletakkan segera setelah pemicu `[Save changes]` dengan toast sukses sebagai anchor positif pada langkah berikutnya (8b butir 11).
- Temuan untuk QA:
  - TC-FA-PREF-80 Post Condition a ("In-service Date Source tersimpan "Activation date"") dan TC-FA-PREF-397 Post Condition a dan b tidak punya langkah observasi di TC sehingga tidak diasersi (S-01); Post Condition b TC-FA-PREF-80 ("status Setup Incomplete selesai") sepadan dengan Expected d (banner hilang) yang sudah diasersi.
  - TC-FA-PREF-80, 397, dan 398 tidak menyebut nama env var password; nama `FA_TC_PASSWORD` diusulkan spec dan perlu keputusan tim.
