---
id: TC-FA-CAT-E2E-038-batas-depth-plan-growth-dan-happy-path-lintas-tier-plan
title: "Batas Depth Plan Growth dan Happy Path Create, Edit, Delete Identik Lintas Tier Plan"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CAT-123
  - TC-FA-CAT-129
coverage:
  web: automated
---

# Batas Depth Plan Growth dan Happy Path Create, Edit, Delete Identik Lintas Tier Plan

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net` pada client CatGrowth (Pre-setup #28, plan Growth, cap Category count 20 dan depth 2), password dari `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (CatMain).
- Ganti akun eksplisit di langkah 6 (badan perulangan): tiap client pada tabel "Client yang diuji" dimasuki dengan akun Total Control Pre-setup #1 pada client itu, password `Spectra.env.FA_TC_PASSWORD`.
- Env var `FA_TC_PASSWORD` didaftarkan di `executionConfig.environmentVariables` dan `.env.example` (nama usulan, lihat Temuan untuk QA).

| Baris | Client | Pre-setup | Plan |
|---|---|---|---|
| 1 | CatGrowth | #28 | Growth (cap depth 2) |
| 2 | CatStarter | #27 | Starter (count 4, cap 5) |
| 3 | CatDeep | #26 | Professional (cap depth 5) |
| 4 | CatMain | #20 | Enterprise |

- Data Pre-setup dibaca: `Growth Root` (Code `GR`) > `Growth Child` (Code `GC`) pada CatGrowth.
- Data Dinamis (dibuat dan dihapus spec pada tiap client): `Tier Check {runId}-038` (Description `Tier desc`). Hook `after` menghapus sisa `Tier Check {runId}-038` pada keempat client. Seed dan pemulihan lewat API disediakan tim FE/BE (butir hook suite di `suite.md`).
- Spec ini mengubah sesi antar-client (kelas h: tier plan); suite berjalan serial.
- Fixture `fixtures/settings-categories.json` disediakan tim FE.

## Test Steps

### TC-FA-CAT-123: Plan Growth, parent depth 1 lolos dan depth 2 diblok

1. Klik elipsis (⋯) pada `Growth Root` > `+ Add Subcategory`
2. Verifikasi popup New Subcategory terbuka
3. Klik `✕` pada popup
4. Klik elipsis (⋯) pada `Growth Child` > `+ Add Subcategory`
5. Verifikasi dialog D-02 `Cannot Add Category` · `This exceeds the category depth limit for your plan. Upgrade to nest deeper.` · `[OK]` tampil
6. Klik `[OK]`

### TC-FA-CAT-129: Happy path lintas tier plan

Untuk setiap baris pada tabel "Client yang diuji" (langkah 7 sampai 19):

7. Ganti akun: logout, lalu login dengan Total Control client pada baris tabel
8. Klik `[+] Category` pada sidebar
9. Isi Category Name `Tier Check {runId}-038`
10. Klik `[Submit]`
11. Verifikasi toast `Success, category has been created.` tampil
12. Klik elipsis (⋯) pada baris `Tier Check {runId}-038` > `Edit`
13. Ubah Description menjadi `Tier desc`
14. Klik `[Save]`
15. Verifikasi toast `Success, category has been updated.` tampil
16. Klik elipsis (⋯) pada baris `Tier Check {runId}-038` > `Delete`
17. Klik `[Delete]` pada dialog konfirmasi
18. Verifikasi toast `Success, category has been deleted.` tampil
19. Verifikasi tidak ada upsell atau gating menu per plan pada halaman

## Notes

- Alasan di atas sekitar 35 langkah: langkah 7 sampai 19 diulang pada empat client (ekspansi 52 langkah, 6 + 52 = 58 langkah) dengan parameter di tabel Prerequisites; bagian tiap client berdiri sendiri sehingga kegagalan satu client tidak membuat client lain kehilangan makna (8b butir 7).
- Langkah penghubung (S-03): langkah 3 (menutup popup tanpa input), langkah 6 (menutup dialog), langkah 7 (ganti akun; baris 1 mengulang login akun yang sama agar badan perulangan seragam tanpa langkah bersyarat).
- Cap count tidak tercapai pada keempat client (CatStarter count 4 menjadi 5 lalu kembali 4 setelah Delete).
- Hook `after` menjalankan pembersihan walau spec gagal di tengah perulangan.
- Temuan untuk QA:
  - TC-129 menyebut "tidak ada upsell atau gating menu per plan" tanpa menyebut elemen yang diperiksa; spec mengasersi pada halaman Categories tiap client.
  - TC-129 tidak menyebut akun tiap client; spec memakai Total Control Pre-setup #1 per client.
  - Nama env var password aktor tidak tertulis di TC; `FA_TC_PASSWORD` adalah usulan.
