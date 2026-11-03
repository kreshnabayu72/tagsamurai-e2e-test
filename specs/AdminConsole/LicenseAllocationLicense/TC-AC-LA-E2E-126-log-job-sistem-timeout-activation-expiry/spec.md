---
id: TC-AC-LA-E2E-126-log-job-sistem-timeout-activation-expiry
title: "Log Job Sistem: Timeout Auto-Cancel, Auto-Expire, dan Auto-Activate"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-LA-395
  - TC-AC-LA-396
  - TC-AC-LA-398
  - TC-AC-LA-406
  - TC-AC-LA-407
coverage:
  web: automated
---

# Log Job Sistem: Timeout Auto-Cancel, Auto-Expire, dan Auto-Activate

## Prerequisites

- Mode: FE+BE
- Login di hook `before` spec ini sebagai Hendra Wijaya (pengamat log setelah job berjalan; job sistem berjalan tanpa aktor login); halaman dibuka hook `beforeEach` suite (tab Current), yang juga menjadi jaring pengaman `beforeunload` dan dialog `Unsaved Changes` (lihat `suite.md`). Flag Guided Tooltip diatur hook `before` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Akun yang dipakai:

| Akun | Pre-setup | Peran | Email | Env password |
|---|---|---|---|---|
| Hendra Wijaya | #1 | Total Control Principal (membuka log setelah job) | `totalControlLic_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.AC_LA_TC_PRINCIPAL_PASSWORD` |

  Email dan `{namaCompany}` dirujuk lewat `Fixture.license-allocation-license` (fixture belum ada; disediakan tim FE).
- Data Pre-setup: Client PT Sejahtera (Pre-setup #19), Toko Serba Ada (Pre-setup #21; term Pending `SUBS-20260819-00001`, 1 Jan 2027 sampai 31 Dec 2027), Bengkel Cahaya Motor (Pre-setup #23; FAMS Professional Paid Active, End Date 31 Dec 2026), kantong wallet Distributor PT Maju Bersama saldo $10,000.00 (Pre-setup #33), Product Price (Pre-setup #34), Approval Timeout 3 day(s) (Pre-setup #40), Require Approval for Allocation ON (Pre-setup #38).
- Data Dinamis (seed milik spec ini, dibuat lewat seeding backend di hook `before`; tidak memakai baris Pre-setup #41, #46, dan #47 bersama):
  - `{idTimeout}`: alokasi `Waiting for Approval` Concurrent User +5 ke `SUBS-20260101-A1B2C` PT Sejahtera, requester Dewi Anggraini (Pre-setup #4), Cost $150.00 di-Reserve (bentuk Pre-setup #41);
  - `{idActivate}`: alokasi `Completed` berstatus lisensi `Pending` Concurrent User +10 ke term Pending `SUBS-20260819-00001` Toko Serba Ada, requester Dewi Anggraini, Cost $3,650.00 di-Reserve (bentuk Pre-setup #46);
  - `{idExpire}`: alokasi `Active` Concurrent User +10 ke FAMS Professional Bengkel Cahaya Motor (End Date 31 Dec 2026), requester Dewi Anggraini (bentuk Pre-setup #47).
- Kemampuan teknis (disediakan tim FE/BE): seeding alokasi dan pembersihannya; fixture waktu untuk jam server dan jam browser dengan nilai absolut; kueri fixture status job untuk menunggu satu siklus job; kemampuan membaca jumlah entri System Log Detail User `Dewi Anggraini` (`{nSysLog}`), dicatat sebelum jam digeser (S-12).
- State global: jam server dan jam browser diatur ke `1 Jan 2027 00:01` (zona waktu Plan Owner) satu kali untuk ketiga job: Timeout Auto-Cancel (jauh melewati SLA 3 hari sejak waktu terbit seed), Activation Transition (Start Date term Pending 1 Jan 2027 00:00 ditambah 1 menit), dan Expiry Transition (End Date 31 Dec 2026 berakhir 1 Jan 2027 00:00 ditambah 1 menit). Margin 1 menit terhadap batas Activation dan Expiry dihitung dari Start Date term seed. Jam dipulihkan sebelum Hendra Wijaya membuka Changelog, System Log, atau Activity Log (S-09); hook `after` memulihkan jam sebagai cadangan. Job yang berjalan juga memproses alokasi lain yang memenuhi syarat; data Pre-setup yang terpengaruh dipulihkan baseline automation. Log bercap waktu masa depan dicari berdasarkan Allocation ID, bukan posisi teratas (S-12).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### Menjalankan job sistem

1. Catat jumlah entri System Log `Dewi Anggraini` sebagai `{nSysLog}`
2. Atur jam server dan jam browser ke `1 Jan 2027 00:01` (nilai absolut, zona waktu Plan Owner)
3. Tunggu satu siklus job hingga kueri fixture status job menyatakan Timeout Auto-Cancel, Activation Transition, dan Expiry Transition selesai (batas tunggu 2 menit)
4. Pulihkan jam server dan jam browser ke waktu nyata

### Changelog dan Activity Log (TC-AC-LA-395, TC-AC-LA-396, TC-AC-LA-398)

5. Klik ikon `Changelog` pada List
6. Ketik Search `{idTimeout}`, tekan Enter
7. Verifikasi Changelog memuat entri Action `Timeout Auto-Cancel`, Status `Waiting for Approval` ke `Canceled`, Modified By `System`
8. Ganti isi kotak search dengan `{idExpire}`, tekan Enter
9. Verifikasi Changelog memuat entri Action `Auto-Expire`, Status `Active` ke `Expired`, Modified By `System`
10. Ganti isi kotak search dengan `{idActivate}`, tekan Enter
11. Verifikasi Changelog memuat entri Action `Auto-Activate`, Status `Pending` ke `Active`, Modified By `System`
12. Tutup modal Changelog
13. Buka Activity Log Admin Console
14. Ketik Search `{idTimeout}`, tekan Enter
15. Verifikasi Activity Log memuat entri Action `Timeout Auto-Cancel`, Status `Waiting for Approval` ke `Canceled`, Modified By `System`
16. Ganti isi kotak search dengan `{idExpire}`, tekan Enter
17. Verifikasi Activity Log memuat entri Action `Auto-Expire`, Status `Active` ke `Expired`, Modified By `System`
18. Ganti isi kotak search dengan `{idActivate}`, tekan Enter
19. Verifikasi Activity Log memuat entri Action `Auto-Activate`, Status `Pending` ke `Active`, Modified By `System`

### System Log tanpa entri job (TC-AC-LA-395 butir c, TC-AC-LA-396 butir b, TC-AC-LA-398 butir b)

20. Buka Detail User `Dewi Anggraini` > tab System Log
21. Verifikasi jumlah entri System Log `Dewi Anggraini` sama dengan `{nSysLog}` (tidak ada entri untuk Timeout Auto-Cancel, Auto-Expire, dan Auto-Activate)

### Allocation Log Allocation activated (TC-AC-LA-407)

22. Buka Allocation > License Allocation (tab Current)
23. Ketik Search `{idActivate}`, tekan Enter
24. Klik row action `Allocation Log` pada baris `{idActivate}`
25. Verifikasi judul entri `Allocation activated` tanpa `by [PIC]`
26. Verifikasi entri tanpa Description
27. Verifikasi entri memuat Date & Time sesuai General Settings
28. Verifikasi baris judul berupa teks biasa, bukan badge
29. Tutup modal Allocation Log

### Allocation Log Allocation auto-canceled (TC-AC-LA-406)

30. Klik tab `History`
31. Ketik Search `{idTimeout}`, tekan Enter
32. Klik row action `Allocation Log` pada baris `{idTimeout}`
33. Verifikasi judul entri `Allocation auto-canceled` tanpa `by [PIC]`
34. Verifikasi Description entri `Reason: Approval timeout`
35. Verifikasi entri memuat Date & Time sesuai General Settings
36. Verifikasi baris judul berupa teks biasa, bukan badge
37. Tutup modal Allocation Log

## Notes

- P-1: langkah 21 adalah asersi absence System Log untuk TC-AC-LA-395 butir c, TC-AC-LA-396 butir b, dan TC-AC-LA-398 butir b. Spec absence tidak memuat TC ini, dan ketiga job berjalan sekali pada state berat (jam server digeser, tiga record seed dengan Reserve wallet) sehingga asersi ditulis di sini dengan baseline agregat `{nSysLog}` (langkah 1); pemicu job tidak menyentuh entitas yang diamati, sehingga anchor berupa jumlah total sebelum dan sesudah (8b.2).
- Penggabungan job: satu pergeseran jam dan satu siklus job melayani ketiga record seed; TC-AC-LA-395 dan TC-AC-LA-406 memakai record `{idTimeout}` yang sama, dan TC-AC-LA-398 dan TC-AC-LA-407 memakai record `{idActivate}` yang sama. Alasan: ketiganya bergantung state jam yang sama dan hook membangunnya satu kali.
- Alasan di atas sekitar 35 langkah: seluruh blok satu kelas harness (job sistem dan pergeseran jam) dan topik yang sama (pencatatan log job), dan berdiri sendiri pada record seed masing-masing. Blok baca-log berpola (buka surface, cari entri, `Verifikasi` kolom log) tidak dihitung pada ambang smell; langkah aksi hanya 4.
- Langkah penghubung (S-03, R-16): langkah 2 dan 4 (mengatur dan memulihkan jam), langkah 3 (menunggu siklus job lewat kueri fixture status job, bukan tunggu waktu nyata), langkah 6, 8, 10, 14, 16, 18, 23, dan 31 (Search entri atau baris berdasarkan Allocation ID), langkah 12, 29, dan 37 (menutup modal), langkah 22 (kembali ke List), langkah 30 (pindah tab History).
- Pembagian TC lintas spec: TC-AC-LA-408, 412, 525, 526, dan 437 (event Expired, entri Allocation Log tanpa PIC, dan notifikasi Timeout) ada di spec 127.
- Temuan untuk QA:
  - TC-AC-LA-395, 396, dan 398 ber-Precondition "Tidak ada aktor login: job terjadwal sistem" dan tidak menyebut akun yang membuka Changelog, Activity Log, dan System Log; spec memakai Hendra Wijaya (Pre-setup #1) seperti TC-AC-LA-406 dan TC-AC-LA-407.
  - TC-AC-LA-396 dan TC-AC-LA-398 menyebut "System Log" tanpa menyebut pengguna; spec memakai System Log requester Dewi Anggraini seperti TC-AC-LA-395.
  - TC-AC-LA-395 menyebut "Geser waktu server melewati SLA" tanpa nilai absolut; spec memakai `1 Jan 2027 00:01` sehingga satu pergeseran jam melayani ketiga job.
  - Pre-setup #41, #46, dan #47 tidak menyebut requester akun; spec memakai Dewi Anggraini sesuai definisi seed ("requester `Dewi A`").
  - Job juga memproses alokasi Pre-setup lain yang memenuhi syarat Expiry dan Activation; pemulihannya bergantung baseline automation.
