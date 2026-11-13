---
id: TC-FA-FAREG-UI-017-form-tab-asset-tampilan
title: "Form Register Asset: tab Asset, tabel Asset per Item, badge, dan kartu filter"
layer: ui-client
priority: Critical
caseType: Positive
status: draft
sourceRules: ["F-FAREG-04", "F-FAREG-15", "FAREG-LOGIC-04b", "FAREG-LOGIC-11e", "FAREG-LOGIC-17a", "FLD-REG-06", "S-REG-06", "§4.1#b21", "§4.1#b22", "§4.1#b23", "§4.1#b24", "§4.1#b28", "§4.1#p28", "§4.1#r98", "§4.1#r99", "§4.1#r100", "§4.1#r102", "§4.1#r103", "§4.1#r104", "§4.1#r105", "§4.4#r9", "§4.5#p1", "§9.9#r7"]
smoke: []
dependsOn: []
trace:
  "F-FAREG-04": [32, 35]
  "F-FAREG-15": [12, 13, 14]
  "FAREG-LOGIC-04b": [14, 67]
  "FAREG-LOGIC-11e": [31, 32, 33]
  "FAREG-LOGIC-17a": [12, 15]
  "FLD-REG-06": [23, 24]
  "S-REG-06": [70, 71, 75, 76]
  "§4.1#b21": 3
  "§4.1#b22": [3, 4, 5, 6, 7]
  "§4.1#b23": [8, 9]
  "§4.1#b24": [38, 39, 40, 41]
  "§4.1#b28": 57
  "§4.1#p28": [3, 26, 28, 43, 44, 46, 47, 50, 51, 52, 53, 55]
  "§4.1#r98": 8
  "§4.1#r99": [10, 11]
  "§4.1#r100": [12, 13, 14, 15]
  "§4.1#r102": [16, 17]
  "§4.1#r103": [18, 23]
  "§4.1#r104": [31, 32, 33, 35]
  "§4.1#r105": 19
  "§4.4#r9": 37
  "§4.5#p1": [31, 62, 64]
  "§9.9#r7": 23
anchor: [59, 61]
coverage:
  web: automated
---

# Form Register Asset: tab Asset, tabel Asset per Item, badge, dan kartu filter

## Prerequisites
- Aktor: Total Control.
- Layar awal: Assets > Registration > Draft
- Komponen: Halaman `Register Asset`
- Data:
  - DU-017-1: Item `Laptop Dell Latitude 5440`, TAG Type `RFID`, Quantity `3`, Custom field per aset `Serial Number` (teks, wajib); aset `Laptop Dell Latitude 5440 - 1` ber-Serial Number `SN-LDL-0001`, Tag `RFID-000201` Verified, Photo `2`, Condition `Normal`, Status `✓ Ready`; aset `Laptop Dell Latitude 5440 - 2` tanpa Serial Number dan tanpa Tag, Photo `1`, Condition `Normal`, kekurangan `Serial Number` dan `Tag` sehingga Status `Serial Number` dengan `+1`; aset `Laptop Dell Latitude 5440 - 3` ber-Serial Number `SN-LDL-0003`, tanpa Tag, tanpa Photo, Condition `Normal`, kekurangan `Tag` saja.
  - DU-017-2: Item `Kursi Kerja Ergonomis`, TAG Type `QR`, Quantity `2`, tanpa Custom field per aset; aset `Kursi Kerja Ergonomis - 1` ber-Tag `QR-000301` dan aset `Kursi Kerja Ergonomis - 2` ber-Tag `QR-000302`, keduanya Condition `Normal` dan Ready.
  - DU-017-3: Item `Printer Epson L3250`, TAG Type `RFID`, Quantity `2`, Custom field per aset `Tanggal Garansi` (tanggal) dan `Jenis Tinta` (pilihan, placeholder `Select Jenis Tinta`); aset `Printer Epson L3250 - 1` ber-Tag `RFID-000401`, Tanggal Garansi `15/11/2026`, Jenis Tinta `Black`, Condition `Normal`, Ready; aset `Printer Epson L3250 - 2` tanpa Tag, tanpa Tanggal Garansi, tanpa Jenis Tinta, Condition `Normal`, kekurangan `Tag`.
  - DU-017-4: Item `Meja Lipat Aluminium`, TAG Type `Non-TAG`, Quantity `1`; aset `Meja Lipat Aluminium - 1`.
  - DU-017-5: Item `Laptop Dell Latitude 5440` dengan 12 aset bernama `Laptop Dell Latitude 5440 - 1` sampai `Laptop Dell Latitude 5440 - 12`.
- Kondisi:
  - K1: form `Edit` draft tersimpan dengan Item DU-017-1, DU-017-2, dan DU-017-3; format tanggal General Settings `DD/MM/YYYY`; kartu filter berjumlah `All` 7, `Needs data` 3, `Ready` 4.
  - K2: form `Edit` draft tersimpan dengan Item DU-017-4 dan DU-017-2.
  - K3: form `Register Asset` baru tanpa Asset Name yang dipilih.
  - K4: form `Edit` draft tersimpan dengan Item DU-017-2 saja.
  - K5: form `Edit` draft tersimpan dengan Item DU-017-5.

## Test Steps
### Accordion per Item, badge, dan kolom tabel aset
1. Tampilkan Halaman `Register Asset` dengan kondisi K1
2. Klik tab `Asset`
3. Verifikasi judul Item `Laptop Dell Latitude 5440`, `Kursi Kerja Ergonomis`, dan `Printer Epson L3250` tampil sebagai Accordion per Item
4. Verifikasi judul Item `Laptop Dell Latitude 5440` memuat badge `Incomplete`
5. Verifikasi judul Item `Kursi Kerja Ergonomis` memuat badge `Complete`
6. Verifikasi tooltip `2 assets still need data.` tampil saat pointer berada di badge `Incomplete` Item `Laptop Dell Latitude 5440`
7. Verifikasi tooltip `1 asset still needs data.` tampil saat pointer berada di badge `Incomplete` Item `Printer Epson L3250`
8. Verifikasi kolom `#` menampilkan nomor urut `1`, `2`, dan `3` pada tabel Item `Laptop Dell Latitude 5440`
9. Verifikasi tabel aset tidak memiliki checkbox
10. Verifikasi kolom `Name` menampilkan `Laptop Dell Latitude 5440 - 1`
11. Verifikasi kolom `Name` terisi pada `Laptop Dell Latitude 5440 - 2` dan `Laptop Dell Latitude 5440 - 3`
12. Verifikasi kolom `Serial Number` pada `Laptop Dell Latitude 5440 - 2` menampilkan placeholder `Enter value`
13. Verifikasi kolom `Tanggal Garansi` pada `Printer Epson L3250 - 2` menampilkan placeholder `Select date`
14. Verifikasi kolom `Jenis Tinta` pada `Printer Epson L3250 - 2` menampilkan placeholder `Select Jenis Tinta`
15. Verifikasi tabel Item `Kursi Kerja Ergonomis` tidak memiliki kolom Custom field per aset
16. Verifikasi kolom `Photo` pada `Laptop Dell Latitude 5440 - 1` menampilkan `2`
17. Verifikasi kolom `Photo` pada `Laptop Dell Latitude 5440 - 3` menampilkan `—`
18. Verifikasi kolom `Condition` pada `Laptop Dell Latitude 5440 - 1` menampilkan `Normal` tanpa placeholder
19. Verifikasi row option (titik tiga) pada `Laptop Dell Latitude 5440 - 1` memuat `Detail`

### Condition dan Custom field per aset dapat diedit
20. Tampilkan Halaman `Register Asset` dengan kondisi K1
21. Klik tab `Asset`
22. Klik sel `Condition` pada `Laptop Dell Latitude 5440 - 1`
23. Verifikasi opsi `Normal` dan `Damaged` tampil di dropdown `Condition`
24. Verifikasi opsi `Missing` tidak tampil di dropdown `Condition`
25. Klik `Damaged`
26. Verifikasi sel `Condition` pada `Laptop Dell Latitude 5440 - 1` menampilkan `Damaged`
27. Ganti isi sel `Serial Number` pada `Laptop Dell Latitude 5440 - 2` dengan `SN-LDL-0002`
28. Verifikasi sel `Serial Number` pada `Laptop Dell Latitude 5440 - 2` menampilkan `SN-LDL-0002`

### Kolom Status, daftar kekurangan, dan kartu filter
29. Tampilkan Halaman `Register Asset` dengan kondisi K1
30. Klik tab `Asset`
31. Verifikasi Status `Laptop Dell Latitude 5440 - 1` menampilkan teks `✓ Ready`
32. Verifikasi Status `Laptop Dell Latitude 5440 - 2` menampilkan kekurangan pertama `Serial Number` dan `+1`
33. Verifikasi Status `Laptop Dell Latitude 5440 - 3` menampilkan `Tag` tanpa `+N`
34. Arahkan pointer ke Status `Laptop Dell Latitude 5440 - 2`
35. Verifikasi daftar kekurangan lengkap `Serial Number` dan `Tag` tampil pada hover Status
36. Klik `+1` pada Status `Laptop Dell Latitude 5440 - 2`
37. Verifikasi popover daftar kekurangan lengkap memuat `Serial Number` dan `Tag`
38. Verifikasi kartu filter `All`, `Needs data`, dan `Ready` tampil
39. Verifikasi kartu `All` menampilkan jumlah `7`
40. Verifikasi kartu `Needs data` menampilkan jumlah `3`
41. Verifikasi kartu `Ready` menampilkan jumlah `4`
42. Klik kartu `Needs data`
43. Verifikasi tabel memuat `Laptop Dell Latitude 5440 - 2`, `Laptop Dell Latitude 5440 - 3`, dan `Printer Epson L3250 - 2`
44. Verifikasi `Laptop Dell Latitude 5440 - 1` tidak tampil di tabel
45. Klik kartu `Ready`
46. Verifikasi tabel memuat `Laptop Dell Latitude 5440 - 1`
47. Verifikasi `Laptop Dell Latitude 5440 - 2` tidak tampil di tabel

### Tabel aset memakai paginasi tanpa colvis, Search, filter, dan sort
48. Tampilkan Halaman `Register Asset` dengan kondisi K5
49. Klik tab `Asset`
50. Verifikasi paginasi menawarkan `10`, `25`, `50`, dan `100`
51. Verifikasi kontrol column visibility tidak tampil pada tabel aset
52. Verifikasi kotak Search tidak tampil pada tabel aset
53. Verifikasi filter selain kartu filter tidak tampil pada tabel aset
54. Klik header kolom `Name`
55. Verifikasi urutan aset tetap `Laptop Dell Latitude 5440 - 1`, `Laptop Dell Latitude 5440 - 2`, `Laptop Dell Latitude 5440 - 3` dari atas

### Accordion dapat dilipat dengan keyboard
56. Tampilkan Halaman `Register Asset` dengan kondisi K1
57. Verifikasi tabel General Information tidak memuat kolom `Condition`
58. Klik tab `Asset`
59. Verifikasi baris `Laptop Dell Latitude 5440 - 1` tampil
60. Tekan `Enter` pada judul Item `Laptop Dell Latitude 5440`
61. Verifikasi judul Item `Laptop Dell Latitude 5440` tetap tampil
62. Verifikasi baris `Laptop Dell Latitude 5440 - 1` tidak tampil karena Accordion dilipat
63. Tekan `Enter` pada judul Item `Laptop Dell Latitude 5440`
64. Verifikasi baris `Laptop Dell Latitude 5440 - 1` tampil kembali

### Item TAG Type Non-TAG tidak memiliki slot Tag
65. Tampilkan Halaman `Register Asset` dengan kondisi K2
66. Klik tab `Asset`
67. Verifikasi kolom Tag pada `Meja Lipat Aluminium - 1` menampilkan `No tag`

### Empty state tab Asset dan hasil saring kosong
68. Tampilkan Halaman `Register Asset` dengan kondisi K3
69. Klik tab `Asset`
70. Verifikasi tab `Asset` menampilkan `No assets yet`
71. Verifikasi tab `Asset` menampilkan `Select an Asset Name in General Information to see the assets here.`
72. Tampilkan Halaman `Register Asset` dengan kondisi K4
73. Klik tab `Asset`
74. Klik kartu `Needs data`
75. Verifikasi tabel menampilkan `No results found`
76. Verifikasi tabel menampilkan `Try adjusting your search or filter.`
