---
id: TC-FA-ASTL-UI-075-dialog-edit-purchase-bulk
title: "Dialog Edit Purchase mode Bulk"
layer: ui-client
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["FI-03", "FI-04", "FI-05", "FI-06", "FI-08", "FI-10", "EC-29", "§4.1i#b7", "§9.9#r9"]
smoke: []
dependsOn: []
trace:
  "FI-03": 23
  "FI-04": [4, 18, 23]
  "FI-05": [5, 6, 18]
  "FI-06": 7
  "FI-08": [32, 33]
  "FI-10": 30
  "EC-29": [5, 6, 7, 18, 44, 45]
  "§4.1i#b7": [2, 3, 4, 5, 6, 7, 9, 11, 12, 14, 18, 30, 47, 50]
  "§9.9#r9": [39, 40, 41]
anchor: []
coverage:
  web: automated
---
# Dialog Edit Purchase mode Bulk

## Prerequisites
- Aktor: Total Control.
- Layar awal: Fixed Asset > Assets > All Assets.
- Komponen: Dialog Edit Purchase
- Data:
  - DU-075-1: Aset `Laptop Pro 16 - 1`, Asset ID `AST-0001`, Group `IT`, tidak berjejak Posted.
  - DU-075-2: Aset `Laptop Pro 16 - 2`, Asset ID `AST-0002`, Group `IT`, tidak berjejak Posted.
  - DU-075-3: Aset `Server Rack - 1`, Asset ID `AST-0040`, Group `IT`, berjejak Posted.
  - DU-075-4: Aset `Monitor Dell 24 - 6`, Asset ID `AST-0095`, Group `IT`, sudah memiliki 10 Warranty.
  - DU-075-5: Aset `Monitor Dell 24 - 7`, Asset ID `AST-0096`, Group `IT`, sudah memiliki 10 Warranty.
  - DU-075-6: Aset `Proyektor X2 - 1`, Asset ID `AST-0101`, Group `Cabang Bandung`, tidak berjejak Posted.
  - DU-075-7: Aset `Proyektor X2 - 2`, Asset ID `AST-0102`, Group `Cabang Bandung`, tidak berjejak Posted.
  - DU-075-8: Aset `Proyektor X2 - 3`, Asset ID `AST-0103`, Group `Cabang Bandung`, tidak berjejak Posted.
  - DU-075-9: Aset `Proyektor X2 - 4`, Asset ID `AST-0104`, Group `Cabang Bandung`, tidak berjejak Posted.
  - DU-075-10: Aset `Proyektor X2 - 5`, Asset ID `AST-0105`, Group `Cabang Bandung`, tidak berjejak Posted.
  - DU-075-11: Aset `Proyektor X2 - 6`, Asset ID `AST-0106`, Group `Cabang Bandung`, tidak berjejak Posted.
  - DU-075-12: Aset `Proyektor X2 - 7`, Asset ID `AST-0107`, Group `Cabang Bandung`, tidak berjejak Posted.
  - DU-075-13: Purchase Cost `5.000.000,00`.
  - DU-075-14: Reference Price Currency `USD` dan jumlah `1.150,00`.
  - DU-075-15: Warranty baru `Garansi tambahan bulk` sampai `01/12/27` Provider `Dell Service`.
  - DU-075-16: Purchase Cost `0`.
  - DU-075-17: Custom field Purchasing tidak wajib `Vendor note` bertipe Text, dibiarkan kosong pada Bulk.
  - Teks yang diharapkan: `Monitor Dell 24 - 6 would exceed 10 warranties.` dan `Monitor Dell 24 - 7 would exceed 10 warranties.`, dari nama aset DU-075-4 dan DU-075-5.
  - Teks yang diharapkan untuk dua aset: `2 assets selected`, dari jumlah aset 2; untuk satu aset: `1 asset selected`, dari jumlah aset 1; untuk tujuh aset: `7 assets selected`, dari jumlah aset 7.
- Kondisi:
  - K1: Bulk, seleksi DU-075-1 dan DU-075-2; simpan berhasil.
  - K2: Bulk, seleksi DU-075-1 saja.
  - K3: Bulk, seleksi tujuh aset DU-075-6 sampai DU-075-12.
  - K4: Bulk, seleksi DU-075-1 dan DU-075-3.
  - K5: Bulk, seleksi DU-075-4 dan DU-075-5; simpan ditolak server karena kedua aset melampaui 10 Warranty setelah penambahan.

## Test Steps

### Tampilan awal Bulk untuk dua aset
1. Tampilkan Dialog Edit Purchase dengan kondisi K1
2. Verifikasi dialog berjudul `Edit Purchase` tampil dengan teks `2 assets selected`
3. Verifikasi bullet `Laptop Pro 16 - 1` dan `Laptop Pro 16 - 2` tampil di bawah teks jumlah aset
4. Verifikasi field Purchase Date, Reference Price, dan daftar Warranty kosong
5. Verifikasi field berlabel `Purchase Cost (per asset)` kosong dengan helper text `This value will be applied to each selected asset.`
6. Verifikasi tidak ada tampilan total Purchase Cost
7. Verifikasi bagian Additional costs tidak tampil

### Teks jumlah aset untuk satu aset
8. Tampilkan Dialog Edit Purchase dengan kondisi K2
9. Verifikasi teks `1 asset selected` tampil

### Daftar bullet tujuh aset
10. Tampilkan Dialog Edit Purchase dengan kondisi K3
11. Verifikasi teks `7 assets selected` tampil
12. Verifikasi bullet `Proyektor X2 - 1` sampai `Proyektor X2 - 5` terlihat tanpa menggulir
13. Gulir daftar bullet sampai bawah
14. Verifikasi bullet `Proyektor X2 - 6` dan `Proyektor X2 - 7` terlihat

### Purchase Cost diterapkan per aset
15. Tampilkan Dialog Edit Purchase dengan kondisi K1
16. Isi `Purchase Cost (per asset)` `5.000.000,00`
17. Klik `[Save]`
18. Verifikasi permintaan simpan membawa Purchase Cost `5.000.000,00` untuk setiap aset terpilih tanpa dibagi jumlah aset dan tanpa field lain yang kosong

### Reference Price diterapkan per aset
19. Tampilkan Dialog Edit Purchase dengan kondisi K1
20. Pilih Currency `USD` pada Reference Price
21. Isi jumlah Reference Price `1.150,00`
22. Klik `[Save]`
23. Verifikasi permintaan simpan membawa Reference Price `USD` dan `1.150,00` untuk setiap aset terpilih tanpa dibagi jumlah aset

### Baris Warranty ditambahkan ke setiap aset
24. Tampilkan Dialog Edit Purchase dengan kondisi K1
25. Klik `[+ Add warranty]`
26. Isi Warranty name `Garansi tambahan bulk`
27. Pilih Warranty until `01/12/27`
28. Isi Provider `Dell Service`
29. Klik `[Save]`
30. Verifikasi permintaan simpan membawa satu baris Warranty `Garansi tambahan bulk` sampai `01/12/27` dengan Provider `Dell Service` yang berlaku untuk kedua aset terpilih

### Aset berjejak Posted mengunci tanggal dan biaya seluruh seleksi
31. Tampilkan Dialog Edit Purchase dengan kondisi K4
32. Verifikasi field Purchase Date dan `Purchase Cost (per asset)` read-only untuk seluruh seleksi
33. Verifikasi field Reference Price dapat diisi

### Penolakan server karena batas 10 Warranty terlampaui
34. Tampilkan Dialog Edit Purchase dengan kondisi K5
35. Klik `[+ Add warranty]`
36. Isi Warranty name `Garansi tambahan bulk`
37. Pilih Warranty until `01/12/27`
38. Klik `[Save]`
39. Verifikasi alert inline `Monitor Dell 24 - 6 would exceed 10 warranties.` tampil
40. Verifikasi alert inline `Monitor Dell 24 - 7 would exceed 10 warranties.` tampil
41. Verifikasi dialog `Edit Purchase` tetap terbuka

### Purchase Cost 0 pada Bulk tanpa helper text nilai nol
42. Tampilkan Dialog Edit Purchase dengan kondisi K1
43. Isi `Purchase Cost (per asset)` `0`
44. Verifikasi helper text `This value will be applied to each selected asset.` tampil di bawah `Purchase Cost (per asset)`
45. Verifikasi helper text `Asset value will be 0 and the asset will not be depreciated.` tidak tampil

### Custom field Purchasing yang kosong tidak menimpa nilai aset pada Bulk
46. Tampilkan Dialog Edit Purchase dengan kondisi K1
47. Verifikasi custom field Purchasing `Vendor note` tampil dan kosong
48. Isi `Purchase Cost (per asset)` `5.000.000,00`
49. Klik `[Save]`
50. Verifikasi permintaan simpan tidak memuat custom field `Vendor note` sehingga nilai `Vendor note` kedua aset terpilih tidak ditimpa
