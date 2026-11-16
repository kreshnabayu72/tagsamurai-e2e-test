---
id: TC-FA-TDC-E2E-102-delete-single-dialog-blok-guard-1-dan-guard-2
title: "Delete Single: Dialog Blok Guard 1 dan Guard 2"
layer: ui-e2e
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-FA-TDC-399
  - TC-FA-TDC-400
  - TC-FA-TDC-401
  - TC-FA-TDC-402
sourceRules: ["D-04", "FATDC-LOGIC-09a", "D-05", "FATDC-LOGIC-09b", "FATDC-LOGIC-09c"]
smoke: []
dependsOn: []
trace:
  "D-04": [2, 14, 16]
  "FATDC-LOGIC-09a": 3
  "D-05": [6, 10]
  "FATDC-LOGIC-09b": [7, 11]
  "FATDC-LOGIC-09c": 15
coverage:
  web: automated
---

# Delete Single: Dialog Blok Guard 1 dan Guard 2

## Prerequisites

- Mode: FE+BE.
- Akun: Total Control (company uji Fixed Asset). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Akun dan email disediakan tim FE (email tidak tertulis di TC; lihat Temuan untuk QA); password lewat `Spectra.env.FA_TC_PASSWORD`.
- Hook suite, seeding, dan flag Guided Tooltip mengikuti `suite.md`.
- Data Pre-setup (`Fixture.fixedAssetTaxDepreciationClass.exampleData`, disediakan tim FE): sembilan class Example Data PRD (BLD-NP, BLD-P, LAND, NB-1, NB-2, NB-4, NB-KHS, NB-OLD, NB-SL) dengan nilai kolom persis Example Data. Kebutuhan spec ini:
  - NB-KHS (nama "Kelompok khusus pernah diposting"): Last Posted Tax Year 2026, Used By 0 (Guard 1).
  - BLD-P (nama "Bangunan permanen"): Used By 1, Last Posted Tax Year kosong (Guard 2).
  - NB-2 (nama "Bukan bangunan – Kelompok 2"): Used By 3, Last Posted Tax Year kosong (Guard 2).
  - NB-1 (nama "Bukan bangunan – Kelompok 1"): Last Posted Tax Year 2026, Used By 5 (kedua guard terpenuhi).
  Asset Class pemakai dibentuk lewat fixture API (disediakan tim FE/BE). Sembilan baris berada dalam satu halaman Pagination (10 baris per halaman), sehingga baris target tidak dicari lewat Search. Semua blok hanya membuka lalu menutup dialog blok; tidak ada data class yang berubah. Class Code dibatasi 15 karakter menurut TC sehingga kode class memakai literal Example Data tanpa suffix `{runId}-<NNN>` (lihat Temuan untuk QA); hook `before` menyeed ulang kondisi awal lewat API dan hook `after` memulihkannya. Data Dinamis: tidak ada.
- Kemampuan teknis (disediakan tim FE/BE, lihat `suite.md`): seed dan pemulihan class, Last Posted Tax Year, dan Asset Class pemakai lewat API.
- State global yang diubah: tidak ada.

## Test Steps

### TC-FA-TDC-399: Dialog blok Delete Guard 1 untuk class yang pernah diposting tanpa Asset Class pemakai

1. Klik tombol `⋯` baris NB-KHS lalu `Delete`
2. Verifikasi dialog dengan judul `Cannot Delete Tax Depreciation Class`, body bullet `• NB-KHS – Kelompok khusus pernah diposting` lalu kalimat `It was used for fiscal depreciation in 2026.`, dan footer satu tombol `[OK]`
3. Verifikasi baris NB-KHS tetap ada di tabel
4. Klik `[OK]` untuk menutup dialog

### TC-FA-TDC-400: Dialog blok Delete Guard 2 untuk class dengan Used By 1

5. Klik tombol `⋯` baris BLD-P lalu `Delete`
6. Verifikasi dialog dengan judul `Cannot Delete Tax Depreciation Class`, body bullet `• BLD-P – Bangunan permanen` lalu kalimat `This class is used by 1 asset class.`, dan footer satu tombol `[OK]`
7. Verifikasi baris BLD-P tetap ada di tabel
8. Klik `[OK]` untuk menutup dialog

### TC-FA-TDC-401: Dialog blok Delete Guard 2 untuk class dengan Used By lebih dari 1

9. Klik tombol `⋯` baris NB-2 lalu `Delete`
10. Verifikasi dialog dengan judul `Cannot Delete Tax Depreciation Class`, body bullet `• NB-2 – Bukan bangunan – Kelompok 2` lalu kalimat `This class is used by 3 asset classes.`, dan footer satu tombol `[OK]`
11. Verifikasi baris NB-2 tetap ada di tabel
12. Klik `[OK]` untuk menutup dialog

### TC-FA-TDC-402: Guard 1 menang atas Guard 2 saat kedua guard terpenuhi

13. Klik tombol `⋯` baris NB-1 lalu `Delete`
14. Verifikasi dialog `Cannot Delete Tax Depreciation Class` tampil dengan bullet `• NB-1 – Bukan bangunan – Kelompok 1` dan kalimat `It was used for fiscal depreciation in 2026.`
15. Verifikasi kalimat `This class is used by 5 asset classes.` tidak tampil
16. Verifikasi footer dialog berisi satu tombol `[OK]`
17. Klik `[OK]` untuk menutup dialog

## Notes

- Langkah penghubung (S-03): langkah 4, 8, 12, dan 17 (menutup dialog blok dengan `[OK]`; perilaku `[OK]` diuji di spec 103).
- Absence pada langkah 15 didahului langkah 14 yang membuktikan dialog dan kalimat Guard 1 tampil (8b.2).
- Temuan untuk QA:
  - Email akun Total Control tidak tertulis di TC; nama env password adalah usulan.
  - TC tidak memiliki tabel Data Uji Pre-setup dan Dinamis terpisah; data ditulis di kolom Precondition tiap TC dan disalin ke Prerequisites.
  - Class Code dibatasi 15 karakter, sehingga suffix `{runId}-<NNN>` tidak dapat dipasang pada kode class (S-12); spec memakai kode literal Example Data dan menyeed ulang lewat hook. Perlu konfirmasi QA.
  - TC-FA-TDC-399 Expected d ("Baris NB-KHS tetap ada di tabel") tidak menyebut apakah dicek saat dialog terbuka atau sesudah ditutup; spec mengecek saat dialog terbuka (baris di belakang dialog), sama untuk TC-FA-TDC-400 dan TC-FA-TDC-401.
  - TC tidak menyebut mekanisme membentuk Asset Class pemakai (Used By 1, 3, dan 5) dan Last Posted Tax Year; spec menuliskannya sebagai kemampuan fixture "disediakan tim FE/BE" tanpa endpoint karangan (S-13).
