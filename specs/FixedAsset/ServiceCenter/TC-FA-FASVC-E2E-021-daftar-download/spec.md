---
id: TC-FA-FASVC-E2E-021-daftar-download
title: "Daftar Service Center: Download CSV dan XLSX Mengikuti Filter, Sort, dan Kolom"
layer: ui-e2e
priority: Critical
caseType: Positive
status: ready-for-automation
sourceRules: ["EC-FASVC-31", "F-FASVC-01.k1", "§5#b5", "EB-DL-1@tabel-service-center", "EB-DL-2@tabel-service-center", "EB-DL-3@tabel-service-center", "EB-FB-2@download-daftar", "EB-DL-4", "§9.4.3#b7"]
smoke: []
dependsOn: []
trace:
  "EC-FASVC-31": [75, 76, 72]
  "F-FASVC-01.k1": [71, 75, 76, 81]
  "§5#b5": [16, 21, 29, 36, 81]
  "EB-DL-1@tabel-service-center": [6, 10, 16, 21, 35, 36]
  "EB-DL-2@tabel-service-center": [11, 77]
  "EB-DL-3@tabel-service-center": [9, 19]
  "EB-FB-2@download-daftar": [9, 11, 77]
  "EB-DL-4": [20, 26, 29, 44, 45, 46, 47, 48, 49, 53, 54, 55, 59, 60, 64, 65, 69, 75, 76]
  "§9.4.3#b7": [81]
anchor: [9, 75]
coverage:
  web: automated
---

# Daftar Service Center: Download CSV dan XLSX Mengikuti Filter, Sort, dan Kolom

## Prerequisites
- Aktor: Total Control `Rina Wijaya` (cakupan seluruh Group).
- Layar awal: Add-ons > Service Center (halaman daftar).
- Data:
  - DU-021-1: Group `Wilayah Unduh {runId}`, anak langsung dari root pohon Group.
  - DU-021-2: Group `Cabang Unduh Satu {runId}`, anak dari `Wilayah Unduh {runId}`.
  - DU-021-3: Group `Cabang Unduh Dua {runId}`, anak dari `Wilayah Unduh {runId}`.
  - DU-021-4: Group `Cabang Unduh Tiga {runId}`, anak dari `Wilayah Unduh {runId}`.
  - DU-021-5: Category `Mesin Unduh {runId}`, induk di pohon Category.
  - DU-021-6: Category `Genset Unduh {runId}`, anak dari `Mesin Unduh {runId}`.
  - DU-021-7: Brand `Merek Unduh Satu {runId}`, status Active di master.
  - DU-021-8: Brand `Merek Unduh Dua {runId}`, status Active di master.
  - DU-021-9: Service Center `Zzz Unduh 01 {runId}`, Service type `Routine`, Available to `Cabang Unduh Satu {runId}`, `Cabang Unduh Dua {runId}`, dan `Cabang Unduh Tiga {runId}`, Specialization `Genset Unduh {runId}`, Brands `Merek Unduh Satu {runId}`, City `Kota Unduh Satu {runId}`, Usage `0`, Status `Active`; dibuat dan terakhir diubah oleh `Rina Wijaya`.
  - DU-021-10: Service Center `Zzz Unduh 02 {runId}`, Service type `Repair`, Available to `Cabang Unduh Satu {runId}`, Specialization kosong, Brands kosong, City `Kota Unduh Dua {runId}`, Usage `0`, Status `Inactive`.
  - DU-021-11: Service Center `Zzz Unduh 03 {runId}`, Service type `Routine` dan `Repair`, Available to `Cabang Unduh Satu {runId}`, Specialization `Genset Unduh {runId}`, Brands `Merek Unduh Satu {runId}` dan `Merek Unduh Dua {runId}`, City `Kota Unduh Satu {runId}`, Usage `0`, Status `Active`.
  - DU-021-12: 6 Service Center `Zzz Unduh 04 {runId}` sampai `Zzz Unduh 09 {runId}`, Service type `Routine`, Available to `Cabang Unduh Satu {runId}`, City `Kota Unduh Tiga {runId}`, Usage `0`, Status `Active`.
  - DU-021-13: Service Center `Zzz Unduh 10 {runId}`, Service type `Routine`, Available to `Cabang Unduh Satu {runId}`, City `Kota Unduh Tiga {runId}`, Usage `0`, Status `Inactive`.
  - DU-021-14: Service Center `Zzz Unduh "Bintang", Barat {runId}`, Service type `Routine`, Available to `Cabang Unduh Satu {runId}`, City `Kota Unduh Tiga {runId}`, Usage `0`, Status `Active`; Name memuat koma dan tanda kutip ganda.
  - DU-021-15: Service Center `Zzz Unduh Ünïcode {runId}`, Service type `Routine`, Available to `Cabang Unduh Satu {runId}`, City `Kota Unduh Tiga {runId}`, Usage `0`, Status `Active`; Name memuat huruf non-ASCII Ü dan ï.
  - DU-021-16: Kata kunci Search `Zzz Tidak Ada {runId}`, `Bintang`, `Ünïcode`, dan `{runId}`.
- Kondisi: client memiliki lisensi addon Maintenance berstatus aktif. Daftar memuat lebih dari 10 Service Center secara keseluruhan (dua belas milik spec ini).

## Test Steps

### Download tanpa Search atau Filter memuat semua baris, tidak dibatasi halaman
1. Klik ikon `Changelog` pada toolbar daftar
2. Ketik Search `{runId}` pada modal Changelog, tekan Enter
3. Catat jumlah baris hasil Search sebagai jumlah awal entri Changelog
4. Tutup modal Changelog lewat icon close
5. Klik `Last Page` pada paginasi daftar
6. Verifikasi baris `Zzz Unduh Ünïcode {runId}` tampil pada halaman terakhir, bukan pada halaman 1
7. Klik ikon `Download` pada toolbar daftar
8. Klik `Download as CSV`
9. Verifikasi nama berkas unduhan `Service-Centers.csv`
10. Verifikasi berkas memuat baris `Zzz Unduh Ünïcode {runId}` yang pada layar berada di halaman terakhir
11. Verifikasi tidak ada toast yang tampil sesudah unduhan selesai

### Download mengikuti Search dan Filter yang aktif
12. Ketik Search `{runId}` pada daftar, tekan Enter
13. Klik ikon `Filter` pada toolbar daftar
14. Pilih `Inactive` pada filter `Status`
15. Klik `[Apply]`
16. Verifikasi baris `Zzz Unduh 02 {runId}` dan `Zzz Unduh 10 {runId}` tampil
17. Klik ikon `Download` pada toolbar daftar
18. Klik `Download as XLSX`
19. Verifikasi nama berkas unduhan `Service-Centers.xlsx`
20. Verifikasi berkas memuat satu sheet bernama `Sheet1`
21. Verifikasi berkas memuat tepat dua baris data, yaitu `Zzz Unduh 02 {runId}` dan `Zzz Unduh 10 {runId}`

### Download mengikuti urutan Sort aktif
22. Klik `[Clear Field]`
23. Klik `[Apply]`
24. Klik header kolom `Name`
25. Klik header kolom `Name`
26. Verifikasi baris `Zzz Unduh Ünïcode {runId}` berada di baris pertama daftar
27. Klik ikon `Download` pada toolbar daftar
28. Klik `Download as CSV`
29. Verifikasi baris data pertama pada berkas adalah `Zzz Unduh Ünïcode {runId}`, mengikuti urutan Name descending pada layar

### Download mengikuti kolom yang tampil
30. Klik header kolom Actions (`⋯`) pada tabel daftar
31. Hilangkan centang `Brands` pada panel Column Visibility
32. Tekan Esc untuk menutup panel Column Visibility
33. Klik ikon `Download` pada toolbar daftar
34. Klik `Download as CSV`
35. Verifikasi header berkas memuat `Name`, `Service Type`, dan `Status`
36. Verifikasi header berkas tidak memuat `Brands`
37. Klik header kolom Actions (`⋯`) pada tabel daftar
38. Centang `Brands` pada panel Column Visibility
39. Tekan Esc untuk menutup panel Column Visibility

### Isi berkas: badge, hierarki penuh, nama user lengkap, dan nilai kosong
40. Klik header kolom `Name`
41. Ganti isi kotak search daftar dengan `Zzz Unduh 01 {runId}`, tekan Enter
42. Klik ikon `Download` pada toolbar daftar
43. Klik `Download as CSV`
44. Verifikasi sel Service Type baris `Zzz Unduh 01 {runId}` pada berkas bernilai `Routine`
45. Verifikasi sel Status baris `Zzz Unduh 01 {runId}` pada berkas bernilai `Active`
46. Verifikasi sel Available To baris `Zzz Unduh 01 {runId}` memuat ketiga nilai berhierarki penuh dipisah `, `: `Wilayah Unduh {runId} > Cabang Unduh Satu {runId}`, `Wilayah Unduh {runId} > Cabang Unduh Dua {runId}`, dan `Wilayah Unduh {runId} > Cabang Unduh Tiga {runId}`, tanpa teks `+1 more`
47. Verifikasi sel Specialization baris `Zzz Unduh 01 {runId}` bernilai `Mesin Unduh {runId} > Genset Unduh {runId}`
48. Verifikasi sel Brands baris `Zzz Unduh 01 {runId}` bernilai `Merek Unduh Satu {runId}` tanpa hierarki
49. Verifikasi sel Modified By baris `Zzz Unduh 01 {runId}` bernilai nama lengkap `Rina Wijaya`, bukan `Rina W`
50. Ganti isi kotak search daftar dengan `Zzz Unduh 02 {runId}`, tekan Enter
51. Klik ikon `Download` pada toolbar daftar
52. Klik `Download as CSV`
53. Verifikasi sel Service Type baris `Zzz Unduh 02 {runId}` pada berkas bernilai `Repair`
54. Verifikasi sel Status baris `Zzz Unduh 02 {runId}` pada berkas bernilai `Inactive`
55. Verifikasi sel Specialization dan sel Brands baris `Zzz Unduh 02 {runId}` pada berkas bernilai `-`
56. Ganti isi kotak search daftar dengan `Zzz Unduh 03 {runId}`, tekan Enter
57. Klik ikon `Download` pada toolbar daftar
58. Klik `Download as CSV`
59. Verifikasi sel Service Type baris `Zzz Unduh 03 {runId}` pada berkas bernilai `Repair, Routine`, dipisah koma dan spasi dan urut A-Z
60. Verifikasi sel Brands baris `Zzz Unduh 03 {runId}` pada berkas bernilai `Merek Unduh Dua {runId}, Merek Unduh Satu {runId}`

### Isi berkas CSV: koma, tanda kutip, dan karakter non-ASCII
61. Ganti isi kotak search daftar dengan `Bintang`, tekan Enter
62. Klik ikon `Download` pada toolbar daftar
63. Klik `Download as CSV`
64. Verifikasi sel Name baris `Zzz Unduh "Bintang", Barat {runId}` pada berkas dibungkus tanda kutip ganda dengan tanda kutip di dalamnya digandakan: `"Zzz Unduh ""Bintang"", Barat {runId}"`
65. Verifikasi sel Name itu tetap satu sel walau memuat koma
66. Ganti isi kotak search daftar dengan `Ünïcode`, tekan Enter
67. Klik ikon `Download` pada toolbar daftar
68. Klik `Download as CSV`
69. Verifikasi berkas dikodekan UTF-8 dengan BOM dan sel Name baris `Zzz Unduh Ünïcode {runId}` terbaca utuh dengan huruf Ü dan ï

### Download dengan nol baris hanya berisi header dan tidak dicatat di log
70. Ganti isi kotak search daftar dengan `Zzz Tidak Ada {runId}`, tekan Enter
71. Verifikasi empty state dengan judul `No results found` tampil
72. Verifikasi tombol `Download` pada toolbar daftar aktif
73. Klik ikon `Download` pada toolbar daftar
74. Klik `Download as CSV`
75. Verifikasi berkas memuat satu baris header dengan kolom `Name`, `Service Type`, dan `Status`
76. Verifikasi berkas tidak memuat baris data
77. Verifikasi tidak ada toast yang tampil sesudah unduhan selesai
78. Ganti isi kotak search daftar dengan `{runId}`, tekan Enter
79. Klik ikon `Changelog` pada toolbar daftar
80. Ketik Search `{runId}` pada modal Changelog, tekan Enter
81. Verifikasi jumlah baris hasil Search sama dengan jumlah yang dicatat pada langkah 3
82. Tutup modal Changelog lewat icon close