---
id: TC-FA-CAT-E2E-037-batas-depth-plan-catdeep-guard-depth-diblok-d-02
title: "Batas Depth Plan CatDeep: Depth 5 Lolos dan Depth Melebihi Cap Diblok D-02"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-FA-CAT-122
  - TC-FA-CAT-649
  - TC-FA-CAT-121
coverage:
  web: automated
---

# Batas Depth Plan CatDeep: Depth 5 Lolos dan Depth Melebihi Cap Diblok D-02

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net` pada client CatDeep (Pre-setup #26, plan Professional, cap Category count 100 dan depth 5), password dari `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (CatMain). Tidak ada ganti akun di tengah spec.
- Env var `FA_TC_PASSWORD` didaftarkan di `executionConfig.environmentVariables` dan `.env.example` (nama usulan, lihat Temuan untuk QA).
- Data Pre-setup #26 (CatDeep), dibaca: rantai `Level One` > `Level Two` > `Level Three` > `Level Four` (Code `L4`) > `Level Five` (depth 5).
- State yang diubah spec: Asset Name `Deep Item` yang menunjuk `Level Five` (varian Pre-setup #26) disiapkan di langkah 6. Hook `after` menghapus Asset Name `Deep Item` dan menghapus `Level Five Alt {runId}-037`. Seed dan pemulihan lewat API disediakan tim FE/BE (butir hook suite di `suite.md`).
- Data Dinamis (dibuat spec): `Level Five Alt {runId}-037` (di bawah `Level Four`).
- Fixture `fixtures/settings-categories.json` disediakan tim FE.

## Test Steps

### TC-FA-CAT-122: Depth melebihi cap memunculkan D-02

1. Expand rantai `Level One` sampai `Level Five` di sidebar dan klik node `Level Four`
2. Klik elipsis (⋯) pada baris `Level Five` > `+ Add Subcategory`
3. Verifikasi dialog 🔒 `Cannot Add Category` dengan body `This exceeds the category depth limit for your plan. Upgrade to nest deeper.` dan tombol `[OK]` tampil
4. Verifikasi popup New Subcategory tidak terbuka
5. Klik `[OK]`

### TC-FA-CAT-649: Guard depth mendahului heads-up D-05

6. Siapkan Asset Name `Deep Item` yang menunjuk `Level Five` lewat seed API dan muat ulang halaman Categories
7. Expand rantai sampai `Level Five` dan klik node `Level Four`
8. Klik elipsis (⋯) pada baris `Level Five` (leaf, ditunjuk `Deep Item`) > `+ Add Subcategory`
9. Verifikasi dialog 🔒 `Cannot Add Category` dengan body `This exceeds the category depth limit for your plan. Upgrade to nest deeper.` dan tombol `[OK]` tampil
10. Verifikasi dialog heads-up D-05 dan popup New Subcategory tidak terbuka
11. Klik `[OK]`

### TC-FA-CAT-121: Depth sama dengan cap lolos

12. Klik node `Level Three` di sidebar
13. Klik elipsis (⋯) pada baris `Level Four` > `+ Add Subcategory` (hasil depth 5)
14. Verifikasi popup terbuka tanpa dialog blok
15. Isi Category Name `Level Five Alt {runId}-037`
16. Klik `[Submit]`
17. Verifikasi toast `Success, category has been created.` tampil
18. Klik node `Level Four` di sidebar
19. Verifikasi kategori `Level Five Alt {runId}-037` tersimpan

## Notes

- Satu client dan satu topik (cap depth plan) atas rantai depth 5 yang sama.
- Urutan: blokir (122, 649) mendahului aksi sukses (121) yang menambah satu kategori.
- Langkah penghubung (S-03): langkah 1, 7, 12, 18 (navigasi dan memilih node induk) dan langkah 6 (state).
- Temuan untuk QA:
  - TC-649 menyebut `Level Five` ditunjuk Asset Name `Deep Item` tetapi tidak ada di Pre-setup #21.
  - Nama env var password aktor tidak tertulis di TC; `FA_TC_PASSWORD` adalah usulan.
