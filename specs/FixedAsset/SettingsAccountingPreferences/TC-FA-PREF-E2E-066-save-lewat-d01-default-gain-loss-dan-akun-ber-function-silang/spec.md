---
id: TC-FA-PREF-E2E-066-save-lewat-d01-default-gain-loss-dan-akun-ber-function-silang
title: "Save Lewat D-01: Default Gain, Default Loss, Akun Ber-function Silang"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-PREF-210
  - TC-FA-PREF-211
  - TC-FA-PREF-212
coverage:
  web: automated
---

# Save Lewat D-01: Default Gain, Default Loss, Akun Ber-function Silang

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup, company `PT Contoh Konstruksi`): `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Accounting > Preferences). Hook `after` mengembalikan sesi ke akun default suite.
- Env var `FA_TC_PASSWORD` belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`: didaftarkan tim FE. Password tidak ditulis di spec atau fixture.
- Data Pre-setup PB-1 (company `PT Contoh Konstruksi`, plan Growth, entitas Active; Preferences nilai awal: Fiscal Year Start January, First Accounting Period Mar 2026, Default Capitalization Threshold 5.000.000, In-service Date Source Activation date, Depreciation in Disposal Month Up to previous month, Default Gain/Loss on Disposal, Default Capitalization Offset dan Found Asset Credit Account kosong, Disposal Documents semua jenis Optional, Journal Grouping Group; periode Mar 2026 sampai Dec 2026 Open; belum ada penyusutan diposting) dan PB-2 (akun Chart of Accounts uji). PB-3 (Asset Class IT Equipment, Vehicles, Furniture). PB-6b (2 pelepasan belum diposting).
- Seed dan pemulihan lewat API (Preferences ke nilai awal, Asset Class, pelepasan, akun Chart of Accounts, penguncian) disediakan tim FE/BE (butir "Seed dan pemulihan lewat API" di `suite.md`); tiap TC dijalankan dari keadaan awal yang dinyatakan di Precondition TC-nya.
- Identitas data Pre-setup dibaca dari `fixtures/settings-accounting-preferences.json` (belum ada; disediakan tim FE, nama kunci ditetapkan tim FE). Nama akun dan Asset Class ditulis seperti di TC.
- Flag Guided Tooltip halaman Preferences: hook suite `before` men-set true dan `after` memulihkannya (butir "Flag Guided Tooltip" di `suite.md`).
- Data Dinamis DB-1 (nilai Preferences hasil Save) dipulihkan ke PB-1 lewat seed API sebelum TC berikutnya dan di hook `after`.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-PREF-210: Save mengubah Default Gain on Disposal lewat D-01

1. Seed 2 pelepasan belum diposting (PB-6b) lewat API
2. Pilih "4-9100 – Laba Pelepasan Aset" pada Select Default Gain on Disposal
3. Klik [Save changes]
4. Verifikasi body dialog memuat daftar bullet: "2 asset classes use the default account. 2 unposted disposals will use the new account."
5. Klik [Save] pada dialog D-01
6. Verifikasi dialog D-01 tertutup
7. Verifikasi toast "Success, accounting preferences have been saved." tampil di kanan bawah layar
8. Verifikasi Select Default Gain on Disposal menampilkan "4-9100 – Laba Pelepasan Aset"
9. Verifikasi form tetap terbuka dengan nilai tersimpan
10. Verifikasi [Save changes] dan [Cancel] berstatus Disabled (tetap tampil, tidak dapat diklik)
11. Pulihkan Preferences ke nilai awal PB-1 lewat seed API, lalu muat ulang halaman dengan F5

### TC-FA-PREF-211: Save mengubah Default Loss on Disposal ke 5-9100 lewat D-01

12. Pilih "5-9100 – Rugi Pelepasan Aset" pada Select Default Loss on Disposal
13. Klik [Save changes]
14. Verifikasi body dialog memuat daftar bullet: "1 asset class uses the default account. 2 unposted disposals will use the new account."
15. Klik [Save] pada dialog D-01
16. Verifikasi dialog D-01 tertutup
17. Verifikasi toast "Success, accounting preferences have been saved." tampil di kanan bawah layar
18. Verifikasi Select Default Loss on Disposal menampilkan "5-9100 – Rugi Pelepasan Aset"
19. Verifikasi form tetap terbuka dengan nilai tersimpan
20. Verifikasi [Save changes] dan [Cancel] berstatus Disabled (tetap tampil, tidak dapat diklik)
21. Pulihkan Preferences ke nilai awal PB-1 lewat seed API, lalu muat ulang halaman dengan F5

### TC-FA-PREF-212: Save akun ber-function Loss pada Default Gain dan akun ber-function Gain pada Default Loss

22. Pilih "5-9100 – Rugi Pelepasan Aset" (function Loss on Disposal) pada Select Default Gain on Disposal
23. Pilih "4-9100 – Laba Pelepasan Aset" (function Gain on Disposal) pada Select Default Loss on Disposal
24. Klik [Save changes]
25. Klik [Save] pada dialog D-01
26. Verifikasi dialog D-01 tertutup
27. Verifikasi toast "Success, accounting preferences have been saved." tampil di kanan bawah layar
28. Verifikasi Select Default Gain on Disposal menampilkan "5-9100 – Rugi Pelepasan Aset"
29. Verifikasi Select Default Loss on Disposal menampilkan "4-9100 – Laba Pelepasan Aset"
30. Pulihkan Preferences ke nilai awal PB-1 lewat seed API, lalu muat ulang halaman dengan F5

## Notes

- Langkah penghubung (S-03): seed pelepasan dan pemulihan Preferences di akhir tiap TC.
- Temuan untuk QA:
  - Post Condition "Entri log L-02 untuk setting yang berubah ditulis (diuji pada Section 5)" tidak punya langkah observasi di TC ini, sehingga tidak diasersi; pencatatan log diuji pada TC Section 5.
  - TC-210 Post Condition b (pelepasan belum diposting memakai akun baru; diuji pada Section 7) tidak punya langkah observasi di TC ini; tidak diasersi.
  - TC-212 tidak mencantumkan Expected untuk dialog D-01 sebelum [Save]; spec tidak menambahkannya.
