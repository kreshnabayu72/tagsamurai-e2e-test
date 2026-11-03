---
id: TC-AC-ACTS-E2E-109-lintas-modul-stock-ledger-device-allocation-add-approve-delete-dan-batch-waiting
title: "Lintas Modul: Saldo Stock Ledger di Device Allocation (Add Stock, Approve, Delete), Batch Seluruhnya Waiting, dan Baris Ledger Pertama"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACTS-685
  - TC-AC-ACTS-686
  - TC-AC-ACTS-687
  - TC-AC-ACTS-725
  - TC-AC-ACTS-726
coverage:
  web: automated
---

# Lintas Modul: Saldo Stock Ledger di Device Allocation (Add Stock, Approve, Delete), Batch Seluruhnya Waiting, dan Baris Ledger Pertama

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net` (Pre-setup #1), password dari `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control).
- Akun ganti di tengah spec: Distributor Toggle ON (Local Registration aktif; jalur approval normal tanpa bypass E2a) `distributorOn_automated_{namaCompany}@qwertysystem.net` (Pre-setup #9), password dari `Spectra.env.AC_DIST_ON_PASSWORD`. Pergantian akun ditulis sebagai langkah eksplisit.
- Halaman awal spec: TAG > Stock (Stock List, dibuka hook `beforeEach` suite).
- Hook suite (flag Guided Tooltip, sesi API aktor, simulator reader, fixture BE, jam server dan jam browser, pemulihan state global) dinyatakan di `suite.md`; spec ini merujuknya dan tidak mengubahnya kecuali yang tertulis di Prerequisites ini.
- Kelas d (harness eksternal) hanya untuk TC-AC-ACTS-725: simulator reader RFID (scan, `[Add by Scan]`, `[Stop]`) disediakan tim FE; mekanismenya tidak dikarang di spec.
- SKU `GPS-TRACK-CORE-G3` (Data Pre-setup #15) dan `RFID-ASSET-CORE-R5` (#12). IMEI Data Dinamis #2 (`356938035643809`, `356938035643811`, `356938035643812`, `356938035643813`, `356938035643814`) bersifat tetap dan tidak dapat bersuffix `{runId}`; seeding idempotent dan pemulihan lewat fixture BE; unit yang didaftarkan spec ini dihapus lewat fixture BE di hook `after`. Subject Register Duplicate pending (TC-AC-ACTS-686), unit Available milik spec ini untuk Delete (TC-AC-ACTS-687), dan dua TAG existing milik entitas lain pada SKU `RFID-ASSET-CORE-R5` (TC-AC-ACTS-725) disiapkan seeding fixture BE. Fixture `fixtures/tag-stock.json` belum ada dan dibuat di tahap script.
- Kemampuan teknis disediakan tim FE/BE: kemampuan membaca saldo Stock Ledger (Device Allocation > Stock Balance Summary Panel) sebagai baseline (S-12), dan kemampuan baca jumlah baris Event Log SKU `RFID-ASSET-CORE-R5` (Tab Add Stock) lewat BE sebagai baseline TC-AC-ACTS-725 (S-12) dan reset baris ledger entitas aktor untuk Category GPS agar TC-AC-ACTS-726 mulai dari entitas tanpa baris ledger (entitas baru dari data pre-setup tidak punya akun di Pre-setup TC; lihat Temuan untuk QA).
- Env var password akun aktor: `Spectra.env.AC_TC_PASSWORD`, `Spectra.env.AC_DIST_ON_PASSWORD`. Password tidak ditulis di spec atau fixture. Nama `AC_DIST_ON_PASSWORD` adalah nama baru yang didaftarkan di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example` oleh pemilik repo e2e.
- Suite berjalan serial (`parallel: false`). Spec ini menyiapkan dan memulihkan datanya sendiri dan tidak bergantung pada hasil spec lain.

## Test Steps

### TC-AC-ACTS-685: Add Stock menambah saldo Stock Ledger yang terlihat di Device Allocation

1. Buka Device Allocation > Stock Balance Summary Panel dan catat saldo entitas registrant untuk Category GPS
2. Buka halaman Add Stock SKU `GPS-TRACK-CORE-G3` dari Stock List lewat row action Add Stock
3. Tambahkan tiga IMEI baru `356938035643809`, `356938035643811`, dan `356938035643812` lewat Manual Entry
4. Klik `[Submit]`
5. Tunggu aksi selesai (Preview kosong dan tombol `[Submit]` aktif kembali)
6. Buka Device Allocation > Stock Balance Summary Panel
7. Verifikasi saldo entitas registrant untuk Category GPS bertambah 3 terhadap baseline

### TC-AC-ACTS-686: Approve Register Duplicate menambah saldo Stock Ledger 1

8. Buka Device Allocation > Stock Balance Summary Panel dan catat saldo entitas requester
9. Buka Approvals > TAG Stock > Tab Active, klik `Review` pada Subject Register Duplicate pending
10. Pilih Approve, klik `[Submit]`
11. Tunggu aksi selesai (dialog Review tertutup)
12. Buka Device Allocation > Stock Balance Summary Panel
13. Verifikasi saldo entitas requester bertambah 1 terhadap baseline

### TC-AC-ACTS-687: Delete unit mengurangi saldo Stock Ledger 1 di Device Allocation

14. Buka Device Allocation > Stock Balance Summary Panel dan catat saldo entitas registrant
15. Buka Detail SKU `RFID-ASSET-CORE-R5` > Tab Available, klik (⋯) > `Delete` pada unit Available milik spec ini
16. Klik `[Delete]` pada dialog `Delete Unit`
17. Tunggu aksi selesai (dialog `Delete Unit` tertutup)
18. Buka Device Allocation > Stock Balance Summary Panel
19. Verifikasi saldo entitas registrant berkurang 1 terhadap baseline

### TC-AC-ACTS-726: Add Stock pertama untuk kombinasi entitas dan Category tanpa baris ledger membuat baris ledger baru tanpa duplikat

20. Reset baris ledger entitas aktor untuk Category GPS (fixture BE) dan catat baseline saldo
21. Buka halaman Add Stock SKU `GPS-TRACK-CORE-G3` dari Stock List lewat row action Add Stock
22. Tambahkan tiga IMEI baru `356938035643813`, `356938035643814`, dan `356938035643815` lewat Manual Entry, klik `[Submit]`
23. Tunggu aksi selesai (Preview kosong dan tombol `[Submit]` aktif kembali)
24. Buka Device Allocation > Stock Balance Summary Panel
25. Verifikasi saldo entitas untuk Category GPS tercatat 3 (selisih +3 terhadap baseline nol)
26. Buka halaman Add Stock SKU `GPS-TRACK-CORE-G3` dari Stock List lewat row action Add Stock
27. Tambahkan dua IMEI baru `356938035643816` dan `356938035643817` lewat Manual Entry, klik `[Submit]`
28. Tunggu aksi selesai (Preview kosong dan tombol `[Submit]` aktif kembali)
29. Buka kembali Device Allocation > Stock Balance Summary Panel
30. Verifikasi saldo entitas untuk Category GPS menjadi 5 (selisih +5 terhadap baseline nol)
31. Verifikasi hanya ada satu entri saldo untuk kombinasi entitas dan Category GPS

### TC-AC-ACTS-725: Batch Add Stock yang seluruhnya Waiting, unit tidak tampil di Tab Available dan saldo Stock Ledger tidak berubah

32. Ganti akun: klik Logout
33. Login sebagai Distributor Toggle ON (`distributorOn_automated_{namaCompany}@qwertysystem.net`)
34. Buka Device Allocation > Stock Balance Summary Panel dan catat saldo entitas Distributor untuk Category RFID
35. Catat baseline jumlah baris Event Log SKU `RFID-ASSET-CORE-R5` (Tab Add Stock) lewat kemampuan baca BE
36. Buka halaman Add Stock SKU `RFID-ASSET-CORE-R5` dari Stock List lewat row action Add Stock
37. Klik `[Add by Scan]`, scan dua TAG yang cocok unit existing milik entitas lain, klik `[Stop]`, klik `[Submit]`
38. Verifikasi toast "Success, 2 TAGs have been sent for approval."
39. Buka Detail SKU `RFID-ASSET-CORE-R5` > Tab Available
40. Verifikasi Tab Available memuat sedikitnya satu baris
41. Verifikasi Tab Available Distributor tidak memuat dua unit Waiting for Approval
42. Buka modal `[Event Log]` (Tab Add Stock)
43. Verifikasi jumlah baris Event Log bertambah 1 dari baseline yang dicatat sebelum `[Submit]`, dengan baris baru (baris teratas urutan default `Date` terbaru) berupa Activity `Add Stock`, Success `0`, dan Waiting for Approval `2` untuk batch ini
44. Tutup modal Event Log
45. Buka Device Allocation > Stock Balance Summary Panel
46. Verifikasi saldo Stock Ledger entitas Distributor untuk Category RFID tidak berubah terhadap baseline

## Notes

- Mode: FE+BE. Spec ini melewati sekitar 35 langkah (46 langkah); alasan: semua blok satu halaman sumber (saldo Stock Ledger di Device Allocation) dan satu dataset, dan tiap blok TC berdiri sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna.
- P-9: TC-AC-ACTS-725 membutuhkan simulator reader RFID (`[Add by Scan]`, scan, `[Stop]`) hanya untuk membentuk state (precondition batch yang seluruhnya Waiting); objek ujinya adalah batch Waiting (Tab Available, Event Log, dan saldo Stock Ledger), bukan perangkat scan. Blok yang tidak membutuhkan hardware (TC-AC-ACTS-685, 686, 687, dan 726) diletakkan lebih dulu dan blok TC-AC-ACTS-725 di akhir spec sehingga kegagalan simulator tidak menutupi blok sebelumnya (S-10); state antar blok dipulihkan lewat langkah penghubung (ganti akun, buka Device Allocation, tutup modal Event Log).
- Langkah penghubung tanpa Verifikasi (S-03): mencatat baseline saldo (S-12), "Tunggu aksi selesai" sesudah aksi tulis yang tidak diasersi sebelum membuka Device Allocation (bagian 8b butir 8), membuka layar baca, dan langkah ganti akun. Absence unit Waiting di Tab Available didahului anchor positif (Tab Available memuat sedikitnya satu baris; 8b butir 2). Langkah "Tutup modal Event Log" menutup modal sebelum pindah surface atau ganti akun (pemulihan state, S-09).
- Temuan untuk QA:
  - TC-AC-ACTS-685 menyebut "Add Stock 3 unit" tanpa TAG Type dan akun; spec memakai Add Stock GPS Manual Entry oleh Total Control (tanpa reader).
  - TC-AC-ACTS-726 mensyaratkan "entitas registrant belum pernah menerima kredit Stock Ledger untuk Category GPS (entitas baru dari data pre-setup)" tanpa akun entitas itu; spec memakai reset baris ledger lewat fixture BE dan menulis ulang nilai absolut 3 dan 5 sebagai selisih terhadap baseline nol.
  - TC-AC-ACTS-725 menyebut "Dua TAG yang akan discan sudah terdaftar sebagai unit existing milik entitas lain" tanpa identifier; disediakan seeding.
