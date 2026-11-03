---
id: TC-AC-SG-E2E-056-sort-tabel-utama-kolom-group-total-user-dan-total-member
title: "Sort Tabel Utama: Kolom Group, Total User, dan Total Member"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SG-202
  - TC-AC-SG-203
  - TC-AC-SG-204
coverage:
  web: automated
---

# Sort Tabel Utama: Kolom Group, Total User, dan Total Member

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control entitas Principal (Pre-setup #1, nama tampil `Budi Santoso`) `totalControlGroup_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Flag Guided Tooltip halaman Settings > Group disetel `seen` oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Data Pre-setup (dibaca saja, tidak ditulis spec ini): `Pohon Uji Utama` entitas Principal (Pre-setup #16, #17, #19), node `All Groups` terpilih, 14 group, urutan bawaan Group A-Z. Total User: nilai 2 sampai 5 (`Default Group` dan `Region A` bernilai 5; `Warehouse Jakarta` 3; `Branch 1` 4; node lain 2). Total Member: nilai 0 sampai 4 (`Region A` 4; `Branch 2` 3; `Branch 1` 2; `Room 301`, `Region B`, `Region C` 1; node lain 0). Tiap kolom memiliki sedikitnya dua nilai distinct (S-11).
- Page size diubah ke 25 pada langkah 1 supaya seluruh 14 baris berada pada satu halaman (TC-AC-SG-224 membuktikan page size 25 menampilkan 14 baris pada halaman 1).
- Kelima kolom data tampil secara default; preferensi kolom di browser bersih.
- Kemampuan teknis: Fixture BE untuk baseline `Pohon Uji Utama`, disediakan tim FE/BE (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`); spec ini hanya membaca data dan tidak mengubah state global.

## Test Steps

1. Pilih page size 25

### TC-AC-SG-202: Sort tabel utama kolom Group: siklus tiga klik

2. Klik header kolom Group sekali
3. Verifikasi ascending (↑): `Branch 1`, `Branch 2`, dan `Branch 3` berurutan dari atas dan `Warehouse Jakarta` di baris terakhir
4. Klik header Group kedua kali
5. Verifikasi descending (↓) Z-A: `Warehouse Jakarta` di baris pertama
6. Klik header Group ketiga kali
7. Verifikasi indikator sort hilang
8. Verifikasi urutan kembali ke bawaan Group A-Z (`Branch 1` di baris pertama dan `Warehouse Jakarta` di baris terakhir)

### TC-AC-SG-203: Sort tabel utama kolom Total User: siklus tiga klik

9. Klik header kolom Total User sekali
10. Verifikasi ascending (↑): nilai terkecil (2) di baris pertama dan nilai terbesar (5) di baris terakhir
11. Klik header Total User kedua kali
12. Verifikasi descending (↓): nilai terbesar (5) di baris pertama
13. Klik header Total User ketiga kali
14. Verifikasi indikator sort hilang
15. Verifikasi urutan kembali ke bawaan Group A-Z (`Branch 1` di baris pertama)

### TC-AC-SG-204: Sort tabel utama kolom Total Member: siklus tiga klik

16. Klik header kolom Total Member sekali
17. Verifikasi ascending (↑): nilai 0 di baris pertama dan nilai 4 di baris terakhir
18. Klik header Total Member kedua kali
19. Verifikasi descending (↓): nilai 4 di baris pertama
20. Klik header Total Member ketiga kali
21. Verifikasi indikator sort hilang
22. Verifikasi urutan kembali ke bawaan Group A-Z (`Branch 1` di baris pertama)
23. Pilih page size 10

## Notes

- Langkah penghubung (S-03): langkah 1 (page size 25 supaya asersi baris terakhir pada langkah 3, 10, dan 17 berada di halaman yang sama dengan baris pertama, S-14) dan langkah 23 (memulihkan page size bawaan 10 sesudah blok terakhir, S-09).
- Hasil sort pada nilai yang sama (mis. Total User 2) tidak diasersi urutan antarbaris; asersi memakai nilai pada baris pertama dan terakhir.
- Temuan untuk QA:
  - TC-AC-SG-202 Expected a menyebut urutan sampai `Warehouse Jakarta` tanpa menyebut halaman; pada page size bawaan 10 baris `Warehouse Jakarta` berada di halaman 2, sehingga spec memakai page size 25.
