---
id: TC-FA-FAREG-BE-129-daftar-search-sort-filter
title: "Daftar registrasi: Search, sort, dan Filter di server"
layer: be-e2e
priority: Medium
caseType: Positive
status: draft
sourceRules: [EB-FLT-3, EB-SRC-1, EB-SRT-1, EB-SRT-2]
smoke: []
dependsOn: []
trace:
  EB-FLT-3: [19, 21, 22]
  EB-SRC-1: [2, 4, 5, 7, 8, 10, 11, 13, 14, 16]
  EB-SRT-1: [24, 26, 28, 30, 32, 34, 40, 42, 44, 46, 48, 49, 51, 53, 54]
  EB-SRT-2: [32, 34, 36, 38, 40, 42, 44, 56, 58, 59, 60, 62]
owner: BE
---
# Daftar registrasi: Search, sort, dan Filter di server

## Prerequisites
- Aktor: Rina (Total Control, seluruh client).
- Data:
  - DU-129-1: Asset Name `Meja Kerja {runId}`, Category `Furnitur`, Brand `Olympic`, Model `OL-129`, TAG Type `Non-TAG`; isi setiap batch Draft di bawah adalah aset `Meja Kerja {runId}` sebanyak Total Asset.
  - DU-129-2: batch Draft Group `anggur Depot {runId}`, Origin `—`, Total Asset `5` (Ready `2`), Progress `40%`, Requested By `Rina Wulandari`, Last Updated `T0 − 5 jam`.
  - DU-129-3: batch Draft Group `Apel Depot {runId}`, Origin `REG-20261105-00502`, Total Asset `2` (Ready `1`), Progress `50%`, Requested By `Siti Nurhaliza`, Last Updated `T0 − 1 jam`.
  - DU-129-4: batch Draft Group `Elan Depot {runId}`, Origin `—`, Total Asset `9` (Ready `9`), Progress `100%`, Requested By `Agus Pratama`, Last Updated `T0 − 4 jam`.
  - DU-129-5: batch Draft Group `Élan Depot {runId}`, Origin `—`, Total Asset `10` (Ready `1`), Progress `10%`, Requested By `Budi Santoso`, Last Updated `T0 − 2 jam`.
  - DU-129-6: batch Draft Group `Ezra Depot {runId}`, Origin `REG-20261101-00501`, Total Asset `7` (Ready `0`), Progress `0%`, Requested By `Budi Hartono`, Last Updated `T0 − 6 jam`.
  - DU-129-7: batch Draft Group `3D Depot {runId}`, Origin `—`, Total Asset `2` (Ready `2`), Progress `100%`, Requested By `Siti Nurhaliza`, Last Updated `T0 − 3 jam`.
  - DU-129-8: batch Draft Group `#Gudang Depot {runId}`, Origin `—`, Total Asset `40` (Ready `20`), Progress `50%`, Requested By `Rina Wulandari`, Last Updated `T0 − 7 jam`.
  - DU-129-9: dua belas batch Draft Group `Kantor Volume {runId}`, Origin `—`, Total Asset `{n}` untuk n = 1 sampai 12, Progress `0%`, Requested By `Rina Wulandari`, Last Updated `T0 − {n} menit`.
  - DU-129-10: dua belas batch Draft Group `Kantor Seragam {runId}`, Origin `—`, Total Asset `3`, Progress `0%`, Requested By `Rina Wulandari`, Last Updated `T0 − {n} menit` untuk n = 1 sampai 12.
  - Ketujuh batch DU-129-2 sampai DU-129-8 diurutkan menurut default sort tabel (Last Updated terbaru di atas): `Apel Depot {runId}`, `Élan Depot {runId}`, `3D Depot {runId}`, `Elan Depot {runId}`, `anggur Depot {runId}`, `Ezra Depot {runId}`, `#Gudang Depot {runId}`.
- Kondisi:
  - Jumlah baris per halaman bernilai `10`.

## Test Steps

### Search mencocokkan substring tanpa membedakan huruf per kelas kolom
1. Rina mencari di sub tab Draft dengan kata kunci `Depot {runId}`
2. Verifikasi tabel memuat tepat tujuh baris data uji: `Apel Depot {runId}`, `Élan Depot {runId}`, `3D Depot {runId}`, `Elan Depot {runId}`, `anggur Depot {runId}`, `Ezra Depot {runId}`, `#Gudang Depot {runId}`
3. Rina mencari dengan kata kunci `NGGUR DEPOT {runId}`
4. Verifikasi baris `anggur Depot {runId}` tampil
5. Verifikasi baris `Apel Depot {runId}` tidak tampil
6. Rina mencari dengan kata kunci `REG-20261105-00502`
7. Verifikasi baris `Apel Depot {runId}` tampil karena kolom Origin cocok
8. Verifikasi baris `Ezra Depot {runId}` tidak tampil
9. Rina mencari dengan kata kunci `Budi H`
10. Verifikasi baris `Ezra Depot {runId}` tampil karena kolom Requested By cocok
11. Verifikasi baris `Élan Depot {runId}` tidak tampil
12. Rina mencari dengan kata kunci `40`
13. Verifikasi baris `anggur Depot {runId}` tampil karena kolom Progress `40%` cocok
14. Verifikasi baris `#Gudang Depot {runId}` tampil karena kolom Total Asset `40` cocok
15. Rina mencari dengan kata kunci `zzz-tidak-ada {runId}`
16. Verifikasi tabel tidak memuat satu baris pun

### Filter menerapkan OR dalam satu field dan AND antar field
17. Rina mencari dengan kata kunci `Depot {runId}`
18. Rina menerapkan Filter Requested By `Rina Wulandari` dan `Siti Nurhaliza`
19. Verifikasi tabel memuat tepat empat baris: `anggur Depot {runId}`, `Apel Depot {runId}`, `3D Depot {runId}`, `#Gudang Depot {runId}`
20. Rina menambahkan Filter Total Asset Min `5` dan Max `40` tanpa melepas Filter Requested By
21. Verifikasi tabel memuat tepat dua baris: `anggur Depot {runId}`, `#Gudang Depot {runId}`
22. Verifikasi baris `Apel Depot {runId}` dan `3D Depot {runId}` tidak tampil karena Total Asset `2` di luar rentang
23. Rina mengosongkan kedua Filter

### Sort kolom teks dan kolom Origin
24. Verifikasi tabel memuat tujuh baris data uji dengan urutan default Last Updated terbaru di atas: `Apel Depot {runId}`, `Élan Depot {runId}`, `3D Depot {runId}`, `Elan Depot {runId}`, `anggur Depot {runId}`, `Ezra Depot {runId}`, `#Gudang Depot {runId}`
25. Rina mengurutkan kolom Group secara menaik
26. Verifikasi urutan baris tanpa membedakan huruf besar dan kecil, simbol sebelum angka sebelum huruf, huruf beraksen sesudah huruf polos: `#Gudang Depot {runId}`, `3D Depot {runId}`, `anggur Depot {runId}`, `Apel Depot {runId}`, `Elan Depot {runId}`, `Élan Depot {runId}`, `Ezra Depot {runId}`
27. Rina mengurutkan kolom Group secara menurun
28. Verifikasi urutan baris kebalikan penuh: `Ezra Depot {runId}`, `Élan Depot {runId}`, `Elan Depot {runId}`, `Apel Depot {runId}`, `anggur Depot {runId}`, `3D Depot {runId}`, `#Gudang Depot {runId}`
29. Rina mengurutkan kolom Group untuk ketiga kalinya
30. Verifikasi urutan baris kembali ke urutan default tabel: `Apel Depot {runId}`, `Élan Depot {runId}`, `3D Depot {runId}`, `Elan Depot {runId}`, `anggur Depot {runId}`, `Ezra Depot {runId}`, `#Gudang Depot {runId}`
31. Rina mengurutkan kolom Requested By secara menaik
32. Verifikasi urutan baris menurut nama pengaju, nilai sama menurut default sort: `Elan Depot {runId}`, `Ezra Depot {runId}`, `Élan Depot {runId}`, `anggur Depot {runId}`, `#Gudang Depot {runId}`, `Apel Depot {runId}`, `3D Depot {runId}`
33. Rina mengurutkan kolom Requested By secara menurun
34. Verifikasi urutan baris kebalikan antar nama pengaju, nilai sama tetap menurut default sort: `Apel Depot {runId}`, `3D Depot {runId}`, `anggur Depot {runId}`, `#Gudang Depot {runId}`, `Élan Depot {runId}`, `Ezra Depot {runId}`, `Elan Depot {runId}`
35. Rina mengurutkan kolom Origin secara menaik
36. Verifikasi baris ber-Origin terisi tampil lebih dulu dan baris ber-Origin `—` di akhir menurut default sort: `Ezra Depot {runId}`, `Apel Depot {runId}`, `Élan Depot {runId}`, `3D Depot {runId}`, `Elan Depot {runId}`, `anggur Depot {runId}`, `#Gudang Depot {runId}`
37. Rina mengurutkan kolom Origin secara menurun
38. Verifikasi baris ber-Origin `—` di awal menurut default sort, disusul baris ber-Origin terisi: `Élan Depot {runId}`, `3D Depot {runId}`, `Elan Depot {runId}`, `anggur Depot {runId}`, `#Gudang Depot {runId}`, `Apel Depot {runId}`, `Ezra Depot {runId}`

### Sort kolom angka dan tanggal
39. Rina mengurutkan kolom Total Asset secara menaik
40. Verifikasi urutan baris menurut angka natural, nilai sama menurut default sort: `Apel Depot {runId}`, `3D Depot {runId}`, `anggur Depot {runId}`, `Ezra Depot {runId}`, `Elan Depot {runId}`, `Élan Depot {runId}`, `#Gudang Depot {runId}`
41. Rina mengurutkan kolom Total Asset secara menurun
42. Verifikasi urutan baris kebalikan antar angka, nilai sama tetap menurut default sort: `#Gudang Depot {runId}`, `Élan Depot {runId}`, `Elan Depot {runId}`, `Ezra Depot {runId}`, `anggur Depot {runId}`, `Apel Depot {runId}`, `3D Depot {runId}`
43. Rina mengurutkan kolom Progress secara menaik
44. Verifikasi urutan baris menurut persen terkecil ke terbesar, nilai sama menurut default sort: `Ezra Depot {runId}`, `Élan Depot {runId}`, `anggur Depot {runId}`, `Apel Depot {runId}`, `#Gudang Depot {runId}`, `3D Depot {runId}`, `Elan Depot {runId}`
45. Rina mengurutkan kolom Last Updated secara menaik
46. Verifikasi urutan baris dari yang terlama: `#Gudang Depot {runId}`, `Ezra Depot {runId}`, `anggur Depot {runId}`, `Elan Depot {runId}`, `3D Depot {runId}`, `Élan Depot {runId}`, `Apel Depot {runId}`
47. Rina mengurutkan kolom Last Updated secara menurun
48. Verifikasi urutan baris dari yang terbaru: `Apel Depot {runId}`, `Élan Depot {runId}`, `3D Depot {runId}`, `Elan Depot {runId}`, `anggur Depot {runId}`, `Ezra Depot {runId}`, `#Gudang Depot {runId}`
49. Verifikasi urutan baris pada sort Total Asset menaik, sort Requested By menaik, dan sort Group menaik saling berbeda satu sama lain

### Sort melintasi halaman dengan nilai berbeda
50. Rina mencari dengan kata kunci `Kantor Volume {runId}`
51. Verifikasi tabel memuat dua belas baris data uji yang terbagi di dua halaman
52. Rina mengurutkan kolom Total Asset secara menaik
53. Verifikasi halaman pertama memuat baris ber-Total Asset `1` sampai `10` berurutan secara natural
54. Verifikasi halaman kedua memuat baris ber-Total Asset `11` lalu `12`

### Sort dengan nilai sama melintasi halaman tetap deterministik
55. Rina mencari dengan kata kunci `Kantor Seragam {runId}`
56. Verifikasi tabel memuat dua belas baris data uji yang semuanya ber-Total Asset `3`
57. Rina mengurutkan kolom Total Asset secara menaik
58. Verifikasi halaman pertama memuat sepuluh baris dengan Last Updated terbaru lebih dulu menurut default sort
59. Verifikasi halaman kedua memuat dua baris sisanya dengan Last Updated paling lama
60. Verifikasi gabungan kedua halaman memuat dua belas baris berbeda tanpa baris ganda dan tanpa baris terlewat
61. Rina mengurutkan kolom Total Asset secara menurun
62. Verifikasi urutan baris pada kedua halaman sama persis dengan urutan sort menaik
