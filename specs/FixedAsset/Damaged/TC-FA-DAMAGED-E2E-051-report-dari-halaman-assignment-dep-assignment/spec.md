---
id: TC-FA-DAMAGED-E2E-051-report-dari-halaman-assignment-dep-assignment
title: "Aktor Assignment tanpa hak Aktor Damaged melapor rusak dari halaman transaksi Assignment: record Waiting for Confirmation Source Assigned asset, status global Damaged, baris Assignment tidak berubah, dan Cancel Report lewat D-DMG-08 dari halaman Assignment"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["§2.1#b2", "§4.8#r3", "§Aturan Logika Modul#r37", "EC-DMG-03", "§4.2.3#p1", "T-DMG-01", "§Aturan Logika Modul#r28", "§Aturan Logika Modul#r43", "§Aturan Logika Modul#r51", "§2#b7", "§2.1#b1", "§4.2.4#p7"]
smoke: []
dependsOn:
  - "Assignment: Detail Assignment (tombol Report Damaged, Cancel Report)"
trace:
  "§2.1#b2": [8, 9, 11, 12, 18, 23, 24, 25]
  "§4.8#r3": [4]
  "§Aturan Logika Modul#r37": [14, 15]
  "EC-DMG-03": [14, 15]
  "§4.2.3#p1": [4]
  "T-DMG-01": [18, 19, 20, 22, 23, 24, 25]
  "§Aturan Logika Modul#r28": [28]
  "§Aturan Logika Modul#r43": [18]
  "§Aturan Logika Modul#r51": [32, 38, 40, 44, 46]
  "§2#b7": [8, 18, 25]
  "§2.1#b1": [4, 18]
  "§4.2.4#p7": [34, 35, 36]
anchor: [39]
coverage:
  web: automated
---

# Aktor Assignment tanpa hak Aktor Damaged melapor rusak dari halaman transaksi Assignment: record Waiting for Confirmation Source Assigned asset, status global Damaged, baris Assignment tidak berubah, dan Cancel Report lewat D-DMG-08 dari halaman Assignment

## Prerequisites
- Aktor: Aktor Assignment Group `Head Office`, tanpa hak Aktor Damaged pada Group aset (tanpa hak Update Manage asset & TAG), sehingga pelapor umum, yang juga memegang role Read Only.
- Layar awal: halaman Assignment.
- Data:
  - DU-051-1: aset Name `Headset Jabra Evolve2 {runId}`, Group `Head Office`, tanpa TAG, belum punya record Damage, sedang ditugaskan kepada `Maya Lestari {runId}` lewat baris Assignment berstatus `Assigned`.

## Test Steps

### Report Damaged dari Detail Assignment membuat record Waiting for Confirmation
1. Ketik Search `{runId}`, tekan Enter
2. Buka Detail Assignment aset `Headset Jabra Evolve2 {runId}`
3. Klik `Report Damaged` pada Detail Assignment
4. Verifikasi dialog `Report Damaged` tampil
5. Isi What happened `Earcup kiri retak dan bantalan terlepas`
6. Pilih Damaged Photo `headset-earcup-retak.jpg`
7. Klik `[Report Damaged]`
8. Verifikasi toast `Success, your report has been sent to the asset admins.` tampil

### Damage Log terbuka dari penanda di halaman transaksi
9. Verifikasi penanda `Damage reported` tampil di Detail Assignment
10. Klik penanda `Damage reported`
11. Verifikasi dialog `Damage Log` tampil
12. Verifikasi node `Reported damaged by [Reporter Name]` memuat baris detail What happened `Earcup kiri retak dan bantalan terlepas`
13. Tutup dialog Damage Log

### Baris Assignment tidak berubah oleh laporan
14. Verifikasi baris Assignment aset `Headset Jabra Evolve2 {runId}` tetap berstatus `Assigned`
15. Verifikasi pemegang pada baris itu tetap `Maya Lestari {runId}`

### Record Waiting for Confirmation di tab Damaged dan tanpa aksi tulis bagi Aktor Assignment
16. Buka halaman Assets, tab `Damaged`
17. Ketik Search `{runId}`, tekan Enter
18. Verifikasi baris aset `Headset Jabra Evolve2 {runId}` tampil di sub-tab `Active` dengan Status `Waiting for Confirmation`
19. Verifikasi kolom Source pada baris itu `Assigned asset`
20. Verifikasi kolom Reported By pada baris itu memuat nama Aktor Assignment yang melapor, dalam bentuk nama depan dan inisial nama belakang
21. Klik `⋯` pada baris aset `Headset Jabra Evolve2 {runId}`
22. Verifikasi aksi `Damage Log` tampil pada menu baris
23. Verifikasi aksi `Mark as Repaired` tidak tampil pada menu baris
24. Verifikasi aksi `Report Missing` tidak tampil pada menu baris
25. Verifikasi aksi `Review` tidak tampil pada menu baris

### Status global aset Damaged sejak laporan
26. Buka halaman Assets, tab `Assets`
27. Ketik Search `{runId}`, tekan Enter
28. Verifikasi status global aset `Damaged` pada baris `Headset Jabra Evolve2 {runId}`

### Cancel Report dari halaman Assignment lewat dialog konfirmasi
29. Buka halaman Assignment
30. Ketik Search `{runId}`, tekan Enter
31. Buka Detail Assignment aset `Headset Jabra Evolve2 {runId}`
32. Verifikasi aksi `Cancel Report` tampil pada Detail Assignment
33. Klik `Cancel Report` pada Detail Assignment
34. Verifikasi dialog `Cancel Report` tampil dengan butir `Headset Jabra Evolve2 {runId}`
35. Verifikasi dialog memuat pertanyaan `Are you sure you want to cancel it?`
36. Verifikasi dialog memuat tombol `[Go Back]` dan `[Cancel Report]`
37. Klik `[Cancel Report]` pada dialog
38. Verifikasi toast `Success, report has been canceled.` tampil
39. Verifikasi pemegang pada Detail Assignment tetap `Maya Lestari {runId}`
40. Verifikasi penanda `Damage reported` tidak tampil lagi di Detail Assignment

### Record Canceled di sub-tab History dengan node pembatalan
41. Buka halaman Assets, tab `Damaged`
42. Klik sub-tab `History`
43. Ketik Search `{runId}`, tekan Enter
44. Verifikasi baris aset `Headset Jabra Evolve2 {runId}` tampil di sub-tab `History` dengan Status `Canceled`
45. Klik nama aset pada baris aset `Headset Jabra Evolve2 {runId}`
46. Verifikasi node `Report canceled by [Reporter Name]` tampil di dialog Damage Log
47. Tutup dialog Damage Log
