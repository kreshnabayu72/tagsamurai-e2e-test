---
id: TC-AC-LCS-E2E-177-validasi-server-client-lifecycle-relasi
title: "Validasi Server-Side Client Lifecycle: Relasi Reminder, Purge Warning, dan Archive Period"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AC-LCS-639
  - TC-AC-LCS-640
  - TC-AC-LCS-641
  - TC-AC-LCS-642
  - TC-AC-LCS-643
coverage:
  web: automated
---

# Validasi Server-Side Client Lifecycle: Relasi Reminder, Purge Warning, dan Archive Period

## Prerequisites

- Mode: FE+BE. Kelas harness a (defense-in-depth: permintaan langsung ke server tanpa melalui UI).
- Akun aktor: Total Control `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net` (nama tampil `Andi Wijaya`), password dari `Spectra.env.AC_TC_PASSWORD` (akun default suite). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control). Permintaan langsung memakai login API password akun yang sama (sesi API aktor, disediakan tim BE/FE).
- Data Pre-setup yang dipakai: ketujuh tab pada nilai default (Pre-setup 7).
- Kemampuan teknis (disediakan tim FE/BE; tidak ada endpoint yang dikarang): klien HTTP/Fixture BE untuk mengirim permintaan langsung ke server tanpa melalui UI dan membaca status respons; Fixture BE untuk memulihkan ketujuh tab ke nilai default atau mengisi satu tab dengan nilai non-default. Field payload selain yang disebut langkah memakai nilai tersimpan tab itu.
- State global: konfigurasi tab Lifecycle Settings diubah lewat Fixture BE atau permintaan langsung; dipulihkan di hook `beforeEach` dan `after` suite lewat Fixture BE; suite berjalan serial.
- Hook suite (`suite.md`): `beforeEach` memulihkan ketujuh tab Lifecycle Settings ke nilai default, jam server dan jam browser, General Settings (Date Format `dd MMM yy`, Time Format 24 jam, Time Zone UTC), dan intercept, lalu membuka Plans & Licensing > Lifecycle Settings; flag Guided Tooltip halaman ini diset true oleh hook `before` suite; hook `after` suite memulihkan state global. Suite berjalan serial (`parallel: false`).
- Data Pre-setup (akun aktor, nilai default tujuh tab, dataset Changelog, daftar client; tanpa password) dirujuk lewat `Fixture.lifecycleSettings.<kunci>` (`fixtures/lifecycle-settings.json`); nilai uji yang diketik atau dikirim di langkah sama dengan TC (S-02).

## Test Steps

### TC-AC-LCS-639: Save lewat permintaan langsung dengan First Reminder Before Event tidak lebih besar dari Second Reminder Before Event ditolak

1. Kirim permintaan Save tab Client Lifecycle langsung ke server dengan First Reminder = `7` dan Second Reminder = `7`
2. Verifikasi permintaan ditolak server dengan status `422` (validasi relasi gagal)
3. Muat ulang halaman dan buka tab Client Lifecycle
4. Verifikasi First Reminder tetap `30`

### TC-AC-LCS-640: Save lewat permintaan langsung dengan Second Reminder Before Event tidak lebih besar dari Final Reminder Before Event ditolak

5. Kirim permintaan Save tab Client Lifecycle langsung ke server dengan Second Reminder = `1` dan Final Reminder = `1`
6. Verifikasi permintaan ditolak server dengan status `422` (validasi relasi gagal)
7. Muat ulang halaman dan buka tab Client Lifecycle
8. Verifikasi Second Reminder tetap `7`

### TC-AC-LCS-641: Save lewat permintaan langsung dengan Purge Warning Email tidak lebih besar dari Purge Urgent Warning Email ditolak

9. Kirim permintaan Save tab Client Lifecycle langsung ke server dengan Purge Warning = `2` dan Purge Urgent = `2`
10. Verifikasi permintaan ditolak server dengan status `422` (validasi relasi gagal)
11. Muat ulang halaman dan buka tab Client Lifecycle
12. Verifikasi Purge Warning tetap `10`

### TC-AC-LCS-642: Save lewat permintaan langsung dengan Purge Warning Email melebihi Archive Period Duration ditolak

13. Kirim permintaan Save tab Client Lifecycle langsung ke server dengan Purge Warning = `31` dan Archive Period Duration = `30`
14. Verifikasi permintaan ditolak server dengan status `422` (validasi relasi gagal)
15. Muat ulang halaman dan buka tab Client Lifecycle
16. Verifikasi Purge Warning tetap `10`

### TC-AC-LCS-643: Save lewat permintaan langsung dengan Purge Urgent Warning Email melebihi Archive Period Duration ditolak

17. Kirim permintaan Save tab Client Lifecycle langsung ke server dengan Purge Urgent = `31`, Purge Warning = `32`, dan Archive Period Duration = `30`
18. Verifikasi permintaan ditolak server dengan status `422` (validasi relasi gagal)
19. Muat ulang halaman dan buka tab Client Lifecycle
20. Verifikasi Purge Urgent tetap `2`

## Notes

- Mode: FE+BE. Sumber: `admin-console/plans-licensing-lifecycle-settings/TestCases/tc-plans-licensing-lifecycle-settings.md`. Kelas harness a.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- `K-1`: TC defense-in-depth (kelas a) dengan Expected respons API tetap masuk spec FE+BE walau isinya tumpang tindih dengan `tc-plans-licensing-lifecycle-settings-backend.md`; TC granular tetap sumber dan tiap TC tepat satu spec.
- Urutan TC mengikuti urutan nomor kolom `sourceTc`.
- Temuan untuk QA:
  - TC tidak merinci nilai field lain pada payload permintaan langsung; spec memakai nilai tersimpan tab untuk field lain tanpa mengarang struktur payload (S-13).
  - Post Condition seluruh TC ("Tidak ada perubahan data") tanpa langkah observasi tidak diasersi.
- Langkah penghubung (aksi tanpa awalan `Verifikasi`; pemulihan state, pembukaan tab, pengaturan data lewat Fixture BE, dan ganti akun): langkah .
