---
id: TC-FA-FACO-BE-153-status-activate-deactivate
title: "Activate dan Deactivate: idempotensi dan commit per akun"
layer: be-e2e
priority: Medium
caseType: Negative
status: draft
owner: BE
sourceRules: [R-04, "§7.3#b5", "§[F-FACO-03] Activate Account#p1", "§[F-FACO-03] Activate Account#r2", "§[F-FACO-04] Deactivate Account#r3", "§9.4.2#r10", "§9.4.2#r13", EB-CON-3, EB-EDG-1]
smoke: []
dependsOn: []
trace:
  R-04: [3, 4, 7]
  "§7.3#b5": [7, 8, 11, 12, 17, 20]
  "§[F-FACO-03] Activate Account#p1": [4, 15, 16, 17, 20, 32]
  "§[F-FACO-03] Activate Account#r2": [7, 8]
  "§[F-FACO-04] Deactivate Account#r3": [11, 12]
  "§9.4.2#r10": [7, 8]
  "§9.4.2#r13": [11, 12]
  EB-CON-3: [23, 24, 27, 28, 32, 36]
  EB-EDG-1: [7, 8, 11, 12, 32, 36]
---

# Activate dan Deactivate: idempotensi dan commit per akun

## Prerequisites
- Aktor: Admin A dan Admin B, keduanya Total Control dengan cakupan seluruh client.
- Data:
  - DU-153-1: Account Code `AKT-{runId}`, Account Name `Kas Akan Diaktifkan {runId}`, Account Function `Asset Cost`, Status `Inactive`.
  - DU-153-2: Account Code `ACT-{runId}`, Account Name `Kas Sudah Aktif {runId}`, Account Function `Asset Cost`, Status `Active`.
  - DU-153-3: Account Code `NAK-{runId}`, Account Name `Kas Sudah Nonaktif {runId}`, Account Function `Asset Cost`, Status `Inactive`.
  - DU-153-4: Account Code `BLA-{runId}`, Account Name `Kas Bulk Satu {runId}`, Account Function `Asset Cost`, Status `Inactive`.
  - DU-153-5: Account Code `BLB-{runId}`, Account Name `Kas Bulk Dua {runId}`, Account Function `Asset Cost`, Status `Inactive`.
  - DU-153-6: Account Code `BLC-{runId}`, Account Name `Kas Bulk Tiga {runId}`, Account Function `Asset Cost`, Status `Active`.
  - DU-153-7: Account Code `CAA-{runId}`, Account Name `Kas Aktif Semua Satu {runId}`, Account Function `Asset Cost`, Status `Active`.
  - DU-153-8: Account Code `CAB-{runId}`, Account Name `Kas Aktif Semua Dua {runId}`, Account Function `Asset Cost`, Status `Active`.
  - DU-153-9: Account Code `CNA-{runId}`, Account Name `Kas Aktivasi Serentak {runId}`, Account Function `Asset Cost`, Status `Inactive`.
  - DU-153-10: Account Code `CND-{runId}`, Account Name `Kas Deaktivasi Serentak {runId}`, Account Function `Asset Cost`, Status `Active`.
  - DU-153-11: Account Code `DLA-{runId}`, Account Name `Kas Dihapus Lalu Diaktifkan {runId}`, Account Function `Asset Cost`, Status `Inactive`.
  - DU-153-12: Account Code `DLD-{runId}`, Account Name `Kas Dihapus Lalu Dinonaktifkan {runId}`, Account Function `Asset Cost`, Status `Active`.
- Kondisi:
  - Semua akun di atas belum pernah diekspor dan tidak dipakai Asset Class (Used By 0), sehingga Deactivate dan Delete tidak diblokir.

## Test Steps

### Activate akun Inactive menjadi Active dan tercatat per akun
1. Admin A mencatat jumlah entri log akun `AKT-{runId}` pada Changelog, pada System Log milik Admin A, dan pada Activity Log
2. Admin A mengirim Activate atas akun `AKT-{runId}`
3. Verifikasi akun `AKT-{runId}` berstatus `Active`
4. Verifikasi jumlah entri log akun `AKT-{runId}` bertambah satu pada masing-masing dari ketiga surface

### Activate atas akun yang sudah Active idempotent
5. Admin A mencatat jumlah entri log akun `ACT-{runId}` pada Changelog, pada System Log milik Admin A, dan pada Activity Log
6. Admin A mengirim Activate atas akun `ACT-{runId}`
7. Verifikasi permintaan berhasil tanpa mengubah data: akun `ACT-{runId}` tetap `Active` dengan Account Name `Kas Sudah Aktif {runId}`
8. Verifikasi jumlah entri log akun `ACT-{runId}` tidak bertambah pada ketiga surface

### Deactivate atas akun yang sudah Inactive idempotent
9. Admin A mencatat jumlah entri log akun `NAK-{runId}` pada Changelog, pada System Log milik Admin A, dan pada Activity Log
10. Admin A mengirim Deactivate atas akun `NAK-{runId}`
11. Verifikasi permintaan berhasil tanpa mengubah data: akun `NAK-{runId}` tetap `Inactive` dengan Account Name `Kas Sudah Nonaktif {runId}`
12. Verifikasi jumlah entri log akun `NAK-{runId}` tidak bertambah pada ketiga surface

### Bulk Activate pada seleksi campuran commit per akun dan melewati akun yang sudah Active
13. Admin A mencatat jumlah entri log akun `BLA-{runId}`, `BLB-{runId}`, dan `BLC-{runId}` pada Changelog, pada System Log milik Admin A, dan pada Activity Log
14. Admin A mengirim Activate bulk atas akun `BLA-{runId}`, `BLB-{runId}`, dan `BLC-{runId}`
15. Verifikasi akun `BLA-{runId}` dan `BLB-{runId}` berstatus `Active`
16. Verifikasi jumlah entri log akun `BLA-{runId}` dan akun `BLB-{runId}` masing-masing bertambah satu pada setiap surface, sehingga data dan ketiga log tiap akun tercatat sendiri-sendiri
17. Verifikasi akun `BLC-{runId}` tetap `Active` dan jumlah entri log akun itu tidak bertambah, karena sudah berstatus target

### Bulk Activate atas akun yang seluruhnya sudah Active tidak mengubah data
18. Admin A mencatat jumlah entri log akun `CAA-{runId}` dan `CAB-{runId}` pada Changelog, pada System Log milik Admin A, dan pada Activity Log
19. Admin A mengirim Activate bulk atas akun `CAA-{runId}` dan `CAB-{runId}`
20. Verifikasi akun `CAA-{runId}` dan `CAB-{runId}` tetap `Active`, dan jumlah entri log kedua akun tidak bertambah pada ketiga surface

### Dua admin meng-Activate akun yang sama serentak
21. Admin A mencatat jumlah entri log akun `CNA-{runId}` pada Changelog dan pada Activity Log
22. Admin A dan Admin B secara serentak mengirim Activate atas akun `CNA-{runId}`
23. Verifikasi kedua permintaan selesai tanpa kesalahan dan akun `CNA-{runId}` berstatus `Active`
24. Verifikasi jumlah entri log akun `CNA-{runId}` bertambah tepat satu pada Changelog dan pada Activity Log

### Dua admin meng-Deactivate akun yang sama serentak
25. Admin A mencatat jumlah entri log akun `CND-{runId}` pada Changelog dan pada Activity Log
26. Admin A dan Admin B secara serentak mengirim Deactivate atas akun `CND-{runId}`
27. Verifikasi kedua permintaan selesai tanpa kesalahan dan akun `CND-{runId}` berstatus `Inactive`
28. Verifikasi jumlah entri log akun `CND-{runId}` bertambah tepat satu pada Changelog dan pada Activity Log

### Activate dan Deactivate atas akun yang sudah dihapus admin lain tidak berefek
29. Admin A menghapus akun `DLA-{runId}`
30. Admin A mencatat jumlah entri Changelog dengan Account Code `DLA-{runId}`
31. Admin B mengirim Activate atas akun `DLA-{runId}`
32. Verifikasi permintaan Admin B tidak mengubah data: tidak ada akun dengan Account Code `DLA-{runId}`, dan jumlah entri Changelog dengan Account Code `DLA-{runId}` tidak bertambah
33. Admin A menghapus akun `DLD-{runId}`
34. Admin A mencatat jumlah entri Changelog dengan Account Code `DLD-{runId}`
35. Admin B mengirim Deactivate atas akun `DLD-{runId}`
36. Verifikasi permintaan Admin B tidak mengubah data: tidak ada akun dengan Account Code `DLD-{runId}`, dan jumlah entri Changelog dengan Account Code `DLD-{runId}` tidak bertambah
