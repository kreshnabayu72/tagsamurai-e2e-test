---
id: TC-FA-GRP-E2E-177-tab-users-kombinasi-search-filter-sort-clear-ganti-sort-dan-pemulihan-empty-state
title: "Tab Users Kombinasi: Search + Filter + Sort, Clear Filter/Search, Ganti Target Sort, dan Pemulihan dari Empty State"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-GRP-625
  - TC-FA-GRP-626
  - TC-FA-GRP-627
  - TC-FA-GRP-628
  - TC-FA-GRP-629
coverage:
  web: automated
---

# Tab Users Kombinasi: Search + Filter + Sort, Clear Filter/Search, Ganti Target Sort, dan Pemulihan dari Empty State

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Pre-setup No 1 `totalControlGroups_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD` (nama env baru; didaftarkan di `executionConfig.environmentVariables` dan `.env.example`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Hook suite (flag Guided Tooltip, sesi API aktor, fixture BE, pemulihan state global): lihat `suite.md`. Suite berjalan serial (`parallel: false`).
- Data Pre-setup: Warehouse A (Pre-setup No 9) dibaca dan tidak diubah; memuat >= 12 user dengan variasi role. Tabel Data Uji variasi baris tidak punya tabel konkret di TC (lihat Temuan untuk QA); asersi Search, Filter, dan Sort memakai data dengan sedikitnya dua nilai distinct pada kolom yang diasersi.
- Fixture (berkas baru `groupsTabUsers`, ditetapkan tim FE): `Fixture.groupsTabUsers.irisanKeyword` dan filter Position `Fixture.groupsTabUsers.irisanPosition` yang beririsan pada sedikitnya dua baris; `Fixture.groupsTabUsers.disjointKeyword` yang tidak beririsan dengan Position itu sehingga menghasilkan 0 hasil.

## Test Steps

1. Klik angka Total User Warehouse A

### TC-625: Search + Filter + Sort

2. Ketik Search `Fixture.groupsTabUsers.irisanKeyword`, tekan Enter
3. Klik icon Filter, pilih `Fixture.groupsTabUsers.irisanPosition` pada Position, klik [Apply]
4. Klik header Name sampai sort Desc
5. Verifikasi sedikitnya satu baris tampil pada tabel
6. Verifikasi keyword search, filter, dan sort berlaku bersamaan tanpa saling reset
7. Verifikasi urutan hasil Desc pada himpunan irisan

### TC-626: Clear Filter saat Search dan Sort aktif

8. Buka Filter, klik [Clear Field], klik [Apply]
9. Verifikasi sedikitnya satu baris tampil pada tabel
10. Verifikasi keyword search dan arah sort tetap berlaku
11. Verifikasi hanya kriteria filter yang terlepas
12. Buka Filter, pilih `Fixture.groupsTabUsers.irisanPosition` pada Position, klik [Apply]

### TC-627: Clear Search saat Filter dan Sort aktif

13. Klik (✕) pada Search, tekan Enter pada input kosong
14. Verifikasi sedikitnya satu baris tampil pada tabel
15. Verifikasi kriteria filter dan arah sort tetap berlaku
16. Verifikasi hanya keyword search yang terlepas

### TC-628: Ganti target sort saat Search dan Filter aktif

17. Ketik Search `Fixture.groupsTabUsers.irisanKeyword`, tekan Enter
18. Klik header Name sampai sort Asc (kolom A)
19. Klik header Email (kolom B)
20. Verifikasi sedikitnya satu baris tampil pada tabel
21. Verifikasi sort berpindah ke kolom Email (Asc) dan kolom Name kembali netral
22. Verifikasi search dan filter tetap menyaring

### TC-629: Pemulihan dari empty state

23. Buka Filter, klik [Clear Field], klik [Apply]
24. Klik header Email sampai sort netral
25. Ganti isi kotak search dengan `Fixture.groupsTabUsers.disjointKeyword`, tekan Enter
26. Buka Filter, pilih `Fixture.groupsTabUsers.irisanPosition` pada Position, klik [Apply]
27. Verifikasi tabel menampilkan empty state dengan title "No results found" dan body "Try adjusting your search or filter."
28. Buka Filter, klik [Clear Field], klik [Apply]
29. Verifikasi tabel pulih menampilkan data yang cocok dengan keyword
30. Klik `(←)` pada kotak Search

## Notes

- Langkah penghubung (aksi tanpa `Verifikasi`, S-03 dan S-09): memasang ulang filter setelah TC-626, mengosongkan Filter dan sort sebelum TC-629, dan `(←)` pada kotak Search di akhir spec. State akhir tiap TC (Search + Filter + Sort aktif) sama dengan precondition TC berikutnya; langkah pemasangan ulang ditulis eksplisit.
- Asersi tambahan (S-03, 8b.2): `Verifikasi sedikitnya satu baris tampil pada tabel` ditambahkan sebelum asersi hasil Search atau Filter yang bersifat universal ("hanya baris ...", "nilai lain tidak tampil") agar asersi tidak vacuous; bukan klausa Expected TC.
- Temuan untuk QA:
  - Tabel Data Uji untuk variasi baris Tab Users tidak punya tabel konkret di TC (hanya `>= 12 user variasi role`); spec mendefinisikan kebutuhan nilai distinct di Prerequisites.
  - TC-625 sampai 629 menyebut "filter", "kolom A", dan "kolom B" tanpa nilai; spec memakai fixture (Prerequisites) dan Name sebagai kolom A serta Email sebagai kolom B.
