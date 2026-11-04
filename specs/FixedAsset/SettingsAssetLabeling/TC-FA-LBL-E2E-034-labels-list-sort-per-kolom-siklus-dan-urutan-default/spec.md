---
id: TC-FA-LBL-E2E-034-labels-list-sort-per-kolom-siklus-dan-urutan-default
title: "Labels List: Sort per kolom, siklus Sort, dan urutan default"
priority: Medium
caseType: Positive
status: draft
sourceRules:
  - FALB:obl/T-ALB-01/sort-default
  - FALB:defaults-ordering-spec/default-sort-tabel
  - FALB:obl/T-ALB-01/sort-cycle
  - FALB:obl/T-ALB-01/sort/FLD-01
  - FALB:obl/T-ALB-01/sort/FLD-02
  - FALB:obl/T-ALB-01/sort/FLD-03
  - FALB:obl/T-ALB-01/sort/FLD-04
  - FALB:obl/T-ALB-01/sort/FLD-05
  - FALB:global-table-rules/sort
coverage:
  web: automated
---

# Labels List: Sort per kolom, siklus Sort, dan urutan default

## Prerequisites

- Mode: FE+BE
- Akun aktor: Total Control `DU-01` (env `FA_TC_EMAIL`, `FA_TC_PASSWORD`). Login di hook `before` spec ini; halaman Settings > Asset Master > tab Labels dibuka hook `beforeEach` suite.
- Data uji: `DU-56` (12 label bersuffix `Lst-{runId}-034-01` sampai `Lst-{runId}-034-12`). Total Asset `DU-56` bernilai 0 sampai 3 sehingga ada label ber-Total Asset sama; Modified By berasal dari dua pelaku (`DU-01` dan `DU-31`) yang namanya berbeda; Last Updated terbagi dua kelompok seed yang berbeda menit (hook `before` menunggu pergantian menit, maksimum 60 detik, konvensi bagian 6), masing-masing kelompok berisi paling banyak 10 label. `DU-31` (akun Total Control kedua, env `FA_TC2_EMAIL`, `FA_TC2_PASSWORD`) dipakai hanya sebagai pelaku kedua lewat sesi API saat seeding; tidak login di UI.
- Kemampuan teknis (disediakan tim FE/BE): sesi API aktor dan fixture BE untuk seeding label dan aset.
- State global: tidak ada yang diubah. Hook `after` menghapus label seed `DU-56` lewat sesi API.

## Test Steps

### FALB:obl/T-ALB-01/sort-default: Urutan bawaan saat pertama dimuat

1. Ketik Search `DU-56` (nama dasar `Lst-{runId}-034`), tekan Enter
2. Verifikasi Labels List menampilkan sedikitnya dua baris label `DU-56`
3. Verifikasi baris pada halaman pertama berurutan kolom Label naik A→Z, yaitu `DU-56` ke-01 sampai ke-10

### FALB:defaults-ordering-spec/default-sort-tabel: Sort bawaan tabel

4. Verifikasi tidak ada header kolom yang menampilkan indikator sort aktif, sehingga urutan bawaan kolom Label naik (A→Z) berlaku

### FALB:obl/T-ALB-01/sort-cycle: Siklus Sort dan satu kolom aktif

5. Klik header kolom Total Asset
6. Verifikasi header kolom Total Asset menampilkan indikator naik (`↑`)
7. Klik header kolom Total Asset
8. Verifikasi header kolom Total Asset menampilkan indikator turun (`↓`)
9. Klik header kolom Total Asset
10. Verifikasi header kolom Total Asset tidak menampilkan indikator sort aktif dan baris pada halaman pertama kembali berurutan kolom Label naik A→Z
11. Klik header kolom Color Hex
12. Verifikasi header kolom Color Hex menampilkan indikator naik (`↑`)
13. Klik header kolom Last Updated
14. Verifikasi header kolom Last Updated menampilkan indikator naik (`↑`) dan header kolom Color Hex tidak menampilkan indikator sort aktif

### FALB:obl/T-ALB-01/sort/FLD-01: Sort kolom Label

15. Klik header kolom Label
16. Verifikasi baris pada halaman pertama berurutan kolom Label naik A→Z, yaitu `DU-56` ke-01 sampai ke-10
17. Klik header kolom Label
18. Verifikasi baris pada halaman pertama berurutan kolom Label turun Z→A, yaitu `DU-56` ke-12 sampai ke-03

### FALB:obl/T-ALB-01/sort/FLD-02: Sort kolom Color Hex

19. Klik header kolom Color Hex
20. Verifikasi baris pada halaman pertama berurutan kolom Color Hex naik A→Z tanpa membedakan huruf besar-kecil
21. Klik header kolom Color Hex
22. Verifikasi baris pada halaman pertama berurutan kolom Color Hex turun Z→A tanpa membedakan huruf besar-kecil

### FALB:obl/T-ALB-01/sort/FLD-03: Sort kolom Total Asset

23. Klik header kolom Total Asset
24. Verifikasi baris pada halaman pertama berurutan kolom Total Asset naik secara numerik
25. Klik header kolom Total Asset
26. Verifikasi baris pada halaman pertama berurutan kolom Total Asset turun secara numerik

### FALB:obl/T-ALB-01/sort/FLD-04: Sort kolom Modified By

27. Klik header kolom Modified By
28. Verifikasi baris pada halaman pertama berurutan kolom Modified By naik A→Z menurut nama lengkap user (bukan menurut format tampilan)
29. Klik header kolom Modified By
30. Verifikasi baris pada halaman pertama berurutan kolom Modified By turun Z→A menurut nama lengkap user (bukan menurut format tampilan)

### FALB:obl/T-ALB-01/sort/FLD-05: Sort kolom Last Updated

31. Verifikasi kolom Last Updated menampilkan dua nilai tanggal dan jam dengan menit berbeda pada baris `DU-56` (dua kelompok seed)
32. Klik header kolom Last Updated
33. Verifikasi baris kelompok seed dengan Last Updated lebih awal berada di atas baris kelompok seed berikutnya (Oldest First)
34. Klik header kolom Last Updated
35. Verifikasi baris kelompok seed dengan Last Updated lebih akhir berada di atas baris kelompok seed sebelumnya (Newest First)

### FALB:global-table-rules/sort: Sort bawaan Label, satu kolom aktif, dan urutan baris bernilai sama

36. Klik header kolom Total Asset
37. Verifikasi baris yang memiliki Total Asset sama berurutan kolom Label naik A→Z
38. Klik header kolom Total Asset dua kali berturut-turut hingga indikator sort kembali netral

## Notes

- Langkah penghubung (S-03): langkah 1 (Search yang mempersempit tabel ke label `DU-56` dan membatasi asersi urutan pada data milik spec, bagian 8b butir 15), langkah 38 (memulihkan sort ke bawaan, S-09).
- Langkah 5 sampai 9 menjalankan siklus penuh pada kolom Total Asset; langkah 11 dan 13 menunjukkan bahwa hanya satu kolom aktif pada satu waktu. Langkah 15, 19, 23, 27, dan 32 mengawali tiap blok kolom dari kolom lain yang sedang aktif, sehingga klik pertama selalu menghasilkan urutan naik.
- Asersi urutan memakai baris halaman pertama hasil Search `DU-56` (12 baris, 2 halaman), tidak bergantung pada baris data bawaan; langkah 2 membuktikan sedikitnya dua baris data uji sebelum asersi sort pertama. Asersi Last Updated hanya membandingkan dua baris dari kelompok menit berbeda; urutan baris sekelompok tidak diasersi.
- Kolom Last Updated langkah 31 menjadi anchor tampilnya Date seed sebelum asersi sort Date.
- Spec ini di atas smell 35 langkah (38 langkah). Alasan dipertahankan: seluruh blok satu kelas harness (Sort pada tabel yang sama) dengan dataset `DU-56` yang sama; tiap blok dimulai dengan klik header kolom lain sehingga tidak bergantung pada hasil blok sebelumnya, dan kegagalan satu blok tidak membuat blok lain kehilangan makna.
