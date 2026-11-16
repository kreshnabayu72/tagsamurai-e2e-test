---
id: TC-FA-TDC-E2E-232-batas-master-data-count-limit-slot-terakhir-dan-stay-on-form-hingga-batas
title: "Batas Master Data Count Limit: Create pada Slot Terakhir Diizinkan, lalu Ditolak D-07, Termasuk Create Berulang dengan Stay on This Form"
layer: ui-e2e
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-TDC-130
  - TC-FA-TDC-133
sourceRules: ["§4.1#r2", "T-01", "FATDC-LOGIC-13a", "D-07", "F-FATDC-01.k9", "FI-10", "FATDC-LOGIC-13d", "§7.3#b1", "§4.2c#b1"]
smoke: []
dependsOn: []
trace:
  "§4.1#r2": [4, 15]
  "T-01": [6, 19]
  "FATDC-LOGIC-13a": [7, 22]
  "D-07": [9, 25]
  "F-FATDC-01.k9": 10
  "FI-10": [20, 21]
  "FATDC-LOGIC-13d": 27
  "§7.3#b1": [28, 29]
  "§4.2c#b1": 31
coverage:
  web: automated
---

# Batas Master Data Count Limit: Create pada Slot Terakhir Diizinkan, lalu Ditolak D-07, Termasuk Create Berulang dengan Stay on This Form

## Prerequisites

- Mode: FE+BE.
- Aktor: Total Control pada company uji khusus automation. Akun, email, dan company tidak tertulis di TC (lihat Temuan untuk QA); disediakan tim FE. Password lewat `Spectra.env.FA_TC_PASSWORD` (nama env belum terdaftar di `executionConfig.environmentVariables` dan `.env.example`; didaftarkan tim FE).
- Login di hook `before` spec ini sebagai Total Control; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Data uji (kelas e, volume data; kunci di `Fixture.fixedAssetTaxDepreciationClass`, fixture belum ada dan disediakan tim FE): Master Data Count Limit di Admin Console > Plans & Licensing > Lifecycle Settings > System Limits bernilai 1000 (nilai minimum). Total class (semua status) diatur lewat API pre-setup: 999 untuk TC-FA-TDC-130 (7 class seed bawaan ditambah 992 class tambahan) dan 998 untuk TC-FA-TDC-133 (7 class seed bawaan ditambah 991 class tambahan). Class Code `KHS-14`, `KHS-17`, `KHS-18`, dan `KHS-19` belum ada.
- Nilai form valid (nilai field wajib selain Class Code tidak tertulis di TC; lihat Temuan untuk QA): Regulation Reference `UU HPP 7/2021; PMK 72/2023`, Class Name `Kelompok uji {runId}-232`, Asset Type `Non-building`, Useful Life `10`, Allowed Methods `Straight Line`.
- Tabel "Class Create Stay" (parameter langkah 18 sampai 23): `KHS-17` dengan total class 999 sesudah Submit; `KHS-18` dengan total class 1000 sesudah Submit.
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan): mengatur Master Data Count Limit, mengatur total class (menambah atau menghapus class tambahan), dan membaca total class lewat fixture BE.
- State global: Master Data Count Limit dan total class. Hook `after` menghapus `KHS-14`, `KHS-17`, dan `KHS-18` beserta class tambahan dan memulihkan Master Data Count Limit ke nilai awal.
- Rujukan suite: `suite.md` (hook `before`, `beforeEach`, `after`; seed dan pemulihan lewat API).

## Test Steps

### TC-FA-TDC-130: Create pada slot terakhir diizinkan, + Class berikutnya ditolak D-07

1. Atur total class menjadi 999 lewat fixture BE hingga tersimpan
2. Muat ulang halaman dengan F5
3. Klik `+ Class` di toolbar
4. Verifikasi Drawer Add Tax Depreciation Class terbuka
5. Isi form valid dengan Class Code `KHS-14` sesuai Prerequisites, lalu klik `[Submit]`
6. Verifikasi toast sukses "Success, tax depreciation class has been created." tampil
7. Verifikasi total class menjadi 1000
8. Klik `+ Class` lagi
9. Verifikasi dialog D-07 muncul dengan teks "You've reached the platform limit of 1000 records. Contact support if you need a higher limit."
10. Verifikasi Drawer tidak terbuka
11. Klik `[OK]` pada dialog D-07

### TC-FA-TDC-133: Create berulang dengan Stay dicentang hingga batas

12. Atur total class menjadi 998 lewat fixture BE hingga tersimpan
13. Muat ulang halaman dengan F5
14. Klik `+ Class` di toolbar
15. Verifikasi Drawer Add Tax Depreciation Class terbuka
16. Centang checkbox "Stay on this form after submitting"

Untuk setiap baris tabel "Class Create Stay" (langkah 17 sampai 22):

17. Isi form valid dengan Class Code pada baris tersebut sesuai Prerequisites
18. Klik `[Submit]`
19. Verifikasi toast sukses "Success, tax depreciation class has been created." tampil
20. Verifikasi form direset
21. Verifikasi Drawer tetap terbuka
22. Verifikasi total class sesuai kolom total pada baris tersebut

23. Isi form valid Class Code `KHS-19` sesuai Prerequisites
24. Klik `[Submit]`
25. Verifikasi dialog D-07 muncul dengan teks "You've reached the platform limit of 1000 records. Contact support if you need a higher limit."
26. Klik `[OK]` pada dialog D-07
27. Verifikasi class `KHS-19` tidak tersimpan
28. Verifikasi Drawer tetap terbuka
29. Verifikasi input `KHS-19` dipertahankan pada form
30. Tutup Drawer dengan `[×]`
31. Verifikasi dialog `Unsaved Changes` tampil
32. Klik `[Leave]`

## Notes

- Langkah 17 sampai 22 diulang dua kali (`KHS-17`, `KHS-18`); parameter tiap iterasi ada di tabel "Class Create Stay" (8b.7). Ekspansi: 38 langkah.
- Langkah penghubung (S-03): langkah 1, 2, 12, dan 13 membentuk total class 999 dan 998 lewat fixture BE; langkah 11 dan 26 menutup dialog D-07; langkah 30 sampai 32 menutup form Create yang dirty secara deterministik (S-08). Langkah 4 dan 15 adalah `Verifikasi` dari tanda "→ ... terbuka" pada langkah 1 TC (R-02).
- Langkah 27: asersi absence `KHS-19` didahului langkah 25 yang membuktikan penolakan server (dialog D-07) dan dibaca lewat kemampuan baca fixture BE.
- Alasan spec melewati sekitar 35 langkah (38 langkah): seluruh langkah satu kelas harness (e, batas Master Data Count Limit) dan menguji slot terakhir yang sama; TC-FA-TDC-133 adalah satu alur berurutan (item ke N berhasil, item ke N+1 ditolak) yang tidak dapat dipisah tanpa kehilangan makna, dan perulangan Create-nya sudah dijadikan tabel.
- Temuan untuk QA:
  - TC tidak menyebut akun, email, dan company Total Control.
  - TC-FA-TDC-130 dan 133 menulis "isi form valid" tanpa nilai field wajib selain Class Code; spec memakai nilai yang sama dengan TC-FA-TDC-884 (Regulation Reference, Asset Type, Useful Life, Allowed Methods) dan Class Name bersuffix.
  - TC-FA-TDC-133 tidak menyebut cara menutup dialog D-07 sebelum memeriksa Drawer; spec menambah `[OK]` sebagai langkah penghubung.
  - TC-FA-TDC-130 dan 133 menyebut "total class menjadi 1000" tanpa menyebut cara mengamati; spec memakai kemampuan baca fixture BE.
