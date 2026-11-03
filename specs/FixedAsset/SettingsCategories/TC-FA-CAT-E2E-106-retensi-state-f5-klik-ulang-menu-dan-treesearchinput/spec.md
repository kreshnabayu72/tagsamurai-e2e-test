---
id: TC-FA-CAT-E2E-106-retensi-state-f5-klik-ulang-menu-dan-treesearchinput
title: "Retensi State Halaman: F5, Klik Ulang Menu Settings > Categories, dan Perilaku TreeSearchInput"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CAT-376
  - TC-FA-CAT-378
  - TC-FA-CAT-380
  - TC-FA-CAT-381
  - TC-FA-CAT-382
coverage:
  web: automated
---

# Retensi State Halaman: F5, Klik Ulang Menu Settings > Categories, dan Perilaku TreeSearchInput

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net` pada client CatMain (Pre-setup #20), password dari `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite. Tidak ada ganti akun di tengah spec.
- Env var `FA_TC_PASSWORD` didaftarkan di `executionConfig.environmentVariables` dan `.env.example` (nama usulan, lihat Temuan untuk QA).
- Data Pre-setup #20 (CatMain), hanya dibaca dan tidak diubah: L1 `Default Category`, `Electronics` (berisi L2 `Laptop` Code `ELEC-LT` dan `Monitor`), `Furniture`, `Peripheral` (berisi `Keyboard`, `Mouse`), `Accessory`, `Tools`, `Vehicle`, `Spare Part`. Seed client disediakan tim FE/BE (lihat Hook suite di `suite.md`); fixture `fixtures/settings-categories.json` disediakan tim FE.
- Flag Guided Tooltip halaman Categories di-set true oleh hook suite `before` untuk akun aktor (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-CAT-378: Klik ulang menu Settings > Categories mereset state

1. Klik node `Electronics` di Sidebar Category Tree
2. Ketik Search `Lap`, tekan Enter
3. Klik header Code dua kali (Descending)
4. Klik menu `Settings > Categories` pada sidebar navigasi
5. Verifikasi node kembali ke `All Categories`
6. Verifikasi Search kosong
7. Verifikasi Sort kembali default Category A-Z
8. Verifikasi Filter kosong
9. Verifikasi tabel berada di halaman 1

### TC-FA-CAT-376: F5 mempertahankan node, Search, Sort, Filter, dan paginasi

10. Klik node `Electronics` di Sidebar Category Tree
11. Ketik Search `Lap`, tekan Enter
12. Klik header Code dua kali (Descending)
13. Terapkan Filter Total Asset Min `0` lalu klik `[Apply]`
14. Catat halaman aktif dan jumlah baris per halaman (baseline)
15. Expand node `Peripheral` di Sidebar Category Tree
16. Ketik `Mon` pada TreeSearchInput, tekan Enter
17. Tekan F5
18. Verifikasi node `Electronics` tetap terpilih
19. Verifikasi Category Context Header tetap `Electronics`
20. Verifikasi Search `Lap` tetap ter-Apply
21. Verifikasi Sort Code Descending tetap ter-Apply
22. Verifikasi Filter Total Asset Min `0` tetap ter-Apply
23. Verifikasi halaman aktif dan jumlah baris per halaman sama dengan baseline langkah 14
24. Verifikasi isi TreeSearchInput kosong kembali
25. Verifikasi node `Peripheral` tampil dan tidak lagi ter-expand

### TC-FA-CAT-380: TreeSearchInput berjalan saat Enter dan mencocokkan Name dan Code

26. Klik menu `Settings > Categories` pada sidebar navigasi untuk mereset state
27. Ketik `lt` pada TreeSearchInput tanpa menekan Enter
28. Verifikasi pohon tidak berubah (seluruh node L1 tetap tampil)
29. Tekan `Enter`
30. Verifikasi node `Laptop` tampil karena Code `ELEC-LT` mengandung `lt`
31. Verifikasi ancestor `Electronics` tetap tampil dan ter-expand
32. Verifikasi node yang tidak cocok disembunyikan

### TC-FA-CAT-381: TreeSearchInput tanpa hasil

33. Ganti isi TreeSearchInput dengan `zzzz`, tekan Enter
34. Verifikasi area pohon menampilkan Title `No results found`
35. Verifikasi area pohon menampilkan Description `Try adjusting your search or filter.`

### TC-FA-CAT-382: Mengosongkan TreeSearchInput mereset pohon dan tidak memengaruhi tabel

36. Kosongkan isi TreeSearchInput, tekan Enter
37. Klik node `Electronics` di Sidebar Category Tree
38. Catat isi tabel (baseline)
39. Ketik `Fur` pada TreeSearchInput, tekan Enter
40. Verifikasi Category Context Header tetap `Electronics` selama pencarian
41. Verifikasi isi tabel sama dengan baseline langkah 38 selama pencarian
42. Kosongkan isi TreeSearchInput, tekan Enter
43. Verifikasi pohon kembali tanpa filter (seluruh node L1 tampil)

## Notes

- Langkah penghubung (S-03): langkah 14 dan 38 (mencatat baseline), 26 (reset state lewat klik ulang menu, S-09), 36 (mengosongkan pencarian pohon sebelum TC-382).
- Urutan TC: TC-378 dijalankan lebih dulu karena berakhir pada state bersih. TC-FA-CAT-379 (tab baru memulai dari default) ada di spec TC-FA-CAT-E2E-203.
- Langkah 15 (expand `Peripheral`) ditulis sebelum langkah 16 karena pencarian `Mon` menyembunyikan `Peripheral`; TC menulis urutan sebaliknya (lihat Temuan untuk QA).
- Ambang sekitar 35 langkah terlampaui (43 langkah). Alasan: seluruh TC satu halaman, satu dataset CatMain, dan satu kelas harness (retensi state dan TreeSearchInput); tiap TC berdiri sendiri dan kegagalan satu TC tidak membuat TC lain kehilangan makna.
- Temuan untuk QA:
  - TC-376 menulis "ketik `Mon` pada TreeSearchInput lalu expand node `Peripheral`", padahal pencarian `Mon` menyembunyikan node tak cocok termasuk `Peripheral` (TC-380); spec meng-expand `Peripheral` sebelum mengetik.
  - TC-376 menyebut "halaman aktif dan jumlah baris per halaman tetap", tetapi hasil Search `Lap` pada node `Electronics` hanya satu baris sehingga halaman selain 1 tidak teramati.
  - TC-382 tidak menyebut cara membuat node `Electronics` terlihat sesudah TC-381; langkah 36 mengosongkan pencarian pohon terlebih dahulu.
  - Nama env var password aktor tidak tertulis di TC; `FA_TC_PASSWORD` adalah usulan.
