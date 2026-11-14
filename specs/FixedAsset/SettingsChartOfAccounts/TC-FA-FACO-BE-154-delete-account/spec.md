---
id: TC-FA-FACO-BE-154-delete-account
title: "Delete Account: hard delete, akun sudah terhapus, dan tanpa efek pada data lain"
layer: be-e2e
priority: Medium
caseType: Negative
status: draft
owner: BE
sourceRules: [R-06, "§7.3#b4", "§[F-FACO-05] Delete Account#p2", "§[F-FACO-05] Delete Account#r10", "§9.4.2#r19", EB-ERR-3, EB-EDG-1, EB-EDG-3]
smoke: []
dependsOn: []
trace:
  R-06: [6, 9]
  "§7.3#b4": [13, 19, 24]
  "§[F-FACO-05] Delete Account#p2": [17, 18]
  "§[F-FACO-05] Delete Account#r10": [9, 13]
  "§9.4.2#r19": [9, 13]
  EB-ERR-3: [13, 24]
  EB-EDG-1: [9, 13, 24]
  EB-EDG-3: [2, 3, 4]
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
7. Admin A mencatat jumlah entri Changelog dan jumlah entri Activity Log dengan Account Code `RPT-{runId}`
8. Admin A mengirim Delete atas akun `RPT-{runId}` sekali lagi
9. Verifikasi permintaan ulangan tidak mengubah data: tidak ada akun dengan Account Code `RPT-{runId}`, dan jumlah entri Changelog serta Activity Log dengan Account Code `RPT-{runId}` tidak bertambah

### Delete atas akun yang sudah dihapus admin lain
10. Admin A mengirim Delete atas akun `OTH-{runId}`
11. Admin B mencatat jumlah entri Changelog dan jumlah entri Activity Log dengan Account Code `OTH-{runId}`
12. Admin B mengirim Delete atas akun `OTH-{runId}`
13. Verifikasi permintaan Admin B ditangani sebagai akun yang tidak lagi tersedia tanpa mengubah data: tidak ada akun dengan Account Code `OTH-{runId}`, dan jumlah entri Changelog serta Activity Log dengan Account Code `OTH-{runId}` tidak bertambah

### Bulk Delete melewati akun yang sudah dihapus admin lain
14. Admin A mengirim Delete atas akun `BDC-{runId}`
15. Admin B mencatat jumlah entri Changelog dan jumlah entri Activity Log akun `BDA-{runId}`, `BDB-{runId}`, dan `BDC-{runId}`
16. Admin B mengirim Delete bulk atas akun `BDA-{runId}`, `BDB-{runId}`, dan `BDC-{runId}`
17. Verifikasi tidak ada lagi akun dengan Account Code `BDA-{runId}` dan tidak ada lagi akun dengan Account Code `BDB-{runId}`
18. Verifikasi jumlah entri Changelog dan Activity Log akun `BDA-{runId}` dan akun `BDB-{runId}` masing-masing bertambah satu, sehingga tiap akun yang terhapus tercatat sendiri-sendiri
19. Verifikasi akun `BDC-{runId}` dilewati tanpa log: jumlah entri Changelog dan Activity Log akun itu tidak bertambah

### Bulk Delete atas akun yang seluruhnya sudah dihapus tidak berefek
20. Admin A mengirim Delete atas akun `ALA-{runId}`
21. Admin A mengirim Delete atas akun `ALB-{runId}`
22. Admin B mencatat jumlah entri Changelog dan jumlah entri Activity Log akun `ALA-{runId}` dan `ALB-{runId}`
23. Admin B mengirim Delete bulk atas akun `ALA-{runId}` dan `ALB-{runId}`
24. Verifikasi permintaan bulk tidak mengubah data dan tidak menulis log: tidak ada akun `ALA-{runId}` maupun `ALB-{runId}`, dan jumlah entri Changelog serta Activity Log kedua akun tidak bertambah
