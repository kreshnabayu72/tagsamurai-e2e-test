---
id: TC-FA-FACO-BE-167-akun-terekspor-dep-export-journal
title: "Update Last Used in Journal dan kunci akun yang pernah diekspor"
layer: be-e2e
priority: Medium
caseType: Negative
status: ready-for-automation
owner: BE
sourceRules: [C-06, FACO-LOGIC-03a, FACO-LOGIC-03c, FACO-LOGIC-04a, FACO-LOGIC-04b, FACO-LOGIC-04e, FACO-LOGIC-07b, FACO-LOGIC-07c, J-04, L-10, N-01, N-03, N-07, R-09, "§4.1.1#b2", "§7.2#b1", "§[F-FACO-02] Edit Account#r1", "§[F-FACO-02] Edit Account#r2", "§[F-FACO-02] Edit Account#r12", "§[F-FACO-05] Delete Account#r1", "§[F-FACO-05] Delete Account#r3", "§[F-FACO-05] Delete Account#r14", "§[F-FACO-08] Update Last Used in Journal#b1", "§[F-FACO-08] Update Last Used in Journal#b2", "§[F-FACO-08] Update Last Used in Journal#r1", "§[F-FACO-08] Update Last Used in Journal#r2", "§[F-FACO-08] Update Last Used in Journal#r3", "§9.4.2#r5", "§9.4.2#r6", "§9.4.2#r16", "§9.4.2#r18", "§9.4.2#r23", "§9.4.2#r24", "§9.4.2#r25", "§9.4.2#r34", "§9.7#r32", "§8.2#r1", "§8.3#p1", "§8.1#p2"]
smoke: []
dependsOn: ["Export Journal: export jurnal yang mengisi Last Used in Journal", "Asset Class: pemakaian akun pada field akun Asset Class (Used By)"]
trace:
  C-06: [13, 17]
  FACO-LOGIC-03a: [36, 39, 41, 43]
  FACO-LOGIC-03c: [45]
  FACO-LOGIC-04a: [26, 58]
  FACO-LOGIC-04b: [31]
  FACO-LOGIC-04e: [29, 33, 58]
  FACO-LOGIC-07b: [3, 9, 13, 17]
  FACO-LOGIC-07c: [21, 22]
  J-04: [4, 10, 23]
  L-10: [4, 10, 23, 62, 63]
  N-01: [36, 37, 43]
  N-03: [26, 27, 31]
  N-07: [13, 14]
  R-09: [5, 6, 17]
  "§4.1.1#b2": [61]
  "§7.2#b1": [29, 33]
  "§[F-FACO-02] Edit Account#r1": [26, 27, 29, 34]
  "§[F-FACO-02] Edit Account#r2": [31, 33, 34]
  "§[F-FACO-02] Edit Account#r12": [58, 59]
  "§[F-FACO-05] Delete Account#r1": [36, 37, 41, 43, 52]
  "§[F-FACO-05] Delete Account#r3": [45]
  "§[F-FACO-05] Delete Account#r14": [52, 53]
  "§[F-FACO-08] Update Last Used in Journal#b1": [3, 5, 6, 9, 13]
  "§[F-FACO-08] Update Last Used in Journal#b2": [3, 4, 10]
  "§[F-FACO-08] Update Last Used in Journal#r1": [3, 4, 9, 10, 23]
  "§[F-FACO-08] Update Last Used in Journal#r2": [5, 6, 13, 14, 17]
  "§[F-FACO-08] Update Last Used in Journal#r3": [21, 22]
  "§9.4.2#r5": [26, 27]
  "§9.4.2#r6": [31]
  "§9.4.2#r16": [36, 37, 43]
  "§9.4.2#r18": [45]
  "§9.4.2#r23": [3, 4, 9, 10]
  "§9.4.2#r24": [5, 6, 13, 14, 17]
  "§9.4.2#r25": [21, 22]
  "§9.4.2#r34": [29, 33, 34]
  "§9.7#r32": [4, 10, 14, 23]
  "§8.2#r1": [62]
  "§8.3#p1": [63]
  "§8.1#p2": [4, 23]
---

# Update Last Used in Journal dan kunci akun yang pernah diekspor

## Prerequisites
- Aktor: Admin A, Admin B, dan pemanggil terotorisasi, ketiganya Total Control dengan cakupan seluruh client.
- Data:
  - DU-167-1: User `Maya Pengelola {runId}`, Access Level `Total Control`, cakupan seluruh client, pengekspor pada Export Journal oleh Admin A.
  - DU-167-2: User `Budi Pengelola {runId}`, Access Level `Total Control`, cakupan seluruh client.
  - DU-167-3: User `Rudi Integrasi {runId}`, Access Level `Total Control`, cakupan seluruh client, pemanggil terotorisasi yang mengirim request langsung.
  - DU-167-4: Account Code `XJA-{runId}`, Account Name `Kas Perdana Ekspor {runId}`, Account Function `Asset Cost`, Status `Active`, Last Used in Journal kosong, Used By 1, dipakai DU-167-6.
  - DU-167-5: Account Code `XJB-{runId}`, Account Name `Akumulasi Maju Ekspor {runId}`, Account Function `Accumulated Depreciation`, Status `Active`, Last Used in Journal periode `M0 − 6 bulan`, Used By 1, dipakai DU-167-6.
  - DU-167-6: Asset Class `Kelas Ekspor {runId}`, Status `Active`; Asset Cost `XJA-{runId}`, Accumulated Depreciation `XJB-{runId}`.
  - DU-167-7: Account Code `XJC-{runId}`, Account Name `Kas Lama Ekspor {runId}`, Account Function `Asset Cost`, Status `Active`, Last Used in Journal periode `M0 − 11 bulan`, Used By 1, dipakai DU-167-9.
  - DU-167-8: Account Code `XJD-{runId}`, Account Name `Kas Pengganti Ekspor {runId}`, Account Function `Asset Cost`, Status `Active`, Last Used in Journal kosong, Used By 0.
  - DU-167-9: Asset Class `Kelas Alih {runId}`, Status `Active`; Asset Cost `XJC-{runId}`.
  - DU-167-10: Account Code `XJE-{runId}`, Account Name `Kas Terkunci Ekspor {runId}`, Account Function `Asset Cost`, Status `Active`, Last Used in Journal periode `M0 − 8 bulan`, Used By 0.
  - DU-167-12: Account Code `XJF-{runId}`, Account Name `Kas Nonaktif Terekspor Ekspor {runId}`, Account Function `Asset Cost`, Status `Inactive`, Last Used in Journal periode `M0 − 8 bulan`, Used By 0.
  - DU-167-13: Account Code `XJG-{runId}`, Account Name `Beban Guard Ganda Ekspor {runId}`, Account Function `Depreciation Expense`, Status `Active`, Last Used in Journal periode `M0 − 8 bulan`, Used By 1, dipakai DU-167-14.
  - DU-167-14: Asset Class `Kelas Guard Ganda {runId}`, Status `Active`; Depreciation Expense `XJG-{runId}`.
  - DU-167-15: Account Code `XJH-{runId}`, Account Name `Kas Cek Ulang Ekspor {runId}`, Account Function `Asset Cost`, Status `Active`, Last Used in Journal kosong, Used By 0.
  - DU-167-16: Account Code `XJJ-{runId}`, Account Name `Kas Pengalih Ekspor {runId}`, Account Function `Asset Cost`, Status `Active`, Last Used in Journal kosong, Used By 0.
  - DU-167-17: Asset Class `Kelas Cek Ulang Ekspor {runId}`, Status `Active`, belum memakai akun `XJH-{runId}` maupun `XJJ-{runId}`.
  - DU-167-18: Account Code `XJI-{runId}`, Account Name `Kas Kunci Ekspor {runId}`, Account Function `Depreciation Expense`, Status `Active`, Last Used in Journal kosong, Used By 1, dipakai DU-167-19.
  - DU-167-19: Asset Class `Kelas Edit Kunci {runId}`, Status `Active`; Depreciation Expense `XJI-{runId}`.
  - DU-167-20: Account Code `XJE2-{runId}`, nilai input Edit atas akun `XJE-{runId}` yang tidak boleh tersimpan.
  - DU-167-21: Account Code `XJI2-{runId}` dan Account Name `Kas Kunci Diubah Ekspor {runId}`, nilai input Save Edit atas akun `XJI-{runId}` yang tidak boleh tersimpan.
  - DU-167-22: Export Journal periode `M0 − 6 bulan`, hanya memuat jurnal aset ber-Asset Class `Kelas Ekspor {runId}`, sehingga akun `XJA-{runId}` dan `XJB-{runId}` ikut berkas.
  - DU-167-23: Export Journal periode `M0 − 4 bulan`, hanya memuat jurnal aset ber-Asset Class `Kelas Ekspor {runId}`.
  - DU-167-24: Export Journal periode `M0 − 5 bulan`, lebih lama dari periode `M0 − 4 bulan`, hanya memuat jurnal aset ber-Asset Class `Kelas Ekspor {runId}`.
  - DU-167-25: Export Journal periode `M0 − 3 bulan`, hanya memuat jurnal aset ber-Asset Class `Kelas Alih {runId}`.
  - DU-167-26: Export Journal periode `M0 − 2 bulan`, hanya memuat jurnal aset ber-Asset Class `Kelas Cek Ulang Ekspor {runId}`.
  - DU-167-27: Export Journal periode `M0 − 3 bulan`, hanya memuat jurnal aset ber-Asset Class `Kelas Edit Kunci {runId}`.
- Kondisi:
  - Akun terekspor yang Used By-nya 0 pada data awal (DU-167-10 dan DU-167-12) dahulu dipakai Asset Class yang kini dialihkan ke akun lain.
  - M0 adalah bulan saat spec dijalankan. Periode jurnal ditulis `MMM YYYY` (bukan format tanggal General Settings), dan semua periode di bawah sudah lewat.
  - Semua akun di atas bukan nilai default company.
  - Setiap Asset Class di atas memiliki akun yang lengkap menurut definisi kelengkapan Asset Class dan semua akunnya Active, sehingga jurnal asetnya tidak ditahan (Held) oleh Export Journal dan ikut berkas export yang memuat Asset Class itu.

## Test Steps

### Export Journal mengisi Last Used in Journal yang masih kosong
1. Admin A mencatat jumlah entri log akun `XJA-{runId}` dan `XJB-{runId}` pada Changelog, pada System Log milik Admin A, dan pada Activity Log
2. Admin A menyelesaikan Export Journal periode `M0 − 6 bulan` yang memuat akun `XJA-{runId}`, yang Last Used in Journal-nya kosong, dan akun `XJB-{runId}`, yang Last Used in Journal-nya sudah periode `M0 − 6 bulan`, karena keduanya dipakai Asset Class `Kelas Ekspor {runId}`
3. Verifikasi Last Used in Journal akun `XJA-{runId}` kini periode `M0 − 6 bulan`, periode jurnal yang diekspor dan bukan tanggal export
4. Verifikasi Changelog, System Log milik Admin A, dan Activity Log masing-masing memuat tepat satu entri baru untuk akun `XJA-{runId}` dengan Action `Edit`, Field `Last Used in Journal`, Old Value `-` (satu tanda hubung, sisi kosong disimpan sebagai `-`), dan New Value periode `M0 − 6 bulan`, dan Modified By adalah Admin A
5. Verifikasi Last Used in Journal akun `XJB-{runId}` tetap periode `M0 − 6 bulan`, karena periode yang diekspor sama dengan nilai tersimpan
6. Verifikasi jumlah entri log akun `XJB-{runId}` tidak bertambah pada ketiga surface oleh Export Journal periode `M0 − 6 bulan`

### Export periode yang lebih baru memajukan nilai
7. Admin A mencatat jumlah entri log akun `XJB-{runId}` pada Changelog, pada System Log milik Admin A, dan pada Activity Log
8. Admin A menyelesaikan Export Journal periode `M0 − 4 bulan` yang memuat akun `XJA-{runId}` dan `XJB-{runId}` karena dipakai Asset Class `Kelas Ekspor {runId}`, dengan Last Used in Journal keduanya periode `M0 − 6 bulan`
9. Verifikasi Last Used in Journal akun `XJB-{runId}` kini periode `M0 − 4 bulan`
10. Verifikasi Changelog, System Log milik Admin A, dan Activity Log masing-masing memuat tepat satu entri baru untuk akun `XJB-{runId}` dengan Action `Edit`, Field `Last Used in Journal`, Old Value periode `M0 − 6 bulan`, dan New Value periode `M0 − 4 bulan`, dan Modified By adalah Admin A

### Export periode yang lebih lama tidak memundurkan nilai
11. Admin A mencatat jumlah entri log akun `XJB-{runId}` pada Changelog, pada System Log milik Admin A, dan pada Activity Log
12. Admin A menyelesaikan Export Journal periode `M0 − 5 bulan`, lebih lama dari periode `M0 − 4 bulan`, yang memuat akun `XJA-{runId}` dan `XJB-{runId}` karena dipakai Asset Class `Kelas Ekspor {runId}`
13. Verifikasi Last Used in Journal akun `XJB-{runId}` tetap periode `M0 − 4 bulan`, tidak mundur dan tidak kosong
14. Verifikasi jumlah entri log akun `XJB-{runId}` tidak bertambah pada ketiga surface, karena tidak ada perubahan

### Export ulang periode yang sama tidak berefek
15. Admin A mencatat jumlah entri log akun `XJB-{runId}` pada Changelog, pada System Log milik Admin A, dan pada Activity Log
16. Admin A menyelesaikan Export Journal periode `M0 − 4 bulan`, sama dengan nilai tersimpan, yang memuat akun `XJA-{runId}` dan `XJB-{runId}` karena dipakai Asset Class `Kelas Ekspor {runId}`
17. Verifikasi Last Used in Journal akun `XJB-{runId}` tetap periode `M0 − 4 bulan` dan jumlah entri log akun itu tidak bertambah pada ketiga surface

### Akun yang tidak lagi ikut export tetap menyimpan periode terakhirnya
18. Admin A mencatat jumlah entri log akun `XJC-{runId}` pada Changelog, pada System Log milik Admin A, dan pada Activity Log
19. Admin B mengalihkan field Asset Cost Asset Class `Kelas Alih {runId}` dari akun `XJC-{runId}` ke akun `XJD-{runId}`
20. Admin A menyelesaikan Export Journal periode `M0 − 3 bulan` yang kini memuat akun `XJD-{runId}` dan tidak lagi memuat akun `XJC-{runId}`
21. Verifikasi Last Used in Journal akun `XJC-{runId}` tetap periode `M0 − 11 bulan`, tidak berubah dan tidak dikosongkan
22. Verifikasi jumlah entri log akun `XJC-{runId}` tidak bertambah pada ketiga surface, sehingga akun yang tidak lagi ikut export tidak menulis L-10
23. Verifikasi Last Used in Journal akun `XJD-{runId}` kini periode `M0 − 3 bulan` dengan Changelog, System Log milik Admin A, dan Activity Log masing-masing memuat tepat satu entri baru untuk akun `XJD-{runId}` dengan Action `Edit`, Field `Last Used in Journal`, Old Value `-` (satu tanda hubung, sisi kosong disimpan sebagai `-`), dan New Value periode `M0 − 3 bulan`, dan Modified By adalah Admin A

### Account Code akun terekspor terkunci terhadap Edit
24. Admin A mencatat jumlah entri log akun `XJE-{runId}` pada Changelog, pada System Log milik Admin A, dan pada Activity Log
25. Admin A mengirim Edit akun `XJE-{runId}` dengan Account Code `XJE2-{runId}`, padahal Last Used in Journal akun itu periode `M0 − 8 bulan` dan Used By-nya 0
26. Verifikasi Edit ditolak dan Account Code akun tetap `XJE-{runId}`
27. Verifikasi jumlah entri log akun `XJE-{runId}` tidak bertambah pada ketiga surface
28. Pemanggil terotorisasi (DU-167-3) mengirim Edit lewat request langsung atas akun `XJE-{runId}` dengan Account Code `XJE2-{runId}`
29. Verifikasi request langsung ditolak server dan Account Code akun tetap `XJE-{runId}`, karena kunci ditegakkan apa pun jalurnya

### Account Function akun terekspor terkunci walau Used By 0
30. Admin A mengirim Edit akun `XJE-{runId}` dengan Account Function `Loss on Disposal`, padahal Used By akun itu 0 dan penyebab kunci hanya Last Used in Journal terisi
31. Verifikasi Edit ditolak dan Account Function akun `XJE-{runId}` tetap `Asset Cost`
32. Pemanggil terotorisasi (DU-167-3) mengirim Edit lewat request langsung atas akun `XJE-{runId}` dengan Account Function `Gain on Disposal`
33. Verifikasi request langsung ditolak server dan Account Function akun `XJE-{runId}` tetap `Asset Cost`
34. Verifikasi jumlah entri log akun `XJE-{runId}` tetap tidak bertambah pada ketiga surface setelah kedua penolakan itu

### Akun terekspor yang Active tidak dapat dihapus, dan Deactivate adalah jalan keluarnya
35. Admin A mengirim Delete atas akun `XJE-{runId}`, yang Active, terekspor, dan Used By-nya 0
36. Verifikasi Delete ditolak karena akun pernah ikut Export Journal dan akun `XJE-{runId}` masih ada dengan Status `Active`
37. Verifikasi jumlah entri log akun `XJE-{runId}` tidak bertambah pada ketiga surface, karena penolakan tidak menulis log
38. Admin A mengirim Deactivate atas akun `XJE-{runId}`
39. Verifikasi akun `XJE-{runId}` berstatus `Inactive` dan memiliki tepat satu entri log baru dengan Field `Status`, Old Value `Active`, dan New Value `Inactive` pada ketiga surface
40. Admin A mengirim Delete atas akun `XJE-{runId}` sekali lagi, kini setelah Inactive
41. Verifikasi Delete ditolak dan akun `XJE-{runId}` tetap tersimpan dengan Status `Inactive`

### Akun terekspor yang sudah Inactive tetap tersimpan
42. Admin A mengirim Delete atas akun `XJF-{runId}`, yang sudah Inactive, terekspor, dan Used By-nya 0
43. Verifikasi Delete ditolak dan akun `XJF-{runId}` tetap tersimpan dengan Status `Inactive`

### Guard 1 dan Guard 2 bersamaan: Guard 1 yang ditampilkan
44. Admin A mengirim Delete atas akun `XJG-{runId}`, yang terekspor dan juga dipakai satu Asset Class
45. Verifikasi Delete ditolak dengan alasan Guard 1, yaitu akun pernah ikut Export Journal pada periode `M0 − 8 bulan`, bukan alasan Guard 2 pemakaian Asset Class, dan akun `XJG-{runId}` masih ada

### Akun menjadi diekspor antara pengecekan awal dan Confirm Delete
46. Admin A membaca akun `XJH-{runId}` yang belum pernah diekspor, Used By-nya 0, dan boleh dihapus
47. Admin A mencatat jumlah entri log akun `XJH-{runId}` pada Changelog, pada System Log milik Admin A, dan pada Activity Log
48. Admin B menetapkan akun `XJH-{runId}` pada field Asset Cost Asset Class `Kelas Cek Ulang Ekspor {runId}`
49. Admin B menyelesaikan Export Journal periode `M0 − 2 bulan` yang memuat akun `XJH-{runId}`
50. Admin B mengalihkan field Asset Cost Asset Class `Kelas Cek Ulang Ekspor {runId}` dari akun `XJH-{runId}` ke akun `XJJ-{runId}`, sehingga Used By akun `XJH-{runId}` kembali 0 tetapi Last Used in Journal-nya terisi
51. Admin A mengirim Delete atas akun `XJH-{runId}`, sebagai Confirm atas pengecekan awal yang sudah basi
52. Verifikasi Confirm ditolak oleh cek ulang karena akun kini terekspor dan akun `XJH-{runId}` masih ada
53. Verifikasi jumlah entri log akun `XJH-{runId}` pada Changelog dan pada Activity Log hanya bertambah satu, yaitu entri L-10 dari Export Journal Admin B, jumlah pada System Log milik Admin A tidak bertambah karena entri L-10 itu masuk ke System Log milik Admin B sebagai aktornya, dan Delete yang ditolak tidak menambah entri pada ketiga surface

### Akun menjadi terekspor antara form Edit dibuka dan Save: Save atomik ditolak
54. Admin A membaca akun `XJI-{runId}` yang belum pernah diekspor sehingga Account Code-nya dapat diubah
55. Admin A mencatat jumlah entri log akun `XJI-{runId}` pada Changelog, pada System Log milik Admin A, dan pada Activity Log
56. Admin B menyelesaikan Export Journal periode `M0 − 3 bulan` yang memuat akun `XJI-{runId}` karena dipakai Asset Class `Kelas Edit Kunci {runId}`
57. Admin A mengirim Save Edit atas akun `XJI-{runId}` dengan Account Name `Kas Kunci Diubah Ekspor {runId}` dan Account Code `XJI2-{runId}`
58. Verifikasi Save ditolak seluruhnya: Account Code akun tetap `XJI-{runId}` dan Account Name tetap `Kas Kunci Ekspor {runId}`, tanpa field yang tersimpan sebagian
59. Verifikasi akun `XJI-{runId}` hanya memiliki entri log baru dari Export Journal Admin B, dan Save yang ditolak tidak menambah entri pada ketiga surface

### Periode jurnal ditulis MMM YYYY pada berkas Download
60. Admin A mengirim Download as CSV dengan Search `Ekspor {runId}` dan kolom visible yang memuat Account Code, Account Name, dan Last Used in Journal
61. Verifikasi kolom Last Used in Journal berkas ditulis sebagai periode bulan berformat `MMM YYYY`, bukan sebagai tanggal: periode `M0 − 4 bulan` untuk akun `XJA-{runId}`, periode `M0 − 4 bulan` untuk akun `XJB-{runId}`, dan periode `M0 − 11 bulan` untuk akun `XJC-{runId}`

### Entri L-10 pada System Log dan Activity Log memuat Object dan Name
62. Verifikasi, setelah Export Journal periode `M0 − 3 bulan` pada langkah 20 ter-commit, System Log milik Admin A memuat entri L-10 untuk akun `XJD-{runId}` dengan Object `Chart of Accounts` dan Name `XJD-{runId}`
63. Verifikasi, setelah Export Journal yang sama ter-commit, Activity Log memuat entri L-10 untuk akun `XJD-{runId}` dengan Object `Chart of Accounts`, Name `XJD-{runId}`, dan Modified By Admin A sebagai pengekspor
