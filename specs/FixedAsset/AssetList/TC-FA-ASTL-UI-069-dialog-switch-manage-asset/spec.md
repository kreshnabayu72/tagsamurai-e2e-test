---
id: TC-FA-ASTL-UI-069-dialog-switch-manage-asset
title: "Dialog Switch Manage Asset"
layer: ui-client
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["ASTL-LOGIC-15k", "FI-14", "V-03", "D-04", "D-04ExampleTable", "FLD-40", "§7.1#r3", "§7.1#p1"]
smoke: []
dependsOn: []
trace:
  "ASTL-LOGIC-15k": [10, 11, 27, 28, 30, 31, 54, 55, 60, 61]
  "FI-14": [7, 8, 10, 11, 13, 24, 25, 27, 28, 30, 31, 33, 34, 54, 55, 60, 61]
  "V-03": [8, 10, 11, 14, 25, 27, 28, 30, 31, 34, 54, 55, 60, 61]
  "D-04": [2, 3, 4, 5, 16, 18, 19, 23, 46, 50, 65, 66, 70, 71]
  "D-04ExampleTable": 6
  "FLD-40": [7, 8, 10, 54, 55, 60, 61]
  "§7.1#r3": [21, 36, 37]
  "§7.1#p1": [39, 40, 41, 43]
anchor: []
coverage:
  web: automated
---
# Dialog Switch Manage Asset

## Prerequisites
- Aktor: Total Control.
- Layar awal: Fixed Asset > Assets > All Assets.
- Komponen: Dialog Switch Manage Asset
- Data:
  - DU-069-1: Aset managed `Laptop Pro 16 - 1`, Asset ID `AST-0001`, Group `IT`, Category `Laptop`.
  - DU-069-2: Aset managed `Laptop Pro 16 - 2`, Asset ID `AST-0002`, Group `IT`, Category `Laptop`.
  - DU-069-3: Aset managed `Laptop Pro 16 - 3`, Asset ID `AST-0003`, Group `IT`, Category `Laptop`.
  - DU-069-4: Aset Unmanaged yang akan di-Manage `Scanner Gudang - 2`, Group `IT`.
  - DU-069-5: Aset Unmanaged yang akan di-Manage `Scanner Gudang - 3`, Group `IT`.
  - DU-069-6: Kata kunci Search tanpa hasil `Meja Bundar - 9`.
  - Keterangan yang diharapkan untuk satu aset: `Select 1 managed asset in IT to become unmanaged. Its license will be used by the selected asset.`, dari jumlah aset 1 dan group `IT`.
  - Keterangan yang diharapkan untuk dua aset: `Select 2 managed assets in IT to become unmanaged. Their licenses will be used by the selected assets.`, dari jumlah aset 2 dan group `IT`.
- Kondisi:
  - K1: satu aset di-Manage (DU-069-4); tabel memuat DU-069-1 sampai DU-069-3.
  - K2: dua aset di-Manage (DU-069-4 dan DU-069-5); tabel memuat DU-069-1 sampai DU-069-3.
  - K3: satu aset di-Manage (DU-069-4); group `IT` tidak memiliki aset managed lain.
  - K4: satu aset di-Manage (DU-069-4); memuat tabel gagal karena error server pada percobaan pertama dan berhasil memuat DU-069-1 sampai DU-069-3 pada percobaan berikutnya.
  - K5: satu aset di-Manage (DU-069-4); tabel memuat DU-069-1 sampai DU-069-3; `[Switch]` pertama gagal karena error server.
  - K6: satu aset di-Manage (DU-069-4); tabel memuat DU-069-1 sampai DU-069-3; `[Switch]` gagal karena timeout atau jaringan terputus.

## Test Steps

### Tampilan awal dan pilihan tepat satu aset
1. Tampilkan Dialog Switch Manage Asset dengan kondisi K1
2. Verifikasi dialog berjudul `Switch Manage Asset` tampil dengan keterangan `Select 1 managed asset in IT to become unmanaged. Its license will be used by the selected asset.`
3. Verifikasi tombol `[Cancel]` dan `[Switch]` tampil
4. Verifikasi kolom `Name`, `Asset ID`, `Group`, dan `Category` tampil di tabel
5. Verifikasi kolom `Brand`, `Model / Type`, `Status`, dan `Labels` tidak tampil
6. Verifikasi baris `Laptop Pro 16 - 1`, `Laptop Pro 16 - 2`, dan `Laptop Pro 16 - 3` tampil dengan Asset ID `AST-0001`, `AST-0002`, `AST-0003` dan Group `IT`
7. Verifikasi tidak ada baris yang tercentang dan penghitung `0 of 1 selected` tampil
8. Verifikasi `[Switch]` Disabled
9. Centang baris `Laptop Pro 16 - 2`
10. Verifikasi penghitung `1 of 1 selected` tampil
11. Verifikasi `[Switch]` aktif
12. Hapus centang baris `Laptop Pro 16 - 2`
13. Verifikasi penghitung `0 of 1 selected` tampil
14. Verifikasi `[Switch]` Disabled kembali

### Search, Filter, dan Column Visibility tabel
15. Tampilkan Dialog Switch Manage Asset dengan kondisi K1
16. Verifikasi kotak Search, tombol Filter, dan trigger Column Visibility tersedia di tabel
17. Ketik Search `Laptop Pro 16 - 3`, tekan Enter
18. Verifikasi baris `Laptop Pro 16 - 3` tampil
19. Verifikasi baris `Laptop Pro 16 - 1` tidak tampil
20. Ganti isi kotak Search dengan `Meja Bundar - 9`, tekan Enter
21. Verifikasi `No results found` dan `Try adjusting your search or filter.` tampil

### Pilihan tepat dua aset
22. Tampilkan Dialog Switch Manage Asset dengan kondisi K2
23. Verifikasi keterangan `Select 2 managed assets in IT to become unmanaged. Their licenses will be used by the selected assets.` tampil
24. Verifikasi penghitung `0 of 2 selected` tampil
25. Verifikasi `[Switch]` Disabled
26. Centang baris `Laptop Pro 16 - 1`
27. Verifikasi penghitung `1 of 2 selected` tampil
28. Verifikasi `[Switch]` masih Disabled
29. Centang baris `Laptop Pro 16 - 2`
30. Verifikasi penghitung `2 of 2 selected` tampil
31. Verifikasi `[Switch]` aktif
32. Hapus centang baris `Laptop Pro 16 - 1`
33. Verifikasi penghitung `1 of 2 selected` tampil
34. Verifikasi `[Switch]` Disabled kembali

### Tidak ada aset managed lain di group
35. Tampilkan Dialog Switch Manage Asset dengan kondisi K3
36. Verifikasi `No managed assets available` tampil
37. Verifikasi `There are no other managed assets in this group to switch with.` tampil

### Gagal memuat tabel
38. Tampilkan Dialog Switch Manage Asset dengan kondisi K4
39. Verifikasi teks `Unable to load this data.` tampil
40. Verifikasi tombol `[Try Again]` tampil
41. Verifikasi empty state `No managed assets available` tidak tampil
42. Klik `[Try Again]`
43. Verifikasi baris `Laptop Pro 16 - 1` tampil

### Panel Filter dan Column Visibility memuat seluruh kolom
44. Tampilkan Dialog Switch Manage Asset dengan kondisi K1
45. Klik tombol Filter pada tabel
46. Verifikasi panel Filter memuat filter `Group`, `Category`, `Brand`, `Model / Type`, `Status`, dan `Labels`
47. Tutup panel Filter
48. Klik trigger Column Visibility pada tabel
49. Tampilkan kolom `Brand`, `Model / Type`, `Status`, dan `Labels`
50. Verifikasi kolom `Brand`, `Model / Type`, `Status`, dan `Labels` tampil di tabel

### Pilihan melebihi jumlah aset satu aset
51. Tampilkan Dialog Switch Manage Asset dengan kondisi K1
52. Centang baris `Laptop Pro 16 - 1`
53. Centang baris `Laptop Pro 16 - 2`
54. Verifikasi penghitung `2 of 1 selected` tampil
55. Verifikasi `[Switch]` Disabled

### Pilihan melebihi jumlah aset dua aset
56. Tampilkan Dialog Switch Manage Asset dengan kondisi K2
57. Centang baris `Laptop Pro 16 - 1`
58. Centang baris `Laptop Pro 16 - 2`
59. Centang baris `Laptop Pro 16 - 3`
60. Verifikasi penghitung `3 of 2 selected` tampil
61. Verifikasi `[Switch]` Disabled

### Kegagalan server mempertahankan dialog
62. Tampilkan Dialog Switch Manage Asset dengan kondisi K5
63. Centang baris `Laptop Pro 16 - 2`
64. Klik `[Switch]`
65. Verifikasi toast `Error, failed to manage asset.` tampil
66. Verifikasi dialog `Switch Manage Asset` tetap terbuka dengan baris `Laptop Pro 16 - 2` masih tercentang, penghitung `1 of 1 selected` tampil, dan `[Switch]` aktif kembali

### Timeout mempertahankan dialog
67. Tampilkan Dialog Switch Manage Asset dengan kondisi K6
68. Centang baris `Laptop Pro 16 - 2`
69. Klik `[Switch]`
70. Verifikasi toast `Connection problem. Please try again.` tampil setelah `[Switch]` diklik
71. Verifikasi dialog `Switch Manage Asset` tetap terbuka dengan baris `Laptop Pro 16 - 2` masih tercentang, penghitung `1 of 1 selected` tampil, dan `[Switch]` aktif kembali
