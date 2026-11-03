---
id: TC-AC-LA-E2E-074-job-activation-transition
title: "Job Sistem Activation Transition"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-LA-267
  - TC-AC-LA-268
coverage:
  web: automated
---

# Job Sistem Activation Transition

## Prerequisites

- Mode: FE+BE.
- Akun pengamat: disediakan tim FE. Email akun ini tidak tertulis di Pre-setup TC (lihat Temuan untuk QA); akun harus dapat membuka List, Allocation Log, Wallet, Changelog, Activity Log, System Log, dan notifikasi. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Hook suite: `beforeEach` suite menjadi jaring pengaman S-09 dan flag Guided Tooltip diset `seen`, sesuai `suite.md`.
- `Fixture.license-allocation-license` belum ada (disediakan tim FE): memuat identitas akun, nama Client, ID Subscription, dan harga.
- Data Pre-setup (hanya dibaca): Toko Serba Ada (#21) dengan term Pending `SUBS-20260819-00001` mulai 1 Jan 2027, kantong wallet (#33), Product Price (#34).
- Data Dinamis (seeding lewat API di hook `before`, milik spec ini, bentuknya sama dengan Pre-setup #46): satu alokasi `Completed` berstatus lisensi `Pending` Concurrent User +10 ke term Pending `SUBS-20260819-00001` Toko Serba Ada oleh `Dewi A` (Cost $3,650.00 di-Reserve). Allocation ID dibaca dari hasil seeding. Record ini menjadi `Active` oleh blok TC-AC-LA-267 dan dipakai blok TC-AC-LA-268 (dependensi TC-AC-LA-267).
- Kemampuan teknis (disediakan tim FE/BE): fixture waktu untuk mengatur jam server dan jam browser ke nilai absolut, menunggu satu siklus job. Jam dipulihkan sebelum membuka Activity Log, System Log, dan Changelog (S-09) dan di hook `after`. Penanda baseline entri log dicatat per Allocation ID seed (baseline nol sebelum aktivasi, S-12).
- State global yang diubah: jam server dan jam browser; dipulihkan di hook `after`. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AC-LA-267: Activation Transition Pending menjadi Active dengan Capture

1. Atur jam server dan jam browser ke 1 Jan 2027 (Start Date term)
2. Tunggu satu siklus job
3. Pulihkan jam server dan jam browser ke waktu nyata
4. Ketik Search Allocation ID seed Pending di tab Current, tekan Enter
5. Verifikasi status seed menjadi `Active`
6. Buka Subscription Detail > License Quota term `SUBS-20260819-00001`
7. Verifikasi kuota ledger term menjadi efektif
8. Buka Wallet
9. Verifikasi Reserve $3,650.00 di-Capture (Balance berkurang)
10. Buka Allocation > License Allocation tab Current, klik row action `Allocation Log` pada baris seed
11. Verifikasi entri `Allocation activated` tampil tanpa Description
12. Verifikasi entri `Allocation activated` tanpa `by [PIC]`
13. Buka Changelog, cari entri dengan Allocation ID seed
14. Verifikasi Action `Auto-Activate`, Status `Pending` ke `Active`, Modified By `System`
15. Buka Activity Log, cari entri dengan Allocation ID seed
16. Verifikasi Action `Auto-Activate`, Status `Pending` ke `Active`, Modified By `System`
17. Buka System Log, cari Allocation ID seed
18. Verifikasi tidak ada entri System Log untuk seed
19. Buka notifikasi Plan Owner PT Maju Bersama
20. Verifikasi tidak ada notifikasi ke Plan Owner untuk seed

### TC-AC-LA-268: Activation ulang pada record Active adalah no-op

21. Buka Allocation Log seed Active dan catat jumlah entri sebagai baseline
22. Catat jumlah notifikasi Plan Owner untuk seed sebagai baseline dan saldo Wallet sebagai baseline
23. Atur jam server dan jam browser maju dua siklus job, tunggu dua siklus job, lalu pulihkan jam
24. Buka Allocation Log seed Active, Wallet, dan notifikasi
25. Verifikasi status seed tetap `Active`
26. Verifikasi saldo Wallet sama dengan baseline (tidak ada Capture ganda)
27. Verifikasi jumlah entri Allocation Log seed sama dengan baseline (anchor: entri `Allocation activated` tampil)
28. Verifikasi jumlah notifikasi Plan Owner untuk seed sama dengan baseline

## Notes

- Sumber: `admin-console/license-allocation-license/TestCases/tc-license-allocation-license.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): langkah 3 (memulihkan jam sebelum membuka log, S-09), 4, 10, 13, 15, 17, 19, 21 sampai 24 (membuka surface dan Search untuk menemukan baris target, R-16; baseline S-12).
- P-1: TC-AC-LA-268 memakai record yang diaktifkan blok TC-AC-LA-267 (Dependensi TC-AC-LA-267 di TC) sebagai state berat time-travel; asersi tidak ada entri log, Capture, dan notifikasi baru (langkah 18, 20, 26 sampai 28) berbaseline dan beranchor positif. TC-AC-LA-268 Precondition menyebut alokasi Active (Pre-setup #47); spec memakai record hasil blok 267.
- Temuan untuk QA:
  - TC-AC-LA-267 dan TC-AC-LA-268 menyebut "Tidak ada aktor login: job terjadwal sistem" dan tidak menyebut akun pengamat; akun pengamat disediakan tim FE.
  - TC-AC-LA-267 Expected a ("kuota ledger term menjadi efektif") tidak menyebut cara pengamatan; spec memakai Subscription Detail > License Quota (modul pemilik di luar modul ini).
  - TC-AC-LA-267 Expected e ("Tidak ada notifikasi ke Plan Owner") tidak menyebut akun Plan Owner; spec memakai Plan Owner PT Maju Bersama yang disediakan tim FE.
  - TC-AC-LA-268 Langkah 1 ("dua siklus") tidak menyebut cara menunggu dua siklus selain menunggu; spec mengikuti fixture waktu.
