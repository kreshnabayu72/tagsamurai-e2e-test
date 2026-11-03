---
id: TC-AC-ACTS-E2E-110-lintas-modul-notifikasi-permintaan-hasil-keputusan-dan-gagal-kirim
title: "Lintas Modul: Notifikasi Permintaan Approval ke Pool, Hasil Keputusan ke Requester, Auto-Read, dan Notifikasi Gagal Terkirim Tidak Menggagalkan Approve"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACTS-688
  - TC-AC-ACTS-689
  - TC-AC-ACTS-690
  - TC-AC-ACTS-813
coverage:
  web: automated
---

# Lintas Modul: Notifikasi Permintaan Approval ke Pool, Hasil Keputusan ke Requester, Auto-Read, dan Notifikasi Gagal Terkirim Tidak Menggagalkan Approve

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Distributor Toggle ON (Local Registration aktif; jalur approval normal tanpa bypass E2a) `distributorOn_automated_{namaCompany}@qwertysystem.net` (Pre-setup #9), password dari `Spectra.env.AC_DIST_ON_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control).
- Akun ganti di tengah spec: Total Control Principal `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net` (Pre-setup #1), password dari `Spectra.env.AC_TC_PASSWORD`. Pergantian akun ditulis sebagai langkah eksplisit.
- Akun ganti di tengah spec: Additional Approver tanpa capability `additionalApprover_automated_{namaCompany}@qwertysystem.net` (Pre-setup #4), password dari `Spectra.env.AC_AA_PASSWORD`. Pergantian akun ditulis sebagai langkah eksplisit.
- Halaman awal: halaman Add Stock SKU `GPS-TRACK-CORE-G3` (Import/Manual IMEI), dibuka dari Stock List lewat row action Add Stock pada SKU itu oleh hook `beforeEach` suite.
- Hook suite (flag Guided Tooltip, sesi API aktor, simulator reader, fixture BE, jam server dan jam browser, pemulihan state global) dinyatakan di `suite.md`; spec ini merujuknya dan tidak mengubahnya kecuali yang tertulis di Prerequisites ini.
- SKU `GPS-TRACK-CORE-G3` (Data Pre-setup #15). Requester TC-AC-ACTS-688 memakai Add Stock GPS Manual Entry IMEI `356938035643810` (unit existing Available; Data Dinamis #2, identifier tetap tidak dapat bersuffix `{runId}`; seeding idempotent dan pemulihan lewat fixture BE), sehingga notifikasi memuat `GPS — 356938035643810`. Subject Register Duplicate pending dari Distributor Toggle ON untuk TC-AC-ACTS-689 (dua Subject: satu Approve, satu Reject), TC-AC-ACTS-690 (satu Subject dengan notifikasi actionable pending di approver lain), dan TC-AC-ACTS-813 (satu Subject), disiapkan seeding fixture BE (disediakan tim FE/BE). Fixture `fixtures/tag-stock.json` belum ada dan dibuat di tahap script.
- Pool approver memuat Total Control dan Additional Approver (`additionalApprover`, Pre-setup #4). Kemampuan teknis disediakan tim FE/BE: kemampuan membuat pengiriman notifikasi hasil approval gagal (TC-AC-ACTS-813) beserta pelepasannya di hook `after`, dan kemampuan baca jumlah notifikasi (Total Control, Additional Approver, dan Distributor) dan Total Registered SKU sebagai baseline (S-12).
- Env var password akun aktor: `Spectra.env.AC_DIST_ON_PASSWORD`, `Spectra.env.AC_TC_PASSWORD`, `Spectra.env.AC_AA_PASSWORD`. Password tidak ditulis di spec atau fixture. Nama `AC_DIST_ON_PASSWORD`, `AC_AA_PASSWORD` adalah nama baru yang didaftarkan di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example` oleh pemilik repo e2e.
- Suite berjalan serial (`parallel: false`). Spec ini menyiapkan dan memulihkan datanya sendiri dan tidak bergantung pada hasil spec lain.

## Test Steps

### TC-AC-ACTS-688: Notifikasi permintaan approval dikirim ke pool tanpa requester

1. Catat baseline jumlah notifikasi Total Control, Additional Approver, dan Distributor (kemampuan baca)
2. Tambahkan IMEI existing `356938035643810` lewat Manual Entry
3. Klik `[Submit]`
4. Verifikasi toast "Success, 1 TAG has been sent for approval."
5. Ganti akun: klik Logout
6. Login sebagai Total Control (`totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`)
7. Buka Notification Center
8. Verifikasi notifikasi actionable baru muncul untuk Total Control (jumlah notifikasi bertambah terhadap baseline)
9. Verifikasi Title `Duplicate identifier needs your review`
10. Verifikasi Body `GPS — 356938035643810` terisi dengan jenis TAG dan identifier yang discan

### TC-AC-ACTS-689 (bagian Total Control): Notifikasi hasil keputusan dikirim ke requester

11. Buka Approvals > TAG Stock > Tab Active, klik `Review` pada Subject pertama, pilih Approve, klik `[Submit]`
12. Klik `Review` pada Subject kedua, pilih Reject, isi Approval Note `Duplicate hardware`, klik `[Submit]`
13. Tunggu aksi selesai (dialog Review tertutup)

### TC-AC-ACTS-813: Notifikasi gagal terkirim tidak menggagalkan Approve (dependency non-kritis)

14. Buat pengiriman notifikasi hasil approval gagal (fixture BE)
15. Catat Total Registered SKU `GPS-TRACK-CORE-G3` di TAG > Stock sebagai baseline
16. Buka Approvals > TAG Stock > Tab Active, klik `Review` pada Subject Register Duplicate pending
17. Pilih Approve, klik `[Submit]`
18. Verifikasi toast sukses "Success, duplicate TAG has been approved and registered as [TAG Code]."
19. Verifikasi tidak ada toast error terkait notifikasi
20. Lepas kegagalan pengiriman notifikasi (fixture BE)
21. Buka Approvals > Tab History
22. Verifikasi Subject masuk Tab History dengan Approval `Approved` dan TAG Code baru
23. Buka TAG > Stock
24. Verifikasi unit berstatus Available dan Total Registered SKU bertambah 1 terhadap baseline

### TC-AC-ACTS-690 (bagian Total Control): Notifikasi actionable approval otomatis ter-read setelah keputusan

25. Buka Approvals > TAG Stock > Tab Active, klik `Review` pada Subject yang notifikasi actionable-nya pending di approver lain, pilih Approve, klik `[Submit]`
26. Tunggu aksi selesai (dialog Review tertutup)
27. Ganti akun: klik Logout
28. Login sebagai Additional Approver (`additionalApprover_automated_{namaCompany}@qwertysystem.net`)
29. Buka Notification Center

### TC-AC-ACTS-688 (bagian Additional Approver): Notifikasi permintaan approval dikirim ke pool tanpa requester

30. Verifikasi notifikasi actionable baru muncul untuk Additional Approver (jumlah notifikasi bertambah terhadap baseline)

### TC-AC-ACTS-690 (bagian Additional Approver): Notifikasi actionable approval otomatis ter-read setelah keputusan

31. Verifikasi notifikasi terkait Subject yang diputuskan Total Control ter-read otomatis

### TC-AC-ACTS-689 (bagian Distributor): Notifikasi hasil keputusan dikirim ke requester

32. Ganti akun: klik Logout
33. Login sebagai Distributor Toggle ON (`distributorOn_automated_{namaCompany}@qwertysystem.net`)
34. Buka Notification Center
35. Verifikasi notifikasi hasil baru diterima entitas yang scan untuk kedua keputusan (jumlah notifikasi bertambah terhadap baseline)
36. Verifikasi notifikasi Approve dengan Title `Duplicate identifier approved` dan Body `Registered as [TAG Code]` (TAG Code baru)
37. Verifikasi notifikasi Reject dengan Title `Duplicate identifier rejected` dan Body `Duplicate hardware`

## Notes

- Mode: FE+BE. Spec ini melewati sekitar 35 langkah (37 langkah); alasan: semua blok satu pokok notifikasi lintas akun dan satu dataset Subject pending, dan tiap blok TC berdiri sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna; penggantian akun dituntut TC-AC-ACTS-688, TC-AC-ACTS-689, dan TC-AC-ACTS-690.
- Urutan langkah dikelompokkan per akun (Distributor Toggle ON, Total Control, Additional Approver, lalu Distributor Toggle ON) supaya penggantian akun sesedikit mungkin (S-07, S-10); karena itu TC-AC-ACTS-688, TC-AC-ACTS-689, dan TC-AC-ACTS-690 muncul lebih dari satu kali dengan label "bagian" (pembagian TC di dalam satu spec). Verifikasi tiap Expected tetap tepat setelah aksi yang dicek di akun masing-masing (R-03).
- Langkah penghubung tanpa Verifikasi (S-03): langkah ganti akun (langkah 5 dan 27), membuka layar baca, dan mencatat baseline (S-12), dan "Tunggu aksi selesai" sebelum Logout (bagian 8b butir 8). Langkah "Tunggu aksi selesai" ditambahkan sebelum pindah surface atau ganti akun sesudah aksi yang hasilnya tidak diasersi langsung (bagian 8b butir 8).
- Temuan untuk QA:
  - TC-AC-ACTS-688 menyebut "seluruh Total Control dan Additional Approver (kecuali requester)" tanpa jumlah akun; spec memeriksa Total Control uji dan Additional Approver (#4).
  - TC-AC-ACTS-690 menyebut "approver lain" tanpa akun; spec memakai Additional Approver (#4).
  - TC-AC-ACTS-689 menyebut "Subject kedua untuk skenario Reject" tanpa nilai; spec memakai `Duplicate hardware`.
