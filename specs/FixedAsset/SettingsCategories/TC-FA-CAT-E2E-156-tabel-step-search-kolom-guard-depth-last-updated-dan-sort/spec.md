---
id: TC-FA-CAT-E2E-156-tabel-step-search-kolom-guard-depth-last-updated-dan-sort
title: "Tabel Step Category Consolidation: Search pada Kolom yang Dapat Dicari, Guard Depth dan Last Updated, serta Sort Tiga State Last Updated"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CAT-443
  - TC-FA-CAT-444
  - TC-FA-CAT-445
  - TC-FA-CAT-448
coverage:
  web: automated
---

# Tabel Step Category Consolidation: Search pada Kolom yang Dapat Dicari, Guard Depth dan Last Updated, serta Sort Tiga State Last Updated

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net` pada client CatPostT0 (Pre-setup #33), password dari `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite. Tidak ada ganti akun di tengah spec.
- Env var `FA_TC_PASSWORD` didaftarkan di `executionConfig.environmentVariables` dan `.env.example` (nama usulan, lihat Temuan untuk QA).
- Data Pre-setup #33 (CatPostT0, Starter cap 5, T-0 sudah lewat, belum pernah submit selection) hanya dibaca: 8 kategori root `Alpha Tech` (Code `AT`), `Beta Tools`, `Gamma Parts`, `Delta Supply`, `Epsilon Gear`, `Zeta Vehicle`, `Eta Furniture`, `Theta Heavy`, dengan Modified By bergantian `Jane Smith`, `Alex Brown`, dan `System`. Kebutuhan data uji: sedikitnya satu baris berstatus `Excess` dan satu `Usable` (langkah 13 sampai 16) serta sedikitnya dua nilai Last Updated yang berbeda pada format yang ditampilkan (langkah 24 sampai 29); keduanya tidak tertulis di Pre-setup #33 dan disediakan tim FE/BE lewat seed (lihat Temuan untuk QA).
- Seed dan pemulihan client Pre-setup mengikuti butir "Seed dan pemulihan lewat API" di `suite.md`; flag Guided Tooltip mengikuti hook suite.
- Fixture `fixtures/settings-categories.json` disediakan tim FE.

## Test Steps

1. Klik `[Choose Categories]` pada Alert Category Consolidation

### TC-FA-CAT-443: Search Step pada Category Name, Code, dan Modified By

2. Ketik Search `alpha`, tekan Enter
3. Verifikasi tabel Step hanya memuat `Alpha Tech` (cocok pada Category Name, case-insensitive)
4. Ganti isi kotak search dengan `AT`, tekan Enter
5. Verifikasi tabel Step memuat `Alpha Tech` (cocok pada Code)
6. Ganti isi kotak search dengan `jane`, tekan Enter
7. Verifikasi tabel Step memuat sedikitnya satu baris
8. Verifikasi setiap baris hasil ber-Modified By `Jane S` (cocok pada Modified By)
9. Klik icon panah (←) di kiri toolbar untuk menutup kotak Search

### TC-FA-CAT-444: Search Step pada Total Asset dan Status

10. Ketik Search `0`, tekan Enter
11. Verifikasi tabel Step memuat sedikitnya satu baris
12. Verifikasi setiap baris hasil ber-Total Asset yang mengandung angka `0`
13. Ganti isi kotak search dengan `excess`, tekan Enter
14. Verifikasi tabel Step memuat sedikitnya satu baris
15. Verifikasi setiap baris hasil berstatus `Excess`
16. Verifikasi tidak ada baris berstatus `Usable` pada hasil
17. Klik icon panah (←) di kiri toolbar untuk menutup kotak Search

### TC-FA-CAT-445: Guard, Depth dan Last Updated tidak dapat dicari lewat Search Step

18. Catat nilai tanggal Last Updated pada baris pertama tabel Step
19. Ketik Search `L1`, tekan Enter
20. Verifikasi empty state `No results found` dengan deskripsi `Try adjusting your search or filter.` tampil
21. Ganti isi kotak search dengan nilai tanggal Last Updated yang dicatat pada langkah 18, tekan Enter
22. Verifikasi empty state `No results found` dengan deskripsi `Try adjusting your search or filter.` tampil
23. Klik icon panah (←) di kiri toolbar untuk menutup kotak Search

### TC-FA-CAT-448: Sort 3-state tabel Step kolom Last Updated

24. Klik header Last Updated satu kali
25. Verifikasi Ascending (↑): Oldest First, tanggal terlama di atas
26. Klik header Last Updated kedua kali
27. Verifikasi Descending (↓): Newest First, kebalikan penuh dari Ascending
28. Klik header Last Updated ketiga kali
29. Verifikasi Netral: tabel kembali ke default Category Name A-Z

## Notes

- Langkah penghubung (S-03, S-09, R-16): langkah 9, 17, 23 (menutup kotak Search dan mereset tabel), langkah 18 (mencatat nilai tanggal yang dipakai langkah 21).
- Asersi hasil Search yang universal ("setiap baris", "tidak ada baris berstatus `Usable`") didahului Verifikasi sedikitnya satu baris (langkah 7, 11, 14) sebagai pembanding (bagian 8b butir 2).
- Empty state pada langkah 20 dan 22 memakai teks `No results found` / `Try adjusting your search or filter.` dari TC-FA-CAT-596 Expected a (tabel Step yang sama); Expected TC-FA-CAT-445 hanya menyebut "Tidak ada hasil". Empty state menjadi anchor positif untuk absence hasil (bagian 8b butir 2).
- Langkah 3 memverifikasi hasil hanya `Alpha Tech`, selaras dengan TC-FA-CAT-595 Expected c pada tabel yang sama.
- Search `AT` pada langkah 4 memakai pola atomik "ketik Search, tekan Enter" (bagian 8b butir 9); TC-FA-CAT-443 langkah 3 tidak menyebut Enter.
- Temuan untuk QA:
  - Nama env var password aktor tidak tertulis di TC; `FA_TC_PASSWORD` adalah usulan.
  - TC-FA-CAT-443 langkah 3 ("Search kode kategori `AT` ... pada Code") tidak menyebut Enter dan mencampur nama kolom dengan nilai; spec menulis Search `AT` + Enter.
  - TC-FA-CAT-443 Expected hanya menyebut "mencocokkan substring case-insensitive" tanpa baris spesifik; spec memverifikasi `Alpha Tech` untuk `alpha` dan `AT` (nilai dari Pre-setup #33) dan Modified By `Jane S` untuk `jane` (format `[First Name] [Last Initial]`).
  - TC-FA-CAT-444 membutuhkan baris `Excess` dan `Usable` sekaligus pada Pre-setup #33 yang tidak menyebut status tiap baris.
  - TC-FA-CAT-445 langkah 3 menyebut "nilai tanggal Last Updated" tanpa nilai; spec memakai nilai sel baris pertama yang dicatat saat spec berjalan.
  - TC-FA-CAT-448 membutuhkan dua nilai Last Updated berbeda; Pre-setup #33 tidak menyebut waktu pembuatan tiap kategori.
