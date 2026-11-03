---
id: TC-AC-ACC-E2E-273-modified-by-snapshot-nama-aktor-saat-aksi
title: "Modified By Changelog Client Adalah Snapshot Nama Aktor Saat Aksi dan Tidak Berubah Setelah Nama User Diganti"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AC-ACC-432
coverage:
  web: automated
---

# Modified By Changelog Client Adalah Snapshot Nama Aktor Saat Aksi dan Tidak Berubah Setelah Nama User Diganti

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Principal) A-01 `totalControlPrincipal_automated_qaTeam1@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman List Client dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control).
- Data fixture Tabel A3 (hanya dibaca, skrip seed): riwayat Changelog Client baris L-01 (Action `Create`, Client Name `PT Sejahtera Abadi`, Modified By pelaku seed U-LOG-1 "Andi Wijaya"); User Global Settings "Andi Wijaya" (U-LOG-1) tersedia dan namanya dapat diubah.
- Kemampuan teknis: ubah nama user "Andi Wijaya" menjadi "Andi Saputra" di Global Settings > User lewat UI Admin Console atau sesi API aktor (disediakan tim FE); pemulihan nama di langkah 8 dan di hook `after`. Changelog adalah audit trail permanen: baris seed L-01 dicari lewat Search "PT Sejahtera Abadi" (S-14).
- State global: nama user U-LOG-1 diubah lalu dipulihkan; suite berjalan serial (`parallel: false`); flag Guided Tooltip halaman List diatur hook suite.
- Env var `AC_TC_PASSWORD` sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example`.

## Test Steps

1. Klik ikon Changelog di toolbar List
2. Ketik "PT Sejahtera Abadi" di Search modal, tekan Enter, lalu ubah ukuran halaman modal menjadi 100
3. Verifikasi sel Modified By baris L-01 (Action `Create`) bernilai `Andi W`
4. Arahkan kursor ke sel Modified By baris L-01
5. Verifikasi tooltip menampilkan "Andi Wijaya"
6. Tutup modal, lalu ubah nama user "Andi Wijaya" menjadi "Andi Saputra" di Global Settings > User hingga perubahan tersimpan
7. Muat ulang Admin Console > Client (F5), klik ikon Changelog di toolbar List, ketik "PT Sejahtera Abadi" di Search modal, tekan Enter, dan ubah ukuran halaman modal menjadi 100
8. Verifikasi sel Modified By baris L-01 (Action `Create`) tetap `Andi W` (tidak menjadi `Andi S`)
9. Arahkan kursor ke sel Modified By baris L-01
10. Verifikasi tooltip tetap menampilkan "Andi Wijaya" (snapshot nama aktor saat aksi)
11. Tutup modal, lalu kembalikan nama user "Andi Saputra" menjadi "Andi Wijaya" di Global Settings > User hingga perubahan tersimpan

## Notes

- Sumber: `admin-console/client/TestCases/tc-client.md`.
- Langkah penghubung (S-03, R-16): langkah 2 dan 7 (Search "PT Sejahtera Abadi" dan ukuran halaman 100 agar baris seed L-01 berada di halaman teramati pada audit trail permanen, S-14), langkah 6 (mengubah nama user, langkah TC 2), langkah 11 (pemulihan Post Condition TC).
- Kolom Modified By diasersi berformat `[First Name] [Last Initial]` (`Andi W`) dengan tooltip nama lengkap (R-14).
- Temuan untuk QA:
  - TC-AC-ACC-432 langkah 2 tidak menyebut pelaku perubahan nama (akun dan cara) di Global Settings > User; spec memakai UI Admin Console atau sesi API aktor yang disediakan tim FE. Bila perubahan nama memakai UI oleh A-01, langkah itu juga menambah baris log di Global Settings.
  - TC-AC-ACC-432 Post Condition mengembalikan nama user ke "Andi Wijaya"; bila pemulihan gagal di tengah spec, nama "Andi Saputra" bertahan dan merusak spec lain yang membaca Modified By "Andi W"; spec memulihkan juga di hook `after`.
