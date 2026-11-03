---
id: TC-AC-LCS-E2E-087-resilience-reset-500-recycle-approval-limits
title: "Resilience Reset to Default 500 pada Tab Recycle Bin, Approval Settings, dan System Limits"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AC-LCS-233
  - TC-AC-LCS-248
  - TC-AC-LCS-288
coverage:
  web: automated
---

# Resilience Reset to Default 500 pada Tab Recycle Bin, Approval Settings, dan System Limits

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net` (nama tampil `Andi Wijaya`), password dari `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Plans & Licensing > Lifecycle Settings, tab Trial Settings aktif); hook `after` spec mengembalikan sesi ke akun default suite (Total Control). Tidak ada ganti akun di tengah spec.
- Data: konfigurasi ketujuh tab Lifecycle Settings pada nilai default (Pre-setup 7: Trial 30, 50, 10, OFF, 7, 1; Free Plan 365; License Timing 24, 2, 2; Client Lifecycle 45, 30, 7, 1, 30, 30, 10, 2, 730; Recycle Bin 30; Approval 3; System Limits 1000, 1000, 1000, 50, 10000, 20) dipulihkan hook `beforeEach` suite dan hook `after` suite lewat Fixture BE. Berkas fixture data modul belum ada (disediakan tim FE); spec menulis nilai uji sesuai TC dan merujuk `Fixture.<berkas>.<kunci>` setelah berkas itu tersedia.
- Flag Guided Tooltip halaman Lifecycle Settings disetel true oleh hook suite `before` dan dipulihkan hook `after` (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`).
- Kemampuan teknis (disediakan tim FE/BE): Fixture BE untuk memulihkan konfigurasi tab ke nilai default (dipakai hook suite). Endpoint tidak ditulis di spec ini.
- Kemampuan teknis tambahan (disediakan tim FE/BE): Fixture BE untuk mengatur nilai tersimpan non-default pada tab yang diuji sebagai precondition TC.
- Kemampuan teknis tambahan (disediakan tim FE): `Spectra.intercept` di atas backend nyata untuk memaksa permintaan Reset tab Recycle Bin, Approval Settings, System Limits gagal HTTP 500; intercept dipulihkan hook `beforeEach` suite.
- Data uji (nilai non-default tersimpan, precondition TC): Recycle Bin: Permanently Delete Recycle Bin `45`; Approval Settings: Approval Timeout `7`; System Limits: Bulk Transaction Row Limit `2000`, Selection Limit `1500`, Register Asset Bulk Limit `2500`, Hierarchy Depth Limit `60`, Master Data Count Limit `20000`, Max Visible Columns `25`.
- State global yang diubah: nilai tersimpan non-default pada tab yang diuji (Reset selalu gagal sehingga nilainya tidak berubah); pemulihan lewat hook `beforeEach` suite dan hook `after` suite (Fixture BE); intercept dipulihkan hook `beforeEach` suite.
- Env var `AC_TC_PASSWORD` sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture.

## Test Steps

1. Pasang intercept: permintaan Reset tab Recycle Bin dan Approval Settings dan System Limits dipaksa gagal HTTP 500

### TC-AC-LCS-233: Reset to Default tab Recycle Bin gagal 500: toast error, data tidak berubah, tab tidak refresh

2. Atur nilai tersimpan tab Recycle Bin ke nilai non-default lewat Fixture BE: Permanently Delete Recycle Bin `45`
3. Muat ulang halaman dengan F5, lalu buka tab Recycle Bin
4. Klik `[Reset to Default]`
5. Verifikasi toast error "Error, failed to reset recycle bin settings."
6. Verifikasi tab tidak refresh
7. Muat ulang halaman dengan F5, lalu buka kembali tab Recycle Bin
8. Verifikasi nilai tersimpan tetap Permanently Delete Recycle Bin `45`

### TC-AC-LCS-248: Reset to Default tab Approval Settings gagal 500: toast error, data tidak berubah, tab tidak refresh

9. Atur nilai tersimpan tab Approval Settings ke nilai non-default lewat Fixture BE: Approval Timeout `7`
10. Muat ulang halaman dengan F5, lalu buka tab Approval Settings
11. Klik `[Reset to Default]`
12. Verifikasi toast error "Error, failed to reset approval settings."
13. Verifikasi tab tidak refresh
14. Muat ulang halaman dengan F5, lalu buka kembali tab Approval Settings
15. Verifikasi nilai tersimpan tetap Approval Timeout `7`

### TC-AC-LCS-288: Reset to Default tab System Limits gagal 500: toast error, data tidak berubah, tab tidak refresh

16. Atur nilai tersimpan tab System Limits ke nilai non-default lewat Fixture BE: Bulk Transaction Row Limit `2000`, Selection Limit `1500`, Register Asset Bulk Limit `2500`, Hierarchy Depth Limit `60`, Master Data Count Limit `20000`, Max Visible Columns `25`
17. Muat ulang halaman dengan F5, lalu buka tab System Limits
18. Klik `[Reset to Default]`
19. Verifikasi toast error "Error, failed to reset system limits settings."
20. Verifikasi tab tidak refresh
21. Muat ulang halaman dengan F5, lalu buka kembali tab System Limits
22. Verifikasi nilai tersimpan tetap Bulk Transaction Row Limit `2000`, Selection Limit `1500`, Register Asset Bulk Limit `2500`, Hierarchy Depth Limit `60`, Master Data Count Limit `20000`, Max Visible Columns `25`

## Notes

- Kelas harness b (fault injection): spec ini hanya memuat TC kegagalan yang dipaksa; kegagalan dipicu intercept di atas backend nyata (Mode FE+BE) karena Expected mengasersi state backend (nilai tersimpan setelah F5).
- Langkah penghubung tanpa `Verifikasi`: langkah 1 (memasang intercept) dan langkah 2, 3, 7, 9, 10, 14, 16, 17, 21 (mengatur nilai tersimpan non-default sebagai precondition TC dan memuat ulang halaman agar tab membaca nilai dari server).
- Temuan untuk QA:
  - Post Condition "Tidak ada perubahan data" tidak punya langkah observasi di TC sehingga tidak diasersi; Post Condition "tersimpan" teramati lewat Expected setelah F5.
