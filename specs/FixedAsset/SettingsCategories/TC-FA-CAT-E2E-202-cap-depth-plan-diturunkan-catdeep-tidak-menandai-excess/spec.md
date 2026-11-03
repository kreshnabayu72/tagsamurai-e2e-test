---
id: TC-FA-CAT-E2E-202-cap-depth-plan-diturunkan-catdeep-tidak-menandai-excess
title: "Cap Depth Plan CatDeep Diturunkan: Node Lebih Dalam Tidak Excess dan Tetap Berfungsi, Add Subcategory Baru Diblok D-02"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-CAT-318
  - TC-FA-CAT-516
coverage:
  web: automated
---

# Cap Depth Plan CatDeep Diturunkan: Node Lebih Dalam Tidak Excess dan Tetap Berfungsi, Add Subcategory Baru Diblok D-02

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net` pada client CatDeep (Pre-setup #26, plan Professional, cap Category count 100 dan depth 5), password dari `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (CatMain). Tidak ada ganti akun di tengah spec.
- Pelaku kedua: Principal Automation (Pre-setup #11) lewat sesi API (butir hook suite di `suite.md`; akun disediakan tim FE) untuk menurunkan cap depth plan CatDeep di Admin Console > Plans & Licensing.
- Env var `FA_TC_PASSWORD` didaftarkan di `executionConfig.environmentVariables` dan `.env.example` (nama usulan, lihat Temuan untuk QA).
- Data Pre-setup #26 (CatDeep), dibaca: rantai `Level One` > `Level Two` > `Level Three` > `Level Four` > `Level Five` (depth 5). Jumlah kategori jauh di bawah cap Category count 100.
- State global yang diubah: cap depth plan CatDeep diturunkan dari 5 menjadi 2 oleh Principal Automation di langkah 1. Hook `after` memulihkan cap depth plan menjadi 5. Pemulihan lewat API disediakan tim FE/BE (butir hook suite di `suite.md`). Suite berjalan serial.
- Fixture `fixtures/settings-categories.json` disediakan tim FE.

## Test Steps

### TC-FA-CAT-318: Cap kedalaman turun tidak memangkas dan tidak menandai Excess

1. Principal Automation menurunkan cap depth plan CatDeep menjadi 2 hingga tersimpan
2. Muat ulang halaman Categories dan expand rantai `Level One` sampai `Level Five`
3. Verifikasi `Level Four` dan `Level Five` bukan Excess
4. Verifikasi `Level Four` dan `Level Five` tidak redup
5. Klik elipsis (⋯) pada `Level Five` di sidebar
6. Verifikasi menu memuat aksi `Edit`
7. Tutup menu
8. Klik elipsis (⋯) pada `Level Two` di sidebar > `+ Add Subcategory`
9. Verifikasi dialog D-02 `This exceeds the category depth limit for your plan. Upgrade to nest deeper.` tampil
10. Klik `[OK]`

### TC-FA-CAT-516: Excess hanya berlaku untuk Category count

11. Klik menu Fixed Asset > Settings > Categories untuk membuka ulang halaman
12. Verifikasi Breadcrumb halaman Categories tampil
13. Verifikasi tidak ada node berstatus Excess dan Alert Consolidation tidak tampil

## Notes

- Satu client dan satu topik (cap depth plan diturunkan atas rantai depth 5 yang sama); TC-516 memakai state yang sama dengan TC-318 sehingga berurutan tanpa menurunkan cap ulang.
- Principal Automation hanya pemicu state lewat sesi API, bukan konteks kedua; tanpa butir `P-2`. Langkah 1 ditulis "... hingga ... tersimpan" (R-20).
- TC-516 dibuka ulang di langkah 11 dengan Breadcrumb sebagai anchor positif (R-21) sebelum asersi absence di langkah 13.
- Langkah penghubung (S-03): langkah 2 (muat ulang dan expand rantai), 7 (menutup menu), 10 (menutup dialog), 11 (membuka ulang halaman) dan langkah 1 (state).
- Temuan untuk QA:
  - TC-318 tidak menyebut akun pengubah plan; spec memakai Principal Automation (Pre-setup #11) lewat sesi API.
  - Nama env var password aktor tidak tertulis di TC; `FA_TC_PASSWORD` adalah usulan.
