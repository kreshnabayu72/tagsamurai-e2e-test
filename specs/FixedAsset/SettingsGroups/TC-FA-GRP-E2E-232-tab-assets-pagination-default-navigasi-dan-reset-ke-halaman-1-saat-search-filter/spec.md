---
id: TC-FA-GRP-E2E-232-tab-assets-pagination-default-navigasi-dan-reset-ke-halaman-1-saat-search-filter
title: "Tab Assets Pagination: Default dan Page Size, Navigasi, serta Reset ke Halaman 1 Saat Search/Filter"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-GRP-1047
  - TC-FA-GRP-1048
coverage:
  web: automated
---

# Tab Assets Pagination: Default dan Page Size, Navigasi, serta Reset ke Halaman 1 Saat Search/Filter

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup No 1) `totalControlGroups_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook suite pada `suite.md` berlaku.
- Data Pre-setup (hanya dibaca): Warehouse A (WH-A, Assignable, 24 aset aktif variasi status, ditambah 2 Disposed) pada pohon group Tabel A. N total = 24 aset aktif (dari seeding, 8b butir 10); page size default 10 sehingga 3 halaman.
- Data pencarian dan filter untuk TC-FA-GRP-1048: kata Search yang cocok dengan beberapa aset (sedikitnya 2) di Warehouse A dan opsi Status yang cocok dengan sedikitnya satu aset; nilai dipilih dari fixture Warehouse A (TC tidak menyebut nilai).
- State global: tidak ada. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-GRP-1047: Default dan pilihan page size

1. Klik angka Total Asset Warehouse A
2. Verifikasi footer pagination menampilkan default 10 baris per halaman
3. Verifikasi tabel menampilkan 10 baris
4. Buka dropdown page size
5. Verifikasi pilihan page size: 10 / 25 / 50 / 100
6. Verifikasi dropdown page size tidak memuat opsi All
7. Pilih page size 25
8. Verifikasi tabel menampilkan 24 baris (seluruh aset aktif, kurang dari 25)
9. Buka dropdown page size
10. Pilih page size 50
11. Verifikasi tabel menampilkan 24 baris
12. Buka dropdown page size
13. Pilih page size 100
14. Verifikasi tabel menampilkan 24 baris
15. Buka dropdown page size
16. Pilih page size 10
17. Verifikasi tabel menampilkan 10 baris

### TC-FA-GRP-1048: Navigasi, input nomor halaman, dan reset ke halaman 1

18. Klik next
19. Verifikasi tabel berpindah ke halaman 2
20. Klik prev
21. Verifikasi tabel berpindah ke halaman 1
22. Ketik nomor halaman 2 di input halaman, tekan Enter
23. Verifikasi halaman 2 terbuka
24. Ketik Search `<kata cocok>`, tekan Enter
25. Verifikasi tabel menampilkan sedikitnya satu baris hasil Search
26. Verifikasi tabel menampilkan halaman 1 dari hasil Search
27. Klik `(←)` pada kotak Search
28. Klik next
29. Verifikasi tabel berada di halaman 2
30. Klik icon Filter
31. Pilih satu opsi Status
32. Klik [Apply]
33. Verifikasi tabel menampilkan sedikitnya satu baris hasil Filter
34. Verifikasi tabel menampilkan halaman 1 dari hasil Filter
35. Hapus pilihan Status pada Filter lalu klik [Apply]

## Notes

- Subjudul `###` memetakan langkah ke id TC granular. `<kata cocok>` pada langkah 24 adalah kata Search dari fixture Warehouse A.
- Langkah penghubung (S-03): langkah 27 mengosongkan Search sebelum navigasi berikutnya; langkah 28 dan 29 mengembalikan tabel ke halaman 2 sebelum Filter (Langkah 6 TC: "Pindah ke halaman 2"); langkah 35 membersihkan Filter; langkah 16 mengembalikan page size ke 10 sebelum TC-FA-GRP-1048.
- Temuan untuk QA:
  - TC-FA-GRP-1048 Langkah 5 tidak menyebut kata Search dan Langkah 6 tidak menyebut opsi Filter; spec memakai nilai dari fixture Warehouse A.
  - TC-FA-GRP-1047 Expected b "jumlah baris menyesuaikan pilihan" untuk page size 25, 50, dan 100 dengan N = 24 diasersi sebagai 24 baris (seluruh data).
