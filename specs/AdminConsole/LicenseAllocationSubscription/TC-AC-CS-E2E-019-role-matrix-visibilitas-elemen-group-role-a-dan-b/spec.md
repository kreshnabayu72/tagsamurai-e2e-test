---
id: TC-AC-CS-E2E-019-role-matrix-visibilitas-elemen-group-role-a-dan-b
title: "Role Matrix: Visibilitas Elemen Group Role A dan B"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-CS-80
  - TC-AC-CS-330
  - TC-AC-CS-81
coverage:
  web: automated
---

# Role Matrix: Visibilitas Elemen Group Role A dan B

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: `groupAReadSub_automated_{namaCompany}@qwertysystem.net` (`Gilang Ramadhan`, Group Role Manage allocation Read saja pada Group A, Distributor; Pre-setup #16), password `Spectra.env.AC_SUB_GROUPA_PASSWORD`; login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Akun lain (ganti akun lewat langkah eksplisit di `## Test Steps`; hook `after` mengembalikan sesi ke akun default suite, Total Control Principal #1):
  - `groupBCreateSub_automated_{namaCompany}@qwertysystem.net` (`Hana Permata`, Group Role Manage allocation Create dan Read pada Group B, Distributor; Pre-setup #17), password `Spectra.env.AC_SUB_GROUPB_PASSWORD`
- Email akun dirujuk lewat `Fixture.license-allocation-subscription` (belum ada; disediakan tim FE); nama env password terdaftar di `executionConfig.environmentVariables` dan `.env.example` (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`). Hook `beforeEach` suite membuka Allocation > Client Subscription tab Current dan menjadi jaring pengaman S-09 (lihat `suite.md`). Flag Guided Tooltip diatur hook `before` suite (`seen`), sehingga walkthrough tidak muncul.
- Tabel "Role yang diuji": Group Role Manage allocation Read saja pada Group A (#16), Group Role Create dan Read pada Group B (#17).
- Data Pre-setup baca-saja: Client `Toko Group A` dengan term FAMS Growth dan SAMS Growth Active (#127, tab Current hanya memuat Product FAMS dan SAMS bertipe Paid bagi akun #16), term Active `SUBS-20260401-00005` Client `Toko Group B` (#132).

## Test Steps

### TC-AC-CS-80: Group A Read-only: list dan Detail view-only

1. Verifikasi Search, Filter, Download, dan Changelog Show di toolbar
2. Verifikasi `[+ Subscription]` dan `[+ Activate Trial]` Hidden
3. Ketik Search `Toko Group A`, tekan Enter
4. Klik ikon `⋯` pada salah satu baris dalam Group A
5. Verifikasi menu row action hanya berisi Detail dan Subscription Log
6. Klik `Detail`
7. Verifikasi Detail terbuka tanpa tombol aksi tulis
8. Verifikasi tombol Subscription Log tetap tampil
9. Klik segmen `Client Subscription` pada Breadcrumb

### TC-AC-CS-330: Opsi dropdown Product dan Type hanya nilai yang ada pada baris tab aktif

10. Klik ikon Filter di toolbar
11. Buka dropdown Product
12. Verifikasi opsi Product hanya `FAMS` dan `SAMS`
13. Buka dropdown Type
14. Verifikasi opsi Type hanya `Paid`
15. Verifikasi `SIEM` dan `Trial` tidak tampil karena tidak ada barisnya
16. Tutup Filter Panel

### TC-AC-CS-81: Group B Create dan Read: aksi Create tersedia tetapi Cancel Subscription tidak

17. Logout lalu login sbg Role: Group B Create dan Read (Distributor) `Hana Permata`
18. Buka menu `Allocation > Client Subscription`
19. Verifikasi `[+ Subscription]` dan `[+ Activate Trial]` Show
20. Ketik Search `SUBS-20260401-00005`, tekan Enter
21. Klik ikon `⋯` pada baris Active dalam Group B
22. Verifikasi menu row action berisi Detail, Subscription Log, dan Renew
23. Verifikasi Cancel Subscription tidak tersedia karena memerlukan Delete

## Notes

- Mode: FE+BE. Sumber: `admin-console/license-allocation-subscription/TestCases/tc-license-allocation-subscription.md`.
- Subjudul `###` memetakan langkah ke id TC granular.
- Spec ditulis per blok role karena ganti akun menuntut langkah eksplisit (bagian 3a; akun pertama login di hook `before`). Langkah penghubung (S-03): langkah Search untuk menemukan baris target (R-16), klik segmen `Client Subscription` pada Breadcrumb, dan menutup Filter Panel. Urutan TC: 80, 330, 81 (S-10). Verifikasi toolbar di awal TC-AC-CS-80 mendahului Verifikasi `Hidden` sebagai anchor absence (bagian 8b butir 2).
- Temuan untuk QA:
  - TC-AC-CS-330 tidak menyebut tab Current yang aktif saat Filter dibuka; spec membukanya pada tab `Current` sesudah klik segmen `Client Subscription` (halaman dibuka hook `beforeEach` pada awal, tab `Current`).
  - TC-AC-CS-80 langkah 2 "Buka Detail salah satu baris" tidak menyebut baris; spec memakai baris Group A dari Search `Toko Group A`.
