---
id: TC-AC-CS-E2E-052-activate-trial-toggle-approval-distributor-dan-partner
title: "Activate Trial: Toggle Approval Distributor dan Partner"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-CS-200
  - TC-AC-CS-201
  - TC-AC-CS-202
coverage:
  web: automated
---

# Activate Trial: Toggle Approval Distributor dan Partner

## Prerequisites

- Mode: FE+BE.
- Akun aktor awal (login di hook `before`): Total Control Distributor PT Maju Bersama, Eko Saputra (Pre-setup #9), `totalControlDistSub_automated_{namaCompany}@qwertysystem.net` (dirujuk lewat `Fixture.license-allocation-subscription`, belum ada, disediakan tim FE; kredensial `Spectra.env.AC_SUB_DIST_TC_PASSWORD`, nama didaftarkan di `executionConfig.environmentVariables` dan `.env.example`).
- Akun berikutnya (ganti akun eksplisit di Test Steps): Total Control Partner CV Karya Mandiri, Lestari Wulandari (Pre-setup #11), `totalControlPartnerSub_automated_{namaCompany}@qwertysystem.net` (dirujuk lewat `Fixture.license-allocation-subscription`, belum ada, disediakan tim FE; kredensial `Spectra.env.AC_SUB_PARTNER_TC_PASSWORD`, nama didaftarkan di `executionConfig.environmentVariables` dan `.env.example`).
- Akun berikutnya (ganti akun eksplisit di Test Steps): Total Control Principal PT ABC, Hendra Wijaya (Pre-setup #1), `totalControlSub_automated_{namaCompany}@qwertysystem.net` (dirujuk lewat `Fixture.license-allocation-subscription`, belum ada, disediakan tim FE; kredensial `Spectra.env.AC_SUB_TC_PASSWORD`, nama didaftarkan di `executionConfig.environmentVariables` dan `.env.example`).
- Akun berikutnya (ganti akun eksplisit di Test Steps): Additional Approver Manage allocation Principal PT ABC, Maya Tanjung (Pre-setup #4), `approverSub_automated_{namaCompany}@qwertysystem.net` (dirujuk lewat `Fixture.license-allocation-subscription`, belum ada, disediakan tim FE; kredensial `Spectra.env.AC_SUB_APPROVER_PASSWORD`, nama didaftarkan di `executionConfig.environmentVariables` dan `.env.example`).
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Allocation > Client Subscription, tab Current). Hook `after` mengembalikan sesi ke akun default suite (Total Control Principal, Pre-setup #1).
- Hook suite yang dirujuk spec ini dan dinyatakan sekali di `suite.md`: flag Guided Tooltip `guided_tooltip_seen_ac-license-allocation-subscription` disetel `seen` di hook `before` dan dipulihkan di hook `after`, sesi API aktor untuk pelaku kedua dan aksi pemicu, serta fixture backend pemulihan state Pre-setup.
- Suite serial: `parallel: false` (lihat `suite.md`).
- Data Pre-setup: Toggle `Require Approval for Trial Activation` (Plans & Licensing > Lifecycle Settings > Trial Settings, platform-wide) (#24): OFF untuk TC-AC-CS-200, ON untuk TC-AC-CS-201 dan TC-AC-CS-202.
- Data seed milik spec (dibuat lewat API di hook `before`, dihapus di hook `after`): Client `Client Tanpa Subscription A+{runId}-052` (TC-AC-CS-200) dan `Client Tanpa Subscription B+{runId}-052` (TC-AC-CS-201), keduanya binaan langsung PT Maju Bersama pada group `Jawa` tanpa term maupun trial (padanan Pre-setup #48); Client `Bengkel Maju Jaya+{runId}-052` binaan langsung CV Karya Mandiri (padanan Pre-setup #30).
- Data Dinamis: trial dan pengajuan trial yang dibuat dihapus bersama Client seed di hook `after`; hanya toggle (state global) yang dipulihkan ke nilai awal di hook `after`.
- Kemampuan teknis (disediakan tim FE/BE): toggle Require Approval for Trial Activation; membaca Detail baris trial (License Quota).

## Test Steps

### TC-AC-CS-200: Distributor dengan toggle Trial OFF mengaktifkan trial langsung

1. Atur toggle Require Approval for Trial Activation OFF lewat kemampuan tim FE/BE
2. Klik `[+ Activate Trial]`
3. Pilih Client `Client Tanpa Subscription A+{runId}-052`, Product `FAMS`, Plan `Growth`, isi Trial Duration `30`, Trial Asset Quota `50`, Trial Concurrent User Quota `10`
4. Klik `[Submit]`
5. Verifikasi toast sukses "Success, trial has been activated for Client Tanpa Subscription A+{runId}-052 — Growth, 30 days."
6. Ketik Search `Client Tanpa Subscription A+{runId}-052`, tekan Enter
7. Verifikasi baris Trial berstatus Active dengan Plan Owner `PT Maju Bersama (Distributor)`

### TC-AC-CS-201: Distributor dengan toggle Trial ON mengajukan trial Waiting for Approval

8. Atur toggle Require Approval for Trial Activation ON lewat kemampuan tim FE/BE, lalu buka Allocation > Client Subscription tab Current
9. Klik `[+ Activate Trial]`
10. Pilih Client `Client Tanpa Subscription B+{runId}-052`, Product `FAMS`, Plan `Growth`, isi Trial Duration `30`, Trial Asset Quota `50`, Trial Concurrent User Quota `10`
11. Klik `[Submit]`
12. Verifikasi toast sukses "Success, trial request for Client Tanpa Subscription B+{runId}-052 has been submitted for approval."
13. Ketik Search `Client Tanpa Subscription B+{runId}-052`, tekan Enter
14. Verifikasi baris Trial berstatus Waiting for Approval
15. Verifikasi Start Date dan End Date baris Trial "—"
16. Buka Detail baris Trial
17. Verifikasi Subscription Info dan License Quota tampil
18. Verifikasi License Quota belum menampilkan saldo kuota yang diinisialisasi

### TC-AC-CS-202: Partner dengan toggle Trial ON mengajukan trial yang di-review Principal

19. Ganti akun: Logout lalu login sebagai Total Control Partner (`Lestari Wulandari`)
20. Buka menu Allocation > Client Subscription
21. Klik `[+ Activate Trial]`
22. Pilih Client `Bengkel Maju Jaya+{runId}-052`, Product `SAMS`, Plan `Growth`, isi Trial Duration `30`, Trial Asset Quota `50`, Trial Concurrent User Quota `10`
23. Klik `[Submit]`
24. Verifikasi toast sukses "Success, trial request for Bengkel Maju Jaya+{runId}-052 has been submitted for approval."
25. Ketik Search `Bengkel Maju Jaya+{runId}-052`, tekan Enter
26. Verifikasi baris Trial berstatus Waiting for Approval dengan Plan Owner `CV Karya Mandiri (Partner)`

### Reviewer pengajuan TC-AC-CS-201 dan TC-AC-CS-202

27. Ganti akun: Logout lalu login sebagai Total Control Principal (`Hendra Wijaya`), buka Approvals > Client Subscription Tab Active
28. Verifikasi pengajuan Trial Client `Client Tanpa Subscription B+{runId}-052` dengan Type `Trial` tampil
29. Verifikasi pengajuan Trial Client `Bengkel Maju Jaya+{runId}-052` tampil untuk Total Control Principal
30. Ganti akun: Logout lalu login sebagai Additional Approver Manage allocation Principal (`Maya Tanjung`), buka Approvals > Client Subscription Tab Active
31. Verifikasi pengajuan Trial Client `Bengkel Maju Jaya+{runId}-052` tampil untuk Additional Approver Principal

## Notes

- Urutan menyimpang dari urutan TC sumber (S-10): pemeriksaan reviewer di Approvals (Expected TC-AC-CS-201 butir c dan TC-AC-CS-202 butir c) dikumpulkan di blok akhir supaya login Principal dan Additional Approver hanya satu kali; kedua pengajuan tetap Waiting for Approval sampai blok itu selesai.
- Langkah penghubung (S-03): Search untuk menemukan baris target (R-16); pengaturan toggle antar TC; ganti akun eksplisit (S-07).
- Temuan untuk QA: (1) TC-AC-CS-201 dan TC-AC-CS-202 Post Condition (notifikasi "Subscription needs approval" ke Total Control dan Additional Approver Principal) tanpa langkah observasi di TC sehingga tidak diasersi. (2) TC-AC-CS-202 butir c ("bukan approver entitas Partner") tidak punya cara pengamatan di TC; spec hanya mengamati pengajuan tampil bagi Total Control dan Additional Approver Principal. (3) TC-AC-CS-201 butir "Saldo kuota lisensi belum diinisialisasi" tidak menyebut layar; spec mengamatinya di License Quota Detail Trial. (4) Email dan password akun Additional Approver `Maya Tanjung` dan Total Control Partner `Lestari Wulandari` dari Pre-setup #4 dan #11 dirujuk lewat fixture yang disediakan tim FE.
