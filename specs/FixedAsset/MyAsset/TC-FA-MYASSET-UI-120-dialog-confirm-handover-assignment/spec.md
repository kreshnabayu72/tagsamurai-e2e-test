---
id: TC-FA-MYASSET-UI-120-dialog-confirm-handover-assignment
title: "Dialog Confirm Handover varian Assignment: isi, pernyataan tanggung jawab, dan dua pesan validasi"
layer: ui-client
priority: Medium
caseType: Negative
status: ready-for-automation
sourceRules: ["FI-04", "FI-07", "FI-08", "FLD-01", "FLD-03", "FLD-04", "V-04", "§1.2#r70", "§4.2.2b#p1", "§4.2.5#p6", "§4.2.5#p7", "§4.2.5#p8", "§4.4#r39"]
smoke: []
dependsOn: []
trace:
  "FI-04": 39
  "FI-07": 31
  "FI-08": 17
  "FLD-01": [8, 24, 39]
  "FLD-03": [9, 17, 25, 31]
  "FLD-04": 5
  "V-04": [24, 25, 31, 39]
  "§1.2#r70": [4, 8, 9, 10]
  "§4.2.2b#p1": [4, 6, 9, 10]
  "§4.2.5#p6": [4, 5, 6, 7, 8, 9, 10, 15, 16, 24, 25, 46, 51]
  "§4.2.5#p7": 11
  "§4.2.5#p8": [24, 25, 26]
  "§4.4#r39": 7
anchor: [44]
coverage:
  web: automated
---

# Dialog Confirm Handover varian Assignment: isi, pernyataan tanggung jawab, dan dua pesan validasi

## Prerequisites
- Aktor: Assignee Employee `Budi Santoso` pada kondisi K1, dan PIC Division `Finance` yaitu `Budi Santoso` pada kondisi K2.
- Layar awal: My Asset > Task.
- Komponen: Dialog Confirm Handover (D-MYA-01)
- Data:
  - DU-120-1: Task Confirm Handover (Assignment) sebagai Assignee sendiri dengan Transaction ID `ASG-2026-0071`, Task `Confirm Handover`, Group `Room 301` (hierarki lengkap `Head Office A > Floor 1 > Room 301`), Total Asset `2`, Handed Over By `Rina W`, Expires At `09/11/26, 20:43`, Assignee `Budi Santoso`.
  - DU-120-2: Task Confirm Handover (Assignment) atas nama Division dengan Transaction ID `ASG-2026-0072`, Task `Confirm Handover`, Group `Head Office`, Total Asset `1`, Handed Over By `Rina W`, Expires At `09/11/26, 20:48`, Assignee Division `Finance` dengan PIC `Budi Santoso`.
  - DU-120-3: aset sesi Handover dengan Photo `laptop-dell-latitude-5420.jpg`, Name `Laptop Dell Latitude 5420 - 44`, Asset ID `LPT-2026-0044`, Brand `Dell`, Model/Type `Latitude 5420`.
  - DU-120-4: aset sesi Handover dengan Photo `meeting-mic-set.jpg`, Name `Meeting Mic Set - 7`, Asset ID `MIC-2026-0007`, Brand `Jabra`, Model/Type `Speak 510`.
  - DU-120-5: aset sesi Handover dengan Photo `projector-epson-eb-x06.jpg`, Name `Projector Epson EB-X06 - 15`, Asset ID `PRJ-2026-0015`, Brand `Epson`, Model/Type `EB-X06`.
  - DU-120-6: pilihan aset tanpa satu pun tercentang: `Laptop Dell Latitude 5420 - 44` dan `Meeting Mic Set - 7` dihapus centangnya.
  - DU-120-7: pernyataan `I acknowledge receipt of these assets and accept responsibility for them.` yang belum dicentang.
- Kondisi:
  - K1: Task DU-120-1 tampil di tab Task, sesi Handover-nya masih menunggu konfirmasi dan memuat aset DU-120-3 dan DU-120-4.
  - K2: Task DU-120-2 tampil di tab Task, sesi Handover-nya masih menunggu konfirmasi dan memuat aset DU-120-5.

## Test Steps

### Isi dialog varian Assignment untuk Assignee Employee
1. Tampilkan Dialog Confirm Handover dengan kondisi K1
2. Klik `⋯` pada baris Task `ASG-2026-0071`
3. Klik `Confirm Handover`
4. Verifikasi dialog `Confirm Handover` tampil dengan Info `Assignee`, `Group`, dan `Handed Over By` yang bernilai `Budi Santoso`, `Room 301`, dan `Rina W`
5. Verifikasi teks bantu `Uncheck any asset you didn't receive.` tampil di atas tabel aset
6. Verifikasi tabel aset memuat kolom `Photo`, `Name`, `Asset ID`, `Brand`, dan `Model/Type`
7. Verifikasi tabel aset tidak memuat kolom `Return by`
8. Verifikasi semua baris aset tercentang
9. Verifikasi pernyataan `I acknowledge receipt of these assets and accept responsibility for them.` tampil sebagai checkbox
10. Verifikasi footer dialog memuat tombol `[Cancel]` dan `[Confirm]`
11. Verifikasi dialog tidak memuat aksi untuk menolak seluruh penugasan

### Assignee Division dan pernyataan atas nama Division
12. Tampilkan Dialog Confirm Handover dengan kondisi K2
13. Klik `⋯` pada baris Task `ASG-2026-0072`
14. Klik `Confirm Handover`
15. Verifikasi Info `Assignee` memuat nama Division `Finance`
16. Verifikasi `PIC: Budi Santoso` tersampaikan pada Assignee `Finance`
17. Verifikasi pernyataan tanggung jawab memuat `on behalf of Finance`

### Dua pesan validasi tampil bersamaan tanpa aset dan pernyataan
18. Tampilkan Dialog Confirm Handover dengan kondisi K1
19. Klik `⋯` pada baris Task `ASG-2026-0071`
20. Klik `Confirm Handover`
21. Hapus centang baris `Laptop Dell Latitude 5420 - 44`
22. Hapus centang baris `Meeting Mic Set - 7`
23. Klik `[Confirm]`
24. Verifikasi error `Check at least one asset you received` tampil di bawah tabel aset
25. Verifikasi error `Check the statement to confirm` tampil di bawah checkbox pernyataan
26. Verifikasi dialog `Confirm Handover` tetap terbuka

### Pernyataan belum dicentang ditolak saat aset tercentang
27. Tampilkan Dialog Confirm Handover dengan kondisi K1
28. Klik `⋯` pada baris Task `ASG-2026-0071`
29. Klik `Confirm Handover`
30. Klik `[Confirm]`
31. Verifikasi error `Check the statement to confirm` tampil

### Tanpa aset tercentang ditolak saat pernyataan dicentang
32. Tampilkan Dialog Confirm Handover dengan kondisi K1
33. Klik `⋯` pada baris Task `ASG-2026-0071`
34. Klik `Confirm Handover`
35. Centang checkbox pernyataan `I acknowledge receipt of these assets and accept responsibility for them.`
36. Hapus centang baris `Laptop Dell Latitude 5420 - 44`
37. Hapus centang baris `Meeting Mic Set - 7`
38. Klik `[Confirm]`
39. Verifikasi error `Check at least one asset you received` tampil di bawah tabel aset

### Checkbox header memilih semua baris pada varian Assignment
40. Tampilkan Dialog Confirm Handover dengan kondisi K1
41. Klik `⋯` pada baris Task `ASG-2026-0071`
42. Klik `Confirm Handover`
43. Hapus centang baris `Laptop Dell Latitude 5420 - 44`
44. Verifikasi baris `Laptop Dell Latitude 5420 - 44` tidak tercentang, sedangkan baris `Meeting Mic Set - 7` tetap tercentang
45. Klik checkbox header tabel aset
46. Verifikasi semua baris aset tercentang

### Group pada Info menyampaikan hierarki lengkap
47. Tampilkan Dialog Confirm Handover dengan kondisi K1
48. Klik `⋯` pada baris Task `ASG-2026-0071`
49. Klik `Confirm Handover`
50. Arahkan kursor ke badge Group `Room 301`
51. Verifikasi hierarki lengkap `Head Office A > Floor 1 > Room 301` tersampaikan
