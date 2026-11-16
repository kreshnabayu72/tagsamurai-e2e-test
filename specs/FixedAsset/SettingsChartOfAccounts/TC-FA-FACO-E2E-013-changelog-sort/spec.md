---
id: TC-FA-FACO-E2E-013-changelog-sort
title: "Sort di modal Changelog mengurutkan entri per kolom"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["§4.1.1#p7", "§4.1.1#r21", "§4.1.1#r22", "§4.1.1#r23", "§4.1.1#r24", "§4.1.1#r25", "§4.1.1#r26", "§4.1.1#r27", "EB-SRT-3@tabel-changelog"]
smoke: []
dependsOn: []
trace:
  "§4.1.1#p7": 37
  "§4.1.1#r21": [37, 39, 41]
  "§4.1.1#r22": [49, 51]
  "§4.1.1#r23": [43, 45]
  "§4.1.1#r24": [53, 55]
  "§4.1.1#r25": [57, 59]
  "§4.1.1#r26": [61, 63]
  "§4.1.1#r27": [65, 66, 68, 69]
  "EB-SRT-3@tabel-changelog": [47, 71]
coverage:
  web: automated
---

# Sort di modal Changelog mengurutkan entri per kolom

## Prerequisites
- Aktor: pengguna Total Control (aktor M). Aktor lain: Admin B (DU-013-11) dan Admin C (DU-013-12).
- Layar awal: Settings > Accounting > Chart of Accounts.
- Data:
  - Sepuluh akun dengan Account Code berbentuk QS-{runId}-huruf, masing-masing menghasilkan tepat satu entri Changelog pada langkah spec ini. Seluruh Account Code berbentuk QS-{runId}-huruf, sehingga Search `QS-{runId}` pada modal Changelog menampilkan sepuluh entri ini. Entri dibuat berurutan E1 sampai E10 (E1 paling lama).
  - DU-013-1 (E1, aktor M): akun `QS-{runId}-c`, Account Name `Melati`, Account Function `Asset Cost`, Status `Active`. Edit Account Name menjadi `Mawar`.
  - DU-013-2 (E2, aktor M): akun `QS-{runId}-a`, Account Name `anggur`, Account Function `Asset Cost`, Status `Active`. Edit Account Name menjadi `zebra`.
  - DU-013-3 (E3, aktor M): akun `QS-{runId}-h`, Account Name `Apel`, Account Function `Asset Cost`, Status `Active`. Edit Account Name menjadi `Bambu`.
  - DU-013-4 (E4, aktor M): akun `QS-{runId}-B`, Account Name `500`, Account Function `Asset Cost`, Status `Active`. Edit Account Name menjadi `90`.
  - DU-013-5 (E5, aktor M): akun `QS-{runId}-e`, dibuat lewat form dengan Account Name `Akun Baru Urut {runId}`, Account Function `Asset Cost`, menghasilkan entri Create.
  - DU-013-6 (E6, aktor M): akun `QS-{runId}-j`, Account Name `Akun Hapus Urut {runId}`, Account Function `Asset Cost`, Status `Active`. Akun dihapus, menghasilkan entri Delete.
  - DU-013-7 (E7, aktor M): akun `QS-{runId}-D`, Account Name `Akun Fungsi Urut {runId}`, Account Function `Asset Cost`, Status `Active`. Edit Account Function menjadi `Gain on Disposal`.
  - DU-013-8 (E8, aktor M): akun `QS-{runId}-f`, Account Name `Akun Status Urut {runId}`, Account Function `Asset Cost`, Status `Active`. Dinonaktifkan lewat switch Status, menghasilkan entri Field `Status`.
  - DU-013-9 (E9, Admin B): akun `QS-{runId}-i`, Account Name `Melati`, Account Function `Asset Cost`, Status `Active`. Admin B mengubah Account Name menjadi `Mawar`.
  - DU-013-10 (E10, Admin C): akun `QS-{runId}-g`, Account Name `70`, Account Function `Asset Cost`, Status `Active`. Admin C mengubah Account Name menjadi `400`.
  - DU-013-11: Admin B, nama lengkap `Lina Adi` (nama tampil Lina A), role Total Control, cakupan seluruh client, akun aktif dan kredensialnya disediakan fase 2.
  - DU-013-12: Admin C, nama lengkap `Lina Agus` (nama tampil Lina A), role Total Control, cakupan seluruh client, akun aktif dan kredensialnya disediakan fase 2.
- Kondisi:
  - Ukuran halaman modal Changelog adalah 10 baris (nilai bawaan), sehingga sepuluh entri muat di satu halaman.
  - Aturan sort alfabetis memakai ICU collation `en-US`.

## Test Steps
### Urutan default Newest First dan sort kolom Date
1. Ketik Search `QS-{runId}-c`, tekan Enter
2. Klik `⋯` pada baris `QS-{runId}-c` > `Edit`
3. Ganti isi Account Name dengan `Mawar`
4. Klik `[Save]`
5. Ganti isi kotak Search dengan `QS-{runId}-a`, tekan Enter
6. Klik `⋯` pada baris `QS-{runId}-a` > `Edit`
7. Ganti isi Account Name dengan `zebra`
8. Klik `[Save]`
9. Ganti isi kotak Search dengan `QS-{runId}-h`, tekan Enter
10. Klik `⋯` pada baris `QS-{runId}-h` > `Edit`
11. Ganti isi Account Name dengan `Bambu`
12. Klik `[Save]`
13. Ganti isi kotak Search dengan `QS-{runId}-B`, tekan Enter
14. Klik `⋯` pada baris `QS-{runId}-B` > `Edit`
15. Ganti isi Account Name dengan `90`
16. Klik `[Save]`
17. Klik `(←)` pada kotak Search
18. Klik `[+ Account]`
19. Isi Account Code `QS-{runId}-e`
20. Isi Account Name `Akun Baru Urut {runId}`
21. Pilih `Asset Cost` pada field Account Function
22. Klik `[Submit]`
23. Ketik Search `QS-{runId}-j`, tekan Enter
24. Klik `⋯` pada baris `QS-{runId}-j` > `Delete`
25. Klik `[Delete]` pada dialog `Delete Account`
26. Ganti isi kotak Search dengan `QS-{runId}-D`, tekan Enter
27. Klik `⋯` pada baris `QS-{runId}-D` > `Edit`
28. Pilih `Gain on Disposal` pada field Account Function
29. Klik `[Save]`
30. Ganti isi kotak Search dengan `QS-{runId}-f`, tekan Enter
31. Klik switch Status baris `QS-{runId}-f`
32. Klik `[Deactivate]` pada dialog `Deactivate Account`
33. Admin B mengubah Account Name `QS-{runId}-i` dari `Melati` menjadi `Mawar`
34. Admin C mengubah Account Name `QS-{runId}-g` dari `70` menjadi `400`
35. Klik ikon Changelog
36. Ketik Search `QS-{runId}` pada modal Changelog, tekan Enter
37. Verifikasi modal memuat sepuluh entri, dengan urutan default Newest First menurut Account Code: `QS-{runId}-g`, `QS-{runId}-i`, `QS-{runId}-f`, `QS-{runId}-D`, `QS-{runId}-j`, `QS-{runId}-e`, `QS-{runId}-B`, `QS-{runId}-h`, `QS-{runId}-a`, `QS-{runId}-c`
38. Klik header kolom Date (klik pertama)
39. Verifikasi urutan entri menaik (Oldest First) menurut Date, entri yang ditulis lebih akhir tampil lebih bawah, ditulis dengan Account Code: `QS-{runId}-c`, `QS-{runId}-a`, `QS-{runId}-h`, `QS-{runId}-B`, `QS-{runId}-e`, `QS-{runId}-j`, `QS-{runId}-D`, `QS-{runId}-f`, `QS-{runId}-i`, `QS-{runId}-g`
40. Klik header kolom Date (klik kedua)
41. Verifikasi urutan entri menurun (Newest First) menurut Date: `QS-{runId}-g`, `QS-{runId}-i`, `QS-{runId}-f`, `QS-{runId}-D`, `QS-{runId}-j`, `QS-{runId}-e`, `QS-{runId}-B`, `QS-{runId}-h`, `QS-{runId}-a`, `QS-{runId}-c`

### Sort Account Code tanpa membedakan huruf besar-kecil dan kembali ke urutan default
42. Klik header kolom Account Code (klik pertama pada kolom ini, sementara kolom Date sedang aktif)
43. Verifikasi urutan entri menaik menurut Account Code tanpa membedakan huruf besar-kecil, bukan menurut Date: `QS-{runId}-a`, `QS-{runId}-B`, `QS-{runId}-c`, `QS-{runId}-D`, `QS-{runId}-e`, `QS-{runId}-f`, `QS-{runId}-g`, `QS-{runId}-h`, `QS-{runId}-i`, `QS-{runId}-j`
44. Klik header kolom Account Code (klik kedua)
45. Verifikasi urutan entri menurun menurut Account Code: `QS-{runId}-j`, `QS-{runId}-i`, `QS-{runId}-h`, `QS-{runId}-g`, `QS-{runId}-f`, `QS-{runId}-e`, `QS-{runId}-D`, `QS-{runId}-c`, `QS-{runId}-B`, `QS-{runId}-a`
46. Klik header kolom Account Code (klik ketiga)
47. Verifikasi urutan entri kembali ke urutan default Newest First: `QS-{runId}-g`, `QS-{runId}-i`, `QS-{runId}-f`, `QS-{runId}-D`, `QS-{runId}-j`, `QS-{runId}-e`, `QS-{runId}-B`, `QS-{runId}-h`, `QS-{runId}-a`, `QS-{runId}-c`

### Sort Action dengan nilai sama diurutkan menurut default sort
48. Klik header kolom Action (klik pertama)
49. Verifikasi urutan entri menaik menurut Action: entri Create, lalu Delete, lalu delapan entri Edit yang tetap Newest First: `QS-{runId}-e`, `QS-{runId}-j`, `QS-{runId}-g`, `QS-{runId}-i`, `QS-{runId}-f`, `QS-{runId}-D`, `QS-{runId}-B`, `QS-{runId}-h`, `QS-{runId}-a`, `QS-{runId}-c`
50. Klik header kolom Action (klik kedua)
51. Verifikasi urutan entri menurun menurut Action: delapan entri Edit yang tetap Newest First, lalu Delete, lalu Create: `QS-{runId}-g`, `QS-{runId}-i`, `QS-{runId}-f`, `QS-{runId}-D`, `QS-{runId}-B`, `QS-{runId}-h`, `QS-{runId}-a`, `QS-{runId}-c`, `QS-{runId}-j`, `QS-{runId}-e`

### Sort Field menurut nama field
52. Klik header kolom Field (klik pertama)
53. Verifikasi urutan entri menaik menurut Field: `Account Code` (Newest First), `Account Function`, `Account Name` (Newest First), `Status`: `QS-{runId}-j`, `QS-{runId}-e`, `QS-{runId}-D`, `QS-{runId}-g`, `QS-{runId}-i`, `QS-{runId}-B`, `QS-{runId}-h`, `QS-{runId}-a`, `QS-{runId}-c`, `QS-{runId}-f`
54. Klik header kolom Field (klik kedua)
55. Verifikasi urutan entri menurun menurut Field: `Status`, `Account Name` (Newest First), `Account Function`, `Account Code` (Newest First): `QS-{runId}-f`, `QS-{runId}-g`, `QS-{runId}-i`, `QS-{runId}-B`, `QS-{runId}-h`, `QS-{runId}-a`, `QS-{runId}-c`, `QS-{runId}-D`, `QS-{runId}-j`, `QS-{runId}-e`

### Sort Old Value dengan nilai campuran numerik, teks, dan kosong
56. Klik header kolom Old Value (klik pertama)
57. Verifikasi urutan entri menaik menurut Old Value: angka `70` dan `500` lebih dulu, lalu teks A-Z, nilai sama `Melati` tetap Newest First, nilai kosong `—` di akhir: `QS-{runId}-g`, `QS-{runId}-B`, `QS-{runId}-f`, `QS-{runId}-a`, `QS-{runId}-h`, `QS-{runId}-D`, `QS-{runId}-i`, `QS-{runId}-c`, `QS-{runId}-j`, `QS-{runId}-e`
58. Klik header kolom Old Value (klik kedua)
59. Verifikasi urutan entri menurun menurut Old Value: nilai kosong `—` di awal, teks Z-A, lalu angka `500` dan `70`: `QS-{runId}-e`, `QS-{runId}-j`, `QS-{runId}-i`, `QS-{runId}-c`, `QS-{runId}-D`, `QS-{runId}-h`, `QS-{runId}-a`, `QS-{runId}-f`, `QS-{runId}-B`, `QS-{runId}-g`

### Sort New Value dengan nilai kosong
60. Klik header kolom New Value (klik pertama)
61. Verifikasi urutan entri menaik menurut New Value: angka `90` dan `400` lebih dulu menurut nilai angkanya, lalu teks A-Z tanpa membedakan huruf besar-kecil, nilai sama `Mawar` tetap Newest First, nilai kosong `—` di akhir: `QS-{runId}-B`, `QS-{runId}-g`, `QS-{runId}-h`, `QS-{runId}-D`, `QS-{runId}-f`, `QS-{runId}-i`, `QS-{runId}-c`, `QS-{runId}-e`, `QS-{runId}-a`, `QS-{runId}-j`
62. Klik header kolom New Value (klik kedua)
63. Verifikasi urutan entri menurun menurut New Value: nilai kosong `—` di awal, teks Z-A, lalu angka `400` dan `90`: `QS-{runId}-j`, `QS-{runId}-a`, `QS-{runId}-e`, `QS-{runId}-i`, `QS-{runId}-c`, `QS-{runId}-f`, `QS-{runId}-D`, `QS-{runId}-h`, `QS-{runId}-g`, `QS-{runId}-B`

### Sort Modified By menurut nama lengkap dan nilai sama menurut default sort
64. Klik header kolom Modified By (klik pertama)
65. Verifikasi pada urutan menaik menurut Modified By, entri milik Admin B (`QS-{runId}-i`) tampil sebelum entri milik Admin C (`QS-{runId}-g`), walau keduanya tampil sebagai Lina A, karena nama lengkap `Lina Adi` mendahului `Lina Agus`
66. Verifikasi delapan entri milik aktor M tampil berurutan Newest First di dalam satu blok: `QS-{runId}-f`, `QS-{runId}-D`, `QS-{runId}-j`, `QS-{runId}-e`, `QS-{runId}-B`, `QS-{runId}-h`, `QS-{runId}-a`, `QS-{runId}-c`
67. Klik header kolom Modified By (klik kedua)
68. Verifikasi pada urutan menurun menurut Modified By, entri milik Admin C (`QS-{runId}-g`) tampil sebelum entri milik Admin B (`QS-{runId}-i`)
69. Verifikasi delapan entri milik aktor M tetap berurutan Newest First di dalam satu blok: `QS-{runId}-f`, `QS-{runId}-D`, `QS-{runId}-j`, `QS-{runId}-e`, `QS-{runId}-B`, `QS-{runId}-h`, `QS-{runId}-a`, `QS-{runId}-c`
70. Klik header kolom Modified By (klik ketiga)
71. Verifikasi urutan entri kembali ke urutan default Newest First: `QS-{runId}-g`, `QS-{runId}-i`, `QS-{runId}-f`, `QS-{runId}-D`, `QS-{runId}-j`, `QS-{runId}-e`, `QS-{runId}-B`, `QS-{runId}-h`, `QS-{runId}-a`, `QS-{runId}-c`
