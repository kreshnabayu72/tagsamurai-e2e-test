---
id: TC-FA-TDC-E2E-100-deactivate-single-alert-class-active-terakhir-per-asset-type
title: "Deactivate Single: Alert Class Active Terakhir per Asset Type"
layer: ui-e2e
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TDC-383
  - TC-FA-TDC-384
  - TC-FA-TDC-385
  - TC-FA-TDC-386
sourceRules: ["D-01", "FATDC-LOGIC-08d", "FATDC-LOGIC-08h", "R-05"]
smoke: []
dependsOn: []
trace:
  "D-01": [2, 3, 6, 7, 10, 11, 12, 13]
  "FATDC-LOGIC-08d": [6, 11]
  "FATDC-LOGIC-08h": 16
  "R-05": 17
anchor: [15]
coverage:
  web: automated
---

# Deactivate Single: Alert Class Active Terakhir per Asset Type

## Prerequisites

- Mode: FE+BE.
- Akun: Total Control (company uji Fixed Asset). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Akun dan email disediakan tim FE (email tidak tertulis di TC; lihat Temuan untuk QA); password lewat `Spectra.env.FA_TC_PASSWORD`.
- Hook suite, seeding, dan flag Guided Tooltip mengikuti `suite.md`.
- Data Pre-setup (`Fixture.fixedAssetTaxDepreciationClass.exampleData`, disediakan tim FE) disesuaikan hook `before` lewat API menjadi kondisi berikut, semuanya dengan Used By 0 dan Last Posted Tax Year kosong, satu halaman Pagination (kurang dari 10 baris) sehingga baris target tidak dicari lewat Search:
  - Asset Type Land: hanya LAND (nama "Tanah") yang Active.
  - Asset Type Building: hanya BLD-NP (nama "Bangunan tidak permanen") yang Active; BLD-P Inactive.
  - Asset Type Non-building: NB-1, NB-2, NB-4 (nama "Bukan bangunan – Kelompok 4"), dan NB-SL Active.
  Class Code dibatasi 15 karakter menurut TC sehingga kode class memakai literal Example Data tanpa suffix `{runId}-<NNN>` (lihat Temuan untuk QA); hook `before` menyeed kondisi ini lewat API dan hook `after` memulihkannya (LAND Active lagi setelah blok TC-FA-TDC-384). Data Dinamis: tidak ada.
- Kemampuan teknis (disediakan tim FE/BE, lihat `suite.md`): seed dan pemulihan class lewat API.
- State global yang diubah: status Active class LAND (dipulihkan di hook `after`).

## Test Steps

### TC-FA-TDC-386: Dialog Deactivate tanpa Alert bila masih ada class Active lain dengan Asset Type yang sama

1. Klik toggle `Active` pada baris NB-4
2. Verifikasi body dialog Deactivate berisi bullet `• NB-4 – Bukan bangunan – Kelompok 4` dan kalimat `Are you sure you want to deactivate it?`
3. Verifikasi dialog tidak memuat Alert peringatan
4. Klik `[Cancel]` untuk menutup dialog

### TC-FA-TDC-385: Dialog Deactivate memuat Alert peringatan untuk class Active terakhir bertipe Building

5. Klik toggle `Active` pada baris BLD-NP
6. Verifikasi Alert peringatan (`severity="warning"`) tampil dengan teks `No active Building class will remain. New asset classes of that type cannot be set up.`
7. Verifikasi body dialog berisi bullet `• BLD-NP – Bangunan tidak permanen` lalu kalimat `Are you sure you want to deactivate it?`
8. Klik `[Cancel]` untuk menutup dialog

### TC-FA-TDC-383: Dialog Deactivate memuat Alert peringatan untuk class Active terakhir bertipe Land

9. Klik toggle `Active` pada baris LAND
10. Verifikasi header dialog berjudul `Deactivate Tax Depreciation Class`
11. Verifikasi Alert peringatan (`severity="warning"`) tampil dengan teks `No active Land class will remain. New asset classes of that type cannot be set up.`
12. Verifikasi body dialog berisi bullet `• LAND – Tanah` lalu kalimat `Are you sure you want to deactivate it?`
13. Verifikasi footer dialog berisi tombol `[Cancel]` lalu `[Deactivate]`

### TC-FA-TDC-384: Confirm Deactivate class Active terakhir bertipe Land tetap diizinkan

14. Klik `[Deactivate]` pada dialog
15. Verifikasi dialog menutup
16. Verifikasi toggle `Active` baris LAND menjadi Off
17. Verifikasi toast sukses `Success, tax depreciation class has been deactivated.`

## Notes

- Urutan TC: 386, 385, 383, 384 (aksi yang mengubah data, TC-FA-TDC-384, di akhir; dialog yang dibatalkan lebih dulu). Dialog dari langkah 9 dipakai sebagai pembuka TC-FA-TDC-384 (langkah 1 TC: klik toggle yang sama; keadaan identik), sehingga langkah 14 langsung `[Deactivate]`.
- Langkah penghubung (S-03): langkah 4 dan 8 (menutup dialog yang hanya diamati). Pemulihan LAND Active dilakukan hook `after`; sesudah langkah 17 tidak ada asersi yang bergantung pada LAND Active.
- Absence Alert pada langkah 3 didahului langkah 2 yang membuktikan body dialog tampil (8b.2).
- Temuan untuk QA:
  - Email akun Total Control tidak tertulis di TC; nama env password adalah usulan.
  - TC tidak memiliki tabel Data Uji Pre-setup dan Dinamis terpisah; data ditulis di kolom Precondition tiap TC dan disalin ke Prerequisites.
  - Class Code dibatasi 15 karakter, sehingga suffix `{runId}-<NNN>` tidak dapat dipasang pada kode class (S-12); spec memakai kode literal Example Data dan menyeed ulang lewat hook. Perlu konfirmasi QA.
  - TC-FA-TDC-385 mensyaratkan BLD-P Inactive, sedangkan Example Data PRD dan TC lain (mis. TC-FA-TDC-379) memakai BLD-P Active dengan Used By 1; spec menyeed kondisi Inactive di hook `before` spec ini saja.
  - Post Condition TC-FA-TDC-384 ("Status class LAND tersimpan Inactive") tidak punya langkah observasi di luar Expected, sehingga tidak diasersi terpisah (S-01).
