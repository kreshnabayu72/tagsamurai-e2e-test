---
id: TC-FA-TDC-E2E-241-activate-dan-deactivate-single-confirm-sukses-loading-dan-toast
title: "Activate dan Deactivate Single: Konfirmasi Sukses, Loading, dan Toast"
layer: ui-e2e
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TDC-362
  - TC-FA-TDC-374
sourceRules: ["ST-28", "§3.4#p1", "§[F-FATDC-04] Activate Tax Depreciation Class#b2", "T-04", "L-04", "§[F-FATDC-05] Deactivate Tax Depreciation Class#b3"]
smoke: []
dependsOn: []
trace:
  "ST-28": [5, 15]
  "§3.4#p1": [7, 17]
  "§[F-FATDC-04] Activate Tax Depreciation Class#b2": [8, 9]
  "T-04": 9
  "L-04": [11, 20]
  "§[F-FATDC-05] Deactivate Tax Depreciation Class#b3": [18, 19]
anchor: [10]
coverage:
  web: automated
---

# Activate dan Deactivate Single: Konfirmasi Sukses, Loading, dan Toast

## Prerequisites

- Mode: FE+BE.
- Akun: Total Control (company uji Fixed Asset). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Akun dan email disediakan tim FE (email tidak tertulis di TC; lihat Temuan untuk QA); password lewat `Spectra.env.FA_TC_PASSWORD`.
- Hook suite, seeding, dan flag Guided Tooltip mengikuti `suite.md`.
- Data Pre-setup (`Fixture.fixedAssetTaxDepreciationClass.exampleData`, disediakan tim FE): sembilan class Example Data PRD (BLD-NP, BLD-P, LAND, NB-1, NB-2, NB-4, NB-KHS, NB-OLD, NB-SL) dengan nilai kolom persis Example Data. Kebutuhan spec ini: NB-OLD berstatus Inactive dengan Used By 0 (target Activate, TC-FA-TDC-362); NB-4 Active dengan Used By 0 (target Deactivate, TC-FA-TDC-374); masih ada class Active lain bertipe Non-building (NB-1, NB-2, NB-SL) sehingga NB-4 lolos guard. Sembilan baris berada dalam satu halaman Pagination (10 baris per halaman), sehingga baris target tidak dicari lewat Search. Class Code dibatasi 15 karakter menurut TC sehingga kode class memakai literal Example Data tanpa suffix `{runId}-<NNN>` (lihat Temuan untuk QA); hook `before` menyeed ulang kondisi awal lewat API dan hook `after` memulihkannya (NB-OLD Inactive, NB-4 Active). Data Dinamis: tidak ada.
- Kemampuan teknis: `Spectra.intercept()` untuk menunda respons request Activate dan request Deactivate selama 2 detik (endpoint ditetapkan tim FE dari sumber modul; tidak dikarang di spec) sehingga state Loading teramati; penundaan dilepas segera sesudah state Loading diasersi (S-09). Seed dan pemulihan class lewat API (disediakan tim FE/BE, lihat `suite.md`).
- State global yang diubah: status NB-OLD dan NB-4 (dipulihkan di hook `after`); intercept jaringan pada sesi browser (dilepas di hook `after` sebagai cadangan).

## Test Steps

### TC-FA-TDC-362: Activate class Inactive lewat toggle Active dan Confirm pada dialog

1. Catat nilai kolom baris NB-OLD (Class Code, Used By, Allowed Methods, Useful Life (years), dan rate) sebelum Activate, serta nilai kolom baris NB-4 sebelum Deactivate
2. Klik toggle `Active` pada baris NB-OLD
3. Aktifkan intercept network: respons request Activate ditahan 2 detik
4. Klik `[Activate]` pada dialog Activate
5. Verifikasi toggle `Active` baris NB-OLD tampil Loading (spinner) dan tidak dapat diklik
6. Tunggu respons selesai
7. Verifikasi dialog menutup
8. Verifikasi toggle `Active` baris NB-OLD menjadi On
9. Verifikasi toast sukses `Success, tax depreciation class has been activated.` tampil di kanan bawah
10. Verifikasi toast hilang otomatis setelah 4 detik
11. Verifikasi kolom lain baris NB-OLD tidak berubah: Class Code NB-OLD, Used By 0, Allowed Methods, Useful Life (years), dan rate sama dengan langkah 1

### TC-FA-TDC-374: Deactivate class lolos guard lewat toggle Active dan Confirm

12. Klik toggle `Active` baris NB-4
13. Aktifkan intercept network: respons request Deactivate ditahan 2 detik
14. Klik `[Deactivate]` pada dialog
15. Verifikasi toggle `Active` baris NB-4 tampil Loading dan tidak dapat diklik
16. Tunggu respons selesai
17. Verifikasi dialog menutup
18. Verifikasi toggle `Active` baris NB-4 menjadi Off
19. Verifikasi toast sukses `Success, tax depreciation class has been deactivated.` tampil
20. Verifikasi kolom lain baris NB-4 tidak berubah: Class Code, Class Name, Used By 0, Allowed Methods, Useful Life (years), dan rate sama dengan langkah 1

## Notes

- Langkah penghubung (S-03): langkah 1 (mencatat nilai kolom sebagai pembanding langkah 11 dan 20, tanpa asersi) dan langkah 3 dan 13 (memasang penundaan respons sebagai kebutuhan TC untuk mengamati Loading; langkah 6 dan 16 menjalankan tunggu respons selesai sesuai TC).
- Penundaan respons hanya untuk mengamati state Loading dan bukan kelas fault injection; spec ini fungsional. Loading diasersi sebelum hasil lain karena state sementara (8b.5).
- Dialog screening, Cancel, Esc, dan backdrop untuk Activate ada di spec 097, untuk Deactivate di spec 098; klik ganda cepat pada konfirmasi ada di spec 104; kegagalan 5xx dan timeout ada di spec 105.
- Temuan untuk QA:
  - Email akun Total Control tidak tertulis di TC; nama env password adalah usulan.
  - TC tidak memiliki tabel Data Uji Pre-setup dan Dinamis terpisah; data ditulis di kolom Precondition tiap TC dan disalin ke Prerequisites.
  - Class Code dibatasi 15 karakter, sehingga suffix `{runId}-<NNN>` tidak dapat dipasang pada kode class (S-12); spec memakai kode literal Example Data dan menyeed ulang lewat hook. Perlu konfirmasi QA.
  - Post Condition TC-FA-TDC-362 dan TC-FA-TDC-374 (status tersimpan, pilihan pada Asset Class di bagian 7 PRD, log L-04 di tiga surface di bagian 5 PRD) tidak punya langkah observasi di luar Expected; tidak diasersi di spec ini (S-01). Pengecekan Asset Class dan log ada di spec sinkronisasi dan pencatatan log.
  - TC-FA-TDC-362 Expected d dan TC-FA-TDC-374 Expected d membandingkan nilai kolom "seperti sebelum" tanpa menyebut nilai pembanding; spec mencatat nilai kolom pada langkah 1.
