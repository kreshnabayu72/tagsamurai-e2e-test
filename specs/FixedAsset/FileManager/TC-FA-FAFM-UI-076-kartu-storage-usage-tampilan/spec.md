---
id: TC-FA-FAFM-UI-076-kartu-storage-usage-tampilan
title: "Kartu Storage Usage: tampilan, format angka, ProgressBar, dan Alert"
layer: ui-client
priority: High
caseType: Negative
status: ready-for-automation
sourceRules: ["EC-19", "EC-20", "F-FAFM-06.k3", "F-FAFM-06j", "F-FAFM-06k", "INV-02a", "INV-02d", "INV-02h", "INV-02i", "S-10", "SUC-01a", "SUC-01b", "SUC-01c", "SUC-02a", "SUC-02b", "SUC-02c", "SUC-02d", "SUC-02e", "SUC-03b", "SUC-03c", "SUC-04b", "SUC-04c", "SUC-04d", "SUC-04e", "SUC-04f", "SUC-05a", "SUC-05b", "SUC-05c", "SUC-05d", "SUC-05e", "SUC-05f", "SUC-06b", "SUC-06c", "TBL-01c", "TBL-01e", "TBL-09a", "TBL-09b", "TBL-09c", "§4.2c#p3", "§4.2c#r37", "§4.2c#r38", "§4.2c#r39", "§9.2#p18", "EB-TBL-13@kartu-storage-usage"]
smoke: []
dependsOn: []
trace:
  "EC-19": [27, 29, 30]
  "EC-20": [12, 17, 22, 23]
  "F-FAFM-06.k3": [12, 18, 27, 29, 30]
  "F-FAFM-06j": [27, 29, 30]
  "F-FAFM-06k": [12, 18]
  "INV-02a": [7, 8, 12, 16, 18]
  "INV-02d": [3, 4, 9]
  "INV-02h": [65, 66, 67]
  "INV-02i": [59, 60]
  "S-10": [12, 16, 17, 18, 33, 34, 35, 36]
  "SUC-01a": [2, 25]
  "SUC-01b": [2]
  "SUC-01c": [25]
  "SUC-02a": [10, 12, 33, 49, 52]
  "SUC-02b": [13, 14]
  "SUC-02c": [10, 49]
  "SUC-02d": [30]
  "SUC-02e": [15]
  "SUC-03b": [3, 19, 26, 55]
  "SUC-03c": [39]
  "SUC-04b": [4, 20, 56]
  "SUC-04c": [27]
  "SUC-04d": [5]
  "SUC-04e": [6]
  "SUC-04f": [32, 33, 34, 35, 36, 38, 39, 40, 41, 42]
  "SUC-05a": [7, 44, 47]
  "SUC-05b": [7, 16, 44, 47, 51]
  "SUC-05c": [17, 34, 45]
  "SUC-05d": [8, 18, 35, 48, 53]
  "SUC-05e": [29]
  "SUC-05f": [48]
  "SUC-06b": [9, 21, 57]
  "SUC-06c": [28]
  "TBL-01c": [59, 60, 62, 64]
  "TBL-01e": [59, 60]
  "TBL-09a": [65]
  "TBL-09b": [67, 68]
  "TBL-09c": [59, 60]
  "§4.2c#p3": [25, 28]
  "§4.2c#r37": [3, 4, 7, 8, 9, 10]
  "§4.2c#r38": [12, 16, 17, 18, 19, 20, 21]
  "§4.2c#r39": [26, 27, 28, 29]
  "§9.2#p18": [12]
  "EB-TBL-13@kartu-storage-usage": [3, 4, 9]
anchor: []
coverage:
  web: automated
---

# Kartu Storage Usage: tampilan, format angka, ProgressBar, dan Alert

## Prerequisites
- Aktor: Total Control.
- Layar awal: Kartu Storage Usage.
- Komponen: Kartu Storage Usage.
- Data:
  - DU-076-1: Total Used `4.8 GB`, Storage Quota `50.0 GB`, Fixed Asset `3.2 GB`; label persentase yang diharapkan `9%`, dari 4.8 GB dari 50.0 GB (9,6%) dibulatkan ke bawah.
  - DU-076-2: Total Used `50.4 GB`, Storage Quota `50.0 GB`, Fixed Asset `48.8 GB`; label persentase yang diharapkan `100%`, dari 50.4 GB dari 50.0 GB (100,8%) dibulatkan ke bawah.
  - DU-076-3: Total Used `3.2 GB`, Storage Quota `—` (belum pernah dialokasikan), Fixed Asset `3.2 GB`.
  - DU-076-4: Total Used `1.0 GB`, Storage Quota `0.0 GB`, Fixed Asset `1.0 GB`.
  - DU-076-5: Total Used `—` (angka belum tersedia), Storage Quota `50.0 GB`, Fixed Asset `3.2 GB`.
  - DU-076-6: Total Used `60.0 GB`, Storage Quota `50.0 GB`, Fixed Asset `58.0 GB`; label persentase yang diharapkan `120%`, dari 60.0 GB dari 50.0 GB.
  - DU-076-7: Total Used `49.9 GB`, Storage Quota `50.0 GB`, Fixed Asset `40.0 GB`; label persentase yang diharapkan `99%`, dari 49.9 GB dari 50.0 GB (99,8%) dibulatkan ke bawah.
  - DU-076-8: Total Used `50.0 GB`, Storage Quota `50.0 GB`, Fixed Asset `40.0 GB`; label persentase yang diharapkan `100%`, dari 50.0 GB dari 50.0 GB.
  - DU-076-9: Total Used `1,536.0 GB`, Storage Quota `2,000.0 GB`, Fixed Asset `1,200.0 GB`.
- Kondisi:
  - K1: kartu berisi DU-076-1.
  - K2: kartu berisi DU-076-2.
  - K3: kartu berisi DU-076-3.
  - K4: kartu berisi DU-076-4.
  - K5: kartu berisi DU-076-5.
  - K6: kartu berisi DU-076-6.
  - K7: kartu berisi DU-076-7.
  - K8: kartu berisi DU-076-8.
  - K9: kartu berisi DU-076-9.

## Test Steps

### Kartu di bawah kuota
1. Tampilkan Kartu Storage Usage dengan kondisi K1
2. Verifikasi judul `Storage Usage` tampil
3. Verifikasi `Total Used` tampil `4.8 GB`
4. Verifikasi `Storage Quota` tampil `50.0 GB`
5. Verifikasi `Storage Quota` tampil sebagai teks informasi tanpa kontrol yang bisa diubah
6. Verifikasi tidak ada aksi top-up pada kartu
7. Verifikasi label ProgressBar `9%` tampil
8. Verifikasi ProgressBar memakai severity default
9. Verifikasi `Fixed Asset 3.2 GB` tampil
10. Verifikasi Alert Storage penuh tidak tampil

### Kartu melewati kuota
11. Tampilkan Kartu Storage Usage dengan kondisi K2
12. Verifikasi Alert Storage penuh tampil
13. Verifikasi Alert memuat teks `Storage is full. New uploads are blocked until storage is freed or the quota is increased.`
14. Verifikasi Alert memakai severity `danger`
15. Verifikasi Alert tidak memuat tombol aksi
16. Verifikasi label ProgressBar `100%` tampil
17. Verifikasi bar ProgressBar terisi penuh
18. Verifikasi ProgressBar memakai severity `danger`
19. Verifikasi `Total Used` tampil `50.4 GB`
20. Verifikasi `Storage Quota` tampil `50.0 GB`
21. Verifikasi `Fixed Asset 48.8 GB` tampil
22. Verifikasi tombol Changelog tetap aktif
23. Verifikasi tombol Recycle Bin tetap aktif

### Kuota belum dialokasikan
24. Tampilkan Kartu Storage Usage dengan kondisi K3
25. Verifikasi judul `Storage Usage` tetap tampil
26. Verifikasi `Total Used` tampil `3.2 GB`
27. Verifikasi `Storage Quota` tampil `—`
28. Verifikasi `Fixed Asset 3.2 GB` tetap tampil
29. Verifikasi ProgressBar tidak tampil
30. Verifikasi Alert Storage penuh tidak tampil

### Kuota 0.0 GB diperlakukan sebagai kuota terisi
31. Tampilkan Kartu Storage Usage dengan kondisi K4
32. Verifikasi `Storage Quota` tampil `0.0 GB`
33. Verifikasi Alert Storage penuh tampil
34. Verifikasi bar ProgressBar terisi penuh
35. Verifikasi ProgressBar memakai severity `danger`
36. Verifikasi label persentase tidak tampil pada ProgressBar

### Total Used belum tersedia
37. Tampilkan Kartu Storage Usage dengan kondisi K5
38. Verifikasi `Storage Quota` tampil `50.0 GB`
39. Verifikasi `Total Used` tampil `—`
40. Verifikasi ProgressBar tidak tampil
41. Verifikasi label persentase tidak tampil
42. Verifikasi Alert Storage penuh tidak tampil

### Persentase di atas 100%
43. Tampilkan Kartu Storage Usage dengan kondisi K6
44. Verifikasi label ProgressBar `120%` tampil
45. Verifikasi bar ProgressBar terisi penuh

### Satu langkah di bawah kuota
46. Tampilkan Kartu Storage Usage dengan kondisi K7
47. Verifikasi label ProgressBar `99%` tampil
48. Verifikasi ProgressBar memakai severity default
49. Verifikasi Alert Storage penuh tidak tampil

### Tepat di kuota
50. Tampilkan Kartu Storage Usage dengan kondisi K8
51. Verifikasi label ProgressBar `100%` tampil
52. Verifikasi Alert Storage penuh tampil
53. Verifikasi ProgressBar memakai severity `danger`

### Format ukuran dengan pemisah ribuan
54. Tampilkan Kartu Storage Usage dengan kondisi K9
55. Verifikasi `Total Used` tampil `1,536.0 GB`
56. Verifikasi `Storage Quota` tampil `2,000.0 GB`
57. Verifikasi `Fixed Asset 1,200.0 GB` tampil

### Header kartu dan kartu bukan tabel
58. Tampilkan Kartu Storage Usage dengan kondisi K1
59. Verifikasi tombol Changelog tampil pada header kartu
60. Verifikasi tombol Recycle Bin tampil pada header kartu
61. Arahkan kursor ke tombol Changelog
62. Verifikasi teks `Changelog` tersampaikan pada tombol Changelog
63. Arahkan kursor ke tombol Recycle Bin
64. Verifikasi teks `Recycle Bin` tersampaikan pada tombol Recycle Bin
65. Verifikasi tidak ada tabel pada kartu
66. Verifikasi tidak ada Checkbox pada kartu
67. Verifikasi tidak ada Search dan Filter pada kartu
68. Verifikasi tidak ada Sort, Bulk Action, Pagination, dan Download pada kartu
