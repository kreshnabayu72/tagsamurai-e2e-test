---
id: TC-FA-PREF-E2E-061-d01-pv03-pelepasan-menunggu-posting
title: "D-01 PV-03: Pelepasan Menunggu Posting (Jamak, Tunggal, Nol)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-PREF-191
  - TC-FA-PREF-192
  - TC-FA-PREF-193
coverage:
  web: automated
---

# D-01 PV-03: Pelepasan Menunggu Posting (Jamak, Tunggal, Nol)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup, company `PT Contoh Konstruksi`): `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Accounting > Preferences). Hook `after` mengembalikan sesi ke akun default suite.
- Env var `FA_TC_PASSWORD` belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`: didaftarkan tim FE. Password tidak ditulis di spec atau fixture.
- Data Pre-setup PB-1 (company `PT Contoh Konstruksi`, plan Growth, entitas Active; Preferences nilai awal: Fiscal Year Start January, First Accounting Period Mar 2026, Default Capitalization Threshold 5.000.000, In-service Date Source Activation date, Depreciation in Disposal Month Up to previous month, Default Gain/Loss on Disposal, Default Capitalization Offset dan Found Asset Credit Account kosong, Disposal Documents semua jenis Optional, Journal Grouping Group; periode Mar 2026 sampai Dec 2026 Open; belum ada penyusutan diposting) dan PB-2 (akun Chart of Accounts uji). PB-6a (1 pelepasan menunggu posting) dan PB-6b (2 pelepasan), disiapkan lewat seed API karena modul Disposal belum disusun.
- Seed dan pemulihan lewat API (Preferences ke nilai awal, Asset Class, pelepasan, akun Chart of Accounts, penguncian) disediakan tim FE/BE (butir "Seed dan pemulihan lewat API" di `suite.md`); tiap TC dijalankan dari keadaan awal yang dinyatakan di Precondition TC-nya.
- Identitas data Pre-setup dibaca dari `fixtures/settings-accounting-preferences.json` (belum ada; disediakan tim FE, nama kunci ditetapkan tim FE). Nama akun dan Asset Class ditulis seperti di TC.
- Flag Guided Tooltip halaman Preferences: hook suite `before` men-set true dan `after` memulihkannya (butir "Flag Guided Tooltip" di `suite.md`).
- Langkah muat ulang saat form dirty: dialog `beforeunload` dikonfirmasi (kemampuan disediakan tim FE; dipakai pada langkah pemulihan).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-PREF-191: PV-03 bentuk jamak dengan 2 pelepasan menunggu posting

1. Seed 2 pelepasan menunggu posting (PB-6b) lewat API
2. Ubah Select Depreciation in Disposal Month dari "Up to previous month" menjadi "Including disposal month"
3. Klik [Save changes]
4. Verifikasi dialog D-01 berjudul "Save Changes" tampil (severity warning)
5. Verifikasi body dialog memuat daftar bullet: "2 disposals waiting posting are affected."
6. Verifikasi body dialog ditutup pertanyaan "Are you sure you want to save these changes?"
7. Verifikasi footer dialog memuat tombol [Cancel] (variant text, severity contrast) dan [Save]
8. Muat ulang halaman dengan F5 dan konfirmasi dialog beforeunload (membuang perubahan yang belum disimpan)

### TC-FA-PREF-192: PV-03 bentuk tunggal dengan 1 pelepasan menunggu posting

9. Seed 1 pelepasan menunggu posting (PB-6a) lewat API
10. Ubah Select Depreciation in Disposal Month dari "Up to previous month" menjadi "Daily prorata"
11. Klik [Save changes]
12. Verifikasi dialog D-01 berjudul "Save Changes" tampil (severity warning)
13. Verifikasi body dialog memuat daftar bullet: "1 disposal waiting posting is affected."
14. Verifikasi body dialog ditutup pertanyaan "Are you sure you want to save these changes?"
15. Verifikasi footer dialog memuat tombol [Cancel] (variant text, severity contrast) dan [Save]
16. Muat ulang halaman dengan F5 dan konfirmasi dialog beforeunload (membuang perubahan yang belum disimpan)

### TC-FA-PREF-193: PV-03 bentuk N dengan hitungan 0

17. Hapus pelepasan menunggu posting lewat seed API (PB-1: tidak ada pelepasan)
18. Ubah Select Depreciation in Disposal Month dari "Up to previous month" menjadi "Including disposal month"
19. Klik [Save changes]
20. Verifikasi dialog D-01 berjudul "Save Changes" tampil (severity warning)
21. Verifikasi body dialog memuat daftar bullet: "0 disposals waiting posting are affected."
22. Verifikasi body dialog ditutup pertanyaan "Are you sure you want to save these changes?"
23. Verifikasi footer dialog memuat tombol [Cancel] (variant text, severity contrast) dan [Save]
24. Muat ulang halaman dengan F5 dan konfirmasi dialog beforeunload (membuang perubahan yang belum disimpan)

## Notes

- Langkah penghubung (S-03): seed pelepasan dan membuang perubahan form dengan F5 setelah tiap TC.
- Temuan untuk QA:
  - Post Condition "Preferences company belum berubah ..." tidak punya langkah observasi di TC ini, sehingga tidak diasersi (S-01).
