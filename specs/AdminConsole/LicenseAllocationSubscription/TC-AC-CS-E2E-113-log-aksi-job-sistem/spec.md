---
id: TC-AC-CS-E2E-113-log-aksi-job-sistem
title: "Log Aksi: Job Sistem"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-CS-438
  - TC-AC-CS-439
  - TC-AC-CS-441
  - TC-AC-CS-453
  - TC-AC-CS-456
coverage:
  web: automated
---

# Log Aksi: Job Sistem

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Total Control Principal PT ABC (Pre-setup #1) `totalControlSub_automated_{namaCompany}@qwertysystem.net` (`Hendra Wijaya`), password `Spectra.env.AC_SUB_TC_PASSWORD`; login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Email dan identitas data Pre-setup dirujuk lewat `Fixture.license-allocation-subscription` (belum ada; disediakan tim FE). Nama env var password di atas didaftarkan di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example` oleh tim FE, sesuai `suite.md`.
- Suite berjalan serial (`parallel: false`). Hook `beforeEach` suite membuka Allocation > Client Subscription tab Current dan menjadi jaring pengaman S-09 (lihat `suite.md`); flag Guided Tooltip diatur hook suite (`seen`), sehingga walkthrough tidak muncul.
- Sesi API aktor: aksi pemicu (kolom Dependensi TC) dijalankan lewat login API akun aktor sesuai `suite.md`; kemampuan menulis lewat API, endpoint, dan payloadnya tidak tertulis di TC, PRD, atau LLD sehingga disediakan tim BE/FE (S-13). Sesi UI aktor tidak terpengaruh (bagian 5).
- Baseline S-12: jumlah entri Changelog, Activity Log, dan System Log per Client, Action, dan user pelaku dicatat di hook `before` lewat kemampuan membaca audit trail (disediakan tim FE/BE, bagian 8b butir 10) sebelum aksi pemicu pertama; Changelog, Activity Log, dan System Log adalah audit trail permanen sehingga asersi "entri baru" memakai selisih terhadap baseline itu dan entri dicari lewat Action, Client, dan email pelaku (bukan posisi teratas).
- Data seed milik spec, dibuat lewat sesi API aktor di hook `before` dan dibersihkan di hook `after` (S-06, S-12; bersuffix `+{runId}-113`). Spec tidak menulis ke baris Pre-setup bersama dan tidak memerlukan langkah pemulihan data antar blok karena tiap blok memakai Client seed sendiri; entri audit trail (Changelog, Activity Log, System Log) yang dihasilkan job permanen dan dibaca lewat selisih terhadap baseline. Satu seed per blok:
  1. TC-AC-CS-438: Client `Toko Harapan Baru A+{runId}-113` (binaan langsung PT Maju Bersama pada group `Jawa`) dengan predecessor FAMS plan Growth status Active (01/09/25 sampai 31/08/26) dan successor Renewal FAMS plan Professional status Pending (01/09/26 sampai 31/08/27), Plan Owner PT Maju Bersama (Distributor), requester `Fajar N` (bentuk Pre-setup #108).
  2. TC-AC-CS-439: Client `Percetakan Mega+{runId}-113` dengan term Pending FAMS plan Professional (15/09/26 sampai 14/09/27), Plan Owner PT Maju Bersama (Distributor), requester `Dewi A` (bentuk Pre-setup #57).
  3. TC-AC-CS-441: Client `Toko Harapan Baru B+{runId}-113` (binaan langsung PT Maju Bersama pada group `Jawa`) dengan predecessor SAMS plan Enterprise status Archive dan successor SAMS plan Enterprise status Pending (01/01/25 sampai 31/12/25), requester `Fajar N` (bentuk Pre-setup #109).
  4. TC-AC-CS-453: Client `Toko Timeout+{runId}-113` (binaan langsung PT Maju Bersama pada group `Jawa`) dengan pengajuan FAMS plan Growth status Waiting for Approval, disubmit 16/08/26 09:00 (Approval Timeout 3 hari), requester `Fajar N` (bentuk Pre-setup #134).
  5. TC-AC-CS-456: Client `Toko Timeout Trial+{runId}-113` (binaan langsung PT Maju Bersama pada group `Jawa`) dengan pengajuan Trial status Waiting for Approval, disubmit 16/08/26 09:00, requester `Eko S` (bentuk Pre-setup #134).
- Kelas harness eksternal (d): jam server dan jam browser diatur absolut ke waktu efektif tiap job, lalu job (Renew terjadwal, Activate terjadwal, Scheduled Flip, Timeout Auto-Cancel) dipicu atau di-poll lewat kemampuan tim FE/BE (suite.md); jam dipulihkan pada langkah eksplisit `Pulihkan jam server dan jam browser` tepat setelah tiap langkah pemicu, sebelum aksi aktor membuka Changelog, Activity Log, atau System Log (S-09), dan sekali lagi di hook `after` sebagai jaring pengaman (jam adalah state global yang tidak dapat dimiliki spec). Nilai waktu absolut tiap job dibaca dari tanggal efektif dan waktu submit data Pre-setup yang disebut tiap blok (margin terhadap batas di atas 5 menit).
- Requester pemicu seed (`Fajar N`, `Dewi A`, `Eko S`) tidak login; aktor spec ini hanya Principal.

## Test Steps

### TC-AC-CS-438: Log Renew efek terjadwal diterapkan oleh sistem

1. Pemicu (sesi API): atur jam server dan jam browser ke 01/09/26 00:00 dan jalankan job Renew terjadwal pada term `Toko Harapan Baru A+{runId}-113 — FAMS` hingga perubahan tersimpan
2. Pulihkan jam server dan jam browser
3. Buka modal Changelog, ketik Search `Toko Harapan Baru A+{runId}-113`, tekan Enter, dan cari entri Action `Renew (efek terjadwal, diterapkan)`
4. Verifikasi entri Changelog baru (selisih satu terhadap baseline): Action `Renew (efek terjadwal, diterapkan)`, Client — Product `Toko Harapan Baru A+{runId}-113 — FAMS`, Field `Plan/End Date`, Old Value `Growth/31/08/26`, New Value `Professional/31/08/27`, Modified By `System`
5. Buka Admin Console > Activity Log, saring Object `Client Subscription`, dan cari entri yang sama
6. Verifikasi entri Activity Log `Client Subscription` baru: Name `Toko Harapan Baru A+{runId}-113 — FAMS`, Action `Renew (efek terjadwal, diterapkan)`, Field `Plan/End Date`, Old `Growth/31/08/26`, New `Professional/31/08/27`, Modified By `System`
7. Buka Detail user requester `Fajar N`, tab System Log
8. Verifikasi tabel System Log menampilkan sedikitnya satu entri lain
9. Verifikasi System Log requester tidak memuat entri Action `Renew (efek terjadwal, diterapkan)` (jumlah entri sama dengan baseline) karena aksi dijalankan job tanpa user aktor

### TC-AC-CS-439: Log Activate efek terjadwal diterapkan oleh sistem

10. Pemicu (sesi API): atur jam server dan jam browser ke tanggal Start Date term Pending dan jalankan job Activate terjadwal pada term `Percetakan Mega+{runId}-113 — FAMS` hingga perubahan tersimpan
11. Pulihkan jam server dan jam browser
12. Buka menu Allocation > Client Subscription
13. Buka modal Changelog, ketik Search `Percetakan Mega+{runId}-113`, tekan Enter, dan cari entri Action `Activate (efek terjadwal, diterapkan)`
14. Verifikasi entri Changelog baru (selisih satu terhadap baseline): Action `Activate (efek terjadwal, diterapkan)`, Client — Product `Percetakan Mega+{runId}-113 — FAMS`, Field `Status`, Old Value `Pending`, New Value `Active`, Modified By `System`
15. Buka Admin Console > Activity Log, saring Object `Client Subscription`, dan cari entri yang sama
16. Verifikasi entri Activity Log `Client Subscription` baru: Name `Percetakan Mega+{runId}-113 — FAMS`, Action `Activate (efek terjadwal, diterapkan)`, Field `Status`, Old `Pending`, New `Active`, Modified By `System`
17. Buka Detail user requester `Dewi A`, tab System Log
18. Verifikasi tabel System Log menampilkan sedikitnya satu entri lain
19. Verifikasi System Log requester tidak memuat entri Action `Activate (efek terjadwal, diterapkan)` (jumlah entri sama dengan baseline) karena aksi dijalankan job tanpa user aktor

### TC-AC-CS-441: Log Scheduled Flip Auto-Cancel

20. Pemicu (sesi API): atur jam server dan jam browser ke waktu Scheduled Flip dan jalankan job Scheduled Flip pada term `Toko Harapan Baru B+{runId}-113 — SAMS` hingga perubahan tersimpan
21. Pulihkan jam server dan jam browser
22. Buka menu Allocation > Client Subscription
23. Buka modal Changelog, ketik Search `Toko Harapan Baru B+{runId}-113`, tekan Enter, dan cari entri Action `Scheduled Flip Auto-Cancel`
24. Verifikasi entri Changelog baru (selisih satu terhadap baseline): Action `Scheduled Flip Auto-Cancel`, Client — Product `Toko Harapan Baru B+{runId}-113 — SAMS`, Field `Status`, Old Value `Pending`, New Value `Canceled`, Modified By `System`
25. Buka Admin Console > Activity Log, saring Object `Client Subscription`, dan cari entri yang sama
26. Verifikasi entri Activity Log `Client Subscription` baru: Name `Toko Harapan Baru B+{runId}-113 — SAMS`, Action `Scheduled Flip Auto-Cancel`, Field `Status`, Old `Pending`, New `Canceled`, Modified By `System`
27. Buka Detail user requester `Fajar N`, tab System Log
28. Verifikasi tabel System Log menampilkan sedikitnya satu entri lain
29. Verifikasi System Log requester tidak memuat entri Action `Scheduled Flip Auto-Cancel` (jumlah entri sama dengan baseline) karena aksi dijalankan job tanpa user aktor

### TC-AC-CS-453: Log Timeout Auto-Cancel

30. Pemicu (sesi API): atur jam server dan jam browser melewati Approval Timeout dan jalankan job Timeout Auto-Cancel pada pengajuan `Toko Timeout+{runId}-113 — FAMS` hingga perubahan tersimpan
31. Pulihkan jam server dan jam browser
32. Buka menu Allocation > Client Subscription
33. Buka modal Changelog, ketik Search `Toko Timeout+{runId}-113`, tekan Enter, dan cari entri Action `Timeout Auto-Cancel`
34. Verifikasi entri Changelog baru (selisih satu terhadap baseline): Action `Timeout Auto-Cancel`, Client — Product `Toko Timeout+{runId}-113 — FAMS`, Field `Status`, Old Value `Waiting for Approval`, New Value `Canceled`, Modified By `System`
35. Buka Admin Console > Activity Log, saring Object `Client Subscription`, dan cari entri yang sama
36. Verifikasi entri Activity Log `Client Subscription` baru: Name `Toko Timeout+{runId}-113 — FAMS`, Action `Timeout Auto-Cancel`, Field `Status`, Old `Waiting for Approval`, New `Canceled`, Modified By `System`
37. Buka Detail user requester `Fajar N`, tab System Log
38. Verifikasi tabel System Log menampilkan sedikitnya satu entri lain
39. Verifikasi System Log requester tidak memuat entri Action `Timeout Auto-Cancel` (jumlah entri sama dengan baseline) karena aksi dijalankan job tanpa user aktor

### TC-AC-CS-456: Log Timeout Auto-Cancel Trial

40. Pemicu (sesi API): atur jam server dan jam browser melewati Approval Timeout dan jalankan job Timeout Auto-Cancel pada pengajuan Trial `Toko Timeout Trial+{runId}-113` hingga perubahan tersimpan
41. Pulihkan jam server dan jam browser
42. Buka menu Allocation > Client Subscription
43. Buka modal Changelog, ketik Search `Toko Timeout Trial+{runId}-113`, tekan Enter, dan cari entri Action `Timeout Auto-Cancel (Trial)`
44. Verifikasi entri Changelog baru (selisih satu terhadap baseline): Action `Timeout Auto-Cancel (Trial)`, Client — Product `Toko Timeout Trial+{runId}-113` (varian Trial mencatat Client saja tanpa Product), Field `Status`, Old Value `Waiting for Approval`, New Value `Canceled`, Modified By `System`
45. Buka Admin Console > Activity Log, saring Object `Client Subscription`, dan cari entri yang sama
46. Verifikasi entri Activity Log `Client Subscription` baru: Name `Toko Timeout Trial+{runId}-113`, Action `Timeout Auto-Cancel (Trial)`, Field `Status`, Old `Waiting for Approval`, New `Canceled`, Modified By `System`
47. Buka Detail user requester `Eko S`, tab System Log
48. Verifikasi tabel System Log menampilkan sedikitnya satu entri lain
49. Verifikasi System Log requester tidak memuat entri Action `Timeout Auto-Cancel (Trial)` (jumlah entri sama dengan baseline) karena aksi dijalankan job tanpa user aktor

## Notes

- Aksi pemicu tiap blok adalah aksi pada kolom Dependensi TC (bukan Langkah Uji TC ini); spec memicunya lewat sesi API aktor yang sama dan menulis langkah pemicu "... hingga ... tersimpan" (R-20). Sesi API bukan konteks kedua dan tidak memakai `P-2`.
- Spec ini 49 langkah, melewati sekitar 35 langkah. Alasannya: seluruh blok satu topik (log hasil job sistem, kelas harness eksternal yang sama), berpola sama, dan berdiri sendiri; kegagalan satu blok tidak membuat blok lain kehilangan makna. Blok baca-log berpola (buka surface, cari entri, `Verifikasi` kolom log) tidak dihitung pada ambang (bagian 3, Smell).
- P-1: asersi absence entri System Log requester (TC-AC-CS-438, 439, 441, 453, 456) milik TC ini bergantung pada state job hasil manipulasi jam yang baru dibangun pada blok yang sama, sehingga tetap berada di spec ini dengan baseline (S-12) dan anchor entri Activity Log serta entri System Log lain.
- Langkah penghubung (S-03): langkah Search untuk menemukan entri target di modal Changelog (R-16), langkah menyaring Object `Client Subscription` di Activity Log, dan langkah `Buka menu Allocation > Client Subscription` (langkah 12, 22, 32, dan 42) yang membuka List kembali sebelum modal Changelog dibuka. Langkah `Pulihkan jam server dan jam browser` mengikuti tiap langkah pemicu (langkah 2, 11, 21, 31, dan 41) dan hook `after` memulihkannya sekali lagi; entri dicari lewat Search, Action, dan Client, bukan posisi teratas (S-12).
- Temuan untuk QA:
  - Aksi pemicu terletak di TC pada kolom Dependensi, tanpa endpoint, payload, atau data kunci (nama Client, plan, nilai) di Langkah Uji TC ini; spec mengambil nama Client, plan, dan nilai dari Expected TC dan memicu aksi lewat sesi API yang kemampuannya tidak tertulis di TC, PRD, atau LLD (disediakan tim BE/FE).
  - Langkah pemicu job dan nilai jam absolut tiap job tidak tertulis di TC pada kolom Dependensi; nilai waktu dihitung dari data Pre-setup dan disediakan tim FE/BE.
  - Expected c tiap blok (System Log requester tidak memuat entri) tidak punya langkah observasi di TC; spec membuka System Log requester dengan baseline jumlah entri dan anchor entri lain yang tampil.
