---
id: TC-AC-ACC-E2E-317-entitas-induk-partner-suspend-unsuspend
title: "Client Derived Saat Entitas Induk Partner Di-Suspend dan Di-Unsuspend: Tetap Active, Badge Derived, dan Aksi Menu"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AC-ACC-1000
coverage:
  web: automated
---

# Client Derived Saat Entitas Induk Partner Di-Suspend dan Di-Unsuspend: Tetap Active, Badge Derived, dan Aksi Menu

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Principal) `totalControlPrincipal_automated_qaTeam1@qwertysystem.net` (A-01), password dari `Spectra.env.AC_TC_PASSWORD`. Login akun ini dilakukan di hook `before` spec ini; halaman Admin Console > Client dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control, `AC_TC_PASSWORD`). Tidak ada ganti akun di tengah spec.
- Data Pre-setup: Tabel A (C-01 sampai C-14) tersedia sebagai fixture residen yang hanya dibaca; spec ini tidak mengubahnya.
- Suite berjalan serial (`parallel: false`); spec ini tidak bergantung pada hasil spec lain.
- Flag Guided Tooltip halaman List dan Detail diset true oleh hook `before` suite dan dipulihkan hook `after` suite (dinyatakan sekali di `suite.md`).
- Fixture milik spec (Fixture BE, disediakan tim FE/BE; kembaran fixture A3 yang dirujuk TC, dengan Company Name bersuffix `{runId}-NNN` dan atribut persis seperti baris fixture di tc-client.md); cleanup di hook `after`; Post Condition `Seed ulang` pada TC dipenuhi dengan seeding ulang di hook `before`. Nama fixture yang dirujuk TC dipetakan di tabel di bawah.
  - TC-AC-ACC-1000: P-FX15-3 dan C-FX15-3 -> Partner dan Client Derived `CV Mitra Suspend Induk {runId}-317` (Partner di bawah Distributor PT Distribusi Nusantara, Group Cabang Menteng; Client Active, FAMS Active, Group Area Jakarta pada view Principal). Post Condition TC (Partner dipulihkan ke Active) dipenuhi langkah Unsuspend di spec dan seeding ulang di hook `after`.
- Kemampuan teknis: kemampuan membaca Activity Log (Admin Console > Activity Log) dan System Log akun aktor (Settings > User > Detail akun aktor > Tab System Log); baseline hitungan baris log dicatat sebelum aksi dengan Search nama bersuffix (S-12). Tidak butuh jam server, intercept, atau klien HTTP.

## Test Steps

### Suspend lalu Unsuspend entitas induk (TC-AC-ACC-1000)

1. Klik `[Changelog]` di toolbar List, ketik Search `CV Mitra Suspend Induk {runId}-317` di Search modal, tekan Enter, catat jumlah baris Action `Suspend` (N1), lalu tutup modal
2. Buka Admin Console > Partner, ketik Search `CV Mitra Suspend Induk {runId}-317`, tekan Enter, buka `⋯` baris itu → Suspend, lalu klik `[Suspend]` pada dialog konfirmasi Suspend Partner
3. Verifikasi toast `Success, partner has been suspended.`
4. Buka Admin Console > Client, klik sub-tab Active, ketik Search `CV Mitra Suspend Induk {runId}-317`, tekan Enter
5. Verifikasi baris `CV Mitra Suspend Induk {runId}-317` tampil di sub-tab Active (bukan Suspended)
6. Verifikasi badge `Derived`
7. Verifikasi sel FAMS `Active`
8. Buka `⋯` baris `CV Mitra Suspend Induk {runId}-317`
9. Verifikasi menu `⋯` memuat `Detail | Edit`
10. Verifikasi `Suspend`, `Unsuspend`, `Change Partner`, dan `Delete` tidak ada
11. Klik Company Name `CV Mitra Suspend Induk {runId}-317`
12. Verifikasi badge status di header Detail `Active`
13. Kembali ke List, klik `[Changelog]` di toolbar, ketik Search `CV Mitra Suspend Induk {runId}-317` di Search modal, tekan Enter
14. Catat jumlah baris Action `Suspend` untuk `CV Mitra Suspend Induk {runId}-317` pada hasil Search (N2)
15. Verifikasi N2 = N1 (Modal Changelog Client tidak memuat baris Action `Suspend` baru untuk `CV Mitra Suspend Induk {runId}-317`)
16. Tutup modal Changelog, buka Admin Console > Partner, ketik Search `CV Mitra Suspend Induk {runId}-317`, tekan Enter, buka `⋯` baris itu → Unsuspend, lalu klik `[Unsuspend]` pada dialog konfirmasi Unsuspend Partner
17. Verifikasi toast `Success, partner has been unsuspended.`
18. Buka Admin Console > Client, klik sub-tab Active, ketik Search `CV Mitra Suspend Induk {runId}-317`, tekan Enter
19. Verifikasi baris `CV Mitra Suspend Induk {runId}-317` tetap di sub-tab Active
20. Verifikasi badge `Derived`
21. Verifikasi sel FAMS `Active`
22. Klik Company Name `CV Mitra Suspend Induk {runId}-317`
23. Verifikasi badge status header `Active`

## Notes

- Absence `tidak ada baris Action Suspend` pada Changelog Client memakai baseline hitungan N1 sebelum aksi (S-12); entri Changelog yang diasersi hanya Action `Suspend`.
- Spec melewati sekitar 35 langkah; alasan: satu TC dengan dua aksi (Suspend lalu Unsuspend) pada fixture yang sama, bagian sesudah Unsuspend tidak bermakna bila bagian sebelumnya gagal keras.
- Langkah penghubung (S-03): `(←)` pada kotak Search, pemilihan sub-tab, dan muat ulang List adalah pemulihan/penghubung tanpa asersi.
- Temuan untuk QA
  - TC-AC-ACC-1000: Expected butir (e) `Modal Changelog Client tidak memuat baris Action Suspend` tanpa pembanding positif; spec memakai baseline hitungan baris Action `Suspend` sebelum aksi.
