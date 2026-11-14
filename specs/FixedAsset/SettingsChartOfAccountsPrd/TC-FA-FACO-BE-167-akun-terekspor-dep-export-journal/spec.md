---
id: TC-FA-FACO-BE-167-akun-terekspor-dep-export-journal
title: "Update Last Used in Journal dan kunci akun yang pernah diekspor"
layer: be-e2e
priority: Medium
caseType: Negative
status: draft
owner: BE
sourceRules: [C-06, FACO-LOGIC-03a, FACO-LOGIC-03c, FACO-LOGIC-04a, FACO-LOGIC-04b, FACO-LOGIC-04e, FACO-LOGIC-07b, FACO-LOGIC-07c, J-04, L-10, N-01, N-03, N-07, R-09, "§4.1.1#b3", "§7.2#b1", "§[F-FACO-02] Edit Account#r1", "§[F-FACO-02] Edit Account#r2", "§[F-FACO-02] Edit Account#r10", "§[F-FACO-05] Delete Account#r1", "§[F-FACO-05] Delete Account#r3", "§[F-FACO-05] Delete Account#r14", "§[F-FACO-08] Update Last Used in Journal#b1", "§[F-FACO-08] Update Last Used in Journal#b2", "§[F-FACO-08] Update Last Used in Journal#r1", "§[F-FACO-08] Update Last Used in Journal#r2", "§[F-FACO-08] Update Last Used in Journal#r3", "§9.4.2#r5", "§9.4.2#r6", "§9.4.2#r16", "§9.4.2#r18", "§9.4.2#r23", "§9.4.2#r24", "§9.4.2#r25", "§9.4.2#r34", "§9.7#r32"]
smoke: []
dependsOn: ["Export Journal: export jurnal yang mengisi Last Used in Journal", "Asset Class: pemakaian akun pada field akun Asset Class (Used By)"]
trace:
  C-06: [11, 15]
  FACO-LOGIC-03a: [34, 37, 39, 41]
  FACO-LOGIC-03c: [43]
  FACO-LOGIC-04a: [24, 56]
  FACO-LOGIC-04b: [29]
  FACO-LOGIC-04e: [27, 31, 56]
  FACO-LOGIC-07b: [3, 7, 11, 15]
  FACO-LOGIC-07c: [19, 20]
  J-04: [4, 8, 21]
  L-10: [4, 8, 21]
  N-01: [34, 35, 41]
  N-03: [24, 25, 29]
  N-07: [11, 12]
  R-09: [15]
  "§4.1.1#b3": [59]
  "§7.2#b1": [27, 31]
  "§[F-FACO-02] Edit Account#r1": [24, 25, 27, 32]
  "§[F-FACO-02] Edit Account#r2": [29, 31, 32]
  "§[F-FACO-02] Edit Account#r10": [56, 57]
  "§[F-FACO-05] Delete Account#r1": [34, 35, 39, 41, 50]
  "§[F-FACO-05] Delete Account#r3": [43]
  "§[F-FACO-05] Delete Account#r14": [50, 51]
  "§[F-FACO-08] Update Last Used in Journal#b1": [3, 7, 11]
  "§[F-FACO-08] Update Last Used in Journal#b2": [3, 4, 8]
  "§[F-FACO-08] Update Last Used in Journal#r1": [3, 4, 7, 8, 21]
  "§[F-FACO-08] Update Last Used in Journal#r2": [11, 12, 15]
  "§[F-FACO-08] Update Last Used in Journal#r3": [19, 20]
  "§9.4.2#r5": [24, 25]
  "§9.4.2#r6": [29]
  "§9.4.2#r16": [34, 35, 41]
  "§9.4.2#r18": [43]
  "§9.4.2#r23": [3, 4, 7, 8]
  "§9.4.2#r24": [11, 12, 15]
  "§9.4.2#r25": [19, 20]
  "§9.4.2#r34": [27, 31, 32]
  "§9.7#r32": [4, 8, 12, 21]
---

# Update Last Used in Journal dan kunci akun yang pernah diekspor

## Prerequisites
- Aktor: Admin A, Admin B, dan pemanggil terotorisasi, ketiganya Total Control dengan cakupan seluruh client.
- Data:
  - DU-167-1: User `Maya Pengelola {runId}`, Access Level `Total Control`, cakupan seluruh client, pengekspor pada Export Journal oleh Admin A.
  - DU-167-2: User `Budi Pengelola {runId}`, Access Level `Total Control`, cakupan seluruh client.
  - DU-167-3: User `Rudi Integrasi {runId}`, Access Level `Total Control`, cakupan seluruh client, pemanggil terotorisasi yang mengirim request langsung.
  - DU-167-4: Account Code `XJA-{runId}`, Account Name `Kas Perdana Ekspor {runId}`, Account Function `Asset Cost`, Status `Active`, Last Used in Journal kosong, Used By 1, dipakai DU-167-6.
  - DU-167-5: Account Code `XJB-{runId}`, Account Name `Akumulasi Maju Ekspor {runId}`, Account Function `Accumulated Depreciation`, Status `Active`, Last Used in Journal `Aug 2026`, Used By 1, dipakai DU-167-6.
  - DU-167-6: Asset Class `Kelas Ekspor {runId}`, Status `Active`; Asset Cost `XJA-{runId}`, Accumulated Depreciation `XJB-{runId}`.
  - DU-167-7: Account Code `XJC-{runId}`, Account Name `Kas Lama Ekspor {runId}`, Account Function `Asset Cost`, Status `Active`, Last Used in Journal `Mar 2026`, Used By 1, dipakai DU-167-9.
  - DU-167-8: Account Code `XJD-{runId}`, Account Name `Kas Pengganti Ekspor {runId}`, Account Function `Asset Cost`, Status `Active`, Last Used in Journal kosong, Used By 0.
  - DU-167-9: Asset Class `Kelas Alih {runId}`, Status `Active`; Asset Cost `XJC-{runId}`.
  - DU-167-10: Account Code `XJE-{runId}`, Account Name `Kas Terkunci Ekspor {runId}`, Account Function `Asset Cost`, Status `Active`, Last Used in Journal `Jun 2026`, Used By 0.
  - DU-167-12: Account Code `XJF-{runId}`, Account Name `Kas Nonaktif Terekspor Ekspor {runId}`, Account Function `Asset Cost`, Status `Inactive`, Last Used in Journal `Jun 2026`, Used By 0.
  - DU-167-13: Account Code `XJG-{runId}`, Account Name `Beban Guard Ganda Ekspor {runId}`, Account Function `Depreciation Expense`, Status `Active`, Last Used in Journal `Jun 2026`, Used By 1, dipakai DU-167-14.
  - DU-167-14: Asset Class `Kelas Guard Ganda {runId}`, Status `Active`; Depreciation Expense `XJG-{runId}`.
  - DU-167-15: Account Code `XJH-{runId}`, Account Name `Kas Cek Ulang Ekspor {runId}`, Account Function `Asset Cost`, Status `Active`, Last Used in Journal kosong, Used By 0.
  - DU-167-16: Account Code `XJJ-{runId}`, Account Name `Kas Pengalih Ekspor {runId}`, Account Function `Asset Cost`, Status `Active`, Last Used in Journal kosong, Used By 0.
  - DU-167-17: Asset Class `Kelas Cek Ulang Ekspor {runId}`, Status `Active`, belum memakai akun `XJH-{runId}` maupun `XJJ-{runId}`.
  - DU-167-18: Account Code `XJI-{runId}`, Account Name `Kas Kunci Ekspor {runId}`, Account Function `Depreciation Expense`, Status `Active`, Last Used in Journal kosong, Used By 1, dipakai DU-167-19.
  - DU-167-19: Asset Class `Kelas Edit Kunci {runId}`, Status `Active`; Depreciation Expense `XJI-{runId}`.
  - DU-167-20: Account Code `XJE2-{runId}`, nilai input Edit atas akun `XJE-{runId}` yang tidak boleh tersimpan.
  - DU-167-21: Account Code `XJI2-{runId}` dan Account Name `Kas Kunci Diubah Ekspor {runId}`, nilai input Save Edit atas akun `XJI-{runId}` yang tidak boleh tersimpan.
  - DU-167-22: Export Journal periode `Aug 2026`, yang memuat akun Asset Class yang disebut pada langkahnya.
  - DU-167-23: Export Journal periode `Oct 2026`, dengan muatan yang sama.
  - DU-167-24: Export Journal periode `Sep 2026`, lebih lama dari `Oct 2026`, dengan muatan yang sama.
  - DU-167-25: Export Journal periode `Nov 2026`, dengan muatan yang sama.
  - DU-167-26: Export Journal periode `Dec 2026`, dengan muatan yang sama.
- Kondisi:
  - Akun terekspor yang Used By-nya 0 pada data awal (DU-167-10 dan DU-167-12) dahulu dipakai Asset Class yang kini dialihkan ke akun lain.
  - Periode jurnal ditulis `MMM YYYY` (contoh, bukan format tanggal General Settings).
  - Semua akun di atas bukan nilai default company.

## Test Steps

### Export Journal mengisi Last Used in Journal yang masih kosong
1. Admin A mencatat jumlah entri log akun `XJA-{runId}` pada Changelog, pada System Log milik Admin A, dan pada Activity Log
2. Admin A menyelesaikan Export Journal periode `Aug 2026` yang memuat akun `XJA-{runId}` karena dipakai Asset Class `Kelas Ekspor {runId}`
3. Verifikasi Last Used in Journal akun `XJA-{runId}` kini `Aug 2026`, periode jurnal yang diekspor dan bukan tanggal export
4. Verifikasi Changelog, System Log milik Admin A, dan Activity Log masing-masing memuat tepat satu entri baru untuk akun `XJA-{runId}` dengan Action `Edit`, Field `Last Used in Journal`, Old Value `—`, dan New Value `Aug 2026`, dan Modified By adalah Admin A

### Export periode yang lebih baru memajukan nilai
5. Admin A mencatat jumlah entri log akun `XJB-{runId}` pada Changelog, pada System Log milik Admin A, dan pada Activity Log
6. Admin A menyelesaikan Export Journal periode `Oct 2026` yang memuat akun `XJB-{runId}`, yang Last Used in Journal-nya `Aug 2026`
7. Verifikasi Last Used in Journal akun `XJB-{runId}` kini `Oct 2026`
8. Verifikasi Changelog, System Log milik Admin A, dan Activity Log masing-masing memuat tepat satu entri baru untuk akun `XJB-{runId}` dengan Action `Edit`, Field `Last Used in Journal`, Old Value `Aug 2026`, dan New Value `Oct 2026`, dan Modified By adalah Admin A

### Export periode yang lebih lama tidak memundurkan nilai
9. Admin A mencatat jumlah entri log akun `XJB-{runId}` pada Changelog, pada System Log milik Admin A, dan pada Activity Log
10. Admin A menyelesaikan Export Journal periode `Sep 2026`, lebih lama dari `Oct 2026`, yang memuat akun `XJB-{runId}`
11. Verifikasi Last Used in Journal akun `XJB-{runId}` tetap `Oct 2026`, tidak mundur dan tidak kosong
12. Verifikasi jumlah entri log akun `XJB-{runId}` tidak bertambah pada ketiga surface, karena tidak ada perubahan

### Export ulang periode yang sama tidak berefek
13. Admin A mencatat jumlah entri log akun `XJB-{runId}` pada Changelog, pada System Log milik Admin A, dan pada Activity Log
14. Admin A menyelesaikan Export Journal periode `Oct 2026`, sama dengan nilai tersimpan, yang memuat akun `XJB-{runId}`
15. Verifikasi Last Used in Journal akun `XJB-{runId}` tetap `Oct 2026` dan jumlah entri log akun itu tidak bertambah pada ketiga surface

### Akun yang tidak lagi ikut export tetap menyimpan periode terakhirnya
16. Admin A mencatat jumlah entri log akun `XJC-{runId}` pada Changelog, pada System Log milik Admin A, dan pada Activity Log
17. Admin B mengalihkan field Asset Cost Asset Class `Kelas Alih {runId}` dari akun `XJC-{runId}` ke akun `XJD-{runId}`
18. Admin A menyelesaikan Export Journal periode `Nov 2026` yang kini memuat akun `XJD-{runId}` dan tidak lagi memuat akun `XJC-{runId}`
19. Verifikasi Last Used in Journal akun `XJC-{runId}` tetap `Mar 2026`, tidak berubah dan tidak dikosongkan
20. Verifikasi jumlah entri log akun `XJC-{runId}` tidak bertambah pada ketiga surface, sehingga akun yang tidak lagi ikut export tidak menulis L-10
21. Verifikasi Last Used in Journal akun `XJD-{runId}` kini `Nov 2026` dengan Changelog, System Log milik Admin A, dan Activity Log masing-masing memuat tepat satu entri baru untuk akun `XJD-{runId}` dengan Action `Edit`, Field `Last Used in Journal`, Old Value `—`, dan New Value `Nov 2026`, dan Modified By adalah Admin A

### Account Code akun terekspor terkunci terhadap Edit
22. Admin A mencatat jumlah entri log akun `XJE-{runId}` pada Changelog, pada System Log milik Admin A, dan pada Activity Log
23. Admin A mengirim Edit akun `XJE-{runId}` dengan Account Code `XJE2-{runId}`, padahal Last Used in Journal akun itu `Jun 2026` dan Used By-nya 0
24. Verifikasi Edit ditolak dan Account Code akun tetap `XJE-{runId}`
25. Verifikasi jumlah entri log akun `XJE-{runId}` tidak bertambah pada ketiga surface
26. Pemanggil terotorisasi (DU-167-3) mengirim Edit lewat request langsung atas akun `XJE-{runId}` dengan Account Code `XJE2-{runId}`
27. Verifikasi request langsung ditolak server dan Account Code akun tetap `XJE-{runId}`, karena kunci ditegakkan apa pun jalurnya

### Account Function akun terekspor terkunci walau Used By 0
28. Admin A mengirim Edit akun `XJE-{runId}` dengan Account Function `Loss on Disposal`, padahal Used By akun itu 0 dan penyebab kunci hanya Last Used in Journal terisi
29. Verifikasi Edit ditolak dan Account Function akun `XJE-{runId}` tetap `Asset Cost`
30. Pemanggil terotorisasi (DU-167-3) mengirim Edit lewat request langsung atas akun `XJE-{runId}` dengan Account Function `Gain on Disposal`
31. Verifikasi request langsung ditolak server dan Account Function akun `XJE-{runId}` tetap `Asset Cost`
32. Verifikasi jumlah entri log akun `XJE-{runId}` tetap tidak bertambah pada ketiga surface setelah kedua penolakan itu

### Akun terekspor yang Active tidak dapat dihapus, dan Deactivate adalah jalan keluarnya
33. Admin A mengirim Delete atas akun `XJE-{runId}`, yang Active, terekspor, dan Used By-nya 0
34. Verifikasi Delete ditolak karena akun pernah ikut Export Journal dan akun `XJE-{runId}` masih ada dengan Status `Active`
35. Verifikasi jumlah entri log akun `XJE-{runId}` tidak bertambah pada ketiga surface, karena penolakan tidak menulis log
36. Admin A mengirim Deactivate atas akun `XJE-{runId}`
37. Verifikasi akun `XJE-{runId}` berstatus `Inactive` dan memiliki tepat satu entri log baru dengan Field `Status`, Old Value `Active`, dan New Value `Inactive` pada ketiga surface
38. Admin A mengirim Delete atas akun `XJE-{runId}` sekali lagi, kini setelah Inactive
39. Verifikasi Delete ditolak dan akun `XJE-{runId}` tetap tersimpan dengan Status `Inactive`

### Akun terekspor yang sudah Inactive tetap tersimpan
40. Admin A mengirim Delete atas akun `XJF-{runId}`, yang sudah Inactive, terekspor, dan Used By-nya 0
41. Verifikasi Delete ditolak dan akun `XJF-{runId}` tetap tersimpan dengan Status `Inactive`

### Guard 1 dan Guard 2 bersamaan: Guard 1 yang ditampilkan
42. Admin A mengirim Delete atas akun `XJG-{runId}`, yang terekspor dan juga dipakai satu Asset Class
43. Verifikasi Delete ditolak dengan alasan Guard 1, yaitu akun pernah ikut Export Journal pada `Jun 2026`, bukan alasan Guard 2 pemakaian Asset Class, dan akun `XJG-{runId}` masih ada

### Akun menjadi diekspor antara pengecekan awal dan Confirm Delete
44. Admin A membaca akun `XJH-{runId}` yang belum pernah diekspor, Used By-nya 0, dan boleh dihapus
45. Admin A mencatat jumlah entri log akun `XJH-{runId}` pada Changelog, pada System Log milik Admin A, dan pada Activity Log
46. Admin B menetapkan akun `XJH-{runId}` pada field Asset Cost Asset Class `Kelas Cek Ulang Ekspor {runId}`
47. Admin B menyelesaikan Export Journal periode `Dec 2026` yang memuat akun `XJH-{runId}`
48. Admin B mengalihkan field Asset Cost Asset Class `Kelas Cek Ulang Ekspor {runId}` dari akun `XJH-{runId}` ke akun `XJJ-{runId}`, sehingga Used By akun `XJH-{runId}` kembali 0 tetapi Last Used in Journal-nya terisi
49. Admin A mengirim Delete atas akun `XJH-{runId}`, sebagai Confirm atas pengecekan awal yang sudah basi
50. Verifikasi Confirm ditolak oleh cek ulang karena akun kini terekspor dan akun `XJH-{runId}` masih ada
51. Verifikasi jumlah entri log akun `XJH-{runId}` hanya bertambah satu, yaitu entri L-10 dari Export Journal Admin B, dan tidak bertambah oleh Delete yang ditolak

### Akun menjadi terekspor antara form Edit dibuka dan Save: Save atomik ditolak
52. Admin A membaca akun `XJI-{runId}` yang belum pernah diekspor sehingga Account Code-nya dapat diubah
53. Admin A mencatat jumlah entri log akun `XJI-{runId}` pada Changelog, pada System Log milik Admin A, dan pada Activity Log
54. Admin B menyelesaikan Export Journal periode `Nov 2026` yang memuat akun `XJI-{runId}` karena dipakai Asset Class `Kelas Edit Kunci {runId}`
55. Admin A mengirim Save Edit atas akun `XJI-{runId}` dengan Account Name `Kas Kunci Diubah Ekspor {runId}` dan Account Code `XJI2-{runId}`
56. Verifikasi Save ditolak seluruhnya: Account Code akun tetap `XJI-{runId}` dan Account Name tetap `Kas Kunci Ekspor {runId}`, tanpa field yang tersimpan sebagian
57. Verifikasi akun `XJI-{runId}` hanya memiliki entri log baru dari Export Journal Admin B, dan Save yang ditolak tidak menambah entri pada ketiga surface

### Periode jurnal ditulis MMM YYYY pada berkas Download
58. Admin A mengirim Download as CSV dengan Search `Ekspor {runId}` dan kolom visible yang memuat Account Code, Account Name, dan Last Used in Journal
59. Verifikasi kolom Last Used in Journal berkas ditulis sebagai periode bulan `Aug 2026` untuk akun `XJA-{runId}`, `Oct 2026` untuk akun `XJB-{runId}`, dan `Mar 2026` untuk akun `XJC-{runId}`, bukan sebagai tanggal
