---
id: TC-FA-FAFM-BE-069-perhitungan-storage-fams
title: "Perhitungan Storage FAMS per komponen, realtime, dan tidak memblokir aksi"
layer: be-e2e
priority: Medium
caseType: Positive
status: draft
owner: BE
sourceRules: ["ARS-07a", "ARS-07d", "ARS-08a", "ARS-08b", "ARS-08f", "EC-23", "EC-24", "F-FAFM-01h", "F-FAFM-06b", "F-FAFM-06h", "FAFM-LOGIC-03d", "FAFM-LOGIC-06b", "FAFM-LOGIC-06c", "FAFM-LOGIC-06e", "FAFM-LOGIC-06f", "FAFM-LOGIC-06h", "FAFM-LOGIC-06i", "FAFM-LOGIC-06j", "FAFM-LOGIC-06k", "FAFM-LOGIC-06l", "FAFM-LOGIC-07f", "FAFM-LOGIC-07g", "FAFM-LOGIC-08c", "S-25", "SUC-02f", "SUC-03d", "SYN-03j", "SYN-03k", "SYN-04g", "SYN-05j", "SYN-06f", "SYN-08e", "SYN-09a", "SYN-09b", "SYN-09c", "SYN-09e", "§4.2d#p5", "§9.2#p26", "§9.4.3#b10", "§9.4.3#b11"]
smoke: []
dependsOn: []
trace:
  "ARS-07a": 92
  "ARS-07d": [93, 94]
  "ARS-08a": [3, 4]
  "ARS-08b": 15
  "ARS-08f": 15
  "EC-23": 9
  "EC-24": [65, 68, 70, 72]
  "F-FAFM-01h": [45, 46, 48, 53]
  "F-FAFM-06b": 15
  "F-FAFM-06h": 15
  "FAFM-LOGIC-03d": 10
  "FAFM-LOGIC-06b": [5, 86]
  "FAFM-LOGIC-06c": 15
  "FAFM-LOGIC-06e": [11, 86]
  "FAFM-LOGIC-06f": 63
  "FAFM-LOGIC-06h": [15, 24, 30, 62]
  "FAFM-LOGIC-06i": [10, 38]
  "FAFM-LOGIC-06j": [61, 63]
  "FAFM-LOGIC-06k": [57, 59]
  "FAFM-LOGIC-06l": 65
  "FAFM-LOGIC-07f": 77
  "FAFM-LOGIC-07g": [78, 79]
  "FAFM-LOGIC-08c": 16
  "S-25": 66
  "SUC-02f": 65
  "SUC-03d": 66
  "SYN-03j": [18, 26]
  "SYN-03k": [17, 25]
  "SYN-04g": [36, 37]
  "SYN-05j": [31, 32]
  "SYN-06f": 54
  "SYN-08e": [42, 84, 85]
  "SYN-09a": [5, 41, 83, 86, 89]
  "SYN-09b": 19
  "SYN-09c": 15
  "SYN-09e": [15, 63]
  "§4.2d#p5": [65, 68, 70, 72]
  "§9.2#p26": 10
  "§9.4.3#b10": 59
  "§9.4.3#b11": [11, 86]
---

# Perhitungan Storage FAMS per komponen, realtime, dan tidak memblokir aksi

## Prerequisites
- Aktor: Total Control `Bagas Pratama {runId}` dan Read Only terbatas `Wulan Anggraini {runId}`.
- Data:
  - DU-069-1: User `Bagas Pratama {runId}`, role Total Control, cakupan seluruh group.
  - DU-069-2: User `Wulan Anggraini {runId}`, role Custom dengan "Manage files": Read pada group `Branch Bandung` saja.
  - DU-069-3: Aset `Printer HP M404 {runId}`, group `Branch Bandung`, Status `Disposed`, dengan file DU-069-8, DU-069-9, DU-069-10, dan DU-069-11.
  - DU-069-4: Aset `Scanner Epson DS-530 {runId}`, group `Head Office`, Status `Disposed`, dengan file DU-069-12.
  - DU-069-5: Aset `Monitor LG 24 {runId}`, group `Head Office`, Status `Active`, tanpa file, akan berubah Status menjadi `Unmanaged`.
  - DU-069-6: Aset `Laptop Dell Latitude 5420 {runId}`, group `Head Office`, Status `Active`, tersedia untuk transaksi Assignment baru, Photo merujuk DU-069-13, dengan file DU-069-17 dan DU-069-18.
  - DU-069-7: Aset Draft `Camera Canon EOS 90D {runId}`, group `Head Office`, Status `Draft`, foto registrasi merujuk DU-069-15.
  - DU-069-8: File `dsp-receipt-{runId}.pdf`, Source `Disposal Document`, File Format PDF, aset DU-069-3, group `Branch Bandung`, Size `3.2 MB`, aktif.
  - DU-069-9: File `maint-after-{runId}.jpg`, Source `Maintenance After Photo`, File Format JPG, aset DU-069-3, group `Branch Bandung`, Size `1.9 MB`, aktif.
  - DU-069-10: File `maint-before-{runId}.jpg`, Source `Maintenance Before Photo`, File Format JPG, aset DU-069-3, group `Branch Bandung`, Size `750.0 KB`, berada di Recycle Bin dan masih dalam masa retensi.
  - DU-069-11: File `maint-old-{runId}.jpg`, Source `Maintenance Before Photo`, File Format JPG, aset DU-069-3, group `Branch Bandung`, Size `600.0 KB`, berada di Recycle Bin dengan batas purge tersimpan belum tercapai (Auto-Purge In `29 days`), dan batas purge-nya baru terlewati pada langkah 21.
  - DU-069-12: File `scanner-doc-{runId}.pdf`, Source `Disposal Document`, File Format PDF, aset DU-069-4, group `Head Office`, Size `2.0 MB`, aktif.
  - DU-069-13: File `foto-laptop-lama-{runId}.jpg`, Source `Asset Photo`, File Format JPG, aset DU-069-6, group `Head Office`, Size `820.4 KB`, aktif.
  - DU-069-14: File `foto-laptop-baru-{runId}.jpg`, Source `Asset Photo`, File Format JPG, Size `640.0 KB`, unggahan pengganti untuk aset DU-069-6, belum ada sebelum langkah 34.
  - DU-069-15: File `foto-draft-lama-{runId}.jpg`, Source `Asset Photo`, File Format JPG, aset DU-069-7, group `Head Office`, Size `450.2 KB`, aktif sebagai foto registrasi pertama.
  - DU-069-16: File `foto-draft-baru-{runId}.jpg`, Source `Asset Photo`, File Format JPG, aset DU-069-7, group `Head Office`, Size `640.0 KB`, unggahan pengganti foto registrasi, belum ada sebelum langkah 43.
  - DU-069-17: File `penuh-satu-{runId}.pdf`, Source `Attachment`, Reference `General`, File Format PDF, aset DU-069-6, group `Head Office`, Size `310.0 KB`, aktif.
  - DU-069-18: File `penuh-dua-{runId}.pdf`, Source `Attachment`, Reference `General`, File Format PDF, aset DU-069-6, group `Head Office`, Size `300.0 KB`, berada di Recycle Bin dan masih dalam masa retensi.
  - DU-069-19: File `batal-{runId}.jpg`, Source `Asset Photo`, File Format JPG, Size `500.0 KB`, diunggah ke form yang dibatalkan sebelum tersimpan.
  - DU-069-20: File `handover-{runId}.jpg`, Source `Handover Photo`, File Format JPG, Size `450.2 KB`, foto wajib transaksi pada langkah Photo at start Assignment atas aset DU-069-6 yang upload-nya ditolak saat Storage penuh.
  - DU-069-21: Aset `Router Cisco ISR 4331 {runId}`, group `Head Office`, Status `Active`, dengan file DU-069-22, akan berubah Status menjadi `Unmanaged` lalu kembali `Active`.
  - DU-069-22: File `router-manual-{runId}.pdf`, Source `Attachment`, Reference `General`, File Format PDF, aset DU-069-21, group `Head Office`, Size `1.5 MB`, aktif.
  - DU-069-23: Aset `Tablet Samsung Galaxy Tab S8 {runId}`, group `Head Office`, Status `Active`, sedang dalam transaksi Assignment yang belum dikembalikan dan siap pada langkah Photo at end.
  - DU-069-24: Aset `Proyektor Epson EB-X49 {runId}`, group `Head Office`, Status `Active`, dalam transaksi Transfer yang siap pada langkah Send (Photo at start).
  - DU-069-25: Aset `Kamera Sony ZV-E10 {runId}`, group `Head Office`, Status `Active`, dalam transaksi Transfer yang sudah dikirim dan siap pada langkah Receive (Photo at end).
  - DU-069-26: File `return-{runId}.jpg`, Source `Return Photo`, File Format JPG, Size `410.6 KB`, foto wajib pengembalian aset DU-069-23 yang upload-nya ditolak saat Storage penuh.
  - DU-069-27: File `send-{runId}.jpg`, Source `Send Photo`, File Format JPG, Size `380.4 KB`, foto wajib langkah Send aset DU-069-24 yang upload-nya ditolak saat Storage penuh.
  - DU-069-28: File `receive-{runId}.jpg`, Source `Receive Photo`, File Format JPG, Size `395.8 KB`, foto wajib langkah Receive aset DU-069-25 yang upload-nya ditolak saat Storage penuh.
- Kondisi:
  - Retensi Recycle Bin bernilai `30 hari`.
  - Pada kelompok «Storage penuh tidak memblokir aksi File Manager», «Upload foto wajib transaksi diblokir di titik upload», dan «Blokir upload berlaku pada Return Photo, Send Photo, dan Receive Photo», Total Used client lebih besar dari atau sama dengan Storage Quota; pada kelompok lain Storage client tidak penuh.

## Test Steps

### Pembacaan Storage bersifat read-only dan idempoten
1. `Bagas Pratama {runId}` membaca baris aset `Printer HP M404 {runId}` pada tab Asset Data (Data & Log Size, Files Size, Total Size) langsung ke server
2. `Bagas Pratama {runId}` membaca ulang baris aset `Printer HP M404 {runId}` pada tab Asset Data langsung ke server
3. Verifikasi Data & Log Size, Files Size, dan Total Size pada langkah 2 sama dengan langkah 1
4. Verifikasi pembacaan pada langkah 1 dan 2 tidak membuat entri Changelog baru untuk aset `Printer HP M404 {runId}`
5. Verifikasi Total Size baris aset `Printer HP M404 {runId}` sama dengan Data & Log Size ditambah Files Size

### Delete (soft) memindahkan byte antar komponen tanpa mengubah total
6. `Bagas Pratama {runId}` membaca label tab Maintenance dan baris aset `Printer HP M404 {runId}` pada tab Asset Data langsung ke server
7. `Bagas Pratama {runId}` mengirim permintaan Delete atas file `maint-after-{runId}.jpg` langsung ke server
8. `Bagas Pratama {runId}` membaca label tab Maintenance dan baris aset `Printer HP M404 {runId}` pada tab Asset Data langsung ke server
9. Verifikasi permintaan Delete atas file `maint-after-{runId}.jpg` diterima dan tidak diblokir
10. Verifikasi Files Size baris aset `Printer HP M404 {runId}` pada langkah 8 sama dengan langkah 6, karena file di Recycle Bin tetap terhitung sampai dihapus permanen
11. Verifikasi label tab Maintenance pada langkah 8 turun sebesar Size file `maint-after-{runId}.jpg` (`1.9 MB`) dibanding langkah 6, karena byte itu hanya dihitung di satu komponen

### Permanently Delete langsung menurunkan pemakaian pada pembacaan berikutnya
12. `Bagas Pratama {runId}` membaca label tab Maintenance, label tab `Disposed & Unmanaged Assets`, baris aset `Printer HP M404 {runId}` pada tab Asset Data, dan nilai pemakaian FAMS pada kartu Storage Usage langsung ke server
13. `Bagas Pratama {runId}` mengirim permintaan Permanently Delete atas file `maint-before-{runId}.jpg` langsung ke server
14. `Bagas Pratama {runId}` membaca label tab Maintenance, label tab `Disposed & Unmanaged Assets`, baris aset `Printer HP M404 {runId}` pada tab Asset Data, dan nilai pemakaian FAMS pada kartu Storage Usage langsung ke server
15. Verifikasi Files Size baris aset `Printer HP M404 {runId}` pada langkah 14 turun sebesar Size file `maint-before-{runId}.jpg` (`750.0 KB`) dibanding langkah 12, pada pembacaan pertama sesudah aksi tanpa menunggu laporan berkala
16. Verifikasi Total Size baris aset `Printer HP M404 {runId}` pada langkah 14 turun sebesar `750.0 KB` dibanding langkah 12
17. Verifikasi label tab `Disposed & Unmanaged Assets` pada langkah 14 turun sedikitnya `750.0 KB` dibanding langkah 12
18. Verifikasi label tab Maintenance pada langkah 14 tidak berubah dibanding langkah 12, karena file di Recycle Bin tidak dihitung ke label tab kategori
19. Verifikasi nilai pemakaian FAMS pada kartu Storage Usage pada langkah 14 turun sebesar `750.0 KB` dibanding langkah 12, karena komponen file di Recycle Bin berkurang sebesar Size file itu

### Auto-purge dan cascade purge langsung menurunkan pemakaian
20. `Bagas Pratama {runId}` membaca label tab Maintenance, label tab `Disposed & Unmanaged Assets`, dan baris aset `Printer HP M404 {runId}` pada tab Asset Data langsung ke server
21. Waktu berlalu sampai batas purge file `maint-old-{runId}.jpg` terlewati
22. Job auto-purge harian berjalan
23. `Bagas Pratama {runId}` membaca label tab Maintenance, label tab `Disposed & Unmanaged Assets`, label tab kategori Source `Disposal Document`, serta baris aset `Printer HP M404 {runId}` dan baris aset `Scanner Epson DS-530 {runId}` pada tab Asset Data langsung ke server
24. Verifikasi Files Size baris aset `Printer HP M404 {runId}` pada langkah 23 turun sebesar Size file `maint-old-{runId}.jpg` (`600.0 KB`) dibanding langkah 20
25. Verifikasi label tab `Disposed & Unmanaged Assets` pada langkah 23 turun sedikitnya `600.0 KB` dibanding langkah 20, karena Total Size memuat file di Recycle Bin
26. Verifikasi label tab Maintenance pada langkah 23 tidak berubah dibanding langkah 20, karena file di Recycle Bin tidak dihitung ke label tab kategori
27. Data aset `Scanner Epson DS-530 {runId}` dihapus lewat Delete Asset Data oleh `Bagas Pratama {runId}`
28. Cascade purge atas aset `Scanner Epson DS-530 {runId}` selesai
29. `Bagas Pratama {runId}` membaca tab Asset Data dengan kata kunci `Scanner Epson DS-530 {runId}`, label tab `Disposed & Unmanaged Assets`, dan label tab kategori Source `Disposal Document` langsung ke server
30. Verifikasi aset `Scanner Epson DS-530 {runId}` tidak lagi ada pada tab Asset Data dan file `scanner-doc-{runId}.pdf` terhapus permanen
31. Verifikasi label tab `Disposed & Unmanaged Assets` pada langkah 29 turun sebesar Total Size baris aset `Scanner Epson DS-530 {runId}` yang terbaca pada langkah 23
32. Verifikasi label tab kategori Source `Disposal Document` pada langkah 29 turun sebesar Size file aktif `scanner-doc-{runId}.pdf` (`2.0 MB`) dibanding langkah 23, karena cascade purge menghapus file aktif aset itu

### Auto-transition dan perubahan Status aset menghitung ulang label tab
33. `Bagas Pratama {runId}` membaca label tab Asset Photo dan nilai pemakaian FAMS pada kartu Storage Usage langsung ke server
34. Record aset `Laptop Dell Latitude 5420 {runId}` disimpan atas nama `Bagas Pratama {runId}` dengan Photo diganti ke file baru `foto-laptop-baru-{runId}.jpg`
35. `Bagas Pratama {runId}` membaca label tab Asset Photo dan nilai pemakaian FAMS pada kartu Storage Usage langsung ke server
36. Verifikasi label tab Asset Photo pada langkah 35 tidak lagi memuat Size file lama `foto-laptop-lama-{runId}.jpg` (`820.4 KB`) dibanding langkah 33
37. Verifikasi label tab Asset Photo pada langkah 35 memuat Size file baru `foto-laptop-baru-{runId}.jpg` (`640.0 KB`) dibanding langkah 33
38. Verifikasi nilai pemakaian FAMS pada kartu Storage Usage pada langkah 35 naik sebesar `640.0 KB` dibanding langkah 33, karena byte file lama `foto-laptop-lama-{runId}.jpg` hanya berpindah dari komponen file aktif ke komponen Recycle Bin tanpa mengubah total
39. Status aset `Monitor LG 24 {runId}` diubah dari `Active` menjadi `Unmanaged`
40. `Bagas Pratama {runId}` membaca baris aset `Monitor LG 24 {runId}` pada tab Asset Data dan label tab `Disposed & Unmanaged Assets` langsung ke server
41. Verifikasi baris aset `Monitor LG 24 {runId}` pada tab Asset Data memiliki Files Size `0.0 KB` dan Total Size sama dengan Data & Log Size
42. Verifikasi label tab `Disposed & Unmanaged Assets` pada langkah 40 tidak lebih kecil daripada Total Size baris aset `Monitor LG 24 {runId}`, karena label mencakup baris itu dan dihitung ulang server pada pembacaan berikutnya

### Aset Draft: file dihitung aktif, baris Recycle Bin memakai Group pembuat, dan pemakaian dihitung ulang
43. Foto registrasi aset Draft `Camera Canon EOS 90D {runId}` diganti ke file baru `foto-draft-baru-{runId}.jpg` oleh `Bagas Pratama {runId}`
44. `Bagas Pratama {runId}` membaca daftar Recycle Bin dengan kata kunci `{runId}` langsung ke server
45. Verifikasi baris file `foto-draft-lama-{runId}.jpg` pada Recycle Bin menampilkan Asset `—`
46. Verifikasi baris file `foto-draft-lama-{runId}.jpg` pada Recycle Bin menampilkan Group `Head Office`, yaitu Group pembuat record Draft
47. `Wulan Anggraini {runId}` membaca daftar Recycle Bin dengan kata kunci `{runId}` langsung ke server
48. Verifikasi `Wulan Anggraini {runId}` tidak melihat baris file `foto-draft-lama-{runId}.jpg`, karena lingkup aktor mengikuti Group `Head Office`
49. `Bagas Pratama {runId}` membaca label tab Asset Photo dan nilai pemakaian FAMS pada kartu Storage Usage langsung ke server
50. Aset Draft `Camera Canon EOS 90D {runId}` dihapus oleh `Bagas Pratama {runId}`
51. Cascade purge atas aset Draft `Camera Canon EOS 90D {runId}` selesai
52. `Bagas Pratama {runId}` membaca label tab Asset Photo dan nilai pemakaian FAMS pada kartu Storage Usage langsung ke server
53. Verifikasi nilai pemakaian FAMS pada kartu Storage Usage pada langkah 52 turun sedikitnya Size file aktif `foto-draft-baru-{runId}.jpg` (`640.0 KB`) dibanding langkah 49, karena file aset Draft dihitung sebagai file aktif pada komponen file aktif
54. Verifikasi label tab Asset Photo pada langkah 52 tidak lebih besar daripada langkah 49, karena penghapusan aset Draft hanya mengurangi file dan label dihitung ulang server pada pembacaan berikutnya

### Storage penuh tidak memblokir aksi File Manager
55. `Bagas Pratama {runId}` membaca nilai Storage Quota client, nilai Total Used, dan nilai pemakaian FAMS pada kartu Storage Usage langsung ke server
56. `Bagas Pratama {runId}` mengirim permintaan Delete atas file `penuh-satu-{runId}.pdf` langsung ke server
57. Verifikasi permintaan Delete atas file `penuh-satu-{runId}.pdf` diterima dan file berada di Recycle Bin
58. `Bagas Pratama {runId}` mengirim permintaan Permanently Delete atas file `penuh-dua-{runId}.pdf` langsung ke server
59. Verifikasi permintaan Permanently Delete atas file `penuh-dua-{runId}.pdf` diterima dan file terhapus permanen
60. `Bagas Pratama {runId}` membaca nilai Storage Quota client, nilai Total Used, dan nilai pemakaian FAMS pada kartu Storage Usage langsung ke server
61. Verifikasi Storage Quota client pada langkah 60 sama dengan langkah 55, tanpa perubahan akibat aksi File Manager
62. Verifikasi nilai pemakaian FAMS pada kartu Storage Usage pada langkah 60 turun sebesar Size file `penuh-dua-{runId}.pdf` (`300.0 KB`) dibanding langkah 55, karena hanya Permanently Delete yang menurunkan pemakaian dan Delete atas `penuh-satu-{runId}.pdf` hanya memindahkan byte
63. Verifikasi Total Used pada langkah 60 sama dengan langkah 55, karena Total Used bukan angka yang dihitung atau diubah oleh File Manager, sedangkan nilai pemakaian FAMS pada kartu dihitung realtime

### Upload foto wajib transaksi diblokir di titik upload
64. Foto wajib transaksi (Handover Photo) `handover-{runId}.jpg` diunggah pada langkah Photo at start sebuah transaksi atas aset `Laptop Dell Latitude 5420 {runId}` oleh `Bagas Pratama {runId}`
65. Verifikasi upload ditolak dan langkah yang mewajibkan foto tidak dapat diselesaikan sampai Storage dibebaskan atau kuota ditambah
66. Verifikasi tidak ada file `handover-{runId}.jpg` yang menjadi record File Manager, dan penolakan berasal dari titik upload, bukan dari aksi File Manager yang tetap diterima pada langkah 57 dan 59

### Blokir upload berlaku pada Return Photo, Send Photo, dan Receive Photo
67. Foto wajib pengembalian (Return Photo) `return-{runId}.jpg` diunggah pada langkah Photo at end sebuah transaksi atas aset `Tablet Samsung Galaxy Tab S8 {runId}` oleh `Bagas Pratama {runId}`
68. Verifikasi upload `return-{runId}.jpg` ditolak dan langkah pengembalian yang mewajibkan foto tidak dapat diselesaikan
69. Foto wajib langkah Send (Send Photo) `send-{runId}.jpg` diunggah pada langkah Send sebuah transaksi pemindahan aset `Proyektor Epson EB-X49 {runId}` oleh `Bagas Pratama {runId}`
70. Verifikasi upload `send-{runId}.jpg` ditolak dan langkah Send yang mewajibkan foto tidak dapat diselesaikan
71. Foto wajib langkah Receive (Receive Photo) `receive-{runId}.jpg` diunggah pada langkah Receive sebuah transaksi pemindahan aset `Kamera Sony ZV-E10 {runId}` oleh `Bagas Pratama {runId}`
72. Verifikasi upload `receive-{runId}.jpg` ditolak dan langkah Receive yang mewajibkan foto tidak dapat diselesaikan

### Berkas dari form yang dibatalkan tidak menjadi record
73. `Bagas Pratama {runId}` membaca label tab Asset Photo dan nilai pemakaian FAMS pada kartu Storage Usage langsung ke server
74. File `batal-{runId}.jpg` diunggah ke form oleh `Bagas Pratama {runId}`
75. Form dibatalkan oleh `Bagas Pratama {runId}` sebelum tersimpan
76. `Bagas Pratama {runId}` membaca daftar tab Files dan Recycle Bin dengan kata kunci `{runId}`, label tab Asset Photo, dan nilai pemakaian FAMS pada kartu Storage Usage langsung ke server
77. Verifikasi file `batal-{runId}.jpg` tidak ada pada tab Files maupun Recycle Bin
78. Verifikasi label tab Asset Photo pada langkah 76 tidak bertambah sebesar Size file `batal-{runId}.jpg` (`500.0 KB`) dibanding langkah 73
79. Verifikasi nilai pemakaian FAMS pada kartu Storage Usage pada langkah 76 sama dengan langkah 73, karena byte `batal-{runId}.jpg` tidak dihitung ke komponen Storage mana pun

### Aset dengan file berganti Status: file tetap dihitung di tab kategori dan footprint masuk pemakaian FAMS
80. `Bagas Pratama {runId}` membaca label tab Asset Documents dan nilai pemakaian FAMS pada kartu Storage Usage langsung ke server
81. Status aset `Router Cisco ISR 4331 {runId}` diubah dari `Active` menjadi `Unmanaged`
82. `Bagas Pratama {runId}` membaca label tab Asset Documents, label tab `Disposed & Unmanaged Assets`, baris aset `Router Cisco ISR 4331 {runId}` pada tab Asset Data, dan nilai pemakaian FAMS pada kartu Storage Usage langsung ke server
83. Verifikasi baris aset `Router Cisco ISR 4331 {runId}` pada tab Asset Data memiliki Files Size `1.5 MB` dan Total Size sama dengan Data & Log Size ditambah Files Size
84. Verifikasi label tab Asset Documents pada langkah 82 sama dengan langkah 80, karena file `router-manual-{runId}.pdf` tetap dihitung sebagai file aktif pada tab kategori
85. Verifikasi label tab `Disposed & Unmanaged Assets` pada langkah 82 tidak lebih kecil daripada Total Size baris aset `Router Cisco ISR 4331 {runId}`, karena label mencakup baris itu
86. Verifikasi nilai pemakaian FAMS pada kartu Storage Usage pada langkah 82 naik sebesar Data & Log Size baris aset `Router Cisco ISR 4331 {runId}` dibanding langkah 80, karena footprint data dan log aset Unmanaged masuk sebagai komponen sendiri dan byte `router-manual-{runId}.pdf` tidak dihitung di dua komponen
87. Status aset `Router Cisco ISR 4331 {runId}` diubah kembali dari `Unmanaged` menjadi `Active`
88. `Bagas Pratama {runId}` membaca nilai pemakaian FAMS pada kartu Storage Usage langsung ke server
89. Verifikasi nilai pemakaian FAMS pada kartu Storage Usage pada langkah 88 turun sebesar Data & Log Size baris aset `Router Cisco ISR 4331 {runId}` yang terbaca pada langkah 82

### Pembacaan kartu Storage Usage bersifat idempoten dan read-only
90. `Bagas Pratama {runId}` membaca nilai pemakaian FAMS pada kartu Storage Usage, daftar entri Changelog yang dicatat atas nama `Bagas Pratama {runId}`, serta daftar tab Files dan Recycle Bin dengan kata kunci `{runId}` langsung ke server
91. `Bagas Pratama {runId}` membaca ulang hal yang sama langsung ke server tanpa aksi lain di antaranya
92. Verifikasi nilai pemakaian FAMS pada kartu Storage Usage pada langkah 91 sama dengan langkah 90
93. Verifikasi daftar entri Changelog atas nama `Bagas Pratama {runId}` pada langkah 91 sama dengan langkah 90, sehingga pembacaan kartu tidak membuat entri log
94. Verifikasi daftar tab Files dan Recycle Bin dengan kata kunci `{runId}` pada langkah 91 sama dengan langkah 90, sehingga pembacaan kartu tidak mengubah record file
