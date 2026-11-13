---
id: TC-FA-FAREG-UI-025-form-submit-aset-belum-lengkap
title: "Form Register Asset: Submit dengan aset belum memenuhi Tingkat 2"
layer: ui-client
priority: Medium
caseType: Negative
status: ready-for-automation
sourceRules: ["FAREG-LOGIC-01i", "FLD-REG-08", "S-REG-22", "V-REG-02", "V-REG-03", "§4.1#r6", "§4.2.3#b1", "§9.9#r2", "§9.9#r3", "§9.9#r4", "§9.9#r8", "§9.9#r11"]
smoke: []
dependsOn: []
trace:
  "FAREG-LOGIC-01i": [4, 5, 9, 17, 34]
  "FLD-REG-08": [9, 10, 13, 20, 39, 40, 41]
  "S-REG-22": [4, 17, 34]
  "V-REG-02": [4, 9, 10, 17, 20, 24, 25, 26, 39, 34]
  "V-REG-03": 11
  "§4.1#r6": [4, 17, 34]
  "§4.2.3#b1": [4, 5, 6, 7, 9, 18, 32, 35, 36, 37]
  "§9.9#r2": 24
  "§9.9#r3": 25
  "§9.9#r4": 26
  "§9.9#r8": 11
  "§9.9#r11": [9, 10, 13, 20, 39]
anchor: [31]
coverage:
  web: automated
---

# Form Register Asset: Submit dengan aset belum memenuhi Tingkat 2

## Prerequisites
- Aktor: Total Control.
- Layar awal: Assets > Registration > Draft
- Komponen: Halaman `Register Asset`
- Data:
  - DU-025-1: Item `Laptop Dell Latitude 5440` dengan Quantity `3`; aset `Laptop Dell Latitude 5440 - 1`, `Laptop Dell Latitude 5440 - 2`, dan `Laptop Dell Latitude 5440 - 3`; Asset Name, Brand, Model, dan Group terisi.
  - DU-025-2: Item `Printer Epson L3250` dengan Quantity `1`; aset `Printer Epson L3250 - 1`; Asset Name, Brand, Model, dan Group terisi.
  - DU-025-3: master Custom field wajib `Kapasitas RAM` (Scope Specific Asset Name `Laptop Dell Latitude 5440`) dan `Serial Number` (Value Type Specific, Scope Specific Asset Name `Laptop Dell Latitude 5440`).
  - DU-025-4: master Custom field wajib `Jenis Tinta` (tipe dropdown, Scope Specific Asset Name `Printer Epson L3250`).
  - DU-025-5: `Kapasitas RAM` dan `Serial Number` pada tiga aset laptop belum diisi; pesan `Kapasitas RAM must not be empty` dan `Serial Number must not be empty`.
  - DU-025-6: `Jenis Tinta` belum dipilih, field menampilkan `Select Jenis Tinta`; pesan `Jenis Tinta must not be empty`.
  - DU-025-7: aset `Laptop Dell Latitude 5440 - 1` ber-Condition `Damaged` tanpa Damage note; pesan `Damage note must not be empty`.
  - DU-025-8: tiga aset belum lengkap; pesan Alert `Please complete the data for 3 assets to continue.`
  - DU-025-9: satu aset belum lengkap; pesan Alert `Please complete the data for 1 asset to continue.`
  - DU-025-10: baris Item baru dengan Asset Name, Brand, dan Model belum dipilih, Quantity `1`.
  - DU-025-11: Item `Kursi Kerja Ergonomis` dengan Quantity `1`; aset `Kursi Kerja Ergonomis - 1`; Asset Name, Brand, Model, dan Group terisi; `Nomor Inventaris` terisi `INV-0001` dan `Catatan Garansi` kosong.
  - DU-025-12: master Custom field Scope General `Nomor Inventaris` (wajib) dan `Catatan Garansi` (tidak wajib).
  - DU-025-13: aset `Printer Epson L3250 - 1` dengan `Nomor Inventaris` dan `Catatan Garansi` belum diisi; pesan `Nomor Inventaris must not be empty`.
- Kondisi:
  - K1: form `Edit` draft tersimpan dengan Item DU-025-1; master Custom field DU-025-3; Custom field DU-025-5; Condition DU-025-7; tiga aset belum lengkap (DU-025-8).
  - K2: form `Edit` draft tersimpan dengan Item DU-025-2; master Custom field DU-025-4; Custom field DU-025-6; satu aset belum lengkap (DU-025-9).
  - K3: form `Edit` draft tersimpan dengan baris Item DU-025-10.
  - K4: form `Edit` draft tersimpan dengan Item DU-025-11 dan DU-025-2, keduanya terbuka; master Custom field DU-025-3 dan DU-025-12; Custom field DU-025-13 pada aset `Printer Epson L3250 - 1`; satu aset belum lengkap.

## Test Steps
### Submit ditolak pada tiga aset: Alert jumlah banyak, Custom field wajib, dan Damage note
1. Tampilkan Halaman `Register Asset` dengan kondisi K1
2. Klik tab `Asset`
3. Klik `[Submit]`
4. Verifikasi Alert Danger `Please complete the data for 3 assets to continue.` tampil di atas footer `[Submit]`
5. Verifikasi dialog konfirmasi Submit tidak tampil
6. Verifikasi Item `Laptop Dell Latitude 5440` terbuka otomatis
7. Verifikasi halaman menggulir ke aset pertama yang bermasalah, yaitu baris `Laptop Dell Latitude 5440 - 1`
8. Klik kolom `Name` pada `Laptop Dell Latitude 5440 - 1`
9. Verifikasi field `Kapasitas RAM` ditandai Danger dengan pesan `Kapasitas RAM must not be empty` di bawahnya
10. Verifikasi field `Serial Number` ditandai Danger dengan pesan `Serial Number must not be empty` di bawahnya
11. Verifikasi `Damage note` ditandai Danger dengan pesan `Damage note must not be empty` di bawahnya
12. Klik kolom `Name` pada `Laptop Dell Latitude 5440 - 2`
13. Verifikasi field `Kapasitas RAM` pada `Laptop Dell Latitude 5440 - 2` ditandai Danger dengan pesan `Kapasitas RAM must not be empty`

### Submit ditolak pada satu aset: Alert jumlah satu dan pilihan Custom field wajib
14. Tampilkan Halaman `Register Asset` dengan kondisi K2
15. Klik tab `Asset`
16. Klik `[Submit]`
17. Verifikasi Alert Danger `Please complete the data for 1 asset to continue.` tampil di atas footer `[Submit]`
18. Verifikasi Item `Printer Epson L3250` terbuka otomatis
19. Klik kolom `Name` pada `Printer Epson L3250 - 1`
20. Verifikasi field `Jenis Tinta` masih menampilkan `Select Jenis Tinta` dan ditandai Danger dengan pesan `Jenis Tinta must not be empty` di bawahnya

### Submit ditolak pada baris Item tanpa Asset Name, Brand, dan Model
21. Tampilkan Halaman `Register Asset` dengan kondisi K3
22. Klik tab `Asset`
23. Klik `[Submit]`
24. Verifikasi pesan `Asset Name must not be empty` tampil di bawah sel `Asset Name` baris Item baru
25. Verifikasi pesan `Brand must not be empty` tampil di bawah sel `Brand` baris Item baru
26. Verifikasi pesan `Model must not be empty` tampil di bawah sel `Model` baris Item baru

### Custom field General wajib, opsional kosong, Specific lain tidak dituntut, dan hanya Item bermasalah terbuka otomatis
27. Tampilkan Halaman `Register Asset` dengan kondisi K4
28. Klik tab `Asset`
29. Tekan `Enter` pada judul Item `Kursi Kerja Ergonomis`
30. Tekan `Enter` pada judul Item `Printer Epson L3250`
31. Verifikasi judul Item `Kursi Kerja Ergonomis` dan `Printer Epson L3250` tampil
32. Verifikasi baris `Kursi Kerja Ergonomis - 1` dan `Printer Epson L3250 - 1` tidak tampil karena Accordion dilipat
33. Klik `[Submit]`
34. Verifikasi Alert Danger `Please complete the data for 1 asset to continue.` tampil di atas footer `[Submit]`
35. Verifikasi Item `Printer Epson L3250` terbuka otomatis dan baris `Printer Epson L3250 - 1` tampil
36. Verifikasi Item `Kursi Kerja Ergonomis` tetap dilipat dan baris `Kursi Kerja Ergonomis - 1` tidak tampil
37. Verifikasi halaman menggulir ke aset yang bermasalah, yaitu baris `Printer Epson L3250 - 1`
38. Klik kolom `Name` pada `Printer Epson L3250 - 1`
39. Verifikasi field `Nomor Inventaris` ditandai Danger dengan pesan `Nomor Inventaris must not be empty` di bawahnya
40. Verifikasi field `Catatan Garansi` yang kosong tidak ditandai Danger dan tidak memiliki pesan error
41. Verifikasi tidak ada field `Kapasitas RAM` pada panel `Printer Epson L3250 - 1`
