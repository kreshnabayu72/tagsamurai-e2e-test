---
id: TC-AC-LCS-E2E-086-resilience-reset-500-trial-sampai-client-lifecycle
title: "Resilience Reset to Default 500 pada Tab Trial, Free Plan, License Timing, dan Client Lifecycle"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AC-LCS-125
  - TC-AC-LCS-140
  - TC-AC-LCS-165
  - TC-AC-LCS-218
coverage:
  web: automated
---

# Resilience Reset to Default 500 pada Tab Trial, Free Plan, License Timing, dan Client Lifecycle

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net` (nama tampil `Andi Wijaya`), password dari `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Plans & Licensing > Lifecycle Settings, tab Trial Settings aktif); hook `after` spec mengembalikan sesi ke akun default suite (Total Control). Tidak ada ganti akun di tengah spec.
- Data: konfigurasi ketujuh tab Lifecycle Settings pada nilai default (Pre-setup 7: Trial 30, 50, 10, OFF, 7, 1; Free Plan 365; License Timing 24, 2, 2; Client Lifecycle 45, 30, 7, 1, 30, 30, 10, 2, 730; Recycle Bin 30; Approval 3; System Limits 1000, 1000, 1000, 50, 10000, 20) dipulihkan hook `beforeEach` suite dan hook `after` suite lewat Fixture BE. Berkas fixture data modul belum ada (disediakan tim FE); spec menulis nilai uji sesuai TC dan merujuk `Fixture.<berkas>.<kunci>` setelah berkas itu tersedia.
- Flag Guided Tooltip halaman Lifecycle Settings disetel true oleh hook suite `before` dan dipulihkan hook `after` (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`).
- Kemampuan teknis (disediakan tim FE/BE): Fixture BE untuk memulihkan konfigurasi tab ke nilai default (dipakai hook suite). Endpoint tidak ditulis di spec ini.
- Kemampuan teknis tambahan (disediakan tim FE/BE): Fixture BE untuk mengatur nilai tersimpan non-default pada tab yang diuji sebagai precondition TC.
- Kemampuan teknis tambahan (disediakan tim FE): `Spectra.intercept` di atas backend nyata untuk memaksa permintaan Reset tab Trial Settings, Free Plan Settings, License Timing, Client Lifecycle gagal HTTP 500; intercept dipulihkan hook `beforeEach` suite.
- Data uji (nilai non-default tersimpan, precondition TC): Trial Settings: Max Trial Duration `45`, Max Trial Asset Quota `100`, Max Trial Concurrent User Quota `20`, Require Approval for Trial Activation `ON`, First Notification `14`, Second Notification `3`; Free Plan Settings: Free Plan Duration `400`; License Timing: Managed Transition Time `48`, Managed Action Retry Delay `5`, Addon Reactivation Delay `7`; Client Lifecycle: Notify Plan Owner Before Event `60`, First Reminder Before Event `45`, Second Reminder Before Event `14`, Final Reminder Before Event `3`, Grace Period Duration `20`, Archive Period Duration `25`, Purge Warning Email `12`, Purge Urgent Warning Email `4`, Post-Purge Retention `1000`.
- State global yang diubah: nilai tersimpan non-default pada tab yang diuji (Reset selalu gagal sehingga nilainya tidak berubah); pemulihan lewat hook `beforeEach` suite dan hook `after` suite (Fixture BE); intercept dipulihkan hook `beforeEach` suite.
- Env var `AC_TC_PASSWORD` sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture.

## Test Steps

1. Pasang intercept: permintaan Reset tab Trial Settings dan Free Plan Settings dan License Timing dan Client Lifecycle dipaksa gagal HTTP 500

### TC-AC-LCS-125: Reset to Default tab Trial Settings gagal 500: toast error, data tidak berubah, tab tidak refresh

2. Atur nilai tersimpan tab Trial Settings ke nilai non-default lewat Fixture BE: Max Trial Duration `45`, Max Trial Asset Quota `100`, Max Trial Concurrent User Quota `20`, Require Approval for Trial Activation `ON`, First Notification `14`, Second Notification `3`
3. Muat ulang halaman dengan F5, lalu buka tab Trial Settings
4. Klik `[Reset to Default]`
5. Verifikasi toast error "Error, failed to reset trial settings."
6. Verifikasi tab tidak refresh
7. Muat ulang halaman dengan F5, lalu buka kembali tab Trial Settings
8. Verifikasi nilai tersimpan tetap Max Trial Duration `45`, Max Trial Asset Quota `100`, Max Trial Concurrent User Quota `20`, Require Approval for Trial Activation `ON`, First Notification `14`, Second Notification `3`

### TC-AC-LCS-140: Reset to Default tab Free Plan Settings gagal 500: toast error, data tidak berubah, tab tidak refresh

9. Atur nilai tersimpan tab Free Plan Settings ke nilai non-default lewat Fixture BE: Free Plan Duration `400`
10. Muat ulang halaman dengan F5, lalu buka tab Free Plan Settings
11. Klik `[Reset to Default]`
12. Verifikasi toast error "Error, failed to reset free plan settings."
13. Verifikasi tab tidak refresh
14. Muat ulang halaman dengan F5, lalu buka kembali tab Free Plan Settings
15. Verifikasi nilai tersimpan tetap Free Plan Duration `400`

### TC-AC-LCS-165: Reset to Default tab License Timing gagal 500: toast error, data tidak berubah, tab tidak refresh

16. Atur nilai tersimpan tab License Timing ke nilai non-default lewat Fixture BE: Managed Transition Time `48`, Managed Action Retry Delay `5`, Addon Reactivation Delay `7`
17. Muat ulang halaman dengan F5, lalu buka tab License Timing
18. Klik `[Reset to Default]`
19. Verifikasi toast error "Error, failed to reset license timing settings."
20. Verifikasi tab tidak refresh
21. Muat ulang halaman dengan F5, lalu buka kembali tab License Timing
22. Verifikasi nilai tersimpan tetap Managed Transition Time `48`, Managed Action Retry Delay `5`, Addon Reactivation Delay `7`

### TC-AC-LCS-218: Reset to Default tab Client Lifecycle gagal 500: toast error, data tidak berubah, tab tidak refresh

23. Atur nilai tersimpan tab Client Lifecycle ke nilai non-default lewat Fixture BE: Notify Plan Owner Before Event `60`, First Reminder Before Event `45`, Second Reminder Before Event `14`, Final Reminder Before Event `3`, Grace Period Duration `20`, Archive Period Duration `25`, Purge Warning Email `12`, Purge Urgent Warning Email `4`, Post-Purge Retention `1000`
24. Muat ulang halaman dengan F5, lalu buka tab Client Lifecycle
25. Klik `[Reset to Default]`
26. Verifikasi toast error "Error, failed to reset client lifecycle settings."
27. Verifikasi tab tidak refresh
28. Muat ulang halaman dengan F5, lalu buka kembali tab Client Lifecycle
29. Verifikasi nilai tersimpan tetap Notify Plan Owner Before Event `60`, First Reminder Before Event `45`, Second Reminder Before Event `14`, Final Reminder Before Event `3`, Grace Period Duration `20`, Archive Period Duration `25`, Purge Warning Email `12`, Purge Urgent Warning Email `4`, Post-Purge Retention `1000`

## Notes

- Kelas harness b (fault injection): spec ini hanya memuat TC kegagalan yang dipaksa; kegagalan dipicu intercept di atas backend nyata (Mode FE+BE) karena Expected mengasersi state backend (nilai tersimpan setelah F5).
- Langkah penghubung tanpa `Verifikasi`: langkah 1 (memasang intercept) dan langkah 2, 3, 7, 9, 10, 14, 16, 17, 21, 23, 24, 28 (mengatur nilai tersimpan non-default sebagai precondition TC dan memuat ulang halaman agar tab membaca nilai dari server).
- Temuan untuk QA:
  - Post Condition "Tidak ada perubahan data" tidak punya langkah observasi di TC sehingga tidak diasersi; Post Condition "tersimpan" teramati lewat Expected setelah F5.
