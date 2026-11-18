---
id: TC-FA-ASSIGN-E2E-013-log-assignment-per-aset
title: "Assignment Log per aset dalam satu ASG"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: [D-ASG-29, "§4.1#r12", "§5#r8", "§8#p1", "§8.1#p1", "§8.1#r1", "§8.1#r2", "§8.1#r3", "§8.1#r4", "§8.1#r5", "§8.1#b1", "§8.1#b2", "§8.1#r6", "§8.1#r7", "§8.1#r8", "§8.1#r9", "§8.1#r10", "§8.1#r11", "§8.1#r12", "§8.1#r13", "§8.1#r14", "§8.1#r15", "§8.1#r16", "§8.1#r17", "§8.1#r18", "§8.1#r19", "§8.1#r20", "§8.1#r21", "§8.1#r22", "§8.1#r23", "§8.1#r24", "§8.1#r25", "§8.1#p4", "§8.1#p6"]
smoke: []
dependsOn: []
trace:
  D-ASG-29: 5
  "§4.1#r12": [5, 53, 69]
  "§5#r8": 70
  "§8#p1": 70
  "§8.1#p1": [5, 14]
  "§8.1#r1": 6
  "§8.1#r2": 6
  "§8.1#r3": [7, 17, 25, 28, 30, 41, 42]
  "§8.1#r4": 8
  "§8.1#r5": [9, 53, 69]
  "§8.1#b1": [45, 46, 56]
  "§8.1#b2": []
  "§8.1#r6": [12, 20, 61]
  "§8.1#r7": [11, 60]
  "§8.1#r8": [19, 76]
  "§8.1#r9": 18
  "§8.1#r10": [10, 26]
  "§8.1#r11": [36, 59, 82]
  "§8.1#r12": 27
  "§8.1#r13": 58
  "§8.1#r14": [35, 56]
  "§8.1#r15": 34
  "§8.1#r16": [32, 55]
  "§8.1#r17": 33
  "§8.1#r18": 31
  "§8.1#r19": 57
  "§8.1#r20": 54
  "§8.1#r21": []
  "§8.1#r22": 46
  "§8.1#r23": 43
  "§8.1#r24": 44
  "§8.1#r25": 45
  "§8.1#p4": [62, 63]
  "§8.1#p6": [13, 54]
coverage:
  web: automated
---

# Assignment Log per aset dalam satu ASG

## Prerequisites
- Aktor: Total Control `Hendra Kusuma {runId}`, yang juga memegang hak Aktor Damaged dan Aktor Missing.
- Layar awal: Transactions > Assignment.
- Data:
  - DU-013-1: User `Hendra Kusuma {runId}`, role Total Control, cakupan seluruh client dengan hak Aktor Damaged dan Aktor Missing; ia aktor spec ini dan pelaku node keputusan Damaged dan Missing.
  - DU-013-2: Group `Head Office {runId}`.
  - DU-013-3: User `Agus Prasetyo {runId}`, role Asset Admin pada Group `Head Office {runId}`; ia pengaju ASG, pemberi saat Handover, dan penerima saat Unassign.
  - DU-013-4: User `Rina Wijaya {runId}`, role Approver pada Group `Head Office {runId}`.
  - DU-013-5: User `Sari Dewi {runId}`, role Approver pada Group `Head Office {runId}`.
  - DU-013-6: Division `Finance {runId}` dengan PIC aktif `Dewi Anggraini {runId}` dan PIC lama `Dedi Hartono {runId}`, keduanya karyawan aktif tanpa akses menu Assignment.
  - DU-013-7: ASG untuk Assignee Division `Finance {runId}` dengan PIC `Dewi Anggraini {runId}` di Group `Head Office {runId}`, diajukan `Agus Prasetyo {runId}`, memuat enam aset `Camera Sony A7 {runId}`, `Excavator PC200 {runId}`, `Laptop Dell Latitude 5420 {runId}`, `Mouse Logitech MX Master {runId}`, `Proyektor Epson EB-X49 {runId}`, dan `Tablet Samsung Tab S8 {runId}` yang riwayatnya di bawah; ASG ini aktif karena `Proyektor Epson EB-X49 {runId}` masih `Assigned`.
  - DU-013-8: Aset `Laptop Dell Latitude 5420 {runId}` di ASG DU-013-7 dengan riwayat dari lama ke baru: diajukan `Agus Prasetyo {runId}` dengan Purpose `Audit lapangan` dan Approval `Waiting 2 approvers`; disetujui `Rina Wijaya {runId}` dan `Sari Dewi {runId}` dengan Mode `All` dan Note `Disetujui untuk audit`; diserahkan `Agus Prasetyo {runId}` dengan Confirmation `Accepted on phone` dan Condition `Normal`; PIC diganti dari `Dedi Hartono {runId}` ke `Dewi Anggraini {runId}` oleh `Agus Prasetyo {runId}`; TAG dilaporkan `Agus Prasetyo {runId}`; kerusakan dilaporkan `Dewi Anggraini {runId}` atas nama `Finance {runId}` dengan Description `Layar retak`; laporan dikonfirmasi `Hendra Kusuma {runId}`; di-Unassign `Agus Prasetyo {runId}` dengan Condition `Damaged`; selama riwayat itu juga terjadi peristiwa yang tidak dicatat: Draft atas aset ini dibuat dan diubah `Agus Prasetyo {runId}` sebelum diajukan, `Remind Assignee` oleh `Agus Prasetyo {runId}`, dan anggota Division `Finance {runId}` ditambah `Joko Santoso {runId}`.
  - DU-013-9: Aset `Proyektor Epson EB-X49 {runId}` di ASG DU-013-7 dengan riwayat dari lama ke baru: diajukan tanpa approval; diserahkan `Agus Prasetyo {runId}` dengan Confirmation `Confirmed by Agus Prasetyo {runId} on behalf of Finance {runId}` dan foto handover tersedia; kerusakan dilaporkan `Agus Prasetyo {runId}` dengan Description `Baterai menggembung` dan Condition handover `Normal`, lalu laporan dibatalkan `Agus Prasetyo {runId}`; dilaporkan lagi dan ditolak `Hendra Kusuma {runId}` dengan Reason `Kerusakan tidak ditemukan`; dilaporkan lagi, dikonfirmasi, lalu ditandai selesai diperbaiki oleh `Hendra Kusuma {runId}`; barisnya berstatus `Assigned`.
  - DU-013-10: Aset `Camera Sony A7 {runId}` di ASG DU-013-7 dengan riwayat dari lama ke baru: diajukan tanpa approval; diserahkan; dilaporkan hilang oleh `Dewi Anggraini {runId}` atas nama `Finance {runId}` dengan Reason `Hilang saat dinas luar` dan Status `Waiting for Confirmation`; laporan dibatalkan PIC; dilaporkan lagi dan ditolak `Hendra Kusuma {runId}` dengan Reason `Belum cukup bukti`; dilaporkan lagi dan dikonfirmasi `Hendra Kusuma {runId}` sehingga barisnya `Unassigned` dengan marker `Missing`.
  - DU-013-11: Aset `Excavator PC200 {runId}` di ASG DU-013-7 dengan riwayat dari lama ke baru: diajukan dengan Approval `Routed to: Group Manager (no eligible approver)`; approval dialihkan sistem ke `Group Manager` dengan Reason `No eligible approver`; ditolak `Maya Putri {runId}`, Group Manager penerima reroute, dengan Reason `Anggaran belum disetujui`.
  - DU-013-12: Aset `Tablet Samsung Tab S8 {runId}` di ASG DU-013-7 dengan riwayat dari lama ke baru: diajukan tanpa approval; konfirmasi tidak diterima karena jendela konfirmasi habis, dimulai `Agus Prasetyo {runId}`; dibatalkan sistem dengan Reason `Not handed over`.
  - DU-013-13: Aset `Mouse Logitech MX Master {runId}` di ASG DU-013-7 dengan riwayat dari lama ke baru: diajukan `Agus Prasetyo {runId}` dengan Purpose `Kerja harian` dan Approval `Waiting 1 approver`; disetujui `Sari Dewi {runId}` dengan Mode `Any one` dan Note `Setuju`; dibatalkan `Agus Prasetyo {runId}` dengan `Save as Draft to edit`; aset ini sebelumnya pernah `Assigned` lalu `Unassigned` di ASG lain DU-013-18.
  - DU-013-14: User `Maya Putri {runId}`, role Group Manager aktif pada Group `Head Office {runId}`; penerima reroute approval DU-013-11.
  - DU-013-15: User `Wulan Hartati {runId}`, karyawan aktif tanpa akses menu Assignment; tampil sebagai `Wulan H`.
  - DU-013-16: Group `Branch Medan {runId}` tanpa Group Manager aktif.
  - DU-013-17: ASG untuk Assignee DU-013-15 di Group `Branch Medan {runId}`, diajukan `Hendra Kusuma {runId}`, dengan satu aset `Zebra Printer ZT230 {runId}` `Waiting for Approval` yang approval-nya dialihkan sistem ke `Total Control` dengan Reason `No eligible approver`.
  - DU-013-18: ASG lama untuk Assignee Division `Procurement {runId}` di Group `Head Office {runId}` yang memuat aset `Mouse Logitech MX Master {runId}`, pernah diserahkan lalu di-Unassign; riwayat itu milik ASG lama dan bukan milik ASG DU-013-7.

## Test Steps

### Dialog dari Assignment Detail: aset dengan berbagai riwayat
1. Ketik Search `Finance {runId}`, tekan Enter
2. Klik tautan Transaction ID pada baris `Finance {runId}`
3. Klik `⋯` pada baris `Mouse Logitech MX Master {runId}`
4. Klik `Assignment Log`
5. Verifikasi dialog `Assignment Log` terbuka dan tidak memuat kontrol untuk mengubah atau menghapus riwayat
6. Verifikasi dialog memuat judul `Assignment Log` dan Transaction ID berformat `ASG-YYYY-NNNN`
7. Verifikasi tombol `Prev` dan `Next` tampil di header dialog
8. Verifikasi pihak `Requested By` bernilai `Agus Prasetyo {runId}` dan `Assignee` bernilai `Finance {runId} · PIC Dewi Anggraini {runId}`
9. Verifikasi badge status baris `Canceled` tampil
10. Verifikasi node `Canceled by [Actor]` dengan pelaku `Agus Prasetyo {runId}` tampil dengan keterangan `Saved as draft` dan tanpa Reason karena dibatalkan pengaju
11. Verifikasi node `Approved by [Approver]` dengan pelaku `Sari Dewi {runId}` tampil dengan `Mode` bernilai `Any one` dan `Note` bernilai `Setuju`
12. Verifikasi node `Assignment requested by [Actor]` dengan pelaku `Agus Prasetyo {runId}` tampil dengan `Purpose` bernilai `Kerja harian` dan `Approval` bernilai `Waiting 1 approver`
13. Verifikasi urutan node dari atas ke bawah adalah `Canceled by`, `Approved by`, lalu `Assignment requested by` dengan tanggal dan waktu di setiap node
14. Verifikasi dialog tidak memuat node `Handed over by [Giver]` maupun `Unassigned by [Receiver]` karena keduanya milik ASG lain
15. Klik `Prev`
16. Klik `Prev`
17. Verifikasi dialog menampilkan aset `Excavator PC200 {runId}`
18. Verifikasi node `Rejected by [Approver]` dengan pelaku `Maya Putri {runId}` tampil dengan `Reason` bernilai `Anggaran belum disetujui`
19. Verifikasi node `Approval rerouted` tampil dengan `Routed to` bernilai `Group Manager` dan `Reason` bernilai `No eligible approver`
20. Verifikasi node `Assignment requested by [Actor]` untuk aset itu tampil dengan `Approval` bernilai `Routed to: Group Manager (no eligible approver)`
21. Klik `Next`
22. Klik `Next`
23. Klik `Next`
24. Klik `Next`
25. Verifikasi dialog menampilkan aset `Tablet Samsung Tab S8 {runId}`
26. Verifikasi node `Canceled by [Actor]` dengan pelaku `System` tampil dengan `Reason` bernilai `Not handed over`
27. Verifikasi node `Confirmation not received` tampil dengan `Started by` bernilai `Agus Prasetyo {runId}` dan penyebab jendela konfirmasi habis
28. Verifikasi `Next` Disabled karena `Tablet Samsung Tab S8 {runId}` berada di urutan terakhir tabel Assets
29. Klik `Prev`
30. Verifikasi dialog menampilkan aset `Proyektor Epson EB-X49 {runId}`
31. Verifikasi node `Marked as repaired by [Actor]` dengan pelaku `Hendra Kusuma {runId}` tampil dan badge `Damaged` hilang
32. Verifikasi node `Damage report confirmed by [Actor]` dengan pelaku `Hendra Kusuma {runId}` tampil dan badge `Reported Damaged` menjadi `Damaged`
33. Verifikasi node `Damage report rejected by [Actor]` dengan pelaku `Hendra Kusuma {runId}` tampil dengan `Reason` bernilai `Kerusakan tidak ditemukan` dan badge `Reported Damaged` hilang
34. Verifikasi node `Damage report canceled by [Actor]` dengan pelaku `Agus Prasetyo {runId}` tampil dengan `Report No.` berupa tautan dan barisnya tetap `Assigned`
35. Verifikasi node `Damage reported by [Reporter]` dengan pelaku `Agus Prasetyo {runId}` tampil dengan `Description` bernilai `Baterai menggembung` dan `Report No.` berupa tautan
36. Verifikasi node `Handed over by [Giver]` dengan pelaku `Agus Prasetyo {runId}` tampil dengan `Confirmation` bernilai `Confirmed by Agus Prasetyo {runId} on behalf of Finance {runId}` dan `Condition` bernilai `Normal`
37. Klik `Prev`
38. Klik `Prev`
39. Klik `Prev`
40. Klik `Prev`
41. Verifikasi dialog menampilkan aset `Camera Sony A7 {runId}`
42. Verifikasi `Prev` Disabled karena `Camera Sony A7 {runId}` berada di urutan pertama tabel Assets
43. Verifikasi node `Missing confirmed by [Actor]` dengan pelaku `Hendra Kusuma {runId}` tampil dan barisnya ditutup `Unassigned` dengan marker `Missing`
44. Verifikasi node `Missing report rejected by [Actor]` dengan pelaku `Hendra Kusuma {runId}` tampil dengan `Reason` bernilai `Belum cukup bukti` dan barisnya tetap `Assigned`
45. Verifikasi node `Missing report canceled by [Actor]` tampil dengan pelaku ditulis `[PIC] on behalf of [Division]` untuk PIC `Dewi Anggraini {runId}` atas nama `Finance {runId}`
46. Verifikasi node `Reported missing by [Actor]` dengan pelaku `Dewi Anggraini {runId}` atas nama `Finance {runId}` tampil dengan `Reason` bernilai `Hilang saat dinas luar` dan `Status` bernilai `Waiting for Confirmation`
47. Tutup dialog `Assignment Log`

### Dialog dari tab History By Asset: aset Unassigned dengan marker Damaged
48. Klik tab `History`
49. Klik sub-tab `By Asset`
50. Ketik Search `Laptop Dell Latitude 5420 {runId}`, tekan Enter
51. Klik `⋯` pada baris `Laptop Dell Latitude 5420 {runId}`
52. Klik `Assignment Log`
53. Verifikasi dialog `Assignment Log` terbuka dari tab `History` dan memuat badge status baris `Unassigned` dengan badge kedua `Damaged`
54. Verifikasi node `Unassigned by [Receiver]` dengan pelaku `Agus Prasetyo {runId}` tampil dengan `Status` bernilai `Unassigned · Damaged`, `Condition` bernilai `Damaged`, dan `Report No.`
55. Verifikasi node `Damage report confirmed by [Actor]` dengan pelaku `Hendra Kusuma {runId}` tampil dan badge `Reported Damaged` menjadi `Damaged`
56. Verifikasi node `Damage reported by [Reporter]` dengan pelaku `Dewi Anggraini {runId}` atas nama `Finance {runId}` tampil dengan `Description` bernilai `Layar retak`
57. Verifikasi node `TAG reported by [Reporter]` dengan pelaku `Agus Prasetyo {runId}` tampil dengan kode TAG, `Report Type`, dan `Report No.`
58. Verifikasi node `PIC changed by [Actor]` dengan pelaku `Agus Prasetyo {runId}` tampil dengan PIC lama `Dedi Hartono {runId}` dan PIC baru `Dewi Anggraini {runId}`
59. Verifikasi node `Handed over by [Giver]` dengan pelaku `Agus Prasetyo {runId}` tampil dengan `Confirmation` bernilai `Accepted on phone` dan `Condition` bernilai `Normal`
60. Verifikasi dua node `Approved by` tampil, untuk `Rina Wijaya {runId}` dan `Sari Dewi {runId}`, masing-masing dengan `Mode` bernilai `All` dan `Note` bernilai `Disetujui untuk audit`
61. Verifikasi node `Assignment requested by [Actor]` dengan pelaku `Agus Prasetyo {runId}` tampil dengan `Purpose` bernilai `Audit lapangan` dan `Approval` bernilai `Waiting 2 approvers`
62. Verifikasi dialog tidak memuat node untuk Draft, `Remind Assignee`, maupun perubahan keanggotaan
63. Verifikasi dialog tidak memuat node `Confirmed` atau `Verified` yang terpisah dan tidak memuat node `Level n approved`
64. Tutup dialog `Assignment Log`

### Dialog dari tab Assigned Assets By Asset
65. Klik tab `Assigned Assets`
66. Ketik Search `Proyektor Epson EB-X49 {runId}`, tekan Enter
67. Klik `⋯` pada baris `Proyektor Epson EB-X49 {runId}`
68. Klik `Assignment Log`
69. Verifikasi dialog `Assignment Log` terbuka dari tab `Assigned Assets` dan memuat badge status baris `Assigned`
70. Verifikasi Changelog tidak ada pada halaman Assignment sehingga riwayat hanya dibaca lewat dialog `Assignment Log`

### Approval rerouted ke Total Control
71. Klik tab `Transactions`
72. Ganti isi kotak search dengan `Zebra Printer ZT230 {runId}`, tekan Enter
73. Klik tautan Transaction ID pada baris `Wulan H`
74. Klik `⋯` pada baris `Zebra Printer ZT230 {runId}`
75. Klik `Assignment Log`
76. Verifikasi node `Approval rerouted` tampil dengan `Routed to` bernilai `Total Control` dan `Reason` bernilai `No eligible approver`
77. Tutup dialog `Assignment Log`

### Node Handed over memuat foto handover
78. Klik tab `Assigned Assets`
79. Ketik Search `Proyektor Epson EB-X49 {runId}`, tekan Enter
80. Klik `⋯` pada baris `Proyektor Epson EB-X49 {runId}`
81. Klik `Assignment Log`
82. Verifikasi node `Handed over by [Giver]` dengan pelaku `Agus Prasetyo {runId}` memuat `Photo` berupa foto handover aset `Proyektor Epson EB-X49 {runId}`
83. Tutup dialog `Assignment Log`
