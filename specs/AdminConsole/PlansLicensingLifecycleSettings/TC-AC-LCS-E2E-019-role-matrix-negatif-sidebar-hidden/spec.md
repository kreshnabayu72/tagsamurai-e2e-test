---
id: TC-AC-LCS-E2E-019-role-matrix-negatif-sidebar-hidden
title: "Role Matrix Negatif: Item Sidebar Hidden untuk Principal Tanpa Capability, Distributor, Partner, dan Client"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AC-LCS-62
  - TC-AC-LCS-64
  - TC-AC-LCS-66
  - TC-AC-LCS-68
coverage:
  web: automated
---

# Role Matrix Negatif: Item Sidebar Hidden untuk Principal Tanpa Capability, Distributor, Partner, dan Client

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Principal tanpa Global Role Manage plans & licensing `noCapabilityAdminConsole_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.AC_NOCAP_PASSWORD` (terdaftar di `executionConfig.environmentVariables` dan `.env.example`).
- Login akun aktor pertama di hook `before` spec ini; layar awal spec ini dikecualikan dari pembukaan Lifecycle Settings oleh hook `beforeEach` suite (pengecualian di `suite.md`): layar awal adalah halaman utama setelah login (spec 019) atau tujuan akses langsung (spec 020), diatur di hook `before` atau langkah spec. Hook `after` spec ini mengembalikan sesi ke akun default suite (Total Control, `AC_TC_PASSWORD`). Ganti akun di tengah spec ditulis sebagai langkah eksplisit.
- Akun aktor: Distributor (user entitas Distributor) `distributorUser_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.AC_DIST_PASSWORD` (terdaftar di `executionConfig.environmentVariables` dan `.env.example`).
- Akun aktor: Partner (user entitas Partner) `partnerUser_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.AC_PARTNER_PASSWORD` (terdaftar di `executionConfig.environmentVariables` dan `.env.example`).
- Akun aktor: Client (user entitas Client) `clientUser_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.AC_CLIENT_PASSWORD` (terdaftar di `executionConfig.environmentVariables` dan `.env.example`).
- Role yang diuji:

| Role | Akun | Env var password |
|---|---|---|
| Principal tanpa Global Role Manage plans & licensing | `noCapabilityAdminConsole_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.AC_NOCAP_PASSWORD` |
| Distributor (user entitas Distributor) | `distributorUser_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.AC_DIST_PASSWORD` |
| Partner (user entitas Partner) | `partnerUser_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.AC_PARTNER_PASSWORD` |
| Client (user entitas Client) | `clientUser_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.AC_CLIENT_PASSWORD` |

- Data: konfigurasi ketujuh tab Lifecycle Settings pada nilai default (Pre-setup 7: Trial Settings 30, 50, 10, OFF, 7, 1; Free Plan Settings 365; License Timing 24, 2, 2; Client Lifecycle 45, 30, 7, 1, 30, 30, 10, 2, 730; Recycle Bin 30; Approval Settings 3; System Limits 1000, 1000, 1000, 50, 10000, 20); General Settings Date Format `dd MMM yy`, Time Format 24 jam, Time Zone UTC. Hook `beforeEach` suite memulihkan semuanya lewat Fixture BE dan hook `after` suite memulihkannya sekali lagi (kemampuan Fixture BE disediakan tim FE/BE). Berkas `fixtures/<modul>.json` untuk modul ini belum ada; nilai default dan nilai uji pada langkah dirujuk lewat `Fixture.lifecycleSettings.<kunci>` setelah tim FE menyediakannya.
- Hook `beforeEach` suite membuka halaman Lifecycle Settings untuk akun aktor default; untuk akun aktor spec ini yang tidak berhak, layar awal adalah halaman utama setelah login (Precondition TC) dan spec tidak bergantung pada halaman Lifecycle Settings terbuka.
- Flag Guided Tooltip halaman ini disetel true oleh hook `before` suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Kemampuan teknis: Fixture BE (pemulihan konfigurasi per tab dan General Settings, disediakan tim FE/BE).
- State global: ketujuh tab adalah satu set pengaturan platform-wide dan suite berjalan serial (`parallel: false`); konfigurasi dan Changelog dipulihkan sebagaimana tertulis pada baris Data. Entri Changelog permanen dan tidak dapat dihapus lewat UI.
- Env var: hanya `Spectra.env.*` yang tertulis pada baris akun di atas yang dipakai; password tidak ditulis di spec atau fixture.

## Test Steps

### TC-AC-LCS-62: Item sidebar Lifecycle Settings Hidden untuk Principal tanpa capability Manage plans & licensing

1. Buka grup Plans & Licensing pada sidebar
2. Verifikasi Sedikitnya satu item menu lain tampil pada sidebar yang sama (anchor untuk asersi Hidden)
3. Verifikasi Item "Lifecycle Settings" tidak tampil sama sekali pada grup Plans & Licensing (Hidden, bukan disabled)

### TC-AC-LCS-64: Item sidebar Lifecycle Settings Hidden untuk Distributor

4. Ganti akun: logout dari akun Principal tanpa Global Role Manage plans & licensing
5. Login dengan akun Distributor (user entitas Distributor) `distributorUser_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.AC_DIST_PASSWORD`
6. Buka grup Plans & Licensing pada sidebar
7. Verifikasi Sedikitnya satu item menu lain tampil pada sidebar yang sama (anchor untuk asersi Hidden)
8. Verifikasi Item "Lifecycle Settings" tidak tampil sama sekali pada grup Plans & Licensing (Hidden, bukan disabled)

### TC-AC-LCS-66: Item sidebar Lifecycle Settings Hidden untuk Partner

9. Ganti akun: logout dari akun Distributor (user entitas Distributor)
10. Login dengan akun Partner (user entitas Partner) `partnerUser_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.AC_PARTNER_PASSWORD`
11. Buka grup Plans & Licensing pada sidebar
12. Verifikasi Sedikitnya satu item menu lain tampil pada sidebar yang sama (anchor untuk asersi Hidden)
13. Verifikasi Item "Lifecycle Settings" tidak tampil sama sekali pada grup Plans & Licensing (Hidden, bukan disabled)

### TC-AC-LCS-68: Item sidebar Lifecycle Settings Hidden untuk Client

14. Ganti akun: logout dari akun Partner (user entitas Partner)
15. Login dengan akun Client (user entitas Client) `clientUser_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.AC_CLIENT_PASSWORD`
16. Buka grup Plans & Licensing pada sidebar
17. Verifikasi Sedikitnya satu item menu lain tampil pada sidebar yang sama (anchor untuk asersi Hidden)
18. Verifikasi Item "Lifecycle Settings" tidak tampil sama sekali pada grup Plans & Licensing (Hidden, bukan disabled)

## Notes

- Spec Role Matrix ditulis per blok role karena ganti akun menuntut Step eksplisit (bagian 3a, KEPUTUSAN 2026-10-30). Langkah penghubung (S-03, S-07): logout lalu login pada pergantian akun.
- Temuan untuk QA: TC 62, 64, 66, dan 68 menulis "Buka grup Plans & Licensing pada sidebar bila grup tampil" (langkah bersyarat) tanpa menyatakan apakah grup tampil bagi tiap aktor; spec menulis langkah tanpa syarat (S-08) dan asersi Hidden didahului `Verifikasi` item menu lain pada sidebar tampil (bagian 8b butir 2). Bila grup tidak tampil untuk suatu aktor, TC perlu menyatakannya.
- Hook `beforeEach` suite (membuka halaman Lifecycle Settings) tidak berlaku untuk akun tanpa capability; pengecualiannya sudah dinyatakan di `suite.md`.
- Mekanisme Fixture BE (pemulihan konfigurasi per tab dan General Settings) tidak didefinisikan di TC, PRD, atau LLD; ditulis sebagai kemampuan yang disediakan tim FE/BE tanpa endpoint karangan (S-13, R-19).
