---
id: TC-FA-GRP-E2E-166-tab-users-filter-position-chip-dan-filter-division-opsi
title: "Tab Users Filter: Chip Opsi Position dan Filter Division (Isi Opsi, Satu Opsi, Dua Opsi OR)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-GRP-590
  - TC-FA-GRP-591
  - TC-FA-GRP-592
  - TC-FA-GRP-593
coverage:
  web: automated
---

# Tab Users Filter: Chip Opsi Position dan Filter Division (Isi Opsi, Satu Opsi, Dua Opsi OR)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Pre-setup No 1 `totalControlGroups_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD` (nama env baru; didaftarkan di `executionConfig.environmentVariables` dan `.env.example`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Hook suite (flag Guided Tooltip, sesi API aktor, fixture BE, pemulihan state global): lihat `suite.md`. Suite berjalan serial (`parallel: false`).
- Data Pre-setup: Warehouse A (Pre-setup No 9) dibaca dan tidak diubah; memuat >= 12 user dengan variasi role, dan client punya Custom Field aktif Phone (Data Dinamis, dibaca saja). Tabel Data Uji variasi baris tidak punya tabel konkret di TC (lihat Temuan untuk QA); asersi Search, Filter, dan Sort memakai data dengan sedikitnya dua nilai distinct pada kolom yang diasersi.
- Opsi A dan opsi B: dua nilai distinct dari kolom yang difilter pada tabel Warehouse A (diambil dari data tabel saat spec berjalan).

## Test Steps

1. Klik angka Total User Warehouse A
2. Klik icon Filter

### TC-590: Chip Position dihapus via (X)

3. Buka dropdown Position
4. Centang opsi A lalu opsi B pada Position
5. Tutup dropdown
6. Verifikasi chip A dan chip B tampil di dalam field (chip B tidak menggantikan chip A)
7. Klik (X) pada chip opsi A
8. Verifikasi chip A hilang
9. Buka dropdown Position
10. Verifikasi checkbox A di dropdown ikut ter-uncheck
11. Tutup dropdown
12. Verifikasi chip B tetap ada
13. Klik [Apply]
14. Verifikasi sedikitnya satu baris tampil pada tabel
15. Verifikasi tabel hanya menyaring Position = opsi B
16. Buka Filter, klik [Clear Field], klik [Apply]
17. Klik icon Filter

### TC-591: Chip Position dihapus via uncheck

18. Buka dropdown Position
19. Centang opsi A lalu opsi B pada Position
20. Buka lagi dropdown dan uncheck opsi A dari dalam dropdown
21. Verifikasi chip A hilang dari field
22. Verifikasi chip B tetap ada
23. Klik [Apply]
24. Verifikasi sedikitnya satu baris tampil pada tabel
25. Verifikasi tabel hanya menyaring Position = opsi B
26. Buka Filter, klik [Clear Field], klik [Apply]
27. Klik icon Filter

### TC-592: Isi opsi Filter Division

28. Buka dropdown Division
29. Verifikasi opsi = nilai Division distinct yang ada di baris tabel ini saat ini, tidak termasuk nilai yang tidak dipakai baris mana pun
30. Verifikasi opsi dapat dicentang lebih dari satu (multi-select)
31. Verifikasi ada kotak search internal
32. Tutup dropdown

### TC-593: Satu opsi Division

33. Buka dropdown Division
34. Pilih 1 opsi pada Division
35. Klik [Apply]
36. Verifikasi sedikitnya satu baris tampil pada tabel
37. Verifikasi hanya baris dengan Division = opsi terpilih yang tampil
38. Verifikasi indikator filter aktif tampil pada icon Filter
39. Buka Filter, klik [Clear Field], klik [Apply]

## Notes

- Langkah penghubung (aksi tanpa `Verifikasi`, S-03): menutup dropdown, membuka dropdown untuk memeriksa checkbox opsi A pada TC-590 (Expected b), serta `Buka Filter, klik [Clear Field], klik [Apply]` antar TC (S-09).
- Spec memiliki 39 langkah, di atas smell 35 langkah. Alasan: dua keluarga satu topik (chip opsi dan opsi Filter Tab Users pada dataset yang sama) tanpa pemisah kelas harness, dan tiap TC berdiri sendiri; TC-590 sendiri memuat 15 langkah karena Expected b memeriksa chip dan checkbox.
- Asersi tambahan (S-03, 8b.2): `Verifikasi sedikitnya satu baris tampil pada tabel` ditambahkan sebelum asersi hasil Search atau Filter yang bersifat universal ("hanya baris ...", "nilai lain tidak tampil") agar asersi tidak vacuous; bukan klausa Expected TC.
- Temuan untuk QA:
  - Tabel Data Uji untuk variasi baris Tab Users tidak punya tabel konkret di TC (hanya `>= 12 user variasi role`); spec mendefinisikan kebutuhan nilai distinct di Prerequisites.
  - TC-590 Expected b memeriksa checkbox opsi A di dropdown setelah chip dihapus; spec menambah langkah buka dropdown agar checkbox teramati.
