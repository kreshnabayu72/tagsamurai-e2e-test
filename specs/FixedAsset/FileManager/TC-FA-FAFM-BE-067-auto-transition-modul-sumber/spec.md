---
id: TC-FA-FAFM-BE-067-auto-transition-modul-sumber
title: "Auto-transition: file lama di-soft-delete saat modul sumber mengganti atau mengosongkan file"
layer: be-e2e
priority: Critical
caseType: Positive
status: ready-for-automation
owner: BE
sourceRules: ["ARS-03a", "ARS-03b", "ARS-03c", "ARS-03d", "ARS-03e", "ARS-03f", "ARS-03g", "ARS-03h", "ARS-03i", "ARS-03j", "ARS-03k", "F-FAFM-04.k1", "F-FAFM-04.k2", "F-FAFM-04a", "F-FAFM-04c", "F-FAFM-04d", "F-FAFM-04e", "F-FAFM-04g", "F-FAFM-04b", "FAFM-LOGIC-07a", "FAFM-LOGIC-07b", "FAFM-LOGIC-07d", "FAFM-LOGIC-07e", "SYN-04a", "SYN-04b", "SYN-04c", "SYN-04d", "SYN-04e", "§9.4.3#b3"]
smoke: []
dependsOn: []
trace:
  "ARS-03a": 31
  "ARS-03b": [5, 31]
  "ARS-03c": [6, 7, 16, 17, 32, 33]
  "ARS-03d": 10
  "ARS-03e": 22
  "ARS-03f": [24, 25, 27, 28]
  "ARS-03g": 2
  "ARS-03h": [4, 13, 14]
  "ARS-03i": [36, 37, 38]
  "ARS-03j": 10
  "ARS-03k": [3, 8, 15, 18, 34]
  "F-FAFM-04.k1": [10, 36]
  "F-FAFM-04.k2": [25, 26, 27, 28]
  "F-FAFM-04a": [2, 12]
  "F-FAFM-04c": [4, 5]
  "F-FAFM-04d": [37, 38]
  "F-FAFM-04e": [24, 26]
  "F-FAFM-04g": [20, 21, 40, 41, 42]
  "F-FAFM-04b": [2, 3]
  "FAFM-LOGIC-07a": [2, 30]
  "FAFM-LOGIC-07b": 12
  "FAFM-LOGIC-07d": [3, 8, 34]
  "FAFM-LOGIC-07e": [15, 18]
  "SYN-04a": [4, 13]
  "SYN-04b": 2
  "SYN-04c": [4, 9]
  "SYN-04d": 2
  "SYN-04e": 10
  "§9.4.3#b3": 9
---

# Auto-transition: file lama di-soft-delete saat modul sumber mengganti atau mengosongkan file

## Prerequisites
- Aktor: Total Control `Bagas Pratama {runId}`.
- Data:
  - DU-067-1: User `Bagas Pratama {runId}`, role Total Control, cakupan seluruh group.
  - DU-067-2: Aset `Laptop Dell Latitude 5420 {runId}`, group `Head Office`, Status `Active`, Photo merujuk DU-067-6.
  - DU-067-3: Aset `Scanner Epson DS-530 {runId}`, group `Branch Bandung`, Status `Active`, Photo merujuk DU-067-9.
  - DU-067-4: Aset `Printer HP M404 {runId}`, group `Head Office`, Status `Active`, dokumen Attachment kelompok General yang rujukannya sudah dikosongkan karena DU-067-10 di-soft-delete.
  - DU-067-5: Aset `Monitor LG 24 {runId}`, group `Head Office`, Status `Active`, Photo merujuk DU-067-11.
  - DU-067-6: File `foto-laptop-lama-{runId}.jpg`, Source `Asset Photo`, File Format JPG, aset DU-067-2, group `Head Office`, Size `820.4 KB`, aktif.
  - DU-067-7: File `foto-laptop-baru-{runId}.jpg`, Source `Asset Photo`, File Format JPG, Size `640.0 KB`, unggahan pengganti pertama untuk aset DU-067-2, belum ada sebelum langkah 1.
  - DU-067-8: File `foto-laptop-baru2-{runId}.jpg`, Source `Asset Photo`, File Format JPG, Size `700.0 KB`, unggahan pengganti kedua untuk aset DU-067-2, belum ada sebelum langkah 29.
  - DU-067-9: File `foto-scanner-{runId}.jpg`, Source `Asset Photo`, File Format JPG, aset DU-067-3, group `Branch Bandung`, Size `750.0 KB`, aktif.
  - DU-067-10: File `manual-printer-{runId}.pdf`, Source `Attachment`, Reference `General`, File Format PDF, aset DU-067-4, group `Head Office`, Size `310.0 KB`, sudah berada di Recycle Bin dan masih dalam masa retensi.
  - DU-067-11: File `foto-monitor-lama-{runId}.jpg`, Source `Asset Photo`, File Format JPG, aset DU-067-5, group `Head Office`, Size `880.0 KB`, aktif.
  - DU-067-12: File `foto-monitor-baru-{runId}.jpg`, Source `Asset Photo`, File Format JPG, Size `600.0 KB`, unggahan pengganti untuk aset DU-067-5, belum ada sebelum langkah 23.
  - DU-067-13: Aset `Tablet Samsung Galaxy Tab {runId}`, group `Branch Bandung`, Status `Active`, Photo merujuk DU-067-14.
  - DU-067-14: File `foto-tablet-lama-{runId}.jpg`, Source `Asset Photo`, File Format JPG, aset DU-067-13, group `Branch Bandung`, Size `900.0 KB`, aktif.
  - DU-067-15: File `foto-tablet-baru-{runId}.jpg`, Source `Asset Photo`, File Format JPG, Size `1.0 MB`, unggahan pengganti untuk aset DU-067-13, tidak ada sesudah langkah 35 karena transaksi gagal.
  - DU-067-16: Aset `Projector Epson EB-X49 {runId}`, group `Head Office`, Status `Active`, dokumen Attachment kelompok General yang rujukannya sudah dikosongkan karena DU-067-17 dihapus permanen.
  - DU-067-17: File `panduan-projector-{runId}.pdf`, Source `Attachment`, Reference `General`, File Format PDF, aset DU-067-16, group `Head Office`, Size `450.0 KB`, sudah dihapus permanen (tidak ada di tab Files maupun Recycle Bin).
- Kondisi:
  - Pada kelompok «Rujukan ke file di Recycle Bin ditolak», form record aset `Printer HP M404 {runId}` dibuka sebelum file `manual-printer-{runId}.pdf` di-soft-delete sehingga masih membawa rujukan lama.
  - Pada kelompok «Rujukan ke file yang sudah dihapus permanen ditolak», form record aset `Projector Epson EB-X49 {runId}` dibuka sebelum file `panduan-projector-{runId}.pdf` dihapus permanen sehingga masih membawa rujukan lama.
  - Pada kelompok «Kegagalan di tengah transaksi», transaksi penyimpanan record gagal di tengah; pada kelompok lain transaksi berhasil.

## Test Steps

### Mengganti file: file lama di-soft-delete atomik dengan aktor System
1. Record aset `Laptop Dell Latitude 5420 {runId}` atas nama `Bagas Pratama {runId}` disimpan dengan Photo diganti ke file baru `foto-laptop-baru-{runId}.jpg`
2. Verifikasi file lama `foto-laptop-lama-{runId}.jpg` berada di Recycle Bin
3. Verifikasi aktor soft-delete file `foto-laptop-lama-{runId}.jpg` adalah `System`
4. Verifikasi file baru `foto-laptop-baru-{runId}.jpg` tampil di tab Files sebagai file aktif dan Photo aset `Laptop Dell Latitude 5420 {runId}` merujuk file itu
5. Verifikasi untuk penggantian ini dibuat tepat satu file baru, yaitu `foto-laptop-baru-{runId}.jpg`
6. Verifikasi ada satu entri Changelog untuk penggantian ini
7. Verifikasi ada satu entri Activity Log untuk penggantian ini
8. Verifikasi aktor entri Activity Log penggantian ini adalah `System`
9. Verifikasi file lama `foto-laptop-lama-{runId}.jpg` tidak lagi tampil di tab Files
10. Verifikasi rujukan record sumber, file lama, dan file baru berubah bersama pada pembacaan pertama sesudah simpan, tanpa keadaan setengah jadi

### Mengosongkan file tanpa pengganti: aktor pengguna pelaku
11. Record aset `Scanner Epson DS-530 {runId}` atas nama `Bagas Pratama {runId}` disimpan dengan Photo dikosongkan tanpa pengganti
12. Verifikasi file lama `foto-scanner-{runId}.jpg` berada di Recycle Bin
13. Verifikasi Photo aset `Scanner Epson DS-530 {runId}` kosong
14. Verifikasi tidak ada file baru yang dibuat untuk aset `Scanner Epson DS-530 {runId}`
15. Verifikasi aktor soft-delete file `foto-scanner-{runId}.jpg` adalah pengguna pelaku `Bagas Pratama {runId}`, bukan `System`
16. Verifikasi ada satu entri Changelog untuk pengosongan Photo aset `Scanner Epson DS-530 {runId}`
17. Verifikasi ada satu entri Activity Log untuk pengosongan Photo aset `Scanner Epson DS-530 {runId}`
18. Verifikasi aktor entri Activity Log pengosongan ini adalah pengguna pelaku `Bagas Pratama {runId}`, bukan `System`

### Rujukan ke file di Recycle Bin ditolak
19. Record aset `Printer HP M404 {runId}` atas nama `Bagas Pratama {runId}` disimpan dengan form yang masih membawa rujukan ke file `manual-printer-{runId}.pdf` yang sudah di-soft-delete
20. Verifikasi penyimpanan ditolak dan record aset `Printer HP M404 {runId}` tidak berubah
21. Verifikasi rujukan aset `Printer HP M404 {runId}` tidak dikembalikan ke file `manual-printer-{runId}.pdf` di Recycle Bin
22. Verifikasi file `manual-printer-{runId}.pdf` tetap berada di Recycle Bin tanpa entri Changelog baru

### Delete manual dan auto-transition serentak pada file yang sama
23. `Bagas Pratama {runId}` mengirim permintaan Delete atas file `foto-monitor-lama-{runId}.jpg` langsung ke server, serentak dengan penyimpanan record aset `Monitor LG 24 {runId}` dengan Photo diganti ke file baru `foto-monitor-baru-{runId}.jpg`
24. Verifikasi file `foto-monitor-lama-{runId}.jpg` berada di Recycle Bin tepat satu kali
25. Verifikasi ada tepat satu entri Changelog soft-delete untuk File Name `foto-monitor-lama-{runId}.jpg`
26. Verifikasi aktor entri itu adalah salah satu dari pengguna pelaku `Bagas Pratama {runId}` atau `System` sesuai transaksi yang commit lebih dulu, dan tidak ada entri kedua dari transaksi yang kalah
27. Verifikasi Photo aset `Monitor LG 24 {runId}` tidak merujuk file `foto-monitor-lama-{runId}.jpg` yang berada di Recycle Bin
28. Verifikasi setiap file `foto-monitor-baru-{runId}.jpg` yang ada sebagai file aktif dirujuk Photo aset `Monitor LG 24 {runId}`, tanpa file baru yang tidak dirujuk record mana pun

### Penggantian berulang menambah efek
29. Record aset `Laptop Dell Latitude 5420 {runId}` atas nama `Bagas Pratama {runId}` disimpan dengan Photo diganti lagi ke file baru `foto-laptop-baru2-{runId}.jpg`
30. Verifikasi file `foto-laptop-baru-{runId}.jpg` ikut di-soft-delete ke Recycle Bin
31. Verifikasi dibuat satu file baru lagi, yaitu `foto-laptop-baru2-{runId}.jpg`, dan Photo aset `Laptop Dell Latitude 5420 {runId}` merujuk file itu
32. Verifikasi ada dua entri Changelog penggantian untuk aset `Laptop Dell Latitude 5420 {runId}`, satu per penggantian
33. Verifikasi ada dua entri Activity Log penggantian untuk aset `Laptop Dell Latitude 5420 {runId}`, satu per penggantian
34. Verifikasi aktor entri Activity Log penggantian kedua adalah `System`

### Kegagalan di tengah transaksi
35. Record aset `Tablet Samsung Galaxy Tab {runId}` atas nama `Bagas Pratama {runId}` disimpan dengan Photo diganti ke file baru `foto-tablet-baru-{runId}.jpg`, dan transaksi gagal di tengah
36. Verifikasi file lama `foto-tablet-lama-{runId}.jpg` tetap aktif dan Photo aset `Tablet Samsung Galaxy Tab {runId}` masih merujuk file itu
37. Verifikasi file baru `foto-tablet-baru-{runId}.jpg` tidak ada
38. Verifikasi tidak ada entri Changelog maupun Activity Log baru untuk aset `Tablet Samsung Galaxy Tab {runId}`

### Rujukan ke file yang sudah dihapus permanen ditolak
39. Record aset `Projector Epson EB-X49 {runId}` atas nama `Bagas Pratama {runId}` disimpan dengan form yang masih membawa rujukan ke file `panduan-projector-{runId}.pdf` yang sudah dihapus permanen
40. Verifikasi penyimpanan ditolak dan record aset `Projector Epson EB-X49 {runId}` tidak berubah
41. Verifikasi rujukan aset `Projector Epson EB-X49 {runId}` tidak dikembalikan ke file `panduan-projector-{runId}.pdf`
42. Verifikasi file `panduan-projector-{runId}.pdf` tetap tidak ada, baik di tab Files maupun di Recycle Bin
