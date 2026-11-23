---
id: TC-FA-FAFM-BE-073-pencatatan-log-file-manager
title: "Pencatatan Changelog File Manager dan hal yang tidak boleh tercatat"
layer: be-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
owner: BE
sourceRules: ["ACT-02g", "ACT-03i", "ACT-04f", "ACT-05f", "ACT-06f", "ARS-01l", "ARS-02j", "ARS-05e", "ARS-06e", "ARS-07f", "ARS-08g", "F-FAFM-06m", "FAFM-LOGIC-04d", "SYN-01g", "SYN-02g", "SYN-03h", "SYN-04f", "SYN-07e", "SYN-08d", "SYN-09f", "SYN-10f", "SYN-11h", "§8.1#r2", "§8.1#r3", "§8.1#r5", "§8.1#r6", "§8.1#b3", "§9.4.1#r15"]
smoke: []
dependsOn: []
trace:
  "ACT-02g": 3
  "ACT-03i": 43
  "ACT-04f": [16, 20]
  "ACT-05f": 9
  "ACT-06f": 23
  "ARS-01l": [3, 16]
  "ARS-02j": [9, 23]
  "ARS-05e": 32
  "ARS-06e": 43
  "ARS-07f": [44, 56]
  "ARS-08g": [44, 56]
  "F-FAFM-06m": [44, 56]
  "FAFM-LOGIC-04d": 36
  "SYN-01g": [3, 5]
  "SYN-02g": [9, 10, 13]
  "SYN-03h": 32
  "SYN-04f": [26, 29]
  "SYN-07e": 45
  "SYN-08d": 46
  "SYN-09f": 44
  "SYN-10f": 57
  "SYN-11h": 57
  "§8.1#r2": 6
  "§8.1#r3": 4
  "§8.1#r5": [26, 29, 32, 36]
  "§8.1#r6": [16, 17, 18]
  "§8.1#b3": [49, 50, 53, 54]
  "§9.4.1#r15": [26, 32, 36]
---

# Pencatatan Changelog File Manager dan hal yang tidak boleh tercatat

## Prerequisites
- Aktor: Total Control `Bagas Pratama {runId}`, Group Manager `Hendra Gunawan {runId}`, Custom `Indra Wijaya {runId}`, dan Custom `Wulan Anggraini {runId}`.
- Data:
  - DU-073-1: User `Bagas Pratama {runId}`, role Total Control, cakupan seluruh group.
  - DU-073-2: User `Hendra Gunawan {runId}`, role Group Manager atas group `Head Office` beserta descendant, akan diubah namanya menjadi `Hendra Setiawan {runId}` pada langkah 11.
  - DU-073-3: User `Indra Wijaya {runId}`, role Custom dengan "Manage files": Read dan Delete pada group `Head Office` dan akses Attachments kelompok Purchase.
  - DU-073-4: User `Wulan Anggraini {runId}`, role Custom dengan "Manage files": Read pada group `Head Office` tanpa akses Attachments kelompok Purchase, yang aksesnya ditambah pada langkah 51.
  - DU-073-5: Aset `Laptop Dell Latitude 5420 {runId}`, group `Head Office`, Status `Active`, pemilik DU-073-11 dan DU-073-23.
  - DU-073-6: Aset `Printer HP M404 {runId}`, group `Head Office`, Status `Active`, pemilik DU-073-12, DU-073-13, DU-073-14, DU-073-15, dan DU-073-19.
  - DU-073-7: Aset `Scanner Epson DS-530 {runId}`, group `Head Office`, Status `Active`, Photo merujuk DU-073-16.
  - DU-073-8: Aset `Monitor LG 24 {runId}`, group `Head Office`, Status `Active`, Photo merujuk DU-073-18.
  - DU-073-9: Aset `Tablet Samsung Galaxy Tab {runId}`, group `Head Office`, Status `Active`, pemilik DU-073-20 dan DU-073-21, akan dihapus lewat Delete Asset Data.
  - DU-073-10: Aset `Camera Canon EOS 90D {runId}`, group `Head Office`, Status `Active`, pemilik DU-073-22, akan ditransfer ke group `Branch Bandung` lalu diubah Status menjadi `Disposed`.
  - DU-073-11: File `manual-delete-{runId}.jpg`, Source `Asset Photo`, File Format JPG, aset DU-073-5, group `Head Office`, Size `820.4 KB`, aktif.
  - DU-073-12: File `bulk-satu-{runId}.pdf`, Source `Attachment`, Reference `General`, File Format PDF, aset DU-073-6, group `Head Office`, Size `310.0 KB`, aktif.
  - DU-073-13: File `bulk-dua-{runId}.pdf`, Source `Attachment`, Reference `General`, File Format PDF, aset DU-073-6, group `Head Office`, Size `450.2 KB`, aktif.
  - DU-073-14: File `bulk-lama-{runId}.pdf`, Source `Attachment`, Reference `General`, File Format PDF, aset DU-073-6, group `Head Office`, Size `300.0 KB`, sudah berada di Recycle Bin dan masih dalam masa retensi.
  - DU-073-15: File `bulk-tidak-ikut-{runId}.pdf`, Source `Attachment`, Reference `General`, File Format PDF, aset DU-073-6, group `Head Office`, Size `640.0 KB`, aktif, tidak diikutkan dalam permintaan bulk.
  - DU-073-16: File `ganti-lama-{runId}.jpg`, Source `Asset Photo`, File Format JPG, aset DU-073-7, group `Head Office`, Size `750.0 KB`, aktif.
  - DU-073-17: File `ganti-baru-{runId}.jpg`, Source `Asset Photo`, File Format JPG, aset DU-073-7, group `Head Office`, Size `600.0 KB`, unggahan pengganti, belum ada sebelum langkah 24.
  - DU-073-18: File `kosong-{runId}.jpg`, Source `Asset Photo`, File Format JPG, aset DU-073-8, group `Head Office`, Size `900.0 KB`, aktif.
  - DU-073-19: File `purge-{runId}.png`, Source `Asset Photo`, File Format PNG, aset DU-073-6, group `Head Office`, Size `1.0 MB`, berada di Recycle Bin dengan batas purge tersimpan sudah terlampaui (Auto-Purge In `0 days`).
  - DU-073-20: File `cascade-aktif-{runId}.pdf`, Source `Attachment`, Reference `General`, File Format PDF, aset DU-073-9, group `Head Office`, Size `520.0 KB`, aktif.
  - DU-073-21: File `cascade-bin-{runId}.png`, Source `Asset Photo`, File Format PNG, aset DU-073-9, group `Head Office`, Size `510.0 KB`, berada di Recycle Bin dan masih dalam masa retensi.
  - DU-073-22: File `aman-{runId}.pdf`, Source `Attachment`, Reference `General`, File Format PDF, aset DU-073-10, group `Head Office`, Size `430.0 KB`, aktif, tidak di-Delete oleh spec ini.
  - DU-073-23: File `invoice-{runId}.pdf`, Source `Attachment`, Reference `Purchase`, File Format PDF, aset DU-073-5, group `Head Office`, Size `450.2 KB`, aktif.
- Kondisi:
  - Retensi Recycle Bin bernilai `30 hari`.

## Test Steps

### Delete manual dan Permanently Delete manual: satu entri per file
1. `Bagas Pratama {runId}` mengirim permintaan Delete atas file `manual-delete-{runId}.jpg` langsung ke server
2. `Bagas Pratama {runId}` membaca Changelog File Manager dengan filter File Name `manual-delete-{runId}.jpg` langsung ke server
3. Verifikasi ada tepat satu entri Changelog dengan Action `Delete` untuk File Name `manual-delete-{runId}.jpg`
4. Verifikasi entri itu memuat Field `File Name`, Old Value `manual-delete-{runId}.jpg`, dan New Value `—`
5. Verifikasi Modified By entri itu adalah pengguna pelaku `Bagas Pratama {runId}`
6. Verifikasi entri itu tercatat pada object path `File Manager`
7. `Hendra Gunawan {runId}` mengirim permintaan Permanently Delete atas file `manual-delete-{runId}.jpg` langsung ke server
8. `Bagas Pratama {runId}` membaca Changelog File Manager dengan filter File Name `manual-delete-{runId}.jpg` langsung ke server
9. Verifikasi ada tepat satu entri Changelog dengan Action `Permanently Delete`, Field `File Name`, Old Value `manual-delete-{runId}.jpg`, dan New Value `—`
10. Verifikasi entri Delete dan entri Permanently Delete untuk file yang sama memiliki Modified By berbeda: `Bagas Pratama {runId}` dan `Hendra Gunawan {runId}`

### Aktor di-rename sesudah entri dicatat
11. Nama user `Hendra Gunawan {runId}` diubah menjadi `Hendra Setiawan {runId}`
12. `Bagas Pratama {runId}` membaca Changelog File Manager dengan filter File Name `manual-delete-{runId}.jpg` langsung ke server
13. Verifikasi Modified By entri Permanently Delete tetap `Hendra Gunawan {runId}`, bukan nama baru `Hendra Setiawan {runId}`

### Bulk: satu entri per file yang diproses, item yang dilewati tidak tercatat
14. `Bagas Pratama {runId}` mengirim permintaan Delete bulk atas file `bulk-satu-{runId}.pdf`, `bulk-dua-{runId}.pdf`, dan `bulk-lama-{runId}.pdf` langsung ke server
15. `Bagas Pratama {runId}` membaca Changelog File Manager dengan filter File Name `bulk-satu-{runId}.pdf`, `bulk-dua-{runId}.pdf`, `bulk-lama-{runId}.pdf`, dan `bulk-tidak-ikut-{runId}.pdf` langsung ke server
16. Verifikasi ada tepat satu entri Changelog `Delete` untuk File Name `bulk-satu-{runId}.pdf` dan satu untuk File Name `bulk-dua-{runId}.pdf`
17. Verifikasi tidak ada entri Changelog baru untuk File Name `bulk-lama-{runId}.pdf` yang dilewati karena sudah berada di Recycle Bin
18. Verifikasi tidak ada entri Changelog untuk File Name `bulk-tidak-ikut-{runId}.pdf` yang tidak diikutkan dalam permintaan bulk
19. `Bagas Pratama {runId}` membaca ulang Changelog File Manager dengan filter yang sama langsung ke server
20. Verifikasi entri `bulk-satu-{runId}.pdf` dan `bulk-dua-{runId}.pdf` yang ditulis oleh permintaan bulk yang sama tampil tepat sekali dan dalam urutan yang sama pada pembacaan langkah 15 dan langkah 19
21. `Bagas Pratama {runId}` mengirim permintaan Permanently Delete bulk atas file `bulk-satu-{runId}.pdf` dan `bulk-dua-{runId}.pdf` langsung ke server
22. `Bagas Pratama {runId}` membaca Changelog File Manager dengan filter File Name `bulk-satu-{runId}.pdf` dan `bulk-dua-{runId}.pdf` langsung ke server
23. Verifikasi ada tepat satu entri Changelog `Permanently Delete` untuk File Name `bulk-satu-{runId}.pdf` dan satu untuk File Name `bulk-dua-{runId}.pdf`

### Jalur non-form: auto-transition, auto-purge, dan cascade purge
24. Record aset `Scanner Epson DS-530 {runId}` disimpan atas nama `Bagas Pratama {runId}` dengan Photo diganti ke file baru `ganti-baru-{runId}.jpg`
25. `Bagas Pratama {runId}` membaca Changelog File Manager dengan filter File Name `ganti-lama-{runId}.jpg` langsung ke server
26. Verifikasi ada tepat satu entri Changelog `Delete` untuk File Name `ganti-lama-{runId}.jpg` dengan Modified By `System`, karena file diganti
27. Record aset `Monitor LG 24 {runId}` disimpan atas nama `Bagas Pratama {runId}` dengan Photo dikosongkan tanpa pengganti
28. `Bagas Pratama {runId}` membaca Changelog File Manager dengan filter File Name `kosong-{runId}.jpg` langsung ke server
29. Verifikasi ada tepat satu entri Changelog `Delete` untuk File Name `kosong-{runId}.jpg` dengan Modified By `Bagas Pratama {runId}`, bukan `System`, karena file dikosongkan tanpa pengganti
30. Job auto-purge harian berjalan
31. `Bagas Pratama {runId}` membaca Changelog File Manager dengan filter File Name `purge-{runId}.png` langsung ke server
32. Verifikasi ada tepat satu entri Changelog `Permanently Delete` untuk File Name `purge-{runId}.png` dengan Modified By `System`
33. Data aset `Tablet Samsung Galaxy Tab {runId}` dihapus lewat Delete Asset Data oleh `Bagas Pratama {runId}`
34. Cascade purge atas aset `Tablet Samsung Galaxy Tab {runId}` selesai
35. `Bagas Pratama {runId}` membaca Changelog File Manager dengan filter File Name `cascade-aktif-{runId}.pdf` dan `cascade-bin-{runId}.png` langsung ke server
36. Verifikasi tidak ada entri Changelog File Manager untuk File Name `cascade-aktif-{runId}.pdf` maupun `cascade-bin-{runId}.png`, dan tidak ada entri yang mencatat jumlah file yang terhapus oleh cascade purge

### Hal yang tidak boleh tercatat
37. `Bagas Pratama {runId}` meminta Download file `aman-{runId}.pdf` langsung ke server
38. `Bagas Pratama {runId}` meminta ZIP Download atas file `aman-{runId}.pdf` langsung ke server
39. `Bagas Pratama {runId}` membaca kartu Storage Usage dan tab Asset Data langsung ke server
40. Aset `Camera Canon EOS 90D {runId}` ditransfer ke group `Branch Bandung`
41. Status aset `Camera Canon EOS 90D {runId}` diubah menjadi `Disposed`
42. `Bagas Pratama {runId}` membaca Changelog File Manager dengan filter File Name `aman-{runId}.pdf` langsung ke server
43. Verifikasi Download single dan ZIP Download atas file `aman-{runId}.pdf` tidak menambah entri Changelog untuk File Name `aman-{runId}.pdf`
44. Verifikasi pembacaan kartu Storage Usage dan tab Asset Data tidak menambah entri Changelog untuk File Name `aman-{runId}.pdf`
45. Verifikasi transfer aset `Camera Canon EOS 90D {runId}` tidak menambah entri Changelog File Manager untuk File Name `aman-{runId}.pdf`
46. Verifikasi perubahan Status aset `Camera Canon EOS 90D {runId}` menjadi `Disposed` tidak menambah entri Changelog File Manager untuk File Name `aman-{runId}.pdf`

### Visibilitas entri kelompok Purchase mengikuti akses saat dibaca
47. `Indra Wijaya {runId}` mengirim permintaan Delete atas file `invoice-{runId}.pdf` langsung ke server
48. `Wulan Anggraini {runId}` membaca Changelog File Manager dan opsi filter File Name serta Modified By dengan kata kunci `{runId}` langsung ke server
49. Verifikasi `Wulan Anggraini {runId}` tidak melihat entri Changelog untuk File Name `invoice-{runId}.pdf`
50. Verifikasi opsi filter File Name dan Modified By bagi `Wulan Anggraini {runId}` tidak memuat `invoice-{runId}.pdf` maupun `Indra Wijaya {runId}`
51. Akses Attachments kelompok Purchase role `Wulan Anggraini {runId}` ditambah
52. `Wulan Anggraini {runId}` membaca Changelog File Manager dan opsi filter File Name serta Modified By dengan kata kunci `{runId}` langsung ke server
53. Verifikasi `Wulan Anggraini {runId}` melihat entri Changelog `Delete` untuk File Name `invoice-{runId}.pdf`, termasuk entri yang ditulis sebelum akses ditambah
54. Verifikasi opsi filter File Name dan Modified By bagi `Wulan Anggraini {runId}` memuat `invoice-{runId}.pdf` dan `Indra Wijaya {runId}`

### Pembacaan kartu dan tab Asset Data tidak menambah entri milik aktor, dan Changelog hanya mencatat Delete dan Permanently Delete
55. `Bagas Pratama {runId}` membaca Changelog File Manager dengan filter Modified By `Bagas Pratama {runId}` langsung ke server
56. Verifikasi pembacaan langkah 55 memuat tepat enam entri, yaitu entri `Delete` dan `Permanently Delete` hasil aksi `Bagas Pratama {runId}` pada langkah 1, 14, 21, dan 27, tanpa entri tambahan dari Download, ZIP Download, serta pembacaan kartu Storage Usage dan tab Asset Data pada langkah 37 sampai 39
57. Verifikasi setiap entri pada pembacaan langkah 55 ber-Action `Delete` atau `Permanently Delete`, tanpa entri dengan Action lain
