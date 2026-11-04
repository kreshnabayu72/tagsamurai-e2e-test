---
id: TC-FA-LBL-E2E-066-default-provenance-relasi-label-asal-template-dan-manual
title: "Defaults: provenance relasi label (default dari template Asset Name, manual dari Asset Detail)"
priority: Medium
caseType: Positive
status: draft
sourceRules:
  - FALB:defaults-ordering-spec/default-provenance
coverage:
  web: automated
---

# Defaults: provenance relasi label (default dari template Asset Name, manual dari Asset Detail)

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control (`DU-01`), env `FA_TC_EMAIL` dan `FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Settings > Asset Master > tab Labels dibuka hook `beforeEach` suite. Tidak ada ganti akun.
- Data uji `DU-73` (Asset Name dengan Default Label dan aset untuk uji provenance), bersuffix `{runId}-066`, dibuat lewat sesi API di hook `before` dan dihapus di hook `after` (relasi label, aset, Asset Name, lalu label): Asset Name `Prov-{runId}-066` dengan label seed `Prov-{runId}-066-d` sebagai Default Label, satu aset Active seed yang dibuat dari template Asset Name itu (relasi label `-d` bersumber `default`), dan label seed kedua `Prov-{runId}-066-m` yang ditempel manual pada aset yang sama lewat Asset Detail pada langkah 5 sampai 6 (relasi bersumber `manual`).
- Kemampuan teknis: sesi API aktor dan fixture BE untuk seeding label, Asset Name, dan aset serta membaca asal-usul (`source`) relasi aset dan label; disediakan tim FE/BE. Asset List dan Asset Detail dimiliki modul `asset/` (`asset/PRD/asset.md` §4.1d).
- State global: spec menempelkan satu label manual pada aset seed; hook `after` membersihkan semuanya. Suite berjalan serial (`parallel: false`).

## Test Steps

### FALB:defaults-ordering-spec/default-provenance: Provenance relasi: manual lewat Asset Detail, default lewat template Asset Name

1. Buka Asset List modul `asset/`, ketik Search aset seed `DU-73`, tekan Enter
2. Buka Asset Detail aset seed `DU-73`
3. Verifikasi chip label `-d` milik `DU-73` tampil pada seksi Labels
4. Verifikasi ikon `[✕]` tidak tampil pada chip label `-d` (relasi dari template Asset Name terkunci)
5. Klik `[+ Add Label]` pada seksi Labels, lalu pilih label `-m` milik `DU-73`
6. Verifikasi chip label `-m` milik `DU-73` tampil dengan ikon `[✕]` pada seksi Labels
7. Verifikasi chip label `-d` milik `DU-73` tetap tampil tanpa ikon `[✕]`
8. Baca relasi label aset seed `DU-73` lewat fixture BE
9. Verifikasi relasi label `-d` bersumber `default`
10. Verifikasi relasi label `-m` bersumber `manual`

## Notes

- Langkah penghubung (S-03): langkah 1 menemukan aset seed di Asset List yang dapat memuat lebih dari satu halaman (R-16); langkah 2 membuka Asset Detail; langkah 8 membaca state lewat fixture BE (bagian 8b butir 1: hanya state data yang diasersi, langkah 9 dan 10).
- Anchor positif: langkah 3 membuktikan relasi `-d` sudah termuat sebelum asersi ikon `[✕]` tidak tampil di langkah 4; langkah 6 (chip `-m` dengan ikon `[✕]`) menjadi pembanding untuk langkah 7.
- Asal-usul (`source`) tidak tampil di UI; ikon `[✕]` pada chip hanya ada untuk relasi manual (`asset/` §4.1d, `FALB-LOGIC-04c`) dan menjadi bukti tampilan, sedangkan nilai `source` (`default` atau `manual`) diasersi lewat fixture BE (langkah 9 dan 10).
- Desain data: relasi `manual` dan `default` diuji pada satu aset seed dengan dua label (`-d` dan `-m`), karena aset dari Asset Name yang sama selalu memperoleh Default Label lewat template.
