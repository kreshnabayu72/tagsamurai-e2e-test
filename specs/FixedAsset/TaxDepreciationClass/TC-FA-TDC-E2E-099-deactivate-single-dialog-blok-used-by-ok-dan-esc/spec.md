---
id: TC-FA-TDC-E2E-099-deactivate-single-dialog-blok-used-by-ok-dan-esc
title: "Deactivate Single: Dialog Blok Used By, OK, dan Esc"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-FA-TDC-379
  - TC-FA-TDC-380
  - TC-FA-TDC-381
  - TC-FA-TDC-382
coverage:
  web: automated
---

# Deactivate Single: Dialog Blok Used By, OK, dan Esc

## Prerequisites

- Mode: FE+BE.
- Akun: Total Control (company uji Fixed Asset). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Akun dan email disediakan tim FE (email tidak tertulis di TC; lihat Temuan untuk QA); password lewat `Spectra.env.FA_TC_PASSWORD`.
- Hook suite, seeding, dan flag Guided Tooltip mengikuti `suite.md`.
- Data Pre-setup (`Fixture.fixedAssetTaxDepreciationClass.exampleData`, disediakan tim FE): sembilan class Example Data PRD (BLD-NP, BLD-P, LAND, NB-1, NB-2, NB-4, NB-KHS, NB-OLD, NB-SL) dengan nilai kolom persis Example Data. Kebutuhan spec ini: BLD-P (nama "Bangunan permanen") Active dengan Used By 1 (satu Asset Class pemakai); NB-2 (nama "Bukan bangunan – Kelompok 2") Active dengan Used By 3 (tiga Asset Class pemakai). Asset Class pemakai dibentuk lewat fixture API (disediakan tim FE/BE). Sembilan baris berada dalam satu halaman Pagination (10 baris per halaman), sehingga baris target tidak dicari lewat Search. Semua blok hanya membuka lalu menutup dialog blok; tidak ada data class yang berubah. Class Code dibatasi 15 karakter menurut TC sehingga kode class memakai literal Example Data tanpa suffix `{runId}-<NNN>` (lihat Temuan untuk QA); hook `before` menyeed ulang kondisi awal (termasuk Used By) lewat API dan hook `after` memulihkannya. Data Dinamis: tidak ada.
- Kemampuan teknis (disediakan tim FE/BE, lihat `suite.md`): seed dan pemulihan class serta Asset Class pemakai lewat API; kemampuan baca jumlah entri Changelog class NB-2 untuk field Status (baseline dicatat sebelum aksi dan dibandingkan sesudahnya, 8b.10, S-12); menekan `Esc`.
- State global yang diubah: tidak ada.

## Test Steps

### TC-FA-TDC-379: Dialog blok Deactivate single untuk class dengan Used By 1

1. Klik toggle `Active` pada baris BLD-P
2. Verifikasi toggle `Active` baris BLD-P tetap On
3. Verifikasi dialog dengan judul `Cannot Deactivate Tax Depreciation Class`, body bullet `• BLD-P – Bangunan permanen` lalu kalimat `Used by 1 asset class. Change it in Asset Class first.`, dan footer satu tombol `[OK]`
4. Klik `[OK]` untuk menutup dialog

### TC-FA-TDC-380: Dialog blok Deactivate single untuk class dengan Used By lebih dari 1

5. Catat baseline jumlah entri Changelog class NB-2 untuk field Status
6. Klik toggle `Active` pada baris NB-2
7. Verifikasi toggle `Active` baris NB-2 tetap On
8. Verifikasi dialog dengan judul `Cannot Deactivate Tax Depreciation Class`, body bullet `• NB-2 – Bukan bangunan – Kelompok 2` lalu kalimat `Used by 3 asset classes. Change them in Asset Class first.`, dan footer satu tombol `[OK]`

### TC-FA-TDC-381: Tombol OK menutup dialog blok Deactivate tanpa perubahan

9. Klik `[OK]` pada dialog blok
10. Verifikasi dialog menutup
11. Verifikasi toggle `Active` baris NB-2 tetap On
12. Verifikasi tidak ada toast
13. Klik ikon Changelog di toolbar
14. Verifikasi modal Changelog menampilkan sedikitnya satu entri
15. Verifikasi jumlah entri Changelog NB-2 untuk field Status sama dengan baseline langkah 5 (tidak ada entri Status baru)
16. Tutup modal Changelog

### TC-FA-TDC-382: Tombol Esc menutup dialog blok Deactivate tanpa perubahan

17. Klik toggle `Active` baris NB-2
18. Tekan tombol `Esc`
19. Verifikasi dialog blok menutup
20. Verifikasi toggle `Active` baris NB-2 tetap On
21. Verifikasi tidak ada toast
22. Verifikasi jumlah entri Changelog NB-2 untuk field Status sama dengan baseline langkah 5 (tidak ada entri log baru)

## Notes

- Langkah penghubung (S-03): langkah 4 (menutup dialog TC-FA-TDC-379 sebelum blok berikut), langkah 16 (menutup modal Changelog), dan langkah 5 (baseline Changelog yang juga dipakai langkah 22 karena tidak ada aksi yang mengubah log di antara blok, S-12). Dialog dari langkah 6 dipakai sebagai pembuka TC-FA-TDC-381 (langkah 1 TC: klik toggle yang sama; keadaan identik), sehingga langkah 9 langsung `[OK]`.
- Absence "tidak ada toast" pada langkah 12 dan 21 diletakkan segera setelah pemicu dengan Verifikasi dialog menutup dan keadaan toggle sebagai anchor (8b.2, 8b.11). Absence entri pada langkah 15 didahului anchor langkah 14.
- Temuan untuk QA:
  - Email akun Total Control tidak tertulis di TC; nama env password adalah usulan.
  - TC tidak memiliki tabel Data Uji Pre-setup dan Dinamis terpisah; data ditulis di kolom Precondition tiap TC dan disalin ke Prerequisites.
  - Class Code dibatasi 15 karakter, sehingga suffix `{runId}-<NNN>` tidak dapat dipasang pada kode class (S-12); spec memakai kode literal Example Data dan menyeed ulang lewat hook. Perlu konfirmasi QA.
  - TC tidak menyebut mekanisme membentuk Asset Class pemakai (Used By 1 dan 3); spec menuliskannya sebagai kemampuan fixture "disediakan tim FE/BE" tanpa endpoint karangan (S-13).
  - TC-FA-TDC-382 menyebut "tidak ada entri log baru" tanpa pembanding; spec memakai baseline jumlah entri (langkah 5).
