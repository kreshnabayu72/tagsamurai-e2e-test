---
id: TC-AC-ACAL-E2E-048-breadcrumb-route-per-tab-dan-tab-session-saat-masuk-dari-sidebar
title: "Breadcrumb Per Tab, Route Per Tab, dan Tab Session Saat Masuk dari Sidebar"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACAL-03
coverage:
  web: automated
---

# Breadcrumb Per Tab, Route Per Tab, dan Tab Session Saat Masuk dari Sidebar

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Principal) `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net` (Pre-setup No 1; kredensial `Spectra.env.AC_TC_PASSWORD`). Login di hook `before` spec ini; halaman Admin Console > Activity Log (tab Session) dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite. Password tidak ditulis di spec atau fixture; nama env `AC_TC_PASSWORD` mengikuti bagian 5 konvensi dan sudah terdaftar di `.env.example` dan `spectra.config.ts`. Email akun memuat placeholder `{namaCompany}` seperti di Pre-setup TC (lihat Temuan untuk QA).
- Kemampuan teknis (disediakan tim FE): membaca URL (route) halaman aktif; tombol Back browser; mengetik URL di address bar, termasuk path Activity Log tanpa segmen tab (nilai path ditetapkan tim FE sesuai route aplikasi).
- Guided Tooltip: hook suite `before`/`after` menyetel flag seen (lihat suite.md).
- State global: tidak ada yang diubah (spec read-only, tanpa aksi tulis).
- Suite serial: `parallel: false` (lihat suite.md).

## Test Steps

### TC-AC-ACAL-03: Breadcrumb per tab, route per tab, dan tab Session saat masuk dari sidebar

1. Catat URL (route) tab Session sebagai pembanding
2. Klik tab "User Action"
3. Verifikasi Breadcrumb `Activity Log > User Action`
4. Verifikasi URL (route) tab User Action berbeda dari URL tab Session pada langkah 1
5. Klik segmen terakhir Breadcrumb
6. Verifikasi klik segmen terakhir Breadcrumb tidak memindahkan halaman
7. Klik tab "Session"
8. Verifikasi Breadcrumb `Activity Log > Session`
9. Verifikasi URL (route) tab Session berbeda dari URL tab User Action
10. Klik tab "User Action"
11. Klik menu Activity Log di sidebar Admin Console
12. Verifikasi tab `Session` aktif
13. Verifikasi Breadcrumb `Activity Log > Session`
14. Klik tab "User Action"
15. Ketik URL Activity Log tanpa segmen tab di address bar, tekan Enter
16. Verifikasi dialihkan ke tab default `Session`
17. Verifikasi Breadcrumb `Activity Log > Session`
18. Klik tab "User Action"
19. Klik tombol Back browser
20. Verifikasi tab `Session` aktif
21. Verifikasi Breadcrumb `Activity Log > Session`

## Notes

- Sumber: `admin-console/activity-log/TestCases/tc-activity-log.md` (TC-AC-ACAL-03). Tidak ada TC hanya-BE di spec ini.
- Subjudul `###` memetakan langkah ke id TC untuk report per langkah.
- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan dari langkah TC): langkah 1 (mencatat URL tab Session pada keadaan awal yang dibuka hook `beforeEach` suite, sebagai pembanding butir Expected TC-03 a dan c), 10 dan 14 (kembali ke tab User Action karena langkah TC-03 nomor 4 dan 5 dimulai dari tab User Action, sedangkan langkah nomor 3 meninggalkan tab itu; langkah 14 juga membuat pengalihan ke tab default dapat diamati).
- Temuan untuk QA:
  - Email akun Pre-setup memakai placeholder `{namaCompany}` (Pre-setup No 1) dan password memakai `AC_TC_PASSWORD` (akun `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`), terdaftar di `.env.example` dan `spectra.config.ts`.
  - TC-03 langkah 3 meninggalkan tab User Action, tetapi langkah 4 dimulai "Pada tab User Action"; spec menambah langkah penghubung kembali ke tab User Action (langkah 10 dan 14).
  - TC-03 langkah 5 tidak menyebut path URL tanpa segmen tab; nilai path ditetapkan tim FE sesuai route aplikasi.
  - TC-03 Expected c menyatakan URL kedua tab berbeda tanpa menyebut path; spec mengasersi perbedaan relatif.
