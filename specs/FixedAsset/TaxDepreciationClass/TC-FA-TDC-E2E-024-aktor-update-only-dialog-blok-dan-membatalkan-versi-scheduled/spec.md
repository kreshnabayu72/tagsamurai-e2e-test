---
id: TC-FA-TDC-E2E-024-aktor-update-only-dialog-blok-dan-membatalkan-versi-scheduled
title: "Aktor Update-Only: Dialog Blok Deactivate dan Membatalkan Versi Scheduled"
layer: ui-e2e
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TDC-78
  - TC-FA-TDC-79
  - TC-FA-TDC-80
  - TC-FA-TDC-81
  - TC-FA-TDC-313
sourceRules: ["D-02", "F-FATDC-05.k1", "D-10", "FATDC-LOGIC-04ac", "T-07", "§[F-FATDC-03] Cancel Scheduled Version#b3", "ST-30", "F-FATDC-03.k7", "FATDC-LOGIC-04ad", "FATDC-LOGIC-04aa", "F-FATDC-03.k6", "FATDC-LOGIC-04ae", "§4.1.6#r14"]
smoke: []
dependsOn: []
trace:
  "D-02": 2
  "F-FATDC-05.k1": [4, 5]
  "D-10": [8, 19]
  "FATDC-LOGIC-04ac": 8
  "T-07": [10, 21, 32]
  "§[F-FATDC-03] Cancel Scheduled Version#b3": [11, 22]
  "ST-30": 12
  "F-FATDC-03.k7": [18, 19]
  "FATDC-LOGIC-04ad": [24, 39]
  "FATDC-LOGIC-04aa": [29, 33]
  "F-FATDC-03.k6": 33
  "FATDC-LOGIC-04ae": 38
  "§4.1.6#r14": 39
coverage:
  web: automated
---

# Aktor Update-Only: Dialog Blok Deactivate dan Membatalkan Versi Scheduled

## Prerequisites

- Mode: FE+BE.
- Role yang diuji:

| Role | Akun | Password (env) | Blok langkah |
|---|---|---|---|
| Update-Only (Manage accounting) | disediakan tim FE (tidak ada nomor Pre-setup di TC) | `Spectra.env.FA_UPDATEONLY_PASSWORD` | langkah 1 sampai 42 |

- Login di hook `before` spec ini sebagai Update-Only (Manage accounting); halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control).
- Kemampuan teknis (disediakan tim FE/BE, lihat `suite.md`): seed dan pemulihan data lewat API (class, versi, Used By, tabel tanpa class), akun per role, dan perubahan capability role. Endpoint tidak dikarang (S-13).
- Data Pre-setup dirujuk lewat fixture `fixtures/fixedAssetTaxDepreciationClass.json` (belum ada; disediakan tim FE, nama kunci ditetapkan tim FE): kode dan nilai kolom class Example Data. Nama env password di tabel "Role yang diuji" belum terdaftar di `executionConfig.environmentVariables` dan `.env.example`; penulis script mendaftarkannya.
- Data (kondisi awal): tabel berisi 9 class sesuai Example Data PRD (BLD-NP, BLD-P, LAND, NB-1, NB-2, NB-4, NB-KHS, NB-OLD, NB-SL) dengan nilai kolom persis Example Data; 9 baris berada dalam satu halaman Pagination (10 baris per halaman), sehingga baris target tidak dicari lewat Search. Hook `before` spec ini menyeed ulang kondisi itu lewat API dan hook `after` memulihkannya; Class Code dibatasi 15 karakter sehingga kode class memakai literal TC tanpa suffix `{runId}-<NNN>` (lihat Temuan untuk QA).
- Akun aktor sudah tersedia dan memiliki akses tab (Read) ke Settings > Accounting > Tax Depreciation Class.
- Jam sistem uji: 15 Okt 2026 10:00 WIB (Time Zone entitas Asia/Jakarta, UTC+07:00); Fiscal Year Start Januari. Jam server dan jam browser diatur bersama lewat kendali jam suite (`suite.md`) dan dipulihkan di hook `after`. Jam diatur pada blok TC-FA-TDC-313 (langkah 35) dan dipulihkan di langkah 42 serta hook `after`.
- Kebutuhan data: NB-1 memiliki Used By 5 (TC-FA-TDC-78); BLD-NP memiliki satu versi Scheduled Effective From Jan 2027 yang diseed ulang lewat API sebelum TC-FA-TDC-80 dan dengan dua versi Scheduled (Jan 2027 dan Jan 2028) sebelum TC-FA-TDC-81; class `KHS-C6` memiliki empat versi: Scheduled Jan 2028, Current Jan 2026, Past tanpa Effective From, dan Cancelled Jan 2027 (TC-FA-TDC-313). Dengan KHS-C6 tabel berisi 10 baris, satu halaman Pagination.
- Flag Guided Tooltip halaman ini disetel `seen` oleh hook suite untuk setiap akun aktor (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`) sesuai `suite.md`; spec ini tidak mengubah state global kecuali yang tertulis di bawah.

## Test Steps


### Dialog blok Deactivate class yang dipakai (TC-FA-TDC-78)

1. Klik toggle Active pada baris NB-1 (Used By 5)
2. Verifikasi dialog `Cannot Deactivate Tax Depreciation Class` tampil dengan bullet `NB-1 – Bukan bangunan – Kelompok 1`, teks `Used by 5 asset classes. Change them in Asset Class first.`, tombol `[OK]`
3. Klik `[OK]`
4. Verifikasi tidak ada toast
5. Verifikasi toggle NB-1 tetap On

### Membatalkan versi Scheduled lewat Alert (TC-FA-TDC-79)

6. Klik Class Code BLD-NP
7. Klik `Cancel scheduled version` pada Alert
8. Verifikasi dialog tampil dengan bullet `BLD-NP – Bangunan tidak permanen`, baris `Effective From Jan 2027`, teks `Are you sure you want to cancel this scheduled version?`, tombol `[Back]` dan `[Cancel version]`
9. Klik `[Cancel version]`
10. Verifikasi toast sukses `Success, scheduled version has been cancelled.`
11. Verifikasi Drawer tetap terbuka
12. Verifikasi Alert versi Scheduled hilang
13. Tutup Drawer dengan `[×]`

### Membatalkan versi Scheduled lewat Popup Versions (TC-FA-TDC-80)

14. Seed ulang versi Scheduled Jan 2027 pada BLD-NP lewat API hingga tersimpan, lalu muat ulang halaman
15. Klik Class Code BLD-NP
16. Klik `View versions`
17. Klik `Cancel` pada baris Scheduled
18. Verifikasi Popup Versions menutup
19. Verifikasi dialog pembatalan untuk versi Jan 2027 terbuka
20. Klik `[Cancel version]`
21. Verifikasi toast sukses `Success, scheduled version has been cancelled.`
22. Verifikasi Drawer tetap terbuka
23. Klik `View versions`
24. Verifikasi versi Jan 2027 berstatus `Cancelled`
25. Tutup Popup Versions
26. Tutup Drawer dengan `[×]`

### Membatalkan versi Scheduled paling awal (TC-FA-TDC-81)

27. Seed ulang dua versi Scheduled (Jan 2027 dan Jan 2028) pada BLD-NP lewat API hingga tersimpan, lalu muat ulang halaman
28. Klik Class Code BLD-NP
29. Verifikasi Alert merujuk versi Scheduled paling awal: Effective From Jan 2027
30. Klik `Cancel scheduled version`
31. Klik `[Cancel version]`
32. Verifikasi toast sukses `Success, scheduled version has been cancelled.`
33. Verifikasi Alert kini merujuk versi Scheduled berikutnya: Effective From Jan 2028
34. Tutup Drawer dengan `[×]`

### Tombol Cancel hanya pada baris Scheduled (TC-FA-TDC-313)

35. Atur jam sistem uji ke 15 Okt 2026 10:00 WIB (jam server dan jam browser bersama)
36. Klik Class Code KHS-C6
37. Klik `View versions`
38. Verifikasi baris `Jan 2028` berstatus `Scheduled` memiliki tombol `[Cancel]`
39. Verifikasi baris `Jan 2026` `Current`, baris `—` `Past`, dan baris `Jan 2027` `Cancelled` tidak memiliki tombol apa pun pada kolom Action
40. Tutup Popup Versions
41. Tutup Drawer dengan `[×]`
42. Pulihkan jam sistem uji ke jam semula

## Notes

- Satu aktor (Update-Only) untuk seluruh spec; login di hook `before`, tidak ada ganti akun. Spec melewati sekitar 35 langkah. Alasan: seluruh blok satu aktor dan satu topik (dialog blok dan pembatalan versi Scheduled), berdiri sendiri, dan kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Langkah penghubung (S-03): seed ulang versi Scheduled BLD-NP lewat API sebelum TC-FA-TDC-80 dan TC-FA-TDC-81 (TC-FA-TDC-79 membatalkan versi itu), menutup Drawer dan Popup, serta mengatur dan memulihkan jam (langkah 35 dan 42). Hook `after` menjadi cadangan pemulihan jam dan data (S-09).
- Urutan TC: TC-FA-TDC-313 diletakkan terakhir karena satu-satunya yang membutuhkan jam sistem tertentu.
- Temuan untuk QA:
  - Akun per role tidak punya nomor Pre-setup, email, atau company di TC; Prerequisites menandainya "disediakan tim FE" dan nama env password adalah usulan.
  - TC tidak memiliki tabel Data Uji Pre-setup dan Dinamis; data ditulis di kolom Precondition tiap TC dan disalin ke Prerequisites.
  - Class Code dibatasi 15 karakter (TC-136, 137), sehingga suffix `{runId}-<NNN>` tidak dapat dipasang pada kode class (S-12); spec memakai kode literal Example Data dan menyeed ulang data milik spec di hook `before` serta memulihkannya di hook `after`. Perlu konfirmasi QA.
  - TC-80 menyebut Popup Versions menutup dan dialog pembatalan terbuka sebagai satu butir; spec memecahnya menjadi dua Verifikasi.
  - TC-313 memakai kata "Klik link Class Code ... → Drawer terbuka" dengan jalur; spec memakai langkah klik biasa dan Drawer Edit tidak diasersi terpisah karena bukan butir Expected.
