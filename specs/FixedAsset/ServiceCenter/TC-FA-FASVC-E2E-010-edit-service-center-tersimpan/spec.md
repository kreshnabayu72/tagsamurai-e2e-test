---
id: TC-FA-FASVC-E2E-010-edit-service-center-tersimpan
title: "Edit Service Center: Nilai Berubah, Bertahan Setelah Muat Ulang, dan Edit Saat Inactive"
layer: ui-e2e
priority: Critical
caseType: Positive
status: ready-for-automation
sourceRules: ["FASVC-LOGIC-05i", "EC-FASVC-38", "F-FASVC-02.k14", "§9.2#p14", "EB-FB-1@edit-service-center", "EB-FB-3@form-edit-service-center", "EB-FRM-1@form-edit-service-center", "EB-ERR-4", "EB-FRM-9", "F-FASVC-02.k1"]
smoke: []
dependsOn: []
trace:
  "FASVC-LOGIC-05i": [95, 96]
  "EC-FASVC-38": [84, 95, 96]
  "F-FASVC-02.k14": [96, 101, 102, 103]
  "§9.2#p14": [95, 96]
  "EB-FB-1@edit-service-center": 63
  "EB-FB-3@form-edit-service-center": [28, 29, 34, 35, 40, 46, 49]
  "EB-FRM-1@form-edit-service-center": [66, 81, 110, 113]
  "EB-ERR-4": [15, 17, 19]
  "EB-FRM-9": [7, 9, 66, 69]
  "F-FASVC-02.k1": [66, 67, 68, 70, 73, 74, 75, 76, 77, 81, 97, 98]
anchor: [2, 11]
coverage:
  web: automated
---

# Edit Service Center: Nilai Berubah, Bertahan Setelah Muat Ulang, dan Edit Saat Inactive

## Prerequisites
- Aktor: Total Control.
- Layar awal: Add-ons > Service Center.
- Data:
  - DU-010-1: Category `Pendingin Udara {runId}` ada di master Category.
  - DU-010-2: Brand `Daikin {runId}` ada di master Brand.
  - DU-010-3: Service Center `Edit Utama {runId}`, Status `Active`, Service type `Routine, Repair`, Available to `All groups`, Specialization `Pendingin Udara {runId}`, Brands `Daikin {runId}`, Country `Malaysia`, Province / State `Selangor`, City `Shah Alam {runId}`, Postal code `40000`, Address line `Jalan Pahlawan No. 8`, Company phone `+60 3555123456`, Company email `utama@editutama.example`, Contact persons `Rahmat Hidayat, +60 3555123400, rahmat@editutama.example, Primary`, Notes `Vendor utama untuk uji Edit`, Attachments `Brosur Edit Utama.pdf`.
  - DU-010-4: Service Center `Servis Dua {runId}`, Status `Active`, Service type `Routine`, Available to `All groups`, Specialization `Pendingin Udara {runId}`, Brands `Daikin {runId}`, Country `Malaysia`, Province / State `Pulau Pinang`, City `Butterworth {runId}`, Postal code `13000`, Address line `Jalan Raja Uda No. 10`, Company phone `+60 4123450001`, Notes `Catatan awal vendor dua`.
  - DU-010-5: Service Center `Servis Tiga {runId}`, Status `Inactive`, Service type `Repair`, Available to `All groups`, Country `Malaysia`, City `Kuantan {runId}`, Company phone `+60 9555000111`, tanpa Specialization, Brands, Province / State, Postal code, Address line, dan Notes.

## Test Steps

### Clear Field pada Edit lalu Save ditolak dan nilai tersimpan tidak berubah
1. Ketik Search `Edit Utama {runId}`, tekan Enter
2. Verifikasi tabel memuat tepat satu baris `Edit Utama {runId}`
3. Klik `⋯` pada baris `Edit Utama {runId}`
4. Klik `Edit`
5. Klik `[Clear Field]`
6. Klik `[Save]`
7. Verifikasi dialog `Edit Service Center` tetap terbuka tanpa toast sukses
8. Klik `✕` pada form, lalu klik `[Leave]` pada dialog Unsaved Changes
9. Verifikasi baris `Edit Utama {runId}` tampil dengan Service Type `Routine` dan `Repair`

### Name yang sama dengan Service Center lain ditolak dan nilai lama tetap
10. Ganti isi kotak search dengan `Servis Dua {runId}`, tekan Enter
11. Verifikasi tabel memuat tepat satu baris `Servis Dua {runId}`
12. Klik `⋯` pada baris `Servis Dua {runId}`
13. Klik `Edit`
14. Ganti isi Name dengan `Edit Utama {runId}`
15. Verifikasi pesan `Name already exists` tampil di bawah field Name
16. Klik `[Save]`
17. Verifikasi dialog `Edit Service Center` tetap terbuka dengan pesan `Name already exists` di bawah field Name, tanpa toast sukses
18. Klik `✕` pada form, lalu klik `[Leave]` pada dialog Unsaved Changes
19. Verifikasi tabel memuat tepat satu baris `Servis Dua {runId}`

### Edit tanpa perubahan nilai tidak menulis log
20. Klik `[Changelog]`
21. Ketik Search `Edit Utama {runId}`, tekan Enter
22. Catat jumlah baris Changelog yang tampil sebagai jumlah awal
23. Klik ikon close pada modal `Changelog: Service Center`
24. Ganti isi kotak search dengan `Edit Utama {runId}`, tekan Enter
25. Klik `⋯` pada baris `Edit Utama {runId}`
26. Klik `Edit`
27. Klik `[Save]`
28. Verifikasi toast `No changes to save.` tampil
29. Verifikasi dialog `Edit Service Center` tertutup
30. Klik `⋯` pada baris `Edit Utama {runId}`
31. Klik `Edit`
32. Ganti isi Name dengan `EDIT UTAMA {runId}`
33. Klik `[Save]`
34. Verifikasi toast `No changes to save.` tampil
35. Verifikasi kolom Name pada baris `Edit Utama {runId}` tetap bertuliskan `Edit Utama {runId}` dengan kapitalisasi semula
36. Klik `⋯` pada baris `Edit Utama {runId}`
37. Klik `Edit`
38. Ganti isi Name dengan `Edit Utama {runId}` diikuti satu spasi
39. Klik `[Save]`
40. Verifikasi toast `No changes to save.` tampil
41. Klik `⋯` pada baris `Edit Utama {runId}`
42. Klik `Edit`
43. Ganti isi Name dengan `Perubahan Sementara {runId}`
44. Ganti isi Name dengan `Edit Utama {runId}`
45. Klik `[Save]`
46. Verifikasi toast `No changes to save.` tampil
47. Klik `[Changelog]`
48. Ketik Search `Edit Utama {runId}`, tekan Enter
49. Verifikasi jumlah baris Changelog sama dengan jumlah awal
50. Klik ikon close pada modal `Changelog: Service Center`

### Edit nilai baru tersimpan dan bertahan setelah muat ulang
51. Ganti isi kotak search dengan `Servis Dua {runId}`, tekan Enter
52. Klik `⋯` pada baris `Servis Dua {runId}`
53. Klik `Edit`
54. Ganti isi Name dengan `Servis Dua Baru {runId}`
55. Lepas pilihan Specialization `Pendingin Udara {runId}`
56. Lepas pilihan Brands `Daikin {runId}`
57. Kosongkan Province / State
58. Kosongkan Postal code
59. Kosongkan Address line
60. Kosongkan Notes
61. Klik `[Save]`
62. Klik `[Save]` pada dialog `Widen Coverage`
63. Verifikasi toast `Success, Servis Dua Baru {runId} has been updated.` tampil
64. Muat ulang halaman
65. Ganti isi kotak search dengan `Servis Dua Baru {runId}`, tekan Enter
66. Verifikasi tabel memuat tepat satu baris `Servis Dua Baru {runId}`
67. Verifikasi kolom Specialization pada baris `Servis Dua Baru {runId}` bernilai `All categories`
68. Verifikasi kolom Brands pada baris `Servis Dua Baru {runId}` bernilai `All brands`
69. Verifikasi kolom Service Type pada baris `Servis Dua Baru {runId}` tetap `Routine`
70. Verifikasi kolom City pada baris `Servis Dua Baru {runId}` memuat `Butterworth {runId}`
71. Klik `⋯` pada baris `Servis Dua Baru {runId}`
72. Klik `Edit`
73. Verifikasi field Name berisi `Servis Dua Baru {runId}`
74. Verifikasi field Province / State kosong
75. Verifikasi field Postal code kosong
76. Verifikasi field Address line kosong
77. Verifikasi field Notes kosong
78. Klik `✕` pada form (form belum diubah)
79. Klik `[Changelog]`
80. Ketik Search `Servis Dua {runId}`, tekan Enter
81. Verifikasi tabel Changelog memuat tepat satu baris dengan Action `Updated`, Field `Name`, Old Value `Servis Dua {runId}`, dan New Value `Servis Dua Baru {runId}`
82. Klik ikon close pada modal `Changelog: Service Center`

### Edit pada Service Center Inactive diizinkan dan status tidak berubah
83. Ganti isi kotak search dengan `Servis Tiga {runId}`, tekan Enter
84. Verifikasi baris `Servis Tiga {runId}` tampil dengan Status `Inactive`
85. Klik `⋯` pada baris `Servis Tiga {runId}`
86. Klik `Edit`
87. Ganti isi Name dengan `SERVIS TIGA {runId}`
88. Pilih Specialization `Pendingin Udara {runId}`
89. Pilih Brands `Daikin {runId}`
90. Isi Province / State `Penang`
91. Isi Postal code `11900`
92. Isi Address line `Jalan Bayan Lepas No. 3`
93. Isi Notes `Vendor cadangan wilayah utara`
94. Klik `[Save]`
95. Verifikasi kolom Name pada baris hasil Search `Servis Tiga {runId}` bertuliskan `SERVIS TIGA {runId}`
96. Verifikasi kolom Status pada baris `SERVIS TIGA {runId}` tetap `Inactive`
97. Verifikasi kolom Specialization pada baris `SERVIS TIGA {runId}` memuat `Pendingin Udara {runId}`
98. Verifikasi kolom Brands pada baris `SERVIS TIGA {runId}` memuat `Daikin {runId}`
99. Klik `[Changelog]`
100. Ketik Search `Servis Tiga {runId}`, tekan Enter
101. Verifikasi tabel Changelog memuat baris dengan Action `Updated`, Field `Name`, Old Value `Servis Tiga {runId}`, dan New Value `SERVIS TIGA {runId}`
102. Verifikasi tabel Changelog memuat baris dengan Action `Updated`, Field `Specialization`, dan New Value `Pendingin Udara {runId}`
103. Verifikasi tabel Changelog memuat baris dengan Action `Updated`, Field `Brands`, dan New Value `Daikin {runId}`

### Klik ganda Save pada Edit menulis satu entri Changelog
104. Klik ikon close pada modal `Changelog: Service Center`
105. Ganti isi kotak search dengan `Edit Utama {runId}`, tekan Enter
106. Klik `⋯` pada baris `Edit Utama {runId}`
107. Klik `Edit`
108. Ganti isi City dengan `Petaling Jaya {runId}`
109. Klik ganda `[Save]`
110. Verifikasi toast `Success, Edit Utama {runId} has been updated.` tampil
111. Klik `[Changelog]`
112. Ketik Search `Edit Utama {runId}`, tekan Enter
113. Verifikasi tabel Changelog memuat tepat satu baris dengan Action `Updated`, Field `City`, Old Value `Shah Alam {runId}`, dan New Value `Petaling Jaya {runId}`
