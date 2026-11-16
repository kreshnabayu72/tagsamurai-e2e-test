---
id: TC-FA-FACO-E2E-078-export-saat-form-terbuka-dep-export-journal
title: "Export Journal selesai saat form Edit atau dialog Delete terbuka"
layer: ui-e2e
priority: Medium
caseType: Negative
status: ready-for-automation
sourceRules: [D-16, "§[F-FACO-02] Edit Account#r4", "§[F-FACO-02] Edit Account#r13", "§[F-FACO-02] Edit Account#r14", "§[F-FACO-02] Edit Account#r15", "§[F-FACO-02] Edit Account#r16", "§[F-FACO-05] Delete Account#r15", "§9.4.2#r8", "§9.4.2#r22", "§[F-FACO-05] Delete Account#r16"]
smoke: []
dependsOn: ["Export Journal: export jurnal yang mengisi Last Used in Journal"]
trace:
  D-16: [8, 11]
  "§[F-FACO-02] Edit Account#r4": [8, 36]
  "§[F-FACO-02] Edit Account#r13": [8, 9]
  "§[F-FACO-02] Edit Account#r14": [11, 12, 14, 16, 17]
  "§[F-FACO-02] Edit Account#r15": [25, 27]
  "§[F-FACO-02] Edit Account#r16": [34, 35, 36, 37, 40]
  "§[F-FACO-05] Delete Account#r15": [48, 49, 50, 51]
  "§9.4.2#r8": [8, 36]
  "§9.4.2#r22": [48, 55, 64, 65, 66, 67, 70, 73, 83, 84, 86, 87, 92, 95]
  "§[F-FACO-05] Delete Account#r16": [64, 65, 67, 73, 83, 84, 87, 92, 95]
anchor: [23, 45, 61, 72, 80, 91, 94]
coverage:
  web: automated
---

# Export Journal selesai saat form Edit atau dialog Delete terbuka

## Prerequisites
- Aktor: Admin A dengan role Total Control, cakupan seluruh client. Pemicu perubahan: Admin B dengan role Total Control, cakupan seluruh client, yang menjalankan Export Journal.
- Layar awal: Settings > Accounting > Chart of Accounts.
- Data:
  - M0 adalah bulan saat spec dijalankan. Periode ditulis dengan format `MMM YYYY`.
  - DU-078-1: Account Code `LKB1-{runId}`, Account Name `Rental Equipment Cost {runId}`, Account Function `Capitalization Offset`, Status `Active`, Used By `0`, Last Used in Journal `—` (belum pernah diekspor), ada di entitas aktor.
  - Label akun DU-078-1 pada bullet dialog adalah `LKB1-{runId} – Rental Equipment Cost {runId}`, dari Account Code `LKB1-{runId}` dan Account Name `Rental Equipment Cost {runId}`.
  - DU-078-2: perubahan yang dikirim Admin A pada form Edit DU-078-1: Account Code `LKB1X-{runId}` dan Account Name `Rental Equipment Cost Revised {runId}`.
  - DU-078-3: Account Code `LKB2-{runId}`, Account Name `Warehouse Racking Cost {runId}`, Account Function `Capitalization Offset`, Status `Active`, Used By `0`, Last Used in Journal `—` (belum pernah diekspor), ada di entitas aktor.
  - DU-078-4: Account Name baru untuk DU-078-3: `Warehouse Racking Cost Revised {runId}`.
  - DU-078-5: Account Code `LKB3-{runId}`, Account Name `Dock Leveler Cost {runId}`, Account Function `Capitalization Offset`, Status `Active`, Used By `0`, Last Used in Journal `—` (belum pernah diekspor), ada di entitas aktor.
  - Label akun DU-078-5 pada bullet dialog adalah `LKB3-{runId} – Dock Leveler Cost {runId}`, dari Account Code `LKB3-{runId}` dan Account Name `Dock Leveler Cost {runId}`.
  - DU-078-6: Account Code `LKB4-{runId}`, Account Name `Pallet Jack Cost {runId}`, Account Function `Capitalization Offset`, Status `Active`, Used By `0`, bukan nilai default company, Last Used in Journal `—` (belum pernah diekspor), ada di entitas aktor.
  - DU-078-7: Account Code `LKB5-{runId}`, Account Name `Conveyor Belt Cost {runId}`, Account Function `Capitalization Offset`, Status `Active`, Used By `0`, bukan nilai default company, Last Used in Journal `—` (belum pernah diekspor), ada di entitas aktor.
  - DU-078-8: Account Code `LKB6-{runId}`, Account Name `Mezzanine Floor Cost {runId}`, Account Function `Capitalization Offset`, Status `Active`, Used By `0`, bukan nilai default company, Last Used in Journal `—` (belum pernah diekspor), ada di entitas aktor.
  - DU-078-9: Account Code `LKB7-{runId}`, Account Name `Cold Storage Fit-out Cost {runId}`, Account Function `Capitalization Offset`, Status `Active`, Used By `0`, bukan nilai default company, Last Used in Journal `—` (belum pernah diekspor), ada di entitas aktor.
  - Label akun DU-078-6 pada bullet dialog adalah `LKB4-{runId} – Pallet Jack Cost {runId}`, dari Account Code `LKB4-{runId}` dan Account Name `Pallet Jack Cost {runId}`.
  - Label akun DU-078-7 pada bullet dialog adalah `LKB5-{runId} – Conveyor Belt Cost {runId}`, dari Account Code `LKB5-{runId}` dan Account Name `Conveyor Belt Cost {runId}`.
  - Label akun DU-078-8 pada bullet dialog adalah `LKB6-{runId} – Mezzanine Floor Cost {runId}`, dari Account Code `LKB6-{runId}` dan Account Name `Mezzanine Floor Cost {runId}`.
  - Label akun DU-078-9 pada bullet dialog adalah `LKB7-{runId} – Cold Storage Fit-out Cost {runId}`, dari Account Code `LKB7-{runId}` dan Account Name `Cold Storage Fit-out Cost {runId}`.
- Kondisi:
  - Setiap Export Journal yang dijalankan Admin B di spec ini memakai periode jurnal `M0 − 2 bulan` dan hanya memuat akun yang disebut pada langkahnya; akun DU-078-1 sampai DU-078-9 yang tidak disebut pada langkah itu tidak ikut berkasnya dan Last Used in Journal-nya tetap `—`.

## Test Steps

### Save Edit yang mengubah field terkunci ditolak saat Export Journal selesai sesudah form dibuka
1. Ketik Search `LKB1-{runId}`, tekan Enter
2. Klik `⋯` pada baris `LKB1-{runId}`
3. Klik `Edit`
4. Admin B menjalankan Export Journal untuk periode `M0 − 2 bulan` yang memuat akun `LKB1-{runId}`, dan export selesai saat form Edit masih terbuka
5. Ganti isi Account Code dengan `LKB1X-{runId}`
6. Ganti isi Account Name dengan `Rental Equipment Cost Revised {runId}`
7. Klik `[Save]`
8. Verifikasi dialog `Cannot Save Account` tampil dengan bullet `LKB1-{runId} – Rental Equipment Cost {runId}`
9. Verifikasi tidak ada toast yang tampil bersama dialog `Cannot Save Account`
10. Klik `[OK]`
11. Verifikasi field Account Code Disabled dengan nilai tersimpan `LKB1-{runId}`
12. Verifikasi field Account Function Disabled dengan nilai tersimpan `Capitalization Offset`
13. Arahkan kursor ke field Account Code
14. Verifikasi alasan `Account Code can't be changed because this account was used in a journal in [Month Year]. Create a new account if needed.` dengan `[Month Year]` berisi periode `M0 − 2 bulan` yang ditulis `MMM YYYY` tersampaikan pada field Account Code yang Disabled
15. Arahkan kursor ke field Account Function
16. Verifikasi alasan `Account Function can't be changed because this account was used in a journal in [Month Year].` dengan `[Month Year]` berisi periode `M0 − 2 bulan` yang ditulis `MMM YYYY` tersampaikan pada field Account Function yang Disabled
17. Verifikasi field Account Name tetap berisi `Rental Equipment Cost Revised {runId}`
18. Klik `✕` pada form Edit, lalu klik `[Leave]` pada dialog Unsaved Changes
19. Muat ulang halaman
20. Ketik Search `LKB1-{runId}`, tekan Enter
21. Klik ikon `Changelog` di toolbar
22. Ketik Search `LKB1-{runId}`, tekan Enter
23. Verifikasi baris Changelog dengan Field `Last Used in Journal` untuk Account Code `LKB1-{runId}` tampil
24. Ganti isi kotak search dengan `LKB1X-{runId}`, tekan Enter
25. Verifikasi tidak ada baris Changelog dengan Account Code `LKB1X-{runId}`
26. Klik `✕` pada modal Changelog
27. Verifikasi baris `LKB1-{runId}` tampil dengan Account Name `Rental Equipment Cost {runId}`

### Save Edit yang hanya mengubah field tidak terkunci berhasil walau kunci berubah
28. Ganti isi kotak search dengan `LKB2-{runId}`, tekan Enter
29. Klik `⋯` pada baris `LKB2-{runId}`
30. Klik `Edit`
31. Admin B menjalankan Export Journal untuk periode `M0 − 2 bulan` yang memuat akun `LKB2-{runId}`, dan export selesai saat form Edit masih terbuka
32. Ganti isi Account Name dengan `Warehouse Racking Cost Revised {runId}`
33. Klik `[Save]`
34. Verifikasi toast `Success, account has been updated.` tampil
35. Verifikasi form Edit tertutup
36. Verifikasi baris `LKB2-{runId}` tampil dengan Account Name `Warehouse Racking Cost Revised {runId}`
37. Verifikasi Last Used in Journal baris `LKB2-{runId}` bernilai periode `M0 − 2 bulan` yang ditulis `MMM YYYY`, tanpa muat ulang halaman
38. Klik ikon `Changelog` di toolbar
39. Ganti isi kotak search dengan `LKB2-{runId}`, tekan Enter
40. Verifikasi baris Changelog dengan Action `Edit`, Field `Account Name`, Old Value `Warehouse Racking Cost {runId}`, dan New Value `Warehouse Racking Cost Revised {runId}` tampil
41. Klik `✕` pada modal Changelog

### Delete ditolak saat Export Journal selesai sesudah dialog dibuka
42. Ganti isi kotak search dengan `LKB3-{runId}`, tekan Enter
43. Klik `⋯` pada baris `LKB3-{runId}`
44. Klik `Delete`
45. Verifikasi dialog `Delete Account` tampil, yaitu akun belum diblokir saat dialog dibuka
46. Admin B menjalankan Export Journal untuk periode `M0 − 2 bulan` yang memuat akun `LKB3-{runId}`, dan export selesai saat dialog Delete masih terbuka
47. Klik `[Delete]`
48. Verifikasi dialog `Cannot Delete Account` tampil dengan bullet `LKB3-{runId} – Dock Leveler Cost {runId}`
49. Verifikasi kalimat `This account was last used in a journal in [Month Year]. Deleting it may break historical records.` tampil dengan `[Month Year]` berisi periode `M0 − 2 bulan` yang ditulis `MMM YYYY`
50. Verifikasi kalimat saran `Deactivate it instead.` tampil, karena akun masih Active dan Used By `0`
51. Verifikasi tidak ada toast yang tampil bersama dialog `Cannot Delete Account`
52. Klik `[OK]`
53. Muat ulang halaman
54. Ketik Search `LKB3-{runId}`, tekan Enter
55. Verifikasi baris `LKB3-{runId}` masih tampil di tabel

### Bulk Delete: akun yang menjadi diekspor sesudah dialog dibuka dilewati dan akun lain terhapus
56. Ganti isi kotak search dengan `{runId}`, tekan Enter
57. Centang baris `LKB4-{runId}`
58. Centang baris `LKB5-{runId}`
59. Klik `Bulk Action`
60. Pilih `Delete`
61. Verifikasi dialog `Delete Accounts` tampil dengan bullet `LKB4-{runId} – Pallet Jack Cost {runId}` dan bullet `LKB5-{runId} – Conveyor Belt Cost {runId}`, yaitu kedua akun belum diblokir saat dialog dibuka
62. Admin B menjalankan Export Journal untuk periode `M0 − 2 bulan` yang memuat akun `LKB5-{runId}`, dan export selesai saat dialog Delete masih terbuka
63. Klik `[Delete]` pada dialog
64. Verifikasi toast `Success, account has been deleted. Some items were skipped (still in use, used in a journal, or default company).` tampil
65. Verifikasi dialog `Cannot Delete Accounts` tidak tampil
66. Verifikasi baris `LKB4-{runId}` tidak ada lagi di tabel
67. Verifikasi baris `LKB5-{runId}` tetap tampil di tabel
68. Klik ikon `Changelog` di toolbar
69. Ketik Search `LKB4-{runId}`, tekan Enter
70. Verifikasi baris Changelog dengan Action `Delete` untuk Account Code `LKB4-{runId}` tampil
71. Ganti isi kotak search dengan `LKB5-{runId}`, tekan Enter
72. Verifikasi baris Changelog dengan Field `Last Used in Journal` untuk Account Code `LKB5-{runId}` tampil
73. Verifikasi tidak ada baris Changelog dengan Action `Delete` untuk Account Code `LKB5-{runId}`
74. Klik `✕` pada modal Changelog

### Bulk Delete: seluruh akun terpilih yang menjadi diekspor sesudah dialog dibuka ditolak seluruhnya
75. Ganti isi kotak search dengan `{runId}`, tekan Enter
76. Centang baris `LKB6-{runId}`
77. Centang baris `LKB7-{runId}`
78. Klik `Bulk Action`
79. Pilih `Delete`
80. Verifikasi dialog `Delete Accounts` tampil dengan bullet `LKB6-{runId} – Mezzanine Floor Cost {runId}` dan bullet `LKB7-{runId} – Cold Storage Fit-out Cost {runId}`, yaitu kedua akun belum diblokir saat dialog dibuka
81. Admin B menjalankan Export Journal untuk periode `M0 − 2 bulan` yang memuat akun `LKB6-{runId}` dan `LKB7-{runId}`, dan export selesai saat dialog Delete masih terbuka
82. Klik `[Delete]` pada dialog
83. Verifikasi dialog `Cannot Delete Accounts` tampil
84. Verifikasi dialog memuat bullet `LKB6-{runId} – Mezzanine Floor Cost {runId}` dan bullet `LKB7-{runId} – Cold Storage Fit-out Cost {runId}` pada kelompok `The following were last used in a journal and cannot be deleted:`
85. Klik `[OK]`
86. Verifikasi baris `LKB6-{runId}` tetap tampil di tabel
87. Verifikasi baris `LKB7-{runId}` tetap tampil di tabel
88. Klik `×` pada Bulk Action bar
89. Klik ikon `Changelog` di toolbar
90. Ketik Search `LKB6-{runId}`, tekan Enter
91. Verifikasi baris Changelog dengan Field `Last Used in Journal` untuk Account Code `LKB6-{runId}` tampil
92. Verifikasi tidak ada baris Changelog dengan Action `Delete` untuk Account Code `LKB6-{runId}`
93. Ganti isi kotak search dengan `LKB7-{runId}`, tekan Enter
94. Verifikasi baris Changelog dengan Field `Last Used in Journal` untuk Account Code `LKB7-{runId}` tampil
95. Verifikasi tidak ada baris Changelog dengan Action `Delete` untuk Account Code `LKB7-{runId}`
96. Klik `✕` pada modal Changelog
