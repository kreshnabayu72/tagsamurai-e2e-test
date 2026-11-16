---
id: TC-FA-TDC-E2E-133-konflik-delete-single-class-berubah-saat-dialog-terbuka
title: "Konflik Delete Single: Class Berubah Saat Dialog Delete Terbuka"
layer: ui-e2e
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-TDC-407
  - TC-FA-TDC-408
  - TC-FA-TDC-409
  - TC-FA-TDC-895
sourceRules: ["D-05", "R-06", "L-05", "D-04", "T-13", "E-FATDC-31", "§[F-FATDC-06] Delete Tax Depreciation Class#b3", "L-04"]
smoke: []
dependsOn: []
trace:
  "D-05": 7
  "R-06": [10, 21]
  "L-05": [11, 22, 31, 41]
  "D-04": 18
  "T-13": [29, 30]
  "E-FATDC-31": 39
  "§[F-FATDC-06] Delete Tax Depreciation Class#b3": 40
  "L-04": 41
anchor: [8, 19]
coverage:
  web: automated
---

# Konflik Delete Single: Class Berubah Saat Dialog Delete Terbuka

## Prerequisites

- Mode: FE+BE.
- Akun aktor sesi A: Total Control (company uji Fixed Asset). Email akun tidak tertulis di Pre-setup TC (lihat Temuan untuk QA) dan disediakan tim FE; password lewat `Spectra.env.FA_TC_PASSWORD`.
- Pelaku kedua (sesi B): sesi API aktor Total Control kedua (akun berbeda; email tidak tertulis di TC dan disediakan tim FE; password lewat `Spectra.env.FA_TC_B_PASSWORD`, nama env baru yang didaftarkan di `executionConfig.environmentVariables` dan `.env.example`) dan fixture BE untuk Last Posted Tax Year (posting penyusutan fiskal belum tersedia di UI). Sesi B hanya memicu perubahan state dan hasilnya tidak diasersi di sesi itu.
- Login sesi A di hook `before` spec ini; halaman Fixed Asset > Settings > Accounting > Tax Depreciation Class dibuka hook `beforeEach` suite.
- Kemampuan suite yang dipakai (dinyatakan di `suite.md`): seed dan pemulihan lewat API (termasuk Used By lewat Asset Class pemakai dan class berkunci), sesi API aktor, flag Guided Tooltip disetel true oleh hook suite, hook `beforeEach` mengonfirmasi `beforeunload`. Kemampuan tambahan: pembacaan jumlah dan isi entri Changelog class lewat fixture BE (disediakan tim FE/BE).
- Data milik spec (seed idempotent di hook `before` lewat API, dihapus atau dipulihkan di hook `after`; nilai mengacu ke `Fixture.fixedAssetTaxDepreciationClass.<kunci>`, fixture disediakan tim FE):

| Kunci fixture (usulan) | Class Code | Nilai |
|---|---|---|
| `nb4` | `NB-4` | Class Name `Bukan bangunan – Kelompok 4`, Active, Used By 0, Last Posted Tax Year kosong |
| `assetClassPemakai` | Asset Class milik spec | dipakai sesi B pada TC-FA-TDC-407 untuk mengganti Tax Depreciation Class menjadi `NB-4` (nama Asset Class disediakan tim FE) |

- `NB-4` diseed ulang lewat API di antara blok (langkah 12, 23, dan 32) karena tiap blok memberi pemakai, mengunci, atau menghapus class.
- Suite berjalan serial (`parallel: false`) karena Class Code seed bersifat literal.

## Test Steps

### TC-FA-TDC-407: Class menjadi dipakai Asset Class setelah dialog Delete dibuka lalu Confirm

1. Ketik Search `NB-4`, tekan Enter
2. Catat baseline jumlah entri Changelog class `NB-4` lewat fixture BE
3. Sesi A: klik tombol ⋯ baris `NB-4`
4. Sesi A: klik `Delete` (dialog Delete terbuka, belum Confirm)
5. Sesi B (sesi API, modul Asset Class): ubah Tax Depreciation Class sebuah Asset Class menjadi `NB-4` hingga perubahan tersimpan
6. Sesi A: klik `[Delete]` pada dialog
7. Verifikasi dialog blok `Cannot Delete Tax Depreciation Class` tampil dengan bullet `• NB-4 – Bukan bangunan – Kelompok 4` dan kalimat `This class is used by 1 asset class.`
8. Verifikasi tidak ada toast tambahan
9. Tekan Esc untuk menutup dialog blok
10. Verifikasi baris `NB-4` tetap ada di tabel
11. Verifikasi jumlah entri Changelog class `NB-4` sama dengan baseline langkah 2 (tidak ada entri log Delete)

### TC-FA-TDC-408: Class menjadi diposting setelah dialog Delete dibuka lalu Confirm

12. Pulihkan class `NB-4` lewat seeding API ke Active dengan Used By 0 dan Last Posted Tax Year kosong
13. Catat baseline jumlah entri Changelog class `NB-4` lewat fixture BE
14. Sesi A: klik tombol ⋯ baris `NB-4`
15. Sesi A: klik `Delete` (dialog Delete terbuka, belum Confirm)
16. Sesi B (fixture BE): isi Last Posted Tax Year `NB-4` dengan `2026` hingga tersimpan
17. Sesi A: klik `[Delete]` pada dialog
18. Verifikasi dialog blok `Cannot Delete Tax Depreciation Class` tampil dengan bullet `• NB-4 – Bukan bangunan – Kelompok 4` dan kalimat `It was used for fiscal depreciation in 2026.`
19. Verifikasi tidak ada toast
20. Tekan Esc untuk menutup dialog blok
21. Verifikasi baris `NB-4` tetap ada di tabel
22. Verifikasi jumlah entri Changelog class `NB-4` sama dengan baseline langkah 13 (tidak ada entri log Delete)

### TC-FA-TDC-409: Delete class yang sudah dihapus sesi lain saat Confirm menampilkan toast netral

23. Pulihkan class `NB-4` lewat seeding API ke Active dengan Used By 0 dan Last Posted Tax Year kosong
24. Catat baseline jumlah entri Changelog class `NB-4` lewat fixture BE
25. Sesi A: klik tombol ⋯ baris `NB-4`
26. Sesi A: klik `Delete` (dialog Delete terbuka, belum Confirm)
27. Sesi B (sesi API): hapus class `NB-4` hingga class terhapus di server
28. Sesi A: klik `[Delete]` pada dialog
29. Verifikasi muncul toast netral (severity Info): `This tax depreciation class is no longer available.`
30. Verifikasi tabel sesi A disegarkan dan baris `NB-4` tidak ada
31. Verifikasi jumlah entri Changelog class `NB-4` bertambah tepat satu dari baseline langkah 24, yaitu entri Delete dari sesi B (tidak ada entri Delete kedua)

### TC-FA-TDC-895: Delete dilanjutkan setelah sesi lain menonaktifkan class yang sama

32. Pulihkan class `NB-4` lewat seeding API ke Active dengan Used By 0 dan Last Posted Tax Year kosong
33. Ganti isi kotak search dengan `NB-4`, tekan Enter
34. Catat baseline jumlah entri Changelog class `NB-4` lewat fixture BE
35. Sesi A: klik tombol ⋯ baris `NB-4`
36. Sesi A: klik `Delete` (dialog Delete terbuka, belum Confirm)
37. Sesi B (sesi API): nonaktifkan `NB-4` lewat toggle Active hingga status Inactive tersimpan
38. Sesi A: klik `[Delete]` pada dialog
39. Verifikasi class `NB-4` terhapus: baris `NB-4` tidak ada di tabel sesi A
40. Verifikasi muncul toast sukses: `Success, tax depreciation class has been deleted.`
41. Verifikasi jumlah entri Changelog class `NB-4` bertambah tepat dua dari baseline langkah 34, yaitu entri Status Active ke Inactive (sesi B) lalu entri Delete (sesi A)
42. Klik `(←)` pada kotak Search

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/tax-depreciation-class/TestCases/tc-tax-depreciation-class.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): langkah 1 dan 33 (Search agar baris target ada di halaman teramati; R-16, 8b.13; langkah 33 memuat ulang hasil Search sesudah class dibuat ulang), langkah 9 dan 20 (menutup dialog blok dengan Esc), langkah 12, 23, dan 32 (membentuk precondition tiap blok), langkah 42 (mengosongkan Search). Langkah 2, 13, 24, dan 34 mencatat baseline Changelog (S-12, 8b.10).
- Langkah 5, 16, 27, dan 37 (pelaku kedua lewat sesi API aktor atau fixture BE) ditulis "... hingga ..." (R-20); sesi A tetap memegang dialog Delete yang terbuka sebelum sesi B bertindak.
- Langkah 8, 10, 11, 19, 21, 22, 30, dan 39 (absence atau perubahan baris): dialog blok langkah 7 dan 18 dan toast langkah 29 dan 40 adalah respons server yang sudah diasersi dan menjadi anchor positif (8b.2). Asersi log ditulis dengan baseline di spec ini (S-05) karena TC kelas c ini tidak dimuat spec absence dan keadaan dua sesi baru dibentuk pada langkah 5, 16, 27, dan 37 (P-1).
- Langkah 31 dan 41 (Expected c): ditulis sebagai selisih terhadap baseline (S-12); langkah 41 menunjukkan dua entri baru dan urutannya mengikuti Expected TC (Status dari sesi B, lalu Delete dari sesi A).
- Alasan spec melewati sekitar 35 langkah (42 langkah): semua blok adalah kelas c pada dialog Delete satu class, masing-masing berdiri sendiri dengan seed ulang, dan kegagalan satu blok tidak membuat blok lain kehilangan makna; Delete yang menghabisi class ada di blok terakhir (S-10).
- Temuan untuk QA:
  - Email akun Total Control sesi A dan sesi B tidak tertulis di Pre-setup TC (S-11): disediakan tim FE.
  - Class Code `NB-4` ditulis literal tanpa suffix `{runId}-<NNN>`; kode ini dipakai TC apa adanya dan menjadi target aksi hapus (S-06, S-12). Lampiran A konvensi belum memuat pengecualian untuk modul ini; class diseed dan dipulihkan lewat fixture pada company/state khusus automation.
  - TC-FA-TDC-407 dan TC-FA-TDC-408 tidak menyebut tombol penutup dialog blok; spec menutupnya dengan Esc (langkah 9 dan 20).
  - TC-FA-TDC-407, TC-FA-TDC-408, TC-FA-TDC-409, dan TC-FA-TDC-895 Expected c menyebut "entri log"/"Changelog"; spec membaca entri Changelog lewat fixture BE karena TC tidak merinci cara membuka modal Changelog untuk asersi jumlah.
  - TC-FA-TDC-409 langkah 2 ("hapus class NB-4 dan Confirm") dan TC-FA-TDC-895 langkah 2 tidak menyebut mekanisme sesi B; spec memakai sesi API aktor.
  - Kolom Automation TC-FA-TDC-407, TC-FA-TDC-408, TC-FA-TDC-409, dan TC-FA-TDC-895 memuat `Manual Only — (d) dua sesi paralel`; TC tetap masuk spec (konvensi bagian 2).
