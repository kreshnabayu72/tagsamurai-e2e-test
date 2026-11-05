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
- Kemampuan teknis tambahan (disediakan tim FE/BE): kemampuan baca saldo kantong Wallet dan jumlah notifikasi Plan Owner untuk baseline (langkah 28 dan 29); seeding satu notifikasi Plan Owner PT Maju Bersama yang tidak terkait seed sehingga daftar notifikasi Plan Owner memuat sedikitnya satu notifikasi lain sebagai anchor asersi absence notifikasi (langkah 23 dan 40). Jendela tunggu 5 detik tanpa memuat ulang halaman (langkah 24 dan 41) adalah pilihan spec, bukan nilai TC atau PRD (bagian 6).
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
10. Buka Allocation > License Allocation, klik tab `Current`, ketik Search Allocation ID seed, tekan Enter, lalu klik row action `Allocation Log` pada baris seed
11. Verifikasi entri `Allocation activated` tampil tanpa Description
12. Verifikasi entri `Allocation activated` tanpa `by [PIC]`
13. Tutup modal Allocation Log
14. Buka Changelog, cari entri dengan Allocation ID seed
15. Verifikasi Action `Auto-Activate`, Status `Pending` ke `Active`, Modified By `System`
16. Tutup modal Changelog
17. Buka Activity Log, cari entri dengan Allocation ID seed
18. Verifikasi Action `Auto-Activate`, Status `Pending` ke `Active`, Modified By `System`
19. Buka System Log, ketik Search Allocation ID seed, tekan Enter
20. Verifikasi empty state `No results found` tampil pada System Log
21. Verifikasi tidak ada entri System Log untuk seed
22. Buka notifikasi Plan Owner PT Maju Bersama
23. Verifikasi daftar notifikasi Plan Owner memuat sedikitnya satu notifikasi lain (daftar termuat, anchor)
24. Tunggu 5 detik tanpa memuat ulang halaman
25. Verifikasi tidak ada notifikasi ke Plan Owner untuk seed

### TC-AC-LA-268: Activation ulang pada record Active adalah no-op

26. Buka Allocation > License Allocation, klik tab `Current`, ketik Search Allocation ID seed Active, tekan Enter, lalu buka Allocation Log seed Active dan catat jumlah entri sebagai baseline
27. Tutup modal Allocation Log
28. Buka Wallet, catat saldo Wallet sebagai baseline
29. Buka notifikasi Plan Owner PT Maju Bersama, catat jumlah notifikasi Plan Owner untuk seed sebagai baseline
30. Atur jam server dan jam browser maju dua siklus job, tunggu dua siklus job, lalu pulihkan jam
31. Buka Allocation > License Allocation, klik tab `Current`, ketik Search Allocation ID seed Active, tekan Enter
32. Verifikasi status seed tetap `Active`
33. Buka Wallet
34. Verifikasi saldo Wallet sama dengan baseline (tidak ada Capture ganda)
35. Buka Allocation > License Allocation, klik tab `Current`, ketik Search Allocation ID seed Active, tekan Enter, lalu buka Allocation Log seed Active
36. Verifikasi entri `Allocation activated` seed Active tampil pada Allocation Log (anchor)
37. Verifikasi jumlah entri Allocation Log seed sama dengan baseline
38. Tutup modal Allocation Log
39. Buka notifikasi Plan Owner PT Maju Bersama
40. Verifikasi daftar notifikasi Plan Owner memuat sedikitnya satu notifikasi lain (daftar termuat, anchor)
41. Tunggu 5 detik tanpa memuat ulang halaman
42. Verifikasi jumlah notifikasi Plan Owner untuk seed sama dengan baseline

## Notes

- Sumber: `admin-console/license-allocation-license/TestCases/tc-license-allocation-license.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): langkah 3 (memulihkan jam sebelum membuka log, S-09), 4, 10, 14, 17, 19, 22, 26 sampai 31 (membuka surface dan Search untuk menemukan baris target, R-16; baseline S-12; langkah 28 membuka Wallet dan langkah 29 membuka notifikasi Plan Owner sebelum mencatat baseline saldo dan jumlah notifikasi).
- Setelah pindah modul (Wallet, Subscription Detail), langkah 10, 26, 31, dan 35 membuka List, klik tab, lalu mengetik Search pada kotak yang kosong di halaman yang baru dimuat, tanpa `✕` (S-14, 8b butir 9).
- Langkah 16 (menutup modal Changelog sebelum membuka Activity Log, S-09), langkah 13, 27, dan 38 (menutup modal Allocation Log sebelum membuka surface lain, S-09), langkah 33, 35, dan 39 (membuka Wallet, List, atau notifikasi sebelum asersi pada surface itu, S-14), serta langkah 24 dan 41 (jendela tunggu 5 detik tanpa Verifikasi sebelum asersi absence notifikasi, bagian 6) adalah langkah penghubung. Anchor positif asersi absence: langkah 20 (empty state `No results found` pada System Log setelah Search Allocation ID, pola spec 022 dan 072) mendahului langkah 21; langkah 23 dan 40 (daftar notifikasi Plan Owner termuat dan memuat notifikasi lain) mendahului langkah 25 dan 42; langkah 36 (entri `Allocation activated` seed Active tampil pada Allocation Log yang sama) mendahului langkah 37 (jumlah entri sama dengan baseline).
- P-1: TC-AC-LA-268 memakai record yang diaktifkan blok TC-AC-LA-267 (Dependensi TC-AC-LA-267 di TC) sebagai state berat time-travel; asersi tidak ada entri log, Capture, dan notifikasi baru (langkah 21, 25, 34 sampai 42) berbaseline dan beranchor positif. TC-AC-LA-268 Precondition menyebut alokasi Active (Pre-setup #47); spec memakai record hasil blok 267.
- Spec melewati sekitar 35 langkah (42 langkah). Alasan pertahanan: kedua blok satu kelas harness (job Activation Transition) pada record seed yang sama (blok TC-AC-LA-268 bergantung pada record yang diaktifkan blok TC-AC-LA-267), dan langkah di atas 35 adalah langkah penghubung (menutup modal, membuka surface) serta anchor dan jendela tunggu asersi absence notifikasi (bagian 6); blok baca-log tidak dihitung menurut bagian 3.
- Temuan untuk QA:
  - TC-AC-LA-267 dan TC-AC-LA-268 menyebut "Tidak ada aktor login: job terjadwal sistem" dan tidak menyebut akun pengamat; akun pengamat disediakan tim FE.
  - TC-AC-LA-267 Expected a ("kuota ledger term menjadi efektif") tidak menyebut cara pengamatan; spec memakai Subscription Detail > License Quota (modul pemilik di luar modul ini).
  - TC-AC-LA-267 Expected e ("Tidak ada notifikasi ke Plan Owner") tidak menyebut akun Plan Owner; spec memakai Plan Owner PT Maju Bersama yang disediakan tim FE.
  - TC-AC-LA-268 Langkah 1 ("dua siklus") tidak menyebut cara menunggu dua siklus selain menunggu; spec mengikuti fixture waktu.
