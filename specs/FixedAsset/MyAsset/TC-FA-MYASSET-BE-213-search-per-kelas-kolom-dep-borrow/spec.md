---
id: TC-FA-MYASSET-BE-213-search-per-kelas-kolom-dep-borrow
title: "Search My Asset per kelas kolom di keempat tabel"
layer: be-e2e
priority: Medium
caseType: Positive
status: draft
sourceRules: ["T-MYA-01", "T-MYA-04", "§4.1b#r2", "§4.1b#r3", "§4.1b#r4", "§4.1b#r5", "§4.1b#r6", "§4.1b#r7", "§4.1b#r8", "§4.1b#r9", "§4.1b#r11", "§4.1b#r12", "§4.1b#r13", "§4.1b#r14", "§4.1b#r15", "§4.1b#r17", "§4.1b#r18", "§4.1c#r2", "§4.1c#r3", "§4.1c#r4", "§4.1c#r5", "§4.1c#r6", "§4.1c#r7", "§4.1c#r8", "§4.1c#r9", "§4.1c#r10", "§4.1c#r11", "§4.1c#r12", "§4.1c#r17", "§5#r3", "EB-SRC-1"]
smoke: []
dependsOn: ["Transactions > Borrow: pinjaman, approval, sesi Handover, Extension, dan Return oleh Aktor Borrow", "Transactions > Assignment: penugasan, approval, sesi Handover, Change PIC, dan Unassign oleh Aktor Assignment"]
owner: BE
trace:
  "T-MYA-01": [78, 80, 82, 84, 86, 88]
  "T-MYA-04": [56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76]
  "§4.1b#r2": 2
  "§4.1b#r3": 4
  "§4.1b#r4": 6
  "§4.1b#r5": 8
  "§4.1b#r6": 10
  "§4.1b#r7": 12
  "§4.1b#r8": 14
  "§4.1b#r9": 16
  "§4.1b#r11": 18
  "§4.1b#r12": 20
  "§4.1b#r13": 30
  "§4.1b#r14": 22
  "§4.1b#r15": 24
  "§4.1b#r17": 26
  "§4.1b#r18": 28
  "§4.1c#r2": 32
  "§4.1c#r3": 34
  "§4.1c#r4": 36
  "§4.1c#r5": 38
  "§4.1c#r6": 40
  "§4.1c#r7": 42
  "§4.1c#r8": 44
  "§4.1c#r9": 46
  "§4.1c#r10": 48
  "§4.1c#r11": 50
  "§4.1c#r12": 54
  "§4.1c#r17": 52
  "§5#r3": [88, 90, 92]
  "EB-SRC-1": [90, 92, 94]
---

# Search My Asset per kelas kolom di keempat tabel

## Prerequisites
- Aktor: Borrower dan Assignee, yaitu pengguna ber-akun login `Rina Wulandari {runId}` (DU-213-1) yang membuka My Asset dan tidak punya baris lain selain DU-213-2 sampai DU-213-11. Aktor Borrow `Budi Santoso {runId}` dan Aktor Assignment `Agus Pratama {runId}` dan `Siti Rahmawati {runId}` menyerahkan aset ke Aktor, masing-masing dengan hak atas Group aset yang diserahkannya.
- Data:
  - DU-213-1: Aktor pemegang semua baris di bawah, tanpa baris lain di My Asset: Name `Rina Wulandari {runId}`, Posisi `Borrower dan Assignee`.
  - DU-213-2: pinjaman Admin berstatus Borrowed milik Aktor: Name `Laptop Operasional {runId}`, Asset ID `LPT-0101 {runId}`, Brand `Dell`, Model/Type `Latitude 5440`, Group `Ruang IT`, Status `Borrowed`, TAG `RFID`, Category `Komputer`, Remaining `Due in`, Borrower `Me`, Transaction ID `nomor BRW milik DU-213-2`, Source `Admin`, Duration `3 days`, Extensions `1 / 3`, Purpose `Dinas luar kota ke Surabaya`.
  - DU-213-3: pinjaman self-service berstatus Waiting for Approval milik Aktor: Name `Proyektor Rapat {runId}`, Asset ID `PRJ-0202 {runId}`, Brand `Epson`, Model/Type `EB-X500`, Group `Ruang Rapat`, Status `Waiting for Approval`, TAG `NFC`, Category `Elektronik`, Remaining `—`, Borrower `Me`, Transaction ID `nomor BRW milik DU-213-3`, Source `Self-service`, Duration `5 days`, Extensions `0 / 1`, Purpose `Presentasi klien di kantor cabang`.
  - DU-213-4: pinjaman Admin Waiting for Handover atas nama Borrower tanpa akun yang PIC-nya Aktor: Name `Kamera Dokumentasi {runId}`, Asset ID `CAM-0303 {runId}`, Brand `Canon`, Model/Type `EOS R50`, Group `Studio`, Status `Waiting for Handover`, TAG `Non TAG`, Category `Fotografi`, Remaining `—`, Borrower `Hendra Wijaya {runId}`, Transaction ID `nomor BRW milik DU-213-4`, Source `Admin`, Duration `8 hours`, Extensions `0 / 2`, Purpose `Liputan acara gathering tahunan`.
  - DU-213-5: pinjaman Returned milik Aktor: Name `Mikrofon Studio {runId}`, Asset ID `MIC-0404 {runId}`, Brand `Shure`, Model/Type `SM58`, Group `Ruang Rekam`, Status `Returned`, Holder `Me`, TAG `RFID`, Category `Audio`, Type `Borrow`, Transaction ID `nomor BRW milik DU-213-5`, Purpose `Rekaman siaran internal`.
  - DU-213-6: penugasan Unassigned atas nama Division yang PIC-nya Aktor: Name `Monitor Kerja {runId}`, Asset ID `MON-0505 {runId}`, Brand `Samsung`, Model/Type `S24C`, Group `Ruang Finance`, Status `Unassigned`, Holder `Divisi Keuangan {runId}`, TAG `NFC`, Category `Peripheral`, Type `Assignment`, Transaction ID `nomor ASG milik DU-213-6`, Purpose `Penggunaan harian tim keuangan`.
  - DU-213-7: pinjaman Rejected atas nama Borrower tanpa akun yang PIC-nya Aktor: Name `Printer Kantor {runId}`, Asset ID `PRN-0606 {runId}`, Brand `Brother`, Model/Type `HL-L2320`, Group `Ruang Arsip`, Status `Rejected`, Holder `Hendra Wijaya {runId}`, TAG `Non TAG`, Category `Perangkat Cetak`, Type `Borrow`, Transaction ID `nomor BRW milik DU-213-7`, Purpose `Cetak dokumen audit`.
  - DU-213-8: penugasan Assigned milik Aktor: Name `Notebook Staf {runId}`, Asset ID `LTP-0707 {runId}`, Brand `Lenovo`, Model/Type `ThinkPad T14`, Group `Ruang Staf`, Status `Assigned`, Assigned To `Me`, TAG `RFID`, Category `Laptop`, Transaction ID `nomor ASG milik DU-213-8`, Assigned By `Siti Rahmawati {runId}`.
  - DU-213-9: penugasan Waiting for Handover atas nama Division yang PIC-nya Aktor: Name `Meja Rapat Besar {runId}`, Asset ID `FRN-0808 {runId}`, Brand `Informa`, Model/Type `Oval 200`, Group `Ruang Direksi`, Status `Waiting for Handover`, Assigned To `Divisi Keuangan {runId}`, TAG `NFC`, Category `Furnitur`, Transaction ID `nomor ASG milik DU-213-9`, Assigned By `Agus Pratama {runId}`.
  - DU-213-10: Task Confirm Handover pinjaman milik Aktor: Transaction ID `nomor BRW milik DU-213-10`, Task `Confirm Handover`, Group `Ruang IT`, Total Asset `2`, Handed Over By `Budi Santoso {runId}`, Expires At `waktu Expires At milik DU-213-10`.
  - DU-213-11: Task Confirm Handover penugasan milik Aktor: Transaction ID `nomor ASG milik DU-213-11`, Task `Confirm Handover`, Group `Ruang Direksi`, Total Asset `7`, Handed Over By `Agus Pratama {runId}`, Expires At `waktu Expires At milik DU-213-11`.
- Kondisi:
  - Date Format bernilai `dd/MM/yy` dan Time Format bernilai `24 jam`
  - Kolom `TAG`, `Category`, `Extensions`, dan `Purpose` tampil pada tabel yang dicari

## Test Steps

### Search tab Borrowed mencocokkan kolom teks, badge, dan ikon
1. Aktor meminta daftar tab Borrowed dengan kata kunci Search `Operasional`
2. Verifikasi hasil memuat baris DU-213-2 dan tidak memuat baris DU-213-3 maupun DU-213-4
3. Aktor meminta daftar tab Borrowed dengan kata kunci Search `LPT-0101`
4. Verifikasi hasil memuat baris DU-213-2 dan tidak memuat baris DU-213-3 maupun DU-213-4
5. Aktor meminta daftar tab Borrowed dengan kata kunci Search `Dell`
6. Verifikasi hasil memuat baris DU-213-2 dan tidak memuat baris DU-213-3 maupun DU-213-4
7. Aktor meminta daftar tab Borrowed dengan kata kunci Search `Latitude`
8. Verifikasi hasil memuat baris DU-213-2 dan tidak memuat baris DU-213-3 maupun DU-213-4
9. Aktor meminta daftar tab Borrowed dengan kata kunci Search `Ruang IT`
10. Verifikasi hasil memuat baris DU-213-2 dan tidak memuat baris DU-213-3 maupun DU-213-4
11. Aktor meminta daftar tab Borrowed dengan kata kunci Search `Waiting for Approval`
12. Verifikasi hasil memuat baris DU-213-3 dan tidak memuat baris DU-213-2 maupun DU-213-4
13. Aktor meminta daftar tab Borrowed dengan kata kunci Search `RFID`
14. Verifikasi hasil memuat baris DU-213-2 dan tidak memuat baris DU-213-3 maupun DU-213-4
15. Aktor meminta daftar tab Borrowed dengan kata kunci Search `Komputer`
16. Verifikasi hasil memuat baris DU-213-2 dan tidak memuat baris DU-213-3 maupun DU-213-4
17. Aktor meminta daftar tab Borrowed dengan kata kunci Search `Due in`
18. Verifikasi hasil memuat baris DU-213-2 dan tidak memuat baris DU-213-3 maupun DU-213-4
19. Aktor meminta daftar tab Borrowed dengan kata kunci Search `Hendra`
20. Verifikasi hasil memuat baris DU-213-4 dan tidak memuat baris DU-213-2 maupun DU-213-3
21. Aktor meminta daftar tab Borrowed dengan kata kunci Search `Self-service`
22. Verifikasi hasil memuat baris DU-213-3 dan tidak memuat baris DU-213-2 maupun DU-213-4
23. Aktor meminta daftar tab Borrowed dengan kata kunci Search `8 hours`
24. Verifikasi hasil memuat baris DU-213-4 dan tidak memuat baris DU-213-2 maupun DU-213-3
25. Aktor meminta daftar tab Borrowed dengan kata kunci Search `1 / 3`
26. Verifikasi hasil memuat baris DU-213-2 dan tidak memuat baris DU-213-3 maupun DU-213-4
27. Aktor meminta daftar tab Borrowed dengan kata kunci Search `Surabaya`
28. Verifikasi hasil memuat baris DU-213-2 dan tidak memuat baris DU-213-3 maupun DU-213-4
29. Aktor meminta daftar tab Borrowed dengan kata kunci Search berupa nomor BRW milik DU-213-3
30. Verifikasi hasil memuat baris DU-213-3 dan tidak memuat baris DU-213-2 maupun DU-213-4

### Search tab History mencocokkan kolom teks, badge, ikon, dan pemegang
31. Aktor meminta daftar tab History dengan kata kunci Search `Mikrofon`
32. Verifikasi hasil memuat baris DU-213-5 dan tidak memuat baris DU-213-6 maupun DU-213-7
33. Aktor meminta daftar tab History dengan kata kunci Search `MIC-0404`
34. Verifikasi hasil memuat baris DU-213-5 dan tidak memuat baris DU-213-6 maupun DU-213-7
35. Aktor meminta daftar tab History dengan kata kunci Search `Shure`
36. Verifikasi hasil memuat baris DU-213-5 dan tidak memuat baris DU-213-6 maupun DU-213-7
37. Aktor meminta daftar tab History dengan kata kunci Search `SM58`
38. Verifikasi hasil memuat baris DU-213-5 dan tidak memuat baris DU-213-6 maupun DU-213-7
39. Aktor meminta daftar tab History dengan kata kunci Search `Ruang Arsip`
40. Verifikasi hasil memuat baris DU-213-7 dan tidak memuat baris DU-213-5 maupun DU-213-6
41. Aktor meminta daftar tab History dengan kata kunci Search `Rejected`
42. Verifikasi hasil memuat baris DU-213-7 dan tidak memuat baris DU-213-5 maupun DU-213-6
43. Aktor meminta daftar tab History dengan kata kunci Search `Divisi Keuangan`
44. Verifikasi hasil memuat baris DU-213-6 dan tidak memuat baris DU-213-5 maupun DU-213-7
45. Aktor meminta daftar tab History dengan kata kunci Search `NFC`
46. Verifikasi hasil memuat baris DU-213-6 dan tidak memuat baris DU-213-5 maupun DU-213-7
47. Aktor meminta daftar tab History dengan kata kunci Search `Audio`
48. Verifikasi hasil memuat baris DU-213-5 dan tidak memuat baris DU-213-6 maupun DU-213-7
49. Aktor meminta daftar tab History dengan kata kunci Search `Assignment`
50. Verifikasi hasil memuat baris DU-213-6 dan tidak memuat baris DU-213-5 maupun DU-213-7
51. Aktor meminta daftar tab History dengan kata kunci Search `siaran`
52. Verifikasi hasil memuat baris DU-213-5 dan tidak memuat baris DU-213-6 maupun DU-213-7
53. Aktor meminta daftar tab History dengan kata kunci Search berupa nomor ASG milik DU-213-6
54. Verifikasi hasil memuat baris DU-213-6 dan tidak memuat baris DU-213-5 maupun DU-213-7

### Search tab Assigned mencocokkan setiap kolom searchable
55. Aktor meminta daftar tab Assigned dengan kata kunci Search `Notebook`
56. Verifikasi hasil memuat baris DU-213-8 dan tidak memuat baris DU-213-9
57. Aktor meminta daftar tab Assigned dengan kata kunci Search `LTP-0707`
58. Verifikasi hasil memuat baris DU-213-8 dan tidak memuat baris DU-213-9
59. Aktor meminta daftar tab Assigned dengan kata kunci Search `Lenovo`
60. Verifikasi hasil memuat baris DU-213-8 dan tidak memuat baris DU-213-9
61. Aktor meminta daftar tab Assigned dengan kata kunci Search `ThinkPad`
62. Verifikasi hasil memuat baris DU-213-8 dan tidak memuat baris DU-213-9
63. Aktor meminta daftar tab Assigned dengan kata kunci Search `Ruang Staf`
64. Verifikasi hasil memuat baris DU-213-8 dan tidak memuat baris DU-213-9
65. Aktor meminta daftar tab Assigned dengan kata kunci Search `Waiting for Handover`
66. Verifikasi hasil memuat baris DU-213-9 dan tidak memuat baris DU-213-8
67. Aktor meminta daftar tab Assigned dengan kata kunci Search `Divisi Keuangan`
68. Verifikasi hasil memuat baris DU-213-9 dan tidak memuat baris DU-213-8
69. Aktor meminta daftar tab Assigned dengan kata kunci Search `RFID`
70. Verifikasi hasil memuat baris DU-213-8 dan tidak memuat baris DU-213-9
71. Aktor meminta daftar tab Assigned dengan kata kunci Search `Laptop`
72. Verifikasi hasil memuat baris DU-213-8 dan tidak memuat baris DU-213-9
73. Aktor meminta daftar tab Assigned dengan kata kunci Search `Agus`
74. Verifikasi hasil memuat baris DU-213-9 dan tidak memuat baris DU-213-8
75. Aktor meminta daftar tab Assigned dengan kata kunci Search berupa nomor ASG milik DU-213-9
76. Verifikasi hasil memuat baris DU-213-9 dan tidak memuat baris DU-213-8

### Search tab Task mencocokkan kolom searchable dan tidak mencocokkan Expires At
77. Aktor meminta daftar tab Task dengan kata kunci Search berupa nomor BRW milik DU-213-10
78. Verifikasi hasil memuat baris DU-213-10 dan tidak memuat baris DU-213-11
79. Aktor meminta daftar tab Task dengan kata kunci Search `Confirm Handover`
80. Verifikasi hasil memuat baris DU-213-10 dan DU-213-11
81. Aktor meminta daftar tab Task dengan kata kunci Search `Direksi`
82. Verifikasi hasil memuat baris DU-213-11 dan tidak memuat baris DU-213-10
83. Aktor meminta daftar tab Task dengan kata kunci Search `7`
84. Verifikasi hasil memuat baris DU-213-11
85. Aktor meminta daftar tab Task dengan kata kunci Search `Budi`
86. Verifikasi hasil memuat baris DU-213-10 dan tidak memuat baris DU-213-11
87. Aktor meminta daftar tab Task dengan kata kunci Search berupa tanggal Expires At milik DU-213-10 sebagaimana tampil menurut Date Format dan Time Format
88. Verifikasi hasil tidak memuat baris apa pun karena kolom tanggal tidak ikut dicari

### Search mencocokkan substring, tidak peka huruf besar kecil, dan kata kunci tanpa kecocokan tidak menghasilkan baris
89. Aktor meminta daftar tab Borrowed dengan kata kunci Search `tional`, potongan di tengah nilai Name DU-213-2
90. Verifikasi hasil memuat baris DU-213-2 dan tidak memuat baris DU-213-3 maupun DU-213-4
91. Aktor meminta daftar tab Borrowed dengan kata kunci Search `OPERASIONAL`, huruf besar semua
92. Verifikasi hasil memuat baris DU-213-2 dan tidak memuat baris DU-213-3 maupun DU-213-4
93. Aktor meminta daftar tab Borrowed dengan kata kunci Search `zzz tidak ada`
94. Verifikasi hasil tidak memuat baris apa pun
