---
id: TC-FA-PREF-E2E-053-opsi-select-akun-active-function-dan-urut-kode-a-z-seri-pa-dan-pc
title: "Opsi Select akun hanya memuat akun Active sesuai function dan berurutan menurut kode A-Z (seri PA dan PC)"
layer: ui-e2e
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-PREF-171
  - TC-FA-PREF-172
  - TC-FA-PREF-173
  - TC-FA-PREF-174
  - TC-FA-PREF-588
  - TC-FA-PREF-589
  - TC-FA-PREF-590
  - TC-FA-PREF-591
sourceRules: ["FI-04", "FAPREF-LOGIC-06a", "FAPREF-LOGIC-06h", "FAPREF-LOGIC-08a", "FI-05", "FAPREF-LOGIC-08e"]
smoke: []
dependsOn: []
trace:
  "FI-04": [2, 7, 15, 21, 25, 29, 33]
  "FAPREF-LOGIC-06a": [2, 4, 7, 21, 25]
  "FAPREF-LOGIC-06h": [3, 8]
  "FAPREF-LOGIC-08a": [11, 12, 29]
  "FI-05": [12, 16, 22, 26, 30, 34]
  "FAPREF-LOGIC-08e": [15, 16, 33]
coverage:
  web: automated
---

# Opsi Select akun hanya memuat akun Active sesuai function dan berurutan menurut kode A-Z (seri PA dan PC)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup) `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net` pada company `PT Contoh Konstruksi`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Env var `FA_TC_PASSWORD` belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`: didaftarkan tim FE. Password tidak ditulis di spec atau fixture.
- Data TC-FA-PREF-171 sampai 174: seri PA (TC-FA-PREF-1-175), company `PT Contoh Konstruksi` plan Growth (PA-1): Preferences nilai awal PA-2 (tidak terkunci, semua setting wajib terisi); Chart of Accounts PA-3. Active: 1-1001 Kas Utama (Asset Cost), 1-2900 Biaya Dikapitalisasi (Capitalization Offset), 4-1500 Pendapatan Lain-lain (Depreciation Expense), 4-7002 Gain and Loss on Disposal (Gain on Disposal), 4-9100 Laba Pelepasan Aset (Gain on Disposal), 5-9100 Rugi Pelepasan Aset (Loss on Disposal). Inactive: 4-9200 Laba Lama (Gain on Disposal), 5-9200 Rugi Lama (Loss on Disposal), 1-2950 Biaya Lama (Capitalization Offset), 4-1600 Pendapatan Lama (Depreciation Expense).
- Data TC-FA-PREF-588 sampai 591: seri PC (TC-FA-PREF-362-621), company `PT Contoh Konstruksi` plan Growth (PC-1): seluruh setting tersimpan pada nilai awal, belum ada posting penyusutan, semua periode Open; Chart of Accounts PC-5. Active: 1-1001 Kas Utama (Asset Cost), 1-2900 Biaya Dikapitalisasi (Capitalization Offset), 1-2910 Biaya Dikapitalisasi Proyek (Capitalization Offset), 4-7002 Gain and Loss on Disposal (Gain on Disposal), 4-1500 Pendapatan Lain-lain (Depreciation Expense), 4-9100 Laba Pelepasan Aset (Gain on Disposal), 5-9100 Rugi Pelepasan Aset (Loss on Disposal). Inactive: 6-9300 Rugi Penghapusan Lama (Loss on Disposal) dan 1-2950 Biaya Lama (Capitalization Offset).
- Seri PA dan PC memakai Chart of Accounts yang tidak setara (PA-3 dan PC-5); spec men-seed ulang company ke seri PC (PC-1, PC-5) lewat API sebelum blok TC-FA-PREF-588 sampai 591 (langkah 18 dan 19).
- State yang diubah spec: tidak ada (spec hanya membaca daftar opsi). Hook `after` memulihkan Chart of Accounts dan Preferences ke nilai awal lewat seed API.
- Seed dan pemulihan lewat API (Preferences ke nilai awal, plan, penguncian, versi Tax Depreciation Class, transaksi bertanggal, akun Chart of Accounts) disediakan tim FE/BE: butir "Seed dan pemulihan lewat API" di `suite.md`.
- Flag Guided Tooltip halaman Preferences: hook suite `before` men-set true untuk akun aktor dan `after` memulihkannya (butir "Flag Guided Tooltip" di `suite.md`).
- Identitas data Pre-setup dibaca dari `fixtures/settings-accounting-preferences.json` (belum ada; disediakan tim FE, nama kunci ditetapkan tim FE). Nama data Pre-setup ditulis seperti di TC.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-PREF-171: Opsi Select Default Gain on Disposal memuat akun Active ber-function Gain atau Loss on Disposal urut kode A-Z

1. Klik Select Default Gain on Disposal
2. Verifikasi opsi Select Default Gain on Disposal berurutan kode A-Z: `4-7002 – Gain and Loss on Disposal | 4-9100 – Laba Pelepasan Aset | 5-9100 – Rugi Pelepasan Aset`
3. Verifikasi daftar opsi tidak memuat akun Inactive "4-9200 – Laba Lama"
4. Verifikasi daftar opsi tidak memuat akun ber-function lain "1-1001 – Kas Utama" dan "4-1500 – Pendapatan Lain-lain"
5. Tutup daftar opsi Select Default Gain on Disposal

### TC-FA-PREF-172: Opsi Select Default Loss on Disposal memuat function yang sama dengan Default Gain on Disposal

6. Klik Select Default Loss on Disposal
7. Verifikasi opsi Select Default Loss on Disposal berurutan kode A-Z: `4-7002 – Gain and Loss on Disposal | 4-9100 – Laba Pelepasan Aset | 5-9100 – Rugi Pelepasan Aset`
8. Verifikasi daftar opsi tidak memuat akun Inactive "5-9200 – Rugi Lama"
9. Tutup daftar opsi Select Default Loss on Disposal

### TC-FA-PREF-173: Opsi Select Default Capitalization Offset hanya akun Active ber-function Capitalization Offset

10. Klik Select Default Capitalization Offset
11. Verifikasi opsi Select Default Capitalization Offset hanya `1-2900 – Biaya Dikapitalisasi`
12. Verifikasi daftar opsi tidak memuat akun Inactive "1-2950 – Biaya Lama" dan akun function lain
13. Tutup daftar opsi Select Default Capitalization Offset

### TC-FA-PREF-174: Opsi Select Found Asset Credit Account memuat seluruh akun Active tanpa filter function urut kode A-Z

14. Klik Select Found Asset Credit Account
15. Verifikasi opsi Select Found Asset Credit Account berurutan kode A-Z: `1-1001 – Kas Utama | 1-2900 – Biaya Dikapitalisasi | 4-1500 – Pendapatan Lain-lain | 4-7002 – Gain and Loss on Disposal | 4-9100 – Laba Pelepasan Aset | 5-9100 – Rugi Pelepasan Aset`
16. Verifikasi daftar opsi tidak memuat akun Inactive "4-1600 – Pendapatan Lama"
17. Tutup daftar opsi Select Found Asset Credit Account

### TC-FA-PREF-588: Opsi Select Default Gain on Disposal hanya memuat akun Active sesuai function dan tidak memuat akun Inactive

18. Seed ulang company ke seri PC (Preferences PC-1 dan Chart of Accounts PC-5) lewat API hingga tersimpan
19. Buka ulang Fixed Asset > Settings > Accounting > Preferences
20. Klik Select Default Gain on Disposal
21. Verifikasi daftar opsi berurutan menurut kode akun A-Z berisi: 4-7002 – Gain and Loss on Disposal, 4-9100 – Laba Pelepasan Aset, 5-9100 – Rugi Pelepasan Aset
22. Verifikasi daftar opsi tidak memuat: 6-9300 – Rugi Penghapusan Lama
23. Tutup daftar opsi Select Default Gain on Disposal

### TC-FA-PREF-589: Opsi Select Default Loss on Disposal hanya memuat akun Active sesuai function dan tidak memuat akun Inactive

24. Klik Select Default Loss on Disposal
25. Verifikasi daftar opsi berurutan menurut kode akun A-Z berisi: 4-7002 – Gain and Loss on Disposal, 4-9100 – Laba Pelepasan Aset, 5-9100 – Rugi Pelepasan Aset
26. Verifikasi daftar opsi tidak memuat: 6-9300 – Rugi Penghapusan Lama
27. Tutup daftar opsi Select Default Loss on Disposal

### TC-FA-PREF-590: Opsi Select Default Capitalization Offset hanya memuat akun Active sesuai function dan tidak memuat akun Inactive

28. Klik Select Default Capitalization Offset
29. Verifikasi daftar opsi berurutan menurut kode akun A-Z berisi: 1-2900 – Biaya Dikapitalisasi, 1-2910 – Biaya Dikapitalisasi Proyek
30. Verifikasi daftar opsi tidak memuat: 1-2950 – Biaya Lama
31. Tutup daftar opsi Select Default Capitalization Offset

### TC-FA-PREF-591: Opsi Select Found Asset Credit Account memuat seluruh akun Active tanpa filter function dan tidak memuat akun Inactive

32. Klik Select Found Asset Credit Account
33. Verifikasi daftar opsi berurutan menurut kode akun A-Z berisi: 1-1001 – Kas Utama, 1-2900 – Biaya Dikapitalisasi, 1-2910 – Biaya Dikapitalisasi Proyek, 4-1500 – Pendapatan Lain-lain, 4-7002 – Gain and Loss on Disposal, 4-9100 – Laba Pelepasan Aset, 5-9100 – Rugi Pelepasan Aset
34. Verifikasi daftar opsi tidak memuat: 6-9300 – Rugi Penghapusan Lama, 1-2950 – Biaya Lama
35. Tutup daftar opsi Select Found Asset Credit Account

## Notes

- Sumber: `fixed-asset/settings-accounting-preferences/TestCases/tc-settings-accounting-preferences.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Mode: FE+BE.
- Langkah 1 TC ("Buka Tab Preferences") dijalankan hook `beforeEach` suite.
- Langkah penghubung (S-03): menutup daftar opsi: langkah 5, 9, 13, 17, 23, 27, 31, 35; memulihkan state server ke seri PC lewat seed/API dan membuka ulang halaman: langkah 18, 19.
- Asersi absence akun (langkah 3, 4, 8, 12, 16, 22, 26, 30, 34) didahului `Verifikasi` daftar opsi berurutan yang memuat akun pembanding pada daftar yang sama (8b.2); daftar opsi diasersi saat terbuka (8b.5).
- Pada TC-FA-PREF-171, butir b "akun function Loss on Disposal (5-9100) tetap muncul" sudah tercakup oleh daftar opsi pada langkah 2 yang memuat 5-9100; tidak dibuat langkah terpisah.
- Spec 35 langkah dengan 8 TC berpola sama (buka Select, periksa daftar, tutup); seluruh blok satu topik dan satu kelas fungsional. Perbedaan seri PA dan PC memerlukan seed ulang antar-blok (langkah 18, 19).
- Temuan untuk QA:
  - TC-FA-PREF-171 dan 172 menyebut bahwa Select Default Gain/Loss memuat akun ber-function Loss on Disposal (5-9100) dan akun Gain (4-9100) pada kedua Select (function yang sama); ini sesuai Expected, tetapi nama TC-FA-PREF-171 ("Gain atau Loss on Disposal") dan TC-FA-PREF-588 ("sesuai function") tidak menjelaskan aturan function lain; spec hanya mengasersi daftar tertulis.
  - TC-FA-PREF-173 menulis "akun function lain tidak muncul" tanpa merinci akun; spec mengasersi absence "1-2950 – Biaya Lama" bersama "akun function lain" yang sudah tercakup oleh daftar tunggal pada langkah 11.
  - Seri PA (PA-3) dan seri PC (PC-5) berbeda isi Chart of Accounts (PC memuat 1-2910 dan 6-9300 dan tidak memuat 4-9200, 5-9200, 4-1600); spec menjalankan keduanya sebagai blok terpisah dengan seed ulang.
  - Post Condition kosong pada TC-FA-PREF-171 sampai 174 dan 588 sampai 591; tidak ada yang diasersi lebih lanjut.
