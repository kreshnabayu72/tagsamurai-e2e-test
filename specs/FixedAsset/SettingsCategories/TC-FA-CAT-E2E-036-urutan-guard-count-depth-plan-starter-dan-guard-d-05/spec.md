---
id: TC-FA-CAT-E2E-036-urutan-guard-count-depth-plan-starter-dan-guard-d-05
title: "Urutan Guard Plan Starter: Depth D-02, Count D-01 Mendahului Depth, dan Guard Mendahului Heads-up D-05"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-CAT-124
  - TC-FA-CAT-125
  - TC-FA-CAT-650
coverage:
  web: automated
---

# Urutan Guard Plan Starter: Depth D-02, Count D-01 Mendahului Depth, dan Guard Mendahului Heads-up D-05

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net` pada client CatStarter (Pre-setup #27, plan Starter, cap Category count 5 dan depth 1), password dari `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (CatMain). Tidak ada ganti akun di tengah spec.
- Env var `FA_TC_PASSWORD` didaftarkan di `executionConfig.environmentVariables` dan `.env.example` (nama usulan, lihat Temuan untuk QA).
- State awal (hook `before`, seed lewat API disediakan tim FE/BE): CatStarter dengan 4 kategori L1 `Starter A` sampai `Starter D` (count 4). Langkah 4 menyiapkan varian CatStarterFull lewat seed API: menambah kategori kelima milik spec `Starter Fifth {runId}-036` dan Asset Name `Starter Item` yang menunjuk `Starter A`. Hook `after` memulihkan CatStarter ke 4 kategori dan menghapus Asset Name `Starter Item`.
- Fixture `fixtures/settings-categories.json` disediakan tim FE.

## Test Steps

### TC-FA-CAT-124: Depth cap 1 memblok setiap Add Subcategory

1. Klik elipsis (⋯) pada baris `Starter A` > `+ Add Subcategory`
2. Verifikasi dialog D-02 `Cannot Add Category` · `This exceeds the category depth limit for your plan. Upgrade to nest deeper.` · `[OK]` tampil walau count masih di bawah cap
3. Klik `[OK]`
4. Siapkan varian CatStarterFull lewat seed API dan muat ulang halaman Categories

### TC-FA-CAT-125: Count cap mendahului depth cap

5. Klik elipsis (⋯) pada baris `Starter A` > `+ Add Subcategory`
6. Verifikasi dialog yang tampil D-01 (`You've reached the category limit for your plan. Upgrade to add more.`)
7. Verifikasi dialog yang tampil bukan D-02
8. Verifikasi hanya satu dialog blok yang tampil
9. Klik `[OK]`

### TC-FA-CAT-650: Guard mendahului heads-up D-05

10. Klik elipsis (⋯) pada baris `Starter A` (leaf, ditunjuk Asset Name `Starter Item`) > `+ Add Subcategory`
11. Verifikasi dialog 🔒 `Cannot Add Category` dengan body `You've reached the category limit for your plan. Upgrade to add more.` dan tombol `[OK]` tampil
12. Verifikasi dialog heads-up D-05 dan popup New Subcategory tidak terbuka
13. Klik `[OK]`

## Notes

- Langkah penghubung (S-03): langkah 3, 9, 13 (menutup dialog) dan langkah 4 (menyiapkan varian; dilakukan setelah TC-124 karena TC-124 membutuhkan count 4).
- Pada langkah 6 sampai 8 Expected a dan b TC-125 dipecah per klausa (S-01).
- Temuan untuk QA:
  - Varian CatStarterFull pada Pre-setup #27 tidak menyebut kategori kelima; spec memakai kategori milik spec.
  - TC-650 menyebut `Starter A` ditunjuk Asset Name `Starter Item` tetapi Pre-setup #21 tidak memuatnya; Asset Name itu disediakan tim FE/BE.
  - Nama env var password aktor tidak tertulis di TC; `FA_TC_PASSWORD` adalah usulan.
