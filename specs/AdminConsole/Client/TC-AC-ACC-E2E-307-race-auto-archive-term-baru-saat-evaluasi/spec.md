---
id: TC-AC-ACC-E2E-307-race-auto-archive-term-baru-saat-evaluasi
title: "Auto-Archive Dibatalkan Bila Term Baru Dibuat Saat Evaluasi Berjalan: Re-cek di Titik Commit"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AC-ACC-435
coverage:
  web: automated
---

# Auto-Archive Dibatalkan Bila Term Baru Dibuat Saat Evaluasi Berjalan: Re-cek di Titik Commit

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Principal) `totalControlPrincipal_automated_qaTeam1@qwertysystem.net` (A-01), password dari `Spectra.env.AC_TC_PASSWORD`. Login akun ini dilakukan di hook `before` spec ini; halaman Admin Console > Client dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control, `AC_TC_PASSWORD`). Tidak ada ganti akun di tengah spec.
- Data Pre-setup: Tabel A (C-01 sampai C-14) tersedia sebagai fixture residen yang hanya dibaca; spec ini tidak mengubahnya.
- Suite berjalan serial (`parallel: false`); spec ini tidak bergantung pada hasil spec lain.
- Flag Guided Tooltip halaman List dan Detail diset true oleh hook `before` suite dan dipulihkan hook `after` suite (dinyatakan sekali di `suite.md`).
- Fixture bersuffix milik spec (Fixture BE, disediakan tim FE/BE): Client `PT Race Arsip {runId}-307` (Active, Group Area Jakarta, FAMS satu-satunya term; kondisi memenuhi syarat Auto-Archive setelah term itu di-Cancel). TC tidak menyebut Client target (lihat Temuan untuk QA); kembaran fixture C-ISO-9.
- Kemampuan teknis (kelas c dan d, disediakan tim BE): menahan evaluasi Auto-Archive pada titik sebelum commit dan membuat term baru dari sesi API selama evaluasi tertahan; tanpa endpoint yang dikarang. Jam server tidak dimajukan.

## Test Steps

### Re-cek Auto-Archive di titik commit (TC-AC-ACC-435)

1. Ketik Search `PT Race Arsip`, tekan Enter
2. Verifikasi baris `PT Race Arsip {runId}-307` tampil di sub-tab Active
3. Dari sesi API aktor: Cancel term FAMS `PT Race Arsip {runId}-307` sehingga evaluasi Auto-Archive berjalan, dan tahan evaluasi sebelum commit
4. Dari sesi API aktor: buat term baru FAMS `PT Race Arsip {runId}-307` saat evaluasi berjalan hingga term tersimpan, lalu lepas tahanan evaluasi
5. Tunggu aksi selesai
6. Muat ulang Admin Console > Client, klik sub-tab Active, ketik Search `PT Race Arsip`, tekan Enter
7. Verifikasi Client tetap tampil di sub-tab Active
8. Klik sub-tab Archived, ketik Search `PT Race Arsip`, tekan Enter
9. Verifikasi empty state Title `No results found` dengan Description `Try adjusting your search or filter.`

## Notes

- Kelas c/d berat (race dengan job latar); spec berdiri sendiri satu TC.
- Expected TC `Evaluasi re-cek di titik commit; Client tetap Active` diasersi lewat sub-tab Active dan absen di sub-tab Archived; empty state `No results found` adalah anchor positif absence (bagian 8b butir 2).
- Temuan untuk QA
  - TC-AC-ACC-435: Langkah TC `Buat term baru saat evaluasi Auto-Archive berjalan` tidak menyebut Client, cara memicu evaluasi, atau cara menyinkronkan term baru dengan evaluasi (precondition hanya `Data Pre-setup C-01…C-14`, tanpa fixture C-ISO). Mekanisme penahanan evaluasi dan pemicu dibutuhkan dari tim BE.
  - TC-AC-ACC-435: Expected tidak menyebut baris Changelog `Auto-Archive` yang tidak boleh muncul; spec tidak mengasersinya.
