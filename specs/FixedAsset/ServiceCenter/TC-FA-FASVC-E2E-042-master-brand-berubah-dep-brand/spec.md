---
id: TC-FA-FASVC-E2E-042-master-brand-berubah-dep-brand
title: "Brand Di-Inactivate, Dihapus, Di-merge, atau Di-rename: Brands Service Center"
layer: ui-e2e
priority: High
caseType: Positive
status: ready-for-automation
sourceRules: [MR-FASVC-05a, MR-FASVC-05b, MR-FASVC-05c, MR-FASVC-06a, MR-FASVC-06b, MR-FASVC-06c, MR-FASVC-08a, MR-FASVC-08b, MR-FASVC-08c, MR-FASVC-08d, MR-FASVC-09a, MR-FASVC-09b, MR-FASVC-10a, MR-FASVC-10b, EC-FASVC-48, EC-FASVC-49a, EC-FASVC-49b, EC-FASVC-50a, EC-FASVC-50b, EC-FASVC-50c, EC-FASVC-57a, EC-FASVC-57b, EC-FASVC-57c, EC-FASVC-59, F-FASVC-08.k5, F-FASVC-08.k6, F-FASVC-08.k7, F-FASVC-08.k8, F-FASVC-08.k9, "§8#r18", "§9.2#p9", S-FASVC-09, FASVC-LOGIC-02m, "§9.7#r6", "§9.4.3#b4"]
smoke: []
dependsOn: ["Brand: master Brand"]
trace:
  MR-FASVC-05a: 10
  MR-FASVC-05b: 10
  MR-FASVC-05c: 12
  MR-FASVC-06a: [37, 40, 63, 64]
  MR-FASVC-06b: 48
  MR-FASVC-06c: 52
  MR-FASVC-08a: 100
  MR-FASVC-08b: 96
  MR-FASVC-08c: [89, 91]
  MR-FASVC-08d: 99
  MR-FASVC-09a: 48
  MR-FASVC-09b: 49
  MR-FASVC-10a: 31
  MR-FASVC-10b: [40, 52]
  EC-FASVC-48: [63, 69, 72]
  EC-FASVC-49a: 48
  EC-FASVC-49b: 52
  EC-FASVC-50a: 10
  EC-FASVC-50b: 12
  EC-FASVC-50c: 22
  EC-FASVC-57a: 96
  EC-FASVC-57b: [89, 91]
  EC-FASVC-57c: 99
  EC-FASVC-59: [53, 54]
  F-FASVC-08.k5: [48, 52]
  F-FASVC-08.k6: [63, 72]
  F-FASVC-08.k7: 16
  F-FASVC-08.k8: [99, 100]
  F-FASVC-08.k9: [53, 54]
  "§8#r18": [40, 52, 69, 72]
  "§9.2#p9": [63, 64, 66, 69, 70, 72]
  S-FASVC-09: [12, 22]
  FASVC-LOGIC-02m: 48
  "§9.7#r6": [10, 37, 48, 63]
  "§9.4.3#b4": 96
anchor: [2, 21, 25, 27, 36, 43, 57, 59, 75, 80, 83]
coverage:
  web: automated
---
# Brand Di-Inactivate, Dihapus, Di-merge, atau Di-rename: Brands Service Center

## Prerequisites
- Aktor: Total Control `Rina Wulandari {runId}` (cakupan seluruh Group) menguji layarnya. Admin Brand `Dimas Pratama {runId}` (Total Control, cakupan seluruh Group) memicu perubahan di master Brand dari sesinya sendiri.
- Layar awal: Add-ons > Service Center.
- Data:
  - DU-042-1: Brand `Daikin {runId}`, Status `Active`, ada di entitas aktor.
  - DU-042-2: Brand `LG {runId}`, Status `Active`.
  - DU-042-3: Brand `Hitachi {runId}`, Status `Active`.
  - DU-042-4: Brand `Panasonic {runId}`, Status `Active`.
  - DU-042-5: Brand `Samsung {runId}`, Status `Active`.
  - DU-042-6: Brand `Sanyo {runId}`, Status `Active`.
  - DU-042-7: Brand `Sharp {runId}`, Status `Active`.
  - DU-042-8: Brand `Toshiba {runId}`, Status `Active`.
  - DU-042-9: Brand `Polytron {runId}`, Status `Active`.
  - DU-042-10: Brand `Fujitsu {runId}`, Status `Active`.
  - DU-042-11: Brand `Mitsubishi {runId}`, Status `Active`.
  - DU-042-12: Service Center `Servis AC Mitra Bandung {runId}`, Service type `Routine` dan `Repair`, Available to `All groups`, Specialization kosong (`All categories`), Brands `Daikin {runId}` dan `LG {runId}`, Country `Indonesia`, City `Bandung`, Company phone nomor `81234500421`, Company email `ac@mitrabandung.example`, Usage `0`, Status `Active`.
  - DU-042-13: Service Center `Servis AC Mitra Cimahi {runId}`, Service type `Routine` dan `Repair`, Available to `All groups`, Specialization kosong (`All categories`), Brands kosong (`All brands`), Country `Indonesia`, City `Cimahi`, Company phone nomor `81234500422`, Company email `ac@mitracimahi.example`, Usage `0`, Status `Active`.
  - DU-042-14: Service Center `Servis Elektronik Mitra Bekasi {runId}`, Service type `Routine` dan `Repair`, Available to `All groups`, Specialization kosong (`All categories`), Brands `Hitachi {runId}` dan `Panasonic {runId}`, Country `Indonesia`, City `Bekasi`, Company phone nomor `81234500423`, Company email `elektronik@mitrabekasi.example`, Usage `0`, Status `Active`.
  - DU-042-15: Service Center `Servis Pompa Mitra Depok {runId}`, Service type `Routine` dan `Repair`, Available to `All groups`, Specialization kosong (`All categories`), Brands `Samsung {runId}` dan `Sanyo {runId}`, Country `Indonesia`, City `Depok`, Company phone nomor `81234500424`, Company email `pompa@mitradepok.example`, Usage `0`, Status `Active`.
  - DU-042-16: Service Center `Servis Audio Mitra Bogor {runId}`, Service type `Routine` dan `Repair`, Available to `All groups`, Specialization kosong (`All categories`), Brands `Sharp {runId}` dan `Toshiba {runId}`, Country `Indonesia`, City `Bogor`, Company phone nomor `81234500425`, Company email `audio@mitrabogor.example`, Usage `0`, Status `Active`.
  - DU-042-17: Service Center `Servis Audio Mitra Tangerang {runId}`, Service type `Routine` dan `Repair`, Available to `All groups`, Specialization kosong (`All categories`), Brands `Polytron {runId}` dan `Toshiba {runId}`, Country `Indonesia`, City `Tangerang`, Company phone nomor `81234500426`, Company email `audio@mitratangerang.example`, Usage `0`, Status `Active`.
  - DU-042-18: Service Center `Servis Mesin Mitra Cirebon {runId}`, Service type `Routine` dan `Repair`, Available to `All groups`, Specialization kosong (`All categories`), Brands `Fujitsu {runId}`, Country `Indonesia`, City `Cirebon`, Company phone nomor `81234500427`, Company email `mesin@mitracirebon.example`, Usage `0`, Status `Active`.
  - DU-042-19: Notes `Perlu cek ulang kontrak {runId}`, nilai yang dicoba disimpan pada dialog Edit `Servis Elektronik Mitra Bekasi {runId}`.
  - DU-042-20: User Total Control `Rina Wulandari {runId}`, cakupan seluruh Group.
  - DU-042-21: User Admin Brand `Dimas Pratama {runId}`, role Total Control, cakupan seluruh Group.
  - Brand pada DU-042-1 sampai DU-042-11 belum dipakai aset.

## Test Steps

### Brand di-Inactivate: Brands tetap tersimpan, tampil dengan badge Inactive, dan tidak dapat dipilih baru
1. Ketik Search `Servis AC Mitra Bandung {runId}`, tekan Enter
2. Verifikasi baris `Servis AC Mitra Bandung {runId}` tampil dengan Brands `Daikin {runId}` dan `LG {runId}`
3. Klik `Changelog` pada toolbar
4. Ketik Search `Servis AC Mitra Bandung {runId}` pada modal `Changelog: Service Center`, tekan Enter
5. Catat jumlah baris yang tampil di modal sebagai jumlah awal
6. Tutup modal `Changelog: Service Center` lewat icon close
7. Admin Brand meng-inactivate Brand `Daikin {runId}` di master Brand
8. Muat ulang halaman
9. Ganti isi kotak Search dengan `Servis AC Mitra Bandung {runId}`, tekan Enter
10. Verifikasi Brands baris `Servis AC Mitra Bandung {runId}` tetap memuat `Daikin {runId}` dan `LG {runId}`
11. Klik `⋯` pada baris `Servis AC Mitra Bandung {runId}`, lalu klik `Edit`
12. Verifikasi field Brands di dialog `Edit Service Center` memuat `Daikin {runId}` dengan badge `Inactive`
13. Klik `✕` pada form yang belum diubah
14. Klik `Changelog` pada toolbar
15. Ketik Search `Servis AC Mitra Bandung {runId}` pada modal `Changelog: Service Center`, tekan Enter
16. Verifikasi jumlah baris untuk `Servis AC Mitra Bandung {runId}` di modal sama dengan jumlah awal
17. Tutup modal `Changelog: Service Center` lewat icon close
18. Ganti isi kotak Search dengan `Servis AC Mitra Cimahi {runId}`, tekan Enter
19. Klik `⋯` pada baris `Servis AC Mitra Cimahi {runId}`, lalu klik `Edit`
20. Klik field Brands untuk membuka daftar pilihan
21. Verifikasi daftar pilihan Brands memuat `LG {runId}`
22. Verifikasi daftar pilihan Brands tidak memuat `Daikin {runId}`
23. Klik `✕` pada form yang belum diubah

### Brand dihapus saat dialog Edit terbuka: Brand dilepas dari Brands dan versi data naik
24. Ganti isi kotak Search dengan `Servis Elektronik Mitra Bekasi {runId}`, tekan Enter
25. Verifikasi baris `Servis Elektronik Mitra Bekasi {runId}` tampil dengan Brands `Hitachi {runId}` dan `Panasonic {runId}`
26. Klik `⋯` pada baris `Servis Elektronik Mitra Bekasi {runId}`, lalu klik `Edit`
27. Verifikasi field Brands di dialog `Edit Service Center` memuat `Hitachi {runId}` dan `Panasonic {runId}`
28. Admin Brand menghapus Brand `Hitachi {runId}` dari master Brand
29. Ganti isi field Notes dengan `Perlu cek ulang kontrak {runId}`
30. Klik `[Save]`
31. Verifikasi dialog `Service Center Changed` tampil karena versi data dinaikkan oleh System
32. Klik `[OK]`
33. Klik `✕` pada form yang belum diubah sejak diisi ulang
34. Muat ulang halaman
35. Ganti isi kotak Search dengan `Servis Elektronik Mitra Bekasi {runId}`, tekan Enter
36. Verifikasi Brands baris `Servis Elektronik Mitra Bekasi {runId}` memuat `Panasonic {runId}`
37. Verifikasi Brands baris `Servis Elektronik Mitra Bekasi {runId}` tidak memuat `Hitachi {runId}`
38. Klik `Changelog` pada toolbar
39. Ketik Search `Servis Elektronik Mitra Bekasi {runId}` pada modal `Changelog: Service Center`, tekan Enter
40. Verifikasi entri dengan Action `Updated`, Field `Brands`, Old Value `Hitachi {runId}, Panasonic {runId}`, New Value `Panasonic {runId}`, dan Modified By `System` tampil
41. Tutup modal `Changelog: Service Center` lewat icon close

### Dua Brand dihapus beruntun: cakupan melebar tanpa konfirmasi dan tiap perubahan tercatat sebagai entri Changelog sendiri
42. Ganti isi kotak Search dengan `Servis Pompa Mitra Depok {runId}`, tekan Enter
43. Verifikasi baris `Servis Pompa Mitra Depok {runId}` tampil dengan Brands `Samsung {runId}` dan `Sanyo {runId}`
44. Admin Brand menghapus Brand `Samsung {runId}` dari master Brand
45. Admin Brand menghapus Brand `Sanyo {runId}` dari master Brand
46. Muat ulang halaman
47. Ganti isi kotak Search dengan `Servis Pompa Mitra Depok {runId}`, tekan Enter
48. Verifikasi Brands baris `Servis Pompa Mitra Depok {runId}` tampil `All brands` tanpa aksi `[Save]` dan tanpa dialog `Widen Coverage` dari pengguna
49. Verifikasi Status baris `Servis Pompa Mitra Depok {runId}` tetap `Active`
50. Klik `Changelog` pada toolbar
51. Ketik Search `Servis Pompa Mitra Depok {runId}` pada modal `Changelog: Service Center`, tekan Enter
52. Verifikasi entri dengan Action `Updated`, Field `Brands`, Old Value `Sanyo {runId}`, New Value `All brands`, dan Modified By `System` tampil
53. Verifikasi entri dengan Action `Updated`, Field `Brands`, Old Value `Samsung {runId}, Sanyo {runId}`, New Value `Sanyo {runId}`, dan Modified By `System` tampil
54. Verifikasi hanya ada dua entri dengan Action `Updated` dan Field `Brands`, satu untuk tiap Brand yang dihapus
55. Tutup modal `Changelog: Service Center` lewat icon close

### Brand di-merge: Brand sumber diganti Brand hasil merge tanpa ganda
56. Ganti isi kotak Search dengan `Servis Audio Mitra Bogor {runId}`, tekan Enter
57. Verifikasi baris `Servis Audio Mitra Bogor {runId}` tampil dengan Brands `Sharp {runId}` dan `Toshiba {runId}`
58. Ganti isi kotak Search dengan `Servis Audio Mitra Tangerang {runId}`, tekan Enter
59. Verifikasi baris `Servis Audio Mitra Tangerang {runId}` tampil dengan Brands `Polytron {runId}` dan `Toshiba {runId}`
60. Admin Brand me-merge Brand `Sharp {runId}` dan `Toshiba {runId}` ke Brand `Polytron {runId}` di master Brand
61. Muat ulang halaman
62. Ganti isi kotak Search dengan `Servis Audio Mitra Bogor {runId}`, tekan Enter
63. Verifikasi Brands baris `Servis Audio Mitra Bogor {runId}` tampil satu entri `Polytron {runId}`
64. Verifikasi Brands baris `Servis Audio Mitra Bogor {runId}` tidak memuat `Sharp {runId}` dan `Toshiba {runId}`
65. Ganti isi kotak Search dengan `Servis Audio Mitra Tangerang {runId}`, tekan Enter
66. Verifikasi Brands baris `Servis Audio Mitra Tangerang {runId}` tampil satu entri `Polytron {runId}` tanpa ganda
67. Klik `Changelog` pada toolbar
68. Ketik Search `Servis Audio Mitra Tangerang {runId}` pada modal `Changelog: Service Center`, tekan Enter
69. Verifikasi entri dengan Action `Updated`, Field `Brands`, Old Value `Polytron {runId}, Toshiba {runId}`, New Value `Polytron {runId}`, dan Modified By `System` tampil
70. Verifikasi hanya ada satu entri dengan Action `Updated` dan Field `Brands` untuk `Servis Audio Mitra Tangerang {runId}`
71. Ganti isi kotak Search dengan `Servis Audio Mitra Bogor {runId}` pada modal `Changelog: Service Center`, tekan Enter
72. Verifikasi entri dengan Action `Updated`, Field `Brands`, Old Value `Sharp {runId}, Toshiba {runId}`, New Value `Polytron {runId}`, dan Modified By `System` tampil
73. Tutup modal `Changelog: Service Center` lewat icon close

### Brand di-rename: nama terkini tampil di tabel dan form, pencocokan memakai ID, Changelog lama tetap nama snapshot
74. Ganti isi kotak Search dengan `Servis Mesin Mitra Cirebon {runId}`, tekan Enter
75. Verifikasi baris `Servis Mesin Mitra Cirebon {runId}` tampil dengan Brands `Fujitsu {runId}`
76. Klik `⋯` pada baris `Servis Mesin Mitra Cirebon {runId}`, lalu klik `Edit`
77. Klik field Brands untuk membuka daftar pilihan
78. Pilih `Mitsubishi {runId}` pada field Brands
79. Klik `[Save]`
80. Verifikasi Brands baris `Servis Mesin Mitra Cirebon {runId}` memuat `Fujitsu {runId}` dan `Mitsubishi {runId}`
81. Klik `Changelog` pada toolbar
82. Ketik Search `Servis Mesin Mitra Cirebon {runId}` pada modal `Changelog: Service Center`, tekan Enter
83. Verifikasi entri dengan Action `Updated`, Field `Brands`, Old Value `Fujitsu {runId}`, dan New Value `Fujitsu {runId}, Mitsubishi {runId}` tampil
84. Catat jumlah baris yang tampil di modal sebagai jumlah awal
85. Tutup modal `Changelog: Service Center` lewat icon close
86. Admin Brand mengubah nama Brand `Mitsubishi {runId}` menjadi `Mitsubishi Electric {runId}` di master Brand
87. Muat ulang halaman
88. Ganti isi kotak Search dengan `Servis Mesin Mitra Cirebon {runId}`, tekan Enter
89. Verifikasi Brands baris `Servis Mesin Mitra Cirebon {runId}` memuat `Fujitsu {runId}` dan `Mitsubishi Electric {runId}`
90. Klik `⋯` pada baris `Servis Mesin Mitra Cirebon {runId}`, lalu klik `Edit`
91. Verifikasi field Brands di dialog `Edit Service Center` memuat `Mitsubishi Electric {runId}`
92. Klik `✕` pada form yang belum diubah
93. Klik `Filter` pada toolbar
94. Pilih `Mitsubishi Electric {runId}` pada field Brands di Filter Panel
95. Klik `[Apply]`
96. Verifikasi baris `Servis Mesin Mitra Cirebon {runId}` tampil karena Brand `Mitsubishi Electric {runId}` dicocokkan lewat ID
97. Klik `Changelog` pada toolbar
98. Ketik Search `Servis Mesin Mitra Cirebon {runId}` pada modal `Changelog: Service Center`, tekan Enter
99. Verifikasi entri dengan Action `Updated`, Field `Brands`, dan New Value `Fujitsu {runId}, Mitsubishi {runId}` tetap tampil dengan nama lama
100. Verifikasi jumlah baris untuk `Servis Mesin Mitra Cirebon {runId}` di modal sama dengan jumlah awal
101. Tutup modal `Changelog: Service Center` lewat icon close
