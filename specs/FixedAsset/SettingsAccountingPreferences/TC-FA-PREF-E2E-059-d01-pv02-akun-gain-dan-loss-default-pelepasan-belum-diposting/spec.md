---
id: TC-FA-PREF-E2E-059-d01-pv02-akun-gain-dan-loss-default-pelepasan-belum-diposting
title: "D-01 PV-02: Asset Class Akun Gain dan Loss Default, Pelepasan Belum Diposting"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-PREF-187
  - TC-FA-PREF-188
  - TC-FA-PREF-189
  - TC-FA-PREF-190
coverage:
  web: automated
---

# D-01 PV-02: Asset Class Akun Gain dan Loss Default, Pelepasan Belum Diposting

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup, company `PT Contoh Konstruksi`): `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Accounting > Preferences). Hook `after` mengembalikan sesi ke akun default suite.
- Env var `FA_TC_PASSWORD` belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`: didaftarkan tim FE. Password tidak ditulis di spec atau fixture.
- Data Pre-setup PB-1 (company `PT Contoh Konstruksi`, plan Growth, entitas Active; Preferences nilai awal: Fiscal Year Start January, First Accounting Period Mar 2026, Default Capitalization Threshold 5.000.000, In-service Date Source Activation date, Depreciation in Disposal Month Up to previous month, Default Gain/Loss on Disposal, Default Capitalization Offset dan Found Asset Credit Account kosong, Disposal Documents semua jenis Optional, Journal Grouping Group; periode Mar 2026 sampai Dec 2026 Open; belum ada penyusutan diposting) dan PB-2 (akun Chart of Accounts uji). PB-3 (Asset Class IT Equipment, Vehicles, Furniture). PB-6b (2 pelepasan belum diposting dan menunggu posting; disiapkan lewat seed API karena modul Disposal belum disusun) dan varian PB-4 untuk TC-190.
- Seed dan pemulihan lewat API (Preferences ke nilai awal, Asset Class, pelepasan, akun Chart of Accounts, penguncian) disediakan tim FE/BE (butir "Seed dan pemulihan lewat API" di `suite.md`); tiap TC dijalankan dari keadaan awal yang dinyatakan di Precondition TC-nya.
- Identitas data Pre-setup dibaca dari `fixtures/settings-accounting-preferences.json` (belum ada; disediakan tim FE, nama kunci ditetapkan tim FE). Nama akun dan Asset Class ditulis seperti di TC.
- Flag Guided Tooltip halaman Preferences: hook suite `before` men-set true dan `after` memulihkannya (butir "Flag Guided Tooltip" di `suite.md`).
- Langkah muat ulang saat form dirty: dialog `beforeunload` dikonfirmasi (kemampuan disediakan tim FE; dipakai pada langkah pemulihan).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-PREF-187: PV-02 saat hanya Default Gain on Disposal berubah dengan 2 pelepasan belum diposting

1. Seed 2 pelepasan belum diposting (PB-6b) lewat API
2. Pilih "4-9100 – Laba Pelepasan Aset" pada Select Default Gain on Disposal
3. Klik [Save changes]
4. Verifikasi dialog D-01 berjudul "Save Changes" tampil (severity warning)
5. Verifikasi body dialog memuat daftar bullet: "2 asset classes use the default account. 2 unposted disposals will use the new account."
6. Verifikasi body dialog ditutup pertanyaan "Are you sure you want to save these changes?"
7. Verifikasi footer dialog memuat tombol [Cancel] (variant text, severity contrast) dan [Save]
8. Muat ulang halaman dengan F5 dan konfirmasi dialog beforeunload (membuang perubahan yang belum disimpan)

### TC-FA-PREF-188: PV-02 saat hanya Default Loss on Disposal berubah

9. Pilih "5-9100 – Rugi Pelepasan Aset" pada Select Default Loss on Disposal
10. Klik [Save changes]
11. Verifikasi dialog D-01 berjudul "Save Changes" tampil (severity warning)
12. Verifikasi body dialog memuat daftar bullet: "1 asset class uses the default account. 2 unposted disposals will use the new account."
13. Verifikasi body dialog ditutup pertanyaan "Are you sure you want to save these changes?"
14. Verifikasi footer dialog memuat tombol [Cancel] (variant text, severity contrast) dan [Save]
15. Muat ulang halaman dengan F5 dan konfirmasi dialog beforeunload (membuang perubahan yang belum disimpan)

### TC-FA-PREF-189: PV-02 satu kali dengan tiap Asset Class dihitung sekali saat Gain dan Loss sama-sama berubah

16. Pilih "4-7002 – Gain and Loss on Disposal" pada Select Default Gain on Disposal
17. Pilih "4-7002 – Gain and Loss on Disposal" pada Select Default Loss on Disposal
18. Klik [Save changes]
19. Verifikasi dialog D-01 berjudul "Save Changes" tampil (severity warning)
20. Verifikasi body dialog memuat daftar bullet: "2 asset classes use the default account. 2 unposted disposals will use the new account."
21. Verifikasi body dialog ditutup pertanyaan "Are you sure you want to save these changes?"
22. Verifikasi footer dialog memuat tombol [Cancel] (variant text, severity contrast) dan [Save]
23. Muat ulang halaman dengan F5 dan konfirmasi dialog beforeunload (membuang perubahan yang belum disimpan)

### TC-FA-PREF-190: PV-02 bentuk tunggal dengan 0 pelepasan belum diposting

24. Seed varian PB-4 lewat API (hanya IT Equipment yang mengosongkan akun Gain dan Loss) dan hapus pelepasan belum diposting
25. Pilih "4-9100 – Laba Pelepasan Aset" pada Select Default Gain on Disposal
26. Klik [Save changes]
27. Verifikasi dialog D-01 berjudul "Save Changes" tampil (severity warning)
28. Verifikasi body dialog memuat daftar bullet: "1 asset class uses the default account. 0 unposted disposals will use the new account."
29. Verifikasi body dialog ditutup pertanyaan "Are you sure you want to save these changes?"
30. Verifikasi footer dialog memuat tombol [Cancel] (variant text, severity contrast) dan [Save]
31. Muat ulang halaman dengan F5 dan konfirmasi dialog beforeunload (membuang perubahan yang belum disimpan)
32. Pulihkan Asset Class ke PB-3 lewat seed API

## Notes

- Langkah penghubung (S-03): seed pelepasan dan varian Asset Class, membuang perubahan form dengan F5 setelah tiap TC.
- Temuan untuk QA:
  - Post Condition "Preferences company belum berubah ..." tidak punya langkah observasi di TC ini, sehingga tidak diasersi (S-01).
  - TC-189 Data Uji menulis akun 4-7002 (function Gain on Disposal di PB-2) sebagai pilihan Default Loss; spec mengikuti TC.
