---
id: TC-FA-CAT-E2E-047-resilience-baca-asset-name-add-subcategory-dan-wizard-bagian-2
title: "Resilience Baca Bagian 2: Fetch Asset Name Saat Add Subcategory (5xx dan Timeout) serta Error Load Tabel Wizard Consolidation"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-CAT-645
  - TC-FA-CAT-646
  - TC-FA-CAT-454
coverage:
  web: automated
---

# Resilience Baca Bagian 2: Fetch Asset Name Saat Add Subcategory (5xx dan Timeout) serta Error Load Tabel Wizard Consolidation

## Prerequisites

- Mode: FE+BE (intercept parsial di atas backend nyata; respons pengambilan daftar Asset Name dan data tabel Wizard dipaksa 5xx atau tanpa respons lewat `Spectra.intercept()`, sedangkan state kategori dan data normal dari backend nyata diasersi).
- Akun aktor pertama: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, client CatMain (Pre-setup #20), password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Akun kedua lewat langkah Ganti akun: akun yang sama pada client CatPostT0 (Pre-setup #33). Hook `after` mengembalikan sesi ke akun default suite.
- Data Pre-setup #20 (CatMain) dan #21: `Furniture` (Code `FURN`, leaf) ditunjuk Asset Name `Office Chair`; `Furniture` hanya dibaca dan dipakai sebagai parent yang ditolak atau dibatalkan, tidak ada kategori tersimpan.
- Data Pre-setup #33 (CatPostT0, T-0 sudah lewat, Starter cap 5, 8 kategori usable): Alert Consolidation dan `[Choose Categories]` tampil bagi Total Control. Spec tidak menyimpan seleksi.
- Kemampuan teknis: membaca jumlah entri Changelog kategori sebelum dan sesudah aksi (baseline, S-12) dan membaca state BE kategori; disediakan tim FE/BE.
- Kebutuhan intercept (kelas b, fault injection; `Spectra.intercept()`):
  - TC-FA-CAT-645: respons pengambilan daftar Asset Name untuk `Furniture` dipaksa 500.
  - TC-FA-CAT-646: respons pengambilan daftar Asset Name untuk `Furniture` tidak diberikan (timeout jaringan).
  - TC-FA-CAT-454: respons data tabel Step Wizard dipaksa 5xx.
  Intercept dilepas segera setelah pemicu selesai dan dipulihkan di hook `after` bila spec gagal di tengah. Endpoint yang di-intercept mengikuti halaman; tidak ada endpoint karangan.
- Suite berjalan serial (`parallel: false`).
- Env var `FA_TC_PASSWORD` didaftarkan di `executionConfig.environmentVariables` dan `.env.example`.

## Test Steps

### TC-FA-CAT-645: Gagal mengambil daftar Asset Name (5xx) saat klik Add Subcategory

1. Paksa respons pengambilan daftar Asset Name untuk `Furniture` menjadi 500 lewat intercept jaringan
2. Catat baseline jumlah entri Changelog kategori (N1)
3. Klik elipsis (⋯) pada baris `Furniture` > `+ Add Subcategory`
4. Verifikasi toast error `Error, failed to create category.` tampil tanpa tombol aksi
5. Verifikasi dialog heads-up D-05 tidak terbuka
6. Verifikasi popup New Subcategory tidak terbuka
7. Verifikasi `Furniture` tetap leaf (tidak punya anak, dibaca dari state BE)
8. Verifikasi jumlah entri Changelog sama dengan N1 (tidak ada baris log)
9. Lepas intercept respons pengambilan daftar Asset Name
10. Klik elipsis (⋯) pada baris `Furniture` > `+ Add Subcategory`
11. Verifikasi dialog `Add Subcategory` tampil dengan bullet `Furniture` dan bullet `Office Chair`
12. Klik `[Cancel]` pada dialog

### TC-FA-CAT-646: Pengambilan daftar Asset Name tanpa respons (timeout jaringan)

13. Putus respons pengambilan daftar Asset Name untuk `Furniture` lewat intercept jaringan (tidak ada respons)
14. Catat baseline jumlah entri Changelog kategori (N2)
15. Klik elipsis (⋯) pada baris `Furniture` > `+ Add Subcategory`
16. Verifikasi toast error baku `Connection problem. Please try again.` tampil tanpa tombol aksi
17. Verifikasi toast error T-02 `Error, failed to create category.` tidak tampil
18. Verifikasi dialog heads-up D-05 tidak terbuka
19. Verifikasi popup New Subcategory tidak terbuka
20. Verifikasi `Furniture` tetap leaf (tidak punya anak, dibaca dari state BE)
21. Verifikasi jumlah entri Changelog sama dengan N2 (tidak ada baris log)
22. Pulihkan jaringan (lepas intercept respons pengambilan daftar Asset Name)
23. Klik elipsis (⋯) pada baris `Furniture` > `+ Add Subcategory`
24. Verifikasi dialog `Add Subcategory` tampil
25. Klik `[Cancel]` pada dialog
26. Verifikasi dialog `Add Subcategory` tertutup
27. Verifikasi `Furniture` tetap leaf (tanpa efek, dibaca dari state BE)

### TC-FA-CAT-454: Search tanpa hasil dan error load tabel Step Wizard

28. Ganti akun: logout, lalu login sebagai Total Control `totalControl_automated_{namaCompany}@qwertysystem.net` pada client CatPostT0 dengan `Spectra.env.FA_TC_PASSWORD`
29. Klik `[Choose Categories]` pada Alert Category Consolidation
30. Ketik Search `zzzz`, tekan Enter
31. Verifikasi Title `No results found` dan Description `Try adjusting your search or filter.` tampil
32. Klik `(←)` pada kotak Search
33. Klik icon close (✕) pada popup Consolidation
34. Paksa respons data tabel Step Wizard gagal 5xx lewat intercept jaringan
35. Klik `[Choose Categories]` pada Alert Category Consolidation
36. Verifikasi area tabel Step menampilkan `Unable to load this data.` dan `[Try Again]`
37. Lepas intercept respons data tabel Step
38. Klik icon close (✕) pada popup Consolidation

## Notes

- Mode: FE+BE (kelas b, fault injection). Tiga blok berdiri sendiri dan satu kelas harness; kegagalan satu blok tidak menghilangkan makna blok lain, sehingga jumlah langkah (38) sedikit melewati sekitar 35. TC-FA-CAT-13, 287, dan 415 ada di spec 046.
- Langkah penghubung (S-03, S-09): langkah 9, 22, 37 (melepas intercept), langkah 12 dan 25 (menutup dialog heads-up D-05 yang dibuka sesudah intercept dilepas), langkah 32 sampai 33 dan 38 (mengosongkan Search dan menutup popup Consolidation tanpa seleksi), langkah 28 (ganti akun eksplisit, S-07), langkah 2 dan 14 (baseline log, S-12).
- Asersi "tidak ada baris log" (langkah 8, 21) ditulis dengan baseline di spec ini; kedua TC tidak punya spec absence yang memuat aksinya (S-05). Surface yang diperiksa hanya Changelog.
- Temuan untuk QA:
  - TC-FA-CAT-645 dan 646 menyebut "tidak ada baris log" tanpa menyebut surface log; spec memeriksa Changelog saja.
  - TC-FA-CAT-646 Expected c menyebut `[Cancel]` menutup dialog "tanpa efek"; spec memverifikasi dialog tertutup dan `Furniture` tetap leaf.
  - TC-FA-CAT-454 tidak menyebut langkah pemulihan Search sebelum mengulang dengan 5xx; spec menambah langkah 32 (S-03).
- Spec melewati 35 langkah (38 langkah). Alasan: satu kelas harness dan satu dataset; Expected dipecah per klausa (S-01) dan blok berdiri sendiri; nomor cadangan slice habis sehingga tidak dipecah lebih jauh.
