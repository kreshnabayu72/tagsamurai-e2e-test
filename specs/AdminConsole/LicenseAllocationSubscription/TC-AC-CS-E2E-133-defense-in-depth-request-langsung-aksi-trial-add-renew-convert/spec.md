---
id: TC-AC-CS-E2E-133-defense-in-depth-request-langsung-aksi-trial-add-renew-convert
title: "Defense-in-Depth: Request Langsung Aksi Trial, Add, Renew, Convert"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AC-CS-498
  - TC-AC-CS-499
  - TC-AC-CS-500
  - TC-AC-CS-501
  - TC-AC-CS-502
  - TC-AC-CS-503
  - TC-AC-CS-504
  - TC-AC-CS-505
coverage:
  web: automated
---

# Defense-in-Depth: Request Langsung Aksi Trial, Add, Renew, Convert

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal (Pre-setup #1) `totalControlSub_automated_{namaCompany}@qwertysystem.net` (`Hendra Wijaya`), password `Spectra.env.AC_SUB_TC_PASSWORD`; login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Semua langkah spec ini adalah request langsung ke server dengan token sesi aktor, tanpa melalui browser.
- Email dan identitas data Pre-setup dirujuk lewat `Fixture.license-allocation-subscription` (belum ada; disediakan tim FE). Nama env var password adalah usulan: belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`, didaftarkan tim FE.
- Kemampuan teknis (disediakan tim FE/BE): klien HTTP atau fixture BE yang mengirim request dengan token sesi aktor (login API password, token tidak dihitung sebagai sesi web); membaca jumlah term dan trial per Client sebagai state data. Aksi yang dikirim hanya yang dinamai TC (Add Subscription mode New, Renew, Cancel Subscription, Convert mode New, Activate Trial); path dan body request tidak tertulis di TC, PRD, atau LLD dan disediakan tim FE/BE tanpa endpoint karangan (S-13, 8b butir 1); jam server dan jam browser diatur absolut ke tanggal acuan `19/08/26` (fixture waktu, disediakan tim FE/BE), dipulihkan di hook `after`.
- Data milik spec, dibuat lewat API di hook `before` dan dibersihkan di hook `after` (S-06, S-12; request yang diuji ditolak sehingga tidak ada perubahan data), Client binaan Principal dan PT Maju Bersama dengan nama bersuffix `+{runId}-133`; jumlah term dan trial tiap Client dicatat sebagai baseline sebelum langkah pertama:
  1. Client `S1` (setara `PT Sejahtera`, Pre-setup #38): term paid FAMS Professional Active dan trial FAMS Enterprise Active (setara #61 dan #60). Dipakai TC-AC-CS-498, 500, 501, 502, 505.
  2. Client `K1` (setara `Klinik Harapan Bunda`, #43): trial SAMS Growth Active tanpa term paid SAMS (Plan Owner CV Karya Mandiri) dan trial FAMS Starter Expired tanpa term paid FAMS. Dipakai TC-AC-CS-499 dan 503.
  3. Client `K2` (setara `PT Bintang Timur`, #37): trial FAMS Waiting for Approval tanpa term paid. Dipakai TC-AC-CS-499.
  4. Client `T1` (setara `Toko Uji Trial`, #103): trial FAMS Growth Converted. Dipakai TC-AC-CS-504.
- Hook suite (lihat `suite.md`): `beforeEach` membuka Allocation > Client Subscription tab Current dan menjadi jaring pengaman S-09; flag Guided Tooltip diatur `seen`. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AC-CS-498: Add mode New langsung untuk Client yang sudah punya term live ditolak

1. Kirim POST Add Subscription mode New Client `S1` Product `FAMS` dengan token sesi aktor
2. Verifikasi respons server menolak dengan pesan "This client already has an active subscription for this product."
3. Verifikasi jumlah term Client `S1` sama dengan baseline (tidak ada term baru)

### TC-AC-CS-499: Add mode New langsung untuk Client dan Product yang punya baris Trial ditolak

4. Kirim POST Add Subscription mode New Client `K1` Product `SAMS` Plan `Growth` Duration `1` Start Date `19/08/26` saat ada baris Trial Active
5. Verifikasi respons server menolak dengan pesan "This client already has a trial for this product. Use Convert on the trial row."
6. Kirim POST Add Subscription mode New Client `K2` Product `FAMS` Plan `Growth` Duration `1` Start Date `19/08/26` saat ada baris Trial Waiting for Approval
7. Verifikasi respons server menolak dengan pesan "This client already has a trial for this product. Use Convert on the trial row."
8. Kirim POST Add Subscription mode New Client `K1` Product `FAMS` Plan `Growth` Duration `1` Start Date `19/08/26` saat ada baris Trial Expired
9. Verifikasi respons server menolak dengan pesan "This client already has a trial for this product. Use Convert on the trial row."
10. Verifikasi jumlah term dan keadaan trial Client `K1` dan `K2` sama dengan baseline (tidak ada term baru, trial tidak berubah)

### TC-AC-CS-500: Renew langsung saat Client punya trial Active produk sama ditolak

11. Kirim POST Renew term paid FAMS Client `S1` dengan token sesi aktor
12. Verifikasi respons server menolak dengan pesan "This client has an active trial. Use Convert on the trial row."
13. Verifikasi jumlah term Client `S1` sama dengan baseline (tidak ada term baru)

### TC-AC-CS-501: Renew langsung dengan predecessor bertype Trial ditolak

14. Kirim POST Renew dengan predecessor trial FAMS Client `S1` dengan token sesi aktor
15. Verifikasi respons server menolak dengan pesan "This action is only available for paid subscriptions."
16. Verifikasi jumlah term Client `S1` sama dengan baseline (tidak ada term baru)

### TC-AC-CS-502: Cancel Subscription langsung pada baris Trial ditolak

17. Kirim POST Cancel Subscription pada trial FAMS Client `S1` dengan token sesi aktor
18. Verifikasi respons server menolak dengan pesan "This action is only available for paid subscriptions."
19. Verifikasi status trial FAMS Client `S1` tidak berubah (Active)

### TC-AC-CS-503: Convert mode New langsung dengan Start Date bukan hari ini ditolak

20. Kirim POST Convert mode New pada trial SAMS Client `K1` dengan Start Date `25/08/26`
21. Verifikasi respons server menolak dengan pesan "Start date must be today when converting a trial"
22. Verifikasi trial SAMS Client `K1` tidak berubah dan tidak ada term paid SAMS

### TC-AC-CS-504: Activate Trial langsung untuk plan yang sudah dipakai ditolak

23. Kirim POST Activate Trial Client `T1` Product `FAMS` Plan `Growth` dengan token sesi aktor
24. Verifikasi respons server menolak dengan pesan "Trial already used for Growth"
25. Verifikasi tidak ada trial baru pada Client `T1`

### TC-AC-CS-505: Activate Trial langsung untuk Client yang sudah punya trial aktif ditolak

26. Kirim POST Activate Trial Client `S1` Product `FAMS` Plan `Starter` dengan token sesi aktor
27. Verifikasi respons server menolak dengan pesan "This client already has an active trial. Wait until it expires or it converts."
28. Verifikasi tidak ada trial baru pada Client `S1`

## Notes

- Subjudul `###` memetakan langkah ke id TC granular.
- K-1: TC kelas a (defense-in-depth) dengan Expected berupa respons API tetap masuk spec FE+BE walau tumpang tindih dengan `tc-license-allocation-subscription-backend.md`; asersi hanya respons server dan state data (bagian 8b butir 1), tanpa perilaku FE.
- Data milik spec dipakai sebagai pengganti baris Pre-setup (setara Pre-setup #38/#61/#60, #43/#71/#72, #37/#59, #103) karena request yang diuji ditolak dan data milik spec menjaga baseline Pre-setup tidak berubah (S-06).
- Penghubung (S-03): tidak ada langkah penghubung; jumlah term dibaca lewat fixture BE (state data) sebagai baseline pada hook `before`.
- Temuan untuk QA:
  - TC-AC-CS-498 sampai 505 Expected a menyebut pesan penolakan tanpa kode status HTTP dan kode error; spec mengasersi penolakan dengan pesan itu tanpa status (S-02).
  - TC-AC-CS-498 menyebut V-07 dievaluasi lebih dulu daripada V-32 tanpa langkah yang membedakannya; spec hanya mengasersi pesan V-07.
  - TC-AC-CS-500, 501, 502, 503 tidak menyebut body request (Plan, Duration, Start Date, Pay From) selain yang ditulis; payload disediakan tim FE/BE.
  - TC-AC-CS-499 Expected b dan TC-AC-CS-503 Expected b ("trial tidak berubah") tidak menyebut kolom yang dibandingkan; spec membandingkan status dan jumlah record dengan baseline.
