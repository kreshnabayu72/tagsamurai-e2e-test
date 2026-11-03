---
id: TC-AC-ACAL-E2E-019-isolasi-realtime-lintas-entitas-tidak-menerima-event
title: "Isolasi Real-time Lintas Entitas: Tidak Menerima Event Entitas Lain"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AC-ACAL-154
  - TC-AC-ACAL-160
coverage:
  web: automated
---

# Isolasi Real-time Lintas Entitas: Tidak Menerima Event Entitas Lain

## Prerequisites

- Mode: FE+BE.
- Suite serial (`parallel: false`); hook suite dinyatakan di suite.md.
- Guided Tooltip: hook before/after spec ini menyetel dan memulihkan flag seen halaman Activity Log untuk akun Total Control Distributor Alfa (kemampuan disediakan tim FE/BE; lihat suite.md).
- Akun aktor (password tidak ditulis di spec atau fixture; di antara nama env AC_* hanya `AC_TC_PASSWORD` yang sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example`, nama lain adalah usulan tim FE (lihat Temuan untuk QA)): Total Control (Distributor Alfa), `totalControlAdminConsoleDistributorAlfa_automated_{namaCompany}@qwertysystem.net` (Pre-setup No 7), `Spectra.env.AC_ALFA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Admin Console > Activity Log (tab Session) dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control Principal). Spec tidak berganti akun.
- Pelaku kedua (admin Gamma, admin Principal, dan staf yang membuka Admin Console) hanya memicu perubahan state dan tidak diasersi, sehingga dijalankan lewat sesi API (bagian 3 prinsip 13, `[KEPUTUSAN 2026-10-30]`); tidak ada sesi UI kedua dan tidak memakai `P-2`. Langkah pemicu diberi awalan "Pemicu API".
- Jendela pengamatan absence: "Tunggu 5 detik tanpa memuat ulang halaman" adalah pilihan spec (bagian 6 konvensi, jendela amat SSE); TC tidak menyatakan durasinya.
- Data Dinamis (suffix per run dan nomor spec, bagian 5 konvensi), dibuat lewat sesi API di hook `before`; password staf dan admin `Spectra.env.AC_DYN_PASSWORD`:
  - Admin `Admin Gamma {runId}-019` (Distributor Gamma) dan Client `Omega Uji {runId}-019` milik Distributor Gamma (setara Client Omega Pre-setup No 8; dibuat sendiri agar data Pre-setup tidak diubah).
  - Client `Klien Alfa {runId}-019` milik Distributor Alfa, dipakai Principal sebagai pemicu anchor positif pada langkah 3.
  - Staf `Staf Gamma {runId}-019` (Distributor Gamma), `Staf Principal {runId}-019` (Principal), dan `Staf Beta {runId}-019` (Partner Beta, jaringan Alfa).
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus lewat API kedua client, admin, dan semua staf dinamis bila masih ada. Entri log tidak dapat dihapus; nama bersuffix run.
- Kemampuan teknis (disediakan tim FE/BE): sesi API aktor admin dan staf dinamis (mengubah PIC Name Client, membuka Admin Console); inspeksi koneksi stream browser Alfa (event SSE yang diterima, TC menyebut "network inspector aktif"); baseline jumlah total dari footer tabel sebelum aksi pemicu (S-12).
- Tidak ada state global yang diubah.

## Test Steps

### TC-AC-ACAL-154: Event real-time entitas lain tidak pernah diterima (Tab User Action)

1. Klik tab "User Action", lalu catat jumlah total entri dari footer `Showing X–Y of Z entries` (nilai Z) sebagai baseline U0
2. Pemicu API: `Admin Gamma {runId}-019` mengubah PIC Name Client `Omega Uji {runId}-019` hingga tersimpan
3. Pemicu API: Principal mengubah PIC Name Client `Klien Alfa {runId}-019` hingga tersimpan
4. Tunggu 5 detik tanpa memuat ulang halaman
5. Verifikasi baris `Edit` `Client` `Klien Alfa {runId}-019` Field `PIC Name` muncul di tabel tanpa memuat ulang halaman
6. Verifikasi tidak ada event untuk aksi Admin Gamma pada koneksi stream Distributor Alfa
7. Verifikasi tabel tidak berubah oleh aksi Gamma: jumlah total pada footer sama dengan baseline U0 ditambah satu

### TC-AC-ACAL-160: Event real-time Tab Session entitas lain tidak pernah diterima

8. Klik tab "Session", lalu catat jumlah total entri dari footer `Showing X–Y of Z entries` (nilai Z) sebagai baseline S0
9. Pemicu API: `Staf Gamma {runId}-019` membuka Admin Console hingga baris `Session started` tersimpan
10. Pemicu API: `Staf Principal {runId}-019` membuka Admin Console hingga baris `Session started` tersimpan
11. Pemicu API: `Staf Beta {runId}-019` membuka Admin Console hingga baris `Session started` tersimpan
12. Tunggu 5 detik tanpa memuat ulang halaman
13. Verifikasi baris `Session started` milik `Staf Beta {runId}-019` muncul di tabel tanpa memuat ulang halaman
14. Verifikasi tidak ada sinyal untuk sesi `Staf Gamma {runId}-019` pada koneksi stream Distributor Alfa
15. Verifikasi tidak ada sinyal untuk sesi `Staf Principal {runId}-019` pada koneksi stream Distributor Alfa
16. Verifikasi tabel tidak memuat sesi staf Gamma maupun staf Principal: jumlah total pada footer sama dengan baseline S0 ditambah satu

## Notes

- Sumber TC: `admin-console/activity-log/TestCases/tc-activity-log.md` (TC-AC-ACAL-154, 160).
- Kelas: scope exclusion dengan anchor positif dan data milik spec, bukan kelas g (bagian 3 prinsip 13g, `[KEPUTUSAN 2026-10-21]`); tidak ada TC kelas harness lain di spec ini.
- Langkah penghubung (tanpa awalan `Verifikasi`): membuka tab dan mencatat baseline (langkah 1 dan 8), pemicu lewat sesi API (langkah 2, 3, 9, 10, 11), dan "Tunggu 5 detik tanpa memuat ulang halaman" (langkah 4 dan 12, bagian 6 konvensi).
- Asersi tambahan di luar Expected TC (S-03): langkah 3 (pemicu Principal atas Client milik Alfa) dan langkah 5 menjadi anchor positif bahwa stream Alfa menerima event dalam scopenya sebelum asersi absence pada langkah 6 dan 7 (bagian 8b butir 2). Pada TC-AC-ACAL-160 anchor-nya adalah sesi staf Partner Beta yang memang muncul (Expected c TC) pada langkah 13, sebelum langkah 14 sampai 16.
- Urutan asersi TC-AC-ACAL-160 berbeda dari urutan Expected TC (a, b, c, d menjadi c lalu a, b, d): anchor positif ditaruh lebih dulu (bagian 8b butir 2 dan 5).
- Pemicu Admin Gamma dan Client Omega memakai data milik spec (`Omega Uji {runId}-019`, `Klien Alfa {runId}-019`) pengganti Client Omega Pre-setup (S-06); aksi "mengedit Client Omega" pada TC dilakukan sebagai ubah PIC Name.
- Temuan untuk QA:
  - TC-AC-ACAL-154 dan 160 mensyaratkan "network inspector aktif" tanpa menyebut cara mengamati koneksi stream; spec menulis kemampuan inspeksi stream sebagai "disediakan tim FE/BE".
  - TC-AC-ACAL-154 tidak menyebut field yang diubah pada Client Omega; spec memakai PIC Name (mengikuti TC-AC-ACAL-137).
  - TC-AC-ACAL-154 Expected a menyebut "tabel tidak berubah" tanpa angka; spec memakai selisih jumlah total terhadap baseline setelah anchor positif.
  - Email Pre-setup memakai placeholder `{namaCompany}`; password: `AC_ALFA_TC_PASSWORD`, `AC_DYN_PASSWORD` adalah nama usulan tim FE dan belum terdaftar di `.env.example` maupun `spectra.config.ts`.
