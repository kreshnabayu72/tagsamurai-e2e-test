---
id: TC-FA-FACO-E2E-002-search-account-list
title: "Search Account List menyaring baris menurut kolom yang dicari"
layer: ui-e2e
priority: Medium
caseType: Positive
status: draft
sourceRules: ["§4.1.1#r2", "§4.1.1#r3", "§4.1.1#r4", "§5#b2", "EB-SRC-2@tabel-account-list", "EB-SRC-3@tabel-account-list", "EB-SRC-1"]
smoke: ["EB-SRC-1"]
dependsOn: []
trace:
  "§4.1.1#r2": 2
  "§4.1.1#r3": [4, 6, 8, 29, 35, 36]
  "§4.1.1#r4": [12, 13]
  "§5#b2": [23, 62, 67, 72, 76]
  "EB-SRC-2@tabel-account-list": [12, 15, 16, 23]
  "EB-SRC-3@tabel-account-list": [25, 27, 31, 33, 38, 39, 41, 42, 44, 45, 47, 50, 53]
  "EB-SRC-1": [6, 8, 56]
anchor: [21, 74]
coverage:
  web: automated
---

# Search Account List menyaring baris menurut kolom yang dicari

## Prerequisites
- Aktor: pengguna Total Control.
- Layar awal: Settings > Accounting > Chart of Accounts.
- Data:
  - DU-002-1: akun `S1-{runId}`, Account Name `Procurement Cabang {runId}`, Account Function `Asset Cost`, Status `Active`, tanpa entri Changelog sama sekali.
  - DU-002-2: akun `S2-{runId}`, Account Name `Biaya Pemeliharaan {runId}`, Account Function `Depreciation Expense`, Status `Active`.
  - DU-002-3: akun `LK9-{runId}`, Account Name `Akun Utama {runId}`, Account Function `Capitalization Offset`, Status `Active`.
  - DU-002-4: akun `S4-{runId}`, Account Name `Akun LK9-{runId}`, Account Function `Disposal Proceeds`, Status `Active`.
  - DU-002-5: akun `S5-{runId}`, Account Name `Head Office Room {runId}`, Account Function `Loss on Disposal`, Status `Active`.
  - DU-002-6: akun `S6-{runId}`, Account Name `Active Reserve {runId}`, Account Function `Gain on Disposal`, Status `Active`.
  - DU-002-7: akun `S7-{runId}`, Account Name `Inactive Reserve {runId}`, Account Function `Accumulated Depreciation`, Status `Active`.
  - DU-002-8: akun `S8-{runId}`, Account Name `Biaya 10% {runId}`, Account Function `Asset Cost`, Status `Active`.
  - DU-002-9: akun `S9-{runId}`, Account Name `Biaya 100 {runId}`, Account Function `Asset Cost`, Status `Active`.
  - DU-002-10: akun `S10-{runId}`, Account Name `Kas_Kecil {runId}`, Account Function `Asset Cost`, Status `Active`.
  - DU-002-11: akun `S11-{runId}`, Account Name `KasXKecil {runId}`, Account Function `Asset Cost`, Status `Active`.
  - DU-002-12: akun `S12-{runId}`, Account Name `Akun.*Lain {runId}`, Account Function `Asset Cost`, Status `Active`.
  - DU-002-13: akun `S13-{runId}`, Account Name `Akun Lain {runId}`, Account Function `Asset Cost`, Status `Active`.
  - DU-002-22: akun `S14-{runId}`, Account Name `Biaya Perawatan Mesin {runId}`, Account Function `Depreciation Expense`, Status `Inactive`.
- Kondisi:
  - Date Format bernilai `dd/MM/yy`.
  - Time Format bernilai `24h`.

## Test Steps

### Search menyaring kolom teks Account Code dan Account Name
1. Ketik Search `S1-{runId}`, tekan Enter
2. Verifikasi baris `S1-{runId}` tampil
3. Ganti isi kotak Search dengan `Procurement Cabang {runId}`, tekan Enter
4. Verifikasi baris `S1-{runId}` tampil

### Pencocokan substring dan huruf besar-kecil
5. Ganti isi kotak Search dengan `curement Cabang {runId}`, tekan Enter
6. Verifikasi baris `S1-{runId}` tampil
7. Ganti isi kotak Search dengan `PROCUREMENT Cabang {runId}`, tekan Enter
8. Verifikasi baris `S1-{runId}` tampil

### Search menyaring kolom badge Function
9. Klik dropdown `Rows per page`
10. Pilih ukuran halaman `100`
11. Ganti isi kotak Search dengan `Asset Cost`, tekan Enter
12. Verifikasi baris `S1-{runId}` tampil
13. Verifikasi baris `S2-{runId}` tidak tampil

### Kata kunci yang cocok di dua kolom berbeda
14. Ganti isi kotak Search dengan `LK9-{runId}`, tekan Enter
15. Verifikasi baris `LK9-{runId}` tampil karena cocok di kolom Account Code
16. Verifikasi baris `S4-{runId}` tampil karena cocok di kolom Account Name

### Kolom tanggal tidak ikut dicari
17. Ganti isi kotak Search dengan `S2-{runId}`, tekan Enter
18. Klik header kolom Actions `⋯`
19. Centang `Last Updated` pada panel Column Visibility
20. Klik header kolom Actions `⋯` untuk menutup panel
21. Verifikasi baris `S2-{runId}` tampil dengan Last Updated terisi
22. Ganti isi kotak Search dengan bagian tanggal (Date Format `dd/MM/yy`) dari sel Last Updated baris `S2-{runId}`, tekan Enter
23. Verifikasi `No results found` tampil

### Spasi di tepi dibuang dan spasi di tengah dipertahankan
24. Ganti isi kotak Search dengan ` Procurement Cabang {runId} ` (satu spasi di awal dan satu spasi di akhir), tekan Enter
25. Verifikasi baris `S1-{runId}` tampil
26. Ganti isi kotak Search dengan `Procurement  Cabang {runId}` (dua spasi di antara `Procurement` dan `Cabang`), tekan Enter
27. Verifikasi `No results found` tampil
28. Ganti isi kotak Search dengan `Head Office Room {runId}`, tekan Enter
29. Verifikasi baris `S5-{runId}` tampil
30. Ganti isi kotak Search dengan `Head Room {runId}`, tekan Enter
31. Verifikasi `No results found` tampil karena query tidak dipecah menjadi kata terpisah
32. Ganti isi kotak Search dengan tiga spasi, tekan Enter
33. Verifikasi `No results found` tidak tampil

### Nilai yang menjadi substring nilai lain
34. Ganti isi kotak Search dengan `Active Reserve {runId}`, tekan Enter
35. Verifikasi baris `S6-{runId}` tampil
36. Verifikasi baris `S7-{runId}` tampil karena `Inactive Reserve {runId}` memuat `Active Reserve {runId}`

### Karakter pola dicari sebagai teks
37. Ganti isi kotak Search dengan `Biaya 10% {runId}`, tekan Enter
38. Verifikasi baris `S8-{runId}` tampil
39. Verifikasi baris `S9-{runId}` tidak tampil
40. Ganti isi kotak Search dengan `Kas_Kecil {runId}`, tekan Enter
41. Verifikasi baris `S10-{runId}` tampil
42. Verifikasi baris `S11-{runId}` tidak tampil
43. Ganti isi kotak Search dengan `Akun.*Lain {runId}`, tekan Enter
44. Verifikasi baris `S12-{runId}` tampil
45. Verifikasi baris `S13-{runId}` tidak tampil

### Payload skrip, SQL, dan NoSQL dicari sebagai teks
46. Ganti isi kotak Search dengan `<script>alert(1)</script> {runId}`, tekan Enter
47. Verifikasi `No results found` tampil
48. Klik `(←)` pada kotak Search
49. Ketik Search `' OR '1'='1 {runId}`, tekan Enter
50. Verifikasi `No results found` tampil
51. Klik `(←)` pada kotak Search
52. Ketik Search `{"$ne": null} {runId}`, tekan Enter
53. Verifikasi `No results found` tampil
54. Klik `(←)` pada kotak Search

### Kata kunci tanpa kecocokan
55. Ketik Search `tidakada-{runId}`, tekan Enter
56. Verifikasi `No results found` tampil
57. Klik `(←)` pada kotak Search

### Kolom yang di-hide tidak ikut dicari
58. Klik header kolom Actions `⋯`
59. Hapus centang `Account Name` pada panel Column Visibility
60. Klik header kolom Actions `⋯` untuk menutup panel
61. Ketik Search `Procurement Cabang {runId}`, tekan Enter
62. Verifikasi `No results found` tampil
63. Klik header kolom Actions `⋯`
64. Centang `Account Name` pada panel Column Visibility
65. Klik header kolom Actions `⋯` untuk menutup panel
66. Tekan Enter pada kotak Search
67. Verifikasi baris `S1-{runId}` tampil

### Kolom Modified By ikut dicari
68. Klik header kolom Actions `⋯`
69. Centang `Modified By` pada panel Column Visibility
70. Klik header kolom Actions `⋯` untuk menutup panel
71. Ganti isi kotak Search dengan `System`, tekan Enter
72. Verifikasi baris `S1-{runId}` tampil dengan Modified By `System`

### Switch Status tidak ikut dicari
73. Ganti isi kotak Search dengan `S14-{runId}`, tekan Enter
74. Verifikasi switch Status baris `S14-{runId}` dalam keadaan `Inactive`
75. Ganti isi kotak Search dengan `Inactive`, tekan Enter
76. Verifikasi baris `S14-{runId}` tidak tampil
77. Klik `(←)` pada kotak Search
