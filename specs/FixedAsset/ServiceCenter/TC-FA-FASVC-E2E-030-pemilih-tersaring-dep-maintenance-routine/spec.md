---
id: TC-FA-FASVC-E2E-030-pemilih-tersaring-dep-maintenance-routine
title: "Select Service Center di Maintenance Routine: Hanya Vendor yang Memenuhi Syarat"
layer: ui-e2e
priority: Critical
caseType: Negative
status: ready-for-automation
sourceRules: [FASVC-LOGIC-04a, FASVC-LOGIC-04b, FASVC-LOGIC-04c, FASVC-LOGIC-04d, FASVC-LOGIC-04e, FASVC-LOGIC-04f, FASVC-LOGIC-04g, FASVC-LOGIC-04h, FASVC-LOGIC-04i, FASVC-LOGIC-04j, FASVC-LOGIC-04k, FASVC-LOGIC-04l, F-FASVC-05.k1, F-FASVC-05.k2, F-FASVC-05.k5, EC-FASVC-17, EC-FASVC-24, EC-FASVC-45, EC-FASVC-46, "§9.2#p10", "§9.2#p11", "§9.7#r9", "§9.5#r10", "§Aturan Logika Modul#p9", "§Aturan Logika Modul#p11", "§Aturan Logika Modul#p12", "§Aturan Logika Modul#p13", "EB-XM-2@maintenance-routine", "§9.4.3#b5"]
smoke: []
dependsOn: ["Maintenance Routine: form Schedule dan Task"]
trace:
  FASVC-LOGIC-04a: [4, 5, 7, 8, 9, 10, 11, 19, 20, 21, 30, 31, 32]
  FASVC-LOGIC-04b: 7
  FASVC-LOGIC-04c: 8
  FASVC-LOGIC-04d: [9, 95, 99]
  FASVC-LOGIC-04e: [4, 5, 10]
  FASVC-LOGIC-04f: [5, 11, 15, 108]
  FASVC-LOGIC-04g: 15
  FASVC-LOGIC-04h: [19, 20, 21, 103, 104]
  FASVC-LOGIC-04i: [30, 31]
  FASVC-LOGIC-04j: [30, 32]
  FASVC-LOGIC-04k: [37, 38]
  FASVC-LOGIC-04l: 6
  F-FASVC-05.k1: 15
  F-FASVC-05.k2: 25
  F-FASVC-05.k5: [37, 38]
  EC-FASVC-17: 15
  EC-FASVC-24: 25
  EC-FASVC-45: [20, 112, 113]
  EC-FASVC-46: [37, 38]
  "§9.2#p10": [5, 11, 15]
  "§9.2#p11": [20, 21, 103, 104]
  "§9.7#r9": 51
  "§9.5#r10": 6
  "§Aturan Logika Modul#p9": [20, 113]
  "§Aturan Logika Modul#p11": [20, 113]
  "§Aturan Logika Modul#p12": [20, 113]
  "§Aturan Logika Modul#p13": [25, 112]
  "EB-XM-2@maintenance-routine": [51, 61, 62, 72, 81, 91]
  "§9.4.3#b5": 15
anchor: [71, 90]
coverage:
  web: automated
---

# Select Service Center di Maintenance Routine: Hanya Vendor yang Memenuhi Syarat

## Prerequisites
- Aktor: Total Control entitas `Klien Pemilih Vendor {runId}`.
- Layar awal: Maintenance Routine.
- Data:
  - Spec ini memakai entitas khusus `Klien Pemilih Vendor {runId}` yang tidak dipakai spec lain.
  - DU-030-23: Entitas `Klien Pemilih Vendor {runId}`, lisensi addon Maintenance `Active`.
  - DU-030-1: Group `Kantor Pusat {runId}`, dengan anak `Cabang Surabaya {runId}` dan `Cabang Malang {runId}`.
  - DU-030-25: Group `Wilayah Semarang {runId}`, Group tersendiri di luar `Kantor Pusat {runId}`.
  - DU-030-2: Category `Pendingin {runId}` dengan anak `AC {runId}`.
  - DU-030-3: Category `Pembangkit {runId}` dengan anak `Genset {runId}`.
  - DU-030-4: Brand `Daikin {runId}`.
  - DU-030-5: Brand `LG {runId}`.
  - DU-030-6: Aset `AC Ruang Server {runId}`, Group `Cabang Surabaya {runId}`, Category `AC {runId}`, Brand `Daikin {runId}`.
  - DU-030-7: Aset `AC Lobi {runId}`, Group `Cabang Surabaya {runId}`, Category `AC {runId}`, Brand `LG {runId}`.
  - DU-030-8: Aset `Genset Cadangan {runId}`, Group `Cabang Malang {runId}`, Category `Genset {runId}`, tanpa Brand.
  - DU-030-9: Aset `Genset Gudang {runId}`, Group `Cabang Malang {runId}`, Category `Genset {runId}`, Brand `Daikin {runId}`.
  - DU-030-26: Aset `AC Aula Semarang {runId}`, Group `Wilayah Semarang {runId}`, Category `AC {runId}`, Brand `Daikin {runId}`.
  - DU-030-27: Aset `AC Kantin Semarang {runId}`, Group `Wilayah Semarang {runId}`, Category `AC {runId}`, Brand `LG {runId}`.
  - DU-030-10: Service Center `Anugerah Servis Umum {runId}`, Service type `Routine`, Status `Active`, Available to `Cabang Surabaya {runId}`, Specialization belum diisi, Brands belum diisi, City `Surabaya`, Company phone `+62 315550101`.
  - DU-030-11: Service Center `Sejuk Abadi Teknik {runId}`, Service type `Routine` dan `Repair`, Status `Active`, Available to `Cabang Surabaya {runId}`, Specialization `Pendingin {runId}`, Brands `Daikin {runId}`, City `Surabaya`, Company phone `+62 315550102`.
  - DU-030-12: Service Center `Lestari LG Service {runId}`, Service type `Routine`, Status `Active`, Available to `Kantor Pusat {runId}`, Specialization belum diisi, Brands `LG {runId}`, City `Surabaya`, Company phone `+62 315550103`.
  - DU-030-13: Service Center `Prima Genset Service {runId}`, Service type `Routine`, Status `Active`, Available to `Cabang Malang {runId}`, Specialization `Genset {runId}`, Brands `Daikin {runId}`, City `Malang`, Company phone `+62 341550104`.
  - DU-030-14: Service Center `Bengkel Motor Jaya {runId}`, Service type `Repair`, Status `Active`, Available to `Kantor Pusat {runId}`, Specialization belum diisi, Brands belum diisi, City `Bandung`, Company phone `+62 225550105`.
  - DU-030-15: Service Center `Dingin Mandiri Servis {runId}`, Service type `Routine`, Status `Inactive`, Available to `Cabang Surabaya {runId}`, Specialization belum diisi, Brands belum diisi, City `Surabaya`, Company phone `+62 315550106`.
  - DU-030-16: Service Center `Cahaya Kalibrasi {runId}`, Service type `Routine`, Status `Active`, Available to `Cabang Malang {runId}`, Specialization belum diisi, Brands belum diisi, City `Malang`, Company phone `+62 341550107`.
  - DU-030-17: Service Center `Gemilang Pembangkit {runId}`, Service type `Routine`, Status `Active`, Available to `Cabang Surabaya {runId}`, Specialization `Genset {runId}`, Brands belum diisi, City `Surabaya`, Company phone `+62 315550108`.
  - DU-030-18: Service Center `Kencana Pendingin Malang {runId}`, Service type `Routine`, Status `Active`, Available to `Cabang Malang {runId}`, Specialization `AC {runId}`, Brands belum diisi, City `Malang`, Company phone `+62 341550109`.
  - DU-030-24: Service Center `Pendingin Pusat Teknik {runId}`, Service type `Routine`, Status `Active`, Available to `Kantor Pusat {runId}`, Specialization `Pendingin {runId}`, Brands `Daikin {runId}`, City `Surabaya`, Company phone `+62 315550110`, dibuat sesudah DU-030-10 dan DU-030-11.
  - DU-030-28: Service Center `Daikin Khusus Semarang {runId}`, Service type `Routine`, Status `Active`, Available to `Wilayah Semarang {runId}`, Specialization belum diisi, Brands `Daikin {runId}`, City `Semarang`, Company phone `+62 245550111`.
- Kondisi:
  - Lisensi addon Maintenance aktif.
  - Entitas `Klien Pemilih Vendor {runId}` hanya berisi Service Center yang tercantum di Data dan yang dibuat spec ini.
  - Schedule `Servis Genset Berkala {runId}` disimpan dengan seluruh field wajib form Schedule terisi nilai valid.

## Test Steps

### Pemilih satu aset hanya memuat vendor yang memenuhi syarat
1. Buka form Create Schedule di Maintenance Routine
2. Pilih aset `AC Ruang Server {runId}` saja
3. Klik pemilih `Select service center`
4. Verifikasi opsi `Anugerah Servis Umum {runId}` tampil (Specialization belum diisi)
5. Verifikasi opsi `Sejuk Abadi Teknik {runId}` tampil (Specialization `Pendingin {runId}` adalah induk dari kategori aset `AC {runId}`, dan Brands memuat merek aset `Daikin {runId}`)
6. Verifikasi urutan opsi dari atas ke bawah adalah `Anugerah Servis Umum {runId}`, `Pendingin Pusat Teknik {runId}`, `Sejuk Abadi Teknik {runId}` (Name A–Z, berbeda dari urutan ketiganya dibuat)
7. Verifikasi `Dingin Mandiri Servis {runId}` yang berstatus `Inactive` tidak ada di opsi
8. Verifikasi `Bengkel Motor Jaya {runId}` yang Service type-nya hanya `Repair` tidak ada di opsi
9. Verifikasi `Cahaya Kalibrasi {runId}` yang Available to-nya hanya `Cabang Malang {runId}` tidak ada di opsi
10. Verifikasi `Gemilang Pembangkit {runId}` yang Specialization-nya `Genset {runId}` tidak ada di opsi
11. Verifikasi `Lestari LG Service {runId}` yang Brands-nya hanya `LG {runId}` tidak ada di opsi

### Aset tanpa merek tidak diuji syarat Brands
12. Buka form Create Schedule di Maintenance Routine
13. Pilih aset `Genset Cadangan {runId}` saja
14. Klik pemilih `Select service center`
15. Verifikasi opsi `Prima Genset Service {runId}` yang Brands-nya `Daikin {runId}` tampil walau aset tidak punya merek

### Banyak aset: syarat berlaku untuk setiap aset
16. Buka form Create Schedule di Maintenance Routine
17. Pilih aset `AC Ruang Server {runId}` (merek `Daikin {runId}`) dan `AC Lobi {runId}` (merek `LG {runId}`)
18. Klik pemilih `Select service center`
19. Verifikasi opsi `Anugerah Servis Umum {runId}` tampil
20. Verifikasi `Sejuk Abadi Teknik {runId}` yang hanya melayani merek `Daikin {runId}` tidak ada di opsi
21. Verifikasi `Lestari LG Service {runId}` yang hanya melayani merek `LG {runId}` tidak ada di opsi

### Tidak ada vendor yang cocok untuk semua aset
22. Buka form Create Schedule di Maintenance Routine
23. Pilih aset `AC Ruang Server {runId}` (lokasi `Cabang Surabaya {runId}`) dan `Genset Cadangan {runId}` (lokasi `Cabang Malang {runId}`)
24. Klik pemilih `Select service center`
25. Verifikasi pesan `No service center covers every asset here. Split the schedule or widen a service center's coverage.` tampil

### Schedule All matching assets menguji kategori Schedule dan merek aset yang cocok
26. Buka form Create Schedule di Maintenance Routine
27. Isi Name `Servis Genset Berkala {runId}`
28. Pilih mode `All matching assets` dan kategori `Genset {runId}`
29. Klik pemilih `Select service center`
30. Verifikasi opsi `Prima Genset Service {runId}` tampil (Specialization `Genset {runId}` dan Brands `Daikin {runId}`, merek aset `Genset Gudang {runId}` yang cocok)
31. Verifikasi `Kencana Pendingin Malang {runId}` yang Specialization-nya `AC {runId}` tidak ada di opsi
32. Verifikasi `Lestari LG Service {runId}` yang Brands-nya hanya `LG {runId}` tidak ada di opsi
33. Pilih `Prima Genset Service {runId}` sebagai pelaksana default
34. Simpan Schedule dengan seluruh field wajib Schedule lainnya terisi nilai valid

### Aset yang masuk kemudian diuji ulang oleh Maintenance Routine
35. Aset `Genset Baru {runId}` (lokasi `Cabang Malang {runId}`, kategori `Genset {runId}`, merek `LG {runId}`) didaftarkan sehingga masuk Schedule `Servis Genset Berkala {runId}`
36. Job pembuatan Task Schedule `Servis Genset Berkala {runId}` berjalan
37. Verifikasi Task untuk aset `Genset Baru {runId}` berstatus `Waiting for Assignment`
38. Verifikasi Task itu bertanda `Service center doesn't cover this asset`

### Service Center baru langsung muncul di pemilih
39. Buka Add-ons > Service Center
40. Klik `[+ Service Center]`
41. Isi Name `Nusantara Servis Baru {runId}`
42. Centang Service type `Routine`
43. Hilangkan centang `All groups` pada Available to
44. Pilih Available to `Cabang Surabaya {runId}`
45. Isi City `Surabaya`
46. Isi Company phone dengan Dial Code `+62` dan nomor `315550123`
47. Klik `[Submit]`
48. Buka form Create Schedule di Maintenance Routine
49. Pilih aset `AC Ruang Server {runId}` saja
50. Klik pemilih `Select service center`
51. Verifikasi opsi `Nusantara Servis Baru {runId}` tampil

### Edit Name tercermin di pemilih
52. Buka Add-ons > Service Center
53. Ketik Search `Nusantara Servis Baru {runId}`, tekan Enter
54. Klik `⋯` pada baris `Nusantara Servis Baru {runId}`
55. Klik `Edit`
56. Ganti isi Name menjadi `Nusantara Servis Utama {runId}`
57. Klik `[Save]`
58. Buka form Create Schedule di Maintenance Routine
59. Pilih aset `AC Ruang Server {runId}` saja
60. Klik pemilih `Select service center`
61. Verifikasi opsi `Nusantara Servis Utama {runId}` tampil
62. Verifikasi `Nusantara Servis Baru {runId}` tidak ada di opsi

### Inactivate menghilangkan vendor dari pemilih
63. Buka Add-ons > Service Center
64. Ketik Search `Nusantara Servis Utama {runId}`, tekan Enter
65. Klik `⋯` pada baris `Nusantara Servis Utama {runId}`
66. Klik `Inactivate`
67. Klik `[Inactivate]` pada dialog `Inactivate Service Center`
68. Buka form Create Schedule di Maintenance Routine
69. Pilih aset `AC Ruang Server {runId}` saja
70. Klik pemilih `Select service center`
71. Verifikasi opsi `Anugerah Servis Umum {runId}` tampil
72. Verifikasi `Nusantara Servis Utama {runId}` yang berstatus `Inactive` tidak ada di opsi

### Activate mengembalikan vendor ke pemilih
73. Buka Add-ons > Service Center
74. Ketik Search `Nusantara Servis Utama {runId}`, tekan Enter
75. Klik `⋯` pada baris `Nusantara Servis Utama {runId}`
76. Klik `Activate`
77. Klik `[Activate]` pada dialog `Activate Service Center`
78. Buka form Create Schedule di Maintenance Routine
79. Pilih aset `AC Ruang Server {runId}` saja
80. Klik pemilih `Select service center`
81. Verifikasi opsi `Nusantara Servis Utama {runId}` tampil

### Delete menghilangkan vendor dari pemilih
82. Buka Add-ons > Service Center
83. Ketik Search `Nusantara Servis Utama {runId}`, tekan Enter
84. Klik `⋯` pada baris `Nusantara Servis Utama {runId}`
85. Klik `Delete`
86. Klik `[Delete]` pada dialog `Delete Service Center`
87. Buka form Create Schedule di Maintenance Routine
88. Pilih aset `AC Ruang Server {runId}` saja
89. Klik pemilih `Select service center`
90. Verifikasi opsi `Anugerah Servis Umum {runId}` tampil
91. Verifikasi `Nusantara Servis Utama {runId}` yang sudah dihapus tidak ada di opsi

### Available to induk mencakup aset di descendant-nya
92. Buka form Create Schedule di Maintenance Routine
93. Pilih aset `AC Lobi {runId}` saja
94. Klik pemilih `Select service center`
95. Verifikasi opsi `Lestari LG Service {runId}` (Available to `Kantor Pusat {runId}`, Specialization belum diisi, Brands `LG {runId}`) tampil untuk aset di `Cabang Surabaya {runId}`

### Vendor induk Group dan Category tampil untuk satu aset
96. Buka form Create Schedule di Maintenance Routine
97. Pilih aset `AC Ruang Server {runId}` saja
98. Klik pemilih `Select service center`
99. Verifikasi opsi `Pendingin Pusat Teknik {runId}` (Available to `Kantor Pusat {runId}`, Specialization `Pendingin {runId}`, Brands `Daikin {runId}`) tampil

### Specialization berlaku untuk setiap aset
100. Buka form Create Schedule di Maintenance Routine
101. Pilih aset `AC Ruang Server {runId}` (kategori `AC {runId}`) dan `Genset Gudang {runId}` (kategori `Genset {runId}`), keduanya bermerek `Daikin {runId}`
102. Klik pemilih `Select service center`
103. Verifikasi pesan `No service center covers every asset here. Split the schedule or widen a service center's coverage.` tampil
104. Verifikasi `Pendingin Pusat Teknik {runId}` yang Specialization-nya `Pendingin {runId}` hanya mencakup kategori `AC {runId}` tidak ada di opsi

### Vendor Daikin tampil untuk aset Daikin saja
105. Buka form Create Schedule di Maintenance Routine
106. Pilih aset `AC Aula Semarang {runId}` saja
107. Klik pemilih `Select service center`
108. Verifikasi opsi `Daikin Khusus Semarang {runId}` yang Brands-nya `Daikin {runId}` tampil untuk aset bermerek `Daikin {runId}`

### Schedule AC Daikin dan LG: vendor hanya Daikin tidak muncul dan pesan kosong menyarankan memecah Schedule
109. Buka form Create Schedule di Maintenance Routine
110. Pilih aset `AC Aula Semarang {runId}` (merek `Daikin {runId}`) dan `AC Kantin Semarang {runId}` (merek `LG {runId}`)
111. Klik pemilih `Select service center`
112. Verifikasi pesan `No service center covers every asset here. Split the schedule or widen a service center's coverage.` tampil
113. Verifikasi `Daikin Khusus Semarang {runId}` yang hanya melayani merek `Daikin {runId}` tidak ada di opsi
