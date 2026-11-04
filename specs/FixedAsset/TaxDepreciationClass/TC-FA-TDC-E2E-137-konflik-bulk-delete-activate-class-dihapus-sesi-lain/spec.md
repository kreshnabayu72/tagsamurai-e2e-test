---
id: TC-FA-TDC-E2E-137-konflik-bulk-delete-activate-class-dihapus-sesi-lain
title: "Konflik Bulk Delete dan Bulk Activate: Sebagian atau Seluruh Class Sudah Dihapus Sesi Lain Saat Confirm"
priority: Medium
caseType: Edge
status: draft
sourceTc:
  - TC-FA-TDC-478
  - TC-FA-TDC-479
  - TC-FA-TDC-480
coverage:
  web: automated
---

# Konflik Bulk Delete dan Bulk Activate: Sebagian atau Seluruh Class Sudah Dihapus Sesi Lain Saat Confirm

## Prerequisites

- Mode: FE+BE.
- Akun aktor sesi A: Total Control (company uji Fixed Asset). Email akun tidak tertulis di Pre-setup TC (lihat Temuan untuk QA) dan disediakan tim FE; password lewat `Spectra.env.FA_TC_PASSWORD`.
- Pelaku kedua (sesi B): sesi API aktor Total Control kedua (akun berbeda; email tidak tertulis di TC dan disediakan tim FE; password lewat `Spectra.env.FA_TC_B_PASSWORD`, nama env baru yang didaftarkan di `executionConfig.environmentVariables` dan `.env.example`). Sesi B hanya memicu penghapusan class dan hasilnya tidak diasersi di sesi itu.
- Login sesi A di hook `before` spec ini; halaman Fixed Asset > Settings > Accounting > Tax Depreciation Class dibuka hook `beforeEach` suite.
- Kemampuan suite yang dipakai (dinyatakan di `suite.md`): seed dan pemulihan lewat API, sesi API aktor, flag Guided Tooltip disetel true oleh hook suite, hook `beforeEach` mengonfirmasi `beforeunload`. Kemampuan tambahan: pembacaan jumlah dan isi entri Changelog class lewat fixture BE (disediakan tim FE/BE).
- Data milik spec (seed idempotent di hook `before` lewat API, dihapus atau dipulihkan di hook `after`; nilai mengacu ke `Fixture.fixedAssetTaxDepreciationClass.<kunci>`, fixture disediakan tim FE):

| Kunci fixture (usulan) | Class Code | Nilai |
|---|---|---|
| `nb3` | `NB-3` | Class Name `Bukan bangunan – Kelompok 3`, Active, Used By 0, tanpa Last Posted Tax Year |
| `nb4` | `NB-4` | Class Name `Bukan bangunan – Kelompok 4`, Active, Used By 0, tanpa Last Posted Tax Year |
| `nbOld` | `NB-OLD` | Inactive, Used By 0 |
| `nbOld2` | `NB-OLD2` | Inactive, Used By 0 |

- Class diseed ulang lewat API di antara blok (langkah 11 dan 24).
- Hasil Search `NB-` memuat `NB-3` dan `NB-4`, dan hasil Search `NB-OLD` memuat `NB-OLD` dan `NB-OLD2`, pada halaman pertama (dataset company khusus automation berisi kurang dari 10 baris dengan awalan itu).
- Suite berjalan serial (`parallel: false`) karena Class Code seed bersifat literal.

## Test Steps

### TC-FA-TDC-478: Matriks 14d, Bulk Delete, sebagian class sudah dihapus sesi lain saat Confirm

1. Ketik Search `NB-`, tekan Enter
2. Catat baseline jumlah entri Changelog Delete class `NB-3` dan `NB-4` lewat fixture BE
3. Sesi A: centang checkbox baris `NB-3`
4. Sesi A: centang checkbox baris `NB-4`
5. Sesi A: klik aksi `Delete` pada Bulk Action Bar (dialog D-06 jamak terbuka, belum Confirm)
6. Sesi B (sesi API): hapus class `NB-3` hingga class terhapus di server
7. Sesi A: klik `[Delete]`
8. Verifikasi baris `NB-4` terhapus tanpa pesan error
9. Verifikasi muncul toast sukses: `Success, tax depreciation class has been deleted.`
10. Verifikasi jumlah entri Changelog Delete bertambah tepat satu untuk `NB-3` (sesi B) dan tepat satu untuk `NB-4` (sesi A) dari baseline langkah 2

### TC-FA-TDC-479: Matriks 14e, Bulk Delete, semua class sudah dihapus sesi lain saat Confirm

11. Pulihkan class `NB-3` dan `NB-4` lewat seeding API ke Active dengan Used By 0 tanpa Last Posted Tax Year
12. Ganti isi kotak search dengan `NB-`, tekan Enter
13. Catat baseline jumlah entri Changelog Delete class `NB-3` dan `NB-4` lewat fixture BE
14. Sesi A: centang checkbox baris `NB-3`
15. Sesi A: centang checkbox baris `NB-4`
16. Sesi A: klik aksi `Delete` pada Bulk Action Bar (dialog D-06 jamak terbuka, belum Confirm)
17. Sesi B (sesi API): hapus class `NB-3` dan `NB-4` hingga keduanya terhapus di server
18. Sesi A: klik `[Delete]`
19. Verifikasi muncul toast netral (severity Info): `This tax depreciation class is no longer available.`
20. Verifikasi tabel sesi A disegarkan dan baris `NB-3` dan `NB-4` tidak ada
21. Verifikasi jumlah entri Changelog Delete bertambah tepat satu untuk `NB-3` dan tepat satu untuk `NB-4`, keduanya dari sesi B, dari baseline langkah 13 (tidak ada entri Delete tambahan dari sesi A)
22. Verifikasi seleksi dikosongkan
23. Verifikasi Bulk Action Bar hilang

### TC-FA-TDC-480: Matriks 14f, Bulk Activate, semua class dihapus sesi lain saat Confirm

24. Pulihkan class `NB-OLD` dan `NB-OLD2` lewat seeding API ke Inactive dengan Used By 0
25. Ganti isi kotak search dengan `NB-OLD`, tekan Enter
26. Sesi A: centang checkbox baris `NB-OLD`
27. Sesi A: centang checkbox baris `NB-OLD2`
28. Sesi A: klik aksi `Activate` pada Bulk Action Bar (dialog D-03 jamak terbuka, belum Confirm)
29. Sesi B (sesi API): hapus class `NB-OLD` dan `NB-OLD2` hingga keduanya terhapus di server
30. Sesi A: klik `[Activate]`
31. Verifikasi muncul toast netral (severity Info): `This tax depreciation class is no longer available.`
32. Verifikasi tabel sesi A disegarkan dan baris `NB-OLD` dan `NB-OLD2` tidak ada
33. Verifikasi seleksi dikosongkan
34. Verifikasi Bulk Action Bar hilang
35. Klik `(←)` pada kotak Search

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/tax-depreciation-class/TestCases/tc-tax-depreciation-class.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): langkah 1, 12, dan 25 (Search agar baris target ada di halaman teramati dan seleksi bersih; R-16, 8b.13), langkah 11 dan 24 (membentuk precondition tiap blok), langkah 35 (mengosongkan Search). Langkah 2 dan 13 mencatat baseline Changelog (S-12, 8b.10).
- Langkah 6, 17, dan 29 (pelaku kedua lewat sesi API aktor) ditulis "... hingga ..." (R-20); sesi A tetap memegang dialog yang terbuka sebelum sesi B bertindak.
- Langkah 10 dan 21 (Expected c, jumlah entri log): ditulis sebagai selisih terhadap baseline (S-12).
- Langkah 20 dan 32 (baris hilang): toast netral langkah 19 dan 31 menjadi anchor positif (8b.2). Langkah 22, 23, 33, dan 34 (keadaan seleksi dan Bulk Action Bar) tidak memerlukan pembanding karena barisnya dibuktikan oleh aksi centang pada langkah 14, 15, 26, dan 27.
- Temuan untuk QA:
  - Email akun Total Control sesi A dan sesi B tidak tertulis di Pre-setup TC (S-11): disediakan tim FE.
  - Class Code `NB-3`, `NB-4`, `NB-OLD`, dan `NB-OLD2` ditulis literal tanpa suffix `{runId}-<NNN>`; kode ini dipakai TC apa adanya dan menjadi target aksi tulis (S-06, S-12). Lampiran A konvensi belum memuat pengecualian untuk modul ini; class diseed dan dipulihkan lewat fixture pada company/state khusus automation.
  - TC-FA-TDC-480 tidak memuat Expected log (berbeda dengan TC-FA-TDC-479); spec tidak mengasersi log pada blok TC-FA-TDC-480 (S-01).
  - TC-FA-TDC-478 dan TC-FA-TDC-479 Expected c menyebut "log"; spec membaca entri Changelog lewat fixture BE karena TC tidak merinci cara membuka modal Changelog untuk asersi jumlah.
  - Kolom Automation TC-FA-TDC-478, TC-FA-TDC-479, dan TC-FA-TDC-480 memuat `Manual Only — (d) dua sesi paralel`; TC tetap masuk spec (konvensi bagian 2).
