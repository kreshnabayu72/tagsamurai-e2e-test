---
id: TC-AC-LA-E2E-065-approve-snapshot-harga-app-station-storage
title: "Approve: Term Pending Menjadi Active, Snapshot Harga, Asset Control App, Station, dan Storage"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-LA-244
  - TC-AC-LA-245
  - TC-AC-LA-246
  - TC-AC-LA-247
coverage:
  web: automated
---

# Approve: Term Pending Menjadi Active, Snapshot Harga, Asset Control App, Station, dan Storage

## Prerequisites

- Mode: FE+BE
- Login di hook `before` spec ini sebagai Fajar Nugroho (Pre-setup #10, Total Control Distributor PT Maju Bersama); halaman License Allocation dibuka hook `beforeEach` suite (tab Current), dan spec ini berpindah ke Approvals sebagai langkah pertama.
- Akun: `totalControlDistLic_automated_{namaCompany}@qwertysystem.net`, password lewat `Spectra.env.AC_LA_TC_DIST_PASSWORD`. Email dan `{namaCompany}` dirujuk lewat `Fixture.license-allocation-license` (fixture belum ada; disediakan tim FE).
- Data Pre-setup: PT Sejahtera (Pre-setup #19), Toko Serba Ada (Pre-setup #21; term Pending `SUBS-20260819-00001`), CV Mitra Sejati (Pre-setup #22), Klinik Harapan Bunda (Pre-setup #24), kantong wallet Distributor PT Maju Bersama saldo $10,000.00 (Pre-setup #33), Product Price (Pre-setup #34: Concurrent User $365, Asset Control App flat $150, Asset Control Station $50.00 per Station), Require Approval ON (Pre-setup #38).
- Data Dinamis (seed milik spec ini, dibuat lewat seeding backend di hook `before` oleh requester Dewi Anggraini, Pre-setup #4; tidak memakai baris Pre-setup #41, #44, #45, dan #81 bersama), semuanya `Waiting for Approval`:
  - `{idTerm}`: Concurrent User +10 ke term Pending `SUBS-20260819-00001` Toko Serba Ada, Cost $3,650.00 di-Reserve (bentuk Pre-setup #81);
  - `{idHarga}`: Concurrent User +5 ke `SUBS-20260101-A1B2C` PT Sejahtera, Cost $150.00 di-Reserve (bentuk Pre-setup #41);
  - `{idApp}`: Asset Control App ke `SUBS-20260105-K2L3M` CV Mitra Sejati (bentuk Pre-setup #44), pada Subscription yang belum punya Asset Control App Active atau Pending;
  - `{idStation}`: Asset Control Station +2 `Client-wide` Klinik Harapan Bunda (bentuk Pre-setup #45).
- Kemampuan teknis (disediakan tim FE/BE; TC dan PRD tidak menyebut endpoint atau halamannya): seeding alokasi dan pembersihannya, fixture waktu (jam server dan jam browser ke 2 Jan 2027 sehingga term Pending menjadi Active), fixture harga (mengubah dan memulihkan Product Price Concurrent User), kemampuan membaca saldo kantong, status App pada Subscription, tanggal kedaluwarsa, entri Allocation Log record, jumlah entri Activity Log, dan notifikasi `License allocated`.
- State global: jam server dan jam browser diatur pada langkah 1 dan dipulihkan pada langkah 9; Product Price Concurrent User dinaikkan pada langkah 10 dan dipulihkan pada langkah 17; hook `after` memulihkan keduanya sebagai cadangan. Saldo kantong dan kuota dikembalikan oleh pembersihan record seed.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### Term Pending menjadi Active antara Submit dan Approve

1. Atur jam server dan jam browser ke 2 Jan 2027 sehingga term Pending `SUBS-20260819-00001` sudah Active (fixture waktu)
2. Buka Approvals > License Allocation
3. Klik `[Review]` pada alokasi `{idTerm}`
4. Pilih Approve
5. Klik Submit
6. Verifikasi status lisensi langsung `Active`
7. Verifikasi Reserve di-Capture saat Approve
8. Verifikasi nominal Capture `$3,650.00` sama dengan Cost awal alokasi `{idTerm}`, tanpa hitung ulang
9. Pulihkan jam server dan jam browser ke nilai awal (fixture waktu)

### Harga berubah antara Submit dan Approve

10. Naikkan harga Concurrent User dari `$365` menjadi `$730` (fixture harga)
11. Buka Approvals > License Allocation
12. Klik `[Review]` pada alokasi `{idHarga}`
13. Pilih Approve
14. Klik Submit
15. Verifikasi Capture sebesar snapshot `$150.00`, bukan harga baru
16. Verifikasi Cost pada entri Allocation Log `{idHarga}` tetap `$150.00 (Wallet)`
17. Pulihkan harga Concurrent User ke `$365` (fixture harga)

### Approve Asset Control App

18. Buka Approvals > License Allocation
19. Klik `[Review]` pada alokasi `{idApp}`
20. Pilih Approve
21. Klik Submit
22. Verifikasi status App pada Subscription menjadi `Active`
23. Verifikasi alokasi `Completed` berstatus `Active`
24. Verifikasi tanggal kedaluwarsa sama dengan End Date term Target

### Approve Asset Control Station

25. Buka Approvals > License Allocation
26. Klik `[Review]` pada alokasi `{idStation}`
27. Pilih Approve
28. Klik Submit
29. Verifikasi alokasi `Active` tanpa tanggal kedaluwarsa
30. Verifikasi tidak ada notifikasi `License allocated` (Station tidak punya Plan Owner)
31. Buka Activity Log
32. Verifikasi Activity Log hanya memuat entri approver (`Fajar N`) atas `{idStation}`, tanpa entri untuk Plan Owner

## Notes

- Langkah penghubung (S-03): langkah 2, 11, 18, 25, dan 31 (berpindah halaman), langkah 1, 9, 10, dan 17 (mengatur dan memulihkan jam serta harga). Langkah 9 memulihkan jam sebelum aksi lain supaya Last Updated dan log tidak bercap waktu masa depan (S-09, S-12).
- Langkah 30 diletakkan segera setelah Approve dan sebelum membuka Activity Log; status `Active` pada langkah 29 menjadi anchor positif bagi asersi ketiadaan notifikasi (8b butir 2 dan 11).
- Langkah 8 mengasersi butir b TC-AC-LA-244 (nominal Capture sama dengan Cost awal `$3,650.00` tanpa hitung ulang).
- Temuan untuk QA:
  - TC-AC-LA-244 tidak menyebut langkah yang membuat term Pending menjadi Active setelah jam digeser (Catatan TC menyatakan job Activation berjalan eventual dan Langkah Uji memuat langkah tunggu satu siklus job, tetapi TC ini tidak memuatnya); spec mengasumsikan term sudah Active setelah jam diatur.
  - TC-AC-LA-245 butir b ("Cost pada Allocation Log tetap `$150.00 (Wallet)`") tidak punya langkah membuka Allocation Log di LK; langkah 16 mengamatinya lewat kemampuan baca entri Allocation Log record `{idHarga}` dari tim FE/BE.
  - TC-AC-LA-246 butir a ("Status App pada Subscription") tidak menyebut halaman tempat status App dibaca, dan tanggal kedaluwarsa tidak disebut permukaannya; spec memakai kemampuan baca state BE dari tim FE/BE.
  - TC-AC-LA-246 memakai Pre-setup #44 untuk Subscription `SUBS-20260105-K2L3M` sedangkan Pre-setup #53 menyatakan Subscription yang sama sudah punya Asset Control App Active; spec memakai seed App pada Subscription tanpa App Active atau Pending.
  - TC-AC-LA-247 butir b menyebut Activity Log "hanya entri approver" tanpa menyebut cara memastikan tidak ada entri lain; langkah 32 mengasersi entri atas `{idStation}` hanya milik `Fajar N`. Akun pengamat notifikasi Plan Owner tidak disebut.
