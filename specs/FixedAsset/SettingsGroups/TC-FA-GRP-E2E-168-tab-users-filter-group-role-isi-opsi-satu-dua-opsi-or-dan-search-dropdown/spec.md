---
id: TC-FA-GRP-E2E-168-tab-users-filter-group-role-isi-opsi-satu-dua-opsi-or-dan-search-dropdown
title: "Tab Users Filter Group Role: Isi Opsi, Satu/Dua Opsi (OR), dan Search Dropdown"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-GRP-598
  - TC-FA-GRP-599
  - TC-FA-GRP-600
  - TC-FA-GRP-601
coverage:
  web: automated
---

# Tab Users Filter Group Role: Isi Opsi, Satu/Dua Opsi (OR), dan Search Dropdown

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Pre-setup No 1 `totalControlGroups_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD` (nama env baru; didaftarkan di `executionConfig.environmentVariables` dan `.env.example`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Hook suite (flag Guided Tooltip, sesi API aktor, fixture BE, pemulihan state global): lihat `suite.md`. Suite berjalan serial (`parallel: false`).
- Data Pre-setup: Warehouse A (Pre-setup No 9) dibaca dan tidak diubah; memuat >= 12 user dengan variasi role. Tabel Data Uji variasi baris tidak punya tabel konkret di TC (lihat Temuan untuk QA); asersi Search, Filter, dan Sort memakai data dengan sedikitnya dua nilai distinct pada kolom yang diasersi.
- Opsi A dan opsi B: dua nilai distinct dari kolom yang difilter pada tabel Warehouse A (diambil dari data tabel saat spec berjalan).
- Warehouse A memuat user ber-Group Role bervariasi (Total Control, Read Only, Group Manager, dan nama Group Role biasa) termasuk user dengan sel `[N] roles`.

## Test Steps

1. Ketik Search `Warehouse A`, tekan Enter, lalu klik angka Total User Warehouse A
2. Telusuri semua halaman tabel dari halaman 1 sampai halaman terakhir, lalu catat himpunan nilai Group Role distinct pada sel tunggal baris tabel (tanpa nilai `—` dan tanpa sel `[N] roles`)
3. Kembali ke halaman 1 pagination tabel
4. Klik icon Filter

### TC-598: Isi opsi Filter Group Role

5. Buka dropdown Group Role
6. Verifikasi opsi memuat seluruh nilai Group Role yang dicatat pada langkah 2
7. Verifikasi opsi dapat dicentang lebih dari satu (multi-select)
8. Verifikasi ada kotak search internal
9. Verifikasi opsi memuat Total Control, Read Only, Group Manager, dan nama Group Role yang dipegang user di tabel, termasuk role milik user bersel `[N] roles`
10. Verifikasi tidak ada opsi `—`
11. Tutup dropdown

### TC-599: Satu opsi

12. Buka dropdown Group Role
13. Pilih 1 opsi pada Group Role
14. Klik [Apply]
15. Verifikasi sedikitnya satu baris tampil pada tabel
16. Verifikasi hanya baris dengan Group Role = opsi terpilih yang tampil
17. Verifikasi indikator filter aktif tampil pada icon Filter
18. Verifikasi untuk opsi nama role, user yang memegang role itu tampil walau selnya `[N] roles`
19. Buka Filter, klik [Clear Field], klik [Apply]
20. Klik icon Filter

### TC-600: Dua opsi (OR)

21. Buka dropdown Group Role
22. Centang 2 opsi berbeda pada Group Role
23. Klik [Apply]
24. Verifikasi sedikitnya satu baris tampil pada tabel
25. Verifikasi baris dengan Group Role = opsi 1 atau opsi 2 tampil (OR di dalam field)
26. Verifikasi baris dengan nilai lain tidak tampil
27. Buka Filter, klik [Clear Field], klik [Apply]
28. Klik icon Filter

### TC-601: Search internal dropdown

29. Buka dropdown Group Role
30. Ketik potongan nama opsi huruf kecil di kotak search dropdown
31. Verifikasi daftar opsi menyempit ke opsi yang mengandung substring (case-insensitive)
32. Ganti isi kotak search dropdown dengan teks yang tidak ada di opsi mana pun
33. Verifikasi daftar opsi kosong dengan teks "No results found" (teks saja, tanpa ilustrasi)
34. Tutup dropdown
35. Tutup Filter Panel

## Notes

- Langkah penghubung (aksi tanpa `Verifikasi`, S-03): menutup dropdown, membuka Filter, dan `Buka Filter, klik [Clear Field], klik [Apply]` antar TC (S-09); menutup Filter Panel di akhir spec.
- Himpunan nilai Group Role distinct dicatat dengan menelusuri seluruh halaman tabel, karena Warehouse A memuat >= 12 user dengan page size 10 sehingga halaman 1 saja tidak mewakili himpunan (S-12, S-14).
- Asersi tambahan (S-03, 8b.2): `Verifikasi sedikitnya satu baris tampil pada tabel` ditambahkan sebelum asersi hasil Search atau Filter yang bersifat universal ("hanya baris ...", "nilai lain tidak tampil") agar asersi tidak vacuous; bukan klausa Expected TC.
- Baris `Warehouse A` dicari lewat Search sebelum klik angka Total User (client memiliki lebih dari 10 node level 1 dan page size 10, sehingga posisi baris di halaman 1 tidak diandalkan; Refresh F5 membuang Search sehingga Search diketik ulang). Langkah Search digabung ke langkah klik angka dan dihitung langkah penghubung (S-03, S-14, R-16).
- Temuan untuk QA:
  - Sel Group Role bernilai `[N] roles` tidak menampilkan nama role-nya pada tabel, sehingga himpunan lengkap opsi Group Role tidak dapat diturunkan dari baris tabel. Spec membandingkan opsi sebagai superset dari nilai sel tunggal yang dicatat (langkah 2) dan memeriksa role milik user bersel `[N] roles` terpisah; TC perlu menyediakan daftar role Warehouse A bila kesamaan penuh dibutuhkan.
  - Tabel Data Uji untuk variasi baris Tab Users tidak punya tabel konkret di TC (hanya `>= 12 user variasi role`); spec mendefinisikan kebutuhan nilai distinct di Prerequisites.
