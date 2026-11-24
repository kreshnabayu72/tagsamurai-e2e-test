---
id: TC-FA-FACO-BE-151-validasi-edit-dan-no-op
title: "Validasi server Edit Account, Edit tanpa perubahan, dan Edit bersamaan"
layer: be-e2e
priority: Medium
caseType: Negative
status: ready-for-automation
owner: BE
sourceRules: [FACO-LOGIC-07d, N-08, R-02, R-03, "§8#b1", "§[F-FACO-02] Edit Account#b2", "§[F-FACO-02] Edit Account#b3", "§[F-FACO-02] Edit Account#r9", "§[F-FACO-02] Edit Account#r17", "§[F-FACO-02] Edit Account#r18", "§[F-FACO-02] Edit Account#r19", "§9.4.2#r9", "§9.9#r1", "§9.9#r2", "§9.9#r3", EB-FRM-6@form-edit-account, EB-FRM-8@account-code, EB-FRM-8@account-name, EB-FRM-8@account-function, EB-ERR-4, EB-CON-1, "§[F-FACO-02] Edit Account#r20", "§[F-FACO-02] Edit Account#r21", "§[F-FACO-02] Edit Account#r22", "§[F-FACO-02] Edit Account#r23", "§9.4.2#r40", EB-CON-3]
smoke: []
dependsOn: []
trace:
  FACO-LOGIC-07d: [46]
  N-08: [7, 8, 15]
  R-02: [49, 50, 64, 65]
  R-03: [5, 6]
  "§8#b1": [10, 11, 18]
  "§[F-FACO-02] Edit Account#b2": [5, 10, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44]
  "§[F-FACO-02] Edit Account#b3": [2, 5, 14, 17]
  "§[F-FACO-02] Edit Account#r9": [7, 8]
  "§[F-FACO-02] Edit Account#r17": [50, 56]
  "§[F-FACO-02] Edit Account#r18": [51, 96]
  "§[F-FACO-02] Edit Account#r19": [64, 65, 71, 72]
  "§9.4.2#r9": [49, 50, 51, 55, 56]
  "§9.9#r1": [20, 22, 24, 26, 28, 34, 40, 44, 98, 100]
  "§9.9#r2": [30, 32, 36, 42, 102, 104]
  "§9.9#r3": [38]
  EB-FRM-6@form-edit-account: [28, 32]
  EB-FRM-8@account-code: [20, 22, 24, 26, 28, 34, 40, 44, 67]
  EB-FRM-8@account-name: [30, 32, 36, 42, 69]
  EB-FRM-8@account-function: [38]
  EB-ERR-4: [20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 59]
  EB-CON-1: [49, 50, 56, 62, 94]
  "§[F-FACO-02] Edit Account#r20": [75, 82, 89, 91, 95, 96]
  "§[F-FACO-02] Edit Account#r21": [75, 82]
  "§[F-FACO-02] Edit Account#r22": [76, 77, 83, 84]
  "§[F-FACO-02] Edit Account#r23": [78, 79, 85, 86]
  "§9.4.2#r40": [75, 76, 77, 78, 79, 82, 83, 84, 85, 86]
  EB-CON-3: [49, 62, 75, 82, 89, 90, 91, 94, 95]
---

# Validasi server Edit Account, Edit tanpa perubahan, dan Edit bersamaan

## Prerequisites
- Aktor: Admin A dan Admin B, keduanya Total Control dengan cakupan seluruh client.
- Data:
  - DU-151-1: Account Code `SWA-{runId}`, Account Name `Beban Sewa Kantor {runId}`, Account Function `Depreciation Expense`.
  - DU-151-3: Account Code `NOP-{runId}`, Account Name `Kas Kecil Pusat {runId}`, Account Function `Asset Cost`.
  - DU-151-4: Account Code `KDB-{runId}`, Account Name `Kas di Bank {runId}`, Account Function `Asset Cost`.
  - DU-151-6: Account Code `SPT-{runId}`, Account Name `Kas Cabang {runId}`, Account Function `Asset Cost`.
  - DU-151-8: Account Code `NPK-{runId}`, Account Name `Beban Gaji {runId}`, Account Function `Depreciation Expense`.
  - DU-151-10: Account Code `REF-{runId}`, Account Name `Rekening Referensi {runId}`, Account Function `Asset Cost`.
  - DU-151-11: Account Code `EDD-{runId}`, Account Name `Beban Dibayar Dimuka {runId}`, Account Function `Asset Cost`.
  - DU-151-22: Account Code `BDY-{runId}`, Account Name `Beban Batas {runId}`, Account Function `Asset Cost`.
  - DU-151-25: Account Code `UTG-{runId}`, Account Name `Utang Usaha Cabang {runId}`, Account Function `Asset Cost`, ada di client lain, bukan client aktor.
  - DU-151-27: Account Code `LUJ-{runId}`, Account Name `Beban Audit {runId}`, Account Function `Asset Cost`.
  - DU-151-29: Account Code `CWL-{runId}`, Account Name `Kas Besar Awal {runId}`, Account Function `Asset Cost`.
  - DU-151-32: Account Code `STL-{runId}`, Account Name `Piutang Karyawan {runId}`, Account Function `Asset Cost`.
  - DU-151-35: Account Code `DLP-{runId}`, Account Name `Beban Promosi {runId}`, Account Function `Asset Cost`.
  - DU-151-37: Account Code `STS-{runId}`, Account Name `Beban Asuransi {runId}`, Account Function `Asset Cost`, Status `Active`.
  - DU-151-39: Account Code `CN1-{runId}`, Account Name `Kas Proyek Satu {runId}`, Account Function `Asset Cost`.
  - DU-151-40: Account Code `CN2-{runId}`, Account Name `Kas Proyek Dua {runId}`, Account Function `Asset Cost`.
  - DU-151-42: Account Code `TRB-{runId}`, Account Name `Batas Setelah Trim {runId}`, Account Function `Asset Cost`.
  - DU-151-45: Account Code `CSM-{runId}`, Account Name `Kas Serentak {runId}`, Account Function `Asset Cost`.
  - DU-151-48: Account Code `EAC-{runId}`, Account Name `Kas Edit Aktivasi {runId}`, Account Function `Asset Cost`, Status `Inactive`.
  - DU-151-50: Account Code `EDC-{runId}`, Account Name `Kas Edit Deaktivasi {runId}`, Account Function `Asset Cost`, Status `Active`.
  - DU-151-52: Account Code `DED-{runId}`, Account Name `Kas Hapus Edit Serentak {runId}`, Account Function `Asset Cost`.
  - DU-151-54: Account Code `SEQ-{runId}`, Account Name `Kas Berurutan Awal {runId}`, Account Function `Asset Cost`.
  - DU-151-57: Account Code `WLS-{runId}`, Account Name `Kas Whitelist Edit {runId}`, Account Function `Asset Cost`.
  - DU-151-60: Account Code `HTM-{runId}`, Account Name `Kas Pelaporan Pajak {runId}`, Account Function `Asset Cost`.
  - DU-151-62: Account Code `NAE-{runId}`, Account Name `Kas Pelaporan Regional {runId}`, Account Function `Asset Cost`.
- Kondisi:
  - Semua akun di atas belum pernah diekspor (Last Used in Journal kosong) dan tidak dipakai Asset Class (Used By 0), sehingga tidak ada field yang terkunci.

## Test Steps

### Edit dengan nilai baru tersimpan
1. Admin A mengirim Edit akun `SWA-{runId}` dengan Account Code `SWB-{runId}`, Account Name `Beban Sewa Gedung {runId}`, Account Function `Accumulated Depreciation`
2. Verifikasi akun dengan Account Code `SWB-{runId}` tersimpan dengan Account Name `Beban Sewa Gedung {runId}` dan Account Function `Accumulated Depreciation`, dan tidak ada lagi akun dengan Account Code `SWA-{runId}`

### Edit tanpa perubahan nilai tidak mengubah data dan tidak menulis log
3. Admin A mencatat jumlah entri log akun `NOP-{runId}` pada Changelog, pada System Log milik Admin A, dan pada Activity Log
4. Admin A mengirim Edit akun `NOP-{runId}` dengan Account Code `NOP-{runId}`, Account Name `Kas Kecil Pusat {runId}`, Account Function `Asset Cost`, semuanya identik dengan nilai tersimpan
5. Verifikasi permintaan berhasil dengan respons sukses, bukan respons tanpa konten, nilai akun tidak berubah, dan Account Code `NOP-{runId}` tidak ditolak sebagai duplikat dari akun itu sendiri
6. Verifikasi versi akun `NOP-{runId}` tidak naik
7. Verifikasi jumlah entri log akun `NOP-{runId}` pada Changelog sama dengan jumlah yang dicatat sebelum Edit
8. Verifikasi jumlah entri log akun `NOP-{runId}` pada System Log milik Admin A dan pada Activity Log sama dengan jumlah yang dicatat sebelum Edit

### Perubahan hanya huruf besar-kecil pada Account Code adalah perubahan nyata
9. Admin A mengirim Edit akun `KDB-{runId}` dengan Account Code `kdb-{runId}`, Account Name `Kas di Bank {runId}`, Account Function `Asset Cost`
10. Verifikasi akun tersimpan dengan Account Code `kdb-{runId}`, dan perubahan tidak ditolak sebagai duplikat dari akun itu sendiri
11. Verifikasi Changelog memuat entri Edit untuk field Account Code dengan Old Value `KDB-{runId}` dan New Value `kdb-{runId}`

### Perubahan hanya spasi di awal dan akhir bukan perubahan nilai
12. Admin A mencatat jumlah entri log akun `SPT-{runId}` pada Changelog
13. Admin A mengirim Edit akun `SPT-{runId}` dengan Account Code `SPT-{runId}`, Account Name `" Kas Cabang {runId} "`, Account Function `Asset Cost`
14. Verifikasi Account Name akun `SPT-{runId}` tetap `Kas Cabang {runId}` tanpa spasi di awal dan akhir
15. Verifikasi jumlah entri log akun `SPT-{runId}` pada Changelog sama dengan jumlah yang dicatat sebelum Edit

### Perubahan nyata ditambah perubahan huruf besar-kecil pada Account Code
16. Admin A mengirim Edit akun `NPK-{runId}` dengan Account Code `npk-{runId}`, Account Name `Beban Gaji Karyawan {runId}`, Account Function `Depreciation Expense`
17. Verifikasi akun tersimpan dengan Account Code `npk-{runId}` dan Account Name `Beban Gaji Karyawan {runId}`
18. Verifikasi Changelog akun itu memuat satu entri Edit untuk field Account Name dan satu entri Edit untuk field Account Code

### Edit ditolak server dan data tidak berubah
19. Admin A mengirim Edit akun `EDD-{runId}` dengan Account Code `REF-{runId}`, Account Name `Beban Dibayar Dimuka {runId}`, Account Function `Asset Cost`
20. Verifikasi permintaan ditolak dengan alasan `Account code already exists`, dan akun `EDD-{runId}` tetap bernilai Account Code `EDD-{runId}` dan Account Name `Beban Dibayar Dimuka {runId}`
21. Admin A mengirim Edit akun `EDD-{runId}` dengan Account Code `ref-{runId}`, Account Name `Beban Dibayar Dimuka {runId}`, Account Function `Asset Cost`
22. Verifikasi permintaan ditolak dengan alasan `Account code already exists` karena perbedaan huruf besar-kecil tidak membuat kode berbeda, dan akun `EDD-{runId}` tetap bernilai Account Code `EDD-{runId}`
23. Admin A mengirim Edit akun `EDD-{runId}` dengan Account Code `" REF-{runId} "`, Account Name `Beban Dibayar Dimuka {runId}`, Account Function `Asset Cost`
24. Verifikasi permintaan ditolak dengan alasan `Account code already exists` karena kode dibandingkan setelah trim, dan akun `EDD-{runId}` tetap bernilai Account Code `EDD-{runId}`
25. Admin A mengirim Edit akun `EDD-{runId}` dengan Account Code `BE151-EDITT-A16X` (16 karakter), Account Name `Beban Dibayar Dimuka {runId}`, Account Function `Asset Cost`
26. Verifikasi permintaan ditolak karena Account Code melebihi 15 karakter, dan akun `EDD-{runId}` tetap bernilai Account Code `EDD-{runId}`
27. Admin A mengirim Edit akun `EDD-{runId}` dengan Account Code `EDD#{runId}`, Account Name `Beban Dibayar Dimuka {runId}`, Account Function `Asset Cost`
28. Verifikasi permintaan ditolak karena Account Code memuat karakter di luar huruf Latin, angka, `-`, `_`, dan `.`, dan akun `EDD-{runId}` tetap bernilai Account Code `EDD-{runId}`
29. Admin A mengirim Edit akun `EDD-{runId}` dengan Account Code `EDD-{runId}`, Account Name `Beban Pemeliharaan Kendaraan Operasional Distribusi Barang Cabang Surabaya Timur Periode Semester Pertama Tahun Berjalan.` (121 karakter), Account Function `Asset Cost`
30. Verifikasi permintaan ditolak karena Account Name melebihi 120 karakter, dan akun `EDD-{runId}` tetap bernilai Account Name `Beban Dibayar Dimuka {runId}`
31. Admin A mengirim Edit akun `EDD-{runId}` dengan Account Code `EDD-{runId}`, Account Name `Beban 😊 {runId}`, Account Function `Asset Cost`
32. Verifikasi permintaan ditolak karena Account Name memuat emoji, dan akun `EDD-{runId}` tetap bernilai Account Name `Beban Dibayar Dimuka {runId}`
33. Admin A mengirim Edit akun `EDD-{runId}` dengan Account Code kosong, Account Name `Beban Dibayar Dimuka {runId}`, Account Function `Asset Cost`
34. Verifikasi permintaan ditolak karena Account Code kosong, dan akun `EDD-{runId}` tetap bernilai Account Code `EDD-{runId}`
35. Admin A mengirim Edit akun `EDD-{runId}` dengan Account Code `EDD-{runId}`, Account Name kosong, Account Function `Asset Cost`
36. Verifikasi permintaan ditolak karena Account Name kosong, dan akun `EDD-{runId}` tetap bernilai Account Name `Beban Dibayar Dimuka {runId}`
37. Admin A mengirim Edit akun `EDD-{runId}` dengan Account Code `EDD-{runId}`, Account Name `Beban Dibayar Dimuka {runId}`, Account Function kosong
38. Verifikasi permintaan ditolak karena Account Function kosong, dan akun `EDD-{runId}` tetap bernilai Account Function `Asset Cost`

### Edit pada batas panjang dan Account Code yang sama dengan client lain diterima
39. Admin A mengirim Edit akun `BDY-{runId}` dengan Account Code `BE151-EDITT-A15` (15 karakter), Account Name `Beban Batas {runId}`, Account Function `Asset Cost`
40. Verifikasi akun diterima dan tersimpan dengan Account Code `BE151-EDITT-A15`
41. Admin A mengirim Edit akun `BE151-EDITT-A15` dengan Account Code `BE151-EDITT-A15`, Account Name `Beban Pemeliharaan Kendaraan Operasional Distribusi Barang Cabang Surabaya Timur Periode Semester Pertama Tahun Berjalan` (120 karakter), Account Function `Asset Cost`
42. Verifikasi akun `BE151-EDITT-A15` diterima dan tersimpan dengan Account Name 120 karakter itu
43. Admin A mengirim Edit akun `BE151-EDITT-A15` dengan Account Code `UTG-{runId}`, Account Name `Beban Batas {runId}`, Account Function `Asset Cost`
44. Verifikasi akun diterima dan tersimpan dengan Account Code `UTG-{runId}` di client aktor, karena keunikan hanya berlaku di dalam satu client dan DU-151-25 ada di client lain

### Last Used in Journal tidak bisa diisi lewat permintaan langsung
45. Admin A mengirim Edit akun `LUJ-{runId}` dengan Last Used in Journal `Oct 2026`
46. Verifikasi Last Used in Journal akun `LUJ-{runId}` tetap kosong

### Dua admin menyimpan Edit atas akun yang sama serentak
47. Admin A mencatat jumlah entri log field Account Name akun `CWL-{runId}` pada Changelog
48. Admin A mengirim Edit akun `CWL-{runId}` dengan Account Name `Kas Besar Pusat {runId}`, dan Admin B secara serentak mengirim Edit akun `CWL-{runId}` dengan Account Name `Kas Besar Cabang {runId}`
49. Verifikasi kedua permintaan berhasil, tanpa penolakan karena konflik versi
50. Verifikasi Account Name akun `CWL-{runId}` adalah `Kas Besar Pusat {runId}` atau `Kas Besar Cabang {runId}`, yaitu nilai dari Save yang diterima terakhir
51. Verifikasi jumlah entri log field Account Name akun `CWL-{runId}` pada Changelog bertambah dua dibanding jumlah yang dicatat, satu per Save

### Edit atas akun yang sudah diubah admin lain sejak dibaca
52. Admin B membaca akun `STL-{runId}` dengan Account Name `Piutang Karyawan {runId}`
53. Admin A mengirim Edit akun `STL-{runId}` dengan Account Name `Piutang Karyawan Tetap {runId}`
54. Admin B mengirim Edit akun `STL-{runId}` dengan Account Name `Piutang Karyawan Kontrak {runId}`, tanpa penanda versi
55. Verifikasi Edit Admin B berhasil, tanpa penolakan atau dialog konflik karena akun sudah berubah sejak dibaca
56. Verifikasi Account Name akun `STL-{runId}` adalah `Piutang Karyawan Kontrak {runId}`, nilai dari Save terakhir

### Edit atas akun yang sudah dihapus admin lain
57. Admin A menghapus akun `DLP-{runId}`
58. Admin B mengirim Edit akun `DLP-{runId}` dengan Account Name `Beban Promosi Digital {runId}`
59. Verifikasi permintaan Admin B tidak mengubah data: tidak ada akun dengan Account Code `DLP-{runId}` dan tidak ada akun dengan Account Name `Beban Promosi Digital {runId}`

### Edit atas akun yang statusnya diubah admin lain
60. Admin A menonaktifkan akun `STS-{runId}`
61. Admin B mengirim Edit akun `STS-{runId}` dengan Account Name `Beban Asuransi Gedung {runId}`
62. Verifikasi Status akun `STS-{runId}` tetap `Inactive`, karena Edit tidak mengubah Status

### Dua admin mengubah Account Code dua akun menjadi nilai yang sama serentak
63. Admin A mengirim Edit akun `CN1-{runId}` dengan Account Code `CNC-{runId}`, dan Admin B secara serentak mengirim Edit akun `CN2-{runId}` dengan Account Code `CNC-{runId}`
64. Verifikasi satu permintaan Edit berhasil mengubah Account Code menjadi `CNC-{runId}`, sedangkan permintaan Edit lainnya ditolak dengan alasan `Account code already exists`
65. Verifikasi daftar akun client aktor dengan Account Code `CNC-{runId}` memuat tepat satu akun

### Edit Account Code 15 karakter setelah trim diterima
66. Admin A mengirim Edit akun `TRB-{runId}` dengan Account Code `" BE151-TRIMM-B15 "` (satu spasi di awal dan satu di akhir; setelah trim panjangnya 15 karakter), Account Name `Batas Setelah Trim {runId}`, Account Function `Asset Cost`
67. Verifikasi akun diterima dan tersimpan dengan Account Code `BE151-TRIMM-B15`, karena batas dihitung dari panjang setelah trim

### Edit dengan Account Name yang hanya berisi spasi ditolak
68. Admin A mengirim Edit akun `EDD-{runId}` dengan Account Code `EDD-{runId}`, Account Name berisi tiga spasi saja, Account Function `Asset Cost`
69. Verifikasi permintaan ditolak karena Account Name yang hanya berisi spasi dianggap kosong, dan akun `EDD-{runId}` tetap bernilai Account Name `Beban Dibayar Dimuka {runId}`

### Dua admin menyimpan Edit atas akun yang sama, satu memakai Account Code milik akun lain
70. Admin A mengirim Edit akun `CSM-{runId}` dengan Account Code `REF-{runId}`, Account Name `Kas Serentak {runId}`, Account Function `Asset Cost`, dan Admin B secara serentak mengirim Edit akun `CSM-{runId}` dengan Account Code `CSM-{runId}`, Account Name `Kas Serentak Baru {runId}`, Account Function `Asset Cost`
71. Verifikasi Edit Admin A ditolak dengan alasan `Account code already exists`, sedangkan Edit Admin B berhasil
72. Verifikasi akun `CSM-{runId}` bernilai Account Code `CSM-{runId}` dan Account Name `Kas Serentak Baru {runId}`, dan hanya satu akun yang ber-Account Code `REF-{runId}`

### Edit serentak dengan Activate atas akun yang sama
73. Admin A mencatat jumlah entri log akun `EAC-{runId}` pada Changelog untuk field Account Name dan untuk field Status
74. Admin A mengirim Edit akun `EAC-{runId}` dengan Account Code `EAC-{runId}`, Account Name `Kas Edit Aktivasi Baru {runId}`, Account Function `Asset Cost`, dan Admin B secara serentak mengirim Activate akun `EAC-{runId}`
75. Verifikasi kedua permintaan berhasil, tanpa saling menolak
76. Verifikasi Status akun `EAC-{runId}` adalah `Active`, tidak dikembalikan menjadi `Inactive` oleh Edit
77. Verifikasi Account Code `EAC-{runId}`, Account Name `Kas Edit Aktivasi Baru {runId}`, dan Account Function `Asset Cost` akun itu adalah nilai dari Edit, tidak diubah oleh Activate
78. Verifikasi Changelog memuat tepat satu entri baru dengan Action `Edit` untuk field Account Name akun `EAC-{runId}`, Old Value `Kas Edit Aktivasi {runId}` dan New Value `Kas Edit Aktivasi Baru {runId}`
79. Verifikasi Changelog memuat tepat satu entri baru dengan Action `Edit` untuk field Status akun `EAC-{runId}`, Old Value `Inactive` dan New Value `Active`

### Edit serentak dengan Deactivate atas akun yang sama
80. Admin A mencatat jumlah entri log akun `EDC-{runId}` pada Changelog untuk field Account Function dan untuk field Status
81. Admin A mengirim Edit akun `EDC-{runId}` dengan Account Code `EDC-{runId}`, Account Name `Kas Edit Deaktivasi {runId}`, Account Function `Disposal Proceeds`, dan Admin B secara serentak mengirim Deactivate akun `EDC-{runId}`
82. Verifikasi kedua permintaan berhasil, tanpa saling menolak
83. Verifikasi Status akun `EDC-{runId}` adalah `Inactive`, tidak dikembalikan menjadi `Active` oleh Edit
84. Verifikasi Account Code `EDC-{runId}`, Account Name `Kas Edit Deaktivasi {runId}`, dan Account Function `Disposal Proceeds` akun itu adalah nilai dari Edit, tidak diubah oleh Deactivate
85. Verifikasi Changelog memuat tepat satu entri baru dengan Action `Edit` untuk field Account Function akun `EDC-{runId}`, Old Value `Asset Cost` dan New Value `Disposal Proceeds`
86. Verifikasi Changelog memuat tepat satu entri baru dengan Action `Edit` untuk field Status akun `EDC-{runId}`, Old Value `Active` dan New Value `Inactive`

### Delete serentak dengan Edit atas akun yang sama
87. Admin A mencatat jumlah entri log akun `DED-{runId}` pada Changelog dengan Action `Edit` untuk field Account Name dan dengan Action `Delete`
88. Admin A mengirim Delete akun `DED-{runId}`, dan Admin B secara serentak mengirim Edit akun `DED-{runId}` dengan Account Name `Kas Hapus Edit Serentak Baru {runId}`
89. Verifikasi tidak ada lagi akun dengan Account Code `DED-{runId}` dan tidak ada akun dengan Account Name `Kas Hapus Edit Serentak Baru {runId}`, karena Delete menang atas Edit yang menyusul
90. Verifikasi Changelog memuat tepat satu entri baru dengan Action `Delete` untuk akun `DED-{runId}`
91. Verifikasi jumlah entri baru dengan Action `Edit` untuk field Account Name akun `DED-{runId}` adalah nol atau satu, tidak lebih, karena Edit yang menyusul Delete tidak menulis log

### Dua Edit serentak atas akun yang sama diproses satu per satu
92. Admin A mencatat jumlah entri log akun `SEQ-{runId}` pada Changelog untuk field Account Name dan untuk field Account Function
93. Admin A mengirim Edit akun `SEQ-{runId}` dengan Account Code `SEQ-{runId}`, Account Name `Kas Berurutan Satu {runId}`, Account Function `Gain on Disposal`, dan Admin B secara serentak mengirim Edit akun `SEQ-{runId}` dengan Account Code `SEQ-{runId}`, Account Name `Kas Berurutan Dua {runId}`, Account Function `Loss on Disposal`
94. Verifikasi kedua permintaan berhasil, tanpa penolakan karena konflik
95. Verifikasi pasangan Account Name dan Account Function akun `SEQ-{runId}` adalah `Kas Berurutan Satu {runId}` bersama `Gain on Disposal`, atau `Kas Berurutan Dua {runId}` bersama `Loss on Disposal`, tidak tercampur dari kedua Save
96. Verifikasi Changelog memuat dua entri baru untuk field Account Name dan dua entri baru untuk field Account Function akun `SEQ-{runId}`, dan pada tiap field Old Value entri yang lebih akhir sama dengan New Value entri sebelumnya, karena Save atas akun yang sama diproses satu per satu
### Account Code berisi garis bawah dan titik diterima saat Edit
97. Admin A mengirim Edit akun `WLS-{runId}` dengan Account Code `WLS_{runId}`, Account Name `Kas Whitelist Edit {runId}`, Account Function `Asset Cost`
98. Verifikasi akun tersimpan dengan Account Code `WLS_{runId}`, karena `_` termasuk karakter yang diizinkan, dan tidak ada lagi akun dengan Account Code `WLS-{runId}`
99. Admin A mengirim Edit akun `WLS_{runId}` dengan Account Code `WLS.{runId}`, Account Name `Kas Whitelist Edit {runId}`, Account Function `Asset Cost`
100. Verifikasi akun tersimpan dengan Account Code `WLS.{runId}`, karena `.` termasuk karakter yang diizinkan, dan tidak ada lagi akun dengan Account Code `WLS_{runId}`

### Account Name berisi HTML disimpan apa adanya saat Edit
101. Admin A mengirim Edit akun `HTM-{runId}` dengan Account Code `HTM-{runId}`, Account Name `<b>Kas Kecil</b> {runId}`, Account Function `Asset Cost`
102. Verifikasi akun `HTM-{runId}` tersimpan dengan Account Name persis `<b>Kas Kecil</b> {runId}` sebagai teks

### Account Name dengan karakter non-ASCII disimpan apa adanya saat Edit
103. Admin A mengirim Edit akun `NAE-{runId}` dengan Account Code `NAE-{runId}`, Account Name `Café Ünïcode 北京 {runId}`, Account Function `Asset Cost`
104. Verifikasi akun `NAE-{runId}` tersimpan dengan Account Name persis `Café Ünïcode 北京 {runId}`, tanpa karakter non-ASCII yang diubah atau dibuang
