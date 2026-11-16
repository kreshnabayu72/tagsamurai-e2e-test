---
id: TC-FA-TDC-E2E-106-resilience-delete-single-5xx-timeout-dan-retry-activate-deactivate
title: "Resilience Delete Single: Gagal 5xx dan Timeout, serta Retry Activate dan Deactivate"
layer: ui-e2e
priority: Medium
caseType: Negative
status: draft
sourceTc:
  - TC-FA-TDC-410
  - TC-FA-TDC-411
  - TC-FA-TDC-899
  - TC-FA-TDC-900
sourceRules: ["R-06", "§7.3#b1", "§9.6#p1", "T-04", "§4.2c#r16", "FATDC-LOGIC-08h", "L-04", "R-05", "§4.2c#r13"]
smoke: []
dependsOn: []
trace:
  "R-06": [4, 8, 18]
  "§7.3#b1": [6, 15, 16]
  "§9.6#p1": [7, 9, 15, 17, 19]
  "T-04": [24, 28]
  "§4.2c#r16": 26
  "FATDC-LOGIC-08h": [27, 38]
  "L-04": [30, 31, 41, 42]
  "R-05": [35, 39]
  "§4.2c#r13": 37
anchor: [5]
coverage:
  web: automated
---

# Resilience Delete Single: Gagal 5xx dan Timeout, serta Retry Activate dan Deactivate

## Prerequisites

- Mode: FE+BE. Respons request Delete, Activate, dan Deactivate dipaksa gagal lewat `Spectra.intercept()` di atas backend nyata; asersi atas baris yang dipertahankan, status tersimpan, dan entri Changelog memuat state server, sehingga spec bukan `Mode: mock`.
- Akun: Total Control (company uji Fixed Asset). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Akun dan email disediakan tim FE (email tidak tertulis di TC; lihat Temuan untuk QA); password lewat `Spectra.env.FA_TC_PASSWORD`.
- Hook suite, seeding, dan flag Guided Tooltip mengikuti `suite.md`.
- Data Pre-setup (`Fixture.fixedAssetTaxDepreciationClass.exampleData`, disediakan tim FE): sembilan class Example Data PRD (BLD-NP, BLD-P, LAND, NB-1, NB-2, NB-4, NB-KHS, NB-OLD, NB-SL) dengan nilai kolom persis Example Data. Kebutuhan spec ini: NB-4 Active dengan Used By 0 dan Last Posted Tax Year kosong (target Delete yang gagal, TC-FA-TDC-410 dan 411, lalu target Deactivate, TC-FA-TDC-900); NB-OLD berstatus Inactive dengan Used By 0 (target Activate, TC-FA-TDC-899). Sembilan baris berada dalam satu halaman Pagination (10 baris per halaman), sehingga baris target tidak dicari lewat Search. Class Code dibatasi 15 karakter menurut TC sehingga kode class memakai literal Example Data tanpa suffix `{runId}-<NNN>` (lihat Temuan untuk QA); hook `before` menyeed ulang kondisi awal lewat API dan hook `after` memulihkannya (NB-OLD Inactive, NB-4 Active). Data Dinamis: tidak ada.
- Kemampuan teknis: `Spectra.intercept()` atas request Delete, Activate, dan Deactivate (endpoint ditetapkan tim FE dari sumber modul; tidak dikarang di spec) untuk (a) mengembalikan respons 500 satu kali, lalu meneruskan request berikutnya ke backend, dan (b) menahan request tanpa respons sampai timeout satu kali; intercept lepas otomatis sesudah satu respons atau timeout (S-09). Kemampuan baca jumlah entri Changelog (Delete NB-4, Status NB-OLD, Status NB-4; disediakan tim FE/BE; baseline dicatat sebelum aksi dan dibandingkan sesudahnya, 8b.10, S-12). Seed dan pemulihan class lewat API (disediakan tim FE/BE, lihat `suite.md`).
- State global yang diubah: intercept jaringan pada sesi browser (dilepas di hook `after` sebagai cadangan); status NB-OLD dan NB-4 (dipulihkan di hook `after`).

## Test Steps

### TC-FA-TDC-410: Delete gagal 5xx: dialog tetap terbuka dan baris dipertahankan

1. Catat baseline jumlah entri Delete Changelog class NB-4, jumlah entri Status Changelog class NB-OLD, dan jumlah entri Status Changelog class NB-4
2. Aktifkan intercept network: request Delete dijawab 500 satu kali
3. Klik tombol `⋯` baris NB-4, `Delete`, lalu `[Delete]` pada dialog
4. Verifikasi toast error `Error, failed to delete tax depreciation class.` tampil
5. Verifikasi toast error tidak hilang otomatis
6. Verifikasi dialog Delete tetap terbuka
7. Verifikasi tombol `[Delete]` kembali enabled untuk percobaan ulang
8. Verifikasi baris NB-4 tetap ada di tabel
9. Verifikasi jumlah entri Delete Changelog NB-4 sama dengan baseline langkah 1 (tidak ada entri log Delete)
10. Tutup toast error
11. Klik `[Cancel]` pada dialog Delete

### TC-FA-TDC-411: Delete timeout: dialog tetap terbuka, baris dipertahankan, tombol enabled untuk retry

12. Aktifkan intercept network: request Delete ditahan tanpa respons sampai timeout
13. Klik tombol `⋯` baris NB-4, `Delete`, lalu `[Delete]` pada dialog
14. Tunggu sampai timeout
15. Verifikasi toast error `Connection problem. Please try again.` tampil tanpa tombol aksi
16. Verifikasi dialog Delete tetap terbuka
17. Verifikasi tombol `[Delete]` kembali enabled
18. Verifikasi baris NB-4 tetap ada di tabel
19. Verifikasi jumlah entri Delete Changelog NB-4 sama dengan baseline langkah 1 (tidak ada entri log Delete)
20. Tutup toast error
21. Klik `[Cancel]` pada dialog Delete

### TC-FA-TDC-899: Retry Activate setelah 5xx berhasil tanpa duplikasi log

22. Aktifkan intercept network: request Activate dijawab 500 satu kali
23. Klik toggle `Active` baris NB-OLD lalu `[Activate]` (gagal)
24. Verifikasi toast error `Error, failed to activate tax depreciation class.` tampil
25. Klik `[Activate]` lagi pada dialog yang tetap terbuka
26. Verifikasi dialog menutup
27. Verifikasi toggle `Active` baris NB-OLD menjadi On
28. Verifikasi toast sukses `Success, tax depreciation class has been activated.` tampil
29. Klik ikon Changelog di toolbar
30. Verifikasi jumlah entri Status Changelog NB-OLD bertambah tepat satu dibanding baseline langkah 1
31. Verifikasi entri baru itu berisi Status Inactive ke Active untuk NB-OLD
32. Tutup modal Changelog

### TC-FA-TDC-900: Retry Deactivate setelah 5xx berhasil tanpa duplikasi log

33. Aktifkan intercept network: request Deactivate dijawab 500 satu kali
34. Klik toggle `Active` baris NB-4 lalu `[Deactivate]` (gagal)
35. Verifikasi toast error `Error, failed to deactivate tax depreciation class.` tampil
36. Klik `[Deactivate]` lagi pada dialog yang tetap terbuka
37. Verifikasi dialog menutup
38. Verifikasi toggle `Active` baris NB-4 menjadi Off
39. Verifikasi toast sukses `Success, tax depreciation class has been deactivated.` tampil
40. Klik ikon Changelog di toolbar
41. Verifikasi jumlah entri Status Changelog NB-4 bertambah tepat satu dibanding baseline langkah 1
42. Verifikasi entri baru itu berisi Status Active ke Inactive untuk NB-4
43. Tutup modal Changelog

## Notes

- Spec ini 43 langkah, di atas sekitar 35 langkah. Alasan: seluruh blok satu kelas harness (fault injection pada aksi tabel, termasuk retry sesudah kegagalan yang dipaksa) dan berdiri sendiri; tiap blok memuat asersi yang masing-masing satu klausa (S-01), dan kegagalan satu blok tidak membuat blok lain kehilangan makna. Kegagalan Activate dan Deactivate single ada di spec 105; kegagalan bulk ada di spec 107 dan 108.
- Urutan TC: 410, 411, 899, 900; blok yang mengubah status (899, 900) setelah blok yang hanya memaksa kegagalan. Tidak ada aksi sukses yang menghapus data.
- Langkah penghubung (S-03): langkah 1 (baseline Changelog yang dipakai pembanding langkah 9, 19, 30, dan 41; kelas entri yang dibandingkan berbeda per kelas dan tidak berubah sebelum aksi yang diasersi), langkah 10 dan 20 (menutup toast error persisten, R-12), langkah 11 dan 21 (menutup dialog yang tetap terbuka), serta langkah 32 dan 43 (menutup modal Changelog).
- Pada TC-FA-TDC-899 dan TC-FA-TDC-900 Expected TC memakai penomoran lokal ("Langkah 2", "Langkah 3"); spec memetakannya ke langkah 24 dan langkah 26 sampai 28 (899) serta langkah 35 dan langkah 37 sampai 39 (900) (R-04).
- Intercept memakai pola satu kali dan lepas otomatis sehingga tidak ada intercept yang tertinggal setelah pemicu selesai (S-09).
- Temuan untuk QA:
  - Email akun Total Control tidak tertulis di TC; nama env password adalah usulan.
  - TC tidak memiliki tabel Data Uji Pre-setup dan Dinamis terpisah; data ditulis di kolom Precondition tiap TC dan disalin ke Prerequisites.
  - Class Code dibatasi 15 karakter, sehingga suffix `{runId}-<NNN>` tidak dapat dipasang pada kode class (S-12); spec memakai kode literal Example Data dan menyeed ulang lewat hook. Perlu konfirmasi QA.
  - TC-FA-TDC-411 tidak menyebut durasi timeout dan cara intercept menahan request; spec menuliskannya sebagai kemampuan `Spectra.intercept()` tanpa mengarang endpoint (S-13).
  - TC-FA-TDC-410 dan 411 menyebut "tidak ada entri log Delete" tanpa pembanding; spec memakai baseline jumlah entri (langkah 1). TC-FA-TDC-899 dan 900 menyebut "tepat satu entri" tanpa pembanding; spec memakai selisih terhadap baseline (S-12).
