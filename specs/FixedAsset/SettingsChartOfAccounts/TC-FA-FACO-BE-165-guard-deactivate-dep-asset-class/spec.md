---
id: TC-FA-FACO-BE-165-guard-deactivate-dep-asset-class
title: "Guard Deactivate untuk akun yang dipakai Asset Class"
layer: be-e2e
priority: Medium
caseType: Negative
status: ready-for-automation
owner: BE
sourceRules: [FACO-LOGIC-02c, N-02, R-05, "§[F-FACO-04] Deactivate Account#b2", "§[F-FACO-04] Deactivate Account#r1", "§[F-FACO-04] Deactivate Account#r6", "§9.4.2#r11", "§9.4.2#r12", "§9.4.2#r34"]
smoke: []
dependsOn: ["Asset Class: pemakaian akun pada field akun Asset Class (Used By)"]
trace:
  FACO-LOGIC-02c: [3, 6, 8, 12, 16, 19, 24]
  N-02: [3, 6, 8, 10]
  R-05: [24, 25, 29, 30]
  "§[F-FACO-04] Deactivate Account#b2": [24, 25, 29, 30]
  "§[F-FACO-04] Deactivate Account#r1": [3, 4, 6, 8, 10, 15, 16, 19]
  "§[F-FACO-04] Deactivate Account#r6": [24, 25, 30]
  "§9.4.2#r11": [3, 4]
  "§9.4.2#r12": [24, 25, 30]
  "§9.4.2#r34": [10]
---

# Guard Deactivate untuk akun yang dipakai Asset Class

## Prerequisites
- Aktor: Admin A, Admin B, dan pemanggil terotorisasi, ketiganya Total Control dengan cakupan seluruh client.
- Data:
  - DU-165-1: User `Maya Pengelola {runId}`, Access Level `Total Control`, cakupan seluruh client.
  - DU-165-2: User `Rudi Integrasi {runId}`, Access Level `Total Control`, cakupan seluruh client, pemanggil terotorisasi yang mengirim request langsung.
  - DU-165-3: User `Budi Pengelola {runId}`, Access Level `Total Control`, cakupan seluruh client.
  - DU-165-4: Account Code `DGA-{runId}`, Account Name `Mesin Bubut {runId}`, Account Function `Asset Cost`, Status `Active`, Used By 1, dipakai DU-165-9.
  - DU-165-5: Account Code `DGB-{runId}`, Account Name `Akumulasi Mesin {runId}`, Account Function `Accumulated Depreciation`, Status `Active`, Used By 2, dipakai DU-165-9 dan DU-165-10.
  - DU-165-6: Account Code `DGC-{runId}`, Account Name `Beban Mesin Lama {runId}`, Account Function `Depreciation Expense`, Status `Active`, Used By 1, dipakai DU-165-10.
  - DU-165-7: Account Code `DGD-{runId}`, Account Name `Laba Pelepasan Tersedia {runId}`, Account Function `Gain on Disposal`, Status `Active`, Used By 0.
  - DU-165-8: Account Code `DGF-{runId}`, Account Name `Kas Bulk Terbuka {runId}`, Account Function `Asset Cost`, Status `Active`, Used By 0.
  - DU-165-9: Asset Class `Kelas Mesin {runId}`, Status `Active`; Asset Cost `DGA-{runId}`, Accumulated Depreciation `DGB-{runId}`.
  - DU-165-10: Asset Class `Kelas Kantor {runId}`, Status `Inactive`; Accumulated Depreciation `DGB-{runId}`, Depreciation Expense `DGC-{runId}`.
  - DU-165-11: Account Code `RCK-{runId}`, Account Name `Beban Cek Ulang {runId}`, Account Function `Depreciation Expense`, Status `Active`, Used By 0.
  - DU-165-12: Account Code `RCL-{runId}`, Account Name `Kas Cek Ulang Satu {runId}`, Account Function `Asset Cost`, Status `Active`, Used By 0.
  - DU-165-13: Account Code `RCM-{runId}`, Account Name `Kas Cek Ulang Dua {runId}`, Account Function `Asset Cost`, Status `Active`, Used By 0.
  - DU-165-14: Asset Class `Kelas Cek Ulang {runId}`, Status `Active`, belum memakai akun `RCK-{runId}` maupun `RCL-{runId}`.
- Kondisi:
  - Semua akun di atas belum pernah diekspor, sehingga satu-satunya penghalang Deactivate adalah pemakaian Asset Class.

## Test Steps

### Deactivate akun yang dipakai satu Asset Class ditolak
1. Admin A mencatat jumlah entri log akun `DGA-{runId}` pada Changelog, pada System Log milik Admin A, dan pada Activity Log
2. Admin A mengirim Deactivate atas akun `DGA-{runId}`, yang Used By-nya 1
3. Verifikasi Deactivate ditolak karena akun dipakai Asset Class dan akun `DGA-{runId}` tetap berstatus `Active`
4. Verifikasi jumlah entri log akun `DGA-{runId}` tidak bertambah pada ketiga surface, karena penolakan tidak menulis log

### Deactivate akun yang dipakai oleh lebih dari satu Asset Class ditolak
5. Admin A mengirim Deactivate atas akun `DGB-{runId}`, yang dipakai dua Asset Class dan Used By-nya 2
6. Verifikasi Deactivate ditolak dan akun `DGB-{runId}` tetap berstatus `Active`

### Asset Class berstatus Inactive tetap dihitung sebagai pemakai
7. Admin A mengirim Deactivate atas akun `DGC-{runId}`, yang hanya dipakai Asset Class berstatus `Inactive`
8. Verifikasi Deactivate ditolak dan akun `DGC-{runId}` tetap berstatus `Active`, karena Asset Class dihitung tanpa melihat statusnya

### Request langsung tanpa melalui UI tetap ditolak server
9. Pemanggil terotorisasi (DU-165-2) mengirim Deactivate lewat request langsung atas akun `DGA-{runId}`
10. Verifikasi request langsung ditolak server walau tidak melalui UI, dan akun `DGA-{runId}` tetap berstatus `Active`

### Akun yang tidak dipakai dapat dinonaktifkan sebagai pembanding
11. Admin A mengirim Deactivate atas akun `DGD-{runId}`, yang Used By-nya 0
12. Verifikasi akun `DGD-{runId}` berstatus `Inactive` dan memiliki tepat satu entri log dengan Field `Status`, Old Value `Active`, dan New Value `Inactive` pada ketiga surface

### Bulk Deactivate melewati akun yang dipakai dan memproses akun lainnya
13. Admin A mencatat jumlah entri log akun `DGF-{runId}` dan `DGA-{runId}` pada Changelog, pada System Log milik Admin A, dan pada Activity Log
14. Admin A mengirim Deactivate bulk atas akun `DGF-{runId}` yang tidak dipakai dan akun `DGA-{runId}` yang dipakai
15. Verifikasi akun `DGF-{runId}` berstatus `Inactive` dengan jumlah entri log bertambah satu pada setiap surface
16. Verifikasi akun `DGA-{runId}` dilewati: tetap berstatus `Active` dan jumlah entri log akun itu tidak bertambah

### Bulk Deactivate yang seluruh akunnya dipakai tidak mengubah apa pun
17. Admin A mencatat jumlah entri log akun `DGA-{runId}` dan `DGB-{runId}` pada Changelog, pada System Log milik Admin A, dan pada Activity Log
18. Admin A mengirim Deactivate bulk atas akun `DGA-{runId}` dan `DGB-{runId}`
19. Verifikasi kedua akun tetap berstatus `Active` dan jumlah entri log keduanya tidak bertambah pada ketiga surface

### Akun menjadi dipakai antara pengecekan awal dan Confirm: cek ulang menolak
20. Admin A membaca akun `RCK-{runId}` yang Used By-nya 0 dan boleh dinonaktifkan
21. Admin A mencatat jumlah entri log akun `RCK-{runId}` pada Changelog, pada System Log milik Admin A, dan pada Activity Log
22. Admin B menetapkan akun `RCK-{runId}` pada field Depreciation Expense Asset Class `Kelas Cek Ulang {runId}`, sehingga Used By akun itu menjadi 1
23. Admin A mengirim Deactivate atas akun `RCK-{runId}`, sebagai Confirm atas pengecekan awal yang sudah basi
24. Verifikasi Confirm ditolak oleh cek ulang guard saat Confirm dan akun `RCK-{runId}` tetap berstatus `Active`, walau pengecekan awal menyatakan akun itu lolos
25. Verifikasi jumlah entri log akun `RCK-{runId}` tidak bertambah pada ketiga surface, sehingga cek ulang dan perubahan status tidak meninggalkan setengah hasil

### Bulk Confirm: akun yang menjadi dipakai dilewati dan akun lain di-commit per akun
26. Admin A mencatat jumlah entri log akun `RCL-{runId}` dan `RCM-{runId}` pada Changelog, pada System Log milik Admin A, dan pada Activity Log
27. Admin B menetapkan akun `RCL-{runId}` pada field Asset Cost Asset Class `Kelas Cek Ulang {runId}`, sehingga Used By akun itu menjadi 1
28. Admin A mengirim Deactivate bulk atas akun `RCL-{runId}` dan `RCM-{runId}`, sebagai Confirm atas pengecekan awal yang menyatakan keduanya lolos
29. Verifikasi akun `RCM-{runId}` berstatus `Inactive` dengan jumlah entri log bertambah satu pada setiap surface
30. Verifikasi akun `RCL-{runId}` dilewati oleh cek ulang: tetap berstatus `Active` dan jumlah entri log akun itu tidak bertambah
