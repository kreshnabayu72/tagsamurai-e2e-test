---
id: TC-AC-ACC-E2E-309-auto-archive-via-cancel-term-terakhir
title: "Auto-Archive Client Setelah Seluruh Term Terminal Lewat Cancel Subscription: Client Active, Client Suspended, dan Term Non-terminal"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACC-433
  - TC-AC-ACC-434
  - TC-AC-ACC-436
coverage:
  web: automated
---

# Auto-Archive Client Setelah Seluruh Term Terminal Lewat Cancel Subscription: Client Active, Client Suspended, dan Term Non-terminal

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Principal) `totalControlPrincipal_automated_qaTeam1@qwertysystem.net` (A-01), password dari `Spectra.env.AC_TC_PASSWORD`. Login akun ini dilakukan di hook `before` spec ini; halaman Admin Console > Client dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control, `AC_TC_PASSWORD`). Tidak ada ganti akun di tengah spec.
- Data Pre-setup: Tabel A (C-01 sampai C-14) tersedia sebagai fixture residen yang hanya dibaca; spec ini tidak mengubahnya.
- Suite berjalan serial (`parallel: false`); spec ini tidak bergantung pada hasil spec lain.
- Flag Guided Tooltip halaman List dan Detail diset true oleh hook `before` suite dan dipulihkan hook `after` suite (dinyatakan sekali di `suite.md`).
- Fixture milik spec (Fixture BE, disediakan tim FE/BE; kembaran fixture A3 yang dirujuk TC, dengan Company Name bersuffix `{runId}-NNN` dan atribut persis seperti baris fixture di tc-client.md); cleanup di hook `after`; Post Condition `Seed ulang` pada TC dipenuhi dengan seeding ulang di hook `before`. Nama fixture yang dirujuk TC dipetakan di tabel di bawah.
  - TC-AC-ACC-433: C-ISO-9 `PT Auto Arsip Aksi` -> `PT Auto Arsip Aksi {runId}-309` (Active; FAMS satu-satunya term Active; Partner CV Mitra Sejati; Group Area Jakarta).
  - TC-AC-ACC-434: C-ISO-10 `PT Suspend Auto Arsip` -> `PT Suspend Auto Arsip {runId}-309` (Suspended; FAMS satu-satunya term Active; Partner CV Mitra Sejati; Group Area Jakarta).
  - TC-AC-ACC-436: tidak ada fixture di TC; spec memakai `PT Dua Produk Arsip {runId}-309` (Active; FAMS Active dan SAMS Active; Partner CV Mitra Sejati; Group Area Jakarta) sebagai wujud `satu produk Archive, produk lain Active`.
- Kemampuan teknis: tidak butuh jam server (Cancel Subscription memicu Auto-Archive langsung), intercept, atau klien HTTP. Auto-Archive berjalan tanpa aksi manual.

## Test Steps

### Auto-Archive Client Active (TC-AC-ACC-433)

1. Ketik Search `PT Auto Arsip Aksi {runId}-309`, tekan Enter, lalu buka `⋯` baris itu di sub-tab Active
2. Verifikasi menu `⋯` memuat `Detail | Edit | Change Partner | Suspend`
3. Buka Admin Console > Client Subscription, ketik Search `PT Auto Arsip Aksi {runId}-309`, tekan Enter, buka `⋯` baris term FAMS Active → Cancel Subscription, lalu klik `[Cancel Subscription]` pada dialog
4. Tunggu aksi selesai (Cancel Subscription)
5. Muat ulang Admin Console > Client, klik sub-tab Archived, ketik Search `PT Auto Arsip Aksi {runId}-309`, tekan Enter
6. Verifikasi `PT Auto Arsip Aksi {runId}-309` tampil di sub-tab Archived tanpa aksi manual
7. Buka `⋯` baris `PT Auto Arsip Aksi {runId}-309`
8. Verifikasi menu `⋯` memuat `Detail | Edit | Delete`
9. Verifikasi `Suspend` dan `Change Partner` tidak ada pada menu
10. Klik `[Changelog]` di toolbar List, ketik Search `PT Auto Arsip Aksi {runId}-309` di Search modal, tekan Enter, ubah ukuran halaman modal menjadi 100
11. Verifikasi hasil Search memuat baris Action `Auto-Archive`, Client Name `PT Auto Arsip Aksi {runId}-309`, Field `Status`, Old Value `Active`, New Value `Archived`, Modified By `System`

### Auto-Archive Client Suspended (TC-AC-ACC-434)

12. Klik sub-tab Suspended, ketik Search `PT Suspend Auto Arsip {runId}-309`, tekan Enter
13. Verifikasi sel FAMS `Active`
14. Buka Admin Console > Client Subscription, ketik Search `PT Suspend Auto Arsip {runId}-309`, tekan Enter, buka `⋯` baris term FAMS Active → Cancel Subscription, lalu klik `[Cancel Subscription]` pada dialog
15. Tunggu aksi selesai (Cancel Subscription)
16. Muat ulang Admin Console > Client, klik sub-tab Archived, ketik Search `PT Suspend Auto Arsip {runId}-309`, tekan Enter
17. Verifikasi `PT Suspend Auto Arsip {runId}-309` tampil di sub-tab Archived
18. Klik `[Changelog]` di toolbar List, ketik Search `PT Suspend Auto Arsip {runId}-309` di Search modal, tekan Enter, ubah ukuran halaman modal menjadi 100
19. Verifikasi hasil Search memuat baris Action `Auto-Archive`, Client Name `PT Suspend Auto Arsip {runId}-309`, Field `Status`, Old Value `Suspended`, New Value `Archived`, Modified By `System`

### Tidak Auto-Archive bila masih ada term non-terminal (TC-AC-ACC-436)

20. Tutup modal Changelog, klik sub-tab Active, ketik Search `PT Dua Produk Arsip {runId}-309`, tekan Enter
21. Verifikasi sel FAMS `Active` dan sel SAMS `Active`
22. Buka Admin Console > Client Subscription, ketik Search `PT Dua Produk Arsip {runId}-309`, tekan Enter, buka `⋯` baris term FAMS Active → Cancel Subscription, lalu klik `[Cancel Subscription]` pada dialog
23. Tunggu aksi selesai (Cancel Subscription)
24. Muat ulang Admin Console > Client, klik sub-tab Active, ketik Search `PT Dua Produk Arsip {runId}-309`, tekan Enter
25. Verifikasi sel SAMS `Active` (produk lain tetap Active)
26. Verifikasi sel FAMS `Archive` (satu produk Archive)
27. Verifikasi `PT Dua Produk Arsip {runId}-309` tetap tampil di sub-tab Active

## Notes

- Langkah penghubung (S-03): `(←)` pada kotak Search, pemilihan sub-tab, dan muat ulang List adalah pemulihan/penghubung tanpa asersi.
- Cancel term dilakukan lewat UI Client Subscription (Langkah 2 TC-AC-ACC-433 dan TC-AC-ACC-434) dan dihitung bagian dari spec ini; langkah Cancel diulang per TC karena tiap TC memakai Client berbeda.
- Spec melewati sekitar 35 langkah; alasan: semua blok satu kelas harness (Auto-Archive via Cancel) dan data berbeda per TC, kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Langkah penghubung (S-03, R-16): Langkah 4, 15, 23 `Tunggu aksi selesai (...)` menunggu hasil aksi tulis selesai sebelum muat ulang atau pindah halaman; tanpa asersi.
- Temuan untuk QA
  - TC-AC-ACC-436: Langkah TC (`Satu produk Archive, produk lain Active`) tidak menyebut Client, cara membuat satu produk Archive, dan tidak punya fixture di Tabel A3; spec membuat kembaran dengan dua produk dan meng-Cancel FAMS.
  - TC-AC-ACC-433, 434: Langkah `Cancel term FAMS dari Client Subscription` tidak menyebut dialog; spec memakai alur dialog dari TC-AC-ACC-971.
  - TC-AC-ACC-434: Old Value `Suspended` di Changelog Auto-Archive diasersi persis sesuai Expected TC.
