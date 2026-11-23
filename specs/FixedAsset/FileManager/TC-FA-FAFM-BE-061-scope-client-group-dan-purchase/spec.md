---
id: TC-FA-FAFM-BE-061-scope-client-group-dan-purchase
title: "Server menegakkan scope client, scope group, dan visibilitas kelompok Purchase"
layer: be-e2e
priority: Critical
caseType: Negative
status: ready-for-automation
owner: BE
sourceRules: ["DIM-04b", "DIM-04c", "DIM-04d", "EC-13", "F-FAFM-01.k1", "F-FAFM-01b", "FAFM-LOGIC-09b", "SYN-07f", "V-11", "§6#p3", "§9.4.3#b2", "§9.11#p1"]
smoke: []
dependsOn: []
trace:
  "DIM-04b": [3, 5, 7, 9, 11]
  "DIM-04c": [15, 17, 19, 21, 23]
  "DIM-04d": [31, 33, 35, 37, 39, 41, 62]
  "EC-13": [5, 7, 9, 11, 17, 19, 21, 23, 33, 35, 37, 62]
  "F-FAFM-01.k1": [5, 7, 9, 11, 17, 19, 21, 23]
  "F-FAFM-01b": [2, 3, 14, 15, 53, 55]
  "FAFM-LOGIC-09b": [33, 35, 37, 39, 41]
  "SYN-07f": [56]
  "V-11": [5, 7, 9, 11, 12, 17, 19, 21, 23, 24, 33, 35, 37, 42, 62, 64]
  "§6#p3": [5, 17, 26, 29, 66]
  "§9.4.3#b2": [5, 7, 17, 19]
  "§9.11#p1": [3, 44, 46, 47, 49, 53, 55, 58, 60, 69]
---

# Server menegakkan scope client, scope group, dan visibilitas kelompok Purchase

## Prerequisites
- Aktor: Total Control `Bagas Pratama {runId}`, Group Manager `Hendra Gunawan {runId}`, pemegang Manage files `Wulan Anggraini {runId}` dan `Dimas Prakoso {runId}`, serta `Maya Kartika {runId}` yang role-nya punya akses Attachments kelompok Purchase.
- Data:
  - DU-061-1: User `Bagas Pratama {runId}`, role Total Control, cakupan seluruh group.
  - DU-061-2: User `Hendra Gunawan {runId}`, role Group Manager atas group `Head Office` beserta descendant.
  - DU-061-3: User `Wulan Anggraini {runId}`, capability Manage files dengan Read atas group `Branch Bandung` beserta descendant, tanpa capability lain.
  - DU-061-4: User `Maya Kartika {runId}`, role dengan akses Attachments kelompok Purchase, Read atas group `Head Office` beserta descendant.
  - DU-061-5: User `Dimas Prakoso {runId}`, capability Manage files dengan Read dan Delete atas group `Head Office` beserta descendant, tanpa akses Attachments kelompok Purchase.
  - DU-061-6: Aset `Laptop Dell Latitude 5420 {runId}`, group `Head Office`, Status Active.
  - DU-061-7: Aset `Scanner Epson DS-530 {runId}`, group `Branch Bandung`, Status Active.
  - DU-061-8: Aset `Monitor LG 24 {runId}`, group `Head Office`, Status Active.
  - DU-061-9: Aset `Printer HP M404 {runId}`, group `Head Office`, Status `Disposed`.
  - DU-061-10: File `laptop-ho-{runId}.jpg`, Source `Asset Photo`, File Format JPG, aset DU-061-6, group `Head Office`, Size `820.4 KB`, aktif.
  - DU-061-11: File `laptop-ho-lama-{runId}.png`, Source `Asset Photo`, File Format PNG, aset DU-061-6, group `Head Office`, Size `1.0 MB`, sudah berada di Recycle Bin dan masih dalam masa retensi.
  - DU-061-12: File `scan-bb-{runId}.jpg`, Source `Asset Photo`, File Format JPG, aset DU-061-7, group `Branch Bandung`, Size `640.0 KB`, aktif.
  - DU-061-13: File `scan-bb-lama-{runId}.png`, Source `Asset Photo`, File Format PNG, aset DU-061-7, group `Branch Bandung`, Size `900.0 KB`, sudah berada di Recycle Bin dan masih dalam masa retensi.
  - DU-061-14: File `foto-monitor-{runId}.jpg`, Source `Asset Photo`, File Format JPG, aset DU-061-8, group `Head Office`, Size `750.0 KB`, aktif.
  - DU-061-15: File `manual-monitor-{runId}.pdf`, Source `Attachment`, Reference `General`, File Format PDF, aset DU-061-8, group `Head Office`, Size `310.0 KB`, aktif.
  - DU-061-16: File `invoice-printer-{runId}.pdf`, Source `Attachment`, Reference `Purchase`, File Format PDF, aset DU-061-9, group `Head Office`, Size `450.2 KB`, aktif.
  - DU-061-17: File `warranty-printer-{runId}.pdf`, Source `Attachment`, Reference `General`, File Format PDF, aset DU-061-9, group `Head Office`, Size `300.0 KB`, aktif.
  - DU-061-18: File `dokumen-klien-lain-{runId}.pdf`, Source `Attachment`, Reference `General`, File Format PDF, milik klien lain yang bukan entitas aktor, Size `310.0 KB`, aktif.
  - DU-061-19: File `arsip-klien-lain-{runId}.pdf`, Source `Attachment`, Reference `General`, File Format PDF, milik klien lain yang bukan entitas aktor, Size `300.0 KB`, sudah berada di Recycle Bin dan masih dalam masa retensi.
  - DU-061-20: File `kuitansi-laptop-{runId}.pdf`, Source `Attachment`, Reference `Purchase`, File Format PDF, aset DU-061-6, group `Head Office`, Size `200.0 KB`, sudah berada di Recycle Bin dan masih dalam masa retensi.
  - Files Size yang diharapkan untuk aset DU-061-9: `750.2 KB` bagi role dengan akses Purchase dan `300.0 KB` bagi role tanpa akses Purchase, dari 450.2 KB ditambah 300.0 KB.

## Test Steps

### File klien lain diperlakukan tidak ditemukan
1. `Bagas Pratama {runId}` membaca daftar file tab Asset Documents dengan kata kunci `{runId}`
2. Verifikasi daftar memuat file `warranty-printer-{runId}.pdf`, file aset dalam scope `Bagas Pratama {runId}`
3. Verifikasi daftar tidak memuat file `dokumen-klien-lain-{runId}.pdf` milik klien lain
4. `Bagas Pratama {runId}` meminta Preview file `dokumen-klien-lain-{runId}.pdf` langsung ke server
5. Verifikasi respons tidak ditemukan tanpa membocorkan keberadaan file
6. `Bagas Pratama {runId}` meminta Download file `dokumen-klien-lain-{runId}.pdf` langsung ke server
7. Verifikasi respons tidak ditemukan dan tidak ada isi file yang dikirim
8. `Bagas Pratama {runId}` mengirim permintaan Delete atas file `dokumen-klien-lain-{runId}.pdf` langsung ke server
9. Verifikasi respons tidak ditemukan, tanpa mutasi
10. `Bagas Pratama {runId}` mengirim permintaan Permanently Delete atas file `arsip-klien-lain-{runId}.pdf` langsung ke server
11. Verifikasi respons tidak ditemukan, tanpa mutasi
12. Verifikasi file `dokumen-klien-lain-{runId}.pdf` tetap aktif dan file `arsip-klien-lain-{runId}.pdf` tetap berada di Recycle Bin pada entitas pemiliknya, dan tidak ada entri Changelog untuk keduanya pada entitas `Bagas Pratama {runId}`

### File di luar scope group diperlakukan tidak ditemukan
13. `Hendra Gunawan {runId}` membaca daftar file tab Asset Photo dengan kata kunci `{runId}`
14. Verifikasi daftar memuat file `laptop-ho-{runId}.jpg`, file aset dalam scope group `Head Office`
15. Verifikasi daftar tidak memuat file `scan-bb-{runId}.jpg`, file aset di luar scope group `Hendra Gunawan {runId}`
16. `Hendra Gunawan {runId}` meminta Preview file `scan-bb-{runId}.jpg` langsung ke server
17. Verifikasi respons tidak ditemukan tanpa membocorkan keberadaan file
18. `Hendra Gunawan {runId}` meminta Download file `scan-bb-{runId}.jpg` langsung ke server
19. Verifikasi respons tidak ditemukan dan tidak ada isi file yang dikirim
20. `Hendra Gunawan {runId}` mengirim permintaan Delete atas file `scan-bb-{runId}.jpg` langsung ke server
21. Verifikasi respons tidak ditemukan, bukan penolakan hak akses, dan tanpa mutasi
22. `Hendra Gunawan {runId}` mengirim permintaan Permanently Delete atas file `scan-bb-lama-{runId}.png` langsung ke server
23. Verifikasi respons tidak ditemukan, bukan penolakan hak akses, dan tanpa mutasi
24. Verifikasi file `scan-bb-{runId}.jpg` tetap aktif, file `scan-bb-lama-{runId}.png` tetap berada di Recycle Bin, dan tidak ada entri Changelog untuk keduanya

### File di Recycle Bin tetap tersedia, file yang dihapus permanen tidak
25. `Bagas Pratama {runId}` meminta Download file `laptop-ho-lama-{runId}.png` langsung ke server
26. Verifikasi file dikirim sebagai stream karena file yang sudah di-soft-delete masih tersedia
27. `Bagas Pratama {runId}` mengirim permintaan Permanently Delete atas file `laptop-ho-lama-{runId}.png` langsung ke server
28. `Bagas Pratama {runId}` meminta Download file `laptop-ho-lama-{runId}.png` langsung ke server
29. Verifikasi respons tidak ditemukan karena file sudah dihapus permanen

### Visibilitas file kelompok Purchase
30. `Maya Kartika {runId}` meminta Download file `invoice-printer-{runId}.pdf` langsung ke server
31. Verifikasi file dikirim sebagai stream karena role `Maya Kartika {runId}` punya akses Attachments kelompok Purchase
32. `Dimas Prakoso {runId}` meminta Preview file `invoice-printer-{runId}.pdf` langsung ke server
33. Verifikasi respons tidak ditemukan tanpa membocorkan keberadaan file
34. `Dimas Prakoso {runId}` meminta Download file `invoice-printer-{runId}.pdf` langsung ke server
35. Verifikasi respons tidak ditemukan dan tidak ada isi file yang dikirim
36. `Dimas Prakoso {runId}` mengirim permintaan Delete atas file `invoice-printer-{runId}.pdf` langsung ke server
37. Verifikasi respons tidak ditemukan, bukan penolakan hak akses walau `Dimas Prakoso {runId}` punya Delete atas group `Head Office`, dan tanpa mutasi
38. `Dimas Prakoso {runId}` meminta Download (ZIP) atas file `invoice-printer-{runId}.pdf` dan `warranty-printer-{runId}.pdf`
39. Verifikasi berkas ZIP memuat file `warranty-printer-{runId}.pdf` tetapi tidak memuat file `invoice-printer-{runId}.pdf`
40. `Dimas Prakoso {runId}` meminta ekspor `Download as CSV` tab Asset Documents dengan kata kunci `{runId}`
41. Verifikasi ekspor memuat file `warranty-printer-{runId}.pdf` tetapi tidak memuat file `invoice-printer-{runId}.pdf`
42. Verifikasi file `invoice-printer-{runId}.pdf` tetap aktif dan tidak ada entri Changelog untuk file itu
43. `Maya Kartika {runId}` membaca baris aset `Printer HP M404 {runId}` di tab `Disposed & Unmanaged Assets`
44. Verifikasi Files Size baris itu bagi `Maya Kartika {runId}` adalah `750.2 KB`
45. `Dimas Prakoso {runId}` membaca baris aset `Printer HP M404 {runId}` di tab `Disposed & Unmanaged Assets`
46. Verifikasi Files Size baris itu bagi `Dimas Prakoso {runId}` adalah `300.0 KB`
47. Verifikasi Total Size baris itu bagi `Dimas Prakoso {runId}` lebih kecil `450.2 KB` daripada bagi `Maya Kartika {runId}`
48. `Dimas Prakoso {runId}` membaca kartu Storage Usage
49. Verifikasi ukuran Fixed Asset pada kartu Storage Usage bagi `Dimas Prakoso {runId}` tidak lebih kecil daripada `750.2 KB`, karena kartu memuat angka agregat client termasuk file `invoice-printer-{runId}.pdf`

### Scope baris mengikuti group aset saat request, scope Changelog mengikuti group saat aksi
50. `Bagas Pratama {runId}` mengirim permintaan Delete atas file `foto-monitor-{runId}.jpg`
51. Group aset `Monitor LG 24 {runId}` berubah dari `Head Office` menjadi `Branch Bandung`
52. `Hendra Gunawan {runId}` membaca daftar file tab Asset Documents dengan kata kunci `{runId}`
53. Verifikasi daftar tidak memuat file `manual-monitor-{runId}.pdf`, karena scope baris mengikuti group aset pada saat request
54. `Wulan Anggraini {runId}` membaca daftar file tab Asset Documents dengan kata kunci `{runId}`
55. Verifikasi daftar memuat file `manual-monitor-{runId}.pdf`
56. Verifikasi ukuran pada label tab Asset Documents bagi `Wulan Anggraini {runId}` tidak lebih kecil daripada `310.0 KB`, karena sudah mencakup file `manual-monitor-{runId}.pdf` dan dihitung ulang server pada pembacaan berikutnya
57. `Hendra Gunawan {runId}` membaca Changelog
58. Verifikasi Changelog memuat entri Action `Delete` untuk File Name `foto-monitor-{runId}.jpg`, karena scope entri Changelog mengikuti group `Head Office` pada saat aksi
59. `Wulan Anggraini {runId}` membaca Changelog
60. Verifikasi Changelog tidak memuat entri untuk File Name `foto-monitor-{runId}.jpg`, karena scope entri tidak berpindah ke group `Branch Bandung` ketika aset dipindahkan

### Permanently Delete file kelompok Purchase di Recycle Bin diperlakukan tidak ditemukan
61. `Dimas Prakoso {runId}` mengirim permintaan Permanently Delete atas file `kuitansi-laptop-{runId}.pdf` langsung ke server
62. Verifikasi respons tidak ditemukan, bukan penolakan hak akses walau `Dimas Prakoso {runId}` punya Delete atas group `Head Office`, dan tanpa mutasi
63. `Maya Kartika {runId}` membaca Recycle Bin dengan kata kunci `{runId}`
64. Verifikasi file `kuitansi-laptop-{runId}.pdf` tetap berada di Recycle Bin dan tidak ada entri Changelog untuk file itu

### File di Recycle Bin tetap tersedia untuk Preview
65. `Bagas Pratama {runId}` meminta Preview file `scan-bb-lama-{runId}.png` langsung ke server
66. Verifikasi file dikirim sebagai stream karena file yang sudah di-soft-delete masih tersedia untuk Preview

### Kartu Storage Usage tetap memuat angka agregat client bagi role tanpa akses Purchase
67. `Maya Kartika {runId}` membaca kartu Storage Usage
68. `Dimas Prakoso {runId}` membaca kartu Storage Usage
69. Verifikasi ukuran Fixed Asset pada kartu Storage Usage bagi `Dimas Prakoso {runId}` sama dengan bagi `Maya Kartika {runId}`, karena kartu tetap memuat angka agregat client termasuk file kelompok Purchase
