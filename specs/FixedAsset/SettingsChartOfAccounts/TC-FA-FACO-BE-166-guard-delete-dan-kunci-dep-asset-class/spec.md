---
id: TC-FA-FACO-BE-166-guard-delete-dan-kunci-dep-asset-class
title: "Guard Delete dan kunci Account Function untuk akun yang dipakai Asset Class"
layer: be-e2e
priority: Medium
caseType: Negative
status: ready-for-automation
owner: BE
sourceRules: [FACO-LOGIC-03b, FACO-LOGIC-03f, FACO-LOGIC-04b, FACO-LOGIC-04e, N-04, "§[F-FACO-02] Edit Account#r2", "§[F-FACO-02] Edit Account#r12", "§[F-FACO-05] Delete Account#b2", "§[F-FACO-05] Delete Account#r2", "§[F-FACO-05] Delete Account#r14", "§9.4.2#r6", "§9.4.2#r17"]
smoke: []
dependsOn: ["Asset Class: pemakaian akun pada field akun Asset Class (Used By)"]
trace:
  FACO-LOGIC-03b: [3, 6, 8, 10, 13, 14]
  FACO-LOGIC-03f: [19, 20, 24, 25]
  FACO-LOGIC-04b: [28, 31, 36]
  FACO-LOGIC-04e: [31, 36]
  N-04: [28, 29]
  "§[F-FACO-02] Edit Account#r2": [28, 29, 31]
  "§[F-FACO-02] Edit Account#r12": [36, 37]
  "§[F-FACO-05] Delete Account#b2": [19, 20, 24, 25]
  "§[F-FACO-05] Delete Account#r2": [3, 4, 6, 8, 13, 14]
  "§[F-FACO-05] Delete Account#r14": [19, 20, 25]
  "§9.4.2#r6": [28, 29, 31]
  "§9.4.2#r17": [3, 4]
---

# Guard Delete dan kunci Account Function untuk akun yang dipakai Asset Class

## Prerequisites
- Aktor: Admin A, Admin B, dan pemanggil terotorisasi, ketiganya Total Control dengan cakupan seluruh client.
- Data:
  - DU-166-1: User `Maya Pengelola {runId}`, Access Level `Total Control`, cakupan seluruh client.
  - DU-166-2: User `Rudi Integrasi {runId}`, Access Level `Total Control`, cakupan seluruh client, pemanggil terotorisasi yang mengirim request langsung.
  - DU-166-3: User `Budi Pengelola {runId}`, Access Level `Total Control`, cakupan seluruh client.
  - DU-166-4: Account Code `DHA-{runId}`, Account Name `Kas Mesin Utama {runId}`, Account Function `Asset Cost`, Status `Active`, Used By 1, dipakai DU-166-10.
  - DU-166-5: Account Code `DHB-{runId}`, Account Name `Akumulasi Mesin Utama {runId}`, Account Function `Accumulated Depreciation`, Status `Active`, Used By 2, dipakai DU-166-10 dan DU-166-11.
  - DU-166-6: Account Code `DHC-{runId}`, Account Name `Beban Mesin Lama {runId}`, Account Function `Depreciation Expense`, Status `Active`, Used By 1, dipakai DU-166-11.
  - DU-166-7: Account Code `DHD-{runId}`, Account Name `Laba Pelepasan Terbuka {runId}`, Account Function `Gain on Disposal`, Status `Active`, Used By 0.
  - DU-166-8: Account Code `DHE-{runId}`, Account Name `Rugi Pelepasan Terbuka {runId}`, Account Function `Loss on Disposal`, Status `Active`, Used By 0.
  - DU-166-9: Account Code `LKA-{runId}`, Account Name `Beban Kunci Pemakaian {runId}`, Account Function `Depreciation Expense`, Status `Active`, Used By 1, dipakai DU-166-10.
  - DU-166-10: Asset Class `Kelas Mesin Utama {runId}`, Status `Active`; Asset Cost `DHA-{runId}`, Accumulated Depreciation `DHB-{runId}`, Depreciation Expense `LKA-{runId}`.
  - DU-166-11: Asset Class `Kelas Kantor Lama {runId}`, Status `Inactive`; Accumulated Depreciation `DHB-{runId}`, Depreciation Expense `DHC-{runId}`.
  - DU-166-12: Account Code `RDK-{runId}`, Account Name `Kas Cek Ulang Hapus Satu {runId}`, Account Function `Asset Cost`, Status `Active`, Used By 0.
  - DU-166-13: Account Code `RDL-{runId}`, Account Name `Akumulasi Cek Ulang Satu {runId}`, Account Function `Accumulated Depreciation`, Status `Active`, Used By 0.
  - DU-166-14: Account Code `RDM-{runId}`, Account Name `Akumulasi Cek Ulang Dua {runId}`, Account Function `Accumulated Depreciation`, Status `Active`, Used By 0.
  - DU-166-15: Account Code `LKB-{runId}`, Account Name `Beban Kunci Berubah {runId}`, Account Function `Depreciation Expense`, Status `Active`, Used By 0.
  - DU-166-16: Asset Class `Kelas Cek Ulang Hapus {runId}`, Status `Active`, belum memakai akun `RDK-{runId}`, `RDL-{runId}`, maupun `LKB-{runId}`.
  - DU-166-17: Account Name `Beban Kunci Diubah {runId}`, nilai input Save Edit atas akun `LKB-{runId}` yang tidak boleh tersimpan.
- Kondisi:
  - Semua akun di atas belum pernah diekspor dan bukan nilai default company, sehingga Guard 1 tidak berlaku dan satu-satunya penghalang adalah pemakaian Asset Class.

## Test Steps

### Delete akun yang dipakai Asset Class ditolak oleh Guard 2
1. Admin A mencatat jumlah entri log akun `DHA-{runId}` pada Changelog, pada System Log milik Admin A, dan pada Activity Log
2. Admin A mengirim Delete atas akun `DHA-{runId}`, yang Used By-nya 1
3. Verifikasi Delete ditolak karena akun dipakai Asset Class dan akun `DHA-{runId}` masih ada dengan Status `Active`
4. Verifikasi jumlah entri log akun `DHA-{runId}` tidak bertambah pada ketiga surface, karena penolakan tidak menulis log

### Akun yang dipakai lebih dari satu Asset Class, atau hanya oleh Asset Class Inactive, tetap tidak dapat dihapus
5. Admin A mengirim Delete atas akun `DHB-{runId}`, yang dipakai dua Asset Class dan Used By-nya 2
6. Verifikasi Delete ditolak dan akun `DHB-{runId}` masih ada
7. Admin A mengirim Delete atas akun `DHC-{runId}`, yang hanya dipakai Asset Class berstatus `Inactive`
8. Verifikasi Delete ditolak dan akun `DHC-{runId}` masih ada, karena Asset Class dihitung tanpa melihat statusnya

### Akun yang tidak dipakai lolos Guard 2 dan terhapus
9. Admin A mengirim Delete atas akun `DHD-{runId}`, yang Used By-nya 0
10. Verifikasi tidak ada lagi akun dengan Account Code `DHD-{runId}` dan Changelog memuat tepat satu entri dengan Action `Delete`, Account Code `DHD-{runId}`, Old Value `DHD-{runId}`, dan New Value `—`

### Bulk Delete melewati akun yang dipakai dan menghapus akun lainnya
11. Admin A mencatat jumlah entri log akun `DHA-{runId}` pada Changelog, pada System Log milik Admin A, dan pada Activity Log
12. Admin A mengirim Delete bulk atas akun `DHE-{runId}` yang tidak dipakai dan akun `DHA-{runId}` yang dipakai
13. Verifikasi akun `DHE-{runId}` terhapus dan Changelog memuat tepat satu entri dengan Action `Delete` untuk akun itu
14. Verifikasi akun `DHA-{runId}` dilewati: masih ada, dan jumlah entri log akun itu tidak bertambah pada ketiga surface

### Akun menjadi dipakai antara pengecekan awal dan Confirm: cek ulang Delete menolak
15. Admin A membaca akun `RDK-{runId}` yang Used By-nya 0 dan boleh dihapus
16. Admin A mencatat jumlah entri log akun `RDK-{runId}` pada Changelog, pada System Log milik Admin A, dan pada Activity Log
17. Admin B menetapkan akun `RDK-{runId}` pada field Asset Cost Asset Class `Kelas Cek Ulang Hapus {runId}`, sehingga Used By akun itu menjadi 1
18. Admin A mengirim Delete atas akun `RDK-{runId}`, sebagai Confirm atas pengecekan awal yang sudah basi
19. Verifikasi Confirm ditolak oleh cek ulang guard saat Confirm dan akun `RDK-{runId}` masih ada, walau pengecekan awal menyatakan akun itu lolos
20. Verifikasi jumlah entri log akun `RDK-{runId}` tidak bertambah pada ketiga surface, sehingga cek ulang dan penghapusan tidak meninggalkan setengah hasil

### Bulk Confirm Delete: akun yang menjadi dipakai dilewati dan akun lain di-commit per akun
21. Admin A mencatat jumlah entri log akun `RDL-{runId}` dan `RDM-{runId}` pada Changelog, pada System Log milik Admin A, dan pada Activity Log
22. Admin B menetapkan akun `RDL-{runId}` pada field Accumulated Depreciation Asset Class `Kelas Cek Ulang Hapus {runId}`, sehingga Used By akun itu menjadi 1
23. Admin A mengirim Delete bulk atas akun `RDL-{runId}` dan `RDM-{runId}`, sebagai Confirm atas pengecekan awal yang menyatakan keduanya lolos
24. Verifikasi akun `RDM-{runId}` terhapus dengan tepat satu entri log `Delete` pada setiap surface
25. Verifikasi akun `RDL-{runId}` dilewati oleh cek ulang: masih ada dan jumlah entri log akun itu tidak bertambah

### Account Function akun yang dipakai Asset Class terkunci
26. Admin A mencatat jumlah entri log akun `LKA-{runId}` pada Changelog, pada System Log milik Admin A, dan pada Activity Log
27. Admin A mengirim Edit akun `LKA-{runId}` dengan Account Function `Loss on Disposal`, padahal akun dipakai satu Asset Class dan belum pernah diekspor
28. Verifikasi Edit ditolak dan Account Function akun `LKA-{runId}` tetap `Depreciation Expense`
29. Verifikasi jumlah entri log akun `LKA-{runId}` tidak bertambah pada ketiga surface
30. Pemanggil terotorisasi (DU-166-2) mengirim Edit lewat request langsung atas akun `LKA-{runId}` dengan Account Function `Gain on Disposal`
31. Verifikasi request langsung ditolak server dan Account Function akun `LKA-{runId}` tetap `Depreciation Expense`, karena penolakan perubahan terkunci berlaku apa pun jalurnya

### Kunci berubah antara form dibuka dan Save: Save atomik ditolak
32. Admin A membaca akun `LKB-{runId}` yang Used By-nya 0 sehingga Account Function-nya dapat diubah
33. Admin A mencatat jumlah entri log akun `LKB-{runId}` pada Changelog, pada System Log milik Admin A, dan pada Activity Log
34. Admin B menetapkan akun `LKB-{runId}` pada field Depreciation Expense Asset Class `Kelas Cek Ulang Hapus {runId}`, sehingga Used By akun itu menjadi 1
35. Admin A mengirim Save Edit atas akun `LKB-{runId}` dengan Account Name `Beban Kunci Diubah {runId}` dan Account Function `Gain on Disposal`
36. Verifikasi Save ditolak seluruhnya: Account Function akun `LKB-{runId}` tetap `Depreciation Expense` dan Account Name tetap `Beban Kunci Berubah {runId}`, tanpa field yang tersimpan sebagian
37. Verifikasi jumlah entri log akun `LKB-{runId}` tidak bertambah pada ketiga surface
