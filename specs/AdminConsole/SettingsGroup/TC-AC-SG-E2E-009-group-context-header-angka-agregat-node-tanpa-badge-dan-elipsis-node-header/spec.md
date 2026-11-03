---
id: TC-AC-SG-E2E-009-group-context-header-angka-agregat-node-tanpa-badge-dan-elipsis-node-header
title: "Group Context Header: Angka Node Sendiri, Tanpa Badge, Elipsis Node Header, dan Angka Tetap saat Search atau Filter"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SG-33
  - TC-AC-SG-34
  - TC-AC-SG-36
  - TC-AC-SG-400
coverage:
  web: automated
---

# Group Context Header: Angka Node Sendiri, Tanpa Badge, Elipsis Node Header, dan Angka Tetap saat Search atau Filter

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal (Pre-setup #1) `totalControlGroup_automated_{namaCompany}@qwertysystem.net` (nama tampil `Budi Santoso`), password `Spectra.env.AC_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Flag Guided Tooltip `guided_tooltip_seen_ac-settings-group` disetel `seen` oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Data Pre-setup (dibaca saja, tidak diubah): `Pohon Uji Utama` entitas Principal (#16, 14 group); Total User dan Total Member per node (#17, #19): `Region A` 5 dan 4, `Branch 1` 4 dan 2, `Floor 1` 2 dan 0; `Modified By` per node (#20): `Branch 1` dan `Branch 2` oleh `Admin B`.
- Data Dinamis: tidak ada; spec tidak membuat atau mengubah data sehingga tidak ada seeding, suffix `{runId}-009`, maupun cleanup.
- Suite berjalan serial (`parallel: false`); spec ini tidak mengubah state global.

## Test Steps

### TC-AC-SG-33: Angka Group Context Header pada node terpilih adalah angka node itu sendiri

1. Klik node `Branch 1`
2. Verifikasi Group Context Header menampilkan "Branch 1" | "Total User: 4" | "Total Member: 2" (tanpa akumulasi subgroup `Floor 1` dan `Room 301`)
3. Klik node `Floor 1`
4. Verifikasi Group Context Header menampilkan "Floor 1" | "Total User: 2" | "Total Member: 0" (Total Member `Room 301` tidak ikut terhitung)

### TC-AC-SG-34: Group Context Header node terpilih tanpa badge atau kode group

5. Klik node `Head Office`
6. Verifikasi Group Context Header menampilkan "Head Office" sebagai teks nama
7. Verifikasi Group Context Header tanpa badge, tanpa kode group, dan tanpa ikon menu aksi

### TC-AC-SG-36: Node yang sedang menjadi header hanya dapat diaksi lewat elipsis sidebar

8. Klik node `Region A` sehingga menjadi header
9. Cari baris `Region A` pada tabel
10. Verifikasi tabel menampilkan baris descendant `Branch 1`
11. Verifikasi baris `Region A` tidak ada di tabel sehingga tidak ada row action untuknya
12. Klik ikon `⋯` pada node `Region A` di sidebar
13. Verifikasi menu `⋯` node sidebar `Region A` menampilkan "+ Add Subgroup", "Edit", dan "Delete"
14. Tutup menu node dengan Esc
15. Klik node `Region A` sekali lagi untuk melepas pilihan

### TC-AC-SG-400: Angka Group Context Header tidak berubah saat Search atau Filter tabel aktif

16. Klik node `Region A` di sidebar
17. Verifikasi Group Context Header menampilkan "Total User: 5" dan "Total Member: 4"
18. Ketik Search `Branch 1`, tekan Enter
19. Verifikasi tabel memuat sedikitnya satu baris
20. Verifikasi setiap baris tabel cocok dengan pencarian `Branch 1`
21. Verifikasi Group Context Header tetap "Total User: 5" dan "Total Member: 4"
22. Klik `(←)` pada kotak Search
23. Klik ikon Filter pada toolbar
24. Pilih Modified By "Admin B"
25. Klik `[Apply]`
26. Verifikasi tabel memuat sedikitnya satu baris
27. Verifikasi setiap baris tabel adalah descendant `Region A` ber-Modified By "Admin B"
28. Verifikasi Group Context Header tetap "Total User: 5" dan "Total Member: 4"
29. Bersihkan Filter Modified By
30. Klik node `Region A` sekali lagi untuk melepas pilihan

## Notes

- Langkah penghubung (S-03, S-09, R-16): langkah 9 mengamati tanpa asersi sendiri; langkah 14 menutup menu; langkah 15 dan 30 melepas pilihan node `Region A`; langkah 22 mengosongkan Search sebelum Filter; langkah 29 membersihkan Filter sebelum spec berakhir. Pilihan node pada blok TC-AC-SG-33 dan TC-AC-SG-34 digantikan pilihan berikutnya (pilihan exclusive).
- Asersi universal langkah 20 dan 27 didahului pembanding generik "sedikitnya satu baris" (langkah 19 dan 26, bagian 8b butir 2); absence langkah 11 berjangkar pada baris descendant yang tampil (langkah 10).
- Total User dan Total Member agregat All Groups sebagai user distinct, bukan penjumlahan per node (TC-AC-SG-32), ada di spec 106.
- Temuan untuk QA:
  - TC-AC-SG-400 langkah 4 memakai "Filter Modified By 'Admin B'" tanpa menyebut cara membersihkan Filter; langkah 29 ditulis sebagai langkah penghubung tanpa label tombol.
  - TC-AC-SG-400 langkah 3 menyebut "Hapus pencarian" sebelum Filter; spec memakai `(←)` pada kotak Search (bagian 8b butir 9).
