---
id: TC-AC-LCS-E2E-018-role-matrix-positif-sidebar-dan-halaman
title: "Role Matrix Positif: Item Sidebar dan Halaman Lifecycle Settings Terbuka per Role"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-LCS-58
  - TC-AC-LCS-59
  - TC-AC-LCS-60
  - TC-AC-LCS-61
coverage:
  web: automated
---

# Role Matrix Positif: Item Sidebar dan Halaman Lifecycle Settings Terbuka per Role

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net` (nama tampil `Andi Wijaya`), password dari `Spectra.env.AC_TC_PASSWORD` (akun default suite).
- Login akun aktor pertama (Total Control) di hook `before` spec ini; layar awal spec ini dikecualikan dari pembukaan Lifecycle Settings oleh hook `beforeEach` suite (pengecualian di `suite.md`): halaman utama setelah login sesuai Precondition TC 58 sampai 61, diatur di hook `before` spec atau langkah spec. Ganti akun di tengah spec ditulis sebagai langkah eksplisit.
- Akun aktor: Default User `defaultUserAdminConsole_automated_{namaCompany}@qwertysystem.net` (nama tampil `Dewi Lestari`), password dari `Spectra.env.AC_DU_PASSWORD` (terdaftar di `executionConfig.environmentVariables` dan `.env.example`).
- Akun aktor: Read Only `readOnlyAdminConsole_automated_{namaCompany}@qwertysystem.net` (nama tampil `Hadi Pratama`), password dari `Spectra.env.AC_RO_PASSWORD` (terdaftar di `executionConfig.environmentVariables` dan `.env.example`).
- Akun aktor: Manage plans & licensing (Read dan Update) `managePlansLicensingAdminConsole_automated_{namaCompany}@qwertysystem.net` (nama tampil `Rina Kusuma`), password dari `Spectra.env.AC_MPL_PASSWORD` (terdaftar di `executionConfig.environmentVariables` dan `.env.example`).
- Role yang diuji:

| Role | Akun | Env var password |
|---|---|---|
| Total Control | `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.AC_TC_PASSWORD` |
| Default User | `defaultUserAdminConsole_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.AC_DU_PASSWORD` |
| Read Only | `readOnlyAdminConsole_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.AC_RO_PASSWORD` |
| Manage plans & licensing (Read dan Update) | `managePlansLicensingAdminConsole_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.AC_MPL_PASSWORD` |

- Data: konfigurasi ketujuh tab Lifecycle Settings pada nilai default (Pre-setup 7: Trial Settings 30, 50, 10, OFF, 7, 1; Free Plan Settings 365; License Timing 24, 2, 2; Client Lifecycle 45, 30, 7, 1, 30, 30, 10, 2, 730; Recycle Bin 30; Approval Settings 3; System Limits 1000, 1000, 1000, 50, 10000, 20); General Settings Date Format `dd MMM yy`, Time Format 24 jam, Time Zone UTC. Hook `beforeEach` suite memulihkan semuanya lewat Fixture BE dan hook `after` suite memulihkannya sekali lagi (kemampuan Fixture BE disediakan tim FE/BE). Berkas `fixtures/<modul>.json` untuk modul ini belum ada; nilai default dan nilai uji pada langkah dirujuk lewat `Fixture.lifecycleSettings.<kunci>` setelah tim FE menyediakannya.
- Flag Guided Tooltip halaman ini disetel true oleh hook `before` suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Kemampuan teknis: Fixture BE (pemulihan konfigurasi per tab dan General Settings, disediakan tim FE/BE).
- State global: ketujuh tab adalah satu set pengaturan platform-wide dan suite berjalan serial (`parallel: false`); konfigurasi dan Changelog dipulihkan sebagaimana tertulis pada baris Data. Entri Changelog permanen dan tidak dapat dihapus lewat UI.
- Env var: hanya `Spectra.env.*` yang tertulis pada baris akun di atas yang dipakai; password tidak ditulis di spec atau fixture.

## Test Steps

### TC-AC-LCS-58: Item sidebar Lifecycle Settings tampil dan halaman terbuka untuk Total Control

1. Buka grup Plans & Licensing pada sidebar
2. Verifikasi Item "Lifecycle Settings" tampil pada grup Plans & Licensing
3. Klik item "Lifecycle Settings"
4. Verifikasi Halaman terbuka pada tab Trial Settings
5. Verifikasi Breadcrumb "Plans & Licensing > Lifecycle Settings > Trial Settings"

### TC-AC-LCS-59: Item sidebar Lifecycle Settings tampil dan halaman terbuka untuk Default User

6. Ganti akun: logout dari akun Total Control
7. Login dengan akun Default User `defaultUserAdminConsole_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.AC_DU_PASSWORD`
8. Buka grup Plans & Licensing pada sidebar
9. Verifikasi Item "Lifecycle Settings" tampil pada grup Plans & Licensing
10. Klik item "Lifecycle Settings"
11. Verifikasi Halaman terbuka pada tab Trial Settings
12. Verifikasi Breadcrumb "Plans & Licensing > Lifecycle Settings > Trial Settings"

### TC-AC-LCS-60: Item sidebar Lifecycle Settings tampil dan halaman terbuka untuk Read Only

13. Ganti akun: logout dari akun Default User
14. Login dengan akun Read Only `readOnlyAdminConsole_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.AC_RO_PASSWORD`
15. Buka grup Plans & Licensing pada sidebar
16. Verifikasi Item "Lifecycle Settings" tampil pada grup Plans & Licensing
17. Klik item "Lifecycle Settings"
18. Verifikasi Halaman terbuka pada tab Trial Settings
19. Verifikasi Breadcrumb "Plans & Licensing > Lifecycle Settings > Trial Settings"

### TC-AC-LCS-61: Item sidebar Lifecycle Settings tampil dan halaman terbuka untuk Manage plans & licensing

20. Ganti akun: logout dari akun Read Only
21. Login dengan akun Manage plans & licensing (Read dan Update) `managePlansLicensingAdminConsole_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.AC_MPL_PASSWORD`
22. Buka grup Plans & Licensing pada sidebar
23. Verifikasi Item "Lifecycle Settings" tampil pada grup Plans & Licensing
24. Klik item "Lifecycle Settings"
25. Verifikasi Halaman terbuka pada tab Trial Settings
26. Verifikasi Breadcrumb "Plans & Licensing > Lifecycle Settings > Trial Settings"

## Notes

- Spec Role Matrix ditulis per blok role karena ganti akun menuntut Step eksplisit (akun pertama login di hook `before`; bagian 3a, KEPUTUSAN 2026-10-30). Langkah penghubung (S-03, S-07): logout lalu login pada pergantian akun.
- Precondition TC 58 sampai 61 menyatakan user berada di halaman utama setelah login, sedangkan hook `beforeEach` suite membuka halaman Lifecycle Settings; spec ini dikecualikan darinya (pengecualian dinyatakan di `suite.md`).
- Mekanisme Fixture BE (pemulihan konfigurasi per tab dan General Settings) tidak didefinisikan di TC, PRD, atau LLD; ditulis sebagai kemampuan yang disediakan tim FE/BE tanpa endpoint karangan (S-13, R-19).
