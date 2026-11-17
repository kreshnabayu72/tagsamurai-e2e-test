---
id: TC-FA-MYASSET-E2E-033-tab-borrowed-filter-dep-borrow
title: "Filter tab Borrowed: opsi DISTINCT, opsi Status berkombinasi badge, dan kombinasi dengan Search"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["§4.1b#r7", "EB-FLT-1@tabel-borrowed", "EB-FLT-4@tabel-borrowed", "EB-FLT-3"]
smoke: ["EB-FLT-3"]
dependsOn: ["Transactions > Borrow: pinjaman, approval, sesi Handover, Extension, dan Return oleh Aktor Borrow"]
trace:
  "§4.1b#r7": [4, 15, 16, 21, 111, 112]
  "EB-FLT-1@tabel-borrowed": [4, 5, 8, 9, 103]
  "EB-FLT-4@tabel-borrowed": [42, 43, 45, 53, 56, 62, 65, 100]
  "EB-FLT-3": [21, 32, 33, 70, 75, 76, 81, 88]
anchor: [1, 24, 95, 99]
coverage:
  web: automated
---

# Filter tab Borrowed: opsi DISTINCT, opsi Status berkombinasi badge, dan kombinasi dengan Search

## Prerequisites
- Aktor: Borrower `Eka Prasetya {runId}`, pengguna karyawan ber-akun login tanpa role admin. Aktor Borrow `Rina Wulandari {runId}` hanya memicu satu pinjaman baru di akhir spec.
- Layar awal: halaman My Asset, tab `Borrowed`.
- Data:
  - DU-033-1: User `Eka Prasetya {runId}`, tanpa role admin, cakupan Group `Head Office`.
  - DU-033-2: User `Rina Wulandari {runId}`, role Asset Admin dengan hak Aktor Borrow, cakupan Group `Head Office`.
  - DU-033-3: Brand `Logitech` ada di sistem dan tidak dipakai aset mana pun di tabel Borrowed `Eka Prasetya {runId}`.
  - DU-033-4: pinjaman Admin atas nama `Eka Prasetya {runId}`, aset `Printer Canon G3010 {runId}`, Brand `Canon`, Model/Type `G3010`, Category `Elektronik`, Status `Borrowed`, Duration `1 day`, Handed Over At `T0`, Due Date `T0 + 1 hari`.
  - DU-033-5: pinjaman Admin atas nama `Eka Prasetya {runId}`, aset `Laptop Dell Latitude 5420 {runId}`, Brand `Dell`, Model/Type `Latitude 5420`, Category `Elektronik`, Status `Borrowed`, Duration `3 days`, Handed Over At `T0`, Due Date `T0 + 3 hari`.
  - DU-033-6: pinjaman Admin atas nama `Eka Prasetya {runId}`, aset `Kamera Canon EOS 90D {runId}`, Brand `Canon`, Model/Type `EOS 90D`, Category `Elektronik`, Status `Overdue`, Duration `5 days`, Handed Over At `T0 − 7 hari`, Due Date `T0 − 2 hari`.
  - DU-033-7: pinjaman Admin atas nama `Eka Prasetya {runId}`, aset `Monitor Dell 24 inci {runId}`, Brand `Dell`, Model/Type `U2422H`, Category `Elektronik`, Status `Overdue`, Duration `6 days`, Handed Over At `T0 − 10 hari`, Due Date `T0 − 4 hari`.
  - DU-033-8: pinjaman Admin atas nama `Eka Prasetya {runId}`, aset `Proyektor Epson EB-X06 {runId}`, Brand `Epson`, Model/Type `EB-X06`, Category `Elektronik`, Status `Waiting for Handover`, Duration `2 days`, Due Date `—`.
  - DU-033-9: pinjaman Admin atas nama `Eka Prasetya {runId}`, aset `Meja Rapat Kayu {runId}`, Brand `Informa`, Model/Type `Meja Rapat`, Category `Furnitur`, Status `Waiting for Approval`, Duration `4 days`, Due Date `—`.
  - DU-033-10: pinjaman Admin atas nama `Eka Prasetya {runId}`, aset `Speaker Konferensi {runId}`, Brand `Dell`, Model/Type `Speaker`, Category `Elektronik`, Status `Borrowed` dengan badge `Reported Damaged`, sehingga opsi Status-nya `Borrowed · Reported Damaged`, Duration `7 days`, Handed Over At `T0 − 1 hari`, Due Date `T0 + 6 hari`.
  - DU-033-11: pinjaman Admin atas nama `Eka Prasetya {runId}`, aset `Webcam Logitech C920 {runId}`, Brand `Logitech`, dibuat Aktor Borrow `Rina Wulandari {runId}` pada langkah spec.
  - DU-033-14: pinjaman Admin atas nama `Eka Prasetya {runId}`, aset `Docking Station Dell WD19 {runId}`, Brand `Dell`, Model/Type `WD19`, Category `Elektronik`, Status `Borrowed` dengan badge `Damaged` dan `Reported Missing`, sehingga opsi Status-nya `Borrowed · Damaged · Reported Missing`, Duration `7 days`, Handed Over At `T0 − 2 hari`, Due Date `T0 + 5 hari`.
  - Kata kunci Search: DU-033-12 `Overdue`, DU-033-13 `Borrowed`.
- Kondisi:
  - Tab Borrowed `Eka Prasetya {runId}` berisi 8 baris aset, dari DU-033-4 sampai DU-033-10 dan DU-033-14, sebelum DU-033-11 dibuat.
  - Kolom `Category` tidak tampil pada tabel Borrowed (kolom tambahan, tersembunyi pada konfigurasi bawaan).
  - Tidak ada Search, Filter, dan Sort aktif pada tabel Borrowed.

## Test Steps

### Opsi Filter berisi nilai DISTINCT dari tabel
1. Verifikasi tabel Borrowed memuat 8 baris aset milik `Eka Prasetya {runId}`
2. Klik ikon `Filter` pada toolbar
3. Klik field `Status`
4. Verifikasi opsi field `Status` berisi `Borrowed`, `Borrowed · Damaged · Reported Missing`, `Borrowed · Reported Damaged`, `Overdue`, `Waiting for Approval`, dan `Waiting for Handover`
5. Verifikasi opsi `Extension Request` dan `Extension Approval` tidak tampil di field `Status` karena tidak ada baris bernilai itu
6. Tekan `Esc` untuk menutup daftar opsi
7. Klik field `Brand`
8. Verifikasi opsi field `Brand` berisi `Canon`, `Dell`, `Epson`, dan `Informa`
9. Verifikasi opsi `Logitech` tidak tampil di field `Brand` karena tidak dipakai baris mana pun
10. Tekan `Esc` untuk menutup daftar opsi

### Hasil filter Status cocok hanya dengan opsi yang sama persis dan OR dalam satu field
11. Klik field `Status`
12. Centang opsi `Borrowed`
13. Tekan `Esc` untuk menutup daftar opsi
14. Klik `[Apply]`
15. Verifikasi tabel memuat tepat dua baris, yaitu `Printer Canon G3010 {runId}` dan `Laptop Dell Latitude 5420 {runId}`
16. Verifikasi baris `Speaker Konferensi {runId}` tidak tampil karena Status-nya `Borrowed · Reported Damaged` bukan opsi `Borrowed`
17. Klik field `Status`
18. Centang opsi `Borrowed · Reported Damaged`
19. Tekan `Esc` untuk menutup daftar opsi
20. Klik `[Apply]`
21. Verifikasi tabel memuat tepat tiga baris, yaitu `Printer Canon G3010 {runId}`, `Laptop Dell Latitude 5420 {runId}`, dan `Speaker Konferensi {runId}`, tanpa baris Overdue

### AND antar field
22. Klik `[Clear Field]`
23. Klik `[Apply]`
24. Verifikasi tabel Borrowed memuat 8 baris setelah saringan dilepas
25. Klik field `Status`
26. Centang opsi `Borrowed`
27. Tekan `Esc` untuk menutup daftar opsi
28. Klik field `Brand`
29. Centang opsi `Canon`
30. Tekan `Esc` untuk menutup daftar opsi
31. Klik `[Apply]`
32. Verifikasi tabel hanya memuat baris `Printer Canon G3010 {runId}` yang memenuhi Status `Borrowed` dan Brand `Canon`
33. Verifikasi baris `Laptop Dell Latitude 5420 {runId}` (Brand `Dell`), `Kamera Canon EOS 90D {runId}` (Status `Overdue`), dan `Monitor Dell 24 inci {runId}` (Status `Overdue`, Brand `Dell`) tidak tampil

### Filter lalu Search menghasilkan irisan dan Clear Search mempertahankan Filter dan Sort
34. Klik `[Clear Field]`
35. Klik `[Apply]`
36. Klik header kolom Duration
37. Klik field `Brand`
38. Centang opsi `Canon`
39. Tekan `Esc` untuk menutup daftar opsi
40. Klik `[Apply]`
41. Ketik Search `Overdue`, tekan Enter
42. Verifikasi tabel hanya memuat baris `Kamera Canon EOS 90D {runId}` yang cocok dengan Filter dan Search sekaligus
43. Verifikasi baris `Printer Canon G3010 {runId}` (cocok Filter saja) dan `Monitor Dell 24 inci {runId}` (cocok Search saja) tidak tampil
44. Klik `(←)` pada kotak Search
45. Verifikasi baris `Printer Canon G3010 {runId}` lalu `Kamera Canon EOS 90D {runId}` tampil dari atas ke bawah menurut Shortest First dengan Filter Brand `Canon` tetap aktif

### Search lalu Filter menghasilkan irisan yang sama dan Clear Filter mempertahankan Search dan Sort
46. Klik `[Clear Field]`
47. Klik `[Apply]`
48. Ketik Search `Overdue`, tekan Enter
49. Klik field `Brand`
50. Centang opsi `Canon`
51. Tekan `Esc` untuk menutup daftar opsi
52. Klik `[Apply]`
53. Verifikasi tabel hanya memuat baris `Kamera Canon EOS 90D {runId}`, irisan yang sama seperti saat Filter diterapkan lebih dulu
54. Klik `[Clear Field]`
55. Klik `[Apply]`
56. Verifikasi baris `Kamera Canon EOS 90D {runId}` lalu `Monitor Dell 24 inci {runId}` tampil dari atas ke bawah menurut Shortest First dengan Search `Overdue` tetap aktif

### Irisan kosong dipulihkan dengan melepas satu saringan
57. Ganti isi kotak search dengan `Borrowed`, tekan Enter
58. Klik field `Brand`
59. Centang opsi `Epson`
60. Tekan `Esc` untuk menutup daftar opsi
61. Klik `[Apply]`
62. Verifikasi empty state `No results found` tampil karena irisan Search `Borrowed` dan Brand `Epson` kosong
63. Klik `[Clear Field]`
64. Klik `[Apply]`
65. Verifikasi baris `Printer Canon G3010 {runId}`, `Laptop Dell Latitude 5420 {runId}`, dan `Speaker Konferensi {runId}` tampil kembali setelah Filter dilepas

### Filter rentang tanggal Due Date
66. Klik `(←)` pada kotak Search
67. Klik field `Due Date`
68. Pilih rentang dari `T0 − 4 hari` sampai `T0 − 2 hari`
69. Klik `[Apply]`
70. Verifikasi tabel hanya memuat baris `Monitor Dell 24 inci {runId}` dengan Due Date tepat di tanggal awal dan baris `Kamera Canon EOS 90D {runId}` dengan Due Date tepat di tanggal akhir
71. Klik `[Clear Field]`
72. Klik field `Due Date`
73. Pilih rentang dari `T0` sampai `T0 + 2 hari`
74. Klik `[Apply]`
75. Verifikasi tabel hanya memuat baris `Printer Canon G3010 {runId}` dengan Due Date `T0 + 1 hari` di dalam rentang
76. Verifikasi baris `Laptop Dell Latitude 5420 {runId}` dengan Due Date `T0 + 3 hari` di luar rentang tidak tampil
77. Klik `[Clear Field]`
78. Klik field `Due Date`
79. Pilih rentang satu hari dengan tanggal awal dan tanggal akhir `T0 + 3 hari`
80. Klik `[Apply]`
81. Verifikasi tabel hanya memuat baris `Laptop Dell Latitude 5420 {runId}` yang Due Date-nya jatuh pada rentang satu hari itu
82. Klik `[Clear Field]`
83. Klik `[Apply]`

### Filter pada kolom Category yang tersembunyi
84. Klik field `Category`
85. Centang opsi `Furnitur`
86. Tekan `Esc` untuk menutup daftar opsi
87. Klik `[Apply]`
88. Verifikasi tabel hanya memuat baris `Meja Rapat Kayu {runId}` walau kolom `Category` tidak tampil
89. Klik `[Clear Field]`
90. Klik `[Apply]`

### Record yang diubah tidak lagi cocok dan record baru menjadi opsi
91. Klik field `Status`
92. Centang opsi `Waiting for Handover`
93. Tekan `Esc` untuk menutup daftar opsi
94. Klik `[Apply]`
95. Verifikasi tabel hanya memuat baris `Proyektor Epson EB-X06 {runId}`
96. Klik `⋯` pada baris `Proyektor Epson EB-X06 {runId}`
97. Klik `Cancel Borrow`
98. Klik `[Cancel Borrow]` pada dialog `Cancel Borrow`
99. Verifikasi toast `Success, borrow has been canceled.` tampil
100. Verifikasi empty state `No results found` tampil dan baris `Proyektor Epson EB-X06 {runId}` tidak tampil karena sudah tidak cocok dengan Status `Waiting for Handover`
101. Aktor Borrow `Rina Wulandari {runId}` membuat pinjaman atas nama `Eka Prasetya {runId}` untuk aset `Webcam Logitech C920 {runId}` ber-Brand `Logitech`
102. Klik field `Brand`
103. Verifikasi opsi `Logitech` tampil di field `Brand` tanpa memuat ulang halaman

### Opsi Status dengan dua badge tambahan cocok hanya dengan opsi yang sama persis
104. Tekan `Esc` untuk menutup daftar opsi
105. Klik `[Clear Field]`
106. Klik `[Apply]`
107. Klik field `Status`
108. Centang opsi `Borrowed · Damaged · Reported Missing`
109. Tekan `Esc` untuk menutup daftar opsi
110. Klik `[Apply]`
111. Verifikasi tabel memuat baris `Docking Station Dell WD19 {runId}` yang Status-nya `Borrowed · Damaged · Reported Missing`
112. Verifikasi baris `Speaker Konferensi {runId}` (Status `Borrowed · Reported Damaged`) tidak tampil karena bukan opsi yang sama persis
