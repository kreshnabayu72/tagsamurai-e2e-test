---
id: TC-FA-FATR-BE-083-resolusi
title: "Penyelesaian nilai efektif menurut tingkat pewarisan"
layer: be-e2e
priority: Critical
caseType: Positive
status: ready-for-automation
owner: BE
sourceRules: ["§Aturan Logika Modul#r1", "§Aturan Logika Modul#r2", "§Aturan Logika Modul#r18", "§Aturan Logika Modul#r19", "§Aturan Logika Modul#r20", "§Aturan Logika Modul#r21", "§Aturan Logika Modul#r22", "§Aturan Logika Modul#r47", "§Aturan Logika Modul#r103", "§4.1#r99", "§4.1#r100", "§9.2#r1", "§9.2#r2", "§9.2#r3", "§9.2#r4", "§9.2#r5", "§9.2#r6", "§9.2#r7", "§9.2#r8", "§9.2#p6", "§9.2#b5", "§9.2#b78", "§9.2#b92", "§9.2#b109", "§9.2#b165", "§9.2#b183", "§9.2#b193", "§9.2#b200", "§9.4.2#r6", "§9.4.2#r56", "§9.4.2#r57", "§9.4.2#r110", "§9.4.2#r124", "§9.6#r11", "§9.7#r18", "§9.10.4#b3", "§4.4#r7", "§9.2#b86", "§9.2#b566"]
smoke: []
dependsOn: []
trace:
  "§Aturan Logika Modul#r1": [1, 2, 3]
  "§Aturan Logika Modul#r2": [5, 10, 45]
  "§Aturan Logika Modul#r18": [5, 19, 22]
  "§Aturan Logika Modul#r19": 15
  "§Aturan Logika Modul#r20": 14
  "§Aturan Logika Modul#r21": 15
  "§Aturan Logika Modul#r22": [34, 56, 59]
  "§Aturan Logika Modul#r47": [16, 69]
  "§Aturan Logika Modul#r103": [48, 49, 52]
  "§4.1#r99": 47
  "§4.1#r100": 45
  "§9.2#r1": [5, 6]
  "§9.2#r2": [29, 30]
  "§9.2#r3": [7, 8]
  "§9.2#r4": [19, 20]
  "§9.2#r5": [22, 23]
  "§9.2#r6": 34
  "§9.2#r7": [40, 41]
  "§9.2#r8": [13, 15, 17]
  "§9.2#p6": [38, 40]
  "§9.2#b5": 38
  "§9.2#b78": 9
  "§9.2#b92": 35
  "§9.2#b109": 25
  "§9.2#b165": [34, 59]
  "§9.2#b183": 16
  "§9.2#b193": [48, 49]
  "§9.2#b200": 53
  "§9.4.2#r6": [37, 40]
  "§9.4.2#r56": [13, 16]
  "§9.4.2#r57": [14, 15]
  "§9.4.2#r110": 32
  "§9.4.2#r124": 25
  "§9.6#r11": 43
  "§9.7#r18": 27
  "§9.10.4#b3": [61, 63, 64, 66]
  "§4.4#r7": 43
  "§9.2#b86": [34, 35]
  "§9.2#b566": [70, 71, 73, 74]
---
# Penyelesaian nilai efektif menurut tingkat pewarisan

## Prerequisites
- Aktor: Maya Pengelola (DU-083-2), Total Control dengan cakupan seluruh entitas; pemanggil terotorisasi Rudi Integrasi (DU-083-3), Total Control dengan cakupan seluruh entitas; dan Operator Platform (DU-083-24), operator Admin Console di luar entitas.
- Data:
  - DU-083-1: Entitas, entitas khusus spec ini: Name `Entitas Resolusi {runId}`.
  - DU-083-2: User, pengelola yang menyimpan setting dan override: Name `Maya Pengelola {runId}`; Access Level `Total Control`; Cakupan `seluruh entitas`.
  - DU-083-3: User, pemanggil terotorisasi yang mengirim request langsung: Name `Rudi Integrasi {runId}`; Access Level `Total Control`; Cakupan `seluruh entitas`.
  - DU-083-4: Group, Group induk: Name `Proyek Karawang {runId}`; Parent `(tanpa induk)`.
  - DU-083-5: Group, Group turunan Proyek Karawang: Name `Workshop {runId}`; Parent `Proyek Karawang {runId}`.
  - DU-083-6: Group, Group terpisah: Name `Kantor Pusat {runId}`; Parent `(tanpa induk)`.
  - DU-083-7: Group, Group yang berstatus excess pada masa Grace: Name `Gudang Cadangan {runId}`; Parent `(tanpa induk)`.
  - DU-083-8: Category, Category leaf: Name `Pool car {runId}`.
  - DU-083-9: Category, Category leaf: Name `Machinery {runId}`.
  - DU-083-10: Category, Category leaf yang mewarisi seluruh nilai: Name `Elektronik {runId}`.
  - DU-083-11: Category, Category leaf yang mewarisi seluruh nilai: Name `Furnitur {runId}`.
  - DU-083-12: Asset, aset Pool car di Group induk: Name `Mobil Pool Karawang {runId}`; Asset Name `Mobil Pool Operasional {runId}`; Category `Pool car {runId}`; Group `Proyek Karawang {runId}`.
  - DU-083-13: Asset, aset Pool car di Group terpisah: Name `Mobil Pool Pusat {runId}`; Asset Name `Mobil Pool Operasional {runId}`; Category `Pool car {runId}`; Group `Kantor Pusat {runId}`.
  - DU-083-14: Asset, aset Pool car di Group turunan: Name `Mobil Pool Workshop {runId}`; Asset Name `Mobil Pool Operasional {runId}`; Category `Pool car {runId}`; Group `Workshop {runId}`.
  - DU-083-15: Asset, aset kategori lain di Group induk: Name `Laptop Karawang {runId}`; Asset Name `Laptop Kerja {runId}`; Category `Elektronik {runId}`; Group `Proyek Karawang {runId}`.
  - DU-083-16: Asset, aset kategori Elektronik di Group terpisah: Name `Laptop Pusat {runId}`; Asset Name `Laptop Kerja {runId}`; Category `Elektronik {runId}`; Group `Kantor Pusat {runId}`.
  - DU-083-17: Asset, aset Machinery di Group turunan: Name `Excavator Workshop {runId}`; Asset Name `Excavator Besar {runId}`; Category `Machinery {runId}`; Group `Workshop {runId}`.
  - DU-083-18: Asset, aset Machinery di Group terpisah: Name `Excavator Pusat {runId}`; Asset Name `Excavator Besar {runId}`; Category `Machinery {runId}`; Group `Kantor Pusat {runId}`.
  - DU-083-19: Asset, aset Furnitur di Group terpisah: Name `Kursi Pusat {runId}`; Asset Name `Kursi Kantor {runId}`; Category `Furnitur {runId}`; Group `Kantor Pusat {runId}`.
  - DU-083-20: Asset, aset di Group excess: Name `Rak Cadangan {runId}`; Asset Name `Rak Gudang {runId}`; Category `Elektronik {runId}`; Group `Gudang Cadangan {runId}`.
  - DU-083-21: Asset, aset Furnitur di Group induk: Name `Kursi Karawang {runId}`; Asset Name `Kursi Kantor {runId}`; Category `Furnitur {runId}`; Group `Proyek Karawang {runId}`.
  - DU-083-22: Category, Category leaf yang berstatus excess pada masa Grace: Name `Arsip Cadangan {runId}`.
  - DU-083-23: Asset, aset di Category excess: Name `Printer Cadangan {runId}`; Asset Name `Printer Arsip {runId}`; Category `Arsip Cadangan {runId}`; Group `Kantor Pusat {runId}`.
  - DU-083-24: User, operator Admin Console yang membaca nilai Approval Timeout platform: Name `Operator Platform {runId}`; Peran `operator Admin Console di luar entitas`.
  - DU-083-25: Group, Group tempat override All categories Deny dan override Category leaf Allow bertemu: Name `Gudang Utara {runId}`; Parent `(tanpa induk)`.
  - DU-083-26: Asset, aset Pool car di Group Gudang Utara: Name `Van Operasional Utara {runId}`; Asset Name `Van Antar Jemput {runId}`; Category `Pool car {runId}`; Group `Gudang Utara {runId}`.
  - Seluruh aset memakai Asset Name dan Category seperti di entri masing-masing, dan Asset Name `Mobil Pool Operasional {runId}` berada di Category `Pool car {runId}`.
- Kondisi:
  - Spec ini memakai entitas khusus `Entitas Resolusi {runId}` (DU-083-1) yang tidak dipakai spec lain, karena yang diasersi adalah setting Company default dan setting Category.
  - Transaksi yang diasersi di spec ini adalah Borrow; di langkah ia disebut «transaksi peminjaman».
  - Level Feature Suite Borrowing entitas bernilai `Full`.
  - Company default pada transaksi Borrow: Allow Borrow `Allow`, Max duration `14`, Duration unit `Days`, Photo at start `ON`, Photo at end `ON`, dan Transaction timeout `7`.
  - Category `Pool car {runId}` pada transaksi Borrow: Max duration nilai sendiri `7` dan Photo at end nilai sendiri `OFF`; field lainnya Inherit.
  - Category `Machinery {runId}` pada transaksi Borrow: Allow Borrow nilai sendiri `Deny`; field lainnya Inherit.
  - Category `Elektronik {runId}` dan `Furnitur {runId}` pada transaksi Borrow: seluruh field Inherit.
  - Belum ada override apa pun pada entitas ini.
  - Entitas berada pada masa Grace, Group `Gudang Cadangan {runId}` berstatus excess, dan Category `Arsip Cadangan {runId}` berstatus excess.
  - Category `Arsip Cadangan {runId}` pada transaksi Borrow: Max duration nilai sendiri `11`; field lainnya Inherit.
  - Nilai Approval Timeout platform adalah satu nilai milik platform yang dikonfigurasi di Admin Console tab Approval Settings (approval-foundation.md §1.7); spec ini tidak mengubahnya.
  - Addon Maintenance aktif pada entitas.
  - Pada tab Maintenance, Company default: Reminder before due `5`; Category `Pool car {runId}`: Reminder before due nilai sendiri `2`; Category `Elektronik {runId}`: Reminder before due Inherit.

## Test Steps

### Company default selalu bernilai dan Category leaf menimpa Company default
1. Verifikasi Company default memiliki nilai untuk setiap field peminjaman, termasuk Max duration `14`, tanpa mode Inherit
2. Verifikasi nilai efektif Max duration untuk aset `Laptop Pusat {runId}` adalah `14`, diwarisi dari Company default lewat Category `Elektronik {runId}` yang Inherit
3. Verifikasi nilai efektif Max duration untuk aset `Mobil Pool Pusat {runId}` adalah `7`, dari nilai sendiri Category leaf `Pool car {runId}`

### Group override mengalahkan Category leaf dan hanya menimpa field yang dimuatnya
4. Maya Pengelola menambahkan override Group `Proyek Karawang {runId}` untuk All categories pada transaksi peminjaman dengan Max duration `30` dan Photo at start `OFF`
5. Verifikasi nilai efektif Max duration untuk aset `Mobil Pool Karawang {runId}` adalah `30`
6. Verifikasi nilai efektif Max duration untuk aset `Mobil Pool Pusat {runId}` tetap `7`
7. Verifikasi nilai efektif Photo at start untuk aset `Mobil Pool Karawang {runId}` adalah `OFF`, dari override Group
8. Verifikasi nilai efektif Photo at end untuk aset `Mobil Pool Karawang {runId}` adalah `OFF`, diwarisi dari Category `Pool car {runId}`
9. Verifikasi nilai efektif Duration unit untuk aset `Mobil Pool Karawang {runId}` tetap `Days`, nilai Company default, karena override Group hanya memuat Max duration dan Photo at start
10. Verifikasi nilai efektif Photo at start untuk aset `Laptop Pusat {runId}` tetap `ON`, karena override Group tidak berlaku di luar Group-nya

### Group paling dalam menang dan cakupan Category memutus seri pada Group yang sama
11. Maya Pengelola menambahkan override Group `Workshop {runId}` untuk All categories pada transaksi peminjaman dengan Max duration `12`
12. Maya Pengelola menambahkan override Group `Proyek Karawang {runId}` untuk Category `Pool car {runId}` pada transaksi peminjaman dengan Max duration `20`
13. Verifikasi Add override untuk Category leaf `Pool car {runId}` pada Group yang sudah punya override All categories diterima, bukan ditolak sebagai duplikat, sehingga kedua override Group `Proyek Karawang {runId}` tersimpan
14. Verifikasi nilai efektif Max duration untuk aset `Mobil Pool Workshop {runId}` adalah `12`, karena override pada Group paling dalam menang atas override Group induk
15. Verifikasi nilai efektif Max duration untuk aset `Mobil Pool Karawang {runId}` adalah `20`, karena dua override pada Group yang sama diputus oleh cakupan Category
16. Verifikasi untuk field Max duration yang sama, override Category leaf menang atas override All categories pada target dan transaksi yang sama
17. Verifikasi nilai efektif Max duration untuk aset `Laptop Karawang {runId}` adalah `30`, dari override All categories

### Asset Name override kalah dari Group override yang lebih dekat ke aset
18. Maya Pengelola menambahkan override Asset Name `Mobil Pool Operasional {runId}` untuk All categories pada transaksi peminjaman dengan Max duration `10`
19. Verifikasi nilai efektif Max duration untuk aset `Mobil Pool Karawang {runId}` adalah `20`, karena override Group lebih dekat ke aset daripada override Asset Name
20. Verifikasi nilai efektif Max duration untuk aset `Mobil Pool Pusat {runId}` adalah `10`, dari override Asset Name

### Override aset adalah tingkat paling dekat ke aset
21. Maya Pengelola menambahkan override aset `Mobil Pool Karawang {runId}` untuk All categories pada transaksi peminjaman dengan Max duration `5`
22. Verifikasi nilai efektif Max duration untuk aset `Mobil Pool Karawang {runId}` adalah `5`
23. Verifikasi nilai efektif Max duration untuk aset `Laptop Karawang {runId}` tetap `30`, karena override aset hanya berlaku untuk asetnya

### Override yang dihapus membuat aset kembali mengikuti tingkat di atasnya
24. Maya Pengelola menghapus override aset `Mobil Pool Karawang {runId}` pada transaksi peminjaman
25. Verifikasi nilai efektif Max duration untuk aset `Mobil Pool Karawang {runId}` kembali `20`, mengikuti override Group di atasnya
26. Maya Pengelola menghapus override Group `Workshop {runId}` untuk All categories pada transaksi peminjaman
27. Verifikasi nilai efektif Max duration untuk aset `Mobil Pool Workshop {runId}` kembali `20`, mengikuti override Group `Proyek Karawang {runId}` untuk Category `Pool car {runId}`

### Deny pada Category, Allow pada Group, dan evaluasi ulang di server
28. Maya Pengelola menambahkan override Group `Workshop {runId}` untuk All categories pada transaksi peminjaman dengan Allow Borrow `Allow`
29. Verifikasi nilai efektif Allow Borrow untuk aset `Excavator Workshop {runId}` adalah `Allow`, sehingga peminjaman aset itu boleh
30. Verifikasi nilai efektif Allow Borrow untuk aset `Excavator Pusat {runId}` adalah `Deny`, sehingga peminjaman aset itu dilarang
31. Rudi Integrasi mengirim langsung pengajuan peminjaman atas aset `Excavator Pusat {runId}`
32. Verifikasi pengajuan itu ditolak server karena Deny pada Category dievaluasi ulang di server, tidak hanya disembunyikan di tampilan

### Deny pada override mengalahkan semua nilai lain
33. Maya Pengelola menambahkan override aset `Excavator Workshop {runId}` untuk All categories pada transaksi peminjaman dengan Allow Borrow `Deny`
34. Verifikasi nilai efektif Allow Borrow untuk aset `Excavator Workshop {runId}` adalah `Deny`, walau override Group `Workshop {runId}` bernilai `Allow`
35. Verifikasi aset `Excavator Workshop {runId}` tidak bisa dipinjam apa pun nilai di tingkat lain

### Nilai sendiri sama dengan warisan tetap nilai sendiri, dan Company default berubah
36. Maya Pengelola menyimpan Category `Furnitur {runId}` pada transaksi peminjaman dengan Max duration nilai sendiri `14`, sama dengan nilai Company default, lewat Save Changes
37. Verifikasi Save itu diproses sebagai perubahan nyata, bukan sebagai Save tanpa perubahan, karena perpindahan dari Inherit ke nilai sendiri dengan angka yang sama berselisih
38. Verifikasi Max duration Category `Furnitur {runId}` tersimpan sebagai nilai sendiri `14`, bukan Inherit
39. Maya Pengelola menyimpan Company default pada transaksi peminjaman dengan Max duration `21` lewat Save Changes
40. Verifikasi nilai efektif Max duration untuk aset `Kursi Pusat {runId}` tetap `14`, karena nilai sendiri tidak ikut berubah saat sumber warisannya berubah
41. Verifikasi nilai efektif Max duration untuk aset `Laptop Pusat {runId}` menjadi `21`, karena Category `Elektronik {runId}` yang Inherit ikut berubah
42. Rudi Integrasi mengirim langsung pengajuan peminjaman baru atas aset `Laptop Pusat {runId}`
43. Verifikasi pengajuan baru itu dievaluasi dengan Max duration `21`, karena Save yang berhasil berlaku untuk transaksi baru

### Duration unit diselesaikan sendiri per field
44. Maya Pengelola menyimpan Category `Elektronik {runId}` pada transaksi peminjaman dengan Duration unit nilai sendiri `Hours` lewat Save Changes
45. Verifikasi nilai efektif aset `Laptop Karawang {runId}` adalah Max duration `30` dengan Duration unit `Hours`, karena override Group hanya memuat Max duration dan Duration unit efektif aset diselesaikan sendiri dari Category
46. Maya Pengelola menyimpan Category `Elektronik {runId}` pada transaksi peminjaman dengan Duration unit nilai sendiri `Days` lewat Save Changes
47. Verifikasi nilai efektif aset `Laptop Karawang {runId}` adalah Max duration `30` yang kini dibaca dengan Duration unit `Days`

### Field khusus All categories memiliki satu nilai efektif per transaksi
48. Verifikasi nilai efektif Transaction timeout transaksi peminjaman adalah `7` untuk aset `Mobil Pool Karawang {runId}`, walau aset itu punya override Group dan override Asset Name
49. Verifikasi nilai efektif Transaction timeout transaksi peminjaman adalah `7` untuk aset `Excavator Pusat {runId}`, yang Category-nya berbeda
50. Operator Platform mencatat nilai Approval Timeout platform yang berlaku
51. Maya Pengelola menyimpan Company default pada transaksi peminjaman dengan Transaction timeout `5` lewat Save Changes
52. Verifikasi nilai efektif Transaction timeout transaksi peminjaman menjadi `5` untuk aset `Laptop Pusat {runId}` dan `Mobil Pool Karawang {runId}` sekaligus
53. Verifikasi nilai Approval Timeout platform yang dibaca kembali Operator Platform tetap sama dengan yang dicatat, karena Transaction timeout per transaksi tidak mengubah satu nilai Approval Timeout milik platform

### Deny pada override Group dan Asset Name mengalahkan Allow yang lebih dekat ke aset
54. Maya Pengelola menambahkan override aset `Mobil Pool Pusat {runId}` untuk All categories pada transaksi peminjaman dengan Allow Borrow `Allow`
55. Maya Pengelola menambahkan override Group `Kantor Pusat {runId}` untuk All categories pada transaksi peminjaman dengan Allow Borrow `Deny`
56. Verifikasi nilai efektif Allow Borrow untuk aset `Mobil Pool Pusat {runId}` adalah `Deny`, walau override aset lebih dekat ke aset dan bernilai `Allow`
57. Maya Pengelola menambahkan override aset `Kursi Karawang {runId}` untuk All categories pada transaksi peminjaman dengan Allow Borrow `Allow`
58. Maya Pengelola menambahkan override Asset Name `Kursi Kantor {runId}` untuk All categories pada transaksi peminjaman dengan Allow Borrow `Deny`
59. Verifikasi nilai efektif Allow Borrow untuk aset `Kursi Karawang {runId}` adalah `Deny`, karena override Asset Name bernilai `Deny` walau override aset lebih dekat ke aset dan bernilai `Allow`, dan Group `Proyek Karawang {runId}` tidak punya override `Deny`

### Setting dan override pada Group excess dievaluasi seperti biasa
60. Maya Pengelola menambahkan override Group `Gudang Cadangan {runId}` untuk All categories pada transaksi peminjaman dengan Max duration `9`, walau Group itu berstatus excess
61. Verifikasi nilai efektif Max duration untuk aset `Rak Cadangan {runId}` adalah `9`, karena status excess Group tidak membatasi evaluasi override
62. Status excess Group `Gudang Cadangan {runId}` dilepas karena jumlah Group tidak lagi melebihi cap plan aktif
63. Verifikasi nilai efektif Max duration untuk aset `Rak Cadangan {runId}` tetap `9`, karena evaluasi tidak berubah saat status excess dilepas

### Setting Category excess dievaluasi seperti biasa
64. Verifikasi nilai efektif Max duration untuk aset `Printer Cadangan {runId}` adalah `11`, dari nilai sendiri Category `Arsip Cadangan {runId}` yang berstatus excess
65. Status excess Category `Arsip Cadangan {runId}` dilepas karena jumlah Category tidak lagi melebihi cap plan aktif
66. Verifikasi nilai efektif Max duration untuk aset `Printer Cadangan {runId}` tetap `11`, karena evaluasi tidak berubah saat status excess dilepas

### Deny pada override All categories mengalahkan Allow pada override Category leaf
67. Maya Pengelola menambahkan override Group `Gudang Utara {runId}` untuk Category `Pool car {runId}` pada transaksi peminjaman dengan Allow Borrow `Allow`
68. Maya Pengelola menambahkan override Group `Gudang Utara {runId}` untuk All categories pada transaksi peminjaman dengan Allow Borrow `Deny`
69. Verifikasi nilai efektif Allow Borrow untuk aset `Van Operasional Utara {runId}` adalah `Deny`, karena override All categories bernilai Deny mengalahkan override Category leaf `Pool car {runId}` pada Group dan transaksi yang sama walau Category leaf lebih spesifik dan bernilai `Allow`

### Nilai efektif tab Maintenance per aset diselesaikan dari Category leaf lalu Company default
70. Verifikasi nilai efektif Reminder before due untuk aset `Mobil Pool Pusat {runId}` adalah `2`, dari nilai sendiri Category leaf `Pool car {runId}` dan bukan Company default `5`
71. Verifikasi nilai efektif Reminder before due untuk aset `Laptop Pusat {runId}` adalah `5`, diwarisi dari Company default lewat Category `Elektronik {runId}` yang Inherit
72. Maya Pengelola menyimpan Company default pada tab Maintenance dengan Reminder before due `9` lewat Save Changes
73. Verifikasi nilai efektif Reminder before due untuk aset `Laptop Pusat {runId}` menjadi `9`, karena Category `Elektronik {runId}` yang Inherit ikut berubah
74. Verifikasi nilai efektif Reminder before due untuk aset `Mobil Pool Pusat {runId}` tetap `2`, karena nilai sendiri Category leaf tidak ikut berubah saat Company default berubah
