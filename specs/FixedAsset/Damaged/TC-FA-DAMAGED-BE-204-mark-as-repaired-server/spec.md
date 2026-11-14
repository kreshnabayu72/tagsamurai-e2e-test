---
id: TC-FA-DAMAGED-BE-204-mark-as-repaired-server
title: "Server memvalidasi Mark as Repaired: Scan TAG milik aset untuk aset ber-TAG, After photo menurut setting, Repair note, identifikasi manual, status record Repaired dengan penghapusan penanda secara atomik, dan penolakan pada status Disposal"
layer: be-e2e
priority: Critical
caseType: Positive
status: ready-for-automation
sourceRules: ["§Aturan Logika Modul#r57", "§Aturan Logika Modul#r58", "§Aturan Logika Modul#r88", "§9.2#r5", "§9.2#b16", "§9.2#b17", "§9.6#r5", "§9.9#r3", "§9.9#r4", "§9.9#r5", "V-DMG-03", "V-DMG-04", "V-DMG-05", "FI-DMG-08", "FI-DMG-11", "FI-DMG-12", "S-DMG-07", "§9.4.2#r13", "§9.4.2#r27", "§9.4.4#r22", "§9.4.4#r24", "§9.4.4#r25", "§9.4.4#r9", "§9.4.1#r12", "EB-FRM-4@repair-note", "§3#p6", "§9.1#r5"]
smoke: []
dependsOn: []
owner: BE
trace:
  "§Aturan Logika Modul#r57": [2, 18]
  "§Aturan Logika Modul#r58": 2
  "§Aturan Logika Modul#r88": 21
  "§9.2#r5": 2
  "§9.2#b16": 30
  "§9.2#b17": [3, 23, 25]
  "§9.6#r5": [3, 4, 5]
  "§9.9#r3": [7, 9]
  "§9.9#r4": 20
  "§9.9#r5": [12, 14]
  "V-DMG-03": 9
  "V-DMG-04": 7
  "V-DMG-05": [32, 34]
  "FI-DMG-08": 7
  "FI-DMG-11": 20
  "FI-DMG-12": 20
  "S-DMG-07": 20
  "§9.4.2#r13": 30
  "§9.4.2#r27": [27, 28]
  "§9.4.4#r22": 30
  "§9.4.4#r24": 10
  "§9.4.4#r25": [32, 35, 36]
  "§9.4.4#r9": 28
  "§9.4.1#r12": 30
  "EB-FRM-4@repair-note": [14, 16]
  "§3#p6": 2
  "§9.1#r5": 2
---

# Server memvalidasi Mark as Repaired: Scan TAG milik aset untuk aset ber-TAG, After photo menurut setting, Repair note, identifikasi manual, status record Repaired dengan penghapusan penanda secara atomik, dan penolakan pada status Disposal

## Prerequisites
- Aktor:
  - Total Control `Agus Pratama {runId}`, Aktor Damaged.
  - Pemegang Manage asset & TAG (Update) `Rina Wulandari {runId}`, Aktor Damaged pada Group `Head Office {runId}`, juga pelapor admin.
- Data:
  - DU-204-1: User `Agus Pratama {runId}`, Total Control, cakupan seluruh client.
  - DU-204-2: User `Rina Wulandari {runId}`, Manage asset & TAG (Update), cakupan Group `Head Office {runId}` beserta descendant.
  - DU-204-3: User `Budi Santoso {runId}`, pelapor umum, pemegang aset, cakupan aset yang ia pegang.
  - DU-204-4: Group `Head Office {runId}`.
  - DU-204-5: Aset `Laptop Dell Latitude 5420 - 21 {runId}`, Group `Head Office {runId}`, TAG `RFID-L21 {runId}`, punya record `Damaged`.
  - DU-204-6: Aset `Laptop Dell Latitude 5420 - 22 {runId}`, Group `Head Office {runId}`, TAG `RFID-L22 {runId}`, punya record `Damaged`.
  - DU-204-7: Aset `Monitor Dell P2422H - 21 {runId}`, Group `Head Office {runId}`, TAG `RFID-M21 {runId}`, `Borrowed` oleh `Budi Santoso {runId}`, punya record `Damaged`.
  - DU-204-8: Aset `Monitor Dell P2422H - 22 {runId}`, Group `Head Office {runId}`, TAG `RFID-M22 {runId}`, `Assigned` kepada `Budi Santoso {runId}`, punya record `Damaged`.
  - DU-204-9: Aset `Forklift Toyota 8FD - 21 {runId}`, Group `Head Office {runId}`, TAG `RFID-F21 {runId}`, punya record `Damaged`, TAG tidak terbaca oleh pemindai.
  - DU-204-10: Aset `Projector Epson EB-X06 - 21 {runId}`, Group `Head Office {runId}`, TAG `RFID-P21 {runId}`, punya record `Reported Disposal`.
  - DU-204-11: Aset `Projector Epson EB-X06 - 22 {runId}`, Group `Head Office {runId}`, TAG `RFID-P22 {runId}`, punya record `In Disposal Process`.
  - DU-204-12: Aset `Camera Canon EOS - 21 {runId}`, Group `Head Office {runId}`, TAG `RFID-C21 {runId}`, punya record `Waiting for Confirmation` dari laporan pelapor umum `Budi Santoso {runId}`.
  - DU-204-13: Aset `Projector Epson EB-X06 - 23 {runId}`, Group `Head Office {runId}`, tanpa TAG, punya record `Damaged` Source `Registration` tanpa Damaged Photo.
  - DU-204-14: Aset `Printer HP LaserJet M404 - 21 {runId}`, Group `Head Office {runId}`, TAG `RFID-H21 {runId}`, punya record `Damaged` dari laporan `Rina Wulandari {runId}`.
  - DU-204-15: TAG `RFID-X99 {runId}`, milik aset lain `Handheld Scanner Zebra TC21 - 21 {runId}`.
  - DU-204-16: Aset `Handheld Scanner Zebra TC21 - 21 {runId}`, TAG `RFID-X99 {runId}`.
  - DU-204-17: Repair note `Komponen rusak sudah diganti {runId}`.
  - DU-204-18: Repair note `Komponen utama sudah diganti dan unit diuji ulang selama beberapa jam tanpa gangguan apa pun pada seluruh fungsinya, Komponen utama sudah diganti dan unit diuji ulang selama beberapa jam tanpa gangguan apa pun pada seluruh fungsinya, Komponen utama sudah diganti dan unit diuji ulang selama beberapa jam tanpa gangguan apa pun pada seluruh fungsinya, Komponenx` (360 karakter).
  - DU-204-19: Repair note `Komponen utama sudah diganti dan unit diuji ulang selama beberapa jam tanpa gangguan apa pun pada seluruh fungsinya, Komponen utama sudah diganti dan unit diuji ulang selama beberapa jam tanpa gangguan apa pun pada seluruh fungsinya, Komponen utama sudah diganti dan unit diuji ulang selama beberapa jam tanpa gangguan apa pun pada seluruh fungsinya, Komponenxy` (361 karakter).
  - DU-204-20: Repair note dikosongkan.
  - DU-204-21: After photo `perbaikan-{runId}.jpg`.
- Kondisi:
  - After photo required bernilai `OFF`.

## Test Steps

### Mark as Repaired atas aset ber-TAG yang valid menyelesaikan record sebagai Repaired
1. Total Control `Agus Pratama {runId}` menjalankan Mark as Repaired atas `Laptop Dell Latitude 5420 - 21 {runId}` dengan Scan TAG `RFID-L21 {runId}` milik aset, Repair note `Komponen rusak sudah diganti {runId}`, dan After photo `perbaikan-{runId}.jpg`
2. Verifikasi record `Damaged` berubah menjadi `Repaired` oleh Aktor Damaged
3. Verifikasi status record, status global aset `Normal`, dan penghapusan penanda terjadi bersamaan sebagai satu transaksi
4. Verifikasi Damage Log memuat node `Marked as repaired by` dengan pelaku `Agus Pratama {runId}`, Repair note, dan After photo
5. Verifikasi Transaction log aset dan Transaction admin log `Agus Pratama {runId}` memuat Mark as Repaired itu

### Aset ber-TAG wajib terverifikasi: belum dipindai atau TAG milik aset lain ditolak
6. Total Control `Agus Pratama {runId}` menjalankan Mark as Repaired atas `Laptop Dell Latitude 5420 - 22 {runId}` tanpa Scan TAG dengan Repair note `Komponen rusak sudah diganti {runId}`
7. Verifikasi permintaan ditolak karena aset ber-TAG belum terverifikasi dan record tetap `Damaged`
8. Total Control `Agus Pratama {runId}` menjalankan Mark as Repaired atas `Laptop Dell Latitude 5420 - 22 {runId}` dengan Scan TAG `RFID-X99 {runId}` milik `Handheld Scanner Zebra TC21 - 21 {runId}` dan Repair note `Komponen rusak sudah diganti {runId}`
9. Verifikasi permintaan ditolak karena TAG bukan milik `Laptop Dell Latitude 5420 - 22 {runId}` dan record tetap `Damaged`
10. Verifikasi penolakan TAG itu tidak menambah node Damage Log di record

### Repair note wajib 1 sampai 360 karakter
11. Total Control `Agus Pratama {runId}` menjalankan Mark as Repaired atas `Laptop Dell Latitude 5420 - 22 {runId}` dengan Scan TAG `RFID-L22 {runId}` milik aset dan Repair note dikosongkan
12. Verifikasi permintaan ditolak karena Repair note kosong dan record tetap `Damaged`
13. Total Control `Agus Pratama {runId}` menjalankan Mark as Repaired atas `Laptop Dell Latitude 5420 - 22 {runId}` dengan Scan TAG `RFID-L22 {runId}` milik aset dan Repair note `Komponen utama sudah diganti dan unit diuji ulang selama beberapa jam tanpa gangguan apa pun pada seluruh fungsinya, Komponen utama sudah diganti dan unit diuji ulang selama beberapa jam tanpa gangguan apa pun pada seluruh fungsinya, Komponen utama sudah diganti dan unit diuji ulang selama beberapa jam tanpa gangguan apa pun pada seluruh fungsinya, Komponenxy` (361 karakter)
14. Verifikasi permintaan ditolak karena Repair note lebih dari 360 karakter dan record tetap `Damaged`
15. Total Control `Agus Pratama {runId}` menjalankan Mark as Repaired atas `Laptop Dell Latitude 5420 - 22 {runId}` dengan Scan TAG `RFID-L22 {runId}` milik aset dan Repair note `Komponen utama sudah diganti dan unit diuji ulang selama beberapa jam tanpa gangguan apa pun pada seluruh fungsinya, Komponen utama sudah diganti dan unit diuji ulang selama beberapa jam tanpa gangguan apa pun pada seluruh fungsinya, Komponen utama sudah diganti dan unit diuji ulang selama beberapa jam tanpa gangguan apa pun pada seluruh fungsinya, Komponenx` (360 karakter)
16. Verifikasi permintaan diterima dan record menjadi `Repaired` dengan Repair note sepanjang 360 karakter

### After photo mengikuti nilai After photo required
17. Pemegang Update `Rina Wulandari {runId}` menjalankan Mark as Repaired atas `Camera Canon EOS - 21 {runId}` yang dilaporkan pelapor umum dan masih `Waiting for Confirmation` dengan Scan TAG `RFID-C21 {runId}` milik aset dan Repair note `Komponen rusak sudah diganti {runId}`
18. Verifikasi permintaan ditolak karena record bukan `Damaged` dan record tetap `Waiting for Confirmation`
19. Pemegang Update `Rina Wulandari {runId}` menjalankan Mark as Repaired atas `Printer HP LaserJet M404 - 21 {runId}` yang ia laporkan sendiri dengan Scan TAG `RFID-H21 {runId}` milik aset, Repair note `Komponen rusak sudah diganti {runId}`, dan tanpa After photo
20. Verifikasi After photo hanya wajib bila `After photo required` bernilai `ON`; karena nilainya `OFF`, permintaan tanpa After photo diterima
21. Verifikasi record menjadi `Repaired` karena Mark as Repaired oleh pelapor admin diperbolehkan

### Mark as Repaired atas aset yang sedang dipinjam atau ditugaskan dan atas aset tanpa TAG
22. Pemegang Update `Rina Wulandari {runId}` menjalankan Mark as Repaired atas `Monitor Dell P2422H - 21 {runId}` yang sedang dipinjam dengan Scan TAG `RFID-M21 {runId}` milik aset dan Repair note `Komponen rusak sudah diganti {runId}`
23. Verifikasi record menjadi `Repaired` dan baris peminjaman `Budi Santoso {runId}` tetap tidak berubah
24. Pemegang Update `Rina Wulandari {runId}` menjalankan Mark as Repaired atas `Monitor Dell P2422H - 22 {runId}` yang sedang ditugaskan dengan Scan TAG `RFID-M22 {runId}` milik aset dan Repair note `Komponen rusak sudah diganti {runId}`
25. Verifikasi record menjadi `Repaired` dan baris penugasan `Budi Santoso {runId}` tetap tidak berubah
26. Pemegang Update `Rina Wulandari {runId}` menjalankan Mark as Repaired atas `Projector Epson EB-X06 - 23 {runId}` yang tidak memiliki TAG dengan Repair note `Komponen rusak sudah diganti {runId}`
27. Verifikasi permintaan diterima tanpa Scan TAG dan record menjadi `Repaired`
28. Verifikasi Damage Log record itu memuat node `Reported damaged by` tanpa Damaged Photo karena Source `Registration`

### Identifikasi manual saat TAG tidak terbaca
29. Total Control `Agus Pratama {runId}` menjalankan Mark as Repaired atas `Forklift Toyota 8FD - 21 {runId}` yang TAG-nya tidak terbaca dengan identifikasi manual lewat Report TAG dan Repair note `Komponen rusak sudah diganti {runId}`
30. Verifikasi record menjadi `Repaired` tanpa Scan TAG dan node `Marked as repaired by` mencatat `Manual identification`

### Record berstatus Disposal menolak Mark as Repaired
31. Total Control `Agus Pratama {runId}` menjalankan Mark as Repaired atas `Projector Epson EB-X06 - 21 {runId}` yang berstatus `Reported Disposal` dengan Scan TAG `RFID-P21 {runId}` milik aset dan Repair note `Komponen rusak sudah diganti {runId}`
32. Verifikasi permintaan ditolak karena status record sudah berubah dan record tetap `Reported Disposal`
33. Total Control `Agus Pratama {runId}` menjalankan Mark as Repaired atas `Projector Epson EB-X06 - 22 {runId}` yang berstatus `In Disposal Process` dengan Scan TAG `RFID-P22 {runId}` milik aset dan Repair note `Komponen rusak sudah diganti {runId}`
34. Verifikasi permintaan ditolak karena status record sudah berubah dan record tetap `In Disposal Process`
35. Verifikasi penolakan itu tidak menambah node Damage Log di kedua record
36. Verifikasi penolakan itu tidak memicu event `damaged_resolved` untuk kedua record
