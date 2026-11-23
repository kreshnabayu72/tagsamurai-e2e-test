---
id: TC-FA-FAFM-UI-084-tabel-files-paginasi
title: "Tabel Files: paginasi dan ukuran halaman"
layer: ui-client
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["TBL-02a", "TBL-02b", "EB-TBL-7@tabel-files"]
smoke: []
dependsOn: []
trace:
  "TBL-02a": [2, 3, 22, 23, 25, 26, 27, 31, 33]
  "TBL-02b": [5, 6, 11, 14, 17, 19]
  "EB-TBL-7@tabel-files": [9, 11, 12, 36, 38, 39, 42, 45, 49, 52, 55]
anchor: []
coverage:
  web: automated
---

# Tabel Files: paginasi dan ukuran halaman

## Prerequisites
- Aktor: Total Control.
- Layar awal: Tabel File Manager tab Files.
- Komponen: Tabel File Manager tab Files.
- Data:
  - DU-084-1: 23 file `Asset Photo` bernama `site-photo-{n}.jpg` (n = 1 sampai 23), Asset `Laptop Dell Latitude 5420 - 4`, Group `Head Office`; dengan ukuran halaman 10, laporan halaman 1 `Showing 1 to 10 of 23`, halaman 2 `Showing 11 to 20 of 23`, halaman 3 `Showing 21 to 23 of 23`.
  - DU-084-2: 11 file `Asset Photo` bernama `site-photo-{n}.jpg` (n = 1 sampai 11); dengan ukuran halaman 10, laporan halaman 2 `Showing 11 to 11 of 11`.
  - DU-084-3: 10 file `Asset Photo` bernama `site-photo-{n}.jpg` (n = 1 sampai 10); laporan halaman 1 `Showing 1 to 10 of 10`.
  - DU-084-4: 26 file `Asset Photo` bernama `site-photo-{n}.jpg` (n = 1 sampai 26); dengan ukuran halaman 10, laporan halaman 2 `Showing 11 to 20 of 26`; dengan ukuran halaman 25, laporan halaman 1 `Showing 1 to 25 of 26` dan halaman 2 `Showing 26 to 26 of 26`.
  - DU-084-5: 101 file `Asset Photo` bernama `site-photo-{n}.jpg` (n = 1 sampai 101); dengan ukuran halaman 100, laporan halaman 1 `Showing 1 to 100 of 101` dan halaman 2 `Showing 101 to 101 of 101`.
  - DU-084-6: 12 file Source `Attachment` bernama `contract-{n}.pdf` (n = 1 sampai 12); dengan ukuran halaman 10, laporan halaman 1 `Showing 1 to 10 of 12` dan halaman 2 `Showing 11 to 12 of 12`.
  - DU-084-7: 18 file Source `Attachment` bernama `survey-{n}.pdf` (n = 1 sampai 18); tidak cocok dengan kata kunci `contract`.
  - DU-084-8: input nomor halaman uji: nol `0`, negatif `-1`, melebihi halaman terakhir `4`, dan non-angka `abc`.
- Kondisi:
  - Semua kondisi: data dimuat per halaman dari server; ukuran halaman bawaan 10; belum ada Search, filter, atau sort yang diklik.
  - K1: tab `Asset Photo` aktif; tabel berisi DU-084-1.
  - K2: tab `Asset Photo` aktif; tabel berisi DU-084-2.
  - K3: tab `Asset Photo` aktif; tabel berisi DU-084-3.
  - K4: tab `Asset Photo` aktif; tabel berisi DU-084-4.
  - K5: tab `Asset Photo` aktif; tabel berisi DU-084-5.
  - K6: tab `Asset Documents` aktif; tabel berisi DU-084-6 dan DU-084-7 (30 file).

## Test Steps

### Ukuran halaman bawaan dan pilihan ukuran
1. Tampilkan Tabel File Manager tab Files dengan kondisi K1
2. Verifikasi laporan `Showing 1 to 10 of 23` tampil
3. Verifikasi dropdown `Rows per page` menampilkan ukuran terpilih `10`
4. Buka dropdown `Rows per page`
5. Verifikasi pilihan ukuran halaman tampil sebagai himpunan `10`, `25`, `50`, dan `100`
6. Verifikasi pilihan ukuran `All` tidak tampil

### Ganti ukuran halaman kembali ke halaman 1
7. Tampilkan Tabel File Manager tab Files dengan kondisi K4
8. Klik halaman `2`
9. Verifikasi laporan `Showing 11 to 20 of 26` tampil
10. Pilih ukuran `25` pada dropdown `Rows per page`
11. Verifikasi laporan `Showing 1 to 25 of 26` tampil
12. Verifikasi halaman `1` menjadi halaman aktif
13. Klik halaman `2`
14. Verifikasi laporan `Showing 26 to 26 of 26` tampil

### Data lebih banyak dari ukuran maksimum 100
15. Tampilkan Tabel File Manager tab Files dengan kondisi K5
16. Pilih ukuran `100` pada dropdown `Rows per page`
17. Verifikasi laporan `Showing 1 to 100 of 101` tampil
18. Klik halaman `2`
19. Verifikasi laporan `Showing 101 to 101 of 101` tampil

### Satu baris di halaman terakhir
20. Tampilkan Tabel File Manager tab Files dengan kondisi K2
21. Klik halaman `2`
22. Verifikasi laporan `Showing 11 to 11 of 11` tampil
23. Verifikasi tombol `Next Page` tidak dapat diklik

### Data tepat sebesar ukuran halaman
24. Tampilkan Tabel File Manager tab Files dengan kondisi K3
25. Verifikasi laporan `Showing 1 to 10 of 10` tampil
26. Verifikasi tombol halaman `1` tampil
27. Verifikasi tombol halaman `2` tidak tampil

### Hasil Search lebih dari satu halaman
28. Tampilkan Tabel File Manager tab Files dengan kondisi K6
29. Isi kotak Search dengan `contract`
30. Tekan Enter
31. Verifikasi laporan `Showing 1 to 10 of 12` tampil
32. Klik halaman `2`
33. Verifikasi laporan `Showing 11 to 12 of 12` tampil

### Ganti sort tetap di halaman sekarang
34. Tampilkan Tabel File Manager tab Files dengan kondisi K1
35. Klik halaman `2`
36. Verifikasi laporan `Showing 11 to 20 of 23` tampil
37. Klik header kolom `File Name`
38. Verifikasi laporan `Showing 11 to 20 of 23` tetap tampil setelah sort diganti
39. Verifikasi halaman `2` tetap menjadi halaman aktif

### Nomor halaman tidak valid
40. Tampilkan Tabel File Manager tab Files dengan kondisi K1
41. Klik halaman `2`
42. Verifikasi laporan `Showing 11 to 20 of 23` tampil
43. Isi kolom `Jump to page` dengan `0`
44. Tekan Enter
45. Verifikasi laporan `Showing 1 to 10 of 23` tampil setelah nomor `0`
46. Klik halaman `2`
47. Isi kolom `Jump to page` dengan `-1`
48. Tekan Enter
49. Verifikasi laporan `Showing 1 to 10 of 23` tampil setelah nomor `-1`
50. Isi kolom `Jump to page` dengan `4`
51. Tekan Enter
52. Verifikasi laporan `Showing 21 to 23 of 23` tampil setelah nomor `4`
53. Isi kolom `Jump to page` dengan `abc`
54. Tekan Enter
55. Verifikasi laporan `Showing 21 to 23 of 23` tetap tampil setelah input `abc`
