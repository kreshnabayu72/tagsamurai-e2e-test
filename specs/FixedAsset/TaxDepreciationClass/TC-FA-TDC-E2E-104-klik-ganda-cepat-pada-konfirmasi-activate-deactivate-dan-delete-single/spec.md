---
id: TC-FA-TDC-E2E-104-klik-ganda-cepat-pada-konfirmasi-activate-deactivate-dan-delete-single
title: "Klik Ganda Cepat pada Konfirmasi Activate, Deactivate, dan Delete Single"
priority: Medium
caseType: Edge
status: draft
sourceTc:
  - TC-FA-TDC-371
  - TC-FA-TDC-392
  - TC-FA-TDC-412
coverage:
  web: automated
---

# Klik Ganda Cepat pada Konfirmasi Activate, Deactivate, dan Delete Single

## Prerequisites

- Mode: FE+BE.
- Akun: Total Control (company uji Fixed Asset). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Akun dan email disediakan tim FE (email tidak tertulis di TC; lihat Temuan untuk QA); password lewat `Spectra.env.FA_TC_PASSWORD`.
- Hook suite, seeding, dan flag Guided Tooltip mengikuti `suite.md`.
- Data Pre-setup (`Fixture.fixedAssetTaxDepreciationClass.exampleData`, disediakan tim FE): sembilan class Example Data PRD (BLD-NP, BLD-P, LAND, NB-1, NB-2, NB-4, NB-KHS, NB-OLD, NB-SL) dengan nilai kolom persis Example Data. Kebutuhan spec ini: NB-OLD berstatus Inactive dengan Used By 0 (target Activate); NB-4 Active dengan Used By 0 dan Last Posted Tax Year kosong (target Deactivate lalu Delete). Sembilan baris berada dalam satu halaman Pagination (10 baris per halaman), sehingga baris target tidak dicari lewat Search. Class Code dibatasi 15 karakter menurut TC sehingga kode class memakai literal Example Data tanpa suffix `{runId}-<NNN>` (lihat Temuan untuk QA); hook `before` menyeed ulang kondisi awal lewat API dan hook `after` memulihkannya (NB-OLD Inactive, NB-4 ada dan Active). Data Dinamis: tidak ada.
- Kemampuan teknis (disediakan tim FE/BE, lihat `suite.md`): seed dan pemulihan class lewat API; klik ganda cepat (dua klik berurutan tanpa jeda) pada tombol dialog; pengamatan jumlah request Activate, Deactivate, dan Delete yang terkirim lewat `Spectra.intercept()` (hanya mengamati dan meneruskan request); kemampuan baca jumlah entri Changelog (baseline dicatat sebelum aksi dan dibandingkan sesudahnya, 8b.10, S-12).
- State global yang diubah: intercept pengamat jaringan pada sesi browser (dilepas di hook `after` sebagai cadangan); status NB-OLD dan NB-4 serta penghapusan NB-4 (dipulihkan di hook `after`).

## Test Steps

### TC-FA-TDC-371: Klik ganda cepat pada tombol Activate hanya memproses satu request

1. Catat baseline jumlah entri Status Changelog class NB-OLD dan class NB-4, serta jumlah entri Delete Changelog class NB-4
2. Klik toggle `Active` baris NB-OLD
3. Klik ganda cepat `[Activate]` pada dialog
4. Verifikasi tombol `[Activate]` non-aktif dengan spinner setelah klik pertama
5. Verifikasi hanya satu request Activate yang terkirim
6. Verifikasi satu toast sukses `Success, tax depreciation class has been activated.` tampil
7. Klik ikon Changelog di toolbar
8. Verifikasi jumlah entri Status Changelog NB-OLD bertambah tepat satu dibanding baseline langkah 1
9. Verifikasi entri baru itu berisi Status Inactive ke Active untuk NB-OLD
10. Tutup modal Changelog

### TC-FA-TDC-392: Klik ganda cepat pada tombol Deactivate hanya memproses satu request

11. Klik toggle `Active` baris NB-4
12. Klik ganda cepat `[Deactivate]` pada dialog
13. Verifikasi tombol `[Deactivate]` non-aktif dengan spinner setelah klik pertama
14. Verifikasi hanya satu request Deactivate yang terkirim
15. Verifikasi satu toast sukses `Success, tax depreciation class has been deactivated.` tampil
16. Klik ikon Changelog di toolbar
17. Verifikasi jumlah entri Status Changelog NB-4 bertambah tepat satu dibanding baseline langkah 1
18. Verifikasi entri baru itu berisi Status Active ke Inactive untuk NB-4
19. Tutup modal Changelog

### TC-FA-TDC-412: Klik ganda cepat pada tombol Delete hanya memproses satu request

20. Klik tombol `⋯` baris NB-4 lalu `Delete`
21. Klik ganda cepat `[Delete]` pada dialog
22. Verifikasi tombol `[Delete]` non-aktif dengan spinner setelah klik pertama
23. Verifikasi hanya satu request Delete yang terkirim
24. Verifikasi satu toast sukses `Success, tax depreciation class has been deleted.` tampil
25. Verifikasi toast netral `This tax depreciation class is no longer available.` tidak tampil
26. Klik ikon Changelog di toolbar
27. Verifikasi jumlah entri Delete Changelog NB-4 bertambah tepat satu dibanding baseline langkah 1
28. Tutup modal Changelog

## Notes

- Urutan TC: 371, 392, 412 (aksi yang menghapus data, TC-FA-TDC-412, di akhir). TC-FA-TDC-488 dan TC-FA-TDC-487 (klik ganda cepat pada dialog bulk) ada di spec 242.
- Langkah penghubung (S-03): langkah 1 (baseline Changelog yang dibandingkan pada langkah 8, 17, dan 27; setiap pembanding memakai kelas entri berbeda sehingga satu catatan cukup), serta langkah 10, 19, dan 28 (menutup modal Changelog).
- Spinner pada langkah 4, 13, dan 22 diasersi lebih dulu daripada hasil lain karena state sementara (8b.5). Absence toast netral pada langkah 25 didahului toast sukses langkah 24 sebagai anchor (8b.2, 8b.11).
- Temuan untuk QA:
  - Email akun Total Control tidak tertulis di TC; nama env password adalah usulan.
  - TC tidak memiliki tabel Data Uji Pre-setup dan Dinamis terpisah; data ditulis di kolom Precondition tiap TC dan disalin ke Prerequisites.
  - Class Code dibatasi 15 karakter, sehingga suffix `{runId}-<NNN>` tidak dapat dipasang pada kode class (S-12); spec memakai kode literal Example Data dan menyeed ulang lewat hook. Perlu konfirmasi QA.
  - TC-FA-TDC-371, 392, dan 412 Expected a ("hanya satu request ... terkirim") tidak menyebut cara mengamati jumlah request; spec memakai `Spectra.intercept()` sebagai pengamat tanpa mengarang endpoint (S-13).
  - TC-FA-TDC-412 tidak menyebut status NB-4 saat dihapus; setelah TC-FA-TDC-392 NB-4 berstatus Inactive. Penghapusan class Inactive diizinkan (TC-FA-TDC-395), sehingga alur ini dipertahankan.
