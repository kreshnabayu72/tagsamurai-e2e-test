---
id: TC-AC-CS-E2E-125-subscription-log-katalog-canceled-archived-activated
title: "Subscription Log: Katalog Canceled, Archived, Activated"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-CS-599
  - TC-AC-CS-600
  - TC-AC-CS-601
  - TC-AC-CS-605
coverage:
  web: automated
---

# Subscription Log: Katalog Canceled, Archived, Activated

## Prerequisites

- Mode: FE+BE.
- Akun aktor UI: Total Control Principal (Pre-setup #1) `totalControlSub_automated_{namaCompany}@qwertysystem.net` (`Hendra Wijaya`), password `Spectra.env.AC_SUB_TC_PASSWORD`; login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Akun pemicu lewat sesi API (bukan sesi UI), semua dijalankan di hook `before` spec ini:

| Pre-setup | Email | Peran | Env password |
|---|---|---|---|
| #6 | `createOnlySub_automated_{namaCompany}@qwertysystem.net` (`Fajar Nugroho`) | Create-Only Distributor | `Spectra.env.AC_SUB_CREATE_PASSWORD` |
| #5 | `groupManagerSub_automated_{namaCompany}@qwertysystem.net` (`Dewi Anggraini`) | Group Manager Distributor | `Spectra.env.AC_SUB_GM_PASSWORD` |
| #1 | akun aktor UI di atas (`Hendra Wijaya`) | Total Control Principal | `Spectra.env.AC_SUB_TC_PASSWORD` |

- Email dan identitas data Pre-setup dirujuk lewat `Fixture.license-allocation-subscription` (belum ada; disediakan tim FE). Nama env var password adalah usulan: belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`, didaftarkan tim FE.
- Data milik spec, dibuat lewat API di hook `before` dan dibersihkan di hook `after` (S-06, S-12; bersuffix `+{runId}-125`). Tidak ada baris Pre-setup bersama yang ditulis spec ini; entri Changelog dan Subscription Log yang terbentuk bersifat permanen. Subscription ID yang dibentuk sistem dibaca lewat API seeding:
  1. Client `Apotek Sehat Sentosa+{runId}-125` dengan pengajuan FAMS Waiting for Approval Duration `1` (setara #49) dan term SIEM Pending Duration `1`.
  2. Client `PT Bintang Timur+{runId}-125` dengan trial Active.
  3. Term Pending `{idPending600}` (setara `{idPending600}`).
  4. Predecessor `{idPred601}` (setara `{idPred601}`) dengan successor Waiting for Approval `{idSucc601}` (setara `{idSucc601}`).
  5. Client `Percetakan Mega+{runId}-125` dengan term Pending FAMS (setara `SUBS-20260819-00002`, #57).
- Aksi pemicu hook `before` (berurutan, hingga tersimpan; endpoint tulis tidak tertulis di TC, PRD, atau LLD sehingga disediakan tim FE/BE, lihat Temuan untuk QA):
  1. TC-AC-CS-599: `Fajar Nugroho` mengedit Duration term `Apotek Sehat Sentosa+{runId}-125` FAMS Waiting for Approval dari `1` ke `2`; mengedit trial `PT Bintang Timur+{runId}-125` menjadi Duration `14`, Asset Quota `25`, Concurrent User Quota `5`; mengedit term Pending `Apotek Sehat Sentosa+{runId}-125` SIEM dari Duration `1` ke `2` (kembali Waiting for Approval).
  2. TC-AC-CS-600: `Fajar Nugroho` meng-Cancel Request pengajuan `Apotek Sehat Sentosa+{runId}-125` FAMS Waiting for Approval; `Dewi Anggraini` meng-Cancel Request term Pending `{idPending600}`.
  3. TC-AC-CS-601: `Hendra Wijaya` meng-Cancel Subscription predecessor `{idPred601}` yang punya successor `{idSucc601}` Waiting for Approval.
  4. TC-AC-CS-605: `Dewi Anggraini` mengedit Start Date term Pending `Percetakan Mega+{runId}-125` FAMS menjadi hari ini `19/08/26` sehingga term langsung Active.
- Seed dan efek pemicu dibersihkan di hook `after`.
- Kemampuan teknis (disediakan tim FE/BE): sesi API aktor; pemulihan state Pre-setup; jam server dan jam browser diatur absolut ke tanggal acuan `19/08/26` (fixture waktu), dipulihkan di hook `after`. Jam browser dan jam server sinkron.
- Hook suite (lihat `suite.md`): `beforeEach` membuka Allocation > Client Subscription tab Current dan menjadi jaring pengaman S-09; flag Guided Tooltip diatur `seen`. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AC-CS-599: Entri Subscription edited, satu baris per field yang berubah

1. Klik tab `History`
2. Ketik Search `Apotek Sehat Sentosa+{runId}-125`, tekan Enter
3. Klik ikon `⋯` pada term `Apotek Sehat Sentosa+{runId}-125` FAMS, klik `Subscription Log`
4. Verifikasi entri `Subscription edited by Fajar Nugroho` dengan satu baris `Duration: 2 year(s)`
5. Klik `[✕]`
6. Klik tab `Current`
7. Ganti isi kotak search dengan `PT Bintang Timur+{runId}-125`, tekan Enter
8. Klik ikon `⋯` pada baris Trial `PT Bintang Timur+{runId}-125`, klik `Subscription Log`
9. Verifikasi satu entri `Subscription edited by Fajar Nugroho` dengan tiga baris `Duration: 14 days`, `Asset Quota: 25`, dan `Concurrent User Quota: 5`
10. Klik `[✕]`
11. Ganti isi kotak search dengan `Apotek Sehat Sentosa+{runId}-125`, tekan Enter
12. Klik ikon `⋯` pada term `Apotek Sehat Sentosa+{runId}-125` SIEM, klik `Subscription Log`
13. Verifikasi entri `Subscription edited by Fajar Nugroho` dengan satu baris `Duration: 2 year(s)`, tanpa baris Description untuk perubahan Status
14. Verifikasi header `Status:` badge Waiting for Approval
15. Klik `[✕]`

### TC-AC-CS-600: Entri Subscription canceled oleh requester dan Group Manager

16. Klik tab `History`
17. Ganti isi kotak search dengan `Apotek Sehat Sentosa+{runId}-125`, tekan Enter
18. Klik ikon `⋯` pada term `Apotek Sehat Sentosa+{runId}-125` FAMS yang di-Cancel Request, klik `Subscription Log`
19. Verifikasi entri teratas `Subscription canceled by Fajar Nugroho` tanpa baris Description
20. Verifikasi header `Status:` badge Canceled
21. Klik `[✕]`
22. Ganti isi kotak search dengan `{idPending600}`, tekan Enter
23. Klik ikon `⋯` pada baris `{idPending600}`, klik `Subscription Log`
24. Verifikasi entri teratas `Subscription canceled by Dewi Anggraini` tanpa baris Description
25. Klik `[✕]`

### TC-AC-CS-601: Entri archived dan successor yang ikut dibatalkan memakai PIC aktor Cancel Subscription

26. Ganti isi kotak search dengan `{idPred601}`, tekan Enter
27. Klik ikon `⋯` pada baris `{idPred601}`, klik `Subscription Log`
28. Verifikasi entri teratas `Subscription archived by Hendra Wijaya` tanpa baris Description
29. Verifikasi header `Status:` badge Archive
30. Verifikasi predecessor memuat tepat satu entri `Subscription archived`
31. Klik `[✕]`
32. Ganti isi kotak search dengan `{idSucc601}`, tekan Enter
33. Klik ikon `⋯` pada baris successor `{idSucc601}`, klik `Subscription Log`
34. Verifikasi entri teratas `Subscription canceled by Hendra Wijaya` tanpa baris Description
35. Verifikasi header `Status:` badge Canceled
36. Verifikasi successor memuat tepat satu entri `Subscription canceled`
37. Klik `[✕]`

### TC-AC-CS-605: Entri Subscription activated akibat Save Edit memuat pelaku

38. Klik tab `Current`
39. Ganti isi kotak search dengan `Percetakan Mega+{runId}-125`, tekan Enter
40. Klik ikon `⋯` pada term `Percetakan Mega+{runId}-125` FAMS, klik `Subscription Log`
41. Verifikasi entri `Subscription edited by Dewi Anggraini` dengan baris Description `Start Date: 19/08/26`
42. Verifikasi entri `Subscription activated by Dewi Anggraini` tanpa baris Description, menyusul entri edited
43. Verifikasi header `Status:` badge Active

## Notes

- Subjudul `###` memetakan langkah ke id TC granular.
- Aksi pemicu dijalankan di hook `before` (S-04, seeding API); pelaku kedua lewat sesi API bukan konteks kedua (`P-2` tidak dipakai). Urutan hook mengikuti urutan pada Prerequisites, sehingga term `Apotek Sehat Sentosa` FAMS berada di tab `History` saat dibuka di langkah 1 sampai 5.
- Langkah penghubung (S-03): langkah 1, 6, 16, 38 (pindah tab), langkah 2, 7, 11, 17, 22, 26, 32, 39 (Search untuk menemukan baris target, R-16), dan langkah 5, 10, 15, 21, 25, 31, 37 (menutup modal).
- Spec ini melewati ~35 langkah (43). Alasan: satu topik (katalog entri Subscription Log berdasarkan jenis kejadian) dan satu permukaan, tiap blok membaca log record seeded berbeda sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna, dan semua pemicu memakai satu hook `before`.
- Temuan untuk QA:
  - TC-AC-CS-601 dan TC-AC-CS-598 (spec 124) memakai record yang sama di Pre-setup (`SUBS-20260819-00003`, Waiting for Approval versus Rejected); masing-masing spec memakai seed sendiri sehingga dependensi TC tidak saling mengubah state.
  - Aksi pemicu pada kolom Dependensi TC (TC-AC-CS-223, 224, 226, 233, 263, 272, 274) tidak punya endpoint tulis di TC, PRD, atau LLD (S-13).
  - TC-AC-CS-599 dan TC-AC-CS-600 memakai term `Apotek Sehat Sentosa` FAMS yang sama; pada spec ini term itu sudah Canceled saat dibuka (urutan pemicu), sehingga TC-AC-CS-599 membuka lognya dari tab `History`.
  - TC-AC-CS-600 langkah 1 menyebut term hasil Cancel Request tanpa Subscription ID; spec memakai Search nama Client.
