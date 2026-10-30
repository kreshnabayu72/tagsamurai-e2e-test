---
id: TC-GS-ACTLOG-E2E-057-defense-in-depth-request-langsung-ke-endpoint-log
title: "Defense-in-Depth: Request Langsung ke Endpoint Log"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-GS-ACTLOG-215
  - TC-GS-ACTLOG-216
  - TC-GS-ACTLOG-217
coverage:
  web: automated
---

# Defense-in-Depth: Request Langsung ke Endpoint Log

## Prerequisites

- Mode: FE+BE.
- Kemampuan teknis: klien HTTP yang mengirim request langsung ke server tanpa melewati browser dan membawa sesi akun aktor yang sedang dipakai; endpoint yang dipakai adalah enam path baca Activity Log di `global-settings/activity-log/API/openapi.yaml` (daftar, opsi filter, dan export untuk tiap tab Session dan User Action). Spec ini hanya mengasersi respons server (status dan isi respons); perilaku FE untuk respons yang sama tidak diasersi di sini.
- Akun (sesi klien HTTP; autentikasi akun pertama di hook `before`, akun lain lewat langkah ganti akun eksplisit):
  - Total Control Client A (Sari Dewi) `totalControl_automated_qaTeam1@qwertysystem.net` (kredensial `Spectra.env.GS_TC_PASSWORD`): aktor TC-GS-ACTLOG-217 dan akun yang dipulihkan di hook `after`.
  - Create-Only `createOnly_automated_qaTeam1@qwertysystem.net` (kredensial `Spectra.env.GS_CREATE_PASSWORD`): aktor TC-GS-ACTLOG-215.
  - Pemegang akses baca Admin Console tanpa access level Global Settings: `Fixture.activityLog.adminConsoleSeeAll`, disediakan tim FE (fixture baru; email tidak ditulis di spec), kredensial `Spectra.env.GS_ACSEEALL_PASSWORD` (nama env diusulkan; tim FE mendaftarkannya di `executionConfig.environmentVariables` dan `.env.example`): aktor TC-GS-ACTLOG-216.
- Guided Tooltip: hook suite `before`/`after` menyetel flag seen (lihat suite.md).
- Guided Tooltip: hook before/after spec ini menyetel dan memulihkan flag seen untuk akun Create-Only dan pemegang akses baca Admin Console, halaman Activity Log (kemampuan disediakan tim FE/BE).
- Data Pre-setup: tidak ada data tetap yang diubah.
- Data Dinamis: subjek `John Doe {runId}-057` (email `johndoe+{runId}-057@qwertysystem.net`) di-seed lewat API di hook `before` dan login lewat alur Auth dengan password uji `Spectra.env.ACTLOG_PASSWORD` (fixture baru; tim FE mendaftarkannya di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture) sehingga baris event platform Login tercatat di Client A; entri Session sesi Fixed Asset (`Session started`) milik subjek di-seed BE pada entitas yang sama (kemampuan disediakan tim FE/BE tanpa mengarang endpoint). Subjek dihapus di hook `after`; entri log bersifat tetap.
- Suite serial (`parallel: false`) mengikuti `suite.md`. Hook `after` mengembalikan sesi klien ke Total Control Client A.

## Test Steps

### TC-GS-ACTLOG-217: Parameter produk yang disisipkan tidak memperluas cakupan ke log produk lain

1. Kirim request langsung ke endpoint daftar Session dengan sesi Total Control Client A, filter User `John Doe {runId}-057`, dan isi request disisipi parameter produk `fams`; baca seluruh halaman respons
2. Verifikasi respons server berstatus sukses
3. Verifikasi baris event platform Login milik `John Doe {runId}-057` ada dalam baris yang dikembalikan
4. Verifikasi hanya baris event platform dan event sesi Global Settings yang dikembalikan
5. Verifikasi baris sesi Fixed Asset (`Session started`) milik `John Doe {runId}-057` tidak ada dalam baris yang dikembalikan

### TC-GS-ACTLOG-215: Request langsung oleh aktor tanpa access level ditolak

6. Ganti akun: autentikasi klien HTTP sebagai Create-Only `createOnly_automated_qaTeam1@qwertysystem.net`
7. Kirim request langsung ke endpoint daftar Session, daftar User Action, opsi filter Session, opsi filter User Action, export Session, dan export User Action
8. Verifikasi setiap respons berstatus `403 Forbidden`
9. Verifikasi tidak ada data log, opsi filter, maupun berkas export yang dikembalikan pada respons tersebut

### TC-GS-ACTLOG-216: Request langsung oleh pemegang akses baca Admin Console ditolak

10. Ganti akun: autentikasi klien HTTP sebagai pemegang akses baca Admin Console (`Fixture.activityLog.adminConsoleSeeAll`)
11. Kirim request langsung ke endpoint daftar Session dan daftar User Action
12. Verifikasi setiap respons berstatus `403 Forbidden`
13. Verifikasi tidak ada data log yang dikembalikan pada respons tersebut

## Notes

- Sumber: `global-settings/activity-log/TestCases/tc-activity-log.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC-GS-ACTLOG-217, 215, lalu 216 (bukan urutan angka TC) supaya akun Total Control yang sudah login di hook `before` dipakai lebih dulu dan hanya ada dua langkah ganti akun.
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): langkah 6 dan 10 (ganti akun eksplisit, S-07). Hook `after` mengembalikan sesi klien ke Total Control Client A.
- Langkah 1 membatasi request dengan filter User subjek dan membaca seluruh halaman respons supaya absence pada langkah 5 bukan akibat baris terpotong paging.
- Langkah 3 pada TC-GS-ACTLOG-217 adalah anchor positif (8b butir 2) untuk asersi absence pada langkah 5: baris milik subjek yang sama dari event platform harus ada di respons yang sama.
- Pembagian TC lintas spec: TC-GS-ACTLOG-218, 219, dan 220 ada di spec 058.
- Temuan untuk QA:
  - TC-GS-ACTLOG-215 menyebut aktor Create-Only Brand (capability individual tanpa access level), sedangkan akun `createOnly_automated_qaTeam1` di `.env.example` adalah System Role Create dan Read; mohon konfirmasi akun yang dimaksud atau fixture baru.
  - Akun pemegang akses baca Admin Console (`adminConsoleSeeAll`) belum ada di `.env.example`; email dan fixture disediakan tim FE (fixture baru), diusulkan env `GS_ACSEEALL_PASSWORD`.
  - TC-GS-ACTLOG-217 tidak menyebut cara membuat entri Session sesi Fixed Asset milik `John Doe`; spec menuliskannya sebagai seed BE yang disediakan tim FE/BE.
  - TC-GS-ACTLOG-217 tidak menyebut baris event platform tertentu sebagai pembanding; spec memakai baris Login subjek (event platform) sebagai anchor.
  - Expected TC-GS-ACTLOG-215 "tidak ada ... berkas export yang dikembalikan" diasersi dari isi respons 403 saja.
