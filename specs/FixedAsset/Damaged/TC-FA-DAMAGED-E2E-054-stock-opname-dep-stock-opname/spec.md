---
id: TC-FA-DAMAGED-E2E-054-stock-opname-dep-stock-opname
title: "Pelapor dari Task Detail Audit tanpa hak Aktor Damaged melapor rusak: record Waiting for Confirmation Source Audit dengan penanda Damage reported tanpa mengubah status global aset, Damage Log dapat dibuka pelapor, dan Cancel my report membatalkan laporan"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["§2.1#b1", "§2.1#b2", "§2#b6", "§4.8#r3", "§Aturan Logika Modul#r46", "§3#p2", "EC-DMG-22", "§9.11#r1", "T-DMG-01", "§9.4.2#r38", "§9.4.2#r40", "§9.4.2#r42", "§2.1#b4", "§2.1#b3", "§4.8#r8", "§4.2.4#r14", "§3#p5", "§Aturan Logika Modul#r32", "§Aturan Logika Modul#r47", "§Aturan Logika Modul#r55", "§4.2.4#p8", "§2#b7", "§2.1#r2", "§2.1#r5", "§4.2.3#p1", "§9.4.3#b6"]
smoke: []
dependsOn:
  - "Audit: Task Detail Audit (tombol Report Damaged, Cancel my report, penanda Damage reported)"
trace:
  "§2.1#b1": [2, 17, 59, 71]
  "§2.1#b2": [11, 17, 59, 68, 71]
  "§2#b6": [17, 59]
  "§4.8#r3": [2]
  "§Aturan Logika Modul#r46": [55, 59]
  "§3#p2": [4, 55, 59]
  "EC-DMG-22": [11]
  "§9.11#r1": [11]
  "T-DMG-01": [17, 18, 19, 21, 22, 23, 24, 41, 59, 60, 71, 72]
  "§9.4.2#r38": [17, 59]
  "§9.4.2#r40": [36, 37, 41, 47, 48]
  "§9.4.2#r42": [27, 28]
  "§2.1#b4": [30, 56]
  "§2.1#b3": [22, 23, 24, 30]
  "§4.8#r8": [30, 56, 69]
  "§4.2.4#r14": [32, 36]
  "§3#p5": [9, 27, 28]
  "§Aturan Logika Modul#r32": [27, 28]
  "§Aturan Logika Modul#r47": [8, 12, 13, 17]
  "§Aturan Logika Modul#r55": [30, 36, 41, 43]
  "§4.2.4#p8": [32, 33, 34]
  "§2#b7": [17, 71, 73]
  "§2.1#r2": [17, 59]
  "§2.1#r5": [30, 36]
  "§4.2.3#p1": [4, 67]
  "§9.4.3#b6": [24, 76]
anchor: [75]
coverage:
  web: automated
---

# Pelapor dari Task Detail Audit tanpa hak Aktor Damaged melapor rusak: record Waiting for Confirmation Source Audit dengan penanda Damage reported tanpa mengubah status global aset, Damage Log dapat dibuka pelapor, dan Cancel my report membatalkan laporan

## Prerequisites
- Aktor: Staff Auditor `Hendra Wijaya {runId}` (DU-054-3), tanpa hak Aktor Damaged pada Group aset (tanpa hak Update Manage asset & TAG), sehingga pelapor umum, yang juga memegang role Read Only. Untuk kelompok Pelapor admin: Aktor Damaged dengan role Total Control. Untuk kelompok Asset Admin sub-tab Audit: Asset Admin `Wulan Pramesti {runId}` (DU-054-5), tanpa hak Aktor Damaged pada Group aset.
- Layar awal: halaman Task Audit `Audit Gudang Pusat {runId}`.
- Data:
  - DU-054-1: Task Audit Name `Audit Gudang Pusat {runId}` untuk Group `Head Office`, dikerjakan `Hendra Wijaya {runId}`, berisi aset Name `Rak Besi Heavy Duty {runId}`, aset Name `Lemari Arsip Besi {runId}`, dan aset Name `Meja Kerja Kayu Jati {runId}`, ketiganya Group `Head Office`, tanpa TAG, status global `Normal`, dan belum punya record Damage.
  - DU-054-5: User `Wulan Pramesti {runId}`, Asset Admin sub-tab Audit (bukan pelaksana Task Audit DU-054-1), role Read Only pada Group `Head Office`, tanpa hak Update Manage asset & TAG pada Group aset; cakupan: Group `Head Office`.
  - DU-054-3: User `Hendra Wijaya {runId}`, Staff Auditor pada Task Audit DU-054-1, role Read Only pada Group `Head Office`, tanpa hak Update Manage asset & TAG pada Group aset; cakupan: Group `Head Office`.

## Test Steps

### Report Damaged dari Task Detail Audit oleh pelapor tanpa hak Aktor Damaged
1. Buka Task Detail Audit aset `Rak Besi Heavy Duty {runId}` pada Task Audit `Audit Gudang Pusat {runId}`
2. Verifikasi tombol `Report Damaged` tampil pada Task Detail Audit
3. Klik `Report Damaged` pada Task Detail Audit
4. Verifikasi dialog `Report Damaged` tampil
5. Isi What happened `Kaki rak bengkok dan tidak stabil saat diberi beban`
6. Pilih Damaged Photo `rak-kaki-bengkok.jpg`
7. Klik `[Report Damaged]`
8. Verifikasi toast `Success, your report has been sent to the asset admins.` tampil

### Damage Log terbuka dari penanda Damage reported di Task Detail Audit
9. Verifikasi penanda `Damage reported` tampil pada Task Detail Audit
10. Klik penanda `Damage reported`
11. Verifikasi dialog `Damage Log` tampil
12. Verifikasi node `Reported damaged by [Reporter Name]` memuat baris detail What happened `Kaki rak bengkok dan tidak stabil saat diberi beban`
13. Verifikasi baris detail Damaged Photo pada node itu memuat `rak-kaki-bengkok.jpg`
14. Tutup dialog Damage Log

### Record Waiting for Confirmation Source Audit di tab Damaged dan tanpa aksi tulis bagi pelapor
15. Buka halaman Assets, tab `Damaged`
16. Ketik Search `{runId}`, tekan Enter
17. Verifikasi baris aset `Rak Besi Heavy Duty {runId}` tampil di sub-tab `Active` dengan Status `Waiting for Confirmation`
18. Verifikasi kolom Source pada baris itu `Audit`
19. Verifikasi kolom Reported By pada baris itu memuat nama Staff Auditor `Hendra Wijaya {runId}`, dalam bentuk nama depan dan inisial nama belakang
20. Klik `⋯` pada baris aset `Rak Besi Heavy Duty {runId}`
21. Verifikasi aksi `Damage Log` tampil pada menu baris
22. Verifikasi aksi `Mark as Repaired` tidak tampil pada menu baris
23. Verifikasi aksi `Report Missing` tidak tampil pada menu baris
24. Verifikasi aksi `Review` tidak tampil pada menu baris

### Status global aset tetap dan hanya diberi penanda Damage reported
25. Buka halaman Assets, tab `Assets`
26. Ketik Search `Rak Besi Heavy Duty {runId}`, tekan Enter
27. Verifikasi status global aset `Normal` pada baris `Rak Besi Heavy Duty {runId}`
28. Verifikasi baris `Rak Besi Heavy Duty {runId}` memuat penanda `Damage reported`

### Cancel my report dari Task Detail Audit membatalkan laporan
29. Buka Task Detail Audit aset `Rak Besi Heavy Duty {runId}` pada Task Audit `Audit Gudang Pusat {runId}`
30. Verifikasi aksi `Cancel my report` tampil pada Task Detail Audit
31. Klik `Cancel my report` pada Task Detail Audit
32. Verifikasi dialog `Cancel Report` tampil dengan butir `Rak Besi Heavy Duty {runId}`
33. Verifikasi dialog memuat pertanyaan `Are you sure you want to cancel it?`
34. Verifikasi dialog memuat tombol `[Go Back]` dan `[Cancel Report]`
35. Klik `[Cancel Report]` pada dialog
36. Verifikasi toast `Success, report has been canceled.` tampil
37. Verifikasi penanda `Damage reported` tidak tampil lagi pada Task Detail Audit

### Record Canceled di sub-tab History dan status global aset tidak berubah
38. Buka halaman Assets, tab `Damaged`
39. Klik sub-tab `History`
40. Ketik Search `{runId}`, tekan Enter
41. Verifikasi baris aset `Rak Besi Heavy Duty {runId}` tampil di sub-tab `History` dengan Status `Canceled`
42. Klik nama aset pada baris aset `Rak Besi Heavy Duty {runId}`
43. Verifikasi node `Report canceled by [Reporter Name]` tampil di dialog Damage Log
44. Tutup dialog Damage Log
45. Buka halaman Assets, tab `Assets`
46. Ketik Search `Rak Besi Heavy Duty {runId}`, tekan Enter
47. Verifikasi status global aset `Normal` pada baris `Rak Besi Heavy Duty {runId}`
48. Verifikasi baris `Rak Besi Heavy Duty {runId}` tidak memuat penanda `Damage reported`

### Pelapor admin dari Task Detail Audit langsung Damaged dan tidak memakai Cancel my report
49. Masuk sebagai Aktor Damaged dengan role Total Control
50. Buka Task Detail Audit aset `Lemari Arsip Besi {runId}` pada Task Audit `Audit Gudang Pusat {runId}`
51. Klik `Report Damaged` pada Task Detail Audit
52. Isi What happened `Pintu lemari arsip macet dan engsel patah`
53. Pilih Damaged Photo `lemari-engsel-patah.jpg`
54. Klik `[Report Damaged]`
55. Verifikasi toast `Success, asset has been reported damaged.` tampil
56. Verifikasi aksi `Cancel my report` tidak tampil pada Task Detail Audit
57. Buka halaman Assets, tab `Damaged`
58. Ketik Search `Lemari Arsip Besi {runId}`, tekan Enter
59. Verifikasi baris aset `Lemari Arsip Besi {runId}` tampil di sub-tab `Active` dengan Status `Damaged`, tanpa Confirm
60. Verifikasi kolom Source pada baris itu `Audit`

### Asset Admin sub-tab Audit tanpa hak Aktor Damaged melapor sebagai pelapor umum
61. Masuk sebagai Asset Admin sub-tab Audit `Wulan Pramesti {runId}`
62. Buka Task Detail Audit aset `Meja Kerja Kayu Jati {runId}` pada Task Audit `Audit Gudang Pusat {runId}` dari sub-tab Audit
63. Klik `Report Damaged` pada Task Detail Audit
64. Isi What happened `Permukaan meja terkelupas dan salah satu kaki goyah`
65. Pilih Damaged Photo `meja-permukaan-terkelupas.jpg`
66. Klik `[Report Damaged]`
67. Verifikasi toast `Success, your report has been sent to the asset admins.` tampil
68. Verifikasi penanda `Damage reported` tampil pada Task Detail Audit
69. Verifikasi aksi `Cancel my report` tampil pada Task Detail Audit
70. Buka halaman Assets, tab `Damaged`, ketik Search `Meja Kerja Kayu Jati {runId}`, tekan Enter
71. Verifikasi baris aset `Meja Kerja Kayu Jati {runId}` tampil di sub-tab `Active` dengan Status `Waiting for Confirmation`
72. Verifikasi kolom Source pada baris itu `Audit`
73. Verifikasi kolom Reported By pada baris itu memuat nama Asset Admin `Wulan Pramesti {runId}`, dalam bentuk nama depan dan inisial nama belakang

### Damage Log record pelapor umum tidak menampilkan Confirm dan Reject
74. Klik nama aset pada baris aset `Meja Kerja Kayu Jati {runId}`
75. Verifikasi dialog `Damage Log` aset `Meja Kerja Kayu Jati {runId}` tampil dengan node `Reported damaged by [Reporter Name]`
76. Verifikasi tombol `[Confirm]` dan `[Reject]` tidak tampil pada dialog Damage Log bagi pelapor `Wulan Pramesti {runId}`
77. Tutup dialog Damage Log
