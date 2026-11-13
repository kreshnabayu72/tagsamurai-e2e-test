---
id: TC-FA-FAREG-UI-013-form-general-information-tampilan
title: "Form Register Asset: tampilan awal tab General Information, tabel Item, dan footer"
layer: ui-client
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: [FAREG-LOGIC-01g, FAREG-LOGIC-15a, FLD-REG-01, "§2.1#p1", "§4.1#r4", "§4.1#p1", "§4.1#b9", "§4.1#b10", "§4.1#b11", "§4.1#b13", "§4.1#b14", "§4.1#b15", "§4.1#b19", "§4.1#b31", "§4.1#b33", "§4.1#p26", "§4.1#r90", "§4.1#r91", "§4.1#r92", "§4.1#r93", "§4.1#r94", "§4.1#r95", "§4.1#r96", "§4.1#r97", "§4.1#p42", "§4.2#p1", "§4.2.1#p1", "§9.2#p14", "§9.4.3#b11", "EB-FRM-7@form-register-asset"]
smoke: []
dependsOn: []
trace:
  FAREG-LOGIC-01g: [66, 36, 77, 80, 83]
  FAREG-LOGIC-15a: 66
  FLD-REG-01: [17, 21, 22, 26, 30]
  "§2.1#p1": [66, 77, 80, 83]
  "§4.1#r4": 6
  "§4.1#p1": 7
  "§4.1#b9": 6
  "§4.1#b10": 9
  "§4.1#b11": [10, 11, 35]
  "§4.1#b13": 7
  "§4.1#b14": [13, 17, 89, 90]
  "§4.1#b15": 61
  "§4.1#b19": 63
  "§4.1#b31": 10
  "§4.1#b33": 12
  "§4.1#p26": [55, 56, 57, 58, 59, 61, 95, 97]
  "§4.1#r90": 38
  "§4.1#r91": 39
  "§4.1#r92": 40
  "§4.1#r93": [41, 42]
  "§4.1#r94": [43, 44]
  "§4.1#r95": [45, 46, 92, 93]
  "§4.1#r96": [47, 48, 72, 73]
  "§4.1#r97": [50, 51]
  "§4.1#p42": [21, 26, 30]
  "§4.2#p1": [3, 4, 5, 8, 86, 87]
  "§4.2.1#p1": [2, 32, 76, 33]
  "§9.2#p14": 67
  "§9.4.3#b11": [66, 77, 80, 83]
  EB-FRM-7@form-register-asset: [69, 70]
anchor: [53, 65, 75, 79, 82, 85]
coverage:
  web: automated
---

# Form Register Asset: tampilan awal tab General Information, tabel Item, dan footer

## Prerequisites
- Aktor: Total Control; pada K3 aktornya Manage purchase, pada K4 Group Manager, dan pada K5 Manage asset & TAG.
- Layar awal: Assets > Registration > Draft
- Komponen: Halaman `Register Asset`
- Data:
  - DU-013-1: Group `Kantor Pusat`, induk dari `Gudang 1`, Assignable `Ya`, Excess `Tidak`.
  - DU-013-2: Group `Gudang 1`, anak dari `Kantor Pusat`, Assignable `Ya`, Excess `Tidak`.
  - DU-013-3: Group `Gudang Retur`, anak dari `Kantor Pusat`, Assignable `Tidak`, Excess `Tidak`.
  - DU-013-4: Group `Gudang Excess Pusat`, anak dari `Kantor Pusat`, Assignable `Ya`, Excess `Ya`.
  - DU-013-5: Item draft 1, Category `Elektronik > Komputer > Laptop`, Asset Name `Laptop Dell Latitude 5440`, Brand `Dell`, Model `Latitude 5440`, TAG Type `RFID`, Quantity `10`.
  - DU-013-6: Item draft 2, Category `Furnitur > Kursi`, Asset Name `Kursi Kerja Ergonomis`, Brand `Ergotec`, Model `ErgoMesh 200`, TAG Type `QR`, Quantity `20`.
  - Judul tab `Asset` pada K2 adalah `Asset (30)`, dari Quantity `10` ditambah `20`; sesudah Quantity Item pertama diganti `5` menjadi `Asset (25)`, dari `5` ditambah `20`.
- Kondisi:
  - K1: form `Register Asset` baru tanpa draft tersimpan; Group belum dipilih; tabel Item berisi satu Item dengan Quantity awal; pohon Group berisi DU-013-1 sampai DU-013-4.
  - K2: form `Edit` draft tersimpan dengan Group DU-013-2; tabel Item berisi DU-013-5 lalu DU-013-6 berurutan.
  - K3: draft tersimpan dengan Group DU-013-2 dan satu Item DU-013-5 dibuka dalam mode `Detail` (read-only) oleh aktor ber-role Manage purchase.
  - K4: form `Register Asset` baru tanpa draft tersimpan dibuka oleh aktor ber-role Group Manager; pohon Group berisi DU-013-1 sampai DU-013-4.
  - K5: form `Register Asset` baru tanpa draft tersimpan dibuka oleh aktor ber-role Manage asset & TAG; pohon Group berisi DU-013-1 sampai DU-013-4.

## Test Steps

### Struktur halaman dan tab form baru
1. Tampilkan Halaman `Register Asset` dengan kondisi K1
2. Verifikasi Breadcrumb menampilkan `Assets > Registration > Draft > Register Asset`
3. Verifikasi Breadcrumb tampil di luar `SectionCard` mana pun
4. Verifikasi konten halaman dibungkus `SectionCard`
5. Verifikasi tidak ada Page Title Header terpisah di antara Breadcrumb dan `SectionCard`
6. Verifikasi halaman penuh memuat tab `General Information` dan `Asset`
7. Verifikasi tab `General Information` aktif
8. Verifikasi Group hanya dapat dipilih lewat `TreeSelect`, tanpa pohon Group terpisah di samping tabel Item
9. Verifikasi tidak ada kartu ringkasan di tab `General Information`

### Footer form baru
10. Verifikasi footer memuat `[Cancel]`, `[Save draft]`, dan `[Submit]`
11. Verifikasi tidak ada tombol `Back` dan `Next`
12. Verifikasi checkbox `Stay on this form after submitting` tidak tampil

### Pemilih Group hanya menerima node Assignable bukan Excess
13. Verifikasi field `Group` berupa `TreeSelect` pilihan tunggal dengan placeholder `Select group`
14. Buka pemilih `Group`
15. Klik node `Gudang 1`
16. Klik `[Select]`
17. Verifikasi field `Group` menampilkan `Gudang 1`
18. Buka pemilih `Group` lewat `Edit selection`
19. Klik node `Kantor Pusat`
20. Klik `[Select]`
21. Verifikasi field `Group` menampilkan `Kantor Pusat` sebagai node induk yang dapat dipilih
22. Verifikasi `Gudang 1` tidak lagi menjadi nilai field `Group`
23. Buka pemilih `Group` lewat `Edit selection`
24. Klik node `Gudang Excess Pusat`
25. Klik `[Select]`
26. Verifikasi field `Group` tetap menampilkan `Kantor Pusat`
27. Buka pemilih `Group` lewat `Edit selection`
28. Klik node `Gudang Retur`
29. Klik `[Select]`
30. Verifikasi field `Group` tetap menampilkan `Kantor Pusat`

### Footer, Breadcrumb, dan tab Asset pada draft tersimpan
31. Tampilkan Halaman `Register Asset` dengan kondisi K2
32. Verifikasi Breadcrumb menampilkan `Assets > Registration > Draft` dan segmen terakhir `Edit`
33. Verifikasi judul tab `Asset (30)` memuat jumlah aset, yaitu 30 dari Quantity `10` dan `20`
34. Klik tab `Asset`
35. Verifikasi footer tab `Asset` memuat `[Cancel]`, `[Save draft]`, dan `[Submit]`
36. Verifikasi tab `Asset` tidak memuat field Purchase

### Kolom tabel Item pada form baru
37. Tampilkan Halaman `Register Asset` dengan kondisi K1
38. Verifikasi kolom `#` menampilkan `1` pada Item pertama
39. Verifikasi kolom `Category` menampilkan placeholder `Select category`
40. Verifikasi kolom `Asset Name` menampilkan placeholder `Select asset name`
41. Verifikasi kolom `Brand` menampilkan placeholder `Select brand`
42. Verifikasi `Brand` Disabled sebelum Asset Name dipilih
43. Verifikasi kolom `Model` menampilkan placeholder `Select model`
44. Verifikasi `Model` Disabled sebelum Brand dipilih
45. Verifikasi sel `TAG Type` menampilkan `—`
46. Verifikasi sel `TAG Type` Read-only
47. Verifikasi kolom `Quantity` menampilkan `1`
48. Verifikasi sel `Quantity` tidak memiliki placeholder
49. Klik row option (titik tiga) pada Item pertama
50. Verifikasi `Remove from List` Disabled
51. Verifikasi tooltip `At least one item is required.` tampil saat pointer berada di `Remove from List`

### Tabel Item tanpa sort, kolom, paginasi, Search, dan filter; sel dapat diedit; tambah Item
52. Tampilkan Halaman `Register Asset` dengan kondisi K2
53. Verifikasi tabel Item memuat `Laptop Dell Latitude 5440` lalu `Kursi Kerja Ergonomis` berurutan
54. Klik header kolom `Asset Name`
55. Verifikasi urutan Item tetap `Laptop Dell Latitude 5440` lalu `Kursi Kerja Ergonomis`
56. Verifikasi kontrol column visibility tidak tampil pada tabel Item
57. Verifikasi paginasi tidak tampil pada tabel Item
58. Verifikasi kotak Search tidak tampil pada tabel Item
59. Verifikasi filter tidak tampil pada tabel Item
60. Ganti isi sel `Quantity` Item pertama dengan `5`
61. Verifikasi sel `Quantity` Item pertama menampilkan `5` dan tabel tetap berupa tabel editable
62. Klik `[+ Asset Name]`
63. Verifikasi tabel Item memuat tiga Item dengan `#` `3` pada Item baru

### Field Purchase dan Project tidak ada di form
64. Tampilkan Halaman `Register Asset` dengan kondisi K1
65. Verifikasi tabel Item tampil dengan kolom `Asset Name`
66. Verifikasi tidak ada field Purchase di tab `General Information`
67. Verifikasi tidak ada field `Project` di tab `General Information`

### Aksesibilitas field dan Quantity di luar rentang dijepit ke batas
68. Tampilkan Halaman `Register Asset` dengan kondisi K1
69. Verifikasi field `Group`, `Asset Name`, `Brand`, dan `Model` memiliki atribut aria-required
70. Verifikasi kontrol row option (titik tiga) memiliki label aksesibel
71. Ganti isi sel `Quantity` Item pertama dengan `0`, tekan Enter
72. Verifikasi nilai `0` yang diketik pada sel `Quantity` Item pertama dijepit ke batas bawah `1`[^drift-1]
73. Verifikasi tidak ada pesan rentang di bawah sel `Quantity`[^drift-1]

### Breadcrumb mode Detail dan field Purchase tidak ada bagi Manage purchase
74. Tampilkan Halaman `Register Asset` dengan kondisi K3
75. Verifikasi tabel Item memuat `Laptop Dell Latitude 5440`
76. Verifikasi Breadcrumb menampilkan `Assets > Registration > Draft` dan segmen terakhir `Detail`
77. Verifikasi tidak ada field Purchase di form

### Field Purchase tidak ada bagi Group Manager
78. Tampilkan Halaman `Register Asset` dengan kondisi K4
79. Verifikasi tabel Item tampil dengan kolom `Asset Name`
80. Verifikasi tidak ada field Purchase di tab `General Information`

### Field Purchase tidak ada bagi Manage asset & TAG
81. Tampilkan Halaman `Register Asset` dengan kondisi K5
82. Verifikasi tabel Item tampil dengan kolom `Asset Name`
83. Verifikasi tidak ada field Purchase di tab `General Information`

### SectionCard tanpa kontrol buka-tutup dan berjarak dari Breadcrumb
84. Tampilkan Halaman `Register Asset` dengan kondisi K1
85. Verifikasi tabel Item tampil di dalam `SectionCard`
86. Verifikasi jarak langsung dari Breadcrumb ke `SectionCard` adalah `gap-3` (12px)
87. Verifikasi tidak ada kontrol untuk membuka atau menutup isi `SectionCard`

### Posisi field Group di toolbar tabel Item
88. Tampilkan Halaman `Register Asset` dengan kondisi K1
89. Verifikasi label `Group` berada di kiri field dan field memanjang horizontal
90. Verifikasi field `Group` berada di sisi kiri toolbar tabel Item, sejajar dengan `[+ Asset Name]` di kanan toolbar

### Tooltip nama tipe Tag pada ikon TAG Type
91. Tampilkan Halaman `Register Asset` dengan kondisi K2
92. Verifikasi tooltip `RFID` tampil saat pointer berada di ikon `TAG Type` Item `Laptop Dell Latitude 5440`
93. Verifikasi tooltip `QR` tampil saat pointer berada di ikon `TAG Type` Item `Kursi Kerja Ergonomis`

### Perubahan sel Quantity langsung tercermin di judul tab Asset
94. Tampilkan Halaman `Register Asset` dengan kondisi K2
95. Verifikasi judul tab `Asset (30)` sebelum Quantity diganti
96. Ganti isi sel `Quantity` Item pertama dengan `5`, tekan Enter
97. Verifikasi judul tab `Asset` berubah menjadi `Asset (25)` tanpa mengklik `[Save draft]`

[^drift-1]: Drift PRD vs kontrak komponen. PRD V-REG-10 dan §9.9 baris Quantity: nilai di luar rentang 1 sampai [Max] memunculkan pesan `Quantity must be between 1 and [Max]` dengan timing Langsung. Kontrak `NumberInput#1`: `min` dan `max` adalah rentang, dan saat blur atau Enter nilai dijepit ke batas terdekat (`-7` menjadi `0`, di atas `max` menjadi `max`). Kontrak `NumberInput#15`: tidak ada pesan rentang dan tidak ada keadaan invalid untuk nilai di luar `min`/`max`, hanya dijepit. Diasersi: kontrak, yaitu nilai `0` dijepit ke batas bawah `1` tanpa pesan rentang di bawah sel.
