---
id: TC-FA-MYASSET-BE-203-confirm-handover-pinjaman-aturan-server-dep-borrow
title: "Aturan server Confirm Handover pinjaman: konfirmasi pertama berlaku, batas Expires At, dan aset tidak tercentang"
layer: be-e2e
priority: Critical
caseType: Negative
status: ready-for-automation
sourceRules: ["FI-05", "T-MYA-01", "V-03", "§4.2.5#p3", "§9.2#b3", "§9.2#r2", "§9.2#r3", "§9.4.2#r35", "§9.4.2#r38", "§9.4.2#r40", "§9.4.2#r88", "§9.6#r1", "EB-CON-3", "EB-EDG-1"]
smoke: []
dependsOn: ["Transactions > Borrow: pinjaman, approval, sesi Handover, Extension, dan Return oleh Aktor Borrow"]
trace:
  "FI-05": [63, 65]
  "T-MYA-01": [51, 55, 58]
  "V-03": [2, 4, 10, 14, 18, 20, 24, 28, 32, 34, 36, 42, 51, 58, 60, 71]
  "§4.2.5#p3": [63, 65]
  "§9.2#b3": [42, 44, 48]
  "§9.2#r2": [4, 18, 22, 24, 30, 34, 38, 71]
  "§9.2#r3": [14, 20, 28, 36]
  "§9.4.2#r35": [20, 42, 51]
  "§9.4.2#r38": [16, 22, 44, 53]
  "§9.4.2#r40": [10, 20, 28]
  "§9.4.2#r88": 51
  "§9.6#r1": [6, 8, 12, 26, 46, 62, 67, 73, 75, 77]
  "EB-CON-3": [14, 20, 28, 36, 42]
  "EB-EDG-1": [10, 12]
owner: BE
---

# Aturan server Confirm Handover pinjaman: konfirmasi pertama berlaku, batas Expires At, dan aset tidak tercentang

## Prerequisites
- Aktor: Maya (Borrower), Wulan (PIC Borrower atas nama Anton), dan Gita (Aktor Borrow yang menyerahkan aset, mengonfirmasi lewat perangkat admin, dan menekan `Cancel Request`).
- Data:
  - DU-203-1: User `Maya Anggraini {runId}`, role Read Only, cakupan Group `Head Office` beserta Group di bawahnya, Borrower pada DU-203-5 sampai DU-203-13.
  - DU-203-2: User `Gita Permata {runId}`, role Asset Admin, cakupan Group `Head Office` beserta Group di bawahnya, Aktor Borrow Group `Head Office`.
  - DU-203-3: Borrower tanpa akun `Anton Saputra {runId}`, PIC-nya Wulan, Borrower pada DU-203-8.
  - DU-203-4: User `Wulan Pratiwi {runId}`, role Read Only, cakupan Group `Head Office` beserta Group di bawahnya, PIC Anton.
  - DU-203-5: Pinjaman Maya dengan sesi Handover berjalan yang menunggu konfirmasi, aset `Laptop Dell Latitude 5420 - 31 {runId}`, Group `Head Office`, status `Waiting for Handover`, jendela konfirmasi belum habis.
  - DU-203-6: Pinjaman Maya dengan sesi Handover berjalan yang menunggu konfirmasi, aset `Laptop Dell Latitude 5420 - 32 {runId}`, Group `Head Office`, status `Waiting for Handover`, jendela konfirmasi belum habis.
  - DU-203-7: Pinjaman Maya dengan sesi Handover berjalan yang menunggu konfirmasi, aset `Laptop Dell Latitude 5420 - 33 {runId}`, Group `Head Office`, status `Waiting for Handover`, jendela konfirmasi belum habis.
  - DU-203-8: Pinjaman Anton dengan sesi Handover berjalan yang menunggu konfirmasi, aset `Laptop Dell Latitude 5420 - 34 {runId}`, Group `Head Office`, status `Waiting for Handover`, jendela konfirmasi belum habis.
  - DU-203-9: Pinjaman Maya dengan sesi Handover berjalan yang menunggu konfirmasi, aset `Laptop Dell Latitude 5420 - 35 {runId}`, Group `Head Office`, status `Waiting for Handover`, jendela konfirmasi belum habis.
  - DU-203-10: Pinjaman Maya dengan sesi Handover berjalan yang menunggu konfirmasi, aset `Laptop Dell Latitude 5420 - 36 {runId}`, Group `Head Office`, status `Waiting for Handover`, Expires At sesi: T0 + lama jendela konfirmasi, dengan T0 waktu sesi dimulai; sesi ini dimulai lebih dulu daripada sesi DU-203-11.
  - DU-203-11: Pinjaman Maya dengan sesi Handover berjalan yang menunggu konfirmasi, aset `Laptop Dell Latitude 5420 - 37 {runId}`, Group `Head Office`, status `Waiting for Handover`, Expires At sesi: T0 + lama jendela konfirmasi, dengan T0 waktu sesi dimulai, paling sedikit 1 menit sesudah sesi DU-203-10 dimulai.
  - DU-203-12: Pinjaman Maya dengan satu sesi Handover berjalan berisi tiga aset: `Projector Epson EB-X06 - 38 {runId}`, `Laptop Dell Latitude 5420 - 39 {runId}`, dan `Meeting Mic Set - 40 {runId}`, Group `Head Office`, ketiganya berstatus `Waiting for Handover`, Expires At sesi: T0 + lama jendela konfirmasi, dengan T0 waktu sesi dimulai, paling sedikit 1 menit sesudah sesi DU-203-11 dimulai, sehingga Expires At sesi lebih akhir daripada waktu pada langkah 56.
  - DU-203-13: Pinjaman Maya dengan sesi Handover berjalan yang menunggu konfirmasi, aset `Laptop Dell Latitude 5420 - 41 {runId}`, Group `Head Office`, status `Waiting for Handover`, Expires At sesi: T0 + lama jendela konfirmasi, dengan T0 waktu sesi dimulai, paling sedikit 1 menit sesudah sesi DU-203-11 dimulai, sehingga Expires At sesi lebih akhir daripada waktu pada langkah 56.

## Test Steps

### Konfirmasi Borrower diterima, konfirmasi kedua oleh Borrower dan perangkat admin ditolak
1. Maya meminta data tab Task
2. Verifikasi data memuat Task Confirm Handover untuk aset `Laptop Dell Latitude 5420 - 31 {runId}`
3. Maya mengirim Confirm Handover untuk sesi DU-203-5 dengan aset `Laptop Dell Latitude 5420 - 31 {runId}` tercentang
4. Verifikasi konfirmasi diterima server
5. Maya meminta data tab Borrowed
6. Verifikasi baris pinjaman aset `Laptop Dell Latitude 5420 - 31 {runId}` berstatus `Borrowed`
7. Maya meminta Borrow Log baris pinjaman aset `Laptop Dell Latitude 5420 - 31 {runId}`
8. Verifikasi Borrow Log memuat satu node `Handed over`
9. Maya mengirim Confirm Handover kedua untuk sesi DU-203-5 dengan aset `Laptop Dell Latitude 5420 - 31 {runId}` tercentang
10. Verifikasi konfirmasi kedua ditolak server karena sesi sudah dikonfirmasi
11. Maya meminta Borrow Log baris pinjaman aset `Laptop Dell Latitude 5420 - 31 {runId}`
12. Verifikasi Borrow Log tetap memuat satu node `Handed over`
13. Gita mengonfirmasi sesi DU-203-5 lewat `Confirm on This Device`
14. Verifikasi konfirmasi dari perangkat admin ditolak server karena sesi sudah dikonfirmasi lewat cara lain
15. Maya meminta data tab Borrowed
16. Verifikasi baris pinjaman aset `Laptop Dell Latitude 5420 - 31 {runId}` tetap berstatus `Borrowed`

### Konfirmasi dari perangkat admin yang masuk lebih dulu berlaku
17. Gita mengonfirmasi sesi DU-203-6 lewat `Confirm on This Device` dengan aset `Laptop Dell Latitude 5420 - 32 {runId}` tercentang
18. Verifikasi konfirmasi dari perangkat admin diterima server
19. Maya mengirim Confirm Handover untuk sesi DU-203-6 dengan aset `Laptop Dell Latitude 5420 - 32 {runId}` tercentang
20. Verifikasi konfirmasi Maya ditolak server karena sesi sudah dikonfirmasi lewat cara lain
21. Maya meminta data tab Borrowed
22. Verifikasi baris pinjaman aset `Laptop Dell Latitude 5420 - 32 {runId}` berstatus `Borrowed` sebagai hasil konfirmasi dari perangkat admin

### Konfirmasi lewat Accept yang masuk lebih dulu berlaku
23. Maya mengonfirmasi sesi DU-203-7 lewat Accept
24. Verifikasi konfirmasi lewat Accept diterima server
25. Maya meminta data tab Task
26. Verifikasi data tidak memuat Task Confirm Handover untuk aset `Laptop Dell Latitude 5420 - 33 {runId}`
27. Maya mengirim Confirm Handover untuk sesi DU-203-7 dengan aset `Laptop Dell Latitude 5420 - 33 {runId}` tercentang
28. Verifikasi konfirmasi lewat Confirm Handover ditolak server karena sesi sudah dikonfirmasi lewat cara lain
29. Maya meminta data tab Borrowed
30. Verifikasi baris pinjaman aset `Laptop Dell Latitude 5420 - 33 {runId}` berstatus `Borrowed` sebagai hasil konfirmasi lewat Accept

### Konfirmasi PIC yang masuk lebih dulu berlaku
31. Wulan meminta data tab Task
32. Verifikasi data memuat Task Confirm Handover untuk aset `Laptop Dell Latitude 5420 - 34 {runId}` milik Anton
33. Wulan mengirim Confirm Handover atas nama Anton untuk sesi DU-203-8 dengan aset `Laptop Dell Latitude 5420 - 34 {runId}` dan pernyataan tercentang
34. Verifikasi konfirmasi PIC diterima server
35. Gita mengonfirmasi sesi DU-203-8 lewat `Confirm on This Device`
36. Verifikasi konfirmasi dari perangkat admin ditolak server karena sesi sudah dikonfirmasi lewat cara lain
37. Wulan meminta data tab Borrowed
38. Verifikasi baris pinjaman aset `Laptop Dell Latitude 5420 - 34 {runId}` berstatus `Borrowed` sebagai hasil konfirmasi PIC

### Konfirmasi sesudah Cancel Request ditolak dan baris tetap Waiting for Handover
39. Gita menekan `Cancel Request` pada sesi DU-203-9
40. Gita meminta Custody aset `Laptop Dell Latitude 5420 - 35 {runId}`
41. Maya mengirim Confirm Handover untuk sesi DU-203-9 dengan aset `Laptop Dell Latitude 5420 - 35 {runId}` tercentang
42. Verifikasi konfirmasi ditolak server karena sesi dibatalkan lewat `Cancel Request`
43. Maya meminta data tab Borrowed
44. Verifikasi baris pinjaman aset `Laptop Dell Latitude 5420 - 35 {runId}` tetap berstatus `Waiting for Handover`
45. Gita meminta Custody aset `Laptop Dell Latitude 5420 - 35 {runId}`
46. Verifikasi Custody aset `Laptop Dell Latitude 5420 - 35 {runId}` sama dengan Custody pada langkah 40
47. Maya meminta data tab Task
48. Verifikasi data tidak memuat Task Confirm Handover untuk aset `Laptop Dell Latitude 5420 - 35 {runId}`

### Batas Expires At: tepat pada batas ditolak, sebelum batas diterima
49. Waktu berlalu sampai tepat Expires At sesi DU-203-10
50. Maya mengirim Confirm Handover untuk sesi DU-203-10 dengan aset `Laptop Dell Latitude 5420 - 36 {runId}` tercentang
51. Verifikasi konfirmasi pada Expires At ditolak server karena jendela konfirmasi habis
52. Maya meminta data tab Borrowed
53. Verifikasi baris pinjaman aset `Laptop Dell Latitude 5420 - 36 {runId}` tetap berstatus `Waiting for Handover`
54. Maya meminta data tab Task
55. Verifikasi data tidak memuat Task Confirm Handover untuk aset `Laptop Dell Latitude 5420 - 36 {runId}`
56. Waktu berlalu sampai satu detik sebelum Expires At sesi DU-203-11
57. Maya mengirim Confirm Handover untuk sesi DU-203-11 dengan aset `Laptop Dell Latitude 5420 - 37 {runId}` tercentang
58. Verifikasi konfirmasi sebelum Expires At diterima server

### Aset tidak tercentang tetap Waiting for Handover dan tercatat hanya di Borrow Log
59. Maya mengirim Confirm Handover untuk sesi DU-203-12 dengan aset `Projector Epson EB-X06 - 38 {runId}` dan `Laptop Dell Latitude 5420 - 39 {runId}` tercentang, dan aset `Meeting Mic Set - 40 {runId}` tidak tercentang
60. Verifikasi konfirmasi diterima server
61. Maya meminta data tab Borrowed
62. Verifikasi baris pinjaman aset `Projector Epson EB-X06 - 38 {runId}` dan `Laptop Dell Latitude 5420 - 39 {runId}` berstatus `Borrowed`
63. Verifikasi baris pinjaman aset `Meeting Mic Set - 40 {runId}` tetap berstatus `Waiting for Handover`
64. Maya meminta Borrow Log baris pinjaman aset `Meeting Mic Set - 40 {runId}`
65. Verifikasi Borrow Log memuat node `Handover not confirmed` dengan keterangan `Not received`
66. Maya meminta Borrow Log baris pinjaman aset `Projector Epson EB-X06 - 38 {runId}`
67. Verifikasi Borrow Log memuat node `Handed over`

### Konfirmasi yang berhasil memindahkan Custody dan tercatat di Transaction log aset
68. Gita meminta Custody aset `Laptop Dell Latitude 5420 - 41 {runId}`
69. Gita meminta Transaction log aset `Laptop Dell Latitude 5420 - 41 {runId}` dan mencatat entri teratasnya
70. Maya mengirim Confirm Handover untuk sesi DU-203-13 dengan aset `Laptop Dell Latitude 5420 - 41 {runId}` tercentang
71. Verifikasi konfirmasi diterima server
72. Maya meminta data tab Borrowed
73. Verifikasi baris pinjaman aset `Laptop Dell Latitude 5420 - 41 {runId}` berstatus `Borrowed`
74. Gita meminta Custody aset `Laptop Dell Latitude 5420 - 41 {runId}`
75. Verifikasi Custody aset `Laptop Dell Latitude 5420 - 41 {runId}` sudah berubah dibandingkan Custody pada langkah 68
76. Gita meminta Transaction log aset `Laptop Dell Latitude 5420 - 41 {runId}`
77. Verifikasi Transaction log aset `Laptop Dell Latitude 5420 - 41 {runId}` memuat satu entri baru dibandingkan entri teratas pada langkah 69
