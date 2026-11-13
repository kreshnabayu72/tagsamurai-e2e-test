---
id: TC-FA-FAREG-UI-016-form-remove-item-quantity-turun
title: "Form Register Asset: Remove from List, Quantity turun, dan dialog Remove Assets"
layer: ui-client
priority: Medium
caseType: Positive
status: draft
sourceRules: ["D-REG-18", "FAREG-LOGIC-03o", "FAREG-LOGIC-03u", "FI-REG-07", "S-REG-16", "T-REG-12", "T-REG-13", "T-REG-15", "§4.8#r25", "§9.6#r13", "§9.6#r14", "EB-FB-1@remove-item"]
smoke: []
dependsOn: []
trace:
  "D-REG-18": [16, 17, 18, 19, 20, 22, 34, 35, 36, 37]
  "FAREG-LOGIC-03o": [16, 34]
  "FAREG-LOGIC-03u": [9, 16, 32]
  "FI-REG-07": [9, 12, 16, 23, 28]
  "S-REG-16": [3, 4]
  "T-REG-12": [43, 52]
  "T-REG-13": 48
  "T-REG-15": [9, 27]
  "§4.8#r25": [3, 7, 9, 16]
  "§9.6#r13": [32, 34, 39, 52]
  "§9.6#r14": [9, 11, 27, 28, 43, 44, 48, 49]
  "EB-FB-1@remove-item": [9, 43]
anchor: [10, 31]
coverage:
  web: automated
---

# Form Register Asset: Remove from List, Quantity turun, dan dialog Remove Assets

## Prerequisites
- Aktor: Total Control.
- Layar awal: Assets > Registration > Draft
- Komponen: Halaman `Register Asset`
- Data:
  - DU-016-1: Item `Laptop Dell Latitude 5440` dengan Quantity `3`; Name sementara aset `Laptop Dell Latitude 5440 - 1`, `Laptop Dell Latitude 5440 - 2`, `Laptop Dell Latitude 5440 - 3`; semua aset masih kosong.
  - DU-016-2: Item `Kursi Kerja Ergonomis` dengan Quantity `2`; Name sementara aset `Kursi Kerja Ergonomis - 1` dan `Kursi Kerja Ergonomis - 2`; semua aset masih kosong.
  - DU-016-3: Item `Printer Epson L3250` dengan Quantity `2`; aset `Printer Epson L3250 - 1` berisi Tag `RFID-000123`; aset `Printer Epson L3250 - 2` berisi Foto `printer-2.jpg`.
- Kondisi:
  - K1: form `Edit` draft tersimpan dengan Item DU-016-1 saja.
  - K2: form `Edit` draft tersimpan dengan Item DU-016-1, DU-016-2, dan DU-016-3; semua Item masih Draft.
  - K3: sama dengan K2; hapus Item gagal karena error server.
  - K4: sama dengan K2; hapus Item gagal karena gangguan jaringan.
  - K5: sama dengan K2; Quantity turun gagal karena error server.

## Test Steps
### Remove from List Disabled bila hanya satu Item
1. Tampilkan Halaman `Register Asset` dengan kondisi K1
2. Klik row option (titik tiga) pada Item `Laptop Dell Latitude 5440`
3. Verifikasi `Remove from List` berstatus Disabled karena hanya satu Item
4. Verifikasi tooltip `At least one item is required.` tampil pada `Remove from List` yang Disabled

### Item yang semua asetnya kosong dihapus langsung dengan toast
5. Tampilkan Halaman `Register Asset` dengan kondisi K2
6. Klik row option (titik tiga) pada Item `Kursi Kerja Ergonomis`
7. Verifikasi `Remove from List` tidak Disabled pada draft dengan tiga Item
8. Klik `Remove from List`
9. Verifikasi toast `Success, item has been deleted.` tampil
10. Verifikasi tabel Item masih memuat `Laptop Dell Latitude 5440`
11. Verifikasi `Kursi Kerja Ergonomis` tidak tampil lagi di tabel Item
12. Verifikasi dialog `Remove Assets` tidak tampil

### Item yang asetnya berisi data membuka dialog Remove Assets lebih dulu
13. Tampilkan Halaman `Register Asset` dengan kondisi K2
14. Klik row option (titik tiga) pada Item `Printer Epson L3250`
15. Klik `Remove from List`
16. Verifikasi dialog `Remove Assets` tampil sebelum Item dihapus
17. Verifikasi bullet `Printer Epson L3250 - 1` dan `Printer Epson L3250 - 2` tampil tanpa diringkas di dialog
18. Verifikasi dialog memuat `Their TAG, photo, and custom field data will be lost. This action cannot be undone.`
19. Verifikasi dialog memuat pertanyaan `Are you sure you want to remove them?`
20. Verifikasi dialog memuat tombol `[Cancel]` dan `[Remove]`
21. Klik `[Cancel]`
22. Verifikasi dialog `Remove Assets` tertutup
23. Verifikasi `Printer Epson L3250` masih tampil di tabel Item
24. Klik row option (titik tiga) pada Item `Printer Epson L3250`
25. Klik `Remove from List`
26. Klik `[Remove]`
27. Verifikasi toast `Success, item has been deleted.` tampil
28. Verifikasi `Printer Epson L3250` tidak tampil lagi di tabel Item

### Quantity turun menghapus aset increment terakhir
29. Tampilkan Halaman `Register Asset` dengan kondisi K2
30. Ganti isi sel `Quantity` Item `Laptop Dell Latitude 5440` dengan `2`
31. Verifikasi sel `Quantity` Item `Laptop Dell Latitude 5440` menampilkan `2`
32. Verifikasi dialog `Remove Assets` tidak tampil untuk Item yang semua asetnya kosong
33. Ganti isi sel `Quantity` Item `Printer Epson L3250` dengan `1`
34. Verifikasi dialog `Remove Assets` tampil untuk aset increment terakhir yang berisi data
35. Verifikasi bullet `Printer Epson L3250 - 2` tampil di dialog
36. Verifikasi bullet `Printer Epson L3250 - 1` tidak tampil di dialog
37. Verifikasi dialog memuat pertanyaan `Are you sure you want to remove it?`
38. Klik `[Remove]`
39. Verifikasi sel `Quantity` Item `Printer Epson L3250` menampilkan `1`

### Hapus Item gagal karena error server
40. Tampilkan Halaman `Register Asset` dengan kondisi K3
41. Klik row option (titik tiga) pada Item `Kursi Kerja Ergonomis`
42. Klik `Remove from List`
43. Verifikasi toast Error `Error, failed to delete item.` tampil
44. Verifikasi form `Register Asset` tetap terbuka dengan `Kursi Kerja Ergonomis` masih tampil di tabel Item

### Hapus Item gagal karena gangguan jaringan
45. Tampilkan Halaman `Register Asset` dengan kondisi K4
46. Klik row option (titik tiga) pada Item `Kursi Kerja Ergonomis`
47. Klik `Remove from List`
48. Verifikasi toast Error `Connection problem. Please try again.` tampil
49. Verifikasi form `Register Asset` tetap terbuka dengan `Kursi Kerja Ergonomis` masih tampil di tabel Item

### Quantity turun gagal karena error server
50. Tampilkan Halaman `Register Asset` dengan kondisi K5
51. Ganti isi sel `Quantity` Item `Laptop Dell Latitude 5440` dengan `2`
52. Verifikasi toast Error dengan awalan `Error, failed to` tampil
