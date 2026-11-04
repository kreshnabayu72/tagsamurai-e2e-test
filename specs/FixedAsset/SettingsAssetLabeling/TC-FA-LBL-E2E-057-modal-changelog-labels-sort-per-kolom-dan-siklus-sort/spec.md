---
id: TC-FA-LBL-E2E-057-modal-changelog-labels-sort-per-kolom-dan-siklus-sort
title: "Modal Changelog: Labels: Sort per kolom, siklus Sort, dan urutan Old Value dan New Value campuran"
priority: Medium
caseType: Positive
status: draft
sourceRules:
  - FALB:obl/T-ALB-03/sort-cycle
  - FALB:obl/T-ALB-03/sort/FLD-11
  - FALB:obl/T-ALB-03/sort/FLD-12
  - FALB:obl/T-ALB-03/sort/FLD-13
  - FALB:obl/T-ALB-03/sort/FLD-14
  - FALB:obl/T-ALB-03/sort/FLD-15
  - FALB:obl/T-ALB-03/sort/FLD-16
  - FALB:obl/T-ALB-03/sort/FLD-17
coverage:
  web: automated
---

# Modal Changelog: Labels: Sort per kolom, siklus Sort, dan urutan Old Value dan New Value campuran

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control (`DU-01`), env `FA_TC_EMAIL` dan `FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Settings > Asset Master > tab Labels dibuka hook `beforeEach` suite. Pelaku kedua seeding lewat sesi API: `DU-31`, env `FA_TC2_EMAIL` dan `FA_TC2_PASSWORD`.
- Data uji `DU-62` (Dataset Changelog: Labels), bersuffix `{runId}-057`, label `Log-{runId}-057-nn`, dibuat lewat sesi API di hook `before` dalam dua kelompok Date yang dipisah pergantian menit (hook menunggu sampai menit berganti, maksimum 60 detik, konvensi bagian 6): kelompok 1 = Create `-01` dan `-04` sampai `-09` oleh `DU-01`; kelompok 2 = Edit Label Name `-01` menjadi `-01-baru` oleh `DU-31`, Edit Color `-01` dari `#3B82F6` ke `#EF4444` oleh `DU-31`, Create `-02` oleh `DU-31`, Create `-03` oleh `DU-01`, lalu Delete `-03` oleh `DU-01`. Total 12 entri; urutan entri se-menit tidak diasersi. Hook `after` menghapus label `-01-baru`, `-02`, dan `-04` sampai `-09` lewat sesi API.
- Kemampuan teknis: sesi API aktor dan fixture BE untuk seeding label dan membaca entri Changelog, disediakan tim FE/BE.
- State global: tidak ada yang diubah; Sort adalah state tampilan Modal Changelog. Suite berjalan serial (`parallel: false`).

## Test Steps

1. Klik ikon Changelog pada toolbar tabel
2. Ketik Search `DU-62`, tekan Enter
3. Pilih 25 pada pilihan jumlah baris per halaman
4. Verifikasi dua belas baris entri `DU-62`, termasuk entri Create `-04` dan entri Delete `-03` dari dua kelompok Date berbeda, tampil pada satu halaman

### FALB:obl/T-ALB-03/sort-cycle: Siklus sort: satu kolom aktif, naik, turun, dan netral

5. Klik header kolom Date
6. Verifikasi indikator sort naik aktif pada header kolom Date sedangkan header kolom lain netral
7. Klik header kolom Date
8. Verifikasi indikator sort turun aktif pada header kolom Date
9. Klik header kolom Date
10. Verifikasi indikator sort netral pada header kolom Date dan baris pertama kembali berupa entri Delete label `-03` (urutan default Newest First)
11. Klik header kolom Action, lalu klik header kolom Label Name
12. Verifikasi indikator sort naik aktif hanya pada header kolom Label Name sedangkan header kolom Action netral

### FALB:obl/T-ALB-03/sort/FLD-11: Sort kolom Date: Oldest First dan Newest First

13. Klik header kolom Date
14. Verifikasi entri Create label `-04` tampil di atas entri Delete label `-03` (Oldest First)
15. Klik header kolom Date
16. Verifikasi entri Delete label `-03` tampil di atas entri Create label `-04` (Newest First)

### FALB:obl/T-ALB-03/sort/FLD-12: Sort kolom Action: Alphabetical (A-Z)

17. Klik header kolom Action
18. Verifikasi baris pertama memiliki Action `Create` dan baris terakhir memiliki Action `Edit`
19. Klik header kolom Action
20. Verifikasi baris pertama memiliki Action `Edit` dan baris terakhir memiliki Action `Create`

### FALB:obl/T-ALB-03/sort/FLD-13: Sort kolom Label Name: Alphabetical (A-Z)

21. Klik header kolom Label Name
22. Verifikasi baris Create label `-04` tampil di atas baris Create label `-09`
23. Klik header kolom Label Name
24. Verifikasi baris Create label `-09` tampil di atas baris Create label `-04`

### FALB:obl/T-ALB-03/sort/FLD-14: Sort kolom Field: Alphabetical (A-Z)

25. Klik header kolom Field
26. Verifikasi baris Edit dengan Field `Color` tampil di atas baris Create dengan Field `Label Name`
27. Klik header kolom Field
28. Verifikasi baris Create dengan Field `Label Name` tampil di atas baris Edit dengan Field `Color`

### FALB:obl/T-ALB-03/sort/FLD-15: Sort kolom Old Value: kolom campuran tipe

29. Klik header kolom Old Value
30. Verifikasi baris Edit Color dengan Old Value `#3B82F6` tampil di atas baris Edit dengan Field `Label Name` dengan Old Value `Log-{runId}-057-01`
31. Verifikasi baris terakhir memiliki Old Value `—`
32. Klik header kolom Old Value
33. Verifikasi baris pertama memiliki Old Value `—`

### FALB:obl/T-ALB-03/sort/FLD-16: Sort kolom New Value: kolom campuran tipe

34. Klik header kolom New Value
35. Verifikasi baris Edit Color dengan New Value `#EF4444` tampil di atas baris Create label `-04` dengan New Value nama label `Log-{runId}-057-04`
36. Verifikasi baris terakhir memiliki New Value `—`
37. Klik header kolom New Value
38. Verifikasi baris pertama memiliki New Value `—`

### FALB:obl/T-ALB-03/sort/FLD-17: Sort kolom Modified By: Alphabetical (A-Z) menurut nama lengkap

39. Klik header kolom Modified By
40. Arahkan kursor ke sel Modified By baris pertama, catat nama lengkap pada tooltip sebagai nama A
41. Arahkan kursor ke sel Modified By baris terakhir, catat nama lengkap pada tooltip sebagai nama B
42. Verifikasi nama A secara alfabetis tidak berada setelah nama B menurut nama lengkap
43. Klik header kolom Modified By
44. Arahkan kursor ke sel Modified By baris pertama
45. Verifikasi tooltip baris pertama menampilkan nama B

## Notes

- Langkah penghubung (S-03): langkah 1 membuka modal; langkah 2 mempersempit tabel ke entri `DU-62` (R-16); langkah 3 memperbesar ukuran halaman agar kedua belas entri berada pada satu halaman; langkah 11 memindahkan sort aktif dari Action ke Label Name tanpa asersi sendiri; langkah 40, 41, dan 44 hanya menggerakkan kursor.
- Asersi urutan memakai Search `DU-62` (bagian 8b butir 15a); langkah 4 memverifikasi sedikitnya dua baris data uji dari kelompok Date berbeda sebelum asersi sort pertama (butir 15d); asersi Date hanya membandingkan pasangan entri yang berbeda menit (langkah 14 dan 16), urutan entri se-menit tidak diasersi.
- Urutan Old Value dan New Value (langkah 30 sampai 38): aturan PRD §4.1.2 menyatakan nilai numerik berdasarkan angka, teks termasuk kode hex alfabetis tanpa membedakan huruf besar-kecil dengan collation ICU `en-US`, nilai kosong `—` di akhir saat ascending dan di awal saat descending. Dataset `DU-62` tidak memuat nilai numerik; urutan kode hex terhadap nama label mengandalkan collation ICU `en-US` (tanda `#` mendahului huruf).
- Kolom Date, Action, Label Name, Field, Old Value, New Value, dan Modified By seluruhnya sortable (Tabel 3 PRD §4.1.2).
- Alasan spec melewati 35 langkah: seluruh blok satu kelas harness (fungsional Sort Modal Changelog) dengan data `DU-62` yang sama dan pola langkah yang sama per kolom (klik naik, `Verifikasi`, klik turun, `Verifikasi`); tiap blok kolom berdiri sendiri karena memulai dari klik kolom baru yang menetralkan sort kolom sebelumnya. Pemecahan menambah login dan seeding dua kelompok Date (penantian pergantian menit) per spec.
