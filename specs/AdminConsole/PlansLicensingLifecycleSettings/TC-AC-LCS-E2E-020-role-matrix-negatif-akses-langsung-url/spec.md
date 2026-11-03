---
id: TC-AC-LCS-E2E-020-role-matrix-negatif-akses-langsung-url
title: "Role Matrix Negatif: Akses Langsung URL Ditolak untuk Principal Tanpa Capability, Distributor, Partner, dan Client"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AC-LCS-63
  - TC-AC-LCS-65
  - TC-AC-LCS-67
  - TC-AC-LCS-69
coverage:
  web: automated
---

# Role Matrix Negatif: Akses Langsung URL Ditolak untuk Principal Tanpa Capability, Distributor, Partner, dan Client

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
- Data: URL tab Trial Settings (alamat halaman Lifecycle Settings pada tab Trial Settings) disalin dari sesi akun Total Control (akun default suite, `Spectra.env.AC_TC_PASSWORD`) di hook `before` spec ini sebelum login akun aktor pertama; URL tidak memuat rahasia.
- Flag Guided Tooltip halaman ini disetel true oleh hook `before` suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Kemampuan teknis: Fixture BE (pemulihan konfigurasi per tab dan General Settings, disediakan tim FE/BE); penyalinan URL halaman dari sesi Total Control ke variabel spec.
- State global: ketujuh tab adalah satu set pengaturan platform-wide dan suite berjalan serial (`parallel: false`); konfigurasi dan Changelog dipulihkan sebagaimana tertulis pada baris Data. Entri Changelog permanen dan tidak dapat dihapus lewat UI.
- Env var: hanya `Spectra.env.*` yang tertulis pada baris akun di atas yang dipakai; password tidak ditulis di spec atau fixture.

## Test Steps

### TC-AC-LCS-63: Akses langsung ke URL Lifecycle Settings oleh Principal tanpa capability Manage plans & licensing ditolak

1. Tempel URL tab Trial Settings pada address bar, tekan Enter
2. Verifikasi Toast error: "You don't have permission to do this."
3. Verifikasi Antarmuka dimuat ulang
4. Verifikasi Halaman Lifecycle Settings tidak menampilkan field maupun data konfigurasi
5. Verifikasi Tidak ada redirect ke halaman unauthorized terpisah

### TC-AC-LCS-65: Akses langsung ke URL Lifecycle Settings oleh Distributor ditolak

6. Ganti akun: logout dari akun Principal tanpa Global Role Manage plans & licensing
7. Login dengan akun Distributor (user entitas Distributor) `distributorUser_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.AC_DIST_PASSWORD`
8. Tempel URL tab Trial Settings pada address bar, tekan Enter
9. Verifikasi Toast error: "You don't have permission to do this."
10. Verifikasi Antarmuka dimuat ulang
11. Verifikasi Halaman Lifecycle Settings tidak menampilkan field maupun data konfigurasi
12. Verifikasi Tidak ada redirect ke halaman unauthorized terpisah

### TC-AC-LCS-67: Akses langsung ke URL Lifecycle Settings oleh Partner ditolak

13. Ganti akun: logout dari akun Distributor (user entitas Distributor)
14. Login dengan akun Partner (user entitas Partner) `partnerUser_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.AC_PARTNER_PASSWORD`
15. Tempel URL tab Trial Settings pada address bar, tekan Enter
16. Verifikasi Toast error: "You don't have permission to do this."
17. Verifikasi Antarmuka dimuat ulang
18. Verifikasi Halaman Lifecycle Settings tidak menampilkan field maupun data konfigurasi
19. Verifikasi Tidak ada redirect ke halaman unauthorized terpisah

### TC-AC-LCS-69: Akses langsung ke URL Lifecycle Settings oleh Client ditolak

20. Ganti akun: logout dari akun Partner (user entitas Partner)
21. Login dengan akun Client (user entitas Client) `clientUser_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.AC_CLIENT_PASSWORD`
22. Tempel URL tab Trial Settings pada address bar, tekan Enter
23. Verifikasi Toast error: "You don't have permission to do this."
24. Verifikasi Antarmuka dimuat ulang
25. Verifikasi Halaman Lifecycle Settings tidak menampilkan field maupun data konfigurasi
26. Verifikasi Tidak ada redirect ke halaman unauthorized terpisah

## Notes

- Spec Role Matrix ditulis per blok role karena ganti akun menuntut Step eksplisit (bagian 3a, KEPUTUSAN 2026-10-30). Langkah penghubung (S-03, S-07): logout lalu login pada pergantian akun; logout dan login baru juga membersihkan toast blok sebelumnya sehingga toast error yang sama diasersi lagi dari keadaan bersih (R-12).
- Hook `beforeEach` suite membuka halaman Lifecycle Settings; untuk akun tanpa capability hook itu menghasilkan toast yang sama dengan Expected TC, sehingga spec ini dikecualikan darinya (pengecualian dinyatakan di `suite.md`) agar toast pertama berasal dari langkah spec.
- Mekanisme Fixture BE (pemulihan konfigurasi per tab dan General Settings) tidak didefinisikan di TC, PRD, atau LLD; ditulis sebagai kemampuan yang disediakan tim FE/BE tanpa endpoint karangan (S-13, R-19).
