---
id: TC-AC-DC-E2E-017-role-matrix-negatif-partner-client-tanpa-capability
title: "Role Matrix Negatif: Partner, Client, dan Principal Tanpa Capability Ditolak"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AC-DC-46
  - TC-AC-DC-47
  - TC-AC-DC-48
  - TC-AC-DC-49
coverage:
  web: automated
---
# Role Matrix Negatif: Partner, Client, dan Principal Tanpa Capability Ditolak

## Prerequisites

- Mode: FE+BE.
- Aktor pertama: Partner (Pre-setup #11); Login di hook `before` spec ini; halaman awal hook `beforeEach` suite tidak dipakai; TC membuka halamannya sendiri. Ganti akun eksplisit di tengah spec ke Client (#12), lalu ke Principal tanpa capability (#8). Hook `after` mengembalikan sesi ke akun default suite.

| Role yang diuji | Akun (Pre-setup) | Password |
|---|---|---|
| Total Control entitas Partner `Partner Jaringan` | #11 `totalControlPartner_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.AC_DC_PARTNER_PASSWORD` |
| Total Control entitas Client `Client Jaringan` | #12 `totalControlClient_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.AC_DC_CLIENT_PASSWORD` |
| Principal tanpa capability Manage device master data (hanya Manage language) | #8 `noCapabilityDevCat_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.AC_DC_NOCAP_PASSWORD` |

- Data Pre-setup: #14 (Pohon Uji Kategori, hanya dibaca). Nilai data mengacu ke fixture `settingsDeviceCategory` (belum ada; disediakan tim FE). Nama node Pre-setup #14 ditulis sebagaimana di TC.
- Spec ini tidak membuat data; tidak ada seeding dan cleanup data.
- Env var `AC_DC_CLIENT_PASSWORD`, `AC_DC_NOCAP_PASSWORD`, `AC_DC_PARTNER_PASSWORD` belum terdaftar: perlu didaftarkan tim FE di `spectra.config.ts` (`executionConfig.environmentVariables`) dan `.env.example`.
- Suite berjalan serial (`parallel: false`): pohon Category, Changelog, dan log audit adalah state bersama.

## Test Steps

### TC-AC-DC-46: Partner tidak memiliki akses ke Category dan ditolak lewat URL langsung

1. Ketik URL `Settings > Device > Device Name` langsung di address bar
2. Verifikasi toast error "You don't have permission to do this." tampil
3. Verifikasi Sidebar Category dan tree tidak tampil
4. Verifikasi tidak ada redirect ke halaman unauthorized
5. Tutup toast error

### TC-AC-DC-47: Client tidak memiliki akses ke Category dan ditolak lewat URL langsung

6. Logout dari akun Partner
7. Login sebagai Client (`totalControlClient_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.AC_DC_CLIENT_PASSWORD`)
8. Ketik URL `Settings > Device > Device Name` langsung di address bar
9. Verifikasi toast error "You don't have permission to do this." tampil
10. Verifikasi Sidebar Category dan tree tidak tampil
11. Verifikasi tidak ada redirect ke halaman unauthorized
12. Tutup toast error

### TC-AC-DC-48: Principal tanpa capability Manage device master data ditolak lewat URL langsung

13. Logout dari akun Client
14. Login sebagai Principal tanpa capability Manage device master data (`noCapabilityDevCat_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.AC_DC_NOCAP_PASSWORD`)
15. Ketik URL `Settings > Device > Device Name` langsung di address bar
16. Verifikasi toast error "You don't have permission to do this." tampil
17. Verifikasi Sidebar Category tidak tampil
18. Verifikasi tidak ada redirect ke halaman unauthorized
19. Tutup toast error

### TC-AC-DC-49: Item menu Settings > Device untuk role tanpa capability Manage device master data

20. Buka halaman beranda Admin Console
21. Buka menu navigasi Settings
22. Verifikasi sedikitnya satu item menu Settings lain tampil di daftar menu Settings
23. Verifikasi item menu Settings > Device tidak tampil (Hidden) di daftar menu Settings

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-device-category/TestCases/tc-settings-device-category.md`.
- Subjudul `###` memetakan langkah ke id TC granular.
- Spec Role Matrix negatif ditulis per blok akun (bukan perulangan satu `it()` per role) karena ganti akun menuntut Step eksplisit dan akun pertama login di hook `before` (bagian 3a, KEPUTUSAN 2026-10-30). Blok TC-AC-DC-46, 47, dan 48 berisi langkah identik; TC-AC-DC-49 memakai akun TC-AC-DC-48 tanpa ganti akun.
- Langkah penghubung: langkah 5, 12, 19 (menutup toast error sebelum TC berikutnya, R-12), 6 dan 13 (ganti akun eksplisit, S-07), 20 (membuka beranda Admin Console untuk memulai TC-AC-DC-49), TC-AC-DC-49 (langkah 20 dan sesudahnya) memakai akun yang sama dengan blok TC-AC-DC-48.
- Langkah pembanding di dalam TC-AC-DC-49: sedikitnya satu item menu Settings lain tampil sebagai anchor absence item menu (8b butir 2); item itu tidak disebut TC sehingga ditulis generik.
- Temuan untuk QA:
  - Hook `beforeEach` suite membuka Settings > Device > Device Name; untuk akun yang ditolak di halaman itu (Distributor, Partner, Client, tanpa capability) pembukaan itu memicu penolakan akses. Perlu pengecualian di hook suite; langkah pertama tiap TC spec ini membuka halaman sendiri.
  - Di TC-AC-DC-49 menu Settings yang tersisa bagi akun hanya-Manage language tidak disebut; anchor ditulis generik.
  - Post Condition TC-AC-DC-46, 47, 48, dan 49 ('-') tidak punya langkah observasi dan tidak diasersi.
