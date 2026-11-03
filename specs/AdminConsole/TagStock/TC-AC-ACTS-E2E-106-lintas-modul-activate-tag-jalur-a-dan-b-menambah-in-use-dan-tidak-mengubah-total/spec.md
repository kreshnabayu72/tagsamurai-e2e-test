---
id: TC-AC-ACTS-E2E-106-lintas-modul-activate-tag-jalur-a-dan-b-menambah-in-use-dan-tidak-mengubah-total
title: "Lintas Modul: Activate TAG Jalur A dan B Memindahkan Unit ke Tab In Use, Menaikkan In Use, dan Jalur B Tanpa SKU Tidak Tampil"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACTS-673
  - TC-AC-ACTS-674
  - TC-AC-ACTS-675
  - TC-AC-ACTS-676
coverage:
  web: automated
---

# Lintas Modul: Activate TAG Jalur A dan B Memindahkan Unit ke Tab In Use, Menaikkan In Use, dan Jalur B Tanpa SKU Tidak Tampil

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal `totalControl_automated_{namaCompany}@qwertysystem.net` (Pre-setup #1), password dari `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control).
- Halaman awal spec: TAG > Stock (Stock List, dibuka hook `beforeEach` suite).
- Hook suite (flag Guided Tooltip, sesi API aktor, simulator reader, fixture BE, jam server dan jam browser, pemulihan state global) dinyatakan di `suite.md`; spec ini merujuknya dan tidak mengubahnya kecuali yang tertulis di Prerequisites ini.
- SKU `RFID-ASSET-CORE-R5` (Data Pre-setup #12) dengan sedikitnya dua unit Available milik spec ini (U-A untuk TC-AC-ACTS-673 dan U-B untuk TC-AC-ACTS-674), disiapkan seeding fixture BE (disediakan tim FE/BE). Client memiliki akses Global Settings > TAG; Activate TAG dipicu lewat sesi API aktor (akun Client tidak ada di Pre-setup TC; disediakan tim FE/BE). Tag BYO Jalur B baru dengan SKU (TC-AC-ACTS-675) dan tanpa SKU (TC-AC-ACTS-676) memakai identifier baru yang belum terdaftar. Fixture `fixtures/tag-stock.json` belum ada dan dibuat di tahap script.
- Kemampuan teknis disediakan tim FE/BE: kemampuan baca In Use dan Total Registered SKU sebagai baseline (S-12). Unit yang diaktivasi dan unit Jalur B yang dibuat dipulihkan lewat fixture BE di hook `after`.
- Env var password akun aktor: `Spectra.env.AC_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Suite berjalan serial (`parallel: false`). Spec ini menyiapkan dan memulihkan datanya sendiri dan tidak bergantung pada hasil spec lain.

## Test Steps

### TC-AC-ACTS-673: Activate TAG Jalur A memindahkan unit dari Tab Available ke Tab In Use

1. Buka Detail SKU `RFID-ASSET-CORE-R5` > Tab Available dan catat unit U-A
2. Client mengaktivasi unit U-A lewat Global Settings > TAG > Activate TAG hingga tersimpan (sesi API aktor)
3. Buka Tab Available lalu Tab In Use tanpa memuat ulang halaman
4. Verifikasi Tab Available memuat sedikitnya satu baris unit lain (anchor)
5. Verifikasi unit U-A hilang dari Tab Available
6. Verifikasi unit U-A muncul di Tab In Use dengan Client pemegang dan Activated At
7. Verifikasi Registered At dan Registered By unit U-A tetap

### TC-AC-ACTS-674: Activate TAG menaikkan In Use dan tidak mengubah Total Registered

8. Buka TAG > Stock, catat In Use dan Total Registered SKU `RFID-ASSET-CORE-R5`
9. Client mengaktivasi unit U-B hingga tersimpan (sesi API aktor)
10. Buka TAG > Stock
11. Verifikasi In Use SKU bertambah 1 terhadap baseline
12. Verifikasi Total Registered SKU tidak berubah terhadap baseline

### TC-AC-ACTS-675: Activate TAG Jalur B dengan SKU tanpa collision membuat unit In Use baru

13. Catat In Use dan Total Registered SKU di TAG > Stock
14. Client mengaktivasi tag BYO dengan memilih SKU `RFID-ASSET-CORE-R5` (identifier belum terdaftar) hingga tersimpan (sesi API aktor)
15. Buka Detail SKU `RFID-ASSET-CORE-R5` > Tab In Use
16. Verifikasi unit baru langsung In Use di Tab In Use SKU itu
17. Verifikasi Registered By unit baru `—`
18. Buka TAG > Stock
19. Verifikasi In Use dan Total Registered SKU bertambah 1 terhadap baseline

### TC-AC-ACTS-676: Activate TAG Jalur B tanpa SKU tidak tampil dan tidak dihitung

20. Catat In Use dan Total Registered SKU di TAG > Stock serta jumlah baris Stock List
21. Client mengaktivasi tag BYO tanpa SKU hingga tersimpan (sesi API aktor)
22. Buka TAG > Stock
23. Verifikasi Stock List memuat baris SKU lain (anchor)
24. Verifikasi unit tidak muncul di Stock List
25. Buka Detail SKU `RFID-ASSET-CORE-R5` > Tab In Use
26. Verifikasi Tab In Use memuat sedikitnya satu baris
27. Verifikasi unit tidak muncul di Detail SKU dan Tab In Use
28. Verifikasi In Use dan Total Registered tidak berubah terhadap baseline (tidak dihitung pada metrik)

## Notes

- Mode: FE+BE. Pemicu Client lewat sesi API aktor bukan konteks kedua (P-2 tidak dipakai; keputusan 2026-10-30).
- Langkah penghubung tanpa Verifikasi (S-03): mencatat baseline (S-12) dan membuka layar baca. Pelaku Client ditulis "hingga tersimpan" (R-20).
- Absence unit pada TC-AC-ACTS-673 dan TC-AC-ACTS-676 didahului anchor positif (baris pembanding pada tabel yang sama; 8b butir 2).
- Temuan untuk QA:
  - TC-AC-ACTS-673 sampai TC-AC-ACTS-676 menyebut "Client aktivasi" tanpa akun Client dan mekanisme Activate TAG; spec menuliskannya sebagai pemicu sesi API aktor yang disediakan tim FE/BE.
  - TC-AC-ACTS-676 tidak menyebut jumlah baris awal Stock List; spec memakai baseline jumlah baris.
