---
id: TC-AC-LCS-E2E-024-role-matrix-positif-manage-plans-trial-free-license
title: "Role Matrix Positif: Manage Plans & Licensing Mengeksekusi Save dan Reset Tab Trial Settings, Free Plan Settings, dan License Timing"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-LCS-77
  - TC-AC-LCS-78
  - TC-AC-LCS-79
  - TC-AC-LCS-80
  - TC-AC-LCS-81
  - TC-AC-LCS-82
coverage:
  web: automated
---

# Role Matrix Positif: Manage Plans & Licensing Mengeksekusi Save dan Reset Tab Trial Settings, Free Plan Settings, dan License Timing

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Manage plans & licensing (Read dan Update) `managePlansLicensingAdminConsole_automated_{namaCompany}@qwertysystem.net` (nama tampil `Rina Kusuma`), password dari `Spectra.env.AC_MPL_PASSWORD` (terdaftar di `executionConfig.environmentVariables` dan `.env.example`).
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Plans & Licensing > Lifecycle Settings, tab Trial Settings aktif). Hook `after` spec ini mengembalikan sesi ke akun default suite (Total Control, `AC_TC_PASSWORD`).
- Role yang diuji:

| Role | Akun | Env var password |
|---|---|---|
| Manage plans & licensing (Read dan Update) | `managePlansLicensingAdminConsole_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.AC_MPL_PASSWORD` |

- Data: konfigurasi ketujuh tab Lifecycle Settings pada nilai default (Pre-setup 7: Trial Settings 30, 50, 10, OFF, 7, 1; Free Plan Settings 365; License Timing 24, 2, 2; Client Lifecycle 45, 30, 7, 1, 30, 30, 10, 2, 730; Recycle Bin 30; Approval Settings 3; System Limits 1000, 1000, 1000, 50, 10000, 20); General Settings Date Format `dd MMM yy`, Time Format 24 jam, Time Zone UTC. Hook `beforeEach` suite memulihkan semuanya lewat Fixture BE dan hook `after` suite memulihkannya sekali lagi (kemampuan Fixture BE disediakan tim FE/BE). Berkas `fixtures/<modul>.json` untuk modul ini belum ada; nilai default dan nilai uji pada langkah dirujuk lewat `Fixture.lifecycleSettings.<kunci>` setelah tim FE menyediakannya.
- Flag Guided Tooltip halaman ini disetel true oleh hook `before` suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Kemampuan teknis: Fixture BE (pemulihan konfigurasi per tab dan General Settings, disediakan tim FE/BE); pemulihan konfigurasi tiap tab ke default sesudah Save (sudah dipulihkan oleh Reset to Default pada spec ini; Fixture BE di hook `beforeEach` suite menjadi cadangan).
- State global: ketujuh tab adalah satu set pengaturan platform-wide dan suite berjalan serial (`parallel: false`); konfigurasi dan Changelog dipulihkan sebagaimana tertulis pada baris Data. Entri Changelog permanen dan tidak dapat dihapus lewat UI.
- Env var: hanya `Spectra.env.*` yang tertulis pada baris akun di atas yang dipakai; password tidak ditulis di spec atau fixture.

## Test Steps

### TC-AC-LCS-77: Save tab Trial Settings oleh aktor Manage plans & licensing (Update) berhasil

1. Ubah Max Trial Duration dari `30` menjadi `31`
2. Klik `[Save]`
3. Verifikasi Toast sukses: "Success, trial settings have been saved."
4. Verifikasi Tab refresh: Max Trial Duration bernilai `31`
5. Verifikasi `[Save]` disabled

### TC-AC-LCS-78: Reset to Default tab Trial Settings oleh aktor Manage plans & licensing (Update) berhasil

6. Klik `[Reset to Default]`
7. Verifikasi Toast sukses: "Success, trial settings have been reset to default."
8. Verifikasi Max Trial Duration kembali `30`
9. Verifikasi `[Save]` disabled

### TC-AC-LCS-79: Save tab Free Plan Settings oleh aktor Manage plans & licensing (Update) berhasil

10. Klik tab Free Plan Settings pada tab bar
11. Ubah Free Plan Duration dari `365` menjadi `366`
12. Klik `[Save]`
13. Verifikasi Toast sukses: "Success, free plan settings have been saved."
14. Verifikasi Tab refresh: Free Plan Duration bernilai `366`
15. Verifikasi `[Save]` disabled

### TC-AC-LCS-80: Reset to Default tab Free Plan Settings oleh aktor Manage plans & licensing (Update) berhasil

16. Klik `[Reset to Default]`
17. Verifikasi Toast sukses: "Success, free plan settings have been reset to default."
18. Verifikasi Free Plan Duration kembali `365`
19. Verifikasi `[Save]` disabled

### TC-AC-LCS-81: Save tab License Timing oleh aktor Manage plans & licensing (Update) berhasil

20. Klik tab License Timing pada tab bar
21. Ubah Managed Transition Time dari `24` menjadi `25`
22. Klik `[Save]`
23. Verifikasi Toast sukses: "Success, license timing settings have been saved."
24. Verifikasi Tab refresh: Managed Transition Time bernilai `25`
25. Verifikasi `[Save]` disabled

### TC-AC-LCS-82: Reset to Default tab License Timing oleh aktor Manage plans & licensing (Update) berhasil

26. Klik `[Reset to Default]`
27. Verifikasi Toast sukses: "Success, license timing settings have been reset to default."
28. Verifikasi Managed Transition Time kembali `24`
29. Verifikasi `[Save]` disabled

## Notes

- Spec Role Matrix positif dengan satu role (Manage plans & licensing, Read dan Update); akun login di hook `before` spec dan hook `after` mengembalikan sesi ke akun default suite. Langkah penghubung (S-03): klik tab pada blok TC yang dimulai dari tab selain Trial Settings (Precondition TC).
- Blok Reset to Default memakai nilai tersimpan hasil blok Save sebelumnya dalam spec yang sama (TC Reset menyatakan nilai tersimpan non-default pada Precondition d); spec tidak menumpang spec lain (S-06).
- Temuan untuk QA: Post Condition TC Save ("satu entri Changelog tab ... tercatat") dan Post Condition nilai tersimpan tidak punya langkah observasi di TC; tidak diasersi (S-01) dan dicatat di sini. Entri Changelog permanen sehingga spec tidak mengasersi jumlah absolut (S-12).
- Mekanisme Fixture BE (pemulihan konfigurasi per tab dan General Settings) tidak didefinisikan di TC, PRD, atau LLD; ditulis sebagai kemampuan yang disediakan tim FE/BE tanpa endpoint karangan (S-13, R-19).
