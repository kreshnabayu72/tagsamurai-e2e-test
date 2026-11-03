---
id: TC-AC-CS-E2E-022-capability-edit-cancel-request-resubmit-cancel-subscription-sampai-sukses
title: "Capability: Edit, Cancel Request, Resubmit, dan Cancel Subscription sampai Sukses"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-CS-87
  - TC-AC-CS-88
  - TC-AC-CS-89
  - TC-AC-CS-90
coverage:
  web: automated
---

# Capability: Edit, Cancel Request, Resubmit, dan Cancel Subscription sampai Sukses

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: `createOnlySub_automated_{namaCompany}@qwertysystem.net` (`Fajar Nugroho`, capability Create saja, Distributor PT Maju Bersama; Pre-setup #6), password `Spectra.env.AC_SUB_CREATE_PASSWORD`; login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Akun lain (ganti akun lewat langkah eksplisit di `## Test Steps`; hook `after` mengembalikan sesi ke akun default suite, Total Control Principal #1):
  - `createOnlyPartnerSub_automated_{namaCompany}@qwertysystem.net` (`Rina Pratama`, capability Create saja, Partner CV Karya Mandiri; Pre-setup #12), password `Spectra.env.AC_SUB_PARTNER_CREATE_PASSWORD`
  - `deleteOnlySub_automated_{namaCompany}@qwertysystem.net` (`Siti Rahmawati`, capability Delete saja, Distributor PT Maju Bersama; Pre-setup #7), password `Spectra.env.AC_SUB_DELETE_PASSWORD`
- Email akun dirujuk lewat `Fixture.license-allocation-subscription` (belum ada; disediakan tim FE); nama env password terdaftar di `executionConfig.environmentVariables` dan `.env.example` (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`). Hook `beforeEach` suite membuka Allocation > Client Subscription tab Current dan menjadi jaring pengaman S-09 (lihat `suite.md`). Flag Guided Tooltip diatur hook `before` suite (`seen`), sehingga walkthrough tidak muncul.
- Kemampuan teknis (disediakan tim FE/BE, mekanisme tidak tertulis di TC, PRD, atau LLD sehingga tanpa endpoint karangan; S-13): mengatur toggle Require Approval for Allocation (per entitas PT Maju Bersama dan CV Karya Mandiri; Pre-setup #23) dan Require Approval for Trial Activation (platform-wide; #24), serta memulihkan data Pre-setup yang berubah. Nilai awal toggle dicatat di hook `before` dan dipulihkan di hook `after`.
- State awal: Require Approval for Allocation ON untuk CV Karya Mandiri (TC-AC-CS-89; aktor bukan bypass; Pre-setup #23), diatur di hook `before` spec ini; Pay From `Partner Pocket` saldo $25,000.00 (Pre-setup #21, tidak diubah selain Reserve oleh Resubmit dan dipulihkan fixture).
- Data seed milik spec (dibuat lewat API di hook `before` dengan sesi API aktor pemilik, dihapus di hook `after`):
  - Client `Apotek Sehat Sentosa+{runId}-022`: pengajuan Waiting for Approval milik `Fajar Nugroho`, Duration `1` (padanan Pre-setup #49); menerima Edit lalu Cancel Request.
  - Client `Optik Cahaya+{runId}-022`: pengajuan berstatus Canceled milik `Rina Pratama`, Plan Owner CV Karya Mandiri (padanan Pre-setup #56); menerima Resubmit.
  - Client `PT Sejahtera+{runId}-022`: term Active, scope WRITE bagi `Siti Rahmawati` (padanan Pre-setup #61); menerima Cancel Subscription.
- Restore yang tersisa hanya untuk state global: saldo Wallet `Partner Pocket` (Pre-setup #21) yang berkurang oleh Reserve Resubmit, dipulihkan fixture backend di langkah penghubung dan di hook `after`; seed per spec tidak dapat memulihkan Wallet bersama.

## Test Steps

### TC-AC-CS-87: Pemegang Create saja menyelesaikan Edit pada pengajuannya sendiri

1. Ketik Search `Apotek Sehat Sentosa+{runId}-022`, tekan Enter
2. Klik ikon `⋯` pada baris Client `Apotek Sehat Sentosa+{runId}-022`
3. Pilih `Edit`
4. Ubah Duration dari `1` menjadi `2`
5. Klik `[Save]`
6. Verifikasi modal tertutup
7. Verifikasi muncul toast sukses "Success, subscription has been updated."
8. Verifikasi status tetap Waiting for Approval

### TC-AC-CS-88: Pemegang Create saja menyelesaikan Cancel Request pada pengajuannya sendiri

9. Ganti isi kotak search dengan `Apotek Sehat Sentosa+{runId}-022`, tekan Enter
10. Klik ikon `⋯` pada baris Client `Apotek Sehat Sentosa+{runId}-022`
11. Pilih `Cancel Request`
12. Klik `[Cancel Request]` pada dialog
13. Verifikasi muncul toast sukses "Success, your request has been canceled."
14. Klik tab `History`
15. Verifikasi baris berstatus Canceled Client `Apotek Sehat Sentosa+{runId}-022` tampil di tab `History`
16. Klik tab `Current`

### TC-AC-CS-89: Pemegang Create saja menyelesaikan Resubmit atas record Canceled miliknya

17. Logout lalu login sbg Role: Create-Only (Partner) `Rina Pratama`
18. Buka menu `Allocation > Client Subscription`
19. Klik tab `History`
20. Ketik Search `Optik Cahaya+{runId}-022`, tekan Enter
21. Klik ikon `⋯` pada baris Client `Optik Cahaya+{runId}-022`
22. Pilih `Resubmit`
23. Pilih Pay From `Partner Pocket`
24. Klik `[Submit]`
25. Verifikasi muncul toast sukses "Success, your request has been submitted for approval."
26. Klik tab `Current`
27. Verifikasi record baru berstatus Waiting for Approval tampil di tab `Current`
28. Pulihkan saldo Wallet `Partner Pocket` (Pre-setup #21) ke saldo awal melalui fixture backend

### TC-AC-CS-90: Pemegang Delete saja menyelesaikan Cancel Subscription

29. Logout lalu login sbg Role: Delete-Only (Distributor) `Siti Rahmawati`
30. Buka menu `Allocation > Client Subscription`
31. Ketik Search `PT Sejahtera+{runId}-022`, tekan Enter
32. Klik ikon `⋯` pada baris Client `PT Sejahtera+{runId}-022`
33. Pilih `Cancel Subscription`
34. Klik `[Cancel Subscription]` pada dialog
35. Verifikasi muncul toast sukses "Success, subscription has been canceled."
36. Klik tab `History`
37. Verifikasi baris berstatus Archive Client `PT Sejahtera+{runId}-022` tampil di tab `History`

## Notes

- Mode: FE+BE. Sumber: `admin-console/license-allocation-subscription/TestCases/tc-license-allocation-subscription.md`.
- Subjudul `###` memetakan langkah ke id TC granular.
- Spec ditulis per blok akun karena ganti akun menuntut langkah eksplisit (bagian 3a; akun pertama login di hook `before`). Langkah penghubung (S-03): langkah Search untuk menemukan baris target (R-16), klik tab `Current` dan `History`, dan pemulihan saldo Wallet `Partner Pocket` lewat fixture backend (state global). TC-AC-CS-90 ditulis terakhir karena Cancel Subscription mengubah status term (S-10).
- Spec positif: hanya capability yang dimiliki yang diasersi; jalur ditolak ada di spec Role Matrix lain.
- Spec ini 37 langkah, di atas smell 35 langkah. Alasan: empat blok TC (Edit dan Cancel Request, Resubmit, Cancel Subscription) satu kelas fungsional positif pada halaman List yang sama; tiga akun (Create-Only Distributor, Create-Only Partner, Delete-Only Distributor) dengan ganti akun eksplisit di langkah 17 dan 29 karena TC mensyaratkan peran berbeda (bagian 3a); tiap blok memakai Client seed sendiri sehingga tidak ada state antar blok; jumlah langkah berasal dari Verifikasi per klausa Expected (S-01) dan Search per baris target (R-16); pemecahan menambah login ulang dan seeding tanpa menambah isolasi.
- Temuan untuk QA:
  - TC-AC-CS-89 Expected b menyebut "record baru" tanpa Subscription ID; spec mengenalinya dari status Waiting for Approval pada Client `Optik Cahaya`.
  - TC-AC-CS-90 menyebut role Delete-Only (Distributor) sebagai aktor; akun `Siti Rahmawati` (#7) ada di Tabel Data Uji Pre-setup tanpa disebut di LK TC.
  - TC-AC-CS-87 mengubah Duration `1` menjadi `2` tanpa menyebut Start Date, dan TC tidak menyebut Estimated Cost; spec tidak mengasersi keduanya.
