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
- Data seed milik spec (replika bersuffix `{runId}-273`; di-seed lewat Fixture BE di hook `before`, dihapus di hook `after`; kemampuan disediakan tim FE/BE, endpoint tidak dikarang; S-06): Client `PT Sejahtera Abadi {runId}-273` (setara C-01: Active; Partner CV Mitra Sejati; Group Area Jakarta; FAMS Active) dengan satu baris Changelog Client L-01 (Action `Create`, Client Name `PT Sejahtera Abadi {runId}-273`, Field `Company Name`, Old Value `—`, New Value `PT Sejahtera Abadi {runId}-273`, Modified By pelaku seed) dan User Global Settings pelaku seed (setara U-LOG-1: nama depan `Andi`, nama belakang `Wijaya {runId}-273`, sehingga Modified By `Andi W` dan tooltip `Andi Wijaya {runId}-273`; namanya dapat diubah). Pada TC baris L-01 adalah seed bersama; spec ini men-seed baris dan user replika sendiri agar perubahan nama user tidak menyentuh fixture bersama U-LOG-1.
- Kemampuan teknis: ubah nama user "Andi Wijaya {runId}-273" menjadi "Andi Saputra {runId}-273" di Global Settings > User lewat UI Admin Console atau sesi API aktor (disediakan tim FE); pemulihan nama di langkah 11 dan di hook `after`. Changelog adalah audit trail permanen: baris seed L-01 dicari lewat Search "PT Sejahtera Abadi {runId}-273" (S-14).
- State global: nama user replika `Andi Wijaya {runId}-273` diubah lalu dipulihkan; suite berjalan serial (`parallel: false`); flag Guided Tooltip halaman List diatur hook suite.
- Env var `AC_TC_PASSWORD` sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example`.

## Test Steps

1. Klik ikon Changelog di toolbar List
2. Ketik "PT Sejahtera Abadi {runId}-273" di Search modal, tekan Enter, lalu ubah ukuran halaman modal menjadi 100
3. Verifikasi sel Modified By baris L-01 (Action `Create`) bernilai `Andi W`
4. Arahkan kursor ke sel Modified By baris L-01
5. Verifikasi tooltip menampilkan "Andi Wijaya {runId}-273"
6. Tutup modal, lalu ubah nama user "Andi Wijaya {runId}-273" menjadi "Andi Saputra {runId}-273" di Global Settings > User hingga perubahan tersimpan
7. Muat ulang Admin Console > Client (F5), klik ikon Changelog di toolbar List, ketik "PT Sejahtera Abadi {runId}-273" di Search modal, tekan Enter, dan ubah ukuran halaman modal menjadi 100
8. Verifikasi sel Modified By baris L-01 (Action `Create`) tetap `Andi W` (tidak menjadi `Andi S`)
9. Arahkan kursor ke sel Modified By baris L-01
10. Verifikasi tooltip tetap menampilkan "Andi Wijaya {runId}-273" (snapshot nama aktor saat aksi)
11. Tutup modal, lalu kembalikan nama user "Andi Saputra {runId}-273" menjadi "Andi Wijaya {runId}-273" di Global Settings > User hingga perubahan tersimpan

## Notes

- Sumber: `admin-console/client/TestCases/tc-client.md`.
- Langkah penghubung (S-03, R-16): langkah 2 dan 7 (Search "PT Sejahtera Abadi {runId}-273" dan ukuran halaman 100 agar baris seed L-01 berada di halaman teramati pada audit trail permanen, S-14), langkah 6 (mengubah nama user, langkah TC 2), langkah 11 (pemulihan Post Condition TC).
- Target aksi tulis (ubah nama user) memakai user replika bersuffix `{runId}-273` dan Client replika (S-06), bukan U-LOG-1 dan C-01 bersama.
- Kolom Modified By diasersi berformat `[First Name] [Last Initial]` (`Andi W`) dengan tooltip nama lengkap (R-14).
- Temuan untuk QA:
  - TC-AC-ACC-432 langkah 2 tidak menyebut pelaku perubahan nama (akun dan cara) di Global Settings > User; spec memakai UI Admin Console atau sesi API aktor yang disediakan tim FE. Bila perubahan nama memakai UI oleh A-01, langkah itu juga menambah baris log di Global Settings.
  - TC-AC-ACC-432 Post Condition mengembalikan nama user ke "Andi Wijaya"; spec mengubah nama user replika `Andi Wijaya {runId}-273` (bukan U-LOG-1 bersama), sehingga kegagalan pemulihan di tengah spec tidak merusak spec lain yang membaca Modified By "Andi W"; spec tetap memulihkan di hook `after` dan menghapus user replika.
  - Seed baris Changelog L-01 dengan pelaku user replika bergantung pada Fixture BE (disediakan tim FE/BE); kemampuan itu belum tertulis di `suite.md`. Pemisahan nama depan dan belakang user replika mengikuti format Modified By `[First Name] [Last Initial]` (R-14).
