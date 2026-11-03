---
id: TC-FA-PREF-E2E-060-d01-pv02-bentuk-tunggal-nol-dan-asset-class-inactive
title: "D-01 PV-02 Bentuk Tunggal dan Nol; Asset Class Inactive Tidak Dihitung"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-PREF-611
  - TC-FA-PREF-612
  - TC-FA-PREF-621
coverage:
  web: automated
---

# D-01 PV-02 Bentuk Tunggal dan Nol; Asset Class Inactive Tidak Dihitung

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup, company `PT Contoh Konstruksi`): `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Accounting > Preferences). Hook `after` mengembalikan sesi ke akun default suite.
- Env var `FA_TC_PASSWORD` belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`: didaftarkan tim FE. Password tidak ditulis di spec atau fixture.
- Data Pre-setup PC-1 (Preferences nilai awal), PC-5 (akun Chart of Accounts), PC-6 (Asset Class IT Equipment threshold sendiri 2.000.000 dan akun Gain/Loss kosong; Vehicles tanpa threshold dan akun Gain kosong; Furniture akun terisi), PC-18 (1 pelepasan belum diposting), PC-19 (varian nol: ketiga Asset Class mengisi akun Gain dan Loss), PC-7 (3 pelepasan belum diposting), PC-21 (PC-6 ditambah Asset Class `Legacy Machinery` Inactive).
- Seed dan pemulihan lewat API (Preferences ke nilai awal, Asset Class, pelepasan, akun Chart of Accounts, penguncian) disediakan tim FE/BE (butir "Seed dan pemulihan lewat API" di `suite.md`); tiap TC dijalankan dari keadaan awal yang dinyatakan di Precondition TC-nya.
- Identitas data Pre-setup dibaca dari `fixtures/settings-accounting-preferences.json` (belum ada; disediakan tim FE, nama kunci ditetapkan tim FE). Nama akun dan Asset Class ditulis seperti di TC.
- Flag Guided Tooltip halaman Preferences: hook suite `before` men-set true dan `after` memulihkannya (butir "Flag Guided Tooltip" di `suite.md`).
- Langkah muat ulang saat form dirty: dialog `beforeunload` dikonfirmasi (kemampuan disediakan tim FE; dipakai pada langkah pemulihan).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-PREF-611: PV-02 bentuk tunggal untuk 1 pelepasan belum diposting

1. Seed PC-6 dan 1 pelepasan belum diposting (PC-18) lewat API
2. Pilih "4-9100 – Laba Pelepasan Aset" pada Select Default Gain on Disposal
3. Klik [Save changes]
4. Verifikasi dialog D-01 berjudul "Save Changes" tampil (severity warning)
5. Verifikasi body dialog memuat daftar bullet: "2 asset classes use the default account. 1 unposted disposal will use the new account."
6. Verifikasi body dialog ditutup pertanyaan "Are you sure you want to save these changes?"
7. Verifikasi footer dialog memuat tombol [Cancel] (variant text, severity contrast) dan [Save]
8. Verifikasi kalimat kedua memakai bentuk tunggal "unposted disposal" (bukan bentuk jamak)
9. Muat ulang halaman dengan F5 dan konfirmasi dialog beforeunload (membuang perubahan yang belum disimpan)

### TC-FA-PREF-612: PV-02 untuk 0 Asset Class yang memakai akun default

10. Seed varian PC-19 dan 3 pelepasan belum diposting (PC-7) lewat API
11. Pilih "4-9100 – Laba Pelepasan Aset" pada Select Default Gain on Disposal
12. Klik [Save changes]
13. Verifikasi dialog D-01 berjudul "Save Changes" tampil (severity warning)
14. Verifikasi body dialog memuat daftar bullet: "0 asset classes use the default account. 3 unposted disposals will use the new account."
15. Verifikasi body dialog ditutup pertanyaan "Are you sure you want to save these changes?"
16. Verifikasi footer dialog memuat tombol [Cancel] (variant text, severity contrast) dan [Save]
17. Verifikasi kalimat pertama memakai bentuk jamak dengan angka 0 ("0 asset classes")
18. Muat ulang halaman dengan F5 dan konfirmasi dialog beforeunload (membuang perubahan yang belum disimpan)

### TC-FA-PREF-621: D-01 tidak menghitung Asset Class Inactive pada PV-01 dan PV-02

19. Seed PC-6 ditambah Asset Class `Legacy Machinery` Inactive (PC-21) dan 1 pelepasan belum diposting (PC-18) lewat API
20. Ketik 10000000 pada CurrencyInput Default Capitalization Threshold
21. Pilih "4-9100 – Laba Pelepasan Aset" pada Select Default Gain on Disposal
22. Klik [Save changes]
23. Verifikasi dialog D-01 berjudul "Save Changes" tampil (severity warning)
24. Verifikasi body dialog memuat daftar bullet: "2 asset classes use the default threshold." lalu "2 asset classes use the default account. 1 unposted disposal will use the new account."
25. Verifikasi Asset Class Legacy Machinery (Inactive) tidak ikut terhitung pada kedua bullet
26. Verifikasi body dialog ditutup pertanyaan "Are you sure you want to save these changes?"
27. Verifikasi footer dialog memuat tombol [Cancel] (variant text, severity contrast) dan [Save]
28. Muat ulang halaman dengan F5 dan konfirmasi dialog beforeunload (membuang perubahan yang belum disimpan)
29. Pulihkan Asset Class dan pelepasan ke keadaan awal PC-1 lewat seed API

## Notes

- Langkah penghubung (S-03): seed varian Asset Class dan pelepasan, membuang perubahan form dengan F5 setelah tiap TC.
- Temuan untuk QA:
  - Post Condition "Preferences company belum berubah ..." tidak punya langkah observasi di TC ini, sehingga tidak diasersi (S-01).
  - Seri PC memakai data PC-5 sampai PC-21 yang berbeda dari PB-2 sampai PB-6 untuk TC dengan topik sama (TC-187 sampai 190 di spec 059).
