---
id: TC-FA-PREF-E2E-162-select-offset-dan-found-asset-tanpa-shortcut-dan-save-akun-gabungan-gain-loss
title: "Select Default Capitalization Offset, Found Asset Credit Account, dan Default Disposal Proceeds Account tanpa shortcut Create account, dan akun gabungan Gain dan Loss disimpan lewat dialog"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-PREF-170
  - TC-FA-PREF-592
coverage:
  web: automated
---

# Select Default Capitalization Offset, Found Asset Credit Account, dan Default Disposal Proceeds Account tanpa shortcut Create account, dan akun gabungan Gain dan Loss disimpan lewat dialog

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup) `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net` pada company `PT Contoh Konstruksi`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Env var `FA_TC_PASSWORD` belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`: didaftarkan tim FE. Password tidak ditulis di spec atau fixture.
- Data TC-FA-PREF-170: seri PA (TC-FA-PREF-1-175), company `PT Contoh Konstruksi` plan Growth (PA-1): Preferences nilai awal PA-2 (tidak terkunci, semua setting wajib terisi; akun default kosong); Chart of Accounts PA-3 (Active: 1-1001 Kas Utama, 1-2900 Biaya Dikapitalisasi, 4-1500 Pendapatan Lain-lain, 4-7002 Gain and Loss on Disposal, 4-9100 Laba Pelepasan Aset, 5-9100 Rugi Pelepasan Aset).
- Data TC-FA-PREF-592: seri PC (TC-FA-PREF-362-621), company `PT Contoh Konstruksi` plan Growth (PC-1): seluruh setting tersimpan pada nilai awal, belum ada posting penyusutan, semua periode Open; Asset Class IT Equipment dan Vehicles mengosongkan akun Gain, Asset Class IT Equipment mengosongkan akun Loss; ada 3 pelepasan belum diposting (PC-5, PC-6, PC-7), disediakan tim FE.
- Seri fixture PA dan PC bernilai awal setara (PA-2, PC-1); spec men-seed ulang lewat API di antara TC sesuai Precondition TC.
- State yang diubah spec: Default Gain on Disposal dan Default Loss on Disposal tersimpan 4-7002 (TC-FA-PREF-592) dan entri log hasil Save. Hook `after` memulihkan Preferences ke nilai awal lewat seed API.
- Seed dan pemulihan lewat API (Preferences ke nilai awal, plan, penguncian, versi Tax Depreciation Class, transaksi bertanggal, akun Chart of Accounts, pelepasan menunggu posting) disediakan tim FE/BE: butir "Seed dan pemulihan lewat API" di `suite.md`.
- Flag Guided Tooltip halaman Preferences: hook suite `before` men-set true untuk akun aktor dan `after` memulihkannya (butir "Flag Guided Tooltip" di `suite.md`).
- Identitas data Pre-setup dibaca dari `fixtures/settings-accounting-preferences.json` (belum ada; disediakan tim FE, nama kunci ditetapkan tim FE). Nama data Pre-setup ditulis seperti di TC.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-PREF-170: Select Default Capitalization Offset, Found Asset Credit Account, dan Default Disposal Proceeds Account tidak memiliki shortcut Create account

1. Klik Select Default Gain on Disposal
2. Verifikasi shortcut `+ Create account` tampil pada Select Default Gain on Disposal
3. Tutup daftar opsi Select Default Gain on Disposal
4. Klik Select Default Capitalization Offset
5. Verifikasi daftar opsi Select Default Capitalization Offset memuat "1-2900 – Biaya Dikapitalisasi"
6. Verifikasi Select Default Capitalization Offset tidak memiliki shortcut `+ Create account`
7. Tutup daftar opsi Select Default Capitalization Offset
8. Klik Select Found Asset Credit Account
9. Verifikasi daftar opsi Select Found Asset Credit Account memuat "1-1001 – Kas Utama"
10. Verifikasi Select Found Asset Credit Account tidak memiliki shortcut `+ Create account`
11. Tutup daftar opsi Select Found Asset Credit Account
12. Klik Select Default Disposal Proceeds Account
13. Verifikasi Select Default Disposal Proceeds Account tidak memiliki shortcut `+ Create account`
14. Tutup daftar opsi Select Default Disposal Proceeds Account

### TC-FA-PREF-592: Akun gabungan Gain dan Loss dapat dipilih di kedua Select dan disimpan

15. Seed ulang Preferences company ke nilai awal PC-1 lewat API hingga tersimpan
16. Buka ulang Fixed Asset > Settings > Accounting > Preferences
17. Pilih "4-7002 – Gain and Loss on Disposal" pada Select Default Gain on Disposal
18. Pilih "4-7002 – Gain and Loss on Disposal" pada Select Default Loss on Disposal
19. Klik `[Save changes]`
20. Verifikasi dialog "Save Changes" (severity warning) tampil dengan bullet baris dampak "2 asset classes use the default account. 3 unposted disposals will use the new account.", lalu pertanyaan "Are you sure you want to save these changes?", dan tombol `[Cancel]` dan `[Save]`
21. Klik `[Save]` pada dialog "Save Changes"
22. Verifikasi toast "Success, accounting preferences have been saved." tampil
23. Verifikasi Select Default Gain on Disposal menampilkan "4-7002 – Gain and Loss on Disposal"
24. Verifikasi Select Default Loss on Disposal menampilkan "4-7002 – Gain and Loss on Disposal"

## Notes

- Sumber: `fixed-asset/settings-accounting-preferences/TestCases/tc-settings-accounting-preferences.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Mode: FE+BE.
- Urutan blok: TC-FA-PREF-170 (tidak mengubah state) lebih dulu, lalu TC-FA-PREF-592 yang menyimpan (S-10). Langkah 1 TC ("Buka Tab Preferences") dijalankan hook `beforeEach` suite.
- Langkah penghubung (S-03): menutup daftar opsi: langkah 3, 7, 11, 14; memulihkan state server lewat seed/API dan membuka ulang halaman sebelum TC berikutnya: langkah 15, 16.
- Langkah 1 sampai 3 adalah anchor positif asersi absence shortcut (8b.2): shortcut `+ Create account` pada Select Default Gain on Disposal membuktikan bahwa shortcut tampil pada Select yang memilikinya; langkah 5 dan 9 membuktikan daftar opsi kedua Select sudah termuat; Select Default Disposal Proceeds Account (langkah 12 sampai 14) memakai pembanding yang sama. Bentuk dan posisi shortcut mengikuti TC-FA-PREF-168 (tampil pada Select).
- Post Condition TC-FA-PREF-592 (kedua default tersimpan 4-7002) hanya diasersi lewat tampilan Select sesudah Save (langkah 23, 24); nilai tersimpan di server dan entri log tidak punya langkah observasi di TC dan tidak diasersi.
- Temuan untuk QA:
  - TC-FA-PREF-170 butir c (Select Default Disposal Proceeds Account) tidak menyebut opsi yang diharapkan; data PA-3 tidak memuat akun ber-function Disposal Proceeds (akun itu ada di PC-22), sehingga daftar opsi Select tersebut dapat kosong dan spec hanya mengasersi ketiadaan shortcut `+ Create account`.
  - TC-FA-PREF-170 menyebut "Periksa Select" tanpa menjelaskan letak shortcut `+ Create account` (di dalam daftar opsi atau di samping Select) dan tidak menyebut pembanding positif; spec memakai Select Default Gain on Disposal sebagai pembanding berdasarkan TC-FA-PREF-168.
  - TC-FA-PREF-170 tidak menyebut opsi yang diharapkan pada kedua Select; opsi "1-2900 – Biaya Dikapitalisasi" dan "1-1001 – Kas Utama" diambil dari Expected TC-FA-PREF-173 dan 174.
  - TC-FA-PREF-592 butir a: angka "2 asset classes" dan "3 unposted disposals" bergantung pada data PC-5 sampai PC-7 yang disediakan tim FE; Precondition menyebut "Asset Class IT Equipment dan Vehicles mengosongkan akun Gain" tetapi tidak merinci Asset Class lain.
  - Post Condition TC yang tidak punya langkah observasi di TC (nilai tersimpan, entri log) tidak diasersi.
