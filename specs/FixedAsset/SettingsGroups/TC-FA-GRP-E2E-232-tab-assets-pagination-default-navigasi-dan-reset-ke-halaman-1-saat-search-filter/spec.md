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

1. Ketik Search `Warehouse A`, tekan Enter
2. Klik angka Total Asset Warehouse A
3. Verifikasi footer pagination menampilkan default 10 baris per halaman
4. Verifikasi tabel menampilkan 10 baris
5. Buka dropdown page size
6. Verifikasi pilihan page size: 10 / 25 / 50 / 100
7. Verifikasi dropdown page size tidak memuat opsi All
8. Pilih page size 25
9. Verifikasi tabel menampilkan 24 baris (seluruh aset aktif, kurang dari 25)
10. Buka dropdown page size
11. Pilih page size 50
12. Verifikasi tabel menampilkan 24 baris
13. Buka dropdown page size
14. Pilih page size 100
15. Verifikasi tabel menampilkan 24 baris
16. Buka dropdown page size
17. Pilih page size 10
18. Verifikasi tabel menampilkan 10 baris

### TC-FA-GRP-1048: Navigasi, input nomor halaman, dan reset ke halaman 1

19. Klik next
20. Verifikasi tabel berpindah ke halaman 2
21. Klik prev
22. Verifikasi tabel berpindah ke halaman 1
23. Ketik nomor halaman 2 di input halaman, tekan Enter
24. Verifikasi halaman 2 terbuka
25. Ketik Search `<kata cocok>`, tekan Enter
26. Verifikasi tabel menampilkan sedikitnya satu baris hasil Search
27. Verifikasi tabel menampilkan halaman 1 dari hasil Search
28. Klik `(←)` pada kotak Search
29. Klik next
30. Verifikasi tabel berada di halaman 2
31. Klik icon Filter
32. Pilih satu opsi Status
33. Klik [Apply]
34. Verifikasi tabel menampilkan sedikitnya satu baris hasil Filter
35. Verifikasi tabel menampilkan halaman 1 dari hasil Filter
36. Klik icon Filter, hapus pilihan Status, klik [Apply]

## Notes

- Subjudul `###` memetakan langkah ke id TC granular. `<kata cocok>` pada langkah 25 adalah kata Search dari fixture Warehouse A.
- Langkah penghubung (S-03): langkah 28 mengosongkan Search sebelum navigasi berikutnya; langkah 29 dan 30 mengembalikan tabel ke halaman 2 sebelum Filter (Langkah 6 TC: "Pindah ke halaman 2"); langkah 36 membuka kembali Filter Panel (menutup sesudah [Apply] langkah 33) lalu membersihkan Filter; langkah 17 mengembalikan page size ke 10 sebelum TC-FA-GRP-1048.
- Baris target dicari lewat Search nama (client memiliki lebih dari 10 node level 1 dan page size 10, sehingga posisi baris di halaman 1 tidak diandalkan). Langkah Search adalah langkah penghubung (S-03, R-16).
- Spec memiliki 36 langkah, di atas smell 35 langkah. Alasan: seluruh blok satu topik (pagination Tab Assets) pada satu dataset Warehouse A; TC-FA-GRP-1047 memuat klausa Expected terpisah untuk tiap pilihan page size (S-01) dan tiap blok berdiri sendiri.
- Temuan untuk QA:
  - TC-FA-GRP-1048 Langkah 6 tidak menyebut kata Search dan Langkah 7 tidak menyebut opsi Filter; spec memakai nilai dari fixture Warehouse A.
  - TC-FA-GRP-1047 Expected b "jumlah baris menyesuaikan pilihan" untuk page size 25, 50, dan 100 dengan N = 24 diasersi sebagai 24 baris (seluruh data).
