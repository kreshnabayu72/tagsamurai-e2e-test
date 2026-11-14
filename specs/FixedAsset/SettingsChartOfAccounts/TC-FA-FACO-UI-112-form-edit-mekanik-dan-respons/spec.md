---
id: TC-FA-FACO-UI-112-form-edit-mekanik-dan-respons
title: "Form Edit Account: Saving, menutup form, Clear Field, No-Op, dan reaksi atas respons server"
layer: ui-client
priority: Medium
caseType: Positive
status: draft
sourceRules: [D-16, R-02, R-03, T-02, T-03, T-12, §4.1.2#p4, §4.2f#b3, §7.3#b1, §7.3#b4, §[F-FACO-02] Edit Account#r8, §[F-FACO-02] Edit Account#r9, §[F-FACO-02] Edit Account#r12, §9.4.2#r7, §9.4.2#r32, EB-FB-1@edit-account, EB-FB-3@form-edit-account, EB-FRM-1@form-edit-account, EB-FRM-2@form-edit-account, EB-FRM-3@form-edit-account, EB-ERR-1@edit-account]
smoke: []
dependsOn: []
trace:
  D-16: [52, 53, 54, 55]
  R-02: [8, 9]
  R-03: [27, 41]
  T-02: [4, 8]
  T-03: [27, 28, 30]
  T-12: 45
  §4.1.2#p4: [63, 65, 66, 67, 71, 72, 73, 76, 77, 78, 80]
  §4.2f#b3: [90, 91, 99, 102]
  §7.3#b1: [9, 10, 15, 16, 17, 115, 116]
  §7.3#b4: [45, 46, 47]
  §[F-FACO-02] Edit Account#r8: 29
  §[F-FACO-02] Edit Account#r9: 27
  §[F-FACO-02] Edit Account#r12: [57, 58, 60, 61]
  §9.4.2#r7: 27
  §9.4.2#r32: 110
  EB-FB-1@edit-account: [4, 8]
  EB-FB-3@form-edit-account: [27, 29, 30]
  EB-FRM-1@form-edit-account: [106, 107, 108, 109, 110]
  EB-FRM-2@form-edit-account: [34, 36, 83, 86, 90, 91, 93, 95, 97, 99, 102]
  EB-FRM-3@form-edit-account: [63, 65, 66, 67, 68, 69]
  EB-ERR-1@edit-account: [8, 9, 10, 11, 15, 16, 17, 18, 22, 24, 114, 115, 116, 117]
anchor: []
coverage:
  web: automated
---

# Form Edit Account: Saving, menutup form, Clear Field, No-Op, dan reaksi atas respons server

## Prerequisites
- Aktor: Total Control.
- Layar awal: Modal Edit Account pada Settings > Accounting > Chart of Accounts.
- Komponen: Modal Edit Account.
- Data:
  - DU-112-1: akun dengan Account Code `5-6001`, Account Name `Depreciation Expense – Admin`, Account Function `Depreciation Expense`, Used By `0`, Last Used in Journal `—`.
  - DU-112-2: akun dengan Account Code `1-1001`, Account Name `Fixed Assets – Equipment`, Account Function `Asset Cost`, Used By `3`, Last Used in Journal `Oct 2026`.
- Kondisi:
  - K1: form Edit Account dibuka untuk akun DU-112-1, yang tidak terkunci, dan penyimpanan akun berhasil bila `[Save]` dikirim.
  - K2: seperti K1, dan penyimpanan gagal karena error server.
  - K3: seperti K1, dan penyimpanan gagal karena timeout.
  - K4: seperti K1, dan server menjawab permintaan tanpa perubahan nilai dengan berhasil tanpa isi respons (No-Op).
  - K5: seperti K1, dan akun sudah dihapus user lain saat `[Save]` dikirim.
  - K6: seperti K1, dan status kunci berubah antara form dibuka dan `[Save]`: akun mulai dipakai Asset Class sehingga Account Function terkunci, sedangkan submit mengubah Account Function.
  - K7: seperti K1, dan penyimpanan gagal karena error server pada percobaan pertama, lalu berhasil pada percobaan berikutnya.
  - K8: form Edit Account dibuka untuk akun DU-112-2, yang terkunci karena Last Used in Journal terisi.
  - K9: seperti K1, dan penyimpanan berjalan lambat sehingga respons belum diterima.
  - K10: seperti K1, dan penyimpanan gagal karena koneksi terputus.

## Test Steps

### Save dengan nilai baru menampilkan toast sukses
1. Tampilkan Modal Edit Account dengan kondisi K1
2. Ganti isi field `Account Name` dengan `Depreciation Expense – Admin Revisi {runId}`
3. Klik `[Save]`
4. Verifikasi toast `Success, account has been updated.` tampil sesudah `[Save]` pada form Edit

### Error server menampilkan toast gagal tanpa menutup form Edit
5. Tampilkan Modal Edit Account dengan kondisi K2
6. Ganti isi field `Account Name` dengan `Depreciation Expense – Admin Gagal`
7. Klik `[Save]`
8. Verifikasi toast `Error, failed to update account.` tampil sesudah `[Save]` pada form Edit
9. Verifikasi modal Edit Account tetap terbuka sesudah toast gagal tampil
10. Verifikasi field `Account Name` masih berisi `Depreciation Expense – Admin Gagal` sesudah toast gagal pada form Edit
11. Verifikasi tombol `[Save]` dapat diklik lagi sesudah toast gagal pada form Edit

### Timeout menampilkan toast koneksi tanpa menutup form Edit
12. Tampilkan Modal Edit Account dengan kondisi K3
13. Ganti isi field `Account Name` dengan `Depreciation Expense – Admin Putus`
14. Klik `[Save]`
15. Verifikasi toast `Connection problem. Please try again.` tampil sesudah `[Save]` pada form Edit timeout
16. Verifikasi modal Edit Account tetap terbuka sesudah timeout
17. Verifikasi field `Account Name` masih berisi `Depreciation Expense – Admin Putus` sesudah timeout pada form Edit
18. Verifikasi tombol `[Save]` dapat diklik lagi sesudah timeout pada form Edit

### Save ulang sesudah penyimpanan pulih berhasil
19. Tampilkan Modal Edit Account dengan kondisi K7
20. Ganti isi field `Account Name` dengan `Depreciation Expense – Admin Pulih {runId}`
21. Klik `[Save]`
22. Verifikasi toast `Error, failed to update account.` tampil sesudah percobaan pertama pada form Edit
23. Klik `[Save]` sekali lagi
24. Verifikasi toast `Success, account has been updated.` tampil sesudah Save ulang pada form Edit

### Save tanpa perubahan adalah No-Op
25. Tampilkan Modal Edit Account dengan kondisi K4
26. Klik `[Save]` tanpa mengubah isi field apa pun
27. Verifikasi toast `No changes to save.` tampil sesudah `[Save]` tanpa perubahan
28. Verifikasi toast tersebut netral dengan severity Info, bukan toast sukses atau gagal
29. Verifikasi modal Edit Account tertutup sesudah `[Save]` tanpa perubahan
30. Verifikasi toast `Success, account has been updated.` tidak tampil sesudah `[Save]` tanpa perubahan

### Nilai diubah lalu dikembalikan dianggap bersih
31. Tampilkan Modal Edit Account dengan kondisi K1
32. Ganti isi field `Account Name` dengan `Depreciation Expense – Admin Sementara`
33. Ganti isi field `Account Name` dengan `Depreciation Expense – Admin` sehingga sama dengan nilai tersimpan
34. Verifikasi field `Account Name` berisi `Depreciation Expense – Admin` kembali sama dengan nilai tersimpan pada form Edit
35. Klik `✕` pada form yang nilainya kembali sama dengan nilai tersimpan
36. Verifikasi modal Edit Account tertutup langsung tanpa dialog Unsaved Changes karena nilai sama dengan tersimpan

### Nilai diubah lalu dikembalikan menghasilkan No-Op saat Save
37. Tampilkan Modal Edit Account dengan kondisi K4
38. Ganti isi field `Account Name` dengan `Depreciation Expense – Admin Sementara`
39. Ganti isi field `Account Name` dengan `Depreciation Expense – Admin` sehingga sama dengan nilai tersimpan
40. Klik `[Save]` pada form yang nilainya kembali sama dengan nilai tersimpan
41. Verifikasi toast `No changes to save.` tampil karena nilai akhir sama dengan nilai tersimpan

### Akun sudah dihapus user lain saat Save
42. Tampilkan Modal Edit Account dengan kondisi K5
43. Ganti isi field `Account Name` dengan `Depreciation Expense – Admin Terhapus`
44. Klik `[Save]`
45. Verifikasi toast netral `This account is no longer available.` tampil sesudah `[Save]` pada akun yang sudah terhapus
46. Verifikasi modal Edit Account tertutup sesudah akun dinyatakan tidak tersedia
47. Verifikasi toast `Error, failed to update account.` tidak tampil untuk akun yang sudah terhapus

### Status kunci berubah antara form dibuka dan Save
48. Tampilkan Modal Edit Account dengan kondisi K6
49. Ganti isi field `Account Function` dengan `Asset Cost`
50. Ganti isi field `Account Name` dengan `Depreciation Expense – Admin Terkunci`
51. Klik `[Save]`
52. Verifikasi dialog `Cannot Save Account` tampil
53. Verifikasi dialog memuat kalimat `This account has been locked for editing by another action. The form has been reloaded with the latest lock status.`
54. Verifikasi dialog memuat satu butir daftar bullet untuk satu akun
55. Verifikasi dialog memiliki tombol `[OK]`
56. Klik `[OK]` pada dialog `Cannot Save Account`
57. Verifikasi modal Edit Account tetap terbuka sesudah dialog ditutup
58. Verifikasi field `Account Function` kembali ke nilai tersimpan `Depreciation Expense` dan Disabled sesudah status kunci dimuat ulang
59. Arahkan kursor ke field `Account Function` yang Disabled sesudah status kunci dimuat ulang
60. Verifikasi tooltip alasan tampil pada field `Account Function` yang Disabled sesudah status kunci dimuat ulang
61. Verifikasi field `Account Name` masih berisi `Depreciation Expense – Admin Terkunci` sesudah status kunci dimuat ulang

### Clear Field pada akun tidak terkunci mengosongkan field
62. Tampilkan Modal Edit Account dengan kondisi K1
63. Verifikasi form Edit terisi nilai tersimpan: Account Code `5-6001`, Account Name `Depreciation Expense – Admin`, dan Account Function `Depreciation Expense`
64. Klik `[Clear Field]` pada form Edit akun yang tidak terkunci
65. Verifikasi field `Account Code` dikosongkan oleh `[Clear Field]` pada form Edit
66. Verifikasi field `Account Name` dikosongkan oleh `[Clear Field]` pada form Edit
67. Verifikasi field `Account Function` menampilkan `Select account function` sesudah `[Clear Field]`
68. Verifikasi field dikosongkan oleh `[Clear Field]` alih-alih dikembalikan ke nilai tersimpan
69. Verifikasi tidak ada dialog konfirmasi yang tampil sesudah `[Clear Field]` pada form Edit
70. Klik `[Save]`
71. Verifikasi caption `Account code must not be empty` tampil di bawah field `Account Code` sesudah Clear Field lalu Save
72. Verifikasi caption `Account name must not be empty` tampil di bawah field `Account Name` sesudah Clear Field lalu Save
73. Verifikasi caption `Account function must not be empty` tampil di bawah field `Account Function` sesudah Clear Field lalu Save

### Clear Field pada akun terkunci hanya mengosongkan field yang tidak terkunci
74. Tampilkan Modal Edit Account dengan kondisi K8
75. Klik `[Clear Field]` pada form Edit akun yang terkunci
76. Verifikasi field `Account Code` tetap Disabled dengan nilai tersimpan `1-1001` sesudah `[Clear Field]`
77. Verifikasi field `Account Function` tetap Disabled dengan nilai tersimpan `Asset Cost` sesudah `[Clear Field]`
78. Verifikasi field `Account Name` dikosongkan oleh `[Clear Field]` pada akun yang terkunci
79. Klik `[Save]`
80. Verifikasi caption `Account name must not be empty` tampil di bawah field `Account Name` pada akun yang terkunci

### Menutup form Edit yang belum diubah
81. Tampilkan Modal Edit Account dengan kondisi K1
82. Klik `✕` pada form Edit yang belum diubah
83. Verifikasi modal Edit Account tertutup langsung tanpa dialog Unsaved Changes sesudah `✕` diklik pada form Edit yang bersih
84. Tampilkan Modal Edit Account dengan kondisi K1
85. Tekan `Esc` pada form Edit yang belum diubah
86. Verifikasi modal Edit Account tertutup langsung tanpa dialog Unsaved Changes sesudah `Esc` ditekan pada form Edit yang bersih

### Menutup form Edit yang sudah diubah memunculkan Unsaved Changes
87. Tampilkan Modal Edit Account dengan kondisi K1
88. Ganti isi field `Account Name` dengan `Depreciation Expense – Admin Draf`
89. Klik `✕` pada form Edit yang sudah diubah
90. Verifikasi dialog `Unsaved Changes` pada form Edit tampil dengan pesan `You have unsaved changes. Are you sure you want to leave?`
91. Verifikasi dialog Unsaved Changes pada form Edit memiliki tombol `[Leave]` dan `[Cancel]`
92. Tekan `Esc`
93. Verifikasi dialog Unsaved Changes pada form Edit tertutup dan modal Edit Account tetap terbuka dengan Account Name `Depreciation Expense – Admin Draf`, sama seperti `[Cancel]`
94. Klik area backdrop di luar modal Edit Account
95. Verifikasi modal Edit Account tetap terbuka dengan Account Name `Depreciation Expense – Admin Draf` tanpa dialog Unsaved Changes sesudah backdrop diklik
96. Tekan `Esc` pada form Edit yang sudah diubah
97. Verifikasi dialog Unsaved Changes pada form Edit tampil sesudah `Esc` ditekan pada form yang sudah diubah
98. Klik `[Cancel]` pada dialog Unsaved Changes
99. Verifikasi dialog Unsaved Changes pada form Edit tertutup dan modal Edit Account tetap terbuka dengan Account Name `Depreciation Expense – Admin Draf` sesudah `[Cancel]`
100. Klik `✕` pada form Edit yang sudah diubah
101. Klik `[Leave]` pada dialog Unsaved Changes
102. Verifikasi modal Edit Account tertutup tanpa menyimpan sesudah `[Leave]`

### Saving pada form Edit mencegah klik ganda
103. Tampilkan Modal Edit Account dengan kondisi K9
104. Ganti isi field `Account Name` dengan `Depreciation Expense – Admin Ganda`
105. Klik ganda `[Save]`
106. Verifikasi tombol `[Save]` tidak bisa diklik selama permintaan berjalan pada form Edit
107. Verifikasi tombol `[Clear Field]` tidak bisa diklik selama permintaan berjalan pada form Edit
108. Verifikasi tombol `✕` tidak bisa diklik selama permintaan berjalan pada form Edit
109. Verifikasi field `Account Code`, `Account Name`, dan `Account Function` tidak bisa diubah selama permintaan berjalan pada form Edit
110. Verifikasi hanya satu permintaan Edit Account yang dikirim sesudah klik ganda

### Koneksi terputus menampilkan toast koneksi tanpa menutup form Edit
111. Tampilkan Modal Edit Account dengan kondisi K10
112. Ganti isi field `Account Name` dengan `Depreciation Expense – Admin Koneksi Putus`
113. Klik `[Save]`
114. Verifikasi toast `Connection problem. Please try again.` tampil sesudah `[Save]` pada form Edit saat koneksi terputus
115. Verifikasi modal Edit Account tetap terbuka sesudah koneksi terputus
116. Verifikasi field `Account Name` masih berisi `Depreciation Expense – Admin Koneksi Putus` sesudah koneksi terputus pada form Edit
117. Verifikasi tombol `[Save]` dapat diklik lagi sesudah koneksi terputus pada form Edit
