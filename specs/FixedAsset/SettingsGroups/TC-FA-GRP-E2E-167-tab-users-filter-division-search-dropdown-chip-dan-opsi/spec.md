---
id: TC-FA-GRP-E2E-167-tab-users-filter-division-search-dropdown-chip-dan-opsi
title: "Tab Users Filter Division: Dua Opsi OR, Search Dropdown, dan Chip Opsi"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-GRP-594
  - TC-FA-GRP-595
  - TC-FA-GRP-596
  - TC-FA-GRP-597
coverage:
  web: automated
---

# Tab Users Filter Division: Dua Opsi OR, Search Dropdown, dan Chip Opsi

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Pre-setup No 1 `totalControlGroups_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD` (nama env baru; didaftarkan di `executionConfig.environmentVariables` dan `.env.example`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Hook suite (flag Guided Tooltip, sesi API aktor, fixture BE, pemulihan state global): lihat `suite.md`. Suite berjalan serial (`parallel: false`).
- Data Pre-setup: Warehouse A (Pre-setup No 9) dibaca dan tidak diubah; memuat >= 12 user dengan variasi role, dan client punya Custom Field aktif Phone (Data Dinamis, dibaca saja). Tabel Data Uji variasi baris tidak punya tabel konkret di TC (lihat Temuan untuk QA); asersi Search, Filter, dan Sort memakai data dengan sedikitnya dua nilai distinct pada kolom yang diasersi.
- Opsi A dan opsi B: dua nilai distinct dari kolom yang difilter pada tabel Warehouse A (diambil dari data tabel saat spec berjalan).

## Test Steps

1. Klik angka Total User Warehouse A
2. Klik icon Filter

### TC-594: Dua opsi (OR)

3. Buka dropdown Division
4. Centang 2 opsi berbeda pada Division
5. Klik [Apply]
6. Verifikasi baris dengan Division = opsi 1 atau opsi 2 tampil (OR di dalam field)
7. Verifikasi baris dengan nilai lain tidak tampil
8. Buka Filter, klik [Clear Field], klik [Apply]
9. Klik icon Filter

### TC-595: Search internal dropdown

10. Buka dropdown Division
11. Ketik potongan nama opsi huruf kecil di kotak search dropdown
12. Verifikasi daftar opsi menyempit ke opsi yang mengandung substring (case-insensitive)
13. Ganti isi kotak search dropdown dengan teks yang tidak ada di opsi mana pun
14. Verifikasi daftar opsi kosong dengan teks "No results found" (teks saja, tanpa ilustrasi)
15. Tutup dropdown

### TC-596: Chip Division dihapus via (X)

16. Buka dropdown Division
17. Centang opsi A lalu opsi B pada Division
18. Tutup dropdown
19. Verifikasi chip A dan chip B tampil di dalam field (chip B tidak menggantikan chip A)
20. Klik (X) pada chip opsi A
21. Verifikasi chip A hilang
22. Buka dropdown Division
23. Verifikasi checkbox A di dropdown ikut ter-uncheck
24. Tutup dropdown
25. Verifikasi chip B tetap ada
26. Klik [Apply]
27. Verifikasi tabel hanya menyaring Division = opsi B
28. Buka Filter, klik [Clear Field], klik [Apply]
29. Klik icon Filter

### TC-597: Chip Division dihapus via uncheck

30. Buka dropdown Division
31. Centang opsi A lalu opsi B pada Division
32. Buka lagi dropdown dan uncheck opsi A dari dalam dropdown
33. Verifikasi chip A hilang dari field
34. Verifikasi chip B tetap ada
35. Klik [Apply]
36. Verifikasi tabel hanya menyaring Division = opsi B
37. Buka Filter, klik [Clear Field], klik [Apply]

## Notes

- Langkah penghubung (aksi tanpa `Verifikasi`, S-03): menutup dropdown, membuka dropdown untuk memeriksa checkbox opsi A pada TC-596, serta `Buka Filter, klik [Clear Field], klik [Apply]` antar TC (S-09).
- Spec memiliki 37 langkah, di atas smell 35 langkah. Alasan: seluruh blok satu topik (Filter Division Tab Users pada dataset yang sama), tiap TC berdiri sendiri, dan TC-596 memuat 12 langkah karena Expected b memeriksa chip dan checkbox.
- Temuan untuk QA:
  - Tabel Data Uji untuk variasi baris Tab Users tidak punya tabel konkret di TC (hanya `>= 12 user variasi role`); spec mendefinisikan kebutuhan nilai distinct di Prerequisites.
