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
- Data Pre-setup: Warehouse A (Pre-setup No 9) dibaca dan tidak diubah; memuat >= 12 user dengan variasi role, dan client punya Custom Field aktif Phone (Data Dinamis, dibaca saja). Tabel Data Uji variasi baris tidak punya tabel konkret di TC (lihat Temuan untuk QA); asersi Search, Filter, dan Sort memakai data dengan sedikitnya dua nilai distinct pada kolom yang diasersi.
- Opsi A dan opsi B: dua nilai distinct dari kolom yang difilter pada tabel Warehouse A (diambil dari data tabel saat spec berjalan).
- Warehouse A memuat user ber-Group Role bervariasi (Total Control, Read Only, Group Manager, dan nama Group Role biasa) termasuk user dengan sel `[N] roles`.

## Test Steps

1. Klik angka Total User Warehouse A
2. Klik icon Filter

### TC-598: Isi opsi Filter Group Role

3. Buka dropdown Group Role
4. Verifikasi opsi = nilai Group Role distinct yang ada di baris tabel ini saat ini, tidak termasuk nilai yang tidak dipakai baris mana pun
5. Verifikasi opsi dapat dicentang lebih dari satu (multi-select)
6. Verifikasi ada kotak search internal
7. Verifikasi opsi memuat Total Control, Read Only, Group Manager, dan nama Group Role yang dipegang user di tabel, termasuk role milik user bersel `[N] roles`
8. Verifikasi tidak ada opsi `—`
9. Tutup dropdown

### TC-599: Satu opsi

10. Buka dropdown Group Role
11. Pilih 1 opsi pada Group Role
12. Klik [Apply]
13. Verifikasi sedikitnya satu baris tampil pada tabel
14. Verifikasi hanya baris dengan Group Role = opsi terpilih yang tampil
15. Verifikasi indikator filter aktif tampil pada icon Filter
16. Verifikasi untuk opsi nama role, user yang memegang role itu tampil walau selnya `[N] roles`
17. Buka Filter, klik [Clear Field], klik [Apply]
18. Klik icon Filter

### TC-600: Dua opsi (OR)

19. Buka dropdown Group Role
20. Centang 2 opsi berbeda pada Group Role
21. Klik [Apply]
22. Verifikasi sedikitnya satu baris tampil pada tabel
23. Verifikasi baris dengan Group Role = opsi 1 atau opsi 2 tampil (OR di dalam field)
24. Verifikasi baris dengan nilai lain tidak tampil
25. Buka Filter, klik [Clear Field], klik [Apply]
26. Klik icon Filter

### TC-601: Search internal dropdown

27. Buka dropdown Group Role
28. Ketik potongan nama opsi huruf kecil di kotak search dropdown
29. Verifikasi daftar opsi menyempit ke opsi yang mengandung substring (case-insensitive)
30. Ganti isi kotak search dropdown dengan teks yang tidak ada di opsi mana pun
31. Verifikasi daftar opsi kosong dengan teks "No results found" (teks saja, tanpa ilustrasi)
32. Tutup dropdown
33. Tutup Filter Panel

## Notes

- Langkah penghubung (aksi tanpa `Verifikasi`, S-03): menutup dropdown, membuka Filter, dan `Buka Filter, klik [Clear Field], klik [Apply]` antar TC (S-09); menutup Filter Panel di akhir spec.
- Asersi tambahan (S-03, 8b.2): `Verifikasi sedikitnya satu baris tampil pada tabel` ditambahkan sebelum asersi hasil Search atau Filter yang bersifat universal ("hanya baris ...", "nilai lain tidak tampil") agar asersi tidak vacuous; bukan klausa Expected TC.
- Temuan untuk QA:
  - Tabel Data Uji untuk variasi baris Tab Users tidak punya tabel konkret di TC (hanya `>= 12 user variasi role`); spec mendefinisikan kebutuhan nilai distinct di Prerequisites.
