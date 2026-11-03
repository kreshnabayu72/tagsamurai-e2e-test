---
id: TC-AC-LCS-E2E-170-otorisasi-server-read-only-system-limits-dan-tanpa-capability
title: "Otorisasi Server: Read Only Save dan Reset System Limits serta Principal Tanpa Capability Baca dan Save Ditolak"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AC-LCS-598
  - TC-AC-LCS-599
  - TC-AC-LCS-609
coverage:
  web: automated
---

# Otorisasi Server: Read Only Save dan Reset System Limits serta Principal Tanpa Capability Baca dan Save Ditolak

## Prerequisites

- Mode: FE+BE. Kelas harness a (defense-in-depth: permintaan langsung ke server tanpa melalui UI).
- Akun aktor: Read Only `readOnlyAdminConsole_automated_{namaCompany}@qwertysystem.net` (nama tampil `Hadi Pratama`), password dari `Spectra.env.AC_RO_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; permintaan langsung memakai login API password akun yang sama (sesi API aktor, disediakan tim BE/FE); hook `after` mengembalikan sesi ke akun default suite (Total Control). Akun kedua: Principal tanpa capability `noCapabilityAdminConsole_automated_{namaCompany}@qwertysystem.net` (Pre-setup 5), password dari `Spectra.env.AC_NOCAP_PASSWORD`, hanya untuk permintaan langsung (login API password); ganti akun ke Total Control (`Spectra.env.AC_TC_PASSWORD`) di langkah eksplisit sebelum membaca tab Approval Settings.
- Data Pre-setup yang dipakai: ketujuh tab pada nilai default (Pre-setup 7); nilai non-default tab System Limits untuk TC 599 diatur lewat Fixture BE sebagai precondition TC (Data Dinamis 2).
- Kemampuan teknis (disediakan tim FE/BE; tidak ada endpoint yang dikarang): klien HTTP/Fixture BE untuk mengirim permintaan langsung ke server tanpa melalui UI dan membaca status respons; Fixture BE untuk memulihkan ketujuh tab ke nilai default atau mengisi satu tab dengan nilai non-default. Field payload selain yang disebut langkah memakai nilai tersimpan tab itu.
- State global: konfigurasi tab Lifecycle Settings diubah lewat Fixture BE atau permintaan langsung; dipulihkan di hook `beforeEach` dan `after` suite lewat Fixture BE; suite berjalan serial.
- Hook suite (`suite.md`): `beforeEach` memulihkan ketujuh tab Lifecycle Settings ke nilai default, jam server dan jam browser, General Settings (Date Format `dd MMM yy`, Time Format 24 jam, Time Zone UTC), dan intercept, lalu membuka Plans & Licensing > Lifecycle Settings; flag Guided Tooltip halaman ini diset true oleh hook `before` suite; hook `after` suite memulihkan state global. Suite berjalan serial (`parallel: false`).
- Data Pre-setup (akun aktor, nilai default tujuh tab, dataset Changelog, daftar client; tanpa password) dirujuk lewat `Fixture.lifecycleSettings.<kunci>` (`fixtures/lifecycle-settings.json`); nilai uji yang diketik atau dikirim di langkah sama dengan TC (S-02).

## Test Steps

### TC-AC-LCS-598: Save tab System Limits lewat permintaan langsung oleh Read Only ditolak server

1. Kirim permintaan Save tab System Limits langsung ke server dengan Bulk Transaction Row Limit = `1001` memakai sesi Read Only
2. Verifikasi permintaan ditolak server dengan status `403` (tidak berwenang)
3. Muat ulang halaman Lifecycle Settings dan buka tab System Limits
4. Verifikasi Bulk Transaction Row Limit tetap `1000`

### TC-AC-LCS-599: Reset to Default tab System Limits lewat permintaan langsung oleh Read Only ditolak server

5. Atur lewat Fixture BE: ketujuh tab pada nilai default kecuali tab System Limits tersimpan dengan nilai non-default: Bulk Transaction Row Limit: 2000, Selection Limit: 1500, Register Asset Bulk Limit: 2500, Hierarchy Depth Limit: 60, Master Data Count Limit: 20000, Max Visible Columns: 25
6. Kirim permintaan Reset tab System Limits langsung ke server memakai sesi Read Only
7. Verifikasi permintaan ditolak server dengan status `403` (tidak berwenang)
8. Muat ulang halaman dan buka tab System Limits
9. Verifikasi nilai tab tidak kembali ke default (tetap Bulk Transaction Row Limit: 2000, Selection Limit: 1500, Register Asset Bulk Limit: 2500, Hierarchy Depth Limit: 60, Master Data Count Limit: 20000, Max Visible Columns: 25)

### TC-AC-LCS-609: Baca dan Save lewat permintaan langsung oleh Principal tanpa capability Manage plans & licensing ditolak

10. Pulihkan ketujuh tab ke nilai default lewat Fixture BE
11. Kirim permintaan baca konfigurasi Approval Settings langsung ke server memakai sesi Principal tanpa capability (login API password akun tersebut)
12. Verifikasi permintaan baca ditolak server dengan status `403`
13. Verifikasi respons permintaan baca tidak memuat nilai konfigurasi
14. Kirim permintaan Save tab Approval Settings dengan Approval Timeout = `7` memakai sesi Principal tanpa capability
15. Verifikasi permintaan Save ditolak server dengan status `403`
16. Ganti akun ke Total Control (`totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`) lalu buka Plans & Licensing > Lifecycle Settings, lalu tab Approval Settings
17. Verifikasi Approval Timeout tetap `3`

## Notes

- Mode: FE+BE. Sumber: `admin-console/plans-licensing-lifecycle-settings/TestCases/tc-plans-licensing-lifecycle-settings.md`. Kelas harness a.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- `K-1`: TC defense-in-depth (kelas a) dengan Expected respons API tetap masuk spec FE+BE walau isinya tumpang tindih dengan `tc-plans-licensing-lifecycle-settings-backend.md`; TC granular tetap sumber dan tiap TC tepat satu spec.
- Urutan TC mengikuti urutan nomor kolom `sourceTc` (598, 599, lalu 609); ganti akun ke Total Control terjadi satu kali pada TC 609.
- Expected c "Tidak ada entri Changelog baru" TC-AC-LCS-598 diasersi di spec absence `TC-AC-LCS-E2E-137` (kelas g) dengan permintaan tersebut sebagai pemicu, user dan baseline sendiri (S-05, `P-5` butir a); id TC tetap di `sourceTc` spec ini dan spec ini hanya mengasersi status respons dan state data (bagian 8b butir 1).
- Pemisahan dari 168 dan 169: satu spec untuk tab System Limits dan kasus tanpa capability agar alur tiap kelompok berdiri sendiri.
- Temuan untuk QA:
  - TC 609 langkah 3 "Login sbg Role: Total Control dan buka tab Approval Settings" dipenuhi ganti akun eksplisit; TC 598 dan 599 memakai sesi UI Read Only dari hook `before`.
  - TC tidak merinci nilai field lain pada payload permintaan langsung; spec memakai nilai tersimpan tab untuk field lain tanpa mengarang struktur payload (S-13).
  - Post Condition seluruh TC ("Tidak ada perubahan data") tanpa langkah observasi tidak diasersi.
- Langkah penghubung (aksi tanpa awalan `Verifikasi`; pemulihan state, pembukaan tab, pengaturan data lewat Fixture BE, dan ganti akun): langkah 5, 10, 16.
