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
- Data Pre-setup: Warehouse A (Pre-setup No 9) dibaca dan tidak diubah; memuat >= 12 user dengan variasi role. Tabel Data Uji variasi baris tidak punya tabel konkret di TC (lihat Temuan untuk QA); asersi Search, Filter, dan Sort memakai data dengan sedikitnya dua nilai distinct pada kolom yang diasersi.
- Opsi A dan opsi B: dua nilai distinct dari kolom yang difilter pada tabel Warehouse A (diambil dari data tabel saat spec berjalan).

## Test Steps

1. Ketik Search `Warehouse A`, tekan Enter, lalu klik angka Total User Warehouse A
2. Telusuri semua halaman tabel dari halaman 1 sampai halaman terakhir, lalu catat himpunan nilai Division distinct pada baris tabel (tanpa nilai `—`)
3. Kembali ke halaman 1 pagination tabel
4. Klik icon Filter

### TC-590: Chip Position dihapus via (X)

5. Buka dropdown Position
6. Centang opsi A lalu opsi B pada Position
7. Tutup dropdown
8. Verifikasi chip A dan chip B tampil di dalam field (chip B tidak menggantikan chip A)
9. Klik (X) pada chip opsi A
10. Verifikasi chip A hilang
11. Buka dropdown Position
12. Verifikasi checkbox A di dropdown ikut ter-uncheck
13. Tutup dropdown
14. Verifikasi chip B tetap ada
15. Klik [Apply]
16. Verifikasi sedikitnya satu baris tampil pada tabel
17. Verifikasi tabel hanya menyaring Position = opsi B
18. Buka Filter, klik [Clear Field], klik [Apply]
19. Klik icon Filter

### TC-591: Chip Position dihapus via uncheck

20. Buka dropdown Position
21. Centang opsi A lalu opsi B pada Position
22. Buka lagi dropdown dan uncheck opsi A dari dalam dropdown
23. Verifikasi chip A hilang dari field
24. Verifikasi chip B tetap ada
25. Klik [Apply]
26. Verifikasi sedikitnya satu baris tampil pada tabel
27. Verifikasi tabel hanya menyaring Position = opsi B
28. Buka Filter, klik [Clear Field], klik [Apply]
29. Klik icon Filter

### TC-592: Isi opsi Filter Division

30. Buka dropdown Division
31. Verifikasi opsi = himpunan nilai Division distinct yang dicatat pada langkah 2, tidak termasuk nilai yang tidak dipakai baris mana pun
32. Verifikasi opsi dapat dicentang lebih dari satu (multi-select)
33. Verifikasi ada kotak search internal
34. Tutup dropdown

### TC-593: Satu opsi Division

35. Buka dropdown Division
36. Pilih 1 opsi pada Division
37. Klik [Apply]
38. Verifikasi sedikitnya satu baris tampil pada tabel
39. Verifikasi hanya baris dengan Division = opsi terpilih yang tampil
40. Verifikasi indikator filter aktif tampil pada icon Filter
41. Buka Filter, klik [Clear Field], klik [Apply]

## Notes

- Langkah penghubung (aksi tanpa `Verifikasi`, S-03): menutup dropdown, membuka dropdown untuk memeriksa checkbox opsi A pada TC-590 (Expected b), serta `Buka Filter, klik [Clear Field], klik [Apply]` antar TC (S-09).
- Spec memiliki 41 langkah, di atas smell 35 langkah. Alasan: dua keluarga satu topik (chip opsi dan opsi Filter Tab Users pada dataset yang sama) tanpa pemisah kelas harness, dan tiap TC berdiri sendiri; TC-590 sendiri memuat 15 langkah karena Expected b memeriksa chip dan checkbox.
- Himpunan nilai Division distinct dicatat dengan menelusuri seluruh halaman tabel, karena Warehouse A memuat >= 12 user dengan page size 10 sehingga halaman 1 saja tidak mewakili himpunan (S-12, S-14).
- Asersi tambahan (S-03, 8b.2): `Verifikasi sedikitnya satu baris tampil pada tabel` ditambahkan sebelum asersi hasil Search atau Filter yang bersifat universal ("hanya baris ...", "nilai lain tidak tampil") agar asersi tidak vacuous; bukan klausa Expected TC.
- Baris `Warehouse A` dicari lewat Search sebelum klik angka Total User (client memiliki lebih dari 10 node level 1 dan page size 10, sehingga posisi baris di halaman 1 tidak diandalkan; Refresh F5 membuang Search sehingga Search diketik ulang). Langkah Search digabung ke langkah klik angka dan dihitung langkah penghubung (S-03, S-14, R-16).
- Temuan untuk QA:
  - Tabel Data Uji untuk variasi baris Tab Users tidak punya tabel konkret di TC (hanya `>= 12 user variasi role`); spec mendefinisikan kebutuhan nilai distinct di Prerequisites.
  - TC-590 Expected b memeriksa checkbox opsi A di dropdown setelah chip dihapus; spec menambah langkah buka dropdown agar checkbox teramati.
