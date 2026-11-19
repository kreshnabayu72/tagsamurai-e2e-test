---
id: TC-FA-ASTL-UI-073-dialog-edit-purchase-warranty
title: "Validasi daftar Warranty dan field teks"
layer: ui-client
priority: Medium
caseType: Negative
status: ready-for-automation
sourceRules: ["ASTL-LOGIC-21c", "FI-09", "V-06", "V-10", "V-13", "FLD-30", "FLD-31", "FLD-32", "§4.1i#b5", "§9.9#r4", "§9.9#r5", "§9.9#r6", "EB-FRM-4@edit-purchase"]
smoke: []
dependsOn: []
trace:
  "ASTL-LOGIC-21c": [23, 26, 50, 51, 52, 56, 57, 63]
  "FI-09": [4, 6, 44, 46]
  "V-06": [10, 11, 17, 46]
  "V-10": [23, 26, 50, 51, 56, 57, 63]
  "V-13": [40, 67]
  "FLD-30": 4
  "FLD-31": 4
  "FLD-32": 4
  "§4.1i#b5": [2, 4, 6]
  "§9.9#r4": [10, 17, 30, 32, 34]
  "§9.9#r5": [11, 23]
  "§9.9#r6": [38, 40, 42]
  "EB-FRM-4@edit-purchase": [30, 32, 38, 40]
anchor: []
coverage:
  web: automated
---
# Validasi daftar Warranty dan field teks

## Prerequisites
- Aktor: Total Control.
- Layar awal: Fixed Asset > Assets > All Assets.
- Komponen: Dialog Edit Purchase
- Data:
  - DU-073-1: Aset `Monitor Dell 24 - 1`, Asset ID `AST-0090`, Group `IT`, Purchase Date `10/03/26`, Warranty `Garansi baterai` sampai `10/03/27` Provider `Dell Service`.
  - DU-073-2: Aset `Monitor Dell 24 - 2`, Asset ID `AST-0091`, Group `IT`, sembilan Warranty dengan pola nama `Garansi komponen {n}`.
  - DU-073-3: Aset `Laptop Pro 16 - 2`, Asset ID `AST-0002`, Group `IT`, Purchase Date tersimpan `10/03/26`, Warranty tersimpan yang berakhir `20/05/26`.
  - DU-073-4: Aset `Laptop Pro 16 - 3`, Asset ID `AST-0003`, Group `IT`, Purchase Date tersimpan `10/03/26`, Warranty tersimpan yang berakhir `25/05/26`.
  - DU-073-5: Warranty baru dengan nama sama berbeda huruf besar-kecil `garansi baterai` sampai `10/03/28`.
  - DU-073-6: Warranty baru `Garansi layar` dengan Warranty until sebelum Purchase Date `09/03/26`.
  - DU-073-7: Warranty until tepat pada Purchase Date `10/03/26`.
  - DU-073-8: Warranty name tepat di batas `Garansi BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB` (100 karakter).
  - DU-073-9: Warranty name satu di atas batas `Garansi BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB` (101 karakter).
  - DU-073-10: Warranty name berisi emoji `Garansi😊`, yang diharapkan tersimpan di field `Garansi`.
  - DU-073-11: Provider tepat di batas `Dell Service CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC` (120 karakter).
  - DU-073-12: Provider satu di atas batas `Dell Service CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC` (121 karakter).
  - DU-073-13: Provider berisi emoji `Dell😊Service`, yang diharapkan tersimpan di field `DellService`.
  - DU-073-14: Purchase Date baru `01/06/26`.
  - Alert yang diharapkan: `Laptop Pro 16 - 2 has a warranty that ends before the new purchase date.` dan `Laptop Pro 16 - 3 has a warranty that ends before the new purchase date.`, dari nama aset DU-073-3 dan DU-073-4.
- Kondisi:
  - K1: satu aset terpilih, DU-073-1; simpan berhasil.
  - K2: satu aset terpilih, DU-073-2; batas baris Warranty adalah 10.
  - K4: satu aset terpilih, DU-073-3; simpan ditolak server karena Purchase Date baru membuat Warranty tersimpan aset itu berakhir sebelum Purchase Date.
  - K5: Bulk, seleksi DU-073-3 dan DU-073-4.
  - K3: Bulk, seleksi DU-073-3 dan DU-073-4; simpan ditolak server karena Purchase Date baru membuat Warranty tersimpan kedua aset itu berakhir sebelum Purchase Date.

## Test Steps

### Menambah dan menghapus baris Warranty
1. Tampilkan Dialog Edit Purchase dengan kondisi K1
2. Verifikasi daftar Warranty memuat baris `Garansi baterai` sampai `10/03/27` dengan Provider `Dell Service`
3. Klik `[+ Add warranty]`
4. Verifikasi baris baru bertambah dengan field `Warranty name` ber-placeholder `Enter warranty name`, `Warranty until` ber-placeholder `Select date`, dan `Provider` ber-placeholder `Enter provider`
5. Klik `✕` pada baris baru
6. Verifikasi baris baru hilang dan baris `Garansi baterai` tetap ada

### Warranty name dan Warranty until wajib diisi
7. Tampilkan Dialog Edit Purchase dengan kondisi K1
8. Klik `[+ Add warranty]`
9. Klik `[Save]`
10. Verifikasi pesan `Warranty name must not be empty` tampil di bawah field Warranty name baris baru
11. Verifikasi pesan `Warranty until must not be empty` tampil di bawah field Warranty until baris baru

### Warranty name harus unik per aset tanpa membedakan huruf besar-kecil
12. Tampilkan Dialog Edit Purchase dengan kondisi K1
13. Klik `[+ Add warranty]`
14. Isi Warranty name `garansi baterai`
15. Pilih Warranty until `10/03/28`
16. Klik `[Save]`
17. Verifikasi pesan `Warranty name already exists` tampil di bawah field Warranty name baris baru

### Warranty until tidak boleh sebelum Purchase Date
18. Tampilkan Dialog Edit Purchase dengan kondisi K1
19. Klik `[+ Add warranty]`
20. Isi Warranty name `Garansi layar`
21. Pilih Warranty until `09/03/26`
22. Klik `[Save]`
23. Verifikasi pesan `Warranty until cannot be before purchase date` tampil di bawah field Warranty until baris baru
24. Pilih Warranty until `10/03/26`
25. Klik `[Save]`
26. Verifikasi dialog `Edit Purchase` tertutup

### Batas 100 karakter dan emoji pada Warranty name
27. Tampilkan Dialog Edit Purchase dengan kondisi K1
28. Klik `[+ Add warranty]`
29. Isi Warranty name `Garansi BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB` (100 karakter)
30. Verifikasi field Warranty name menerima nilai tanpa pesan `Max. 100 characters`
31. Isi Warranty name `Garansi BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB` (101 karakter)
32. Verifikasi pesan `Max. 100 characters` tampil di bawah field Warranty name
33. Isi Warranty name `Garansi😊`
34. Verifikasi field Warranty name berisi `Garansi` karena emoji diblok di input

### Batas 120 karakter dan emoji pada Provider
35. Tampilkan Dialog Edit Purchase dengan kondisi K1
36. Klik `[+ Add warranty]`
37. Isi Provider `Dell Service CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC` (120 karakter)
38. Verifikasi field Provider menerima nilai tanpa pesan `Max. 120 characters`
39. Isi Provider `Dell Service CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC` (121 karakter)
40. Verifikasi pesan `Max. 120 characters` tampil di bawah field Provider
41. Isi Provider `Dell😊Service`
42. Verifikasi field Provider berisi `DellService` karena emoji diblok di input

### Batas jumlah baris Warranty
43. Tampilkan Dialog Edit Purchase dengan kondisi K2
44. Verifikasi `[+ Add warranty]` aktif pada sembilan baris Warranty
45. Klik `[+ Add warranty]`
46. Verifikasi `[+ Add warranty]` Disabled pada sepuluh baris Warranty

### Penolakan server karena Warranty tersimpan berakhir sebelum Purchase Date baru
47. Tampilkan Dialog Edit Purchase dengan kondisi K3
48. Pilih Purchase Date `01/06/26`
49. Klik `[Save]`
50. Verifikasi alert inline `Laptop Pro 16 - 2 has a warranty that ends before the new purchase date.` tampil
51. Verifikasi alert inline `Laptop Pro 16 - 3 has a warranty that ends before the new purchase date.` tampil
52. Verifikasi dialog `Edit Purchase` tetap terbuka

### Penolakan server satu aset karena Warranty tersimpan berakhir sebelum Purchase Date baru
53. Tampilkan Dialog Edit Purchase dengan kondisi K4
54. Pilih Purchase Date `01/06/26`
55. Klik `[Save]`
56. Verifikasi alert inline `Laptop Pro 16 - 2 has a warranty that ends before the new purchase date.` tampil
57. Verifikasi dialog `Edit Purchase` tetap terbuka

### Warranty until baru sebelum Purchase Date tersimpan pada Bulk
58. Tampilkan Dialog Edit Purchase dengan kondisi K5
59. Klik `[+ Add warranty]`
60. Isi Warranty name `Garansi layar`
61. Pilih Warranty until `09/03/26`
62. Klik `[Save]`
63. Verifikasi pesan `Warranty until cannot be before purchase date` tampil dan dialog `Edit Purchase` tetap terbuka

### Provider 120 karakter yang diapit spasi tepi dihitung setelah trim
64. Tampilkan Dialog Edit Purchase dengan kondisi K1
65. Klik `[+ Add warranty]`
66. Isi Provider `Dell Service CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC` (120 karakter) yang diapit satu spasi di awal dan satu spasi di akhir
67. Verifikasi field Provider menerima nilai tanpa pesan `Max. 120 characters`
