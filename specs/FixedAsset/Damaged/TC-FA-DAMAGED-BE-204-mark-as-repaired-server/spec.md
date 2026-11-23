---
id: TC-FA-DAMAGED-BE-204-mark-as-repaired-server
title: "Server memvalidasi Mark as Repaired: Scan TAG milik aset untuk aset ber-TAG, After photo menurut setting, Repair note, identifikasi manual, status record Repaired dengan penghapusan penanda secara atomik, dan penolakan pada status Disposal"
layer: be-e2e
priority: Critical
caseType: Positive
status: ready-for-automation
sourceRules: ["§Aturan Logika Modul#r59", "§Aturan Logika Modul#r60", "§Aturan Logika Modul#r90", "§Aturan Logika Modul#r39", "§9.2#r5", "§9.2#b17", "§9.2#b19", "§9.6#r5", FLD-DMG-03, FLD-DMG-04, FLD-DMG-05, V-DMG-03, V-DMG-04, V-DMG-05, FI-DMG-08, FI-DMG-11, FI-DMG-12, S-DMG-07, EC-DMG-16, EC-DMG-31, "§9.4.4#r23", "§9.4.4#r25", "§9.4.4#r26", "§9.4.4#r9", "§9.4.1#r12", EB-FRM-4@repair-note, "§3#p7", F-DMG-05]
smoke: []
dependsOn: []
owner: BE
trace:
  "§Aturan Logika Modul#r59": [2, 19]
  "§Aturan Logika Modul#r60": 2
  "§Aturan Logika Modul#r90": 22
  "§Aturan Logika Modul#r39": [39, 40, 41, 42, 43, 44, 45, 46]
  "§9.2#r5": 2
  "§9.2#b17": 31
  "§9.2#b19": [3, 24, 26]
  "§9.6#r5": [3, 4, 5]
  FLD-DMG-03: [7, 9]
  FLD-DMG-04: 21
  FLD-DMG-05: [13, 15]
  V-DMG-03: 9
  V-DMG-04: 7
  V-DMG-05: [34, 36]
  FI-DMG-08: 7
  FI-DMG-11: 21
  FI-DMG-12: 21
  S-DMG-07: 21
  EC-DMG-16: 31
  EC-DMG-31: [28, 29]
  "§9.4.4#r23": [31, 32]
  "§9.4.4#r25": [10, 11]
  "§9.4.4#r26": [34, 37, 38]
  "§9.4.4#r9": 29
  "§9.4.1#r12": 31
  EB-FRM-4@repair-note: [15, 17]
  "§3#p7": 2
  F-DMG-05: 2
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
  - DU-204-5: Aset `Laptop Dell Latitude 5420 - 21 {runId}`, Group `Head Office {runId}`, TAG `RFID-L21 {runId}`, tidak dipegang, punya record `Damaged`.
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
  - DU-204-22: Aset `Generator Honda EU22i - 21 {runId}`, Group `Head Office {runId}`, TAG `RFID-G21 {runId}`, punya record `Damaged`, Activity Lock `Under Maintenance` karena punya Work Order berjalan dan jadwal maintenance berikutnya.
  - DU-204-23: Aset `Rack Server Dell R740 - 21 {runId}`, Group `Head Office {runId}`, TAG `RFID-R21 {runId}`, punya record `Damaged`, Activity Lock `In Audit` karena menjadi item sesi Audit berjalan milik `Sinta Marlina {runId}` dengan baris audit `Verified`.
- Kondisi:
  - After photo required bernilai `OFF`.

## Test Steps

### Mark as Repaired atas aset ber-TAG yang valid menyelesaikan record sebagai Repaired
1. Total Control `Agus Pratama {runId}` menjalankan Mark as Repaired atas `Laptop Dell Latitude 5420 - 21 {runId}` dengan Scan TAG `RFID-L21 {runId}` milik aset, Repair note `Komponen rusak sudah diganti {runId}`, dan After photo `perbaikan-{runId}.jpg`
2. Verifikasi record `Damaged` berubah menjadi `Repaired` oleh Aktor Damaged
3. Verifikasi status record, status global aset dihitung ulang menjadi `Normal` karena aset tidak dipegang, dan penghapusan penanda terjadi bersamaan sebagai satu transaksi
4. Verifikasi Damage Log memuat node `Marked as repaired by` dengan pelaku `Agus Pratama {runId}`, Repair note, dan After photo
5. Verifikasi Transaction log aset dan Transaction admin log `Agus Pratama {runId}` memuat Mark as Repaired itu

### Aset ber-TAG wajib terverifikasi: belum dipindai atau TAG milik aset lain ditolak
6. Total Control `Agus Pratama {runId}` menjalankan Mark as Repaired atas `Laptop Dell Latitude 5420 - 22 {runId}` tanpa Scan TAG dengan Repair note `Komponen rusak sudah diganti {runId}`
7. Verifikasi permintaan ditolak karena aset ber-TAG belum terverifikasi dan record tetap `Damaged`
8. Total Control `Agus Pratama {runId}` menjalankan Mark as Repaired atas `Laptop Dell Latitude 5420 - 22 {runId}` dengan Scan TAG `RFID-X99 {runId}` milik `Handheld Scanner Zebra TC21 - 21 {runId}` dan Repair note `Komponen rusak sudah diganti {runId}`
9. Verifikasi permintaan ditolak karena TAG bukan milik `Laptop Dell Latitude 5420 - 22 {runId}` dan record tetap `Damaged`
10. Verifikasi penolakan TAG itu tidak menambah node Damage Log di record
11. Verifikasi penolakan TAG itu tidak memicu event `damaged_resolved` untuk record itu

### Repair note wajib 1 sampai 360 karakter
12. Total Control `Agus Pratama {runId}` menjalankan Mark as Repaired atas `Laptop Dell Latitude 5420 - 22 {runId}` dengan Scan TAG `RFID-L22 {runId}` milik aset dan Repair note dikosongkan
13. Verifikasi permintaan ditolak karena Repair note kosong dan record tetap `Damaged`
14. Total Control `Agus Pratama {runId}` menjalankan Mark as Repaired atas `Laptop Dell Latitude 5420 - 22 {runId}` dengan Scan TAG `RFID-L22 {runId}` milik aset dan Repair note `Komponen utama sudah diganti dan unit diuji ulang selama beberapa jam tanpa gangguan apa pun pada seluruh fungsinya, Komponen utama sudah diganti dan unit diuji ulang selama beberapa jam tanpa gangguan apa pun pada seluruh fungsinya, Komponen utama sudah diganti dan unit diuji ulang selama beberapa jam tanpa gangguan apa pun pada seluruh fungsinya, Komponenxy` (361 karakter)
15. Verifikasi permintaan ditolak karena Repair note lebih dari 360 karakter dan record tetap `Damaged`
16. Total Control `Agus Pratama {runId}` menjalankan Mark as Repaired atas `Laptop Dell Latitude 5420 - 22 {runId}` dengan Scan TAG `RFID-L22 {runId}` milik aset dan Repair note `Komponen utama sudah diganti dan unit diuji ulang selama beberapa jam tanpa gangguan apa pun pada seluruh fungsinya, Komponen utama sudah diganti dan unit diuji ulang selama beberapa jam tanpa gangguan apa pun pada seluruh fungsinya, Komponen utama sudah diganti dan unit diuji ulang selama beberapa jam tanpa gangguan apa pun pada seluruh fungsinya, Komponenx` (360 karakter)
17. Verifikasi permintaan diterima dan record menjadi `Repaired` dengan Repair note sepanjang 360 karakter

### After photo mengikuti nilai After photo required
18. Pemegang Update `Rina Wulandari {runId}` menjalankan Mark as Repaired atas `Camera Canon EOS - 21 {runId}` yang dilaporkan pelapor umum dan masih `Waiting for Confirmation` dengan Scan TAG `RFID-C21 {runId}` milik aset dan Repair note `Komponen rusak sudah diganti {runId}`
19. Verifikasi permintaan ditolak karena record bukan `Damaged` dan record tetap `Waiting for Confirmation`
20. Pemegang Update `Rina Wulandari {runId}` menjalankan Mark as Repaired atas `Printer HP LaserJet M404 - 21 {runId}` yang ia laporkan sendiri dengan Scan TAG `RFID-H21 {runId}` milik aset, Repair note `Komponen rusak sudah diganti {runId}`, dan tanpa After photo
21. Verifikasi After photo hanya wajib bila `After photo required` bernilai `ON`; karena nilainya `OFF`, permintaan tanpa After photo diterima
22. Verifikasi record menjadi `Repaired` karena Mark as Repaired oleh pelapor admin diperbolehkan

### Mark as Repaired atas aset yang sedang dipinjam atau ditugaskan dan atas aset tanpa TAG
23. Pemegang Update `Rina Wulandari {runId}` menjalankan Mark as Repaired atas `Monitor Dell P2422H - 21 {runId}` yang sedang dipinjam dengan Scan TAG `RFID-M21 {runId}` milik aset dan Repair note `Komponen rusak sudah diganti {runId}`
24. Verifikasi record menjadi `Repaired` dan baris peminjaman `Budi Santoso {runId}` tetap tidak berubah
25. Pemegang Update `Rina Wulandari {runId}` menjalankan Mark as Repaired atas `Monitor Dell P2422H - 22 {runId}` yang sedang ditugaskan dengan Scan TAG `RFID-M22 {runId}` milik aset dan Repair note `Komponen rusak sudah diganti {runId}`
26. Verifikasi record menjadi `Repaired` dan baris penugasan `Budi Santoso {runId}` tetap tidak berubah
27. Pemegang Update `Rina Wulandari {runId}` menjalankan Mark as Repaired atas `Projector Epson EB-X06 - 23 {runId}` yang tidak memiliki TAG dengan Repair note `Komponen rusak sudah diganti {runId}`
28. Verifikasi permintaan diterima tanpa Scan TAG dan record menjadi `Repaired`
29. Verifikasi Damage Log record itu memuat node `Reported damaged by` tanpa Damaged Photo karena Source `Registration`

### Identifikasi manual saat TAG tidak terbaca
30. Total Control `Agus Pratama {runId}` menjalankan Mark as Repaired atas `Forklift Toyota 8FD - 21 {runId}` yang TAG-nya tidak terbaca dengan identifikasi manual lewat Report TAG dan Repair note `Komponen rusak sudah diganti {runId}`
31. Verifikasi record menjadi `Repaired` tanpa Scan TAG dan node `Marked as repaired by` mencatat `Manual identification`
32. Verifikasi Mark as Repaired lewat identifikasi manual itu memicu tepat satu event `damaged_resolved`

### Record berstatus Disposal menolak Mark as Repaired
33. Total Control `Agus Pratama {runId}` menjalankan Mark as Repaired atas `Projector Epson EB-X06 - 21 {runId}` yang berstatus `Reported Disposal` dengan Scan TAG `RFID-P21 {runId}` milik aset dan Repair note `Komponen rusak sudah diganti {runId}`
34. Verifikasi permintaan ditolak karena status record sudah berubah dan record tetap `Reported Disposal`
35. Total Control `Agus Pratama {runId}` menjalankan Mark as Repaired atas `Projector Epson EB-X06 - 22 {runId}` yang berstatus `In Disposal Process` dengan Scan TAG `RFID-P22 {runId}` milik aset dan Repair note `Komponen rusak sudah diganti {runId}`
36. Verifikasi permintaan ditolak karena status record sudah berubah dan record tetap `In Disposal Process`
37. Verifikasi penolakan itu tidak menambah node Damage Log di kedua record
38. Verifikasi penolakan itu tidak memicu event `damaged_resolved` untuk kedua record

### Mark as Repaired tidak dibatasi Activity Lock dan tidak mengubah Work Order, jadwal maintenance, maupun baris Audit yang sudah final
39. Total Control `Agus Pratama {runId}` menjalankan Mark as Repaired atas `Generator Honda EU22i - 21 {runId}` yang ber-Activity Lock `Under Maintenance` dengan Scan TAG `RFID-G21 {runId}` milik aset dan Repair note `Komponen rusak sudah diganti {runId}`
40. Verifikasi permintaan diterima dan record menjadi `Repaired` untuk aset yang ber-Activity Lock `Under Maintenance`
41. Verifikasi Work Order aset itu tidak diubah, tidak ditutup, dan tidak dijeda, dan jadwal maintenance aset itu tidak berubah
42. Verifikasi Activity Lock `Under Maintenance` tetap ada setelah Mark as Repaired
43. Total Control `Agus Pratama {runId}` menjalankan Mark as Repaired atas `Rack Server Dell R740 - 21 {runId}` yang ber-Activity Lock `In Audit` dengan Scan TAG `RFID-R21 {runId}` milik aset dan Repair note `Komponen rusak sudah diganti {runId}`
44. Verifikasi permintaan diterima dan record menjadi `Repaired` untuk aset yang ber-Activity Lock `In Audit`
45. Verifikasi baris audit aset itu di sesi milik `Sinta Marlina {runId}` tetap `Verified` dan tidak berubah oleh Mark as Repaired
46. Verifikasi Activity Lock `In Audit` tetap ada setelah Mark as Repaired
