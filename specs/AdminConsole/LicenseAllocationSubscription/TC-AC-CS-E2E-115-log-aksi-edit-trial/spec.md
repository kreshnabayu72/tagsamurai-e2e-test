---
id: TC-AC-CS-E2E-115-log-aksi-edit-trial
title: "Log Aksi: Edit Trial"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-CS-448
  - TC-AC-CS-449
  - TC-AC-CS-450
coverage:
  web: automated
---

# Log Aksi: Edit Trial

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Create-Only (capability Create saja), Distributor PT Maju Bersama (Pre-setup #6) `createOnlySub_automated_{namaCompany}@qwertysystem.net` (`Fajar Nugroho`), password `Spectra.env.AC_SUB_CREATE_PASSWORD`; login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Email dan identitas data Pre-setup dirujuk lewat `Fixture.license-allocation-subscription` (belum ada; disediakan tim FE). Nama env var password di atas didaftarkan di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example` oleh tim FE, sesuai `suite.md`.
- Suite berjalan serial (`parallel: false`). Hook `beforeEach` suite membuka Allocation > Client Subscription tab Current dan menjadi jaring pengaman S-09 (lihat `suite.md`); flag Guided Tooltip diatur hook suite (`seen`), sehingga walkthrough tidak muncul.
- Sesi API aktor: aksi pemicu (kolom Dependensi TC) dijalankan lewat login API akun aktor sesuai `suite.md`; kemampuan menulis lewat API, endpoint, dan payloadnya tidak tertulis di TC, PRD, atau LLD sehingga disediakan tim BE/FE (S-13). Sesi UI aktor tidak terpengaruh (bagian 5).
- Baseline S-12: jumlah entri Changelog, Activity Log, dan System Log per Client, Action, dan user pelaku dicatat di hook `before` lewat kemampuan membaca audit trail (disediakan tim FE/BE, bagian 8b butir 10) sebelum aksi pemicu pertama; Changelog, Activity Log, dan System Log adalah audit trail permanen sehingga asersi "entri baru" memakai selisih terhadap baseline itu dan entri dicari lewat Action, Client, dan email pelaku (bukan posisi teratas).
- Data seed milik spec, dibuat lewat sesi API aktor di hook `before` dan dibersihkan di hook `after` (S-06, S-12; bersuffix `+{runId}-115`). Spec tidak menulis ke baris Pre-setup bersama dan tidak memerlukan langkah pemulihan antar blok; entri audit trail (Changelog, Activity Log, System Log) yang dihasilkan aksi pemicu permanen dan dibaca lewat selisih terhadap baseline. Dua seed; blok TC-AC-CS-448 dan 449 memakai seed yang sama karena mengubah field berbeda (Asset Quota dan Concurrent User Quota) sehingga tidak saling bergantung:
  1. TC-AC-CS-448 dan 449: Client `PT Bintang Timur+{runId}-115` dengan pengajuan Trial FAMS Waiting for Approval, Asset Quota 50, Concurrent User Quota 10, Plan Owner PT Maju Bersama (Distributor), requester `Fajar N` (bentuk Pre-setup #59).
  2. TC-AC-CS-450: Client `CV Nusantara Data+{runId}-115` (binaan langsung PT Maju Bersama) dengan pengajuan Trial SIEM Waiting for Approval, Log Source Quota 10, Plan Owner PT Maju Bersama (Distributor), requester `Fajar N` (bentuk Pre-setup #105).

## Test Steps

### TC-AC-CS-448: Log Edit Trial Asset Quota

1. Pemicu (sesi API): simpan Edit Asset Quota Trial `50` menjadi `25` pada pengajuan Trial `PT Bintang Timur+{runId}-115` hingga perubahan tersimpan
2. Buka modal Changelog, ketik Search `PT Bintang Timur+{runId}-115`, tekan Enter, dan cari entri Action `Edit (Trial — Asset Quota, FAMS/SAMS)`
3. Verifikasi entri Changelog baru (selisih satu terhadap baseline): Action `Edit (Trial — Asset Quota, FAMS/SAMS)`, Client — Product `PT Bintang Timur+{runId}-115`, Field `Asset Quota`, Old Value `50`, New Value `25`, Modified By `Fajar N`
4. Buka Admin Console > Activity Log, saring Object `Client Subscription`, dan cari entri yang sama
5. Verifikasi entri Activity Log `Client Subscription` baru: Name `PT Bintang Timur+{runId}-115`, Action `Edit (Trial — Asset Quota, FAMS/SAMS)`, Field `Asset Quota`, Old `50`, New `25`, Modified By `Fajar N`
6. Buka Detail user Fajar N, tab System Log, dan cari entri yang sama
7. Verifikasi entri System Log Detail user Fajar N baru: Action `Edit (Trial — Asset Quota, FAMS/SAMS)`, Object `Client Subscription`, Name `PT Bintang Timur+{runId}-115`, Field `Asset Quota`, Old `50`, New `25`

### TC-AC-CS-449: Log Edit Trial Concurrent User Quota

8. Pemicu (sesi API): simpan Edit Concurrent User Quota Trial `10` menjadi `5` pada pengajuan Trial `PT Bintang Timur+{runId}-115` hingga perubahan tersimpan
9. Buka menu Allocation > Client Subscription
10. Buka modal Changelog, ketik Search `PT Bintang Timur+{runId}-115`, tekan Enter, dan cari entri Action `Edit (Trial — Concurrent User Quota)`
11. Verifikasi entri Changelog baru (selisih satu terhadap baseline): Action `Edit (Trial — Concurrent User Quota)`, Client — Product `PT Bintang Timur+{runId}-115`, Field `Concurrent User Quota`, Old Value `10`, New Value `5`, Modified By `Fajar N`
12. Buka Admin Console > Activity Log, saring Object `Client Subscription`, dan cari entri yang sama
13. Verifikasi entri Activity Log `Client Subscription` baru: Name `PT Bintang Timur+{runId}-115`, Action `Edit (Trial — Concurrent User Quota)`, Field `Concurrent User Quota`, Old `10`, New `5`, Modified By `Fajar N`
14. Buka Detail user Fajar N, tab System Log, dan cari entri yang sama
15. Verifikasi entri System Log Detail user Fajar N baru: Action `Edit (Trial — Concurrent User Quota)`, Object `Client Subscription`, Name `PT Bintang Timur+{runId}-115`, Field `Concurrent User Quota`, Old `10`, New `5`

### TC-AC-CS-450: Log Edit Trial Log Source Quota

16. Pemicu (sesi API): simpan Edit Log Source Quota Trial `10` menjadi `20` pada trial SIEM `CV Nusantara Data+{runId}-115` hingga perubahan tersimpan
17. Buka menu Allocation > Client Subscription
18. Buka modal Changelog, ketik Search `CV Nusantara Data+{runId}-115`, tekan Enter, dan cari entri Action `Edit (Trial — Log Source Quota, SIEM)`
19. Verifikasi entri Changelog baru (selisih satu terhadap baseline): Action `Edit (Trial — Log Source Quota, SIEM)`, Client — Product `CV Nusantara Data+{runId}-115`, Field `Log Source Quota`, Old Value `10`, New Value `20`, Modified By `Fajar N`
20. Buka Admin Console > Activity Log, saring Object `Client Subscription`, dan cari entri yang sama
21. Verifikasi entri Activity Log `Client Subscription` baru: Name `CV Nusantara Data+{runId}-115`, Action `Edit (Trial — Log Source Quota, SIEM)`, Field `Log Source Quota`, Old `10`, New `20`, Modified By `Fajar N`
22. Buka Detail user Fajar N, tab System Log, dan cari entri yang sama
23. Verifikasi entri System Log Detail user Fajar N baru: Action `Edit (Trial — Log Source Quota, SIEM)`, Object `Client Subscription`, Name `CV Nusantara Data+{runId}-115`, Field `Log Source Quota`, Old `10`, New `20`

## Notes

- Aksi pemicu tiap blok adalah aksi pada kolom Dependensi TC (bukan Langkah Uji TC ini); spec memicunya lewat sesi API aktor yang sama dan menulis langkah pemicu "... hingga ... tersimpan" (R-20). Sesi API bukan konteks kedua dan tidak memakai `P-2`.
- Langkah penghubung (S-03): langkah Search untuk menemukan entri target di modal Changelog (R-16), langkah menyaring Object `Client Subscription` di Activity Log, dan langkah `Buka menu Allocation > Client Subscription` (langkah 9 dan 17) yang membuka List kembali sesudah Activity Log dan System Log atau sesudah login sebelum modal Changelog dibuka.
- Temuan untuk QA:
  - Aksi pemicu terletak di TC pada kolom Dependensi, tanpa endpoint, payload, atau data kunci (nama Client, plan, nilai) di Langkah Uji TC ini; spec mengambil nama Client, plan, dan nilai dari Expected TC dan memicu aksi lewat sesi API yang kemampuannya tidak tertulis di TC, PRD, atau LLD (disediakan tim BE/FE).
  - Precondition TC menyebut aktor Create-Only atau Group Manager membuka Activity Log dan Detail user tab System Log; hak akses role itu ke surface tersebut tidak dinyatakan di TC. Spec mengikuti Precondition TC.
