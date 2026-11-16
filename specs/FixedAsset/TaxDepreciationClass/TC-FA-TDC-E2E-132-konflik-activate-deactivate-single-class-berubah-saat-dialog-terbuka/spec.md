---
id: TC-FA-TDC-E2E-132-konflik-activate-deactivate-single-class-berubah-saat-dialog-terbuka
title: "Konflik Activate dan Deactivate Single: Class Berubah Saat Dialog Konfirmasi Terbuka"
layer: ui-e2e
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-TDC-367
  - TC-FA-TDC-368
  - TC-FA-TDC-387
  - TC-FA-TDC-388
  - TC-FA-TDC-389
sourceRules: ["F-FATDC-04.k1", "T-04", "L-04", "T-13", "F-FATDC-04.k2a", "F-FATDC-04.k2b", "F-FATDC-04.k2c", "D-02", "F-FATDC-05.k3", "FATDC-LOGIC-08h", "F-FATDC-05.k4", "F-FATDC-05.k5a", "F-FATDC-05.k5b", "F-FATDC-05.k5c"]
smoke: []
dependsOn: []
trace:
  "F-FATDC-04.k1": [6, 7]
  "T-04": 8
  "L-04": [9, 27, 36]
  "T-13": [15, 42]
  "F-FATDC-04.k2a": 15
  "F-FATDC-04.k2b": 16
  "F-FATDC-04.k2c": 17
  "D-02": 23
  "F-FATDC-05.k3": 24
  "FATDC-LOGIC-08h": 26
  "F-FATDC-05.k4": [33, 34, 35]
  "F-FATDC-05.k5a": 42
  "F-FATDC-05.k5b": 43
  "F-FATDC-05.k5c": 44
coverage:
  web: automated
---

# Konflik Activate dan Deactivate Single: Class Berubah Saat Dialog Konfirmasi Terbuka

## Prerequisites

- Mode: FE+BE.
- Akun aktor sesi A: Total Control (company uji Fixed Asset). Email akun tidak tertulis di Pre-setup TC (lihat Temuan untuk QA) dan disediakan tim FE; password lewat `Spectra.env.FA_TC_PASSWORD`.
- Pelaku kedua (sesi B): sesi API aktor Total Control kedua (akun berbeda; email tidak tertulis di TC dan disediakan tim FE; password lewat `Spectra.env.FA_TC_B_PASSWORD`, nama env baru yang didaftarkan di `executionConfig.environmentVariables` dan `.env.example`). Sesi B hanya memicu perubahan state (aktifkan, nonaktifkan, hapus class, ubah Tax Depreciation Class sebuah Asset Class di modul Asset Class) dan hasilnya tidak diasersi di sesi itu.
- Login sesi A di hook `before` spec ini; halaman Fixed Asset > Settings > Accounting > Tax Depreciation Class dibuka hook `beforeEach` suite.
- Kemampuan suite yang dipakai (dinyatakan di `suite.md`): seed dan pemulihan lewat API (termasuk Used By lewat Asset Class pemakai), sesi API aktor, flag Guided Tooltip disetel true oleh hook suite, hook `beforeEach` mengonfirmasi `beforeunload`. Kemampuan tambahan: pembacaan jumlah dan isi entri Changelog class lewat fixture BE (disediakan tim FE/BE).
- Data milik spec (seed idempotent di hook `before` lewat API, dihapus atau dipulihkan di hook `after`; nilai mengacu ke `Fixture.fixedAssetTaxDepreciationClass.<kunci>`, fixture disediakan tim FE):

| Kunci fixture (usulan) | Class Code | Nilai |
|---|---|---|
| `nbOld` | `NB-OLD` | Inactive, Used By 0 |
| `nb4` | `NB-4` | Class Name `Bukan bangunan – Kelompok 4`, Active, Used By 0 |
| `assetClassPemakai` | Asset Class milik spec | dipakai sesi B pada TC-FA-TDC-387 untuk mengganti Tax Depreciation Class menjadi `NB-4` (nama Asset Class disediakan tim FE) |

- Class diseed ulang lewat API di antara blok (langkah 10, 28, dan 37) karena tiap blok mengubah, menghapus, atau memakai class.
- Suite berjalan serial (`parallel: false`) karena Class Code seed bersifat literal.

## Test Steps

### TC-FA-TDC-367: Activate class yang sudah Active oleh sesi lain saat Confirm bersifat idempotent

1. Catat baseline jumlah entri Changelog Status class `NB-OLD` lewat fixture BE
2. Ketik Search `NB-OLD`, tekan Enter
3. Sesi A: klik toggle `Active` baris `NB-OLD` (dialog Activate terbuka, belum Confirm)
4. Sesi B (sesi API): aktifkan `NB-OLD` hingga status Active tersimpan
5. Sesi A: klik `[Activate]` pada dialog
6. Verifikasi dialog sesi A menutup
7. Verifikasi tabel sesi A disegarkan dan menampilkan toggle baris `NB-OLD` On
8. Verifikasi muncul toast sukses: `Success, tax depreciation class has been activated.`
9. Verifikasi jumlah entri Changelog Status `NB-OLD` bertambah tepat satu dari baseline langkah 1, yaitu Status Inactive ke Active (dari sesi B)

### TC-FA-TDC-368: Activate class yang sudah dihapus sesi lain saat Confirm menampilkan toast netral

10. Pulihkan class `NB-OLD` lewat seeding API ke Inactive dengan Used By 0
11. Catat baseline jumlah entri Changelog Status class `NB-OLD` lewat fixture BE
12. Sesi A: klik toggle `Active` baris `NB-OLD` (dialog Activate terbuka, belum Confirm)
13. Sesi B (sesi API): hapus class `NB-OLD` hingga class terhapus di server
14. Sesi A: klik `[Activate]` pada dialog
15. Verifikasi muncul toast netral (severity Info): `This tax depreciation class is no longer available.`
16. Verifikasi tabel sesi A disegarkan dan baris `NB-OLD` tidak ada
17. Verifikasi jumlah entri Changelog Status `NB-OLD` sama dengan baseline langkah 11 (tidak ada entri Status baru)

### TC-FA-TDC-387: Class menjadi dipakai Asset Class setelah dialog Deactivate dibuka lalu Confirm

18. Ganti isi kotak search dengan `NB-4`, tekan Enter
19. Catat baseline jumlah entri Changelog Status class `NB-4` lewat fixture BE
20. Sesi A: klik toggle `Active` baris `NB-4` (dialog Deactivate terbuka, belum Confirm)
21. Sesi B (sesi API, modul Asset Class): ubah Tax Depreciation Class sebuah Asset Class menjadi `NB-4` hingga perubahan tersimpan
22. Sesi A: klik `[Deactivate]` pada dialog
23. Verifikasi dialog blok `Cannot Deactivate Tax Depreciation Class` tampil dengan bullet `• NB-4 – Bukan bangunan – Kelompok 4` dan kalimat `Used by 1 asset class. Change it in Asset Class first.`
24. Verifikasi tidak ada toast yang tampil
25. Tekan Esc untuk menutup dialog blok
26. Verifikasi toggle `Active` baris `NB-4` tetap On
27. Verifikasi jumlah entri Changelog Status `NB-4` sama dengan baseline langkah 19 (tidak ada entri log Status baru)

### TC-FA-TDC-388: Deactivate class yang sudah Inactive oleh sesi lain saat Confirm bersifat idempotent

28. Pulihkan class `NB-4` lewat seeding API ke Active dengan Used By 0 (Asset Class pemakai dilepas)
29. Catat baseline jumlah entri Changelog Status class `NB-4` lewat fixture BE
30. Sesi A: klik toggle `Active` baris `NB-4` (dialog Deactivate terbuka, belum Confirm)
31. Sesi B (sesi API): nonaktifkan `NB-4` hingga status Inactive tersimpan
32. Sesi A: klik `[Deactivate]` pada dialog
33. Verifikasi dialog sesi A menutup
34. Verifikasi tabel sesi A disegarkan dan menampilkan toggle `NB-4` Off
35. Verifikasi muncul toast sukses: `Success, tax depreciation class has been deactivated.`
36. Verifikasi jumlah entri Changelog Status `NB-4` bertambah tepat satu dari baseline langkah 29, yaitu Status Active ke Inactive (dari sesi B)

### TC-FA-TDC-389: Deactivate class yang sudah dihapus sesi lain saat Confirm menampilkan toast netral

37. Pulihkan class `NB-4` lewat seeding API ke Active dengan Used By 0
38. Catat baseline jumlah entri Changelog Status class `NB-4` lewat fixture BE
39. Sesi A: klik toggle `Active` baris `NB-4` (dialog Deactivate terbuka, belum Confirm)
40. Sesi B (sesi API): hapus class `NB-4` hingga class terhapus di server
41. Sesi A: klik `[Deactivate]` pada dialog
42. Verifikasi muncul toast netral (severity Info): `This tax depreciation class is no longer available.`
43. Verifikasi tabel sesi A disegarkan dan baris `NB-4` tidak ada
44. Verifikasi jumlah entri Changelog Status `NB-4` sama dengan baseline langkah 38 (tidak ada entri log Status baru)
45. Klik `(←)` pada kotak Search

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/tax-depreciation-class/TestCases/tc-tax-depreciation-class.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): langkah 2 dan 18 (Search agar baris target ada di halaman teramati; R-16, 8b.13; langkah 12 memakai Search langkah 2 yang masih aktif, langkah 30 dan 39 memakai Search langkah 18), langkah 10, 28, dan 37 (membentuk precondition tiap blok), langkah 25 (menutup dialog blok dengan Esc), langkah 45 (mengosongkan Search). Langkah 1, 11, 19, 29, dan 38 mencatat baseline Changelog (S-12, 8b.10).
- Langkah 4, 13, 21, 31, dan 40 (pelaku kedua lewat sesi API aktor) ditulis "... hingga ..." (R-20); sesi A tetap memegang dialog yang terbuka sebelum sesi B bertindak.
- Langkah 9 dan 36 (Expected c, tepat satu entri dari sesi B): ditulis sebagai selisih terhadap baseline (S-12); selisih tepat satu sekaligus menunjukkan bahwa sesi A tidak menambah entri.
- Langkah 16, 17, 24, 27, 43, dan 44 (absence): toast atau dialog hasil server yang sudah diasersi (langkah 15, 23, 42) menjadi anchor positif (8b.2); TC kelas c ini tidak dimuat spec absence, sehingga asersi log ditulis dengan baseline di spec ini (S-05) karena keadaan dua sesi baru dibentuk pada langkah 4, 13, 21, dan 40 (P-1).
- Alasan spec melewati sekitar 35 langkah (45 langkah): semua blok adalah kelas c pada toggle Active satu class, masing-masing berdiri sendiri dengan seed ulang, dan kegagalan satu blok tidak membuat blok lain kehilangan makna; langkah berulang per blok adalah baseline, pemicu sesi B, dan `Verifikasi` per klausa (S-01).
- Temuan untuk QA:
  - Email akun Total Control sesi A dan sesi B tidak tertulis di Pre-setup TC (S-11): disediakan tim FE.
  - Class Code `NB-OLD` dan `NB-4` ditulis literal tanpa suffix `{runId}-<NNN>`; kode ini dipakai TC apa adanya dan menjadi target aksi tulis (S-06, S-12). Lampiran A konvensi belum memuat pengecualian untuk modul ini; class diseed dan dipulihkan lewat fixture pada company/state khusus automation.
  - TC-FA-TDC-387 tidak menyebut tombol penutup dialog blok; spec menutupnya dengan Esc (langkah 25).
  - TC-FA-TDC-367 dan TC-FA-TDC-388 Expected c menyebut "Changelog"; spec membaca entri Changelog lewat fixture BE karena TC tidak merinci cara membuka modal Changelog untuk asersi jumlah.
  - Kolom Automation TC-FA-TDC-367, TC-FA-TDC-368, TC-FA-TDC-387, TC-FA-TDC-388, dan TC-FA-TDC-389 memuat `Manual Only — (d) dua sesi paralel`; TC tetap masuk spec (konvensi bagian 2).
