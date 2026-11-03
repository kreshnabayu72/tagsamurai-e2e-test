---
id: TC-AC-CS-E2E-051-activate-trial-principal-dan-inisialisasi-kuota
title: "Activate Trial: Principal dan Inisialisasi Kuota"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-CS-199
  - TC-AC-CS-203
  - TC-AC-CS-204
  - TC-AC-CS-205
  - TC-AC-CS-206
coverage:
  web: automated
---

# Activate Trial: Principal dan Inisialisasi Kuota

## Prerequisites

- Mode: FE+BE.
- Akun aktor awal (login di hook `before`): Total Control Principal PT ABC, Hendra Wijaya (Pre-setup #1), `totalControlSub_automated_{namaCompany}@qwertysystem.net` (dirujuk lewat `Fixture.license-allocation-subscription`, belum ada, disediakan tim FE; kredensial `Spectra.env.AC_SUB_TC_PASSWORD`, nama didaftarkan di `executionConfig.environmentVariables` dan `.env.example`).
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Allocation > Client Subscription, tab Current). Hook `after` mengembalikan sesi ke akun default suite (Total Control Principal, Pre-setup #1).
- Hook suite yang dirujuk spec ini dan dinyatakan sekali di `suite.md`: flag Guided Tooltip `guided_tooltip_seen_ac-license-allocation-subscription` disetel `seen` di hook `before` dan dipulihkan di hook `after`, sesi API aktor untuk pelaku kedua dan aksi pemicu, serta fixture backend pemulihan state Pre-setup.
- Suite serial: `parallel: false` (lihat `suite.md`).
- Data Pre-setup: Toggle `Require Approval for Trial Activation` ON (Plans & Licensing > Lifecycle Settings > Trial Settings, platform-wide) (#24) diatur lewat kemampuan tim FE/BE di hook `before` dan dipulihkan di hook `after`.
- Data seed milik spec (dibuat lewat API di hook `before`, dihapus di hook `after`; padanan Pre-setup #48: binaan langsung PT Maju Bersama pada group `Jawa`, belum punya term maupun trial): satu Client per blok TC supaya tidak ada state antar blok: `Client Tanpa Subscription A+{runId}-051` (TC-AC-CS-199), `Client Tanpa Subscription B+{runId}-051` (TC-AC-CS-203), `Client Tanpa Subscription C+{runId}-051` (TC-AC-CS-204), dan `Client Tanpa Subscription D+{runId}-051` (TC-AC-CS-206).
- Data seed anchor absence (TC-AC-CS-199 langkah 11-12): satu pengajuan Waiting for Approval milik akun lain, dibuat lewat API di hook `before` dengan sesi API pemilik `Fajar Nugroho` (`createOnlySub_automated_{namaCompany}@qwertysystem.net`, Distributor PT Maju Bersama; Pre-setup #6, password `Spectra.env.AC_SUB_CREATE_PASSWORD`, sesi API disediakan tim FE/BE) pada Client `Pengajuan Lain+{runId}-051` (padanan Pre-setup #49, binaan PT Maju Bersama); pengajuan dan Client dihapus di hook `after`. Pengajuan ini bukan milik akun aktor Principal sehingga tampil di Tab Active Approvals.
- Data Pre-setup baca-saja: General Settings Principal PT ABC `dd/MM/yy`, tanggal acuan uji `19/08/26` (#28).
- Data Dinamis: trial yang dibuat pada tiap Client seed dihapus bersama Client seed di hook `after`. Yang dipulihkan hanya state global: toggle Require Approval for Trial Activation dan jam server dan browser, di hook `after`.
- Kemampuan teknis (disediakan tim FE/BE): fixture waktu untuk tanggal acuan `19/08/26` (jam server dan jam browser, dipulihkan di hook `after`); toggle Require Approval for Trial Activation; membaca Detail baris trial (License Quota).

## Test Steps

### TC-AC-CS-199: Principal mengaktifkan trial langsung tanpa approval (juga memenuhi TC-AC-CS-205)

1. Klik `[+ Activate Trial]`
2. Pilih Client `Client Tanpa Subscription A+{runId}-051`, Product `FAMS`, Plan `Growth`, isi Trial Duration `30`, Trial Asset Quota `50`, Trial Concurrent User Quota `10`
3. Klik `[Submit]`
4. Verifikasi toast sukses "Success, trial has been activated for Client Tanpa Subscription A+{runId}-051 — Growth, 30 days."
5. Ketik Search `Client Tanpa Subscription A+{runId}-051`, tekan Enter
6. Verifikasi baris Trial berstatus Active dengan badge Trial
7. Verifikasi Start Date baris Trial `19/08/26`
8. Verifikasi End Date baris Trial `17/09/26` (19/08/26 + 30 hari - 1, End Date inklusif)
9. Verifikasi Plan Owner baris Trial `PT ABC (Principal)`
10. Buka Approvals > Client Subscription
11. Verifikasi pengajuan `Pengajuan Lain+{runId}-051` tampil di Tab Active
12. Verifikasi pengajuan trial Client `Client Tanpa Subscription A+{runId}-051` tidak tampil di Tab Active
13. Buka Allocation > Client Subscription tab Current

### TC-AC-CS-203: Aktivasi trial menginisialisasi saldo kuota lisensi sesuai form

14. Klik `[+ Activate Trial]`
15. Pilih Client `Client Tanpa Subscription B+{runId}-051`, Product `FAMS`, Plan `Growth`, isi Trial Duration `30`, Trial Asset Quota `100`, Trial Concurrent User Quota `5`
16. Klik `[Submit]`
17. Tunggu aksi selesai (dialog/modal tertutup)
18. Ketik Search `Client Tanpa Subscription B+{runId}-051`, tekan Enter
19. Buka Detail baris Trial baru
20. Verifikasi License Quota tampil
21. Verifikasi baris `Asset` pada License Quota Total 100, Remaining 100, dan Used 0
22. Verifikasi baris `Concurrent User` pada License Quota Total 5
23. Verifikasi addon FAMS `Audit`, `Maintenance`, `Tracking`, `Maps`, dan `IT Inventory` masing-masing Total 100 sama dengan Trial Asset Quota

### TC-AC-CS-204: Aktivasi trial SIEM menginisialisasi Concurrent User dan Log Source

24. Kembali ke List Subscriptions tab Current
25. Klik `[+ Activate Trial]`
26. Pilih Client `Client Tanpa Subscription C+{runId}-051`, Product `SIEM`, Plan SIEM, isi Trial Duration `30`, Trial Concurrent User Quota `10`, Trial Log Source Quota `20`
27. Klik `[Submit]`
28. Tunggu aksi selesai (dialog/modal tertutup)
29. Ketik Search `Client Tanpa Subscription C+{runId}-051`, tekan Enter
30. Buka Detail baris Trial SIEM
31. Verifikasi License Quota tampil
32. Verifikasi baris `Concurrent User` Total 10
33. Verifikasi baris `Log Source` Total 20
34. Verifikasi tidak ada baris Asset maupun addon pada License Quota
35. Buka Allocation > Client Subscription tab Current

### TC-AC-CS-206: Stay on this form pada Activate Trial mereset form setelah sukses

36. Klik `[+ Activate Trial]`
37. Centang "Stay on this form after submitting"
38. Pilih Client `Client Tanpa Subscription D+{runId}-051`, Product `FAMS`, Plan `Growth`, isi Trial Duration `30`, Trial Asset Quota `50`, Trial Concurrent User Quota `10`
39. Klik `[Submit]`
40. Verifikasi toast sukses "Success, trial has been activated for Client Tanpa Subscription D+{runId}-051 — Growth, 30 days." muncul
41. Verifikasi modal Activate Trial tetap terbuka
42. Verifikasi semua field kembali bersih
43. Verifikasi checkbox "Stay on this form after submitting" tetap tercentang
44. Klik `[✕]`

## Notes

- TC-AC-CS-205 (Start Date `19/08/26` dan End Date `17/09/26` untuk Duration `30`) memakai Client, Product, Plan, Duration, dan kuota yang identik dengan TC-AC-CS-199; satu pembuatan trial memenuhi aksi kedua TC dan Verifikasi Start Date dan End Date ditulis sekali di blok TC-AC-CS-199. TC-AC-CS-205 tercatat di `sourceTc` spec ini.
- Langkah penghubung (S-03): `Tunggu aksi selesai` setelah `[Submit]` sebelum Search (8b.8); Search untuk menemukan baris trial target (R-16); kembali ke List (langkah 13, 24, 35); `✕` menutup form bersih TC-AC-CS-206 (tanpa dialog).
- Anchor absence (bagian 8b butir 2): ketiadaan pengajuan trial di Approvals Tab Active didahului Verifikasi pengajuan lain tampil pada surface yang sama (pengajuan Waiting for Approval seed `Pengajuan Lain+{runId}-051` milik `Fajar Nugroho`, lihat Prerequisites).
- Alasan melewati sekitar 35 langkah bila dihitung penuh: semua blok satu topik (Activate Trial langsung oleh Principal) pada Client yang sama, tanpa kelas harness lain; tiap blok memakai Client seed sendiri.
- Temuan untuk QA: (1) TC-AC-CS-199 Post Condition a (baris Trial tampil di tab `Current`) sudah menjadi bagian Expected b; Post Condition b (saldo kuota diinisialisasi) diasersi di TC-AC-CS-203. (2) TC-AC-CS-205 tidak menyebut toggle Require Approval for Trial Activation; spec memakai keadaan toggle ON yang sama dengan TC-AC-CS-199.
