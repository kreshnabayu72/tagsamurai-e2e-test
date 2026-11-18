---
id: TC-FA-ASTL-UI-071-dialog-edit-purchase-tampilan
title: "Tampilan awal dan state Dialog Edit Purchase"
layer: ui-client
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["FI-01", "FI-07", "S-17", "S-35", "S-36", "S-37", "D-13", "FLD-33", "§4.1i#p1", "§4.1i#b1", "§4.1i#b3", "§4.1i#b6", "§4.1i#b10", "§9.9#r7", "§9.9#r11"]
smoke: []
dependsOn: []
trace:
  "FI-01": 6
  "FI-07": [22, 24, 26]
  "S-17": [22, 24, 26, 31, 46, 48, 50, 58]
  "S-35": 8
  "S-36": 10
  "S-37": 12
  "D-13": [2, 3, 20]
  "FLD-33": [4, 30, 39]
  "§4.1i#p1": [2, 29]
  "§4.1i#b1": 5
  "§4.1i#b3": [8, 10, 12]
  "§4.1i#b6": [2, 4, 6]
  "§4.1i#b10": [22, 24, 26, 27, 31, 32, 33, 35, 37, 46, 48, 50, 52, 56, 58]
  "§9.9#r7": [14, 16, 18, 73, 76, 78, 79]
  "§9.9#r11": [40, 43, 63, 66, 68]
anchor: [62, 72]
coverage:
  web: automated
---
# Tampilan awal dan state Dialog Edit Purchase

## Prerequisites
- Aktor: Total Control.
- Layar awal: Fixed Asset > Assets > All Assets.
- Komponen: Dialog Edit Purchase
- Data:
  - DU-071-1: Aset `Laptop Pro 16 - 1`, Asset ID `AST-0001`, Group `IT`, Purchase `Complete`, tidak berjejak Posted; Purchase Date `10/03/26`, Purchase Cost `18.500.000,00`, Reference Price Currency `USD` jumlah `1.150,00`, Document No. `INV-2026-0301`, Additional costs `Ongkos kirim` `250.000,00`, Warranty `Garansi mesin` sampai `10/03/27` Provider `Lenovo Care Center`, custom field Purchasing wajib `Contract number` bernilai `CN-0042`, custom field Purchasing tidak wajib `Vendor note` bertipe Text dan kosong.
  - DU-071-2: Aset `Server Rack - 1`, Asset ID `AST-0040`, Group `IT`, Purchase `Complete`, berjejak Posted; Purchase Date `05/01/26`, Purchase Cost `52.000.000,00`, Document No. `INV-2026-0105`, Additional costs `Instalasi` `1.500.000,00`.
  - DU-071-3: Aset `Laptop Pro 16 - 2`, Asset ID `AST-0002`, Group `IT`, Purchase `Complete`, tidak berjejak Posted.
  - DU-071-4: Aset `Printer Laser - 2`, Asset ID `AST-0032`, Group `IT`, Purchase `Complete`, predikat berjejak Posted tidak dapat dibaca; Purchase Date `20/02/26`, Purchase Cost `7.500.000,00`, Additional costs `Pemasangan` `300.000,00`.
  - DU-071-5: Aset `Kursi Kerja - 1`, Asset ID `AST-0072`, Group `GA`, Purchase `Pending` dengan seluruh field Purchase kosong, predikat berjejak Posted dapat dibaca tidak berjejak Posted; custom field Purchasing wajib `Contract number` kosong.
  - DU-071-6: Aset `Meja Rapat - 2`, Asset ID `AST-0051`, Group `GA`, Purchase `Pending`, predikat berjejak Posted tidak dapat dibaca.
  - DU-071-7: Document No. tepat di batas `INV-2026-AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA` (120 karakter).
  - DU-071-8: Document No. satu di atas batas `INV-2026-AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA` (121 karakter).
  - DU-071-9: Document No. berisi emoji `PO😊77`, yang diharapkan tersimpan di field `PO77`.
  - DU-071-10: Document No. `INV-2026-0302`.
  - DU-071-11: Purchase Date `15/03/26` dan Purchase Cost `9.500.000,00` yang diisi pada aset DU-071-6.
  - DU-071-12: Vendor note 120 karakter `Catatan vendor BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB` (120 karakter).
  - DU-071-13: Vendor note 121 karakter `Catatan vendor BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB` (121 karakter).
  - DU-071-14: Document No. `INV-2026-0105`, sama dengan Document No. DU-071-2.
  - Pesan yang diharapkan untuk custom field wajib kosong: `Contract number must not be empty`, dari nama field `Contract number`.
- Kondisi:
  - K1: satu aset terpilih, DU-071-1.
  - K2: satu aset terpilih, DU-071-2.
  - K3: Bulk, seleksi DU-071-3 dan DU-071-2.
  - K4: Bulk, seleksi DU-071-3 dan DU-071-4.
  - K5: Bulk, seleksi DU-071-3 dan DU-071-6.
  - K6: satu aset terpilih, DU-071-5.
  - K7: satu aset terpilih, DU-071-4.
  - K8: satu aset terpilih, DU-071-6; simpan berhasil.
  - K9: satu aset terpilih, DU-071-6 sesudah DU-071-11 tersimpan sehingga Purchase `Complete`; predikat berjejak Posted tetap tidak dapat dibaca.
  - K10: satu aset terpilih, DU-071-1; simpan berhasil.

## Test Steps

### Satu aset tampil dengan nilai tersimpan
1. Tampilkan Dialog Edit Purchase dengan kondisi K1
2. Verifikasi dialog berjudul `Edit Purchase` tampil dengan nama aset `Laptop Pro 16 - 1` di atas field
3. Verifikasi tombol `[Clear Field]` dan `[Save]` tampil
4. Verifikasi field Purchase Date `10/03/26`, Purchase Cost `18.500.000,00`, dan Document No. `INV-2026-0301` terisi nilai tersimpan
5. Verifikasi field Reference Price, Additional costs, daftar Warranty, dan custom field `Contract number` tampil
6. Verifikasi `[Save]` Disabled karena belum ada perubahan

### Tooltip info fungsi field
7. Arahkan kursor ke ikon info di samping label `Document No.`
8. Verifikasi fungsi field `Document No.` tersampaikan lewat teks `The PO or invoice number, used to trace this asset to its purchase document.`
9. Arahkan kursor ke ikon info di samping label `Additional costs`
10. Verifikasi fungsi bagian `Additional costs` tersampaikan lewat teks `Costs to bring the asset into use, such as shipping, installation, and import duty. They are added to the acquisition cost.`
11. Arahkan kursor ke ikon info di samping label `Reference Price`
12. Verifikasi fungsi field `Reference Price` tersampaikan lewat teks `A note of the price in another currency, for example the invoice amount. It is not used in asset value or depreciation.`

### Batas karakter dan emoji pada Document No.
13. Ganti isi field Document No. dengan `INV-2026-AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA` (120 karakter)
14. Verifikasi field Document No. menerima nilai 120 karakter tanpa pesan `Max. 120 characters`
15. Ganti isi field Document No. dengan `INV-2026-AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA` (121 karakter)
16. Verifikasi pesan `Max. 120 characters` tampil di bawah field Document No.
17. Ganti isi field Document No. dengan `PO😊77`
18. Verifikasi field Document No. berisi `PO77` karena emoji diblok di input

### Aset berjejak Posted mengunci tanggal, biaya, dan Additional costs
19. Tampilkan Dialog Edit Purchase dengan kondisi K2
20. Verifikasi dialog berjudul `Edit Purchase` tampil dengan nama aset `Server Rack - 1` di atas field
21. Arahkan kursor ke field Purchase Date
22. Verifikasi field Purchase Date read-only dengan alasan `Asset has posted depreciation or journal entries. Use Value Change in the Accounting tab.`
23. Arahkan kursor ke field Purchase Cost
24. Verifikasi field Purchase Cost read-only dengan alasan `Asset has posted depreciation or journal entries. Use Value Change in the Accounting tab.`
25. Arahkan kursor ke bagian Additional costs
26. Verifikasi bagian Additional costs read-only dengan alasan `Asset has posted depreciation or journal entries. Use Value Change in the Accounting tab.`
27. Verifikasi field Document No. tetap dapat diubah

### Bulk dengan satu aset berjejak Posted
28. Tampilkan Dialog Edit Purchase dengan kondisi K3
29. Verifikasi dialog berjudul `Edit Purchase` tampil
30. Verifikasi field Document No. tidak tampil
31. Verifikasi field Purchase Date read-only untuk seluruh seleksi dengan alasan `Asset has posted depreciation or journal entries. Use Value Change in the Accounting tab.`
32. Verifikasi field `Purchase Cost (per asset)` read-only untuk seluruh seleksi
33. Verifikasi field Reference Price dapat diisi

### Bulk dengan aset Complete yang predikat Posted-nya tidak terbaca
34. Tampilkan Dialog Edit Purchase dengan kondisi K4
35. Verifikasi field Purchase Date dan `Purchase Cost (per asset)` read-only untuk seluruh seleksi

### Bulk dengan aset Pending yang predikat Posted-nya tidak terbaca
36. Tampilkan Dialog Edit Purchase dengan kondisi K5
37. Verifikasi field Purchase Date dan `Purchase Cost (per asset)` dapat diisi

### Aset Pending dengan field kosong dan custom field wajib
38. Tampilkan Dialog Edit Purchase dengan kondisi K6
39. Verifikasi field berlabel `Document No.` kosong dengan placeholder `Enter document no.`
40. Verifikasi field `Contract number` ditandai wajib
41. Ganti isi field Document No. dengan `INV-2026-0302`
42. Klik `[Save]`
43. Verifikasi pesan `Contract number must not be empty` tampil di bawah field `Contract number`

### Satu aset Complete dengan predikat Posted tidak terbaca dikunci
44. Tampilkan Dialog Edit Purchase dengan kondisi K7
45. Arahkan kursor ke field Purchase Date
46. Verifikasi field Purchase Date read-only dengan alasan `Asset has posted depreciation or journal entries. Use Value Change in the Accounting tab.`
47. Arahkan kursor ke field Purchase Cost
48. Verifikasi field Purchase Cost read-only dengan alasan `Asset has posted depreciation or journal entries. Use Value Change in the Accounting tab.`
49. Arahkan kursor ke bagian Additional costs
50. Verifikasi bagian Additional costs read-only dengan alasan `Asset has posted depreciation or journal entries. Use Value Change in the Accounting tab.`

### Satu aset Pending dengan predikat tidak terbaca dapat diisi lalu mengikuti kunci
51. Tampilkan Dialog Edit Purchase dengan kondisi K8
52. Verifikasi field Purchase Date, Purchase Cost, dan bagian Additional costs dapat diisi
53. Isi field Purchase Date dengan `15/03/26`
54. Isi field Purchase Cost dengan `9.500.000,00`
55. Klik `[Save]`
56. Verifikasi toast `Success, purchase data has been saved.` tampil
57. Tampilkan Dialog Edit Purchase dengan kondisi K9
58. Verifikasi field Purchase Date dan Purchase Cost read-only dengan alasan `Asset has posted depreciation or journal entries. Use Value Change in the Accounting tab.`

### Custom field tidak wajib dan batas Text
59. Tampilkan Dialog Edit Purchase dengan kondisi K10
60. Ganti isi field Document No. dengan `INV-2026-0302`
61. Klik `[Save]`
62. Verifikasi toast `Success, purchase data has been saved.` tampil
63. Verifikasi tidak ada pesan kesalahan di bawah custom field `Vendor note` yang dibiarkan kosong
64. Tampilkan Dialog Edit Purchase dengan kondisi K1
65. Ganti isi custom field `Vendor note` dengan `Catatan vendor BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB` (120 karakter)
66. Verifikasi tidak ada pesan batas karakter di bawah custom field `Vendor note`
67. Ganti isi custom field `Vendor note` dengan `Catatan vendor BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB` (121 karakter)
68. Verifikasi pesan batas karakter tampil di bawah custom field `Vendor note`

### Document No. sama dengan aset lain dan nilai setelah trim
69. Tampilkan Dialog Edit Purchase dengan kondisi K10
70. Ganti isi field Document No. dengan `INV-2026-0105`
71. Klik `[Save]`
72. Verifikasi toast `Success, purchase data has been saved.` tampil
73. Verifikasi tidak ada pesan kesalahan di bawah field Document No.
74. Tampilkan Dialog Edit Purchase dengan kondisi K10
75. Ganti isi field Document No. dengan `INV-2026-AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA` (120 karakter) yang diapit satu spasi di awal dan satu spasi di akhir
76. Verifikasi pesan `Max. 120 characters` tidak tampil di bawah field Document No.
77. Klik `[Save]`
78. Verifikasi toast `Success, purchase data has been saved.` tampil
79. Verifikasi permintaan simpan memuat Document No. 120 karakter tersebut tanpa spasi di awal dan di akhir
