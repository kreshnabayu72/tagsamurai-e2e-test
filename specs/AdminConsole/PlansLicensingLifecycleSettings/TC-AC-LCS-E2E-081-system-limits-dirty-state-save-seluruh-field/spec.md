---
id: TC-AC-LCS-E2E-081-system-limits-dirty-state-save-seluruh-field
title: "Tab System Limits: Dirty State dan Save Seluruh Enam Field"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-LCS-282
  - TC-AC-LCS-283
coverage:
  web: automated
---

# Tab System Limits: Dirty State dan Save Seluruh Enam Field

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net` (nama tampil `Andi Wijaya`), password dari `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Plans & Licensing > Lifecycle Settings, tab Trial Settings aktif); hook `after` spec mengembalikan sesi ke akun default suite (Total Control). Tidak ada ganti akun di tengah spec.
- Data: konfigurasi ketujuh tab Lifecycle Settings pada nilai default (Pre-setup 7: Trial 30, 50, 10, OFF, 7, 1; Free Plan 365; License Timing 24, 2, 2; Client Lifecycle 45, 30, 7, 1, 30, 30, 10, 2, 730; Recycle Bin 30; Approval 3; System Limits 1000, 1000, 1000, 50, 10000, 20) dipulihkan hook `beforeEach` suite dan hook `after` suite lewat Fixture BE. Berkas fixture data modul belum ada (disediakan tim FE); spec menulis nilai uji sesuai TC dan merujuk `Fixture.<berkas>.<kunci>` setelah berkas itu tersedia.
- Flag Guided Tooltip halaman Lifecycle Settings disetel true oleh hook suite `before` dan dipulihkan hook `after` (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`).
- Kemampuan teknis (disediakan tim FE/BE): Fixture BE untuk memulihkan konfigurasi tab ke nilai default (dipakai hook suite). Endpoint tidak ditulis di spec ini.
- Data uji: Bulk Transaction Row Limit `1000` lalu `1001`; nilai Save: Bulk Transaction Row Limit `2000`, Selection Limit `1500`, Register Asset Bulk Limit `2500`, Hierarchy Depth Limit `60`, Master Data Count Limit `20000`, Max Visible Columns `25`.
- State global yang diubah: keenam nilai tersimpan System Limits pada TC-AC-LCS-283; pemulihan lewat hook `beforeEach` suite dan hook `after` suite (Fixture BE).
- Env var `AC_TC_PASSWORD` sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture.

## Test Steps

1. Klik tab System Limits

### TC-AC-LCS-282: Tab System Limits: Save mengikuti dirty state dan Reset to Default selalu enabled

2. Verifikasi `[Save]` disabled
3. Verifikasi `[Reset to Default]` enabled
4. Ubah Bulk Transaction Row Limit dari `1000` menjadi `1001`
5. Verifikasi `[Save]` enabled
6. Verifikasi `[Reset to Default]` enabled
7. Kembalikan Bulk Transaction Row Limit menjadi `1000`
8. Verifikasi `[Save]` disabled kembali
9. Verifikasi `[Reset to Default]` tetap enabled

### TC-AC-LCS-283: Save tab System Limits dengan seluruh field diubah ke nilai valid

10. Ubah Bulk Transaction Row Limit menjadi `2000`
11. Ubah Selection Limit menjadi `1500`
12. Ubah Register Asset Bulk Limit menjadi `2500`
13. Ubah Hierarchy Depth Limit menjadi `60`
14. Ubah Master Data Count Limit menjadi `20000`
15. Ubah Max Visible Columns menjadi `25`
16. Klik `[Save]`
17. Verifikasi toast sukses "Success, system limits settings have been saved."
18. Verifikasi tab refresh: field memuat nilai tersimpan
19. Verifikasi `[Save]` disabled setelah tab refresh
20. Muat ulang halaman dengan F5, lalu buka kembali tab System Limits
21. Verifikasi Bulk Transaction Row Limit bernilai `2000`
22. Verifikasi Selection Limit bernilai `1500`
23. Verifikasi Register Asset Bulk Limit bernilai `2500`
24. Verifikasi Hierarchy Depth Limit bernilai `60`
25. Verifikasi Master Data Count Limit bernilai `20000`
26. Verifikasi Max Visible Columns bernilai `25`

## Notes

- Langkah penghubung tanpa `Verifikasi`: langkah 1 (berpindah ke tab) dan langkah 20 (membuka tab dalam keadaan termuat baru).
- Temuan untuk QA:
  - Post Condition "Tidak ada perubahan data" tidak punya langkah observasi di TC sehingga tidak diasersi; Post Condition "tersimpan" teramati lewat Expected setelah F5.
  - Post Condition "Entri Changelog" (satu baris per field berubah) pada TC yang menyimpan atau mereset tidak punya langkah observasi di TC sehingga tidak diasersi di spec ini; spec ini tidak mengamati Changelog.
