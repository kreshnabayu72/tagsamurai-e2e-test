---
id: TC-FA-MYASSET-UI-109-tabel-borrowed-mekanik-search-sort-paginasi
title: "Tabel Borrowed: siklus kotak Search, indikator sort, paginasi, dan teks sel bermarkup"
layer: ui-client
priority: Medium
caseType: Positive
status: draft
sourceRules: ["§5#r2", "EB-TBL-7@tabel-borrowed", "EB-TBL-8@tabel-borrowed", "EB-SRC-4@tabel-borrowed", "EB-SRT-3@tabel-borrowed"]
smoke: []
dependsOn: []
trace:
  "§5#r2": [2, 3, 4, 8, 10, 23, 24, 27, 29, 53, 55]
  "EB-TBL-7@tabel-borrowed": [7, 14, 16, 18, 21, 34]
  "EB-TBL-8@tabel-borrowed": 67
  "EB-SRC-4@tabel-borrowed": [47, 49, 51, 52, 57, 58, 60, 62, 64, 65]
  "EB-SRT-3@tabel-borrowed": [33, 36, 38, 41, 42, 43]
anchor: []
coverage:
  web: automated
---

# Tabel Borrowed: siklus kotak Search, indikator sort, paginasi, dan teks sel bermarkup

## Prerequisites
- Aktor: Borrower.
- Layar awal: My Asset > tab Borrowed.
- Komponen: Tabel Borrowed (T-MYA-02)
- Data:
  - DU-109-1: 14 baris pinjaman dengan Name `Projector Epson EB-X06 - {n}` (n dari 1 sampai 14), Asset ID `PRJ-2026-{n}`, Brand `—`, Model/Type `—`, Group `Head Office`, Status `Borrowed`, Due Date `10/11/26`, Remaining `Due in 1 day`, Borrower `Me`, Transaction ID `BRW-2026-{n}`, Source `Admin`, Duration `4 days`, Handed Over At `07/11/26, 09:00`.
  - DU-109-2: 12 baris pinjaman dengan Name `Laptop Dell Latitude 5420 - {n}` (n dari 1 sampai 12), Asset ID `LPT-2026-{n}`, Brand `—`, Model/Type `—`, Group `Head Office`, Status `Borrowed`, Due Date `10/11/26`, Remaining `Due in 1 day`, Borrower `Me`, Transaction ID `BRW-2026-2{n}`, Source `Admin`, Duration `4 days`, Handed Over At `07/11/26, 09:00`.
  - DU-109-3: 10 baris pinjaman dengan Name `Meeting Mic Set - {n}` (n dari 1 sampai 10), Asset ID `MIC-2026-{n}`, Brand `—`, Model/Type `—`, Group `Head Office`, Status `Borrowed`, Due Date `10/11/26`, Remaining `Due in 1 day`, Borrower `Me`, Transaction ID `BRW-2026-3{n}`, Source `Self-service`, Duration `3 days`, Handed Over At `07/11/26, 09:10`.
  - DU-109-4: 101 baris pinjaman dengan Name `Scanner Zebra DS2208 - {n}` (n dari 1 sampai 101), Asset ID `SCN-2026-{n}`, Brand `—`, Model/Type `—`, Group `Head Office`, Status `Borrowed`, Due Date `10/11/26`, Remaining `Due in 1 day`, Borrower `Me`, Transaction ID `BRW-2026-4{n}`, Source `Admin`, Duration `4 days`, Handed Over At `07/11/26, 09:00`.
  - DU-109-5: satu baris pinjaman dengan Name `<b>Kamera Canon EOS R6</b> - 1`, Asset ID `CAM-2026-0001`, Brand `—`, Model/Type `—`, Group `Head Office`, Status `Borrowed`, Due Date `10/11/26`, Remaining `Due in 1 day`, Borrower `Me`, Transaction ID `BRW-2026-0501`, Source `Admin`, Duration `4 days`, Handed Over At `07/11/26, 09:00`.
  - DU-109-6: nomor halaman yang diketik di kolom lompat ke halaman: `-1` (di bawah 1), `4` (halaman terakhir ditambah satu), `0` (di bawah 1), dan `abc` (bukan angka).
  - DU-109-7: kata kunci Search `Laptop`.
  - Jumlah halaman untuk 26 baris (DU-109-1 dan DU-109-2) pada ukuran halaman `10` adalah `3`, dari 26 baris dibagi 10 per halaman dan dibulatkan ke atas.
- Kondisi:
  - K1: daftar berisi DU-109-1 lalu DU-109-2 (26 baris, urutan itu), dan pencarian dengan kata kunci DU-109-7 dijawab dengan DU-109-2 saja (12 baris). Date Format bernilai `dd/MM/yy`.
  - K2: daftar berisi DU-109-3 saja (10 baris).
  - K3: daftar berisi DU-109-4 saja (101 baris).
  - K4: daftar berisi DU-109-5 saja.

## Test Steps

### Ukuran halaman bawaan dan pilihan ukuran halaman
1. Tampilkan Tabel Borrowed dengan kondisi K1
2. Verifikasi ukuran halaman bawaan adalah `10`
3. Verifikasi pilihan ukuran halaman hanya `10`, `25`, `50`, dan `100`, tanpa opsi `All`
4. Verifikasi halaman `1` menampilkan `10` baris, dari `Projector Epson EB-X06 - 1` sampai `Projector Epson EB-X06 - 10`
5. Klik halaman `2`
6. Pilih ukuran halaman `25`
7. Verifikasi halaman aktif kembali ke `1` sesudah ukuran halaman diganti
8. Verifikasi halaman `1` menampilkan `25` baris pada ukuran halaman `25`
9. Klik halaman `2`
10. Verifikasi halaman `2` menampilkan `1` baris, yaitu `Laptop Dell Latitude 5420 - 12`

### Nomor halaman tidak valid dijepit ke batas atau diabaikan
11. Tampilkan Tabel Borrowed dengan kondisi K1
12. Klik halaman `2`
13. Isi kolom lompat ke halaman dengan `-1`, tekan Enter
14. Verifikasi halaman aktif `1` sesudah nomor di bawah 1 diketik
15. Isi kolom lompat ke halaman dengan `4`, tekan Enter
16. Verifikasi halaman aktif `3`, halaman terakhir, sesudah nomor di atas halaman terakhir diketik
17. Isi kolom lompat ke halaman dengan `0`, tekan Enter
18. Verifikasi halaman aktif `1` sesudah nomor `0` diketik
19. Klik halaman `2`
20. Isi kolom lompat ke halaman dengan `abc`, tekan Enter
21. Verifikasi halaman aktif tetap `2` sesudah input bukan angka

### Daftar yang pas satu halaman
22. Tampilkan Tabel Borrowed dengan kondisi K2
23. Verifikasi halaman `1` menampilkan `10` baris, dari `Meeting Mic Set - 1` sampai `Meeting Mic Set - 10`
24. Verifikasi tombol `Next Page` dan `Last Page` disabled

### Ukuran halaman maksimum
25. Tampilkan Tabel Borrowed dengan kondisi K3
26. Pilih ukuran halaman `100`
27. Verifikasi halaman `1` menampilkan `100` baris pada ukuran halaman `100`
28. Klik halaman `2`
29. Verifikasi halaman `2` menampilkan `1` baris, yaitu `Scanner Zebra DS2208 - 101`

### Siklus tiga klik sort dan kolom tanpa ikon sort
30. Tampilkan Tabel Borrowed dengan kondisi K1
31. Klik halaman `2`
32. Klik ikon sort pada header `Name`
33. Verifikasi indikator sort naik aktif pada header `Name`
34. Verifikasi halaman aktif tetap `2` sesudah sort diganti
35. Klik ikon sort pada header `Name`
36. Verifikasi indikator sort turun aktif pada header `Name`
37. Klik ikon sort pada header `Name`
38. Verifikasi header `Name` tidak lagi memiliki indikator sort aktif
39. Klik ikon sort pada header `Name`
40. Klik ikon sort pada header `Asset ID`
41. Verifikasi indikator sort naik aktif pada header `Asset ID`
42. Verifikasi indikator sort berpindah dari header `Name`, yang kembali netral
43. Verifikasi header `Photo` tidak memiliki ikon sort

### Siklus kotak Search
44. Tampilkan Tabel Borrowed dengan kondisi K1
45. Klik halaman `2`
46. Klik ikon Search
47. Verifikasi input Search terbuka dan fokus berada di input itu
48. Ketik Search `Laptop`
49. Verifikasi tabel belum berubah sebelum Enter: `Projector Epson EB-X06 - 11` masih tampil
50. Tekan Enter
51. Verifikasi hasil pencarian tampil: `Laptop Dell Latitude 5420 - 10`
52. Verifikasi `Projector Epson EB-X06 - 11` tidak tampil sesudah pencarian dijalankan
53. Verifikasi halaman aktif kembali ke `1` sesudah pencarian dijalankan
54. Klik halaman `2`
55. Verifikasi hasil pencarian yang lebih dari satu halaman memiliki halaman `2` dengan `Laptop Dell Latitude 5420 - 12`
56. Klik `(✕)` pada kotak Search
57. Verifikasi isi input Search terhapus
58. Verifikasi `Laptop Dell Latitude 5420 - 12` masih tampil, karena `(✕)` tidak mereset tabel
59. Tekan Enter pada kotak Search yang kosong
60. Verifikasi tabel kembali ke daftar penuh: `Projector Epson EB-X06 - 1` tampil
61. Ketik Search `Laptop`, tekan Enter
62. Verifikasi pencarian berjalan lagi: `Laptop Dell Latitude 5420 - 9` tampil
63. Klik `(←)` pada kotak Search
64. Verifikasi kotak Search tertutup
65. Verifikasi tabel kembali menampilkan `Projector Epson EB-X06 - 2` sesudah kotak Search ditutup

### Teks sel bermarkup tampil apa adanya
66. Tampilkan Tabel Borrowed dengan kondisi K4
67. Verifikasi sel `Name` menampilkan teks `<b>Kamera Canon EOS R6</b> - 1` apa adanya
