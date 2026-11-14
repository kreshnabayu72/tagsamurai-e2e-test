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
  "§4.1.1#r3": [4, 6, 8, 27, 33, 34]
  "§4.1.1#r4": [10, 11]
  "§5#b2": [21, 60, 65, 70, 74]
  "EB-SRC-2@tabel-account-list": [10, 13, 14, 21]
  "EB-SRC-3@tabel-account-list": [23, 25, 29, 31, 36, 37, 39, 40, 42, 43, 45, 48, 51]
  "EB-SRC-1": [6, 8, 54]
anchor: [19, 72]
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
9. Ganti isi kotak Search dengan `Asset Cost`, tekan Enter
10. Verifikasi baris `S1-{runId}` tampil
11. Verifikasi baris `S2-{runId}` tidak tampil

### Kata kunci yang cocok di dua kolom berbeda
12. Ganti isi kotak Search dengan `LK9-{runId}`, tekan Enter
13. Verifikasi baris `LK9-{runId}` tampil karena cocok di kolom Account Code
14. Verifikasi baris `S4-{runId}` tampil karena cocok di kolom Account Name

### Kolom tanggal tidak ikut dicari
15. Ganti isi kotak Search dengan `S2-{runId}`, tekan Enter
16. Klik header kolom Actions `⋯`
17. Centang `Last Updated` pada panel Column Visibility
18. Klik header kolom Actions `⋯` untuk menutup panel
19. Verifikasi baris `S2-{runId}` tampil dengan Last Updated terisi
20. Ganti isi kotak Search dengan bagian tanggal (Date Format `dd/MM/yy`) dari sel Last Updated baris `S2-{runId}`, tekan Enter
21. Verifikasi `No results found` tampil

### Spasi di tepi dibuang dan spasi di tengah dipertahankan
22. Ganti isi kotak Search dengan ` Procurement Cabang {runId} ` (satu spasi di awal dan satu spasi di akhir), tekan Enter
23. Verifikasi baris `S1-{runId}` tampil
24. Ganti isi kotak Search dengan `Procurement  Cabang {runId}` (dua spasi di antara `Procurement` dan `Cabang`), tekan Enter
25. Verifikasi `No results found` tampil
26. Ganti isi kotak Search dengan `Head Office Room {runId}`, tekan Enter
27. Verifikasi baris `S5-{runId}` tampil
28. Ganti isi kotak Search dengan `Head Room {runId}`, tekan Enter
29. Verifikasi `No results found` tampil karena query tidak dipecah menjadi kata terpisah
30. Ganti isi kotak Search dengan tiga spasi, tekan Enter
31. Verifikasi `No results found` tidak tampil

### Nilai yang menjadi substring nilai lain
32. Ganti isi kotak Search dengan `Active Reserve {runId}`, tekan Enter
33. Verifikasi baris `S6-{runId}` tampil
34. Verifikasi baris `S7-{runId}` tampil karena `Inactive Reserve {runId}` memuat `Active Reserve {runId}`

### Karakter pola dicari sebagai teks
35. Ganti isi kotak Search dengan `Biaya 10% {runId}`, tekan Enter
36. Verifikasi baris `S8-{runId}` tampil
37. Verifikasi baris `S9-{runId}` tidak tampil
38. Ganti isi kotak Search dengan `Kas_Kecil {runId}`, tekan Enter
39. Verifikasi baris `S10-{runId}` tampil
40. Verifikasi baris `S11-{runId}` tidak tampil
41. Ganti isi kotak Search dengan `Akun.*Lain {runId}`, tekan Enter
42. Verifikasi baris `S12-{runId}` tampil
43. Verifikasi baris `S13-{runId}` tidak tampil

### Payload skrip, SQL, dan NoSQL dicari sebagai teks
44. Ganti isi kotak Search dengan `<script>alert(1)</script> {runId}`, tekan Enter
45. Verifikasi `No results found` tampil
46. Klik `(←)` pada kotak Search
47. Ketik Search `' OR '1'='1 {runId}`, tekan Enter
48. Verifikasi `No results found` tampil
49. Klik `(←)` pada kotak Search
50. Ketik Search `{"$ne": null} {runId}`, tekan Enter
51. Verifikasi `No results found` tampil
52. Klik `(←)` pada kotak Search

### Kata kunci tanpa kecocokan
53. Ketik Search `tidakada-{runId}`, tekan Enter
54. Verifikasi `No results found` tampil
55. Klik `(←)` pada kotak Search

### Kolom yang di-hide tidak ikut dicari
56. Klik header kolom Actions `⋯`
57. Hapus centang `Account Name` pada panel Column Visibility
58. Klik header kolom Actions `⋯` untuk menutup panel
59. Ketik Search `Procurement Cabang {runId}`, tekan Enter
60. Verifikasi `No results found` tampil
61. Klik header kolom Actions `⋯`
62. Centang `Account Name` pada panel Column Visibility
63. Klik header kolom Actions `⋯` untuk menutup panel
64. Tekan Enter pada kotak Search
65. Verifikasi baris `S1-{runId}` tampil

### Kolom Modified By ikut dicari
66. Klik header kolom Actions `⋯`
67. Centang `Modified By` pada panel Column Visibility
68. Klik header kolom Actions `⋯` untuk menutup panel
69. Ganti isi kotak Search dengan `System`, tekan Enter
70. Verifikasi baris `S1-{runId}` tampil dengan Modified By `System`

### Switch Status tidak ikut dicari
71. Ganti isi kotak Search dengan `S14-{runId}`, tekan Enter
72. Verifikasi switch Status baris `S14-{runId}` dalam keadaan `Inactive`
73. Ganti isi kotak Search dengan `Inactive`, tekan Enter
74. Verifikasi baris `S14-{runId}` tidak tampil
75. Klik `(←)` pada kotak Search
