---
id: TC-FA-FAREG-UI-036-approval-submit-keputusan
title: "Halaman Approval: dialog Submit Approval, dialog blok, toast, dan respons gagal"
layer: ui-client
priority: Medium
caseType: Positive
status: draft
sourceRules: [D-REG-10, D-REG-19, T-REG-08, T-REG-12, T-REG-13, V-REG-14, §4.1#r10, §4.2.4#p4, §4.2.4#b10, §4.2.4#b12, §4.8#r27, §9.4.2#r23, §9.6#r4, §9.9#r21, EB-ERR-1@keputusan-approval, EB-FB-1@keputusan-approval, EB-FRM-1@halaman-approval]
smoke: []
dependsOn: []
trace:
  D-REG-10: [9, 10, 11, 12, 13, 14, 15, 16, 18, 21, 22, 23, 24]
  D-REG-19: [71, 72, 74, 81, 82, 89, 90]
  T-REG-08: [28, 57, 66]
  T-REG-12: [35, 55]
  T-REG-13: 46
  V-REG-14: [93, 94, 99, 100]
  §4.1#r10: [9, 11, 12, 13, 14, 21]
  §4.2.4#p4: [6, 7, 9]
  §4.2.4#b10: [11, 12, 13, 14, 21, 22, 23, 24]
  §4.2.4#b12: [71, 73, 76, 77, 81, 84, 85, 89]
  §4.8#r27: [7, 9]
  §9.4.2#r23: [93, 94, 99]
  §9.6#r4: [28, 29, 35]
  §9.9#r21: [93, 94, 100]
  EB-ERR-1@keputusan-approval: [36, 37, 39, 40, 46, 47, 48, 50, 51, 58]
  EB-FB-1@keputusan-approval: [28, 35]
  EB-FRM-1@halaman-approval: [62, 63, 66]
anchor: []
coverage:
  web: automated
---
# Halaman Approval: dialog Submit Approval, dialog blok, toast, dan respons gagal

## Prerequisites
- Aktor: Dewi A (approver, role Group Manager, cakupan Group binaan + sub-group termasuk Gudang 1, bukan pengaju pengajuan); Hadi K (role Manage asset & TAG, cakupan Group terkelola) yang membatalkan pengajuan pada K1; Agus P (role Total Control, cakupan seluruh client) yang memutuskan pengajuan pada K6.
- Layar awal: Halaman Approval pengajuan yang dibuka dari antrean Approvals tab Active.
- Komponen: Halaman Approval
- Data:
  - DU-036-1: pengajuan Registration ID `REG-20261109-00003`, Status `Waiting for Approval`, Group `Gudang 1`, Requested By `Rina W`, Total Asset `4`.
  - DU-036-2: aset Name `Laptop - 128`, Category `Computers`, Brand `Dell`, Model `Latitude 5440`, Group `Gudang 1`, TAG `Verified`, Condition `Normal`, Corrections `—`, Decision `Approve`, tanpa Reason.
  - DU-036-3: aset Name `Laptop - 129`, Category `Computers`, Brand `Dell`, Model `Latitude 5440`, Group `Gudang 1`, TAG `Skipped`, Condition `Damaged`, Corrections `1`, Decision `Approve`, tanpa Reason.
  - DU-036-4: aset Name `Laptop - 130`, Category `Computers`, Brand `Dell`, Model `Latitude 5440`, Group `Gudang 1`, TAG `Verified`, Condition `Normal`, Corrections `—`, Decision `Approve`, tanpa Reason.
  - DU-036-5: aset Name `Office Desk - 12`, Category `Furniture`, Brand `Kayu Jati`, Model `No Model`, Group `Gudang 1`, TAG `No tag`, Condition `Normal`, Corrections `—`, Decision `Approve`, tanpa Reason.
  - DU-036-6: pengguna Name `Agus P`, role Total Control, cakupan seluruh client.
  - DU-036-7: pengguna Name `Hadi K`, role Manage asset & TAG, cakupan Group terkelola.
  - DU-036-8: aset Name `Laptop - 128`, Category `Computers`, Brand `Lenovo` hasil koreksi staged, Model dikosongkan oleh koreksi Brand, Group `Gudang 1`, TAG `Verified`, Condition `Normal`, Corrections `1`, Decision `Approve`, tanpa Reason.
  - Ringkasan dialog `Submit Approval` yang diharapkan pada K1 setelah `Laptop - 130` diubah ke `Return to Draft` dan `Office Desk - 12` ke `Reject`: Approve `2`, Return to Draft `1`, Reject `1`, koreksi `1`, dari Decision dan Corrections pada DU-036-2 sampai DU-036-5.
  - Ringkasan dialog `Submit Approval` yang diharapkan pada K1 tanpa perubahan Decision: Approve `4`, Return to Draft `0`, Reject `0`, koreksi `1`, dari Decision dan Corrections pada DU-036-2 sampai DU-036-5.
  - Teks dialog yang diharapkan: `This request was canceled by Hadi K. Your decisions were not saved.` (dibatalkan oleh `Hadi K`), `This request was already decided by Agus P. Your decisions were not saved.` (diputuskan oleh `Agus P`), dan `This request was canceled by the system. Your decisions were not saved.` (dibatalkan otomatis oleh sistem), dari template `D-REG-19` dan User `Hadi K`, `Agus P`, atau `the system`.
  - Pesan yang diharapkan saat Model perlu dipilih ulang `Select Model again`, dari template `Select [Field Name] again` dan Field Name `Model`.
- Kondisi:
  - K1: pengajuan DU-036-1 berisi aset DU-036-2, DU-036-3, dan DU-036-4 dalam grup Accordion `Laptop` dan DU-036-5 dalam grup Accordion `Office Desk`, dengan Decision awal `Approve`, approver berhak memutuskan, dan menyimpan keputusan berhasil.
  - K2: seperti K1, dan menyimpan keputusan gagal karena error server.
  - K3: seperti K1, dan menyimpan keputusan gagal karena koneksi terputus.
  - K4: seperti K1, dan menyimpan keputusan gagal karena error server pada percobaan pertama, lalu berhasil pada percobaan kedua.
  - K5: seperti K1, dan menyimpan keputusan lambat sehingga respons belum diterima sesudah `[Submit]` pada dialog diklik.
  - K6: seperti K1, dan jawaban server atas keputusan menyatakan pengajuan sudah diputuskan oleh pengguna DU-036-6.
  - K7: seperti K1, dan jawaban server atas keputusan menyatakan pengajuan dibatalkan otomatis oleh sistem.
  - K8: pengajuan DU-036-1 berisi aset DU-036-8, DU-036-3, dan DU-036-4 dalam grup Accordion `Laptop` dan DU-036-5 dalam grup Accordion `Office Desk`, approver berhak memutuskan, dan menyimpan koreksi berhasil.

## Test Steps

### Footer dan dialog Submit Approval dengan Decision campuran
1. Tampilkan Halaman Approval dengan kondisi K1
2. Pilih Decision `Return to Draft` pada baris `Laptop - 130`
3. Isi Reason pada baris `Laptop - 130` dengan `Photo is missing`
4. Pilih Decision `Reject` pada baris `Office Desk - 12`
5. Isi Reason pada baris `Office Desk - 12` dengan `Duplicate entry`
6. Verifikasi footer memuat tombol `[Cancel]`
7. Verifikasi footer memuat tombol `[Submit]`
8. Klik `[Submit]` di footer halaman
9. Verifikasi dialog `Submit Approval` tampil
10. Verifikasi bullet pada dialog memuat Registration ID pengajuan
11. Verifikasi ringkasan memuat jumlah Approve `2`
12. Verifikasi ringkasan memuat jumlah Return to Draft `1`
13. Verifikasi ringkasan memuat jumlah Reject `1`
14. Verifikasi ringkasan memuat jumlah koreksi `1`
15. Verifikasi pertanyaan konfirmasi `Are you sure you want to submit it?`
16. Verifikasi footer dialog memuat tombol `[Cancel]` dan `[Submit]`
17. Klik `[Cancel]` pada dialog `Submit Approval`
18. Verifikasi dialog `Submit Approval` tertutup

### Ringkasan jumlah pada Decision awal
19. Tampilkan Halaman Approval dengan kondisi K1
20. Klik `[Submit]` di footer halaman
21. Verifikasi ringkasan pada dialog `Submit Approval` memuat jumlah Approve `4`
22. Verifikasi ringkasan pada dialog `Submit Approval` memuat jumlah Return to Draft `0`
23. Verifikasi ringkasan pada dialog `Submit Approval` memuat jumlah Reject `0`
24. Verifikasi ringkasan pada dialog `Submit Approval` memuat jumlah koreksi `1`

### Keputusan berhasil dikirim
25. Tampilkan Halaman Approval dengan kondisi K1
26. Klik `[Submit]` di footer halaman
27. Klik `[Submit]` pada dialog `Submit Approval`
28. Verifikasi toast sukses `Success, registration request has been decided.`
29. Verifikasi dialog `Submit Approval` tertutup setelah keputusan berhasil

### Keputusan gagal karena error server
30. Tampilkan Halaman Approval dengan kondisi K2
31. Pilih Decision `Reject` pada baris `Office Desk - 12`
32. Isi Reason pada baris `Office Desk - 12` dengan `Duplicate entry`
33. Klik `[Submit]` di footer halaman
34. Klik `[Submit]` pada dialog `Submit Approval`
35. Verifikasi toast error `Error, failed to decide registration request.`
36. Verifikasi dialog `Submit Approval` tetap terbuka
37. Verifikasi tombol `[Submit]` pada dialog `Submit Approval` aktif lagi
38. Klik `[Cancel]` pada dialog `Submit Approval`
39. Verifikasi Decision pada baris `Office Desk - 12` tetap `Reject`
40. Verifikasi Reason pada baris `Office Desk - 12` tetap `Duplicate entry`

### Keputusan gagal karena koneksi terputus
41. Tampilkan Halaman Approval dengan kondisi K3
42. Pilih Decision `Reject` pada baris `Office Desk - 12`
43. Isi Reason pada baris `Office Desk - 12` dengan `Duplicate entry`
44. Klik `[Submit]` di footer halaman
45. Klik `[Submit]` pada dialog `Submit Approval`
46. Verifikasi toast error `Connection problem. Please try again.`
47. Verifikasi dialog `Submit Approval` tetap terbuka
48. Verifikasi tombol `[Submit]` pada dialog `Submit Approval` aktif lagi
49. Klik `[Cancel]` pada dialog `Submit Approval`
50. Verifikasi Decision pada baris `Office Desk - 12` tetap `Reject`
51. Verifikasi Reason pada baris `Office Desk - 12` tetap `Duplicate entry`

### Kirim ulang keputusan sesudah pulih berhasil sekali
52. Tampilkan Halaman Approval dengan kondisi K4
53. Klik `[Submit]` di footer halaman
54. Klik `[Submit]` pada dialog `Submit Approval`
55. Verifikasi toast error `Error, failed to decide registration request.`
56. Klik `[Submit]` pada dialog `Submit Approval`
57. Verifikasi toast sukses `Success, registration request has been decided.`
58. Verifikasi hanya satu toast sukses keputusan yang tampil

### Saving state saat keputusan dikirim
59. Tampilkan Halaman Approval dengan kondisi K5
60. Klik `[Submit]` di footer halaman
61. Klik `[Submit]` pada dialog `Submit Approval`
62. Verifikasi tombol `[Submit]` pada dialog `Submit Approval` menampilkan loading dan disabled
63. Verifikasi tombol `[Cancel]` pada dialog `Submit Approval` disabled
64. Klik `[Submit]` pada dialog `Submit Approval`
65. Respons keputusan diterima
66. Verifikasi hanya satu toast `Success, registration request has been decided.` tampil

### Pengajuan dibatalkan pihak lain saat halaman terbuka
67. Tampilkan Halaman Approval dengan kondisi K1
68. Pilih Decision `Reject` pada baris `Office Desk - 12`
69. Isi Reason pada baris `Office Desk - 12` dengan `Duplicate entry`
70. Pengajuan dibatalkan oleh `Hadi K` saat halaman Approval terbuka
71. Verifikasi dialog `Request Canceled` tampil
72. Verifikasi isi dialog `This request was canceled by Hadi K. Your decisions were not saved.`
73. Verifikasi dialog `Unsaved Changes` tidak tampil
74. Verifikasi dialog `Request Canceled` memuat tombol `[OK]`
75. Klik `[OK]`
76. Verifikasi dialog `Request Canceled` tertutup
77. Verifikasi antrean Approvals tampil

### Pengajuan sudah diputuskan pihak lain saat keputusan dikirim
78. Tampilkan Halaman Approval dengan kondisi K6
79. Klik `[Submit]` di footer halaman
80. Klik `[Submit]` pada dialog `Submit Approval`
81. Verifikasi dialog `Request Already Decided` tampil
82. Verifikasi isi dialog `This request was already decided by Agus P. Your decisions were not saved.`
83. Klik `[OK]`
84. Verifikasi dialog `Request Already Decided` tertutup
85. Verifikasi antrean Approvals tampil

### Pengajuan dibatalkan otomatis oleh sistem saat keputusan dikirim
86. Tampilkan Halaman Approval dengan kondisi K7
87. Klik `[Submit]` di footer halaman
88. Klik `[Submit]` pada dialog `Submit Approval`
89. Verifikasi dialog `Request Canceled` tampil
90. Verifikasi isi dialog `This request was canceled by the system. Your decisions were not saved.`

### Model wajib dipilih ulang setelah koreksi Brand memblokir Submit
91. Tampilkan Halaman Approval dengan kondisi K8
92. Klik `[Submit]` di footer halaman
93. Verifikasi pesan `Select Model again` tampil pada Model aset `Laptop - 128`
94. Verifikasi dialog `Submit Approval` tidak tampil
95. Klik nama `Laptop - 128`
96. Pilih Model `ThinkPad T14`
97. Klik `[Save correction]`
98. Klik `[Submit]` di footer halaman
99. Verifikasi dialog `Submit Approval` tampil setelah Model dipilih ulang
100. Verifikasi pesan `Select Model again` tidak tampil
