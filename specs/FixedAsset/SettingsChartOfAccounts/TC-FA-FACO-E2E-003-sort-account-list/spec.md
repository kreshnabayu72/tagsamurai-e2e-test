---
id: TC-FA-FACO-E2E-003-sort-account-list
title: "Sort Account List mengurutkan baris per kolom dan kembali ke urutan default"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["§4.1.1#r1", "§4.1.1#r2", "§4.1.1#r3", "§4.1.1#r4", "§4.1.1#r7", "§4.1.1#r8", "§5#b5", "§9.5#r1", "EB-SRT-3@tabel-account-list", "EB-SRT-1"]
smoke: ["EB-SRT-1"]
dependsOn: []
trace:
  "§4.1.1#r1": [23, 25]
  "§4.1.1#r2": [4, 6]
  "§4.1.1#r3": [10, 12]
  "§4.1.1#r4": [14, 16]
  "§4.1.1#r7": [31, 33, 59, 60, 62, 68, 69, 70, 72]
  "§4.1.1#r8": [35, 37, 44, 47]
  "§5#b5": [2, 39, 53]
  "§9.5#r1": [2, 12, 33]
  "EB-SRT-3@tabel-account-list": [8, 18, 21]
  "EB-SRT-1": [10, 14, 23, 35]
anchor: [41]
coverage:
  web: automated
---

# Sort Account List mengurutkan baris per kolom dan kembali ke urutan default

## Prerequisites
- Aktor: pengguna Total Control. Aktor lain pemicu: Admin B (DU-003-14), `Sinta Wiratna` (DU-003-15), dan `Sinta Wirawan` (DU-003-16).
- Layar awal: Settings > Accounting > Chart of Accounts.
- Data:
  - DU-003-1: akun `K5-{runId}`, Account Name `Élan SRT {runId}`, Account Function `Loss on Disposal`, Status `Inactive`.
  - DU-003-2: akun `K3-{runId}`, Account Name `anggur SRT {runId}`, Account Function `Accumulated Depreciation`, Status `Active`.
  - DU-003-3: akun `K9-{runId}`, Account Name `3D Printer SRT {runId}`, Account Function `Depreciation Expense`, Status `Active`.
  - DU-003-4: akun `K1-{runId}`, Account Name `Melati SRT {runId}`, Account Function `Asset Cost`, Status `Active`.
  - DU-003-5: akun `K7-{runId}`, Account Name `Ezra SRT {runId}`, Account Function `Disposal Proceeds`, Status `Active`. Account Name sesudah diubah `Sinta Wiratna`: `Ezra Baru SRT {runId}`.
  - DU-003-6: akun `K2-{runId}`, Account Name `Zaitun SRT {runId}`, Account Function `Depreciation Expense`, Status `Inactive`. Account Name sesudah diubah `Sinta Wirawan`: `Zaitun Baru SRT {runId}`.
  - DU-003-7: akun `K8-{runId}`, Account Name `#Gudang SRT {runId}`, Account Function `Asset Cost`, Status `Inactive`.
  - DU-003-8: akun `K4-{runId}`, Account Name `Apel SRT {runId}`, Account Function `Gain on Disposal`, Status `Active`. Account Name sesudah diubah Admin B: `Apel Baru SRT {runId}`.
  - DU-003-9: akun `K6-{runId}`, Account Name `Elan SRT {runId}`, Account Function `Capitalization Offset`, Status `Active`.
  - DU-003-10: akun `KA-{runId}`, Account Name `Melati SRT {runId}`, Account Function `Gain on Disposal`, Status `Active`.
  - DU-003-1 sampai DU-003-10 dibuat berurutan menurut nomornya (DU-003-1 paling dulu), sehingga urutan pembuatannya berbeda dari urutan Account Code.
  - DU-003-11: 12 akun, Account Code `V{n}-{runId}`, Account Name `Kas {n} Volume {runId}`, Account Function `Asset Cost`, Status `Active`, untuk n 1 sampai 12. Dibuat berurutan menurut n sesudah DU-003-10.
  - Seluruh baris DU-003-1 sampai DU-003-10 tanpa entri Changelog sama sekali (belum pernah diubah oleh siapa pun), sehingga Modified By-nya `System`, sampai Admin B mengubah DU-003-8 pada kelompok langkah terakhir.
  - DU-003-14: Admin B, nama lengkap `Rani Pratama` (tampil `Rani P` di kolom Modified By), role Total Control, cakupan seluruh client, akun aktif dan kredensialnya disediakan fase 2.
  - DU-003-15: nama lengkap `Sinta Wiratna` (tampil `Sinta W` di kolom Modified By), role Total Control, cakupan seluruh client, akun aktif dan kredensialnya disediakan fase 2.
  - DU-003-16: nama lengkap `Sinta Wirawan` (tampil `Sinta W` di kolom Modified By), role Total Control, cakupan seluruh client, akun aktif dan kredensialnya disediakan fase 2.
- Kondisi:
  - Ukuran halaman tabel adalah 10 baris (nilai bawaan).

## Test Steps

### Urutan default Account Code A-Z
1. Ketik Search `SRT {runId}`, tekan Enter
2. Verifikasi urutan baris dari atas ke bawah menurut Account Code: `K1-{runId}`, `K2-{runId}`, `K3-{runId}`, `K4-{runId}`, `K5-{runId}`, `K6-{runId}`, `K7-{runId}`, `K8-{runId}`, `K9-{runId}`, `KA-{runId}`

### Siklus tiga klik pada Account Code
3. Klik header kolom Account Code (klik pertama)
4. Verifikasi urutan baris menaik menurut Account Code: `K1-{runId}`, `K2-{runId}`, `K3-{runId}`, `K4-{runId}`, `K5-{runId}`, `K6-{runId}`, `K7-{runId}`, `K8-{runId}`, `K9-{runId}`, `KA-{runId}`
5. Klik header kolom Account Code (klik kedua)
6. Verifikasi urutan baris menurun menurut Account Code: `KA-{runId}`, `K9-{runId}`, `K8-{runId}`, `K7-{runId}`, `K6-{runId}`, `K5-{runId}`, `K4-{runId}`, `K3-{runId}`, `K2-{runId}`, `K1-{runId}`
7. Klik header kolom Account Code (klik ketiga)
8. Verifikasi urutan baris kembali ke urutan default: `K1-{runId}`, `K2-{runId}`, `K3-{runId}`, `K4-{runId}`, `K5-{runId}`, `K6-{runId}`, `K7-{runId}`, `K8-{runId}`, `K9-{runId}`, `KA-{runId}`

### Sort Account Name tanpa membedakan huruf besar-kecil dan aksen
9. Klik header kolom Account Name (klik pertama)
10. Verifikasi urutan baris menaik menurut Account Name, ditulis dengan Account Code barisnya: `K8-{runId}`, `K9-{runId}`, `K3-{runId}`, `K4-{runId}`, `K6-{runId}`, `K5-{runId}`, `K7-{runId}`, `K1-{runId}`, `KA-{runId}`, `K2-{runId}`
11. Klik header kolom Account Name (klik kedua)
12. Verifikasi urutan baris menurun menurut Account Name, ditulis dengan Account Code barisnya, dengan dua baris `Melati SRT {runId}` tetap `K1-{runId}` lalu `KA-{runId}`: `K2-{runId}`, `K1-{runId}`, `KA-{runId}`, `K7-{runId}`, `K5-{runId}`, `K6-{runId}`, `K4-{runId}`, `K3-{runId}`, `K9-{runId}`, `K8-{runId}`

### Sort Function menurut label badge
13. Klik header kolom Function (klik pertama)
14. Verifikasi urutan baris menaik menurut label Function, ditulis dengan Account Code barisnya: `K3-{runId}`, `K1-{runId}`, `K8-{runId}`, `K6-{runId}`, `K2-{runId}`, `K9-{runId}`, `K7-{runId}`, `K4-{runId}`, `KA-{runId}`, `K5-{runId}`
15. Klik header kolom Function (klik kedua)
16. Verifikasi urutan baris menurun menurut label Function, ditulis dengan Account Code barisnya: `K5-{runId}`, `K4-{runId}`, `KA-{runId}`, `K7-{runId}`, `K2-{runId}`, `K9-{runId}`, `K6-{runId}`, `K1-{runId}`, `K8-{runId}`, `K3-{runId}`

### Sort pindah ke kolom lain lalu kembali ke default
17. Klik header kolom Account Name (klik pertama pada kolom ini, sementara kolom Function sedang aktif)
18. Verifikasi urutan baris menaik menurut Account Name, bukan menurut Function: `K8-{runId}`, `K9-{runId}`, `K3-{runId}`, `K4-{runId}`, `K6-{runId}`, `K5-{runId}`, `K7-{runId}`, `K1-{runId}`, `KA-{runId}`, `K2-{runId}`
19. Klik header kolom Account Name (klik kedua)
20. Klik header kolom Account Name (klik ketiga)
21. Verifikasi urutan baris kembali ke urutan default: `K1-{runId}`, `K2-{runId}`, `K3-{runId}`, `K4-{runId}`, `K5-{runId}`, `K6-{runId}`, `K7-{runId}`, `K8-{runId}`, `K9-{runId}`, `KA-{runId}`

### Sort kolom Active
22. Klik header kolom Active (klik pertama)
23. Verifikasi urutan baris menaik menurut kolom Active, akun Active lebih dulu, ditulis dengan Account Code barisnya: `K1-{runId}`, `K3-{runId}`, `K4-{runId}`, `K6-{runId}`, `K7-{runId}`, `K9-{runId}`, `KA-{runId}`, `K2-{runId}`, `K5-{runId}`, `K8-{runId}`
24. Klik header kolom Active (klik kedua)
25. Verifikasi urutan baris menurun menurut kolom Active, akun Inactive lebih dulu, ditulis dengan Account Code barisnya: `K2-{runId}`, `K5-{runId}`, `K8-{runId}`, `K1-{runId}`, `K3-{runId}`, `K4-{runId}`, `K6-{runId}`, `K7-{runId}`, `K9-{runId}`, `KA-{runId}`

### Sort Modified By dengan nilai yang sama
26. Klik header kolom Actions `⋯`
27. Centang `Modified By` pada panel Column Visibility
28. Centang `Last Updated` pada panel Column Visibility
29. Klik header kolom Actions `⋯` untuk menutup panel
30. Klik header kolom Modified By (klik pertama)
31. Verifikasi urutan baris menurut Account Code: `K1-{runId}`, `K2-{runId}`, `K3-{runId}`, `K4-{runId}`, `K5-{runId}`, `K6-{runId}`, `K7-{runId}`, `K8-{runId}`, `K9-{runId}`, `KA-{runId}`, karena seluruh baris bernilai Modified By `System` dan urutannya mengikuti default sort
32. Klik header kolom Modified By (klik kedua)
33. Verifikasi urutan baris menurut Account Code tetap `K1-{runId}`, `K2-{runId}`, `K3-{runId}`, `K4-{runId}`, `K5-{runId}`, `K6-{runId}`, `K7-{runId}`, `K8-{runId}`, `K9-{runId}`, `KA-{runId}`, karena nilai Modified By yang sama tidak membalik urutan default sort

### Sort Last Updated menurut urutan pembuatan data
34. Klik header kolom Last Updated (klik pertama)
35. Verifikasi urutan baris dari yang terlama diperbarui, ditulis dengan Account Code barisnya: `K5-{runId}`, `K3-{runId}`, `K9-{runId}`, `K1-{runId}`, `K7-{runId}`, `K2-{runId}`, `K8-{runId}`, `K4-{runId}`, `K6-{runId}`, `KA-{runId}`
36. Klik header kolom Last Updated (klik kedua)
37. Verifikasi urutan baris dari yang terbaru diperbarui, ditulis dengan Account Code barisnya: `KA-{runId}`, `K6-{runId}`, `K4-{runId}`, `K8-{runId}`, `K2-{runId}`, `K7-{runId}`, `K1-{runId}`, `K9-{runId}`, `K3-{runId}`, `K5-{runId}`
38. Klik header kolom Last Updated (klik ketiga)
39. Verifikasi urutan baris kembali ke urutan default menurut Account Code, bukan urutan pembuatan data: `K1-{runId}`, `K2-{runId}`, `K3-{runId}`, `K4-{runId}`, `K5-{runId}`, `K6-{runId}`, `K7-{runId}`, `K8-{runId}`, `K9-{runId}`, `KA-{runId}`

### Sort melintasi halaman
40. Ganti isi kotak Search dengan `Volume {runId}`, tekan Enter
41. Verifikasi hasil Search memuat 12 baris: 10 baris di halaman 1 dan 2 baris di halaman 2
42. Klik header kolom Last Updated (klik pertama)
43. Klik halaman 2 pada Paginator
44. Verifikasi halaman 2 memuat `V11-{runId}` dan `V12-{runId}`
45. Klik header kolom Last Updated (klik kedua)
46. Klik halaman 2 pada Paginator
47. Verifikasi halaman 2 memuat `V1-{runId}` dan `V2-{runId}`
48. Klik header kolom Last Updated (klik ketiga)

### Nilai sort yang sama melintasi halaman
49. Klik header kolom Function (klik pertama)
50. Klik halaman 1 pada Paginator
51. Catat 10 Account Code yang tampil di halaman 1
52. Klik halaman 2 pada Paginator
53. Verifikasi 2 baris di halaman 2 adalah Account Code dari `V1-{runId}` sampai `V12-{runId}` yang belum tampil di halaman 1, sehingga setiap Account Code tampil tepat satu kali

### Sort Modified By dengan dua nilai berbeda menurut nama lengkap
54. Klik header kolom Function (klik kedua)
55. Klik header kolom Function (klik ketiga)
56. Ganti isi kotak Search dengan `SRT {runId}`, tekan Enter
57. Admin B mengubah Account Name `K4-{runId}` menjadi `Apel Baru SRT {runId}`
58. Klik header kolom Modified By (klik pertama)
59. Verifikasi Modified By baris `K4-{runId}` bernilai `Rani P`, nama depan Admin B diikuti inisial nama belakangnya
60. Verifikasi urutan baris menaik menurut Modified By, `Rani Pratama` sebelum `System`, dan baris bernilai `System` mengikuti default sort: `K4-{runId}`, `K1-{runId}`, `K2-{runId}`, `K3-{runId}`, `K5-{runId}`, `K6-{runId}`, `K7-{runId}`, `K8-{runId}`, `K9-{runId}`, `KA-{runId}`
61. Klik header kolom Modified By (klik kedua)
62. Verifikasi urutan baris menurun menurut Modified By, baris bernilai `System` lebih dulu menurut default sort dan `K4-{runId}` terakhir: `K1-{runId}`, `K2-{runId}`, `K3-{runId}`, `K5-{runId}`, `K6-{runId}`, `K7-{runId}`, `K8-{runId}`, `K9-{runId}`, `KA-{runId}`, `K4-{runId}`
63. Klik header kolom Modified By (klik ketiga)

### Sort Modified By dengan nama tampil sama menurut nama lengkap
64. `Sinta Wiratna` mengubah Account Name `K7-{runId}` menjadi `Ezra Baru SRT {runId}`
65. `Sinta Wirawan` mengubah Account Name `K2-{runId}` menjadi `Zaitun Baru SRT {runId}`
66. Ganti isi kotak Search dengan `SRT {runId}`, tekan Enter
67. Klik header kolom Modified By (klik pertama)
68. Verifikasi Modified By baris `K7-{runId}` bernilai `Sinta W`, nama depan `Sinta Wiratna` diikuti inisial nama belakangnya
69. Verifikasi Modified By baris `K2-{runId}` bernilai `Sinta W`, nama depan `Sinta Wirawan` diikuti inisial nama belakangnya
70. Verifikasi urutan baris menaik menurut Modified By dengan nama lengkap sebagai kunci, bukan nama tampil: `Rani Pratama`, `Sinta Wiratna`, `Sinta Wirawan`, lalu `System` dengan baris `System` mengikuti default sort: `K4-{runId}`, `K7-{runId}`, `K2-{runId}`, `K1-{runId}`, `K3-{runId}`, `K5-{runId}`, `K6-{runId}`, `K8-{runId}`, `K9-{runId}`, `KA-{runId}`
71. Klik header kolom Modified By (klik kedua)
72. Verifikasi urutan baris menurun menurut Modified By dengan nama lengkap sebagai kunci, bukan nama tampil: baris `System` lebih dulu menurut default sort, lalu `Sinta Wirawan`, `Sinta Wiratna`, dan `Rani Pratama` terakhir: `K1-{runId}`, `K3-{runId}`, `K5-{runId}`, `K6-{runId}`, `K8-{runId}`, `K9-{runId}`, `KA-{runId}`, `K2-{runId}`, `K7-{runId}`, `K4-{runId}`
73. Klik header kolom Modified By (klik ketiga)
