---
id: TC-AC-CS-E2E-114-log-aksi-edit-duration-pending-dan-start-date
title: "Log Aksi: Edit Duration, Pending, dan Start Date"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-CS-444
  - TC-AC-CS-446
  - TC-AC-CS-447
  - TC-AC-CS-445
coverage:
  web: automated
---

# Log Aksi: Edit Duration, Pending, dan Start Date

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Create-Only (capability Create saja), Distributor PT Maju Bersama (Pre-setup #6) `createOnlySub_automated_{namaCompany}@qwertysystem.net` (`Fajar Nugroho`), password `Spectra.env.AC_SUB_CREATE_PASSWORD`; login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Akun aktor berikutnya (ganti akun dengan langkah eksplisit): Group Manager scope Group Jawa, Distributor PT Maju Bersama (Pre-setup #5) `groupManagerSub_automated_{namaCompany}@qwertysystem.net` (`Dewi Anggraini`), password `Spectra.env.AC_SUB_GM_PASSWORD`; login pada langkah ganti akun, dan hook `after` mengembalikan sesi ke akun default suite (Pre-setup #1).
- Email dan identitas data Pre-setup dirujuk lewat `Fixture.license-allocation-subscription` (belum ada; disediakan tim FE). Nama env var password di atas didaftarkan di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example` oleh tim FE, sesuai `suite.md`.
- Suite berjalan serial (`parallel: false`). Hook `beforeEach` suite membuka Allocation > Client Subscription tab Current dan menjadi jaring pengaman S-09 (lihat `suite.md`); flag Guided Tooltip diatur hook suite (`seen`), sehingga walkthrough tidak muncul.
- Kemampuan teknis (disediakan tim FE/BE): jam server dan jam browser diatur absolut ke tanggal acuan `19/08/26` (fixture waktu, disediakan tim FE/BE), dipulihkan di hook `after`.
- Sesi API aktor: aksi pemicu (kolom Dependensi TC) dijalankan lewat login API akun aktor sesuai `suite.md`; kemampuan menulis lewat API, endpoint, dan payloadnya tidak tertulis di TC, PRD, atau LLD sehingga disediakan tim BE/FE (S-13). Sesi UI aktor tidak terpengaruh (bagian 5).
- Baseline S-12: jumlah entri Changelog, Activity Log, dan System Log per Client, Action, dan user pelaku dicatat di hook `before` lewat kemampuan membaca audit trail (disediakan tim FE/BE, bagian 8b butir 10) sebelum aksi pemicu pertama; Changelog, Activity Log, dan System Log adalah audit trail permanen sehingga asersi "entri baru" memakai selisih terhadap baseline itu dan entri dicari lewat Action, Client, dan email pelaku (bukan posisi teratas).
- Data seed milik spec, dibuat lewat sesi API aktor di hook `before` dan dibersihkan di hook `after` (S-06, S-12; bersuffix `+{runId}-114`). Spec tidak menulis ke baris Pre-setup bersama dan tidak memerlukan langkah pemulihan antar blok; entri audit trail (Changelog, Activity Log, System Log) yang dihasilkan aksi pemicu permanen dan dibaca lewat selisih terhadap baseline. Satu seed per blok:
  1. TC-AC-CS-444: Client `Apotek Sehat Sentosa A+{runId}-114` dengan pengajuan FAMS Waiting for Approval, Duration 1 year(s), Plan Owner PT Maju Bersama (Distributor), requester `Fajar N` (bentuk Pre-setup #49).
  2. TC-AC-CS-446: Client `Apotek Sehat Sentosa B+{runId}-114` dengan term Pending SIEM, Plan Owner PT Maju Bersama (Distributor), diajukan requester `Fajar N` (toggle ON, sudah di-Approve) (bentuk Pre-setup #90).
  3. TC-AC-CS-447: Client `PT Bintang Timur+{runId}-114` dengan pengajuan Trial FAMS Growth Waiting for Approval, Duration 30 days, Plan Owner PT Maju Bersama (Distributor), requester `Fajar N` (bentuk Pre-setup #59).
  4. TC-AC-CS-445: Client `Percetakan Mega+{runId}-114` dengan term Pending FAMS plan Professional, Start Date 15/09/26, Plan Owner PT Maju Bersama (Distributor), requester Group Manager `Dewi A` (bentuk Pre-setup #57).

## Test Steps

### TC-AC-CS-444: Log Edit Duration

1. Pemicu (sesi API): simpan Edit Duration `1` menjadi `2` tahun pada pengajuan `Apotek Sehat Sentosa A+{runId}-114 — FAMS` hingga perubahan tersimpan
2. Buka modal Changelog, ketik Search `Apotek Sehat Sentosa A+{runId}-114`, tekan Enter, dan cari entri Action `Edit (Duration, mode New/Renewal)`
3. Verifikasi entri Changelog baru (selisih satu terhadap baseline): Action `Edit (Duration, mode New/Renewal)`, Client — Product `Apotek Sehat Sentosa A+{runId}-114 — FAMS`, Field `Duration`, Old Value `1 year(s)`, New Value `2 year(s)`, Modified By `Fajar N`
4. Buka Admin Console > Activity Log, saring Object `Client Subscription`, dan cari entri yang sama
5. Verifikasi entri Activity Log `Client Subscription` baru: Name `Apotek Sehat Sentosa A+{runId}-114 — FAMS`, Action `Edit (Duration, mode New/Renewal)`, Field `Duration`, Old `1 year(s)`, New `2 year(s)`, Modified By `Fajar N`
6. Buka Detail user Fajar N, tab System Log, dan cari entri yang sama
7. Verifikasi entri System Log Detail user Fajar N baru: Action `Edit (Duration, mode New/Renewal)`, Object `Client Subscription`, Name `Apotek Sehat Sentosa A+{runId}-114 — FAMS`, Field `Duration`, Old `1 year(s)`, New `2 year(s)`

### TC-AC-CS-446: Log Edit term Pending kembali ke approval

8. Pemicu (sesi API): simpan Edit pada term Pending `Apotek Sehat Sentosa B+{runId}-114 — SIEM` sehingga kembali ke approval hingga perubahan tersimpan
9. Buka menu Allocation > Client Subscription
10. Buka modal Changelog, ketik Search `Apotek Sehat Sentosa B+{runId}-114`, tekan Enter, dan cari entri Action ``Edit (term `pending` kembali ke approval)``
11. Verifikasi entri Changelog baru (selisih satu terhadap baseline): Action ``Edit (term `pending` kembali ke approval)``, Client — Product `Apotek Sehat Sentosa B+{runId}-114 — SIEM`, Field `Status`, Old Value `Pending`, New Value `Waiting for Approval`, Modified By `Fajar N`
12. Buka Admin Console > Activity Log, saring Object `Client Subscription`, dan cari entri yang sama
13. Verifikasi entri Activity Log `Client Subscription` baru: Name `Apotek Sehat Sentosa B+{runId}-114 — SIEM`, Action ``Edit (term `pending` kembali ke approval)``, Field `Status`, Old `Pending`, New `Waiting for Approval`, Modified By `Fajar N`
14. Buka Detail user Fajar N, tab System Log, dan cari entri yang sama
15. Verifikasi entri System Log Detail user Fajar N baru: Action ``Edit (term `pending` kembali ke approval)``, Object `Client Subscription`, Name `Apotek Sehat Sentosa B+{runId}-114 — SIEM`, Field `Status`, Old `Pending`, New `Waiting for Approval`

### TC-AC-CS-447: Log Edit Trial Duration

16. Pemicu (sesi API): simpan Edit Duration Trial `30 days` menjadi `14 days` pada pengajuan Trial `PT Bintang Timur+{runId}-114` hingga perubahan tersimpan
17. Buka menu Allocation > Client Subscription
18. Buka modal Changelog, ketik Search `PT Bintang Timur+{runId}-114`, tekan Enter, dan cari entri Action `Edit (Trial — Duration)`
19. Verifikasi entri Changelog baru (selisih satu terhadap baseline): Action `Edit (Trial — Duration)`, Client — Product `PT Bintang Timur+{runId}-114`, Field `Duration`, Old Value `30 days`, New Value `14 days`, Modified By `Fajar N`
20. Buka Admin Console > Activity Log, saring Object `Client Subscription`, dan cari entri yang sama
21. Verifikasi entri Activity Log `Client Subscription` baru: Name `PT Bintang Timur+{runId}-114`, Action `Edit (Trial — Duration)`, Field `Duration`, Old `30 days`, New `14 days`, Modified By `Fajar N`
22. Buka Detail user Fajar N, tab System Log, dan cari entri yang sama
23. Verifikasi entri System Log Detail user Fajar N baru: Action `Edit (Trial — Duration)`, Object `Client Subscription`, Name `PT Bintang Timur+{runId}-114`, Field `Duration`, Old `30 days`, New `14 days`
24. Ganti akun: klik Logout dari akun sebelumnya
25. Login sebagai `Dewi Anggraini` (`groupManagerSub_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_SUB_GM_PASSWORD`)

### TC-AC-CS-445: Log Edit Start Date mode New

26. Pemicu (sesi API): simpan Edit Start Date `15/09/26` menjadi `19/08/26` pada term `Percetakan Mega+{runId}-114 — FAMS` hingga perubahan tersimpan
27. Buka menu Allocation > Client Subscription
28. Buka modal Changelog, ketik Search `Percetakan Mega+{runId}-114`, tekan Enter, dan cari entri Action `Edit (Start Date, mode New)`
29. Verifikasi entri Changelog baru (selisih satu terhadap baseline): Action `Edit (Start Date, mode New)`, Client — Product `Percetakan Mega+{runId}-114 — FAMS`, Field `Start Date`, Old Value `15/09/26`, New Value `19/08/26`, Modified By `Dewi A`
30. Buka Admin Console > Activity Log, saring Object `Client Subscription`, dan cari entri yang sama
31. Verifikasi entri Activity Log `Client Subscription` baru: Name `Percetakan Mega+{runId}-114 — FAMS`, Action `Edit (Start Date, mode New)`, Field `Start Date`, Old `15/09/26`, New `19/08/26`, Modified By `Dewi A`
32. Buka Detail user Dewi A, tab System Log, dan cari entri yang sama
33. Verifikasi entri System Log Detail user Dewi A baru: Action `Edit (Start Date, mode New)`, Object `Client Subscription`, Name `Percetakan Mega+{runId}-114 — FAMS`, Field `Start Date`, Old `15/09/26`, New `19/08/26`

## Notes

- Aksi pemicu tiap blok adalah aksi pada kolom Dependensi TC (bukan Langkah Uji TC ini); spec memicunya lewat sesi API aktor yang sama dan menulis langkah pemicu "... hingga ... tersimpan" (R-20). Sesi API bukan konteks kedua dan tidak memakai `P-2`.
- Urutan blok: TC-AC-CS-444, 446, dan 447 (akun Create-Only) lebih dulu, lalu TC-AC-CS-445 (akun Group Manager) sesudah ganti akun, agar ganti akun hanya satu kali (S-10).
- Langkah penghubung (S-03): langkah Search untuk menemukan entri target di modal Changelog (R-16), langkah menyaring Object `Client Subscription` di Activity Log, dan langkah `Buka menu Allocation > Client Subscription` (langkah 9, 17, dan 27) yang membuka List kembali sesudah Activity Log dan System Log atau sesudah login sebelum modal Changelog dibuka.
- Temuan untuk QA:
  - Aksi pemicu terletak di TC pada kolom Dependensi, tanpa endpoint, payload, atau data kunci (nama Client, plan, nilai) di Langkah Uji TC ini; spec mengambil nama Client, plan, dan nilai dari Expected TC dan memicu aksi lewat sesi API yang kemampuannya tidak tertulis di TC, PRD, atau LLD (disediakan tim BE/FE).
  - Precondition TC menyebut aktor Create-Only atau Group Manager membuka Activity Log dan Detail user tab System Log; hak akses role itu ke surface tersebut tidak dinyatakan di TC. Spec mengikuti Precondition TC.
  - TC-AC-CS-446 menulis Action sebagai prosa (`Edit (term pending kembali ke approval)`), bukan literal UI Changelog; spec mempertahankan teks itu apa adanya sebagai nilai Action dan perlu literal Action yang sebenarnya tampil dari QA.
