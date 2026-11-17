---
id: TC-FA-PREF-E2E-063-d01-baris-dampak-berurutan-save-dan-cancel
title: "D-01 Baris Dampak Berurutan, Klik [Save] D-01 Menyimpan, [Cancel] D-01"
layer: ui-e2e
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-PREF-198
  - TC-FA-PREF-200
  - TC-FA-PREF-201
sourceRules: ["D-01", "PV-01", "PV-02", "PV-03", "PV-04", "PV-05", "§4.2b#p2", "F-FAPREF-01.k21b", "T-01", "FAPREF-LOGIC-03e", "§3.1#b6", "ST-01", "F-FAPREF-01.k21c", "§7.2#p1"]
smoke: []
dependsOn: []
trace:
  "D-01": [7, 9, 10]
  "PV-01": 8
  "PV-02": 8
  "PV-03": 8
  "PV-04": 8
  "PV-05": 8
  "§4.2b#p2": 11
  "F-FAPREF-01.k21b": 16
  "T-01": 17
  "FAPREF-LOGIC-03e": 18
  "§3.1#b6": 19
  "ST-01": [20, 28]
  "F-FAPREF-01.k21c": [25, 27]
  "§7.2#p1": 26
coverage:
  web: automated
---

# D-01 Baris Dampak Berurutan, Klik [Save] D-01 Menyimpan, [Cancel] D-01

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup, company `PT Contoh Konstruksi`): `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Accounting > Preferences). Hook `after` mengembalikan sesi ke akun default suite.
- Env var `FA_TC_PASSWORD` belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`: didaftarkan tim FE. Password tidak ditulis di spec atau fixture.
- Data Pre-setup PB-1 (company `PT Contoh Konstruksi`, plan Growth, entitas Active; Preferences nilai awal: Fiscal Year Start January, First Accounting Period Mar 2026, Default Capitalization Threshold 5.000.000, In-service Date Source Activation date, Depreciation in Disposal Month Up to previous month, Default Gain/Loss on Disposal, Default Capitalization Offset dan Found Asset Credit Account kosong, Disposal Documents semua jenis Optional, Journal Grouping Group; periode Mar 2026 sampai Dec 2026 Open; belum ada penyusutan diposting) dan PB-2 (akun Chart of Accounts uji). PB-3 (Asset Class IT Equipment, Vehicles, Furniture). PB-6b (2 pelepasan belum diposting dan menunggu posting).
- Jam sistem: bulan berjalan Oktober 2026 menurut Time Zone entitas, dasar hitungan "accounting periods will be rebuilt." pada dialog D-01; jam server dan browser diatur lewat kendali jam (butir "Kendali jam sistem" di `suite.md`) di hook `before` dan dipulihkan di hook `after` spec ini.
- Seed dan pemulihan lewat API (Preferences ke nilai awal, Asset Class, pelepasan, akun Chart of Accounts, penguncian) disediakan tim FE/BE (butir "Seed dan pemulihan lewat API" di `suite.md`); tiap TC dijalankan dari keadaan awal yang dinyatakan di Precondition TC-nya.
- Identitas data Pre-setup dibaca dari `fixtures/settings-accounting-preferences.json` (belum ada; disediakan tim FE, nama kunci ditetapkan tim FE). Nama akun dan Asset Class ditulis seperti di TC.
- Flag Guided Tooltip halaman Preferences: hook suite `before` men-set true dan `after` memulihkannya (butir "Flag Guided Tooltip" di `suite.md`).
- Langkah muat ulang saat form dirty: dialog `beforeunload` dikonfirmasi (kemampuan disediakan tim FE; dipakai pada langkah pemulihan).
- Data Dinamis DB-1 (nilai Preferences hasil Save) dipulihkan ke PB-1 lewat seed API sebelum TC berikutnya dan di hook `after`.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-PREF-198: D-01 menampilkan baris dampak berurutan PV-01 sampai PV-05

1. Seed 2 pelepasan belum diposting dan menunggu posting (PB-6b) lewat API
2. Ketik 10000000 pada CurrencyInput Default Capitalization Threshold
3. Ubah Select Depreciation in Disposal Month menjadi "Including disposal month"
4. Pilih "4-9100 – Laba Pelepasan Aset" pada Select Default Gain on Disposal
5. Ubah Select Fiscal Year Start dari "January" menjadi "July"
6. Klik [Save changes]
7. Verifikasi dialog D-01 berjudul "Save Changes" tampil (severity warning)
8. Verifikasi body dialog memuat daftar bullet: "2 asset classes use the default threshold."; "2 asset classes use the default account. 2 unposted disposals will use the new account."; "2 disposals waiting posting are affected."; "16 accounting periods will be rebuilt."; "Tax year start also follows Fiscal Year Start."
9. Verifikasi body dialog ditutup pertanyaan "Are you sure you want to save these changes?"
10. Verifikasi footer dialog memuat tombol [Cancel] (variant text, severity contrast) dan [Save]
11. Verifikasi urutan bullet dari atas ke bawah: PV-01, PV-02, PV-03, PV-04, PV-05
12. Muat ulang halaman dengan F5 dan konfirmasi dialog beforeunload (membuang perubahan yang belum disimpan)

### TC-FA-PREF-200: Klik [Save] pada D-01 menyimpan perubahan Default Capitalization Threshold

13. Ketik 10000000 pada CurrencyInput Default Capitalization Threshold
14. Klik [Save changes]
15. Klik [Save] pada dialog D-01
16. Verifikasi dialog D-01 tertutup
17. Verifikasi toast "Success, accounting preferences have been saved." tampil di kanan bawah layar
18. Verifikasi CurrencyInput Default Capitalization Threshold menampilkan "Rp 10.000.000,00"
19. Verifikasi form tetap terbuka dengan nilai tersimpan
20. Verifikasi [Save changes] dan [Cancel] berstatus Disabled (tetap tampil, tidak dapat diklik)
21. Pulihkan Preferences ke nilai awal PB-1 lewat seed API, lalu muat ulang halaman dengan F5

### TC-FA-PREF-201: Klik [Cancel] pada D-01 menutup dialog tanpa menyimpan dan form tetap memuat perubahan

22. Ketik 10000000 pada CurrencyInput Default Capitalization Threshold
23. Klik [Save changes]
24. Klik [Cancel] pada dialog D-01
25. Verifikasi dialog D-01 tertutup
26. Verifikasi tidak ada toast yang tampil
27. Verifikasi CurrencyInput Default Capitalization Threshold masih menampilkan "Rp 10.000.000,00" (belum disimpan)
28. Verifikasi [Save changes] dan [Cancel] form berstatus Enabled
29. Muat ulang halaman dengan F5 dan konfirmasi dialog beforeunload (membuang perubahan yang belum disimpan)

## Notes

- Langkah penghubung (S-03): seed pelepasan, pemulihan Preferences, dan membuang perubahan form dengan F5.
- Asersi tidak ada toast pada TC-201 didahului Verifikasi dialog D-01 tertutup sebagai anchor.
- Temuan untuk QA:
  - Post Condition "Entri log L-02 untuk setting yang berubah ditulis (diuji pada Section 5)" tidak punya langkah observasi di TC ini, sehingga tidak diasersi; pencatatan log diuji pada TC Section 5.
  - Post Condition "Preferences company belum berubah ..." tidak punya langkah observasi di TC ini, sehingga tidak diasersi (S-01).
