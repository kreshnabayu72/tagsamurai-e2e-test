---
id: TC-AC-CS-E2E-069-cancel-subscription-efek-dan-alokasi
title: "Cancel Subscription: Efek dan Alokasi"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-CS-263
  - TC-AC-CS-264
  - TC-AC-CS-265
  - TC-AC-CS-262
coverage:
  web: automated
---

# Cancel Subscription: Efek dan Alokasi

## Prerequisites

- Mode: FE+BE.
- Akun aktor awal (login di hook `before`): Total Control Principal PT ABC, Hendra Wijaya (Pre-setup #1), `totalControlSub_automated_{namaCompany}@qwertysystem.net` (dirujuk lewat `Fixture.license-allocation-subscription`, belum ada, disediakan tim FE; kredensial `Spectra.env.AC_SUB_TC_PASSWORD`, nama didaftarkan di `executionConfig.environmentVariables` dan `.env.example`).
- Akun berikutnya (ganti akun eksplisit di Test Steps): Total Control Distributor PT Maju Bersama, Eko Saputra (Pre-setup #9), `totalControlDistSub_automated_{namaCompany}@qwertysystem.net` (dirujuk lewat `Fixture.license-allocation-subscription`, belum ada, disediakan tim FE; kredensial `Spectra.env.AC_SUB_DIST_TC_PASSWORD`, nama didaftarkan di `executionConfig.environmentVariables` dan `.env.example`).
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Allocation > Client Subscription, tab Current). Hook `after` mengembalikan sesi ke akun default suite (Total Control Principal, Pre-setup #1).
- Hook suite yang dirujuk spec ini dan dinyatakan sekali di `suite.md`: flag Guided Tooltip `guided_tooltip_seen_ac-license-allocation-subscription` disetel `seen` di hook `before` dan dipulihkan di hook `after`, sesi API aktor untuk pelaku kedua dan aksi pemicu, serta fixture backend pemulihan state Pre-setup.
- Suite serial: `parallel: false` (lihat `suite.md`).
- Data seed milik spec (dibuat lewat API di hook `before`, dihapus di hook `after`; Subscription ID dibaca lewat API seeding dan dirujuk di langkah sebagai nilai terbaca):
  - Client `Toko Serba Ada+{runId}-069` dengan predecessor `{idPred}` FAMS Professional Active (01/09/25 sampai 31/08/26, Plan Owner PT Maju Bersama (Distributor); padanan Pre-setup #68) dan successor Renewal `{idSucc}` FAMS Enterprise Waiting for Approval ber-Reserve (padanan #67).
  - Client `Toko Prima Sentosa+{runId}-069` (binaan langsung PT Maju Bersama) dengan term SAMS `{idPrima}` Professional Active (01/10/25 sampai 30/09/26, Plan Owner PT Maju Bersama (Distributor)) berkuota Concurrent User 20 (alokasi Active) pada ledger term dan alokasi Station per-client, serta successor Renewal SAMS Professional Pending (01/10/26 sampai 30/09/27) beralokasi Pending (padanan #116).
  - Client `PT Sejahtera A+{runId}-069` (untuk TC-AC-CS-265) dan Client `PT Sejahtera B+{runId}-069` (untuk TC-AC-CS-262), masing-masing dengan term FAMS Professional Active `{idSejA}` dan `{idSejB}` (01/01/26 sampai 31/12/26, Plan Owner PT Maju Bersama (Distributor)) tanpa successor, Capture $10,000.00 sudah dilakukan, alokasi aktif Concurrent User 20 (Used 8) dan Maintenance 2 (Used 1) (padanan #61 dan #76); dua Client terpisah menggantikan pemulihan term ke Active antar blok.
- Data Pre-setup yang tidak ditulis spec: Wallet `Main Pocket` PT Maju Bersama dengan saldo tersedia $25,000.00 (#20).
- Data Dinamis: term, successor, alokasi, dan entri audit trail turunan Cancel ikut dihapus bersama Client seed di hook `after`. Satu-satunya state global adalah saldo Wallet `Main Pocket` PT Maju Bersama; fixture backend (disediakan tim FE/BE) mengembalikannya ke nilai awal di hook `after` bila Reserve atau Capture seed mengubahnya, karena kantong Wallet bukan milik spec dan tidak dapat dibuat per spec.
- Jam: jam server dan jam browser diatur absolut ke tanggal acuan `19/08/26` (fixture waktu, disediakan tim FE/BE) agar term seed tetap berstatus Active dan tidak masuk Grace atau Expired pada rentang tanggal 2026; dipulihkan di hook `after`.
- Kemampuan teknis (disediakan tim FE/BE): membaca saldo Balance, Reserved, dan Available Wallet; membaca ledger alokasi lisensi term pada modul License Allocation; sesi API aktor untuk Cancel dari sesi lain; membaca jumlah entri Changelog.

## Test Steps

### TC-AC-CS-263: Cancel Subscription membatalkan successor pending dan melepas Reserve

1. Ketik Search `Toko Serba Ada+{runId}-069`, tekan Enter, lalu catat jumlah entri Changelog Client `Toko Serba Ada+{runId}-069` — FAMS dan saldo Reserved Main Pocket PT Maju Bersama sebagai baseline
2. Klik ikon `⋯` pada baris `{idPred}` lalu pilih `Cancel Subscription`
3. Klik `[Cancel Subscription]`
4. Tunggu aksi selesai (dialog Cancel Subscription tertutup)
5. Klik tab `History`, ganti isi kotak search dengan `Toko Serba Ada+{runId}-069`, tekan Enter
6. Verifikasi predecessor `{idPred}` berstatus Archive
7. Verifikasi successor `{idSucc}` berstatus Canceled
8. Verifikasi saldo Reserved Main Pocket PT Maju Bersama berkurang dibanding baseline (Reserve wallet successor dilepas penuh)
9. Verifikasi Reserve alokasi pada successor dilepas penuh
10. Buka modal Changelog Client `Toko Serba Ada+{runId}-069` — FAMS
11. Verifikasi entri baru Action `Cancel` untuk predecessor, Modified By `Hendra W`
12. Verifikasi entri baru Action `Cancel Request`, Old `Waiting for Approval`, New `Canceled` untuk successor, Modified By `Hendra W`

### TC-AC-CS-264: Cancel Subscription melepas alokasi Pending dan meng-expire alokasi Active tanpa menyentuh alokasi per-client

13. Tutup modal Changelog, klik tab `Current`
14. Ganti isi kotak search dengan `Toko Prima Sentosa+{runId}-069`, tekan Enter
15. Klik ikon `⋯` pada baris `{idPrima}` lalu pilih `Cancel Subscription`
16. Klik `[Cancel Subscription]`
17. Tunggu aksi selesai (dialog Cancel Subscription tertutup)
18. Buka License Allocation Client `Toko Prima Sentosa+{runId}-069`
19. Verifikasi alokasi Active pada ledger term berstatus expired tanpa refund
20. Verifikasi alokasi Pending pada ledger successor di-Release penuh dengan refund Reserve
21. Verifikasi alokasi per-client (Station dan Storage) tidak terpengaruh

### TC-AC-CS-265: Cancel Subscription ditolak saat term sudah bukan Active

22. Kembali ke Allocation > Client Subscription tab Current, ketik Search `PT Sejahtera A+{runId}-069`, tekan Enter
23. Klik ikon `⋯` pada baris `{idSejA}` lalu pilih `Cancel Subscription`
24. Cancel term itu lewat sesi API aktor hingga status Archive tersimpan, lalu klik `[Cancel Subscription]`
25. Verifikasi dialog blok Title "Cannot Cancel Subscription" dengan Body "• PT Sejahtera A+{runId}-069 — FAMS" dan "This subscription is no longer active."
26. Verifikasi tombol tunggal `[OK]`
27. Klik `[OK]`
28. Klik tab `History`, ganti isi kotak search dengan `PT Sejahtera A+{runId}-069`, tekan Enter
29. Verifikasi term `{idSejA}` tetap berstatus Archive hasil Cancel sesi API (data tidak berubah)

### TC-AC-CS-262: Cancel Subscription: term masuk Archive tanpa refund

30. Ganti akun: Logout lalu login sebagai Total Control Distributor (`Eko Saputra`), buka Wallet > Main Pocket PT Maju Bersama, lalu catat Balance, Reserved, dan Available sebagai baseline
31. Ganti akun: Logout lalu login sebagai Total Control Principal (`Hendra Wijaya`), buka Allocation > Client Subscription tab Current, ketik Search `PT Sejahtera B+{runId}-069`, tekan Enter, lalu catat jumlah entri Changelog Client `PT Sejahtera B+{runId}-069` — FAMS sebagai baseline
32. Klik ikon `⋯` pada baris `{idSejB}` lalu pilih `Cancel Subscription`
33. Klik `[Cancel Subscription]`
34. Verifikasi toast sukses "Success, subscription has been canceled."
35. Klik tab `History`, ganti isi kotak search dengan `PT Sejahtera B+{runId}-069`, tekan Enter
36. Verifikasi baris `{idSejB}` berstatus Archive di tab `History` dan skip Grace
37. Buka modal Changelog Client `PT Sejahtera B+{runId}-069` — FAMS
38. Verifikasi entri baru Action `Cancel`, Field `Status`, Old `Active`, New `Archive`
39. Tutup modal Changelog, buka Detail term, lalu buka ledger alokasi term di modul License Allocation
40. Verifikasi alokasi lisensi Active pada ledger term berstatus expired tanpa refund
41. Ganti akun: Logout lalu login sebagai Total Control Distributor (`Eko Saputra`) dan buka Wallet > Main Pocket PT Maju Bersama
42. Verifikasi Balance, Reserved, dan Available Main Pocket sama dengan baseline (tidak ada refund dan Wallet tidak dipanggil atas charge term ini)

## Notes

- Urutan menyimpang dari urutan TC sumber (S-10): TC-AC-CS-262 (ganti akun ke Distributor untuk Wallet) paling akhir supaya baseline Wallet tidak tergeser oleh pelepasan Reserve TC-AC-CS-263 dan TC-AC-CS-264.
- Pelaku Cancel dari sesi lain pada TC-AC-CS-265 memakai sesi API aktor (bukan konteks kedua); tidak memakai P-2.
- Langkah penghubung (S-03): Search untuk menemukan baris target (R-16); pindah tab `History` dan `Current` untuk baris Archive dan Canceled; tutup modal Changelog; `Tunggu aksi selesai` sesudah tiap `[Cancel Subscription]` yang disusul perpindahan tab atau halaman (8b.8); ganti akun eksplisit (S-07); log dicari berdasarkan Action dan Field, bukan posisi teratas (S-14).
- Spec ini 42 langkah, di atas smell 35 langkah. Alasan: semua blok satu topik (efek Cancel Subscription) pada data seed milik spec (term TC-AC-CS-265 dan TC-AC-CS-262 memakai Client seed terpisah), tanpa kelas harness lain.
- Temuan untuk QA: (1) TC-AC-CS-264 menyebut "daftar alokasi tampil" tanpa menyebut layar License Allocation; spec memakai kemampuan baca ledger alokasi. (2) TC-AC-CS-262 Post Condition b (Auto-Archive Client dievaluasi) tanpa langkah observasi sehingga tidak diasersi. (3) TC-AC-CS-263 menyebut Modified By "aktor"; spec memakai format `[First Name] [Last Initial]` (`Hendra W`).
