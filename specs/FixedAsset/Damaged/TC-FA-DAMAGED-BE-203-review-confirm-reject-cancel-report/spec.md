---
id: TC-FA-DAMAGED-BE-203-review-confirm-reject-cancel-report
title: "Server memproses Confirm, Reject, dan Cancel Report: Aktor Damaged memutuskan laporan mana pun termasuk laporannya sendiri, status akhir, record selesai tidak dibuka ulang, tanpa batas tunggu, dan konflik status"
layer: be-e2e
priority: Critical
caseType: Negative
status: ready-for-automation
sourceRules: ["§Aturan Logika Modul#r19", "§Aturan Logika Modul#r23", "§Aturan Logika Modul#r24", "§Aturan Logika Modul#r53", "§Aturan Logika Modul#r54", "§Aturan Logika Modul#r55", "§Aturan Logika Modul#r56", "§Aturan Logika Modul#r57", "§Aturan Logika Modul#r37", "§Aturan Logika Modul#r66", "§Aturan Logika Modul#r67", "§Aturan Logika Modul#r89", "§9.2#r1", "§9.2#r7", "§9.2#r8", "§9.4.3#b4", "§9.4.3#b5", "§9.6#r2", "§9.6#r3", "§9.6#r4", "§4.2.4#p6", V-DMG-07, D-DMG-06, EC-DMG-07, EC-DMG-08, EC-DMG-23, "§9.4.4#r18", "§9.4.4#r19", "§9.4.1#r11", FLD-DMG-06, "§2.1#b8", "§3#p4", EB-FRM-4@reason, EB-ERR-4, EB-CON-3, EB-EDG-1, F-DMG-04, "§9.4.2#r40", "§9.4.2#r41", "§2.1#r5", "§4.2.4#r15", "§4.2.4#r16", "§4.2.4#r17", "§8.2#p22", "§4.2.4#r13", "§9.2#r2"]
smoke: []
dependsOn: []
owner: BE
trace:
  "§Aturan Logika Modul#r19": 2
  "§Aturan Logika Modul#r23": 11
  "§Aturan Logika Modul#r24": 15
  "§Aturan Logika Modul#r53": 2
  "§Aturan Logika Modul#r54": 11
  "§Aturan Logika Modul#r55": [15, 22, 73, 75, 79, 83, 87, 93, 95, 97, 104, 106, 108, 111]
  "§Aturan Logika Modul#r56": [67, 68, 69]
  "§Aturan Logika Modul#r57": [31, 33]
  "§Aturan Logika Modul#r37": 20
  "§Aturan Logika Modul#r66": [61, 63]
  "§Aturan Logika Modul#r67": [65, 77]
  "§Aturan Logika Modul#r89": [24, 26]
  "§9.2#r1": 2
  "§9.2#r7": 11
  "§9.2#r8": 15
  "§9.4.3#b4": [61, 63]
  "§9.4.3#b5": [67, 71]
  "§9.6#r2": [3, 4, 5]
  "§9.6#r3": [12, 13]
  "§9.6#r4": [16, 17, 80, 81, 84, 85, 89, 90, 100, 101]
  "§4.2.4#p6": [40, 44, 55]
  V-DMG-07: [36, 39, 43, 48, 51, 53, 55, 57]
  D-DMG-06: [40, 44, 55]
  EC-DMG-07: [35, 36, 39, 43]
  EC-DMG-08: [24, 26, 27]
  EC-DMG-23: [67, 68, 69]
  "§9.4.4#r18": [35, 36, 39]
  "§9.4.4#r19": 68
  "§9.4.1#r11": 67
  FLD-DMG-06: [7, 9]
  "§2.1#b8": [24, 26, 29]
  "§3#p4": [15, 87, 97, 108, 111]
  EB-FRM-4@reason: [9, 11]
  EB-ERR-4: [7, 43, 51]
  EB-CON-3: [35, 46, 48, 53, 57, 59]
  EB-EDG-1: [51, 55, 59, 61]
  F-DMG-04: 2
  "§9.4.2#r40": [87, 88, 93, 95, 108, 109]
  "§9.4.2#r41": [97, 98, 99, 104, 106, 111, 112]
  "§2.1#r5": [15, 20, 73, 75, 87, 97, 108, 111]
  "§4.2.4#r15": [97, 98, 104, 111]
  "§4.2.4#r16": [7, 9, 11, 26]
  "§4.2.4#r17": [36, 39, 43, 93, 104]
  "§8.2#p22": [80, 84, 89, 100]
  "§4.2.4#r13": [15, 20]
  "§9.2#r2": 2
---

# Server memproses Confirm, Reject, dan Cancel Report: Aktor Damaged memutuskan laporan mana pun termasuk laporannya sendiri, status akhir, record selesai tidak dibuka ulang, tanpa batas tunggu, dan konflik status

## Prerequisites
- Aktor:
  - Total Control `Agus Pratama {runId}`, Aktor Damaged.
  - Pemegang Manage asset & TAG (Update) `Rina Wulandari {runId}`, Aktor Damaged pada Group `Head Office {runId}`.
  - Aktor peminjaman `Yoga Tanuwijaya {runId}` dan Aktor penugasan `Dewi Anggraini {runId}`, tanpa hak Update Manage asset & TAG.
  - Aktor pelepasan aset `Maya Puspita {runId}`, Asset Admin sub-tab Disposal.
  - Pelapor umum `Budi Santoso {runId}`, `Dedi Kurniawan {runId}`, `Sari Dewanti {runId}`, dan `Hana Lestari {runId}`, tanpa role Damaged kecuali disebut lain.
  - Staff Auditor `Lukman Hakim {runId}` dan Staff Executor Maintenance Routine `Wulan Anggraeni {runId}`, tanpa hak Aktor Damaged pada Group aset.
  - Asset Admin sub-tab Audit `Ratna Dewi {runId}` dan Asset Admin Maintenance Routine `Hendro Prasetyo {runId}`, tanpa hak Aktor Damaged pada Group aset.
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
  - DU-203-47: Aset `Camera Canon EOS - 5 {runId}`, Group `Head Office {runId}`, punya record `Waiting for Confirmation` dari laporan `Sari Dewanti {runId}`.
  - DU-203-48: Aset `Tablet Samsung Tab A8 - 8 {runId}`, Group `Head Office {runId}`, `Borrowed` oleh `Budi Santoso {runId}`, punya record `Waiting for Confirmation` dari laporan `Yoga Tanuwijaya {runId}` lewat halaman peminjaman.
  - DU-203-49: Aset `Camera Canon EOS - 6 {runId}`, Group `Head Office {runId}`, `Assigned` kepada `Budi Santoso {runId}`, punya record `Waiting for Confirmation` dari laporan `Dewi Anggraini {runId}` lewat halaman penugasan.
  - DU-203-50: Aset `Tablet Samsung Tab A8 - 9 {runId}`, Group `Head Office {runId}`, `Borrowed` oleh `Budi Santoso {runId}`, punya record `Waiting for Confirmation` dari laporan `Yoga Tanuwijaya {runId}` lewat halaman peminjaman.
  - DU-203-51: Aset `Camera Canon EOS - 8 {runId}`, Group `Head Office {runId}`, `Assigned` kepada `Budi Santoso {runId}`, punya record `Waiting for Confirmation` dari laporan `Dewi Anggraini {runId}` lewat halaman penugasan.
  - DU-203-52: User `Lukman Hakim {runId}`, Staff Auditor, tanpa hak Aktor Damaged pada Group aset, cakupan Group `Head Office {runId}`.
  - DU-203-53: User `Wulan Anggraeni {runId}`, Staff Executor Maintenance Routine, tanpa hak Aktor Damaged pada Group aset, cakupan Group `Head Office {runId}`.
  - DU-203-54: Aset `Laptop Dell Latitude 5420 - 17 {runId}`, Group `Head Office {runId}`, Condition `Normal`, punya record `Waiting for Confirmation` Source `Audit` dari laporan `Lukman Hakim {runId}` lewat Task Detail Audit.
  - DU-203-55: Aset `Laptop Dell Latitude 5420 - 18 {runId}`, Group `Head Office {runId}`, Condition `Normal`, punya record `Waiting for Confirmation` Source `Audit` dari laporan `Lukman Hakim {runId}` lewat Task Detail Audit.
  - DU-203-56: Aset `Rack Server Dell R740 - 7 {runId}`, Group `Head Office {runId}`, punya record `Damaged` Source `Audit` dari laporan `Agus Pratama {runId}` lewat Task Detail Audit.
  - DU-203-57: Aset `Generator Honda EU22i - 7 {runId}`, Group `Head Office {runId}`, Condition `Normal`, punya Task Maintenance berjalan dan record `Waiting for Confirmation` Source `Maintenance` dari laporan `Wulan Anggraeni {runId}` lewat Task Maintenance.
  - DU-203-58: Aset `Generator Honda EU22i - 8 {runId}`, Group `Head Office {runId}`, Condition `Normal`, punya Task Maintenance berjalan dan record `Waiting for Confirmation` Source `Maintenance` dari laporan `Wulan Anggraeni {runId}` lewat Task Maintenance.
  - DU-203-59: Aset `Generator Honda EU22i - 9 {runId}`, Group `Head Office {runId}`, punya Task Maintenance berjalan dan record `Damaged` Source `Maintenance` dari laporan `Rina Wulandari {runId}` lewat Task Maintenance.
  - DU-203-60: User `Ratna Dewi {runId}`, Asset Admin sub-tab Audit, tanpa hak Aktor Damaged pada Group aset, cakupan Group `Head Office {runId}`.
  - DU-203-61: User `Hendro Prasetyo {runId}`, Asset Admin Maintenance Routine, tanpa hak Aktor Damaged pada Group aset, cakupan Group `Head Office {runId}`.
  - DU-203-62: Aset `Rack Server Dell R740 - 8 {runId}`, Group `Head Office {runId}`, Condition `Normal`, punya record `Waiting for Confirmation` Source `Audit` dari laporan `Ratna Dewi {runId}` lewat Task Detail Audit.
  - DU-203-63: Aset `Generator Honda EU22i - 10 {runId}`, Group `Head Office {runId}`, Condition `Normal`, punya Task Maintenance berjalan dan record `Waiting for Confirmation` Source `Maintenance` dari laporan `Hendro Prasetyo {runId}` lewat Task Maintenance.

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

### Aktor Damaged dapat Confirm atau Reject laporannya sendiri, sedangkan record Damaged dari Pelapor admin tidak punya Review
23. `Sari Dewanti {runId}`, yang kini memiliki hak Aktor Damaged, melakukan Confirm atas laporannya sendiri `Camera Canon EOS - 4 {runId}` yang ia buat sebelum memiliki hak itu
24. Verifikasi Confirm diterima seperti laporan lain dan record berubah dari `Waiting for Confirmation` menjadi `Damaged`
25. `Sari Dewanti {runId}`, yang kini memiliki hak Aktor Damaged, melakukan Reject atas laporannya sendiri `Camera Canon EOS - 5 {runId}` dengan Reason `Foto yang dikirim bukan foto aset ini {runId}`
26. Verifikasi Reject diterima seperti laporan lain dan record menjadi `Rejected`
27. Verifikasi Damage Log record `Camera Canon EOS - 5 {runId}` memuat node `Report rejected by` dengan pelaku `Sari Dewanti {runId}`
28. Pemegang Update `Rina Wulandari {runId}` melakukan Confirm atas `Toyota Avanza - 5 {runId}` yang record `Damaged`-nya berasal dari laporan Pelapor admin
29. Verifikasi Confirm tidak berlaku dan ditolak karena record `Damaged` dari Pelapor admin tidak punya aksi Review dan bukan `Waiting for Confirmation`

### Aktor penugasan: Unassign tidak menunggu keputusan laporan dan keputusan tetap pada Aktor Damaged
30. Aktor penugasan `Dewi Anggraini {runId}` melakukan Unassign atas `Handheld Scanner Zebra TC21 - 4 {runId}` selagi record laporan masih `Waiting for Confirmation`
31. Verifikasi Unassign selesai tanpa menunggu keputusan dan record tetap `Waiting for Confirmation`
32. Pemegang Update `Rina Wulandari {runId}` melakukan Confirm atas laporan `Handheld Scanner Zebra TC21 - 4 {runId}`
33. Verifikasi keputusan atas laporan tetap ada pada Aktor Damaged, record menjadi `Damaged`, dan marker `Damaged` pada baris `Unassigned` mengikuti hasil itu

### Confirm dan Cancel Report atas laporan yang sama: yang memutuskan lebih dulu berlaku
34. Pemegang Update `Rina Wulandari {runId}` melakukan Confirm atas `Office Chair Ergo - 20 {runId}` dan, bersamaan, `Budi Santoso {runId}` melakukan Cancel Report atas laporan yang sama
35. Verifikasi record berakhir tepat di salah satu `Damaged` atau `Canceled`, apa pun urutan tiba kedua permintaan
36. Verifikasi hanya satu node `Report confirmed by` atau `Report canceled by` yang tercatat, dan permintaan yang kalah ditolak karena status record sudah berubah
37. Pemegang Update `Rina Wulandari {runId}` melakukan Confirm atas laporan `Office Chair Ergo - 21 {runId}`
38. Pelapor umum `Budi Santoso {runId}` melakukan Cancel Report atas `Office Chair Ergo - 21 {runId}` yang sudah diputuskan
39. Verifikasi Cancel Report ditolak dan record tetap `Damaged`
40. Verifikasi penolakan itu menyebut pelaku perubahan status terakhir `Rina Wulandari {runId}`
41. Pelapor umum `Budi Santoso {runId}` melakukan Cancel Report atas `Office Chair Ergo - 22 {runId}`
42. Pemegang Update `Rina Wulandari {runId}` melakukan Confirm atas laporan `Office Chair Ergo - 22 {runId}` yang sudah dibatalkan
43. Verifikasi Confirm ditolak karena status record sudah berubah dan record tetap `Canceled`
44. Verifikasi penolakan itu menyebut pelaku perubahan status terakhir `Budi Santoso {runId}`

### Konflik antar aksi tulis lain atas record yang sama
45. Total Control `Agus Pratama {runId}` mengirim Report Damaged atas `Toyota Avanza - 6 {runId}` dan, bersamaan, `Rina Wulandari {runId}` mengirim Report Damaged atas aset yang sama, masing-masing dengan What happened `Casing retak setelah terbentur {runId}` dan Damaged Photo `casing-retak.jpg`
46. Verifikasi `Toyota Avanza - 6 {runId}` memiliki tepat satu record berjalan dan permintaan yang kalah ditolak
47. Total Control `Agus Pratama {runId}` menjalankan Mark as Repaired atas `Projector Epson EB-X06 - 6 {runId}` dengan Scan TAG milik aset dan Repair note `Komponen rusak sudah diganti {runId}` dan, bersamaan, `Rina Wulandari {runId}` menjalankan Report Disposal atas aset yang sama
48. Verifikasi record berakhir tepat di salah satu `Repaired` atau `Reported Disposal`, dan permintaan yang kalah ditolak karena status record sudah berubah
49. Pemegang Update `Rina Wulandari {runId}` menjalankan Report Disposal atas `Projector Epson EB-X06 - 7 {runId}`
50. Total Control `Agus Pratama {runId}` menjalankan Mark as Repaired atas `Projector Epson EB-X06 - 7 {runId}` yang sudah berstatus `Reported Disposal` dengan Scan TAG milik aset dan Repair note `Komponen rusak sudah diganti {runId}`
51. Verifikasi Mark as Repaired ditolak karena status record sudah berubah dan record tetap `Reported Disposal`
52. Total Control `Agus Pratama {runId}` menjalankan Cancel Disposal Report atas `Monitor Dell P2422H - 10 {runId}` dan, bersamaan, Aktor pelepasan aset `Maya Puspita {runId}` menjalankan Dispose dan Submit Request atas laporan yang sama
53. Verifikasi record berakhir tepat di salah satu `Damaged` atau `In Disposal Process`, dan permintaan yang kalah ditolak karena status record sudah berubah
54. Total Control `Agus Pratama {runId}` menjalankan Cancel Disposal Report atas `Drill Bosch GSB - 8 {runId}` yang status terakhirnya diubah `System`
55. Verifikasi Cancel Disposal Report ditolak dan penolakan itu menyebut pelaku perubahan status terakhir `System`
56. Total Control `Agus Pratama {runId}` mengirim Bulk Report Disposal atas `Laptop Dell Latitude 5420 - 12 {runId}` dan `Laptop Dell Latitude 5420 - 13 {runId}` setelah `Rina Wulandari {runId}` menjalankan Mark as Repaired atas `Laptop Dell Latitude 5420 - 12 {runId}`
57. Verifikasi record yang sudah `Repaired` dilewati dan hanya `Laptop Dell Latitude 5420 - 13 {runId}` yang diproses Bulk Report
58. Total Control `Agus Pratama {runId}` mengirim Bulk Report Disposal atas `Laptop Dell Latitude 5420 - 14 {runId}` dan `Laptop Dell Latitude 5420 - 15 {runId}` setelah keduanya dijalankan Mark as Repaired oleh `Rina Wulandari {runId}`
59. Verifikasi tidak ada Disposal Report yang dibuat dan kedua record tetap `Repaired`

### Record Repaired, Rejected, atau Canceled tidak dibuka ulang dan kerusakan baru mendapat record baru
60. Pemegang Update `Rina Wulandari {runId}` melakukan Confirm atas `Printer HP LaserJet M404 - 4 {runId}` yang sudah `Rejected`
61. Verifikasi Confirm ditolak dan record tetap `Rejected`
62. Total Control `Agus Pratama {runId}` menjalankan Mark as Repaired atas `Monitor Dell P2422H - 11 {runId}` yang sudah `Repaired`
63. Verifikasi Mark as Repaired ditolak dan record tetap `Repaired`
64. Total Control `Agus Pratama {runId}` mengirim Report Damaged atas `Printer HP LaserJet M404 - 4 {runId}` dengan What happened `Casing retak setelah terbentur {runId}` dan Damaged Photo `casing-retak.jpg`
65. Verifikasi server membuat record baru berstatus `Damaged` untuk aset itu, sedangkan record `Rejected` sebelumnya tidak berubah

### Tanpa batas tunggu: Waiting for Confirmation tidak dibatalkan otomatis
66. Catat jumlah notifikasi yang diterima pelapor `Hana Lestari {runId}` dan Aktor Damaged `Agus Pratama {runId}`, jumlah node Damage Log, serta penanda yang dimiliki record dan aset `Printer HP LaserJet M404 - 5 {runId}` yang record `Waiting for Confirmation`-nya sudah berumur `T0 − 90 hari, pukul 08:15`
67. Verifikasi record itu tetap `Waiting for Confirmation` tanpa pembatalan otomatis
68. Verifikasi jumlah notifikasi yang diterima `Hana Lestari {runId}` dan `Agus Pratama {runId}` serta jumlah node Damage Log tidak berubah dari yang dicatat
69. Verifikasi record dan aset `Printer HP LaserJet M404 - 5 {runId}` tidak mendapat penanda tambahan dari yang dicatat, dan record tetap hanya berstatus `Waiting for Confirmation`
70. User `Hana Lestari {runId}`, pelapor record itu, dinonaktifkan
71. Verifikasi record itu tetap `Waiting for Confirmation` dan tidak dibatalkan karena pelapornya nonaktif

### Aktor Borrow dan Aktor Assignment membatalkan laporannya dari halaman transaksi tempat ia melapor
72. Aktor peminjaman `Yoga Tanuwijaya {runId}` melakukan Cancel Report atas laporannya `Tablet Samsung Tab A8 - 8 {runId}` dari halaman peminjaman tempat ia melapor
73. Verifikasi record berubah dari `Waiting for Confirmation` menjadi `Canceled` dengan node `Report canceled by` atas nama `Yoga Tanuwijaya {runId}`
74. Aktor penugasan `Dewi Anggraini {runId}` melakukan Cancel Report atas laporannya `Camera Canon EOS - 6 {runId}` dari halaman penugasan tempat ia melapor
75. Verifikasi record berubah dari `Waiting for Confirmation` menjadi `Canceled` dengan node `Report canceled by` atas nama `Dewi Anggraini {runId}`

### Kerusakan baru atas aset ber-record Canceled mendapat record baru
76. Total Control `Agus Pratama {runId}` mengirim Report Damaged atas `Office Chair Ergo - 22 {runId}` yang record sebelumnya sudah `Canceled` dengan What happened `Casing retak setelah terbentur {runId}` dan Damaged Photo `casing-retak.jpg`
77. Verifikasi server membuat record baru berstatus `Damaged` untuk aset itu, sedangkan record `Canceled` sebelumnya tidak berubah

### Cancel Report dari halaman Borrow dan Assignment dicatat di Transaction admin log pelapor dan tidak di Transaction log aset
78. Aktor peminjaman `Yoga Tanuwijaya {runId}` melakukan Cancel Report atas laporannya `Tablet Samsung Tab A8 - 9 {runId}` dari halaman peminjaman tempat ia melapor
79. Verifikasi record `Tablet Samsung Tab A8 - 9 {runId}` berubah dari `Waiting for Confirmation` menjadi `Canceled`
80. Verifikasi Transaction admin log `Yoga Tanuwijaya {runId}` memuat pembatalan atas `Tablet Samsung Tab A8 - 9 {runId}`
81. Verifikasi Transaction log aset `Tablet Samsung Tab A8 - 9 {runId}` tidak memuat pembatalan itu
82. Aktor penugasan `Dewi Anggraini {runId}` melakukan Cancel Report atas laporannya `Camera Canon EOS - 8 {runId}` dari halaman penugasan tempat ia melapor
83. Verifikasi record `Camera Canon EOS - 8 {runId}` berubah dari `Waiting for Confirmation` menjadi `Canceled`
84. Verifikasi Transaction admin log `Dewi Anggraini {runId}` memuat pembatalan atas `Camera Canon EOS - 8 {runId}`
85. Verifikasi Transaction log aset `Camera Canon EOS - 8 {runId}` tidak memuat pembatalan itu

### Pelapor Source Audit tanpa hak Aktor Damaged membatalkan laporannya lewat Cancel my report dari Task Detail Audit
86. Staff Auditor `Lukman Hakim {runId}` melakukan `Cancel my report` di Task Detail Audit atas laporannya `Laptop Dell Latitude 5420 - 17 {runId}`
87. Verifikasi record berubah dari `Waiting for Confirmation` menjadi `Canceled` dengan node `Report canceled by` atas nama `Lukman Hakim {runId}`
88. Verifikasi penanda `Damage reported` pada aset itu dihapus dan status global aset tidak berubah
89. Verifikasi Transaction admin log `Lukman Hakim {runId}` memuat pembatalan atas `Laptop Dell Latitude 5420 - 17 {runId}`
90. Verifikasi Transaction log aset `Laptop Dell Latitude 5420 - 17 {runId}` tidak memuat pembatalan itu
91. Total Control `Agus Pratama {runId}` melakukan Confirm atas laporan `Laptop Dell Latitude 5420 - 18 {runId}`
92. Staff Auditor `Lukman Hakim {runId}` melakukan `Cancel my report` di Task Detail Audit atas `Laptop Dell Latitude 5420 - 18 {runId}` yang sudah diputuskan
93. Verifikasi Cancel my report ditolak karena status record sudah berubah, record tetap `Damaged`, dan penolakan itu menyebut pelaku perubahan status terakhir `Agus Pratama {runId}`
94. Total Control `Agus Pratama {runId}` melakukan `Cancel my report` di Task Detail Audit atas laporannya sendiri `Rack Server Dell R740 - 7 {runId}` yang langsung berstatus `Damaged`
95. Verifikasi Cancel my report ditolak karena pelapor yang langsung `Damaged` tidak memiliki aksi itu dan record tetap `Damaged`

### Pelapor Source Maintenance tanpa hak Aktor Damaged membatalkan laporannya lewat Cancel my report dari Task Maintenance
96. Staff Executor `Wulan Anggraeni {runId}` melakukan `Cancel my report` di Task Maintenance atas laporannya `Generator Honda EU22i - 7 {runId}`
97. Verifikasi record berubah dari `Waiting for Confirmation` menjadi `Canceled` dengan node `Report canceled by` atas nama `Wulan Anggraeni {runId}`
98. Verifikasi penanda `Damage reported` pada task dan aset itu dihapus dan status global aset tidak berubah
99. Verifikasi status dan hasil task Maintenance `Generator Honda EU22i - 7 {runId}` tidak berubah oleh pembatalan
100. Verifikasi Transaction admin log `Wulan Anggraeni {runId}` memuat pembatalan atas `Generator Honda EU22i - 7 {runId}`
101. Verifikasi Transaction log aset `Generator Honda EU22i - 7 {runId}` tidak memuat pembatalan itu
102. Total Control `Agus Pratama {runId}` melakukan Confirm atas laporan `Generator Honda EU22i - 8 {runId}`
103. Staff Executor `Wulan Anggraeni {runId}` melakukan `Cancel my report` di Task Maintenance atas `Generator Honda EU22i - 8 {runId}` yang sudah diputuskan
104. Verifikasi Cancel my report ditolak karena status record sudah berubah, record tetap `Damaged`, dan penolakan itu menyebut pelaku perubahan status terakhir `Agus Pratama {runId}`
105. Pemegang Update `Rina Wulandari {runId}` melakukan `Cancel my report` di Task Maintenance atas laporannya sendiri `Generator Honda EU22i - 9 {runId}` yang langsung berstatus `Damaged`
106. Verifikasi Cancel my report ditolak karena pelapor yang langsung `Damaged` tidak memiliki aksi itu dan record tetap `Damaged`

### Asset Admin sub-tab Audit dan Asset Admin Maintenance Routine tanpa hak Aktor Damaged membatalkan laporannya lewat Cancel my report
107. Asset Admin `Ratna Dewi {runId}` melakukan `Cancel my report` di Task Detail Audit atas laporannya `Rack Server Dell R740 - 8 {runId}`
108. Verifikasi record berubah dari `Waiting for Confirmation` menjadi `Canceled` dengan node `Report canceled by` atas nama `Ratna Dewi {runId}`
109. Verifikasi penanda `Damage reported` pada aset itu dihapus dan status global aset tidak berubah
110. Asset Admin `Hendro Prasetyo {runId}` melakukan `Cancel my report` di Task Maintenance atas laporannya `Generator Honda EU22i - 10 {runId}`
111. Verifikasi record berubah dari `Waiting for Confirmation` menjadi `Canceled` dengan node `Report canceled by` atas nama `Hendro Prasetyo {runId}`
112. Verifikasi penanda `Damage reported` pada task dan aset itu dihapus dan status global aset tidak berubah
