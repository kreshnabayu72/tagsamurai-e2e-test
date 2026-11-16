---
id: TC-FA-FACO-UI-130-guided-tooltip
title: "Guided Tooltip Chart of Accounts: konten step, navigasi, dan replay"
layer: ui-client
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["§4.7#r1", "§4.7#r2", "§4.7#r3", "§4.7#r4", "§4.7#r5", "§4.7#r6", "EB-TBL-10"]
smoke: []
dependsOn: []
trace:
  "§4.7#r1": [4, 5, 6, 44, 63, 72]
  "§4.7#r2": [12, 13, 14, 42, 61, 65]
  "§4.7#r3": [18, 19, 20]
  "§4.7#r4": [23, 24, 25]
  "§4.7#r5": [28, 29, 30]
  "§4.7#r6": [33, 34, 35]
  "EB-TBL-10": [2, 3, 7, 8, 11, 15, 17, 22, 27, 32, 36, 40, 42, 44, 45, 48, 50, 52, 54, 56, 58, 61, 63, 65, 67, 69, 71, 74, 76, 78, 80]
anchor: []
coverage:
  web: automated
---

# Guided Tooltip Chart of Accounts: konten step, navigasi, dan replay

## Prerequisites
- Aktor: Total Control.
- Layar awal: Settings > Accounting > Chart of Accounts.
- Komponen: Guided Tooltip
- Data:
  - DU-130-1: Account `1-1001`, Name `Fixed Assets – Equipment`, Function `Asset Cost`, status Active, Used By `3`, Last Used in Journal `Oct 2026`.
  - DU-130-2: ukuran jendela browser `1024 x 768` piksel.
- Kondisi:
  - K1: tampilan desktop; tabel berisi DU-130-1; aktor belum pernah melihat Guided Tooltip halaman ini (flag seen belum ada).
  - K2: tampilan desktop; tabel berisi DU-130-1; aktor sudah menyelesaikan Guided Tooltip halaman ini (flag seen sudah ada).

## Test Steps

### Tur otomatis pada kunjungan pertama dan konten Step 1
1. Tampilkan Tab Chart of Accounts dengan kondisi K1
2. Verifikasi Guided Tooltip tampil pada Step 1
3. Verifikasi indikator `Step [N] of [Total]` dengan N `1` dan Total `6` tampil
4. Verifikasi judul `Account Code` tampil
5. Verifikasi deskripsi `Use the same code as in your accounting application so exported journals can be imported directly.` tampil
6. Verifikasi header kolom `Account Code` tersorot
7. Verifikasi tombol `[Skip]` dan `[Next]` tampil
8. Verifikasi tombol `[Back]` tidak tampil

### Konten Step 2 sampai Step 6
9. Tampilkan Tab Chart of Accounts dengan kondisi K1
10. Klik `[Next]`
11. Verifikasi indikator `Step [N] of [Total]` dengan N `2` dan Total `6` tampil
12. Verifikasi judul `Account Function` tampil
13. Verifikasi deskripsi `Each account has one function that decides which journal line it is used for.` tampil
14. Verifikasi header kolom `Function` tersorot
15. Verifikasi tombol `[Back]` tampil
16. Klik `[Next]`
17. Verifikasi indikator `Step [N] of [Total]` dengan N `3` dan Total `6` tampil
18. Verifikasi judul `Where an Account Is Used` tampil
19. Verifikasi deskripsi `Shows how many Asset Classes use the account. Accounts that are still in use cannot be deactivated or deleted.` tampil
20. Verifikasi header kolom `Used By` tersorot
21. Klik `[Next]`
22. Verifikasi indikator `Step [N] of [Total]` dengan N `4` dan Total `6` tampil
23. Verifikasi judul `Last Used in Journal` tampil
24. Verifikasi deskripsi `Shows the latest journal period in which the account was exported. Exported accounts cannot be deleted.` tampil
25. Verifikasi header kolom `Last Used in Journal` tersorot
26. Klik `[Next]`
27. Verifikasi indikator `Step [N] of [Total]` dengan N `5` dan Total `6` tampil
28. Verifikasi judul `Filter Accounts` tampil
29. Verifikasi deskripsi `Narrow down the list. Filters combine with your search.` tampil
30. Verifikasi ikon Filter pada toolbar tersorot
31. Klik `[Next]`
32. Verifikasi indikator `Step [N] of [Total]` dengan N `6` dan Total `6` tampil
33. Verifikasi judul `Changelog` tampil
34. Verifikasi deskripsi `See the history of changes made to accounts.` tampil
35. Verifikasi ikon Changelog pada toolbar tersorot
36. Verifikasi tombol `[Done]` tampil sebagai pengganti `[Next]`

### Back kembali ke step sebelumnya
37. Tampilkan Tab Chart of Accounts dengan kondisi K1
38. Klik `[Next]`
39. Klik `[Next]`
40. Verifikasi judul `Where an Account Is Used` tampil
41. Klik `[Back]`
42. Verifikasi judul `Account Function` tampil
43. Klik `[Back]`
44. Verifikasi judul `Account Code` tampil
45. Verifikasi tombol `[Back]` tidak tampil

### Done menutup tur
46. Tampilkan Tab Chart of Accounts dengan kondisi K1
47. Klik `[Next]` lima kali
48. Verifikasi tombol `[Done]` tampil
49. Klik `[Done]`
50. Verifikasi Guided Tooltip tidak tampil

### Skip dan klik overlay menutup tur
51. Tampilkan Tab Chart of Accounts dengan kondisi K1
52. Verifikasi Guided Tooltip tampil pada Step 1
53. Klik `[Skip]`
54. Verifikasi Guided Tooltip tidak tampil
55. Klik `[?]`
56. Verifikasi Guided Tooltip tampil pada Step 1
57. Klik overlay gelap di luar area sorot
58. Verifikasi Guided Tooltip tidak tampil

### Navigasi keyboard
59. Tampilkan Tab Chart of Accounts dengan kondisi K1
60. Tekan `→`
61. Verifikasi judul `Account Function` tampil
62. Tekan `←`
63. Verifikasi judul `Account Code` tampil
64. Tekan Enter
65. Verifikasi judul `Account Function` tampil
66. Tekan `Esc`
67. Verifikasi Guided Tooltip tidak tampil

### Replay lewat tombol [?]
68. Tampilkan Tab Chart of Accounts dengan kondisi K2
69. Verifikasi tombol `[?]` tampil di sebelah kanan Breadcrumb
70. Klik `[?]`
71. Verifikasi Guided Tooltip tampil pada Step 1
72. Verifikasi judul `Account Code` tampil
73. Klik `[Next]`
74. Verifikasi judul `Account Function` tampil
75. Klik `[Skip]`
76. Verifikasi Guided Tooltip tidak tampil

### Mengubah ukuran jendela menutup tur tanpa menandai seen
77. Tampilkan Tab Chart of Accounts dengan kondisi K1
78. Verifikasi Guided Tooltip tampil pada Step 1
79. Ubah ukuran jendela browser menjadi `1024 x 768` piksel
80. Verifikasi Guided Tooltip tidak tampil
