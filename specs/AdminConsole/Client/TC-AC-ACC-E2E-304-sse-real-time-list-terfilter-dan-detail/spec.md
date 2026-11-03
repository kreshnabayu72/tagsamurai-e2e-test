---
id: TC-AC-ACC-E2E-304-sse-real-time-list-terfilter-dan-detail
title: "SSE Real-time: Mutasi Subscription Memperbarui List Terfilter In-place dan Suspend Memperbarui Badge Detail Tanpa Muat Ulang"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AC-ACC-416
  - TC-AC-ACC-445
coverage:
  web: automated
---

# SSE Real-time: Mutasi Subscription Memperbarui List Terfilter In-place dan Suspend Memperbarui Badge Detail Tanpa Muat Ulang

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Principal) `totalControlPrincipal_automated_qaTeam1@qwertysystem.net` (A-01), password dari `Spectra.env.AC_TC_PASSWORD`. Login akun ini dilakukan di hook `before` spec ini; halaman Admin Console > Client dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control, `AC_TC_PASSWORD`). Tidak ada ganti akun di tengah spec.
- Data Pre-setup: Tabel A (C-01 sampai C-14) tersedia sebagai fixture residen yang hanya dibaca; spec ini tidak mengubahnya.
- Suite berjalan serial (`parallel: false`); spec ini tidak bergantung pada hasil spec lain.
- Flag Guided Tooltip halaman List dan Detail diset true oleh hook `before` suite dan dipulihkan hook `after` suite (dinyatakan sekali di `suite.md`).
- Fixture bersuffix milik spec (Fixture BE, disediakan tim FE/BE): Client `PT SSE Filter {runId}-304` (Active, FAMS Active, Group Area Jakarta) untuk TC-AC-ACC-416 dan Client `PT SSE Detail {runId}-304` (Active, FAMS Active, Group Area Jakarta) untuk TC-AC-ACC-445; cleanup di hook `after`. TC tidak menyebut Client target (lihat Temuan untuk QA).
- Kemampuan teknis: pelaku kedua memicu perubahan state lewat sesi API aktor (login API password untuk akun yang sama dengan sesi UI, tidak diusir; dinyatakan di `suite.md`), tanpa UI kedua; perubahan subscription ke Grace dan Suspend client lewat Fixture BE/sesi API tanpa endpoint yang dikarang. Jendela amat SSE 5 detik adalah pilihan spec (bukan nilai TC atau PRD) sampai TC menyatakan durasinya.

## Test Steps

### Mutasi real-time saat List terfilter (TC-AC-ACC-416)

1. Klik Filter, pilih FAMS `Active`, lalu klik [Apply]
2. Ketik Search `PT SSE Filter`, tekan Enter
3. Verifikasi baris `PT SSE Filter {runId}-304` tampil dengan sel FAMS `Active`
4. Dari sesi API aktor: ubah status term FAMS `PT SSE Filter {runId}-304` menjadi Grace hingga perubahan tersimpan
5. Tunggu aksi selesai
6. Tunggu 5 detik tanpa memuat ulang halaman
7. Verifikasi baris `PT SSE Filter {runId}-304` hilang dari tabel in-place tanpa muat ulang halaman
8. Verifikasi tidak ada dialog atau interupsi pada halaman List
9. Klik Filter, klik [Clear Field], klik [Apply], lalu klik `(←)` pada kotak Search

### Suspend dari sesi lain saat Detail terbuka (TC-AC-ACC-445)

10. Ketik Search `PT SSE Detail`, tekan Enter, lalu klik Company Name `PT SSE Detail {runId}-304`
11. Verifikasi badge status entitas header Detail `Active`
12. Dari sesi API aktor: Suspend client `PT SSE Detail {runId}-304` hingga perubahan tersimpan
13. Tunggu aksi selesai
14. Verifikasi badge status entitas header Detail berubah menjadi `Suspended` tanpa muat ulang halaman
15. Klik breadcrumb `Client` untuk kembali ke List, lalu klik sub-tab Suspended
16. Verifikasi baris `PT SSE Detail {runId}-304` tampil di sub-tab Suspended

## Notes

- Pelaku kedua lewat sesi API bukan konteks kedua (bagian 3 prinsip 13, P-2 keputusan 2026-10-30); tidak ada butir P-2. TC-AC-ACC-416 dan TC-AC-ACC-445 berlabel `Manual Only (d) dua sesi paralel` di TC; spec mewujudkan pelaku kedua lewat sesi API karena hanya memicu perubahan state.
- Langkah penghubung (S-03): [Clear Field]/[Apply] dan `(←)` memulihkan state (S-09); navigasi breadcrumb dan sub-tab Suspended pada TC-AC-ACC-445 mewujudkan klausa `sub-tab List ikut berubah`.
- Cabang `baris baru masuk` pada Expected TC-AC-ACC-416 tidak diasersi karena Expected memakai `hilang/baris baru masuk`; spec mengasersi cabang `hilang`.
- Temuan untuk QA
  - TC-AC-ACC-416 dan TC-AC-ACC-445: TC tidak menyebut Client target dan cara `ubah subscription ke Grace`/`Suspend dari sesi lain`; precondition hanya `Data Pre-setup C-01…C-14`. Spec memakai Client bersuffix milik spec.
  - TC-AC-ACC-445: Expected `sub-tab List ikut berubah` ambigu karena List tidak terbuka saat Detail terbuka; spec mengasersi baris di sub-tab Suspended setelah kembali ke List.
