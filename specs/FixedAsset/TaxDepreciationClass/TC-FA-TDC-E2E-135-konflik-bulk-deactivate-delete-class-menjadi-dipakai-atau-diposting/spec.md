---
id: TC-FA-TDC-E2E-135-konflik-bulk-deactivate-delete-class-menjadi-dipakai-atau-diposting
title: "Konflik Bulk Deactivate dan Bulk Delete: Class Menjadi Dipakai Asset Class Antara Dialog Dibuka dan Konfirmasi"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-TDC-470
  - TC-FA-TDC-471
  - TC-FA-TDC-472
  - TC-FA-TDC-473
coverage:
  web: automated
---

# Konflik Bulk Deactivate dan Bulk Delete: Class Menjadi Dipakai Asset Class Antara Dialog Dibuka dan Konfirmasi

## Prerequisites

- Mode: FE+BE.
- Akun aktor sesi A: Total Control (company uji Fixed Asset). Email akun tidak tertulis di Pre-setup TC (lihat Temuan untuk QA) dan disediakan tim FE; password lewat `Spectra.env.FA_TC_PASSWORD`.
- Pelaku kedua (sesi B): sesi API aktor Total Control kedua (akun berbeda; email tidak tertulis di TC dan disediakan tim FE; password lewat `Spectra.env.FA_TC_B_PASSWORD`, nama env baru yang didaftarkan di `executionConfig.environmentVariables` dan `.env.example`). Sesi B bekerja di modul Asset Class (mengganti Tax Depreciation Class sebuah Asset Class) hanya sebagai pemicu perubahan state; hasilnya tidak diasersi di sesi itu.
- Login sesi A di hook `before` spec ini; halaman Fixed Asset > Settings > Accounting > Tax Depreciation Class dibuka hook `beforeEach` suite.
- Kemampuan suite yang dipakai (dinyatakan di `suite.md`): seed dan pemulihan lewat API (termasuk Used By lewat Asset Class pemakai), sesi API aktor, flag Guided Tooltip disetel true oleh hook suite, hook `beforeEach` mengonfirmasi `beforeunload`. Kemampuan tambahan: pembacaan jumlah dan isi entri Changelog class lewat fixture BE (disediakan tim FE/BE).
- Data milik spec (seed idempotent di hook `before` lewat API, dihapus atau dipulihkan di hook `after`; nilai mengacu ke `Fixture.fixedAssetTaxDepreciationClass.<kunci>`, fixture disediakan tim FE):

| Kunci fixture (usulan) | Class Code | Nilai |
|---|---|---|
| `nb3` | `NB-3` | Class Name `Bukan bangunan – Kelompok 3`, Active, Used By 0, tanpa Last Posted Tax Year |
| `nb4` | `NB-4` | Class Name `Bukan bangunan – Kelompok 4`, Active, Used By 0, tanpa Last Posted Tax Year |
| `assetClassPemakai` | dua Asset Class milik spec | dipakai sesi B untuk mengganti Tax Depreciation Class menjadi `NB-3` dan `NB-4` (nama Asset Class disediakan tim FE) |

- Class diseed ulang lewat API di antara blok (langkah 15, 26, dan 41) dan Asset Class pemakai dilepas lagi.
- Hasil Search `NB-` memuat `NB-3` dan `NB-4` pada halaman pertama (dataset company khusus automation berisi kurang dari 10 baris dengan awalan itu).
- Suite berjalan serial (`parallel: false`) karena Class Code seed bersifat literal.

## Test Steps

### TC-FA-TDC-470: Matriks 13a, Bulk Deactivate, semua class menjadi dipakai antara dialog dibuka dan Confirm

1. Ketik Search `NB-`, tekan Enter
2. Catat baseline jumlah entri Changelog Status class `NB-3` dan `NB-4` lewat fixture BE
3. Sesi A: centang checkbox baris `NB-3`
4. Sesi A: centang checkbox baris `NB-4`
5. Sesi A: klik aksi `Deactivate` pada Bulk Action Bar (dialog D-01 jamak terbuka, belum Confirm)
6. Sesi B (sesi API, modul Asset Class): ubah Tax Depreciation Class dua Asset Class menjadi `NB-3` dan `NB-4` hingga perubahan tersimpan
7. Sesi A: klik `[Deactivate]`
8. Verifikasi dialog blok `Cannot Deactivate Tax Depreciation Classes` tampil dengan `• NB-3 – Bukan bangunan – Kelompok 3 — "used by asset classes"` dan `• NB-4 – Bukan bangunan – Kelompok 4 — "used by asset classes"`
9. Verifikasi tidak ada toast
10. Tekan Esc untuk menutup dialog blok
11. Verifikasi toggle `NB-3` dan `NB-4` tetap On
12. Verifikasi jumlah entri Changelog Status `NB-3` dan `NB-4` sama dengan baseline langkah 2 (tidak ada entri log baru)
13. Verifikasi seleksi dan Bulk Action Bar dipertahankan
14. Klik `Unselect All` pada Bulk Action Bar

### TC-FA-TDC-471: Matriks 13b, Bulk Deactivate, sebagian class menjadi dipakai antara dialog dibuka dan Confirm

15. Pulihkan class `NB-3` dan `NB-4` lewat seeding API ke Active dengan Used By 0 (Asset Class pemakai dilepas)
16. Ganti isi kotak search dengan `NB-`, tekan Enter
17. Catat baseline jumlah entri Changelog Status class `NB-3` dan `NB-4` lewat fixture BE
18. Sesi A: centang checkbox baris `NB-3`
19. Sesi A: centang checkbox baris `NB-4`
20. Sesi A: klik aksi `Deactivate` pada Bulk Action Bar (dialog D-01 jamak terbuka, belum Confirm)
21. Sesi B (sesi API, modul Asset Class): ubah Tax Depreciation Class satu Asset Class menjadi `NB-4` hingga perubahan tersimpan
22. Sesi A: klik `[Deactivate]`
23. Verifikasi toggle `NB-3` menjadi Off dan toggle `NB-4` tetap On
24. Verifikasi muncul toast: `Success, tax depreciation class has been deactivated. Some items were skipped (used by asset classes).`
25. Verifikasi jumlah entri Changelog Status bertambah tepat satu untuk `NB-3` dan tidak bertambah untuk `NB-4` dari baseline langkah 17

### TC-FA-TDC-472: Matriks 13c, Bulk Delete, semua class menjadi dipakai antara dialog dibuka dan Confirm

26. Pulihkan class `NB-3` dan `NB-4` lewat seeding API ke Active dengan Used By 0 (Asset Class pemakai dilepas)
27. Ganti isi kotak search dengan `NB-`, tekan Enter
28. Catat baseline jumlah entri Changelog class `NB-3` dan `NB-4` lewat fixture BE
29. Sesi A: centang checkbox baris `NB-3`
30. Sesi A: centang checkbox baris `NB-4`
31. Sesi A: klik aksi `Delete` pada Bulk Action Bar (dialog D-06 jamak terbuka, belum Confirm)
32. Sesi B (sesi API, modul Asset Class): ubah Tax Depreciation Class dua Asset Class menjadi `NB-3` dan `NB-4` hingga perubahan tersimpan
33. Sesi A: klik `[Delete]`
34. Verifikasi dialog blok `Cannot Delete Tax Depreciation Classes` tampil dengan `• NB-3 – Bukan bangunan – Kelompok 3 — "used by asset classes"` dan `• NB-4 – Bukan bangunan – Kelompok 4 — "used by asset classes"`
35. Verifikasi tidak ada toast
36. Tekan Esc untuk menutup dialog blok
37. Verifikasi baris `NB-3` dan `NB-4` tetap ada di tabel
38. Verifikasi jumlah entri Changelog class `NB-3` dan `NB-4` sama dengan baseline langkah 28 (tidak ada entri log)
39. Verifikasi seleksi dan Bulk Action Bar dipertahankan
40. Klik `Unselect All` pada Bulk Action Bar

### TC-FA-TDC-473: Matriks 13d, Bulk Delete, sebagian class menjadi dipakai antara dialog dibuka dan Confirm

41. Pulihkan class `NB-3` dan `NB-4` lewat seeding API ke Active dengan Used By 0 (Asset Class pemakai dilepas)
42. Ganti isi kotak search dengan `NB-`, tekan Enter
43. Catat baseline jumlah entri Changelog Delete class `NB-3` dan `NB-4` lewat fixture BE
44. Sesi A: centang checkbox baris `NB-3`
45. Sesi A: centang checkbox baris `NB-4`
46. Sesi A: klik aksi `Delete` pada Bulk Action Bar (dialog D-06 jamak terbuka, belum Confirm)
47. Sesi B (sesi API, modul Asset Class): ubah Tax Depreciation Class satu Asset Class menjadi `NB-4` hingga perubahan tersimpan
48. Sesi A: klik `[Delete]`
49. Verifikasi baris `NB-3` terhapus dan baris `NB-4` tetap ada
50. Verifikasi muncul toast: `Success, tax depreciation class has been deleted. Some items were skipped (posted or used by asset classes).`
51. Verifikasi jumlah entri Changelog Delete bertambah tepat satu untuk `NB-3` dan tidak bertambah untuk `NB-4` dari baseline langkah 43

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/tax-depreciation-class/TestCases/tc-tax-depreciation-class.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): langkah 1, 16, 27, dan 42 (Search agar baris target ada di halaman teramati dan seleksi bersih; R-16, 8b.13), langkah 10 dan 36 (menutup dialog blok dengan Esc), langkah 14 dan 40 (Unselect All sebelum blok berikutnya; S-09), langkah 15, 26, dan 41 (membentuk precondition tiap blok). Langkah 2, 17, 28, dan 43 mencatat baseline Changelog (S-12, 8b.10).
- Langkah 6, 21, 32, dan 47 (pelaku kedua lewat sesi API aktor) ditulis "... hingga ..." (R-20); sesi A tetap memegang dialog yang terbuka sebelum sesi B bertindak.
- Langkah 9, 11, 12, 35, 37, dan 38 (absence atau keadaan tidak berubah): dialog blok langkah 8 dan 34 adalah respons server yang sudah diasersi dan menjadi anchor positif (8b.2). Asersi log ditulis dengan baseline di spec ini (S-05) karena TC kelas c ini tidak dimuat spec absence dan keadaan dua sesi baru dibentuk pada langkah 6 dan 32 (P-1). Langkah 25 dan 51 (Expected c, "hanya tercatat untuk NB-3"): ditulis sebagai selisih terhadap baseline (S-12).
- Langkah 13 dan 39 (seleksi dan Bulk Action Bar dipertahankan) diasersi sesudah dialog blok ditutup, karena dialog menutupi Bulk Action Bar selama terbuka.
- Alasan spec melewati sekitar 35 langkah (51 langkah): keempat blok adalah kelas c pada dialog bulk yang sama (Deactivate dan Delete) dengan dua class, masing-masing berdiri sendiri dengan seed ulang, dan kegagalan satu blok tidak membuat blok lain kehilangan makna; langkah berulang per blok adalah baseline, centang, pemicu sesi B, dan `Verifikasi` per klausa (S-01). Tidak ada pecahan ke nomor cadangan karena blok tidak berbagi state.
- Temuan untuk QA:
  - Email akun Total Control sesi A dan sesi B tidak tertulis di Pre-setup TC (S-11): disediakan tim FE.
  - Class Code `NB-3` dan `NB-4` ditulis literal tanpa suffix `{runId}-<NNN>`; kode ini dipakai TC apa adanya dan menjadi target aksi tulis (S-06, S-12). Lampiran A konvensi belum memuat pengecualian untuk modul ini; class diseed dan dipulihkan lewat fixture pada company/state khusus automation.
  - TC-FA-TDC-470 sampai TC-FA-TDC-473 tidak menyebut tombol penutup dialog blok; spec menutupnya dengan Esc (langkah 10 dan 36).
  - TC-FA-TDC-470 sampai TC-FA-TDC-473 Expected c menyebut "log"; spec membaca entri Changelog lewat fixture BE karena TC tidak merinci cara membuka modal Changelog untuk asersi jumlah.
  - TC-FA-TDC-471 dan TC-FA-TDC-473 tidak menyebut Asset Class mana yang dipakai sesi B; fixture menyediakan dua Asset Class dan sesi B memilih satu.
  - TC-FA-TDC-472 Expected c ("Baris NB-3 dan NB-4 tetap ada") diasersi pada langkah 37, sebelum langkah log, sesuai urutan Expected a, b, c TC.
  - Kolom Automation TC-FA-TDC-470, TC-FA-TDC-471, TC-FA-TDC-472, dan TC-FA-TDC-473 memuat `Manual Only — (d) dua sesi paralel`; TC tetap masuk spec (konvensi bagian 2).
