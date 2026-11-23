---
id: TC-FA-FAFM-BE-065-permanently-delete-sisi-server
title: "Permanently Delete: hard-delete record dan file fisik, race, dan fail-closed"
layer: be-e2e
priority: High
caseType: Positive
status: ready-for-automation
owner: BE
sourceRules: ["ARS-02a", "ARS-02b", "ARS-02e", "ARS-02f", "ARS-02g", "ARS-02h", "ARS-02i", "F-FAFM-03.k1", "FAFM-LOGIC-03a", "§9.4.1#r12"]
smoke: []
dependsOn: []
trace:
  "ARS-02a": 7
  "ARS-02b": [2, 4]
  "ARS-02e": [11, 18]
  "ARS-02f": [9, 12, 14, 27]
  "ARS-02g": [24, 27]
  "ARS-02h": 21
  "ARS-02i": 22
  "F-FAFM-03.k1": [6, 9, 14]
  "FAFM-LOGIC-03a": [16, 18, 19]
  "§9.4.1#r12": [24, 25, 29]
---

# Permanently Delete: hard-delete record dan file fisik, race, dan fail-closed

## Prerequisites
- Aktor: Total Control `Bagas Pratama {runId}`.
- Data:
  - DU-065-1: User `Bagas Pratama {runId}`, role Total Control, cakupan seluruh group.
  - DU-065-2: File `laptop-lama-{runId}.png`, Source `Asset Photo`, File Format PNG, aset `Laptop Dell Latitude 5420 {runId}`, group `Head Office`, Size `1.0 MB`, sudah berada di Recycle Bin dan masih dalam masa retensi.
  - DU-065-3: File `printer-lama-{runId}.png`, Source `Asset Photo`, File Format PNG, aset `Printer HP M404 {runId}`, group `Head Office`, Size `900.0 KB`, sudah berada di Recycle Bin dan masih dalam masa retensi.
  - DU-065-4: File `scanner-lama-{runId}.png`, Source `Asset Photo`, File Format PNG, aset `Scanner Epson DS-530 {runId}`, group `Branch Bandung`, Size `640.0 KB`, sudah berada di Recycle Bin dan masih dalam masa retensi.
  - DU-065-5: File `monitor-lama-{runId}.png`, Source `Asset Photo`, File Format PNG, aset `Monitor LG 24 {runId}`, group `Branch Bandung`, Size `750.0 KB`, sudah berada di Recycle Bin dan masih dalam masa retensi.
  - DU-065-6: File `proyektor-lama-{runId}.png`, Source `Asset Photo`, File Format PNG, aset `Projector Epson EB-X06 {runId}`, group `Branch Bandung`, Size `820.4 KB`, sudah berada di Recycle Bin dan masih dalam masa retensi.
  - DU-065-7: File `tablet-lama-{runId}.png`, Source `Asset Photo`, File Format PNG, aset `Tablet Samsung Galaxy Tab {runId}`, group `Branch Bandung`, Size `700.0 KB`, sudah berada di Recycle Bin dan masih dalam masa retensi.
  - DU-065-8: File `kamera-lama-{runId}.png`, Source `Asset Photo`, File Format PNG, aset `Camera Canon EOS 90D {runId}`, group `Head Office`, Size `1.2 MB`, sudah berada di Recycle Bin dan masih dalam masa retensi.
  - DU-065-9: File `race-satu-{runId}.png`, Source `Asset Photo`, File Format PNG, aset `Laptop Dell Latitude 5420 {runId}`, group `Head Office`, Size `510.0 KB`, sudah berada di Recycle Bin dan masih dalam masa retensi.
  - DU-065-10: File `race-dua-{runId}.png`, Source `Asset Photo`, File Format PNG, aset `Printer HP M404 {runId}`, group `Head Office`, Size `520.0 KB`, sudah berada di Recycle Bin dan masih dalam masa retensi.
  - DU-065-11: File `gagal-satu-{runId}.png`, Source `Asset Photo`, File Format PNG, aset `Monitor LG 24 {runId}`, group `Head Office`, Size `530.0 KB`, sudah berada di Recycle Bin dan masih dalam masa retensi.
  - DU-065-12: File `gagal-dua-{runId}.png`, Source `Asset Photo`, File Format PNG, aset `Scanner Epson DS-530 {runId}`, group `Head Office`, Size `540.0 KB`, sudah berada di Recycle Bin dan masih dalam masa retensi.
- Kondisi:
  - Selection Limit bernilai `1000`.
  - Pada kelompok «Fail-closed saat penyimpanan file tidak terjangkau», penyimpanan file tidak terjangkau; pada kelompok lain penyimpanan file terjangkau.

## Test Steps

### Permanently Delete single menghapus record dan file fisik
1. `Bagas Pratama {runId}` mengirim permintaan Permanently Delete atas file `laptop-lama-{runId}.png` langsung ke server
2. Verifikasi permintaan diterima dan file `laptop-lama-{runId}.png` tidak lagi ada di Recycle Bin
3. `Bagas Pratama {runId}` meminta Download file `laptop-lama-{runId}.png` langsung ke server
4. Verifikasi respons tidak ditemukan karena file fisik `laptop-lama-{runId}.png` ikut terhapus

### Permanently Delete berulang atas file yang sudah terhapus
5. `Bagas Pratama {runId}` mengirim ulang permintaan Permanently Delete atas file `laptop-lama-{runId}.png` langsung ke server
6. Verifikasi permintaan diperlakukan sebagai file tidak tersedia, tanpa mutasi
7. Verifikasi entri Changelog `Permanently Delete` untuk File Name `laptop-lama-{runId}.png` tetap satu

### Permanently Delete bulk campuran
8. `Bagas Pratama {runId}` mengirim permintaan Permanently Delete bulk atas file `printer-lama-{runId}.png`, `scanner-lama-{runId}.png`, dan `laptop-lama-{runId}.png` langsung ke server
9. Verifikasi hasil per item: `printer-lama-{runId}.png` dan `scanner-lama-{runId}.png` dihapus, `laptop-lama-{runId}.png` dilewati karena sudah tidak tersedia
10. `Bagas Pratama {runId}` membaca daftar Recycle Bin dengan kata kunci `{runId}`
11. Verifikasi daftar tidak lagi memuat file `printer-lama-{runId}.png` dan `scanner-lama-{runId}.png`, di-commit per item walau satu item dilewati
12. Verifikasi ada satu entri Changelog `Permanently Delete` untuk File Name `printer-lama-{runId}.png` dan satu untuk File Name `scanner-lama-{runId}.png`, dan tidak ada entri baru untuk `laptop-lama-{runId}.png`

### Permanently Delete bulk atas item yang seluruhnya tidak tersedia
13. `Bagas Pratama {runId}` mengirim permintaan Permanently Delete bulk atas file `laptop-lama-{runId}.png` dan `printer-lama-{runId}.png` langsung ke server
14. Verifikasi hasil per item: kedua item dilewati, tidak ada yang dihapus dan tidak ada entri Changelog baru

### Select All mengosongkan hasil saringan dan jalur keluar Recycle Bin
15. `Bagas Pratama {runId}` meminta Download file `kamera-lama-{runId}.png` langsung ke server
16. Verifikasi file `kamera-lama-{runId}.png` dikirim sebagai stream dan tetap berada di Recycle Bin, karena Download tidak mengeluarkan file dari Recycle Bin
17. `Bagas Pratama {runId}` mengirim permintaan Permanently Delete bulk atas seluruh hasil saringan Recycle Bin dengan kata kunci `{runId}` dan group `Branch Bandung` (Select All) langsung ke server
18. Verifikasi file `monitor-lama-{runId}.png`, `proyektor-lama-{runId}.png`, dan `tablet-lama-{runId}.png` terhapus permanen, sehingga hasil saringan itu kosong
19. Verifikasi file `kamera-lama-{runId}.png` tetap berada di Recycle Bin karena di luar saringan Select All

### Permintaan serentak atas file yang sama
20. `Bagas Pratama {runId}` mengirim serentak permintaan Permanently Delete atas file `race-satu-{runId}.png` dan permintaan Permanently Delete bulk atas file `race-satu-{runId}.png` dan `race-dua-{runId}.png`
21. Verifikasi file `race-satu-{runId}.png` dan `race-dua-{runId}.png` terhapus permanen, masing-masing dengan tepat satu entri Changelog `Permanently Delete`
22. Verifikasi file `race-satu-{runId}.png` tidak ada di Recycle Bin dan tidak bisa diunduh, tanpa keadaan setengah jadi antara record dan file fisik

### Fail-closed saat penyimpanan file tidak terjangkau
23. `Bagas Pratama {runId}` mengirim permintaan Permanently Delete atas file `gagal-satu-{runId}.png` langsung ke server
24. Verifikasi permintaan gagal dan file `gagal-satu-{runId}.png` tetap berada di Recycle Bin, karena record tidak dihapus bila file fisik tidak bisa dihapus
25. Verifikasi tidak ada entri Changelog `Permanently Delete` untuk File Name `gagal-satu-{runId}.png`
26. `Bagas Pratama {runId}` mengirim permintaan Permanently Delete bulk atas file `gagal-satu-{runId}.png` dan `gagal-dua-{runId}.png` langsung ke server
27. Verifikasi hasil per item: `gagal-satu-{runId}.png` dan `gagal-dua-{runId}.png` gagal, dan tidak ada yang dihapus
28. `Bagas Pratama {runId}` meminta Download file `gagal-satu-{runId}.png` langsung ke server
29. Verifikasi Download gagal dan tidak ada isi file yang dikirim
