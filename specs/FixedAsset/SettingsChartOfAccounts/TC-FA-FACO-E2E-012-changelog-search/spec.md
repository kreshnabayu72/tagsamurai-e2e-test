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
  "§4.1.1#r22": 39
  "§4.1.1#r23": 31
  "§4.1.1#r24": 33
  "§4.1.1#r25": 35
  "§4.1.1#r26": 37
  "§4.1.1#r27": 42
  "EB-SRC-2@tabel-changelog": [35, 40, 44, 48, 50, 51, 73, 78]
  "EB-SRC-3@tabel-changelog": [46, 53, 55, 57, 59, 61, 62, 64, 66]
anchor: [68]
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
30. Ketik Search `CS1-{runId}` pada modal Changelog, tekan Enter
31. Verifikasi entri `CS1-{runId}` tampil di modal Changelog karena cocok di kolom Account Code
32. Ganti isi kotak Search modal Changelog dengan `Account Name`, tekan Enter
33. Verifikasi entri `CS1-{runId}` tampil di modal Changelog karena cocok di kolom Field
34. Ganti isi kotak Search modal Changelog dengan `Procurement Cabang {runId}`, tekan Enter
35. Verifikasi entri `CS1-{runId}` tampil di modal Changelog karena cocok di kolom Old Value
36. Ganti isi kotak Search modal Changelog dengan `Procurement Cabang Baru {runId}`, tekan Enter
37. Verifikasi entri `CS1-{runId}` tampil di modal Changelog karena cocok di kolom New Value
38. Ganti isi kotak Search modal Changelog dengan `Delete`, tekan Enter
39. Verifikasi entri `CS7-{runId}` tampil di modal Changelog karena cocok di kolom Action
40. Verifikasi entri `CS1-{runId}` tidak tampil di modal Changelog karena tidak ada kolom visibelnya yang memuat `Delete`
41. Ganti isi kotak Search modal Changelog dengan teks Modified By persis seperti tampil pada baris entri `CS1-{runId}`, tekan Enter
42. Verifikasi entri `CS1-{runId}` tampil di modal Changelog karena cocok di kolom Modified By

### Pencocokan substring dan huruf besar-kecil
43. Ganti isi kotak Search modal Changelog dengan `curement Cabang {runId}`, tekan Enter
44. Verifikasi entri `CS1-{runId}` tampil di modal Changelog karena kata kunci cocok di bagian tengah nilai
45. Ganti isi kotak Search modal Changelog dengan `PROCUREMENT Cabang {runId}`, tekan Enter
46. Verifikasi entri `CS1-{runId}` tampil di modal Changelog tanpa membedakan huruf besar-kecil

### Kolom tanggal tidak ikut dicari dan kata kunci yang cocok di dua kolom
47. Ganti isi kotak Search modal Changelog dengan bagian tanggal (Date Format `dd/MM/yy`) dari sel Date entri `CS1-{runId}`, tekan Enter
48. Verifikasi `No results found` tampil di modal Changelog karena kolom Date tidak dicari
49. Ganti isi kotak Search modal Changelog dengan `CS6-{runId}`, tekan Enter
50. Verifikasi entri `CS6-{runId}` tampil di modal Changelog karena cocok di kolom Account Code
51. Verifikasi entri `CS5-{runId}` tampil di modal Changelog karena cocok di kolom Old Value

### Spasi di tepi dibuang dan spasi di tengah dipertahankan
52. Ganti isi kotak Search modal Changelog dengan ` Procurement Cabang {runId} ` (satu spasi di awal dan satu spasi di akhir), tekan Enter
53. Verifikasi entri `CS1-{runId}` tampil di modal Changelog sesudah spasi di tepi dibuang
54. Ganti isi kotak Search modal Changelog dengan `Procurement  Cabang {runId}` (dua spasi di antara `Procurement` dan `Cabang`), tekan Enter
55. Verifikasi `No results found` tampil di modal Changelog karena spasi di tengah dipertahankan
56. Ganti isi kotak Search modal Changelog dengan `Head Office Room {runId}`, tekan Enter
57. Verifikasi entri `CS2-{runId}` tampil di modal Changelog
58. Ganti isi kotak Search modal Changelog dengan `Head Room {runId}`, tekan Enter
59. Verifikasi `No results found` tampil di modal Changelog karena kata kunci tidak dipecah menjadi kata terpisah

### Karakter pola dicari sebagai teks
60. Ganti isi kotak Search modal Changelog dengan `Biaya 10% {runId}`, tekan Enter
61. Verifikasi entri `CS3-{runId}` tampil di modal Changelog
62. Verifikasi entri `CS4-{runId}` tidak tampil di modal Changelog karena `%` dicari sebagai karakter biasa
63. Ganti isi kotak Search modal Changelog dengan `<script>alert(1)</script> {runId}`, tekan Enter
64. Verifikasi `No results found` tampil di modal Changelog karena payload skrip dicari sebagai teks

### Kata kunci tanpa kecocokan
65. Ganti isi kotak Search modal Changelog dengan `tidakada-{runId}`, tekan Enter
66. Verifikasi `No results found` tampil di modal Changelog karena kata kunci tidak cocok dengan entri mana pun

### Kolom yang di-hide tidak ikut dicari
67. Ganti isi kotak Search modal Changelog dengan `Procurement Cabang Baru {runId}`, tekan Enter
68. Verifikasi entri `CS1-{runId}` tampil di modal Changelog
69. Klik header kolom Actions `⋯` pada tabel Changelog
70. Hapus centang `New Value` pada panel Column Visibility
71. Klik header kolom Actions `⋯` untuk menutup panel
72. Tekan Enter pada kotak Search modal Changelog
73. Verifikasi `No results found` tampil di modal Changelog karena kolom New Value di-hide
74. Klik header kolom Actions `⋯` pada tabel Changelog
75. Centang `New Value` pada panel Column Visibility
76. Klik header kolom Actions `⋯` untuk menutup panel
77. Tekan Enter pada kotak Search modal Changelog
78. Verifikasi entri `CS1-{runId}` tampil kembali di modal Changelog karena kolom New Value ditampilkan
