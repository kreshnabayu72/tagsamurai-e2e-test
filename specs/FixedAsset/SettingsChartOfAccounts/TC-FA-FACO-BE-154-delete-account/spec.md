---
id: TC-FA-FACO-BE-154-delete-account
title: "Delete Account: hard delete, akun sudah terhapus, dan tanpa efek pada data lain"
layer: be-e2e
priority: Medium
caseType: Negative
status: ready-for-automation
owner: BE
sourceRules: [R-06, "§7.3#b4", "§[F-FACO-05] Delete Account#p2", "§[F-FACO-05] Delete Account#r10", "§9.4.2#r19", EB-ERR-3, EB-EDG-1, EB-EDG-3, "§[F-FACO-02] Edit Account#r7", "§9.4.2#r41"]
smoke: []
dependsOn: []
trace:
  R-06: [6, 9]
  "§7.3#b4": [13, 19, 24, 28, 29, 33, 34, 38, 39, 44, 49]
  "§[F-FACO-05] Delete Account#p2": [17, 18]
  "§[F-FACO-05] Delete Account#r10": [9, 13]
  "§9.4.2#r19": [9, 13]
  EB-ERR-3: [13, 24]
  EB-EDG-1: [9, 13, 24]
  EB-EDG-3: [2, 3, 4]
  "§[F-FACO-02] Edit Account#r7": [28, 29, 34, 39]
  "§9.4.2#r41": [28, 29, 34, 39]
---

# Delete Account: hard delete, akun sudah terhapus, dan tanpa efek pada data lain

## Prerequisites
- Aktor: Admin A dan Admin B, keduanya Total Control dengan cakupan seluruh client.
- Data:
  - DU-154-1: Account Code `HDA-{runId}`, Account Name `Beban Bunga {runId}`, Account Function `Depreciation Expense`.
  - DU-154-2: Account Code `HDB-{runId}`, Account Name `Beban Bunga Pembanding {runId}`, Account Function `Depreciation Expense`.
  - DU-154-3: Account Code `RPT-{runId}`, Account Name `Kas Hapus Ulang {runId}`, Account Function `Asset Cost`.
  - DU-154-4: Account Code `OTH-{runId}`, Account Name `Kas Hapus Admin Lain {runId}`, Account Function `Asset Cost`.
  - DU-154-5: Account Code `BDA-{runId}`, Account Name `Kas Bulk Hapus Satu {runId}`, Account Function `Asset Cost`.
  - DU-154-6: Account Code `BDB-{runId}`, Account Name `Kas Bulk Hapus Dua {runId}`, Account Function `Asset Cost`.
  - DU-154-7: Account Code `BDC-{runId}`, Account Name `Kas Bulk Hapus Tiga {runId}`, Account Function `Asset Cost`.
  - DU-154-8: Account Code `ALA-{runId}`, Account Name `Kas Terhapus Semua Satu {runId}`, Account Function `Asset Cost`.
  - DU-154-9: Account Code `ALB-{runId}`, Account Name `Kas Terhapus Semua Dua {runId}`, Account Function `Asset Cost`.
  - DU-154-10: Account Code `EDX-{runId}`, Account Name `Kas Edit Terhapus {runId}`, Account Function `Asset Cost`.
  - DU-154-12: Account Code `AVD-{runId}`, Account Name `Kas Aktivasi Terhapus {runId}`, Account Function `Asset Cost`, Status `Inactive`.
  - DU-154-13: Account Code `AVE-{runId}`, Account Name `Kas Aktivasi Target {runId}`, Account Function `Asset Cost`, Status `Inactive`.
  - DU-154-14: Account Code `DVD-{runId}`, Account Name `Kas Deaktivasi Terhapus {runId}`, Account Function `Asset Cost`, Status `Active`.
  - DU-154-15: Account Code `DVE-{runId}`, Account Name `Kas Deaktivasi Target {runId}`, Account Function `Asset Cost`, Status `Active`.
  - DU-154-16: Account Code `ZAA-{runId}`, Account Name `Kas Aktivasi Semua Terhapus Satu {runId}`, Account Function `Asset Cost`, Status `Inactive`.
  - DU-154-17: Account Code `ZAB-{runId}`, Account Name `Kas Aktivasi Semua Terhapus Dua {runId}`, Account Function `Asset Cost`, Status `Inactive`.
  - DU-154-18: Account Code `ZDA-{runId}`, Account Name `Kas Deaktivasi Semua Terhapus Satu {runId}`, Account Function `Asset Cost`, Status `Active`.
  - DU-154-19: Account Code `ZDB-{runId}`, Account Name `Kas Deaktivasi Semua Terhapus Dua {runId}`, Account Function `Asset Cost`, Status `Active`.
- Kondisi:
  - Semua akun di atas belum pernah diekspor, tidak dipakai Asset Class (Used By 0), dan bukan nilai default company, sehingga lolos kedua guard Delete.

## Test Steps

### Delete menghapus permanen akun, kode akun tetap di log, dan akun lain tidak terdampak
1. Admin A mengirim Delete atas akun `HDA-{runId}`
2. Verifikasi tidak ada lagi akun dengan Account Code `HDA-{runId}`
3. Verifikasi akun pembanding `HDB-{runId}` tetap ada dengan Account Name `Beban Bunga Pembanding {runId}`
4. Verifikasi Changelog tetap memuat entri dengan Account Code `HDA-{runId}`, karena kode akun tersimpan sebagai snapshot di log walau akun sudah terhapus

### Delete ulangan atas akun yang sudah terhapus tidak berefek
5. Admin A mengirim Delete atas akun `RPT-{runId}`
6. Verifikasi tidak ada lagi akun dengan Account Code `RPT-{runId}`
7. Admin A mencatat jumlah entri log akun `RPT-{runId}` pada Changelog, pada System Log milik Admin A, dan pada Activity Log
8. Admin A mengirim Delete atas akun `RPT-{runId}` sekali lagi
9. Verifikasi permintaan ulangan tidak mengubah data: tidak ada akun dengan Account Code `RPT-{runId}`, dan jumlah entri log akun itu tidak bertambah pada ketiga surface

### Delete atas akun yang sudah dihapus admin lain
10. Admin A mengirim Delete atas akun `OTH-{runId}`
11. Admin B mencatat jumlah entri log akun `OTH-{runId}` pada Changelog, pada System Log milik Admin B, dan pada Activity Log
12. Admin B mengirim Delete atas akun `OTH-{runId}`
13. Verifikasi permintaan Admin B ditangani sebagai akun yang tidak lagi tersedia tanpa mengubah data: tidak ada akun dengan Account Code `OTH-{runId}`, dan jumlah entri log akun itu tidak bertambah pada ketiga surface

### Bulk Delete melewati akun yang sudah dihapus admin lain
14. Admin A mengirim Delete atas akun `BDC-{runId}`
15. Admin B mencatat jumlah entri log akun `BDA-{runId}`, `BDB-{runId}`, dan `BDC-{runId}` pada Changelog, pada System Log milik Admin B, dan pada Activity Log
16. Admin B mengirim Delete bulk atas akun `BDA-{runId}`, `BDB-{runId}`, dan `BDC-{runId}`
17. Verifikasi tidak ada lagi akun dengan Account Code `BDA-{runId}` dan tidak ada lagi akun dengan Account Code `BDB-{runId}`
18. Verifikasi jumlah entri log akun `BDA-{runId}` dan akun `BDB-{runId}` pada Changelog, pada System Log milik Admin B, dan pada Activity Log masing-masing bertambah satu, sehingga tiap akun yang terhapus tercatat sendiri-sendiri pada ketiga surface
19. Verifikasi akun `BDC-{runId}` dilewati tanpa log: jumlah entri log akun itu tidak bertambah pada ketiga surface

### Bulk Delete atas akun yang seluruhnya sudah dihapus tidak berefek
20. Admin A mengirim Delete atas akun `ALA-{runId}`
21. Admin A mengirim Delete atas akun `ALB-{runId}`
22. Admin B mencatat jumlah entri log akun `ALA-{runId}` dan `ALB-{runId}` pada Changelog, pada System Log milik Admin B, dan pada Activity Log
23. Admin B mengirim Delete bulk atas akun `ALA-{runId}` dan `ALB-{runId}`
24. Verifikasi permintaan bulk tidak mengubah data dan tidak menulis log: tidak ada akun `ALA-{runId}` maupun `ALB-{runId}`, dan jumlah entri log kedua akun tidak bertambah pada ketiga surface

### Save Edit atas akun yang sudah dihapus admin lain tidak mengubah data dan tidak menulis log
25. Admin A mengirim Delete atas akun `EDX-{runId}`
26. Admin B mencatat jumlah entri log akun `EDX-{runId}` pada Changelog, pada System Log milik Admin B, dan pada Activity Log
27. Admin B mengirim Edit akun `EDX-{runId}` dengan Account Name `Kas Edit Terlambat {runId}`
28. Verifikasi permintaan Admin B tidak mengubah data: tidak ada akun dengan Account Code `EDX-{runId}` dan tidak ada akun dengan Account Name `Kas Edit Terlambat {runId}`
29. Verifikasi jumlah entri log akun `EDX-{runId}` tidak bertambah pada ketiga surface

### Bulk Activate melewati akun yang sudah dihapus admin lain tanpa log
30. Admin A mengirim Delete atas akun `AVD-{runId}`
31. Admin B mencatat jumlah entri log akun `AVD-{runId}` dan `AVE-{runId}` pada Changelog, pada System Log milik Admin B, dan pada Activity Log
32. Admin B mengirim Activate bulk atas akun `AVD-{runId}` dan `AVE-{runId}`
33. Verifikasi akun `AVE-{runId}` berstatus `Active` dan jumlah entri log akun itu bertambah satu pada masing-masing dari ketiga surface
34. Verifikasi akun `AVD-{runId}` dilewati tanpa log: tidak ada akun dengan Account Code `AVD-{runId}` dan jumlah entri log akun itu tidak bertambah pada ketiga surface

### Bulk Deactivate melewati akun yang sudah dihapus admin lain tanpa log
35. Admin A mengirim Delete atas akun `DVD-{runId}`
36. Admin B mencatat jumlah entri log akun `DVD-{runId}` dan `DVE-{runId}` pada Changelog, pada System Log milik Admin B, dan pada Activity Log
37. Admin B mengirim Deactivate bulk atas akun `DVD-{runId}` dan `DVE-{runId}`
38. Verifikasi akun `DVE-{runId}` berstatus `Inactive` dan jumlah entri log akun itu bertambah satu pada masing-masing dari ketiga surface
39. Verifikasi akun `DVD-{runId}` dilewati tanpa log: tidak ada akun dengan Account Code `DVD-{runId}` dan jumlah entri log akun itu tidak bertambah pada ketiga surface
### Bulk Activate atas akun yang seluruhnya sudah dihapus tidak berefek
40. Admin A mengirim Delete atas akun `ZAA-{runId}`
41. Admin A mengirim Delete atas akun `ZAB-{runId}`
42. Admin B mencatat jumlah entri log akun `ZAA-{runId}` dan `ZAB-{runId}` pada Changelog, pada System Log milik Admin B, dan pada Activity Log
43. Admin B mengirim Activate bulk atas akun `ZAA-{runId}` dan `ZAB-{runId}`
44. Verifikasi permintaan bulk tidak mengubah data dan tidak menulis log: tidak ada akun `ZAA-{runId}` maupun `ZAB-{runId}`, dan jumlah entri log kedua akun tidak bertambah pada ketiga surface

### Bulk Deactivate atas akun yang seluruhnya sudah dihapus tidak berefek
45. Admin A mengirim Delete atas akun `ZDA-{runId}`
46. Admin A mengirim Delete atas akun `ZDB-{runId}`
47. Admin B mencatat jumlah entri log akun `ZDA-{runId}` dan `ZDB-{runId}` pada Changelog, pada System Log milik Admin B, dan pada Activity Log
48. Admin B mengirim Deactivate bulk atas akun `ZDA-{runId}` dan `ZDB-{runId}`
49. Verifikasi permintaan bulk tidak mengubah data dan tidak menulis log: tidak ada akun `ZDA-{runId}` maupun `ZDB-{runId}`, dan jumlah entri log kedua akun tidak bertambah pada ketiga surface
