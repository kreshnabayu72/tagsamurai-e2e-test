---
id: TC-GS-PROFILE-E2E-048-banner-pending-email-change-tautan-kedaluwarsa
title: "Pending Email Change: Tautan Konfirmasi Kurang dari 24 Jam, Lebih dari 24 Jam, dan Halaman 404 Confirmation Link Expired"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-GS-PROFILE-212
  - TC-GS-PROFILE-213
  - TC-GS-PROFILE-214
  - TC-GS-PROFILE-215
coverage:
  web: automated
---

# Pending Email Change: Tautan Konfirmasi Kurang dari 24 Jam, Lebih dari 24 Jam, dan Halaman 404 Confirmation Link Expired

## Prerequisites

- Mode: FE+BE.
- Login akun aktor default suite (Pre-setup #1) dilakukan di hook `before`; spec ini login akun pertamanya di hook `before` spec dan hook `after` mengembalikan sesi ke akun default. Lihat `suite.md`, Hook suite 1.
- Halaman My Profile dibuka hook `beforeEach` suite. Lihat `suite.md`, Hook suite 2.
- Flag Guided Tooltip `guided_tooltip_seen_gs-my-profile` disetel true di hook `before` suite dan dipulihkan di `after`; mekanisme disediakan tim FE/BE. Lihat `suite.md`, Hook suite 3.
- Hook `beforeEach` suite mengonfirmasi `beforeunload` dan menutup dialog `Unsaved Changes` sebagai jaring pengaman (S-09), bukan pengganti langkah pemulihan form. Lihat `suite.md`, Hook suite 5.
- Hook `after` suite memulihkan jam server dan jam browser, password #7/#18/#24 ke `Passw0rd!Old`, counter ke 0, foto #9/#10, kuota dan ledger Storage #11-#13, serta status Client #24/#25 ke Active; fixture pemulihan disediakan tim FE/BE. Suite serial (`parallel: false`). Lihat `suite.md`, Hook suite 7.
- Akun aktor pertama spec: Pre-setup #8 (Citra Lestari, Activated, Email `citralestari@qwertysystem.net`) `pendingEmailProfile_automated_{namaCompany}@qwertysystem.net`, login di hook `before` spec ini dengan `Spectra.env.GS_PROFILE_PENDING_PASSWORD`.
- Env var: `GS_PROFILE_PENDING_PASSWORD`.
- Data Dinamis #2: permintaan Email change live ke `citra.baru@qwertysystem.net`, dibuat lewat fixture BE di hook `before` (disediakan tim FE/BE). Waktu terbit permintaan (T0) dibaca lewat fixture BE, bukan diperkirakan dari waktu hook (bagian 8b butir 3).
- Tautan konfirmasi: URL tautan dibaca lewat fixture BE atau dari email yang masuk di mail-catcher alamat `citra.baru@qwertysystem.net` (kemampuan baca disediakan tim FE/BE; sumber tautan tidak disebut TC, lihat Temuan untuk QA).
- Manipulasi jam: hanya jam server yang diatur, absolut ke T0 + durasi, karena TTL 24 jam dihitung murni di server dan tidak diamati lewat countdown UI (bagian 6). Nilai yang dipakai: T0 + 23 jam 59 menit (TC-GS-PROFILE-212) dan T0 + 24 jam 1 menit (TC-GS-PROFILE-213 sampai 215). Margin terhadap batas 24 jam adalah 1 menit di kedua sisi (kurang dari 5 menit), dihitung sebagai T0 + 24 jam dikurangi atau ditambah 60 detik dari T0 yang dibaca fixture. Sesi login Citra Lestari harus tetap valid saat jam server digeser; kemampuan itu disediakan tim FE/BE (lihat Temuan untuk QA).
- Pemulihan (R-08): langkah 21 dan hook `after` memulihkan jam server ke waktu nyata; hook `after` juga membatalkan permintaan Email change yang dibuat spec dan memastikan Email Citra Lestari tetap `citralestari@qwertysystem.net`.
- State global yang diubah: jam server. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-GS-PROFILE-212: Tautan belum 24 jam, banner tampil

1. Atur jam server absolut ke T0 + 23 jam 59 menit
2. Muat ulang halaman (F5)
3. Verifikasi banner Pending Email Change tampil

### TC-GS-PROFILE-213: Tautan lebih dari 24 jam, banner tetap tampil tanpa error

4. Atur jam server absolut ke T0 + 24 jam 1 menit
5. Muat ulang halaman (F5)
6. Verifikasi banner Pending Email Change tetap tampil
7. Verifikasi tidak ada error pada halaman
8. Verifikasi banner tidak menyediakan aksi dari halaman ini

### TC-GS-PROFILE-214: Halaman 404 Confirmation Link Expired dengan sesi aktif

9. Buka tautan konfirmasi yang kedaluwarsa
10. Verifikasi halaman 404 `Confirmation Link Expired` tampil
11. Verifikasi CTA `Go to Profile` tampil di halaman 404
12. Klik `Go to Profile`
13. Verifikasi My Profile terbuka

### TC-GS-PROFILE-215: Halaman 404 Confirmation Link Expired tanpa sesi

14. Logout
15. Buka tautan konfirmasi yang kedaluwarsa
16. Klik `Go to Profile`
17. Verifikasi halaman Login tampil
18. Login sebagai Citra Lestari (Pre-setup #8)
19. Verifikasi My Profile terbuka
20. Verifikasi banner Pending Email Change tampil
21. Pulihkan jam server ke waktu nyata

## Notes

- Mode: FE+BE. Sumber: `global-settings/my-profile/TestCases/tc-my-profile.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Kelas harness d (TTL 24 jam sebagai batas yang diuji). TC-GS-PROFILE-215 berada paling akhir karena logout; langkah 14 membuka konteks tanpa sesi (R-05).
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): langkah 1 dan 4 (mengatur jam server menggantikan "dibuat 23 jam 59 menit lalu" dan "24 jam 1 menit lalu" pada precondition TC), 2 dan 5 (muat ulang agar banner dibaca pada jam server baru), 21 (pemulihan jam).
- Temuan untuk QA:
  - TC-GS-PROFILE-212 sampai 215 menulis umur permintaan sebagai precondition ("dibuat 23 jam 59 menit lalu") tanpa cara menyiapkannya; spec memakai jam server absolut dari T0 (bagian 8b butir 3).
  - TC-GS-PROFILE-214 dan 215 menyebut "tautan konfirmasi yang kedaluwarsa" tanpa sumber tautan (email baru atau fixture BE); spec menulisnya sebagai kemampuan baca yang disediakan tim FE/BE.
  - TC tidak menyebut efek jam server yang digeser lebih dari 24 jam terhadap sesi login Citra; spec menuliskan kebutuhan sesi tetap valid di Prerequisites.
  - TC-GS-PROFILE-212 dan 213 mengharapkan banner pada halaman yang sudah terbuka; spec memuat ulang halaman setelah jam diatur (langkah 2 dan 5) agar kondisi TTL terbaca.
