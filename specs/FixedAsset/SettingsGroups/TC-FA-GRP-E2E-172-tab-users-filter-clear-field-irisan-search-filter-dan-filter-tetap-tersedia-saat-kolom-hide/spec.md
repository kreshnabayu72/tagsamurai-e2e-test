---
id: TC-FA-GRP-E2E-172-tab-users-filter-clear-field-irisan-search-filter-dan-filter-tetap-tersedia-saat-kolom-hide
title: "Tab Users Filter: [Clear Field], Search lalu Filter, Filter lalu Search, dan Filter Tetap Tersedia Saat Kolom Position Di-Hide"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-GRP-611
  - TC-FA-GRP-612
  - TC-FA-GRP-613
  - TC-FA-GRP-1120
coverage:
  web: automated
---

# Tab Users Filter: [Clear Field], Search lalu Filter, Filter lalu Search, dan Filter Tetap Tersedia Saat Kolom Position Di-Hide

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Pre-setup No 1 `totalControlGroups_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD` (nama env baru; didaftarkan di `executionConfig.environmentVariables` dan `.env.example`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Hook suite (flag Guided Tooltip, sesi API aktor, fixture BE, pemulihan state global): lihat `suite.md`. Suite berjalan serial (`parallel: false`).
- Data Pre-setup: Warehouse A (Pre-setup No 9) dibaca dan tidak diubah; memuat >= 12 user dengan variasi role, dan client punya Custom Field aktif Phone (Data Dinamis, dibaca saja). Tabel Data Uji variasi baris tidak punya tabel konkret di TC (lihat Temuan untuk QA); asersi Search, Filter, dan Sort memakai data dengan sedikitnya dua nilai distinct pada kolom yang diasersi.
- Opsi A dan opsi B: dua nilai distinct dari kolom yang difilter pada tabel Warehouse A (diambil dari data tabel saat spec berjalan).
- Fixture (berkas baru `groupsTabUsers`, ditetapkan tim FE): `Fixture.groupsTabUsers.irisanKeyword` dan nilai Position, Division, Group Role, Activation Status yang beririsan dengan keyword itu (`irisanPosition`, `irisanDivision`, `irisanGroupRole`, `irisanActivation`); irisan memuat sedikitnya satu baris dan lebih sedikit dari hasil Search saja dan Filter saja.

## Test Steps

1. Klik angka Total User Warehouse A
2. Catat nama baris halaman 1 tabel
3. Klik icon Filter

### TC-611: [Clear Field] mengosongkan seluruh field

4. Isi Position dan Division, klik [Apply]
5. Buka Filter lagi, klik [Clear Field]
6. Verifikasi semua field filter kembali kosong dengan placeholder
7. Klik [Apply]
8. Verifikasi tabel kembali menampilkan seluruh data: nama baris halaman 1 sama dengan yang dicatat pada langkah 2

### TC-612: Search lalu Filter

9. Ketik Search `Fixture.groupsTabUsers.irisanKeyword`, tekan Enter
10. Buka Filter, isi semua field filter yang tersedia dengan nilai yang beririsan, klik [Apply]
11. Verifikasi sedikitnya satu baris tampil pada tabel
12. Verifikasi hasil = irisan Search dan Filter
13. Verifikasi keyword search tetap terpasang setelah [Apply]
14. Buka Filter, klik [Clear Field], klik [Apply]
15. Klik `(←)` pada kotak Search

### TC-613: Filter lalu Search

16. Buka Filter, isi semua field filter yang tersedia dengan nilai yang beririsan, klik [Apply]
17. Ketik Search `Fixture.groupsTabUsers.irisanKeyword`, tekan Enter
18. Verifikasi sedikitnya satu baris tampil pada tabel
19. Verifikasi hasil = irisan Filter dan Search
20. Verifikasi kriteria filter tetap aktif setelah search
21. Buka Filter, klik [Clear Field], klik [Apply]
22. Klik `(←)` pada kotak Search

### TC-1120: Filter tetap tersedia saat kolom Position di-hide

23. Klik icon Filter, pilih satu opsi pada Position, klik [Apply]
24. Verifikasi sedikitnya satu baris tampil pada tabel
25. Verifikasi Tab Users hanya memuat baris dengan Position terpilih
26. Catat nama baris halaman 1 tabel
27. Sembunyikan kolom Position lewat Column Visibility
28. Verifikasi filter yang sudah di-Apply tetap berlaku (nama baris halaman 1 sama dengan yang dicatat pada langkah 26)
29. Klik icon Filter
30. Verifikasi Filter Panel tetap memuat field Position walau kolomnya tersembunyi
31. Tampilkan kembali kolom Position
32. Verifikasi hasil dan nilai filter tidak berubah (nama baris halaman 1 sama dengan yang dicatat pada langkah 26)
33. Buka Filter, klik [Clear Field], klik [Apply]

## Notes

- Langkah penghubung (aksi tanpa `Verifikasi`, S-03): `Buka Filter, klik [Clear Field], klik [Apply]` dan `(←)` pada kotak Search antar TC (S-09); membuka Filter Panel sebelum langkah yang menyebutnya.
- Asersi tambahan (S-03, 8b.2): `Verifikasi sedikitnya satu baris tampil pada tabel` ditambahkan sebelum asersi hasil Search atau Filter yang bersifat universal ("hanya baris ...", "nilai lain tidak tampil") agar asersi tidak vacuous; bukan klausa Expected TC. Penanda `Catat nama baris halaman 1 tabel` menjadi baseline asersi "seluruh data" dan "baris yang tampil sama".
- Temuan untuk QA:
  - Tabel Data Uji untuk variasi baris Tab Users tidak punya tabel konkret di TC (hanya `>= 12 user variasi role`); spec mendefinisikan kebutuhan nilai distinct di Prerequisites.
  - TC-612 dan TC-613 menyebut "isi semua field filter yang tersedia dengan nilai yang beririsan" tanpa nilai; spec memakai fixture (Prerequisites). Field Temporary Until dan Custom Field mengikuti field yang tersedia pada saat spec berjalan.
