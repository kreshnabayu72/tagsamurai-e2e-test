---
id: TC-AC-CS-E2E-124-subscription-log-katalog-created-approved-rejected-edited
title: "Subscription Log: Katalog Created, Approved, Rejected, Edited"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-CS-594
  - TC-AC-CS-595
  - TC-AC-CS-596
  - TC-AC-CS-597
  - TC-AC-CS-598
coverage:
  web: automated
---

# Subscription Log: Katalog Created, Approved, Rejected, Edited

## Prerequisites

- Mode: FE+BE.
- Akun aktor UI: Total Control Principal (Pre-setup #1) `totalControlSub_automated_{namaCompany}@qwertysystem.net` (`Hendra Wijaya`), password `Spectra.env.AC_SUB_TC_PASSWORD`; login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Akun pemicu lewat sesi API (bukan sesi UI), semua dijalankan di hook `before` spec ini dengan urutan yang ditulis di bawah:

| Pre-setup | Email | Peran | Env password |
|---|---|---|---|
| #5 | `groupManagerSub_automated_{namaCompany}@qwertysystem.net` (`Dewi Anggraini`) | Group Manager Distributor, bypass approval | `Spectra.env.AC_SUB_GM_PASSWORD` |
| #6 | `createOnlySub_automated_{namaCompany}@qwertysystem.net` (`Fajar Nugroho`) | Create-Only Distributor | `Spectra.env.AC_SUB_CREATE_PASSWORD` |
| #9 | `totalControlDistSub_automated_{namaCompany}@qwertysystem.net` (`Eko Saputra`) | Total Control Distributor (approver) | `Spectra.env.AC_SUB_DIST_TC_PASSWORD` |

- Email dan identitas data Pre-setup dirujuk lewat `Fixture.license-allocation-subscription` (belum ada; disediakan tim FE). Nama env var password adalah usulan: belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`, didaftarkan tim FE.
- Data milik spec, dibuat lewat API di hook `before` dan dibersihkan di hook `after` (S-06, S-12; bersuffix `+{runId}-124`). Tidak ada baris Pre-setup bersama yang ditulis spec ini; entri Changelog, Subscription Log, dan Activity Log yang terbentuk bersifat permanen. Subscription ID yang dibentuk sistem dibaca lewat API seeding:
  1. Client `Client Tanpa Subscription+{runId}-124` tanpa term (setara #48), dipakai TC-AC-CS-594 dan 596.
  2. Client `Warung Kopi Senja+{runId}-124` dengan term Active FAMS Professional `{idAsal595}` (setara `SUBS-20250815-00001`, #69).
  3. Client `Apotek Sehat Sentosa+{runId}-124` dengan pengajuan Waiting for Approval FAMS Growth dibuat oleh `Fajar Nugroho` (setara #49).
  4. Client `Toko Persetujuan+{runId}-124` dengan pengajuan mode New SAMS Growth Start Date `15/09/26` Waiting for Approval (setara #124).
  5. Client `Toko Serba Ada+{runId}-124` dengan pengajuan Renewal FAMS Enterprise Waiting for Approval `{idReject598}` dan Previous Subscription `{idPrev598}` (setara `SUBS-20260819-00003` dan `SUBS-20250901-00001`).
- Aksi pemicu (kolom Dependensi TC; endpoint tulis tidak tertulis di TC, PRD, atau LLD sehingga ditulis sebagai kemampuan sesi API aktor "disediakan tim FE/BE", lihat Temuan untuk QA), dijalankan hingga tersimpan, lalu waktu aksi dicatat sesudah aksi terakhir tiap pemicu:
  1. TC-AC-CS-594: `Dewi Anggraini` membuat term SAMS Growth untuk Client `Client Tanpa Subscription+{runId}-124`, Duration `1`, Start Date `19/08/26`, bypass (term langsung Active).
  2. TC-AC-CS-595: `Fajar Nugroho` mengajukan Renew `{idAsal595}` Client `Warung Kopi Senja+{runId}-124` FAMS dengan Keep current plan, Duration `1`, toggle Require Approval ON (successor Waiting for Approval; Previous Subscription `{idAsal595}`).
  3. TC-AC-CS-596: `Hendra Wijaya` mengaktifkan trial FAMS Growth untuk Client `Client Tanpa Subscription+{runId}-124`, Trial Duration `30`, Asset Quota `50`, Concurrent User Quota `10`.
  4. TC-AC-CS-597: `Eko Saputra` meng-Approve pengajuan Client `Apotek Sehat Sentosa+{runId}-124` FAMS Growth tanpa catatan, dan pengajuan mode New Start Date `15/09/26` Client `Toko Persetujuan+{runId}-124` SAMS Growth dengan catatan `Disetujui sesuai kontrak`.
  5. TC-AC-CS-598: `Eko Saputra` meng-Reject pengajuan Renewal Client `Toko Serba Ada+{runId}-124` FAMS Enterprise (`{idReject598}`, Previous Subscription `{idPrev598}`) dengan Rejection Reason `Budget pengajuan belum disetujui`.
- Seed dan efek pemicu dibersihkan di hook `after`. Pembuka Subscription Log tidak mengubah data.
- Kemampuan teknis (disediakan tim FE/BE): sesi API aktor; pemulihan state Pre-setup; jam server dan jam browser diatur absolut ke tanggal acuan `19/08/26` (fixture waktu), dipulihkan di hook `after`. Jam server dan jam browser sinkron; Date & Time entri dibandingkan dengan waktu aksi pemicu dengan toleransi satu menit (S-12).
- Hook suite (lihat `suite.md`): `beforeEach` membuka Allocation > Client Subscription tab Current dan menjadi jaring pengaman S-09; flag Guided Tooltip diatur `seen`. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AC-CS-594: Entri Subscription created term Paid mode New tanpa approval

1. Ketik Search `Client Tanpa Subscription+{runId}-124`, tekan Enter
2. Klik ikon `⋯` pada baris term SAMS Client `Client Tanpa Subscription+{runId}-124`, klik `Subscription Log`
3. Verifikasi modal memuat entri `Subscription created by Dewi Anggraini` (tepat satu entri)
4. Verifikasi Date & Time entri sesuai waktu aksi pemicu (toleransi satu menit)
5. Verifikasi baris Description `Type: Paid`, `Plan: Growth`, `Duration: 1 year(s)`, dan `Start Date: 19/08/26`
6. Verifikasi tidak ada baris `Previous Subscription` maupun `Resubmitted From`
7. Verifikasi tidak ada entri `Subscription approved`
8. Verifikasi header `Status:` badge Active
9. Klik `[✕]`

### TC-AC-CS-595: Entri Subscription created term Renewal memuat Previous Subscription tanpa Start Date

10. Ganti isi kotak search dengan `Warung Kopi Senja+{runId}-124`, tekan Enter
11. Klik ikon `⋯` pada successor Waiting for Approval Client `Warung Kopi Senja+{runId}-124` FAMS, klik `Subscription Log`
12. Verifikasi entri `Subscription created by Fajar Nugroho` dengan baris Description `Type: Paid`, `Plan: Professional`, `Duration: 1 year(s)`, dan `Previous Subscription: {idAsal595}`
13. Verifikasi tidak ada baris `Start Date` maupun `Resubmitted From`
14. Verifikasi header `Client:` Warung Kopi Senja+{runId}-124
15. Verifikasi header `Product:` FAMS
16. Verifikasi header `Status:` badge Waiting for Approval
17. Klik `[✕]`

### TC-AC-CS-596: Entri Subscription created baris Trial memuat kuota sesuai Product

18. Ganti isi kotak search dengan `Client Tanpa Subscription+{runId}-124`, tekan Enter
19. Klik ikon `⋯` pada baris Trial Client `Client Tanpa Subscription+{runId}-124`, klik `Subscription Log`
20. Verifikasi entri `Subscription created by Hendra Wijaya` dengan baris Description `Type: Trial`, `Plan: Growth`, `Duration: 30 days`, `Asset Quota: 50`, dan `Concurrent User Quota: 10`
21. Verifikasi tidak ada baris `Start Date`, `Previous Subscription`, `Log Source Quota`, maupun `Resubmitted From`
22. Verifikasi header `Plan:` Growth
23. Verifikasi header `Status:` badge Active
24. Klik `[✕]`

### TC-AC-CS-597: Entri Subscription approved, Approval Note hanya bila diisi

25. Ganti isi kotak search dengan `Apotek Sehat Sentosa+{runId}-124`, tekan Enter
26. Klik ikon `⋯` pada term `Apotek Sehat Sentosa+{runId}-124` FAMS hasil Approve, klik `Subscription Log`
27. Verifikasi entri teratas `Subscription approved by Eko Saputra` tanpa baris Description
28. Verifikasi di bawahnya entri `Subscription created by Fajar Nugroho`
29. Klik `[✕]`
30. Ganti isi kotak search dengan `Toko Persetujuan+{runId}-124`, tekan Enter
31. Klik ikon `⋯` pada term `Toko Persetujuan+{runId}-124` SAMS Start Date `15/09/26` hasil Approve, klik `Subscription Log`
32. Verifikasi modal memuat entri teratas `Subscription approved by Eko Saputra` dengan `Approval Note: Disetujui sesuai kontrak`
33. Verifikasi header `Status:` badge Pending
34. Verifikasi tidak ada entri `Subscription activated`
35. Klik `[✕]`

### TC-AC-CS-598: Entri Subscription rejected memuat Rejection Reason

36. Klik tab `History`
37. Ganti isi kotak search dengan `{idReject598}`, tekan Enter
38. Klik ikon `⋯` pada baris `{idReject598}` Client `Toko Serba Ada+{runId}-124`, klik `Subscription Log`
39. Verifikasi entri teratas `Subscription rejected by Eko Saputra` dengan `Rejection Reason: Budget pengajuan belum disetujui`
40. Verifikasi di bawahnya entri `Subscription created by Fajar Nugroho` dengan `Type: Paid`, `Plan: Enterprise`, dan `Previous Subscription: {idPrev598}`
41. Verifikasi header `Status:` badge Rejected dengan severity danger
42. Klik `[✕]`

## Notes

- Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): langkah 1, 10, 18, 25, 30, 37 (Search untuk menemukan baris target, R-16; mengganti isi kotak Search memakai idiom bagian 8b butir 9), langkah 9, 17, 24, 29, 35, 42 (menutup modal), dan langkah 36 (pindah tab).
- Aksi pemicu dijalankan di hook `before` (S-04, seeding API), bukan langkah di Test Steps; pelaku kedua lewat sesi API bukan konteks kedua (`P-2` tidak dipakai).
- Spec ini melewati ~35 langkah (42). Alasan: satu topik (katalog entri Subscription Log record seeded) dan satu permukaan, tiap blok membaca log record berbeda sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna, dan semua aksi pemicu memakai satu hook `before`; pemecahan hanya menambah login dan hook.
- TC-AC-CS-594 Expected d dan TC-AC-CS-597 Expected c ("tanpa entri approved/activated") ditulis sebagai asersi state/jumlah pada modal dengan anchor entri yang tampil di modal yang sama, bukan kelas g.
- Temuan untuk QA:
  - Aksi pemicu pada kolom Dependensi TC (TC-AC-CS-143, 151, 199, 297, 298, 302) tidak punya endpoint tulis di TC, PRD, atau LLD; spec memakai kemampuan sesi API aktor yang disediakan tim FE/BE tanpa endpoint karangan (S-13, R-19).
  - TC-AC-CS-594 langkah 1 menyebut Client `Client Tanpa Subscription` yang tidak punya nomor Pre-setup; dirujuk lewat fixture yang disediakan tim FE (S-11).
  - TC-AC-CS-597 mengacu mode New `Toko Persetujuan` ke Pre-setup #124; kolom Plan Owner/Client dari pengajuan itu tidak tertulis di TC, sehingga spec tidak mengasersinya.
  - TC-AC-CS-595 Expected a tidak menyebut apakah entri `Subscription created` itu satu-satunya entri successor; spec tidak mengasersi jumlah entri.
