---
id: TC-AC-LA-E2E-133-konsumen-subscription-detail-quota-setelah-job
title: "Konsumen Subscription Detail: License Quota setelah Activation dan Expiry"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-LA-426
  - TC-AC-LA-491
coverage:
  web: automated
---

# Konsumen Subscription Detail: License Quota setelah Activation dan Expiry

## Prerequisites

- Mode: FE+BE
- Login di hook `before` spec ini sebagai akun pengamat Subscription Detail; akun itu tidak tertulis di Pre-setup TC dan disediakan tim FE (lihat Temuan untuk QA). Job sistem berjalan tanpa aktor login. Halaman dibuka hook `beforeEach` suite (tab Current), yang juga menjadi jaring pengaman `beforeunload` dan dialog `Unsaved Changes` (lihat `suite.md`); spec berpindah ke Subscription Detail sebagai langkah. Flag Guided Tooltip diatur hook `before` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Akun yang dipakai:

| Akun | Pre-setup | Peran | Email | Env password |
|---|---|---|---|---|
| Pengamat Subscription Detail | tidak tertulis di Pre-setup TC | dengan akses baca Subscription Detail Toko Serba Ada dan Bengkel Cahaya Motor | disediakan tim FE | disediakan tim FE |

- Data Pre-setup: Toko Serba Ada (Pre-setup #21; term Active `SUBS-20250201-J7K8L` dan term Pending `SUBS-20260819-00001`, 1 Jan 2027 sampai 31 Dec 2027), Bengkel Cahaya Motor (Pre-setup #23; FAMS Professional Paid Active, End Date 31 Dec 2026), kantong wallet Distributor PT Maju Bersama saldo $10,000.00 (Pre-setup #33), Product Price (Pre-setup #34).
- Data Dinamis (seed milik spec ini, dibuat lewat seeding backend di hook `before`; tidak memakai baris Pre-setup #46 dan #47 bersama):
  - `{idPendQ}`: alokasi `Completed` berstatus lisensi `Pending` Concurrent User +10 ke term Pending `SUBS-20260819-00001` Toko Serba Ada, requester Dewi Anggraini (Pre-setup #4), Cost $3,650.00 di-Reserve (bentuk Pre-setup #46);
  - `{idActiveQ}`: alokasi `Active` Concurrent User +10 ke FAMS Professional Bengkel Cahaya Motor (End Date 31 Dec 2026), requester Dewi Anggraini (bentuk Pre-setup #47).
- Kemampuan teknis (disediakan tim FE/BE): seeding alokasi dan pembersihannya; fixture waktu untuk jam server dan jam browser dengan nilai absolut; kueri fixture status job untuk menunggu satu siklus job.
- State global: jam server dan jam browser diatur ke `1 Jan 2027 00:01` (zona waktu Plan Owner; Start Date term Pending 1 Jan 2027 00:00 dan End Date 31 Dec 2026 berakhir 1 Jan 2027 00:00, ditambah 1 menit, dihitung dari tanggal term seed) selama pembacaan License Quota, lalu dipulihkan; hook `after` memulihkan jam sebagai cadangan. Job yang berjalan juga memproses alokasi lain yang memenuhi syarat; data Pre-setup yang terpengaruh dipulihkan baseline automation.
- Suite berjalan serial (`parallel: false`).

## Test Steps

1. Buka Subscription Detail `SUBS-20260819-00001` > License Quota
2. Catat total Concurrent User sebagai `{qToko0}`
3. Buka Subscription Detail term FAMS Professional Bengkel Cahaya Motor > License Quota
4. Catat total Concurrent User sebagai `{qBengkel0}`
5. Atur jam server dan jam browser ke `1 Jan 2027 00:01` (nilai absolut, zona waktu Plan Owner)
6. Tunggu satu siklus job hingga kueri fixture status job menyatakan Activation Transition dan Expiry Transition selesai (batas tunggu 2 menit)
7. Buka Subscription Detail `SUBS-20260819-00001` > License Quota
8. Verifikasi kuota Concurrent User term `SUBS-20260819-00001` efektif bertambah 10 terhadap `{qToko0}`
9. Buka Subscription Detail term FAMS Professional Bengkel Cahaya Motor > License Quota
10. Verifikasi kuota Concurrent User term itu berkurang 10 terhadap `{qBengkel0}` sebesar alokasi yang Expired
11. Pulihkan jam server dan jam browser ke waktu nyata

## Notes

- P-2: job sistem (Activation Transition dan Expiry Transition) hanya memicu kondisi yang diuji; objek asersi adalah License Quota di Subscription Detail. Satu pergeseran jam dan satu siklus job melayani kedua TC.
- Langkah penghubung (S-03): langkah 1 sampai 4 (membaca baseline kuota), langkah 5 dan 11 (mengatur dan memulihkan jam), langkah 6 (menunggu siklus job lewat kueri fixture status job).
- Temuan untuk QA:
  - TC-AC-LA-426 dan TC-AC-LA-491 ber-Precondition "Tidak ada aktor login: job terjadwal sistem" dan tidak menyebut akun yang membuka Subscription Detail; TC-AC-LA-491 juga tidak menyebut akun sama sekali. Spec memakai akun pengamat yang disediakan tim FE.
  - TC-AC-LA-426 dan TC-AC-LA-491 menyebut kuota "bertambah 10" dan "berkurang 10" tanpa nilai awal; spec membandingkan terhadap nilai yang dicatat sebelum job.
  - TC-AC-LA-491 menyebut "Geser waktu server ke 1 Jan 2027" tanpa jam; spec memakai `1 Jan 2027 00:01` seperti TC-AC-LA-526.
  - Spec tidak memulihkan jam sebelum membaca License Quota karena kuota efektif bergantung tanggal term; TC tidak menyebut apakah pembacaan memakai jam nyata atau jam geser.
