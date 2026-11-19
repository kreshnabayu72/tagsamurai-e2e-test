---
id: TC-FA-BORROW-UI-066-dialog-mark-as-returned
title: "Dialog Mark as Returned: pilihan hasil, satu aset dan bulk, serta caption skipped"
layer: ui-client
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["D-BRW-25", "DM-BRW-16", "FLD-BRW-14", "FLD-BRW-15"]
smoke: []
dependsOn: []
trace:
  "D-BRW-25": [2, 3, 4, 5, 7, 8, 14, 15, 17, 18, 19, 20, 22, 23, 24, 26, 28, 29, 42, 43, 44, 46, 47, 48, 50, 51]
  "DM-BRW-16": [37, 40]
  "FLD-BRW-14": [5, 6, 10, 12, 18]
  "FLD-BRW-15": [32, 34]
anchor: []
coverage:
  web: automated
---

# Dialog Mark as Returned: pilihan hasil, satu aset dan bulk, serta caption skipped

## Prerequisites
- Aktor: Aktor Borrow `Rina W` dengan cakupan Group `Finance`, level Borrowing bernilai `None`.
- Layar awal: Daftar aset di Asset List
- Komponen: Dialog Mark as Returned
- Data:
  - DU-066-1: aset Borrowed, Name `Laptop Dell Latitude 5420 - 8`, Borrower `Budi Santoso`, Due Date `10/12/2026`.
  - DU-066-2: aset Borrowed yang lewat Due Date, Name `Printer Epson L3110 - 1`, Borrower `Sari Wulandari`, Due Date `05/11/2026`.
  - DU-066-3: aset Borrowed untuk bulk, Name `Kamera Canon EOS 200D`, Borrower `Budi Santoso`.
  - DU-066-4: aset Borrowed untuk bulk, Name `Speaker JBL PartyBox`, Borrower `Sari Wulandari`.
  - DU-066-5: aset Borrowed untuk bulk, Name `Drone DJI Mini 3`, Borrower `Budi Santoso`.
  - DU-066-6: aset terpilih yang bukan Borrowed, Name `Scanner Fujitsu fi-7160`, Custody `Available`.
  - DU-066-7: aset terpilih yang bukan Borrowed, Name `Monitor LG 24MK430`, Custody `Available`.
  - DU-066-8: aset terpilih yang Aktor sendiri Borrower-nya, Name `Genset Honda EU20i - 1`, Borrower `Rina W`.
  - DU-066-9: aset terpilih yang Aktor sendiri Borrower-nya, Name `Forklift Toyota 8FD - 1`, Borrower `Rina W`.
- Kondisi:
  - K1: Date Format bernilai `DD/MM/YYYY`, tanggal hari ini `18/11/2026`, dialog dibuka untuk satu aset DU-066-1.
  - K2: Date Format bernilai `DD/MM/YYYY`, tanggal hari ini `18/11/2026`, dialog dibuka untuk satu aset DU-066-2 yang lewat Due Date.
  - K3: dialog dibuka untuk bulk DU-066-3, DU-066-4, dan DU-066-5.
  - K4: dialog dibuka untuk bulk DU-066-3 dan DU-066-4 bersama DU-066-6, DU-066-7, DU-066-8, dan DU-066-9 dalam pilihan.
  - K5: pilihan bulk hanya berisi DU-066-8 dan DU-066-9, yaitu aset yang Aktor sendiri Borrower-nya.
  - K6: aksi `Mark as Returned` dibuka dari baris aset DU-066-8 yang Aktor sendiri Borrower-nya.
  - K7: dialog dibuka untuk satu aset DU-066-1, lalu dikonfirmasi dan berhasil.
  - K8: dialog dibuka untuk bulk DU-066-3, DU-066-4, dan DU-066-5, lalu dikonfirmasi dan berhasil.
  - K9: dialog dibuka untuk bulk DU-066-3 dan DU-066-4 bersama DU-066-6 dan DU-066-7 dalam pilihan, tanpa aset milik Aktor sendiri.
  - K10: dialog dibuka untuk bulk DU-066-3 dan DU-066-4 bersama DU-066-8 dan DU-066-9 dalam pilihan, tanpa aset yang bukan Borrowed.

## Test Steps

### Dialog Mark as Returned untuk satu aset
1. Tampilkan Dialog Mark as Returned dengan kondisi K1
2. Verifikasi judul dialog `Mark as Returned` tampil
3. Verifikasi dialog menampilkan nama aset `Laptop Dell Latitude 5420 - 8`, Borrower `Budi Santoso`, dan Due date `10/12/2026`
4. Verifikasi badge `Overdue` tidak tampil di samping Due date `10/12/2026`
5. Verifikasi pilihan hasil `Returned`, `Missing`, dan `Damaged` tampil
6. Verifikasi pilihan `Returned` terpilih sebagai default
7. Verifikasi dialog tidak memuat field scan dan field foto
8. Verifikasi tombol `[Cancel]` dan `[Mark as Returned]` tampil
9. Klik pilihan `Missing`
10. Verifikasi pilihan `Missing` terpilih dan `Returned` tidak terpilih
11. Klik pilihan `Damaged`
12. Verifikasi pilihan `Damaged` terpilih dan `Missing` tidak terpilih

### Satu aset yang lewat Due date
13. Tampilkan Dialog Mark as Returned dengan kondisi K2
14. Verifikasi dialog menampilkan Due date `05/11/2026` untuk aset `Printer Epson L3110 - 1`
15. Verifikasi badge `Overdue` tampil di samping Due date `05/11/2026`

### Dialog Mark as Returned untuk bulk
16. Tampilkan Dialog Mark as Returned dengan kondisi K3
17. Verifikasi daftar aset yang diproses memuat `Kamera Canon EOS 200D`, `Speaker JBL PartyBox`, dan `Drone DJI Mini 3`
18. Verifikasi dialog bulk tidak menampilkan pilihan hasil `Missing` dan `Damaged`
19. Verifikasi field Reason tampil sebagai field opsional pada dialog bulk
20. Verifikasi tombol `[Cancel]` dan `[Mark as Returned]` tampil pada dialog bulk

### Caption aset yang dilewati
21. Tampilkan Dialog Mark as Returned dengan kondisi K4
22. Verifikasi daftar aset yang diproses memuat `Kamera Canon EOS 200D` dan `Speaker JBL PartyBox`
23. Verifikasi caption `2 assets skipped because they aren't borrowed.` tampil
24. Verifikasi caption `2 assets skipped because they're yours.` tampil sebagai baris kedua

### Semua aset terpilih milik Aktor sendiri
25. Tampilkan Dialog Mark as Returned dengan kondisi K5
26. Verifikasi dialog `Mark as Returned` tidak terbuka karena semua aset terpilih milik Aktor sendiri

### Aksi Disabled pada aset milik Aktor sendiri
27. Tampilkan Dialog Mark as Returned dengan kondisi K6
28. Verifikasi aksi `Mark as Returned` pada baris `Genset Honda EU20i - 1` disabled
29. Verifikasi tooltip `You can't return your own borrowed asset.` tersampaikan pada aksi `Mark as Returned` yang disabled

### Batas karakter Reason
30. Tampilkan Dialog Mark as Returned dengan kondisi K1
31. Isi Reason dengan `Layar monitor retak setelah terjatuh saat dipindahkan dari ruang rapat lantai dua menuju gudang pusat untuk diperiksa teknisi Layar monitor retak setelah terjatuh saat dipindahkan dari ruang rapat lantai dua menuju gudang pusat untuk diperiksa teknisi Layar monitor retak setelah terjatuh saat dipindahkan dari ruang rapat lantai dua menuju gudang pusat untuk.` (360 karakter)
32. Verifikasi Reason berisi seluruh teks `Layar monitor retak setelah terjatuh saat dipindahkan dari ruang rapat lantai dua menuju gudang pusat untuk diperiksa teknisi Layar monitor retak setelah terjatuh saat dipindahkan dari ruang rapat lantai dua menuju gudang pusat untuk diperiksa teknisi Layar monitor retak setelah terjatuh saat dipindahkan dari ruang rapat lantai dua menuju gudang pusat untuk.` (360 karakter)
33. Ganti isi Reason dengan `Layar monitor retak setelah terjatuh saat dipindahkan dari ruang rapat lantai dua menuju gudang pusat untuk diperiksa teknisi Layar monitor retak setelah terjatuh saat dipindahkan dari ruang rapat lantai dua menuju gudang pusat untuk diperiksa teknisi Layar monitor retak setelah terjatuh saat dipindahkan dari ruang rapat lantai dua menuju gudang pusat untuk..` (361 karakter)
34. Verifikasi Reason dipotong pada batas menjadi `Layar monitor retak setelah terjatuh saat dipindahkan dari ruang rapat lantai dua menuju gudang pusat untuk diperiksa teknisi Layar monitor retak setelah terjatuh saat dipindahkan dari ruang rapat lantai dua menuju gudang pusat untuk diperiksa teknisi Layar monitor retak setelah terjatuh saat dipindahkan dari ruang rapat lantai dua menuju gudang pusat untuk.` (360 karakter)

### Hasil Mark as Returned untuk satu aset
35. Tampilkan Dialog Mark as Returned dengan kondisi K7
36. Klik `[Mark as Returned]`
37. Verifikasi toast `Success, asset has been marked as returned.` tampil

### Hasil Mark as Returned untuk bulk
38. Tampilkan Dialog Mark as Returned dengan kondisi K8
39. Klik `[Mark as Returned]`
40. Verifikasi toast `Success, 3 assets have been marked as returned.` tampil

### Caption hanya untuk aset yang bukan Borrowed
41. Tampilkan Dialog Mark as Returned dengan kondisi K9
42. Verifikasi daftar aset yang diproses memuat `Kamera Canon EOS 200D` dan `Speaker JBL PartyBox`
43. Verifikasi caption `2 assets skipped because they aren't borrowed.` tampil
44. Verifikasi caption `2 assets skipped because they're yours.` tidak tampil

### Caption hanya untuk aset milik Aktor sendiri
45. Tampilkan Dialog Mark as Returned dengan kondisi K10
46. Verifikasi daftar aset yang diproses memuat `Kamera Canon EOS 200D` dan `Speaker JBL PartyBox`
47. Verifikasi caption `2 assets skipped because they're yours.` tampil
48. Verifikasi caption `2 assets skipped because they aren't borrowed.` tidak tampil

### Tanpa caption bila semua aset terpilih Borrowed
49. Tampilkan Dialog Mark as Returned dengan kondisi K3
50. Verifikasi daftar aset yang diproses memuat `Kamera Canon EOS 200D`, `Speaker JBL PartyBox`, dan `Drone DJI Mini 3`
51. Verifikasi dialog bulk tidak menampilkan caption skipped
