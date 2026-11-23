---
id: TC-FA-FAFM-BE-066-auto-purge-harian
title: "Auto-purge harian atas file Recycle Bin yang melewati batas purge"
layer: be-e2e
priority: High
caseType: Positive
status: ready-for-automation
owner: BE
sourceRules: ["ARS-05a", "ARS-05b", "ARS-05c", "ARS-05d", "EC-11", "F-FAFM-03.k2", "F-FAFM-03e", "F-FAFM-03f", "F-FAFM-03i", "S-24", "SYN-03a", "SYN-03b", "SYN-03c", "SYN-03d", "SYN-03f", "SYN-03g", "SYN-11d", "SYN-11f", "§9.4.1#r7", "§9.4.1#r11"]
smoke: []
dependsOn: []
trace:
  "ARS-05a": 15
  "ARS-05b": 6
  "ARS-05c": [17, 19]
  "ARS-05d": 15
  "EC-11": [6, 9]
  "F-FAFM-03.k2": [2, 6]
  "F-FAFM-03e": [6, 7]
  "F-FAFM-03f": 2
  "F-FAFM-03i": [6, 7]
  "S-24": 9
  "SYN-03a": 6
  "SYN-03b": 6
  "SYN-03c": 13
  "SYN-03d": 12
  "SYN-03f": 6
  "SYN-03g": [12, 13]
  "SYN-11d": [6, 8]
  "SYN-11f": [3, 8]
  "§9.4.1#r7": [11, 13]
  "§9.4.1#r11": [3, 8]
---

# Auto-purge harian atas file Recycle Bin yang melewati batas purge

## Prerequisites
- Aktor: Total Control `Bagas Pratama {runId}`.
- Data:
  - DU-066-1: User `Bagas Pratama {runId}`, role Total Control, cakupan seluruh group.
  - DU-066-2: Aset `Toyota Avanza {runId}`, group `Fleet`, Status `Disposed`, memiliki file aktif lain.
  - DU-066-3: Aset `Printer HP M404 {runId}`, group `Branch Bandung`, Status `Unmanaged`, memiliki file aktif lain.
  - DU-066-4: Aset `Laptop Dell Latitude 5420 {runId}`, group `Head Office`, Status `Active`.
  - DU-066-5: Aset `Monitor LG 24 {runId}`, group `Head Office`, Status `Active`.
  - DU-066-6: File `repair-{runId}.jpg`, Source `Repair Photo`, File Format JPG, aset DU-066-2, group `Fleet`, Size `880.0 KB`, berada di Recycle Bin dengan batas purge tersimpan sudah terlampaui (Auto-Purge In `0 days`).
  - DU-066-7: File `damage-{runId}.jpg`, Source `Damaged Photo`, File Format JPG, aset DU-066-3, group `Branch Bandung`, Size `900.0 KB`, berada di Recycle Bin dengan batas purge tersimpan tercapai tepat pada hari kalender UTC job berjalan (Auto-Purge In `0 days`).
  - DU-066-8: File `laptop-lama-{runId}.png`, Source `Asset Photo`, File Format PNG, aset DU-066-4, group `Head Office`, Size `1.0 MB`, berada di Recycle Bin dengan batas purge tersimpan belum tercapai (Auto-Purge In `29 days`).
  - DU-066-9: File `gagal-{runId}.jpg`, Source `Asset Photo`, File Format JPG, aset DU-066-5, group `Head Office`, Size `530.0 KB`, berada di Recycle Bin dengan batas purge tersimpan sudah terlampaui (Auto-Purge In `0 days`).
- Kondisi:
  - Retensi Recycle Bin bernilai `30 hari`.
  - Penyimpanan file `gagal-{runId}.jpg` tidak terjangkau sejak sebelum langkah 5 sampai sebelum langkah 18, lalu pulih; penyimpanan file lain terjangkau.

## Test Steps

### Sebelum job: file yang batas purge-nya sudah lewat masih tampil
1. `Bagas Pratama {runId}` membaca daftar Recycle Bin dengan kata kunci `{runId}` langsung ke server
2. Verifikasi file `repair-{runId}.jpg` dan `damage-{runId}.jpg` masih tampil dengan Auto-Purge In `0 days` sampai job berikutnya berjalan
3. Verifikasi file `laptop-lama-{runId}.png` tampil dengan Auto-Purge In `29 days`
4. `Bagas Pratama {runId}` membaca Files Size aset `Toyota Avanza {runId}` dan aset `Printer HP M404 {runId}` pada tab Asset Data serta nilai `Fixed Asset` pada kartu Storage Usage sebagai pembacaan awal

### Job harian menghapus file yang batas purge-nya tercapai atau terlampaui
5. Job auto-purge harian berjalan
6. Verifikasi file `repair-{runId}.jpg` yang batas purge-nya terlampaui terhapus permanen dan tidak lagi ada di Recycle Bin
7. Verifikasi file `damage-{runId}.jpg` yang batas purge-nya tercapai tepat pada hari kalender UTC job berjalan ikut terhapus permanen, karena batas purge inklusif
8. Verifikasi file `laptop-lama-{runId}.png` yang batas purge-nya belum tercapai tetap berada di Recycle Bin
9. Verifikasi ada satu entri Changelog untuk File Name `repair-{runId}.jpg` dan satu untuk File Name `damage-{runId}.jpg` dengan jalur auto-purge dan aktor `System`, tanpa tindakan pengguna

### Angka storage dibaca realtime sesudah job
10. `Bagas Pratama {runId}` membaca Files Size aset `Toyota Avanza {runId}` dan aset `Printer HP M404 {runId}` pada tab Asset Data serta nilai `Fixed Asset` pada kartu Storage Usage
11. Verifikasi pembacaan pada langkah 10 mencerminkan hasil job tanpa menunggu job lain
12. Verifikasi Files Size aset `Toyota Avanza {runId}` turun sebesar Size file `repair-{runId}.jpg` (`880.0 KB`) dan Files Size aset `Printer HP M404 {runId}` turun sebesar Size file `damage-{runId}.jpg` (`900.0 KB`) dibanding pembacaan awal pada langkah 4
13. Verifikasi nilai `Fixed Asset` pada kartu Storage Usage turun dibanding pembacaan awal pada langkah 4

### Job berulang tidak menambah efek
14. Job auto-purge harian berjalan lagi
15. Verifikasi entri Changelog untuk File Name `repair-{runId}.jpg` dan `damage-{runId}.jpg` tetap satu per file, dan file `laptop-lama-{runId}.png` tetap berada di Recycle Bin

### Kegagalan penyimpanan: retry pada jadwal berikutnya
16. Job auto-purge harian berjalan lagi sementara penyimpanan file `gagal-{runId}.jpg` belum terjangkau
17. Verifikasi file `gagal-{runId}.jpg` tetap berada di Recycle Bin dan tidak ada entri Changelog untuk File Name `gagal-{runId}.jpg`
18. Job auto-purge harian berjalan pada jadwal berikutnya setelah penyimpanan pulih
19. Verifikasi file `gagal-{runId}.jpg` terhapus permanen dan ada satu entri Changelog untuk File Name `gagal-{runId}.jpg`
