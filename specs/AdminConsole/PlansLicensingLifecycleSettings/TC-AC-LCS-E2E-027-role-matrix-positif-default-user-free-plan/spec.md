---
id: TC-AC-LCS-E2E-027-role-matrix-positif-default-user-free-plan
title: "Role Matrix Positif: Default User Mengeksekusi Save dan Reset Tab Free Plan Settings"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-LCS-91
  - TC-AC-LCS-92
coverage:
  web: automated
---

# Role Matrix Positif: Default User Mengeksekusi Save dan Reset Tab Free Plan Settings

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Default User `defaultUserAdminConsole_automated_{namaCompany}@qwertysystem.net` (nama tampil `Dewi Lestari`), password dari `Spectra.env.AC_DU_PASSWORD` (terdaftar di `executionConfig.environmentVariables` dan `.env.example`).
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Plans & Licensing > Lifecycle Settings, tab Trial Settings aktif). Hook `after` spec ini mengembalikan sesi ke akun default suite (Total Control, `AC_TC_PASSWORD`).
- Role yang diuji:

| Role | Akun | Env var password |
|---|---|---|
| Default User | `defaultUserAdminConsole_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.AC_DU_PASSWORD` |

- Data: konfigurasi ketujuh tab Lifecycle Settings pada nilai default (Pre-setup 7: Trial Settings 30, 50, 10, OFF, 7, 1; Free Plan Settings 365; License Timing 24, 2, 2; Client Lifecycle 45, 30, 7, 1, 30, 30, 10, 2, 730; Recycle Bin 30; Approval Settings 3; System Limits 1000, 1000, 1000, 50, 10000, 20); General Settings Date Format `dd MMM yy`, Time Format 24 jam, Time Zone UTC. Hook `beforeEach` suite memulihkan semuanya lewat Fixture BE dan hook `after` suite memulihkannya sekali lagi (kemampuan Fixture BE disediakan tim FE/BE). Berkas `fixtures/<modul>.json` untuk modul ini belum ada; nilai default dan nilai uji pada langkah dirujuk lewat `Fixture.lifecycleSettings.<kunci>` setelah tim FE menyediakannya.
- Flag Guided Tooltip halaman ini disetel true oleh hook `before` suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Kemampuan teknis: Fixture BE (pemulihan konfigurasi per tab dan General Settings, disediakan tim FE/BE).
- State global: ketujuh tab adalah satu set pengaturan platform-wide dan suite berjalan serial (`parallel: false`); konfigurasi dan Changelog dipulihkan sebagaimana tertulis pada baris Data. Entri Changelog permanen dan tidak dapat dihapus lewat UI.
- Env var: hanya `Spectra.env.*` yang tertulis pada baris akun di atas yang dipakai; password tidak ditulis di spec atau fixture.

## Test Steps

### TC-AC-LCS-91: Save tab Free Plan Settings oleh Default User berhasil

1. Klik tab Free Plan Settings pada tab bar
2. Ubah Free Plan Duration dari `365` menjadi `400`
3. Klik `[Save]`
4. Verifikasi Toast sukses: "Success, free plan settings have been saved."
5. Verifikasi Free Plan Duration bernilai `400`
6. Verifikasi `[Save]` disabled

### TC-AC-LCS-92: Reset to Default tab Free Plan Settings oleh Default User berhasil

7. Klik `[Reset to Default]`
8. Verifikasi Toast sukses: "Success, free plan settings have been reset to default."
9. Verifikasi Free Plan Duration kembali `365`

## Notes

- Spec Role Matrix positif dengan satu role (Default User); akun login di hook `before` spec dan hook `after` mengembalikan sesi ke akun default suite. Langkah penghubung (S-03): klik tab Free Plan Settings (Precondition TC). Blok Reset memakai nilai tersimpan hasil blok Save dalam spec yang sama (S-06).
- Temuan untuk QA: Post Condition TC 91 dan TC 92 (nilai tersimpan `400` dan `365`) tidak punya langkah observasi di TC; tidak diasersi (S-01). TC 92 tidak memuat Expected `[Save]` disabled sesudah Reset.
- Mekanisme Fixture BE (pemulihan konfigurasi per tab dan General Settings) tidak didefinisikan di TC, PRD, atau LLD; ditulis sebagai kemampuan yang disediakan tim FE/BE tanpa endpoint karangan (S-13, R-19).
