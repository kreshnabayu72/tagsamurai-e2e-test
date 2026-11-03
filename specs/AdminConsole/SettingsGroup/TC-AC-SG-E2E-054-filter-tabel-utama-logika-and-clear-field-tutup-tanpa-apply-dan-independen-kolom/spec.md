---
id: TC-AC-SG-E2E-054-filter-tabel-utama-logika-and-clear-field-tutup-tanpa-apply-dan-independen-kolom
title: "Filter Tabel Utama: Logika AND, Clear Field, Tutup Tanpa Apply, dan Independen dari Visibilitas Kolom"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AC-SG-194
  - TC-AC-SG-195
  - TC-AC-SG-196
  - TC-AC-SG-197
coverage:
  web: automated
---

# Filter Tabel Utama: Logika AND, Clear Field, Tutup Tanpa Apply, dan Independen dari Visibilitas Kolom

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control entitas Principal (Pre-setup #1, nama tampil `Budi Santoso`) `totalControlGroup_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Flag Guided Tooltip halaman Settings > Group disetel `seen` oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Data Pre-setup (dibaca saja, tidak ditulis spec ini): `Pohon Uji Utama` entitas Principal (Pre-setup #16, #17, #20), node `All Groups` terpilih, 14 group, urutan bawaan Group A-Z. Nilai yang dipakai: `Default Group` Modified By `System`, Total User 5; `Region A` Modified By `Admin A`, Total User 5; `Region B` Modified By `Admin A`, Total User 2; `Branch 1` Modified By `Admin B`, Total User 4. Nilai Total User dan Modified By masing-masing memiliki sedikitnya dua nilai distinct (S-11).
- Kelima kolom data tampil secara default; preferensi kolom di browser bersih. Spec ini menyembunyikan kolom Modified By lewat Overlay Column Visibility (langkah 30) lalu menampilkannya kembali (langkah 35); hook `after` (dan `before`) spec ini menghapus preferensi kolom tabel di browser (kemampuan disediakan tim FE).
- Kemampuan teknis: Fixture BE untuk baseline `Pohon Uji Utama`, disediakan tim FE/BE (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`); spec ini hanya membaca data dan tidak mengubah state global.

## Test Steps

### TC-AC-SG-194: Dua field filter berbeda memakai logika AND

1. Klik ikon Filter pada toolbar
2. Pilih `Admin A` pada Modified By
3. Isi Total User Min = 5
4. Klik `[Apply]`
5. Verifikasi tabel menampilkan `Region A`
6. Verifikasi tidak ada baris selain `Region A` (`Default Group` ber-Modified By `System` tidak tampil)
7. Klik menu `Settings > Group` pada sidebar navigasi untuk mereset Search, Sort, dan Filter

### TC-AC-SG-195: Clear Field mengosongkan kriteria filter tanpa mengubah Search dan Sort

8. Ketik Search `Region`, tekan Enter
9. Klik header kolom Total User sekali (ascending)
10. Klik ikon Filter pada toolbar
11. Pilih `Admin A` pada Modified By, klik `[Apply]`
12. Klik `[Clear Field]`
13. Verifikasi field filter Modified By kosong (tanpa pilihan)
14. Verifikasi field filter Total User kosong (tanpa nilai)
15. Verifikasi field filter Total Member kosong (tanpa nilai)
16. Verifikasi field filter Last Updated kosong (tanpa nilai)
17. Verifikasi kotak Search tetap berisi `Region` dan tabel menampilkan `Region A` dan `Region B`
18. Verifikasi sort Total User ascending tetap aktif (indikator ↑ pada Total User, `Region B` (2) di atas `Region A` (5))
19. Klik menu `Settings > Group` pada sidebar navigasi untuk mereset Search, Sort, dan Filter

### TC-AC-SG-196: Menutup Filter Panel tanpa Apply membuang perubahan draft

20. Klik ikon Filter pada toolbar
21. Pilih `Admin A` pada Modified By, klik `[Apply]`
22. Ubah pilihan Modified By menjadi `Admin B` tanpa klik `[Apply]`
23. Klik ikon Filter untuk menutup panel, lalu klik ikon Filter lagi untuk membukanya
24. Verifikasi panel menampilkan filter ter-Apply terakhir (`Admin A`), bukan draft (`Admin B`)
25. Verifikasi tabel tetap menampilkan hasil `Admin A`: `Region A` tampil dan `Branch 1` tidak tampil
26. Klik menu `Settings > Group` pada sidebar navigasi untuk mereset Search, Sort, dan Filter

### TC-AC-SG-197: Filter independen dari visibilitas kolom

27. Klik ikon Filter pada toolbar
28. Pilih `Admin A` pada Modified By, klik `[Apply]`
29. Klik ikon Filter untuk menutup panel
30. Klik header kolom Actions `⋯` untuk membuka Overlay Column Visibility, hapus centang kolom Modified By
31. Tutup Overlay Column Visibility
32. Klik ikon Filter untuk membuka kembali Filter Panel
33. Verifikasi filter yang di-Apply tetap aktif (indikator filter aktif pada ikon Filter dan `Admin A` terpilih di field Modified By)
34. Verifikasi field Modified By tetap ada di Filter Panel walau kolomnya di-hide
35. Klik header kolom Actions `⋯` untuk membuka Overlay Column Visibility, centang kembali kolom Modified By, lalu tutup overlay

## Notes

- Langkah penghubung (S-03): langkah 7, 19, dan 26 (klik menu `Settings > Group` pada sidebar navigasi mereset Search, Sort, dan Filter; dasar TC-AC-SG-230 dan bagian 4 konvensi, S-09), langkah 29 dan 31 (menutup panel dan overlay), langkah 35 (memulihkan visibilitas kolom, S-09).
- Langkah 6 (absence) didahului langkah 5 yang membuktikan sedikitnya satu baris tampil pada surface yang sama (8b butir 2). Langkah 25 diawali anchor `Region A` tampil sebelum `Branch 1` tidak tampil.
- Filter Panel tetap terbuka sesudah `[Apply]` (mengikuti TC-196, menutup panel dengan klik ikon Filter).
- Temuan untuk QA:
  - TC-AC-SG-195: TC tidak menyatakan apakah `[Clear Field]` tanpa `[Apply]` juga melepas filter dari tabel. Langkah 17 hanya mengasersi `Region A` dan `Region B`, yang tampil pada kedua kemungkinan (Search dan Filter `Admin A` aktif atau hanya Search aktif).
  - TC-AC-SG-194: TC tidak menyebut nilai Total User baris lain secara eksplisit; spec memakai Pre-setup #17 (`Default Group` 5 ber-Modified By `System`).
