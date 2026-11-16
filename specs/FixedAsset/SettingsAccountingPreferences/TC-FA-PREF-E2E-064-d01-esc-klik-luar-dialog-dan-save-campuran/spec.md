---
id: TC-FA-PREF-E2E-064-d01-esc-klik-luar-dialog-dan-save-campuran
title: "D-01 Esc, Klik Luar Dialog Tidak Menutup, Save Campuran Lewat D-01"
layer: ui-e2e
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-PREF-199
  - TC-FA-PREF-202
  - TC-FA-PREF-203
sourceRules: ["D-01", "PV-01", "FAPREF-LOGIC-10k", "§4.2b#b1", "F-FAPREF-01.k21b", "T-01", "§3.1#b6", "ST-01", "FAPREF-LOGIC-03e", "§4.5#b1", "§7.2#p1", "F-FAPREF-01.k21c"]
smoke: []
dependsOn: []
trace:
  "D-01": 4
  "PV-01": 4
  "FAPREF-LOGIC-10k": 4
  "§4.2b#b1": 5
  "F-FAPREF-01.k21b": 7
  "T-01": 8
  "§3.1#b6": [9, 12]
  "ST-01": 10
  "FAPREF-LOGIC-03e": 11
  "§4.5#b1": 17
  "§7.2#p1": [18, 25]
  "F-FAPREF-01.k21c": 19
anchor: [24]
coverage:
  web: automated
---

# D-01 Esc, Klik Luar Dialog Tidak Menutup, Save Campuran Lewat D-01

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup, company `PT Contoh Konstruksi`): `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Accounting > Preferences). Hook `after` mengembalikan sesi ke akun default suite.
- Env var `FA_TC_PASSWORD` belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`: didaftarkan tim FE. Password tidak ditulis di spec atau fixture.
- Data Pre-setup PB-1 (company `PT Contoh Konstruksi`, plan Growth, entitas Active; Preferences nilai awal: Fiscal Year Start January, First Accounting Period Mar 2026, Default Capitalization Threshold 5.000.000, In-service Date Source Activation date, Depreciation in Disposal Month Up to previous month, Default Gain/Loss on Disposal, Default Capitalization Offset dan Found Asset Credit Account kosong, Disposal Documents semua jenis Optional, Journal Grouping Group; periode Mar 2026 sampai Dec 2026 Open; belum ada penyusutan diposting) dan PB-2 (akun Chart of Accounts uji). PB-3 (Asset Class IT Equipment, Vehicles, Furniture).
- Seed dan pemulihan lewat API (Preferences ke nilai awal, Asset Class, pelepasan, akun Chart of Accounts, penguncian) disediakan tim FE/BE (butir "Seed dan pemulihan lewat API" di `suite.md`); tiap TC dijalankan dari keadaan awal yang dinyatakan di Precondition TC-nya.
- Identitas data Pre-setup dibaca dari `fixtures/settings-accounting-preferences.json` (belum ada; disediakan tim FE, nama kunci ditetapkan tim FE). Nama akun dan Asset Class ditulis seperti di TC.
- Flag Guided Tooltip halaman Preferences: hook suite `before` men-set true dan `after` memulihkannya (butir "Flag Guided Tooltip" di `suite.md`).
- Langkah muat ulang saat form dirty: dialog `beforeunload` dikonfirmasi (kemampuan disediakan tim FE; dipakai pada langkah pemulihan).
- Data Dinamis DB-1 (nilai Preferences hasil Save) dipulihkan ke PB-1 lewat seed API sebelum TC berikutnya dan di hook `after`.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-PREF-199: Save campuran: D-01 hanya memuat baris dampak untuk setting berdampak

1. Ketik 10000000 pada CurrencyInput Default Capitalization Threshold
2. Ubah Select In-service Date Source menjadi "Manual by Accounting"
3. Klik [Save changes]
4. Verifikasi dialog D-01 berjudul "Save Changes" memuat bullet "2 asset classes use the default threshold." saja
5. Verifikasi tidak ada baris dampak untuk In-service Date Source pada dialog D-01
6. Klik [Save] pada dialog D-01
7. Verifikasi dialog D-01 tertutup
8. Verifikasi toast "Success, accounting preferences have been saved." tampil di kanan bawah layar
9. Verifikasi form tetap terbuka dengan nilai tersimpan
10. Verifikasi [Save changes] dan [Cancel] berstatus Disabled (tetap tampil, tidak dapat diklik)
11. Verifikasi CurrencyInput Default Capitalization Threshold menampilkan "Rp 10.000.000,00"
12. Verifikasi Select In-service Date Source menampilkan "Manual by Accounting"
13. Pulihkan Preferences ke nilai awal PB-1 lewat seed API, lalu muat ulang halaman dengan F5

### TC-FA-PREF-202: Tombol Esc pada D-01 setara [Cancel]

14. Ketik 10000000 pada CurrencyInput Default Capitalization Threshold
15. Klik [Save changes]
16. Tekan tombol Esc pada keyboard
17. Verifikasi dialog D-01 tertutup
18. Verifikasi tidak ada toast yang tampil
19. Verifikasi CurrencyInput Default Capitalization Threshold masih menampilkan "Rp 10.000.000,00" (belum disimpan)
20. Muat ulang halaman dengan F5 dan konfirmasi dialog beforeunload (membuang perubahan yang belum disimpan)

### TC-FA-PREF-203: Klik area di luar dialog D-01 tidak menutup dialog

21. Ketik 10000000 pada CurrencyInput Default Capitalization Threshold
22. Klik [Save changes]
23. Klik area backdrop gelap di luar dialog D-01
24. Verifikasi dialog D-01 berjudul "Save Changes" tetap terbuka
25. Verifikasi tidak ada toast yang tampil
26. Muat ulang halaman dengan F5 dan konfirmasi dialog beforeunload (membuang perubahan yang belum disimpan)

## Notes

- Langkah penghubung (S-03): pemulihan Preferences dan membuang perubahan form dengan F5.
- Asersi tidak ada toast pada TC-202 dan TC-203 didahului Verifikasi anchor (dialog tertutup dan nilai form, atau dialog tetap terbuka).
- Temuan untuk QA:
  - Post Condition "Entri log L-02 untuk setting yang berubah ditulis (diuji pada Section 5)" tidak punya langkah observasi di TC ini, sehingga tidak diasersi; pencatatan log diuji pada TC Section 5.
  - Post Condition "Preferences company belum berubah ..." tidak punya langkah observasi di TC ini, sehingga tidak diasersi (S-01).
