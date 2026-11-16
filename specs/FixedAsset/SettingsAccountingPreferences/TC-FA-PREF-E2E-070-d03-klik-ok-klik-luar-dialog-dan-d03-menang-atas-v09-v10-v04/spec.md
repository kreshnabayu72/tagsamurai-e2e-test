---
id: TC-FA-PREF-E2E-070-d03-klik-ok-klik-luar-dialog-dan-d03-menang-atas-v09-v10-v04
title: "D-03: Klik [OK] Memuat Ulang Form, Klik Luar Tidak Menutup, D-03 Menang atas V-09, V-10, V-04"
layer: ui-e2e
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-PREF-254
  - TC-FA-PREF-255
  - TC-FA-PREF-256
sourceRules: ["D-03", "ST-05", "F-FAPREF-01.k6d", "ST-01", "E-FAPREF-06", "§6#p2", "ST-27"]
smoke: []
dependsOn: []
trace:
  "D-03": [7, 19, 29, 30]
  "ST-05": [8, 9]
  "F-FAPREF-01.k6d": [8, 9, 10]
  "ST-01": 11
  "E-FAPREF-06": 29
  "§6#p2": 31
  "ST-27": 32
anchor: [18]
coverage:
  web: automated
---

# D-03: Klik [OK] Memuat Ulang Form, Klik Luar Tidak Menutup, D-03 Menang atas V-09, V-10, V-04

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup, company `PT Contoh Konstruksi`): `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Accounting > Preferences). Hook `after` mengembalikan sesi ke akun default suite.
- Env var `FA_TC_PASSWORD` belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`: didaftarkan tim FE. Password tidak ditulis di spec atau fixture.
- Data Pre-setup PB-1 (company `PT Contoh Konstruksi`, plan Growth, entitas Active; Preferences nilai awal: Fiscal Year Start January, First Accounting Period Mar 2026, Default Capitalization Threshold 5.000.000, In-service Date Source Activation date, Depreciation in Disposal Month Up to previous month, Default Gain/Loss on Disposal, Default Capitalization Offset dan Found Asset Credit Account kosong, Disposal Documents semua jenis Optional, Journal Grouping Group; periode Mar 2026 sampai Dec 2026 Open; belum ada penyusutan diposting) dan PB-2 (akun Chart of Accounts uji). PB-8 (Tax Depreciation Class `Commercial Building` dengan versi kedua Effective From 01/07/26) dan PB-9 (transaksi aktivasi aset bertanggal 15/05/26) untuk TC-256.
- Seed dan pemulihan lewat API (Preferences ke nilai awal, Asset Class, pelepasan, akun Chart of Accounts, penguncian) disediakan tim FE/BE (butir "Seed dan pemulihan lewat API" di `suite.md`); tiap TC dijalankan dari keadaan awal yang dinyatakan di Precondition TC-nya.
- Identitas data Pre-setup dibaca dari `fixtures/settings-accounting-preferences.json` (belum ada; disediakan tim FE, nama kunci ditetapkan tim FE). Nama akun dan Asset Class ditulis seperti di TC.
- Flag Guided Tooltip halaman Preferences: hook suite `before` men-set true dan `after` memulihkannya (butir "Flag Guided Tooltip" di `suite.md`).
- Sesi API aktor untuk pemicu perubahan state (fixture BE): kemampuan disediakan tim BE/FE (butir "Sesi API aktor" di `suite.md`).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-PREF-254: Klik [OK] pada D-03 memuat ulang form dari nilai tersimpan

1. Ubah Select Fiscal Year Start dari "January" menjadi "July"
2. Ubah Select In-service Date Source menjadi "Manual by Accounting"
3. Klik [Save changes] sampai dialog D-01 tampil
4. Lewat sesi API (fixture BE), tandai posting penyusutan pertama pada Asset Class IT Equipment hingga status tersimpan
5. Klik [Save] pada dialog D-01 sampai dialog D-03 tampil
6. Klik [OK] pada dialog D-03
7. Verifikasi dialog D-03 tertutup
8. Verifikasi Select Fiscal Year Start menampilkan "January" berstatus Disabled dengan ikon gembok
9. Verifikasi Select bulan dan Select tahun First Accounting Period menampilkan "March" dan "2026" berstatus Disabled dengan ikon gembok
10. Verifikasi Select In-service Date Source menampilkan "Activation date" (perubahan belum disimpan dibuang)
11. Verifikasi [Save changes] dan [Cancel] berstatus Disabled karena form pristine
12. Pulihkan kunci dan Preferences ke PB-1 lewat seed API, lalu muat ulang halaman dengan F5

### TC-FA-PREF-255: Klik area di luar dialog D-03 tidak menutup dialog

13. Ubah Select Fiscal Year Start dari "January" menjadi "July"
14. Klik [Save changes] sampai dialog D-01 tampil
15. Lewat sesi API (fixture BE), tandai posting penyusutan pertama pada Asset Class IT Equipment hingga status tersimpan
16. Klik [Save] pada dialog D-01 sampai dialog D-03 tampil
17. Klik area backdrop gelap di luar dialog D-03
18. Verifikasi dialog D-03 berjudul "Cannot Save Preferences" tetap terbuka
19. Verifikasi tombol [OK] masih satu-satunya tombol
20. Klik [OK] pada dialog D-03
21. Pulihkan kunci dan Preferences ke PB-1 lewat seed API, lalu muat ulang halaman dengan F5

### TC-FA-PREF-256: D-03 menang atas V-09, V-10, dan V-04 saat kunci berubah bersamaan dengan penolakan lain

22. Seed PB-8 (versi kedua Tax Depreciation Class Commercial Building) dan PB-9 (transaksi bertanggal 15/05/26) lewat API, lalu muat ulang halaman dengan F5
23. Ubah Select Fiscal Year Start dari "January" menjadi "April"
24. Ubah Select bulan First Accounting Period dari "March" menjadi "June"
25. Pilih "4-9100 – Laba Pelepasan Aset" pada Select Default Gain on Disposal
26. Klik [Save changes] sampai dialog D-01 tampil
27. Lewat sesi API (fixture BE), ubah status akun 4-9100 menjadi Inactive dan tandai posting penyusutan pertama pada Asset Class IT Equipment hingga status tersimpan
28. Klik [Save] pada dialog D-01
29. Verifikasi dialog D-03 berjudul "Cannot Save Preferences" tampil
30. Verifikasi body dialog D-03: "Fiscal Year Start and First Accounting Period are locked because depreciation has been posted or a period has been closed. The page has been reloaded with the latest lock status."
31. Verifikasi tidak ada caption V-09, V-10, maupun V-04 pada field mana pun
32. Verifikasi tidak ada toast yang tampil
33. Klik [OK] pada dialog D-03
34. Pulihkan kunci, akun 4-9100, PB-8, PB-9 dan Preferences ke PB-1 lewat seed API, lalu muat ulang halaman dengan F5

## Notes

- Langkah penghubung (S-03): klik [OK] pada D-03 dan pemulihan seed di akhir tiap TC. Pemicu kunci lewat sesi API aktor (fixture BE) bukan konteks kedua.
- Asersi absence caption V-09, V-10, V-04 dan toast pada TC-256 didahului Verifikasi D-03 tampil sebagai anchor (bagian 8b butir 2).
- Temuan untuk QA:
  - Post Condition "Preferences company belum berubah ..." tidak punya langkah observasi di TC ini, sehingga tidak diasersi (S-01).
  - TC-255 tidak mencantumkan cara menutup D-03 setelah asersi; spec menambah klik [OK] sebagai langkah penghubung.
