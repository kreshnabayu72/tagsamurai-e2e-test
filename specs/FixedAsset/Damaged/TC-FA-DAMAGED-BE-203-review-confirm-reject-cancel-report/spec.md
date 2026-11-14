---
id: TC-FA-DAMAGED-BE-203-review-confirm-reject-cancel-report
title: "Server memproses Confirm, Reject, dan Cancel Report: pemisahan tugas, status akhir, yang memutuskan lebih dulu berlaku, record selesai tidak dibuka ulang, tanpa batas tunggu, dan konflik status"
layer: be-e2e
priority: Critical
caseType: Negative
status: ready-for-automation
sourceRules: ["§Aturan Logika Modul#r18", "§Aturan Logika Modul#r22", "§Aturan Logika Modul#r23", "§Aturan Logika Modul#r49", "§Aturan Logika Modul#r50", "§Aturan Logika Modul#r51", "§Aturan Logika Modul#r52", "§Aturan Logika Modul#r53", "§Aturan Logika Modul#r54", "§Aturan Logika Modul#r55", "§Aturan Logika Modul#r56", "§Aturan Logika Modul#r35", "§Aturan Logika Modul#r64", "§Aturan Logika Modul#r65", "§Aturan Logika Modul#r87", "§9.2#r1", "§9.2#r7", "§9.2#r8", "§9.2#b14", "§9.4.3#b4", "§9.4.3#b5", "§9.4.3#b6", "§9.6#r2", "§9.6#r3", "§9.6#r4", "§4.2.4#p5", "V-DMG-01", "V-DMG-07", "D-DMG-06", "§9.4.2#r7", "§9.4.2#r8", "§9.4.2#r20", "§9.4.4#r16", "§9.4.4#r17", "§9.4.4#r18", "§9.4.1#r11", "§9.9#r6", "§2.1#b3", "§2.1#b7", "§3#p4", "EB-FRM-4@reason", "EB-ERR-4", "EB-CON-3", "EB-EDG-1", "§9.1#r4"]
smoke: []
dependsOn: []
owner: BE
trace:
  "§Aturan Logika Modul#r18": 2
  "§Aturan Logika Modul#r22": 11
  "§Aturan Logika Modul#r23": 15
  "§Aturan Logika Modul#r49": 2
  "§Aturan Logika Modul#r50": 11
  "§Aturan Logika Modul#r51": 31
  "§Aturan Logika Modul#r52": [35, 79, 81]
  "§Aturan Logika Modul#r53": [15, 22]
  "§Aturan Logika Modul#r54": [73, 74]
  "§Aturan Logika Modul#r55": [31, 32, 83, 84]
  "§Aturan Logika Modul#r56": [37, 39]
  "§Aturan Logika Modul#r35": 20
  "§Aturan Logika Modul#r64": [67, 69]
  "§Aturan Logika Modul#r65": 71
  "§Aturan Logika Modul#r87": [24, 26]
  "§9.2#r1": 2
  "§9.2#r7": 11
  "§9.2#r8": 15
  "§9.2#b14": [2, 11, 15]
  "§9.4.3#b4": [67, 69]
  "§9.4.3#b5": [73, 76]
  "§9.4.3#b6": [24, 26]
  "§9.6#r2": [3, 4, 5]
  "§9.6#r3": [12, 13]
  "§9.6#r4": [16, 17]
  "§4.2.4#p5": [46, 50, 61]
  "V-DMG-01": 24
  "V-DMG-07": [42, 45, 49, 54, 57, 59, 61, 63]
  "D-DMG-06": [46, 50, 61]
  "§9.4.2#r7": [41, 42, 45, 49]
  "§9.4.2#r8": 24
  "§9.4.2#r20": [73, 74]
  "§9.4.4#r16": 27
  "§9.4.4#r17": [41, 42, 45]
  "§9.4.4#r18": 74
  "§9.4.1#r11": 73
  "§9.9#r6": [7, 9]
  "§2.1#b3": [31, 35]
  "§2.1#b7": [24, 29]
  "§3#p4": 15
  "EB-FRM-4@reason": [9, 11]
  "EB-ERR-4": [7, 24, 49, 57]
  "EB-CON-3": [41, 52, 54, 59, 63, 65]
  "EB-EDG-1": [57, 61, 65, 67]
  "§9.1#r4": 2
---

# Server memproses Confirm, Reject, dan Cancel Report: pemisahan tugas, status akhir, yang memutuskan lebih dulu berlaku, record selesai tidak dibuka ulang, tanpa batas tunggu, dan konflik status

## Prerequisites
- Aktor:
  - Total Control `Agus Pratama {runId}`, Aktor Damaged.
  - Pemegang Manage asset & TAG (Update) `Rina Wulandari {runId}`, Aktor Damaged pada Group `Head Office {runId}`.
  - Aktor peminjaman `Yoga Tanuwijaya {runId}` dan Aktor penugasan `Dewi Anggraini {runId}`, tanpa hak Update Manage asset & TAG.
  - Aktor pelepasan aset `Maya Puspita {runId}`, Asset Admin sub-tab Disposal.
  - Pelapor umum `Budi Santoso {runId}`, `Dedi Kurniawan {runId}`, `Sari Dewanti {runId}`, dan `Hana Lestari {runId}`, tanpa role Damaged kecuali disebut lain.
  - PIC `Sinta Maharani {runId}`, pelapor atas nama karyawan tanpa akun `Tono Rahmat {runId}`.
- Data:
  - DU-203-1: User `Agus Pratama {runId}`, Total Control, cakupan seluruh client.
  - DU-203-2: User `Rina Wulandari {runId}`, Manage asset & TAG (Update), cakupan Group `Head Office {runId}` beserta descendant.
  - DU-203-3: User `Yoga Tanuwijaya {runId}`, Aktor Borrow, cakupan Group `Head Office {runId}`.
  - DU-203-4: User `Dewi Anggraini {runId}`, Aktor Assignment, cakupan Group `Head Office {runId}`.
  - DU-203-5: User `Maya Puspita {runId}`, Asset Admin sub-tab Disposal, cakupan Group `Head Office {runId}`.
  - DU-203-6: User `Budi Santoso {runId}`, pelapor umum, pemegang aset, cakupan aset yang ia pegang.
  - DU-203-7: User `Dedi Kurniawan {runId}`, pelapor umum, pemindai TAG, cakupan aset yang ia pindai.
  - DU-203-8: User `Sari Dewanti {runId}`, pelapor umum, kemudian pemegang Manage asset & TAG (Update), cakupan aset yang ia pegang, lalu Group `Head Office {runId}`.
  - DU-203-9: User `Hana Lestari {runId}`, pelapor umum, pemegang aset yang kemudian dinonaktifkan, cakupan aset yang ia pegang.
  - DU-203-10: User `Sinta Maharani {runId}`, PIC pelapor atas nama karyawan tanpa akun `Tono Rahmat {runId}`, cakupan aset yang dipegang `Tono Rahmat {runId}`.
  - DU-203-11: User `Tono Rahmat {runId}`, karyawan tanpa akun, pemegang aset, PIC `Sinta Maharani {runId}`.
  - DU-203-12: Reported By `Sinta Maharani {runId} on behalf of Tono Rahmat {runId}`.
  - DU-203-13: Waktu laporan `T0 − 90 hari, pukul 08:15`.
  - DU-203-14: Group `Head Office {runId}`.
  - DU-203-15: Aset `Laptop Dell Latitude 5420 - 11 {runId}`, Group `Head Office {runId}`, punya record `Waiting for Confirmation` dari laporan `Budi Santoso {runId}`.
  - DU-203-16: Aset `Printer HP LaserJet M404 - 4 {runId}`, Group `Head Office {runId}`, punya record `Waiting for Confirmation` dari laporan `Dedi Kurniawan {runId}` lewat scan TAG.
  - DU-203-17: Aset `Monitor Dell P2422H - 4 {runId}`, Group `Head Office {runId}`, punya record `Waiting for Confirmation` dari laporan `Budi Santoso {runId}`.
  - DU-203-18: Aset `Tablet Samsung Tab A8 - 7 {runId}`, Group `Head Office {runId}`, `Assigned` kepada `Budi Santoso {runId}`, punya record `Waiting for Confirmation` dari laporannya.
  - DU-203-19: Aset `Scanner Fujitsu fi-7160 - 5 {runId}`, Group `Head Office {runId}`, punya record `Waiting for Confirmation` dari laporan `Sinta Maharani {runId} on behalf of Tono Rahmat {runId}`.
  - DU-203-20: Aset `Camera Canon EOS - 4 {runId}`, Group `Head Office {runId}`, punya record `Waiting for Confirmation` dari laporan `Sari Dewanti {runId}`.
  - DU-203-21: Aset `Toyota Avanza - 5 {runId}`, Group `Head Office {runId}`, punya record `Damaged` dari laporan pemegang Update `Rina Wulandari {runId}`.
  - DU-203-22: Aset `Forklift Toyota 8FD - 4 {runId}`, Group `Head Office {runId}`, `Borrowed` oleh `Budi Santoso {runId}`, punya record `Waiting for Confirmation` dari laporannya.
  - DU-203-23: Aset `Drill Bosch GSB - 7 {runId}`, Group `Head Office {runId}`, `Borrowed` oleh `Budi Santoso {runId}`, punya record `Waiting for Confirmation` dari laporannya.
  - DU-203-24: Aset `Handheld Scanner Zebra TC21 - 4 {runId}`, Group `Head Office {runId}`, `Assigned` kepada `Budi Santoso {runId}`, punya record `Waiting for Confirmation` dari laporannya.
  - DU-203-25: Aset `Office Chair Ergo - 20 {runId}`, Group `Head Office {runId}`, punya record `Waiting for Confirmation` dari laporan `Budi Santoso {runId}`.
  - DU-203-26: Aset `Office Chair Ergo - 21 {runId}`, Group `Head Office {runId}`, punya record `Waiting for Confirmation` dari laporan `Budi Santoso {runId}`.
  - DU-203-27: Aset `Office Chair Ergo - 22 {runId}`, Group `Head Office {runId}`, punya record `Waiting for Confirmation` dari laporan `Budi Santoso {runId}`.
  - DU-203-28: Aset `Projector Epson EB-X06 - 6 {runId}`, Group `Head Office {runId}`, punya record `Damaged`, tidak dipegang, ber-TAG `RFID`.
  - DU-203-29: Aset `Projector Epson EB-X06 - 7 {runId}`, Group `Head Office {runId}`, punya record `Damaged`, tidak dipegang, ber-TAG `RFID`.
  - DU-203-30: Aset `Monitor Dell P2422H - 10 {runId}`, Group `Head Office {runId}`, punya record `Reported Disposal`.
  - DU-203-31: Aset `Laptop Dell Latitude 5420 - 12 {runId}`, Group `Head Office {runId}`, punya record `Damaged`, tidak dipegang, ber-TAG `RFID`.
  - DU-203-32: Aset `Laptop Dell Latitude 5420 - 13 {runId}`, Group `Head Office {runId}`, punya record `Damaged`, tidak dipegang.
  - DU-203-33: Aset `Laptop Dell Latitude 5420 - 14 {runId}`, Group `Head Office {runId}`, punya record `Damaged`, tidak dipegang, ber-TAG `RFID`.
  - DU-203-34: Aset `Laptop Dell Latitude 5420 - 15 {runId}`, Group `Head Office {runId}`, punya record `Damaged`, tidak dipegang, ber-TAG `RFID`.
  - DU-203-35: Aset `Toyota Avanza - 6 {runId}`, Group `Head Office {runId}`, `Normal`, tanpa record berjalan.
  - DU-203-36: Aset `Drill Bosch GSB - 8 {runId}`, Group `Head Office {runId}`, punya record `Damaged` yang status terakhirnya diubah `System` saat baris Disposal kedaluwarsa.
  - DU-203-37: Aset `Monitor Dell P2422H - 11 {runId}`, Group `Head Office {runId}`, punya record `Repaired`.
  - DU-203-38: Aset `Printer HP LaserJet M404 - 5 {runId}`, Group `Head Office {runId}`, punya record `Waiting for Confirmation` dari laporan `Hana Lestari {runId}` sejak `T0 − 90 hari, pukul 08:15`.
  - DU-203-39: Reason `Foto yang dikirim bukan foto aset ini {runId}`.
  - DU-203-40: Reason `Gambar yang dilampirkan tidak menunjukkan kerusakan pada aset yang dilaporkan sehingga laporan tidak dapat dilanjutkan, Gambar yang dilampirkan tidak menunjukkan kerusakan pada aset yang dilaporkan sehingga laporan tidak dapat dilanjutkan, Gambar yang dilampirkan tidak menunjukkan kerusakan pada aset yang dilaporkan sehingga laporan tidak dapat dilanjutkan,x` (360 karakter).
  - DU-203-41: Reason `Gambar yang dilampirkan tidak menunjukkan kerusakan pada aset yang dilaporkan sehingga laporan tidak dapat dilanjutkan, Gambar yang dilampirkan tidak menunjukkan kerusakan pada aset yang dilaporkan sehingga laporan tidak dapat dilanjutkan, Gambar yang dilampirkan tidak menunjukkan kerusakan pada aset yang dilaporkan sehingga laporan tidak dapat dilanjutkan,xy` (361 karakter).
  - DU-203-42: Reason dikosongkan.
  - DU-203-43: Repair note `Komponen rusak sudah diganti {runId}`.
  - DU-203-44: What happened `Casing retak setelah terbentur {runId}`, Damaged Photo `casing-retak.jpg`.
  - DU-203-45: Aset `Forklift Toyota 8FD - 6 {runId}`, Group `Head Office {runId}`, `Borrowed` oleh `Budi Santoso {runId}`, punya record `Waiting for Confirmation` dari laporannya.
  - DU-203-46: Aset `Drill Bosch GSB - 9 {runId}`, Group `Head Office {runId}`, `Borrowed` oleh `Budi Santoso {runId}`, punya record `Waiting for Confirmation` dari laporannya.

## Test Steps

### Confirm oleh Aktor Damaged mengubah Waiting for Confirmation menjadi Damaged
1. Pemegang Update `Rina Wulandari {runId}` melakukan Confirm atas laporan `Laptop Dell Latitude 5420 - 11 {runId}`
2. Verifikasi record berubah dari `Waiting for Confirmation` menjadi `Damaged`
3. Verifikasi status record dan status global aset berubah bersamaan sebagai satu kesatuan
4. Verifikasi Damage Log record memuat node `Report confirmed by` dengan pelaku `Rina Wulandari {runId}`
5. Verifikasi Transaction log aset dan Transaction admin log `Rina Wulandari {runId}` memuat Confirm itu

### Reject wajib disertai Reason 1 sampai 360 karakter dan membuat record Rejected
6. Pemegang Update `Rina Wulandari {runId}` melakukan Reject atas laporan `Printer HP LaserJet M404 - 4 {runId}` dengan Reason dikosongkan
7. Verifikasi Reject ditolak dan record tetap `Waiting for Confirmation`
8. Pemegang Update `Rina Wulandari {runId}` melakukan Reject atas laporan `Printer HP LaserJet M404 - 4 {runId}` dengan Reason `Gambar yang dilampirkan tidak menunjukkan kerusakan pada aset yang dilaporkan sehingga laporan tidak dapat dilanjutkan, Gambar yang dilampirkan tidak menunjukkan kerusakan pada aset yang dilaporkan sehingga laporan tidak dapat dilanjutkan, Gambar yang dilampirkan tidak menunjukkan kerusakan pada aset yang dilaporkan sehingga laporan tidak dapat dilanjutkan,xy` (361 karakter)
9. Verifikasi Reject ditolak karena Reason lebih dari 360 karakter dan record tetap `Waiting for Confirmation`
10. Pemegang Update `Rina Wulandari {runId}` melakukan Reject atas laporan `Printer HP LaserJet M404 - 4 {runId}` dengan Reason `Gambar yang dilampirkan tidak menunjukkan kerusakan pada aset yang dilaporkan sehingga laporan tidak dapat dilanjutkan, Gambar yang dilampirkan tidak menunjukkan kerusakan pada aset yang dilaporkan sehingga laporan tidak dapat dilanjutkan, Gambar yang dilampirkan tidak menunjukkan kerusakan pada aset yang dilaporkan sehingga laporan tidak dapat dilanjutkan,x` (360 karakter)
11. Verifikasi Reject diterima dan record menjadi `Rejected` dengan Reason sepanjang 360 karakter tersimpan di node `Report rejected by`
12. Verifikasi Reject itu tercatat di Damage Log, Transaction log aset, dan Transaction admin log `Rina Wulandari {runId}`
13. Verifikasi status record dan penanda laporan berubah bersamaan sebagai satu kesatuan

### Cancel Report oleh pelapor membuat record Canceled, juga setelah aset tidak lagi dipegang
14. Pelapor umum `Budi Santoso {runId}` melakukan Cancel Report atas `Monitor Dell P2422H - 4 {runId}`
15. Verifikasi record berubah dari `Waiting for Confirmation` menjadi `Canceled`
16. Verifikasi pembatalan itu tercatat di Damage Log sebagai node `Report canceled by` dengan pelaku `Budi Santoso {runId}`
17. Verifikasi pembatalan itu tidak tercatat di Transaction log aset dan Transaction admin log
18. Aktor penugasan `Dewi Anggraini {runId}` melakukan Unassign atas `Tablet Samsung Tab A8 - 7 {runId}` dari `Budi Santoso {runId}` selagi record masih `Waiting for Confirmation`
19. Pelapor umum `Budi Santoso {runId}` melakukan Cancel Report atas `Tablet Samsung Tab A8 - 7 {runId}` yang tidak lagi ia pegang
20. Verifikasi pembatalan diterima dan record menjadi `Canceled`
21. PIC `Sinta Maharani {runId}` melakukan Cancel Report atas `Scanner Fujitsu fi-7160 - 5 {runId}` yang ia laporkan atas nama `Tono Rahmat {runId}`
22. Verifikasi record menjadi `Canceled` dengan node `Report canceled by` atas nama PIC `Sinta Maharani {runId}`

### Pelapor tidak dapat Confirm atau Reject laporannya sendiri
23. `Sari Dewanti {runId}` melakukan Confirm atas laporannya sendiri `Camera Canon EOS - 4 {runId}`
24. Verifikasi Confirm ditolak dengan pesan `You reported this. Ask another admin.` dan record tetap `Waiting for Confirmation`
25. `Sari Dewanti {runId}` melakukan Reject atas laporannya sendiri `Camera Canon EOS - 4 {runId}` dengan Reason `Foto yang dikirim bukan foto aset ini {runId}`
26. Verifikasi Reject ditolak dan record tetap `Waiting for Confirmation`
27. Verifikasi penolakan itu tidak menambah node Damage Log di record
28. Pemegang Update `Rina Wulandari {runId}` melakukan Confirm atas `Toyota Avanza - 5 {runId}` yang record `Damaged`-nya berasal dari laporan Pelapor admin
29. Verifikasi Confirm tidak berlaku dan ditolak karena record bukan `Waiting for Confirmation`

### Aktor peminjaman dan Aktor penugasan pada laporan pemegang
30. Aktor peminjaman `Yoga Tanuwijaya {runId}` menyelesaikan Return `Forklift Toyota 8FD - 4 {runId}` dengan Assess Damage Confirm atas laporan pemegang
31. Verifikasi record menjadi `Damaged` dengan node `Report confirmed by` yang pelakunya Aktor peminjaman `Yoga Tanuwijaya {runId}`
32. Verifikasi event `damaged_review_resolved` dipicu oleh keputusan itu
33. Pemegang Update `Rina Wulandari {runId}` melakukan Reject atas laporan `Drill Bosch GSB - 7 {runId}` dengan Reason `Foto yang dikirim bukan foto aset ini {runId}`
34. Aktor peminjaman `Yoga Tanuwijaya {runId}` menyelesaikan Return `Drill Bosch GSB - 7 {runId}` dengan Assess Damage Confirm atas laporan pemegang yang sudah ditolak
35. Verifikasi keputusan yang lebih dulu berlaku: record tetap `Rejected`, tidak ada konfirmasi ulang, dan tidak ada node baru dari Return
36. Aktor penugasan `Dewi Anggraini {runId}` melakukan Unassign atas `Handheld Scanner Zebra TC21 - 4 {runId}` dengan jawaban Assess Damage atas laporan pemegang
37. Verifikasi Unassign menautkan laporan pemegang ke jawaban Assess Damage dan record tetap `Waiting for Confirmation`
38. Pemegang Update `Rina Wulandari {runId}` melakukan Confirm atas laporan `Handheld Scanner Zebra TC21 - 4 {runId}`
39. Verifikasi keputusan atas laporan pemegang aset yang ditugaskan tetap ada pada Aktor Damaged dan record menjadi `Damaged`

### Confirm dan Cancel Report atas laporan yang sama: yang memutuskan lebih dulu berlaku
40. Pemegang Update `Rina Wulandari {runId}` melakukan Confirm atas `Office Chair Ergo - 20 {runId}` dan, bersamaan, `Budi Santoso {runId}` melakukan Cancel Report atas laporan yang sama
41. Verifikasi record berakhir tepat di salah satu `Damaged` atau `Canceled`, apa pun urutan tiba kedua permintaan
42. Verifikasi hanya satu node `Report confirmed by` atau `Report canceled by` yang tercatat, dan permintaan yang kalah ditolak karena status record sudah berubah
43. Pemegang Update `Rina Wulandari {runId}` melakukan Confirm atas laporan `Office Chair Ergo - 21 {runId}`
44. Pelapor umum `Budi Santoso {runId}` melakukan Cancel Report atas `Office Chair Ergo - 21 {runId}` yang sudah diputuskan
45. Verifikasi Cancel Report ditolak dan record tetap `Damaged`
46. Verifikasi penolakan itu menyebut pelaku perubahan status terakhir `Rina Wulandari {runId}`
47. Pelapor umum `Budi Santoso {runId}` melakukan Cancel Report atas `Office Chair Ergo - 22 {runId}`
48. Pemegang Update `Rina Wulandari {runId}` melakukan Confirm atas laporan `Office Chair Ergo - 22 {runId}` yang sudah dibatalkan
49. Verifikasi Confirm ditolak karena status record sudah berubah dan record tetap `Canceled`
50. Verifikasi penolakan itu menyebut pelaku perubahan status terakhir `Budi Santoso {runId}`

### Konflik antar aksi tulis lain atas record yang sama
51. Total Control `Agus Pratama {runId}` mengirim Report Damaged atas `Toyota Avanza - 6 {runId}` dan, bersamaan, `Rina Wulandari {runId}` mengirim Report Damaged atas aset yang sama, masing-masing dengan What happened `Casing retak setelah terbentur {runId}` dan Damaged Photo `casing-retak.jpg`
52. Verifikasi `Toyota Avanza - 6 {runId}` memiliki tepat satu record berjalan dan permintaan yang kalah ditolak
53. Total Control `Agus Pratama {runId}` menjalankan Mark as Repaired atas `Projector Epson EB-X06 - 6 {runId}` dengan Scan TAG milik aset dan Repair note `Komponen rusak sudah diganti {runId}` dan, bersamaan, `Rina Wulandari {runId}` menjalankan Report Disposal atas aset yang sama
54. Verifikasi record berakhir tepat di salah satu `Repaired` atau `Reported Disposal`, dan permintaan yang kalah ditolak karena status record sudah berubah
55. Pemegang Update `Rina Wulandari {runId}` menjalankan Report Disposal atas `Projector Epson EB-X06 - 7 {runId}`
56. Total Control `Agus Pratama {runId}` menjalankan Mark as Repaired atas `Projector Epson EB-X06 - 7 {runId}` yang sudah berstatus `Reported Disposal` dengan Scan TAG milik aset dan Repair note `Komponen rusak sudah diganti {runId}`
57. Verifikasi Mark as Repaired ditolak karena status record sudah berubah dan record tetap `Reported Disposal`
58. Total Control `Agus Pratama {runId}` menjalankan Cancel Disposal Report atas `Monitor Dell P2422H - 10 {runId}` dan, bersamaan, Aktor pelepasan aset `Maya Puspita {runId}` menjalankan Dispose dan Submit Request atas laporan yang sama
59. Verifikasi record berakhir tepat di salah satu `Damaged` atau `In Disposal Process`, dan permintaan yang kalah ditolak karena status record sudah berubah
60. Total Control `Agus Pratama {runId}` menjalankan Cancel Disposal Report atas `Drill Bosch GSB - 8 {runId}` yang status terakhirnya diubah `System`
61. Verifikasi Cancel Disposal Report ditolak dan penolakan itu menyebut pelaku perubahan status terakhir `System`
62. Total Control `Agus Pratama {runId}` mengirim Bulk Report Disposal atas `Laptop Dell Latitude 5420 - 12 {runId}` dan `Laptop Dell Latitude 5420 - 13 {runId}` setelah `Rina Wulandari {runId}` menjalankan Mark as Repaired atas `Laptop Dell Latitude 5420 - 12 {runId}`
63. Verifikasi record yang sudah `Repaired` dilewati dan hanya `Laptop Dell Latitude 5420 - 13 {runId}` yang diproses Bulk Report
64. Total Control `Agus Pratama {runId}` mengirim Bulk Report Disposal atas `Laptop Dell Latitude 5420 - 14 {runId}` dan `Laptop Dell Latitude 5420 - 15 {runId}` setelah keduanya dijalankan Mark as Repaired oleh `Rina Wulandari {runId}`
65. Verifikasi tidak ada Disposal Report yang dibuat dan kedua record tetap `Repaired`

### Record Repaired, Rejected, atau Canceled tidak dibuka ulang dan kerusakan baru mendapat record baru
66. Pemegang Update `Rina Wulandari {runId}` melakukan Confirm atas `Printer HP LaserJet M404 - 4 {runId}` yang sudah `Rejected`
67. Verifikasi Confirm ditolak dan record tetap `Rejected`
68. Total Control `Agus Pratama {runId}` menjalankan Mark as Repaired atas `Monitor Dell P2422H - 11 {runId}` yang sudah `Repaired`
69. Verifikasi Mark as Repaired ditolak dan record tetap `Repaired`
70. Total Control `Agus Pratama {runId}` mengirim Report Damaged atas `Printer HP LaserJet M404 - 4 {runId}` dengan What happened `Casing retak setelah terbentur {runId}` dan Damaged Photo `casing-retak.jpg`
71. Verifikasi server membuat record baru berstatus `Damaged` untuk aset itu, sedangkan record `Rejected` sebelumnya tidak berubah

### Tanpa batas tunggu: Waiting for Confirmation tidak dibatalkan otomatis
72. Catat jumlah notifikasi dan jumlah node Damage Log `Printer HP LaserJet M404 - 5 {runId}` yang record `Waiting for Confirmation`-nya sudah berumur `T0 − 90 hari, pukul 08:15`
73. Verifikasi record itu tetap `Waiting for Confirmation` tanpa pembatalan otomatis
74. Verifikasi jumlah notifikasi dan jumlah node Damage Log tidak berubah dari yang dicatat
75. User `Hana Lestari {runId}`, pelapor record itu, dinonaktifkan
76. Verifikasi record itu tetap `Waiting for Confirmation` dan tidak dibatalkan karena pelapornya nonaktif

### Aktor peminjaman memutuskan lebih dulu: Aktor Damaged tidak dapat memutuskan ulang
77. Aktor peminjaman `Yoga Tanuwijaya {runId}` menyelesaikan Return `Forklift Toyota 8FD - 6 {runId}` dengan Assess Damage Confirm atas laporan pemegang
78. Pemegang Update `Rina Wulandari {runId}` melakukan Reject atas laporan `Forklift Toyota 8FD - 6 {runId}` dengan Reason `Foto yang dikirim bukan foto aset ini {runId}`
79. Verifikasi Reject ditolak karena status record sudah berubah dan record tetap `Damaged` dengan node `Report confirmed by` yang pelakunya Aktor peminjaman `Yoga Tanuwijaya {runId}`
80. Pemegang Update `Rina Wulandari {runId}` melakukan Confirm atas laporan `Forklift Toyota 8FD - 6 {runId}`
81. Verifikasi Confirm ditolak karena record bukan `Waiting for Confirmation` dan tidak ada node Damage Log baru

### Aktor peminjaman menolak laporan pemegang lewat Assess Damage
82. Aktor peminjaman `Yoga Tanuwijaya {runId}` menyelesaikan Return `Drill Bosch GSB - 9 {runId}` dengan Assess Damage Reject atas laporan pemegang dan Reason `Foto yang dikirim bukan foto aset ini {runId}`
83. Verifikasi record menjadi `Rejected` dengan node `Report rejected by` yang pelakunya Aktor peminjaman `Yoga Tanuwijaya {runId}`
84. Verifikasi event `damaged_review_resolved` dipicu oleh keputusan itu

