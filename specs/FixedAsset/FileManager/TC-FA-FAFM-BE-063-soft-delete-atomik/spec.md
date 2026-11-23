---
id: TC-FA-FAFM-BE-063-soft-delete-atomik
title: "Soft-delete atomik: Recycle Bin, pengosongan rujukan, dan guard klik ganda"
layer: be-e2e
priority: High
caseType: Positive
status: ready-for-automation
owner: BE
sourceRules: ["ARS-01a", "ARS-01i", "ARS-01k", "EC-10", "F-FAFM-02.k2", "F-FAFM-02.k4", "F-FAFM-02g", "F-FAFM-02j", "FAFM-LOGIC-01d", "FAFM-LOGIC-02d", "EB-EDG-3"]
smoke: []
dependsOn: []
trace:
  "ARS-01a": 14
  "ARS-01i": 12
  "ARS-01k": [3, 9]
  "EC-10": 11
  "F-FAFM-02.k2": [2, 8]
  "F-FAFM-02.k4": 11
  "F-FAFM-02g": [3, 4, 9]
  "F-FAFM-02j": 11
  "FAFM-LOGIC-01d": 5
  "FAFM-LOGIC-02d": [3, 6]
  "EB-EDG-3": [3, 4]
---

# Soft-delete atomik: Recycle Bin, pengosongan rujukan, dan guard klik ganda

## Prerequisites
- Aktor: Total Control `Bagas Pratama {runId}`.
- Data:
  - DU-063-1: User `Bagas Pratama {runId}`, role Total Control, cakupan seluruh group.
  - DU-063-2: Aset `Laptop Dell Latitude 5420 {runId}`, group `Head Office`, Status `Active`, Photo merujuk DU-063-6, field custom Document `Warranty Card` merujuk DU-063-7.
  - DU-063-3: Aset `Scanner Epson DS-530 {runId}`, group `Branch Bandung`, Status `Active`, Photo merujuk DU-063-8.
  - DU-063-4: Aset `Printer HP M404 {runId}`, group `Head Office`, Status `Active`, dokumen Attachment kelompok General merujuk DU-063-9.
  - DU-063-5: Aset `Monitor LG 24 {runId}`, group `Head Office`, Status `Active`, Photo merujuk DU-063-10.
  - DU-063-6: File `foto-laptop-{runId}.jpg`, Source `Asset Photo`, File Format JPG, aset DU-063-2, group `Head Office`, Size `820.4 KB`, aktif.
  - DU-063-7: File `warranty-card-lpt-{runId}.pdf`, Source `Custom Field Document`, Reference `Warranty Card`, File Format PDF, aset DU-063-2, group `Head Office`, Size `300.0 KB`, aktif.
  - DU-063-8: File `foto-scanner-{runId}.jpg`, Source `Asset Photo`, File Format JPG, aset DU-063-3, group `Branch Bandung`, Size `640.0 KB`, aktif.
  - DU-063-9: File `manual-printer-{runId}.pdf`, Source `Attachment`, Reference `General`, File Format PDF, aset DU-063-4, group `Head Office`, Size `310.0 KB`, aktif.
  - DU-063-10: File `foto-monitor-{runId}.jpg`, Source `Asset Photo`, File Format JPG, aset DU-063-5, group `Head Office`, Size `750.0 KB`, aktif.

## Test Steps

### Delete file yang dirujuk tidak diblokir dan rujukan dikosongkan atomik
1. `Bagas Pratama {runId}` mengirim permintaan Delete atas file `foto-laptop-{runId}.jpg` langsung ke server
2. Verifikasi permintaan diterima dan tidak diblokir walau file `foto-laptop-{runId}.jpg` masih dirujuk Photo aset `Laptop Dell Latitude 5420 {runId}`
3. Verifikasi pada pembacaan sesudahnya file `foto-laptop-{runId}.jpg` berada di Recycle Bin dan Photo aset `Laptop Dell Latitude 5420 {runId}` sudah kosong, tanpa keadaan setengah jadi
4. Verifikasi Status aset `Laptop Dell Latitude 5420 {runId}` tetap `Active`
5. Verifikasi field custom Document `Warranty Card` aset `Laptop Dell Latitude 5420 {runId}` tetap merujuk file `warranty-card-lpt-{runId}.pdf`, karena hanya rujukan file yang di-Delete yang dikosongkan
6. Verifikasi Photo aset `Laptop Dell Latitude 5420 {runId}` sudah kosong pada pembacaan record sumber pertama sesudah Delete, tanpa menunggu tindakan modul sumber atas event penyegaran

### Bulk Delete atas Source campuran diproses seragam
7. `Bagas Pratama {runId}` mengirim permintaan Delete bulk atas file `warranty-card-lpt-{runId}.pdf`, `foto-scanner-{runId}.jpg`, dan `manual-printer-{runId}.pdf` langsung ke server
8. Verifikasi ketiga file berada di Recycle Bin dan tidak ada item yang dilewati karena Source-nya berbeda
9. Verifikasi field custom Document `Warranty Card` aset `Laptop Dell Latitude 5420 {runId}` sudah kosong, Photo aset `Scanner Epson DS-530 {runId}` sudah kosong, dan file `manual-printer-{runId}.pdf` tidak lagi menjadi rujukan aset `Printer HP M404 {runId}`

### Konfirmasi ganda tidak diproses dua kali
10. `Bagas Pratama {runId}` mengirim dua permintaan Delete atas file `foto-monitor-{runId}.jpg` serentak
11. Verifikasi file `foto-monitor-{runId}.jpg` berada di Recycle Bin tepat satu kali dan hanya ada satu entri Changelog `Delete` untuk File Name `foto-monitor-{runId}.jpg`
12. Verifikasi hasil akhir sama untuk urutan tiba permintaan mana pun: file `foto-monitor-{runId}.jpg` berada di Recycle Bin dan Photo aset `Monitor LG 24 {runId}` kosong, tanpa keadaan setengah jadi

### Delete berulang atas file yang sudah di Recycle Bin tidak menambah efek
13. `Bagas Pratama {runId}` mengirim ulang permintaan Delete atas file `foto-monitor-{runId}.jpg` yang sudah berada di Recycle Bin
14. Verifikasi file `foto-monitor-{runId}.jpg` tetap berada di Recycle Bin dan entri Changelog `Delete` untuk File Name `foto-monitor-{runId}.jpg` tetap satu
