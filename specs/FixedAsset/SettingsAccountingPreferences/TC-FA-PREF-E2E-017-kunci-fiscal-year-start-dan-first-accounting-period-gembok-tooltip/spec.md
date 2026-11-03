---
id: TC-FA-PREF-E2E-017-kunci-fiscal-year-start-dan-first-accounting-period-gembok-tooltip
title: "Kunci Fiscal Year Start dan First Accounting Period: gembok, tooltip, field lain tetap Enabled"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-PREF-83
  - TC-FA-PREF-84
  - TC-FA-PREF-85
  - TC-FA-PREF-86
  - TC-FA-PREF-87
  - TC-FA-PREF-124
coverage:
  web: automated
---

# Kunci Fiscal Year Start dan First Accounting Period: gembok, tooltip, field lain tetap Enabled

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup PA-4), email `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, company `PT Contoh Konstruksi` (PA-1), password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Env var `FA_TC_PASSWORD` belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`: didaftarkan tim FE. Password tidak ditulis di spec atau fixture.
- Data awal (seed di hook `before`): Preferences company sesuai PA-2 (nilai awal, semua setting wajib terisi) dengan kunci aktif PA-9: posting penyusutan pertama sudah ada (Last Posted Period Asset Class IT Equipment = Mei 2026). Dipakai TC-FA-PREF-83, 84, 124, 87, dan 86.
- Data blok TC-FA-PREF-85 (seed lewat API oleh langkah penghubung): kunci PA-10, yaitu periode Mar 2026 berstatus Soft Closed dan tidak ada penyusutan diposting. Kunci dibentuk lewat seed BE karena Depreciation Run dan Period Close belum disusun; kemampuan itu disediakan tim FE/BE. Hook `after` memulihkan PA-2 tanpa kunci.
- Kemampuan baca BE (disediakan tim FE/BE): jumlah entri System Log dan Activity Log, dipakai TC-FA-PREF-85 sebagai baseline; jumlah baris Changelog dibaca lewat modal View history.
- Flag Guided Tooltip halaman Preferences: hook suite `before` men-set true untuk akun aktor dan `after` memulihkannya (butir "Flag Guided Tooltip" di `suite.md`).
- Seed dan pemulihan lewat API disediakan tim FE/BE (butir "Seed dan pemulihan lewat API" di `suite.md`).
- Identitas data Pre-setup dibaca dari `fixtures/settings-accounting-preferences.json` (belum ada; disediakan tim FE, nama kunci ditetapkan tim FE).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-PREF-83: Fiscal Year Start terkunci karena penyusutan diposting

1. Verifikasi Select Fiscal Year Start tetap tampil namun Disabled dengan ikon gembok
2. Hover Select Fiscal Year Start
3. Verifikasi tooltip "Fiscal year start is locked because depreciation has been posted or a period has been closed. It cannot be changed from this page." tampil

### TC-FA-PREF-84: First Accounting Period terkunci

4. Verifikasi Select bulan dan Select tahun First Accounting Period tetap tampil namun Disabled dengan ikon gembok
5. Hover Select bulan First Accounting Period
6. Verifikasi tooltip "First accounting period is locked because depreciation has been posted or a period has been closed. It cannot be changed from this page." tampil pada Select bulan
7. Hover Select tahun First Accounting Period
8. Verifikasi tooltip "First accounting period is locked because depreciation has been posted or a period has been closed. It cannot be changed from this page." tampil pada Select tahun

### TC-FA-PREF-124: Total Control tetap tunduk pada kunci

9. Verifikasi Select Fiscal Year Start, Select bulan, dan Select tahun tampil Disabled dengan ikon gembok walau aktor Total Control

### TC-FA-PREF-87: Total Control tidak dapat mengubah field terkunci

10. Klik Select Fiscal Year Start
11. Verifikasi Select Fiscal Year Start tidak membuka daftar opsi
12. Klik Select bulan First Accounting Period
13. Verifikasi Select bulan First Accounting Period tidak membuka daftar opsi

### TC-FA-PREF-86: Field lain tetap Enabled

14. Ubah Default Capitalization Threshold menjadi "6.000.000"
15. Verifikasi CurrencyInput Default Capitalization Threshold dapat diedit
16. Verifikasi `[Save changes]` Enabled
17. Kembalikan Default Capitalization Threshold ke "5.000.000"

### TC-FA-PREF-85: Kunci karena periode Soft Closed mengunci kedua field bersamaan

18. Seed ulang kunci ke PA-10 (periode Mar 2026 Soft Closed tanpa penyusutan diposting) lewat API
19. Catat jumlah entri System Log dan Activity Log serta jumlah baris Changelog Preferences (baseline)
20. Buka ulang Fixed Asset > Settings > Accounting > Preferences
21. Verifikasi Select Fiscal Year Start, Select bulan, dan Select tahun First Accounting Period seluruhnya Disabled dengan ikon gembok bersamaan
22. Verifikasi jumlah baris Changelog Preferences tidak bertambah dari baseline
23. Verifikasi jumlah entri System Log tidak bertambah dari baseline
24. Verifikasi jumlah entri Activity Log tidak bertambah dari baseline

## Notes

- Sumber: `fixed-asset/settings-accounting-preferences/TestCases/tc-settings-accounting-preferences.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Urutan blok: TC-FA-PREF-124 dan TC-FA-PREF-87 ditaruh sesudah TC-FA-PREF-84, dan TC-FA-PREF-86 (membuat form dirty) sebelum TC-FA-PREF-85 yang memakai kunci berbeda, supaya seed kunci PA-9 dipakai sekali (S-10).
- Langkah penghubung (S-03): langkah 17 (pemulihan form dirty ke nilai tersimpan, S-09); langkah 18 sampai 20 (seed ulang kunci PA-10, pencatatan baseline, dan buka ulang halaman).
- P-1: Expected TC-FA-PREF-85 butir b ("tidak ada entri log baru untuk penguncian") ditulis sebagai `Verifikasi` berbaseline di spec ini karena konteksnya bergantung pada state kunci periode yang dibentuk seed berat (langkah 18); tidak ada spec absence (kelas g) yang memuat aksi nyata untuk TC ini (S-05). Surface disebut satu per satu: Changelog Preferences, System Log, Activity Log; anchor positif absence adalah langkah 21 (halaman dan kunci termuat setelah buka ulang).
- Temuan untuk QA:
  - TC-FA-PREF-85 tidak menyebut surface log mana yang dimaksud "entri log baru"; spec memakai ketiga surface log modul (Changelog, System Log, Activity Log).
  - TC-FA-PREF-83 sampai 87 dan 124 tidak menyebut nama env var password; nama `FA_TC_PASSWORD` diusulkan spec dan perlu keputusan tim.
  - TC-FA-PREF-87 tidak menyebut cara membuktikan "tidak membuka daftar opsi" selain mengklik Select; spec memverifikasi daftar opsi tidak tampil setelah klik.
