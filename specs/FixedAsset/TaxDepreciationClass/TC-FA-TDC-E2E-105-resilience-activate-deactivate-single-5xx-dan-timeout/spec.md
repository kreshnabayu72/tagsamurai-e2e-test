---
id: TC-FA-TDC-E2E-105-resilience-activate-deactivate-single-5xx-dan-timeout
title: "Resilience Activate dan Deactivate Single: Gagal 5xx dan Timeout"
priority: Medium
caseType: Negative
status: draft
sourceTc:
  - TC-FA-TDC-369
  - TC-FA-TDC-370
  - TC-FA-TDC-390
  - TC-FA-TDC-391
coverage:
  web: automated
---

# Resilience Activate dan Deactivate Single: Gagal 5xx dan Timeout

## Prerequisites

- Mode: FE+BE. Respons request Activate dan Deactivate dipaksa gagal lewat `Spectra.intercept()` di atas backend nyata; asersi atas status tersimpan dan entri Changelog memuat state server, sehingga spec bukan `Mode: mock`.
- Akun: Total Control (company uji Fixed Asset). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Akun dan email disediakan tim FE (email tidak tertulis di TC; lihat Temuan untuk QA); password lewat `Spectra.env.FA_TC_PASSWORD`.
- Hook suite, seeding, dan flag Guided Tooltip mengikuti `suite.md`.
- Data Pre-setup (`Fixture.fixedAssetTaxDepreciationClass.exampleData`, disediakan tim FE): sembilan class Example Data PRD (BLD-NP, BLD-P, LAND, NB-1, NB-2, NB-4, NB-KHS, NB-OLD, NB-SL) dengan nilai kolom persis Example Data. Kebutuhan spec ini: NB-OLD berstatus Inactive dengan Used By 0 (target Activate, TC-FA-TDC-369 dan 370); NB-4 Active dengan Used By 0 (target Deactivate, TC-FA-TDC-390 dan 391). Sembilan baris berada dalam satu halaman Pagination (10 baris per halaman), sehingga baris target tidak dicari lewat Search. Semua request gagal, sehingga tidak ada data class yang berubah. Class Code dibatasi 15 karakter menurut TC sehingga kode class memakai literal Example Data tanpa suffix `{runId}-<NNN>` (lihat Temuan untuk QA); hook `before` menyeed ulang kondisi awal lewat API dan hook `after` memulihkannya. Data Dinamis: tidak ada.
- Kemampuan teknis: `Spectra.intercept()` atas request Activate dan request Deactivate (endpoint ditetapkan tim FE dari sumber modul; tidak dikarang di spec) untuk (a) mengembalikan respons 500 satu kali, dan (b) menahan request tanpa respons sampai timeout satu kali; intercept lepas otomatis sesudah satu respons atau timeout (S-09). Kemampuan baca jumlah entri Changelog Status class NB-OLD dan class NB-4 (disediakan tim FE/BE; baseline dicatat sebelum aksi dan dibandingkan sesudahnya, 8b.10, S-12). Seed dan pemulihan class lewat API (disediakan tim FE/BE, lihat `suite.md`).
- State global yang diubah: hanya intercept jaringan pada sesi browser; dilepas di hook `after` sebagai cadangan.

## Test Steps

### TC-FA-TDC-369: Activate gagal 5xx: dialog tetap terbuka dan toggle kembali ke nilai tersimpan

1. Catat baseline jumlah entri Status Changelog class NB-OLD dan class NB-4
2. Aktifkan intercept network: request Activate dijawab 500 satu kali
3. Klik toggle `Active` baris NB-OLD lalu klik `[Activate]` pada dialog
4. Verifikasi toast error `Error, failed to activate tax depreciation class.` tampil di kanan bawah
5. Verifikasi toast error tidak hilang otomatis
6. Verifikasi dialog Activate tetap terbuka
7. Verifikasi tombol `[Activate]` kembali enabled untuk percobaan ulang
8. Verifikasi toggle `Active` baris NB-OLD berada pada nilai tersimpan (Off)
9. Verifikasi jumlah entri Status Changelog NB-OLD sama dengan baseline langkah 1 (tidak ada entri log baru)
10. Tutup toast error
11. Klik `[Cancel]` pada dialog Activate

### TC-FA-TDC-370: Activate timeout: dialog tetap terbuka, toggle di nilai tersimpan, tombol enabled untuk retry

12. Aktifkan intercept network: request Activate ditahan tanpa respons sampai timeout
13. Klik toggle `Active` baris NB-OLD lalu klik `[Activate]` pada dialog
14. Tunggu sampai timeout
15. Verifikasi toast error `Connection problem. Please try again.` tampil di kanan bawah tanpa tombol aksi
16. Verifikasi dialog Activate tetap terbuka
17. Verifikasi tombol `[Activate]` kembali enabled untuk retry manual
18. Verifikasi toggle `Active` baris NB-OLD tetap pada nilai tersimpan (Off)
19. Verifikasi jumlah entri Status Changelog NB-OLD sama dengan baseline langkah 1 (tidak ada entri log baru)
20. Tutup toast error
21. Klik `[Cancel]` pada dialog Activate

### TC-FA-TDC-390: Deactivate gagal 5xx: dialog tetap terbuka dan toggle kembali ke nilai tersimpan

22. Aktifkan intercept network: request Deactivate dijawab 500 satu kali
23. Klik toggle `Active` baris NB-4 lalu klik `[Deactivate]` pada dialog
24. Verifikasi toast error `Error, failed to deactivate tax depreciation class.` tampil di kanan bawah
25. Verifikasi toast error tidak hilang otomatis
26. Verifikasi dialog Deactivate tetap terbuka
27. Verifikasi tombol `[Deactivate]` kembali enabled untuk percobaan ulang
28. Verifikasi toggle `Active` baris NB-4 berada pada nilai tersimpan (On)
29. Verifikasi jumlah entri Status Changelog NB-4 sama dengan baseline langkah 1 (tidak ada entri log baru)
30. Tutup toast error
31. Klik `[Cancel]` pada dialog Deactivate

### TC-FA-TDC-391: Deactivate timeout: dialog tetap terbuka, toggle di nilai tersimpan, tombol enabled untuk retry

32. Aktifkan intercept network: request Deactivate ditahan tanpa respons sampai timeout
33. Klik toggle `Active` baris NB-4 lalu klik `[Deactivate]` pada dialog
34. Tunggu sampai timeout
35. Verifikasi toast error `Connection problem. Please try again.` tampil tanpa tombol aksi
36. Verifikasi dialog Deactivate tetap terbuka
37. Verifikasi tombol `[Deactivate]` kembali enabled
38. Verifikasi toggle `Active` baris NB-4 tetap pada nilai tersimpan (On)
39. Verifikasi jumlah entri Status Changelog NB-4 sama dengan baseline langkah 1 (tidak ada entri log baru)
40. Klik `[Cancel]` pada dialog Deactivate

## Notes

- Spec ini 40 langkah, di atas sekitar 35 langkah. Alasan: seluruh blok satu kelas harness (fault injection pada aksi toggle `Active`) dan berdiri sendiri; tiap blok memuat enam sampai sepuluh asersi yang masing-masing satu klausa (S-01), dan kegagalan satu blok tidak membuat blok lain kehilangan makna. Retry setelah 5xx ada di spec 106; kegagalan bulk ada di spec 107 dan 108.
- Langkah penghubung (S-03): langkah 1 (baseline Changelog dipakai pembanding langkah 9, 19, 29, dan 39 karena semua request gagal dan tidak ada aksi yang mengubah log), langkah 10, 20, dan 30 (menutup toast error persisten agar toast berikutnya tidak tertukar, R-12), serta langkah 11, 21, 31, dan 40 (menutup dialog yang tetap terbuka).
- Intercept memakai pola satu kali dan lepas otomatis sehingga tidak ada intercept yang tertinggal setelah pemicu selesai (S-09); langkah 14 dan 34 menunggu timeout yang disimulasikan intercept, bukan jeda nyata panjang.
- Temuan untuk QA:
  - Email akun Total Control tidak tertulis di TC; nama env password adalah usulan.
  - TC tidak memiliki tabel Data Uji Pre-setup dan Dinamis terpisah; data ditulis di kolom Precondition tiap TC dan disalin ke Prerequisites.
  - Class Code dibatasi 15 karakter, sehingga suffix `{runId}-<NNN>` tidak dapat dipasang pada kode class (S-12); spec memakai kode literal Example Data dan menyeed ulang lewat hook. Perlu konfirmasi QA.
  - TC-FA-TDC-370 dan TC-FA-TDC-391 tidak menyebut durasi timeout dan cara intercept menahan request; spec menuliskannya sebagai kemampuan `Spectra.intercept()` tanpa mengarang endpoint (S-13).
  - TC-FA-TDC-369, 370, 390, dan 391 menyebut "tidak ada entri log baru" tanpa pembanding; spec memakai baseline jumlah entri (langkah 1).
