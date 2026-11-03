---
id: TC-AC-LCS-E2E-172-otorisasi-server-entity-reset-trial
title: "Otorisasi Server: Reset to Default Trial Settings oleh Distributor, Partner, dan Client Ditolak"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AC-LCS-602
  - TC-AC-LCS-605
  - TC-AC-LCS-608
coverage:
  web: automated
---

# Otorisasi Server: Reset to Default Trial Settings oleh Distributor, Partner, dan Client Ditolak

## Prerequisites

- Mode: FE+BE. Kelas harness a (defense-in-depth: permintaan langsung ke server tanpa melalui UI).
- Akun aktor: Total Control `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net` (nama tampil `Andi Wijaya`), password dari `Spectra.env.AC_TC_PASSWORD` (akun default suite). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control). Sesi permintaan langsung memakai login API password akun entitas non-Principal (Pre-setup 6): Distributor `distributorUser_automated_{namaCompany}@qwertysystem.net` (`Spectra.env.AC_DIST_PASSWORD`), Partner `partnerUser_automated_{namaCompany}@qwertysystem.net` (`Spectra.env.AC_PARTNER_PASSWORD`), Client `clientUser_automated_{namaCompany}@qwertysystem.net` (`Spectra.env.AC_CLIENT_PASSWORD`); kemampuan sesi API per akun disediakan tim BE/FE.
- Data Pre-setup yang dipakai: ketujuh tab pada nilai default (Pre-setup 7); tab Trial Settings diisi nilai non-default lewat Fixture BE sebagai precondition TC (Data Dinamis 2); ketiga TC menolak permintaan sehingga nilai tidak berubah dan cukup diatur satu kali.
- Kemampuan teknis (disediakan tim FE/BE; tidak ada endpoint yang dikarang): klien HTTP/Fixture BE untuk mengirim permintaan langsung ke server tanpa melalui UI dan membaca status respons; Fixture BE untuk memulihkan ketujuh tab ke nilai default atau mengisi satu tab dengan nilai non-default. Field payload selain yang disebut langkah memakai nilai tersimpan tab itu.
- State global: konfigurasi tab Lifecycle Settings diubah lewat Fixture BE atau permintaan langsung; dipulihkan di hook `beforeEach` dan `after` suite lewat Fixture BE; suite berjalan serial.
- Hook suite (`suite.md`): `beforeEach` memulihkan ketujuh tab Lifecycle Settings ke nilai default, jam server dan jam browser, General Settings (Date Format `dd MMM yy`, Time Format 24 jam, Time Zone UTC), dan intercept, lalu membuka Plans & Licensing > Lifecycle Settings; flag Guided Tooltip halaman ini diset true oleh hook `before` suite; hook `after` suite memulihkan state global. Suite berjalan serial (`parallel: false`).
- Data Pre-setup (akun aktor, nilai default tujuh tab, dataset Changelog, daftar client; tanpa password) dirujuk lewat `Fixture.lifecycleSettings.<kunci>` (`fixtures/lifecycle-settings.json`); nilai uji yang diketik atau dikirim di langkah sama dengan TC (S-02).

## Test Steps

1. Atur lewat Fixture BE: ketujuh tab pada nilai default kecuali tab Trial Settings tersimpan dengan nilai non-default: Max Trial Duration: 45, Max Trial Asset Quota: 100, Max Trial Concurrent User Quota: 20, Require Approval for Trial Activation: ON, First Notification: 14, Second Notification: 3

### TC-AC-LCS-602: Reset to Default Trial Settings lewat permintaan langsung oleh Distributor ditolak

2. Kirim permintaan Reset tab Trial Settings langsung ke server memakai sesi Distributor
3. Verifikasi permintaan ditolak server dengan status `403` (tidak berwenang)
4. Buka tab Trial Settings sebagai Total Control (sesi UI hook `before`) setelah memuat ulang halaman Lifecycle Settings
5. Verifikasi nilai Trial Settings tidak berubah dari nilai non-default (Max Trial Duration: 45, Max Trial Asset Quota: 100, Max Trial Concurrent User Quota: 20, Require Approval for Trial Activation: ON, First Notification: 14, Second Notification: 3)

### TC-AC-LCS-605: Reset to Default Trial Settings lewat permintaan langsung oleh Partner ditolak

6. Kirim permintaan Reset tab Trial Settings langsung ke server memakai sesi Partner
7. Verifikasi permintaan ditolak server dengan status `403` (tidak berwenang)
8. Buka tab Trial Settings sebagai Total Control (sesi UI hook `before`) setelah memuat ulang halaman Lifecycle Settings
9. Verifikasi nilai Trial Settings tidak berubah dari nilai non-default (Max Trial Duration: 45, Max Trial Asset Quota: 100, Max Trial Concurrent User Quota: 20, Require Approval for Trial Activation: ON, First Notification: 14, Second Notification: 3)

### TC-AC-LCS-608: Reset to Default Trial Settings lewat permintaan langsung oleh Client ditolak

10. Kirim permintaan Reset tab Trial Settings langsung ke server memakai sesi Client
11. Verifikasi permintaan ditolak server dengan status `403` (tidak berwenang)
12. Buka tab Trial Settings sebagai Total Control (sesi UI hook `before`) setelah memuat ulang halaman Lifecycle Settings
13. Verifikasi nilai Trial Settings tidak berubah dari nilai non-default (Max Trial Duration: 45, Max Trial Asset Quota: 100, Max Trial Concurrent User Quota: 20, Require Approval for Trial Activation: ON, First Notification: 14, Second Notification: 3)

## Notes

- Mode: FE+BE. Sumber: `admin-console/plans-licensing-lifecycle-settings/TestCases/tc-plans-licensing-lifecycle-settings.md`. Kelas harness a.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- `K-1`: TC defense-in-depth (kelas a) dengan Expected respons API tetap masuk spec FE+BE walau isinya tumpang tindih dengan `tc-plans-licensing-lifecycle-settings-backend.md`; TC granular tetap sumber dan tiap TC tepat satu spec.
- Urutan TC dikelompokkan per entitas (Distributor 602, Partner 605, Client 608).
- Langkah TC "Login sbg Role: Total Control dan buka tab Trial Settings" dipenuhi sesi UI Total Control dari hook `before` dan `beforeEach` suite; spec hanya memuat ulang halaman Lifecycle Settings sebelum membaca tab (S-07).
- Temuan untuk QA:
  - TC 602, 605, dan 608 Expected b "nilai Trial Settings tidak berubah dari nilai non-default" tanpa menyebut nilainya; spec mengasersi nilai non-default dari precondition TC itu sendiri.
  - TC tidak merinci nilai field lain pada payload permintaan langsung; spec memakai nilai tersimpan tab untuk field lain tanpa mengarang struktur payload (S-13).
  - Post Condition seluruh TC ("Tidak ada perubahan data") tanpa langkah observasi tidak diasersi.
- Langkah penghubung (aksi tanpa awalan `Verifikasi`; pemulihan state, pembukaan tab, pengaturan data lewat Fixture BE, dan ganti akun): langkah 1.
