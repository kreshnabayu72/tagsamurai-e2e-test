---
id: TC-FA-PREF-E2E-051-journal-grouping-dikosongkan-ketiga-dimensi-dan-cancel-mengembalikan-nilai-tersimpan
title: "Journal Grouping dikosongkan, memilih ketiga dimensi, dan Cancel mengembalikan Select akun dan MultiSelect ke nilai tersimpan"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-PREF-166
  - TC-FA-PREF-167
  - TC-FA-PREF-275
coverage:
  web: automated
---

# Journal Grouping dikosongkan, memilih ketiga dimensi, dan Cancel mengembalikan Select akun dan MultiSelect ke nilai tersimpan

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup) `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net` pada company `PT Contoh Konstruksi`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Env var `FA_TC_PASSWORD` belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`: didaftarkan tim FE. Password tidak ditulis di spec atau fixture.
- Data TC-FA-PREF-275: seri PB (TC-FA-PREF-176-361), company `PT Contoh Konstruksi` plan Growth (PB-1): Preferences nilai awal (Fiscal Year Start January, First Accounting Period Mar 2026, Default Capitalization Threshold 5.000.000, akun default kosong, Journal Grouping Group); akun Chart of Accounts PB-2 (termasuk "1-2900 – Biaya Dikapitalisasi").
- Data TC-FA-PREF-166 dan 167: seri PA (TC-FA-PREF-1-175), company `PT Contoh Konstruksi` plan Growth (PA-1): Preferences nilai awal PA-2 (tidak terkunci, semua setting wajib terisi; Journal Grouping Group; akun default kosong).
- Seri fixture PA dan PB bernilai awal setara (PA-2, PB-1); spec men-seed ulang lewat API di antara TC sesuai Precondition TC.
- State yang diubah spec: Journal Grouping tersimpan (kosong, lalu Group, Category, Asset Class) dan entri Changelog hasil Save. Hook `after` memulihkan Preferences ke nilai awal lewat seed API.
- Seed dan pemulihan lewat API (Preferences ke nilai awal, plan, penguncian, versi Tax Depreciation Class, transaksi bertanggal, akun Chart of Accounts) disediakan tim FE/BE: butir "Seed dan pemulihan lewat API" di `suite.md`.
- Flag Guided Tooltip halaman Preferences: hook suite `before` men-set true untuk akun aktor dan `after` memulihkannya (butir "Flag Guided Tooltip" di `suite.md`).
- Identitas data Pre-setup dibaca dari `fixtures/settings-accounting-preferences.json` (belum ada; disediakan tim FE, nama kunci ditetapkan tim FE). Nama data Pre-setup ditulis seperti di TC.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-PREF-275: Klik [Cancel] mengembalikan Select akun dan MultiSelect Journal Grouping ke nilai tersimpan

1. Pilih "1-2900 – Biaya Dikapitalisasi" pada Select Default Capitalization Offset
2. Centang opsi "Category" pada MultiSelect Journal Grouping
3. Klik `[Cancel]`
4. Verifikasi Select Default Capitalization Offset kembali menampilkan placeholder "Select account"
5. Verifikasi MultiSelect Journal Grouping kembali menampilkan hanya chip "Group"
6. Verifikasi tidak ada dialog
7. Verifikasi tidak ada toast
8. Verifikasi `[Save changes]` berstatus Disabled
9. Verifikasi `[Cancel]` berstatus Disabled

### TC-FA-PREF-166: Journal Grouping boleh dikosongkan tanpa caption validasi dan dapat disimpan

10. Seed ulang Preferences company ke nilai awal PA-2 lewat API hingga tersimpan
11. Buka ulang Fixed Asset > Settings > Accounting > Preferences
12. Hapus pilihan "Group" pada MultiSelect Journal Grouping
13. Verifikasi MultiSelect Journal Grouping kosong dengan placeholder "Select journal grouping"
14. Verifikasi tidak ada caption pada MultiSelect Journal Grouping
15. Klik `[Save changes]`
16. Verifikasi tidak ada dialog "Save Changes" (Journal Grouping bukan setting berdampak)
17. Verifikasi toast "Success, accounting preferences have been saved." tampil

### TC-FA-PREF-167: Journal Grouping dapat memilih ketiga dimensi sekaligus dan disimpan tanpa dialog

18. Seed ulang Preferences company ke nilai awal PA-2 (Journal Grouping Group) lewat API hingga tersimpan
19. Buka ulang Fixed Asset > Settings > Accounting > Preferences
20. Tambahkan opsi "Category" dan "Asset Class" pada MultiSelect Journal Grouping
21. Verifikasi MultiSelect Journal Grouping menampilkan tiga pilihan "Group", "Category", "Asset Class"
22. Klik `[Save changes]`
23. Verifikasi tidak ada dialog "Save Changes"
24. Verifikasi toast "Success, accounting preferences have been saved." tampil

## Notes

- Sumber: `fixed-asset/settings-accounting-preferences/TestCases/tc-settings-accounting-preferences.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Mode: FE+BE.
- Urutan blok: TC-FA-PREF-275 (tanpa Save, seri PB) lebih dulu, lalu TC-FA-PREF-166 dan 167 (Save, seri PA) (S-10). Langkah 1 TC ("Buka Tab Preferences") dijalankan hook `beforeEach` suite.
- Langkah penghubung (S-03): memulihkan state server lewat seed/API dan membuka ulang halaman sebelum TC berikutnya: langkah 10, 11, 18, 19.
- Pengondisian "Group" pada langkah 12 (hapus pilihan) dan penambahan pada langkah 20 mengikuti nilai awal PA-2 (Journal Grouping Group).
- Post Condition TC-FA-PREF-166 dan 167 (Journal Grouping tersimpan; entri Changelog Field Journal Grouping, Old Value, New Value) tidak punya langkah observasi di TC sehingga tidak diasersi (S-01); entri Changelog ditutup oleh spec log terkait.
- Temuan untuk QA:
  - TC-FA-PREF-166 dan 167 meminta Post Condition entri Changelog tanpa langkah observasi di TC; spec tidak mengasersinya.
  - TC-FA-PREF-275 memakai seri PB dan TC-FA-PREF-166 dan 167 memakai seri PA; spec mengasumsikan nilai awal setara (PA-2 dan PB-1) dengan seed ulang di antara blok.
  - Post Condition TC-FA-PREF-275 ("Preferences company belum berubah") tidak punya langkah observasi sehingga tidak diasersi.
