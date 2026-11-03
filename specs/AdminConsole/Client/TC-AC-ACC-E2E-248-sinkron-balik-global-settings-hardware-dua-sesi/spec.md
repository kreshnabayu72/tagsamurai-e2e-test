---
id: TC-AC-ACC-E2E-248-sinkron-balik-global-settings-hardware-dua-sesi
title: "Dua Sesi: Deactivate Station dan Revoke Tablet dari Global Settings Tampil di Tab Asset Control tanpa Reload"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACC-903
  - TC-AC-ACC-904
coverage:
  web: automated
---

# Dua Sesi: Deactivate Station dan Revoke Tablet dari Global Settings Tampil di Tab Asset Control tanpa Reload

## Prerequisites

- Mode: FE+BE.
- Akun Sesi A (pengamat Admin Console): Total Control A-01 `totalControlPrincipal_automated_qaTeam1@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman List Client dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control).
- Akun Sesi B (Global Settings): Client Default User PT Uji Aksi Asset Control A-AST-8 `clientDefaultUserAksiAC_automated_ptUjiAksiAssetControl@qwertysystem.net`, password `Spectra.env.AC_CLIENT_DEFAULT_AST_PASSWORD` (nama env baru, didaftarkan di `executionConfig.environmentVariables` dan `.env.example` pada tahap script); login pada konteks browser terpisah di Global Settings > Hardware > Asset Control.
- Kemampuan teknis (kelas harness c, sesi kedua menjadi pelaku aksi dan Sesi A objek asersi): dua konteks browser terpisah yang masing-masing login lewat UI; Sesi B ditutup dan sesi login browsernya dihapus di akhir tiap TC (S-09).
- Data fixture Tabel A3 (skrip seed, bukan lewat UI; Deactivate dan Revoke permanen sehingga di-seed ulang lewat reset data uji): C-AST-7 "PT Uji Aksi Asset Control" (Active; Asset Control Total 10 / Used 6) dengan Station Active "Stasiun Sync GS Deactivate" (berisi Tablet "Tablet Sync GS Deactivate 1" Active) dan Station "Stasiun Tablet Uji" (Active; berisi Tablet Active "Tablet Sync GS Revoke" dan Tablet lain).
- State global: tidak ada yang diubah selain data fixture; suite berjalan serial (`parallel: false`); flag Guided Tooltip halaman Detail diatur hook suite.
- Env var `AC_TC_PASSWORD` sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example`; `AC_CLIENT_DEFAULT_AST_PASSWORD` didaftarkan pada tahap script.

## Test Steps

### TC-AC-ACC-903: Deactivate Station dari Global Settings tampil sebagai Deactivated tanpa reload

1. [Sesi A] Ketik Search "PT Uji Aksi Asset Control" di List Client, tekan Enter, klik Company Name "PT Uji Aksi Asset Control", lalu klik Tab Asset Control
2. [Sesi A] Catat Station Quota (Used U1 dan Available A1) dan biarkan halaman terbuka
3. [Sesi B] Login sebagai A-AST-8 dan buka Global Settings > Hardware > Asset Control
4. [Sesi B] Deactivate Station "Stasiun Sync GS Deactivate" lalu klik `[Confirm Deactivate]`
5. [Sesi B] Tunggu aksi selesai (dialog Deactivate tertutup)
6. Verifikasi (Sesi A, tanpa memuat ulang halaman) "Stasiun Sync GS Deactivate" berbadge `Deactivated` (danger)
7. Verifikasi (Sesi A) row action `Deactivate` pada "Stasiun Sync GS Deactivate" Hidden
8. Verifikasi (Sesi A) Station Quota: Used = U1 - 1 dan Available = A1 + 1
9. Verifikasi (Sesi A) kolom Tablets "Stasiun Sync GS Deactivate" bernilai 0
10. Tutup konteks Sesi B dan hapus sesi login browsernya

### TC-AC-ACC-904: Revoke Tablet dari Global Settings tampil sebagai Revoked tanpa reload

11. [Sesi A] Klik row "Stasiun Tablet Uji" untuk expand Tablet List, lalu catat kolom Tablets (T1) dan Station Quota (Used U2 dan Available A2); biarkan halaman terbuka
12. [Sesi B] Login sebagai A-AST-8 dan buka Global Settings > Hardware > Asset Control
13. [Sesi B] Expand "Stasiun Tablet Uji" lalu Revoke "Tablet Sync GS Revoke" dan klik `[Revoke Tablet]`
14. [Sesi B] Tunggu aksi selesai (dialog Revoke tertutup)
15. Verifikasi (Sesi A, tanpa memuat ulang halaman) "Tablet Sync GS Revoke" berbadge `Revoked` (danger)
16. Verifikasi (Sesi A) row action `Revoke` pada "Tablet Sync GS Revoke" Hidden
17. Verifikasi (Sesi A) kolom Tablets "Stasiun Tablet Uji" berkurang 1 dibanding T1
18. Verifikasi (Sesi A) Station Quota tidak berubah (Used = U2 dan Available = A2)
19. Tutup konteks Sesi B dan hapus sesi login browsernya

## Notes

- Sumber: `admin-console/client/TestCases/tc-client.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03, R-16): langkah 1 (Search dan buka Detail Client; hook suite hanya membuka List Client), langkah 3, 12 (login Sesi B), langkah 10, 19 (menutup konteks Sesi B, S-09), langkah 11 (expand row agar Tablet List teramati).
- Pembagian TC lintas spec: Deactivate/Revoke dari Admin Console yang tampil di Global Settings (arah sebaliknya, satu sesi berurutan) ada di spec 249.
- Pengecualian S-06 (diterima user 2026-11-03): aksi Deactivate dan Revoke pada Client "PT Uji Aksi Asset Control" (C-AST-7) tidak direplika bersuffix. Alasan objektif: pelaku Sesi B adalah Default User A-AST-8 yang terikat pada C-AST-7 (Tabel A3: "Default User C-AST-7 (Activated)"; TC-AC-ACC-903 dan 904 mensyaratkan "Client C-AST-7 dan aktor A-AST-8"), dan Global Settings > Hardware > Asset Control hanya menampilkan Station milik Client akun itu; Tabel A dan A3 tidak memuat akun Default User untuk Client kembaran bersuffix dan spec tidak boleh mengarang akun atau password, sehingga Station "Stasiun Sync GS Deactivate" dan Tablet "Tablet Sync GS Revoke" fixture C-AST-7 menjadi target aksi tulis dan dipulihkan lewat seed ulang fixture C-AST-7 oleh environment.
- Temuan untuk QA:
  - TC-AC-ACC-903 dan 904 tidak menyebut durasi tunggu propagasi SSE atau polling sehingga "tanpa memuat ulang halaman" diasersi sesudah aksi Sesi B selesai tanpa jendela waktu eksplisit; durasi tunggu perlu ditetapkan di TC.
  - TC-AC-ACC-903 menyebut tombol `[Confirm Deactivate]` dan TC-AC-ACC-904 `[Revoke Tablet]` di Global Settings; label itu diambil dari TC dan belum diverifikasi terhadap PRD Global Settings.
