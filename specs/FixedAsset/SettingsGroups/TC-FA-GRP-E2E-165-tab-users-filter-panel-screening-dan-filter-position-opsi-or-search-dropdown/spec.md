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
- Data Pre-setup: Warehouse A (Pre-setup No 9) dibaca dan tidak diubah; memuat >= 12 user dengan variasi role, dan Custom Field User `Phone {runId}` di-seed per spec lewat sesi API aktor di `before` dan dihapus di `after` (Data Dinamis, disediakan tim FE/BE). Tabel Data Uji variasi baris tidak punya tabel konkret di TC (lihat Temuan untuk QA); asersi Search, Filter, dan Sort memakai data dengan sedikitnya dua nilai distinct pada kolom yang diasersi.
- Opsi A dan opsi B: dua nilai distinct dari kolom yang difilter pada tabel Warehouse A (diambil dari data tabel saat spec berjalan).

## Test Steps

1. Ketik Search `Warehouse A`, tekan Enter, lalu klik angka Total User Warehouse A
2. Telusuri semua halaman tabel dari halaman 1 sampai halaman terakhir, lalu catat himpunan nilai Position distinct pada baris tabel (tanpa nilai `—`)
3. Kembali ke halaman 1 pagination tabel
4. Klik icon Filter

### TC-585: Screening Filter Panel

5. Verifikasi Filter Panel terbuka berisi field berurutan: Position (dropdown multi-select searchable, placeholder `All positions`), Division (dropdown multi-select searchable, placeholder `All divisions`), Group Role (dropdown multi-select searchable, placeholder `All group roles`), Activation Status (dropdown multi-select searchable, placeholder `All statuses`), Temporary User (dropdown multi-select searchable, placeholder `All options`), Temporary Until (date range picker, placeholder `Select date`), dan Custom Field aktif bertipe Dropdown, Multi-Dropdown, atau Date (placeholder `All [plural noun]`)
6. Verifikasi Custom Field `Phone {runId}` (bukan tipe Dropdown, Multi-Dropdown, atau Date) tidak punya field filter
7. Verifikasi tombol footer [Clear Field] dan [Apply] tampil
8. Verifikasi tidak ada field filter lain di luar daftar Setup Column

### TC-586: Isi opsi Filter Position

9. Buka dropdown Position
10. Verifikasi opsi = himpunan nilai Position distinct yang dicatat pada langkah 2, tidak termasuk nilai yang tidak dipakai baris mana pun
11. Verifikasi opsi dapat dicentang lebih dari satu (multi-select)
12. Verifikasi ada kotak search internal
13. Tutup dropdown

### TC-587: Satu opsi

14. Buka dropdown Position
15. Pilih 1 opsi pada Position
16. Klik [Apply]
17. Verifikasi sedikitnya satu baris tampil pada tabel
18. Verifikasi hanya baris dengan Position = opsi terpilih yang tampil
19. Verifikasi indikator filter aktif tampil pada icon Filter
20. Buka Filter, klik [Clear Field], klik [Apply]
21. Klik icon Filter

### TC-588: Dua opsi (OR)

22. Buka dropdown Position
23. Centang 2 opsi berbeda pada Position
24. Klik [Apply]
25. Verifikasi sedikitnya satu baris tampil pada tabel
26. Verifikasi baris dengan Position = opsi 1 atau opsi 2 tampil (OR di dalam field)
27. Verifikasi baris dengan nilai lain tidak tampil
28. Buka Filter, klik [Clear Field], klik [Apply]
29. Klik icon Filter

### TC-589: Search internal dropdown

30. Buka dropdown Position
31. Ketik potongan nama opsi huruf kecil di kotak search dropdown
32. Verifikasi daftar opsi menyempit ke opsi yang mengandung substring (case-insensitive)
33. Ganti isi kotak search dropdown dengan teks yang tidak ada di opsi mana pun
34. Verifikasi daftar opsi kosong dengan teks "No results found" (teks saja, tanpa ilustrasi)
35. Tutup dropdown
36. Tutup Filter Panel

## Notes

- Langkah penghubung (aksi tanpa `Verifikasi`, S-03): menutup dropdown, membuka Filter, dan `Buka Filter, klik [Clear Field], klik [Apply]` sebelum TC berikutnya agar saringan sebelumnya tidak terbawa (S-09); menutup Filter Panel di akhir spec.
- Himpunan nilai Position distinct dicatat dengan menelusuri seluruh halaman tabel, karena Warehouse A memuat >= 12 user dengan page size 10 sehingga halaman 1 saja tidak mewakili himpunan (S-12, S-14).
- Spec memiliki 36 langkah, di atas smell 35 langkah. Alasan: seluruh blok satu topik (screening dan Filter Position Tab Users pada dataset yang sama), tiap TC berdiri sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna, dan dua langkah tambahan menelusuri halaman untuk baseline himpunan Position.
- Asersi tambahan (S-03, 8b.2): `Verifikasi sedikitnya satu baris tampil pada tabel` ditambahkan sebelum asersi hasil Search atau Filter yang bersifat universal ("hanya baris ...", "nilai lain tidak tampil") agar asersi tidak vacuous; bukan klausa Expected TC.
- Baris `Warehouse A` dicari lewat Search sebelum klik angka Total User (client memiliki lebih dari 10 node level 1 dan page size 10, sehingga posisi baris di halaman 1 tidak diandalkan; Refresh F5 membuang Search sehingga Search diketik ulang). Langkah Search digabung ke langkah klik angka dan dihitung langkah penghubung (S-03, S-14, R-16).
- Temuan untuk QA:
  - Tabel Data Uji untuk variasi baris Tab Users tidak punya tabel konkret di TC (hanya `>= 12 user variasi role`); spec mendefinisikan kebutuhan nilai distinct di Prerequisites.
  - TC-585 Expected a menyebut daftar field, placeholder, dan tipe kontrol dalam satu butir; spec memverifikasinya sebagai satu daftar utuh (S-01).
  - TC-587 tidak menyebut cara memilih opsi A/B; spec memakai dua nilai distinct dari kolom Position (Prerequisites).
