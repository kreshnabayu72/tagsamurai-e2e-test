---
id: TC-FA-FAREG-UI-015-form-quantity-kuota-inline
title: "Form Register Asset: validasi Quantity, pesan kuota, dan Remaining Quota"
layer: ui-client
priority: Medium
caseType: Negative
status: draft
sourceRules: ["FAREG-LOGIC-05g", "FAREG-LOGIC-05m", "FI-REG-23", "FI-REG-24", "FLD-REG-05", "V-REG-10", "V-REG-17", "§4.2.1#b3", "§9.5#r1", "§9.9#r6"]
smoke: []
dependsOn: []
trace:
  "FAREG-LOGIC-05g": [17, 31, 34, 40, 46, 48, 49]
  "FAREG-LOGIC-05m": [17, 20, 23, 31, 34, 37, 58, 59, 60, 61]
  "FI-REG-23": [28, 29, 33, 36]
  "FI-REG-24": [26, 42]
  "FLD-REG-05": [2, 4]
  "V-REG-10": [7, 10, 13]
  "V-REG-17": [17, 20, 23, 31, 34, 37, 46, 48]
  "§4.2.1#b3": [13, 14]
  "§9.5#r1": [2, 7]
  "§9.9#r6": 10
anchor: [6, 25, 39, 41]
coverage:
  web: automated
---

# Form Register Asset: validasi Quantity, pesan kuota, dan Remaining Quota

## Prerequisites
- Aktor: Total Control.
- Layar awal: Assets > Registration > Draft
- Komponen: Halaman `Register Asset`
- Data:
  - DU-015-1: sisa kuota tenant `500`.
  - DU-015-2: sisa kuota tenant `20`.
  - DU-015-3: sisa kuota tenant `1`.
  - DU-015-4: sisa kuota tenant `0`.
  - DU-015-5: sisa kuota tenant `10`.
  - DU-015-6: sisa kuota tenant `5`.
  - DU-015-7: Group `Gudang 2` dengan batas, sisa kuota Group `8`.
  - DU-015-8: Group `Gudang 3` dengan batas, sisa kuota Group `1`.
  - DU-015-9: Group `Gudang 4` dengan batas, sisa kuota Group `0`.
  - DU-015-10: Group `Gudang 5` tanpa batas.
  - DU-015-11: Group `Gudang 6` dengan batas, sisa kuota Group `3`.
- Kondisi:
  - K1: Register Asset Bulk Limit bernilai `100`; form `Register Asset` baru dengan satu Item; sisa kuota tenant DU-015-1.
  - K2: Register Asset Bulk Limit bernilai `100`; form `Register Asset` baru dengan satu Item; sisa kuota tenant DU-015-2; Group belum dipilih.
  - K3: Register Asset Bulk Limit bernilai `100`; form `Register Asset` baru dengan satu Item; sisa kuota tenant DU-015-3; Group belum dipilih.
  - K4: Register Asset Bulk Limit bernilai `100`; form `Register Asset` baru dengan satu Item; sisa kuota tenant DU-015-4; Group belum dipilih.
  - K5: Register Asset Bulk Limit bernilai `100`; form `Register Asset` baru dengan satu Item; sisa kuota tenant DU-015-1; pohon Group memuat DU-015-7 sampai DU-015-10.
  - K6: Register Asset Bulk Limit bernilai `100`; form `Register Asset` baru dengan satu Item; sisa kuota tenant DU-015-6; pohon Group memuat DU-015-11.
  - K7: Register Asset Bulk Limit bernilai `100`; form `Register Asset` baru dengan satu Item; sisa kuota tenant DU-015-5; Group belum dipilih.

## Test Steps
### Quantity di dalam rentang dan nilai awal
1. Tampilkan Halaman `Register Asset` dengan kondisi K1
2. Verifikasi sel `Quantity` Item pertama menampilkan nilai awal `1`
3. Klik `[+ Asset Name]`
4. Verifikasi sel `Quantity` Item kedua menampilkan nilai awal `1`
5. Ganti isi sel `Quantity` Item pertama dengan `100`
6. Verifikasi sel `Quantity` Item pertama menampilkan `100`
7. Verifikasi tidak ada pesan error di bawah sel `Quantity` Item pertama

### Quantity di bawah rentang
8. Tampilkan Halaman `Register Asset` dengan kondisi K1
9. Ganti isi sel `Quantity` Item pertama dengan `0`
10. Verifikasi pesan `Quantity must be between 1 and 100` tampil langsung di bawah sel `Quantity`

### Quantity melebihi Register Asset Bulk Limit
11. Tampilkan Halaman `Register Asset` dengan kondisi K1
12. Ganti isi sel `Quantity` Item pertama dengan `101`
13. Verifikasi pesan `For more than 100 assets, use Import.` tampil di bawah sel `Quantity`
14. Verifikasi pesan itu memuat tautan `Import`

### Pesan kuota tenant: banyak, satu, dan nol
15. Tampilkan Halaman `Register Asset` dengan kondisi K2
16. Ganti isi sel `Quantity` Item pertama dengan `25`
17. Verifikasi pesan `Only 20 more assets can be added on your plan. Reduce the quantity.` tampil di bawah sel `Quantity`
18. Tampilkan Halaman `Register Asset` dengan kondisi K3
19. Ganti isi sel `Quantity` Item pertama dengan `2`
20. Verifikasi pesan `Only 1 more asset can be added on your plan. Reduce the quantity.` tampil di bawah sel `Quantity`
21. Tampilkan Halaman `Register Asset` dengan kondisi K4
22. Ganti isi sel `Quantity` Item pertama dengan `1`
23. Verifikasi pesan `No more assets can be added on your plan.` tampil di bawah sel `Quantity`

### Remaining Quota dan pesan kuota Group berubah langsung saat Group berubah
24. Tampilkan Halaman `Register Asset` dengan kondisi K5
25. Verifikasi `Group` masih menampilkan `Select group`
26. Verifikasi `Remaining Quota` tidak tampil sebelum Group dipilih
27. Pilih Group `Gudang 2`
28. Verifikasi `Remaining Quota: 8` tampil di samping field `Group`
29. Verifikasi `Remaining Quota: 500` tidak tampil
30. Ganti isi sel `Quantity` Item pertama dengan `9`
31. Verifikasi pesan `Only 8 more assets can be added to Gudang 2. Reduce the quantity.` tampil di bawah sel `Quantity`
32. Pilih Group `Gudang 3`
33. Verifikasi `Remaining Quota: 1` tampil di samping field `Group`
34. Verifikasi pesan `Only 1 more asset can be added to Gudang 3. Reduce the quantity.` tampil di bawah sel `Quantity`
35. Pilih Group `Gudang 4`
36. Verifikasi `Remaining Quota: 0` tampil di samping field `Group`
37. Verifikasi pesan `No more assets can be added to Gudang 4.` tampil di bawah sel `Quantity`
38. Pilih Group `Gudang 5`
39. Verifikasi `Group` menampilkan `Gudang 5`
40. Verifikasi pesan kuota Group tidak tampil di bawah sel `Quantity`
41. Verifikasi sel `Quantity` Item pertama tetap menampilkan `9`
42. Verifikasi `Remaining Quota` tidak tampil untuk Group tanpa batas

### Sisa kuota tenant dibandingkan lebih dulu dari sisa kuota Group
43. Tampilkan Halaman `Register Asset` dengan kondisi K6
44. Pilih Group `Gudang 6`
45. Ganti isi sel `Quantity` Item pertama dengan `4`
46. Verifikasi pesan `Only 3 more assets can be added to Gudang 6. Reduce the quantity.` tampil di bawah sel `Quantity`
47. Ganti isi sel `Quantity` Item pertama dengan `6`
48. Verifikasi pesan `Only 5 more assets can be added on your plan. Reduce the quantity.` tampil di bawah sel `Quantity`
49. Verifikasi pesan kuota Group tidak tampil bersamaan dengan pesan kuota tenant

### Error kuota ditandai pada Item pertama yang melampaui dan semua Item sesudahnya
50. Tampilkan Halaman `Register Asset` dengan kondisi K7
51. Ganti isi sel `Quantity` Item pertama dengan `4`
52. Klik `[+ Asset Name]`
53. Ganti isi sel `Quantity` Item kedua dengan `4`
54. Klik `[+ Asset Name]`
55. Ganti isi sel `Quantity` Item ketiga dengan `4`
56. Klik `[+ Asset Name]`
57. Ganti isi sel `Quantity` Item keempat dengan `1`
58. Verifikasi pesan kuota tampil di bawah sel `Quantity` Item ketiga
59. Verifikasi pesan kuota tampil di bawah sel `Quantity` Item keempat
60. Verifikasi pesan kuota tidak tampil di bawah sel `Quantity` Item pertama
61. Verifikasi pesan kuota tidak tampil di bawah sel `Quantity` Item kedua
