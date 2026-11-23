---
id: TC-FA-FAFM-BE-064-bulk-delete-hasil-per-item
title: "Bulk Delete: hasil per item dan commit per item"
layer: be-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
owner: BE
sourceRules: ["ARS-01g", "ARS-01h", "§7#p2"]
smoke: []
dependsOn: []
trace:
  "ARS-01g": [4, 8]
  "ARS-01h": [3, 5, 10]
  "§7#p2": [3, 6, 10, 11]
---

# Bulk Delete: hasil per item dan commit per item

## Prerequisites
- Aktor: Total Control `Bagas Pratama {runId}` dan Group Manager `Hendra Gunawan {runId}`.
- Data:
  - DU-064-1: User `Bagas Pratama {runId}`, role Total Control, cakupan seluruh group.
  - DU-064-2: User `Hendra Gunawan {runId}`, role Group Manager atas group `Head Office` beserta descendant.
  - DU-064-3: File `foto-printer-{runId}.jpg`, Source `Asset Photo`, File Format JPG, aset `Printer HP M404 {runId}`, group `Head Office`, Size `820.4 KB`, aktif.
  - DU-064-4: File `foto-monitor-{runId}.jpg`, Source `Asset Photo`, File Format JPG, aset `Monitor LG 24 {runId}`, group `Head Office`, Size `750.0 KB`, aktif.
  - DU-064-5: File `foto-proyektor-{runId}.jpg`, Source `Asset Photo`, File Format JPG, aset `Projector Epson EB-X06 {runId}`, group `Branch Bandung`, Size `640.0 KB`, aktif.
  - DU-064-6: File `printer-lama-{runId}.png`, Source `Asset Photo`, File Format PNG, aset `Printer HP M404 {runId}`, group `Head Office`, Size `1.0 MB`, sudah berada di Recycle Bin dan masih dalam masa retensi.
  - DU-064-7: File `monitor-lama-{runId}.png`, Source `Asset Photo`, File Format PNG, aset `Monitor LG 24 {runId}`, group `Head Office`, Size `900.0 KB`, sudah berada di Recycle Bin dan masih dalam masa retensi.
  - DU-064-8: File `foto-scanner-{runId}.jpg`, Source `Asset Photo`, File Format JPG, aset `Scanner Epson DS-530 {runId}`, group `Branch Bandung`, Size `700.0 KB`, aktif.
  - DU-064-9: File `laptop-lama-{runId}.png`, Source `Asset Photo`, File Format PNG, aset `Laptop Dell Latitude 5420 {runId}`, group `Head Office`, Size `1.2 MB`, sudah berada di Recycle Bin dan masih dalam masa retensi.

## Test Steps

### Bulk Delete campuran: item tersedia dihapus, sisanya dilewati
1. `Bagas Pratama {runId}` mengirim permintaan Permanently Delete atas file `monitor-lama-{runId}.png` langsung ke server
2. `Hendra Gunawan {runId}` mengirim permintaan Delete bulk atas file `foto-printer-{runId}.jpg`, `foto-monitor-{runId}.jpg`, `foto-proyektor-{runId}.jpg`, `printer-lama-{runId}.png`, dan `monitor-lama-{runId}.png` langsung ke server
3. Verifikasi hasil per item: `foto-printer-{runId}.jpg` dan `foto-monitor-{runId}.jpg` dihapus, sedangkan `foto-proyektor-{runId}.jpg` dan `monitor-lama-{runId}.png` dilewati
4. Verifikasi `foto-printer-{runId}.jpg` dan `foto-monitor-{runId}.jpg` sudah berada di Recycle Bin, di-commit per item walau item lain dilewati
5. Verifikasi `foto-proyektor-{runId}.jpg` tetap aktif, `printer-lama-{runId}.png` tetap berada di Recycle Bin, dan `monitor-lama-{runId}.png` tidak tersedia, tanpa perubahan akibat permintaan bulk itu
6. Verifikasi ada satu entri Changelog `Delete` untuk File Name `foto-printer-{runId}.jpg` dan satu untuk File Name `foto-monitor-{runId}.jpg`, dan tidak ada entri Changelog `Delete` baru untuk `foto-proyektor-{runId}.jpg`, `printer-lama-{runId}.png`, maupun `monitor-lama-{runId}.png`
7. `Hendra Gunawan {runId}` membaca daftar file tab Asset Photo dengan kata kunci `{runId}`
8. Verifikasi daftar tidak lagi memuat file `foto-printer-{runId}.jpg` dan `foto-monitor-{runId}.jpg`

### Bulk Delete: item di luar scope dilewati dan file yang sudah di Recycle Bin tidak berubah
9. `Hendra Gunawan {runId}` mengirim permintaan Delete bulk atas file `foto-scanner-{runId}.jpg` dan `laptop-lama-{runId}.png` langsung ke server
10. Verifikasi hasil per item: `foto-scanner-{runId}.jpg` dilewati karena di luar scope `Hendra Gunawan {runId}`
11. Verifikasi `foto-scanner-{runId}.jpg` tetap aktif, `laptop-lama-{runId}.png` tetap berada di Recycle Bin, dan tidak ada entri Changelog `Delete` baru untuk keduanya
