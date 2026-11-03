---
id: TC-AC-LCS-E2E-025-role-matrix-positif-manage-plans-lifecycle-recycle
title: "Role Matrix Positif: Manage Plans & Licensing Mengeksekusi Save dan Reset Tab Client Lifecycle dan Recycle Bin"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-LCS-83
  - TC-AC-LCS-84
  - TC-AC-LCS-85
  - TC-AC-LCS-86
coverage:
  web: automated
---

# Role Matrix Positif: Manage Plans & Licensing Mengeksekusi Save dan Reset Tab Client Lifecycle dan Recycle Bin

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

### TC-AC-LCS-83: Save tab Client Lifecycle oleh aktor Manage plans & licensing (Update) berhasil

1. Klik tab Client Lifecycle pada tab bar
2. Ubah Notify Plan Owner Before Event dari `45` menjadi `46`
3. Klik `[Save]`
4. Verifikasi Toast sukses: "Success, client lifecycle settings have been saved."
5. Verifikasi Tab refresh: Notify Plan Owner Before Event bernilai `46`
6. Verifikasi `[Save]` disabled

### TC-AC-LCS-84: Reset to Default tab Client Lifecycle oleh aktor Manage plans & licensing (Update) berhasil

7. Klik `[Reset to Default]`
8. Verifikasi Toast sukses: "Success, client lifecycle settings have been reset to default."
9. Verifikasi Notify Plan Owner Before Event kembali `45`
10. Verifikasi `[Save]` disabled

### TC-AC-LCS-85: Save tab Recycle Bin oleh aktor Manage plans & licensing (Update) berhasil

11. Klik tab Recycle Bin pada tab bar
12. Ubah Permanently Delete Recycle Bin dari `30` menjadi `31`
13. Klik `[Save]`
14. Verifikasi Toast sukses: "Success, recycle bin settings have been saved."
15. Verifikasi Tab refresh: Permanently Delete Recycle Bin bernilai `31`
16. Verifikasi `[Save]` disabled

### TC-AC-LCS-86: Reset to Default tab Recycle Bin oleh aktor Manage plans & licensing (Update) berhasil

17. Klik `[Reset to Default]`
18. Verifikasi Toast sukses: "Success, recycle bin settings have been reset to default."
19. Verifikasi Permanently Delete Recycle Bin kembali `30`
20. Verifikasi `[Save]` disabled

## Notes

- Spec Role Matrix positif dengan satu role (Manage plans & licensing, Read dan Update); akun login di hook `before` spec dan hook `after` mengembalikan sesi ke akun default suite. Langkah penghubung (S-03): klik tab pada blok TC yang dimulai dari tab selain Trial Settings (Precondition TC).
- Blok Reset to Default memakai nilai tersimpan hasil blok Save sebelumnya dalam spec yang sama (TC Reset menyatakan nilai tersimpan non-default pada Precondition d); spec tidak menumpang spec lain (S-06).
- Temuan untuk QA: Post Condition TC Save ("satu entri Changelog tab ... tercatat") dan Post Condition nilai tersimpan tidak punya langkah observasi di TC; tidak diasersi (S-01) dan dicatat di sini. Entri Changelog permanen sehingga spec tidak mengasersi jumlah absolut (S-12).
- Mekanisme Fixture BE (pemulihan konfigurasi per tab dan General Settings) tidak didefinisikan di TC, PRD, atau LLD; ditulis sebagai kemampuan yang disediakan tim FE/BE tanpa endpoint karangan (S-13, R-19).
