---
id: TC-FA-CAT-E2E-157-tabel-step-sort-kolom-teks-dan-filter
title: "Tabel Step Category Consolidation: Sort Tiga State Kolom Teks (Category Name, Code, Status, Modified By), Screening Filter Panel, Filter Status dan Modified By, serta Filter Last Updated"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CAT-446
  - TC-FA-CAT-449
  - TC-FA-CAT-450
  - TC-FA-CAT-451
coverage:
  web: automated
---

# Tabel Step Category Consolidation: Sort Tiga State Kolom Teks (Category Name, Code, Status, Modified By), Screening Filter Panel, Filter Status dan Modified By, serta Filter Last Updated

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net` pada client CatPostT0 (Pre-setup #33), password dari `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite. Tidak ada ganti akun di tengah spec.
- Env var `FA_TC_PASSWORD` didaftarkan di `executionConfig.environmentVariables` dan `.env.example` (nama usulan, lihat Temuan untuk QA).
- Data Pre-setup #33 (CatPostT0, Starter cap 5, T-0 sudah lewat, belum pernah submit selection) hanya dibaca: 8 kategori root `Alpha Tech`, `Beta Tools`, `Gamma Parts`, `Delta Supply`, `Epsilon Gear`, `Zeta Vehicle`, `Eta Furniture`, `Theta Heavy`, dengan Modified By bergantian `Jane Smith`, `Alex Brown`, dan `System`. Kebutuhan data uji: sedikitnya dua nilai distinct pada kolom Status, Code, dan Modified By (langkah 2 sampai 7) dan sedikitnya satu baris berstatus `Usable` ber-Modified By `System` (langkah 17 sampai 22); status tiap baris tidak tertulis di Pre-setup #33 dan disediakan tim FE/BE lewat seed (lihat Temuan untuk QA).
- Kolom yang diuji pada langkah 2 sampai 7 (langkah diulang untuk setiap baris tabel):

  | Kolom | Urutan Ascending (↑) |
  |---|---|
  | Category Name | alfabet A-Z case-insensitive |
  | Code | alfabet A-Z case-insensitive |
  | Status | alfabet berdasarkan label |
  | Modified By | alfabet nama lengkap underlying |

- Seed dan pemulihan client Pre-setup mengikuti butir "Seed dan pemulihan lewat API" di `suite.md`; flag Guided Tooltip mengikuti hook suite.
- Fixture `fixtures/settings-categories.json` disediakan tim FE.

## Test Steps

1. Klik `[Choose Categories]` pada Alert Category Consolidation

### TC-FA-CAT-446: Sort 3-state tabel Step kolom Category Name, Code, Status, Modified By (untuk setiap kolom pada tabel Kolom yang diuji, langkah 2 sampai 7)

2. Klik header kolom satu kali
3. Verifikasi Ascending (↑) dengan urutan kolom sesuai tabel
4. Klik header kolom kedua kali
5. Verifikasi Descending (↓) kebalikan penuh dari Ascending
6. Klik header kolom ketiga kali
7. Verifikasi Netral kembali ke default Category Name A-Z

### TC-FA-CAT-449: Screening Filter Panel Step dan filter Depth multi-select

8. Klik icon Filter
9. Verifikasi keempat field tampil dalam satu baris (maksimal 4 field per baris) berurutan Depth, Status, Modified By, Last Updated
10. Verifikasi field Depth berupa multi-select searchable dengan placeholder `All depths`
11. Verifikasi field Status dengan placeholder `All statuses`
12. Verifikasi field Modified By dengan placeholder `All users`
13. Verifikasi field Last Updated berupa date range dengan placeholder `Select date`
14. Buka dropdown Depth
15. Verifikasi opsi Depth di-populate DISTINCT dari baris tabel Step
16. Tutup dropdown Depth dan Filter Panel

### TC-FA-CAT-450: Filter Status dan Modified By pada tabel Step

17. Klik icon Filter, pilih Status `Usable`, lalu klik `[Apply]`
18. Verifikasi tabel Step memuat sedikitnya satu baris
19. Verifikasi setiap baris hasil berstatus badge `Usable`
20. Klik icon Filter, tambah Modified By `System`, lalu klik `[Apply]`
21. Verifikasi tabel Step memuat sedikitnya satu baris
22. Verifikasi setiap baris hasil berstatus badge `Usable` dan ber-Modified By `System` (kombinasi AND)
23. Klik icon Filter, klik `[Clear Field]`, lalu klik `[Apply]`

### TC-FA-CAT-451: Filter Last Updated pada tabel Step

24. Catat tanggal Last Updated pada baris pertama tabel Step
25. Klik icon Filter, pilih rentang Last Updated dari tanggal yang dicatat pada langkah 24 sampai tanggal yang sama, lalu klik `[Apply]`
26. Verifikasi tabel Step memuat sedikitnya satu baris
27. Verifikasi setiap baris hasil ber-Last Updated di dalam rentang (inklusif)

## Notes

- Spec melewati sekitar 35 langkah setelah ekspansi (27 langkah nominal, sort empat kolom diulang: 6 langkah x 4 = 24, total sekitar 45). Alasan: seluruh blok satu kelas fungsional pada tabel Step yang sama, berdiri sendiri, dan langkah sort identik per kolom dengan parameter di tabel `Kolom yang diuji` (bagian 8b butir 7); kegagalan satu blok tidak membuat blok lain kehilangan makna. Langkah yang diulang: 2 sampai 7.
- Langkah penghubung (S-03, S-09): langkah 1, 16 (menutup dropdown dan panel), 23 (membersihkan Filter sebelum TC berikutnya), 24 (mencatat tanggal yang dipakai langkah 25).
- Asersi universal pada langkah 19, 22, dan 27 didahului Verifikasi sedikitnya satu baris (langkah 18, 21, 26) sebagai pembanding (bagian 8b butir 2).
- Temuan untuk QA:
  - Nama env var password aktor tidak tertulis di TC; `FA_TC_PASSWORD` adalah usulan.
  - TC-FA-CAT-449 Expected b menyebut opsi Depth `L1`, `L2` dan "logika OR dalam field", sedangkan Pre-setup #33 hanya berisi kategori root (Depth `L1`); opsi `L2` dan logika OR tidak teramati pada data tertulis, sehingga spec memverifikasi bahwa opsi di-populate distinct dari baris tabel.
  - TC-FA-CAT-450 membutuhkan baris `Usable` ber-Modified By `System`; Pre-setup #33 tidak menyebut status tiap baris maupun hubungan Modified By dengan status.
  - TC-FA-CAT-451 langkah 2 ("Pilih rentang Last Updated") tidak menyebut tanggalnya; spec memakai tanggal sel baris pertama yang dicatat saat spec berjalan.
  - TC-FA-CAT-446 Expected d menyebut urutan Modified By berdasarkan nama lengkap underlying, padahal sel menampilkan `[First Name] [Last Initial]`; spec memverifikasi urutan sesuai tabel `Kolom yang diuji`.
