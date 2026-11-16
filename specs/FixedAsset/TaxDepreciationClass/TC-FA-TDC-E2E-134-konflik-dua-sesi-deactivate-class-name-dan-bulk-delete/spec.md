---
id: TC-FA-TDC-E2E-134-konflik-dua-sesi-deactivate-class-name-dan-bulk-delete
title: "Konflik Dua Sesi: Deactivate dan Edit Class Name pada Class yang Sama, Bulk Delete Setelah Sesi Lain Menonaktifkan, dan Deactivate Class Terakhir bertipe Land"
layer: ui-e2e
priority: Medium
caseType: Edge
status: draft
sourceTc:
  - TC-FA-TDC-896
  - TC-FA-TDC-897
  - TC-FA-TDC-898
sourceRules: ["R-05", "ST-27", "§[F-FATDC-02] Edit Tax Depreciation Class#b4", "FATDC-LOGIC-04c", "L-04", "F-FATDC-13.k8", "FATDC-LOGIC-14c", "L-05", "§9.5#r9"]
smoke: []
dependsOn: []
trace:
  "R-05": [6, 30]
  "ST-27": [9, 29]
  "§[F-FATDC-02] Edit Tax Depreciation Class#b4": 10
  "FATDC-LOGIC-04c": 11
  "L-04": 12
  "F-FATDC-13.k8": 21
  "FATDC-LOGIC-14c": 22
  "L-05": 23
  "§9.5#r9": 31
coverage:
  web: automated
---

# Konflik Dua Sesi: Deactivate dan Edit Class Name pada Class yang Sama, Bulk Delete Setelah Sesi Lain Menonaktifkan, dan Deactivate Class Terakhir bertipe Land

## Prerequisites

- Mode: FE+BE.
- Akun aktor sesi A: Total Control (company uji Fixed Asset). Email akun tidak tertulis di Pre-setup TC (lihat Temuan untuk QA) dan disediakan tim FE; password lewat `Spectra.env.FA_TC_PASSWORD`.
- Pelaku kedua (sesi B): sesi API aktor Total Control kedua (akun berbeda; email tidak tertulis di TC dan disediakan tim FE; password lewat `Spectra.env.FA_TC_B_PASSWORD`, nama env baru yang didaftarkan di `executionConfig.environmentVariables` dan `.env.example`). Sesi B hanya memicu perubahan state (ubah Class Name, nonaktifkan class, buat class) dan hasilnya tidak diasersi di sesi itu.
- Login sesi A di hook `before` spec ini; halaman Fixed Asset > Settings > Accounting > Tax Depreciation Class dibuka hook `beforeEach` suite.
- Kemampuan suite yang dipakai (dinyatakan di `suite.md`): seed dan pemulihan lewat API, sesi API aktor, flag Guided Tooltip disetel true oleh hook suite, hook `beforeEach` mengonfirmasi `beforeunload`. Kemampuan tambahan: pembacaan jumlah dan isi entri Changelog class lewat fixture BE (disediakan tim FE/BE).
- Data milik spec (seed idempotent di hook `before` lewat API, dihapus atau dipulihkan di hook `after`; nilai mengacu ke `Fixture.fixedAssetTaxDepreciationClass.<kunci>`, fixture disediakan tim FE):

| Kunci fixture (usulan) | Class Code | Nilai |
|---|---|---|
| `nb4` | `NB-4` | Class Name `Bukan bangunan – Kelompok 4`, Active, Used By 0, tanpa Last Posted Tax Year |
| `nb3` | `NB-3` | Class Name `Bukan bangunan – Kelompok 3`, Active, Used By 0, tanpa Last Posted Tax Year |
| `land` | `LAND` | Asset Type Land, Active, Used By 0, satu-satunya class Active bertipe Land |
| `land2` | `LAND2` | Asset Type Land, Regulation Reference `UU HPP 7/2021; PMK 72/2023`, Class Name `Tanah 2`, dibuat sesi B pada TC-FA-TDC-898 |

- Class diseed ulang lewat API di antara blok (langkah 13 dan 24).
- Hasil Search `NB-` memuat `NB-3` dan `NB-4` pada halaman pertama (dataset company khusus automation berisi kurang dari 10 baris dengan awalan itu).
- Suite berjalan serial (`parallel: false`) karena Class Code seed bersifat literal.

## Test Steps

### TC-FA-TDC-896: Deactivate dan perubahan Class Name oleh dua sesi pada class yang sama keduanya berhasil

1. Ketik Search `NB-4`, tekan Enter
2. Catat baseline jumlah entri Changelog Class Name dan Status class `NB-4` lewat fixture BE
3. Sesi A: klik toggle `Active` baris `NB-4`
4. Sesi B (sesi API): ubah Class Name `NB-4` menjadi `Kelompok 4 diubah` hingga perubahan tersimpan
5. Sesi A: klik `[Deactivate]`
6. Verifikasi muncul toast sukses: `Success, tax depreciation class has been deactivated.`
7. Muat ulang tab Tax Depreciation Class di sesi A
8. Ganti isi kotak search dengan `NB-4`, tekan Enter
9. Verifikasi baris `NB-4` menampilkan toggle Off
10. Verifikasi baris `NB-4` menampilkan Class Name `Kelompok 4 diubah`
11. Verifikasi jumlah entri Changelog Class Name `NB-4` bertambah tepat satu dari baseline langkah 2 (dari sesi B)
12. Verifikasi jumlah entri Changelog Status `NB-4` bertambah tepat satu dari baseline langkah 2 (dari sesi A)

### TC-FA-TDC-897: Bulk Delete tetap memproses class yang dinonaktifkan sesi lain sebelum Confirm

13. Pulihkan class `NB-3` dan `NB-4` lewat seeding API ke Active dengan Used By 0 tanpa Last Posted Tax Year
14. Ganti isi kotak search dengan `NB-`, tekan Enter
15. Catat baseline jumlah entri Changelog Delete class `NB-3` dan `NB-4` lewat fixture BE
16. Sesi A: centang checkbox baris `NB-3`
17. Sesi A: centang checkbox baris `NB-4`
18. Sesi A: klik aksi `Delete` pada Bulk Action Bar
19. Sesi B (sesi API): nonaktifkan `NB-3` lewat toggle `Active` hingga status Inactive tersimpan
20. Sesi A: klik `[Delete]`
21. Verifikasi muncul toast sukses: `Success, tax depreciation class has been deleted.`
22. Verifikasi baris `NB-3` dan `NB-4` tidak ada di tabel sesi A
23. Verifikasi jumlah entri Changelog Delete bertambah tepat satu untuk `NB-3` dan tepat satu untuk `NB-4` dari baseline langkah 15

### TC-FA-TDC-898: Deactivate class Active terakhir tetap berhasil walau sesi lain membuat class baru bertipe sama setelah Alert tampil

24. Pulihkan class `LAND` lewat seeding API sebagai satu-satunya class Active bertipe Land dengan Used By 0
25. Ganti isi kotak search dengan `LAND`, tekan Enter
26. Sesi A: klik toggle `Active` baris `LAND`
27. Sesi B (sesi API): buat class `LAND2` bertipe Land (Regulation Reference `UU HPP 7/2021; PMK 72/2023`, Class Name `Tanah 2`) hingga class tersimpan
28. Sesi A: klik `[Deactivate]`
29. Verifikasi toggle `Active` baris `LAND` menjadi Off
30. Verifikasi muncul toast sukses: `Success, tax depreciation class has been deactivated.`
31. Verifikasi class `LAND2` tetap Active: baris `LAND2` menampilkan toggle On
32. Klik `(←)` pada kotak Search

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/tax-depreciation-class/TestCases/tc-tax-depreciation-class.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): langkah 1, 8, 14, dan 25 (Search agar baris target ada di halaman teramati; R-16, 8b.13), langkah 7 (memuat ulang tab sesuai langkah TC; Search, Filter, Sort, dan halaman dipertahankan sesudah F5, sehingga langkah 8 menulis "ganti isi kotak search", 8b.9), langkah 13 dan 24 (membentuk precondition tiap blok), langkah 32 (mengosongkan Search). Langkah 2 dan 15 mencatat baseline Changelog (S-12, 8b.10).
- Langkah 4, 19, dan 27 (pelaku kedua lewat sesi API aktor) ditulis "... hingga ..." (R-20); dialog konfirmasi yang dibuka sesi A pada langkah 3, 18, dan 26 tetap terbuka (belum Confirm) sampai sesi B selesai bertindak.
- Langkah 22 (baris hilang): toast sukses langkah 21 menjadi anchor untuk hilangnya baris sesudah Delete (8b.2); toast diasersi lebih dulu daripada urutan Expected TC. Langkah 31: pembanding `LAND2` ditemukan lewat Search langkah 25 yang menyaring `LAND`.
- Langkah 11, 12, dan 23 (Expected c, jumlah entri Changelog): ditulis sebagai selisih terhadap baseline (S-12).
- Urutan TC: TC-FA-TDC-896, TC-FA-TDC-897, lalu TC-FA-TDC-898; blok yang menghapus class ada di tengah karena TC-FA-TDC-898 memakai class `LAND` terpisah (S-10).
- Temuan untuk QA:
  - Email akun Total Control sesi A dan sesi B tidak tertulis di Pre-setup TC (S-11): disediakan tim FE.
  - Class Code `NB-3`, `NB-4`, `LAND`, dan `LAND2` ditulis literal tanpa suffix `{runId}-<NNN>`; kode ini dipakai TC apa adanya dan menjadi target aksi tulis (S-06, S-12). Lampiran A konvensi belum memuat pengecualian untuk modul ini; class diseed dan dipulihkan lewat fixture pada company/state khusus automation.
  - TC-FA-TDC-896 langkah 2 ("buka Drawer Edit NB-4 ... `[Save]`") dilakukan sesi B tanpa asersi; spec memakai sesi API aktor.
  - TC-FA-TDC-898 menyebut `LAND2` bertipe Land hanya dengan Regulation Reference dan Class Name; nilai field lain (Allowed Methods untuk Land) disediakan fixture.
  - TC-FA-TDC-897 Expected c menyebut "satu entri Delete untuk NB-3 dan satu untuk NB-4"; spec membaca entri Changelog lewat fixture BE karena TC tidak merinci cara membuka modal Changelog.
  - Kolom Automation TC-FA-TDC-896, TC-FA-TDC-897, dan TC-FA-TDC-898 memuat `Manual Only — (d) dua sesi paralel`; TC tetap masuk spec (konvensi bagian 2).
