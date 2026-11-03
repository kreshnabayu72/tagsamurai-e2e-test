---
id: TC-FA-CAT-E2E-032-create-kategori-root-code-auto-manual-dan-urutan-az
title: "Create Kategori Root: Code Auto-generate, Code Manual, Urutan Category A-Z"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CAT-108
  - TC-FA-CAT-109
  - TC-FA-CAT-110
  - TC-FA-CAT-164
coverage:
  web: automated
---

# Create Kategori Root: Code Auto-generate, Code Manual, Urutan Category A-Z

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net` pada client CatMain (Pre-setup #20), password dari `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite. Tidak ada ganti akun di tengah spec.
- Env var `FA_TC_PASSWORD` didaftarkan di `executionConfig.environmentVariables` dan `.env.example` (nama usulan, lihat Temuan untuk QA).
- Data Pre-setup #20 (CatMain), dibaca: kategori L1 `Accessory` dan `Default Category` (batas urutan A-Z untuk baris baru).
- Data Dinamis (dibuat spec): `Office Furniture` (Code hasil generate `OF`, literal karena Code diturunkan dari nama), `Networking {runId}-032` (Code `net-01`, Description `Network devices`), `Bravo Sort {runId}-032` (Code `BSORT`), `Manual Code Cat {runId}-032` (Code `mc-1`). Hook `before` menghapus sisa kategori L1 `Office Furniture` serta ber-Code `NET-01`, `BSORT`, `MC-1`; hook `after` menghapus keempat kategori. Seed dan pemulihan lewat API disediakan tim FE/BE (butir hook suite di `suite.md`).
- Jam server dan jam browser sinkron; waktu dicatat sesudah `[Submit]` untuk asersi Last Updated (toleransi satu menit, S-12).
- Fixture `fixtures/settings-categories.json` disediakan tim FE.

## Test Steps

### TC-FA-CAT-108: Create root dengan field wajib saja

1. Klik `[+] Category` pada sidebar
2. Isi Category Name `Office Furniture`
3. Klik `[Submit]`
4. Catat waktu sesudah Submit
5. Verifikasi toast `Success, category has been created.` tampil
6. Verifikasi popup tertutup
7. Verifikasi baris `Office Furniture` tampil di tabel L1
8. Verifikasi node `Office Furniture` baru tampil di sidebar
9. Verifikasi Code baris `Office Furniture` terisi otomatis `OF`
10. Verifikasi Total Asset baris `Office Furniture` adalah `0`
11. Verifikasi Modified By baris `Office Furniture` berformat `[First Name] [Last Initial]` nama aktor
12. Verifikasi Last Updated baris `Office Furniture` sama dengan waktu Submit (toleransi satu menit)
13. Verifikasi seleksi sidebar tetap `All Categories`

### TC-FA-CAT-109: Create root dengan Code manual dan Description

14. Klik `[+] Category` pada sidebar
15. Isi Category Name `Networking {runId}-032`, Code `net-01`, Description `Network devices`
16. Klik `[Submit]`
17. Verifikasi toast `Success, category has been created.` tampil
18. Verifikasi baris `Networking {runId}-032` tampil dengan Code `NET-01`
19. Buka Popup Detail `Networking {runId}-032`
20. Verifikasi Description `Network devices` tampil
21. Tutup Popup Detail

### TC-FA-CAT-110: Baris baru pada posisi urut Category A-Z

22. Klik `[+] Category` pada sidebar
23. Isi Category Name `Bravo Sort {runId}-032` dan Code `BSORT`
24. Klik `[Submit]`
25. Verifikasi baris `Bravo Sort {runId}-032` berada antara `Accessory` dan `Default Category` pada tabel L1

### TC-FA-CAT-164: Code manual tidak memicu auto-generate

26. Klik `[+] Category` pada sidebar
27. Isi Category Name `Manual Code Cat {runId}-032` dan Code `mc-1`
28. Klik `[Submit]`
29. Verifikasi kolom Code baris `Manual Code Cat {runId}-032` berisi `MC-1` (auto-uppercase)
30. Verifikasi kolom Code bukan hasil generate dari nama

## Notes

- Langkah penghubung (S-03): langkah 4 (mencatat waktu Submit), langkah 21 (menutup Popup Detail).
- Pengecualian S-12 yang diperlukan modul: nama `Office Furniture` literal tanpa suffix karena Expected Code `OF` diturunkan dari nama; pembersihan dijamin hook `before` dan `after`. Code hasil generate untuk nama bersuffix tidak diasersi.
- Langkah 30: TC menyebut hasil generate dari nama `MCC`; karena nama bersuffix, spec mengasersi bahwa Code bukan hasil generate tanpa menuliskan nilainya.
- Post Condition TC-108 (root leaf selectable; Changelog satu baris Create, Code tanpa baris) dan TC-109, serta TC-110 tidak punya langkah observasi di TC sehingga tidak diasersi di spec ini (S-01). Pencatatan Changelog Create diasersi di spec 182.
- Temuan untuk QA:
  - TC-108 mencontohkan Modified By `Jane S` tanpa menyebut nama aktor Total Control; spec memakai format `[First Name] [Last Initial]` (R-14).
  - Post Condition TC-108 tanpa langkah observasi (selectable, Changelog).
  - Nama env var password aktor tidak tertulis di TC; `FA_TC_PASSWORD` adalah usulan.
