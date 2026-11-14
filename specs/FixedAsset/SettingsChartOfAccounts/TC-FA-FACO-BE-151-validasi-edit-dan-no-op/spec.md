---
id: TC-FA-FACO-BE-151-validasi-edit-dan-no-op
title: "Validasi server Edit Account, Edit tanpa perubahan, dan Edit bersamaan"
layer: be-e2e
priority: Medium
caseType: Negative
status: draft
owner: BE
sourceRules: [FACO-LOGIC-07d, N-08, R-02, R-03, "§8#b1", "§[F-FACO-02] Edit Account#b2", "§[F-FACO-02] Edit Account#b3", "§[F-FACO-02] Edit Account#r7", "§[F-FACO-02] Edit Account#r15", "§[F-FACO-02] Edit Account#r16", "§[F-FACO-02] Edit Account#r17", "§9.4.2#r9", "§9.9#r1", "§9.9#r2", "§9.9#r3", EB-FRM-6@form-edit-account, EB-FRM-8@account-code, EB-FRM-8@account-name, EB-FRM-8@account-function, EB-ERR-4, EB-CON-1]
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
  "§[F-FACO-02] Edit Account#r7": [7, 8]
  "§[F-FACO-02] Edit Account#r15": [50, 56]
  "§[F-FACO-02] Edit Account#r16": [51]
  "§[F-FACO-02] Edit Account#r17": [64, 65, 71, 72]
  "§9.4.2#r9": [49, 50, 51, 55, 56]
  "§9.9#r1": [20, 22, 24, 26, 28, 34, 40, 44]
  "§9.9#r2": [30, 32, 36, 42]
  "§9.9#r3": [38]
  EB-FRM-6@form-edit-account: [28, 32]
  EB-FRM-8@account-code: [20, 22, 24, 26, 28, 34, 40, 44, 67]
  EB-FRM-8@account-name: [30, 32, 36, 42, 69]
  EB-FRM-8@account-function: [38]
  EB-ERR-4: [20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 59]
  EB-CON-1: [49, 50, 56, 62]
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
- Kondisi:
  - Semua akun di atas belum pernah diekspor (Last Used in Journal kosong) dan tidak dipakai Asset Class (Used By 0), sehingga tidak ada field yang terkunci.

## Test Steps

### Edit dengan nilai baru tersimpan
1. Admin A mengirim Edit akun `SWA-{runId}` dengan Account Code `SWB-{runId}`, Account Name `Beban Sewa Gedung {runId}`, Account Function `Accumulated Depreciation`
2. Verifikasi akun dengan Account Code `SWB-{runId}` tersimpan dengan Account Name `Beban Sewa Gedung {runId}` dan Account Function `Accumulated Depreciation`, dan tidak ada lagi akun dengan Account Code `SWA-{runId}`

### Edit tanpa perubahan nilai tidak mengubah data dan tidak menulis log
3. Admin A mencatat jumlah entri log akun `NOP-{runId}` pada Changelog, pada System Log milik Admin A, dan pada Activity Log
4. Admin A mengirim Edit akun `NOP-{runId}` dengan Account Code `NOP-{runId}`, Account Name `Kas Kecil Pusat {runId}`, Account Function `Asset Cost`, semuanya identik dengan nilai tersimpan
5. Verifikasi permintaan berhasil dengan respons tanpa konten (`No Content`), nilai akun tidak berubah, dan Account Code `NOP-{runId}` tidak ditolak sebagai duplikat dari akun itu sendiri
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
