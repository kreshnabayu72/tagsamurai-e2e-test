---
id: TC-FA-FACO-BE-168-default-company-dep-preferences
title: "Guard Delete untuk akun default company"
layer: be-e2e
priority: Medium
caseType: Negative
status: ready-for-automation
owner: BE
sourceRules: [FACO-LOGIC-03b, "§9.2#p2", "§[F-FACO-05] Delete Account#r2", "§9.4.2#r17"]
smoke: []
dependsOn: ["Settings > Accounting > Preferences: akun default company"]
trace:
  FACO-LOGIC-03b: [3, 5, 7, 9, 11, 12, 14, 15, 20, 22]
  "§9.2#p2": [3, 5, 7, 9, 11, 15, 17, 22, 24, 26]
  "§[F-FACO-05] Delete Account#r2": [3, 5, 7, 9, 11, 12, 14, 15, 17, 20, 22]
  "§9.4.2#r17": [3, 5, 7, 9, 11, 12, 17, 22]
---

# Guard Delete untuk akun default company

## Prerequisites
- Aktor: Admin A dan Admin B, keduanya Total Control dengan cakupan seluruh client.
- Data:
  - DU-168-1: User `Maya Pengelola {runId}`, Access Level `Total Control`, cakupan seluruh client.
  - DU-168-2: User `Budi Pengelola {runId}`, Access Level `Total Control`, cakupan seluruh client.
  - DU-168-3: Account Code `DCA-{runId}`, Account Name `Laba Pelepasan Default {runId}`, Account Function `Gain on Disposal`, Status `Active`, Used By 0.
  - DU-168-4: Account Code `DCB-{runId}`, Account Name `Rugi Pelepasan Default {runId}`, Account Function `Loss on Disposal`, Status `Active`, Used By 0.
  - DU-168-5: Account Code `DCC-{runId}`, Account Name `Lawan Kapitalisasi Default {runId}`, Account Function `Capitalization Offset`, Status `Active`, Used By 0.
  - DU-168-6: Account Code `DCD-{runId}`, Account Name `Kredit Aset Ditemukan Default {runId}`, Account Function `Gain on Disposal`, Status `Active`, Used By 0.
  - DU-168-7: Account Code `DCE-{runId}`, Account Name `Hasil Pelepasan Default {runId}`, Account Function `Disposal Proceeds`, Status `Active`, Used By 0.
  - DU-168-8: Account Code `DCH-{runId}`, Account Name `Kas Biasa Tanpa Default {runId}`, Account Function `Asset Cost`, Status `Active`, Used By 0.
  - DU-168-9: Account Code `DCI-{runId}`, Account Name `Laba Pelepasan Pengganti {runId}`, Account Function `Gain on Disposal`, Status `Active`, Used By 0.
  - DU-168-10: Accounting Preferences client ini: Default Gain on Disposal (SET-05) `DCA-{runId}`, Default Loss on Disposal (SET-06) `DCB-{runId}`, Default Capitalization Offset (SET-08) `DCC-{runId}`, Found Asset Credit Account (SET-09) `DCD-{runId}`, Default Disposal Proceeds Account (SET-13) `DCE-{runId}`.
- Kondisi:
  - Semua akun di atas belum pernah diekspor dan tidak dipakai Asset Class (Used By 0), sehingga satu-satunya penghalang Delete adalah nilai default company.
  - Akun yang menjadi nilai default company tidak menambah Used By (`FACO-LOGIC-02a`).

## Test Steps

### Delete akun default company ditolak untuk setiap setting default
1. Admin A mencatat jumlah entri log akun `DCA-{runId}`, `DCB-{runId}`, `DCC-{runId}`, `DCD-{runId}`, dan `DCE-{runId}` pada Changelog, pada System Log milik Admin A, dan pada Activity Log
2. Admin A mengirim Delete atas akun `DCA-{runId}`, yang menjadi nilai Default Gain on Disposal (SET-05) di Settings > Accounting > Preferences
3. Verifikasi Delete ditolak karena akun adalah nilai default company dan akun `DCA-{runId}` masih ada
4. Admin A mengirim Delete atas akun `DCB-{runId}`, yang menjadi nilai Default Loss on Disposal (SET-06) di Settings > Accounting > Preferences
5. Verifikasi Delete ditolak karena akun adalah nilai default company dan akun `DCB-{runId}` masih ada
6. Admin A mengirim Delete atas akun `DCC-{runId}`, yang menjadi nilai Default Capitalization Offset (SET-08) di Settings > Accounting > Preferences
7. Verifikasi Delete ditolak karena akun adalah nilai default company dan akun `DCC-{runId}` masih ada
8. Admin A mengirim Delete atas akun `DCD-{runId}`, yang menjadi nilai Found Asset Credit Account (SET-09) di Settings > Accounting > Preferences
9. Verifikasi Delete ditolak karena akun adalah nilai default company dan akun `DCD-{runId}` masih ada
10. Admin A mengirim Delete atas akun `DCE-{runId}`, yang menjadi nilai Default Disposal Proceeds Account (SET-13) di Settings > Accounting > Preferences
11. Verifikasi Delete ditolak karena akun adalah nilai default company dan akun `DCE-{runId}` masih ada
12. Verifikasi jumlah entri log kelima akun tidak bertambah pada ketiga surface, karena penolakan tidak menulis log

### Bulk Delete memproses akun biasa dan melewati akun default company
13. Admin A mengirim Delete bulk atas akun `DCH-{runId}` yang bukan nilai default dan akun `DCA-{runId}` yang menjadi nilai default
14. Verifikasi akun `DCH-{runId}` terhapus dengan tepat satu entri log `Delete` pada setiap surface
15. Verifikasi akun `DCA-{runId}` dilewati: masih ada dan jumlah entri log akun itu tidak bertambah pada ketiga surface

### Bulk Delete yang seluruh akunnya default company tidak mengubah apa pun
16. Admin A mengirim Delete bulk atas akun `DCB-{runId}` dan `DCC-{runId}`
17. Verifikasi kedua akun masih ada dan jumlah entri log keduanya tidak bertambah pada ketiga surface

### Akun dapat dihapus setelah nilai default di Preferences diganti
18. Admin B mengganti nilai Default Gain on Disposal di Settings > Accounting > Preferences dari akun `DCA-{runId}` ke akun `DCI-{runId}`
19. Admin A mengirim Delete atas akun `DCA-{runId}`, yang tidak lagi menjadi nilai default company
20. Verifikasi akun `DCA-{runId}` terhapus dengan tepat satu entri log `Delete` pada ketiga surface, dan akun `DCI-{runId}`, nilai default yang baru, masih ada
21. Admin A mengirim Delete atas akun `DCI-{runId}`, yang kini menjadi nilai default company
22. Verifikasi Delete ditolak dan akun `DCI-{runId}` masih ada

### Akun default company tetap dapat dinonaktifkan dan Account Function-nya tetap dapat diubah
23. Admin A mengirim Deactivate atas akun `DCB-{runId}`, yang menjadi nilai Default Loss on Disposal (SET-06) di Settings > Accounting > Preferences dan Used By-nya 0
24. Verifikasi Deactivate tidak ditolak oleh guard Deactivate modul ini dan akun `DCB-{runId}` berstatus `Inactive`
25. Admin A mengirim Edit akun `DCD-{runId}` dengan Account Function `Loss on Disposal`, padahal akun itu menjadi nilai Found Asset Credit Account (SET-09) di Settings > Accounting > Preferences dan Used By-nya 0
26. Verifikasi Edit tidak ditolak oleh kunci Account Function modul ini dan akun `DCD-{runId}` kini ber-Account Function `Loss on Disposal`
