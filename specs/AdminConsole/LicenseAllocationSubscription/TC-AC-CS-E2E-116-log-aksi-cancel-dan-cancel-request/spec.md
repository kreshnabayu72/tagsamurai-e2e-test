---
id: TC-AC-CS-E2E-116-log-aksi-cancel-dan-cancel-request
title: "Log Aksi: Cancel dan Cancel Request"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-CS-451
  - TC-AC-CS-452
  - TC-AC-CS-614
  - TC-AC-CS-455
coverage:
  web: automated
---

# Log Aksi: Cancel dan Cancel Request

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Total Control Principal PT ABC (Pre-setup #1) `totalControlSub_automated_{namaCompany}@qwertysystem.net` (`Hendra Wijaya`), password `Spectra.env.AC_SUB_TC_PASSWORD`; login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Akun aktor berikutnya (ganti akun dengan langkah eksplisit): Create-Only (capability Create saja), Distributor PT Maju Bersama (Pre-setup #6) `createOnlySub_automated_{namaCompany}@qwertysystem.net` (`Fajar Nugroho`), password `Spectra.env.AC_SUB_CREATE_PASSWORD`; login pada langkah ganti akun, dan hook `after` mengembalikan sesi ke akun default suite (Pre-setup #1).
- Akun aktor berikutnya (ganti akun dengan langkah eksplisit): Group Manager scope Group Jawa, Distributor PT Maju Bersama (Pre-setup #5) `groupManagerSub_automated_{namaCompany}@qwertysystem.net` (`Dewi Anggraini`), password `Spectra.env.AC_SUB_GM_PASSWORD`; login pada langkah ganti akun, dan hook `after` mengembalikan sesi ke akun default suite (Pre-setup #1).
- Email dan identitas data Pre-setup dirujuk lewat `Fixture.license-allocation-subscription` (belum ada; disediakan tim FE). Nama env var password di atas didaftarkan di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example` oleh tim FE, sesuai `suite.md`.
- Suite berjalan serial (`parallel: false`). Hook `beforeEach` suite membuka Allocation > Client Subscription tab Current dan menjadi jaring pengaman S-09 (lihat `suite.md`); flag Guided Tooltip diatur hook suite (`seen`), sehingga walkthrough tidak muncul.
- Sesi API aktor: aksi pemicu (kolom Dependensi TC) dijalankan lewat login API akun aktor sesuai `suite.md`; kemampuan menulis lewat API, endpoint, dan payloadnya tidak tertulis di TC, PRD, atau LLD sehingga disediakan tim BE/FE (S-13). Sesi UI aktor tidak terpengaruh (bagian 5).
- Baseline S-12: jumlah entri Changelog, Activity Log, dan System Log per Client, Action, dan user pelaku dicatat di hook `before` lewat kemampuan membaca audit trail (disediakan tim FE/BE, bagian 8b butir 10) sebelum aksi pemicu pertama; Changelog, Activity Log, dan System Log adalah audit trail permanen sehingga asersi "entri baru" memakai selisih terhadap baseline itu dan entri dicari lewat Action, Client, dan email pelaku (bukan posisi teratas).
- Data seed milik spec, dibuat lewat sesi API aktor di hook `before` dan dibersihkan di hook `after` (S-06, S-12; bersuffix `+{runId}-116`). Spec tidak menulis ke baris Pre-setup bersama dan tidak memerlukan langkah pemulihan antar blok; entri audit trail (Changelog, Activity Log, System Log) yang dihasilkan aksi pemicu permanen dan dibaca lewat selisih terhadap baseline. Satu seed per blok:
  1. TC-AC-CS-451: Client `PT Sejahtera+{runId}-116` dengan term FAMS plan Professional status Active (01/01/26 sampai 31/12/26), Plan Owner PT Maju Bersama (Distributor) (bentuk Pre-setup #61).
  2. TC-AC-CS-452: Client `Apotek Sehat Sentosa A+{runId}-116` dengan pengajuan FAMS Waiting for Approval, Plan Owner PT Maju Bersama (Distributor), requester `Fajar N` (bentuk Pre-setup #49).
  3. TC-AC-CS-455: Client `PT Bintang Timur+{runId}-116` dengan pengajuan Trial FAMS Waiting for Approval, Plan Owner PT Maju Bersama (Distributor), requester `Fajar N` (bentuk Pre-setup #59).
  4. TC-AC-CS-614: Client `Apotek Sehat Sentosa B+{runId}-116` dengan term Pending SIEM, Plan Owner PT Maju Bersama (Distributor), diajukan Group Manager `Dewi A` (bentuk Pre-setup #90 dengan requester Group Manager).

## Test Steps

### TC-AC-CS-451: Log Cancel Subscription

1. Pemicu (sesi API): batalkan (Cancel Subscription) term Active `PT Sejahtera+{runId}-116 — FAMS` hingga perubahan tersimpan
2. Buka modal Changelog, ketik Search `PT Sejahtera+{runId}-116`, tekan Enter, dan cari entri Action `Cancel`
3. Verifikasi entri Changelog baru (selisih satu terhadap baseline): Action `Cancel`, Client — Product `PT Sejahtera+{runId}-116 — FAMS`, Field `Status`, Old Value `Active`, New Value `Archive`, Modified By `Hendra W`
4. Buka Admin Console > Activity Log, saring Object `Client Subscription`, dan cari entri yang sama
5. Verifikasi entri Activity Log `Client Subscription` baru: Name `PT Sejahtera+{runId}-116 — FAMS`, Action `Cancel`, Field `Status`, Old `Active`, New `Archive`, Modified By `Hendra W`
6. Buka Detail user Hendra W, tab System Log, dan cari entri yang sama
7. Verifikasi entri System Log Detail user Hendra W baru: Action `Cancel`, Object `Client Subscription`, Name `PT Sejahtera+{runId}-116 — FAMS`, Field `Status`, Old `Active`, New `Archive`
8. Ganti akun: klik Logout dari akun sebelumnya
9. Login sebagai `Fajar Nugroho` (`createOnlySub_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_SUB_CREATE_PASSWORD`)

### TC-AC-CS-452: Log Cancel Request

10. Pemicu (sesi API): batalkan pengajuan (Cancel Request) `Apotek Sehat Sentosa A+{runId}-116 — FAMS` sebagai requester hingga perubahan tersimpan
11. Buka menu Allocation > Client Subscription
12. Buka modal Changelog, ketik Search `Apotek Sehat Sentosa A+{runId}-116`, tekan Enter, dan cari entri Action `Cancel Request`
13. Verifikasi entri Changelog baru (selisih satu terhadap baseline): Action `Cancel Request`, Client — Product `Apotek Sehat Sentosa A+{runId}-116 — FAMS`, Field `Status`, Old Value `Waiting for Approval`, New Value `Canceled`, Modified By `Fajar N`
14. Buka Admin Console > Activity Log, saring Object `Client Subscription`, dan cari entri yang sama
15. Verifikasi entri Activity Log `Client Subscription` baru: Name `Apotek Sehat Sentosa A+{runId}-116 — FAMS`, Action `Cancel Request`, Field `Status`, Old `Waiting for Approval`, New `Canceled`, Modified By `Fajar N`
16. Buka Detail user Fajar N, tab System Log, dan cari entri yang sama
17. Verifikasi entri System Log Detail user Fajar N baru: Action `Cancel Request`, Object `Client Subscription`, Name `Apotek Sehat Sentosa A+{runId}-116 — FAMS`, Field `Status`, Old `Waiting for Approval`, New `Canceled`

### TC-AC-CS-455: Log Cancel Request Trial

18. Pemicu (sesi API): batalkan pengajuan Trial (Cancel Request) `PT Bintang Timur+{runId}-116` sebagai requester hingga perubahan tersimpan
19. Buka menu Allocation > Client Subscription
20. Buka modal Changelog, ketik Search `PT Bintang Timur+{runId}-116`, tekan Enter, dan cari entri Action `Cancel Request (Trial)`
21. Verifikasi entri Changelog baru (selisih satu terhadap baseline): Action `Cancel Request (Trial)`, Client — Product `PT Bintang Timur+{runId}-116` (varian Trial mencatat Client saja tanpa Product), Field `Status`, Old Value `Waiting for Approval`, New Value `Canceled`, Modified By `Fajar N`
22. Buka Admin Console > Activity Log, saring Object `Client Subscription`, dan cari entri yang sama
23. Verifikasi entri Activity Log `Client Subscription` baru: Name `PT Bintang Timur+{runId}-116`, Action `Cancel Request (Trial)`, Field `Status`, Old `Waiting for Approval`, New `Canceled`, Modified By `Fajar N`
24. Buka Detail user Fajar N, tab System Log, dan cari entri yang sama
25. Verifikasi entri System Log Detail user Fajar N baru: Action `Cancel Request (Trial)`, Object `Client Subscription`, Name `PT Bintang Timur+{runId}-116`, Field `Status`, Old `Waiting for Approval`, New `Canceled`
26. Ganti akun: klik Logout dari akun sebelumnya
27. Login sebagai `Dewi Anggraini` (`groupManagerSub_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_SUB_GM_PASSWORD`)

### TC-AC-CS-614: Log Cancel Request term Pending

28. Pemicu (sesi API): batalkan term Pending (Cancel Request) `Apotek Sehat Sentosa B+{runId}-116 — SIEM` hingga perubahan tersimpan
29. Buka menu Allocation > Client Subscription
30. Buka modal Changelog, ketik Search `Apotek Sehat Sentosa B+{runId}-116`, tekan Enter, dan cari entri Action `Cancel Request`
31. Verifikasi entri Changelog baru (selisih satu terhadap baseline): Action `Cancel Request`, Client — Product `Apotek Sehat Sentosa B+{runId}-116 — SIEM`, Field `Status`, Old Value `Pending`, New Value `Canceled`, Modified By `Dewi A`
32. Buka Admin Console > Activity Log, saring Object `Client Subscription`, dan cari entri yang sama
33. Verifikasi entri Activity Log `Client Subscription` baru: Name `Apotek Sehat Sentosa B+{runId}-116 — SIEM`, Action `Cancel Request`, Field `Status`, Old `Pending`, New `Canceled`, Modified By `Dewi A`
34. Buka Detail user Dewi A, tab System Log, dan cari entri yang sama
35. Verifikasi entri System Log Detail user Dewi A baru: Action `Cancel Request`, Object `Client Subscription`, Name `Apotek Sehat Sentosa B+{runId}-116 — SIEM`, Field `Status`, Old `Pending`, New `Canceled`

## Notes

- Aksi pemicu tiap blok adalah aksi pada kolom Dependensi TC (bukan Langkah Uji TC ini); spec memicunya lewat sesi API aktor yang sama dan menulis langkah pemicu "... hingga ... tersimpan" (R-20). Sesi API bukan konteks kedua dan tidak memakai `P-2`.
- Urutan blok: TC-AC-CS-451 (Principal), TC-AC-CS-452 dan 455 (Create-Only), lalu TC-AC-CS-614 (Group Manager), agar tiap akun hanya login satu kali (S-10).
- Langkah penghubung (S-03): langkah Search untuk menemukan entri target di modal Changelog (R-16), langkah menyaring Object `Client Subscription` di Activity Log, dan langkah `Buka menu Allocation > Client Subscription` (langkah 11, 19, dan 29) yang membuka List kembali sesudah Activity Log dan System Log atau sesudah login sebelum modal Changelog dibuka.
- Temuan untuk QA:
  - Aksi pemicu terletak di TC pada kolom Dependensi, tanpa endpoint, payload, atau data kunci (nama Client, plan, nilai) di Langkah Uji TC ini; spec mengambil nama Client, plan, dan nilai dari Expected TC dan memicu aksi lewat sesi API yang kemampuannya tidak tertulis di TC, PRD, atau LLD (disediakan tim BE/FE).
  - Precondition TC menyebut aktor Create-Only atau Group Manager membuka Activity Log dan Detail user tab System Log; hak akses role itu ke surface tersebut tidak dinyatakan di TC. Spec mengikuti Precondition TC.
