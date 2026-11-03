---
id: TC-AC-ACC-E2E-264-changelog-scope-baris-viewer-distributor
title: "Changelog Client dan Asset Control: Viewer Distributor Hanya Melihat Baris Partner dalam Jaringannya"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AC-ACC-1013
  - TC-AC-ACC-1017
coverage:
  web: automated
---

# Changelog Client dan Asset Control: Viewer Distributor Hanya Melihat Baris Partner dalam Jaringannya

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Distributor Total Control A-13 (PT Distribusi Nusantara) `totalControlDistributor_automated_ptDistribusiNusantara@qwertysystem.net`, password `Spectra.env.AC_CLIENT_DIST_TC_PASSWORD` (nama env baru, didaftarkan di `executionConfig.environmentVariables` dan `.env.example` pada tahap script). Login di hook `before` spec ini; halaman List Client dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control).
- Data fixture Tabel A3 (hanya dibaca, skrip seed): C-FX16-1 "PT Jaringan Ganda Uji" (Active; relasi Partner-Client aktif ke CV Mitra Sejati, CV Mitra Lestari (Distributor induk PT Distribusi Nusantara), dan CV Mitra Timur (Distributor induk PT Distribusi Timur); Group Cabang Menteng). Riwayat Changelog Client C-FX16-1: Action `Change Partner`, Field `Partner`, Old Value `—` dengan New Value `CV Mitra Sejati`, `CV Mitra Lestari`, `CV Mitra Timur` (satu baris masing-masing), ditambah satu baris campuran (Old Value `CV Mitra Sejati`, New Value `CV Mitra Timur`). Riwayat Changelog Asset Control FX16: Action `Generate Enrollment QR` dengan Modified By "Rina Putri" (Partner CV Mitra Sejati), "Dewi Lestari" (Partner CV Mitra Lestari), dan "Agus Timur" (Partner CV Mitra Timur); Action `Deactivate Station` dengan Modified By "Bima Support" (user Principal).
- Kemampuan teknis: Changelog adalah audit trail permanen; baris seed dibatasi lewat Search "PT Jaringan Ganda Uji" dan ukuran halaman 100 (S-14).
- State global: tidak ada yang diubah; suite berjalan serial (`parallel: false`); flag Guided Tooltip halaman List dan Detail diatur hook suite.

## Test Steps

### TC-AC-ACC-1013: Changelog Client: viewer Distributor hanya melihat baris Change Partner untuk Partner dalam jaringannya

1. Klik [Changelog] di toolbar List
2. Ketik "PT Jaringan Ganda Uji" di Search modal, tekan Enter, lalu ubah ukuran halaman modal menjadi 100
3. Verifikasi tepat dua baris Action `Change Partner` tampil dengan New Value `CV Mitra Sejati` dan `CV Mitra Lestari` (Field `Partner`, Old Value `—`)
4. Verifikasi tidak ada baris atau sel yang memuat "CV Mitra Timur"
5. Verifikasi tidak ada baris placeholder atau teks "Other manager"
6. Tutup modal Changelog

### TC-AC-ACC-1017: Changelog Asset Control: viewer Distributor hanya melihat baris yang diubah user Partner dalam jaringannya

7. Klik sub-tab Active, ketik Search "PT Jaringan Ganda Uji", tekan Enter, lalu klik Company Name "PT Jaringan Ganda Uji"
8. Klik Tab Asset Control
9. Klik ikon Changelog di Tab Asset Control
10. Verifikasi dua baris Action `Generate Enrollment QR` tampil dengan Modified By "Rina Putri" dan "Dewi Lestari"
11. Verifikasi baris dengan Modified By "Agus Timur" tidak tampil
12. Verifikasi baris Action `Deactivate Station` dengan Modified By "Bima Support" (user Principal) tidak tampil
13. Verifikasi tidak ada baris placeholder atau teks "Other manager"
14. Tutup modal Changelog

## Notes

- Sumber: `admin-console/client/TestCases/tc-client.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03, R-16): langkah 2 (Search "PT Jaringan Ganda Uji" dan ukuran halaman 100 sesuai TC), langkah 6 dan 14 (menutup modal), langkah 7 (Search dan buka Detail Client; hook suite hanya membuka List Client).
- Asersi absence memakai anchor positif baris `Change Partner` `CV Mitra Sejati` dan `CV Mitra Lestari` yang tampil (bagian 8b butir 2) dan scope exclusion dengan data seed milik TC (bukan kelas g).
- Pembagian TC lintas spec: sisi viewer Partner ada di spec 263; baris `Retry Access Setup` untuk Distributor ada di spec 265.
- Temuan untuk QA:
  - TC-AC-ACC-1013 dan 1017 tidak menyebut Modified By baris `Change Partner`; hanya Field, Old Value, dan New Value yang diasersi.
