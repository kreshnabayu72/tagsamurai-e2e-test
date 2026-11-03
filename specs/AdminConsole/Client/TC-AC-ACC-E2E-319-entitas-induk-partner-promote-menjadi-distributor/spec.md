---
id: TC-AC-ACC-E2E-319-entitas-induk-partner-promote-menjadi-distributor
title: "Client Derived Saat Entitas Induk Partner Di-Promote Menjadi Distributor: Badge Derived Tetap, Managed By Pindah, dan Jejak Log"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AC-ACC-1003
coverage:
  web: automated
---

# Client Derived Saat Entitas Induk Partner Di-Promote Menjadi Distributor: Badge Derived Tetap, Managed By Pindah, dan Jejak Log

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Principal) `totalControlPrincipal_automated_qaTeam1@qwertysystem.net` (A-01), password dari `Spectra.env.AC_TC_PASSWORD`. Login akun ini dilakukan di hook `before` spec ini; halaman Admin Console > Client dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control, `AC_TC_PASSWORD`). Tidak ada ganti akun di tengah spec.
- Data Pre-setup: Tabel A (C-01 sampai C-14) tersedia sebagai fixture residen yang hanya dibaca; spec ini tidak mengubahnya.
- Suite berjalan serial (`parallel: false`); spec ini tidak bergantung pada hasil spec lain.
- Flag Guided Tooltip halaman List dan Detail diset true oleh hook `before` suite dan dipulihkan hook `after` suite (dinyatakan sekali di `suite.md`).
- Fixture milik spec (Fixture BE, disediakan tim FE/BE; kembaran fixture A3 yang dirujuk TC, dengan Company Name bersuffix `{runId}-NNN` dan atribut persis seperti baris fixture di tc-client.md); cleanup di hook `after`; Post Condition `Seed ulang` pada TC dipenuhi dengan seeding ulang di hook `before`. Nama fixture yang dirujuk TC dipetakan di tabel di bawah.
  - TC-AC-ACC-1003: P-FX15-4 dan C-FX15-4 -> `CV Mitra Promote Induk {runId}-317` (Partner langsung di bawah Principal dengan Group sendiri Cabang Bekasi; saldo wallet $0 tanpa transaksi pending; Client Derived Active, FAMS Active, Group Cabang Bekasi; Client Code `FX15-004`).
- Kemampuan teknis: kemampuan membaca Activity Log (Admin Console > Activity Log) dan System Log akun aktor (Settings > User > Detail akun aktor > Tab System Log); baseline hitungan baris log dicatat sebelum aksi dengan Search nama bersuffix (S-12). Tidak butuh jam server, intercept, atau klien HTTP.

## Test Steps

### Promote entitas induk menjadi Distributor (TC-AC-ACC-1003)

1. Buka Admin Console > Partner, ketik Search `CV Mitra Promote Induk {runId}-317`, tekan Enter, lalu buka `⋯` baris itu → Promote to Distributor
2. Klik `[Continue]` pada Step Confirm lalu klik `[Confirm Promotion]` pada Review Promotion
3. Verifikasi toast `Success, CV Mitra Promote Induk {runId}-317 has been promoted to distributor.`
4. Verifikasi halaman Detail Distributor hasil Promote tampil
5. Buka Admin Console > Client, klik sub-tab Active, ketik Search `CV Mitra Promote Induk {runId}-317`, tekan Enter
6. Verifikasi baris `CV Mitra Promote Induk {runId}-317` tampil di sub-tab Active dengan badge `Derived`
7. Verifikasi Managed By `CV Mitra Promote Induk {runId}-317 (Direct)` (Distributor hasil Promote)
8. Verifikasi Group `Cabang Bekasi`
9. Verifikasi sel FAMS `Active`
10. Verifikasi Client Code `FX15-004`
11. Klik Company Name `CV Mitra Promote Induk {runId}-317`
12. Verifikasi header menampilkan badge `Derived from CV Mitra Promote Induk {runId}-317`
13. Verifikasi header menampilkan badge status `Active`
14. Kembali ke List lalu buka `⋯` baris `CV Mitra Promote Induk {runId}-317`
15. Verifikasi menu `⋯` memuat `Detail | Edit`
16. Verifikasi `Suspend`, `Change Partner`, dan `Delete` tidak ada
17. Klik `[Changelog]` di toolbar, ketik Search `CV Mitra Promote Induk {runId}-317` di Search modal, tekan Enter
18. Verifikasi Modal Changelog Client menampilkan empty state `No results found` untuk `CV Mitra Promote Induk {runId}-317` (Promote tidak menulis entri di sisi Client)
19. Buka Admin Console > Activity Log lalu cari baris dengan Object `Client` dan Name `CV Mitra Promote Induk {runId}-317`
20. Verifikasi Activity Log tidak memuat baris Object `Client` dengan Name `CV Mitra Promote Induk {runId}-317` (anchor: pencarian menampilkan empty state `No results found`)
21. Buka Settings > User > Detail akun aktor > Tab System Log, klik ikon Search, ketik `CV Mitra Promote Induk {runId}-317`, tekan Enter
22. Verifikasi System Log akun aktor tidak memuat baris Object `Client` dengan Name `CV Mitra Promote Induk {runId}-317` (anchor: pencarian menampilkan empty state `No results found`)

## Notes

- Kelas g (absence log) berada di spec ini dengan P-1 (state berat): asersi `tidak ada baris/entri` bergantung pada aksi Promote yang dibangun di spec ini; anchor memakai empty state hasil Search (bagian 8b butir 2) dan nama bersuffix per run sebagai baseline (S-12). Tidak ada spec absence terpisah yang memuat aksi TC ini.
- Spec melewati sekitar 35 langkah; alasan: satu TC, bagian sesudah Promote tidak bermakna bila bagian sebelumnya gagal keras.
- Langkah penghubung (S-03): `(←)` pada kotak Search, pemilihan sub-tab, dan muat ulang List adalah pemulihan/penghubung tanpa asersi.
- Temuan untuk QA
  - TC-AC-ACC-1003: Group `Cabang Bekasi` pada Detail dan List bergantung pada resolusi Group Distributor hasil Promote; Expected tidak menjelaskan sumber Group.
  - TC-AC-ACC-1003: Expected `System Log akun aktor tidak memuat baris Object Client` tanpa pembanding positif; spec memakai empty state Search sebagai anchor.
