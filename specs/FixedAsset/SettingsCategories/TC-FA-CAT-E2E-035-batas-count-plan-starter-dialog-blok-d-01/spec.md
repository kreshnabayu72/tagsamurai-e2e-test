---
id: TC-FA-CAT-E2E-035-batas-count-plan-starter-dialog-blok-d-01
title: "Batas Category Count Plan Starter: Dialog Blok D-01 pada Cap dan Create Lolos di Bawah Cap"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-FA-CAT-117
  - TC-FA-CAT-118
  - TC-FA-CAT-119
  - TC-FA-CAT-120
coverage:
  web: automated
---

# Batas Category Count Plan Starter: Dialog Blok D-01 pada Cap dan Create Lolos di Bawah Cap

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net` pada client CatStarter (Pre-setup #27, plan Starter, cap Category count 5 dan depth 1), password dari `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (CatMain). Tidak ada ganti akun di tengah spec.
- Env var `FA_TC_PASSWORD` didaftarkan di `executionConfig.environmentVariables` dan `.env.example` (nama usulan, lihat Temuan untuk QA).
- State awal (hook `before`, seed lewat API disediakan tim FE/BE): varian CatStarterFull, yaitu 5 kategori L1 (`Starter A` sampai `Starter D` ditambah satu kategori kelima milik spec `Starter Fifth {runId}-035`; count = cap). Langkah 14 memulihkan CatStarter ke 4 kategori lewat seed API; hook `after` memulihkan CatStarter ke 4 kategori dan menghapus `Starter E {runId}-035`.
- Data Dinamis (dibuat spec): `Starter E {runId}-035`.
- Fixture `fixtures/settings-categories.json` disediakan tim FE.

## Test Steps

### TC-FA-CAT-118 dan TC-FA-CAT-120: Dialog blok D-01 pada `[+] Category`

1. Verifikasi tombol `[+] Category` enabled
2. Klik `[+] Category` pada sidebar
3. Verifikasi dialog 🔒 `Cannot Add Category` dengan body `You've reached the category limit for your plan. Upgrade to add more.` dan tombol `[OK]` tampil
4. Verifikasi popup New Category tidak terbuka
5. Verifikasi tidak ada toast
6. Klik area backdrop di luar dialog
7. Verifikasi dialog tidak menutup
8. Klik `[OK]`
9. Verifikasi dialog menutup tanpa mutasi
10. Verifikasi tidak ada toast

### TC-FA-CAT-119: Dialog blok D-01 pada `+ Add Subcategory`

11. Klik elipsis (⋯) pada baris `Starter A` > `+ Add Subcategory`
12. Verifikasi dialog D-01 `Cannot Add Category` · `You've reached the category limit for your plan. Upgrade to add more.` · `[OK]` tampil
13. Klik `[OK]`

### TC-FA-CAT-117: Create root di bawah cap lolos

14. Pulihkan CatStarter ke 4 kategori lewat seed API (hapus kategori kelima)
15. Muat ulang halaman Categories
16. Klik `[+] Category` pada sidebar
17. Verifikasi popup New Category terbuka tanpa dialog blok
18. Isi Category Name `Starter E {runId}-035`
19. Klik `[Submit]`
20. Verifikasi toast `Success, category has been created.` tampil
21. Verifikasi kategori `Starter E {runId}-035` tersimpan
22. Verifikasi jumlah kategori menjadi 5

## Notes

- Urutan: TC-118/120/119 (diblok) dijalankan pada state penuh sebelum TC-117 (aksi sukses) (S-10). Langkah 14 sampai 15 adalah langkah penghubung pemulihan state (S-03, tanpa `Verifikasi`).
- TC-120 langkah 1 (klik `[+] Category`) dipenuhi dialog yang dibuka pada langkah 2 karena dialog sama dengan TC-118; langkah 6 sampai 9 mengikuti TC-120 langkah 2 dan 3.
- TC-116 dan TC-517 (Stay on this form dengan re-check cap) ada di spec 181.
- Langkah 22: jumlah kategori dibaca dari jumlah baris L1 pada tabel (cap kecil sehingga satu halaman).
- Temuan untuk QA:
  - Varian CatStarterFull pada Pre-setup #27 tidak menyebut kategori kelima; spec memakai kategori milik spec `Starter Fifth {runId}-035`.
  - TC-118 mensyaratkan tombol `[+] Category` enabled sebelum diklik; diasersi pada langkah 1.
  - Nama env var password aktor tidak tertulis di TC; `FA_TC_PASSWORD` adalah usulan.
