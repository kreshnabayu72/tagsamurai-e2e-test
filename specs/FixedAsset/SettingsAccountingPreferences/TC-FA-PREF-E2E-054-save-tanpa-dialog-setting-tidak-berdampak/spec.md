---
id: TC-FA-PREF-E2E-054-save-tanpa-dialog-setting-tidak-berdampak
title: "Save Tanpa Dialog: In-service Date Source, Default Capitalization Offset, Found Asset Credit Account, Journal Grouping"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-PREF-176
  - TC-FA-PREF-178
  - TC-FA-PREF-179
  - TC-FA-PREF-180
coverage:
  web: automated
---

# Save Tanpa Dialog: In-service Date Source, Default Capitalization Offset, Found Asset Credit Account, Journal Grouping

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup, company `PT Contoh Konstruksi`): `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Accounting > Preferences). Hook `after` mengembalikan sesi ke akun default suite.
- Env var `FA_TC_PASSWORD` belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`: didaftarkan tim FE. Password tidak ditulis di spec atau fixture.
- Data Pre-setup PB-1 (company `PT Contoh Konstruksi`, plan Growth, entitas Active; Preferences nilai awal: Fiscal Year Start January, First Accounting Period Mar 2026, Default Capitalization Threshold 5.000.000, In-service Date Source Activation date, Depreciation in Disposal Month Up to previous month, Default Gain/Loss on Disposal, Default Capitalization Offset dan Found Asset Credit Account kosong, Disposal Documents semua jenis Optional, Journal Grouping Group; periode Mar 2026 sampai Dec 2026 Open; belum ada penyusutan diposting) dan PB-2 (akun Chart of Accounts uji).
- Seed dan pemulihan lewat API (Preferences ke nilai awal, Asset Class, pelepasan, akun Chart of Accounts, penguncian) disediakan tim FE/BE (butir "Seed dan pemulihan lewat API" di `suite.md`); tiap TC dijalankan dari keadaan awal yang dinyatakan di Precondition TC-nya.
- Identitas data Pre-setup dibaca dari `fixtures/settings-accounting-preferences.json` (belum ada; disediakan tim FE, nama kunci ditetapkan tim FE). Nama akun dan Asset Class ditulis seperti di TC.
- Flag Guided Tooltip halaman Preferences: hook suite `before` men-set true dan `after` memulihkannya (butir "Flag Guided Tooltip" di `suite.md`).
- Data Dinamis DB-1 (nilai Preferences hasil Save) dipulihkan ke PB-1 lewat seed API sebelum TC berikutnya dan di hook `after`.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-PREF-176: Save hanya mengubah In-service Date Source menjadi Manual by Accounting

1. Ubah Select In-service Date Source dari "Activation date" menjadi "Manual by Accounting"
2. Klik [Save changes]
3. Verifikasi toast "Success, accounting preferences have been saved." tampil di kanan bawah layar
4. Verifikasi tidak ada dialog D-01 yang tampil setelah klik [Save changes]
5. Verifikasi Select In-service Date Source menampilkan "Manual by Accounting"
6. Verifikasi tidak ada langkah approval dan tidak ada notifikasi; nilai langsung berlaku setelah Save
7. Verifikasi form tetap terbuka dengan nilai tersimpan
8. Verifikasi [Save changes] dan [Cancel] berstatus Disabled (tetap tampil, tidak dapat diklik)
9. Pulihkan Preferences ke nilai awal PB-1 lewat seed API, lalu muat ulang halaman dengan F5

### TC-FA-PREF-178: Save hanya mengubah Default Capitalization Offset ke akun 1-2900

10. Buka Select Default Capitalization Offset lalu pilih "1-2900 – Biaya Dikapitalisasi"
11. Klik [Save changes]
12. Verifikasi toast "Success, accounting preferences have been saved." tampil di kanan bawah layar
13. Verifikasi tidak ada dialog D-01 yang tampil setelah klik [Save changes]
14. Verifikasi Select Default Capitalization Offset menampilkan "1-2900 – Biaya Dikapitalisasi"
15. Verifikasi form tetap terbuka dengan nilai tersimpan
16. Verifikasi [Save changes] dan [Cancel] berstatus Disabled (tetap tampil, tidak dapat diklik)
17. Pulihkan Preferences ke nilai awal PB-1 lewat seed API, lalu muat ulang halaman dengan F5

### TC-FA-PREF-179: Save hanya mengubah Found Asset Credit Account ke akun 1-1001

18. Buka Select Found Asset Credit Account lalu pilih "1-1001 – Kas Utama"
19. Klik [Save changes]
20. Verifikasi toast "Success, accounting preferences have been saved." tampil di kanan bawah layar
21. Verifikasi tidak ada dialog D-01 yang tampil setelah klik [Save changes]
22. Verifikasi Select Found Asset Credit Account menampilkan "1-1001 – Kas Utama"
23. Verifikasi form tetap terbuka dengan nilai tersimpan
24. Verifikasi [Save changes] dan [Cancel] berstatus Disabled (tetap tampil, tidak dapat diklik)
25. Pulihkan Preferences ke nilai awal PB-1 lewat seed API, lalu muat ulang halaman dengan F5

### TC-FA-PREF-180: Save hanya mengubah Journal Grouping dengan menambah dimensi Category

26. Buka MultiSelect Journal Grouping lalu centang opsi "Category" sehingga terpilih "Group" dan "Category"
27. Klik [Save changes]
28. Verifikasi toast "Success, accounting preferences have been saved." tampil di kanan bawah layar
29. Verifikasi tidak ada dialog D-01 yang tampil setelah klik [Save changes]
30. Verifikasi MultiSelect Journal Grouping menampilkan chip "Group" dan chip "Category"
31. Verifikasi form tetap terbuka dengan nilai tersimpan
32. Verifikasi [Save changes] dan [Cancel] berstatus Disabled (tetap tampil, tidak dapat diklik)
33. Pulihkan Preferences ke nilai awal PB-1 lewat seed API, lalu muat ulang halaman dengan F5

## Notes

- Langkah penghubung (S-03): pemulihan Preferences lewat seed API dan muat ulang di akhir tiap TC, tanpa Verifikasi (S-09).
- Urutan Verifikasi: toast sukses diasersi lebih dulu sebagai anchor positif sebelum asersi absence dialog D-01 (bagian 8b butir 2); urutan ini menyimpang dari urutan penulisan Expected TC.
- Temuan untuk QA:
  - Post Condition "Entri log L-02 untuk setting yang berubah ditulis (diuji pada Section 5)" tidak punya langkah observasi di TC ini, sehingga tidak diasersi; pencatatan log diuji pada TC Section 5.
  - TC-176 Expected d "tidak ada langkah approval dan tidak ada notifikasi" tidak memberi baseline atau cara cek notifikasi; spec mengasersinya pada layar (tanpa dialog atau status approval).
