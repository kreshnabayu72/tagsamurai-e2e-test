---
id: TC-FA-ASSIGN-UI-103-form-assignment-request-baris-aset-tidak-layak
title: "Form Assignment Request: baris aset Ready dan Not ready"
layer: ui-client
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["S-ASG-01", "S-ASG-02", "FI-ASG-09", "FI-ASG-10", "FI-ASG-11", "FI-ASG-12", "FI-ASG-13", "FI-ASG-14", "FI-ASG-15", "V-ASG-05", "V-ASG-04", "EC-ASG-43", "EC-ASG-44", "ASSIGN-LOGIC-03d", "ASSIGN-LOGIC-03f", "ASSIGN-LOGIC-05f", "§4.4#r5", "§6#p1", "EB-TBL-5@submit-luar-cakupan"]
smoke: []
dependsOn: []
trace:
  "S-ASG-01": 2
  "S-ASG-02": [6, 7, 27]
  "FI-ASG-09": [2, 54, 56, 58, 60]
  "FI-ASG-10": [6, 7, 8]
  "FI-ASG-11": [11, 14, 17]
  "FI-ASG-12": [29, 31, 33]
  "FI-ASG-13": [3, 9, 35, 37, 38]
  "FI-ASG-14": [62, 63, 64]
  "FI-ASG-15": [65, 67]
  "V-ASG-05": [70, 80]
  "V-ASG-04": [7, 23, 29, 56, 60]
  "EC-ASG-43": [70, 71, 80, 81]
  "EC-ASG-44": [46, 47, 49, 52]
  "ASSIGN-LOGIC-03d": [6, 7, 23]
  "ASSIGN-LOGIC-03f": [11, 17, 21]
  "ASSIGN-LOGIC-05f": [4, 73, 75]
  "§4.4#r5": [26, 27, 84, 85, 86, 87]
  "§6#p1": [11, 17, 18, 21, 22]
  "EB-TBL-5@submit-luar-cakupan": 67
anchor: []
coverage:
  web: automated
---

# Form Assignment Request: baris aset Ready dan Not ready

## Prerequisites
- Aktor: Aktor Assignment.
- Layar awal: halaman Assignment Request pada level Full.
- Komponen: Form Assignment Request
- Data:
  - DU-103-1: Assignee Employee `Dewi Kartika`, Email `dewi.kartika@example.com`, Position `Staff`, Division `IT`, Home Group `Head Office`.
  - DU-103-2: Assignee Division `Finance`, Code `FIN`, Users `4`.
  - DU-103-3: PIC `Sari Dewi`, Email `sari.dewi@example.com`, anggota Division `Finance`.
  - DU-103-4: Aset `Laptop Dell Latitude 5420 - 10`, Asset ID `LPT-2026-0010`, Group `Head Office`, Approval Rule `No approval`, Confirmation Rule `Yes`.
  - DU-103-5: Aset `Laptop Dell Latitude 5420 - 11`, Asset ID `LPT-2026-0011`, Group `Head Office`, Approval Rule `No approval`, Confirmation Rule `Yes`.
  - DU-103-6: Aset `Printer HP M404 - 3`, Asset ID `PRN-2026-0003`, Group `Head Office`, Approval Rule `No approval`, Confirmation Rule `No`, tidak boleh ditugaskan ke Division.
  - DU-103-7: Aset `Toyota Avanza - 6`, Asset ID `VEH-2026-0006`, Group `Branch Surabaya`, Approval Rule `Needs approval`, Confirmation Rule `Yes`.
  - DU-103-8: Aset `Excavator PC200 - 5`, Asset ID `EXC-2026-0011`, Group `Head Office`, Approval Rule `Needs approval (all must approve)`, Confirmation Rule `Yes`.
  - DU-103-9: Aset `Excavator PC200 - 4`, Asset ID `EXC-2026-0010`, Group `Branch Bandung`, di luar cakupan Aktor Assignment.
  - DU-103-10: Purpose awal `Operasional kantor pusat` pada baris yang berisi Purpose.
  - DU-103-14: Aset `Laptop Dell Latitude 5420 - 10`, Asset ID `LPT-2026-0010` yang sudah ada pada form dan dipilih lagi lewat dialog Select Asset.
  - DU-103-12: 12 aset layak `Monitor Dell P2422H - {n}`, Group `Head Office`, Approval Rule `No approval`, Confirmation Rule `Yes`.
  - DU-103-13: 12 aset layak `Keyboard Logitech K380 - {n}`, Group `Head Office`, Approval Rule `No approval`, Confirmation Rule `Yes`.
- Kondisi:
  - K1: Assignee DU-103-1 dipilih; tabel berisi DU-103-4 dan DU-103-5, keduanya layak.
  - K2: Assignee DU-103-2 dipilih dengan PIC DU-103-3; tabel berisi DU-103-4 yang layak dan DU-103-6 yang tidak layak karena Assignee bertipe Division tidak diizinkan; Purpose DU-103-10 terisi di setiap baris.
  - K3: Assignee DU-103-2 dipilih dengan PIC DU-103-3; tabel berisi DU-103-4 yang layak, DU-103-7 yang gagal dua aturan (aset sudah dihapus dan Assignee bertipe Division tidak diizinkan), dan DU-103-8 yang gagal dua aturan (aset sudah berada di transaksi aktif lain dan Assignee bertipe Division tidak diizinkan); Purpose DU-103-10 terisi di setiap baris.
  - K4: form dibuka tanpa overlay dengan Assignee DU-103-1 dipilih; tabel berisi DU-103-4 dan DU-103-6, keduanya layak; dialog Select Assignee memuat DU-103-1 dan DU-103-2; dialog Select User memuat DU-103-3; Purpose DU-103-10 terisi di setiap baris.
  - K5: form dibuka dari Asset List dengan Assignee DU-103-2 dan PIC DU-103-3; tabel berisi DU-103-4 yang layak dan DU-103-6 yang tidak layak karena Assignee bertipe Division tidak diizinkan.
  - K6: Edit draft dibuka dengan draft tersimpan: Assignee DU-103-2, PIC DU-103-3, aset DU-103-4 dan DU-103-6; DU-103-6 sudah tidak layak sejak draft disimpan.
  - K7: form baru dengan Assignee DU-103-1 dipilih; tabel berisi DU-103-4 ber-Purpose DU-103-10 yang layak saat form dibuka; saat Submit, DU-103-4 sudah tidak layak karena sudah berada di transaksi aktif lain.
  - K8: Assignee DU-103-1 dipilih; tabel berisi DU-103-4 dalam cakupan dan DU-103-9 di luar cakupan.
  - K9: Assignee DU-103-1 dipilih; tabel hanya berisi DU-103-4; pindai tag menghasilkan aset DU-103-4 yang sama.
  - K10: Assignee DU-103-1 dipilih; tabel berisi DU-103-4 dan DU-103-7, keduanya layak dan ber-Purpose DU-103-10.
  - K11: Assignee DU-103-1 dipilih; tabel hanya berisi DU-103-4; dialog Select Asset memuat DU-103-14.
  - K12: Assignee DU-103-2 dipilih dengan PIC DU-103-3; tabel berisi DU-103-12, DU-103-6, DU-103-13, dan DU-103-8 menurut urutan itu, dengan DU-103-6 dan DU-103-8 tidak layak karena Assignee bertipe Division tidak diizinkan; Purpose DU-103-10 terisi di setiap baris; baris DU-103-6 berada di luar layar saat Submit ditekan.

## Test Steps

### Baris Ready tanpa caption dan tanpa Remove Unavailable
1. Tampilkan Form Assignment Request dengan kondisi K1
2. Verifikasi baris `Laptop Dell Latitude 5420 - 10` dan `Laptop Dell Latitude 5420 - 11` tampil tanpa ikon ⚠ dan tanpa caption error
3. Verifikasi tombol `[Remove Unavailable]` tidak tampil
4. Verifikasi Alert pemecahan tidak tampil

### Baris Not ready ditandai di sel Name
5. Tampilkan Form Assignment Request dengan kondisi K2
6. Verifikasi baris `Printer HP M404 - 3` menampilkan ikon ⚠
7. Verifikasi caption error `This asset can no longer be assigned.` tampil di bawah nama aset pada baris `Printer HP M404 - 3`
8. Verifikasi baris `Laptop Dell Latitude 5420 - 10` tidak berubah: tanpa ikon ⚠ dan tanpa caption
9. Verifikasi tombol `[Remove Unavailable]` tampil
10. Arahkan kursor ke ikon ⚠ pada baris `Printer HP M404 - 3`
11. Verifikasi tooltip `This asset can't be assigned to a division.` tampil
12. Pindahkan kursor keluar dari ikon ⚠
13. Pindahkan fokus keyboard ke ikon ⚠ pada baris `Printer HP M404 - 3`
14. Verifikasi tooltip `This asset can't be assigned to a division.` tampil untuk fokus keyboard

### Tooltip memuat satu alasan dengan prioritas tertinggi
15. Tampilkan Form Assignment Request dengan kondisi K3
16. Arahkan kursor ke ikon ⚠ pada baris `Toyota Avanza - 6`
17. Verifikasi tooltip `This asset has been deleted.` tampil
18. Verifikasi tooltip tidak memuat `This asset can't be assigned to a division.`
19. Pindahkan kursor keluar dari ikon ⚠
20. Arahkan kursor ke ikon ⚠ pada baris `Excavator PC200 - 5`
21. Verifikasi tooltip `This asset is already in another transaction.` tampil
22. Verifikasi tooltip tidak memuat `This asset can't be assigned to a division.`
23. Verifikasi caption error `This asset can no longer be assigned.` sama tampil pada baris `Toyota Avanza - 6` dan `Excavator PC200 - 5`

### Submit gagal sampai aset tidak layak dikeluarkan
24. Tampilkan Form Assignment Request dengan kondisi K2
25. Klik `[Submit]`
26. Verifikasi baris `Printer HP M404 - 3` ditandai ⚠ dan terlihat pada layar
27. Verifikasi tidak ada dialog `Submit Assignment` yang tampil
28. Klik ikon ⋯ pada baris `Printer HP M404 - 3`
29. Verifikasi menu aksi baris tidak layak menyediakan `Remove from List`
30. Klik `Remove from List`
31. Verifikasi baris `Printer HP M404 - 3` tidak lagi tampil
32. Klik `[Submit]`
33. Verifikasi dialog `Submit Assignment` tampil setelah baris tidak layak dikeluarkan

### Remove Unavailable mengeluarkan semua baris tidak layak sekaligus
34. Tampilkan Form Assignment Request dengan kondisi K3
35. Verifikasi tombol `[Remove Unavailable]` tampil
36. Klik `[Remove Unavailable]`
37. Verifikasi baris `Toyota Avanza - 6` dan `Excavator PC200 - 5` tidak lagi tampil dan baris `Laptop Dell Latitude 5420 - 10` tetap tampil
38. Verifikasi tombol `[Remove Unavailable]` tidak tampil lagi

### Mengganti Assignee ke Division hanya menandai aset yang tidak lolos
39. Tampilkan Form Assignment Request dengan kondisi K4
40. Klik tombol Assignee `Dewi Kartika`
41. Klik sub-tab `Divisions`
42. Pilih `Finance` pada sub-tab `Divisions`
43. Konfirmasi pilihan pada dialog Select Assignee
44. Pilih PIC `Sari Dewi` pada dialog Select User
45. Konfirmasi pilihan pada dialog Select User
46. Verifikasi hanya baris `Printer HP M404 - 3` yang ditandai ⚠ dengan caption `This asset can no longer be assigned.`
47. Verifikasi baris `Laptop Dell Latitude 5420 - 10` tidak berubah
48. Klik `[Submit]`
49. Verifikasi tidak ada dialog `Submit Assignment` yang tampil
50. Klik `[Remove Unavailable]`
51. Klik `[Submit]`
52. Verifikasi dialog `Submit Assignment` tampil setelah baris yang tidak lolos dikeluarkan

### Kelayakan dinilai untuk form yang dibuka dengan aset terpilih
53. Tampilkan Form Assignment Request dengan kondisi K5
54. Verifikasi baris `Printer HP M404 - 3` ditandai ⚠ pada form yang dibuka dengan aset terpilih

### Kelayakan dinilai ulang saat Draft dibuka
55. Tampilkan Form Assignment Request dengan kondisi K6
56. Verifikasi baris `Printer HP M404 - 3` ditandai ⚠ dengan caption `This asset can no longer be assigned.` pada Draft yang dibuka

### Kelayakan dinilai ulang saat Submit
57. Tampilkan Form Assignment Request dengan kondisi K7
58. Verifikasi baris `Laptop Dell Latitude 5420 - 10` tampil tanpa ikon ⚠
59. Klik `[Submit]`
60. Verifikasi baris `Laptop Dell Latitude 5420 - 10` ditandai ⚠ dengan caption `This asset can no longer be assigned.` setelah Submit

### Baris di luar cakupan pengguna
61. Tampilkan Form Assignment Request dengan kondisi K8
62. Verifikasi baris `Excavator PC200 - 4` tampil read-only dengan Group `Branch Bandung` dan `Outside your groups`
63. Verifikasi isian Purpose pada baris `Excavator PC200 - 4` disabled
64. Verifikasi tombol hapus pada baris `Excavator PC200 - 4` disabled
65. Verifikasi tombol `[Submit]` disabled
66. Arahkan kursor ke tombol `[Submit]`
67. Verifikasi alasan `Some assets are outside your groups. Ask another admin to submit.` tersampaikan pada tombol `[Submit]` yang disabled

### Aset ganda tidak digandakan
68. Tampilkan Form Assignment Request dengan kondisi K9
69. Pindai tag aset `Laptop Dell Latitude 5420 - 10` yang sudah ada pada form
70. Verifikasi toast error `Error, this asset is already in this assignment.` tampil
71. Verifikasi tabel tetap memuat satu baris `Laptop Dell Latitude 5420 - 10`

### Pemecahan per Group tampil sebelum Submit
72. Tampilkan Form Assignment Request dengan kondisi K10
73. Verifikasi Alert pemecahan tampil dan menyebut Group `Head Office` serta `Branch Surabaya`
74. Klik `[Submit]`
75. Verifikasi dialog `Submit Assignment` menyebut Group `Head Office` dan `Branch Surabaya`

### Aset yang sama dipilih lagi lewat dialog Select Asset tidak digandakan
76. Tampilkan Form Assignment Request dengan kondisi K11
77. Klik `[+ Asset]`
78. Centang aset `Laptop Dell Latitude 5420 - 10` pada dialog Select Asset
79. Klik `[Select]`
80. Verifikasi toast error `Error, this asset is already in this assignment.` tampil untuk aset yang dipilih lewat dialog
81. Verifikasi tabel tetap memuat satu baris `Laptop Dell Latitude 5420 - 10` setelah dipilih lewat dialog

### Submit gagal menggulir ke baris tidak layak pertama
82. Tampilkan Form Assignment Request dengan kondisi K12
83. Klik `[Submit]`
84. Verifikasi baris `Printer HP M404 - 3` ditandai ⚠ dan terlihat pada layar
85. Verifikasi baris `Excavator PC200 - 5` ditandai ⚠ dan tidak terlihat pada layar
86. Verifikasi tidak ada dialog `Submit Assignment` yang tampil untuk Submit dengan banyak baris tidak layak
87. Verifikasi tidak ada permintaan submit yang terkirim
