---
id: TC-AC-CS-E2E-021-capability-create-add-activate-trial-renew-convert-sampai-sukses
title: "Capability Create: Add, Activate Trial, Renew, dan Convert sampai Sukses"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-CS-83
  - TC-AC-CS-84
  - TC-AC-CS-85
  - TC-AC-CS-86
coverage:
  web: automated
---

# Capability Create: Add, Activate Trial, Renew, dan Convert sampai Sukses

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: `createOnlySub_automated_{namaCompany}@qwertysystem.net` (`Fajar Nugroho`, capability Create saja, Distributor PT Maju Bersama; Pre-setup #6), password `Spectra.env.AC_SUB_CREATE_PASSWORD`; login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Hook `after` mengembalikan sesi ke akun default suite (Total Control Principal, Pre-setup #1).
- Email akun dirujuk lewat `Fixture.license-allocation-subscription` (belum ada; disediakan tim FE); nama env password terdaftar di `executionConfig.environmentVariables` dan `.env.example` (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`). Hook `beforeEach` suite membuka Allocation > Client Subscription tab Current dan menjadi jaring pengaman S-09 (lihat `suite.md`). Flag Guided Tooltip diatur hook `before` suite (`seen`), sehingga walkthrough tidak muncul.
- Kemampuan teknis (disediakan tim FE/BE, mekanisme tidak tertulis di TC, PRD, atau LLD sehingga tanpa endpoint karangan; S-13): mengatur toggle Require Approval for Allocation (per entitas PT Maju Bersama dan CV Karya Mandiri; Pre-setup #23) dan Require Approval for Trial Activation (platform-wide; #24), serta memulihkan data Pre-setup yang berubah. Nilai awal toggle dicatat di hook `before` dan dipulihkan di hook `after`.
- Kemampuan teknis (fixture waktu): jam server dan jam browser diatur absolut ke tanggal acuan `19/08/26` (fixture waktu, disediakan tim FE/BE), dipulihkan di hook `after`; tanggal toast Renew `01/09/26` (TC-AC-CS-85) bergantung pada tanggal acuan itu dan End Date seed `31/08/26`.
- State awal: Require Approval for Allocation OFF untuk PT Maju Bersama (TC-AC-CS-83, 85, 86) dan Require Approval for Trial Activation OFF (TC-AC-CS-84), diatur di hook `before` spec ini.
- Data seed milik spec (dibuat lewat API di hook `before`, dihapus di hook `after`; keadaan toggle tetap dipulihkan di hook `after` karena state global):
  - Client `Client Tanpa Subscription+{runId}-021` (binaan langsung PT Maju Bersama pada group `Jawa`, tanpa term maupun trial; padanan Pre-setup #48) menerima term SAMS (TC-AC-CS-83) lalu trial FAMS (TC-AC-CS-84).
  - Client `Warung Kopi Senja+{runId}-021` dengan satu term Active FAMS plan Professional, Start Date 01/09/25, End Date 31/08/26, Plan Owner PT Maju Bersama (Distributor), tanpa successor dan tanpa trial (padanan Pre-setup #69); menerima successor Pending (TC-AC-CS-85).
  - Client `Klinik Harapan Bunda+{runId}-021` dengan trial SAMS Growth Active, Plan Owner CV Karya Mandiri, tanpa term paid SAMS (padanan Pre-setup #71); dikonversi (TC-AC-CS-86).
- Nilai Start Date "hari ini" pada TC-AC-CS-83 ditulis sebagai tanggal hari run (diambil dari jam browser, `19/08/26` menurut fixture waktu).

## Test Steps

### TC-AC-CS-83: Pemegang Create saja menyelesaikan + Subscription mode New sampai sukses

1. Klik `[+ Subscription]`
2. Pilih Client `Client Tanpa Subscription+{runId}-021`, Product `SAMS`, Plan `Growth`, Duration `1`, dan Start Date hari ini
3. Klik `[Submit]`
4. Verifikasi modal tertutup
5. Verifikasi muncul toast sukses "Success, subscription has been added."
6. Ketik Search `Client Tanpa Subscription+{runId}-021`, tekan Enter
7. Verifikasi baris baru berstatus Active tampil di tab `Current` dengan Plan Owner `PT Maju Bersama (Distributor)`
8. Klik `(←)` pada kotak Search

### TC-AC-CS-84: Pemegang Create saja menyelesaikan + Activate Trial

9. Klik `[+ Activate Trial]`
10. Pilih Client `Client Tanpa Subscription+{runId}-021`, Product `FAMS`, Plan `Growth`, isi Duration `30`, Asset Quota `50`, dan Concurrent User Quota `10`
11. Klik `[Submit]`
12. Verifikasi modal tertutup
13. Verifikasi muncul toast sukses "Success, trial has been activated for Client Tanpa Subscription+{runId}-021 — Growth, 30 days."
14. Ketik Search `Client Tanpa Subscription+{runId}-021`, tekan Enter
15. Verifikasi baris Trial berstatus Active tampil di tab `Current`
16. Klik `(←)` pada kotak Search

### TC-AC-CS-85: Pemegang Create saja menyelesaikan Renew

17. Ketik Search `Warung Kopi Senja+{runId}-021`, tekan Enter
18. Klik ikon `⋯` pada baris Client `Warung Kopi Senja+{runId}-021`
19. Pilih `Renew`
20. Pilih Renewal Option `Keep current plan` dan isi Duration `1`
21. Klik `[Submit]`
22. Verifikasi modal tertutup
23. Verifikasi muncul toast sukses "Success, your renewal has been scheduled and will take effect on 01/09/26."
24. Verifikasi term baru berstatus Pending muncul di tab `Current`
25. Verifikasi predecessor term Client `Warung Kopi Senja+{runId}-021` tetap Active

### TC-AC-CS-86: Pemegang Create saja menyelesaikan Convert Trial

26. Ganti isi kotak search dengan `Klinik Harapan Bunda+{runId}-021`, tekan Enter
27. Klik ikon `⋯` pada baris trial
28. Pilih `Convert`
29. Pilih Plan `Professional`, isi Duration `1`, lalu klik `[Submit]`
30. Klik `[Convert]` pada dialog Convert Trial
31. Verifikasi muncul toast sukses "Success, subscription has been added and trial converted."
32. Klik tab `History`
33. Verifikasi baris trial berstatus Converted tampil di tab `History`
34. Klik tab `Current`
35. Verifikasi term paid berstatus Active tampil di tab `Current` dengan Plan Owner `PT Maju Bersama` (aktor Convert, ACCS-LOGIC-04e)

## Notes

- Mode: FE+BE. Sumber: `admin-console/license-allocation-subscription/TestCases/tc-license-allocation-subscription.md`.
- Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): langkah Search untuk menemukan baris target (R-16), `Klik (←)` pada kotak Search (langkah 8 dan sesudah Verifikasi baris Trial), dan Search Client seed sebelum Verifikasi baris Trial pada daftar bersama. Halaman dibuka hook `beforeEach`; baris hasil aksi dicari lewat Search atau tab terkait.
- Empat blok TC memakai satu akun (capability Create saja) dan satu halaman, dengan Client seed terpisah per blok sehingga tidak ada state yang dibawa antar blok; empat aksi tulis berbeda (Add, Activate Trial, Renew, Convert) dikelompokkan karena satu kelas harness (fungsional) dan satu kemampuan yang diuji (Create tanpa capability lain), bukan karena tidak berhubungan.
- Hasil toast dan baris dicek sesudah `[Submit]`; hanya aksi yang berhasil yang diasersi (spec positif). Jalur ditolak untuk capability yang tidak dimiliki ada di spec Role Matrix lain (spec 018).
- Temuan untuk QA:
  - TC-AC-CS-83 tidak menyebut Start Date selain "hari ini" dan Estimated Cost hanya di panah langkah; spec tidak mengasersi Estimated Cost (bukan Expected).
  - TC-AC-CS-85 Expected a menyebut tanggal toast `01/09/26` yang bergantung data seed padanan #69 (End Date 31/08/26) dan bukan hari run.
  - TC-AC-CS-86 Plan Owner term paid `PT Maju Bersama` berbeda dari Plan Owner trial `CV Karya Mandiri` (ACCS-LOGIC-04e); TC tidak menyebut Pay From dan Estimated Cost pada dialog Convert.
  - Toggle dan pemulihan Pre-setup yang dibutuhkan tidak tertulis di TC selain Precondition; mekanisme pengaturan toggle dan pemulihan disediakan tim FE/BE.
