---
id: TC-FA-DAMAGED-E2E-048-report-dari-halaman-borrow-dep-borrow
title: "Aktor Borrow tanpa hak Aktor Damaged melapor rusak dari halaman transaksi Borrow: record Waiting for Confirmation Source Borrowed asset, status global Damaged, baris Borrow tidak berubah, Cancel Report dari halaman Borrow, dan Damage Log terbuka dari penanda"
layer: ui-e2e
priority: Critical
caseType: Positive
status: ready-for-automation
sourceRules: ["§2.1#b1", "§2.1#b2", "§4.8#r3", "§2.1#r2", "§Aturan Logika Modul#r40", "§Aturan Logika Modul#r27", "EC-DMG-03", "§9.4.4#r3", "§4.2.3#p1", "§4.2.3#p2", "EC-DMG-22", "§9.11#r1", "T-DMG-01", "§Aturan Logika Modul#r29", "§Aturan Logika Modul#r47", "§Aturan Logika Modul#r55", "§2#b7", "§4.2.4#p8"]
smoke: []
dependsOn:
  - "Borrow: Detail BRW (tombol Report Damaged, Cancel Report, penanda Damage reported)"
trace:
  "§2.1#b1": [4, 20]
  "§2.1#b2": [10, 11, 13, 14, 20, 27, 28, 29]
  "§4.8#r3": [4]
  "§2.1#r2": [10, 20]
  "§Aturan Logika Modul#r40": [16, 17]
  "§Aturan Logika Modul#r27": [17, 22, 23]
  "EC-DMG-03": [16, 17]
  "§9.4.4#r3": [14, 16, 17]
  "§4.2.3#p1": [4]
  "§4.2.3#p2": [4, 5, 6]
  "EC-DMG-22": [13, 14]
  "§9.11#r1": [13, 14]
  "T-DMG-01": [20, 21, 22, 24, 26, 27, 28, 29]
  "§Aturan Logika Modul#r29": [32]
  "§Aturan Logika Modul#r47": [20]
  "§Aturan Logika Modul#r55": [36, 42, 44, 48, 50]
  "§2#b7": [10, 20, 29]
  "§4.2.4#p8": [38, 39, 40]
anchor: [43]
coverage:
  web: automated
---

# Aktor Borrow tanpa hak Aktor Damaged melapor rusak dari halaman transaksi Borrow: record Waiting for Confirmation Source Borrowed asset, status global Damaged, baris Borrow tidak berubah, Cancel Report dari halaman Borrow, dan Damage Log terbuka dari penanda

## Prerequisites
- Aktor: Aktor Borrow Group `Head Office`, tanpa hak Aktor Damaged pada Group aset (tanpa hak Update Manage asset & TAG), sehingga pelapor umum, yang juga memegang role Read Only.
- Layar awal: halaman Borrow.
- Data:
  - DU-048-1: aset Name `Projector Epson EB-X06 {runId}`, Group `Head Office`, tanpa TAG, belum punya record Damage, sedang dipinjam `Sari Dewanti {runId}` lewat baris Borrow berstatus `Borrowed`.

## Test Steps

### Report Damaged dari Detail BRW membuat record Waiting for Confirmation
1. Ketik Search `{runId}`, tekan Enter
2. Buka Detail BRW aset `Projector Epson EB-X06 {runId}`
3. Klik `Report Damaged` pada Detail BRW
4. Verifikasi dialog `Report Damaged` tampil
5. Verifikasi kotak dampak memuat `The asset admins will review your report.`
6. Verifikasi kotak dampak memuat `[Holder] keeps the asset until it's returned.` dengan `[Holder]` diisi `Sari Dewanti {runId}`
7. Isi What happened `Lensa proyektor berembun dan gambar buram`
8. Pilih Damaged Photo `proyektor-lensa-buram.jpg`
9. Klik `[Report Damaged]`
10. Verifikasi toast `Success, your report has been sent to the asset admins.` tampil

### Damage Log terbuka dari penanda di halaman transaksi
11. Verifikasi penanda `Damage reported` tampil di Detail BRW
12. Klik penanda `Damage reported`
13. Verifikasi dialog `Damage Log` tampil
14. Verifikasi node `Reported damaged by [Reporter Name]` memuat baris detail What happened `Lensa proyektor berembun dan gambar buram`
15. Tutup dialog Damage Log

### Baris Borrow tidak berubah oleh laporan
16. Verifikasi baris Borrow aset `Projector Epson EB-X06 {runId}` tetap berstatus `Borrowed`
17. Verifikasi pemegang pada baris itu tetap `Sari Dewanti {runId}`

### Record Waiting for Confirmation di tab Damaged dan tanpa aksi tulis bagi Aktor Borrow
18. Buka halaman Assets, tab `Damaged`
19. Ketik Search `{runId}`, tekan Enter
20. Verifikasi baris aset `Projector Epson EB-X06 {runId}` tampil di sub-tab `Active` dengan Status `Waiting for Confirmation`
21. Verifikasi kolom Source pada baris itu `Borrowed asset`
22. Verifikasi kolom Last Holder pada baris itu terisi nama pemegang, dalam bentuk nama depan dan inisial nama belakang
23. Verifikasi kolom Group pada baris itu `Head Office`
24. Verifikasi kolom Reported By pada baris itu memuat nama Aktor Borrow yang melapor, dalam bentuk nama depan dan inisial nama belakang
25. Klik `⋯` pada baris aset `Projector Epson EB-X06 {runId}`
26. Verifikasi aksi `Damage Log` tampil pada menu baris
27. Verifikasi aksi `Mark as Repaired` tidak tampil pada menu baris
28. Verifikasi aksi `Report Missing` tidak tampil pada menu baris
29. Verifikasi aksi `Review` tidak tampil pada menu baris

### Status global aset Damaged sejak laporan
30. Buka halaman Assets, tab `Assets`
31. Ketik Search `{runId}`, tekan Enter
32. Verifikasi status global aset `Damaged` pada baris `Projector Epson EB-X06 {runId}`

### Cancel Report dari halaman Borrow membatalkan laporan
33. Buka halaman Borrow
34. Ketik Search `{runId}`, tekan Enter
35. Buka Detail BRW aset `Projector Epson EB-X06 {runId}`
36. Verifikasi aksi `Cancel Report` tampil pada Detail BRW
37. Klik `Cancel Report` pada Detail BRW
38. Verifikasi dialog `Cancel Report` tampil dengan butir `Projector Epson EB-X06 {runId}`
39. Verifikasi dialog memuat pertanyaan `Are you sure you want to cancel it?`
40. Verifikasi dialog memuat tombol `[Go Back]` dan `[Cancel Report]`
41. Klik `[Cancel Report]` pada dialog
42. Verifikasi toast `Success, report has been canceled.` tampil
43. Verifikasi pemegang pada Detail BRW tetap `Sari Dewanti {runId}`
44. Verifikasi penanda `Damage reported` tidak tampil lagi di Detail BRW

### Record Canceled di sub-tab History dengan node pembatalan
45. Buka halaman Assets, tab `Damaged`
46. Klik sub-tab `History`
47. Ketik Search `{runId}`, tekan Enter
48. Verifikasi baris aset `Projector Epson EB-X06 {runId}` tampil di sub-tab `History` dengan Status `Canceled`
49. Klik nama aset pada baris aset `Projector Epson EB-X06 {runId}`
50. Verifikasi node `Report canceled by [Reporter Name]` tampil di dialog Damage Log
51. Tutup dialog Damage Log
