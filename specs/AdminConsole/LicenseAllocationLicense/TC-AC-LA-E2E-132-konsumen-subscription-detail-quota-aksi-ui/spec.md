---
id: TC-AC-LA-E2E-132-konsumen-subscription-detail-quota-aksi-ui
title: "Konsumen Subscription Detail: License Quota setelah Approve dan Cancel Term"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-LA-425
  - TC-AC-LA-492
coverage:
  web: automated
---

# Konsumen Subscription Detail: License Quota setelah Approve dan Cancel Term

## Prerequisites

- Mode: FE+BE
- Login di hook `before` spec ini sebagai Fajar Nugroho; halaman dibuka hook `beforeEach` suite (tab Current), yang juga menjadi jaring pengaman `beforeunload` dan dialog `Unsaved Changes` (lihat `suite.md`); spec berpindah ke Approvals dan Subscription Detail sebagai langkah. Flag Guided Tooltip diatur hook `before` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Akun yang dipakai:

| Akun | Pre-setup | Peran | Email | Env password |
|---|---|---|---|---|
| Fajar Nugroho | #10 | Total Control Distributor PT Maju Bersama (approver, pelaku Cancel Subscription) | `totalControlDistLic_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.AC_LA_TC_DIST_PASSWORD` |

  Email dan `{namaCompany}` dirujuk lewat `Fixture.license-allocation-license` (fixture belum ada; disediakan tim FE).
- Data Pre-setup: Client PT Sejahtera (Pre-setup #19; `SUBS-20260101-A1B2C`), Toko Serba Ada (Pre-setup #21; term Active `SUBS-20250201-J7K8L`) sebagai term pembanding, Bengkel Cahaya Motor (Pre-setup #23; FAMS Professional Paid Active, End Date 31 Dec 2026), kantong wallet Distributor PT Maju Bersama saldo $10,000.00 (Pre-setup #33), Product Price (Pre-setup #34), Require Approval for Allocation ON (Pre-setup #38).
- Data Dinamis (seed milik spec ini, dibuat lewat seeding backend di hook `before`; tidak memakai baris Pre-setup #41 dan #47 bersama):
  - `{idQuota}`: alokasi `Waiting for Approval` Concurrent User +5 ke `SUBS-20260101-A1B2C` PT Sejahtera, requester Dewi Anggraini (Pre-setup #4), Cost $150.00 di-Reserve (bentuk Pre-setup #41);
  - `{idActive}`: alokasi `Active` Concurrent User +10 ke FAMS Professional Bengkel Cahaya Motor (End Date 31 Dec 2026), requester Dewi Anggraini (bentuk Pre-setup #47).
- Kemampuan teknis (disediakan tim FE/BE): seeding alokasi dan pembersihannya; fixture backend untuk memulihkan term Subscription FAMS Professional Bengkel Cahaya Motor yang di-Cancel.
- State global: term FAMS Professional Bengkel Cahaya Motor (Pre-setup #23) berubah menjadi Canceled pada blok TC-AC-LA-492 dan dipulihkan oleh fixture backend di hook `after` (S-06, pengecualian 2026-10-30; Last Updated dan entri audit trail term berubah); saldo kantong #33 dipulihkan oleh pembersihan record.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### License Quota setelah Approve (TC-AC-LA-425)

1. Buka Subscription Detail `SUBS-20260101-A1B2C` > License Quota
2. Catat total Concurrent User sebagai `{q0}`
3. Buka Subscription Detail `SUBS-20250201-J7K8L` > License Quota
4. Catat total Concurrent User sebagai `{qToko0}`
5. Buka Approvals > License Allocation
6. Klik `[Review]` pada alokasi `{idQuota}`
7. Pilih Approve
8. Klik Submit
9. Tunggu aksi selesai (tombol Submit aktif kembali atau baris keputusan hilang dari Tab Active)
10. Buka kembali Subscription Detail `SUBS-20260101-A1B2C` > License Quota tanpa memuat ulang data lain
11. Verifikasi total Concurrent User term `SUBS-20260101-A1B2C` bertambah 5 terhadap `{q0}` (real-time)
12. Buka Subscription Detail `SUBS-20250201-J7K8L` > License Quota
13. Verifikasi total Concurrent User term `SUBS-20250201-J7K8L` sama dengan `{qToko0}` (tidak bertambah pada term lain)

### License Quota setelah Cancel term (TC-AC-LA-492)

14. Buka Subscription Detail term FAMS Professional Bengkel Cahaya Motor > License Quota
15. Catat total Concurrent User sebagai `{qBengkel0}`
16. Klik `Cancel Subscription` pada term FAMS Professional Bengkel Cahaya Motor
17. Konfirmasi dialog pembatalan Subscription
18. Tunggu aksi selesai (dialog pembatalan tertutup)
19. Buka Subscription Detail term itu > License Quota
20. Verifikasi total Concurrent User term itu berkurang 10 terhadap `{qBengkel0}` seketika karena alokasi `{idActive}` menjadi Expired

## Notes

- Langkah penghubung (S-03): langkah 3, 4, dan 12 (membaca term pembanding), langkah 5 (berpindah ke Approvals), langkah 9 dan 18 (menunggu aksi selesai, 8b.8), langkah 17 (konfirmasi dialog pembatalan).
- Temuan untuk QA:
  - TC-AC-LA-425 butir a ("tidak pada term lain") tidak menyebut term pembanding; PT Sejahtera hanya punya satu term (`SUBS-20260101-A1B2C`, Pre-setup #19). Spec memakai term Active Toko Serba Ada `SUBS-20250201-J7K8L` sebagai term lain.
  - TC-AC-LA-425 dan 492 menyebut "License Quota" di Subscription Detail tanpa menyebut letak tab atau nilai awal; spec membandingkan terhadap nilai yang dicatat sebelum aksi.
  - TC-AC-LA-492 tidak menyebut dialog konfirmasi `Cancel Subscription`, akun pelaku selain Pre-setup #10, atau letak aksi pada Subscription Detail; spec mengikuti penulisan TC dan menambah satu langkah penghubung konfirmasi dialog.
  - TC-AC-LA-492 mensyaratkan alokasi `Active` Pre-setup #47 pada term Pre-setup #23 tanpa menyebut bahwa Cancel term mengubah data Pre-setup bersama; pemulihan dijamin fixture backend.
