---
id: TC-FA-ASTL-UI-074-dialog-edit-purchase-additional-costs
title: "Validasi Additional costs"
layer: ui-client
priority: Medium
caseType: Negative
status: ready-for-automation
sourceRules: ["ASTL-LOGIC-21k", "FI-11", "V-14", "V-15", "V-17", "FLD-34", "FLD-35", "§4.1i#b9", "§9.9#r8", "§9.9#r10"]
smoke: []
dependsOn: []
trace:
  "ASTL-LOGIC-21k": [17, 37, 39, 45, 49]
  "FI-11": [4, 6]
  "V-14": 10
  "V-15": 11
  "V-17": 17
  "FLD-34": 4
  "FLD-35": 4
  "§4.1i#b9": [2, 4]
  "§9.9#r8": [10, 17, 21, 23, 25]
  "§9.9#r10": [11, 29, 31, 33, 35]
anchor: []
coverage:
  web: automated
---
# Validasi Additional costs

## Prerequisites
- Aktor: Total Control.
- Layar awal: Fixed Asset > Assets > All Assets.
- Komponen: Dialog Edit Purchase
- Data:
  - DU-074-1: Aset `Monitor Dell 24 - 3`, Asset ID `AST-0092`, Group `IT`, tidak berjejak Posted, Additional costs `Ongkos kirim` `250.000,00`.
  - DU-074-2: Aset `Monitor Dell 24 - 4`, Asset ID `AST-0093`, Group `IT`, tidak berjejak Posted, sembilan Additional costs dengan pola nama `Biaya tambahan {n}` masing-masing `100.000,00`.
  - DU-074-3: Aset `Monitor Dell 24 - 5`, Asset ID `AST-0094`, Group `IT`, tidak berjejak Posted, Purchase Cost `9.999.999.999.999,00`.
  - DU-074-4: Aset `Printer Laser - 4`, Asset ID `AST-0034`, Group `IT`, tidak berjejak Posted, Additional costs `Bea masuk` `9.999.999.999.999,00`.
  - DU-074-5: Aset `Printer Laser - 5`, Asset ID `AST-0035`, Group `IT`, tidak berjejak Posted, tanpa Additional costs.
  - DU-074-6: Additional cost baru dengan nama sama berbeda huruf besar-kecil `ongkos kirim` jumlah `100.000,00`.
  - DU-074-7: Name Additional cost tepat di batas `Biaya DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD` (120 karakter).
  - DU-074-8: Name Additional cost satu di atas batas `Biaya DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD` (121 karakter).
  - DU-074-9: Name Additional cost berisi emoji `Bea😊masuk`, yang diharapkan tersimpan di field `Beamasuk`.
  - DU-074-10: Amount tepat di batas `1234567890123,45` (15 digit termasuk 2 digit desimal).
  - DU-074-11: Amount satu di atas batas `12345678901234,56` (16 digit termasuk 2 digit desimal).
  - DU-074-12: Amount dengan tiga digit desimal `1,234`, yang diharapkan tersimpan di field `1,23`.
  - DU-074-13: Amount bertanda minus `-50`, yang diharapkan tersimpan di field `50`.
  - DU-074-14: Additional cost baru `Bea masuk` jumlah `100,00`.
  - DU-074-15: Purchase Cost `100,00`.
- Kondisi:
  - K1: satu aset terpilih, DU-074-1; simpan berhasil.
  - K2: satu aset terpilih, DU-074-2; batas baris Additional costs adalah 10.
  - K3: satu aset terpilih, DU-074-3; simpan ditolak karena total Purchase Cost ditambah Additional costs melebihi 15 digit.
  - K4: Bulk, seleksi DU-074-4 dan DU-074-5; simpan ditolak server karena total Purchase Cost ditambah Additional costs tersimpan DU-074-4 melebihi 15 digit.

## Test Steps

### Menambah dan menghapus baris Additional costs
1. Tampilkan Dialog Edit Purchase dengan kondisi K1
2. Verifikasi bagian Additional costs memuat baris `Ongkos kirim` dengan jumlah `250.000,00`
3. Klik `[+ Add additional cost]`
4. Verifikasi baris baru bertambah dengan field `Name` ber-placeholder `Enter name` dan field `Amount` ber-placeholder `Enter amount`, keduanya kosong
5. Klik `✕` pada baris baru
6. Verifikasi baris baru hilang dan baris `Ongkos kirim` tetap ada

### Name dan Amount wajib diisi
7. Tampilkan Dialog Edit Purchase dengan kondisi K1
8. Klik `[+ Add additional cost]`
9. Klik `[Save]`
10. Verifikasi pesan `Additional cost name must not be empty` tampil di bawah field Name baris baru
11. Verifikasi pesan `Additional cost amount must not be empty` tampil di bawah field Amount baris baru

### Name harus unik per aset tanpa membedakan huruf besar-kecil
12. Tampilkan Dialog Edit Purchase dengan kondisi K1
13. Klik `[+ Add additional cost]`
14. Isi Name `ongkos kirim`
15. Isi Amount `100.000,00`
16. Klik `[Save]`
17. Verifikasi pesan `Additional cost name already exists` tampil di bawah field Name baris baru

### Batas 120 karakter dan emoji pada Name
18. Tampilkan Dialog Edit Purchase dengan kondisi K1
19. Klik `[+ Add additional cost]`
20. Isi Name `Biaya DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD` (120 karakter)
21. Verifikasi field Name menerima nilai tanpa pesan `Max. 120 characters`
22. Isi Name `Biaya DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD` (121 karakter)
23. Verifikasi pesan `Max. 120 characters` tampil di bawah field Name
24. Isi Name `Bea😊masuk`
25. Verifikasi field Name berisi `Beamasuk` karena emoji diblok di input

### Batas 15 digit, desimal, dan minus pada Amount
26. Tampilkan Dialog Edit Purchase dengan kondisi K1
27. Klik `[+ Add additional cost]`
28. Isi Amount `1234567890123,45`
29. Verifikasi field Amount menerima nilai tanpa pesan `Max. 15 characters`
30. Isi Amount `12345678901234,56`
31. Verifikasi pesan `Max. 15 characters` tampil di bawah field Amount
32. Isi Amount `1,234`
33. Verifikasi field Amount berisi `1,23` karena digit desimal ketiga diblok
34. Isi Amount `-50`
35. Verifikasi field Amount berisi `50` karena tanda minus diblok

### Batas sepuluh baris Additional costs
36. Tampilkan Dialog Edit Purchase dengan kondisi K2
37. Verifikasi `[+ Add additional cost]` aktif pada sembilan baris Additional costs
38. Klik `[+ Add additional cost]`
39. Verifikasi `[+ Add additional cost]` Disabled pada sepuluh baris Additional costs

### Total Purchase Cost dan Additional costs satu aset melebihi 15 digit
40. Tampilkan Dialog Edit Purchase dengan kondisi K3
41. Klik `[+ Add additional cost]`
42. Isi Name `Bea masuk`
43. Isi Amount `100,00`
44. Klik `[Save]`
45. Verifikasi pesan `Max. 15 characters` tampil di bawah field Purchase Cost dan dialog `Edit Purchase` tetap terbuka

### Total pada Bulk melebihi 15 digit ditolak server
46. Tampilkan Dialog Edit Purchase dengan kondisi K4
47. Isi `Purchase Cost (per asset)` `100,00`
48. Klik `[Save]`
49. Verifikasi pesan `Max. 15 characters` tampil di bawah field `Purchase Cost (per asset)` dan dialog `Edit Purchase` tetap terbuka
