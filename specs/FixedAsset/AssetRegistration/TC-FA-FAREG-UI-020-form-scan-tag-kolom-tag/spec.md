---
id: TC-FA-FAREG-UI-020-form-scan-tag-kolom-tag
title: "Form Register Asset: tombol Scan, Badge TAG, dan pesan hasil scan"
layer: ui-client
priority: Medium
caseType: Negative
status: draft
sourceRules: ["FAREG-LOGIC-04c", "FAREG-LOGIC-04d", "FAREG-LOGIC-04e", "FAREG-LOGIC-04o", "FAREG-LOGIC-04q", "S-REG-15", "S-REG-18", "S-REG-28", "V-REG-05", "V-REG-06", "V-REG-07", "V-REG-08", "V-REG-09", "§4.1#r101", "§4.2.2#p1", "§9.4.2#r28", "§9.4.2#r30", "§9.4.2#r31", "§9.4.2#r32", "§9.4.2#r33", "§9.4.2#r34", "§9.4.2#r35", "§9.4.2#r36", "§9.4.2#r37", "§9.4.2#r38", "§9.4.2#r39", "§9.4.2#r40", "§9.4.2#r41", "§9.4.2#r57", "§9.6#r9", "§9.9#r12", "§9.10#p2"]
smoke: []
dependsOn: []
trace:
  "FAREG-LOGIC-04c": 14
  "FAREG-LOGIC-04d": 9
  "FAREG-LOGIC-04e": [85, 86]
  "FAREG-LOGIC-04o": [14, 23, 29, 34, 39, 44, 49, 54, 76, 81, 90]
  "FAREG-LOGIC-04q": [7, 98, 99, 100]
  "S-REG-15": [93, 94]
  "S-REG-18": [8, 14]
  "S-REG-28": [99, 100]
  "V-REG-05": 22
  "V-REG-06": [28, 33, 38, 43, 48, 53]
  "V-REG-07": [62, 66]
  "V-REG-08": 70
  "V-REG-09": 75
  "§4.1#r101": [3, 4, 5, 8, 16, 18, 103, 107]
  "§4.2.2#p1": [10, 15]
  "§9.4.2#r28": 28
  "§9.4.2#r30": 14
  "§9.4.2#r31": 85
  "§9.4.2#r32": [70, 71]
  "§9.4.2#r33": [22, 24]
  "§9.4.2#r34": 28
  "§9.4.2#r35": 33
  "§9.4.2#r36": [38, 43, 48]
  "§9.4.2#r37": 58
  "§9.4.2#r38": 53
  "§9.4.2#r39": [62, 66]
  "§9.4.2#r40": 75
  "§9.4.2#r41": 80
  "§9.4.2#r57": 95
  "§9.6#r9": 14
  "§9.9#r12": [22, 28, 75, 103]
  "§9.10#p2": 100
anchor: [6, 106]
coverage:
  web: automated
---

# Form Register Asset: tombol Scan, Badge TAG, dan pesan hasil scan

## Prerequisites
- Aktor: Total Control.
- Layar awal: Assets > Registration > Draft
- Komponen: Halaman `Register Asset`
- Data:
  - DU-020-1: Item `Laptop Dell Latitude 5440`, TAG Type `RFID`; aset `Laptop Dell Latitude 5440 - 1` dan `Laptop Dell Latitude 5440 - 2`, keduanya `Unverified`.
  - DU-020-2: Item `Kursi Kerja Ergonomis`, TAG Type `QR`; aset `Kursi Kerja Ergonomis - 1`, `Unverified`.
  - DU-020-3: Item `Printer Epson L3250`, TAG Type `RFID` dan `NFC`; aset `Printer Epson L3250 - 1`, kedua slot `Unverified`.
  - DU-020-4: Item `Forklift Toyota 8FD`, TAG Type `RFID` dan `GPS`; aset `Forklift Toyota 8FD - 1`, slot RFID `Unverified`.
  - DU-020-5: Item `Meja Lipat Aluminium`, TAG Type `Non-TAG`; aset `Meja Lipat Aluminium - 1`.
  - DU-020-6: Tag `RFID-000501`, tipe RFID, status `Available`.
  - DU-020-7: Tag `RFID-999999`, tidak ada di registri.
  - DU-020-8: Tag `RFID-000502`, tipe RFID, status `Paired` di aset lain; pesan scan `RFID-000502 is not available (Paired)`.
  - DU-020-9: Tag `RFID-000503`, tipe RFID, status `Reserved` oleh draft lain; pesan scan `RFID-000503 is not available (Reserved)`.
  - DU-020-10: Tag `RFID-000504`, tipe RFID, status `Retired`; pesan scan `RFID-000504 is not available (Retired)`.
  - DU-020-11: Tag `RFID-000505`, tipe RFID, status `Waiting for Approval`; pesan scan `RFID-000505 is not available (Waiting for Approval)`.
  - DU-020-12: Tag `RFID-000506`, tipe RFID, status `Damaged`; pesan scan `RFID-000506 is not available (Damaged)`.
  - DU-020-13: Tag `RFID-000507`, tipe RFID, status `To be Returned` dengan Return Group dalam scope Total Control.
  - DU-020-14: Tag `RFID-000508`, tipe RFID, status `To be Returned` dengan Return Group di luar scope; pesan scan `RFID-000508 is not available (To be Returned)`.
  - DU-020-15: Tag user `USR-000601`.
  - DU-020-16: Tag produk lain `SUP-000701` yang dipakai produk `Supply Asset`.
  - DU-020-17: Tag `RFID-000510`, tipe RFID, status `Available`, terpasang di aset `Laptop Dell Latitude 5440 - 1`.
  - DU-020-18: Tag `RFID-000511`, tipe RFID, status `Available`.
  - DU-020-19: Tag `RFID-000513`, tipe RFID, status `Available`.
- Kondisi:
  - K1: form `Edit` draft tersimpan dengan Item DU-020-1, DU-020-2, DU-020-3, dan DU-020-4; reader TAG terhubung; plan memperbolehkan tipe Tag RFID, QR, dan NFC; semua aset berbadge `Unverified`.
  - K2: sama dengan K1; pemindaian aset `Laptop Dell Latitude 5440 - 1` menghasilkan DU-020-6.
  - K3: sama dengan K1; pemindaian aset `Laptop Dell Latitude 5440 - 1` menghasilkan DU-020-7.
  - K4: sama dengan K1; pemindaian aset `Laptop Dell Latitude 5440 - 1` menghasilkan DU-020-8.
  - K5: sama dengan K1; pemindaian aset `Laptop Dell Latitude 5440 - 1` menghasilkan DU-020-9.
  - K6: sama dengan K1; pemindaian aset `Laptop Dell Latitude 5440 - 1` menghasilkan DU-020-10.
  - K7: sama dengan K1; pemindaian aset `Laptop Dell Latitude 5440 - 1` menghasilkan DU-020-11.
  - K8: sama dengan K1; pemindaian aset `Laptop Dell Latitude 5440 - 1` menghasilkan DU-020-12.
  - K9: sama dengan K1; pemindaian aset `Laptop Dell Latitude 5440 - 1` menghasilkan DU-020-13.
  - K10: sama dengan K1; pemindaian aset `Laptop Dell Latitude 5440 - 1` menghasilkan DU-020-14.
  - K11: sama dengan K1; pemindaian aset `Laptop Dell Latitude 5440 - 1` menghasilkan DU-020-15.
  - K12: sama dengan K1; pemindaian aset `Laptop Dell Latitude 5440 - 1` menghasilkan DU-020-16.
  - K13: sama dengan K1, tetapi aset `Laptop Dell Latitude 5440 - 1` sudah berbadge `Verified` dengan DU-020-17; pemindaian aset itu menghasilkan DU-020-17 lagi.
  - K14: sama dengan K1, tetapi aset `Laptop Dell Latitude 5440 - 1` sudah berbadge `Verified` dengan DU-020-17; pemindaian aset itu menghasilkan DU-020-18.
  - K15: sama dengan K1, tetapi aset `Laptop Dell Latitude 5440 - 1` sudah berbadge `Verified` dengan DU-020-17; pemindaian aset `Laptop Dell Latitude 5440 - 2` menghasilkan DU-020-17.
  - K16: sama dengan K1; pemindaian aset `Kursi Kerja Ergonomis - 1` menghasilkan DU-020-19.
  - K17: sama dengan K1; pembacaan pada aset `Laptop Dell Latitude 5440 - 1` dihentikan pengguna.
  - K18: form `Edit` draft tersimpan dengan Item DU-020-1; reader TAG tidak terhubung.
  - K19: form `Edit` draft tersimpan dengan Item DU-020-1 dan DU-020-2; tipe Tag QR terkunci oleh plan, tipe RFID tidak terkunci.
  - K20: form `Edit` draft tersimpan dengan Item DU-020-2 dan DU-020-5.
  - K21: form `Edit` draft tersimpan dengan Item DU-020-5 saja.

## Test Steps
### Kolom TAG: tombol Scan per tipe dan Badge Unverified
1. Tampilkan Halaman `Register Asset` dengan kondisi K1
2. Klik tab `Asset`
3. Verifikasi tombol `Scan RFID` tampil pada `Laptop Dell Latitude 5440 - 1`
4. Verifikasi tombol `Scan QR` tampil pada `Kursi Kerja Ergonomis - 1`
5. Verifikasi tombol `Scan RFID` dan `Scan NFC` tampil berpasangan pada `Printer Epson L3250 - 1`
6. Verifikasi tombol `Scan RFID` tampil pada `Forklift Toyota 8FD - 1`
7. Verifikasi tombol `Scan GPS` tidak tampil pada `Forklift Toyota 8FD - 1`
8. Verifikasi Badge `Unverified` tampil pada `Laptop Dell Latitude 5440 - 1`
9. Verifikasi kolom TAG tidak memiliki input teks untuk mengetik kode Tag
10. Verifikasi kolom TAG tidak memiliki aksi Skip

### Scan berhasil langsung menampilkan Badge Verified tanpa dialog
11. Tampilkan Halaman `Register Asset` dengan kondisi K2
12. Klik tab `Asset`
13. Klik `Scan RFID` pada `Laptop Dell Latitude 5440 - 1`
14. Verifikasi Badge `Verified` tampil pada `Laptop Dell Latitude 5440 - 1`
15. Verifikasi tidak ada dialog yang terbuka sesudah tombol `Scan RFID` diklik
16. Verifikasi tombol `Scan RFID` masih berlabel `Scan RFID` pada `Laptop Dell Latitude 5440 - 1`
17. Arahkan pointer ke Badge `Verified` pada `Laptop Dell Latitude 5440 - 1`
18. Verifikasi kode Tag `RFID-000501` tampil pada Badge `Verified`

### Tag tidak dikenal ditolak dan scan dapat diulang
19. Tampilkan Halaman `Register Asset` dengan kondisi K3
20. Klik tab `Asset`
21. Klik `Scan RFID` pada `Laptop Dell Latitude 5440 - 1`
22. Verifikasi pesan `Error, can't recognize TAG.` tampil
23. Verifikasi Badge `Unverified` pada `Laptop Dell Latitude 5440 - 1` tidak berubah
24. Verifikasi tombol `Scan RFID` pada `Laptop Dell Latitude 5440 - 1` masih dapat diklik untuk pemindaian ulang

### Tag ditolak karena status
25. Tampilkan Halaman `Register Asset` dengan kondisi K4
26. Klik tab `Asset`
27. Klik `Scan RFID` pada `Laptop Dell Latitude 5440 - 1`
28. Verifikasi pesan `RFID-000502 is not available (Paired)` tampil
29. Verifikasi Badge `Unverified` pada `Laptop Dell Latitude 5440 - 1` tidak berubah
30. Tampilkan Halaman `Register Asset` dengan kondisi K5
31. Klik tab `Asset`
32. Klik `Scan RFID` pada `Laptop Dell Latitude 5440 - 1`
33. Verifikasi pesan `RFID-000503 is not available (Reserved)` tampil
34. Verifikasi Badge `Unverified` pada `Laptop Dell Latitude 5440 - 1` tidak berubah
35. Tampilkan Halaman `Register Asset` dengan kondisi K6
36. Klik tab `Asset`
37. Klik `Scan RFID` pada `Laptop Dell Latitude 5440 - 1`
38. Verifikasi pesan `RFID-000504 is not available (Retired)` tampil
39. Verifikasi Badge `Unverified` pada `Laptop Dell Latitude 5440 - 1` tidak berubah
40. Tampilkan Halaman `Register Asset` dengan kondisi K7
41. Klik tab `Asset`
42. Klik `Scan RFID` pada `Laptop Dell Latitude 5440 - 1`
43. Verifikasi pesan `RFID-000505 is not available (Waiting for Approval)` tampil
44. Verifikasi Badge `Unverified` pada `Laptop Dell Latitude 5440 - 1` tidak berubah
45. Tampilkan Halaman `Register Asset` dengan kondisi K8
46. Klik tab `Asset`
47. Klik `Scan RFID` pada `Laptop Dell Latitude 5440 - 1`
48. Verifikasi pesan `RFID-000506 is not available (Damaged)` tampil
49. Verifikasi Badge `Unverified` pada `Laptop Dell Latitude 5440 - 1` tidak berubah
50. Tampilkan Halaman `Register Asset` dengan kondisi K10
51. Klik tab `Asset`
52. Klik `Scan RFID` pada `Laptop Dell Latitude 5440 - 1`
53. Verifikasi pesan `RFID-000508 is not available (To be Returned)` tampil
54. Verifikasi Badge `Unverified` pada `Laptop Dell Latitude 5440 - 1` tidak berubah

### Tag To be Returned dengan Return Group dalam scope diterima
55. Tampilkan Halaman `Register Asset` dengan kondisi K9
56. Klik tab `Asset`
57. Klik `Scan RFID` pada `Laptop Dell Latitude 5440 - 1`
58. Verifikasi Badge `Verified` tampil pada `Laptop Dell Latitude 5440 - 1`

### Tag user dan Tag produk lain ditolak
59. Tampilkan Halaman `Register Asset` dengan kondisi K11
60. Klik tab `Asset`
61. Klik `Scan RFID` pada `Laptop Dell Latitude 5440 - 1`
62. Verifikasi pesan `This is a user TAG. Scan an asset TAG.` tampil
63. Tampilkan Halaman `Register Asset` dengan kondisi K12
64. Klik tab `Asset`
65. Klik `Scan RFID` pada `Laptop Dell Latitude 5440 - 1`
66. Verifikasi pesan `This TAG is used by Supply Asset` tampil

### Tag sama, duplikat di form, dan tipe lain ditolak
67. Tampilkan Halaman `Register Asset` dengan kondisi K13
68. Klik tab `Asset`
69. Klik `Scan RFID` pada `Laptop Dell Latitude 5440 - 1`
70. Verifikasi pesan `This TAG is the same as the current TAG` tampil
71. Verifikasi Badge `Verified` pada `Laptop Dell Latitude 5440 - 1` tidak berubah
72. Tampilkan Halaman `Register Asset` dengan kondisi K15
73. Klik tab `Asset`
74. Klik `Scan RFID` pada `Laptop Dell Latitude 5440 - 2`
75. Verifikasi pesan `This TAG has already been scanned` tampil
76. Verifikasi Badge `Unverified` pada `Laptop Dell Latitude 5440 - 2` tidak berubah
77. Tampilkan Halaman `Register Asset` dengan kondisi K16
78. Klik tab `Asset`
79. Klik `Scan QR` pada `Kursi Kerja Ergonomis - 1`
80. Verifikasi pesan `This slot needs a QR TAG` tampil
81. Verifikasi Badge `Unverified` pada `Kursi Kerja Ergonomis - 1` tidak berubah

### Rescan pada slot terisi mengganti Tag
82. Tampilkan Halaman `Register Asset` dengan kondisi K14
83. Klik tab `Asset`
84. Klik `Scan RFID` pada `Laptop Dell Latitude 5440 - 1`
85. Verifikasi Badge `Verified` pada `Laptop Dell Latitude 5440 - 1` memuat kode Tag `RFID-000511`
86. Verifikasi kode Tag `RFID-000510` tidak lagi tampil pada `Laptop Dell Latitude 5440 - 1`

### Pembacaan dihentikan pengguna tidak mengubah slot
87. Tampilkan Halaman `Register Asset` dengan kondisi K17
88. Klik tab `Asset`
89. Klik `Scan RFID` pada `Laptop Dell Latitude 5440 - 1`
90. Verifikasi Badge `Unverified` pada `Laptop Dell Latitude 5440 - 1` tidak berubah

### Tombol Scan Disabled saat reader tidak terhubung
91. Tampilkan Halaman `Register Asset` dengan kondisi K18
92. Klik tab `Asset`
93. Verifikasi tombol `Scan RFID` pada `Laptop Dell Latitude 5440 - 1` berstatus Disabled
94. Verifikasi tooltip `Connect a TAG reader to scan.` tampil saat pointer berada di tombol `Scan RFID`
95. Verifikasi banner reader tidak terhubung tampil

### Tombol Scan Disabled untuk tipe Tag terkunci plan
96. Tampilkan Halaman `Register Asset` dengan kondisi K19
97. Klik tab `Asset`
98. Verifikasi tombol `Scan RFID` pada `Laptop Dell Latitude 5440 - 1` tidak Disabled
99. Verifikasi tombol `Scan QR` pada `Kursi Kerja Ergonomis - 1` berstatus Disabled
100. Verifikasi tooltip `This TAG type isn't available on your plan.` tampil saat pointer berada di tombol `Scan QR`

### Item Non-TAG menampilkan No tag dan kolom TAG tersembunyi bila semua aset Non-TAG
101. Tampilkan Halaman `Register Asset` dengan kondisi K20
102. Klik tab `Asset`
103. Verifikasi `No tag` tampil di kolom TAG untuk aset `Meja Lipat Aluminium - 1`
104. Tampilkan Halaman `Register Asset` dengan kondisi K21
105. Klik tab `Asset`
106. Verifikasi kolom `Name` menampilkan `Meja Lipat Aluminium - 1`
107. Verifikasi kolom TAG tidak tampil
