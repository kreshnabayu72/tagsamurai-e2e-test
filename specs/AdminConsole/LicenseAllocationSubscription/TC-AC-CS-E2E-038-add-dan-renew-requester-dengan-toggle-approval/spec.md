---
id: TC-AC-CS-E2E-038-add-dan-renew-requester-dengan-toggle-approval
title: "Add dan Renew: Requester dengan Toggle Approval"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-CS-146
  - TC-AC-CS-486
  - TC-AC-CS-142
  - TC-AC-CS-147
  - TC-AC-CS-151
coverage:
  web: automated
---

# Add dan Renew: Requester dengan Toggle Approval

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Create-Only Distributor PT Maju Bersama (capability Create saja, Pre-setup #6) `createOnlySub_automated_{namaCompany}@qwertysystem.net` (`Fajar Nugroho`), password `Spectra.env.AC_SUB_CREATE_PASSWORD`; login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Pre-setup #1).
- Email akun dan identitas data Pre-setup dirujuk lewat `Fixture.license-allocation-subscription` (belum ada; disediakan tim FE). Nama env var password di atas adalah usulan yang didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`.
- Suite berjalan serial (`parallel: false`); hook `beforeEach` suite, flag Guided Tooltip `seen`, sesi API aktor, dan fixture pemulihan state Pre-setup mengikuti `suite.md` (hook suite).
- Tanggal acuan uji `19/08/26` (Pre-setup #28): jam server dan jam browser diatur absolut ke `19/08/26` di hook `before` dan dipulihkan di hook `after` (kemampuan fixture waktu disediakan tim FE/BE).
- Data seed milik spec (dibuat lewat API di hook `before`, dihapus di hook `after`, beserta term yang dibuat spec): Client `Client Tanpa Subscription A+{runId}-038` (TC-AC-CS-146), `B+{runId}-038` (TC-AC-CS-486), dan `C+{runId}-038` (TC-AC-CS-142 dan 147) (padanan Pre-setup #48: binaan langsung PT Maju Bersama pada group `Jawa`, tanpa term dan tanpa trial, Default User beralamat email yang dibaca lewat `Fixture.license-allocation-subscription`); Client `Warung Kopi Senja+{runId}-038` dengan term Active FAMS plan Professional (Start Date 01/09/25, End Date 31/08/26, Plan Owner PT Maju Bersama, tanpa successor dan tanpa trial aktif; padanan Pre-setup #69) untuk TC-AC-CS-151; pengajuan pembanding `Pembanding+{runId}-038` berstatus Waiting for Approval di Approvals > Client Subscription (dibuat lewat API) untuk anchor absence TC-AC-CS-146.
- State global yang diubah (suite serial) dan pemulihannya di hook `after` lewat fixture BE (disediakan tim FE/BE): toggle `Require Approval for Allocation` PT Maju Bersama (Pre-setup #23) diatur OFF pada langkah 1, diubah ke ON lewat sesi API pada langkah 13, dan dipulihkan ke nilai awal di hook `after`; saldo `Main Pocket` $25,000.00 (Pre-setup #20) dan Reserve dipulihkan; harga SAMS Growth $3,000.00 per tahun (Pre-setup #27).
- Kemampuan teknis (disediakan tim FE/BE): membaca saldo, Reserve, dan Capture Wallet lewat fixture BE; mail-catcher untuk jumlah email per alamat (baseline sebelum aksi, R-11); pembacaan status App Access Client.

## Test Steps

### TC-AC-CS-146: Requester biasa dengan toggle OFF langsung terotorisasi

1. Atur toggle `Require Approval for Allocation` PT Maju Bersama OFF lewat fixture BE
2. Klik `[+ Subscription]`
3. Pilih Client `Client Tanpa Subscription A+{runId}-038`, Product `SAMS`, Plan `Growth`, Duration `1`, Start Date `19/08/26`
4. Klik `[Submit]`
5. Verifikasi toast sukses "Success, subscription has been added." muncul
6. Ketik Search `Client Tanpa Subscription A+{runId}-038`, tekan Enter
7. Verifikasi baris berstatus Active, bukan Waiting for Approval
8. Klik `(←)` pada kotak Search, lalu buka Approvals > Client Subscription dari sidebar
9. Verifikasi pengajuan pembanding `Pembanding+{runId}-038` tampil di Approvals > Client Subscription
10. Verifikasi tidak ada baris untuk Client `Client Tanpa Subscription A+{runId}-038` di Approvals > Client Subscription
11. Buka Allocation > Client Subscription dari sidebar

### TC-AC-CS-486: Toggle Require Approval for Allocation dibaca ulang pada setiap submit

12. Klik `[+ Subscription]`, lalu isi Client `Client Tanpa Subscription B+{runId}-038`, Product `SAMS`, Plan `Growth`, Duration `1`, Start Date `19/08/26`
13. Ubah toggle `Require Approval for Allocation` PT Maju Bersama menjadi ON lewat sesi API hingga perubahan tersimpan
14. Klik `[Submit]`
15. Verifikasi toast "Success, your request has been submitted for approval." muncul
16. Ketik Search `Client Tanpa Subscription B+{runId}-038`, tekan Enter
17. Verifikasi term berstatus Waiting for Approval
18. Klik `(←)` pada kotak Search

### TC-AC-CS-142: Alert info efek setelah approval untuk requester biasa dengan toggle ON

19. Klik `[+ Subscription]`
20. Pilih Client `Client Tanpa Subscription C+{runId}-038`, Product `FAMS`, Plan `Professional`, Duration `1`, Start Date `19/08/26`
21. Verifikasi Alert info di atas footer "Takes effect after approval."

### TC-AC-CS-147: Requester biasa dengan toggle ON mengajukan term Waiting for Approval

22. Ganti Product ke `SAMS` dan Plan ke `Growth`
23. Catat baseline saldo `Main Pocket` dan jumlah email ke alamat Default User Client `Client Tanpa Subscription C+{runId}-038` (fixture BE dan mail-catcher)
24. Klik `[Submit]`
25. Verifikasi toast "Success, your request has been submitted for approval." muncul
26. Ketik Search `Client Tanpa Subscription C+{runId}-038`, tekan Enter
27. Verifikasi baris baru berstatus Waiting for Approval
28. Verifikasi Start Date dan End Date baris itu "—"
29. Verifikasi Reserve $3,000.00 pada `Main Pocket` (dibaca lewat fixture BE)
30. Verifikasi tidak ada Capture pada `Main Pocket` (dibaca lewat fixture BE)
31. Klik `(←)` pada kotak Search, lalu buka Approvals > Client Subscription dari sidebar
32. Verifikasi pengajuan Client `Client Tanpa Subscription C+{runId}-038` muncul dengan Type `Add Subscription`
33. Verifikasi Activation Email belum dikirim (jumlah email ke alamat Default User sama dengan baseline)
34. Verifikasi App Access belum dikirim (dibaca lewat fixture BE)
35. Buka Allocation > Client Subscription dari sidebar

### TC-AC-CS-151: Renew oleh requester biasa dengan toggle ON menjadi Waiting for Approval tanpa menyentuh predecessor

36. Ketik Search `Warung Kopi Senja+{runId}-038`, tekan Enter
37. Klik ikon `⋯` pada baris term Active, lalu pilih `Renew`
38. Pilih Renewal Option `Keep current plan`, lalu isi Duration `1`
39. Klik `[Submit]`
40. Verifikasi toast "Success, your request has been submitted for approval." muncul
41. Verifikasi term baru berstatus Waiting for Approval dengan tanggal "—"
42. Verifikasi predecessor tetap berstatus Active
43. Ganti isi kotak search dengan `Warung Kopi Senja+{runId}-038`, tekan Enter
44. Klik ikon `⋯` pada baris predecessor Active
45. Verifikasi menu `⋯` predecessor memuat item lain selain `Renew`
46. Verifikasi row action `Renew` pada predecessor Hidden selama successor ada
47. Klik `(←)` pada kotak Search

## Notes

- Mode: FE+BE. Sumber: `admin-console/license-allocation-subscription/TestCases/tc-license-allocation-subscription.md`.
- Subjudul `###` memetakan langkah ke id TC granular. Urutan mengikuti state toggle: OFF (TC-AC-CS-146), OFF lalu ON di tengah form (TC-AC-CS-486), kemudian ON (TC-AC-CS-142, 147, 151), sehingga toggle hanya berubah sekali di dalam spec (S-10).
- Langkah penghubung (S-03): mengatur toggle (langkah 1, 13), Search untuk menemukan baris target (R-16; langkah 6, 16, 26, 36, 43), `(←)` pada kotak Search (langkah 8, 18, 31, 47), pindah halaman lewat sidebar (langkah 8, 11, 31, 35), baseline saldo dan email (langkah 23), dan mengganti Product dan Plan pada form yang sama (langkah 22; TC-AC-CS-142 dan 147 memakai pembukaan form yang sama).
- Pindah ke Approvals (langkah 8 dan 31) dilakukan dengan akun yang sama (`Fajar Nugroho`).
- Anchor absence (butir 8b.2): langkah 9 mendahului langkah 10; langkah 45 mendahului langkah 46; absence email dan App Access (langkah 33 dan 34) didahului toast pengajuan (langkah 25).
- Ukuran: 47 langkah, di atas 35 langkah. Alasan pertahanan: semua blok satu kelas (fungsional Add dan Renew oleh requester dengan toggle approval), tiap blok memakai Client seed sendiri dan tidak bergantung pada blok lain, sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna; pemecahan lebih lanjut menambah login, hook, dan seeding toggle tanpa menambah isolasi.
- Temuan untuk QA:
  - TC-AC-CS-147 Expected d dan TC-AC-CS-146 Expected c tidak menyebut akun yang membuka Approvals; spec memakai akun aktor yang sama. Bila `Fajar Nugroho` (capability Create saja) tidak dapat membuka Approvals, langkah 8 sampai 11 dan 31 sampai 35 perlu akun approver (Pre-setup #9 atau #4).
  - TC-AC-CS-146 Expected c ("tidak ada baris di Approvals") tidak menyebut pembanding; spec menambah pengajuan pembanding seed sebagai anchor absence.
  - TC-AC-CS-147 Post Condition c (notifikasi "Subscription needs approval" ke approver pool) tidak punya langkah observasi di TC sehingga tidak diasersi.
  - TC-AC-CS-151 Expected d menyebut Renew Hidden pada predecessor tanpa menyebut anchor; spec memakai item menu lain sebagai anchor.
  - TC-AC-CS-486 Precondition menyebut perubahan toggle "dari OFF ke ON di Settings > Role & Permission"; spec memakai sesi API (kemampuan disediakan tim FE/BE) alih-alih UI Settings.
