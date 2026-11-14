---
id: TC-FA-FACO-E2E-012-changelog-search
title: "Search di modal Changelog menyaring entri"
layer: ui-e2e
priority: Medium
caseType: Positive
status: draft
sourceRules: ["§4.1.1#r22", "§4.1.1#r23", "§4.1.1#r24", "§4.1.1#r25", "§4.1.1#r26", "§4.1.1#r27", "EB-SRC-2@tabel-changelog", "EB-SRC-3@tabel-changelog"]
smoke: []
dependsOn: []
trace:
  "§4.1.1#r22": 42
  "§4.1.1#r23": 34
  "§4.1.1#r24": 36
  "§4.1.1#r25": 38
  "§4.1.1#r26": 40
  "§4.1.1#r27": 45
  "EB-SRC-2@tabel-changelog": [38, 43, 49, 53, 55, 56, 78, 83]
  "EB-SRC-3@tabel-changelog": [51, 58, 60, 62, 64, 66, 67, 69, 71]
anchor: [73]
coverage:
  web: automated
---

# Search di modal Changelog menyaring entri

## Prerequisites
- Aktor: pengguna Total Control (nama lengkap terdiri dari nama depan dan nama belakang).
- Layar awal: Settings > Accounting > Chart of Accounts.
- Data:
  - Setiap akun disimpan tanpa entri Changelog, lalu Account Name-nya diubah pada langkah spec ini sehingga menghasilkan tepat satu entri Edit dengan Field `Account Name`, kecuali DU-012-7 yang dihapus dan menghasilkan satu entri Delete.
  - DU-012-1: akun `CS1-{runId}`, Account Name `Procurement Cabang {runId}`, Account Function `Asset Cost`, Status `Active`. Account Name sesudah Edit: `Procurement Cabang Baru {runId}`.
  - DU-012-2: akun `CS2-{runId}`, Account Name `Head Office Room {runId}`, Account Function `Asset Cost`, Status `Active`. Account Name sesudah Edit: `Ruang Kantor {runId}`.
  - DU-012-3: akun `CS3-{runId}`, Account Name `Biaya 10% {runId}`, Account Function `Asset Cost`, Status `Active`. Account Name sesudah Edit: `Biaya Pokok {runId}`.
  - DU-012-4: akun `CS4-{runId}`, Account Name `Biaya 100 {runId}`, Account Function `Asset Cost`, Status `Active`. Account Name sesudah Edit: `Biaya Lain {runId}`.
  - DU-012-5: akun `CS5-{runId}`, Account Name `Salin CS6-{runId}`, Account Function `Asset Cost`, Status `Active`. Account Name sesudah Edit: `Salin Akhir {runId}`.
  - DU-012-6: akun `CS6-{runId}`, Account Name `Akun Enam {runId}`, Account Function `Asset Cost`, Status `Active`. Account Name sesudah Edit: `Akun Enam B {runId}`.
  - DU-012-7: akun `CS7-{runId}`, Account Name `Akun Hapus {runId}`, Account Function `Asset Cost`, Status `Active`. Akun ini dihapus pada langkah spec ini.
- Kondisi:
  - Date Format bernilai `dd/MM/yy`.
  - Time Format bernilai `24h`.

## Test Steps
### Search menyaring kolom teks pada modal Changelog
1. Ketik Search `CS1-{runId}`, tekan Enter
2. Klik `⋯` pada baris `CS1-{runId}` > `Edit`
3. Ganti isi Account Name dengan `Procurement Cabang Baru {runId}`
4. Klik `[Save]`
5. Ganti isi kotak Search dengan `CS2-{runId}`, tekan Enter
6. Klik `⋯` pada baris `CS2-{runId}` > `Edit`
7. Ganti isi Account Name dengan `Ruang Kantor {runId}`
8. Klik `[Save]`
9. Ganti isi kotak Search dengan `CS3-{runId}`, tekan Enter
10. Klik `⋯` pada baris `CS3-{runId}` > `Edit`
11. Ganti isi Account Name dengan `Biaya Pokok {runId}`
12. Klik `[Save]`
13. Ganti isi kotak Search dengan `CS4-{runId}`, tekan Enter
14. Klik `⋯` pada baris `CS4-{runId}` > `Edit`
15. Ganti isi Account Name dengan `Biaya Lain {runId}`
16. Klik `[Save]`
17. Ganti isi kotak Search dengan `CS5-{runId}`, tekan Enter
18. Klik `⋯` pada baris `CS5-{runId}` > `Edit`
19. Ganti isi Account Name dengan `Salin Akhir {runId}`
20. Klik `[Save]`
21. Ganti isi kotak Search dengan `CS6-{runId}`, tekan Enter
22. Klik `⋯` pada baris `CS6-{runId}` > `Edit`
23. Ganti isi Account Name dengan `Akun Enam B {runId}`
24. Klik `[Save]`
25. Ganti isi kotak Search dengan `CS7-{runId}`, tekan Enter
26. Klik `⋯` pada baris `CS7-{runId}` > `Delete`
27. Klik `[Delete]` pada dialog `Delete Account`
28. Klik `(←)` pada kotak Search
29. Klik ikon Changelog
30. Klik ikon Filter pada modal Changelog
31. Pilih `CS1-{runId}` dan `CS7-{runId}` pada field Account Code
32. Klik `[Apply]`
33. Ketik Search `CS1-{runId}` pada modal Changelog, tekan Enter
34. Verifikasi entri `CS1-{runId}` tampil di modal Changelog karena cocok di kolom Account Code
35. Ganti isi kotak Search modal Changelog dengan `Account Name`, tekan Enter
36. Verifikasi entri `CS1-{runId}` tampil di modal Changelog karena cocok di kolom Field
37. Ganti isi kotak Search modal Changelog dengan `Procurement Cabang {runId}`, tekan Enter
38. Verifikasi entri `CS1-{runId}` tampil di modal Changelog karena cocok di kolom Old Value
39. Ganti isi kotak Search modal Changelog dengan `Procurement Cabang Baru {runId}`, tekan Enter
40. Verifikasi entri `CS1-{runId}` tampil di modal Changelog karena cocok di kolom New Value
41. Ganti isi kotak Search modal Changelog dengan `Delete`, tekan Enter
42. Verifikasi entri `CS7-{runId}` tampil di modal Changelog karena cocok di kolom Action
43. Verifikasi entri `CS1-{runId}` tidak tampil di modal Changelog karena tidak ada kolom visibelnya yang memuat `Delete`
44. Ganti isi kotak Search modal Changelog dengan teks Modified By persis seperti tampil pada baris entri `CS1-{runId}`, tekan Enter
45. Verifikasi entri `CS1-{runId}` tampil di modal Changelog karena cocok di kolom Modified By
46. Klik `[Clear Field]`
47. Klik `[Apply]`

### Pencocokan substring dan huruf besar-kecil
48. Ganti isi kotak Search modal Changelog dengan `curement Cabang {runId}`, tekan Enter
49. Verifikasi entri `CS1-{runId}` tampil di modal Changelog karena kata kunci cocok di bagian tengah nilai
50. Ganti isi kotak Search modal Changelog dengan `PROCUREMENT Cabang {runId}`, tekan Enter
51. Verifikasi entri `CS1-{runId}` tampil di modal Changelog tanpa membedakan huruf besar-kecil

### Kolom tanggal tidak ikut dicari dan kata kunci yang cocok di dua kolom
52. Ganti isi kotak Search modal Changelog dengan bagian tanggal (Date Format `dd/MM/yy`) dari sel Date entri `CS1-{runId}`, tekan Enter
53. Verifikasi `No results found` tampil di modal Changelog karena kolom Date tidak dicari
54. Ganti isi kotak Search modal Changelog dengan `CS6-{runId}`, tekan Enter
55. Verifikasi entri `CS6-{runId}` tampil di modal Changelog karena cocok di kolom Account Code
56. Verifikasi entri `CS5-{runId}` tampil di modal Changelog karena cocok di kolom Old Value

### Spasi di tepi dibuang dan spasi di tengah dipertahankan
57. Ganti isi kotak Search modal Changelog dengan ` Procurement Cabang {runId} ` (satu spasi di awal dan satu spasi di akhir), tekan Enter
58. Verifikasi entri `CS1-{runId}` tampil di modal Changelog sesudah spasi di tepi dibuang
59. Ganti isi kotak Search modal Changelog dengan `Procurement  Cabang {runId}` (dua spasi di antara `Procurement` dan `Cabang`), tekan Enter
60. Verifikasi `No results found` tampil di modal Changelog karena spasi di tengah dipertahankan
61. Ganti isi kotak Search modal Changelog dengan `Head Office Room {runId}`, tekan Enter
62. Verifikasi entri `CS2-{runId}` tampil di modal Changelog
63. Ganti isi kotak Search modal Changelog dengan `Head Room {runId}`, tekan Enter
64. Verifikasi `No results found` tampil di modal Changelog karena kata kunci tidak dipecah menjadi kata terpisah

### Karakter pola dicari sebagai teks
65. Ganti isi kotak Search modal Changelog dengan `Biaya 10% {runId}`, tekan Enter
66. Verifikasi entri `CS3-{runId}` tampil di modal Changelog
67. Verifikasi entri `CS4-{runId}` tidak tampil di modal Changelog karena `%` dicari sebagai karakter biasa
68. Ganti isi kotak Search modal Changelog dengan `<script>alert(1)</script> {runId}`, tekan Enter
69. Verifikasi `No results found` tampil di modal Changelog karena payload skrip dicari sebagai teks

### Kata kunci tanpa kecocokan
70. Ganti isi kotak Search modal Changelog dengan `tidakada-{runId}`, tekan Enter
71. Verifikasi `No results found` tampil di modal Changelog karena kata kunci tidak cocok dengan entri mana pun

### Kolom yang di-hide tidak ikut dicari
72. Ganti isi kotak Search modal Changelog dengan `Procurement Cabang Baru {runId}`, tekan Enter
73. Verifikasi entri `CS1-{runId}` tampil di modal Changelog
74. Klik header kolom Actions `⋯` pada tabel Changelog
75. Hapus centang `New Value` pada panel Column Visibility
76. Klik header kolom Actions `⋯` untuk menutup panel
77. Tekan Enter pada kotak Search modal Changelog
78. Verifikasi `No results found` tampil di modal Changelog karena kolom New Value di-hide
79. Klik header kolom Actions `⋯` pada tabel Changelog
80. Centang `New Value` pada panel Column Visibility
81. Klik header kolom Actions `⋯` untuk menutup panel
82. Tekan Enter pada kotak Search modal Changelog
83. Verifikasi entri `CS1-{runId}` tampil kembali di modal Changelog karena kolom New Value ditampilkan
