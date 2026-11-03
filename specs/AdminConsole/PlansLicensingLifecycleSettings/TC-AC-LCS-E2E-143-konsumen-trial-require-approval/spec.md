---
id: TC-AC-LCS-E2E-143-konsumen-trial-require-approval
title: "Konsumen Trial: Switch Require Approval for Trial Activation pada Aktivasi Trial Distributor dan Principal"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-LCS-502
  - TC-AC-LCS-503
  - TC-AC-LCS-504
  - TC-AC-LCS-505
coverage:
  web: automated
---

# Konsumen Trial: Switch Require Approval for Trial Activation pada Aktivasi Trial Distributor dan Principal

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net` (nama tampil `Andi Wijaya`, Principal), password dari `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control, `AC_TC_PASSWORD`).
- Hook suite (`suite.md`): `beforeEach` memulihkan ketujuh tab ke nilai default (Trial 30, 50, 10, OFF, 7, 1; Free 365; License Timing 24, 2, 2; Client Lifecycle 45, 30, 7, 1, 30, 30, 10, 2, 730; Recycle Bin 30; Approval 3; System Limits 1000, 1000, 1000, 50, 10000, 20), jam server dan jam browser, General Settings (Date Format `dd MMM yy`, Time Format 24 jam, Time Zone UTC), dan intercept, lalu membuka Plans & Licensing > Lifecycle Settings dengan tab Trial Settings aktif; hook `before` suite menyetel flag Guided Tooltip halaman ini true dan menyatakan sesi API aktor.
- Akun tambahan (ganti akun eksplisit di TC-AC-LCS-502): Distributor `distributorUser_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.AC_DIST_PASSWORD`, user entitas Distributor dengan akses Activate Trial.
- Data: Client PT Cahaya Baru (`Fixture.lifecycleSettings.clientCahayaBaru`) berada di bawah Distributor tersebut dan tanpa trial saat spec dimulai; diseed lewat Fixture BE di hook `before` spec ini.
- Kemampuan teknis (disediakan tim FE/BE): Fixture BE untuk menyeed pengajuan trial berstatus Waiting for Approval, menghapus trial PT Cahaya Baru yang dibuat spec, dan memulihkan ketujuh tab ke nilai default.
- Pemulihan: trial dan pengajuan trial PT Cahaya Baru yang dibuat spec dihapus, ketujuh tab dipulihkan ke nilai default lewat Fixture BE di langkah penghubung antar TC dan hook `after` (hook `after` juga mengembalikan sesi ke Total Control).
- Suite berjalan serial (`parallel: false`) karena spec ini memakai state global yang disebut pada butir pemulihan.
- Fixture `fixtures/lifecycleSettings.json` belum ada dan disediakan tim FE; nilai Pre-setup dirujuk lewat `Fixture.lifecycleSettings.<kunci>` setelah tersedia.

## Test Steps

### TC-AC-LCS-502: Toggle Require Approval ON membuat aktivasi trial oleh Distributor berstatus Waiting for Approval

1. Aktifkan Switch `Require Approval for Trial Activation`
2. Klik `[Save]` dan tunggu toast sukses
3. Ganti akun: logout dari Total Control lalu login sebagai Distributor `distributorUser_automated_{namaCompany}@qwertysystem.net`
4. Aktifkan trial untuk Client PT Cahaya Baru sebagai Distributor
5. Buka Allocation > Client Subscription > List Subscriptions
6. Verifikasi trial PT Cahaya Baru berstatus `Waiting for Approval`
7. Verifikasi trial PT Cahaya Baru belum aktif
8. Ganti akun: logout dari Distributor lalu login kembali sebagai Total Control
9. Pulihkan ketujuh tab dan hapus trial PT Cahaya Baru yang dibuat spec lewat Fixture BE, lalu buka Plans & Licensing > Lifecycle Settings

### TC-AC-LCS-503: Toggle Require Approval ON tidak memengaruhi aktivasi trial oleh Principal

10. Aktifkan Switch `Require Approval for Trial Activation`
11. Klik `[Save]` dan tunggu toast sukses
12. Buka Allocation > Client Subscription > List Subscriptions
13. Aktifkan trial untuk PT Cahaya Baru sebagai Principal
14. Verifikasi trial PT Cahaya Baru langsung berstatus `Active` tanpa melewati Waiting for Approval
15. Pulihkan ketujuh tab dan hapus trial PT Cahaya Baru yang dibuat spec lewat Fixture BE, lalu buka Plans & Licensing > Lifecycle Settings

### TC-AC-LCS-504: Mengubah toggle Require Approval tidak mengubah pengajuan trial yang sudah Waiting for Approval

16. Atur lewat Fixture BE: Switch `Require Approval for Trial Activation` tersimpan `ON` dan trial PT Cahaya Baru diajukan Distributor berstatus `Waiting for Approval`, lalu muat ulang halaman Lifecycle Settings
17. Nonaktifkan Switch `Require Approval for Trial Activation`
18. Klik `[Save]` dan tunggu toast sukses
19. Buka Allocation > Client Subscription > List Subscriptions
20. Verifikasi trial PT Cahaya Baru tetap berstatus `Waiting for Approval`
21. Verifikasi trial PT Cahaya Baru masih memerlukan persetujuan Principal
22. Pulihkan ketujuh tab dan hapus pengajuan trial PT Cahaya Baru lewat Fixture BE, lalu buka Plans & Licensing > Lifecycle Settings

### TC-AC-LCS-505: Ceiling trial diambil saat pengajuan dan tidak dicek ulang saat approver menyetujui

23. Atur lewat Fixture BE: Switch `Require Approval for Trial Activation` tersimpan `ON` dan trial PT Cahaya Baru dengan Duration `25` diajukan Distributor saat Max Trial Duration `30` berstatus `Waiting for Approval`, lalu muat ulang halaman Lifecycle Settings
24. Ubah Max Trial Duration dari `30` menjadi `10`
25. Klik `[Save]` dan tunggu toast sukses
26. Setujui pengajuan trial PT Cahaya Baru sebagai Total Control
27. Buka Allocation > Client Subscription > List Subscriptions
28. Verifikasi trial PT Cahaya Baru berstatus `Active`
29. Verifikasi trial PT Cahaya Baru memakai Duration `25` (ceiling `10` tidak dicek ulang saat persetujuan)

## Notes

- Langkah penghubung tanpa `Verifikasi`: "Ganti akun ..." (S-07), "Atur lewat Fixture BE ..." (precondition TC), dan "Pulihkan ..." antar TC (S-03, S-09).
- Temuan untuk QA: TC-AC-LCS-502 menulis "aktifkan trial untuk Client miliknya" tanpa menyebut Client; spec memakai PT Cahaya Baru karena TC-AC-LCS-504 dan 505 menyebut pengajuan Distributor atas client itu.
- Temuan untuk QA: Expected TC-AC-LCS-502 "trial belum aktif" dan TC-AC-LCS-504 "masih memerlukan persetujuan Principal" tidak menyebut elemen UI pengamatnya; spec menulisnya sebagai `Verifikasi` status trial pada List Subscriptions tanpa elemen tambahan (S-02).
- Temuan untuk QA: Post Condition TC "Tidak ada perubahan data" tidak diasersi (S-01).
