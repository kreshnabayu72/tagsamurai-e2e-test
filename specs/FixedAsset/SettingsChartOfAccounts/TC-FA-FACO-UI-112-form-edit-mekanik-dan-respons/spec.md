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
  D-16: [70, 71, 72, 73]
  R-02: [12, 13]
  R-03: [37, 55]
  T-02: [6, 12]
  T-03: [37, 38, 40]
  T-12: 61
  §4.1.2#p4: [83, 85, 86, 87, 91, 92, 93, 98, 99, 100, 102]
  §4.2f#b3: [117, 118, 126, 129]
  §7.3#b1: [13, 14, 21, 22, 23]
  §7.3#b4: [61, 62, 63]
  §[F-FACO-02] Edit Account#r8: 39
  §[F-FACO-02] Edit Account#r9: 37
  §[F-FACO-02] Edit Account#r12: [75, 76, 78, 79]
  §9.4.2#r7: 37
  §9.4.2#r32: 139
  EB-FB-1@edit-account: [6, 12]
  EB-FB-3@form-edit-account: [37, 39, 40]
  EB-FRM-1@form-edit-account: [135, 136, 137, 138, 139]
  EB-FRM-2@form-edit-account: [46, 48, 107, 111, 117, 118, 120, 122, 124, 126, 129]
  EB-FRM-3@form-edit-account: [83, 85, 86, 87, 88, 89]
  EB-ERR-1@edit-account: [12, 13, 14, 15, 21, 22, 23, 24, 30, 32]
anchor: []
coverage:
  web: automated
---

# Form Edit Account: Saving, menutup form, Clear Field, No-Op, dan reaksi atas respons server

## Prerequisites
- Aktor: Total Control.
- Layar awal: Settings > Accounting > Chart of Accounts.
- Komponen: Modal Edit Account.
- Data:
  - DU-112-1: akun dengan Account Code `5-6001`, Account Name `Depreciation Expense – Admin`, Account Function `Depreciation Expense`, Used By `0`, Last Used in Journal `—`.
  - DU-112-2: akun dengan Account Code `1-1001`, Account Name `Fixed Assets – Equipment`, Account Function `Asset Cost`, Used By `3`, Last Used in Journal `Oct 2026`.
- Kondisi:
  - K1: form Edit Account dibuka untuk akun DU-112-1, yang tidak terkunci, dan penyimpanan akun berhasil bila `[Save]` dikirim.
  - K2: seperti K1, dan penyimpanan gagal karena error server.
  - K3: seperti K1, dan penyimpanan gagal karena timeout atau koneksi terputus.
  - K4: seperti K1, dan server menyatakan permintaan tanpa perubahan nilai berhasil sebagai No-Op.
  - K5: seperti K1, dan akun sudah dihapus user lain saat `[Save]` dikirim.
  - K6: seperti K1, dan status kunci berubah antara form dibuka dan `[Save]`: akun mulai dipakai Asset Class sehingga Account Function terkunci, sedangkan submit mengubah Account Function.
  - K7: seperti K1, dan penyimpanan gagal karena error server pada percobaan pertama, lalu berhasil pada percobaan berikutnya.
  - K8: form Edit Account dibuka untuk akun DU-112-2, yang terkunci karena Last Used in Journal terisi.
  - K9: seperti K1, dan penyimpanan berjalan lambat sehingga respons belum diterima.

## Test Steps

### Save dengan nilai baru menampilkan toast sukses
1. Tampilkan Modal Edit Account dengan kondisi K1
2. Klik `⋯` pada baris akun `5-6001`
3. Klik `Edit`
4. Ganti isi field `Account Name` dengan `Depreciation Expense – Admin Revisi {runId}`
5. Klik `[Save]`
6. Verifikasi toast `Success, account has been updated.` tampil sesudah `[Save]` pada form Edit

### Error server menampilkan toast gagal tanpa menutup form Edit
7. Tampilkan Modal Edit Account dengan kondisi K2
8. Klik `⋯` pada baris akun `5-6001`
9. Klik `Edit`
10. Ganti isi field `Account Name` dengan `Depreciation Expense – Admin Gagal`
11. Klik `[Save]`
12. Verifikasi toast `Error, failed to update account.` tampil sesudah `[Save]` pada form Edit
13. Verifikasi modal Edit Account tetap terbuka sesudah toast gagal tampil
14. Verifikasi field `Account Name` masih berisi `Depreciation Expense – Admin Gagal` sesudah toast gagal pada form Edit
15. Verifikasi tombol `[Save]` dapat diklik lagi sesudah toast gagal pada form Edit

### Timeout menampilkan toast koneksi tanpa menutup form Edit
16. Tampilkan Modal Edit Account dengan kondisi K3
17. Klik `⋯` pada baris akun `5-6001`
18. Klik `Edit`
19. Ganti isi field `Account Name` dengan `Depreciation Expense – Admin Putus`
20. Klik `[Save]`
21. Verifikasi toast `Connection problem. Please try again.` tampil sesudah `[Save]` pada form Edit timeout
22. Verifikasi modal Edit Account tetap terbuka sesudah timeout
23. Verifikasi field `Account Name` masih berisi `Depreciation Expense – Admin Putus` sesudah timeout pada form Edit
24. Verifikasi tombol `[Save]` dapat diklik lagi sesudah timeout pada form Edit

### Save ulang sesudah penyimpanan pulih berhasil
25. Tampilkan Modal Edit Account dengan kondisi K7
26. Klik `⋯` pada baris akun `5-6001`
27. Klik `Edit`
28. Ganti isi field `Account Name` dengan `Depreciation Expense – Admin Pulih {runId}`
29. Klik `[Save]`
30. Verifikasi toast `Error, failed to update account.` tampil sesudah percobaan pertama pada form Edit
31. Klik `[Save]` sekali lagi
32. Verifikasi toast `Success, account has been updated.` tampil sesudah Save ulang pada form Edit

### Save tanpa perubahan adalah No-Op
33. Tampilkan Modal Edit Account dengan kondisi K4
34. Klik `⋯` pada baris akun `5-6001`
35. Klik `Edit`
36. Klik `[Save]` tanpa mengubah isi field apa pun
37. Verifikasi toast `No changes to save.` tampil sesudah `[Save]` tanpa perubahan
38. Verifikasi toast tersebut netral dengan severity Info, bukan toast sukses atau gagal
39. Verifikasi modal Edit Account tertutup sesudah `[Save]` tanpa perubahan
40. Verifikasi toast `Success, account has been updated.` tidak tampil sesudah `[Save]` tanpa perubahan

### Nilai diubah lalu dikembalikan dianggap bersih
41. Tampilkan Modal Edit Account dengan kondisi K1
42. Klik `⋯` pada baris akun `5-6001`
43. Klik `Edit`
44. Ganti isi field `Account Name` dengan `Depreciation Expense – Admin Sementara`
45. Ganti isi field `Account Name` dengan `Depreciation Expense – Admin` sehingga sama dengan nilai tersimpan
46. Verifikasi field `Account Name` berisi `Depreciation Expense – Admin` kembali sama dengan nilai tersimpan pada form Edit
47. Klik `✕` pada form yang nilainya kembali sama dengan nilai tersimpan
48. Verifikasi modal Edit Account tertutup langsung tanpa dialog Unsaved Changes karena nilai sama dengan tersimpan

### Nilai diubah lalu dikembalikan menghasilkan No-Op saat Save
49. Tampilkan Modal Edit Account dengan kondisi K4
50. Klik `⋯` pada baris akun `5-6001`
51. Klik `Edit`
52. Ganti isi field `Account Name` dengan `Depreciation Expense – Admin Sementara`
53. Ganti isi field `Account Name` dengan `Depreciation Expense – Admin` sehingga sama dengan nilai tersimpan
54. Klik `[Save]` pada form yang nilainya kembali sama dengan nilai tersimpan
55. Verifikasi toast `No changes to save.` tampil karena nilai akhir sama dengan nilai tersimpan

### Akun sudah dihapus user lain saat Save
56. Tampilkan Modal Edit Account dengan kondisi K5
57. Klik `⋯` pada baris akun `5-6001`
58. Klik `Edit`
59. Ganti isi field `Account Name` dengan `Depreciation Expense – Admin Terhapus`
60. Klik `[Save]`
61. Verifikasi toast netral `This account is no longer available.` tampil sesudah `[Save]` pada akun yang sudah terhapus
62. Verifikasi modal Edit Account tertutup sesudah akun dinyatakan tidak tersedia
63. Verifikasi toast `Error, failed to update account.` tidak tampil untuk akun yang sudah terhapus

### Status kunci berubah antara form dibuka dan Save
64. Tampilkan Modal Edit Account dengan kondisi K6
65. Klik `⋯` pada baris akun `5-6001`
66. Klik `Edit`
67. Ganti isi field `Account Function` dengan `Asset Cost`
68. Ganti isi field `Account Name` dengan `Depreciation Expense – Admin Terkunci`
69. Klik `[Save]`
70. Verifikasi dialog `Cannot Save Account` tampil
71. Verifikasi dialog memuat kalimat `This account has been locked for editing by another action. The form has been reloaded with the latest lock status.`
72. Verifikasi dialog memuat satu butir daftar bullet untuk satu akun
73. Verifikasi dialog memiliki tombol `[OK]`
74. Klik `[OK]` pada dialog `Cannot Save Account`
75. Verifikasi modal Edit Account tetap terbuka sesudah dialog ditutup
76. Verifikasi field `Account Function` kembali ke nilai tersimpan `Depreciation Expense` dan Disabled sesudah status kunci dimuat ulang
77. Arahkan kursor ke field `Account Function` yang Disabled sesudah status kunci dimuat ulang
78. Verifikasi tooltip alasan tampil pada field `Account Function` yang Disabled sesudah status kunci dimuat ulang
79. Verifikasi field `Account Name` masih berisi `Depreciation Expense – Admin Terkunci` sesudah status kunci dimuat ulang

### Clear Field pada akun tidak terkunci mengosongkan field
80. Tampilkan Modal Edit Account dengan kondisi K1
81. Klik `⋯` pada baris akun `5-6001`
82. Klik `Edit`
83. Verifikasi form Edit terisi nilai tersimpan: Account Code `5-6001`, Account Name `Depreciation Expense – Admin`, dan Account Function `Depreciation Expense`
84. Klik `[Clear Field]` pada form Edit akun yang tidak terkunci
85. Verifikasi field `Account Code` dikosongkan oleh `[Clear Field]` pada form Edit
86. Verifikasi field `Account Name` dikosongkan oleh `[Clear Field]` pada form Edit
87. Verifikasi field `Account Function` menampilkan `Select account function` sesudah `[Clear Field]`
88. Verifikasi field dikosongkan oleh `[Clear Field]` alih-alih dikembalikan ke nilai tersimpan
89. Verifikasi tidak ada dialog konfirmasi yang tampil sesudah `[Clear Field]` pada form Edit
90. Klik `[Save]`
91. Verifikasi caption `Account code must not be empty` tampil di bawah field `Account Code` sesudah Clear Field lalu Save
92. Verifikasi caption `Account name must not be empty` tampil di bawah field `Account Name` sesudah Clear Field lalu Save
93. Verifikasi caption `Account function must not be empty` tampil di bawah field `Account Function` sesudah Clear Field lalu Save

### Clear Field pada akun terkunci hanya mengosongkan field yang tidak terkunci
94. Tampilkan Modal Edit Account dengan kondisi K8
95. Klik `⋯` pada baris akun `1-1001`
96. Klik `Edit`
97. Klik `[Clear Field]` pada form Edit akun yang terkunci
98. Verifikasi field `Account Code` tetap Disabled dengan nilai tersimpan `1-1001` sesudah `[Clear Field]`
99. Verifikasi field `Account Function` tetap Disabled dengan nilai tersimpan `Asset Cost` sesudah `[Clear Field]`
100. Verifikasi field `Account Name` dikosongkan oleh `[Clear Field]` pada akun yang terkunci
101. Klik `[Save]`
102. Verifikasi caption `Account name must not be empty` tampil di bawah field `Account Name` pada akun yang terkunci

### Menutup form Edit yang belum diubah
103. Tampilkan Modal Edit Account dengan kondisi K1
104. Klik `⋯` pada baris akun `5-6001`
105. Klik `Edit`
106. Klik `✕` pada form Edit yang belum diubah
107. Verifikasi modal Edit Account tertutup langsung tanpa dialog Unsaved Changes sesudah `✕` diklik pada form Edit yang bersih
108. Klik `⋯` pada baris akun `5-6001`
109. Klik `Edit`
110. Tekan `Esc` pada form Edit yang belum diubah
111. Verifikasi modal Edit Account tertutup langsung tanpa dialog Unsaved Changes sesudah `Esc` ditekan pada form Edit yang bersih

### Menutup form Edit yang sudah diubah memunculkan Unsaved Changes
112. Tampilkan Modal Edit Account dengan kondisi K1
113. Klik `⋯` pada baris akun `5-6001`
114. Klik `Edit`
115. Ganti isi field `Account Name` dengan `Depreciation Expense – Admin Draf`
116. Klik `✕` pada form Edit yang sudah diubah
117. Verifikasi dialog `Unsaved Changes` pada form Edit tampil dengan pesan `You have unsaved changes. Are you sure you want to leave?`
118. Verifikasi dialog Unsaved Changes pada form Edit memiliki tombol `[Leave]` dan `[Cancel]`
119. Tekan `Esc`
120. Verifikasi dialog Unsaved Changes pada form Edit tertutup dan modal Edit Account tetap terbuka dengan Account Name `Depreciation Expense – Admin Draf`, sama seperti `[Cancel]`
121. Klik area backdrop di luar modal Edit Account
122. Verifikasi modal Edit Account tetap terbuka dengan Account Name `Depreciation Expense – Admin Draf` tanpa dialog Unsaved Changes sesudah backdrop diklik
123. Tekan `Esc` pada form Edit yang sudah diubah
124. Verifikasi dialog Unsaved Changes pada form Edit tampil sesudah `Esc` ditekan pada form yang sudah diubah
125. Klik `[Cancel]` pada dialog Unsaved Changes
126. Verifikasi dialog Unsaved Changes pada form Edit tertutup dan modal Edit Account tetap terbuka dengan Account Name `Depreciation Expense – Admin Draf` sesudah `[Cancel]`
127. Klik `✕` pada form Edit yang sudah diubah
128. Klik `[Leave]` pada dialog Unsaved Changes
129. Verifikasi modal Edit Account tertutup tanpa menyimpan sesudah `[Leave]`

### Saving pada form Edit mencegah klik ganda
130. Tampilkan Modal Edit Account dengan kondisi K9
131. Klik `⋯` pada baris akun `5-6001`
132. Klik `Edit`
133. Ganti isi field `Account Name` dengan `Depreciation Expense – Admin Ganda`
134. Klik ganda `[Save]`
135. Verifikasi tombol `[Save]` tidak bisa diklik selama permintaan berjalan pada form Edit
136. Verifikasi tombol `[Clear Field]` tidak bisa diklik selama permintaan berjalan pada form Edit
137. Verifikasi tombol `✕` tidak bisa diklik selama permintaan berjalan pada form Edit
138. Verifikasi field `Account Code`, `Account Name`, dan `Account Function` tidak bisa diubah selama permintaan berjalan pada form Edit
139. Verifikasi hanya satu permintaan Edit Account yang dikirim sesudah klik ganda
