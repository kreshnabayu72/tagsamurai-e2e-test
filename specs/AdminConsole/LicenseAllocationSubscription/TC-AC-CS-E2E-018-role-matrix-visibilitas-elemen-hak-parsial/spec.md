---
id: TC-AC-CS-E2E-018-role-matrix-visibilitas-elemen-hak-parsial
title: "Role Matrix: Visibilitas Elemen Hak Parsial"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-CS-77
  - TC-AC-CS-78
  - TC-AC-CS-79
coverage:
  web: automated
---

# Role Matrix: Visibilitas Elemen Hak Parsial

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: `createOnlySub_automated_{namaCompany}@qwertysystem.net` (`Fajar Nugroho`, capability Create saja, Distributor PT Maju Bersama; Pre-setup #6), password `Spectra.env.AC_SUB_CREATE_PASSWORD`; login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Akun lain (ganti akun lewat langkah eksplisit di `## Test Steps`; hook `after` mengembalikan sesi ke akun default suite, Total Control Principal #1):
  - `deleteOnlySub_automated_{namaCompany}@qwertysystem.net` (`Siti Rahmawati`, capability Delete saja, Distributor PT Maju Bersama; Pre-setup #7), password `Spectra.env.AC_SUB_DELETE_PASSWORD`
  - `createDeleteSub_automated_{namaCompany}@qwertysystem.net` (`Agus Prasetyo`, capability Create dan Delete, Distributor PT Maju Bersama; Pre-setup #8), password `Spectra.env.AC_SUB_CRDEL_PASSWORD`
- Email akun dirujuk lewat `Fixture.license-allocation-subscription` (belum ada; disediakan tim FE); nama env password terdaftar di `executionConfig.environmentVariables` dan `.env.example` (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`). Hook `beforeEach` suite membuka Allocation > Client Subscription tab Current dan menjadi jaring pengaman S-09 (lihat `suite.md`). Flag Guided Tooltip diatur hook `before` suite (`seen`), sehingga walkthrough tidak muncul.
- Tabel "Role yang diuji": capability Create saja Distributor (#6), capability Delete saja Distributor (#7), capability Create dan Delete Distributor tanpa tier Total Control (#8).
- Data Pre-setup baca-saja: #69 `SUBS-20250815-00001` (Warung Kopi Senja, Active, tanpa trial dan tanpa successor), trial Active `Klinik Harapan Bunda` SAMS Growth (Start 10/08/26, End 08/09/26, Plan Owner CV Karya Mandiri, tanpa term paid SAMS; #71), #61 `SUBS-20260101-00001` (Active, scope WRITE).

## Test Steps

### TC-AC-CS-77: Visibilitas elemen untuk pemegang capability Create saja

1. Verifikasi `[+ Subscription]` dan `[+ Activate Trial]` Show
2. Ketik Search `SUBS-20250815-00001`, tekan Enter
3. Klik ikon `⋯` pada baris Active
4. Verifikasi menu row action baris Active menampilkan Detail, Subscription Log, dan Renew
5. Verifikasi Cancel Subscription Hidden karena tidak ada Delete
6. Ganti isi kotak search dengan `Klinik Harapan Bunda`, tekan Enter
7. Klik ikon `⋯` pada baris Trial Active
8. Verifikasi menu row action baris Trial Active menampilkan Detail, Subscription Log, dan Convert

### TC-AC-CS-78: Visibilitas elemen untuk pemegang capability Delete saja

9. Logout lalu login sbg Role: Delete-Only (Distributor) `Siti Rahmawati`
10. Buka menu `Allocation > Client Subscription`
11. Verifikasi Search, Filter, Download, dan Changelog Show di toolbar
12. Verifikasi `[+ Subscription]` dan `[+ Activate Trial]` Hidden
13. Ketik Search `SUBS-20260101-00001`, tekan Enter
14. Klik ikon `⋯` pada baris Active `SUBS-20260101-00001`
15. Verifikasi menu row action berisi Detail, Subscription Log, dan Cancel Subscription
16. Verifikasi Renew, Convert, Edit, Cancel Request, dan Resubmit Hidden

### TC-AC-CS-79: Visibilitas elemen untuk pemegang Create dan Delete tanpa tier Total Control

17. Logout lalu login sbg Role: Create dan Delete (Distributor) `Agus Prasetyo`
18. Buka menu `Allocation > Client Subscription`
19. Verifikasi `[+ Subscription]` dan `[+ Activate Trial]` Show
20. Ketik Search `SUBS-20250815-00001`, tekan Enter
21. Klik ikon `⋯` pada baris Active `SUBS-20250815-00001`
22. Verifikasi menu row action berisi Detail, Subscription Log, Renew, dan Cancel Subscription

## Notes

- Mode: FE+BE. Sumber: `admin-console/license-allocation-subscription/TestCases/tc-license-allocation-subscription.md`.
- Subjudul `###` memetakan langkah ke id TC granular.
- Spec ditulis per blok role karena ganti akun menuntut langkah eksplisit (bagian 3a; akun pertama login di hook `before`). Langkah penghubung (S-03): langkah Search untuk menemukan baris target (R-16).
- Verifikasi `Search, Filter, Download, dan Changelog Show` di awal TC-AC-CS-78 mendahului Verifikasi `Hidden` sebagai anchor absence (bagian 8b butir 2).
- Temuan untuk QA:
  - TC-AC-CS-77 Expected c menyebut "baris Trial Active" tanpa Subscription ID; spec mencarinya lewat Client `Klinik Harapan Bunda` (Pre-setup #71).
  - TC-AC-CS-79 menyebut akun `Agus Prasetyo` dengan Pre-setup #8; TC-AC-CS-78 menyebut role "Delete-Only" tanpa nama akun dan tanpa nomor Pre-setup (sumber: Pre-setup #7 pada Tabel Data Uji Pre-setup).
