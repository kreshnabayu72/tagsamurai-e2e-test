---
id: TC-FA-TDC-E2E-098-deactivate-single-screening-cancel-esc-dan-backdrop
title: "Deactivate Single: Screening Dialog, Cancel, Esc, dan Backdrop"
layer: ui-e2e
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TDC-373
  - TC-FA-TDC-375
  - TC-FA-TDC-376
  - TC-FA-TDC-377
sourceRules: ["FATDC-LOGIC-08h", "D-01", "L-04", "§4.5#b1"]
smoke: []
dependsOn: []
trace:
  "FATDC-LOGIC-08h": [3, 8, 14, 20, 23]
  "D-01": [4, 5]
  "L-04": [10, 16, 24]
  "§4.5#b1": [13, 23]
anchor: [7, 9, 15, 19, 21]
coverage:
  web: automated
---

# Deactivate Single: Screening Dialog, Cancel, Esc, dan Backdrop

## Prerequisites

- Mode: FE+BE.
- Akun: Total Control (company uji Fixed Asset). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Akun dan email disediakan tim FE (email tidak tertulis di TC; lihat Temuan untuk QA); password lewat `Spectra.env.FA_TC_PASSWORD`.
- Hook suite, seeding, dan flag Guided Tooltip mengikuti `suite.md`.
- Data Pre-setup (`Fixture.fixedAssetTaxDepreciationClass.exampleData`, disediakan tim FE): sembilan class Example Data PRD (BLD-NP, BLD-P, LAND, NB-1, NB-2, NB-4, NB-KHS, NB-OLD, NB-SL) dengan nilai kolom persis Example Data. Kebutuhan spec ini: NB-4 (nama "Bukan bangunan – Kelompok 4") Active dengan Used By 0; masih ada class Active lain bertipe Non-building (NB-1, NB-2, NB-SL), sehingga dialog Deactivate NB-4 tidak memuat Alert peringatan dan class Active terakhir per Asset Type tidak dihabiskan. Sembilan baris berada dalam satu halaman Pagination (10 baris per halaman), sehingga baris target tidak dicari lewat Search. Semua blok hanya membuka lalu membatalkan dialog; tidak ada data class yang berubah. Class Code dibatasi 15 karakter menurut TC sehingga kode class memakai literal Example Data tanpa suffix `{runId}-<NNN>` (lihat Temuan untuk QA); hook `before` menyeed ulang kondisi awal lewat API dan hook `after` memulihkannya. Data Dinamis: tidak ada.
- Kemampuan teknis (disediakan tim FE/BE, lihat `suite.md`): seed dan pemulihan class lewat API; kemampuan baca jumlah entri Changelog class NB-4 untuk field Status (baseline dicatat sebelum aksi dan dibandingkan sesudahnya, 8b.10, S-12); menekan `Esc` dan mengklik backdrop dialog.
- State global yang diubah: tidak ada.

## Test Steps

### TC-FA-TDC-373: Screening dialog Deactivate single (lolos guard) dari klik toggle Active On

1. Catat baseline jumlah entri Changelog class NB-4 untuk field Status
2. Klik toggle `Active` pada baris NB-4
3. Verifikasi toggle `Active` baris NB-4 tetap On selama dialog terbuka
4. Verifikasi dialog dengan judul `Deactivate Tax Depreciation Class`, body bullet `• NB-4 – Bukan bangunan – Kelompok 4` lalu kalimat `Are you sure you want to deactivate it?`, dan footer tombol `[Cancel]` lalu `[Deactivate]` bergaya danger
5. Verifikasi dialog tidak memuat Alert peringatan

### TC-FA-TDC-375: Cancel pada dialog Deactivate tidak mengubah status

6. Klik `[Cancel]` pada dialog Deactivate
7. Verifikasi dialog menutup
8. Verifikasi toggle `Active` baris NB-4 tetap On
9. Verifikasi tidak ada toast
10. Verifikasi jumlah entri Changelog NB-4 untuk field Status sama dengan baseline langkah 1 (tidak ada entri log baru)

### TC-FA-TDC-376: Tombol Esc menutup dialog Deactivate setara Cancel

11. Klik toggle `Active` baris NB-4
12. Tekan tombol `Esc`
13. Verifikasi dialog menutup
14. Verifikasi toggle `Active` baris NB-4 tetap On
15. Verifikasi tidak ada toast
16. Verifikasi jumlah entri Changelog NB-4 untuk field Status sama dengan baseline langkah 1 (tidak ada entri log baru)

### TC-FA-TDC-377: Klik backdrop tidak menutup dialog Deactivate (D-01)

17. Klik toggle `Active` baris NB-4
18. Klik area gelap di luar dialog (backdrop)
19. Verifikasi dialog Deactivate tetap terbuka
20. Verifikasi toggle `Active` baris NB-4 tetap On
21. Verifikasi tidak ada toast
22. Tekan `Esc`
23. Verifikasi dialog menutup tanpa perubahan data (toggle `Active` baris NB-4 tetap On)
24. Verifikasi jumlah entri Changelog NB-4 untuk field Status sama dengan baseline langkah 1 (tidak ada entri log baru)

## Notes

- Langkah penghubung (S-03): langkah 1 (baseline Changelog) dipakai sebagai pembanding langkah 10, 16, dan 24 karena tidak ada aksi yang mengubah log di antara blok (S-12). Dialog dari langkah 2 dipakai sebagai pembuka TC-FA-TDC-375 (langkah 1 TC: klik toggle yang sama; keadaan identik), sehingga langkah 6 langsung `[Cancel]`.
- Absence "tidak ada toast" pada langkah 9, 15, dan 21 diletakkan segera setelah pemicu dengan Verifikasi dialog menutup atau keadaan toggle sebagai anchor tabel termuat (8b.2, 8b.11). Absence Alert pada langkah 5 didahului langkah 4 yang membuktikan body dialog tampil (8b.2).
- Konfirmasi `[Deactivate]` yang sukses (loading, toast, kolom lain) ada di spec 241 (TC-FA-TDC-374); dialog blok Used By ada di spec 099; Alert class Active terakhir per Asset Type ada di spec 100.
- Temuan untuk QA:
  - Email akun Total Control tidak tertulis di TC; nama env password adalah usulan.
  - TC tidak memiliki tabel Data Uji Pre-setup dan Dinamis terpisah; data ditulis di kolom Precondition tiap TC dan disalin ke Prerequisites.
  - Class Code dibatasi 15 karakter, sehingga suffix `{runId}-<NNN>` tidak dapat dipasang pada kode class (S-12); spec memakai kode literal Example Data dan menyeed ulang lewat hook. Perlu konfirmasi QA.
  - TC-FA-TDC-375, TC-FA-TDC-376, dan TC-FA-TDC-377 menyebut "tidak ada entri log baru untuk NB-4" tanpa pembanding; spec memakai baseline jumlah entri (langkah 1).
  - TC-FA-TDC-377 langkah 1 memuat klaim "→ dialog Deactivate terbuka" pada langkah aksi; spec menuliskannya sebagai Verifikasi sendiri (R-02).
