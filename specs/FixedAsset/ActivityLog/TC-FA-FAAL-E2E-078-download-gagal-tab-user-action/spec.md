---
id: TC-FA-FAAL-E2E-078-download-gagal-tab-user-action
title: "Kegagalan Server: Download Gagal Tab User Action"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-FA-FAAL-172
coverage:
  web: automated
---

# Kegagalan Server: Download Gagal Tab User Action

## Prerequisites

- Mode: FE+BE. Platform: web, Fixed Asset > Reports & Logs > Activity Log. Kegagalan dipicu intercept jaringan parsial di atas backend nyata (bagian 6 konvensi); data log tetap dari backend nyata.
- Akun aktor: Total Control (Pre-setup #1) `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Env var `FA_TC_PASSWORD` didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture.
- Data: Tab User Action UA-01 sampai UA-15 (Pre-setup #12, 15 baris), dipulihkan ke keadaan Pre-setup oleh fixture backend sebelum spec. Spec tidak mengubah data.
- Kemampuan teknis: intercept jaringan yang memaksa respons Download gagal dengan status 500, lalu melepasnya; penangkap unduhan browser untuk mengamati bahwa tidak ada berkas terunduh. Intercept dilepas segera setelah pemicu selesai (S-09).
- Flag Guided Tooltip: mengikuti butir "Flag Guided Tooltip" di `suite.md` (flag akun Total Control bernilai true lewat hook suite).
- Seed dan pemulihan lewat API disediakan tim FE/BE (butir "Seed dan pemulihan lewat API" di `suite.md`).
- Identitas data Pre-setup dibaca dari `fixtures/activity-log.json` (belum ada; disediakan tim FE, nama kunci ditetapkan tim FE).

## Test Steps

### TC-FA-FAAL-172: Download Tab User Action gagal menampilkan toast error

1. Klik tab User Action
2. Paksa respons Download gagal (500) lewat intercept jaringan
3. Klik icon Download
4. Klik `Download as CSV`
5. Verifikasi toast error tampil: "Error, failed to download Activity-Log-User-Action."
6. Verifikasi tidak ada berkas terunduh
7. Verifikasi toast tidak memiliki tombol aksi
8. Verifikasi toast tidak memiliki tombol tutup
9. Lepas intercept respons Download
10. Verifikasi toast error hilang dengan sendiri tanpa klik apa pun

## Notes

- Sumber: `fixed-asset/activity-log/TestCases/tc-activity-log.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Spec ini kelas fault injection (bagian 3 prinsip 13b), TC-FA-FAAL-10, 11, dan 171 ada di spec 004.
- Langkah penghubung (S-03): langkah 1 (pindah tab), langkah 9 (melepas intercept). Langkah 7 dan 8 memverifikasi Expected b dan c TC-FA-FAAL-172 (tanpa tombol aksi dan tanpa tombol tutup); langkah 10 memverifikasi Expected c (toast auto-dismiss); lama tunggu mengikuti auto-wait Spectra, PRD tidak memberi durasi.
- Temuan untuk QA:
  - Perilaku toast T-01: hilang dengan sendiri tanpa tombol aksi atau tutup manual (Expected b dan c TC-FA-FAAL-172); durasi tidak ditentukan PRD sehingga spec tidak menulis angka.
