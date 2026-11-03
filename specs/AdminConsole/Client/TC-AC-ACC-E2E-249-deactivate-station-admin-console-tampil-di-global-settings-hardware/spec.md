---
id: TC-AC-ACC-E2E-249-deactivate-station-admin-console-tampil-di-global-settings-hardware
title: "Deactivate Station dari Admin Console Tampil sebagai Deactivated di Global Settings > Hardware"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACC-334
coverage:
  web: automated
---

# Deactivate Station dari Admin Console Tampil sebagai Deactivated di Global Settings > Hardware

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Total Control A-01 `totalControlPrincipal_automated_qaTeam1@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman List Client dibuka hook `beforeEach` suite. Akun kedua (langkah ganti akun): Client Default User PT Uji Aksi Asset Control A-AST-8 `clientDefaultUserAksiAC_automated_ptUjiAksiAssetControl@qwertysystem.net`, password `Spectra.env.AC_CLIENT_DEFAULT_AST_PASSWORD` (nama env baru, didaftarkan di `executionConfig.environmentVariables` dan `.env.example` pada tahap script). Hook `after` mengembalikan sesi ke akun default suite (Total Control).
- Data fixture Tabel A3 (skrip seed, bukan lewat UI; Deactivate permanen sehingga di-seed ulang lewat reset data uji): C-AST-7 "PT Uji Aksi Asset Control" dengan Station Active "Stasiun Sync AC Deactivate" berisi Tablet "Tablet Sync AC Deactivate 1" (Active).
- State global: tidak ada yang diubah selain data fixture; suite berjalan serial (`parallel: false`); flag Guided Tooltip halaman Detail diatur hook suite.
- Env var `AC_TC_PASSWORD` sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example`.

## Test Steps

1. Ketik Search "PT Uji Aksi Asset Control" di List Client, tekan Enter, klik Company Name "PT Uji Aksi Asset Control", lalu klik Tab Asset Control
2. Buka ⋯ pada Station "Stasiun Sync AC Deactivate" lalu klik Deactivate, lalu klik `[Deactivate]` pada dialog
3. Verifikasi toast sukses di Admin Console: "Success, station has been deactivated."
4. Logout, lalu login sebagai Client Default User A-AST-8
5. Buka Global Settings > Hardware > Asset Control
6. Verifikasi Station List Global Settings menampilkan "Stasiun Sync AC Deactivate" berstatus `Deactivated`
7. Verifikasi Station List Global Settings menampilkan "Tablet Sync AC Deactivate 1" berstatus `Revoked`

## Notes

- Sumber: `admin-console/client/TestCases/tc-client.md`.
- Langkah penghubung (S-03, R-16): langkah 1 (Search dan buka Detail Client; hook suite hanya membuka List Client).
- Ganti akun (langkah 4) memakai Step eksplisit; sesi tidak paralel sehingga bukan konteks kedua kelas c.
- Pembagian TC lintas spec: arah sebaliknya (Global Settings yang menjadi pelaku, Admin Console sebagai pengamat tanpa reload, dua sesi paralel) ada di spec 248; pencatatan Changelog Asset Control saat Deactivate di spec 270.
- Pengecualian S-06 (diterima user 2026-11-03): aksi Deactivate pada Station "Stasiun Sync AC Deactivate" Client "PT Uji Aksi Asset Control" (C-AST-7) tidak direplika bersuffix. Alasan objektif: TC-AC-ACC-334 mengasersi tampilan Station List di Global Settings > Hardware > Asset Control oleh Default User A-AST-8 yang terikat pada C-AST-7 (Tabel A3: "Default User C-AST-7 (Activated)"), dan hanya Station milik Client akun itu yang tampil; Tabel A dan A3 tidak memuat akun Default User untuk Client kembaran bersuffix dan spec tidak boleh mengarang akun atau password, sehingga Station fixture C-AST-7 menjadi target aksi tulis dan dipulihkan lewat seed ulang fixture C-AST-7 oleh environment.
- Temuan untuk QA:
  - TC-AC-ACC-334 Post Condition (fixture C-AST-7 dipulihkan) dan struktur Station List Global Settings (kolom tempat status tampil) tidak dijelaskan; "Tablet Sync AC Deactivate 1 berstatus Revoked" diasersi pada Station List Global Settings sesuai Expected, tanpa menyebut expand Station.
