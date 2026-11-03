---
id: TC-AC-CS-E2E-008-list-baris-requester-distributor
title: "List: Baris Requester Distributor"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-CS-9
  - TC-AC-CS-14
  - TC-AC-CS-39
  - TC-AC-CS-52
coverage:
  web: automated
---

# List: Baris Requester Distributor

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: `createOnlySub_automated_{namaCompany}@qwertysystem.net` (`Fajar Nugroho`, capability Create saja, Distributor PT Maju Bersama; Pre-setup #6), password `Spectra.env.AC_SUB_CREATE_PASSWORD`; login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Hook `after` mengembalikan sesi ke akun default suite (Total Control Principal, Pre-setup #1).
- Email akun dirujuk lewat `Fixture.license-allocation-subscription` (belum ada; disediakan tim FE); nama env password terdaftar di `executionConfig.environmentVariables` dan `.env.example` (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`). Hook `beforeEach` suite membuka Allocation > Client Subscription tab Current dan menjadi jaring pengaman S-09 (lihat `suite.md`). Flag Guided Tooltip diatur hook `before` suite (`seen`), sehingga walkthrough tidak muncul.
- Data Pre-setup baca-saja: #49 `SUBS-20260819-00001` (Apotek Sehat Sentosa, FAMS Growth, Waiting for Approval, Plan Owner PT Maju Bersama) dan #59 `SUBS-20260819-00004` (PT Bintang Timur, FAMS Growth Trial, Waiting for Approval); aktor adalah requester original kedua baris. Spec tidak mengubah kedua baris.

## Test Steps

### TC-AC-CS-9: Baris term Waiting for Approval di tab Current: badge, tanggal kosong, dan row action requester

1. Ketik Search `SUBS-20260819-00001`, tekan Enter
2. Klik ikon `⋯` pada baris itu
3. Verifikasi kolom Status menampilkan badge "Waiting for Approval" severity warning
4. Verifikasi kolom Start Date dan End Date menampilkan "—"
5. Verifikasi menu row action berisi tepat: Detail, Subscription Log, Edit, Cancel Request
6. Verifikasi Renew, Convert, Resubmit, dan Cancel Subscription tidak ada di menu

### TC-AC-CS-14: Baris Trial Waiting for Approval di tab Current: badge Trial dan row action requester

7. Ganti isi kotak search dengan `SUBS-20260819-00004`, tekan Enter
8. Klik ikon `⋯` pada baris itu
9. Verifikasi kolom Plan menampilkan "Growth" dengan badge "Trial" severity primary
10. Verifikasi kolom Status menampilkan badge "Waiting for Approval" severity warning
11. Verifikasi menu row action berisi tepat: Detail, Subscription Log, Edit, Cancel Request
12. Verifikasi Convert, Renew, dan Cancel Subscription tidak ada di menu

### TC-AC-CS-39: Subscription Info term Waiting for Approval menampilkan tanggal kosong

13. Ganti isi kotak search dengan `SUBS-20260819-00001`, tekan Enter
14. Klik baris `SUBS-20260819-00001`
15. Verifikasi Status `Waiting for Approval`
16. Verifikasi Start Date, End Date, dan Grace End menampilkan "—"
17. Verifikasi Plan Owner `PT Maju Bersama (Distributor)`

### TC-AC-CS-52: Tombol aksi Detail term Waiting for Approval untuk requester

18. Amati tombol aksi di pojok kanan atas card Subscription Info
19. Verifikasi tombol aksi: Edit, Cancel Request, Subscription Log
20. Verifikasi tombol Renew, Cancel Subscription, dan Resubmit tidak ada
21. Klik segmen `Client Subscription` pada Breadcrumb

## Notes

- Mode: FE+BE. Sumber: `admin-console/license-allocation-subscription/TestCases/tc-license-allocation-subscription.md`.
- Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): langkah Search untuk menemukan baris target (R-16) dan klik segmen `Client Subscription` pada Breadcrumb di akhir spec.
- TC-AC-CS-52 melanjutkan dari Detail `SUBS-20260819-00001` yang dibuka TC-AC-CS-39 (Dependensi TC-AC-CS-9 hanya precondition requester; baris dan akun sama).
- Temuan untuk QA:
  - TC-AC-CS-9 dan TC-AC-CS-14 mensyaratkan aktor adalah requester original baris; TC tidak menyebut cara membuktikannya selain data Pre-setup #49 dan #59 (S-15).
  - TC-AC-CS-52 LK "Buka Detail" tidak menyebut baris yang dicari; Precondition menyebut `SUBS-20260819-00001`.
