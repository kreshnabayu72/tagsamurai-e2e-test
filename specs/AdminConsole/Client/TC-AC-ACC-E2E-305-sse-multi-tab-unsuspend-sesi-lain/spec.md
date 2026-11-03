---
id: TC-AC-ACC-E2E-305-sse-multi-tab-unsuspend-sesi-lain
title: "SSE Real-time Dua Tab: Unsuspend dari Sesi Lain Memperbarui Badge Detail dan Sub-tab List Tanpa Muat Ulang"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACC-676
coverage:
  web: automated
---

# SSE Real-time Dua Tab: Unsuspend dari Sesi Lain Memperbarui Badge Detail dan Sub-tab List Tanpa Muat Ulang

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Active-Full (Manage active client: C/R/U/D, exact-match Area Jakarta dan Cabang Menteng) `activeFullJakarta_automated_qaTeam1@qwertysystem.net` (A-15), password dari `Spectra.env.AC_CLIENT_ACTIVE_FULL_PASSWORD` (nama env baru; didaftarkan di `spectra.config.ts` dan `.env.example` saat tahap script). Login akun ini dilakukan di hook `before` spec ini (Sesi A, dua tab); hook `after` mengembalikan sesi ke akun default suite.
- Data Pre-setup: Tabel A (C-01 sampai C-14) tersedia sebagai fixture residen yang hanya dibaca; spec ini tidak mengubahnya.
- Suite berjalan serial (`parallel: false`); spec ini tidak bergantung pada hasil spec lain.
- Flag Guided Tooltip halaman List dan Detail diset true oleh hook `before` suite dan dipulihkan hook `after` suite (dinyatakan sekali di `suite.md`).
- Fixture milik spec (Fixture BE): Client `PT Ditahan Dua {runId}-305` (kembaran C-LIF-6: Suspended; FAMS Active; Default User Activated; Group Area Jakarta); cleanup di hook `after`; Post Condition TC (Suspend kembali) dipenuhi seeding ulang.
- Kemampuan teknis: konteks kedua kelas c (tab kedua pada Sesi A yang sama); Sesi B (Active-Full) memicu Unsuspend lewat sesi API aktor (login API password untuk akun yang sama, tidak mengusir sesi UI, dinyatakan di `suite.md`). Jendela amat SSE 5 detik adalah pilihan spec (bukan nilai TC atau PRD).

## Test Steps

### Unsuspend dari sesi lain (TC-AC-ACC-676)

1. [Sesi A, Tab 1] Ketik Search `PT Ditahan Dua` di sub-tab Suspended, tekan Enter, lalu klik Company Name `PT Ditahan Dua {runId}-305` untuk membuka Detail
2. Verifikasi badge status entitas header Detail `Suspended`
3. [Sesi A, Tab 2] Buka Admin Console > Client, klik sub-tab Suspended, ketik Search `PT Ditahan Dua`, tekan Enter
4. Verifikasi baris `PT Ditahan Dua {runId}-305` tampil di sub-tab Suspended
5. [Sesi B, sesi API Active-Full] Unsuspend client `PT Ditahan Dua {runId}-305` hingga perubahan tersimpan
6. Tunggu aksi selesai
7. [Sesi A, Tab 1] Lihat Tab 1 tanpa muat ulang
8. Verifikasi badge status entitas pada header Detail berubah dari `Suspended` ke `Active`
9. [Sesi A, Tab 2] Lihat Tab 2 tanpa muat ulang
10. Verifikasi baris `PT Ditahan Dua {runId}-305` hilang dari sub-tab Suspended
11. [Sesi A, Tab 2] Klik sub-tab Active
12. Verifikasi baris `PT Ditahan Dua {runId}-305` tampil di sub-tab Active

## Notes

- Kelas c (multi-tab); spec berdiri sendiri satu TC. Sesi B lewat sesi API bukan konteks kedua UI (P-2 keputusan 2026-10-30).
- Langkah Tab 2 yang membuka sub-tab Suspended dan Search mengasersi baris sebagai anchor positif sebelum pemicu; `Verifikasi` hilang dari sub-tab Suspended memakai badge Detail Tab 1 sebagai anchor bahwa perubahan sudah diproses (bagian 8b butir 2).
- Temuan untuk QA
  - TC-AC-ACC-676: Post Condition `Suspend PT Ditahan Dua` dipenuhi spec lewat fixture bersuffix dan cleanup; tidak ada langkah observasi di TC.
