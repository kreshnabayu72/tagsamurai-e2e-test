---
id: TC-FA-FASVC-E2E-009-create-service-center-tersimpan
title: "Create Service Center: Tersimpan, Terbaca Ulang, Default Active, dan Urutan A-Z"
layer: ui-e2e
priority: Critical
caseType: Positive
status: ready-for-automation
sourceRules: ["F-FASVC-02.k1", "FASVC-LOGIC-02d", "FASVC-LOGIC-02h", "ST-FASVC-01", "§3#p1", "§9.5#r5", "§9.9#p3", "EB-FB-1@create-service-center", "EB-FRM-1@form-create-service-center", "EB-FRM-5@name-service-center"]
smoke: []
dependsOn: []
trace:
  "F-FASVC-02.k1": [41, 44, 45, 46, 47, 52, 53, 54, 64, 65, 66, 81, 83]
  "FASVC-LOGIC-02d": 49
  "FASVC-LOGIC-02h": 48
  "ST-FASVC-01": 49
  "§3#p1": 43
  "§9.5#r5": 49
  "§9.9#p3": [16, 17, 19, 47, 88, 93, 95, 98, 106, 108]
  "EB-FB-1@create-service-center": 39
  "EB-FRM-1@form-create-service-center": [42, 52]
  "EB-FRM-5@name-service-center": [3, 8, 11]
anchor: []
coverage:
  web: automated
---

# Create Service Center: Tersimpan, Terbaca Ulang, Default Active, dan Urutan A-Z

## Prerequisites
- Aktor: Total Control, dan Group Manager `Rina Palembang {runId}` (ditugaskan pada `Cabang Palembang {runId}`).
- Layar awal: Add-ons > Service Center.
- Data:
  - DU-009-1: Category `Pendingin Udara {runId}` ada di master Category.
  - DU-009-2: Brand `Daikin {runId}` ada di master Brand.
  - DU-009-3: Service Center `Cakra Urut {runId}`, Service type `Routine`, Available to `All groups`, Country `Malaysia`, City `Melaka {runId}`, Company phone `+60 6123456789`, Status `Active`.
  - DU-009-4: Service Center `Zenith Urut {runId}`, Service type `Repair`, Available to `All groups`, Country `Malaysia`, City `Georgetown {runId}`, Company phone `+60 4123456789`, Status `Active`.
  - DU-009-5: 11 Service Center dengan Name `Bengkel Pantai {n} {runId}`, Service type `Routine`, Available to `All groups`, Country `Malaysia`, City `Pantai Barat {n} {runId}`, Company phone `+60 5123456789`, Status `Active`.
  - DU-009-11: 2 Service Center dengan Name `Bengkel Kembar {n} {runId}`, Service type `Routine`, Available to `All groups`, Country `Malaysia`, City `Pantai Barat 1 {runId}` (sama dengan City baris n=1 pada DU-009-5), Company phone `+60 5123456780`, Status `Active`.
  - DU-009-12: Service Center `Bengkel Teluk {runId}`, Service type `Routine`, Available to `All groups`, Country `Malaysia`, City `Teluk Pantai {runId}`, Company phone `+60 5123456781`, Status `Active`.
  - DU-009-13: Service Center `Bengkel Indonesia {runId}`, Service type `Routine`, Available to `All groups`, Country `Indonesia`, City `Pantai Indah {runId}`, Company phone `+62 8123456780`, Status `Active`.
  - DU-009-14: Group `Cabang Medan {runId}` dan Group `Cabang Palembang {runId}`, masing-masing anak dari root pohon Group entitas aktor.
  - DU-009-15: Aktor `Rina Palembang {runId}` dengan Role `Group Manager`, cakupan `Cabang Palembang {runId}`.
  - DU-009-16: Service Center `Bengkel Medan {runId}`, Service type `Routine`, Available to `Cabang Medan {runId}`, Country `Malaysia`, City `Pantai Medan {runId}`, Company phone `+60 5123456782`, Status `Active`.
- Kondisi:
  - Akun `Rina Palembang {runId}` aktif dan kredensialnya disediakan fase 2.

## Test Steps

### Name yang sudah ada ditolak
1. Klik `[+ Service Center]`
2. Isi Name `Cakra Urut {runId}`
3. Verifikasi pesan `Name already exists` tampil di bawah field Name
4. Centang Service type `Routine`
5. Isi City `Melaka {runId}`
6. Isi Company phone dengan Dial Code `+60` dan nomor `6123456789`
7. Klik `[Submit]`
8. Verifikasi dialog `Add Service Center` tetap terbuka dengan pesan `Name already exists` di bawah field Name
9. Klik `✕` pada form, lalu klik `[Leave]` pada dialog Unsaved Changes
10. Ketik Search `Cakra Urut {runId}`, tekan Enter
11. Verifikasi tabel memuat tepat satu baris `Cakra Urut {runId}`

### Saran City dari Service Center yang sudah ada pada Country terpilih
12. Klik `(←)` pada kotak Search
13. Klik `[+ Service Center]`
14. Pilih Country `Malaysia`
15. Ketik City `p`
16. Verifikasi saran City berjumlah `10`
17. Verifikasi saran City tampil berurutan A-Z
18. Ganti isi City dengan `pantai barat 11`
19. Verifikasi saran City memuat `Pantai Barat 11 {runId}`
20. Klik `✕` pada form, lalu klik `[Leave]` pada dialog Unsaved Changes

### Create lengkap tersimpan, tampil di tabel, dan tercatat di Changelog
21. Klik `[+ Service Center]`
22. Isi Name `Prima Urut {runId}`
23. Centang Service type `Routine`
24. Centang Service type `Repair`
25. Pilih Specialization `Pendingin Udara {runId}`
26. Pilih Brands `Daikin {runId}`
27. Pilih Country `Malaysia`
28. Isi Province / State `Johor`
29. Isi City `Johor Bahru {runId}`
30. Isi Postal code `80000`
31. Isi Address line `Jalan Tebrau No. 5`
32. Isi Company phone dengan Dial Code `+60` dan nomor `7123456789`
33. Isi Company email `kontak@primaservis.example`
34. Klik `[+ Contact person]`
35. Isi Contact name `Budi Santoso`
36. Isi Contact email `budi@primaservis.example`
37. Isi Notes `Vendor AC rujukan wilayah Johor`
38. Klik ganda `[Submit]`
39. Verifikasi toast `Success, Prima Urut {runId} has been added.` tampil
40. Ketik Search `Urut {runId}`, tekan Enter
41. Verifikasi tabel memuat baris `Cakra Urut {runId}`, `Prima Urut {runId}`, dan `Zenith Urut {runId}`
42. Verifikasi tabel memuat tepat satu baris `Prima Urut {runId}`
43. Verifikasi urutan baris `Cakra Urut {runId}`, `Prima Urut {runId}`, lalu `Zenith Urut {runId}` sesuai Name A-Z
44. Verifikasi kolom Service Type pada baris `Prima Urut {runId}` memuat `Routine` dan `Repair`
45. Verifikasi kolom Specialization pada baris `Prima Urut {runId}` memuat `Pendingin Udara {runId}`
46. Verifikasi kolom Brands pada baris `Prima Urut {runId}` memuat `Daikin {runId}`
47. Verifikasi kolom City pada baris `Prima Urut {runId}` memuat `Johor Bahru {runId}`
48. Verifikasi kolom Available To pada baris `Prima Urut {runId}` bernilai `All groups`
49. Verifikasi kolom Status pada baris `Prima Urut {runId}` bernilai `Active`
50. Klik `[Changelog]`
51. Ketik Search `Prima Urut {runId}`, tekan Enter
52. Verifikasi tabel Changelog memuat tepat satu baris dengan Action `Created`, Field `Name`, Old Value `—`, dan New Value `Prima Urut {runId}`
53. Verifikasi tabel Changelog memuat baris dengan Action `Created`, Field `Postal code`, dan New Value `80000`
54. Verifikasi tabel Changelog memuat baris dengan Action `Created`, Field `Notes`, dan New Value `Vendor AC rujukan wilayah Johor`
55. Klik ikon close pada modal `Changelog: Service Center`

### Create dengan isian minimal dan field opsional dibiarkan kosong
56. Klik `(←)` pada kotak Search
57. Klik `[+ Service Center]`
58. Isi Name `Minimal Servis {runId}`
59. Centang Service type `Repair`
60. Isi City `Kuala Lumpur {runId}`
61. Isi Company phone dengan Dial Code `+60` dan nomor `3123456789`
62. Klik `[Submit]`
63. Ketik Search `Minimal Servis {runId}`, tekan Enter
64. Verifikasi tabel memuat baris `Minimal Servis {runId}` dengan Service Type `Repair`
65. Verifikasi kolom Specialization pada baris `Minimal Servis {runId}` bernilai `All categories`
66. Verifikasi kolom Brands pada baris `Minimal Servis {runId}` bernilai `All brands`

### Dua Service Center dibuat berurutan dengan Stay on this form
67. Klik `[+ Service Center]`
68. Isi Name `Batch Servis Satu {runId}`
69. Centang Service type `Routine`
70. Isi City `Ipoh {runId}`
71. Isi Company email `satu@batchservis.example`
72. Centang `Stay on this form after submitting`
73. Klik `[Submit]`
74. Isi Name `Batch Servis Dua {runId}`
75. Centang Service type `Repair`
76. Isi City `Taiping {runId}`
77. Isi Company email `dua@batchservis.example`
78. Klik `[Submit]`
79. Klik `✕` pada form (form belum diubah)
80. Ganti isi kotak search dengan `Batch Servis Satu {runId}`, tekan Enter
81. Verifikasi tabel memuat baris `Batch Servis Satu {runId}`
82. Ganti isi kotak search dengan `Batch Servis Dua {runId}`, tekan Enter
83. Verifikasi tabel memuat baris `Batch Servis Dua {runId}`

### Saran City tidak menggandakan nilai City yang sama
84. Klik `(←)` pada kotak Search
85. Klik `[+ Service Center]`
86. Pilih Country `Malaysia`
87. Ketik City `pantai barat 1 {runId}`
88. Verifikasi saran City `Pantai Barat 1 {runId}` tampil tepat satu kali, walaupun dipakai lebih dari satu Service Center
89. Klik `✕` pada form, lalu klik `[Leave]` pada dialog Unsaved Changes

### Saran City mencocokkan substring di tengah nilai dan hanya pada Country terpilih
90. Klik `[+ Service Center]`
91. Pilih Country `Malaysia`
92. Ketik City `pantai {runId}`
93. Verifikasi saran City memuat `Teluk Pantai {runId}`
94. Ganti isi City dengan `pantai indah {runId}`
95. Verifikasi saran City tidak memuat `Pantai Indah {runId}`
96. Pilih Country `Indonesia`
97. Ganti isi City dengan `pantai indah {runId}`
98. Verifikasi saran City memuat `Pantai Indah {runId}`
99. Klik `✕` pada form, lalu klik `[Leave]` pada dialog Unsaved Changes

### Saran City hanya dari Service Center yang terlihat oleh pengguna
100. Masuk sebagai `Rina Palembang {runId}`
101. Buka menu `Add-ons` pada sidebar
102. Klik `Service Center`
103. Klik `[+ Service Center]`
104. Pilih Country `Malaysia`
105. Ketik City `pantai barat 11 {runId}`
106. Verifikasi saran City memuat `Pantai Barat 11 {runId}`
107. Ganti isi City dengan `pantai medan {runId}`
108. Verifikasi saran City tidak memuat `Pantai Medan {runId}`
109. Klik `✕` pada form, lalu klik `[Leave]` pada dialog Unsaved Changes
