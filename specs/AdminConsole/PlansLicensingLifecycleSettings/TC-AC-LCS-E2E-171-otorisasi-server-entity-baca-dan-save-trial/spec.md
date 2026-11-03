---
id: TC-AC-LCS-E2E-171-otorisasi-server-entity-baca-dan-save-trial
title: "Otorisasi Server: Baca dan Save Trial Settings oleh Distributor, Partner, dan Client Ditolak"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AC-LCS-600
  - TC-AC-LCS-601
  - TC-AC-LCS-603
  - TC-AC-LCS-604
  - TC-AC-LCS-606
  - TC-AC-LCS-607
coverage:
  web: automated
---

# Otorisasi Server: Baca dan Save Trial Settings oleh Distributor, Partner, dan Client Ditolak

## Prerequisites

- Mode: FE+BE. Kelas harness a (defense-in-depth: permintaan langsung ke server tanpa melalui UI).
- Akun aktor: Total Control `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net` (nama tampil `Andi Wijaya`), password dari `Spectra.env.AC_TC_PASSWORD` (akun default suite). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control). Sesi permintaan langsung memakai login API password akun entitas non-Principal (Pre-setup 6): Distributor `distributorUser_automated_{namaCompany}@qwertysystem.net` (`Spectra.env.AC_DIST_PASSWORD`), Partner `partnerUser_automated_{namaCompany}@qwertysystem.net` (`Spectra.env.AC_PARTNER_PASSWORD`), Client `clientUser_automated_{namaCompany}@qwertysystem.net` (`Spectra.env.AC_CLIENT_PASSWORD`); kemampuan sesi API per akun disediakan tim BE/FE.
- Data Pre-setup yang dipakai: ketujuh tab pada nilai default (Pre-setup 7).
- Kemampuan teknis (disediakan tim FE/BE; tidak ada endpoint yang dikarang): klien HTTP/Fixture BE untuk mengirim permintaan langsung ke server tanpa melalui UI dan membaca status respons; Fixture BE untuk memulihkan ketujuh tab ke nilai default atau mengisi satu tab dengan nilai non-default. Field payload selain yang disebut langkah memakai nilai tersimpan tab itu.
- State global: konfigurasi tab Lifecycle Settings diubah lewat Fixture BE atau permintaan langsung; dipulihkan di hook `beforeEach` dan `after` suite lewat Fixture BE; suite berjalan serial.
- Hook suite (`suite.md`): `beforeEach` memulihkan ketujuh tab Lifecycle Settings ke nilai default, jam server dan jam browser, General Settings (Date Format `dd MMM yy`, Time Format 24 jam, Time Zone UTC), dan intercept, lalu membuka Plans & Licensing > Lifecycle Settings; flag Guided Tooltip halaman ini diset true oleh hook `before` suite; hook `after` suite memulihkan state global. Suite berjalan serial (`parallel: false`).
- Data Pre-setup (akun aktor, nilai default tujuh tab, dataset Changelog, daftar client; tanpa password) dirujuk lewat `Fixture.lifecycleSettings.<kunci>` (`fixtures/lifecycle-settings.json`); nilai uji yang diketik atau dikirim di langkah sama dengan TC (S-02).

## Test Steps

### TC-AC-LCS-600: Baca konfigurasi Client Lifecycle lewat permintaan langsung oleh Distributor ditolak

1. Kirim permintaan baca konfigurasi Client Lifecycle langsung ke server memakai sesi Distributor
2. Verifikasi permintaan ditolak server dengan status `403` (tidak berwenang)
3. Verifikasi respons tidak memuat nilai konfigurasi apa pun

### TC-AC-LCS-601: Save Trial Settings lewat permintaan langsung oleh Distributor ditolak

4. Kirim permintaan Save tab Trial Settings langsung ke server dengan Max Trial Duration = `45` memakai sesi Distributor
5. Verifikasi permintaan ditolak server dengan status `403` (tidak berwenang)
6. Buka tab Trial Settings sebagai Total Control (sesi UI hook `before`) setelah memuat ulang halaman Lifecycle Settings
7. Verifikasi Max Trial Duration tetap `30`

### TC-AC-LCS-603: Baca konfigurasi Client Lifecycle lewat permintaan langsung oleh Partner ditolak

8. Kirim permintaan baca konfigurasi Client Lifecycle langsung ke server memakai sesi Partner
9. Verifikasi permintaan ditolak server dengan status `403` (tidak berwenang)
10. Verifikasi respons tidak memuat nilai konfigurasi apa pun

### TC-AC-LCS-604: Save Trial Settings lewat permintaan langsung oleh Partner ditolak

11. Kirim permintaan Save tab Trial Settings langsung ke server dengan Max Trial Duration = `45` memakai sesi Partner
12. Verifikasi permintaan ditolak server dengan status `403` (tidak berwenang)
13. Buka tab Trial Settings sebagai Total Control (sesi UI hook `before`) setelah memuat ulang halaman Lifecycle Settings
14. Verifikasi Max Trial Duration tetap `30`

### TC-AC-LCS-606: Baca konfigurasi Client Lifecycle lewat permintaan langsung oleh Client ditolak

15. Kirim permintaan baca konfigurasi Client Lifecycle langsung ke server memakai sesi Client
16. Verifikasi permintaan ditolak server dengan status `403` (tidak berwenang)
17. Verifikasi respons tidak memuat nilai konfigurasi apa pun

### TC-AC-LCS-607: Save Trial Settings lewat permintaan langsung oleh Client ditolak

18. Kirim permintaan Save tab Trial Settings langsung ke server dengan Max Trial Duration = `45` memakai sesi Client
19. Verifikasi permintaan ditolak server dengan status `403` (tidak berwenang)
20. Buka tab Trial Settings sebagai Total Control (sesi UI hook `before`) setelah memuat ulang halaman Lifecycle Settings
21. Verifikasi Max Trial Duration tetap `30`

## Notes

- Mode: FE+BE. Sumber: `admin-console/plans-licensing-lifecycle-settings/TestCases/tc-plans-licensing-lifecycle-settings.md`. Kelas harness a.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- `K-1`: TC defense-in-depth (kelas a) dengan Expected respons API tetap masuk spec FE+BE walau isinya tumpang tindih dengan `tc-plans-licensing-lifecycle-settings-backend.md`; TC granular tetap sumber dan tiap TC tepat satu spec.
- Urutan TC dikelompokkan per entitas (Distributor 600 dan 601, Partner 603 dan 604, Client 606 dan 607) sesuai urutan nomor TC; TC 602, 605, dan 608 (Reset) ada di spec 172.
- Langkah TC "Login sbg Role: Total Control dan buka tab Trial Settings" dipenuhi sesi UI Total Control dari hook `before` dan `beforeEach` suite; spec hanya memuat ulang halaman Lifecycle Settings sebelum membaca tab (S-07).
- Temuan untuk QA:
  - TC 600 sampai 607 menulis "Login sbg Role: Distributor/Partner/Client" sebagai precondition tetapi aksinya permintaan langsung; spec memakai login API password akun entitas tanpa sesi UI untuk akun tersebut.
  - TC tidak merinci nilai field lain pada payload permintaan langsung; spec memakai nilai tersimpan tab untuk field lain tanpa mengarang struktur payload (S-13).
  - Post Condition seluruh TC ("Tidak ada perubahan data") tanpa langkah observasi tidak diasersi.
- Langkah penghubung (aksi tanpa awalan `Verifikasi`; pemulihan state, pembukaan tab, pengaturan data lewat Fixture BE, dan ganti akun): langkah .
