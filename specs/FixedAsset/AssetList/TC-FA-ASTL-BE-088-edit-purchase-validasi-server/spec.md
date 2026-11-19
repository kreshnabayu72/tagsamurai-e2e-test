---
id: TC-FA-ASTL-BE-088-edit-purchase-validasi-server
title: "Validasi server Edit Purchase"
layer: be-e2e
priority: High
caseType: Negative
status: ready-for-automation
owner: BE
sourceRules: [ASTL-LOGIC-07b, ASTL-LOGIC-11a, ASTL-LOGIC-21g, ASTL-LOGIC-21h, ASTL-LOGIC-21j, ASTL-LOGIC-21a, ASTL-LOGIC-21c, ASTL-LOGIC-21i, ASTL-LOGIC-21k, V-06, V-07, V-11, V-09, V-10, V-12, V-13, V-14, V-15, V-16, V-17, EC-30, EC-37, EC-38, F-ASTL-18.k1, F-ASTL-18.k3, F-ASTL-18.k4, F-ASTL-18.k5, "§9.2#p8", "§9.6#r4", "EB-FRM-4@edit-purchase", "EB-FRM-5@edit-purchase"]
smoke: []
dependsOn: []
trace:
  ASTL-LOGIC-07b: [4, 115]
  ASTL-LOGIC-11a: 20
  ASTL-LOGIC-21g: 17
  ASTL-LOGIC-21h: 23
  ASTL-LOGIC-21j: 37
  ASTL-LOGIC-21a: [8, 10]
  ASTL-LOGIC-21c: [12, 14, 15, 78, 80]
  ASTL-LOGIC-21i: [31, 33, 35]
  ASTL-LOGIC-21k: [39, 40, 42, 44, 52, 54]
  V-06: [25, 27, 29, 82, 84]
  V-07: [68, 70, 72, 98, 107, 109, 111]
  V-11: [17, 18]
  V-09: [8, 10, 76]
  V-10: [12, 14, 15, 78, 80]
  V-12: [31, 33, 35]
  V-13: [56, 58, 60, 62, 64, 66, 86, 88, 90, 92, 94, 96, 100, 102, 104]
  V-14: 48
  V-15: 50
  V-16: [39, 40, 42, 44, 46]
  V-17: 52
  EC-30: [68, 70, 72, 98, 107, 109, 111, 113]
  EC-37: [17, 18, 20]
  EC-38: [8, 12]
  F-ASTL-18.k1: [68, 70, 72, 98, 107, 109, 111, 113]
  F-ASTL-18.k3: [8, 12, 17]
  F-ASTL-18.k4: 37
  F-ASTL-18.k5: [3, 4]
  "§9.2#p8": [3, 6, 21, 37, 68, 74]
  "§9.6#r4": [3, 6, 23, 37, 39, 68, 114]
  "EB-FRM-4@edit-purchase": [56, 58, 60, 62, 64, 66, 86, 88, 90, 92, 94, 96]
  "EB-FRM-5@edit-purchase": [29, 52]
anchor: []
---

# Validasi server Edit Purchase

## Prerequisites
- Aktor: Total Control (Hendra).
- Data:
  - DU-088-1: User, total Control seluruh client: Name `Hendra Saputra {runId}`, Role `Total Control`, Cakupan `Seluruh client`.
  - DU-088-2: Asset, aset dengan Purchase lengkap untuk Edit No-Op dan batas tanggal: Name `Laptop Pro 16 - N1 {runId}`, Lifecycle `Active`, Group `Kantor Pusat {runId}`, Purchase Date `T0 - 30 hari`, Purchase Cost `18500000.00`, Status Purchase `Complete`.
  - DU-088-3: Asset, aset dengan data Purchase belum diisi: Name `Printer Laser - N2 {runId}`, Lifecycle `Active`, Group `Kantor Pusat {runId}`, Status Purchase `Pending`.
  - DU-088-4: Asset, aset dengan 10 garansi: Name `Server Rack - W1 {runId}`, Lifecycle `Active`, Group `Kantor Pusat {runId}`, Warranty 1 `Garansi 1 {runId} berakhir T0 + 365 hari`, Warranty 2 `Garansi 2 {runId} berakhir T0 + 365 hari`, Warranty 3 `Garansi 3 {runId} berakhir T0 + 365 hari`, Warranty 4 `Garansi 4 {runId} berakhir T0 + 365 hari`, Warranty 5 `Garansi 5 {runId} berakhir T0 + 365 hari`, Warranty 6 `Garansi 6 {runId} berakhir T0 + 365 hari`, Warranty 7 `Garansi 7 {runId} berakhir T0 + 365 hari`, Warranty 8 `Garansi 8 {runId} berakhir T0 + 365 hari`, Warranty 9 `Garansi 9 {runId} berakhir T0 + 365 hari`, Warranty 10 `Garansi 10 {runId} berakhir T0 + 365 hari`, Purchase Date `T0 - 30 hari`.
  - DU-088-5: Asset, aset dengan 2 garansi: Name `Server Rack - W2 {runId}`, Lifecycle `Active`, Group `Kantor Pusat {runId}`, Warranty 1 `Garansi 1 {runId} berakhir T0 + 365 hari`, Warranty 2 `Garansi 2 {runId} berakhir T0 + 365 hari`, Purchase Date `T0 - 30 hari`.
  - DU-088-6: Asset, aset dengan 9 garansi: Name `Server Rack - W3 {runId}`, Lifecycle `Active`, Group `Kantor Pusat {runId}`, Warranty 1 `Garansi 1 {runId} berakhir T0 + 365 hari`, Warranty 2 `Garansi 2 {runId} berakhir T0 + 365 hari`, Warranty 3 `Garansi 3 {runId} berakhir T0 + 365 hari`, Warranty 4 `Garansi 4 {runId} berakhir T0 + 365 hari`, Warranty 5 `Garansi 5 {runId} berakhir T0 + 365 hari`, Warranty 6 `Garansi 6 {runId} berakhir T0 + 365 hari`, Warranty 7 `Garansi 7 {runId} berakhir T0 + 365 hari`, Warranty 8 `Garansi 8 {runId} berakhir T0 + 365 hari`, Warranty 9 `Garansi 9 {runId} berakhir T0 + 365 hari`, Purchase Date `T0 - 30 hari`.
  - DU-088-7: Asset, aset dengan garansi berakhir sebelum Purchase Date baru: Name `Monitor Dell - G1 {runId}`, Lifecycle `Active`, Group `Kantor Pusat {runId}`, Purchase Date `T0 - 30 hari`, Warranty 1 `Garansi Pabrik {runId} berakhir T0 - 5 hari`.
  - DU-088-8: Asset, aset dengan garansi berlaku: Name `Monitor Dell - G2 {runId}`, Lifecycle `Active`, Group `Kantor Pusat {runId}`, Purchase Date `T0 - 30 hari`, Warranty 1 `Garansi Pabrik {runId} berakhir T0 + 90 hari`.
  - DU-088-9: Asset, aset untuk Reference Price dan batas panjang: Name `Kamera CCTV - R1 {runId}`, Lifecycle `Active`, Group `Kantor Pusat {runId}`, Purchase Date `T0 - 30 hari`, Purchase Cost `5000000.00`.
  - DU-088-10: Asset, aset dengan satu Additional cost: Name `Genset Diesel - C1 {runId}`, Lifecycle `Active`, Group `Kantor Pusat {runId}`, Purchase Cost `3000000.00`, Additional cost 1 `Biaya Instalasi {runId} jumlah 500000.00`.
  - DU-088-11: Asset, aset dengan 10 Additional costs: Name `Genset Diesel - C2 {runId}`, Lifecycle `Active`, Group `Kantor Pusat {runId}`, Purchase Cost `3000000.00`, Additional cost 1 `Biaya 1 {runId} jumlah 100.00`, Additional cost 2 `Biaya 2 {runId} jumlah 100.00`, Additional cost 3 `Biaya 3 {runId} jumlah 100.00`, Additional cost 4 `Biaya 4 {runId} jumlah 100.00`, Additional cost 5 `Biaya 5 {runId} jumlah 100.00`, Additional cost 6 `Biaya 6 {runId} jumlah 100.00`, Additional cost 7 `Biaya 7 {runId} jumlah 100.00`, Additional cost 8 `Biaya 8 {runId} jumlah 100.00`, Additional cost 9 `Biaya 9 {runId} jumlah 100.00`, Additional cost 10 `Biaya 10 {runId} jumlah 100.00`.
  - DU-088-12: Asset, aset dengan Purchase Cost mendekati batas 15 digit: Name `Genset Diesel - C3 {runId}`, Lifecycle `Active`, Group `Kantor Pusat {runId}`, Purchase Cost `9999999999000.00`, Additional cost 1 `Biaya Kirim {runId} jumlah 500.00`.
  - DU-088-13: Asset, aset berjejak Posted: Name `Pompa Air - P1 {runId}`, Lifecycle `Active`, Group `Kantor Pusat {runId}`, Purchase Date `T0 - 60 hari`, Purchase Cost `18500000.00`, Jejak finansial `Penyusutan Posted`.
  - DU-088-14: Asset, aset Disposed dengan Purchase lengkap: Name `Forklift - X1 {runId}`, Lifecycle `Disposed`, Group `Kantor Pusat {runId}`, Purchase Cost `8000000.00`.
  - DU-088-23: Asset, aset Purchase Complete yang predikat berjejak Posted-nya tidak terbaca: Name `Pompa Air - U1 {runId}`, Lifecycle `Active`, Group `Kantor Pusat {runId}`, Purchase Date `T0 - 45 hari`, Purchase Cost `12000000.00`, Status Purchase `Complete`, Predikat berjejak Posted `tidak terbaca`.
  - DU-088-24: Asset, aset Purchase Pending yang predikat berjejak Posted-nya tidak terbaca: Name `Pompa Air - U2 {runId}`, Lifecycle `Active`, Group `Kantor Pusat {runId}`, Status Purchase `Pending`, Predikat berjejak Posted `tidak terbaca`.
  - DU-088-21: Input, nilai baru untuk validasi tambahan: Warranty name 100 karakter `Garansi Perpanjangan Layanan Purna Jual Resmi Pabrikan Perangkat Keras Server Rack Kantor Pusat XXXX`, Warranty name 101 karakter `Garansi Perpanjangan Layanan Purna Jual Resmi Pabrikan Perangkat Keras Server Rack Kantor Pusat XXXXZ`, Purchase Cost 15 digit `9999999999999.99`, Purchase Cost 16 digit `10000000000000.00`, Reference Price jumlah `9999999999999.99` dan `10000000000000.00`, Warranty name kembar `Garansi Kembar {runId}` dan `GARANSI KEMBAR {runId}`, Warranty name sama dengan tersimpan `GARANSI 1 {runId}`.

## Test Steps

### Simpan tanpa perubahan adalah Edit No-Op
1. Catat versi data aset `Laptop Pro 16 - N1 {runId}` dan jumlah entri Changelog-nya
2. Hendra menyimpan Edit Purchase pada `Laptop Pro 16 - N1 {runId}` dengan Purchase Date `T0 - 30 hari` dan Purchase Cost `18500000.00`, sama dengan nilai tersimpan
3. Verifikasi permintaan dijawab sebagai Edit No-Op dan jumlah entri Changelog `Laptop Pro 16 - N1 {runId}` tidak bertambah
4. Verifikasi versi data aset `Laptop Pro 16 - N1 {runId}` tidak naik

### Status Purchase dihitung ulang server
5. Hendra menyimpan Edit Purchase pada `Printer Laser - N2 {runId}` dengan Purchase Date `T0 - 10 hari` dan Purchase Cost `7500000.00`
6. Verifikasi status Purchase `Printer Laser - N2 {runId}` berubah dari `Pending` menjadi `Complete` dan Changelog-nya memuat satu entri per field yang berubah

### Purchase Date tidak boleh setelah hari ini
7. Hendra menyimpan Edit Purchase pada `Laptop Pro 16 - N1 {runId}` dengan Purchase Date `T0 + 1 hari`
8. Verifikasi permintaan ditolak karena Purchase Date setelah hari ini, dan Purchase Date `Laptop Pro 16 - N1 {runId}` tetap `T0 - 30 hari`
9. Hendra menyimpan Edit Purchase pada `Laptop Pro 16 - N1 {runId}` dengan Purchase Date `T0`
10. Verifikasi permintaan diterima karena Purchase Date tepat hari ini, dan Purchase Date `Laptop Pro 16 - N1 {runId}` menjadi `T0`

### Warranty until tidak boleh sebelum Purchase Date
11. Hendra menyimpan Edit Purchase pada `Monitor Dell - G2 {runId}` dengan Warranty `Garansi Pabrik {runId}` berakhir `T0 - 40 hari`
12. Verifikasi permintaan ditolak karena Warranty until sebelum Purchase Date `T0 - 30 hari`, dan garansi `Monitor Dell - G2 {runId}` tetap berakhir `T0 + 90 hari`
13. Hendra menjalankan Bulk Edit Purchase pada `Monitor Dell - G1 {runId}` dan `Monitor Dell - G2 {runId}` dengan Purchase Date baru `T0 - 2 hari`
14. Verifikasi seluruh Bulk ditolak karena garansi tersimpan `Monitor Dell - G1 {runId}` berakhir `T0 - 5 hari`, sebelum Purchase Date baru, dan alasan penolakan menyebut `Monitor Dell - G1 {runId}`
15. Verifikasi Purchase Date `Monitor Dell - G2 {runId}` tetap `T0 - 30 hari` sehingga tidak ada aset yang berubah

### Batas dan validasi garansi
16. Hendra menjalankan Bulk Edit Purchase dengan menambah Warranty `Garansi Servis {runId}` berakhir `T0 + 200 hari` pada `Server Rack - W1 {runId}` dan `Server Rack - W2 {runId}`
17. Verifikasi seluruh Bulk ditolak karena `Server Rack - W1 {runId}` sudah punya 10 garansi dan akan melampaui batas, dengan alasan menyebut `Server Rack - W1 {runId}`
18. Verifikasi `Server Rack - W2 {runId}` tetap punya 2 garansi sehingga tidak ada aset yang berubah
19. Hendra menjalankan Bulk Edit Purchase dengan menambah Warranty `Garansi Servis {runId}` berakhir `T0 + 200 hari` pada `Server Rack - W2 {runId}` dan `Server Rack - W3 {runId}`
20. Verifikasi Bulk diterima karena `Server Rack - W3 {runId}` dari 9 garansi menjadi tepat 10 garansi, dan `Server Rack - W2 {runId}` menjadi 3 garansi
21. Verifikasi Changelog memuat satu entri per field per aset untuk `Server Rack - W2 {runId}` dan `Server Rack - W3 {runId}`
22. Hendra menjalankan Bulk Edit Purchase pada `Server Rack - W1 {runId}` dengan Warranty bernama `Garansi 1 {runId}` berakhir `T0 + 400 hari`
23. Verifikasi Bulk diterima karena baris bernama sama hanya memperbarui, sehingga `Server Rack - W1 {runId}` tetap punya 10 garansi dengan `Garansi 1 {runId}` berakhir `T0 + 400 hari`
24. Hendra menyimpan Edit Purchase pada `Server Rack - W2 {runId}` dengan Warranty name kosong
25. Verifikasi permintaan ditolak karena Warranty name kosong, dan garansi `Server Rack - W2 {runId}` tidak berubah
26. Hendra menyimpan Edit Purchase pada `Server Rack - W2 {runId}` dengan Warranty name `Garansi Servis {runId}` dan Warranty until kosong
27. Verifikasi permintaan ditolak karena Warranty until kosong, dan garansi `Server Rack - W2 {runId}` tidak berubah
28. Hendra menyimpan Edit Purchase pada `Server Rack - W2 {runId}` dengan dua Warranty bernama `Garansi Baru {runId}`
29. Verifikasi permintaan ditolak karena nama Warranty harus unik per aset, dan garansi `Server Rack - W2 {runId}` tidak berubah

### Reference Price diisi lengkap atau dikosongkan bersama
30. Hendra menyimpan Edit Purchase pada `Kamera CCTV - R1 {runId}` dengan Reference Price hanya Currency `IDR`
31. Verifikasi permintaan ditolak karena Reference Price terisi sebagian, dan Reference Price `Kamera CCTV - R1 {runId}` tidak berubah
32. Hendra menyimpan Edit Purchase pada `Kamera CCTV - R1 {runId}` dengan Reference Price hanya jumlah `1500000.00`
33. Verifikasi permintaan ditolak karena Reference Price terisi sebagian, dan Reference Price `Kamera CCTV - R1 {runId}` tidak berubah
34. Hendra menyimpan Edit Purchase pada `Kamera CCTV - R1 {runId}` dengan Reference Price Currency `IDR` dan jumlah `1500000.00`
35. Verifikasi permintaan diterima dan Reference Price `Kamera CCTV - R1 {runId}` menjadi `IDR` `1500000.00`

### Bulk Edit Purchase dengan Additional costs ditolak
36. Hendra menjalankan Bulk Edit Purchase pada `Genset Diesel - C1 {runId}` dan `Genset Diesel - C3 {runId}` dengan Additional cost `Biaya Uji Bulk {runId}` jumlah `100.00`
37. Verifikasi seluruh Bulk ditolak karena memuat Additional costs, dan tidak ada aset yang berubah

### Total Purchase Cost dan Additional costs pada Bulk dibatasi 15 digit
38. Hendra menjalankan Bulk Edit Purchase pada `Genset Diesel - C3 {runId}` dan `Laptop Pro 16 - N1 {runId}` dengan Purchase Cost `9999999999600.00`
39. Verifikasi seluruh Bulk ditolak karena Purchase Cost ditambah Additional cost tersimpan `500.00` pada `Genset Diesel - C3 {runId}` melebihi 15 digit termasuk 2 digit desimal
40. Verifikasi Purchase Cost `Laptop Pro 16 - N1 {runId}` tetap `18500000.00` sehingga tidak ada aset yang berubah

### Batas panjang dan jumlah Additional costs
41. Hendra menyimpan Edit Purchase pada `Genset Diesel - C3 {runId}` dengan Additional cost `Biaya Pasang {runId}` jumlah `500.00`
42. Verifikasi permintaan ditolak karena total `10000000000000.00` melebihi 15 digit termasuk 2 digit desimal, dan Additional costs `Genset Diesel - C3 {runId}` tidak berubah
43. Hendra menyimpan Edit Purchase pada `Genset Diesel - C3 {runId}` dengan Additional cost `Biaya Pasang {runId}` jumlah `499.99`
44. Verifikasi permintaan diterima karena total tepat `9999999999999.99` dan Additional costs `Genset Diesel - C3 {runId}` menjadi dua baris
45. Hendra menyimpan Edit Purchase pada `Genset Diesel - C1 {runId}` dengan Additional cost jumlah `10000000000000.00`
46. Verifikasi permintaan ditolak karena jumlah Additional cost melebihi 15 digit termasuk 2 digit desimal
47. Hendra menyimpan Edit Purchase pada `Genset Diesel - C1 {runId}` dengan Additional cost bernama kosong dan jumlah `100.00`
48. Verifikasi permintaan ditolak karena nama Additional cost kosong
49. Hendra menyimpan Edit Purchase pada `Genset Diesel - C1 {runId}` dengan Additional cost `Biaya Lain {runId}` tanpa jumlah
50. Verifikasi permintaan ditolak karena jumlah Additional cost kosong
51. Hendra menyimpan Edit Purchase pada `Genset Diesel - C1 {runId}` dengan Additional cost `BIAYA INSTALASI {runId}` jumlah `100.00`
52. Verifikasi permintaan ditolak karena nama sama dengan `Biaya Instalasi {runId}` tanpa membedakan huruf besar-kecil, dan Additional costs `Genset Diesel - C1 {runId}` tidak berubah
53. Hendra menyimpan Edit Purchase pada `Genset Diesel - C2 {runId}` dengan satu Additional cost tambahan `Biaya 11 {runId}` jumlah `100.00` sehingga menjadi 11 baris
54. Verifikasi permintaan ditolak karena batas 10 baris Additional costs per aset, dan `Genset Diesel - C2 {runId}` tetap punya 10 baris
55. Hendra menyimpan Edit Purchase pada `Genset Diesel - C1 {runId}` dengan Additional cost `Biaya Instalasi Jaringan Kantor Pusat Biaya Instalasi Jaringan Kantor Pusat Biaya Instalasi Jaringan Kantor Pusat BiayaX` jumlah `100.00`
56. Verifikasi permintaan diterima karena nama Additional cost tepat di batas `Biaya Instalasi Jaringan Kantor Pusat Biaya Instalasi Jaringan Kantor Pusat Biaya Instalasi Jaringan Kantor Pusat BiayaX` (120 karakter)
57. Hendra menyimpan Edit Purchase pada `Genset Diesel - C1 {runId}` dengan Additional cost `Biaya Instalasi Jaringan Kantor Pusat Biaya Instalasi Jaringan Kantor Pusat Biaya Instalasi Jaringan Kantor Pusat BiayaXZ` jumlah `100.00`
58. Verifikasi permintaan ditolak karena nama Additional cost `Biaya Instalasi Jaringan Kantor Pusat Biaya Instalasi Jaringan Kantor Pusat Biaya Instalasi Jaringan Kantor Pusat BiayaXZ` (121 karakter) melebihi batas 120 karakter
59. Hendra menyimpan Edit Purchase pada `Kamera CCTV - R1 {runId}` dengan Provider `PT Mitra Sarana Teknologi Informasi PT Mitra Sarana Teknologi Informasi PT Mitra Sarana Teknologi Informasi PT Mitra Sar`
60. Verifikasi permintaan diterima karena Provider tepat di batas `PT Mitra Sarana Teknologi Informasi PT Mitra Sarana Teknologi Informasi PT Mitra Sarana Teknologi Informasi PT Mitra Sar` (120 karakter)
61. Hendra menyimpan Edit Purchase pada `Kamera CCTV - R1 {runId}` dengan Provider `PT Mitra Sarana Teknologi Informasi PT Mitra Sarana Teknologi Informasi PT Mitra Sarana Teknologi Informasi PT Mitra SarZ`
62. Verifikasi permintaan ditolak karena Provider `PT Mitra Sarana Teknologi Informasi PT Mitra Sarana Teknologi Informasi PT Mitra Sarana Teknologi Informasi PT Mitra SarZ` (121 karakter) melebihi batas 120 karakter
63. Hendra menyimpan Edit Purchase pada `Kamera CCTV - R1 {runId}` dengan Document No. `DOC-2025-INSTALASI-DOC-2025-INSTALASI-DOC-2025-INSTALASI-DOC-2025-INSTALASI-DOC-2025-INSTALASI-DOC-2025-INSTALASI-DOC-20`
64. Verifikasi permintaan diterima karena Document No. tepat di batas `DOC-2025-INSTALASI-DOC-2025-INSTALASI-DOC-2025-INSTALASI-DOC-2025-INSTALASI-DOC-2025-INSTALASI-DOC-2025-INSTALASI-DOC-20` (120 karakter)
65. Hendra menyimpan Edit Purchase pada `Kamera CCTV - R1 {runId}` dengan Document No. `DOC-2025-INSTALASI-DOC-2025-INSTALASI-DOC-2025-INSTALASI-DOC-2025-INSTALASI-DOC-2025-INSTALASI-DOC-2025-INSTALASI-DOC-20Z`
66. Verifikasi permintaan ditolak karena Document No. `DOC-2025-INSTALASI-DOC-2025-INSTALASI-DOC-2025-INSTALASI-DOC-2025-INSTALASI-DOC-2025-INSTALASI-DOC-2025-INSTALASI-DOC-20Z` (121 karakter) melebihi batas 120 karakter

### Aset berjejak Posted menolak perubahan Purchase
67. Hendra menyimpan Edit Purchase pada `Pompa Air - P1 {runId}` dengan Purchase Cost `20000000.00`
68. Verifikasi permintaan ditolak karena `Pompa Air - P1 {runId}` berjejak Posted, dan Purchase Cost tetap `18500000.00`
69. Hendra menyimpan Edit Purchase pada `Pompa Air - P1 {runId}` dengan Purchase Date `T0 - 20 hari`
70. Verifikasi permintaan ditolak karena `Pompa Air - P1 {runId}` berjejak Posted, dan Purchase Date tetap `T0 - 60 hari`
71. Hendra menyimpan Edit Purchase pada `Pompa Air - P1 {runId}` dengan Additional cost `Biaya Pasang {runId}` jumlah `100.00`
72. Verifikasi permintaan ditolak karena `Pompa Air - P1 {runId}` berjejak Posted, dan Additional costs tidak berubah

### Edit Purchase hanya untuk aset Active
73. Hendra menyimpan Edit Purchase pada aset Disposed `Forklift - X1 {runId}` dengan Purchase Cost `9000000.00`
74. Verifikasi permintaan ditolak karena Lifecycle bukan `Active`, dan Purchase Cost tetap `8000000.00`

### Bulk Purchase Date setelah hari ini ditolak
75. Hendra menjalankan Bulk Edit Purchase pada `Laptop Pro 16 - N1 {runId}` dan `Kamera CCTV - R1 {runId}` dengan Purchase Date `T0 + 1 hari`
76. Verifikasi seluruh Bulk ditolak karena Purchase Date setelah hari ini, Purchase Date `Laptop Pro 16 - N1 {runId}` tetap `T0`, dan Purchase Date `Kamera CCTV - R1 {runId}` tetap `T0 - 30 hari`

### Warranty until tersimpan terhadap Purchase Date baru pada satu aset dan Bulk
77. Hendra menyimpan Edit Purchase pada `Monitor Dell - G1 {runId}` dengan Purchase Date `T0 - 2 hari`
78. Verifikasi permintaan ditolak karena garansi tersimpan `Garansi Pabrik {runId}` berakhir `T0 - 5 hari`, sebelum Purchase Date baru, dan Purchase Date `Monitor Dell - G1 {runId}` tetap `T0 - 30 hari`
79. Hendra menjalankan Bulk Edit Purchase pada `Monitor Dell - G1 {runId}` dan `Monitor Dell - G2 {runId}` tanpa mengisi Purchase Date, dengan menambah Warranty `Garansi Baru Bulk {runId}` berakhir `T0 - 40 hari`
80. Verifikasi seluruh Bulk ditolak karena Warranty until baru sebelum Purchase Date tersimpan `T0 - 30 hari`, dan tidak ada aset yang berubah

### Nama Warranty unik tanpa membedakan huruf besar-kecil
81. Hendra menyimpan Edit Purchase pada `Server Rack - W2 {runId}` dengan dua Warranty bernama `Garansi Kembar {runId}` dan `GARANSI KEMBAR {runId}`
82. Verifikasi permintaan ditolak karena nama Warranty sama tanpa membedakan huruf besar-kecil, dan garansi `Server Rack - W2 {runId}` tidak berubah
83. Hendra menyimpan Edit Purchase pada `Server Rack - W2 {runId}` dengan Warranty baru bernama `GARANSI 1 {runId}`, sama dengan garansi tersimpan `Garansi 1 {runId}` selain huruf besar-kecil
84. Verifikasi permintaan ditolak karena nama sudah ada pada garansi tersimpan tanpa membedakan huruf besar-kecil, dan garansi `Server Rack - W2 {runId}` tidak berubah

### Batas Warranty name, Purchase Cost, dan Reference Price
85. Hendra menyimpan Edit Purchase pada `Server Rack - W2 {runId}` dengan Warranty name `Garansi Perpanjangan Layanan Purna Jual Resmi Pabrikan Perangkat Keras Server Rack Kantor Pusat XXXX` berakhir `T0 + 200 hari`
86. Verifikasi permintaan diterima karena Warranty name tepat di batas 100 karakter
87. Hendra menyimpan Edit Purchase pada `Server Rack - W2 {runId}` dengan Warranty name `Garansi Perpanjangan Layanan Purna Jual Resmi Pabrikan Perangkat Keras Server Rack Kantor Pusat XXXXZ` berakhir `T0 + 200 hari`
88. Verifikasi permintaan ditolak karena Warranty name 101 karakter melebihi batas 100 karakter
89. Hendra menyimpan Edit Purchase pada `Kamera CCTV - R1 {runId}` dengan Purchase Cost `9999999999999.99`
90. Verifikasi permintaan diterima karena Purchase Cost tepat 15 digit termasuk 2 digit desimal
91. Hendra menyimpan Edit Purchase pada `Kamera CCTV - R1 {runId}` dengan Purchase Cost `10000000000000.00`
92. Verifikasi permintaan ditolak karena Purchase Cost melebihi 15 digit termasuk 2 digit desimal, dan Purchase Cost `Kamera CCTV - R1 {runId}` tetap `9999999999999.99`
93. Hendra menyimpan Edit Purchase pada `Kamera CCTV - R1 {runId}` dengan Reference Price Currency `IDR` dan jumlah `9999999999999.99`
94. Verifikasi permintaan diterima karena jumlah Reference Price tepat 15 digit termasuk 2 digit desimal
95. Hendra menyimpan Edit Purchase pada `Kamera CCTV - R1 {runId}` dengan Reference Price Currency `IDR` dan jumlah `10000000000000.00`
96. Verifikasi permintaan ditolak karena jumlah Reference Price melebihi 15 digit termasuk 2 digit desimal, dan jumlah Reference Price `Kamera CCTV - R1 {runId}` tetap `9999999999999.99`

### Bulk Edit Purchase atas seleksi berjejak Posted ditolak
97. Hendra menjalankan Bulk Edit Purchase pada `Pompa Air - P1 {runId}` dan `Kamera CCTV - R1 {runId}` dengan Purchase Date `T0 - 3 hari`
98. Verifikasi seluruh Bulk ditolak `422` karena `Pompa Air - P1 {runId}` berjejak Posted, Purchase Date `Pompa Air - P1 {runId}` tetap `T0 - 60 hari`, dan `Kamera CCTV - R1 {runId}` tidak berubah

### Server men-trim Provider, Document No., dan nama Additional cost
99. Hendra menyimpan Edit Purchase pada `Kamera CCTV - R1 {runId}` dengan Provider `CV Karya Nusantara Teknologi Solusi Terpadu CV Karya Nusantara Teknologi Solusi Terpadu CV Karya Nusantara Teknologi SoK` yang diapit satu spasi di awal dan satu spasi di akhir
100. Verifikasi permintaan diterima karena panjang dihitung setelah trim (120 karakter), dan Provider `Kamera CCTV - R1 {runId}` tersimpan tanpa spasi tepi sebagai `CV Karya Nusantara Teknologi Solusi Terpadu CV Karya Nusantara Teknologi Solusi Terpadu CV Karya Nusantara Teknologi SoK`
101. Hendra menyimpan Edit Purchase pada `Kamera CCTV - R1 {runId}` dengan Document No. `INV-2026-PEMBELIAN-INV-2026-PEMBELIAN-INV-2026-PEMBELIAN-INV-2026-PEMBELIAN-INV-2026-PEMBELIAN-INV-2026-PEMBELIAN-INV-27` yang diapit satu spasi di awal dan satu spasi di akhir
102. Verifikasi permintaan diterima karena panjang dihitung setelah trim (120 karakter), dan Document No. `Kamera CCTV - R1 {runId}` tersimpan tanpa spasi tepi sebagai `INV-2026-PEMBELIAN-INV-2026-PEMBELIAN-INV-2026-PEMBELIAN-INV-2026-PEMBELIAN-INV-2026-PEMBELIAN-INV-2026-PEMBELIAN-INV-27`
103. Hendra menyimpan Edit Purchase pada `Genset Diesel - C1 {runId}` dengan Additional cost bernama `Biaya Pemasangan Jaringan Kabel Kantor Cabang Biaya Pemasangan Jaringan Kabel Kantor Cabang Biaya Pemasangan Jaringan KB` yang diapit satu spasi di awal dan satu spasi di akhir, jumlah `100.00`
104. Verifikasi permintaan diterima karena panjang dihitung setelah trim (120 karakter), dan nama Additional cost tersimpan tanpa spasi tepi sebagai `Biaya Pemasangan Jaringan Kabel Kantor Cabang Biaya Pemasangan Jaringan Kabel Kantor Cabang Biaya Pemasangan Jaringan KB`

### Predikat berjejak Posted yang tidak terbaca pada permintaan langsung
105. Predikat berjejak Posted aset `Pompa Air - U1 {runId}` dan `Pompa Air - U2 {runId}` tidak terbaca
106. Hendra menyimpan Edit Purchase pada `Pompa Air - U1 {runId}` dengan Purchase Cost `13000000.00`
107. Verifikasi permintaan ditolak `422` karena aset Purchase `Complete` diperlakukan berjejak Posted saat predikat tidak terbaca, dan Purchase Cost tetap `12000000.00`
108. Hendra menyimpan Edit Purchase pada `Pompa Air - U1 {runId}` dengan Purchase Date `T0 - 20 hari`
109. Verifikasi permintaan ditolak `422` karena aset Purchase `Complete` diperlakukan berjejak Posted saat predikat tidak terbaca, dan Purchase Date tetap `T0 - 45 hari`
110. Hendra menyimpan Edit Purchase pada `Pompa Air - U1 {runId}` dengan Additional cost `Biaya Pasang {runId}` jumlah `100.00`
111. Verifikasi permintaan ditolak `422` karena aset Purchase `Complete` diperlakukan berjejak Posted saat predikat tidak terbaca, dan Additional costs tidak berubah
112. Hendra menyimpan Edit Purchase pada `Pompa Air - U2 {runId}` dengan Purchase Date `T0 - 10 hari`, Purchase Cost `4000000.00`, dan Additional cost `Biaya Pasang {runId}` jumlah `100.00`
113. Verifikasi permintaan diterima karena aset Purchase `Pending` tidak diperlakukan berjejak Posted walau predikat tidak terbaca, dan Purchase Date, Purchase Cost, serta Additional costs `Pompa Air - U2 {runId}` tersimpan sesuai

### Edit Purchase tercatat di Activity Log
114. Verifikasi Activity Log memuat entri aksi `Edit Purchase` atas `Printer Laser - N2 {runId}` dengan pelaku Hendra dari penyimpanan pada langkah 5
115. Verifikasi Activity Log tidak memuat entri baru untuk Edit No-Op pada `Laptop Pro 16 - N1 {runId}` dari langkah 2
