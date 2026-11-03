---
id: TC-AC-SG-E2E-048-search-tabel-utama-interaksi-kolom-group-dan-total-user
title: "Search Tabel Utama: Interaksi Input, Kolom Group, dan Kolom Total User"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SG-174
  - TC-AC-SG-175
  - TC-AC-SG-176
coverage:
  web: automated
---

# Search Tabel Utama: Interaksi Input, Kolom Group, dan Kolom Total User

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control entitas Principal (Pre-setup #1, nama tampil `Budi Santoso`) `totalControlGroup_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Flag Guided Tooltip halaman Settings > Group disetel `seen` oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Data Pre-setup (dibaca saja, tidak ditulis spec ini): `Pohon Uji Utama` entitas Principal (Pre-setup #16, #17, #19, #20), node `All Groups` terpilih, 14 group (root `All Groups` tidak dihitung), page size bawaan 10 baris, urutan bawaan Group A-Z:

| Group | Induk | Total User | Total Member |
|---|---|---|---|
| `Default Group` | (level 1) | 5 | 0 |
| `Region A` | (level 1) | 5 | 4 |
| `Region B` | (level 1) | 2 | 1 |
| `Region C` | (level 1) | 2 | 1 |
| `Head Office` | (level 1) | 2 | 0 |
| `Warehouse Jakarta` | (level 1) | 3 | 0 |
| `Branch 1` | `Region A` | 4 | 2 |
| `Branch 2` | `Region A` | 2 | 3 |
| `Floor 1` | `Branch 1` | 2 | 0 |
| `Room 301` | `Floor 1` | 2 | 1 |
| `Branch 3` | `Region B` | 2 | 0 |
| `Branch 4` | `Region B` | 2 | 0 |
| `Finance Dept` | `Head Office` | 2 | 0 |
| `IT Dept` | `Head Office` | 2 | 0 |

- Kelima kolom data (Group, Total User, Total Member, Modified By, Last Updated) tampil secara default; preferensi kolom di browser bersih.
- Kemampuan teknis: Fixture BE untuk baseline `Pohon Uji Utama`, disediakan tim FE/BE (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`); spec ini hanya membaca data dan tidak mengubah state global.

## Test Steps

### TC-AC-SG-174: Interaksi Search tabel utama: reveal, submit Enter, clear (✕), dan collapse

1. Catat total record tabel sebelum Search (angka `[N]` pada label root sidebar `All Groups ([N])`)
2. Hover ikon Search pada toolbar
3. Verifikasi tooltip `Search` tampil
4. Klik ikon Search
5. Verifikasi input pencarian terbuka dengan fokus kursor (auto-focus)
6. Verifikasi input pencarian berplaceholder `Search group...`
7. Ketik `Branch` pada input tanpa menekan Enter
8. Verifikasi ikon (✕) muncul di dalam input
9. Verifikasi tabel belum tersaring (info pagination masih menunjukkan total sama dengan total yang dicatat pada langkah 1)
10. Tekan Enter
11. Verifikasi tabel menampilkan `Branch 1`, `Branch 2`, `Branch 3`, dan `Branch 4`
12. Klik ikon (✕) di dalam input
13. Verifikasi input pencarian kosong
14. Verifikasi tabel tetap menampilkan hasil search terakhir (`Branch 1`, `Branch 2`, `Branch 3`, `Branch 4`)
15. Tekan Enter pada input kosong
16. Verifikasi tabel mengembalikan seluruh data (info pagination menunjukkan total sama dengan total yang dicatat pada langkah 1)
17. Ketik Search `Branch`, tekan Enter
18. Klik ikon arrow/close `(←)` untuk menutup input
19. Verifikasi tabel direset ke seluruh data (info pagination menunjukkan total sama dengan total yang dicatat pada langkah 1)

### TC-AC-SG-175: Search tabel utama by kolom Group: substring, case-insensitive, dan tanpa hasil

20. Ketik Search `region`, tekan Enter
21. Verifikasi tabel menampilkan `Region A`, `Region B`, dan `Region C`
22. Ganti isi kotak search dengan `REGION`, tekan Enter
23. Verifikasi hasil identik dengan langkah 21: `Region A`, `Region B`, dan `Region C`
24. Ganti isi kotak search dengan `zzzxxx`, tekan Enter
25. Verifikasi empty state dengan Title `No results found` dan Description `Try adjusting your search or filter.`

### TC-AC-SG-176: Search tabel utama by kolom Total User: substring, case-insensitive, dan tanpa hasil

26. Ganti isi kotak search dengan `4`, tekan Enter
27. Verifikasi tabel menampilkan `Branch 1` (Total User 4), `Region A` (Total Member 4), dan `Branch 4` (nama Group)
28. Ganti isi kotak search dengan versi huruf kapital dari `4` (yaitu `4`), tekan Enter
29. Verifikasi hasil identik dengan langkah 27: `Branch 1`, `Region A`, dan `Branch 4`
30. Ganti isi kotak search dengan `zzzxxx`, tekan Enter
31. Verifikasi empty state dengan Title `No results found` dan Description `Try adjusting your search or filter.`
32. Klik `(←)` pada kotak Search untuk menutup input dan mereset tabel

## Notes

- Langkah penghubung (S-03): langkah 1 (mencatat total record sebelum Search) dan langkah 32 (menutup Search dan mereset tabel, S-09). Antar blok TC kotak search tidak ditutup: isinya diganti ("ganti isi kotak search dengan ..."), sehingga hasil tiap blok tidak bergantung pada blok sebelumnya (S-09).
- Langkah "Pastikan kolom Group tampil" dan "Pastikan kolom Total User tampil" (TC-175, TC-176) dipenuhi oleh Prerequisites (semua kolom tampil secara default) dan tidak ditulis sebagai langkah terpisah.
- Info pagination dipakai untuk membaca jumlah baris total, dibandingkan dengan total yang dicatat pada langkah 1 (tabel menampilkan 10 baris per halaman, S-14).
- Temuan untuk QA:
  - TC-AC-SG-176: kata kunci `4` tidak memiliki varian huruf kapital sehingga uji case-insensitive (Expected b) tidak bermakna; langkah 28 menulis kata kunci yang sama. Usulan: kata kunci TC-176 dan TC-177 memuat huruf (mis. nama group).
  - TC-AC-SG-174 Expected d menyebut total record "ditampilkan per halaman sesuai page size" tanpa menyebut cara membaca total dari halaman 10 baris; spec membaca info pagination (teks info pagination tidak tertulis di TC).
