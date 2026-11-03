---
id: TC-AC-SG-E2E-006-sidebar-group-tree-hapus-search-label-panjang-elipsis-dan-highlight
title: "Sidebar Group Tree: Hapus Search, Label Panjang, Tombol Elipsis, dan Highlight Node"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SG-21
  - TC-AC-SG-25
  - TC-AC-SG-26
  - TC-AC-SG-27
coverage:
  web: automated
---

# Sidebar Group Tree: Hapus Search, Label Panjang, Tombol Elipsis, dan Highlight Node

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal (Pre-setup #1) `totalControlGroup_automated_{namaCompany}@qwertysystem.net` (nama tampil `Budi Santoso`), password `Spectra.env.AC_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Flag Guided Tooltip `guided_tooltip_seen_ac-settings-group` disetel `seen` oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Data Pre-setup (dibaca saja, tidak diubah): `Pohon Uji Utama` entitas Principal (#16, 14 group); agregat "Total User: 10" dan "Total Member: 12" (#17, #19).
- Data Dinamis (dibuat spec; TC-AC-SG-25 menyebutnya seed tambahan ke-15 pada `Pohon Uji Utama`):

| TC | Nama TC | Nama seed | State |
|---|---|---|---|
| TC-AC-SG-25 | `Gudang Distribusi Wilayah Timur Terpadu Gudang Distribusi Wilayah Timur Terpadu Gudang Distribusi Wilayah Timur Terpadu1` (120 karakter) | Awalan nama TC dipotong lalu diakhiri ` {runId}-006` sehingga panjang nama tepat 120 karakter termasuk suffix | Group level 1, tanpa entitas |

- Kemampuan teknis: Fixture BE untuk membuat dan menghapus group seed di atas pada `Pohon Uji Utama`, disediakan tim FE/BE (lihat `suite.md`). Group dibuat di langkah penghubung sebelum blok TC-AC-SG-25 (bagian akhir spec) dan dihapus sesudahnya; hook `after` spec ini menghapusnya juga bila spec berhenti di tengah. Efek pada Last Updated, Modified By, dan entri Changelog `Pohon Uji Utama` dari seeding group ini dicatat di sini: group seed menambah satu group (N menjadi 15) hanya selama blok TC-AC-SG-25.
- Suite berjalan serial (`parallel: false`); spec ini tidak mengubah state global.

## Test Steps

### TC-AC-SG-21: Menghapus pencarian sidebar mengembalikan tree penuh

1. Ketik "Branch" pada input "Search groups..."
2. Verifikasi `Branch 1`, `Branch 2`, `Branch 3`, dan `Branch 4` ter-highlight
3. Verifikasi ancestor tiap node yang cocok ter-expand
4. Verifikasi node lain tetap terlihat
5. Verifikasi isi tabel tetap 14 group
6. Verifikasi Group Context Header tetap "Total User: 10" dan "Total Member: 12"
7. Klik ikon clear pada input pencarian
8. Verifikasi input pencarian kosong
9. Verifikasi highlight pencarian hilang
10. Verifikasi seluruh node tree tampil kembali
11. Verifikasi pilihan node aktif tidak berubah (`All Groups` tetap aktif)

### TC-AC-SG-26: Tombol ⋯ per node sidebar selalu tampil dan sejajar dengan Row Actions tabel

12. Perhatikan sisi kanan setiap node di sidebar tanpa hover
13. Verifikasi ikon `⋯` tampil pada setiap node tanpa perlu hover
14. Verifikasi root "All Groups" tidak memiliki ikon `⋯`
15. Klik ikon `⋯` pada node `Branch 1`
16. Verifikasi menu node memuat aksi yang sama dengan Row Actions tabel: "+ Add Subgroup", "Edit", dan "Delete"
17. Tutup menu node dengan Esc

### TC-AC-SG-27: Node terpilih ber-highlight dan bold sebagai penanda state aktif

18. Klik node `Region B`
19. Verifikasi node `Region B` ber-highlight dan bold
20. Verifikasi root "All Groups" tidak lagi ber-highlight aktif
21. Klik node `Region B` sekali lagi untuk melepas pilihan

### TC-AC-SG-25: Label node panjang terpotong dengan tooltip nama lengkap

22. Buat group seed bernama 120 karakter di level 1 lewat Fixture BE
23. Muat ulang halaman dengan F5
24. Hover label node bernama 120 karakter di sidebar
25. Verifikasi label node terpotong (truncate) dalam lebar panel w-64
26. Verifikasi tooltip menampilkan nama lengkap seluruh 120 karakter
27. Hapus group seed lewat Fixture BE

## Notes

- Urutan TC di spec: TC-AC-SG-21, 26, 27, lalu 25. TC-AC-SG-25 membutuhkan group ke-15 yang mengubah hitungan pohon; diletakkan terakhir agar blok lain membaca `Pohon Uji Utama` apa adanya (14 group) dan agar seed dibersihkan di akhir (S-06, S-10).
- Langkah penghubung (S-03, S-09): langkah 12 mengamati tanpa asersi sendiri; langkah 17 menutup menu; langkah 21 melepas pilihan node `Region B`; langkah 22, 23, dan 27 membuat group seed, memuat ulang halaman supaya tree menampilkannya, dan menghapus group seed.
- Pencarian sidebar tree diketik tanpa Enter (sesuai TC).
- Temuan untuk QA:
  - TC-AC-SG-25 precondition d menyebut nama literal 120 karakter tanpa suffix `{runId}-006`; spec memakai nama bersuffix (S-12) yang dipotong dari awalan nama itu hingga tepat 120 karakter, dan mengasersi tooltip berisi nama lengkap seluruh 120 karakter.
  - TC-AC-SG-25 menyebut group itu "seed tambahan" pada `Pohon Uji Utama` tanpa Pre-setup bernomor; spec membuatnya lewat Fixture BE (disediakan tim FE/BE) dan menghapusnya sesudah blok.
  - TC-AC-SG-26 Expected b ("aksi yang sama dengan Row Actions tabel") diasersi sebagai daftar tiga aksi dari Expected TC-AC-SG-09, bukan perbandingan langsung dengan overlay tabel.
