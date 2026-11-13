---
id: TC-FA-FAREG-UI-013-form-general-information-tampilan
title: "Form Register Asset: tampilan awal tab General Information, tabel Item, dan footer"
layer: ui-client
priority: Medium
caseType: Positive
status: draft
sourceRules: [FAREG-LOGIC-01g, FAREG-LOGIC-15a, FLD-REG-01, "§2.1#p1", "§4.1#r4", "§4.1#p1", "§4.1#b9", "§4.1#b10", "§4.1#b11", "§4.1#b13", "§4.1#b14", "§4.1#b15", "§4.1#b19", "§4.1#b31", "§4.1#b33", "§4.1#p26", "§4.1#r90", "§4.1#r91", "§4.1#r92", "§4.1#r93", "§4.1#r94", "§4.1#r95", "§4.1#r96", "§4.1#r97", "§4.1#p42", "§4.2#p1", "§4.2.1#p1", "§9.2#p14", "§9.4.3#b11", "EB-FRM-7@form-register-asset"]
smoke: []
dependsOn: []
trace:
  FAREG-LOGIC-01g: [60, 30]
  FAREG-LOGIC-15a: 60
  FLD-REG-01: [16, 19, 20, 23, 25]
  "§2.1#p1": 60
  "§4.1#r4": 6
  "§4.1#p1": 7
  "§4.1#b9": 6
  "§4.1#b10": 9
  "§4.1#b11": [10, 11, 29]
  "§4.1#b13": 7
  "§4.1#b14": 13
  "§4.1#b15": [55, 66]
  "§4.1#b19": 57
  "§4.1#b31": 10
  "§4.1#b33": 12
  "§4.1#p26": [49, 50, 51, 52, 53, 55]
  "§4.1#r90": 32
  "§4.1#r91": 33
  "§4.1#r92": 34
  "§4.1#r93": [35, 36]
  "§4.1#r94": [37, 38]
  "§4.1#r95": [39, 40]
  "§4.1#r96": [41, 42]
  "§4.1#r97": [44, 45]
  "§4.1#p42": [19, 23, 25]
  "§4.2#p1": [3, 4, 5, 8]
  "§4.2.1#p1": [2, 27]
  "§9.2#p14": 61
  "§9.4.3#b11": 60
  EB-FRM-7@form-register-asset: [63, 64, 67]
anchor: [47, 59]
coverage:
  web: automated
---

# Form Register Asset: tampilan awal tab General Information, tabel Item, dan footer

## Prerequisites
- Aktor: Total Control.
- Layar awal: Assets > Registration > Draft
- Komponen: Halaman `Register Asset`
- Data:
  - DU-013-1: Group `Kantor Pusat`, induk dari `Gudang 1`, Assignable `Ya`, Excess `Tidak`.
  - DU-013-2: Group `Gudang 1`, anak dari `Kantor Pusat`, Assignable `Ya`, Excess `Tidak`.
  - DU-013-3: Group `Gudang Retur`, anak dari `Kantor Pusat`, Assignable `Tidak`, Excess `Tidak`.
  - DU-013-4: Group `Gudang Excess Pusat`, anak dari `Kantor Pusat`, Assignable `Ya`, Excess `Ya`.
  - DU-013-5: Item draft 1, Category `Elektronik > Komputer > Laptop`, Asset Name `Laptop Dell Latitude 5440`, Brand `Dell`, Model `Latitude 5440`, TAG Type `RFID`, Quantity `10`.
  - DU-013-6: Item draft 2, Category `Furnitur > Kursi`, Asset Name `Kursi Kerja Ergonomis`, Brand `Ergotec`, Model `ErgoMesh 200`, TAG Type `QR`, Quantity `20`.
- Kondisi:
  - K1: form `Register Asset` baru tanpa draft tersimpan; Group belum dipilih; tabel Item berisi satu Item dengan Quantity awal; pohon Group berisi DU-013-1 sampai DU-013-4.
  - K2: form `Edit` draft tersimpan dengan Group DU-013-2; tabel Item berisi DU-013-5 lalu DU-013-6 berurutan.

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
16. Verifikasi field `Group` menampilkan `Gudang 1`
17. Buka pemilih `Group`
18. Klik node `Kantor Pusat`
19. Verifikasi field `Group` menampilkan `Kantor Pusat` sebagai node induk yang dapat dipilih
20. Verifikasi `Gudang 1` tidak lagi menjadi nilai field `Group`
21. Buka pemilih `Group`
22. Klik node `Gudang Excess Pusat`
23. Verifikasi field `Group` tetap menampilkan `Kantor Pusat`
24. Klik node `Gudang Retur`
25. Verifikasi field `Group` tetap menampilkan `Kantor Pusat`

### Footer, Breadcrumb, dan tab Asset pada draft tersimpan
26. Tampilkan Halaman `Register Asset` dengan kondisi K2
27. Verifikasi Breadcrumb menampilkan `Assets > Registration > Draft` dan segmen terakhir `Edit`
28. Klik tab `Asset`
29. Verifikasi footer tab `Asset` memuat `[Cancel]`, `[Save draft]`, dan `[Submit]`
30. Verifikasi tab `Asset` tidak memuat field Purchase

### Kolom tabel Item pada form baru
31. Tampilkan Halaman `Register Asset` dengan kondisi K1
32. Verifikasi kolom `Number` menampilkan `1` pada Item pertama
33. Verifikasi kolom `Category` menampilkan placeholder `Select category`
34. Verifikasi kolom `Asset Name` menampilkan placeholder `Select asset name`
35. Verifikasi kolom `Brand` menampilkan placeholder `Select brand`
36. Verifikasi `Brand` Disabled sebelum Asset Name dipilih
37. Verifikasi kolom `Model` menampilkan placeholder `Select model`
38. Verifikasi `Model` Disabled sebelum Brand dipilih
39. Verifikasi sel `TAG Type` menampilkan `—`
40. Verifikasi sel `TAG Type` Read-only
41. Verifikasi kolom `Quantity` menampilkan `1`
42. Verifikasi sel `Quantity` tidak memiliki placeholder
43. Klik row option (titik tiga) pada Item pertama
44. Verifikasi `Remove from List` Disabled
45. Verifikasi tooltip `At least one item is required.` tampil saat pointer berada di `Remove from List`

### Tabel Item tanpa sort, kolom, paginasi, Search, dan filter; sel dapat diedit; tambah Item
46. Tampilkan Halaman `Register Asset` dengan kondisi K2
47. Verifikasi tabel Item memuat `Laptop Dell Latitude 5440` lalu `Kursi Kerja Ergonomis` berurutan
48. Klik header kolom `Asset Name`
49. Verifikasi urutan Item tetap `Laptop Dell Latitude 5440` lalu `Kursi Kerja Ergonomis`
50. Verifikasi kontrol column visibility tidak tampil pada tabel Item
51. Verifikasi paginasi tidak tampil pada tabel Item
52. Verifikasi kotak Search tidak tampil pada tabel Item
53. Verifikasi filter tidak tampil pada tabel Item
54. Ganti isi sel `Quantity` Item pertama dengan `5`
55. Verifikasi sel `Quantity` Item pertama menampilkan `5` dan tabel tetap berupa tabel editable
56. Klik `[+ Asset Name]`
57. Verifikasi tabel Item memuat tiga Item dengan `Number` `3` pada Item baru

### Field Purchase dan Project tidak ada di form
58. Tampilkan Halaman `Register Asset` dengan kondisi K1
59. Verifikasi tabel Item tampil dengan kolom `Asset Name`
60. Verifikasi tidak ada field Purchase di tab `General Information`
61. Verifikasi tidak ada field `Project` di tab `General Information`

### Aksesibilitas field dan pesan error di bawah sel
62. Tampilkan Halaman `Register Asset` dengan kondisi K1
63. Verifikasi field `Group`, `Asset Name`, `Brand`, dan `Model` memiliki atribut aria-required
64. Verifikasi kontrol row option (titik tiga) memiliki label aksesibel
65. Ganti isi sel `Quantity` Item pertama dengan `0`
66. Verifikasi pesan error tampil di bawah sel `Quantity`
67. Verifikasi sel `Quantity` yang menampilkan pesan error memiliki atribut aria-describedby
