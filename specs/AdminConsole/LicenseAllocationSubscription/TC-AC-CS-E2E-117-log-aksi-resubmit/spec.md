---
id: TC-AC-CS-E2E-117-log-aksi-resubmit
title: "Log Aksi: Resubmit"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-CS-454
  - TC-AC-CS-457
  - TC-AC-CS-616
coverage:
  web: automated
---

# Log Aksi: Resubmit

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Create-Only (capability Create saja), Partner CV Karya Mandiri (Pre-setup #12) `createOnlyPartnerSub_automated_{namaCompany}@qwertysystem.net` (`Rina Pratama`), password `Spectra.env.AC_SUB_PARTNER_CREATE_PASSWORD`; login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Email dan identitas data Pre-setup dirujuk lewat `Fixture.license-allocation-subscription` (belum ada; disediakan tim FE). Nama env var password di atas didaftarkan di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example` oleh tim FE, sesuai `suite.md`.
- Suite berjalan serial (`parallel: false`). Hook `beforeEach` suite membuka Allocation > Client Subscription tab Current dan menjadi jaring pengaman S-09 (lihat `suite.md`); flag Guided Tooltip diatur hook suite (`seen`), sehingga walkthrough tidak muncul.
- Sesi API aktor: aksi pemicu (kolom Dependensi TC) dijalankan lewat login API akun aktor sesuai `suite.md`; kemampuan menulis lewat API, endpoint, dan payloadnya tidak tertulis di TC, PRD, atau LLD sehingga disediakan tim BE/FE (S-13). Sesi UI aktor tidak terpengaruh (bagian 5).
- Baseline S-12: jumlah entri Changelog, Activity Log, dan System Log per Client, Action, dan user pelaku dicatat di hook `before` lewat kemampuan membaca audit trail (disediakan tim FE/BE, bagian 8b butir 10) sebelum aksi pemicu pertama; Changelog, Activity Log, dan System Log adalah audit trail permanen sehingga asersi "entri baru" memakai selisih terhadap baseline itu dan entri dicari lewat Action, Client, dan email pelaku (bukan posisi teratas).
- Data seed milik spec, dibuat lewat sesi API aktor di hook `before` dan dibersihkan di hook `after` (S-06, S-12; bersuffix `+{runId}-117`). Spec tidak menulis ke baris Pre-setup bersama dan tidak memerlukan langkah pemulihan antar blok; entri audit trail (Changelog, Activity Log, System Log) yang dihasilkan aksi pemicu permanen dan dibaca lewat selisih terhadap baseline. Satu seed per blok, sehingga Resubmit TC-AC-CS-457 dan TC-AC-CS-616 tidak memakai Trial yang sama:
  1. TC-AC-CS-454: Client `Optik Cahaya A+{runId}-117` dengan pengajuan FAMS plan Growth status Canceled, Plan Owner CV Karya Mandiri (Partner), requester original `Rina P` (bentuk Pre-setup #56).
  2. TC-AC-CS-457: Client `Optik Cahaya B+{runId}-117` dengan Trial FAMS Professional status Canceled, Plan Owner CV Karya Mandiri, Trial Duration 30 hari, Asset Quota 50, Concurrent User Quota 10, requester original `Rina P` (bentuk Pre-setup #81).
  3. TC-AC-CS-616: Client `Optik Cahaya C+{runId}-117` dengan Trial seperti seed 2 (bentuk Pre-setup #81; Pre-setup Dinamis #9).
- State global: toggle Require Approval for Trial Activation diatur OFF untuk blok TC-AC-CS-616 (Resubmit Trial langsung Active) lewat kemampuan tim FE/BE (suite.md) pada langkah pemicu, dan dipulihkan ke keadaan awal di hook `after`; suite berjalan serial.

## Test Steps

### TC-AC-CS-454: Log Resubmit

1. Pemicu (sesi API): kirim ulang (Resubmit) pengajuan Canceled `Optik Cahaya A+{runId}-117 — FAMS` sebagai requester original hingga perubahan tersimpan
2. Buka modal Changelog, ketik Search `Optik Cahaya A+{runId}-117`, tekan Enter, dan cari entri Action `Resubmit`
3. Verifikasi entri Changelog baru (selisih satu terhadap baseline): Action `Resubmit`, Client — Product `Optik Cahaya A+{runId}-117 — FAMS`, Field `Plan`, Old Value `—`, New Value `Growth`, Modified By `Rina P`
4. Buka Admin Console > Activity Log, saring Object `Client Subscription`, dan cari entri yang sama
5. Verifikasi entri Activity Log `Client Subscription` baru: Name `Optik Cahaya A+{runId}-117 — FAMS`, Action `Resubmit`, Field `Plan`, Old `—`, New `Growth`, Modified By `Rina P`
6. Buka Detail user Rina P, tab System Log, dan cari entri yang sama
7. Verifikasi entri System Log Detail user Rina P baru: Action `Resubmit`, Object `Client Subscription`, Name `Optik Cahaya A+{runId}-117 — FAMS`, Field `Plan`, Old `—`, New `Growth`

### TC-AC-CS-457: Log Resubmit Trial

8. Pemicu (sesi API): kirim ulang (Resubmit) pengajuan Trial Canceled `Optik Cahaya B+{runId}-117` sebagai requester original hingga perubahan tersimpan
9. Buka menu Allocation > Client Subscription
10. Buka modal Changelog, ketik Search `Optik Cahaya B+{runId}-117`, tekan Enter, dan cari entri Action `Resubmit (Trial)`
11. Verifikasi entri Changelog baru (selisih satu terhadap baseline): Action `Resubmit (Trial)`, Client — Product `Optik Cahaya B+{runId}-117` (varian Trial mencatat Client saja tanpa Product), Field `Status`, Old Value `—`, New Value `Waiting for Approval`, Modified By `Rina P`
12. Buka Admin Console > Activity Log, saring Object `Client Subscription`, dan cari entri yang sama
13. Verifikasi entri Activity Log `Client Subscription` baru: Name `Optik Cahaya B+{runId}-117`, Action `Resubmit (Trial)`, Field `Status`, Old `—`, New `Waiting for Approval`, Modified By `Rina P`
14. Buka Detail user Rina P, tab System Log, dan cari entri yang sama
15. Verifikasi entri System Log Detail user Rina P baru: Action `Resubmit (Trial)`, Object `Client Subscription`, Name `Optik Cahaya B+{runId}-117`, Field `Status`, Old `—`, New `Waiting for Approval`

### TC-AC-CS-616: Log Resubmit Trial yang langsung Active

16. Pemicu (sesi API): matikan toggle Require Approval for Trial Activation lalu kirim ulang (Resubmit) Trial Canceled `Optik Cahaya C+{runId}-117` hingga perubahan tersimpan
17. Buka menu Allocation > Client Subscription
18. Buka modal Changelog, ketik Search `Optik Cahaya C+{runId}-117`, tekan Enter, dan cari entri Action `Resubmit (Trial)`
19. Verifikasi entri Changelog baru (selisih satu terhadap baseline): Action `Resubmit (Trial)`, Client — Product `Optik Cahaya C+{runId}-117` (varian Trial mencatat Client saja tanpa Product), Field `Status`, Old Value `—`, New Value `Active`, Modified By `Rina P`
20. Buka Admin Console > Activity Log, saring Object `Client Subscription`, dan cari entri yang sama
21. Verifikasi entri Activity Log `Client Subscription` baru: Name `Optik Cahaya C+{runId}-117`, Action `Resubmit (Trial)`, Field `Status`, Old `—`, New `Active`, Modified By `Rina P`
22. Buka Detail user Rina P, tab System Log, dan cari entri yang sama
23. Verifikasi entri System Log Detail user Rina P baru: Action `Resubmit (Trial)`, Object `Client Subscription`, Name `Optik Cahaya C+{runId}-117`, Field `Status`, Old `—`, New `Active`

## Notes

- Aksi pemicu tiap blok adalah aksi pada kolom Dependensi TC (bukan Langkah Uji TC ini); spec memicunya lewat sesi API aktor yang sama dan menulis langkah pemicu "... hingga ... tersimpan" (R-20). Sesi API bukan konteks kedua dan tidak memakai `P-2`.
- Langkah penghubung (S-03): langkah Search untuk menemukan entri target di modal Changelog (R-16), langkah menyaring Object `Client Subscription` di Activity Log, dan langkah `Buka menu Allocation > Client Subscription` (langkah 9 dan 17) yang membuka List kembali sesudah Activity Log dan System Log atau sesudah login sebelum modal Changelog dibuka.
- Temuan untuk QA:
  - Aksi pemicu terletak di TC pada kolom Dependensi, tanpa endpoint, payload, atau data kunci (nama Client, plan, nilai) di Langkah Uji TC ini; spec mengambil nama Client, plan, dan nilai dari Expected TC dan memicu aksi lewat sesi API yang kemampuannya tidak tertulis di TC, PRD, atau LLD (disediakan tim BE/FE).
  - Precondition TC menyebut aktor Create-Only atau Group Manager membuka Activity Log dan Detail user tab System Log; hak akses role itu ke surface tersebut tidak dinyatakan di TC. Spec mengikuti Precondition TC.
  - TC-AC-CS-616 memakai data Dinamis #9 dan toggle Trial OFF yang tidak dijelaskan cara mengatur dan memulihkannya; spec memakai kemampuan tim FE/BE.
