---
id: TC-AC-CS-E2E-112-log-aksi-renew
title: "Log Aksi: Renew"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-CS-435
  - TC-AC-CS-437
  - TC-AC-CS-613
  - TC-AC-CS-436
coverage:
  web: automated
---

# Log Aksi: Renew

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Total Control Principal PT ABC (Pre-setup #1) `totalControlSub_automated_{namaCompany}@qwertysystem.net` (`Hendra Wijaya`), password `Spectra.env.AC_SUB_TC_PASSWORD`; login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Akun aktor berikutnya (ganti akun dengan langkah eksplisit): Create-Only (capability Create saja), Distributor PT Maju Bersama (Pre-setup #6) `createOnlySub_automated_{namaCompany}@qwertysystem.net` (`Fajar Nugroho`), password `Spectra.env.AC_SUB_CREATE_PASSWORD`; login pada langkah ganti akun, dan hook `after` mengembalikan sesi ke akun default suite (Pre-setup #1).
- Email dan identitas data Pre-setup dirujuk lewat `Fixture.license-allocation-subscription` (belum ada; disediakan tim FE). Nama env var password di atas didaftarkan di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example` oleh tim FE, sesuai `suite.md`.
- Suite berjalan serial (`parallel: false`). Hook `beforeEach` suite membuka Allocation > Client Subscription tab Current dan menjadi jaring pengaman S-09 (lihat `suite.md`); flag Guided Tooltip diatur hook suite (`seen`), sehingga walkthrough tidak muncul.
- Kemampuan teknis (disediakan tim FE/BE): jam server dan jam browser diatur absolut ke tanggal acuan `19/08/26` (fixture waktu, disediakan tim FE/BE), dipulihkan di hook `after`.
- Sesi API aktor: aksi pemicu (kolom Dependensi TC) dijalankan lewat login API akun aktor sesuai `suite.md`; kemampuan menulis lewat API, endpoint, dan payloadnya tidak tertulis di TC, PRD, atau LLD sehingga disediakan tim BE/FE (S-13). Sesi UI aktor tidak terpengaruh (bagian 5).
- Baseline S-12: jumlah entri Changelog, Activity Log, dan System Log per Client, Action, dan user pelaku dicatat di hook `before` lewat kemampuan membaca audit trail (disediakan tim FE/BE, bagian 8b butir 10) sebelum aksi pemicu pertama; Changelog, Activity Log, dan System Log adalah audit trail permanen sehingga asersi "entri baru" memakai selisih terhadap baseline itu dan entri dicari lewat Action, Client, dan email pelaku (bukan posisi teratas).
- Data seed milik spec, dibuat lewat sesi API aktor di hook `before` dan dibersihkan di hook `after` (S-06, S-12; bersuffix `+{runId}-112`). Spec tidak menulis ke baris Pre-setup bersama dan tidak memerlukan langkah pemulihan antar blok karena tiap blok memakai Client seed sendiri; entri audit trail (Changelog, Activity Log, System Log) yang dihasilkan aksi pemicu permanen dan dibaca lewat selisih terhadap baseline. Satu seed per blok:
  1. TC-AC-CS-435: Client `Bengkel Maju Jaya+{runId}-112` dengan term SAMS plan Growth status Expired (End Date lampau, masih dalam Grace End), Plan Owner CV Karya Mandiri (Partner) (bentuk Pre-setup #50).
  2. TC-AC-CS-437: Client `Warung Kopi Senja A+{runId}-112` pada group `Jawa` dengan term FAMS plan Professional status Active, Plan Owner PT Maju Bersama (Distributor) (bentuk Pre-setup #69).
  3. TC-AC-CS-613: Client `CV Mitra Sejati+{runId}-112` dengan term FAMS status Grace, Plan Owner PT ABC (Principal) (bentuk Pre-setup #51).
  4. TC-AC-CS-436: Client `Warung Kopi Senja B+{runId}-112` pada group `Jawa` dengan term FAMS plan Professional status Active, Plan Owner PT Maju Bersama (Distributor), dapat diajukan Renew oleh `Fajar Nugroho` (bentuk Pre-setup #69).

## Test Steps

### TC-AC-CS-435: Log Renew efek langsung

1. Pemicu (sesi API): lakukan Renew efek langsung pada term Expired `Bengkel Maju Jaya+{runId}-112 — SAMS` hingga perubahan tersimpan
2. Buka modal Changelog, ketik Search `Bengkel Maju Jaya+{runId}-112`, tekan Enter, dan cari entri Action `Renew (efek langsung)`
3. Verifikasi entri Changelog baru (selisih satu terhadap baseline): Action `Renew (efek langsung)`, Client — Product `Bengkel Maju Jaya+{runId}-112 — SAMS`, Field `Status`, Old Value `Expired`, New Value `Active`, Modified By `Hendra W`
4. Buka Admin Console > Activity Log, saring Object `Client Subscription`, dan cari entri yang sama
5. Verifikasi entri Activity Log `Client Subscription` baru: Name `Bengkel Maju Jaya+{runId}-112 — SAMS`, Action `Renew (efek langsung)`, Field `Status`, Old `Expired`, New `Active`, Modified By `Hendra W`
6. Buka Detail user Hendra W, tab System Log, dan cari entri yang sama
7. Verifikasi entri System Log Detail user Hendra W baru: Action `Renew (efek langsung)`, Object `Client Subscription`, Name `Bengkel Maju Jaya+{runId}-112 — SAMS`, Field `Status`, Old `Expired`, New `Active`

### TC-AC-CS-437: Log Schedule Renewal efek terjadwal pada submit

8. Pemicu (sesi API): ajukan Renew efek terjadwal ke plan Professional berlaku 01/09/26 pada term `Warung Kopi Senja A+{runId}-112 — FAMS` hingga perubahan tersimpan
9. Buka menu Allocation > Client Subscription
10. Buka modal Changelog, ketik Search `Warung Kopi Senja A+{runId}-112`, tekan Enter, dan cari entri Action `Schedule Renewal (efek terjadwal, submit)`
11. Verifikasi entri Changelog baru (selisih satu terhadap baseline): Action `Schedule Renewal (efek terjadwal, submit)`, Client — Product `Warung Kopi Senja A+{runId}-112 — FAMS`, Field `Pending Renewal`, Old Value `—`, New Value `Professional, effective 01/09/26`, Modified By `Hendra W`
12. Buka Admin Console > Activity Log, saring Object `Client Subscription`, dan cari entri yang sama
13. Verifikasi entri Activity Log `Client Subscription` baru: Name `Warung Kopi Senja A+{runId}-112 — FAMS`, Action `Schedule Renewal (efek terjadwal, submit)`, Field `Pending Renewal`, Old `—`, New `Professional, effective 01/09/26`, Modified By `Hendra W`
14. Buka Detail user Hendra W, tab System Log, dan cari entri yang sama
15. Verifikasi entri System Log Detail user Hendra W baru: Action `Schedule Renewal (efek terjadwal, submit)`, Object `Client Subscription`, Name `Warung Kopi Senja A+{runId}-112 — FAMS`, Field `Pending Renewal`, Old `—`, New `Professional, effective 01/09/26`

### TC-AC-CS-613: Log Renew efek langsung atas predecessor Grace

16. Pemicu (sesi API): lakukan Renew efek langsung pada term Grace `CV Mitra Sejati+{runId}-112 — FAMS` hingga perubahan tersimpan
17. Buka menu Allocation > Client Subscription
18. Buka modal Changelog, ketik Search `CV Mitra Sejati+{runId}-112`, tekan Enter, dan cari entri Action `Renew (efek langsung)`
19. Verifikasi entri Changelog baru (selisih satu terhadap baseline): Action `Renew (efek langsung)`, Client — Product `CV Mitra Sejati+{runId}-112 — FAMS`, Field `Status`, Old Value `Grace`, New Value `Active`, Modified By `Hendra W`
20. Buka Admin Console > Activity Log, saring Object `Client Subscription`, dan cari entri yang sama
21. Verifikasi entri Activity Log `Client Subscription` baru: Name `CV Mitra Sejati+{runId}-112 — FAMS`, Action `Renew (efek langsung)`, Field `Status`, Old `Grace`, New `Active`, Modified By `Hendra W`
22. Buka Detail user Hendra W, tab System Log, dan cari entri yang sama
23. Verifikasi entri System Log Detail user Hendra W baru: Action `Renew (efek langsung)`, Object `Client Subscription`, Name `CV Mitra Sejati+{runId}-112 — FAMS`, Field `Status`, Old `Grace`, New `Active`
24. Ganti akun: klik Logout dari akun sebelumnya
25. Login sebagai `Fajar Nugroho` (`createOnlySub_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_SUB_CREATE_PASSWORD`)

### TC-AC-CS-436: Log Renew request pada submit

26. Pemicu (sesi API): kirim pengajuan Renew pada term `Warung Kopi Senja B+{runId}-112 — FAMS` sebagai requester hingga perubahan tersimpan
27. Buka menu Allocation > Client Subscription
28. Buka modal Changelog, ketik Search `Warung Kopi Senja B+{runId}-112`, tekan Enter, dan cari entri Action `Renew (request, submit)`
29. Verifikasi entri Changelog baru (selisih satu terhadap baseline): Action `Renew (request, submit)`, Client — Product `Warung Kopi Senja B+{runId}-112 — FAMS`, Field `Status`, Old Value `—`, New Value `Waiting for Approval`, Modified By `Fajar N`
30. Buka Admin Console > Activity Log, saring Object `Client Subscription`, dan cari entri yang sama
31. Verifikasi entri Activity Log `Client Subscription` baru: Name `Warung Kopi Senja B+{runId}-112 — FAMS`, Action `Renew (request, submit)`, Field `Status`, Old `—`, New `Waiting for Approval`, Modified By `Fajar N`
32. Buka Detail user Fajar N, tab System Log, dan cari entri yang sama
33. Verifikasi entri System Log Detail user Fajar N baru: Action `Renew (request, submit)`, Object `Client Subscription`, Name `Warung Kopi Senja B+{runId}-112 — FAMS`, Field `Status`, Old `—`, New `Waiting for Approval`

## Notes

- Aksi pemicu tiap blok adalah aksi pada kolom Dependensi TC (bukan Langkah Uji TC ini); spec memicunya lewat sesi API aktor yang sama dan menulis langkah pemicu "... hingga ... tersimpan" (R-20). Sesi API bukan konteks kedua dan tidak memakai `P-2`.
- Urutan blok: TC-AC-CS-435, 437, dan 613 (akun Principal) lebih dulu, lalu TC-AC-CS-436 (akun Create-Only) sesudah ganti akun, agar ganti akun hanya satu kali (S-10).
- Langkah penghubung (S-03): langkah Search untuk menemukan entri target di modal Changelog (R-16), langkah menyaring Object `Client Subscription` di Activity Log, dan langkah `Buka menu Allocation > Client Subscription` (langkah 9, 17, dan 27) yang membuka List kembali sesudah Activity Log dan System Log atau sesudah login sebelum modal Changelog dibuka.
- Temuan untuk QA:
  - Aksi pemicu terletak di TC pada kolom Dependensi, tanpa endpoint, payload, atau data kunci (nama Client, plan, nilai) di Langkah Uji TC ini; spec mengambil nama Client, plan, dan nilai dari Expected TC dan memicu aksi lewat sesi API yang kemampuannya tidak tertulis di TC, PRD, atau LLD (disediakan tim BE/FE).
  - Precondition TC menyebut aktor Create-Only atau Group Manager membuka Activity Log dan Detail user tab System Log; hak akses role itu ke surface tersebut tidak dinyatakan di TC. Spec mengikuti Precondition TC.
  - TC-AC-CS-437 dan TC-AC-CS-436 memakai Client seed terpisah (`Warung Kopi Senja A+{runId}-112` dan `Warung Kopi Senja B+{runId}-112`) karena TC menyebut term `Warung Kopi Senja — FAMS` yang sama; spec menjaga isolasi antar blok dengan seed, bukan dengan langkah pemulihan.
