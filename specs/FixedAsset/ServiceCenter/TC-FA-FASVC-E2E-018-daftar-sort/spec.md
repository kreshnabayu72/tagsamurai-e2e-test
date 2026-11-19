---
id: TC-FA-FASVC-E2E-018-daftar-sort
title: "Daftar Service Center: Sort per Kolom dan Siklus Kembali ke Default Name A-Z"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["§9.5#r1", "EB-SRT-1", "EB-SRT-2", "EB-SRT-3@tabel-service-center"]
smoke: []
dependsOn: []
trace:
  "§9.5#r1": [2, 4]
  "EB-SRT-1": [7, 9, 12, 14, 19, 22, 24, 32, 35, 37, 40, 42, 45, 47, 52, 55, 66, 68, 71, 73, 78, 80]
  "EB-SRT-2": [17, 30, 50, 58, 60, 63, 66, 71]
  "EB-SRT-3@tabel-service-center": [27]
anchor: []
coverage:
  web: automated
---

# Daftar Service Center: Sort per Kolom dan Siklus Kembali ke Default Name A-Z

## Prerequisites
- Aktor: Total Control `Sari Urut {runId}` pada entitas khusus (user milik entitas itu). Aktor lain pemicu perubahan: Total Control `Dewi Santoso {runId}` dan `Dewi Setiawan {runId}` pada entitas yang sama.
- Layar awal: Add-ons > Service Center (halaman daftar).
- Data:
  - Spec ini memakai entitas khusus yang tidak dipakai spec lain, sehingga daftar hanya memuat dua belas Service Center di bawah.
  - DU-018-1: Entitas `Entitas Urut {runId}`, berisi seluruh data di bawah dan tidak memuat Service Center lain.
  - DU-018-2: User `Sari Urut {runId}`, role Total Control, cakupan seluruh Group di `Entitas Urut {runId}`, Status `Active`.
  - DU-018-3: Group `Alfa Urut {runId}`, anak langsung dari root pohon Group.
  - DU-018-4: Group `Beta Urut {runId}`, anak langsung dari root pohon Group.
  - DU-018-5: Group `Gamma Urut {runId}`, anak langsung dari root pohon Group.
  - DU-018-6: Group `Delta Urut {runId}`, anak langsung dari root pohon Group.
  - DU-018-7: Category `Genset Urut {runId}`, di pohon Category.
  - DU-018-8: Category `Kompresor Urut {runId}`, di pohon Category.
  - DU-018-9: Category `Pompa Urut {runId}`, di pohon Category.
  - DU-018-10: Service Center `3D Cepat {runId}`, Service type `Routine`, Available to `Beta Urut {runId}`, Specialization kosong, Brands kosong, City `Madiun`, Usage `148`, Status `Active`; dibuat ke-4 dari 12, dengan selisih satu menit atau lebih antara pembuatan berurutan (Last Updated mengikuti urutan itu).
  - DU-018-11: Service Center `anggur {runId}`, Service type `Routine`, Available to `Alfa Urut {runId}`, Specialization `Genset Urut {runId}`, Brands kosong, City `Blitar`, Usage `0`, Status `Active`; dibuat ke-7 dari 12, dengan selisih satu menit atau lebih antara pembuatan berurutan (Last Updated mengikuti urutan itu).
  - DU-018-12: Service Center `Apel {runId}`, Service type `Routine`, Available to `Alfa Urut {runId}`, `Beta Urut {runId}`, Specialization `Genset Urut {runId}`, `Kompresor Urut {runId}`, `Pompa Urut {runId}`, Brands kosong, City `Kediri`, Usage `24`, Status `Inactive`; dibuat ke-3 dari 12 dengan Status awal `Active`, lalu di-Inactivate setelah selisih satu menit atau lebih dan sebelum Service Center ke-4 dibuat, dengan selisih satu menit atau lebih sebelum pembuatan berikutnya, sehingga Last Updated `Apel {runId}` jatuh sesudah Service Center ke-3 dibuat dan sebelum Service Center ke-4 dibuat (Last Updated mengikuti urutan itu).
  - DU-018-13: Service Center `Elan {runId}`, Service type `Routine`, Available to `Alfa Urut {runId}`, `Beta Urut {runId}`, `Gamma Urut {runId}`, Specialization `Kompresor Urut {runId}`, Brands kosong, City `Malang`, Usage `10`, Status `Active`; dibuat ke-12 dari 12, dengan selisih satu menit atau lebih antara pembuatan berurutan (Last Updated mengikuti urutan itu).
  - DU-018-14: Service Center `Élan {runId}`, Service type `Routine`, Available to `Gamma Urut {runId}`, Specialization kosong, Brands kosong, City `Madiun`, Usage `2`, Status `Active`; dibuat ke-6 dari 12, dengan selisih satu menit atau lebih antara pembuatan berurutan (Last Updated mengikuti urutan itu).
  - DU-018-15: Service Center `Ezra {runId}`, Service type `Routine`, Available to `Alfa Urut {runId}`, Specialization `Pompa Urut {runId}`, Brands kosong, City `Blitar`, Usage `24`, Status `Active`; dibuat ke-10 dari 12, dengan selisih satu menit atau lebih antara pembuatan berurutan (Last Updated mengikuti urutan itu).
  - DU-018-16: Service Center `Hasta {runId}`, Service type `Routine`, Available to `Alfa Urut {runId}`, `Beta Urut {runId}`, `Delta Urut {runId}`, `Gamma Urut {runId}`, Specialization `Genset Urut {runId}`, Brands kosong, City `Kediri`, Usage `0`, Status `Active`; dibuat ke-5 dari 12, dengan selisih satu menit atau lebih antara pembuatan berurutan (Last Updated mengikuti urutan itu).
  - DU-018-17: Service Center `Kencana {runId}`, Service type `Routine`, Available to `Beta Urut {runId}`, Specialization kosong, Brands kosong, City `Malang`, Usage `10`, Status `Active`; dibuat ke-9 dari 12, dengan selisih satu menit atau lebih antara pembuatan berurutan (Last Updated mengikuti urutan itu).
  - DU-018-18: Service Center `Lestari {runId}`, Service type `Routine`, Available to `Gamma Urut {runId}`, Specialization `Kompresor Urut {runId}`, Brands kosong, City `Madiun`, Usage `148`, Status `Active`; dibuat ke-11 dari 12, dengan selisih satu menit atau lebih antara pembuatan berurutan (Last Updated mengikuti urutan itu).
  - DU-018-19: Service Center `Mitra {runId}`, Service type `Routine`, Available to `Alfa Urut {runId}`, `Gamma Urut {runId}`, Specialization `Pompa Urut {runId}`, Brands kosong, City `Blitar`, Usage `2`, Status `Active`; dibuat ke-2 dari 12, dengan selisih satu menit atau lebih antara pembuatan berurutan (Last Updated mengikuti urutan itu).
  - DU-018-20: Service Center `Nusa {runId}`, Service type `Routine`, Available to `Beta Urut {runId}`, `Gamma Urut {runId}`, Specialization kosong, Brands kosong, City `Kediri`, Usage `0`, Status `Active`; dibuat ke-8 dari 12, dengan selisih satu menit atau lebih antara pembuatan berurutan (Last Updated mengikuti urutan itu).
  - DU-018-21: Service Center `Utama {runId}`, Service type `Routine`, Available to `Alfa Urut {runId}`, Specialization `Genset Urut {runId}`, Brands kosong, City `Malang`, Usage `24`, Status `Active`; dibuat ke-1 dari 12, dengan selisih satu menit atau lebih antara pembuatan berurutan (Last Updated mengikuti urutan itu).
  - DU-018-22: User `Dewi Santoso {runId}`, role Total Control, cakupan seluruh Group di `Entitas Urut {runId}`, Status `Active`; tampil `Dewi S` pada kolom Modified By.
  - DU-018-23: User `Dewi Setiawan {runId}`, role Total Control, cakupan seluruh Group di `Entitas Urut {runId}`, Status `Active`; tampil `Dewi S` pada kolom Modified By, sama dengan `Dewi Santoso {runId}`, padahal nama lengkapnya berbeda (`Dewi Santoso {runId}` mendahului `Dewi Setiawan {runId}` menurut urutan nama lengkap).
- Kondisi: client memiliki lisensi addon Maintenance berstatus aktif. Setup Column akun `Sari Urut {runId}` memakai konfigurasi bawaan (semua kolom tampil). Date Format bernilai `dd/MM/yy`. Akun `Dewi Santoso {runId}` dan `Dewi Setiawan {runId}` aktif dan kredensialnya disediakan fase 2.

## Test Steps

### Urutan bawaan daftar adalah Name A-Z
1. Klik halaman `1` pada paginasi daftar
2. Verifikasi urutan baris pada halaman 1: `3D Cepat {runId}`, `anggur {runId}`, `Apel {runId}`, `Elan {runId}`, `Élan {runId}`, `Ezra {runId}`, `Hasta {runId}`, `Kencana {runId}`, `Lestari {runId}`, `Mitra {runId}`
3. Klik halaman `2` pada paginasi daftar
4. Verifikasi urutan baris pada halaman 2: `Nusa {runId}`, `Utama {runId}`

### Sort Name: huruf besar-kecil tidak dibedakan, huruf beraksen sesudah huruf polos, dan angka di awal mendahului huruf
5. Klik header kolom `Name`
6. Klik halaman `1` pada paginasi daftar
7. Verifikasi urutan baris pada halaman 1: `3D Cepat {runId}`, `anggur {runId}`, `Apel {runId}`, `Elan {runId}`, `Élan {runId}`, `Ezra {runId}`, `Hasta {runId}`, `Kencana {runId}`, `Lestari {runId}`, `Mitra {runId}`
8. Klik halaman `2` pada paginasi daftar
9. Verifikasi urutan baris pada halaman 2: `Nusa {runId}`, `Utama {runId}`
10. Klik header kolom `Name`
11. Klik halaman `1` pada paginasi daftar
12. Verifikasi urutan baris pada halaman 1: `Utama {runId}`, `Nusa {runId}`, `Mitra {runId}`, `Lestari {runId}`, `Kencana {runId}`, `Hasta {runId}`, `Ezra {runId}`, `Élan {runId}`, `Elan {runId}`, `Apel {runId}`
13. Klik halaman `2` pada paginasi daftar
14. Verifikasi urutan baris pada halaman 2: `anggur {runId}`, `3D Cepat {runId}`

### Sort angka memakai urutan natural dan nilai sama diurutkan menurut Name A-Z
15. Klik header kolom `Usage`
16. Klik halaman `1` pada paginasi daftar
17. Verifikasi urutan baris pada halaman 1: `anggur {runId}`, `Hasta {runId}`, `Nusa {runId}`, `Élan {runId}`, `Mitra {runId}`, `Elan {runId}`, `Kencana {runId}`, `Apel {runId}`, `Ezra {runId}`, `Utama {runId}`
18. Klik halaman `2` pada paginasi daftar
19. Verifikasi urutan baris pada halaman 2: `3D Cepat {runId}`, `Lestari {runId}`
20. Klik header kolom `Usage`
21. Klik halaman `1` pada paginasi daftar
22. Verifikasi urutan baris pada halaman 1: `3D Cepat {runId}`, `Lestari {runId}`, `Apel {runId}`, `Ezra {runId}`, `Utama {runId}`, `Elan {runId}`, `Kencana {runId}`, `Élan {runId}`, `Mitra {runId}`, `anggur {runId}`
23. Klik halaman `2` pada paginasi daftar
24. Verifikasi urutan baris pada halaman 2: `Hasta {runId}`, `Nusa {runId}`

### Klik ketiga menghilangkan sort dan mengembalikan urutan ke default Name A-Z
25. Klik header kolom `Usage`
26. Klik halaman `1` pada paginasi daftar
27. Verifikasi urutan baris pada halaman 1: `3D Cepat {runId}`, `anggur {runId}`, `Apel {runId}`, `Elan {runId}`, `Élan {runId}`, `Ezra {runId}`, `Hasta {runId}`, `Kencana {runId}`, `Lestari {runId}`, `Mitra {runId}`

### Sort badge Status: nilai sama melintasi halaman diurutkan menurut Name A-Z
28. Klik header kolom `Status`
29. Klik halaman `1` pada paginasi daftar
30. Verifikasi urutan baris pada halaman 1: `3D Cepat {runId}`, `anggur {runId}`, `Elan {runId}`, `Élan {runId}`, `Ezra {runId}`, `Hasta {runId}`, `Kencana {runId}`, `Lestari {runId}`, `Mitra {runId}`, `Nusa {runId}`
31. Klik halaman `2` pada paginasi daftar
32. Verifikasi urutan baris pada halaman 2: `Utama {runId}`, `Apel {runId}`
33. Klik header kolom `Status`
34. Klik halaman `1` pada paginasi daftar
35. Verifikasi urutan baris pada halaman 1: `Apel {runId}`, `3D Cepat {runId}`, `anggur {runId}`, `Elan {runId}`, `Élan {runId}`, `Ezra {runId}`, `Hasta {runId}`, `Kencana {runId}`, `Lestari {runId}`, `Mitra {runId}`
36. Klik halaman `2` pada paginasi daftar
37. Verifikasi urutan baris pada halaman 2: `Nusa {runId}`, `Utama {runId}`

### Sort tanggal Last Updated: Oldest First lalu Newest First
38. Klik header kolom `Last Updated`
39. Klik halaman `1` pada paginasi daftar
40. Verifikasi urutan baris pada halaman 1: `Utama {runId}`, `Mitra {runId}`, `Apel {runId}`, `3D Cepat {runId}`, `Hasta {runId}`, `Élan {runId}`, `anggur {runId}`, `Nusa {runId}`, `Kencana {runId}`, `Ezra {runId}`
41. Klik halaman `2` pada paginasi daftar
42. Verifikasi urutan baris pada halaman 2: `Lestari {runId}`, `Elan {runId}`
43. Klik header kolom `Last Updated`
44. Klik halaman `1` pada paginasi daftar
45. Verifikasi urutan baris pada halaman 1: `Elan {runId}`, `Lestari {runId}`, `Ezra {runId}`, `Kencana {runId}`, `Nusa {runId}`, `anggur {runId}`, `Élan {runId}`, `Hasta {runId}`, `3D Cepat {runId}`, `Apel {runId}`
46. Klik halaman `2` pada paginasi daftar
47. Verifikasi urutan baris pada halaman 2: `Mitra {runId}`, `Utama {runId}`

### Sort kolom chip: kunci jumlah +N more, seri menurut nilai pertama lalu Name A-Z
48. Klik header kolom `Available To`
49. Klik halaman `1` pada paginasi daftar
50. Verifikasi urutan baris pada halaman 1: `anggur {runId}`, `Apel {runId}`, `Ezra {runId}`, `Mitra {runId}`, `Utama {runId}`, `3D Cepat {runId}`, `Kencana {runId}`, `Nusa {runId}`, `Élan {runId}`, `Lestari {runId}`
51. Klik halaman `2` pada paginasi daftar
52. Verifikasi urutan baris pada halaman 2: `Elan {runId}`, `Hasta {runId}`
53. Klik header kolom `Available To`
54. Klik halaman `1` pada paginasi daftar
55. Verifikasi dua baris pertama pada halaman 1: `Hasta {runId}` dan `Elan {runId}`

### Sort kolom chip Specialization: kunci jumlah +N more (tiga nilai) dan nilai kosong di akhir saat ascending dan di awal saat descending
56. Klik header kolom `Specialization`
57. Klik halaman `1` pada paginasi daftar
58. Verifikasi urutan baris pada halaman 1: `anggur {runId}`, `Hasta {runId}`, `Utama {runId}`, `Elan {runId}`, `Lestari {runId}`, `Ezra {runId}`, `Mitra {runId}`, `Apel {runId}`, `3D Cepat {runId}`, `Élan {runId}`
59. Klik halaman `2` pada paginasi daftar
60. Verifikasi urutan baris pada halaman 2: `Kencana {runId}`, `Nusa {runId}`
61. Klik header kolom `Specialization`
62. Klik halaman `1` pada paginasi daftar
63. Verifikasi lima baris pertama pada halaman 1: `3D Cepat {runId}`, `Élan {runId}`, `Kencana {runId}`, `Nusa {runId}`, `Apel {runId}`

### Sort City: Alphabetical A-Z, seri menurut Name A-Z
64. Klik header kolom `City`
65. Klik halaman `1` pada paginasi daftar
66. Verifikasi urutan baris pada halaman 1: `anggur {runId}`, `Ezra {runId}`, `Mitra {runId}`, `Apel {runId}`, `Hasta {runId}`, `Nusa {runId}`, `3D Cepat {runId}`, `Élan {runId}`, `Lestari {runId}`, `Elan {runId}`
67. Klik halaman `2` pada paginasi daftar
68. Verifikasi urutan baris pada halaman 2: `Kencana {runId}`, `Utama {runId}`
69. Klik header kolom `City`
70. Klik halaman `1` pada paginasi daftar
71. Verifikasi urutan baris pada halaman 1: `Elan {runId}`, `Kencana {runId}`, `Utama {runId}`, `3D Cepat {runId}`, `Élan {runId}`, `Lestari {runId}`, `Apel {runId}`, `Hasta {runId}`, `Nusa {runId}`, `anggur {runId}`
72. Klik halaman `2` pada paginasi daftar
73. Verifikasi urutan baris pada halaman 2: `Ezra {runId}`, `Mitra {runId}`

### Sort Modified By menurut nama lengkap, bukan menurut tampilan singkat
74. Pengguna `Dewi Santoso {runId}` mengubah Notes menjadi `Dicek Santoso` pada Service Center `Utama {runId}`
75. Pengguna `Dewi Setiawan {runId}` mengubah Notes menjadi `Dicek Setiawan` pada Service Center `Hasta {runId}`
76. Ketik Search `Dewi S` pada daftar, tekan Enter
77. Klik header kolom `Modified By`
78. Verifikasi urutan baris hasil Search: `Utama {runId}` (Modified By `Dewi S`, nama lengkap `Dewi Santoso {runId}`), lalu `Hasta {runId}` (Modified By `Dewi S`, nama lengkap `Dewi Setiawan {runId}`), walau urutan Name A-Z menempatkan `Hasta {runId}` lebih dulu
79. Klik header kolom `Modified By`
80. Verifikasi urutan baris hasil Search: `Hasta {runId}`, lalu `Utama {runId}`
