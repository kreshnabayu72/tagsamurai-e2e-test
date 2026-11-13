---
id: TC-FA-FAREG-UI-014-form-interaksi-field-item
title: "Form Register Asset: interaksi Category, Asset Name, Brand, Model, dan TAG Type"
layer: ui-client
priority: Medium
caseType: Positive
status: draft
sourceRules: ["FAREG-LOGIC-01k", "FAREG-LOGIC-01l", "FAREG-LOGIC-01m", "FAREG-LOGIC-01p", "FAREG-LOGIC-04a", "FI-REG-01", "FI-REG-02", "FI-REG-03", "FI-REG-04", "FI-REG-05", "FI-REG-06", "FLD-REG-02", "FLD-REG-03", "FLD-REG-04", "S-REG-09", "S-REG-10", "§4.1#b16", "§4.1#b17", "§4.1#b18", "§4.1#p45", "§9.9#r1", "EB-TBL-5@form-register-asset"]
smoke: []
dependsOn: []
trace:
  "FAREG-LOGIC-01k": [12, 17]
  "FAREG-LOGIC-01l": [33, 34, 37, 38]
  "FAREG-LOGIC-01m": [10, 14]
  "FAREG-LOGIC-01p": [71, 73, 74]
  "FAREG-LOGIC-04a": [31, 39, 60]
  "FI-REG-01": [46, 47, 54]
  "FI-REG-02": [64, 65, 66, 67]
  "FI-REG-03": 59
  "FI-REG-04": [37, 38]
  "FI-REG-05": 33
  "FI-REG-06": [6, 31, 39]
  "FLD-REG-02": [41, 57]
  "FLD-REG-03": [2, 12]
  "FLD-REG-04": [4, 16, 17, 18]
  "S-REG-09": 3
  "S-REG-10": 5
  "§4.1#b16": [31, 39]
  "§4.1#b17": [25, 26]
  "§4.1#b18": 41
  "§4.1#p45": [44, 50]
  "§9.9#r1": [50, 52, 54]
  "EB-TBL-5@form-register-asset": [3, 5]
coverage:
  web: automated
---

# Form Register Asset: interaksi Category, Asset Name, Brand, Model, dan TAG Type

## Prerequisites
- Aktor: Total Control.
- Layar awal: Assets > Registration > Draft
- Komponen: Halaman `Register Asset`
- Data:
  - DU-014-1: Asset Name `Laptop Dell Latitude 5440`, Category `Elektronik > Komputer > Laptop`, TAG Type `RFID`, Brand `Dell` dengan Model `Latitude 5440` dan `Inspiron 15 3530`, Brand `Lenovo` dengan Model `ThinkPad T14`.
  - DU-014-2: Asset Name `Kursi Kerja Ergonomis`, Category `Furnitur > Kursi`, TAG Type `QR`, Brand `Ergotec`, Model `ErgoMesh 200`.
  - DU-014-3: Asset Name `Printer Epson L3250`, Category `Elektronik > Periferal > Printer`, TAG Type `RFID` dan `NFC`, Brand `Epson`, Model `L3250`.
  - DU-014-4: Asset Name `Rak Besi Gudang`, Category `Furnitur > Rak`, TAG Type `QR`, tanpa Brand terkait.
- Kondisi:
  - K1: form `Register Asset` baru tanpa draft tersimpan; tabel Item berisi satu Item kosong; master Asset Name, Brand, Model, dan Category berisi DU-014-1 sampai DU-014-4.

## Test Steps
### Brand dan Model Disabled sampai induk dipilih
1. Tampilkan Halaman `Register Asset` dengan kondisi K1
2. Verifikasi `Brand` berstatus Disabled selama Asset Name belum dipilih
3. Verifikasi tooltip `Select asset name first.` tampil saat pointer berada di `Brand`
4. Verifikasi `Model` berstatus Disabled selama Brand belum dipilih
5. Verifikasi tooltip `Select brand first.` tampil saat pointer berada di `Model`
6. Verifikasi TAG Type bernilai `—` sebelum Asset Name dipilih

### Opsi bertingkat Asset Name, Brand, dan Model tanpa auto-pilih
7. Tampilkan Halaman `Register Asset` dengan kondisi K1
8. Buka dropdown `Asset Name`
9. Pilih `Laptop Dell Latitude 5440`
10. Verifikasi `Brand` tidak Disabled dan masih menampilkan placeholder `Select brand`
11. Buka dropdown `Brand`
12. Verifikasi opsi `Dell` dan `Lenovo` tampil di dropdown `Brand`
13. Pilih `Dell`
14. Verifikasi `Model` tidak Disabled dan masih menampilkan placeholder `Select model`
15. Buka dropdown `Model`
16. Verifikasi opsi `No Model` berada paling atas di dropdown `Model`
17. Verifikasi opsi `Latitude 5440` dan `Inspiron 15 3530` tampil di dropdown `Model`
18. Verifikasi opsi `ThinkPad T14` tidak tampil di dropdown `Model`

### Satu Item adalah satu kombinasi Asset Name, Brand, dan Model
19. Tampilkan Halaman `Register Asset` dengan kondisi K1
20. Pilih `Laptop Dell Latitude 5440` di dropdown `Asset Name` Item pertama
21. Pilih `Dell` di dropdown `Brand` Item pertama
22. Pilih `Latitude 5440` di dropdown `Model` Item pertama
23. Klik `[+ Asset Name]`
24. Pilih `Kursi Kerja Ergonomis` di dropdown `Asset Name` Item kedua
25. Verifikasi Item pertama tetap berisi `Laptop Dell Latitude 5440`, `Dell`, dan `Latitude 5440`
26. Verifikasi Item kedua berisi `Kursi Kerja Ergonomis` dengan Brand dan Model masih kosong

### Mengganti induk mengosongkan anak dan TAG Type mengikuti Asset Name
27. Tampilkan Halaman `Register Asset` dengan kondisi K1
28. Pilih `Laptop Dell Latitude 5440` di dropdown `Asset Name`
29. Pilih `Dell` di dropdown `Brand`
30. Pilih `Latitude 5440` di dropdown `Model`
31. Verifikasi `TAG Type` menampilkan ikon `RFID`
32. Ganti Brand menjadi `Lenovo`
33. Verifikasi `Model` menampilkan placeholder `Select model`
34. Verifikasi `Asset Name` tetap `Laptop Dell Latitude 5440`
35. Pilih `ThinkPad T14` di dropdown `Model`
36. Ganti Asset Name menjadi `Printer Epson L3250`
37. Verifikasi `Brand` menampilkan placeholder `Select brand`
38. Verifikasi `Model` menampilkan placeholder `Select model`
39. Verifikasi `TAG Type` menampilkan ikon `RFID` dan ikon `NFC`

### Category menyaring Asset Name dan hanya node terbawah dapat dipilih
40. Tampilkan Halaman `Register Asset` dengan kondisi K1
41. Verifikasi kolom `Category` berada sebelum kolom `Asset Name`
42. Buka pemilih `Category`
43. Klik node `Laptop`
44. Verifikasi `Category` berisi path penuh `Elektronik > Komputer > Laptop`
45. Buka dropdown `Asset Name`
46. Verifikasi opsi `Laptop Dell Latitude 5440` tampil di dropdown `Asset Name`
47. Verifikasi opsi `Kursi Kerja Ergonomis` tidak tampil di dropdown `Asset Name`
48. Buka pemilih `Category`
49. Klik node induk `Elektronik`
50. Verifikasi `Category` tetap berisi path penuh `Elektronik > Komputer > Laptop`
51. Kosongkan `Category`
52. Verifikasi `Category` menampilkan placeholder `Select category`
53. Buka dropdown `Asset Name`
54. Verifikasi opsi `Kursi Kerja Ergonomis` tampil kembali di dropdown `Asset Name`

### Asset Name berupa dropdown master dan mengisi Category otomatis
55. Tampilkan Halaman `Register Asset` dengan kondisi K1
56. Ketik `Meja Tidak Terdaftar` pada dropdown `Asset Name`
57. Verifikasi `Meja Tidak Terdaftar` tidak menjadi nilai `Asset Name`
58. Pilih `Kursi Kerja Ergonomis` di dropdown `Asset Name`
59. Verifikasi `Category` terisi otomatis dengan `Furnitur > Kursi`
60. Verifikasi `TAG Type` menampilkan ikon `QR`
61. Pilih `Ergotec` di dropdown `Brand`
62. Pilih `ErgoMesh 200` di dropdown `Model`
63. Pilih node `Laptop` di pemilih `Category`
64. Verifikasi `Category` berisi path penuh `Elektronik > Komputer > Laptop`
65. Verifikasi `Asset Name` menampilkan placeholder `Select asset name`
66. Verifikasi `Brand` menampilkan placeholder `Select brand`
67. Verifikasi `Model` menampilkan placeholder `Select model`

### Asset Name tanpa Brand terkait dan Category terisi kembali
68. Tampilkan Halaman `Register Asset` dengan kondisi K1
69. Pilih `Rak Besi Gudang` di dropdown `Asset Name`
70. Buka dropdown `Brand`
71. Verifikasi dropdown `Brand` menampilkan `No brand available`
72. Kosongkan `Category`
73. Verifikasi `Category` terisi kembali dengan `Furnitur > Rak`
74. Verifikasi `Asset Name` tetap `Rak Besi Gudang`
