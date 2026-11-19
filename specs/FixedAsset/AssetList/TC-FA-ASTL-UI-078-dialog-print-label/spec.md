---
id: TC-FA-ASTL-UI-078-dialog-print-label
title: "Dialog Print Label"
layer: ui-client
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["FI-17", "FI-18", "FI-19", "FI-20", "T-08", "T-26", "D-16", "EC-42", "FLD-38", "§4.1h#b11", "§4.1h#b12", "§6#r9", "EB-FB-1@print-label", "EB-FB-2@print-label", "EB-ERR-1@print-label"]
smoke: []
dependsOn: []
trace:
  "FI-17": 3
  "FI-18": [7, 9]
  "FI-19": 20
  "FI-20": [12, 13, 18]
  "T-08": [13, 18, 28]
  "T-26": 24
  "D-16": [2, 3, 5, 15]
  "EC-42": [47, 49, 51, 52, 61, 63, 65, 67, 69]
  "FLD-38": [3, 9]
  "§4.1h#b11": [2, 3, 4, 5, 7, 15, 16]
  "§4.1h#b12": [4, 39, 40, 41, 42, 43, 44, 45, 47, 54, 55, 57, 58, 59, 61]
  "§6#r9": [24, 32]
  "EB-FB-1@print-label": [13, 24, 28]
  "EB-FB-2@print-label": 37
  "EB-ERR-1@print-label": [24, 25, 26, 29, 32, 33]
anchor: [36]
coverage:
  web: automated
---
# Dialog Print Label

## Prerequisites
- Aktor: Total Control.
- Layar awal: Fixed Asset > Assets > All Assets.
- Komponen: Dialog Print Label
- Data:
  - DU-078-1: Aset `Laptop Pro 16 - 1`, Asset ID `AST-0001`, Group `IT`, Lifecycle `Active`; nama perusahaan client `PT Nusantara Teknologi`.
  - DU-078-2: Delapan aset `Laptop Pro 16 - 1` sampai `Laptop Pro 16 - 8` yang dipilih bersama, nama perusahaan client `PT Nusantara Teknologi`.
  - Teks sisa Preview yang diharapkan untuk DU-078-2: `+2 more labels`, dari delapan aset dikurangi enam slot.
  - DU-078-3: Aset dengan Asset Name 34 karakter `Laptop Pro 16 Kantor Pusat Lan - 1` (34 karakter), Asset ID `AST-0201`.
  - DU-078-4: Aset dengan Asset Name 35 karakter `Laptop Pro 16 Kantor Pusat Lant - 1` (35 karakter), Asset ID `AST-0202`.
  - DU-078-5: Aset dengan Asset Name 69 karakter `Laptop Pro 16 Kantor Pusat Lantai Tiga Ruang Rapat Utama Gedung B - 1` (69 karakter), Asset ID `AST-0203`.
  - DU-078-6: Aset dengan Asset Name 101 karakter `Laptop Pro 16 Kantor Pusat Lantai Tiga Ruang Rapat Utama Gedung Barat Cabang Medan Sektor Delapan - 1` (101 karakter), Asset ID `AST-0204`.
  - DU-078-7: Aset dengan Asset ID 32 karakter `AST-A0A0A0A0A0A0A0A0A0A0A0A0A0A0` (32 karakter), Asset Name `Meja Rapat - 1`.
  - DU-078-8: Aset dengan Asset ID 33 karakter `AST-A0A0A0A0A0A0A0A0A0A0A0A0A0A0Z` (33 karakter), Asset Name `Meja Rapat - 2`.
  - DU-078-9: Nama perusahaan client 37 karakter `PT Nusantara Teknologi Indonesia Raya` (37 karakter), yang diharapkan tampil `PT Nusantara..donesia Raya` (12 huruf pertama, `..`, 12 huruf terakhir).
  - DU-078-10: Aset dengan Asset Name non-Latin `笔记本电脑 Pro 16 - 1`, Asset ID `AST-0301`.
  - DU-078-11: Aset dengan Asset Name non-Latin `โน้ตบุ๊ก Pro 16 - 1`, Asset ID `AST-0302`.
  - DU-078-12: Aset dengan Asset Name aksara Arab (kanan ke kiri) `حاسوب محمول Pro 16 - 1`, Asset ID `AST-0303`.
  - DU-078-13: Aset dengan Asset Name 68 karakter `Laptop Pro 16 Kantor Pusat Lantai Tiga Ruang Rapat Utama GedungX - 1` (68 karakter), Asset ID `AST-0205`.
  - DU-078-14: Aset dengan Asset Name 100 karakter `Laptop Pro 16 Kantor Pusat Lantai Tiga Ruang Rapat Utama Gedung Barat Cabang Medan Sektor XXXXXX - 1` (100 karakter), Asset ID `AST-0206`.
  - DU-078-15: Aset dengan Asset Name 300 karakter `Laptop Pro 16 Kantor Pusat Lantai Tiga Ruang Rapat Utama Gedung Barat Cabang Medan Sektor Delapan Blok Timur Selatan Utara Kantor Pusat Lantai Tiga Ruang Rapat Utama Gedung Barat Cabang Medan Sektor Delapan Blok Timur Selatan Utara Kantor Pusat Lantai Tiga Ruang Rapat Utama Gedung Barat Cabang X - 1` (300 karakter), Asset ID `AST-0207`.
  - DU-078-16: Nama perusahaan client beraksara Arab (kanan ke kiri) `شركة التقنية الوطنية`.
  - DU-078-17: Nama perusahaan client non-Latin `北京科技有限公司`.
- Kondisi:
  - Semua kondisi memakai nama perusahaan client dari DU-078-1 kecuali dinyatakan lain.
  - K1: dialog berisi satu aset, DU-078-1; cetak berhasil.
  - K2: dialog berisi delapan aset DU-078-2; cetak berhasil.
  - K3: dialog tidak berisi aset.
  - K4: dialog berisi satu aset, DU-078-1; cetak pertama gagal karena error server, cetak berikutnya berhasil.
  - K5: dialog berisi satu aset, DU-078-1; cetak gagal karena timeout atau jaringan terputus.
  - K6: dialog berisi enam aset DU-078-3 sampai DU-078-8 dengan nama perusahaan client DU-078-9.
  - K7: dialog berisi satu aset, DU-078-1; nama perusahaan client kosong; cetak berhasil.
  - K8: dialog berisi aset DU-078-10, DU-078-11, dan DU-078-12.
  - K9: dialog berisi dua aset DU-078-13 dan DU-078-14.
  - K10: dialog berisi satu aset, DU-078-15.
  - K11: dialog berisi satu aset, DU-078-1; nama perusahaan client DU-078-16; cetak berhasil.
  - K12: dialog berisi satu aset, DU-078-1; nama perusahaan client DU-078-17; cetak berhasil.

## Test Steps

### Isi dialog dan pilihan Start print from
1. Tampilkan Dialog Print Label dengan kondisi K1
2. Verifikasi dialog berjudul `Print Label` tampil dengan teks `Selected asset: 1 asset`
3. Verifikasi pilihan `Start print from` memuat `Left` dan `Right`, dan `Left` terpilih
4. Verifikasi Preview menampilkan label aset `Laptop Pro 16 - 1` dengan Asset ID `AST-0001` dan nama perusahaan `PT Nusantara Teknologi`
5. Verifikasi tombol `[Cancel]` dan `[Start Print]` tampil dan `[Start Print]` aktif
6. Pilih `Right` pada `Start print from`
7. Verifikasi slot kiri pertama pada Preview kosong dan label `Laptop Pro 16 - 1` berada di slot berikutnya
8. Pilih `Left` pada `Start print from`
9. Verifikasi label `Laptop Pro 16 - 1` berada di slot kiri pertama pada Preview

### Print satu aset menutup dialog dan menampilkan toast
10. Tampilkan Dialog Print Label dengan kondisi K1
11. Klik `[Start Print]`
12. Verifikasi dialog `Print Label` tertutup
13. Verifikasi toast `Success, label has been sent to print.` tampil

### Print banyak aset dengan Preview terbatas enam slot
14. Tampilkan Dialog Print Label dengan kondisi K2
15. Verifikasi teks `Selected asset: 8 assets` tampil
16. Verifikasi Preview menampilkan enam slot dan teks `+2 more labels`
17. Klik `[Start Print]`
18. Verifikasi toast `Success, labels have been sent to print.` tampil

### Tanpa aset Start Print Disabled
19. Tampilkan Dialog Print Label dengan kondisi K3
20. Verifikasi `[Start Print]` Disabled

### Kegagalan server mempertahankan dialog
21. Tampilkan Dialog Print Label dengan kondisi K4
22. Pilih `Right` pada `Start print from`
23. Klik `[Start Print]`
24. Verifikasi toast `Error, failed to print label.` tampil
25. Verifikasi dialog `Print Label` tetap terbuka dengan `Right` masih terpilih dan `[Start Print]` aktif kembali
26. Verifikasi toast `Error, failed to print label.` tidak memiliki tombol aksi seperti `[Try Again]`
27. Klik `[Start Print]`
28. Verifikasi toast `Success, label has been sent to print.` tampil
29. Verifikasi dialog `Print Label` tertutup dan cetak berhasil tepat satu kali

### Timeout mempertahankan dialog
30. Tampilkan Dialog Print Label dengan kondisi K5
31. Klik `[Start Print]`
32. Verifikasi toast `Connection problem. Please try again.` tampil
33. Verifikasi dialog `Print Label` tetap terbuka dan `[Start Print]` aktif kembali

### Cancel menutup dialog tanpa toast
34. Tampilkan Dialog Print Label dengan kondisi K1
35. Klik `[Cancel]`
36. Verifikasi dialog `Print Label` tertutup
37. Verifikasi tidak ada toast yang tampil

### Ukuran font dan baris teks label menurut jumlah karakter
38. Tampilkan Dialog Print Label dengan kondisi K6
39. Verifikasi Asset Name `Laptop Pro 16 Kantor Pusat Lan - 1` (34 karakter) tampil 10pt satu baris
40. Verifikasi Asset Name `Laptop Pro 16 Kantor Pusat Lant - 1` (35 karakter) tampil 10pt dua baris
41. Verifikasi Asset Name `Laptop Pro 16 Kantor Pusat Lantai Tiga Ruang Rapat Utama Gedung B - 1` (69 karakter) tampil 8pt tiga baris
42. Verifikasi Asset Name `Laptop Pro 16 Kantor Pusat Lantai Tiga Ruang Rapat Utama Gedung Barat Cabang Medan Sektor Delapan - 1` (101 karakter) tampil 7pt empat baris
43. Verifikasi Asset ID `AST-A0A0A0A0A0A0A0A0A0A0A0A0A0A0` (32 karakter) tampil 8pt satu baris
44. Verifikasi Asset ID `AST-A0A0A0A0A0A0A0A0A0A0A0A0A0A0Z` (33 karakter) tampil 7pt dua baris tanpa elipsis
45. Verifikasi nama perusahaan tampil `PT Nusantara..donesia Raya`

### Nama perusahaan kosong
46. Tampilkan Dialog Print Label dengan kondisi K7
47. Verifikasi Preview menampilkan label aset `Laptop Pro 16 - 1` dengan Asset ID `AST-0001` dan baris nama perusahaan kosong
48. Klik `[Start Print]`
49. Verifikasi toast `Success, label has been sent to print.` tampil

### Nama aset non-Latin
50. Tampilkan Dialog Print Label dengan kondisi K8
51. Verifikasi Preview menampilkan Asset Name `笔记本电脑 Pro 16 - 1` dan `โน้ตบุ๊ก Pro 16 - 1` apa adanya
52. Verifikasi Preview menampilkan Asset Name `حاسوب محمول Pro 16 - 1` apa adanya

### Batas atas tier Asset Name
53. Tampilkan Dialog Print Label dengan kondisi K9
54. Verifikasi Asset Name `Laptop Pro 16 Kantor Pusat Lantai Tiga Ruang Rapat Utama GedungX - 1` (68 karakter) tampil 10pt dua baris
55. Verifikasi Asset Name `Laptop Pro 16 Kantor Pusat Lantai Tiga Ruang Rapat Utama Gedung Barat Cabang Medan Sektor XXXXXX - 1` (100 karakter) tampil 8pt tiga baris

### Format label
56. Tampilkan Dialog Print Label dengan kondisi K1
57. Verifikasi label pada Preview memuat tiga baris berurutan: nama aset `Laptop Pro 16 - 1`, Asset ID `AST-0001`, dan nama perusahaan `PT Nusantara Teknologi`
58. Verifikasi label pada Preview tidak memuat QR, barcode, maupun logo vendor TAG Samurai
59. Verifikasi label pada Preview tidak memuat Group, PIC, Status, nilai, Category, Purchase Year, Serial Number, maupun Tag Code

### Asset Name melebihi empat baris
60. Tampilkan Dialog Print Label dengan kondisi K10
61. Verifikasi Asset Name `Laptop Pro 16 Kantor Pusat Lantai Tiga Ruang Rapat Utama Gedung Barat Cabang Medan Sektor Delapan Blok Timur Selatan Utara Kantor Pusat Lantai Tiga Ruang Rapat Utama Gedung Barat Cabang Medan Sektor Delapan Blok Timur Selatan Utara Kantor Pusat Lantai Tiga Ruang Rapat Utama Gedung Barat Cabang X - 1` (300 karakter) tampil 7pt empat baris dengan baris keempat berelipsis

### Nama perusahaan client kanan ke kiri
62. Tampilkan Dialog Print Label dengan kondisi K11
63. Verifikasi Preview menampilkan nama perusahaan `شركة التقنية الوطنية` apa adanya pada label `Laptop Pro 16 - 1`
64. Klik `[Start Print]`
65. Verifikasi toast `Success, label has been sent to print.` tampil

### Nama perusahaan client non-Latin
66. Tampilkan Dialog Print Label dengan kondisi K12
67. Verifikasi Preview menampilkan nama perusahaan `北京科技有限公司` apa adanya pada label `Laptop Pro 16 - 1`
68. Klik `[Start Print]`
69. Verifikasi toast `Success, label has been sent to print.` tampil
