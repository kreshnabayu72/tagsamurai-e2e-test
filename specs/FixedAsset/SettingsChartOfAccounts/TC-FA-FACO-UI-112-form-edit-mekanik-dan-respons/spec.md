---
id: TC-FA-FACO-UI-112-form-edit-mekanik-dan-respons
title: "Form Edit Account: Saving, menutup form, Clear Field, No-Op, dan reaksi atas respons server"
layer: ui-client
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: [D-16, R-02, R-03, T-02, T-03, T-12, §4.1.2#p4, §4.2f#b3, §7.3#b1, §7.3#b4, "§[F-FACO-02] Edit Account#r10", "§[F-FACO-02] Edit Account#r11", "§[F-FACO-02] Edit Account#r14", §9.4.2#r7, §9.4.2#r32, EB-FB-1@edit-account, EB-FB-3@form-edit-account, EB-FRM-1@form-edit-account, EB-FRM-2@form-edit-account, EB-FRM-3@form-edit-account, EB-ERR-1@edit-account]
smoke: []
dependsOn: []
trace:
  D-16: [53, 54, 55, 56]
  R-02: [8, 9, 15, 16, 17]
  R-03: [28, 42]
  T-02: [4, 8]
  T-03: [28, 29, 31]
  T-12: 46
  §4.1.2#p4: [64, 66, 67, 68, 72, 73, 74, 77, 78, 79, 81]
  §4.2f#b3: [91, 92, 100, 103]
  §7.3#b1: [9, 10, 15, 17, 18, 116, 117]
  §7.3#b4: [46, 47, 48]
  §[F-FACO-02] Edit Account#r10: 30
  §[F-FACO-02] Edit Account#r11: 28
  §[F-FACO-02] Edit Account#r14: [58, 59, 61, 62]
  §9.4.2#r7: 28
  §9.4.2#r32: 111
  EB-FB-1@edit-account: [4, 8]
  EB-FB-3@form-edit-account: [28, 30, 31]
  EB-FRM-1@form-edit-account: [107, 108, 109, 110, 111]
  EB-FRM-2@form-edit-account: [35, 37, 84, 87, 91, 92, 94, 96, 98, 100, 103]
  EB-FRM-3@form-edit-account: [64, 66, 67, 68, 69, 70]
  EB-ERR-1@edit-account: [8, 9, 10, 11, 15, 16, 17, 18, 19, 23, 25, 115, 116, 117, 118]
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
  - K4: seperti K1, dan server menjawab permintaan tanpa perubahan nilai dengan `200 OK` (No-Op).
  - K5: seperti K1, dan akun sudah dihapus user lain saat `[Save]` dikirim.
  - K6: seperti K1, dan status kunci berubah antara form dibuka dan `[Save]`: akun mulai dipakai Asset Class sehingga Used By bernilai `1` dan Account Function terkunci, sedangkan submit mengubah Account Function.
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
16. Verifikasi toast `Error, failed to update account.` tidak tampil sesudah timeout pada form Edit
17. Verifikasi modal Edit Account tetap terbuka sesudah timeout
18. Verifikasi field `Account Name` masih berisi `Depreciation Expense – Admin Putus` sesudah timeout pada form Edit
19. Verifikasi tombol `[Save]` dapat diklik lagi sesudah timeout pada form Edit

### Save ulang sesudah penyimpanan pulih berhasil
20. Tampilkan Modal Edit Account dengan kondisi K7
21. Ganti isi field `Account Name` dengan `Depreciation Expense – Admin Pulih {runId}`
22. Klik `[Save]`
23. Verifikasi toast `Error, failed to update account.` tampil sesudah percobaan pertama pada form Edit
24. Klik `[Save]` sekali lagi
25. Verifikasi toast `Success, account has been updated.` tampil sesudah Save ulang pada form Edit

### Save tanpa perubahan adalah No-Op
26. Tampilkan Modal Edit Account dengan kondisi K4
27. Klik `[Save]` tanpa mengubah isi field apa pun
28. Verifikasi toast `No changes to save.` tampil sesudah `[Save]` tanpa perubahan
29. Verifikasi toast tersebut netral dengan severity Info, bukan toast sukses atau gagal
30. Verifikasi modal Edit Account tertutup sesudah `[Save]` tanpa perubahan
31. Verifikasi toast `Success, account has been updated.` tidak tampil sesudah `[Save]` tanpa perubahan

### Nilai diubah lalu dikembalikan dianggap bersih
32. Tampilkan Modal Edit Account dengan kondisi K1
33. Ganti isi field `Account Name` dengan `Depreciation Expense – Admin Sementara`
34. Ganti isi field `Account Name` dengan `Depreciation Expense – Admin` sehingga sama dengan nilai tersimpan
35. Verifikasi field `Account Name` berisi `Depreciation Expense – Admin` kembali sama dengan nilai tersimpan pada form Edit
36. Klik `✕` pada form yang nilainya kembali sama dengan nilai tersimpan
37. Verifikasi modal Edit Account tertutup langsung tanpa dialog Unsaved Changes karena nilai sama dengan tersimpan

### Nilai diubah lalu dikembalikan menghasilkan No-Op saat Save
38. Tampilkan Modal Edit Account dengan kondisi K4
39. Ganti isi field `Account Name` dengan `Depreciation Expense – Admin Sementara`
40. Ganti isi field `Account Name` dengan `Depreciation Expense – Admin` sehingga sama dengan nilai tersimpan
41. Klik `[Save]` pada form yang nilainya kembali sama dengan nilai tersimpan
42. Verifikasi toast `No changes to save.` tampil karena nilai akhir sama dengan nilai tersimpan

### Akun sudah dihapus user lain saat Save
43. Tampilkan Modal Edit Account dengan kondisi K5
44. Ganti isi field `Account Name` dengan `Depreciation Expense – Admin Terhapus`
45. Klik `[Save]`
46. Verifikasi toast netral `This account is no longer available.` tampil sesudah `[Save]` pada akun yang sudah terhapus
47. Verifikasi modal Edit Account tertutup sesudah akun dinyatakan tidak tersedia
48. Verifikasi toast `Error, failed to update account.` tidak tampil untuk akun yang sudah terhapus

### Status kunci berubah antara form dibuka dan Save
49. Tampilkan Modal Edit Account dengan kondisi K6
50. Ganti isi field `Account Function` dengan `Asset Cost`
51. Ganti isi field `Account Name` dengan `Depreciation Expense – Admin Terkunci`
52. Klik `[Save]`
53. Verifikasi dialog `Cannot Save Account` tampil
54. Verifikasi dialog memuat kalimat `This account has been locked for editing by another action. The form has been reloaded with the latest lock status.`
55. Verifikasi dialog memuat satu butir daftar bullet untuk satu akun
56. Verifikasi dialog memiliki tombol `[OK]`
57. Klik `[OK]` pada dialog `Cannot Save Account`
58. Verifikasi modal Edit Account tetap terbuka sesudah dialog ditutup
59. Verifikasi field `Account Function` kembali ke nilai tersimpan `Depreciation Expense` dan Disabled sesudah status kunci dimuat ulang
60. Arahkan kursor ke field `Account Function` yang Disabled sesudah status kunci dimuat ulang
61. Verifikasi alasan `Account Function can't be changed because this account is used by 1 Asset Class.` tersampaikan pada field `Account Function` yang Disabled sesudah status kunci dimuat ulang
62. Verifikasi field `Account Name` masih berisi `Depreciation Expense – Admin Terkunci` sesudah status kunci dimuat ulang

### Clear Field pada akun tidak terkunci mengosongkan field
63. Tampilkan Modal Edit Account dengan kondisi K1
64. Verifikasi form Edit terisi nilai tersimpan: Account Code `5-6001`, Account Name `Depreciation Expense – Admin`, dan Account Function `Depreciation Expense`
65. Klik `[Clear Field]` pada form Edit akun yang tidak terkunci
66. Verifikasi field `Account Code` dikosongkan oleh `[Clear Field]` pada form Edit
67. Verifikasi field `Account Name` dikosongkan oleh `[Clear Field]` pada form Edit
68. Verifikasi field `Account Function` menampilkan `Select account function` sesudah `[Clear Field]`
69. Verifikasi field dikosongkan oleh `[Clear Field]` alih-alih dikembalikan ke nilai tersimpan
70. Verifikasi tidak ada dialog konfirmasi yang tampil sesudah `[Clear Field]` pada form Edit
71. Klik `[Save]`
72. Verifikasi caption `Account code must not be empty` tampil di bawah field `Account Code` sesudah Clear Field lalu Save
73. Verifikasi caption `Account name must not be empty` tampil di bawah field `Account Name` sesudah Clear Field lalu Save
74. Verifikasi caption `Account function must not be empty` tampil di bawah field `Account Function` sesudah Clear Field lalu Save

### Clear Field pada akun terkunci hanya mengosongkan field yang tidak terkunci
75. Tampilkan Modal Edit Account dengan kondisi K8
76. Klik `[Clear Field]` pada form Edit akun yang terkunci
77. Verifikasi field `Account Code` tetap Disabled dengan nilai tersimpan `1-1001` sesudah `[Clear Field]`
78. Verifikasi field `Account Function` tetap Disabled dengan nilai tersimpan `Asset Cost` sesudah `[Clear Field]`
79. Verifikasi field `Account Name` dikosongkan oleh `[Clear Field]` pada akun yang terkunci
80. Klik `[Save]`
81. Verifikasi caption `Account name must not be empty` tampil di bawah field `Account Name` pada akun yang terkunci

### Menutup form Edit yang belum diubah
82. Tampilkan Modal Edit Account dengan kondisi K1
83. Klik `✕` pada form Edit yang belum diubah
84. Verifikasi modal Edit Account tertutup langsung tanpa dialog Unsaved Changes sesudah `✕` diklik pada form Edit yang bersih
85. Tampilkan Modal Edit Account dengan kondisi K1
86. Tekan `Esc` pada form Edit yang belum diubah
87. Verifikasi modal Edit Account tertutup langsung tanpa dialog Unsaved Changes sesudah `Esc` ditekan pada form Edit yang bersih

### Menutup form Edit yang sudah diubah memunculkan Unsaved Changes
88. Tampilkan Modal Edit Account dengan kondisi K1
89. Ganti isi field `Account Name` dengan `Depreciation Expense – Admin Draf`
90. Klik `✕` pada form Edit yang sudah diubah
91. Verifikasi dialog `Unsaved Changes` pada form Edit tampil dengan pesan `You have unsaved changes. Are you sure you want to leave?`
92. Verifikasi dialog Unsaved Changes pada form Edit memiliki tombol `[Leave]` dan `[Cancel]`
93. Tekan `Esc`
94. Verifikasi dialog Unsaved Changes pada form Edit tertutup dan modal Edit Account tetap terbuka dengan Account Name `Depreciation Expense – Admin Draf`, sama seperti `[Cancel]`
95. Klik area backdrop di luar modal Edit Account
96. Verifikasi modal Edit Account tetap terbuka dengan Account Name `Depreciation Expense – Admin Draf` tanpa dialog Unsaved Changes sesudah backdrop diklik
97. Tekan `Esc` pada form Edit yang sudah diubah
98. Verifikasi dialog Unsaved Changes pada form Edit tampil sesudah `Esc` ditekan pada form yang sudah diubah
99. Klik `[Cancel]` pada dialog Unsaved Changes
100. Verifikasi dialog Unsaved Changes pada form Edit tertutup dan modal Edit Account tetap terbuka dengan Account Name `Depreciation Expense – Admin Draf` sesudah `[Cancel]`
101. Klik `✕` pada form Edit yang sudah diubah
102. Klik `[Leave]` pada dialog Unsaved Changes
103. Verifikasi modal Edit Account tertutup tanpa menyimpan sesudah `[Leave]`

### Saving pada form Edit mencegah klik ganda
104. Tampilkan Modal Edit Account dengan kondisi K9
105. Ganti isi field `Account Name` dengan `Depreciation Expense – Admin Ganda`
106. Klik ganda `[Save]`
107. Verifikasi tombol `[Save]` tidak bisa diklik selama permintaan berjalan pada form Edit
108. Verifikasi tombol `[Clear Field]` tidak bisa diklik selama permintaan berjalan pada form Edit
109. Verifikasi tombol `✕` tidak bisa diklik selama permintaan berjalan pada form Edit
110. Verifikasi field `Account Code`, `Account Name`, dan `Account Function` tidak bisa diubah selama permintaan berjalan pada form Edit
111. Verifikasi hanya satu permintaan Edit Account yang dikirim sesudah klik ganda

### Koneksi terputus menampilkan toast koneksi tanpa menutup form Edit
112. Tampilkan Modal Edit Account dengan kondisi K10
113. Ganti isi field `Account Name` dengan `Depreciation Expense – Admin Koneksi Putus`
114. Klik `[Save]`
115. Verifikasi toast `Connection problem. Please try again.` tampil sesudah `[Save]` pada form Edit saat koneksi terputus
116. Verifikasi modal Edit Account tetap terbuka sesudah koneksi terputus
117. Verifikasi field `Account Name` masih berisi `Depreciation Expense – Admin Koneksi Putus` sesudah koneksi terputus pada form Edit
118. Verifikasi tombol `[Save]` dapat diklik lagi sesudah koneksi terputus pada form Edit
