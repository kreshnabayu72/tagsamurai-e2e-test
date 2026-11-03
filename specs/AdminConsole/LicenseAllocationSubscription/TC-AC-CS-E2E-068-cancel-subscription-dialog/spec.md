---
id: TC-AC-CS-E2E-068-cancel-subscription-dialog
title: "Cancel Subscription: Dialog"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-CS-259
  - TC-AC-CS-261
  - TC-AC-CS-260
  - TC-AC-CS-269
  - TC-AC-CS-560
coverage:
  web: automated
---

# Cancel Subscription: Dialog

## Prerequisites

- Mode: FE+BE.
- Akun aktor awal (login di hook `before`): Total Control Principal PT ABC, Hendra Wijaya (Pre-setup #1), `totalControlSub_automated_{namaCompany}@qwertysystem.net` (dirujuk lewat `Fixture.license-allocation-subscription`, belum ada, disediakan tim FE; kredensial `Spectra.env.AC_SUB_TC_PASSWORD`, nama didaftarkan di `executionConfig.environmentVariables` dan `.env.example`).
- Akun berikutnya (ganti akun eksplisit di Test Steps): capability Create saja Distributor PT Maju Bersama, Fajar Nugroho (Pre-setup #6), `createOnlySub_automated_{namaCompany}@qwertysystem.net` (dirujuk lewat `Fixture.license-allocation-subscription`, belum ada, disediakan tim FE; kredensial `Spectra.env.AC_SUB_CREATE_PASSWORD`, nama didaftarkan di `executionConfig.environmentVariables` dan `.env.example`).
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Allocation > Client Subscription, tab Current). Hook `after` mengembalikan sesi ke akun default suite (Total Control Principal, Pre-setup #1).
- Hook suite yang dirujuk spec ini dan dinyatakan sekali di `suite.md`: flag Guided Tooltip `guided_tooltip_seen_ac-license-allocation-subscription` disetel `seen` di hook `before` dan dipulihkan di hook `after`, sesi API aktor untuk pelaku kedua dan aksi pemicu, serta fixture backend pemulihan state Pre-setup.
- Suite serial: `parallel: false` (lihat `suite.md`).
- Data Pre-setup: `SUBS-20260101-00001` Client PT Sejahtera FAMS Professional Active (01/01/26 sampai 31/12/26, Plan Owner PT Maju Bersama (Distributor)) tanpa successor (#61); predecessor `SUBS-20250901-00001` Client Toko Serba Ada FAMS Professional Active (#68) dengan successor `SUBS-20260819-00003` Waiting for Approval (#67); Baris Active `SUBS-20250815-00001` (#69) dan Trial Active `SUBS-20260810-00001` (#60); `SUBS-20260819-00001` Waiting for Approval milik `Fajar Nugroho` (#49, #6); tanggal acuan uji `19/08/26`.
- Data Dinamis: tidak ada; semua dialog ditutup tanpa konfirmasi sehingga data tidak berubah. Form Convert yang dirty ditutup dengan `[Leave]`.
- Kemampuan teknis (disediakan tim FE/BE): fixture waktu: jam server dan jam browser diatur absolut ke tanggal acuan `19/08/26` di hook `before` (trial Active dan pengajuan Waiting for Approval bergantung pada hari ini), dipulihkan di hook `after`; membaca jumlah entri Changelog Client `PT Sejahtera` — FAMS; membaca saldo Reserved Wallet Main Pocket PT Maju Bersama.

## Test Steps

### TC-AC-CS-259: Screening dialog Cancel Subscription tanpa successor

1. Ketik Search `PT Sejahtera`, tekan Enter, lalu catat jumlah entri Changelog Client `PT Sejahtera` — FAMS sebagai baseline
2. Klik ikon `⋯` pada baris `SUBS-20260101-00001` lalu pilih `Cancel Subscription`
3. Verifikasi Header: Title "Cancel Subscription" (dialog danger)
4. Verifikasi Body: bullet "• PT Sejahtera — FAMS — Professional"
5. Verifikasi Body: "Canceling will move this subscription to Archive status. Users will lose access to this product."
6. Verifikasi Body: penutup "This action cannot be undone. Are you sure you want to cancel it?"
7. Verifikasi Body: baris "Your pending renewal will also be canceled." tidak ada
8. Verifikasi Footer: tombol `[Go Back]` dan `[Cancel Subscription]` (danger)

### TC-AC-CS-261: Go Back pada dialog Cancel Subscription tidak mengubah term

9. Klik `[Go Back]`
10. Verifikasi dialog tertutup tanpa toast
11. Verifikasi baris `SUBS-20260101-00001` tetap Active di tab `Current`
12. Verifikasi jumlah entri Changelog Client `PT Sejahtera` — FAMS sama dengan baseline

### TC-AC-CS-260: Dialog Cancel Subscription memuat baris successor pending

13. Ganti isi kotak search dengan `Toko Serba Ada`, tekan Enter, klik ikon `⋯` pada baris `SUBS-20250901-00001` lalu pilih `Cancel Subscription`
14. Verifikasi dialog memuat baris tambahan "Your pending renewal will also be canceled."
15. Verifikasi bullet "• Toko Serba Ada — FAMS — Professional" dan penutup "This action cannot be undone. Are you sure you want to cancel it?"
16. Klik `[Go Back]`

### TC-AC-CS-269: Baris Trial tidak menawarkan Cancel Subscription

17. Ganti isi kotak search dengan `PT Sejahtera`, tekan Enter, lalu klik ikon `⋯` pada baris trial Active `SUBS-20260810-00001`
18. Verifikasi menu hanya berisi Detail, Subscription Log, dan Convert
19. Verifikasi Cancel Subscription dan Renew tidak ada pada baris Trial

### TC-AC-CS-560: Klik backdrop dan Esc pada dialog konfirmasi Cancel Subscription, Convert Trial, dan Cancel Request

20. Tutup menu, ganti isi kotak search dengan `PT Sejahtera`, tekan Enter, klik ikon `⋯` pada baris `SUBS-20260101-00001` lalu pilih `Cancel Subscription`, kemudian klik area gelap di luar dialog
21. Verifikasi klik area gelap tidak menutup dialog Cancel Subscription
22. Tekan `Esc`
23. Verifikasi `Esc` menutup dialog seperti `[Go Back]`, baris `SUBS-20260101-00001` tetap Active, tanpa toast dan tanpa log baru
24. Klik ikon `⋯` pada baris Trial Active lalu pilih `Convert`, pilih Plan `Enterprise`, isi Duration `1` dan klik `[Submit]`, kemudian klik area gelap di luar dialog
25. Verifikasi klik area gelap tidak menutup dialog Convert Trial
26. Tekan `Esc`
27. Verifikasi `Esc` menutup dialog dan form Convert tetap terbuka, trial tetap Active
28. Klik `[✕]`, verifikasi dialog Unsaved Changes, lalu klik `[Leave]`
29. Ganti akun: Logout lalu login sebagai Create-Only Distributor (`Fajar Nugroho`)
30. Buka menu Allocation > Client Subscription
31. Ketik Search `SUBS-20260819-00001`, tekan Enter, lalu catat saldo Reserved Wallet Main Pocket PT Maju Bersama sebagai baseline
32. Klik ikon `⋯` pada baris `SUBS-20260819-00001` lalu pilih `Cancel Request`, kemudian klik area gelap di luar dialog
33. Verifikasi klik area gelap tidak menutup dialog Cancel Request
34. Tekan `Esc`
35. Verifikasi `Esc` menutup dialog seperti `[Go Back]` dan baris tetap Waiting for Approval
36. Verifikasi saldo Reserved Wallet Main Pocket PT Maju Bersama sama dengan baseline (Reserve tidak dilepas)

## Notes

- Urutan menyimpang dari urutan TC sumber (S-10): TC-AC-CS-261 langsung sesudah TC-AC-CS-259 pada dialog yang sama; TC-AC-CS-260 setelahnya.
- Langkah penghubung (S-03): Search untuk menemukan baris target (R-16); menu row action ditutup; `✕`, dialog `Unsaved Changes`, dan `[Leave]` menutup form dirty (S-08, S-09); ganti akun eksplisit (S-07) diikuti `Buka menu Allocation > Client Subscription` sebelum Search (S-14); Search pada kotak terisi ditulis "ganti isi kotak search dengan" (8b.9).
- Alasan melewati sekitar 35 langkah bila dihitung penuh: semua blok satu topik (dialog konfirmasi row action) tanpa kelas harness lain dan tanpa aksi yang mengubah data.
- Temuan untuk QA: (1) TC-AC-CS-560 langkah 3 menyebut Reserve tidak dilepas tanpa layar pengamatan dan tanpa nilai saldo; spec mencatat baseline Reserved Wallet sebelum dialog dan mengasersi sama dengan baseline lewat kemampuan baca Wallet (disediakan tim FE/BE, tercantum di Prerequisites), serta status baris Waiting for Approval. (2) TC-AC-CS-560 menyebut Convert di Trial Active `SUBS-20260810-00001` dengan Plan `Enterprise` tanpa menyebut ID Client; spec memakai Client PT Sejahtera Pre-setup #60.
