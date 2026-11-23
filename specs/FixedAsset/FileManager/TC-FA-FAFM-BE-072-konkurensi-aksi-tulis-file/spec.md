---
id: TC-FA-FAFM-BE-072-konkurensi-aksi-tulis-file
title: "Konkurensi aksi tulis atas file yang sama dan aksi atas file yang sudah selesai"
layer: be-e2e
priority: Medium
caseType: Edge
status: ready-for-automation
owner: BE
sourceRules: ["EC-04", "F-FAFM-02h", "§9.4.1#r6", "EB-ERR-3", "EB-CON-3", "EB-EDG-1"]
smoke: []
dependsOn: []
trace:
  "EC-04": [6, 7, 8, 9, 29, 30, 31, 34]
  "F-FAFM-02h": [25, 26]
  "§9.4.1#r6": [4, 8, 12, 16]
  "EB-ERR-3": [13, 19]
  "EB-CON-3": [2, 3, 11, 12, 15, 16]
  "EB-EDG-1": [21, 23]
---

# Konkurensi aksi tulis atas file yang sama dan aksi atas file yang sudah selesai

## Prerequisites
- Aktor: Total Control `Bagas Pratama {runId}` dan Group Manager `Hendra Gunawan {runId}`.
- Data:
  - DU-072-1: User `Bagas Pratama {runId}`, role Total Control, cakupan seluruh group.
  - DU-072-2: User `Hendra Gunawan {runId}`, role Group Manager atas group `Head Office` beserta descendant.
  - DU-072-3: Aset `Laptop Dell Latitude 5420 {runId}`, group `Head Office`, Status `Active`, Photo merujuk DU-072-8.
  - DU-072-4: Aset `Monitor LG 24 {runId}`, group `Head Office`, Status `Active`, Photo merujuk DU-072-9.
  - DU-072-5: Aset `Printer HP M404 {runId}`, group `Head Office`, Status `Active`, tanpa rujukan file aktif.
  - DU-072-6: Aset `Tablet Samsung Galaxy Tab {runId}`, group `Head Office`, Status `Active`, Photo kosong karena rujukannya sudah dikosongkan proses lain.
  - DU-072-7: Aset `Scanner Epson DS-530 {runId}`, group `Head Office`, Status `Active`, tanpa rujukan file aktif.
  - DU-072-8: File `balap-delete-{runId}.jpg`, Source `Asset Photo`, File Format JPG, aset DU-072-3, group `Head Office`, Size `820.4 KB`, aktif.
  - DU-072-9: File `balap-transisi-lama-{runId}.jpg`, Source `Asset Photo`, File Format JPG, aset DU-072-4, group `Head Office`, Size `750.0 KB`, aktif.
  - DU-072-10: File `balap-transisi-baru-{runId}.jpg`, Source `Asset Photo`, File Format JPG, aset DU-072-4, group `Head Office`, Size `600.0 KB`, unggahan pengganti, belum ada sebelum langkah 5.
  - DU-072-11: File `balap-permanen-{runId}.png`, Source `Asset Photo`, File Format PNG, aset DU-072-5, group `Head Office`, Size `900.0 KB`, berada di Recycle Bin dan masih dalam masa retensi.
  - DU-072-12: File `balap-purge-{runId}.png`, Source `Asset Photo`, File Format PNG, aset DU-072-7, group `Head Office`, Size `640.0 KB`, berada di Recycle Bin dengan batas purge tersimpan sudah terlampaui (Auto-Purge In `0 days`).
  - DU-072-13: File `sudah-hilang-{runId}.png`, Source `Asset Photo`, File Format PNG, aset DU-072-5, group `Head Office`, Size `510.0 KB`, berada di Recycle Bin dan masih dalam masa retensi.
  - DU-072-14: File `sudah-selesai-{runId}.jpg`, Source `Asset Photo`, File Format JPG, aset DU-072-7, group `Head Office`, Size `520.0 KB`, sudah berada di Recycle Bin dan masih dalam masa retensi.
  - DU-072-15: File `rujukan-kosong-{runId}.jpg`, Source `Asset Photo`, File Format JPG, aset DU-072-6, group `Head Office`, Size `450.2 KB`, aktif.
  - DU-072-16: Aset `Webcam Logitech C920 {runId}`, group `Head Office`, Status `Active`, Photo merujuk DU-072-17.
  - DU-072-17: File `balap-kalah-lama-{runId}.jpg`, Source `Asset Photo`, File Format JPG, aset DU-072-16, group `Head Office`, Size `700.0 KB`, aktif.
  - DU-072-18: File `balap-kalah-baru-{runId}.jpg`, Source `Asset Photo`, File Format JPG, aset DU-072-16, group `Head Office`, Size `650.0 KB`, unggahan pengganti yang tidak pernah tersimpan sebagai Photo.
- Kondisi:
  - Retensi Recycle Bin bernilai `30 hari`.

## Test Steps

### Delete dan Delete serentak atas file yang sama
1. `Bagas Pratama {runId}` dan `Hendra Gunawan {runId}` mengirim serentak permintaan Delete atas file `balap-delete-{runId}.jpg` langsung ke server
2. Verifikasi file `balap-delete-{runId}.jpg` berada di Recycle Bin tepat satu kali
3. Verifikasi ada tepat satu entri Changelog Delete untuk File Name `balap-delete-{runId}.jpg`
4. Verifikasi hasil akhir sama untuk urutan tiba mana pun: file berada di Recycle Bin dan Photo aset `Laptop Dell Latitude 5420 {runId}` kosong bersamaan, tanpa keadaan setengah jadi

### Delete dan auto-transition serentak atas file yang sama
5. `Bagas Pratama {runId}` mengirim permintaan Delete atas file `balap-transisi-lama-{runId}.jpg` langsung ke server, serentak dengan penyimpanan record aset `Monitor LG 24 {runId}` dengan Photo diganti ke file baru `balap-transisi-baru-{runId}.jpg`
6. Verifikasi file `balap-transisi-lama-{runId}.jpg` berada di Recycle Bin tepat satu kali
7. Verifikasi ada tepat satu entri Changelog soft-delete untuk File Name `balap-transisi-lama-{runId}.jpg`, dengan aktor `Bagas Pratama {runId}` atau `System` sesuai transaksi yang commit lebih dulu
8. Verifikasi Photo aset `Monitor LG 24 {runId}` tidak pernah merujuk file `balap-transisi-lama-{runId}.jpg` yang berada di Recycle Bin
9. Verifikasi transaksi yang commit belakangan tidak menambah entri soft-delete kedua dan tidak mengembalikan file `balap-transisi-lama-{runId}.jpg` ke aktif

### Permanently Delete dan Permanently Delete serentak atas file yang sama
10. `Bagas Pratama {runId}` dan `Hendra Gunawan {runId}` mengirim serentak permintaan Permanently Delete atas file `balap-permanen-{runId}.png` langsung ke server
11. Verifikasi file `balap-permanen-{runId}.png` terhapus permanen dan tidak lagi ada di Recycle Bin
12. Verifikasi ada tepat satu entri Changelog Permanently Delete untuk File Name `balap-permanen-{runId}.png`
13. Verifikasi permintaan yang tidak commit lebih dulu diperlakukan sebagai file tidak ditemukan tanpa mutasi

### Permanently Delete dan auto-purge serentak atas file yang sama
14. `Bagas Pratama {runId}` mengirim permintaan Permanently Delete atas file `balap-purge-{runId}.png` langsung ke server, serentak dengan job auto-purge harian berjalan
15. Verifikasi file `balap-purge-{runId}.png` terhapus permanen tepat satu kali dan tidak lagi ada di Recycle Bin
16. Verifikasi ada tepat satu entri Changelog hapus permanen untuk File Name `balap-purge-{runId}.png`, dengan aktor `Bagas Pratama {runId}` atau `System`, tidak keduanya

### Aksi atas file yang sudah dihapus oleh pihak lain
17. `Hendra Gunawan {runId}` mengirim permintaan Permanently Delete atas file `sudah-hilang-{runId}.png` langsung ke server
18. `Bagas Pratama {runId}` mengirim permintaan Permanently Delete atas file `sudah-hilang-{runId}.png` langsung ke server, berdasarkan daftar yang dibacanya sebelum langkah 17
19. Verifikasi permintaan pada langkah 18 diperlakukan sebagai file tidak ditemukan tanpa mutasi
20. `Bagas Pratama {runId}` mengirim permintaan Delete atas file `sudah-hilang-{runId}.png` langsung ke server
21. Verifikasi permintaan pada langkah 20 diperlakukan sebagai file tidak ditemukan, tanpa mutasi dan tanpa entri Changelog baru untuk File Name `sudah-hilang-{runId}.png`
22. `Bagas Pratama {runId}` mengirim permintaan Delete atas file `sudah-selesai-{runId}.jpg` yang sudah berada di Recycle Bin langsung ke server
23. Verifikasi file `sudah-selesai-{runId}.jpg` tetap berada di Recycle Bin dan tidak ada entri Changelog Delete baru untuk File Name `sudah-selesai-{runId}.jpg`

### File yang rujukannya sudah dikosongkan proses lain
24. `Bagas Pratama {runId}` mengirim permintaan Delete atas file `rujukan-kosong-{runId}.jpg` langsung ke server
25. Verifikasi file `rujukan-kosong-{runId}.jpg` hanya di-soft-delete: berada di Recycle Bin dan belum terhapus permanen
26. Verifikasi Photo aset `Tablet Samsung Galaxy Tab {runId}` tetap kosong

### Penyimpanan record dengan rujukan ke file yang sudah di-soft-delete atau dihapus permanen
27. `Bagas Pratama {runId}` mengirim permintaan Delete atas file `balap-kalah-lama-{runId}.jpg` langsung ke server
28. `Bagas Pratama {runId}` mengirim penyimpanan record aset `Webcam Logitech C920 {runId}` dengan Photo diganti ke file `balap-kalah-baru-{runId}.jpg` langsung ke server, berdasarkan record yang dibacanya sebelum langkah 27 dan masih merujuk file `balap-kalah-lama-{runId}.jpg`
29. Verifikasi penyimpanan pada langkah 28 ditolak dengan umpan balik netral tanpa mutasi
30. Verifikasi file `balap-kalah-lama-{runId}.jpg` berada di Recycle Bin tepat satu kali dan hanya ada satu entri Changelog soft-delete untuk File Name `balap-kalah-lama-{runId}.jpg`
31. Verifikasi Photo aset `Webcam Logitech C920 {runId}` tidak merujuk file `balap-kalah-lama-{runId}.jpg` maupun file `balap-kalah-baru-{runId}.jpg`
32. `Bagas Pratama {runId}` mengirim permintaan Permanently Delete atas file `balap-kalah-lama-{runId}.jpg` langsung ke server
33. `Bagas Pratama {runId}` mengirim penyimpanan record aset `Webcam Logitech C920 {runId}` dengan Photo diganti ke file `balap-kalah-baru-{runId}.jpg` langsung ke server, berdasarkan record yang sama seperti langkah 28
34. Verifikasi penyimpanan pada langkah 33 ditolak dengan umpan balik netral tanpa mutasi dan rujukan Photo tidak pernah dikembalikan ke file `balap-kalah-lama-{runId}.jpg`
