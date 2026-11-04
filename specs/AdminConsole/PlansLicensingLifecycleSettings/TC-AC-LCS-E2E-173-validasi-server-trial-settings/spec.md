---
id: TC-AC-LCS-E2E-173-validasi-server-trial-settings
title: "Validasi Server-Side Trial Settings: Max Trial Duration dan Relasi Notification"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AC-LCS-610
  - TC-AC-LCS-611
  - TC-AC-LCS-612
  - TC-AC-LCS-613
  - TC-AC-LCS-638
coverage:
  web: automated
---

# Validasi Server-Side Trial Settings: Max Trial Duration dan Relasi Notification

## Prerequisites

- Mode: FE+BE. Kelas harness a (defense-in-depth: permintaan langsung ke server tanpa melalui UI).
- Akun aktor: Total Control `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net` (nama tampil `Andi Wijaya`), password dari `Spectra.env.AC_TC_PASSWORD` (akun default suite). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control). Permintaan langsung memakai login API password akun yang sama (sesi API aktor, disediakan tim BE/FE).
- Data Pre-setup yang dipakai: ketujuh tab pada nilai default (Pre-setup 7).
- Kemampuan teknis (disediakan tim FE/BE; tidak ada endpoint yang dikarang): klien HTTP/Fixture BE untuk mengirim permintaan langsung ke server tanpa melalui UI dan membaca status respons; Fixture BE untuk memulihkan ketujuh tab ke nilai default atau mengisi satu tab dengan nilai non-default. Field payload selain yang disebut langkah memakai nilai tersimpan tab itu.
- State global: konfigurasi tab Lifecycle Settings diubah lewat Fixture BE atau permintaan langsung; dipulihkan di hook `beforeEach` dan `after` suite lewat Fixture BE; suite berjalan serial.
- Hook suite (`suite.md`): `beforeEach` memulihkan ketujuh tab Lifecycle Settings ke nilai default, jam server dan jam browser, General Settings (Date Format `dd MMM yy`, Time Format 24 jam, Time Zone UTC), dan intercept, lalu membuka Plans & Licensing > Lifecycle Settings; flag Guided Tooltip halaman ini diset true oleh hook `before` suite; hook `after` suite memulihkan state global. Suite berjalan serial (`parallel: false`).
- Data Pre-setup (akun aktor, nilai default tujuh tab, dataset Changelog, daftar client; tanpa password) dirujuk lewat `Fixture.lifecycleSettings.<kunci>` (`fixtures/lifecycle-settings.json`); nilai uji yang diketik atau dikirim di langkah sama dengan TC (S-02).

## Test Steps

### TC-AC-LCS-610: Save lewat permintaan langsung dengan Max Trial Duration di atas maksimum ditolak

1. Kirim permintaan Save tab Trial Settings langsung ke server dengan Max Trial Duration = `366`
2. Verifikasi permintaan ditolak server dengan status `422` (validasi gagal pada field tersebut)
3. Muat ulang halaman dan buka tab Trial Settings
4. Verifikasi Max Trial Duration tetap `30`

### TC-AC-LCS-611: Save lewat permintaan langsung dengan Max Trial Duration di bawah minimum ditolak

5. Kirim permintaan Save tab Trial Settings langsung ke server dengan Max Trial Duration = `0`
6. Verifikasi permintaan ditolak server dengan status `422` (validasi gagal pada field tersebut)
7. Muat ulang halaman dan buka tab Trial Settings
8. Verifikasi Max Trial Duration tetap `30`

### TC-AC-LCS-612: Save lewat permintaan langsung dengan Max Trial Duration kosong ditolak

9. Kirim permintaan Save tab Trial Settings langsung ke server dengan Max Trial Duration dikosongkan (null)
10. Verifikasi permintaan ditolak server dengan status `400` (field wajib terisi)
11. Muat ulang halaman dan buka tab Trial Settings
12. Verifikasi Max Trial Duration tetap `30`

### TC-AC-LCS-613: Save lewat permintaan langsung dengan Max Trial Duration bukan bilangan bulat ditolak

13. Kirim permintaan Save tab Trial Settings langsung ke server dengan Max Trial Duration = `30.5`
14. Verifikasi permintaan ditolak server dengan status `400` (nilai harus bilangan bulat)
15. Muat ulang halaman dan buka tab Trial Settings
16. Verifikasi Max Trial Duration tetap `30`

### TC-AC-LCS-638: Save lewat permintaan langsung dengan First Notification tidak lebih besar dari Second Notification ditolak

17. Kirim permintaan Save tab Trial Settings langsung ke server dengan First Notification = `3` dan Second Notification = `3`
18. Verifikasi permintaan ditolak server dengan status `422` (validasi relasi gagal)
19. Muat ulang halaman dan buka tab Trial Settings
20. Verifikasi First Notification tetap `7` dan Second Notification tetap `1`

## Notes

- Mode: FE+BE. Sumber: `admin-console/plans-licensing-lifecycle-settings/TestCases/tc-plans-licensing-lifecycle-settings.md`. Kelas harness a.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- `K-1`: TC defense-in-depth (kelas a) dengan Expected respons API tetap masuk spec FE+BE walau isinya tumpang tindih dengan `tc-plans-licensing-lifecycle-settings-backend.md`; TC granular tetap sumber dan tiap TC tepat satu spec.
- Urutan TC mengikuti urutan nomor kolom `sourceTc`.
- Expected c "Tidak ada entri Changelog baru" TC-AC-LCS-610, TC-AC-LCS-611 diasersi di spec absence `TC-AC-LCS-E2E-138` (kelas g) dengan permintaan tersebut sebagai pemicu, user dan baseline sendiri (S-05, `P-5` butir a); id TC tetap di `sourceTc` spec ini dan spec ini hanya mengasersi status respons dan state data (bagian 8b butir 1).
- Pemisahan dari 174 sampai 176 dan 178 sampai 180: satu spec per tab (Trial Settings) agar validasi server tiap tab berdiri sendiri.
- Temuan untuk QA:
  - TC tidak merinci nilai field lain pada payload permintaan langsung; spec memakai nilai tersimpan tab untuk field lain tanpa mengarang struktur payload (S-13).
  - Post Condition seluruh TC ("Tidak ada perubahan data") tanpa langkah observasi tidak diasersi.
- Langkah penghubung (aksi tanpa awalan `Verifikasi`; pemulihan state, pembukaan tab, pengaturan data lewat Fixture BE, dan ganti akun): tidak ada selain langkah TC.
