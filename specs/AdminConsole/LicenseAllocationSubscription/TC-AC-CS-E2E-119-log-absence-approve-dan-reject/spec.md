---
id: TC-AC-CS-E2E-119-log-absence-approve-dan-reject
title: "Log Absence: Approve dan Reject"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AC-CS-442
  - TC-AC-CS-443
  - TC-AC-CS-617
coverage:
  web: automated
---

# Log Absence: Approve dan Reject

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Total Control Principal PT ABC (Pre-setup #1) `totalControlSub_automated_{namaCompany}@qwertysystem.net` (`Hendra Wijaya`), password `Spectra.env.AC_SUB_TC_PASSWORD`; login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Email dan identitas data Pre-setup dirujuk lewat `Fixture.license-allocation-subscription` (belum ada; disediakan tim FE). Nama env var password di atas didaftarkan di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example` oleh tim FE, sesuai `suite.md`.
- Suite berjalan serial (`parallel: false`). Hook `beforeEach` suite membuka Allocation > Client Subscription tab Current dan menjadi jaring pengaman S-09 (lihat `suite.md`); flag Guided Tooltip diatur hook suite (`seen`), sehingga walkthrough tidak muncul.
- Sesi API aktor: aksi pemicu (kolom Dependensi TC) dijalankan lewat login API akun aktor sesuai `suite.md`; kemampuan menulis lewat API, endpoint, dan payloadnya tidak tertulis di TC, PRD, atau LLD sehingga disediakan tim BE/FE (S-13). Sesi UI aktor tidak terpengaruh (bagian 5).
- Baseline S-12: jumlah entri Changelog, Activity Log, dan System Log per Client, Action, dan user pelaku dicatat di hook `before` lewat kemampuan membaca audit trail (disediakan tim FE/BE, bagian 8b butir 10) sebelum aksi pemicu pertama; Changelog, Activity Log, dan System Log adalah audit trail permanen sehingga asersi "entri baru" memakai selisih terhadap baseline itu dan entri dicari lewat Action, Client, dan email pelaku (bukan posisi teratas).
- Data seed milik spec, dibuat lewat sesi API aktor di hook `before` dan dibersihkan di hook `after` (S-06, S-12; bersuffix `+{runId}-119`). Spec tidak menulis ke baris Pre-setup bersama dan tidak memerlukan langkah pemulihan antar blok; entri audit trail (Changelog, Activity Log, System Log) yang dihasilkan aksi pemicu permanen dan dibaca lewat selisih terhadap baseline. Satu seed per blok, diputuskan oleh approver `Eko Saputra` (Pre-setup #9, `totalControlDistSub_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_SUB_DIST_TC_PASSWORD`) lewat sesi API; requester dan approver tidak login lewat UI:
  1. TC-AC-CS-442: Client `Apotek Sehat Sentosa+{runId}-119` dengan pengajuan FAMS plan Growth Waiting for Approval, requester `Fajar N` (bentuk Pre-setup #49).
  2. TC-AC-CS-443: Client `Toko Serba Ada+{runId}-119` dengan predecessor FAMS plan Professional Active (01/09/25 sampai 31/08/26) dan successor Renewal plan Enterprise Waiting for Approval (bentuk Pre-setup #67 dan #68).
  3. TC-AC-CS-617: Client `Toko Persetujuan+{runId}-119` dengan pengajuan SAMS plan Growth Waiting for Approval, Duration 1, Start Date `15/09/26` (hasil Approve Pending), requester `Fajar N` (bentuk Pre-setup #124).
- Kemampuan teknis (disediakan tim FE/BE): jam server dan jam browser diatur absolut ke tanggal acuan `19/08/26` (fixture waktu, disediakan tim FE/BE), dipulihkan di hook `after`.
- Kelas asersi absence (g): asersi "tidak ada entri Approve atau Reject di Changelog" didahului `Verifikasi` anchor positif pada permukaan yang sama (bagian 8b butir 2) dan memakai baseline jumlah entri (S-12). Pemicu Approve dan Reject adalah kondisi yang diasersi, bukan objek uji (P-5 butir a).

## Test Steps

### TC-AC-CS-442: Log Approve: tidak ada di Changelog, tercatat di Activity Log dan System Log approver

1. Pemicu (sesi API Eko S): Approve pengajuan Waiting for Approval `Apotek Sehat Sentosa+{runId}-119 — FAMS` sebagai approver hingga perubahan tersimpan
2. Buka modal Changelog dan ketik Search `Apotek Sehat Sentosa+{runId}-119`, tekan Enter
3. Verifikasi tabel Changelog menampilkan sedikitnya satu entri lain (anchor positif)
4. Verifikasi tidak ada entri Action `Approve` pada Client — Product `Apotek Sehat Sentosa+{runId}-119 — FAMS` di Changelog
5. Buka Admin Console > Activity Log, saring Object `Client Subscription`, dan cari entri Approve
6. Verifikasi entri Activity Log `Client Subscription` baru: Name `Apotek Sehat Sentosa+{runId}-119 — FAMS`, Action `Approve`, Field `Status`, Old `Waiting for Approval`, New `Active`, Modified By `Eko S`
7. Buka Detail user Eko S, tab System Log, dan cari entri yang sama
8. Verifikasi entri System Log Detail user Eko S baru: Action `Approve`, Object `Client Subscription`, Name `Apotek Sehat Sentosa+{runId}-119 — FAMS`, Field `Status`, Old `Waiting for Approval`, New `Active`
9. Verifikasi Modified By adalah approver dan bukan requester
10. Buka Allocation > Client Subscription (tab Current), ketik Search `Apotek Sehat Sentosa+{runId}-119`, tekan Enter
11. Buka modal Subscription Log term `Apotek Sehat Sentosa+{runId}-119 — FAMS`
12. Verifikasi Subscription Log term memuat entri `Subscription approved by Eko Saputra`

### TC-AC-CS-443: Log Reject: tidak ada di Changelog, tercatat di Activity Log dan System Log approver

13. Pemicu (sesi API Eko S): Reject pengajuan Waiting for Approval `Toko Serba Ada+{runId}-119 — FAMS` sebagai approver hingga perubahan tersimpan
14. Tutup modal Subscription Log, buka modal Changelog dan ketik Search `Toko Serba Ada+{runId}-119`, tekan Enter
15. Verifikasi tabel Changelog menampilkan sedikitnya satu entri lain (anchor positif)
16. Verifikasi tidak ada entri Action `Reject` pada Client — Product `Toko Serba Ada+{runId}-119 — FAMS` di Changelog
17. Buka Admin Console > Activity Log, saring Object `Client Subscription`, dan cari entri Reject
18. Verifikasi entri Activity Log `Client Subscription` baru: Name `Toko Serba Ada+{runId}-119 — FAMS`, Action `Reject`, Field `Status`, Old `Waiting for Approval`, New `Rejected`, Modified By `Eko S`
19. Buka Detail user Eko S, tab System Log, dan cari entri yang sama
20. Verifikasi entri System Log Detail user Eko S baru: Action `Reject`, Object `Client Subscription`, Name `Toko Serba Ada+{runId}-119 — FAMS`, Field `Status`, Old `Waiting for Approval`, New `Rejected`
21. Buka Allocation > Client Subscription, klik tab "History", ketik Search `Toko Serba Ada+{runId}-119`, tekan Enter
22. Buka modal Subscription Log term `Toko Serba Ada+{runId}-119 — FAMS`
23. Verifikasi Subscription Log term memuat tepat satu record audit `Subscription rejected by Eko Saputra`

### TC-AC-CS-617: Log Approve term yang hasilnya Pending

24. Pemicu (sesi API Eko S): Approve pengajuan Waiting for Approval `Toko Persetujuan+{runId}-119 — SAMS` yang hasilnya Pending sebagai approver hingga perubahan tersimpan
25. Buka Allocation > Client Subscription (tab Current), buka modal Changelog dan ketik Search `Toko Persetujuan+{runId}-119`, tekan Enter
26. Verifikasi tabel Changelog menampilkan sedikitnya satu entri lain (anchor positif)
27. Verifikasi tidak ada entri Action `Approve` pada Client — Product `Toko Persetujuan+{runId}-119 — SAMS` di Changelog
28. Buka Admin Console > Activity Log, saring Object `Client Subscription`, dan cari entri Approve
29. Verifikasi entri Activity Log `Client Subscription` baru: Name `Toko Persetujuan+{runId}-119 — SAMS`, Action `Approve`, Field `Status`, Old `Waiting for Approval`, New `Pending`, Modified By `Eko S`
30. Buka Detail user Eko S, tab System Log, dan cari entri yang sama
31. Verifikasi entri System Log Detail user Eko S baru: Action `Approve`, Object `Client Subscription`, Name `Toko Persetujuan+{runId}-119 — SAMS`, Field `Status`, Old `Waiting for Approval`, New `Pending`
32. Verifikasi Modified By adalah approver dan bukan requester

## Notes

- Aksi pemicu tiap blok adalah aksi pada kolom Dependensi TC (bukan Langkah Uji TC ini); spec memicunya lewat sesi API aktor yang sama dan menulis langkah pemicu "... hingga ... tersimpan" (R-20). Sesi API bukan konteks kedua dan tidak memakai `P-2`.
- P-5 butir a: spec absence memuat pemicu Approve dan Reject lewat sesi API approver hanya untuk membentuk kondisi yang diasersi; tiap TC punya data dan baseline sendiri.
- Anchor positif asersi absence: entri lain yang tampil pada Changelog dan, untuk bagian presence, entri Activity Log dan System Log approver yang diasersi sesudahnya. TC-AC-CS-442, 443, dan 617 terbelah antara presence (Activity Log, System Log) dan absence (Changelog); ketiganya hanya ada di spec ini (S-05).
- Langkah penghubung (S-03): langkah Search untuk menemukan entri target di modal Changelog (R-16), langkah menyaring Object `Client Subscription` di Activity Log, langkah kembali ke daftar (Allocation > Client Subscription, tab Current atau History untuk term Rejected) dan Search Client seed sebelum membuka Subscription Log term, serta langkah menutup modal Subscription Log sebelum membuka Changelog.
- Temuan untuk QA:
  - Aksi pemicu terletak di TC pada kolom Dependensi, tanpa endpoint, payload, atau data kunci (nama Client, plan, nilai) di Langkah Uji TC ini; spec mengambil nama Client, plan, dan nilai dari Expected TC dan memicu aksi lewat sesi API yang kemampuannya tidak tertulis di TC, PRD, atau LLD (disediakan tim BE/FE).
  - TC-AC-CS-442 Expected e dan TC-AC-CS-443 Expected d memuat asersi Subscription Log yang tidak berasal dari Langkah Uji; spec membukanya sebagai langkah tambahan (S-03).
  - TC-AC-CS-617 Expected d (Modified By adalah approver dan bukan requester) tidak menyebut identitas requester; spec mengasersi Modified By `Eko S`.
