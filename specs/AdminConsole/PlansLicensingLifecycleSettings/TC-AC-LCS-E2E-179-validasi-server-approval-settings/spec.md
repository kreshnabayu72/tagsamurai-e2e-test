---
id: TC-AC-LCS-E2E-179-validasi-server-approval-settings
title: "Validasi Server-Side Approval Settings: Approval Timeout"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AC-LCS-630
  - TC-AC-LCS-631
  - TC-AC-LCS-632
  - TC-AC-LCS-633
coverage:
  web: automated
---

# Validasi Server-Side Approval Settings: Approval Timeout

## Prerequisites

- Mode: FE+BE. Kelas harness a (defense-in-depth: permintaan langsung ke server tanpa melalui UI).
- Akun aktor: Total Control `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net` (nama tampil `Andi Wijaya`), password dari `Spectra.env.AC_TC_PASSWORD` (akun default suite). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control). Permintaan langsung memakai login API password akun yang sama (sesi API aktor, disediakan tim BE/FE).
- Data Pre-setup yang dipakai: ketujuh tab pada nilai default (Pre-setup 7).
- Kemampuan teknis (disediakan tim FE/BE; tidak ada endpoint yang dikarang): klien HTTP/Fixture BE untuk mengirim permintaan langsung ke server tanpa melalui UI dan membaca status respons; Fixture BE untuk memulihkan ketujuh tab ke nilai default atau mengisi satu tab dengan nilai non-default. Field payload selain yang disebut langkah memakai nilai tersimpan tab itu.
- State global: konfigurasi tab Lifecycle Settings diubah lewat Fixture BE atau permintaan langsung; dipulihkan di hook `beforeEach` dan `after` suite lewat Fixture BE; suite berjalan serial.
- Hook suite (`suite.md`): `beforeEach` memulihkan ketujuh tab Lifecycle Settings ke nilai default, jam server dan jam browser, General Settings (Date Format `dd MMM yy`, Time Format 24 jam, Time Zone UTC), dan intercept, lalu membuka Plans & Licensing > Lifecycle Settings; flag Guided Tooltip halaman ini diset true oleh hook `before` suite; hook `after` suite memulihkan state global. Suite berjalan serial (`parallel: false`).
- Data Pre-setup (akun aktor, nilai default tujuh tab, dataset Changelog, daftar client; tanpa password) dirujuk lewat `Fixture.lifecycleSettings.<kunci>` (`fixtures/lifecycle-settings.json`); nilai uji yang diketik atau dikirim di langkah sama dengan TC (S-02).

## Test Steps

### TC-AC-LCS-630: Save lewat permintaan langsung dengan Approval Timeout di atas maksimum ditolak

1. Kirim permintaan Save tab Approval Settings langsung ke server dengan Approval Timeout = `31`
2. Verifikasi permintaan ditolak server dengan status `422` (validasi gagal pada field tersebut)
3. Muat ulang halaman dan buka tab Approval Settings
4. Verifikasi Approval Timeout tetap `3`

### TC-AC-LCS-631: Save lewat permintaan langsung dengan Approval Timeout di bawah minimum ditolak

5. Kirim permintaan Save tab Approval Settings langsung ke server dengan Approval Timeout = `0`
6. Verifikasi permintaan ditolak server dengan status `422` (validasi gagal pada field tersebut)
7. Muat ulang halaman dan buka tab Approval Settings
8. Verifikasi Approval Timeout tetap `3`

### TC-AC-LCS-632: Save lewat permintaan langsung dengan Approval Timeout kosong ditolak

9. Kirim permintaan Save tab Approval Settings langsung ke server dengan Approval Timeout dikosongkan (null)
10. Verifikasi permintaan ditolak server dengan status `400` (field wajib terisi)
11. Muat ulang halaman dan buka tab Approval Settings
12. Verifikasi Approval Timeout tetap `3`

### TC-AC-LCS-633: Save lewat permintaan langsung dengan Approval Timeout bukan bilangan bulat ditolak

13. Kirim permintaan Save tab Approval Settings langsung ke server dengan Approval Timeout = `3.5`
14. Verifikasi permintaan ditolak server dengan status `400` (nilai harus bilangan bulat)
15. Muat ulang halaman dan buka tab Approval Settings
16. Verifikasi Approval Timeout tetap `3`

## Notes

- Mode: FE+BE. Sumber: `admin-console/plans-licensing-lifecycle-settings/TestCases/tc-plans-licensing-lifecycle-settings.md`. Kelas harness a.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- `K-1`: TC defense-in-depth (kelas a) dengan Expected respons API tetap masuk spec FE+BE walau isinya tumpang tindih dengan `tc-plans-licensing-lifecycle-settings-backend.md`; TC granular tetap sumber dan tiap TC tepat satu spec.
- Urutan TC mengikuti urutan nomor kolom `sourceTc`.
- Expected c "Tidak ada entri Changelog baru" TC-AC-LCS-630, TC-AC-LCS-631 diasersi di spec absence `TC-AC-LCS-E2E-139` (kelas g) dengan permintaan tersebut sebagai pemicu, user dan baseline sendiri (S-05, `P-5` butir a); id TC tetap di `sourceTc` spec ini dan spec ini hanya mengasersi status respons dan state data (bagian 8b butir 1).
- Pemisahan dari 173 sampai 176, 178, 180: satu spec per tab (Approval Settings) agar validasi server tiap tab berdiri sendiri.
- Temuan untuk QA:
  - TC tidak merinci nilai field lain pada payload permintaan langsung; spec memakai nilai tersimpan tab untuk field lain tanpa mengarang struktur payload (S-13).
  - Post Condition seluruh TC ("Tidak ada perubahan data") tanpa langkah observasi tidak diasersi.
- Langkah penghubung (aksi tanpa awalan `Verifikasi`; pemulihan state, pembukaan tab, pengaturan data lewat Fixture BE, dan ganti akun): tidak ada selain langkah TC.
