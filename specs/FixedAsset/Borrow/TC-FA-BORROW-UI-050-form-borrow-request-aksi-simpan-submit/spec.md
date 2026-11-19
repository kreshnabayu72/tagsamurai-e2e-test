---
id: TC-FA-BORROW-UI-050-form-borrow-request-aksi-simpan-submit
title: "Aksi Save Draft dan Submit di form Borrow Request: saving, dialog Unsaved Changes, toast, dan reaksi gagal"
layer: ui-client
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["D-BRW-11", "DM-BRW-18", "FI-BRW-36", "FI-BRW-37", "FI-BRW-38", "FLD-BRW-11", "V-BRW-19", "§4.3#p2", "EB-FB-3@edit-draft", "EB-FRM-1@form-borrow-request", "EB-FRM-2@form-borrow-request", "EB-TBL-5@submit-borrow-request", "EB-ERR-1@save-draft", "EB-ERR-1@submit-borrow"]
smoke: []
dependsOn: []
trace:
  "D-BRW-11": [11, 12, 19]
  "DM-BRW-18": [11, 19, 21, 22, 24, 27, 79, 80]
  "FI-BRW-36": [69, 70]
  "FI-BRW-37": [75, 76]
  "FI-BRW-38": 29
  "FLD-BRW-11": [69, 72]
  "V-BRW-19": 69
  "§4.3#p2": 3
  "EB-FB-3@edit-draft": [32, 33]
  "EB-FRM-1@form-borrow-request": [40, 41, 43, 44]
  "EB-FRM-2@form-borrow-request": [6, 7, 11, 12, 14, 16, 19, 88, 89, 92, 93, 97, 98, 102, 103]
  "EB-TBL-5@submit-borrow-request": [36, 37]
  "EB-ERR-1@save-draft": [47, 48, 49, 50, 52, 55, 56]
  "EB-ERR-1@submit-borrow": [60, 61, 62, 63, 66, 84, 85]
anchor: [2]
coverage:
  web: automated
---
# Aksi Save Draft dan Submit di form Borrow Request: saving, dialog Unsaved Changes, toast, dan reaksi gagal

## Prerequisites
- Aktor: Aktor Borrow dalam cakupan Group `Head Office`.
- Layar awal: halaman Borrow Request.
- Komponen: Form Borrow Request
- Data:
  - DU-050-1: Borrower `Budi Setiawan`, Position `Staff`, Division `Finance`, aktif, Eligibility `Can borrow`.
  - DU-050-2: Baris aset `Laptop Dell Latitude 5420 - 10`, Asset ID `LPT-2026-0010`, Group `Head Office`, Max Duration `3 days`, Duration `2`, Purpose `Rapat vendor`.
  - DU-050-3: Draft tersimpan milik Borrower DU-050-1 dengan baris DU-050-2, Modified By `Rina W`.
  - DU-050-4: Draft tersimpan milik Borrower DU-050-1 yang memuat aset `Toyota Avanza - 6` dari Group `Branch Surabaya` di luar cakupan Aktor, Modified By `Sari D`. Aktor yang bisa Submit Draft ini adalah `Rina W`, Total Control dengan cakupan Group `Head Office` dan `Branch Surabaya`. Alasan Submit disabled yang diharapkan `Some assets are outside your groups. Ask Rina W to submit.`, dari template `Some assets are outside your groups. Ask [Name] to submit.` dengan Name `Rina W`, Aktor yang bisa Submit Draft itu.
  - DU-050-5: Isian lokal tersimpan di perangkat ini berisi Borrower DU-050-1, baris DU-050-2 dengan Duration `2` dan Purpose `Rapat vendor`, dan Note `Mohon disiapkan sebelum jam delapan`.
  - DU-050-6: Isian Note `Mohon disiapkan sebelum jam delapan`.
- Kondisi:
  - K1: form Borrow Request baru yang belum diisi.
  - K2: form Borrow Request baru berisi Borrower DU-050-1 dan baris aset DU-050-2, valid untuk Save Draft; simpan Draft lambat lalu berhasil.
  - K3: seperti K2; simpan Draft gagal karena error server, lalu simpan berikutnya berhasil.
  - K4: seperti K2; simpan Draft gagal karena koneksi terputus, lalu simpan berikutnya berhasil.
  - K5: seperti K2; Submit gagal karena error server, lalu Submit berikutnya berhasil dan semua aset menunggu approval dalam satu BRW.
  - K6: seperti K2, dengan jumlah baris aset melebihi nilai Bulk Transaction Row Limit yang berlaku.
  - K7: Draft DU-050-3 dibuka tanpa perubahan apa pun.
  - K8: Draft DU-050-4 dibuka oleh Aktor Borrow yang cakupan Group-nya tidak meliputi `Branch Surabaya`.
  - K9: Borrow Request dibuka di perangkat yang sama dengan isian lokal DU-050-5 tersimpan.
  - K10: seperti K2, dengan semua aset menunggu approval dalam satu BRW; Submit gagal karena koneksi terputus tanpa respons, lalu Submit berikutnya berhasil.

## Test Steps

### Form transaksi memakai Cancel dan tanpa Clear Field
1. Tampilkan Form Borrow Request dengan kondisi K1
2. Verifikasi tombol `[Cancel]`, `[Save Draft]`, dan `[Submit]` tampil di form
3. Verifikasi tombol `[Clear Field]` tidak tampil di form

### Form bersih ditutup langsung tanpa dialog
4. Tampilkan Form Borrow Request dengan kondisi K1
5. Klik `[Cancel]`
6. Verifikasi form Borrow Request tidak lagi tampil
7. Verifikasi dialog `Unsaved Changes` tidak tampil

### Form kotor meminta konfirmasi sebelum ditutup
8. Tampilkan Form Borrow Request dengan kondisi K1
9. Isi Note dengan `Mohon disiapkan sebelum jam delapan`
10. Klik `[Cancel]`
11. Verifikasi dialog `Unsaved Changes` tampil dengan teks `You have unsaved changes. Are you sure you want to leave?`
12. Verifikasi dialog memuat tombol `[Cancel]` dan `[Leave]`
13. Klik area di luar dialog `Unsaved Changes`
14. Verifikasi dialog `Unsaved Changes` tetap tampil dan isian Note tetap `Mohon disiapkan sebelum jam delapan`
15. Tekan Esc
16. Verifikasi dialog `Unsaved Changes` tertutup, form tetap terbuka, dan isian Note tetap `Mohon disiapkan sebelum jam delapan`
17. Klik `[Cancel]`
18. Klik `[Leave]` pada dialog `Unsaved Changes`
19. Verifikasi form Borrow Request tidak lagi tampil

### Isian lokal yang tersimpan ditawarkan untuk dipulihkan
20. Tampilkan Form Borrow Request dengan kondisi K9
21. Verifikasi dialog `Restore Unsent Borrow` tampil dengan teks `Restore your unsent borrow?`
22. Verifikasi dialog memuat tombol `[Discard]` dan `[Restore]`
23. Klik `[Restore]`
24. Verifikasi Borrower `Budi Setiawan` dan baris `Laptop Dell Latitude 5420 - 10` dipulihkan di form

### Isian lokal yang dibuang menghasilkan form kosong
25. Tampilkan Form Borrow Request dengan kondisi K9
26. Klik `[Discard]`
27. Verifikasi tombol `[Select Borrower]` tampil karena Borrower belum dipilih

### Draft menampilkan teks bantu bahwa Draft tidak mengunci aset
28. Tampilkan Form Borrow Request dengan kondisi K7
29. Verifikasi teks bantu `Drafts don't reserve assets. Submit to lock them.` tampil pada form

### Simpan Draft tanpa perubahan menampilkan toast netral
30. Tampilkan Form Borrow Request dengan kondisi K7
31. Klik `[Save Draft]`
32. Verifikasi toast `No changes to save.` tampil
33. Verifikasi form Borrow Request tidak lagi tampil

### Submit disabled menyampaikan alasannya
34. Tampilkan Form Borrow Request dengan kondisi K8
35. Arahkan kursor ke tombol `[Submit]`
36. Verifikasi tombol `[Submit]` disabled
37. Verifikasi alasan `Some assets are outside your groups. Ask Rina W to submit.` tersampaikan pada tombol `[Submit]` yang disabled

### Saving menonaktifkan form dan hanya mengirim satu permintaan
38. Tampilkan Form Borrow Request dengan kondisi K2
39. Klik `[Save Draft]`
40. Verifikasi tombol `[Save Draft]` tidak bisa diklik selama permintaan berjalan
41. Verifikasi tombol `[Cancel]` dan field Note disabled selama permintaan berjalan
42. Klik `[Save Draft]` sekali lagi
43. Verifikasi hanya satu permintaan simpan yang dikirim
44. Verifikasi toast `Success, borrow has been saved as draft.` tampil satu kali setelah respons diterima

### Save Draft gagal karena error server dipulihkan dengan mengulang aksi
45. Tampilkan Form Borrow Request dengan kondisi K3
46. Klik `[Save Draft]`
47. Verifikasi toast `Error, failed to save draft.` tampil
48. Verifikasi toast itu hanya berisi pesan dan tidak memuat tombol `[Try Again]`
49. Verifikasi form tetap terbuka dengan Borrower `Budi Setiawan` dan baris `Laptop Dell Latitude 5420 - 10` dipertahankan
50. Verifikasi tombol `[Save Draft]` aktif kembali
51. Klik `[Save Draft]`
52. Verifikasi toast `Success, borrow has been saved as draft.` tampil satu kali

### Save Draft gagal karena koneksi terputus
53. Tampilkan Form Borrow Request dengan kondisi K4
54. Klik `[Save Draft]`
55. Verifikasi toast `Connection problem. Please try again.` tampil
56. Verifikasi form tetap terbuka dengan Borrower `Budi Setiawan` dan baris `Laptop Dell Latitude 5420 - 10` dipertahankan, dan tombol `[Save Draft]` aktif kembali

### Submit gagal karena error server dipulihkan dengan mengulang aksi
57. Tampilkan Form Borrow Request dengan kondisi K5
58. Klik `[Submit]` pada form
59. Klik `[Submit]` pada dialog `Submit Borrow`
60. Verifikasi toast `Error, failed to submit borrow.` tampil
61. Verifikasi toast itu hanya berisi pesan dan tidak memuat tombol `[Try Again]`
62. Verifikasi form tetap terbuka dengan Borrower `Budi Setiawan` dan baris `Laptop Dell Latitude 5420 - 10` dipertahankan
63. Verifikasi tombol `[Submit]` aktif kembali
64. Klik `[Submit]` pada form
65. Klik `[Submit]` pada dialog `Submit Borrow`
66. Verifikasi toast `Success, borrow has been submitted for approval.` tampil satu kali

### Submit melebihi Bulk Transaction Row Limit memunculkan dialog blok
67. Tampilkan Form Borrow Request dengan kondisi K6
68. Klik `[Submit]`
69. Verifikasi dialog `Bulk Transaction Row Limit` tampil dengan tombol `[OK]`
70. Verifikasi dialog `Submit Borrow` tidak tampil
71. Klik `[OK]`
72. Verifikasi Borrower `Budi Setiawan` dan baris `Laptop Dell Latitude 5420 - 10` tetap ada di form

### Save Draft tidak dibatasi Bulk Transaction Row Limit
73. Tampilkan Form Borrow Request dengan kondisi K6
74. Klik `[Save Draft]`
75. Verifikasi toast `Success, borrow has been saved as draft.` tampil
76. Verifikasi dialog `Bulk Transaction Row Limit` tidak tampil

### Isian lokal yang dipulihkan memuat Duration, Purpose, dan Note
77. Tampilkan Form Borrow Request dengan kondisi K9
78. Klik `[Restore]`
79. Verifikasi Duration `2` dan Purpose `Rapat vendor` baris `Laptop Dell Latitude 5420 - 10` dipulihkan di form
80. Verifikasi Note `Mohon disiapkan sebelum jam delapan` dipulihkan di form

### Submit gagal karena koneksi terputus
81. Tampilkan Form Borrow Request dengan kondisi K10
82. Klik `[Submit]` pada form
83. Klik `[Submit]` pada dialog `Submit Borrow`
84. Verifikasi toast `Connection problem. Please try again.` tampil
85. Verifikasi form tetap terbuka dengan Borrower `Budi Setiawan` dan baris `Laptop Dell Latitude 5420 - 10` dipertahankan, dan tombol `[Submit]` aktif kembali

### Form bersih ditutup dengan ✕ langsung tanpa dialog
86. Tampilkan Form Borrow Request dengan kondisi K1
87. Klik `✕` pada form
88. Verifikasi form Borrow Request tidak lagi tampil
89. Verifikasi dialog `Unsaved Changes` tidak tampil

### Form bersih ditutup dengan Esc langsung tanpa dialog
90. Tampilkan Form Borrow Request dengan kondisi K1
91. Tekan Esc
92. Verifikasi form Borrow Request tidak lagi tampil
93. Verifikasi dialog `Unsaved Changes` tidak tampil

### Form kotor ditutup dengan ✕ meminta konfirmasi
94. Tampilkan Form Borrow Request dengan kondisi K1
95. Isi Note dengan `Mohon disiapkan sebelum jam delapan`
96. Klik `✕` pada form
97. Verifikasi dialog `Unsaved Changes` tampil dengan teks `You have unsaved changes. Are you sure you want to leave?`
98. Verifikasi form tetap terbuka dan isian Note tetap `Mohon disiapkan sebelum jam delapan`

### Form kotor ditutup dengan Esc meminta konfirmasi
99. Tampilkan Form Borrow Request dengan kondisi K1
100. Isi Note dengan `Mohon disiapkan sebelum jam delapan`
101. Tekan Esc
102. Verifikasi dialog `Unsaved Changes` tampil dengan teks `You have unsaved changes. Are you sure you want to leave?`
103. Verifikasi form tetap terbuka dan isian Note tetap `Mohon disiapkan sebelum jam delapan`
