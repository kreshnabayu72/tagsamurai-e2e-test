---
id: TC-AC-ACC-E2E-263-changelog-scope-baris-viewer-partner
title: "Changelog Client dan Asset Control: Viewer Partner Hanya Melihat Baris yang Melibatkan Dirinya"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AC-ACC-1012
  - TC-AC-ACC-1016
  - TC-AC-ACC-1023
coverage:
  web: automated
---

# Changelog Client dan Asset Control: Viewer Partner Hanya Melihat Baris yang Melibatkan Dirinya

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Partner Total Control A-14 (CV Mitra Sejati) `totalControlPartner_automated_cvMitraSejati@qwertysystem.net`, password `Spectra.env.AC_CLIENT_PARTNER_TC_PASSWORD` (nama env baru, didaftarkan di `executionConfig.environmentVariables` dan `.env.example` pada tahap script). Login di hook `before` spec ini; halaman List Client dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control).
- Data fixture Tabel A3 (hanya dibaca, skrip seed): C-FX16-1 "PT Jaringan Ganda Uji" (Active; Client Code `FX16-001`; relasi Partner-Client aktif ke CV Mitra Sejati (Anchor), CV Mitra Lestari (Distributor induk PT Distribusi Nusantara), dan CV Mitra Timur (Distributor induk PT Distribusi Timur); Group Cabang Menteng). Riwayat Changelog Client C-FX16-1: Action `Change Partner`, Field `Partner`, Old Value `—` dengan New Value `CV Mitra Sejati`, `CV Mitra Lestari`, `CV Mitra Timur` (satu baris masing-masing), ditambah satu baris campuran (Old Value `CV Mitra Sejati`, New Value `CV Mitra Timur`). Riwayat Changelog Asset Control FX16 pada C-FX16-1: Action `Generate Enrollment QR` dengan Modified By "Rina Putri" (Partner CV Mitra Sejati), "Dewi Lestari" (Partner CV Mitra Lestari), dan "Agus Timur" (Partner CV Mitra Timur); Action `Deactivate Station` dengan Modified By "Bima Support" (user Principal).
- Kemampuan teknis: Changelog adalah audit trail permanen; baris seed dibatasi lewat Search "PT Jaringan Ganda Uji" dan ukuran halaman 100 (S-14).
- State global: tidak ada yang diubah; suite berjalan serial (`parallel: false`); flag Guided Tooltip halaman List dan Detail diatur hook suite.

## Test Steps

### TC-AC-ACC-1012: Changelog Client: viewer Partner hanya melihat baris Change Partner yang melibatkan dirinya

1. Klik [Changelog] di toolbar List
2. Ketik "PT Jaringan Ganda Uji" di Search modal, tekan Enter, lalu ubah ukuran halaman modal menjadi 100
3. Verifikasi tepat satu baris Action `Change Partner` tampil: Field `Partner`, Old Value `—`, New Value `CV Mitra Sejati`
4. Verifikasi tidak ada baris atau sel yang memuat "CV Mitra Lestari" atau "CV Mitra Timur"
5. Verifikasi tidak ada baris placeholder atau teks "Other manager"
6. Verifikasi jumlah baris pada Pagination hanya menghitung baris yang tampil

### TC-AC-ACC-1023: Changelog Client: baris campuran Partner viewer dan Partner lain disaring seluruhnya

7. Verifikasi baris Action `Change Partner` dengan Old Value `CV Mitra Sejati` dan New Value `CV Mitra Timur` tidak tampil sama sekali, juga tidak sebagai baris dengan nama disamarkan
8. Verifikasi tepat satu baris Action `Change Partner` tampil: Field `Partner`, Old Value `—`, New Value `CV Mitra Sejati`
9. Verifikasi tidak ada baris atau sel yang memuat "CV Mitra Timur" atau "CV Mitra Lestari"
10. Verifikasi tidak ada baris placeholder atau teks "Other manager"
11. Verifikasi jumlah baris pada Pagination hanya menghitung baris yang tampil
12. Tutup modal Changelog

### TC-AC-ACC-1016: Changelog Asset Control: viewer Partner hanya melihat baris yang diubah user Partner itu sendiri

13. Klik sub-tab Active, ketik Search "PT Jaringan Ganda Uji", tekan Enter, lalu klik Company Name "PT Jaringan Ganda Uji"
14. Klik Tab Asset Control
15. Klik ikon Changelog di Tab Asset Control
16. Verifikasi tepat satu baris Action `Generate Enrollment QR` tampil dengan Modified By "Rina Putri"
17. Verifikasi baris dengan Modified By "Dewi Lestari" dan "Agus Timur" tidak tampil
18. Verifikasi baris Action `Deactivate Station` dengan Modified By "Bima Support" (user Principal) tidak tampil
19. Verifikasi tidak ada baris placeholder atau teks "Other manager"
20. Tutup modal Changelog

## Notes

- Sumber: `admin-console/client/TestCases/tc-client.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03, R-16): langkah 2 (Search "PT Jaringan Ganda Uji" dan ukuran halaman 100 sesuai TC), langkah 12 dan 20 (menutup modal), langkah 13 (Search dan buka Detail Client; hook suite hanya membuka List Client).
- TC-AC-ACC-1012 dan TC-AC-ACC-1023 memakai tampilan modal yang sama (langkah 1 sampai 6 dan 7 sampai 11 berjalan pada tampilan yang sama tanpa membuka ulang); asersi absence memakai anchor positif baris `Change Partner` `CV Mitra Sejati` yang tampil (bagian 8b butir 2) dan scope exclusion dengan data seed milik TC (bukan kelas g).
- Pembagian TC lintas spec: sisi viewer Distributor ada di spec 264; sisi Principal dan Distributor untuk baris `Retry Access Setup` di spec 265.
- Temuan untuk QA:
  - TC-AC-ACC-1012 dan 1023 tidak menyebut Modified By baris `Change Partner` yang dilihat Partner; hanya Field, Old Value, dan New Value yang diasersi.
