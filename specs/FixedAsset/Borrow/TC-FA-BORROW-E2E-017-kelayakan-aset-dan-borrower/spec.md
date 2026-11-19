---
id: TC-FA-BORROW-E2E-017-kelayakan-aset-dan-borrower
title: "Kelayakan aset dan Borrower ditampilkan sebagai alasan tidak layak di form, Draft, dan Select Borrower"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["FI-BRW-29", "FI-BRW-30", "FI-BRW-31", "FI-BRW-32", "V-BRW-01", "V-BRW-02", "V-BRW-03", "V-BRW-04", "V-BRW-05", "V-BRW-06", "V-BRW-08", "V-BRW-09", "V-BRW-10", "V-BRW-11", "V-BRW-12", "V-BRW-13", "V-BRW-14", "V-BRW-40", "V-BRW-41", "V-BRW-42", "V-BRW-43", "V-BRW-44", "V-BRW-45", "V-BRW-46", "§4.8#p2", "§6#p1", "EB-CON-4"]
smoke: []
dependsOn: []
trace:
  "FI-BRW-29": 34
  "FI-BRW-30": 35
  "FI-BRW-31": 37
  "FI-BRW-32": 42
  "V-BRW-01": 7
  "V-BRW-02": 90
  "V-BRW-03": 14
  "V-BRW-04": [5, 24, 26, 28]
  "V-BRW-05": [87, 88]
  "V-BRW-06": [70, 106]
  "V-BRW-08": 34
  "V-BRW-09": [10, 11]
  "V-BRW-10": [9, 92, 93]
  "V-BRW-11": [12, 23]
  "V-BRW-12": 76
  "V-BRW-13": 54
  "V-BRW-14": [42, 47]
  "V-BRW-40": 6
  "V-BRW-41": 7
  "V-BRW-42": 8
  "V-BRW-43": 9
  "V-BRW-44": 10
  "V-BRW-45": 11
  "V-BRW-46": 12
  "§4.8#p2": 10
  "§6#p1": 13
  "EB-CON-4": [76, 80]
anchor: [4, 18]
coverage:
  web: automated
---

# Kelayakan aset dan Borrower ditampilkan sebagai alasan tidak layak di form, Draft, dan Select Borrower

## Prerequisites
- Aktor: Asset Admin `Asset Admin Kelayakan {runId}` (Aktor Borrow) dengan Group penugasan `Head Office` dan `Branch Surabaya`.
- Layar awal: Transactions > Borrow.
- Data:
  - DU-017-1: Aktor `Asset Admin Kelayakan {runId}`, role Asset Admin, Group penugasan `Head Office` dan `Branch Surabaya`.
  - DU-017-2: Borrower `Pratiwi Borrower {runId}`, Email `pratiwi.borrower{runId}@example.com`, Position `Staff {runId}`, Division `Finance {runId}`, Home Group `Head Office`, akun ber-login Status `Active` dan Activation Status `Activated`, Active Borrows `0 assets`.
  - DU-017-3: Borrower `Surya Surabaya {runId}`, Email `surya.surabaya{runId}@example.com`, Position `Staff {runId}`, Division `Finance {runId}`, Home Group `Branch Surabaya`, akun ber-login Status `Active` dan Activation Status `Activated`, Active Borrows `0 assets`.
  - DU-017-4: Borrower `Edo Terlambat {runId}`, Email `edo.terlambat{runId}@example.com`, Position `Operator {runId}`, Division `Warehouse {runId}`, Home Group `Head Office`, akun ber-login aktif, Active Borrows `1 asset` berstatus Overdue (Due date T0 − 3 hari); alasan Blocked `Edo Terlambat {runId} has an overdue borrow: [Asset Code], due [Date]. Return it first.`.
  - DU-017-5: Borrower `Lukman Resign {runId}`, Email `lukman.resign{runId}@example.com`, Home Group `Head Office`, karyawan sudah dinonaktifkan sesudah Draft disimpan; pesan di field Borrower `Lukman Resign {runId} is no longer active. Pick another borrower.`.
  - DU-017-6: karyawan tanpa akun login `Wawan Tanpa PIC {runId}`, Email `wawan.tanpapic{runId}@example.com`, Home Group `Head Office`, PIC sudah dikosongkan sesudah Draft disimpan; pesan di field Borrower `Wawan Tanpa PIC {runId} has no login account and no PIC. Set a PIC in Users first.`; alasan Blocked di Select Borrower `No login account and no PIC. Set a PIC in Users first.`.
  - DU-017-7: Borrower `Citra Batas {runId}`, Email `citra.batas{runId}@example.com`, Home Group `Head Office`, akun ber-login aktif, Active Borrows `9 assets`; pesan batas `Citra Batas {runId} can borrow up to 10 assets at a time.`.
  - DU-017-8: pemegang hak Manage asset & TAG `Rizal Manager {runId}`, kontak pada alasan Deny pada override.
  - DU-017-9: aset `Laptop Lenovo Yoga {runId}` sudah dihapus (Deleted); tooltip `This asset has been deleted.`.
  - DU-017-10: aset `Tablet Samsung Tab {runId}` berstatus Condition `Damaged`; tooltip `This asset is Damaged and can't be borrowed.`.
  - DU-017-11: aset `Genset Honda {runId}` ber-TAG `RFID` yang dapat dipindai dan sedang ada di BRW aktif milik Borrower lain; tooltip `This asset is already in another transaction.`.
  - DU-017-12: aset `Scanner Zebra {runId}` ber-TAG `RFID` yang perlu diganti; tooltip `This asset can't be borrowed until its TAG is replaced.`.
  - DU-017-13: aset `Drone DJI Air {runId}` dengan Deny pada override aset; tooltip `Can't be borrowed: this asset is not available for borrowing. Contact Rizal Manager {runId} (Manage asset & TAG).`.
  - DU-017-14: aset `Forklift Toyota {runId}` dengan Category `Heavy Machine {runId}` yang Allow Borrow efektifnya Deny; tooltip `Borrowing isn't allowed for Heavy Machine {runId}.`.
  - DU-017-15: aset `Bus Hino {runId}` di Group `Branch Surabaya` dengan Allowed borrower `Same Group only`; tooltip bagi Borrower `Pratiwi Borrower {runId}` `Pratiwi Borrower {runId} can't borrow assets from Branch Surabaya.`.
  - DU-017-16: aset `Kamera Fujifilm {runId}` dengan TAG yang perlu diganti dan Deny pada override sekaligus; tooltip yang tampil `This asset can't be borrowed until its TAG is replaced.`.
  - DU-017-17: aset `Printer Brother {runId}` layak: Custody `Available`, Allow Borrow `Allow`, Allowed borrower `Employee in any Group`.
  - DU-017-18: aset `Printer Canon {runId}` di Group `Branch Medan` (di luar Group penugasan Aktor), Custody `Available`.
  - DU-017-19: Draft untuk Borrower `Pratiwi Borrower {runId}` berisi sepuluh aset (`Laptop Lenovo Yoga {runId}`, `Tablet Samsung Tab {runId}`, `Genset Honda {runId}`, `Scanner Zebra {runId}`, `Drone DJI Air {runId}`, `Forklift Toyota {runId}`, `Bus Hino {runId}`, `Kamera Fujifilm {runId}`, `Printer Brother {runId}`, `Printer Canon {runId}`), Total Asset `10`, Modified By `Asset Admin Kelayakan {runId}`.
  - DU-017-20: Draft untuk Borrower `Edo Terlambat {runId}` berisi aset `Radio Motorola {runId}` dengan Duration `1` dan Purpose `Training`.
  - DU-017-21: Draft untuk Borrower `Lukman Resign {runId}` berisi aset `Headset Jabra {runId}` dengan Duration `1` dan Purpose `Training`.
  - DU-017-22: Draft untuk Borrower `Wawan Tanpa PIC {runId}` berisi aset `Tripod Manfrotto {runId}` dengan Duration `1` dan Purpose `Training`.
  - DU-017-23: aset layak `Speaker Bose {runId}`, Group `Head Office`, Max Duration `7 days`, Approval `Needs approval`.
  - DU-017-25: aset layak `Mikrofon Rode {runId}`, Group `Head Office`, Max Duration `7 days`, Approval `Needs approval`.
  - DU-017-24: isian form Borrow Request untuk Borrower `Citra Batas {runId}`: Duration `2` dan Purpose `Training` untuk `Speaker Bose {runId}` dan untuk `Mikrofon Rode {runId}`.
  - DU-017-26: Draft kedua untuk Borrower `Pratiwi Borrower {runId}` berisi sembilan aset (`Laptop Lenovo Yoga {runId}`, `Tablet Samsung Tab {runId}`, `Genset Honda {runId}`, `Scanner Zebra {runId}`, `Drone DJI Air {runId}`, `Forklift Toyota {runId}`, `Bus Hino {runId}`, `Kamera Fujifilm {runId}`, `Printer Brother {runId}`) tanpa aset di luar Group penugasan Aktor, Total Asset `9`, Duration `1` dan Purpose `Training` pada setiap baris, Modified By `Asset Admin Kelayakan {runId}`.
  - DU-017-27: Borrower `Dedi Peminjam {runId}`, Email `dedi.peminjam{runId}@example.com`, Position `Staff {runId}`, Division `Finance {runId}`, Home Group `Head Office`, akun ber-login Status `Active` dan Activation Status `Activated`, Active Borrows `1 asset` berupa `Proyektor Epson {runId}` di BRW aktif; pesan saat aset itu dipindai `Dedi Peminjam {runId} already has this asset in [BRW No.]. Use Extend instead.`.
  - DU-017-28: aset `Proyektor Epson {runId}`, Brand `Epson {runId}`, Model/Type `EB-X06 {runId}`, Group `Head Office`, Category `Projector {runId}`, ber-TAG `RFID` yang dapat dipindai, sedang dipinjam Borrower `Dedi Peminjam {runId}` di BRW aktif.
  - DU-017-29: ubahan Draft DU-017-22: Purpose baris `Tripod Manfrotto {runId}` menjadi `Peminjaman lapangan`.
  - DU-017-30: aset `Headphone Sennheiser {runId}`, Group `Head Office`, Custody `Available`, Allow Borrow `Allow`, Allowed borrower `Employee in any Group`, ber-TAG `RFID` yang dapat dipindai; layak bagi Borrower `Pratiwi Borrower {runId}`.
- Kondisi:
  - Max assets per borrower bernilai `10`.
  - Block new borrow when overdue bernilai ON.

## Test Steps

### Draft dibuka: baris tidak layak ditandai dengan satu alasan menurut prioritas
1. Buka tab Drafts
2. Ketik Search `Pratiwi Borrower {runId}`, tekan Enter
3. Klik ikon pensil `Edit` pada baris Draft dengan Total Asset `10`
4. Verifikasi baris `Printer Brother {runId}` tidak ditandai tidak layak dan tidak punya caption error
5. Verifikasi baris `Laptop Lenovo Yoga {runId}`, `Tablet Samsung Tab {runId}`, `Genset Honda {runId}`, `Scanner Zebra {runId}`, `Drone DJI Air {runId}`, `Forklift Toyota {runId}`, `Bus Hino {runId}`, dan `Kamera Fujifilm {runId}` masing-masing ditandai ⚠ dengan caption `This asset can no longer be borrowed.` di bawah nama aset
6. Verifikasi alasan `This asset has been deleted.` tersampaikan pada ⚠ baris `Laptop Lenovo Yoga {runId}`
7. Verifikasi alasan `This asset is Damaged and can't be borrowed.` tersampaikan pada ⚠ baris `Tablet Samsung Tab {runId}`
8. Verifikasi alasan `This asset is already in another transaction.` tersampaikan pada ⚠ baris `Genset Honda {runId}`
9. Verifikasi alasan `This asset can't be borrowed until its TAG is replaced.` tersampaikan pada ⚠ baris `Scanner Zebra {runId}`
10. Verifikasi alasan `Can't be borrowed: this asset is not available for borrowing. Contact Rizal Manager {runId} (Manage asset & TAG).` tersampaikan pada ⚠ baris `Drone DJI Air {runId}` dan menyebut siapa yang dapat dihubungi
11. Verifikasi alasan `Borrowing isn't allowed for Heavy Machine {runId}.` tersampaikan pada ⚠ baris `Forklift Toyota {runId}`
12. Verifikasi alasan `Pratiwi Borrower {runId} can't borrow assets from Branch Surabaya.` tersampaikan pada ⚠ baris `Bus Hino {runId}`
13. Verifikasi ⚠ baris `Kamera Fujifilm {runId}` hanya memuat satu alasan `This asset can't be borrowed until its TAG is replaced.` walau aset juga gagal karena Deny pada override
14. Verifikasi baris `Printer Canon {runId}` tampil read-only dengan keterangan `Outside your groups` dan tanpa isian yang dapat diubah
15. Klik `[Cancel]` pada form yang belum diubah

### Mengganti Borrower menilai ulang kelayakan Allowed borrower
16. Ketik Search `Pratiwi Borrower {runId}`, tekan Enter
17. Klik ikon pensil `Edit` pada baris Draft dengan Total Asset `9`
18. Verifikasi baris `Bus Hino {runId}` ditandai ⚠ dengan caption `This asset can no longer be borrowed.` untuk Borrower `Pratiwi Borrower {runId}`
19. Klik nama Borrower `Pratiwi Borrower {runId}` pada field Borrower untuk mengganti Borrower
20. Ketik Search `Surya Surabaya {runId}`, tekan Enter
21. Pilih baris `Surya Surabaya {runId}`
22. Klik `[Select]`
23. Verifikasi baris `Bus Hino {runId}` tidak lagi ditandai tidak layak karena Borrower `Surya Surabaya {runId}` memenuhi Allowed borrower `Same Group only`
24. Verifikasi baris `Laptop Lenovo Yoga {runId}` tetap ditandai ⚠ dengan caption `This asset can no longer be borrowed.`

### Submit diblokir sampai aset tidak layak dikeluarkan
25. Klik `[Submit]`
26. Verifikasi caption error `Remove the unavailable assets to continue.` tampil di atas deretan tombol dan tidak ada BRW yang dibuat
27. Klik `[Remove Unavailable]`
28. Verifikasi baris `Laptop Lenovo Yoga {runId}`, `Tablet Samsung Tab {runId}`, `Genset Honda {runId}`, `Scanner Zebra {runId}`, `Drone DJI Air {runId}`, `Forklift Toyota {runId}`, dan `Kamera Fujifilm {runId}` tidak lagi ada di form sedangkan baris `Bus Hino {runId}` dan `Printer Brother {runId}` tetap ada
29. Klik `[Cancel]` pada form
30. Klik `[Leave]` pada dialog Unsaved Changes

### Borrower tidak aktif ditolak saat Submit dan Draft tetap tersimpan
31. Ketik Search `Lukman Resign {runId}`, tekan Enter
32. Klik ikon pensil `Edit` pada baris Draft untuk Borrower itu
33. Klik `[Submit]`
34. Verifikasi caption `Lukman Resign {runId} is no longer active. Pick another borrower.` tampil di field Borrower
35. Verifikasi baris `Headset Jabra {runId}` tetap ada dengan Duration `1` dan Purpose `Training`
36. Klik `[Cancel]` pada form yang belum diubah
37. Verifikasi tabel Drafts tetap memuat baris Draft untuk Borrower `Lukman Resign {runId}`

### Borrower tanpa akun login dan tanpa PIC ditolak
38. Ketik Search `Wawan Tanpa PIC {runId}`, tekan Enter
39. Klik ikon pensil `Edit` pada baris Draft untuk Borrower itu
40. Ganti Purpose baris `Tripod Manfrotto {runId}` dengan `Peminjaman lapangan`
41. Klik `[Save Draft]`
42. Verifikasi caption `Wawan Tanpa PIC {runId} has no login account and no PIC. Set a PIC in Users first.` tampil di field Borrower
43. Klik `[Cancel]` pada form, lalu klik `[Leave]` pada dialog Unsaved Changes
44. Klik `[+ Borrow]`
45. Klik `[Select Borrower]`
46. Ketik Search `Wawan Tanpa PIC {runId}`, tekan Enter
47. Verifikasi baris `Wawan Tanpa PIC {runId}` berstatus Eligibility `Blocked` dengan alasan `No login account and no PIC. Set a PIC in Users first.` tersampaikan
48. Klik `[Cancel]` pada dialog Select Borrower
49. Klik `[Cancel]` pada form yang belum diubah

### Block new borrow when overdue menolak Submit
50. Buka tab Drafts
51. Ketik Search `Edo Terlambat {runId}`, tekan Enter
52. Klik ikon pensil `Edit` pada baris Draft untuk Borrower itu
53. Klik `[Submit]`
54. Verifikasi caption error `Edo Terlambat {runId} has an overdue borrow: [Asset Code], due [Date]. Return it first.` tampil di atas deretan tombol, dengan Asset Code dan Date dari baris Overdue Borrower itu
55. Klik `[Cancel]` pada form yang belum diubah

### Batas Max assets per borrower: pengajuan ke-N berhasil dan ke-N+1 ditolak
56. Klik `[+ Borrow]`
57. Klik `[Select Borrower]`
58. Ketik Search `Citra Batas {runId}`, tekan Enter
59. Pilih baris `Citra Batas {runId}`
60. Klik `[Select]`
61. Klik `[+ Asset]`
62. Ketik Search `{runId}`, tekan Enter
63. Centang baris `Speaker Bose {runId}`
64. Centang baris `Mikrofon Rode {runId}`
65. Klik `[Select]`
66. Klik `[+ Asset]`
67. Ketik Search `{runId}`, tekan Enter
68. Centang baris `Speaker Bose {runId}` yang sudah ada di form
69. Klik `[Select]`
70. Verifikasi toast netral `This asset is already in this borrow.` tampil dan baris aset tidak digandakan
71. Isi Duration baris `Speaker Bose {runId}` dengan `2`
72. Isi Purpose baris `Speaker Bose {runId}` dengan `Training`
73. Isi Duration baris `Mikrofon Rode {runId}` dengan `2`
74. Isi Purpose baris `Mikrofon Rode {runId}` dengan `Training`
75. Klik `[Submit]`
76. Verifikasi caption error `Citra Batas {runId} can borrow up to 10 assets at a time.` tampil di atas deretan tombol untuk pengajuan ke-11
77. Pilih aksi baris `Remove from List` pada baris `Mikrofon Rode {runId}`
78. Klik `[Submit]`
79. Klik `[Submit]` pada dialog `Submit Borrow`
80. Verifikasi toast `Success, borrow has been submitted for approval.` tampil untuk pengajuan ke-10

### Aset yang sudah dipinjam atau yang TAG-nya perlu diganti ditolak saat dipindai di form
81. Klik `[+ Borrow]`
82. Klik `[Select Borrower]`
83. Ketik Search `Dedi Peminjam {runId}`, tekan Enter
84. Pilih baris `Dedi Peminjam {runId}`
85. Klik `[Select]`
86. Scan TAG aset `Proyektor Epson {runId}` lewat `[Add by Scan]`
87. Verifikasi pesan `Dedi Peminjam {runId} already has this asset in [BRW No.]. Use Extend instead.` tampil dengan [BRW No.] berisi nomor BRW yang memuat `Proyektor Epson {runId}`
88. Verifikasi tautan ke BRW itu tersedia bersama pesan tersebut
89. Scan TAG aset `Genset Honda {runId}` lewat `[Add by Scan]`
90. Verifikasi pesan `This asset is already in [BRW No.].` tampil dengan [BRW No.] berisi nomor BRW milik Borrower lain yang memuat `Genset Honda {runId}`
91. Scan TAG aset `Scanner Zebra {runId}` lewat `[Add by Scan]`
92. Verifikasi pesan `This asset can't be borrowed until its TAG is replaced.` tampil
93. Verifikasi aksi `[Report TAG]` tersedia bersama pesan itu
94. Klik `[Cancel]` pada form
95. Klik `[Leave]` pada dialog Unsaved Changes

### Aset yang sudah ada di form tidak digandakan saat dipindai ulang
96. Klik `[+ Borrow]`
97. Klik `[Select Borrower]`
98. Ketik Search `Pratiwi Borrower {runId}`, tekan Enter
99. Pilih baris `Pratiwi Borrower {runId}`
100. Klik `[Select]`
101. Klik `[+ Asset]`
102. Ketik Search `Headphone Sennheiser {runId}`, tekan Enter
103. Centang baris `Headphone Sennheiser {runId}`
104. Klik `[Select]`
105. Scan TAG aset `Headphone Sennheiser {runId}` lewat `[Add by Scan]`
106. Verifikasi toast netral `This asset is already in this borrow.` tampil dan baris `Headphone Sennheiser {runId}` tetap satu baris di form
107. Klik `[Cancel]` pada form
108. Klik `[Leave]` pada dialog Unsaved Changes
