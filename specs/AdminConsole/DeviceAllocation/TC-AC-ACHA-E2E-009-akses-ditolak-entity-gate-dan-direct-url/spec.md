---
id: TC-AC-ACHA-E2E-009-akses-ditolak-entity-gate-dan-direct-url
title: "Akses Ditolak: Entity Gate Client dan Direct URL oleh Aktor Tanpa Capability Read"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AC-ACHA-48
  - TC-AC-ACHA-49
  - TC-AC-ACHA-52
coverage:
  web: automated
---

# Akses Ditolak: Entity Gate Client dan Direct URL oleh Aktor Tanpa Capability Read

## Prerequisites

- Mode: FE+BE.
- Akun yang diuji:

| TC | Akun | Pre-setup | Email | Env var password |
|---|---|---|---|---|
| TC-48 | Pengguna entitas Client PT Sejahtera Logistik tanpa role Admin Console | #39 | `clientUser_automated_qaTeam1@qwertysystem.net` | `Spectra.env.AC_DA_CLIENT_USER_PASSWORD` |
| TC-49 | Pengguna entitas Client PT Sejahtera Logistik dengan role Manage allocation (Create, Read, Update) | #40 | `clientUserCapability_automated_qaTeam1@qwertysystem.net` | `Spectra.env.AC_DA_CLIENT_CAP_PASSWORD` |
| TC-52 | Role tanpa capability Manage allocation, entitas PT Global Distribusi | #41 | `noCapabilityDistributor_automated_qaTeam1@qwertysystem.net` | `Spectra.env.AC_DA_NOCAP_DIST_PASSWORD` |

- Login akun aktor pertama (#39) di hook `before` spec ini. Layar awal spec ini adalah Dashboard Admin Console, bukan halaman Device Allocation, karena entitas Client dan role tanpa capability tidak dapat membuka halaman Device Allocation (hook `beforeEach` suite membuka layar awal akun yang dipakai spec). Hook `after` mengembalikan sesi ke akun default suite (Total Control Principal PT ABC, `AC_TC_PASSWORD`). Ganti akun di tengah spec memakai langkah logout dan login eksplisit.
- Hook suite (dinyatakan sekali di `suite.md`): sesi API aktor, flag Guided Tooltip `guided_tooltip_seen_ac-device-allocation` true untuk akun aktor, fixture API Pre-setup #20 (disediakan tim FE/BE; endpoint tidak dikarang di spec ini), dan pemulihan preferensi kolom Setup Column. Suite berjalan serial (`parallel: false`).
- Data Pre-setup (hanya dibaca, tidak diubah): Client PT Sejahtera Logistik Active (Pre-setup #7); akun Pre-setup #39, #40, dan #41. Spec tidak membuat data.
- Kemampuan teknis: navigasi langsung ke URL halaman Allocation > Device Allocation lewat address bar; path route halaman diketahui tim FE dan tidak dikarang di spec ini.
- General Settings Pre-setup #1 tidak diubah. State global: tidak ada yang diubah; suite berjalan serial.
- Env var `AC_TC_PASSWORD` sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example`. Env var `AC_DA_CLIENT_USER_PASSWORD`, `AC_DA_CLIENT_CAP_PASSWORD`, dan `AC_DA_NOCAP_DIST_PASSWORD` belum terdaftar: didaftarkan tim FE di `spectra.config.ts` dan `.env.example` pada tahap script. Password tidak ditulis di spec atau fixture.

## Test Steps

### TC-AC-ACHA-48: Entitas Client tidak dapat mengakses menu Device Allocation

1. Periksa sidebar
2. Verifikasi item menu Dashboard tampil di sidebar
3. Verifikasi menu `Allocation > Device Allocation` dan seluruh menu Allocation tidak tampil bagi entitas Client
4. Ketik URL halaman Allocation > Device Allocation langsung di address bar dan tekan Enter
5. Verifikasi toast error "You don't have permission to do this."
6. Verifikasi UI di-refresh tanpa redirect ke halaman terpisah
7. Verifikasi tidak ada data transaksi yang ditampilkan

### Ganti akun ke pengguna Client dengan role Manage allocation

8. Logout dari akun pengguna Client
9. Login sebagai pengguna Client dengan role Manage allocation (`clientUserCapability_automated_qaTeam1@qwertysystem.net`, password dari `Spectra.env.AC_DA_CLIENT_CAP_PASSWORD`)

### TC-AC-ACHA-49: Entity Gate menang atas role untuk entitas Client

10. Muat ulang aplikasi (F5)
11. Periksa sidebar
12. Verifikasi item menu Dashboard tampil di sidebar
13. Verifikasi menu `Allocation > Device Allocation` tetap tidak tampil walau akun di-assign capability Manage allocation (Entity Gate menang atas role)
14. Ketik URL halaman Allocation > Device Allocation langsung di address bar dan tekan Enter
15. Verifikasi akses URL langsung ditolak
16. Verifikasi tidak ada data transaksi yang dapat dibaca akun ini

### Ganti akun ke role tanpa capability Manage allocation

17. Logout dari akun pengguna Client dengan role Manage allocation
18. Login sebagai role tanpa capability Manage allocation Distributor (`noCapabilityDistributor_automated_qaTeam1@qwertysystem.net`, password dari `Spectra.env.AC_DA_NOCAP_DIST_PASSWORD`)

### TC-AC-ACHA-52: Direct URL oleh aktor tanpa capability Read ditolak

19. Ketik URL halaman Allocation > Device Allocation langsung di address bar dan tekan Enter (tanpa melalui menu)
20. Verifikasi toast error "You don't have permission to do this."
21. Verifikasi UI di-refresh tanpa redirect ke halaman unauthorized terpisah
22. Verifikasi halaman List tidak menampilkan data transaksi

## Notes

- Mode: FE+BE. Sumber: `admin-console/device-allocation/TestCases/tc-device-allocation.md`. Spec negatif per topik (bagian 3a): akses ditolak karena Entity Gate atau tanpa capability Read; tanpa aksi tulis.
- Spec ditulis per blok akun karena ganti akun menuntut Step eksplisit; langkah tiap blok tidak identik (TC-52 tanpa pemeriksaan sidebar karena Hidden menu role tanpa capability diuji di spec 008 TC-51).
- Anchor absence (bagian 8b butir 2): asersi menu tidak tampil didahului `Verifikasi` item menu Dashboard tampil di sidebar yang sama; asersi "tidak ada data transaksi" didahului `Verifikasi` toast penolakan atau UI di-refresh sebagai bukti respons sudah diproses.
- Langkah penghubung (S-03): langkah logout dan login pada subjudul "Ganti akun ...", muat ulang aplikasi pada TC-49 (mengikuti Langkah Uji TC).
- Temuan untuk QA:
  - TC-49 Expected b tidak menyebut teks toast; spec hanya mengasersi akses ditolak dan tidak ada data (tidak menyalin copy TC-48 agar tidak menambah asersi, S-02).
  - Path URL halaman Allocation > Device Allocation tidak tertulis di TC, PRD kutipan, atau LLD yang dibaca; disediakan tim FE (S-13).
  - TC-48 Expected b memuat tiga klausa (toast, UI di-refresh tanpa redirect, tidak ada data); dipisah menjadi tiga `Verifikasi`.
  - Layar awal akun entitas Client dan role tanpa capability (Dashboard) tidak dinyatakan TC; spec mengasumsikan Dashboard Admin Console.
  - Post Condition TC-48, TC-49, TC-52 bernilai `-`.
