---
id: TC-GS-IMPORT-E2E-081-visibilitas-saran-represented-by-tidak-dibatasi-hak-lihat-aktor-import
title: "Visibilitas Saran Represented By Tidak Dibatasi Hak Lihat Aktor (Import data Create dan Total Control)"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-IMPORT-969
coverage:
  web: automated
---

# Visibilitas Saran Represented By Tidak Dibatasi Hak Lihat Aktor (Import data Create dan Total Control)

## Prerequisites

- Mode: FE+BE (backend nyata). Suite serial (`parallel: false`); lihat `suite.md`.
- Akun (Client A), password lewat env:
  - Import data (Create) Client A (Rina Marlina; capability Import data C dan R, tanpa capability lihat User) `importCreate_automated_qaTeam1@qwertysystem.net`, `Spectra.env.GS_IMPORTCREATE_PASSWORD`; login di hook `before`.
  - Total Control Client A (Sari Dewi) `totalControl_automated_qaTeam1@qwertysystem.net`, `Spectra.env.GS_TC_PASSWORD`; login lewat langkah ganti akun. Hook `after` mengembalikan sesi ke akun default suite.
  - Password tidak ditulis di spec atau fixture.
- Data Dinamis (Client A, disiapkan lewat skrip fixture sebelum TC): D-06 draft User Non Login 5 baris `pending` dari `user-non-login-5.csv`; D-92 dua belas User Login aktif (Activated) `lookup-01@example.com` sampai `lookup-12@example.com` (First Name `Pemilik`, Last Name `01` sampai `12`).
- Layar awal: hook `beforeEach` suite membuka Global Settings > Import > User Non Login. Guided Tooltip: flag `guided_tooltip_seen_gs-import` untuk kedua akun diatur hook suite `before` dan dipulihkan hook `after`; lihat `suite.md`.
- Pemulihan: draft Client A dipulihkan ke D-06 dan 12 User Login D-92 dihapus (Kontrak Fixture R2).

## Test Steps

1. [Import data (Create)] Klik `⋯` pada baris #1
2. [Import data (Create)] Pilih Edit
3. [Import data (Create)] Klik sel Represented By baris #1 dan ketik `lookup-0`
4. [Import data (Create)] Verifikasi daftar saran memuat 9 saran urut `lookup-01@example.com` sampai `lookup-09@example.com`
5. [Import data (Create)] Klik `[Cancel]`, lalu klik `[Discard]` pada dialog
6. Ganti akun: login sebagai Total Control Client A dan buka Import > User Non Login
7. [Total Control] Klik `⋯` pada baris #1
8. [Total Control] Pilih Edit
9. [Total Control] Klik sel Represented By baris #1 dan ketik `lookup-0`
10. [Total Control] Verifikasi daftar saran memuat 9 saran urut `lookup-01@example.com` sampai `lookup-09@example.com`, sama dengan yang tampil untuk akun Import data (Create)
11. [Total Control] Klik `[Cancel]`, lalu klik `[Discard]` pada dialog

## Notes

- Mode: FE+BE. Sumber: `global-settings/import/TestCases/tc-import.md`. Spec Role Matrix ringkas untuk dua akun berurutan dengan langkah identik dan Step ganti akun eksplisit (langkah 6).
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 5 dan 11 (menutup sesi edit; ketikan pada sel membuat sesi dirty sehingga dialog Discard dipakai), langkah 6 (ganti akun).
- Pembagian TC lintas spec: TC-GS-IMPORT-969 hanya ada di spec ini.
- Temuan untuk QA:
  - TC-GS-IMPORT-969 Expected a menyebut "sama dengan yang tampil untuk akun Total Control Client A" tetapi Langkah Uji hanya memuat satu akun (Import data (Create)); spec menambahkan blok kedua dengan akun Total Control sebagai langkah pembanding.
  - TC-GS-IMPORT-969 tidak menyebut cara menutup sesi edit; spec menambahkan `[Cancel]` dan `[Discard]` sebagai langkah penghubung.
