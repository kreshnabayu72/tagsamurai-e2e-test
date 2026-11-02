---
id: TC-FA-GRP-E2E-169-tab-users-filter-group-role-chip-opsi-dan-activation-status
title: "Tab Users Filter: Chip Opsi Group Role dan Filter Activation Status"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-GRP-602
  - TC-FA-GRP-603
  - TC-FA-GRP-1012
coverage:
  web: automated
---

# Tab Users Filter: Chip Opsi Group Role dan Filter Activation Status

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Pre-setup No 1 `totalControlGroups_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD` (nama env baru; didaftarkan di `executionConfig.environmentVariables` dan `.env.example`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Hook suite (flag Guided Tooltip, sesi API aktor, fixture BE, pemulihan state global): lihat `suite.md`. Suite berjalan serial (`parallel: false`).
- Data Pre-setup: Warehouse A (Pre-setup No 9) dibaca dan tidak diubah; memuat >= 12 user dengan variasi role, dan client punya Custom Field aktif Phone (Data Dinamis, dibaca saja). Tabel Data Uji variasi baris tidak punya tabel konkret di TC (lihat Temuan untuk QA); asersi Search, Filter, dan Sort memakai data dengan sedikitnya dua nilai distinct pada kolom yang diasersi.
- Opsi A dan opsi B: dua nilai distinct dari kolom yang difilter pada tabel Warehouse A (diambil dari data tabel saat spec berjalan).
- Warehouse A memuat user ber-Activation Status `Activated` dan `Pending Activation`. Spec ini tidak memakai Custom Field.

## Test Steps

1. Klik angka Total User Warehouse A
2. Klik icon Filter

### TC-602: Chip Group Role dihapus via (X)

3. Buka dropdown Group Role
4. Centang opsi A lalu opsi B pada Group Role
5. Tutup dropdown
6. Verifikasi chip A dan chip B tampil di dalam field (chip B tidak menggantikan chip A)
7. Klik (X) pada chip opsi A
8. Verifikasi chip A hilang
9. Buka dropdown Group Role
10. Verifikasi checkbox A di dropdown ikut ter-uncheck
11. Tutup dropdown
12. Verifikasi chip B tetap ada
13. Klik [Apply]
14. Verifikasi sedikitnya satu baris tampil pada tabel
15. Verifikasi tabel hanya menyaring Group Role = opsi B
16. Buka Filter, klik [Clear Field], klik [Apply]
17. Klik icon Filter

### TC-603: Chip Group Role dihapus via uncheck

18. Buka dropdown Group Role
19. Centang opsi A lalu opsi B pada Group Role
20. Buka lagi dropdown dan uncheck opsi A dari dalam dropdown
21. Verifikasi chip A hilang dari field
22. Verifikasi chip B tetap ada
23. Klik [Apply]
24. Verifikasi sedikitnya satu baris tampil pada tabel
25. Verifikasi tabel hanya menyaring Group Role = opsi B
26. Buka Filter, klik [Clear Field], klik [Apply]
27. Klik icon Filter

### TC-1012: Filter Activation Status

28. Tampilkan kolom Activation Status via Column Visibility
29. Klik icon Filter
30. Buka dropdown Activation Status
31. Verifikasi placeholder field `All statuses`
32. Verifikasi opsi = nilai Activation Status distinct yang ada di baris tabel (Activated dan Pending Activation)
33. Pilih 1 opsi, klik [Apply]
34. Verifikasi sedikitnya satu baris tampil pada tabel
35. Verifikasi hanya baris dengan Activation Status terpilih yang tampil
36. Buka Filter, klik [Clear Field], klik [Apply]
37. Sembunyikan kolom Activation Status via Column Visibility
38. Buka Filter, pilih 1 opsi pada Activation Status, klik [Apply]
39. Verifikasi sedikitnya satu baris tampil pada tabel
40. Verifikasi filter bekerja walau kolom Activation Status sedang tidak tampil (Hidden)
41. Buka Filter, klik [Clear Field], klik [Apply]

## Notes

- Langkah penghubung (aksi tanpa `Verifikasi`, S-03): menutup dropdown, membuka dropdown untuk memeriksa checkbox opsi A pada TC-602, `Buka Filter, klik [Clear Field], klik [Apply]` antar TC (S-09), dan menyembunyikan kolom Activation Status lewat Column Visibility pada TC-1012 (Expected c; kolom curated tidak tampil default sehingga langkah ini hanya memastikan keadaan Hidden).
- Spec memiliki 41 langkah, di atas smell 35 langkah. Alasan: seluruh blok satu topik (Filter Tab Users pada dataset yang sama), tiap TC berdiri sendiri, dan TC-602 memuat 15 langkah karena Expected b memeriksa chip dan checkbox.
- Asersi tambahan (S-03, 8b.2): `Verifikasi sedikitnya satu baris tampil pada tabel` ditambahkan sebelum asersi hasil Search atau Filter yang bersifat universal ("hanya baris ...", "nilai lain tidak tampil") agar asersi tidak vacuous; bukan klausa Expected TC.
- Temuan untuk QA:
  - Tabel Data Uji untuk variasi baris Tab Users tidak punya tabel konkret di TC (hanya `>= 12 user variasi role`); spec mendefinisikan kebutuhan nilai distinct di Prerequisites.
  - TC-1012 Expected c (filter bekerja saat kolom Hidden) tidak menyebut langkah menyembunyikan kolom; kolom Activation Status curated tidak tampil secara default, sehingga spec memastikan keadaan Hidden lewat Column Visibility.
