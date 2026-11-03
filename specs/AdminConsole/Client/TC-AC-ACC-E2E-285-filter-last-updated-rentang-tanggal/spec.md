---
id: TC-AC-ACC-E2E-285-filter-last-updated-rentang-tanggal
title: "Filter Client List: Last Updated Date Range Picker Satu Field, Rentang Inklusif, dan Tanggal Mulai Sama dengan Tanggal Akhir"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACC-382
  - TC-AC-ACC-713
coverage:
  web: automated
---

# Filter Client List: Last Updated Date Range Picker Satu Field, Rentang Inklusif, dan Tanggal Mulai Sama dengan Tanggal Akhir

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Principal) `totalControlPrincipal_automated_qaTeam1@qwertysystem.net` (A-01), password dari `Spectra.env.AC_TC_PASSWORD`. Login akun ini dilakukan di hook `before` spec ini; halaman Admin Console > Client dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control, `AC_TC_PASSWORD`). Tidak ada ganti akun di tengah spec.
- Data Pre-setup: Tabel A (C-01 sampai C-14) tersedia sebagai fixture residen yang hanya dibaca; spec ini tidak mengubahnya.
- Suite berjalan serial (`parallel: false`); spec ini tidak bergantung pada hasil spec lain.
- Flag Guided Tooltip halaman List dan Detail diset true oleh hook `before` suite dan dipulihkan hook `after` suite (dinyatakan sekali di `suite.md`).
- Fixture residen A3 C-LST-1 `PT Sortir Alfa` (Last Updated 05 Mar 2026), C-LST-2 `PT Sortir Beta` (20 Jan 2026 pukul 09:00), dan C-LST-3 `PT Sortir Gamma` (12 Jul 2026) tersedia dan hanya dibaca.
- Time Zone General Settings UTC (disediakan tim FE), tidak diubah spec; nilai Last Updated `PT Sortir Beta` 20 Jan 2026 pukul 09:00 pada rentang inklusif bergantung pada zona ini.
- Format tanggal General Settings tidak diubah spec ini. Tidak butuh klien HTTP, intercept, atau jam server.

## Test Steps

### Rentang inklusif (TC-AC-ACC-382)

1. Ketik Search `Sortir`, tekan Enter
2. Klik Filter dan lihat field Last Updated
3. Verifikasi field berlabel `Last Updated` berupa date range picker satu field dengan placeholder `Select date`
4. Pilih rentang 05 Mar 2026 sampai 12 Jul 2026, lalu klik [Apply]
5. Verifikasi `PT Sortir Alfa` (05 Mar 2026) dan `PT Sortir Gamma` (12 Jul 2026) tampil (batas awal dan batas akhir inklusif)
6. Verifikasi `PT Sortir Beta` (20 Jan 2026) tidak tampil
7. Klik Filter, klik [Clear Field], lalu klik [Apply]

### Tanggal mulai sama dengan tanggal akhir (TC-AC-ACC-713)

8. Klik Filter, pilih rentang 20 Jan 2026 sampai 20 Jan 2026, lalu klik [Apply] (Search `Sortir` masih aktif)
9. Verifikasi `PT Sortir Beta` (Last Updated 20 Jan 2026 pukul 09:00) tampil
10. Verifikasi `PT Sortir Alfa` (05 Mar 2026) dan `PT Sortir Gamma` (12 Jul 2026) tidak tampil
11. Klik Filter, klik [Clear Field], klik [Apply], lalu klik `(←)` pada kotak Search

## Notes

- Langkah penghubung (S-03): [Clear Field]/[Apply] dan `(←)` pada kotak Search sebagai pemulihan state (S-09). Search `Sortir` pada TC-AC-ACC-713 adalah Langkah 1 TC-AC-ACC-713 sendiri.
- Temuan untuk QA
  - TC-AC-ACC-382: nilai Last Updated disebut tanpa zona waktu; pengujian bergantung pada Time Zone General Settings yang tidak dicantumkan di Precondition (disediakan tim FE sebagai Time Zone UTC seperti suite lain; dinyatakan di Prerequisites).
