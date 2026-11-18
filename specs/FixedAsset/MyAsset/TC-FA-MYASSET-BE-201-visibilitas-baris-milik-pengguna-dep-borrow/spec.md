---
id: TC-FA-MYASSET-BE-201-visibilitas-baris-milik-pengguna-dep-borrow
title: "Data My Asset hanya memuat baris milik pengguna atau yang PIC-nya pengguna"
layer: be-e2e
priority: Medium
caseType: Negative
status: ready-for-automation
sourceRules: ["§1.2#r23", "§1.2#r24", "§1.2#r25", "§1.2#r26", "§1.2#r45", "§2.2#r1", "§2.2#r2", "§2.2#r3", "§Dialog aksi baris (tab Borrowed dan Assigned)#r6", "§9.4.2#r34", "§9.4.3#b1", "§9.4.3#b8"]
smoke: []
dependsOn: ["Transactions > Borrow: pinjaman, approval, sesi Handover, Extension, dan Return oleh Aktor Borrow", "Transactions > Assignment: penugasan, approval, sesi Handover, Change PIC, dan Unassign oleh Aktor Assignment", "Users: Borrower tanpa akun beserta PIC-nya, dan User Detail > User Log"]
trace:
  "§1.2#r23": [2, 8]
  "§1.2#r24": 23
  "§1.2#r25": 33
  "§1.2#r26": [4, 9, 45, 46, 48, 49, 51, 52, 54, 55, 57, 58]
  "§1.2#r45": [10, 43, 64, 67]
  "§2.2#r1": [2, 5, 12, 14, 16, 23, 26, 28, 60, 69]
  "§2.2#r2": [8, 10, 17, 35, 37, 42, 63, 64, 66, 67]
  "§2.2#r3": 3
  "§Dialog aksi baris (tab Borrowed dan Assigned)#r6": [21, 31, 40, 72, 73, 75, 76, 78, 79]
  "§9.4.2#r34": [13, 70]
  "§9.4.3#b1": [4, 5, 6, 9, 10, 14, 24, 43, 61, 66, 67]
  "§9.4.3#b8": [18, 19, 29, 38]
owner: BE
---

# Data My Asset hanya memuat baris milik pengguna atau yang PIC-nya pengguna

## Prerequisites
- Aktor: Borrower dan Assignee Employee ber-akun (Sari, Tono, Hendra, Maya, Dimas, Lestari, Fajar, Rudi), PIC Borrower (Wulan), dan PIC Division (Budi). Aktor Borrow dan Aktor Assignment hanya menyiapkan transaksinya.
- Data:
  - DU-201-1: User `Hendra Wijaya {runId}`, role Total Control, cakupan seluruh Group entitas aktor.
  - DU-201-2: User `Maya Anggraini {runId}`, role Group Manager, cakupan Group `Head Office` beserta Group di bawahnya.
  - DU-201-3: User `Sari Kusuma {runId}`, role Asset Admin, cakupan Group `Head Office` beserta Group di bawahnya, termasuk `Branch Surabaya`.
  - DU-201-4: User `Dimas Prasetyo {runId}`, role Approver, cakupan Group `Head Office` beserta Group di bawahnya.
  - DU-201-5: User `Lestari Dewi {runId}`, role Monitoring & Report, cakupan Group `Head Office` beserta Group di bawahnya.
  - DU-201-6: User `Fajar Nugroho {runId}`, role Read Only, cakupan hanya Group `Branch Surabaya`.
  - DU-201-7: Pinjaman Hendra, aset `Laptop Dell Latitude 5420 - 71 {runId}`, Group `Head Office`, status `Borrowed`.
  - DU-201-8: Pinjaman Maya, aset `Laptop Dell Latitude 5420 - 72 {runId}`, Group `Head Office`, status `Borrowed`.
  - DU-201-9: Pinjaman Sari, aset `Laptop Dell Latitude 5420 - 73 {runId}`, Group `Head Office`, status `Borrowed`, Purchase Price `12500000`, Current Value `9800000`.
  - DU-201-10: Pinjaman Dimas, aset `Laptop Dell Latitude 5420 - 74 {runId}`, Group `Head Office`, status `Borrowed`.
  - DU-201-11: Pinjaman Lestari, aset `Laptop Dell Latitude 5420 - 75 {runId}`, Group `Head Office`, status `Borrowed`.
  - DU-201-12: Pinjaman Fajar, aset `Laptop Dell Latitude 5420 - 76 {runId}`, Group `Branch Surabaya`, status `Borrowed`.
  - DU-201-13: Pinjaman Sari yang sudah dikembalikan, aset `Laptop Dell Latitude 5420 - 81 {runId}`, Group `Head Office`, status `Returned`; sesudah pinjaman itu Returned, aset berstatus `Disposed`.
  - DU-201-14: Pinjaman Sari dengan sesi Handover berjalan yang menunggu konfirmasi, aset `Projector Epson EB-X06 - 82 {runId}`, Group `Head Office`, status `Waiting for Handover`.
  - DU-201-15: Penugasan Sari, aset `Monitor Dell P2422H - 83 {runId}`, Group `Head Office`, status `Assigned`.
  - DU-201-16: Penugasan Sari dengan sesi Handover berjalan yang menunggu konfirmasi, aset `Laptop Lenovo ThinkPad T14 - 84 {runId}`, Group `Head Office`, status `Waiting for Handover`.
  - DU-201-17: Borrower tanpa akun `Anton Saputra {runId}`, PIC-nya Wulan.
  - DU-201-18: User `Wulan Pratiwi {runId}`, role Read Only, cakupan Group `Head Office` beserta Group di bawahnya.
  - DU-201-19: Pinjaman Anton, aset `Projector Epson EB-X06 - 85 {runId}`, Group `Head Office`, status `Borrowed`.
  - DU-201-20: Pinjaman Anton yang sudah dikembalikan, aset `Camera Canon EOS R6 - 86 {runId}`, Group `Head Office`, status `Returned`.
  - DU-201-21: Pinjaman Anton dengan sesi Handover berjalan yang menunggu konfirmasi, aset `Tripod Manfrotto 190 - 87 {runId}`, Group `Head Office`, status `Waiting for Handover`.
  - DU-201-22: Division `Finance {runId}`, PIC pada penugasan DU-201-26, DU-201-27, dan DU-201-28 adalah Budi, anggotanya Tono.
  - DU-201-23: User `Budi Santoso {runId}`, role Read Only, cakupan Group `Head Office` beserta Group di bawahnya.
  - DU-201-24: User `Tono Wibowo {runId}`, anggota Division `Finance {runId}` yang bukan PIC, role Asset Admin, cakupan Group `Head Office` beserta Group di bawahnya.
  - DU-201-25: Penugasan Tono, aset `Monitor Dell P2422H - 92 {runId}`, Group `Head Office`, status `Assigned`.
  - DU-201-26: Penugasan Division `Finance {runId}`, aset `Printer HP M404 - 88 {runId}`, Group `Branch Surabaya`, status `Assigned`.
  - DU-201-27: Penugasan Division `Finance {runId}` yang sudah ditutup, aset `Printer HP M404 - 89 {runId}`, Group `Branch Surabaya`, status `Unassigned`.
  - DU-201-28: Penugasan Division `Finance {runId}` dengan sesi Handover berjalan yang menunggu konfirmasi, aset `Printer HP M404 - 90 {runId}`, Group `Branch Surabaya`, status `Waiting for Handover`.
  - DU-201-29: Pinjaman Rudi, Borrower di entitas lain, user `Rudi Hermawan {runId}`, aset `Camera Sony A7 III - 91 {runId}`, status `Borrowed`.
  - DU-201-30: Penugasan Sari yang sudah ditutup, aset `Monitor Dell P2422H - 93 {runId}`, Group `Head Office`, status `Unassigned`.
  - DU-201-31: Pinjaman Sari yang sudah dikembalikan, aset `Laptop Dell Latitude 5420 - 94 {runId}`, Group `Head Office`, status `Returned`; sesudah pinjaman itu Returned, asetnya dihapus.

## Test Steps

### Baris milik Borrower dan Assignee sendiri tampil bagi pemiliknya
1. Sari meminta data tab Borrowed
2. Verifikasi data memuat baris pinjaman aset `Laptop Dell Latitude 5420 - 73 {runId}` milik Sari
3. Verifikasi baris aset `Laptop Dell Latitude 5420 - 73 {runId}` tidak memuat nilai aset `9800000` maupun data pembelian `12500000`
4. Verifikasi data tidak memuat baris pinjaman `Laptop Dell Latitude 5420 - 76 {runId}` milik Fajar, walaupun Group asetnya berada dalam cakupan Sari
5. Verifikasi data tidak memuat baris pinjaman `Projector Epson EB-X06 - 85 {runId}` milik Anton, Borrower tanpa akun yang PIC-nya Wulan
6. Verifikasi data tidak memuat baris pinjaman `Camera Sony A7 III - 91 {runId}` milik Rudi di entitas lain
7. Sari meminta data tab Assigned
8. Verifikasi data memuat baris penugasan aset `Monitor Dell P2422H - 83 {runId}` milik Sari
9. Verifikasi data tidak memuat baris penugasan aset `Monitor Dell P2422H - 92 {runId}` milik Tono
10. Verifikasi data tidak memuat baris penugasan Division `Printer HP M404 - 88 {runId}`, karena Sari bukan PIC-nya
11. Sari meminta data tab History
12. Verifikasi data memuat baris pinjaman aset `Laptop Dell Latitude 5420 - 81 {runId}` berstatus `Returned`
13. Verifikasi baris aset `Laptop Dell Latitude 5420 - 81 {runId}` tetap tampil walaupun asetnya sudah berstatus `Disposed`
14. Verifikasi data tidak memuat baris riwayat `Camera Canon EOS R6 - 86 {runId}` milik Anton
15. Sari meminta data tab Task
16. Verifikasi data memuat Task Confirm Handover pinjaman untuk aset `Projector Epson EB-X06 - 82 {runId}`
17. Verifikasi data memuat Task Confirm Handover penugasan untuk aset `Laptop Lenovo ThinkPad T14 - 84 {runId}`
18. Verifikasi data tidak memuat Task Confirm Handover pinjaman untuk aset `Tripod Manfrotto 190 - 87 {runId}` milik Anton, yang PIC-nya Wulan
19. Verifikasi data tidak memuat Task Confirm Handover penugasan untuk aset `Printer HP M404 - 90 {runId}` milik Division `Finance {runId}`, yang PIC-nya Budi
20. Sari meminta Borrow Log baris pinjaman aset `Laptop Dell Latitude 5420 - 73 {runId}`
21. Verifikasi Borrow Log tersedia dan memuat riwayat baris pinjaman aset `Laptop Dell Latitude 5420 - 73 {runId}`

### Baris atas nama Borrower tanpa akun hanya tampil bagi PIC-nya
22. Wulan meminta data tab Borrowed
23. Verifikasi data memuat baris pinjaman aset `Projector Epson EB-X06 - 85 {runId}` milik Anton
24. Verifikasi data tidak memuat baris pinjaman aset `Laptop Dell Latitude 5420 - 73 {runId}` milik Sari
25. Wulan meminta data tab History
26. Verifikasi data memuat baris riwayat aset `Camera Canon EOS R6 - 86 {runId}` milik Anton
27. Wulan meminta data tab Task
28. Verifikasi data memuat Task Confirm Handover pinjaman untuk aset `Tripod Manfrotto 190 - 87 {runId}` milik Anton
29. Verifikasi data tidak memuat Task Confirm Handover pinjaman untuk aset `Projector Epson EB-X06 - 82 {runId}` milik Sari
30. Wulan meminta Borrow Log baris pinjaman aset `Projector Epson EB-X06 - 85 {runId}`
31. Verifikasi Borrow Log tersedia dan memuat riwayat baris pinjaman aset `Projector Epson EB-X06 - 85 {runId}` atas nama Anton

### Baris Division hanya tampil bagi PIC-nya
32. Budi meminta data tab Assigned
33. Verifikasi data memuat baris penugasan Division `Finance {runId}` untuk aset `Printer HP M404 - 88 {runId}`
34. Budi meminta data tab History
35. Verifikasi data memuat baris riwayat penugasan Division `Finance {runId}` untuk aset `Printer HP M404 - 89 {runId}`
36. Budi meminta data tab Task
37. Verifikasi data memuat Task Confirm Handover penugasan atas nama Division `Finance {runId}` untuk aset `Printer HP M404 - 90 {runId}`
38. Verifikasi data tidak memuat Task Confirm Handover penugasan untuk aset `Laptop Lenovo ThinkPad T14 - 84 {runId}` milik Sari
39. Budi meminta Assignment Log baris penugasan aset `Printer HP M404 - 88 {runId}`
40. Verifikasi Assignment Log tersedia dan memuat riwayat baris penugasan aset `Printer HP M404 - 88 {runId}` atas nama Division `Finance {runId}`
41. Tono meminta data tab Assigned
42. Verifikasi data memuat baris penugasan aset `Monitor Dell P2422H - 92 {runId}` milik Tono
43. Verifikasi data tidak memuat baris penugasan Division `Printer HP M404 - 88 {runId}`, karena Tono anggota Division `Finance {runId}` yang bukan PIC-nya

### Pengguna dengan peran apa pun hanya melihat pinjamannya sendiri
44. Hendra meminta data tab Borrowed
45. Verifikasi data memuat baris pinjaman aset `Laptop Dell Latitude 5420 - 71 {runId}` milik Hendra
46. Verifikasi data tidak memuat baris pinjaman aset `Laptop Dell Latitude 5420 - 72 {runId}` milik Maya
47. Maya meminta data tab Borrowed
48. Verifikasi data memuat baris pinjaman aset `Laptop Dell Latitude 5420 - 72 {runId}` milik Maya
49. Verifikasi data tidak memuat baris pinjaman aset `Laptop Dell Latitude 5420 - 73 {runId}` milik Sari
50. Dimas meminta data tab Borrowed
51. Verifikasi data memuat baris pinjaman aset `Laptop Dell Latitude 5420 - 74 {runId}` milik Dimas
52. Verifikasi data tidak memuat baris pinjaman aset `Laptop Dell Latitude 5420 - 75 {runId}` milik Lestari
53. Lestari meminta data tab Borrowed
54. Verifikasi data memuat baris pinjaman aset `Laptop Dell Latitude 5420 - 75 {runId}` milik Lestari
55. Verifikasi data tidak memuat baris pinjaman aset `Laptop Dell Latitude 5420 - 71 {runId}` milik Hendra
56. Fajar meminta data tab Borrowed
57. Verifikasi data memuat baris pinjaman aset `Laptop Dell Latitude 5420 - 76 {runId}` milik Fajar
58. Verifikasi data tidak memuat baris pinjaman aset `Laptop Dell Latitude 5420 - 73 {runId}` milik Sari, yang cakupannya berbeda dari cakupan Fajar

### Baris milik Borrower di entitas lain tidak tampil di entitas aktor
59. Rudi meminta data tab Borrowed
60. Verifikasi data memuat baris pinjaman aset `Camera Sony A7 III - 91 {runId}` milik Rudi
61. Verifikasi data tidak memuat baris pinjaman aset `Laptop Dell Latitude 5420 - 73 {runId}` milik Sari, yang berada di entitas aktor lain

### Riwayat penugasan tampil bagi Assignee Employee dan tidak bagi yang lain
62. Sari meminta data tab History
63. Verifikasi data memuat baris riwayat penugasan aset `Monitor Dell P2422H - 93 {runId}` milik Sari
64. Verifikasi data tidak memuat baris riwayat penugasan Division `Printer HP M404 - 89 {runId}`, karena Sari bukan PIC-nya
65. Tono meminta data tab History
66. Verifikasi data tidak memuat baris riwayat penugasan aset `Monitor Dell P2422H - 93 {runId}` milik Sari
67. Verifikasi data tidak memuat baris riwayat penugasan Division `Printer HP M404 - 89 {runId}`, karena Tono anggota Division `Finance {runId}` yang bukan PIC-nya

### Baris History tetap tampil walaupun asetnya dihapus
68. Sari meminta data tab History
69. Verifikasi data memuat baris pinjaman aset `Laptop Dell Latitude 5420 - 94 {runId}` berstatus `Returned`
70. Verifikasi baris aset `Laptop Dell Latitude 5420 - 94 {runId}` tetap tampil walaupun asetnya sudah dihapus

### Borrow Log dan Assignment Log baris milik orang lain ditolak
71. Sari meminta Borrow Log baris pinjaman aset `Projector Epson EB-X06 - 85 {runId}` milik Anton, yang PIC-nya Wulan
72. Verifikasi permintaan Borrow Log ditolak server
73. Verifikasi penolakan tidak membuka riwayat baris pinjaman aset `Projector Epson EB-X06 - 85 {runId}`
74. Tono meminta Assignment Log baris penugasan Division `Printer HP M404 - 88 {runId}`, yang PIC-nya Budi
75. Verifikasi permintaan Assignment Log ditolak server
76. Verifikasi penolakan tidak membuka riwayat baris penugasan aset `Printer HP M404 - 88 {runId}`
77. Sari meminta Assignment Log baris penugasan aset `Monitor Dell P2422H - 92 {runId}` milik Tono
78. Verifikasi permintaan Assignment Log ditolak server
79. Verifikasi penolakan tidak membuka riwayat baris penugasan aset `Monitor Dell P2422H - 92 {runId}`
