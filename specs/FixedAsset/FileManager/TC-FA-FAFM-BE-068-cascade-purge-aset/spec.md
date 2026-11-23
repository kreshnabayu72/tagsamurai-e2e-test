---
id: TC-FA-FAFM-BE-068-cascade-purge-aset
title: "Cascade purge atas seluruh file aset yang dihapus"
layer: be-e2e
priority: Critical
caseType: Positive
status: ready-for-automation
owner: BE
sourceRules: ["ARS-04a", "ARS-04b", "ARS-04c", "ARS-04d", "ARS-04e", "DIM-09b", "DIM-14c", "EC-07", "F-FAFM-05.k1", "F-FAFM-05.k2", "F-FAFM-05b", "F-FAFM-05c", "F-FAFM-05d", "F-FAFM-05e", "FAFM-LOGIC-04a", "FAFM-LOGIC-04b", "FAFM-LOGIC-04e", "SYN-05c", "SYN-05h", "SYN-05i", "SYN-06a", "SYN-06d", "SYN-06e", "§9.4.3#b5"]
smoke: []
dependsOn: []
trace:
  "ARS-04a": [24, 25]
  "ARS-04b": 10
  "ARS-04c": [19, 21]
  "ARS-04d": 21
  "ARS-04e": [4, 10]
  "DIM-09b": [10, 17]
  "DIM-14c": 10
  "EC-07": [2, 10, 17]
  "F-FAFM-05.k1": 10
  "F-FAFM-05.k2": [6, 10]
  "F-FAFM-05b": 10
  "F-FAFM-05c": 10
  "F-FAFM-05d": 6
  "F-FAFM-05e": [6, 8, 13, 30, 31, 33, 35, 37, 39, 41, 43, 46]
  "FAFM-LOGIC-04a": [10, 11]
  "FAFM-LOGIC-04b": [24, 27]
  "FAFM-LOGIC-04e": 17
  "SYN-05c": 10
  "SYN-05h": [6, 10]
  "SYN-05i": 10
  "SYN-06a": [10, 17]
  "SYN-06d": [6, 10]
  "SYN-06e": [10, 17]
  "§9.4.3#b5": 11
---

# Cascade purge atas seluruh file aset yang dihapus

## Prerequisites
- Aktor: Total Control `Bagas Pratama {runId}`, Group Manager `Hendra Gunawan {runId}`, dan pemegang Manage files `Wulan Anggraini {runId}`.
- Data:
  - DU-068-1: User `Bagas Pratama {runId}`, role Total Control, cakupan seluruh group.
  - DU-068-2: Aset `Laptop Dell Latitude 5420 {runId}`, group `Head Office`, Status `Active`, memiliki tiga file: DU-068-5, DU-068-6, dan DU-068-7.
  - DU-068-3: Aset Draft `Camera Canon EOS 90D {runId}`, group `Head Office`, Status `Draft`, memiliki satu file: DU-068-8.
  - DU-068-4: Aset `Printer HP M404 {runId}`, group `Branch Bandung`, Status `Active`, memiliki dua file: DU-068-9 dan DU-068-10.
  - DU-068-5: File `foto-laptop-{runId}.jpg`, Source `Asset Photo`, File Format JPG, aset DU-068-2, group `Head Office`, Size `820.4 KB`, aktif.
  - DU-068-6: File `warranty-card-lpt-{runId}.pdf`, Source `Custom Field Document`, Reference `Warranty Card`, File Format PDF, aset DU-068-2, group `Head Office`, Size `300.0 KB`, aktif.
  - DU-068-7: File `laptop-lama-{runId}.png`, Source `Asset Photo`, File Format PNG, aset DU-068-2, group `Head Office`, Size `1.0 MB`, berada di Recycle Bin dengan Auto-Purge In `29 days`.
  - DU-068-8: File `foto-draft-{runId}.jpg`, Source `Asset Photo`, File Format JPG, aset DU-068-3, group `Head Office`, Size `640.0 KB`, aktif.
  - DU-068-9: File `printer-ok-{runId}.jpg`, Source `Asset Photo`, File Format JPG, aset DU-068-4, group `Branch Bandung`, Size `750.0 KB`, aktif.
  - DU-068-10: File `printer-gagal-{runId}.pdf`, Source `Attachment`, Reference `General`, File Format PDF, aset DU-068-4, group `Branch Bandung`, Size `310.0 KB`, aktif.
  - DU-068-11: Aset `Monitor LG 24MK430H {runId}`, group `Head Office`, Status `Active`, memiliki tiga file: DU-068-12, DU-068-13, dan DU-068-14; Asset ID dibentuk server, milik DU-068-11.
  - DU-068-12: File `monitor-depan-{runId}.jpg`, Source `Asset Photo`, File Format JPG, aset DU-068-11, group `Head Office`, Size `410.0 KB`, aktif.
  - DU-068-13: File `monitor-manual-{runId}.pdf`, Source `Attachment`, Reference `General`, File Format PDF, aset DU-068-11, group `Head Office`, Size `280.0 KB`, aktif.
  - DU-068-14: File `monitor-bin-{runId}.png`, Source `Asset Photo`, File Format PNG, aset DU-068-11, group `Head Office`, Size `190.0 KB`, berada di Recycle Bin dengan Auto-Purge In `29 days`.
  - DU-068-15: User `Hendra Gunawan {runId}`, role Group Manager atas group `Head Office` beserta descendant.
  - DU-068-16: User `Wulan Anggraini {runId}`, capability Manage files dengan Read atas group `Branch Bandung` beserta descendant, tanpa capability lain.
- Kondisi:
  - Retensi Recycle Bin bernilai `30 hari`.
  - Pada kelompok «Delete Asset Data: seluruh file aset dihapus permanen secara asinkron», cascade purge atas aset DU-068-2 belum menghapus satu pun file aset itu dari langkah 3 sampai langkah 8 (jeda), dan selesai pada langkah 9.
  - Pada kelompok «Retry sampai berhasil tanpa hitung ganda», penyimpanan file tidak bisa menghapus file `printer-gagal-{runId}.pdf` pada upaya pertama (langkah 18 dan 19), lalu pulih sebelum langkah 21; pada kelompok lain penyimpanan file terjangkau.
  - Pada kelompok «Jeda cascade purge: baris file bertahan dan aksi tetap berjalan», cascade purge atas aset DU-068-11 belum menghapus satu pun file aset itu dari langkah 28 sampai langkah 43 (jeda), dan selesai pada langkah 44.

## Test Steps

### Delete Asset Data: seluruh file aset dihapus permanen secara asinkron
1. `Bagas Pratama {runId}` membaca daftar file tab Files dan Recycle Bin dengan kata kunci `{runId}` langsung ke server
2. Verifikasi aset `Laptop Dell Latitude 5420 {runId}` memiliki tiga file: `foto-laptop-{runId}.jpg` dan `warranty-card-lpt-{runId}.pdf` aktif, serta `laptop-lama-{runId}.png` di Recycle Bin
3. Data aset `Laptop Dell Latitude 5420 {runId}` dihapus lewat Delete Asset Data oleh `Bagas Pratama {runId}`
4. Verifikasi Delete Asset Data ter-commit dan aset `Laptop Dell Latitude 5420 {runId}` tidak lagi ada
5. `Bagas Pratama {runId}` membaca daftar file tab Files dan Recycle Bin dengan kata kunci `{runId}` langsung ke server, segera sesudah commit
6. Verifikasi file `foto-laptop-{runId}.jpg`, `warranty-card-lpt-{runId}.pdf`, dan `laptop-lama-{runId}.png` masih terlihat pada pembacaan ini dan menampilkan Asset `Laptop Dell Latitude 5420 {runId}` serta Group `Head Office` terakhir sebelum aset dihapus, bukan nilai kosong
7. `Bagas Pratama {runId}` meminta Download file `foto-laptop-{runId}.jpg` langsung ke server, segera sesudah pembacaan pada langkah 5
8. Verifikasi Download berhasil karena file `foto-laptop-{runId}.jpg` masih terlihat
9. Cascade purge atas aset `Laptop Dell Latitude 5420 {runId}` selesai
10. Verifikasi file `foto-laptop-{runId}.jpg`, `warranty-card-lpt-{runId}.pdf`, dan `laptop-lama-{runId}.png` terhapus permanen dan tidak lagi ada di tab Files maupun Recycle Bin
11. Verifikasi file `laptop-lama-{runId}.png` terhapus tanpa menunggu countdown retensi `30 hari` berakhir
12. `Bagas Pratama {runId}` mengirim permintaan Delete atas file `foto-laptop-{runId}.jpg` yang sudah dipurge langsung ke server
13. Verifikasi Delete atas file hasil cascade purge itu tidak mengubah apa pun dan diperlakukan sebagai file tidak tersedia

### Penghapusan aset Draft memicu cascade purge yang sama
14. Aset Draft `Camera Canon EOS 90D {runId}` dihapus oleh `Bagas Pratama {runId}`
15. Cascade purge atas aset Draft `Camera Canon EOS 90D {runId}` selesai
16. `Bagas Pratama {runId}` meminta Download file `foto-draft-{runId}.jpg` langsung ke server
17. Verifikasi Download memberi respons tidak ditemukan karena file `foto-draft-{runId}.jpg` sudah terhapus permanen

### Retry sampai berhasil tanpa hitung ganda
18. Data aset `Printer HP M404 {runId}` dihapus lewat Delete Asset Data oleh `Bagas Pratama {runId}`, dan cascade purge atas aset itu berjalan saat file `printer-gagal-{runId}.pdf` tidak bisa dihapus dari penyimpanan
19. Verifikasi file `printer-ok-{runId}.jpg` terhapus permanen pada upaya pertama, sedangkan file `printer-gagal-{runId}.pdf` masih ada
20. Cascade purge atas aset `Printer HP M404 {runId}` dicoba ulang sampai penyimpanan pulih dan penghapusan berhasil
21. Verifikasi file `printer-gagal-{runId}.pdf` akhirnya terhapus permanen, tanpa batas jumlah percobaan
22. Cascade purge atas aset `Printer HP M404 {runId}` dijalankan lagi
23. `Bagas Pratama {runId}` membaca daftar file tab Files dan Recycle Bin dengan kata kunci `{runId}` langsung ke server
24. Verifikasi file `printer-ok-{runId}.jpg` dan `printer-gagal-{runId}.pdf` tetap tidak ada di tab Files maupun Recycle Bin
25. Verifikasi file `monitor-depan-{runId}.jpg` milik aset lain tetap ada, sehingga tidak ada file lain yang ikut terhapus
26. `Bagas Pratama {runId}` membaca Changelog File Manager dengan filter File Name `printer-ok-{runId}.jpg` dan `printer-gagal-{runId}.pdf` langsung ke server
27. Verifikasi tidak ada entri Changelog File Manager untuk File Name `printer-ok-{runId}.jpg` maupun `printer-gagal-{runId}.pdf`, dan tidak ada entri yang mencatat jumlah file yang terhapus oleh cascade purge

### Jeda cascade purge: baris file bertahan dan aksi tetap berjalan
28. Data aset `Monitor LG 24MK430H {runId}` dihapus lewat Delete Asset Data oleh `Bagas Pratama {runId}`
29. `Bagas Pratama {runId}` membaca daftar file tab Files dan Recycle Bin dengan kata kunci `{runId}` langsung ke server, segera sesudah commit
30. Verifikasi file `monitor-depan-{runId}.jpg`, `monitor-manual-{runId}.pdf`, dan `monitor-bin-{runId}.png` masih terlihat dan menampilkan Asset `Monitor LG 24MK430H {runId}` serta Group `Head Office` terakhir sebelum aset dihapus
31. Verifikasi ketiga file itu menampilkan Asset ID milik DU-068-11 terakhir sebelum aset dihapus, bukan nilai kosong
32. `Hendra Gunawan {runId}` membaca daftar file tab Files dan Recycle Bin dengan kata kunci `{runId}` langsung ke server
33. Verifikasi file `monitor-depan-{runId}.jpg` terlihat oleh `Hendra Gunawan {runId}` karena scope group terakhirnya `Head Office`
34. `Wulan Anggraini {runId}` membaca daftar file tab Files dan Recycle Bin dengan kata kunci `{runId}` langsung ke server
35. Verifikasi file `monitor-depan-{runId}.jpg` tidak terlihat oleh `Wulan Anggraini {runId}` karena group `Head Office` di luar scopenya
36. `Bagas Pratama {runId}` meminta Preview file `monitor-depan-{runId}.jpg` langsung ke server
37. Verifikasi Preview berhasil selama jeda
38. `Bagas Pratama {runId}` meminta Download file `monitor-depan-{runId}.jpg` langsung ke server
39. Verifikasi Download berhasil selama jeda
40. `Bagas Pratama {runId}` mengirim permintaan Delete atas file `monitor-manual-{runId}.pdf` langsung ke server
41. Verifikasi Delete berhasil selama jeda dan file `monitor-manual-{runId}.pdf` berpindah ke Recycle Bin
42. `Bagas Pratama {runId}` mengirim permintaan Permanently Delete atas file `monitor-bin-{runId}.png` langsung ke server
43. Verifikasi Permanently Delete berhasil selama jeda dan file `monitor-bin-{runId}.png` terhapus permanen
44. Cascade purge atas aset `Monitor LG 24MK430H {runId}` selesai
45. `Bagas Pratama {runId}` mengirim permintaan Permanently Delete atas file `monitor-manual-{runId}.pdf` yang sudah dipurge langsung ke server
46. Verifikasi Permanently Delete atas file hasil cascade purge itu tidak mengubah apa pun dan diperlakukan sebagai file tidak tersedia
