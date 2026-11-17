---
id: TC-FA-MYASSET-E2E-040-pic-borrower-baris-dan-aksi-dep-users
title: "PIC Borrower: baris Borrower tanpa akun, aksi atas nama, dan Confirm Handover dengan pernyataan PIC"
layer: ui-e2e
priority: Critical
caseType: Positive
status: draft
sourceRules: ["FI-20", "FI-21", "§1.2#r14", "§1.2#r24", "§1.2#r36", "§1.2#r37", "§1.2#r41", "§1.2#r42", "§2.1#r1", "§2.1#r2", "§2.1#r3", "§2.1#r4", "§2.1#r5", "§2.1#r6", "§2.1#r7", "§2.1#r8", "§2.1#r9", "§2.1#r10", "§2.1#r12", "§2.1#r13", "§4.1b#r12", "§4.1b#r31", "§4.1b#p6", "§4.2.3#p1", "§4.2.5#p4", "§Dialog aksi baris (tab Borrowed dan Assigned)#r7", "§4.8#r1", "§4.8#r2", "§4.8#r3", "§4.8#r4", "§4.8#r5", "§4.8#r6", "§4.8#r7", "§4.8#r8", "§4.8#r9", "§4.8#r11", "§4.8#r12", "§4.8#r13", "§4.8#r14", "§9.2#b7"]
smoke: []
dependsOn: ["Users: Borrower tanpa akun beserta PIC-nya, dan User Detail > User Log", "Transactions > Borrow: pinjaman, approval, sesi Handover, Extension, dan Return oleh Aktor Borrow"]
trace:
  "FI-20": [17, 18]
  "FI-21": [20, 21, 22, 25, 27, 28, 29]
  "§1.2#r14": 4
  "§1.2#r24": 4
  "§1.2#r36": [4, 66]
  "§1.2#r37": [6, 67]
  "§1.2#r41": [33, 34, 35, 40, 43, 46, 49, 52, 70]
  "§1.2#r42": 72
  "§2.1#r1": [2, 5]
  "§2.1#r2": 13
  "§2.1#r3": [70, 75, 76, 78]
  "§2.1#r4": 43
  "§2.1#r5": [33, 46]
  "§2.1#r6": 40
  "§2.1#r7": 34
  "§2.1#r8": 35
  "§2.1#r9": [49, 52]
  "§2.1#r10": 36
  "§2.1#r12": 32
  "§2.1#r13": 37
  "§4.1b#r12": [6, 7, 9]
  "§4.1b#r31": 40
  "§4.1b#p6": [18, 20, 27]
  "§4.2.3#p1": [56, 57, 58, 60, 61, 62]
  "§4.2.5#p4": [72, 81]
  "§Dialog aksi baris (tab Borrowed dan Assigned)#r7": 81
  "§4.8#r1": 2
  "§4.8#r2": 70
  "§4.8#r3": 70
  "§4.8#r4": 13
  "§4.8#r5": 36
  "§4.8#r6": 43
  "§4.8#r7": [33, 46]
  "§4.8#r8": 34
  "§4.8#r9": 35
  "§4.8#r11": 40
  "§4.8#r12": [49, 52]
  "§4.8#r13": 32
  "§4.8#r14": 37
  "§9.2#b7": [60, 61, 62]
anchor: [11]
coverage:
  web: automated
---

# PIC Borrower: baris Borrower tanpa akun, aksi atas nama, dan Confirm Handover dengan pernyataan PIC

## Prerequisites
- Aktor: PIC Borrower `Taufik Hidayat {runId}` (DU-040-1), pengguna yang menjadi PIC dua Borrower tanpa akun.
- Layar awal: halaman Fixed Asset yang menampilkan navbar.
- Data:
  - DU-040-1: pengguna `Taufik Hidayat {runId}`, role `Read Only`, Group `Head Office`.
  - DU-040-2: Borrower tanpa akun `Hendra Kusuma`, PIC `Taufik Hidayat {runId}`. Nama tampil `Hendra K`, dari Full Name `Hendra Kusuma`. Hover kolom `Borrower` yang diharapkan `Hendra Kusuma · PIC: Taufik Hidayat {runId}`, dari Full Name dan User Name PIC.
  - DU-040-3: Borrower tanpa akun `Maya Putri`, PIC `Taufik Hidayat {runId}`.
  - DU-040-4: pinjaman aset `Laptop Lenovo E14 {runId}`, Group `Head Office`, Status `Borrowed`, Source `Admin`, Borrower `Hendra Kusuma`.
  - DU-040-5: pinjaman aset `Proyektor Epson X06 {runId}`, Group `Head Office`, Status `Borrowed`, Source `Self-service`, Borrower `Hendra Kusuma`.
  - DU-040-6: pinjaman aset `Kamera Canon M50 {runId}`, Group `Head Office`, Status `Waiting for Approval`, Source `Admin`, Borrower `Hendra Kusuma`.
  - DU-040-7: pinjaman aset `Tablet Samsung A9 {runId}`, Group `Head Office`, Status `Extension Request`, Source `Admin`, Borrower `Hendra Kusuma`. Pengajuan Extend diajukan PIC dan menunggu review Aktor Borrow.
  - DU-040-8: pinjaman aset `Mikrofon Shure SM58 {runId}`, Group `Head Office`, Status `Borrowed`, badge `Reported Damaged`, Source `Admin`, Borrower `Hendra Kusuma`. Damage Report diajukan PIC dan berstatus `Waiting for Confirmation`.
  - DU-040-9: pinjaman aset `Tripod Manfrotto 055 {runId}`, Group `Head Office`, Status `Borrowed`, badge `Reported Missing`, Source `Admin`, Borrower `Hendra Kusuma`. Laporan Missing diajukan PIC dan berstatus `Waiting for Confirmation`.
  - DU-040-10: pinjaman aset `Monitor Dell P2422H {runId}`, Group `Head Office`, Status `Borrowed`, Source `Admin`, Borrower `Me`.
  - DU-040-11: pinjaman aset `Router Mikrotik hAP {runId}`, Group `Head Office`, Status `Borrowed`, Source `Admin`, Borrower `Maya Putri`.
  - DU-040-12: pinjaman aset `Scanner Epson V39 {runId}`, Group `Head Office`, Status `Waiting for Handover`, Source `Admin`, Borrower `Hendra Kusuma`. Task `Confirm Handover` dengan Total Asset `1`.
  - DU-040-13: pinjaman aset `Printer Canon G3010 {runId}`, Group `Head Office`, Status `Returned`, Source `Admin`, Borrower `Hendra Kusuma`.
  - Label tombol saat seluruh baris yang dapat dipilih sudah terpilih `Unselect All (4 records)`, dari `Unselect All ([N] records)` dengan N `4`.
  - Pernyataan PIC yang diharapkan `I confirm that Hendra Kusuma has received the checked assets.`, dari template PRD dengan Borrower `Hendra Kusuma`.
- Kondisi:
  - Tab Borrowed aktor memuat 9 baris, yaitu DU-040-4 sampai DU-040-12. Tab History memuat 1 baris, yaitu DU-040-13. Tab Task memuat 1 baris, yaitu DU-040-12.
  - Baris Borrower `Hendra Kusuma` yang dapat dipilih untuk bulk Request Extension ada `4`: DU-040-4, DU-040-5, DU-040-8, dan DU-040-9.
  - Sesi Handover DU-040-12 menunggu konfirmasi dan jendela konfirmasinya belum habis.

## Test Steps

### Menu My Asset dan keempat tab tersedia bagi PIC Borrower
1. Buka `My Asset` dari menu profil pada navbar
2. Verifikasi tab `Task`, `Borrowed`, `Assigned`, dan `History` tampil

### Baris Borrower tanpa akun tampil di tab Borrowed dengan kolom Borrower
3. Klik tab `Borrowed`
4. Verifikasi baris `Laptop Lenovo E14 {runId}` milik Borrower tanpa akun `Hendra Kusuma` tampil
5. Verifikasi baris `Monitor Dell P2422H {runId}` milik aktor sendiri tampil
6. Verifikasi kolom `Borrower` pada baris `Laptop Lenovo E14 {runId}` berisi `Hendra K`
7. Verifikasi kolom `Borrower` pada baris `Monitor Dell P2422H {runId}` berisi `Me`
8. Arahkan kursor ke kolom `Borrower` pada baris `Laptop Lenovo E14 {runId}`
9. Verifikasi hover kolom `Borrower` memuat `Hendra Kusuma · PIC: Taufik Hidayat {runId}`

### Tab Task memuat Task Borrow dan tidak memuat Task Assignment
10. Klik tab `Task`
11. Verifikasi baris Task `Confirm Handover` untuk pinjaman DU-040-12 tampil dengan Total Asset `1`
12. Ketik Search `ASG`, tekan Enter
13. Verifikasi empty state `No results found` tampil karena tidak ada baris Task Assignment
14. Klik `(←)` pada kotak Search

### Seleksi bulk Request Extension hanya memuat satu Borrower
15. Klik tab `Borrowed`
16. Centang baris `Laptop Lenovo E14 {runId}`
17. Verifikasi checkbox baris `Monitor Dell P2422H {runId}` disabled
18. Verifikasi alasan `Select assets from one borrower only.` tersampaikan pada checkbox baris `Monitor Dell P2422H {runId}` yang disabled
19. Klik checkbox header tabel
20. Verifikasi baris `Laptop Lenovo E14 {runId}`, `Proyektor Epson X06 {runId}`, `Mikrofon Shure SM58 {runId}`, dan `Tripod Manfrotto 055 {runId}` tercentang
21. Verifikasi baris `Monitor Dell P2422H {runId}` dan `Router Mikrotik hAP {runId}` tidak tercentang
22. Verifikasi counter seleksi menampilkan jumlah `4`
23. Klik `✕` pada Bulk Action Bar untuk menghapus seleksi
24. Centang baris `Laptop Lenovo E14 {runId}`
25. Verifikasi tombol `Select All (4 records)` tampil
26. Klik `Select All (4 records)`
27. Verifikasi baris `Proyektor Epson X06 {runId}`, `Mikrofon Shure SM58 {runId}`, dan `Tripod Manfrotto 055 {runId}` tercentang
28. Verifikasi baris `Monitor Dell P2422H {runId}` dan `Router Mikrotik hAP {runId}` tidak tercentang
29. Verifikasi tombol `Unselect All (4 records)` tampil
30. Klik `✕` pada Bulk Action Bar untuk menghapus seleksi

### Aksi baris Borrowed bagi PIC atas nama Borrower tanpa akun
31. Buka menu `⋯` pada baris `Laptop Lenovo E14 {runId}`
32. Verifikasi menu memuat `Borrow Log`
33. Verifikasi menu memuat `Request Extension`
34. Verifikasi menu memuat `Report Damaged`
35. Verifikasi menu memuat `Report Missing`
36. Verifikasi menu tidak memuat `Unassign`
37. Verifikasi menu tidak memuat `Assignment Log`
38. Tutup menu `⋯` dengan Esc
39. Buka menu `⋯` pada baris `Proyektor Epson X06 {runId}`
40. Verifikasi menu memuat `Return`
41. Tutup menu `⋯` dengan Esc
42. Buka menu `⋯` pada baris `Kamera Canon M50 {runId}`
43. Verifikasi menu memuat `Cancel Borrow`
44. Tutup menu `⋯` dengan Esc
45. Buka menu `⋯` pada baris `Tablet Samsung A9 {runId}`
46. Verifikasi menu memuat `Cancel Extension Request`
47. Tutup menu `⋯` dengan Esc
48. Buka menu `⋯` pada baris `Mikrofon Shure SM58 {runId}`
49. Verifikasi menu memuat `Cancel Damage Report`
50. Tutup menu `⋯` dengan Esc
51. Buka menu `⋯` pada baris `Tripod Manfrotto 055 {runId}`
52. Verifikasi menu memuat `Cancel Missing Report`
53. Tutup menu `⋯` dengan Esc

### Request Extension untuk Borrower tanpa akun hanya menawarkan pinjaman Borrower itu
54. Buka menu `⋯` pada baris `Laptop Lenovo E14 {runId}`
55. Klik `Request Extension`
56. Verifikasi breadcrumb `My Asset > Borrowed > Extension Request` tampil
57. Verifikasi tabel Extension Request memuat aset `Laptop Lenovo E14 {runId}`
58. Verifikasi tabel Extension Request tidak memuat kolom `Extensions` dan `Max Duration`
59. Klik `[+ Asset]`
60. Verifikasi daftar kandidat memuat aset `Proyektor Epson X06 {runId}`
61. Verifikasi daftar kandidat tidak memuat aset `Monitor Dell P2422H {runId}` milik aktor sendiri
62. Verifikasi daftar kandidat tidak memuat aset `Router Mikrotik hAP {runId}` milik Borrower `Maya Putri`
63. Tutup daftar kandidat
64. Klik breadcrumb `Borrowed`

### Riwayat Borrower tanpa akun tampil di tab History dengan kolom Holder
65. Klik tab `History`
66. Verifikasi baris `Printer Canon G3010 {runId}` tampil
67. Verifikasi kolom `Holder` pada baris `Printer Canon G3010 {runId}` berisi `Hendra K`

### Confirm Handover atas nama Borrower tanpa akun memakai pernyataan PIC
68. Klik tab `Task`
69. Buka menu `⋯` pada baris Task `Confirm Handover` untuk pinjaman DU-040-12
70. Verifikasi menu memuat `Confirm Handover`
71. Klik `Confirm Handover`
72. Verifikasi pernyataan `I confirm that Hendra Kusuma has received the checked assets.` tampil pada dialog `Confirm Handover`
73. Centang pernyataan pada dialog `Confirm Handover`
74. Klik `[Confirm]`
75. Verifikasi toast `Success, 1 asset has been handed over.` tampil
76. Verifikasi tab Task menampilkan empty state `No tasks`
77. Klik tab `Borrowed`
78. Verifikasi baris `Scanner Epson V39 {runId}` berstatus `Borrowed`
79. Buka menu `⋯` pada baris `Scanner Epson V39 {runId}`
80. Klik `Borrow Log`
81. Verifikasi node konfirmasi pada dialog Borrow Log dicatat `Confirmed by [PIC] on behalf of [Borrower]` dengan PIC `Taufik Hidayat {runId}` dan Borrower `Hendra Kusuma`
