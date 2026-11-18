---
id: TC-FA-BORROW-E2E-036-entitas-suspended-expired-aksi-tulis
title: "Entitas Suspended atau Expired menolak setiap aksi tulis Borrow dan tetap membaca data"
layer: ui-e2e
priority: Medium
caseType: Negative
status: draft
sourceRules: [EB-AKS-7]
smoke: []
dependsOn: []
trace:
  EB-AKS-7: [6, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 32, 33, 35, 41, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 67, 68, 70, 76, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99, 101, 102, 103, 105]
anchor: []
coverage:
  web: automated
---

# Entitas Suspended atau Expired menolak setiap aksi tulis Borrow dan tetap membaca data

## Prerequisites
- Aktor: Total Control; operator Admin Console `Operator Admin Console {runId}` mengubah status entitas dari luar tenant.
- Layar awal: halaman utama aplikasi Fixed Asset.
- Data:
  - DU-036-1: Entitas `Samudra Logistik {runId}`, level Feature Suite Borrowing `Full`, status awal Active.
  - DU-036-2: User `Maya Putri {runId}`, role Total Control, cakupan seluruh client, aktif.
  - DU-036-3: User `Operator Admin Console {runId}`, operator Admin Console di luar tenant, aktif.
  - DU-036-4: Karyawan `Rudi Hartono {runId}`, aktif, Home Group `Head Office {runId}`.
  - DU-036-5: Group `Head Office {runId}`.
  - DU-036-6: Aset `Laptop Lenovo T14 {runId}`, Group `Head Office {runId}`, status Available.
  - DU-036-7: BRW berstatus Waiting for Handover, Group `Head Office {runId}`, Borrower `Rudi Hartono {runId}`, aset `Laptop Dell Latitude 5420 {runId}`, Duration `3 days`, Purpose `Kunjungan klien`, Requested By `Maya Putri {runId}`.
  - DU-036-8: BRW berstatus Borrowed, Group `Head Office {runId}`, Borrower `Rudi Hartono {runId}`, aset `Toyota Avanza {runId}`, Duration `5 days`, Purpose `Survei lokasi`, Requested By `Maya Putri {runId}`.
  - DU-036-9: BRW berstatus Waiting for Approval yang approval-nya dirutekan ke `Maya Putri {runId}` (alasan `No eligible approver`), Group `Head Office {runId}`, Borrower `Rudi Hartono {runId}`, aset `Meeting Mic Set {runId}`, Duration `2 days`, Purpose `Rapat tahunan`, Requested By `Maya Putri {runId}`.
  - DU-036-10: Draft milik Borrower `Rudi Hartono {runId}`, berisi aset `Scanner Epson DS-530 {runId}` (Group `Head Office {runId}`), Total Asset `1`, Modified By `Maya Putri {runId}`.
  - DU-036-11: Percobaan Create BRW untuk Borrower `Rudi Hartono {runId}`, aset `Laptop Lenovo T14 {runId}`, Duration `2`, Purpose `Kunjungan tamu`.
  - DU-036-12: Percobaan ubah Draft DU-036-10: Duration aset `Scanner Epson DS-530 {runId}` menjadi `4`.
  - DU-036-13: Percobaan Request Extension untuk aset `Toyota Avanza {runId}`: Extend By `2 days`, Reason `Pekerjaan belum selesai`.
- Kondisi:
  - Spec ini memakai entitas khusus `Samudra Logistik {runId}` yang tidak dipakai spec lain.
  - Level Feature Suite Borrowing entitas itu bernilai `Full`.
  - Akun `Maya Putri {runId}` aktif dan kredensialnya disediakan fase 2.

## Test Steps

### Entitas Suspended: modul terbuka, data terbaca, dan setiap aksi tulis ditolak
1. Operator Admin Console `Operator Admin Console {runId}` mengubah status entitas `Samudra Logistik {runId}` menjadi `Suspended`
2. Masuk sebagai Total Control `Maya Putri {runId}`
3. Muat ulang halaman
4. Klik menu `Transactions > Borrow`
5. Ketik Search `{runId}`, tekan Enter
6. Verifikasi halaman Borrow terbuka tanpa gerbang akses dan tanpa redirect pada entitas `Suspended`
7. Verifikasi BRW milik DU-036-7 tampil di tabel pada entitas `Suspended`
8. Kirim Create BRW dengan nilai dari DU-036-11
9. Verifikasi toast `Changes can't be saved while this workspace is suspended or expired.` tampil
10. Kirim Save Draft pada Draft milik DU-036-10 dengan nilai dari DU-036-12
11. Verifikasi toast `Changes can't be saved while this workspace is suspended or expired.` tampil
12. Kirim Delete atas Draft milik DU-036-10
13. Verifikasi toast `Changes can't be saved while this workspace is suspended or expired.` tampil
14. Kirim Cancel Borrow atas BRW milik DU-036-7
15. Verifikasi toast `Changes can't be saved while this workspace is suspended or expired.` tampil
16. Kirim Hand Over atas BRW milik DU-036-7
17. Verifikasi toast `Changes can't be saved while this workspace is suspended or expired.` tampil
18. Kirim Remind Borrower atas BRW milik DU-036-7
19. Verifikasi toast `Changes can't be saved while this workspace is suspended or expired.` tampil
20. Kirim Request Extension atas BRW milik DU-036-8 dengan nilai dari DU-036-13
21. Verifikasi toast `Changes can't be saved while this workspace is suspended or expired.` tampil
22. Kirim Return atas BRW milik DU-036-8
23. Verifikasi toast `Changes can't be saved while this workspace is suspended or expired.` tampil
24. Kirim Report Damaged atas aset `Toyota Avanza {runId}`
25. Verifikasi toast `Changes can't be saved while this workspace is suspended or expired.` tampil
26. Kirim Report Missing atas aset `Toyota Avanza {runId}`
27. Verifikasi toast `Changes can't be saved while this workspace is suspended or expired.` tampil
28. Kirim keputusan `Approve` atas aset `Meeting Mic Set {runId}` milik DU-036-9
29. Verifikasi toast `Changes can't be saved while this workspace is suspended or expired.` tampil
30. Ketik Search `{runId}`, tekan Enter
31. Verifikasi BRW milik DU-036-7 masih berstatus `Waiting for Handover`
32. Verifikasi BRW milik DU-036-8 masih berstatus `Borrowed`
33. Verifikasi BRW milik DU-036-9 masih berstatus `Waiting for Approval`
34. Klik tab `Drafts`
35. Verifikasi Draft milik DU-036-10 masih tampil dengan Total Asset `1`
36. Klik tab `Transactions`

### Entitas Expired: modul terbuka, data terbaca, dan setiap aksi tulis ditolak
37. Operator Admin Console `Operator Admin Console {runId}` mengubah status entitas `Samudra Logistik {runId}` menjadi `Expired`
38. Muat ulang halaman
39. Klik menu `Transactions > Borrow`
40. Ketik Search `{runId}`, tekan Enter
41. Verifikasi halaman Borrow terbuka tanpa gerbang akses dan tanpa redirect pada entitas `Expired`
42. Verifikasi BRW milik DU-036-7 tampil di tabel pada entitas `Expired`
43. Kirim Create BRW dengan nilai dari DU-036-11
44. Verifikasi toast `Changes can't be saved while this workspace is suspended or expired.` tampil
45. Kirim Save Draft pada Draft milik DU-036-10 dengan nilai dari DU-036-12
46. Verifikasi toast `Changes can't be saved while this workspace is suspended or expired.` tampil
47. Kirim Delete atas Draft milik DU-036-10
48. Verifikasi toast `Changes can't be saved while this workspace is suspended or expired.` tampil
49. Kirim Cancel Borrow atas BRW milik DU-036-7
50. Verifikasi toast `Changes can't be saved while this workspace is suspended or expired.` tampil
51. Kirim Hand Over atas BRW milik DU-036-7
52. Verifikasi toast `Changes can't be saved while this workspace is suspended or expired.` tampil
53. Kirim Remind Borrower atas BRW milik DU-036-7
54. Verifikasi toast `Changes can't be saved while this workspace is suspended or expired.` tampil
55. Kirim Request Extension atas BRW milik DU-036-8 dengan nilai dari DU-036-13
56. Verifikasi toast `Changes can't be saved while this workspace is suspended or expired.` tampil
57. Kirim Return atas BRW milik DU-036-8
58. Verifikasi toast `Changes can't be saved while this workspace is suspended or expired.` tampil
59. Kirim Report Damaged atas aset `Toyota Avanza {runId}`
60. Verifikasi toast `Changes can't be saved while this workspace is suspended or expired.` tampil
61. Kirim Report Missing atas aset `Toyota Avanza {runId}`
62. Verifikasi toast `Changes can't be saved while this workspace is suspended or expired.` tampil
63. Kirim keputusan `Approve` atas aset `Meeting Mic Set {runId}` milik DU-036-9
64. Verifikasi toast `Changes can't be saved while this workspace is suspended or expired.` tampil
65. Ketik Search `{runId}`, tekan Enter
66. Verifikasi BRW milik DU-036-7 masih berstatus `Waiting for Handover`
67. Verifikasi BRW milik DU-036-8 masih berstatus `Borrowed`
68. Verifikasi BRW milik DU-036-9 masih berstatus `Waiting for Approval`
69. Klik tab `Drafts`
70. Verifikasi Draft milik DU-036-10 masih tampil dengan Total Asset `1`
71. Klik tab `Transactions`

### Entitas Grace: modul terbuka, data terbaca, dan setiap aksi tulis ditolak
72. Operator Admin Console `Operator Admin Console {runId}` mengubah status entitas `Samudra Logistik {runId}` menjadi `Expired (Grace)`
73. Muat ulang halaman
74. Klik menu `Transactions > Borrow`
75. Ketik Search `{runId}`, tekan Enter
76. Verifikasi halaman Borrow terbuka tanpa gerbang akses dan tanpa redirect pada entitas `Expired (Grace)`
77. Verifikasi BRW milik DU-036-7 tampil di tabel pada entitas `Expired (Grace)`
78. Kirim Create BRW dengan nilai dari DU-036-11
79. Verifikasi toast `Changes can't be saved while this workspace is suspended or expired.` tampil
80. Kirim Save Draft pada Draft milik DU-036-10 dengan nilai dari DU-036-12
81. Verifikasi toast `Changes can't be saved while this workspace is suspended or expired.` tampil
82. Kirim Delete atas Draft milik DU-036-10
83. Verifikasi toast `Changes can't be saved while this workspace is suspended or expired.` tampil
84. Kirim Cancel Borrow atas BRW milik DU-036-7
85. Verifikasi toast `Changes can't be saved while this workspace is suspended or expired.` tampil
86. Kirim Hand Over atas BRW milik DU-036-7
87. Verifikasi toast `Changes can't be saved while this workspace is suspended or expired.` tampil
88. Kirim Remind Borrower atas BRW milik DU-036-7
89. Verifikasi toast `Changes can't be saved while this workspace is suspended or expired.` tampil
90. Kirim Request Extension atas BRW milik DU-036-8 dengan nilai dari DU-036-13
91. Verifikasi toast `Changes can't be saved while this workspace is suspended or expired.` tampil
92. Kirim Return atas BRW milik DU-036-8
93. Verifikasi toast `Changes can't be saved while this workspace is suspended or expired.` tampil
94. Kirim Report Damaged atas aset `Toyota Avanza {runId}`
95. Verifikasi toast `Changes can't be saved while this workspace is suspended or expired.` tampil
96. Kirim Report Missing atas aset `Toyota Avanza {runId}`
97. Verifikasi toast `Changes can't be saved while this workspace is suspended or expired.` tampil
98. Kirim keputusan `Approve` atas aset `Meeting Mic Set {runId}` milik DU-036-9
99. Verifikasi toast `Changes can't be saved while this workspace is suspended or expired.` tampil
100. Ketik Search `{runId}`, tekan Enter
101. Verifikasi BRW milik DU-036-7 masih berstatus `Waiting for Handover`
102. Verifikasi BRW milik DU-036-8 masih berstatus `Borrowed`
103. Verifikasi BRW milik DU-036-9 masih berstatus `Waiting for Approval`
104. Klik tab `Drafts`
105. Verifikasi Draft milik DU-036-10 masih tampil dengan Total Asset `1`
106. Klik tab `Transactions`
