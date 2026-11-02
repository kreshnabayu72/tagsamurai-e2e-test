---
id: TC-FA-GRP-E2E-165-tab-users-filter-panel-screening-dan-filter-position-opsi-or-search-dropdown
title: "Tab Users Filter: Screening Panel dan Filter Position (Isi Opsi, Satu/Dua Opsi OR, Search Dropdown)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-GRP-585
  - TC-FA-GRP-586
  - TC-FA-GRP-587
  - TC-FA-GRP-588
  - TC-FA-GRP-589
coverage:
  web: automated
---

# Tab Users Filter: Screening Panel dan Filter Position (Isi Opsi, Satu/Dua Opsi OR, Search Dropdown)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Pre-setup No 1 `totalControlGroups_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD` (nama env baru; didaftarkan di `executionConfig.environmentVariables` dan `.env.example`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Hook suite (flag Guided Tooltip, sesi API aktor, fixture BE, pemulihan state global): lihat `suite.md`. Suite berjalan serial (`parallel: false`).
- Data Pre-setup: Warehouse A (Pre-setup No 9) dibaca dan tidak diubah; memuat >= 12 user dengan variasi role, dan client punya Custom Field aktif Phone (Data Dinamis, dibaca saja). Tabel Data Uji variasi baris tidak punya tabel konkret di TC (lihat Temuan untuk QA); asersi Search, Filter, dan Sort memakai data dengan sedikitnya dua nilai distinct pada kolom yang diasersi.
- Opsi A dan opsi B: dua nilai distinct dari kolom yang difilter pada tabel Warehouse A (diambil dari data tabel saat spec berjalan).

## Test Steps

1. Klik angka Total User Warehouse A
2. Klik icon Filter

### TC-585: Screening Filter Panel

3. Verifikasi Filter Panel terbuka berisi field berurutan: Position (dropdown multi-select searchable, placeholder `All positions`), Division (dropdown multi-select searchable, placeholder `All divisions`), Group Role (dropdown multi-select searchable, placeholder `All group roles`), Activation Status (dropdown multi-select searchable, placeholder `All statuses`), Temporary User (dropdown multi-select searchable, placeholder `All options`), Temporary Until (date range picker, placeholder `Select date`), dan Custom Field aktif bertipe Dropdown, Multi-Dropdown, atau Date (placeholder `All [plural noun]`)
4. Verifikasi Custom Field bertipe lain seperti Phone tidak punya field filter
5. Verifikasi tombol footer [Clear Field] dan [Apply] tampil
6. Verifikasi tidak ada field filter lain di luar daftar Setup Column

### TC-586: Isi opsi Filter Position

7. Buka dropdown Position
8. Verifikasi opsi = nilai Position distinct yang ada di baris tabel ini saat ini, tidak termasuk nilai yang tidak dipakai baris mana pun
9. Verifikasi opsi dapat dicentang lebih dari satu (multi-select)
10. Verifikasi ada kotak search internal
11. Tutup dropdown

### TC-587: Satu opsi

12. Buka dropdown Position
13. Pilih 1 opsi pada Position
14. Klik [Apply]
15. Verifikasi sedikitnya satu baris tampil pada tabel
16. Verifikasi hanya baris dengan Position = opsi terpilih yang tampil
17. Verifikasi indikator filter aktif tampil pada icon Filter
18. Buka Filter, klik [Clear Field], klik [Apply]
19. Klik icon Filter

### TC-588: Dua opsi (OR)

20. Buka dropdown Position
21. Centang 2 opsi berbeda pada Position
22. Klik [Apply]
23. Verifikasi sedikitnya satu baris tampil pada tabel
24. Verifikasi baris dengan Position = opsi 1 atau opsi 2 tampil (OR di dalam field)
25. Verifikasi baris dengan nilai lain tidak tampil
26. Buka Filter, klik [Clear Field], klik [Apply]
27. Klik icon Filter

### TC-589: Search internal dropdown

28. Buka dropdown Position
29. Ketik potongan nama opsi huruf kecil di kotak search dropdown
30. Verifikasi daftar opsi menyempit ke opsi yang mengandung substring (case-insensitive)
31. Ganti isi kotak search dropdown dengan teks yang tidak ada di opsi mana pun
32. Verifikasi daftar opsi kosong dengan teks "No results found" (teks saja, tanpa ilustrasi)
33. Tutup dropdown
34. Tutup Filter Panel

## Notes

- Langkah penghubung (aksi tanpa `Verifikasi`, S-03): menutup dropdown, membuka Filter, dan `Buka Filter, klik [Clear Field], klik [Apply]` sebelum TC berikutnya agar saringan sebelumnya tidak terbawa (S-09); menutup Filter Panel di akhir spec.
- Asersi tambahan (S-03, 8b.2): `Verifikasi sedikitnya satu baris tampil pada tabel` ditambahkan sebelum asersi hasil Search atau Filter yang bersifat universal ("hanya baris ...", "nilai lain tidak tampil") agar asersi tidak vacuous; bukan klausa Expected TC.
- Temuan untuk QA:
  - Tabel Data Uji untuk variasi baris Tab Users tidak punya tabel konkret di TC (hanya `>= 12 user variasi role`); spec mendefinisikan kebutuhan nilai distinct di Prerequisites.
  - TC-585 Expected a menyebut daftar field, placeholder, dan tipe kontrol dalam satu butir; spec memverifikasinya sebagai satu daftar utuh (S-01).
  - TC-587 tidak menyebut cara memilih opsi A/B; spec memakai dua nilai distinct dari kolom Position (Prerequisites).
