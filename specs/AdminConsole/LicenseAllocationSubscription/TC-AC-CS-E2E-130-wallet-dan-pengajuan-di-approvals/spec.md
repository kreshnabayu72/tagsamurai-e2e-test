---
id: TC-AC-CS-E2E-130-wallet-dan-pengajuan-di-approvals
title: "Wallet dan Pengajuan di Approvals"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-CS-477
  - TC-AC-CS-478
  - TC-AC-CS-482
coverage:
  web: automated
---

# Wallet dan Pengajuan di Approvals

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Distributor (Pre-setup #9) `totalControlDistSub_automated_{namaCompany}@qwertysystem.net` (`Eko Saputra`), password `Spectra.env.AC_SUB_DIST_TC_PASSWORD`; login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Pre-setup #1).
- Akun pemicu lewat sesi API (bukan sesi UI): Create-Only Distributor (Pre-setup #6) `createOnlySub_automated_{namaCompany}@qwertysystem.net` (`Fajar Nugroho`), password `Spectra.env.AC_SUB_CREATE_PASSWORD`.
- Email dan identitas data Pre-setup dirujuk lewat `Fixture.license-allocation-subscription` (belum ada; disediakan tim FE). Nama env var password adalah usulan: belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`, didaftarkan tim FE.
- Data: Distributor `PT Maju Bersama` dengan satu kantong Wallet `Main Pocket` saldo tersedia $25,000.00 (Pre-setup #20). Data seed milik spec, dibuat lewat API di hook `before` dan dibersihkan di hook `after` (S-06, S-12), bersuffix `+{runId}-130`:
  1. TC-AC-CS-477: pengajuan SAMS Growth Waiting for Approval ber-Reserve $3,000.00 pada Main Pocket (Data Dinamis #3), Client `Client Wallet Reject+{runId}-130`.
  2. TC-AC-CS-478: Client milik spec dengan Client `Client Wallet Cancel+{runId}-130` dengan term SAMS Growth Active ter-Capture $3,000.00 pada Main Pocket (Data Dinamis #1, Dependensi TC-AC-CS-143), dibuat oleh langkah 18 setelah saldo Main Pocket diatur ke $25,000.00.
  3. TC-AC-CS-482: pengajuan Add Subscription dari requester biasa `Fajar Nugroho` untuk Client `Client Wallet Approve+{runId}-130`, dibuat oleh langkah 32.
- State global yang diubah (suite serial): saldo kantong Main Pocket (#20, Balance/Reserved/Available), diatur dan dipulihkan ke $25,000.00 tanpa Reserved oleh fixture backend yang disediakan tim FE/BE di hook `before`, `after`, dan langkah 18 (S-06, pengecualian 2026-10-30); efeknya (transaksi Wallet dan entri audit trail) tercatat di spec ini.
- Kemampuan teknis (disediakan tim FE/BE): mengatur dan membaca saldo kantong Wallet (Pre-setup #20) lewat fixture; sesi API aktor; endpoint pembuatan data tidak tertulis di TC, PRD, atau LLD (S-13).
- Hook suite (lihat `suite.md`): `beforeEach` membuka Allocation > Client Subscription tab Current dan menjadi jaring pengaman S-09; flag Guided Tooltip diatur `seen`. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AC-CS-477: Wallet: Reserve saat submit request dan Release saat Reject

1. Buka Wallet > Main Pocket
2. Verifikasi Balance $25,000.00 tidak berubah
3. Verifikasi Reserved $3,000.00
4. Verifikasi Available $22,000.00
5. Buka Approvals > Client Subscription
6. Ketik Search `Client Wallet Reject+{runId}-130`, tekan Enter
7. Pilih pengajuan seed TC-AC-CS-477
8. Pilih radio Reject
9. Isi `Rejection Reason` dengan `Budget pengajuan belum disetujui`
10. Klik `[Submit Decision]`
11. Konfirmasi pada dialog Konfirmasi Reject
12. Tunggu aksi selesai (dialog/modal tertutup)
13. Muat ulang Wallet > Main Pocket
14. Verifikasi Reserved $0.00
15. Verifikasi Available $25,000.00
16. Verifikasi Balance $25,000.00 tidak pernah berkurang

### TC-AC-CS-478: Wallet: Capture saat term Active dan tanpa refund saat Cancel

17. Klik menu `Client Subscription` di sidebar
18. Atur saldo Main Pocket ke $25,000.00 lewat fixture, lalu picu lewat sesi API aktor `Eko Saputra`: Add Subscription SAMS Growth untuk Client seed TC-AC-CS-478 hingga term Active dan Capture $3,000.00 tersimpan
19. Buka Wallet > Main Pocket
20. Verifikasi Wallet memuat transaksi Capture $3,000.00 untuk term itu
21. Verifikasi Balance sudah berkurang $3,000.00 menjadi $22,000.00
22. Klik menu `Client Subscription` di sidebar
23. Ketik Search nama Client seed TC-AC-CS-478, tekan Enter
24. Klik ikon `⋯` pada term SAMS Client seed
25. Klik `Cancel Subscription`
26. Klik `[Cancel Subscription]` pada dialog konfirmasi
27. Tunggu aksi selesai (dialog/modal tertutup)
28. Buka Wallet > Main Pocket
29. Verifikasi Balance tidak bertambah kembali ($22,000.00)
30. Verifikasi tidak ada transaksi refund

### TC-AC-CS-482: Pengajuan muncul di Approvals dan berpindah ke History setelah diputuskan

31. Klik menu `Client Subscription` di sidebar
32. Picu lewat sesi API aktor `Fajar Nugroho`: ajukan Add Subscription untuk Client seed TC-AC-CS-482 hingga pengajuan Waiting for Approval tersimpan
33. Buka Approvals > Client Subscription, tab Active
34. Ketik Search `Client Wallet Approve+{runId}-130`, tekan Enter
35. Verifikasi baris pengajuan seed muncul di Tab Active dengan Type `Add Subscription`
36. Pilih pengajuan seed, pilih radio Approve, klik `[Submit Decision]`, konfirmasi dialog
37. Tunggu aksi selesai (dialog/modal tertutup)
38. Klik tab History
39. Verifikasi baris pengajuan pindah ke Tab History dengan Decision Approved
40. Klik menu `Client Subscription` di sidebar
41. Ketik Search Subscription ID pengajuan seed, tekan Enter
42. Verifikasi Subscription ID yang sama muncul di List

## Notes

- Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): langkah 17, 22, 31, 40 (pindah halaman), langkah 6, 23, 34, dan 41 (Search untuk menemukan baris target, R-16; Approvals diasumsikan punya Search, lihat Temuan untuk QA), langkah 13 (Muat ulang Wallet), langkah 12, 27, dan 37 (menunggu aksi konfirmasi selesai sebelum membaca Wallet atau berpindah tab, 8b.8).
- Spec ini melewati ~35 langkah (42). Alasan: satu topik (efek Wallet dan Approvals pada kantong Main Pocket yang sama) dengan state global bersama yang dibangun berurutan (`P-4`: hook suite memulihkan saldo Main Pocket sebelum spec, saldo awal tiap blok ditulis di Prerequisites dan langkah 18); pemecahan menambah login dan hook tanpa isolasi.
- Langkah 18 dan 32 adalah pemicu lewat sesi API (R-20, "hingga ... tersimpan"), bukan konteks UI kedua; `P-2` tidak dipakai. Langkah 26 tidak diikuti Verifikasi status Archive karena TC-AC-CS-478 menempatkan asersi pada Wallet; langkah 28 mengikuti aksi setelah Cancel selesai (term Archive tidak diasersi karena bukan Expected TC).
- Temuan untuk QA:
  - TC-AC-CS-482 langkah 2 ("Approve pengajuan") tidak menyebut kontrol Approve; spec memakai pola radio Approve, `[Submit Decision]`, dan dialog konfirmasi yang sama dengan TC-AC-CS-477. Teks dialog konfirmasi Approve tidak disebut TC.
  - TC-AC-CS-477 dan 478 menyebut Wallet > Main Pocket tanpa label menu dan jalur navigasi eksak; spec memakai label dari TC.
  - TC-AC-CS-478 Expected a menyebut Balance sudah berkurang $3,000.00 tanpa menyebut saldo awal; spec mengatur saldo awal $25,000.00 (Pre-setup #20).
  - TC-477 dan TC-482 tidak menyebut Search pada halaman Approvals; spec mencari pengajuan seed lewat nama Client seed bersuffix sebelum memilih baris.
  - TC-AC-CS-482 Expected b ("Subscription ID yang sama muncul di List") tidak menyebut tab List; spec memakai Search ID pada tab `Current`.
