---
id: TC-AC-SG-E2E-055-search-dan-filter-beririsan-empty-state-kombinasi-filter-lokal-node-dan-reset-halaman
title: "Search dan Filter Beririsan: Empty State Kombinasi, Filter Lokal Node, dan Reset Halaman"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AC-SG-198
  - TC-AC-SG-199
  - TC-AC-SG-200
  - TC-AC-SG-201
  - TC-AC-SG-240
coverage:
  web: automated
---

# Search dan Filter Beririsan: Empty State Kombinasi, Filter Lokal Node, dan Reset Halaman

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control entitas Principal (Pre-setup #1, nama tampil `Budi Santoso`) `totalControlGroup_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Flag Guided Tooltip halaman Settings > Group disetel `seen` oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Data Pre-setup (dibaca saja, tidak ditulis spec ini): `Pohon Uji Utama` entitas Principal (Pre-setup #16, #17, #20), node `All Groups` terpilih, 14 group (2 halaman pada page size bawaan 10 baris), urutan bawaan Group A-Z. Nilai yang dipakai: `Branch 1` dan `Branch 2` Modified By `Admin B`; `Region A` dan `Region B` Modified By `Admin A`; `Region A` memiliki descendant `Branch 1`, `Branch 2`, `Floor 1`, dan `Room 301`; semua Total User bernilai sedikitnya 2.
- Kelima kolom data tampil secara default; preferensi kolom di browser bersih.
- Kemampuan teknis: Fixture BE untuk baseline `Pohon Uji Utama`, disediakan tim FE/BE (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`); spec ini hanya membaca data dan tidak mengubah state global.

## Test Steps

### TC-AC-SG-240: Empty state hasil Search atau Filter kosong pada tabel utama

1. Ketik Search `zzzxxx`, tekan Enter
2. Verifikasi tabel menampilkan empty state dengan Illustration, Title `No results found`, dan Description `Try adjusting your search or filter.` (bukan empty state genuinely empty)
3. Klik `(←)` pada kotak Search untuk menutup input dan mereset tabel

### TC-AC-SG-198: Search dan Filter beririsan (AND) dengan hasil sama untuk urutan berbeda

4. Ketik Search `Branch`, tekan Enter
5. Klik ikon Filter pada toolbar
6. Pilih `Admin B` pada Modified By, klik `[Apply]`
7. Verifikasi tabel menampilkan `Branch 1` dan `Branch 2` (urutan Search lalu Filter)
8. Klik menu `Settings > Group` pada sidebar navigasi untuk mereset Search, Sort, dan Filter
9. Klik ikon Filter pada toolbar
10. Pilih `Admin B` pada Modified By, klik `[Apply]`
11. Ketik Search `Branch`, tekan Enter
12. Verifikasi tabel menampilkan `Branch 1` dan `Branch 2`, identik dengan langkah 7 (urutan Filter lalu Search)

### TC-AC-SG-199: Empty state hasil kombinasi pulih saat salah satu kontrol dilepas

13. Klik menu `Settings > Group` pada sidebar navigasi untuk mereset Search, Sort, dan Filter
14. Ketik Search `Region A`, tekan Enter
15. Klik ikon Filter pada toolbar
16. Pilih `Admin B` pada Modified By, klik `[Apply]`
17. Verifikasi tabel menampilkan empty state dengan Title `No results found` dan Description `Try adjusting your search or filter.`
18. Kosongkan isi kotak search, tekan Enter
19. Verifikasi tabel pulih menampilkan baris ber-Modified By `Admin B`: `Branch 1` dan `Branch 2`

### TC-AC-SG-200: Filter lokal terhadap node yang dipilih

20. Klik menu `Settings > Group` pada sidebar navigasi untuk mereset Search, Sort, dan Filter
21. Klik node `Region A` di sidebar
22. Klik ikon Filter pada toolbar
23. Pilih `Admin A` pada Modified By, klik `[Apply]`
24. Verifikasi tabel hanya menampilkan descendant `Region A` ber-Modified By `Admin A` (tidak ada baris di luar node); bila tidak ada kecocokan tampil empty state `No results found` dengan Description `Try adjusting your search or filter.`

### TC-AC-SG-201: Search dan Apply Filter mereset halaman ke 1

25. Klik menu `Settings > Group` pada sidebar navigasi untuk mereset Search, Sort, dan Filter
26. Pindah ke halaman 2
27. Ketik Search `e`, tekan Enter
28. Verifikasi halaman aktif kembali ke 1 setelah Search
29. Klik `(←)` pada kotak Search untuk menutup input dan mereset tabel
30. Pindah ke halaman 2
31. Klik ikon Filter pada toolbar
32. Isi Total User Min = 2, klik `[Apply]`
33. Verifikasi halaman aktif kembali ke 1 setelah Apply Filter

## Notes

- Urutan TC dalam spec: 240, 198, 199, 200, 201 (TC-240 hanya Search dan tidak bergantung pada TC lain; urutan lain mengikuti nomor TC).
- Langkah penghubung (S-03): langkah 3 dan 29 (menutup Search dan mereset tabel), langkah 8, 13, 20, dan 25 (klik menu `Settings > Group` pada sidebar navigasi mereset Search, Sort, dan Filter; dasar TC-AC-SG-230 dan bagian 4 konvensi, S-09). Langkah 8 sekaligus menjalankan "Reset keduanya" TC-198.
- Temuan untuk QA:
  - TC-AC-SG-200: Expected bersyarat ("bila tidak ada kecocokan empty state") dan Pre-setup #20 tidak menyebut Modified By `Floor 1` dan `Room 301`, sehingga hasil tidak deterministik; langkah 24 mengikuti redaksi TC. Usulan: Pre-setup menyebut Modified By tiap node atau Expected menyebut baris pasti.
  - TC-AC-SG-201: langkah 4 TC ("Pindah ke halaman 2 jika tersedia") bersyarat dan Search `e` menghasilkan 8 baris pada Pohon Uji Utama (satu halaman), sehingga reset halaman setelah Apply Filter tidak teruji dengan Search masih aktif. Spec menutup Search lebih dulu (langkah 29) lalu pindah ke halaman 2 (14 baris, 2 halaman) sebelum Apply Total User Min = 2 (seluruh baris memenuhi).
  - TC-AC-SG-240: TC tidak menyebut teks empty state genuinely empty; pembedanya dibaca dari Title `No results found`.
