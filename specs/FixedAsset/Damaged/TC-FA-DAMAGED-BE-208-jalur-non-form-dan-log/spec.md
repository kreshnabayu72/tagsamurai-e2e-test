---
id: TC-FA-DAMAGED-BE-208-jalur-non-form-dan-log
title: "Server membuat record dan node dari jalur non-form (registrasi, Unassign bermarker Damaged, Task Detail Audit, Transfer receive, Mark as Found), menulis Damage Log, Transaction log, Transaction admin log, Activity Log, dan System Log per aksi, dan tidak mencatat pembukaan dialog maupun Download"
layer: be-e2e
priority: Critical
caseType: Positive
status: ready-for-automation
sourceRules: ["§Aturan Logika Modul#r49", "§Aturan Logika Modul#r50", "§Aturan Logika Modul#r51", "§Aturan Logika Modul#r82", "§Aturan Logika Modul#r83", "§Aturan Logika Modul#r84", "§Aturan Logika Modul#r85", "§Aturan Logika Modul#r86", "§Aturan Logika Modul#r87", "§9.2#b5", "§9.2#b6", "§9.2#b7", "§9.6#r9", "§9.6#p1", "§8#p1", "§8.1#p4", "§8.2#b1", "§8.2#b2", "§8.2#b3", "§8.3#r1", "§8.3#r2", "§8.3#r3", "§8.3#r4", "§8.3#r5", "§8.3#r6", "§8.3#p2", "§8.3#b1", "§8.3#b2", "§5#r7", EC-DMG-06, EC-DMG-28, EC-DMG-29, EC-DMG-31, EC-DMG-32, "§9.4.4#r4", "§9.4.4#r6", "§9.4.4#r9", "§9.4.4#r13", "§9.7#r3", "§9.7#r8", "§9.4.1#r15", "§8.1#r7", "§8.1#r8", "§8.1#r9", "§8.1#r10", "§8.1#r11", "§8.1#r12", "§8.1#r13", "§8.1#r14", "§8.1#r15", "§8.1#r16", "§8.2#p4", "§8.2#p5", "§8.2#p6", "§8.2#p7", "§8.2#p8", "§8.2#p9", "§8.2#p10", "§8.2#p14", "§8.2#p15", "§8.2#p16", "§8.2#p17", "§8.2#p18", "§8.2#p21", "§8.2#p22", "§8.2#p23", "§8.2#p24", "§8.2#p25", "§8.2#p26", "§2#b6", "§2.1#r5", "§3#p2", "§9.2#b4", "§Aturan Logika Modul#r52"]
smoke: []
dependsOn: []
owner: BE
trace:
  "§Aturan Logika Modul#r49": [56, 67, 69]
  "§Aturan Logika Modul#r50": [56, 59, 94]
  "§Aturan Logika Modul#r51": [75, 77]
  "§Aturan Logika Modul#r82": 47
  "§Aturan Logika Modul#r83": 48
  "§Aturan Logika Modul#r84": 47
  "§Aturan Logika Modul#r85": [49, 50]
  "§Aturan Logika Modul#r86": 51
  "§Aturan Logika Modul#r87": 52
  "§9.2#b5": 53
  "§9.2#b6": [49, 50]
  "§9.2#b7": [56, 59, 65]
  "§9.6#r9": 54
  "§9.6#p1": [65, 67, 139, 140, 142, 144]
  "§8#p1": 3
  "§8.1#p4": 91
  "§8.2#b1": [4, 14, 17, 24, 40, 54, 95, 96, 97, 98, 99, 100, 101, 102, 103]
  "§8.2#b2": [5, 104, 125]
  "§8.2#b3": [6, 21, 25, 27, 91]
  "§8.3#r1": 52
  "§8.3#r2": [3, 7, 57, 59, 67, 69, 92]
  "§8.3#r3": [75, 79, 81, 83]
  "§8.3#r4": [29, 32, 34, 39]
  "§8.3#r5": [42, 43]
  "§8.3#r6": [71, 73]
  "§8.3#p2": [75, 77]
  "§8.3#b1": [9, 10, 11]
  "§8.3#b2": [45, 92]
  "§5#r7": 6
  EC-DMG-06: 62
  EC-DMG-28: 47
  EC-DMG-29: 73
  EC-DMG-31: 51
  EC-DMG-32: [52, 53]
  "§9.4.4#r4": [62, 63]
  "§9.4.4#r6": [47, 48]
  "§9.4.4#r9": 51
  "§9.4.4#r13": [71, 72]
  "§9.7#r3": [56, 57, 59, 60]
  "§9.7#r8": 53
  "§9.4.1#r15": [39, 42, 53]
  "§8.1#r7": [3, 52, 87, 123]
  "§8.1#r8": [13, 16]
  "§8.1#r9": 19
  "§8.1#r10": 79
  "§8.1#r11": 81
  "§8.1#r12": [23, 27, 124]
  "§8.1#r13": [29, 89]
  "§8.1#r14": 32
  "§8.1#r15": [34, 37]
  "§8.1#r16": [39, 83]
  "§8.2#p4": [95, 96]
  "§8.2#p5": 97
  "§8.2#p6": 98
  "§8.2#p7": 99
  "§8.2#p8": 100
  "§8.2#p9": 101
  "§8.2#p10": [102, 112, 115, 119]
  "§8.2#p14": [105, 125]
  "§8.2#p15": [105, 126]
  "§8.2#p16": [105, 127]
  "§8.2#p17": [105, 128]
  "§8.2#p18": [105, 129, 131, 133, 134]
  "§8.2#p21": [109, 113, 117, 135]
  "§8.2#p22": [111, 115, 119]
  "§8.2#p23": 106
  "§8.2#p24": 107
  "§8.2#p25": 108
  "§8.2#p26": [5, 14, 20, 21, 24, 30, 35, 57, 59, 85, 109, 112, 113, 115, 119, 121, 136, 137]
  "§2#b6": [3, 59, 60, 69, 77, 121]
  "§2.1#r5": [111, 115, 119]
  "§3#p2": [3, 57, 59, 63, 69, 77]
  "§9.2#b4": [48, 56, 59, 67, 69, 77]
  "§Aturan Logika Modul#r52": [48, 56, 59, 67, 69, 77]
---

# Server membuat record dan node dari jalur non-form (registrasi, Unassign bermarker Damaged, Task Detail Audit, Transfer receive, Mark as Found), menulis Damage Log, Transaction log, Transaction admin log, Activity Log, dan System Log per aksi, dan tidak mencatat pembukaan dialog maupun Download

## Prerequisites
- Aktor:
  - Total Control `Agus Pratama {runId}`, Aktor Damaged dan pelaku Activate.
  - Pemegang Manage asset & TAG (Update) `Rina Wulandari {runId}`, Aktor Damaged.
  - Aktor peminjaman `Yoga Tanuwijaya {runId}`, Aktor penugasan `Dewi Anggraini {runId}`, Aktor pemindahan aset `Tono Riyadi {runId}`, Staff Auditor `Sinta Marlina {runId}` (pelapor dari Task Detail Audit), Staff Executor Maintenance Routine `Joko Prasetyo {runId}` (pelapor dari Task Maintenance), dan Aktor penemuan aset `Hendra Saputra {runId}`, masing-masing tanpa hak Update Manage asset & TAG.
  - Aktor pelepasan aset `Maya Puspita {runId}`, Asset Admin sub-tab Disposal.
  - Pelapor umum `Budi Santoso {runId}`, pemegang aset, tanpa role Damaged.
- Data:
  - DU-208-1: User `Agus Pratama {runId}`, Total Control, cakupan seluruh client.
  - DU-208-2: User `Rina Wulandari {runId}`, Manage asset & TAG (Update), cakupan Group `Head Office {runId}` beserta descendant.
  - DU-208-3: User `Yoga Tanuwijaya {runId}`, Aktor Borrow, cakupan Group `Head Office {runId}`.
  - DU-208-4: User `Dewi Anggraini {runId}`, Aktor Assignment, cakupan Group `Head Office {runId}`.
  - DU-208-5: User `Tono Riyadi {runId}`, Aktor Transfer, cakupan Group `Head Office {runId}` dan Group `Branch Surabaya {runId}`.
  - DU-208-6: User `Sinta Marlina {runId}`, Staff Auditor, pelapor dari Task Detail Audit, tanpa hak Aktor Damaged, cakupan Group `Head Office {runId}`.
  - DU-208-7: User `Hendra Saputra {runId}`, Aktor Missing, cakupan Group `Head Office {runId}`.
  - DU-208-8: User `Maya Puspita {runId}`, Asset Admin sub-tab Disposal, cakupan Group `Head Office {runId}`.
  - DU-208-9: User `Budi Santoso {runId}`, pelapor umum, pemegang aset, cakupan aset yang ia pegang.
  - DU-208-10: Group `Head Office {runId}`.
  - DU-208-11: Group `Branch Surabaya {runId}`.
  - DU-208-12: Entitas `Mitra Lain {runId}`, terpisah dari entitas suite.
  - DU-208-13: Aset `Laptop Dell Latitude 5420 - 111 {runId}`, Group `Head Office {runId}`, `Normal`, tanpa record berjalan.
  - DU-208-14: Aset `Laptop Dell Latitude 5420 - 112 {runId}`, Group `Head Office {runId}`, `Normal`, tanpa record berjalan.
  - DU-208-15: Aset `Laptop Dell Latitude 5420 - 113 {runId}`, Group `Head Office {runId}`, `Normal`, tanpa record berjalan.
  - DU-208-16: Aset `Toyota Avanza - 114 {runId}`, Group `Head Office {runId}`, punya record `Damaged`.
  - DU-208-17: Aset `Drill Bosch GSB - 115 {runId}`, Group `Head Office {runId}`, `Disposed`, tanpa record berjalan.
  - DU-208-18: Aset `Camera Canon EOS - 116 {runId}`, Group `Head Office {runId}`, tanpa catatan apa pun, tidak terlibat dalam aksi mana pun.
  - DU-208-19: Aset `Monitor Dell P2422H - 121 {runId}`, Group `Head Office {runId}`, punya record `Waiting for Confirmation` dari laporan `Budi Santoso {runId}`.
  - DU-208-20: Aset `Monitor Dell P2422H - 122 {runId}`, Group `Head Office {runId}`, punya record `Waiting for Confirmation` dari laporan `Budi Santoso {runId}`.
  - DU-208-21: Aset `Monitor Dell P2422H - 123 {runId}`, Group `Head Office {runId}`, punya record `Waiting for Confirmation` dari laporan `Budi Santoso {runId}`.
  - DU-208-22: Aset `Printer HP LaserJet M404 - 131 {runId}`, Group `Head Office {runId}`, punya record `Damaged`, ber-TAG `RFID-M131 {runId}`.
  - DU-208-23: Aset `Printer HP LaserJet M404 - 132 {runId}`, Group `Head Office {runId}`, punya record `Damaged`, ber-TAG `RFID-M132 {runId}` yang tidak terbaca.
  - DU-208-24: Aset `Scanner Fujitsu fi-7160 - 141 {runId}`, Group `Head Office {runId}`, punya record `Damaged`.
  - DU-208-25: Aset `Scanner Fujitsu fi-7160 - 142 {runId}`, Group `Head Office {runId}`, punya record `Reported Disposal`.
  - DU-208-26: Aset `Scanner Fujitsu fi-7160 - 143 {runId}`, Group `Head Office {runId}`, punya record `Reported Disposal`.
  - DU-208-27: Aset `Scanner Fujitsu fi-7160 - 144 {runId}`, Group `Head Office {runId}`, punya record `In Disposal Process`, baris pelepasan aset dieksekusi.
  - DU-208-28: Aset `Scanner Fujitsu fi-7160 - 145 {runId}`, Group `Head Office {runId}`, punya record `In Disposal Process`, baris pelepasan aset kedaluwarsa.
  - DU-208-29: Aset `Printer HP LaserJet M404 - 191 {runId}`, Group `Head Office {runId}`, punya record `Damaged`.
  - DU-208-30: Aset `Printer HP LaserJet M404 - 192 {runId}`, Group `Head Office {runId}`, punya record `Damaged`.
  - DU-208-31: Aset `Printer HP LaserJet M404 - 193 {runId}`, Group `Head Office {runId}`, punya record `Damaged` yang kemudian menjadi `Repaired` sebelum Submit.
  - DU-208-32: Aset `Projector Epson EB-X06 - 151 {runId}`, Group `Head Office {runId}`, draf registrasi ber-Condition `Damaged`, belum Active.
  - DU-208-35: Aset `Tablet Samsung Tab A8 - 161 {runId}`, Group `Head Office {runId}`, `Borrowed` oleh `Budi Santoso {runId}`, tanpa record berjalan.
  - DU-208-36: Aset `Tablet Samsung Tab A8 - 162 {runId}`, Group `Head Office {runId}`, `Assigned` kepada `Budi Santoso {runId}`, tanpa record berjalan.
  - DU-208-37: Aset `Tablet Samsung Tab A8 - 163 {runId}`, Group `Head Office {runId}`, `Borrowed` oleh `Budi Santoso {runId}`, punya record `Waiting for Confirmation` dari laporan `Budi Santoso {runId}` dengan What happened `Engsel longgar {runId}`.
  - DU-208-38: Aset `Tablet Samsung Tab A8 - 164 {runId}`, Group `Head Office {runId}`, `Borrowed` oleh `Budi Santoso {runId}`, tanpa record berjalan, form Return belum lolos validasi.
  - DU-208-39: Aset `Forklift Toyota 8FD - 171 {runId}`, Group `Head Office {runId}`, item sesi Audit berjalan milik `Sinta Marlina {runId}`, tanpa record berjalan.
  - DU-208-40: Aset `Forklift Toyota 8FD - 172 {runId}`, Group `Head Office {runId}`, dalam pemindahan menuju `Branch Surabaya {runId}`, tanpa record berjalan.
  - DU-208-41: Aset `Forklift Toyota 8FD - 173 {runId}`, Group `Head Office {runId}`, dalam pemindahan menuju `Branch Surabaya {runId}`, punya record `Damaged` dengan What happened `Garpu bengkok {runId}` Source `Manual`.
  - DU-208-42: Aset `Camera Canon EOS - 181 {runId}`, Group `Head Office {runId}`, `Missing` dengan record `Damaged` ditahan dengan What happened `Lensa berjamur {runId}`.
  - DU-208-43: Aset `Camera Canon EOS - 182 {runId}`, Group `Head Office {runId}`, `Missing` tanpa record Damaged.
  - DU-208-44: Aset `Camera Canon EOS - 183 {runId}`, Group `Head Office {runId}`, `Damaged` tanpa laporan hilang sebelumnya, akan dilaporkan hilang.
  - DU-208-45: Aset `Camera Canon EOS - 184 {runId}`, Group `Head Office {runId}`, punya record `Damaged` ditahan dengan laporan hilang dari pemegang yang akan ditolak.
  - DU-208-46: Aset `Camera Canon EOS - 185 {runId}`, Group `Head Office {runId}`, `Missing` dengan record `Damaged` ditahan yang akan menjadi `Disposed`.
  - DU-208-47: Description `Engsel longgar saat dikembalikan {runId}`, foto Return `foto-return.jpg`.
  - DU-208-48: Description `Layar tergores saat dikembalikan {runId}`, foto Unassign `foto-unassign.jpg`.
  - DU-208-49: What happened `Rangka berkarat ditemukan saat audit {runId}`, Damaged Photo `rangka-berkarat.jpg`.
  - DU-208-50: What happened `Garpu bengkok saat diterima {runId}`, Damaged Photo `garpu-bengkok.jpg`.
  - DU-208-51: Note `Ditemukan rusak di ruang arsip {runId}`, Damaged Photo `ditemukan-rusak.jpg`.
  - DU-208-52: What happened `Layar retak setelah terjatuh dari meja {runId}`, Damaged Photo `layar-retak.jpg`.
  - DU-208-53: Reason `Foto yang dikirim bukan foto aset ini {runId}`.
  - DU-208-54: Repair note `Komponen rusak sudah diganti {runId}`.
  - DU-208-55: Reason `Unit sudah tidak ekonomis untuk diperbaiki {runId}`.
  - DU-208-56: Nama baru `Agus Pratama Putra {runId}` untuk `Agus Pratama {runId}`.
  - DU-208-57: Aset `Scanner Fujitsu fi-7160 - 146 {runId}`, Group `Head Office {runId}`, punya record `Reported Disposal`.
  - DU-208-58: Aset `Camera Canon EOS - 186 {runId}`, Group `Head Office {runId}`, punya record `Damaged`.
  - DU-208-59: What happened `Terakhir terlihat di gudang lantai dua {runId}`, Damaged Photo `terakhir-terlihat.jpg`.
  - DU-208-60: Aset `Tablet Samsung Tab A8 - 165 {runId}`, Group `Head Office {runId}`, `Assigned` kepada `Budi Santoso {runId}`, punya record `Waiting for Confirmation` dari laporan `Budi Santoso {runId}`.
  - DU-208-61: User `Joko Prasetyo {runId}`, Staff Executor Maintenance Routine, pelapor dari Task Maintenance, tanpa hak Aktor Damaged, cakupan Group `Head Office {runId}`.
  - DU-208-62: Aset `Generator Honda EU22i - 187 {runId}`, Group `Head Office {runId}`, punya Task Maintenance berjalan yang dikerjakan `Joko Prasetyo {runId}`, tanpa record berjalan.
  - DU-208-63: Aset `Monitor Dell P2422H - 124 {runId}`, Group `Head Office {runId}`, `Assigned` kepada `Rina Wulandari {runId}`, tanpa record berjalan.
  - DU-208-64: After photo `sesudah-perbaikan.jpg`.
  - DU-208-65: Group `Divisi IT {runId}`, anak dari Group `Head Office {runId}`, sehingga hierarki lengkapnya `Head Office {runId} > Divisi IT {runId}`.
  - DU-208-66: Aset `Laptop Dell Latitude 5420 - 195 {runId}`, Group `Divisi IT {runId}`, `Normal`, tanpa record berjalan.
  - DU-208-67: Aset `Tablet Samsung Tab A8 - 166 {runId}`, Group `Head Office {runId}`, `Assigned` kepada `Budi Santoso {runId}`, tanpa record berjalan, form Unassign belum lolos validasi.
  - DU-208-68: Aset `Camera Canon EOS - 187 {runId}`, Group `Head Office {runId}`, `Missing` tanpa record Damaged, form Mark as Found Damaged belum lolos validasi.
  - DU-208-69: Aset `Forklift Toyota 8FD - 174 {runId}`, Group `Head Office {runId}`, dalam pemindahan menuju `Branch Surabaya {runId}`, tanpa record berjalan, form penerimaan belum lolos validasi.
- Kondisi:
  - Approval registrasi aset bernilai `OFF`.
  - Date Format bernilai `dd/MM/yy`.
  - Time Format bernilai `24h`.

## Test Steps

### Report Damaged oleh Pelapor admin tercatat di Damage Log, Transaction log aset, dan Transaction admin log
1. Catat jumlah entri Activity Log dan System Log `Agus Pratama {runId}`, jumlah node Damage Log `Laptop Dell Latitude 5420 - 111 {runId}`, dan jumlah node Damage Log `Camera Canon EOS - 116 {runId}`
2. Total Control `Agus Pratama {runId}` mengirim Report Damaged atas `Laptop Dell Latitude 5420 - 111 {runId}` dengan What happened `Layar retak setelah terjatuh dari meja {runId}` dan Damaged Photo `layar-retak.jpg`
3. Verifikasi Damage Log record memuat satu node `Reported damaged by` dengan pelaku `Agus Pratama {runId}`, What happened `Layar retak setelah terjatuh dari meja {runId}`, dan Damaged Photo `layar-retak.jpg`
4. Verifikasi Transaction log aset memuat Reported damaged dari Report Damaged itu
5. Verifikasi Transaction admin log `Agus Pratama {runId}` sub-tab Damaged memuat Report Damaged itu dengan Activity `Reported damaged`, Name aset itu, Source yang sama dengan Source record itu, dan Group aset saat tindakan
6. Verifikasi Activity Log dan System Log `Agus Pratama {runId}` bertambah satu entri untuk aksi itu dalam transaksi yang sama
7. Verifikasi jumlah node Damage Log `Camera Canon EOS - 116 {runId}` yang tidak terlibat tetap sama dengan yang dicatat

### Report Damaged banyak aset menghasilkan satu node per aset yang diproses
8. Total Control `Agus Pratama {runId}` mengirim satu Report Damaged atas `Laptop Dell Latitude 5420 - 112 {runId}`, `Laptop Dell Latitude 5420 - 113 {runId}`, `Toyota Avanza - 114 {runId}`, dan `Drill Bosch GSB - 115 {runId}` dengan What happened `Layar retak setelah terjatuh dari meja {runId}` dan Damaged Photo `layar-retak.jpg`
9. Verifikasi masing-masing `Laptop Dell Latitude 5420 - 112 {runId}` dan `Laptop Dell Latitude 5420 - 113 {runId}` mendapat satu record dan satu node `Reported damaged by`
10. Verifikasi setiap node `Reported damaged by` tercatat di record aset itu sendiri dan bukan di record aset lain
11. Verifikasi `Toyota Avanza - 114 {runId}` yang sudah punya record berjalan dan `Drill Bosch GSB - 115 {runId}` yang Disposed dilewati tanpa node baru

### Confirm, Reject, dan Cancel Report tercatat menurut surface masing-masing
12. Pemegang Update `Rina Wulandari {runId}` melakukan Confirm atas laporan `Monitor Dell P2422H - 121 {runId}`
13. Verifikasi Damage Log record memuat node `Report confirmed by` dengan pelaku `Rina Wulandari {runId}`
14. Verifikasi Transaction log aset memuat Report confirmed dan Transaction admin log `Rina Wulandari {runId}` memuat Confirm itu
15. Pemegang Update `Rina Wulandari {runId}` melakukan Reject atas laporan `Monitor Dell P2422H - 122 {runId}` dengan Reason `Foto yang dikirim bukan foto aset ini {runId}`
16. Verifikasi Damage Log record memuat node `Report rejected by` dengan pelaku `Rina Wulandari {runId}` dan Reason `Foto yang dikirim bukan foto aset ini {runId}`
17. Verifikasi Transaction log aset memuat Report rejected
18. Pelapor umum `Budi Santoso {runId}` melakukan Cancel Report dari `My Asset` atas `Monitor Dell P2422H - 123 {runId}`
19. Verifikasi Damage Log record memuat node `Report canceled by` dengan pelaku `Budi Santoso {runId}`
20. Verifikasi pembatalan dari `My Asset` itu tidak tercatat di Transaction log aset maupun Transaction admin log
21. Verifikasi pembatalan itu tercatat di Activity Log dan System Log `Budi Santoso {runId}`

### Mark as Repaired tercatat dan TAG Log hanya untuk Report TAG
22. Pemegang Update `Rina Wulandari {runId}` menjalankan Mark as Repaired atas `Printer HP LaserJet M404 - 131 {runId}` dengan Scan TAG `RFID-M131 {runId}` milik aset dan Repair note `Komponen rusak sudah diganti {runId}`
23. Verifikasi Damage Log record memuat node `Marked as repaired by` dengan pelaku `Rina Wulandari {runId}` dan Repair note `Komponen rusak sudah diganti {runId}`
24. Verifikasi Transaction log aset memuat Repaired dan Transaction admin log `Rina Wulandari {runId}` memuat Mark as Repaired itu
25. Verifikasi tidak ada entri TAG Log baru dari Mark as Repaired dengan Scan TAG
26. Pemegang Update `Rina Wulandari {runId}` menjalankan Mark as Repaired atas `Printer HP LaserJet M404 - 132 {runId}` dengan identifikasi manual lewat Report TAG, Repair note `Komponen rusak sudah diganti {runId}`, dan After photo `sesudah-perbaikan.jpg`
27. Verifikasi node `Marked as repaired by` mencatat Manual identification dan TAG Log memuat entri Report TAG yang ditulis oleh modul TAG

### Report Disposal, Decline, dan Cancel Disposal Report tercatat sebagai node Damage Log
28. Total Control `Agus Pratama {runId}` menjalankan Report Disposal atas `Scanner Fujitsu fi-7160 - 141 {runId}` dengan Reason `Unit sudah tidak ekonomis untuk diperbaiki {runId}`
29. Verifikasi Damage Log record memuat node `Disposal reported by` dengan pelaku `Agus Pratama {runId}`, Report ID, dan Reason `Unit sudah tidak ekonomis untuk diperbaiki {runId}`
30. Verifikasi Report Disposal itu dicatat di sub-tab pelepasan aset, tidak diulang di Transaction admin log Damaged
31. Aktor pelepasan aset `Maya Puspita {runId}` menjalankan Decline atas laporan `Scanner Fujitsu fi-7160 - 142 {runId}` dengan Reason `Foto yang dikirim bukan foto aset ini {runId}`
32. Verifikasi Damage Log record memuat node `Disposal report declined by` dengan pelaku `Maya Puspita {runId}`, Report ID, Reason, dan Back to Damaged
33. Total Control `Agus Pratama {runId}` menjalankan Cancel Disposal Report atas `Scanner Fujitsu fi-7160 - 143 {runId}`
34. Verifikasi Damage Log record memuat node `Disposal report canceled by` dengan pelaku `Agus Pratama {runId}`, Report ID, dan Back to Damaged
35. Verifikasi Cancel Disposal Report itu dicatat di sub-tab pelepasan aset, tidak diulang di Transaction admin log Damaged
36. Total Control `Agus Pratama {runId}` menjalankan Report Missing atas `Scanner Fujitsu fi-7160 - 146 {runId}` yang record-nya `Reported Disposal` dari Asset List dengan What happened `Terakhir terlihat di gudang lantai dua {runId}` dan Damaged Photo `terakhir-terlihat.jpg`
37. Verifikasi Damage Log record memuat node `Disposal report canceled by` dengan pelaku `System`, Report ID, Reason `Asset reported missing`, dan Back to Damaged
38. Pelepasan aset `Scanner Fujitsu fi-7160 - 144 {runId}` dieksekusi (Executed)
39. Verifikasi Damage Log record memuat node `Disposed` dengan pelaku `System` dan Disposal No. milik baris pelepasan aset itu
40. Verifikasi Transaction log aset memuat Disposed dari pelepasan aset yang dieksekusi itu
41. Baris pelepasan aset `Scanner Fujitsu fi-7160 - 145 {runId}` kedaluwarsa (timeout) tanpa user aktor
42. Verifikasi node di Damage Log record dicatat dengan PIC `System`
43. Verifikasi Activity Log mencatat Modified By `System` dan tidak ada entri System Log untuk peristiwa itu
44. Total Control `Agus Pratama {runId}` mengirim Bulk Report Disposal atas `Printer HP LaserJet M404 - 191 {runId}`, `Printer HP LaserJet M404 - 192 {runId}`, dan `Printer HP LaserJet M404 - 193 {runId}` dengan satu Reason `Unit sudah tidak ekonomis untuk diperbaiki {runId}`, setelah `Printer HP LaserJet M404 - 193 {runId}` menjadi `Repaired`
45. Verifikasi masing-masing `Printer HP LaserJet M404 - 191 {runId}` dan `Printer HP LaserJet M404 - 192 {runId}` mendapat satu node `Disposal reported by` dengan Report ID sendiri, sedangkan `Printer HP LaserJet M404 - 193 {runId}` yang dilewati tidak mendapat node

### Registrasi aset ber-Condition Damaged membuat record otomatis
46. Total Control `Agus Pratama {runId}` mengaktifkan registrasi `Projector Epson EB-X06 - 151 {runId}` yang ber-Condition `Damaged` dengan Damage note sepanjang 120 karakter
47. Verifikasi server membuat satu record `Damaged` begitu aset menjadi Active, tanpa Confirm
48. Verifikasi Source record itu adalah `Registration`
49. Verifikasi What happened record sama dengan Damage note `Lensa tergores dan bodi penyok akibat benturan saat pengiriman dari gudang pusat ke kantor cabang Lensa tergores dan bod` (120 karakter) tanpa dipotong atau diganti default
50. Verifikasi What happened record tidak melebihi 360 karakter dan pembuatan record otomatis tidak gagal karena panjang What happened
51. Verifikasi record itu tidak memiliki Damaged Photo dan pembuatannya tidak mensyaratkan foto
52. Verifikasi node pertama `Reported damaged by` atas nama pelaku Activate `Agus Pratama {runId}`
53. Verifikasi record dibuat dalam transaksi aktivasi aset tanpa dialog Report Damaged dan tanpa notifikasi
54. Verifikasi Transaction log aset memuat Reported damaged dengan Source `Registration`, dan aktivasi yang dicoba ulang tidak membuat record kedua

### Report Damaged dari halaman Return Borrow dan Unassign bermarker Damaged membawa catatan dan foto, dan tidak menambah laporan bila record sudah ada
55. Aktor peminjaman `Yoga Tanuwijaya {runId}` mengirim Report Damaged dari halaman Return Borrow atas `Tablet Samsung Tab A8 - 161 {runId}` dengan Description `Engsel longgar saat dikembalikan {runId}` dan foto Return `foto-return.jpg`
56. Verifikasi server membuat record `Waiting for Confirmation`, karena Aktor peminjaman tanpa hak Aktor Damaged adalah pelapor umum, dengan Source `Borrow return`, What happened `Engsel longgar saat dikembalikan {runId}`, dan Damaged Photo `foto-return.jpg`
57. Verifikasi node `Reported damaged by` mencatat pelaku Aktor peminjaman `Yoga Tanuwijaya {runId}`, dan tidak ada event `damaged_*` karena notifikasi dimiliki modul asal; Transaction admin log `Yoga Tanuwijaya {runId}` sub-tab Damaged memuat baris Activity `Reported damaged` atas aset itu dengan Source `Borrow return` dan Group `Head Office {runId}` walau ia pelapor umum
58. Aktor penugasan `Dewi Anggraini {runId}` melakukan Unassign berstatus `Unassigned` bermarker `Damaged` atas `Tablet Samsung Tab A8 - 162 {runId}` dengan Description `Layar tergores saat dikembalikan {runId}` dan foto Unassign `foto-unassign.jpg`
59. Verifikasi server membuat record `Damaged` dengan Source `Assign return`, What happened `Layar tergores saat dikembalikan {runId}`, dan Damaged Photo `foto-unassign.jpg`; Transaction admin log `Dewi Anggraini {runId}` sub-tab Damaged memuat baris Activity `Reported damaged` atas aset itu dengan Source `Assign return`
60. Verifikasi status global aset menjadi `Damaged`
61. Aktor peminjaman `Yoga Tanuwijaya {runId}` menyelesaikan Return atas `Tablet Samsung Tab A8 - 163 {runId}` yang sudah punya record berjalan `Waiting for Confirmation`
62. Verifikasi Return tetap selesai tanpa menunggu keputusan, tanpa laporan baru, dan tanpa node baru dari Return di record berjalan yang tetap `Waiting for Confirmation`
63. Verifikasi tidak ada event `damaged_reported` maupun `damaged_review_requested` yang dipicu oleh Return itu
64. Aktor peminjaman `Yoga Tanuwijaya {runId}` mengirim Report Damaged dari halaman Return Borrow atas `Tablet Samsung Tab A8 - 164 {runId}` dengan Description tidak diisi
65. Verifikasi Report Damaged ditolak oleh form modul asal dan tidak ada record yang dibuat, karena record dibuat hanya bila form modul asal lolos validasi

### Task Detail Audit dan penerimaan pemindahan aset membawa bukti dari form modul asal
66. Staff Auditor `Sinta Marlina {runId}` mengirim Report Damaged dari Task Detail Audit atas `Forklift Toyota 8FD - 171 {runId}` dengan What happened `Rangka berkarat ditemukan saat audit {runId}` dan Damaged Photo `rangka-berkarat.jpg`
67. Verifikasi server membuat record `Waiting for Confirmation`, karena Staff Auditor tanpa hak Aktor Damaged adalah pelapor umum, dengan Source `Audit`, What happened `Rangka berkarat ditemukan saat audit {runId}`, Damaged Photo `rangka-berkarat.jpg`, dan node `Reported damaged by` atas nama `Sinta Marlina {runId}`
68. Aktor pemindahan aset `Tono Riyadi {runId}` menerima pemindahan `Forklift Toyota 8FD - 172 {runId}` dan melaporkan Damaged saat penerimaan dengan What happened `Garpu bengkok saat diterima {runId}` dan Damaged Photo `garpu-bengkok.jpg`
69. Verifikasi server membuat record `Damaged` dengan Source `Transfer receive`, What happened `Garpu bengkok saat diterima {runId}`, Damaged Photo `garpu-bengkok.jpg`, dan node `Reported damaged by` atas nama `Tono Riyadi {runId}`
70. Aktor pemindahan aset `Tono Riyadi {runId}` menerima pemindahan `Forklift Toyota 8FD - 173 {runId}` yang record `Damaged`-nya sudah ada
71. Verifikasi tidak ada node baru di Damage Log record dan Source tetap `Manual`
72. Verifikasi penerimaan pemindahan itu tidak memicu event `damaged_*`
73. Verifikasi Group record ikut Group aset tujuan `Branch Surabaya {runId}` tanpa mengubah riwayat Damage Log

### Mark as Found Damaged menambah node atau membuat record baru
74. Aktor penemuan aset `Hendra Saputra {runId}` menjalankan Mark as Found Damaged atas `Camera Canon EOS - 181 {runId}` dengan Note `Ditemukan rusak di ruang arsip {runId}` dan Damaged Photo `ditemukan-rusak.jpg`
75. Verifikasi Damage Log record yang ditahan bertambah node `Asset found` dengan pelaku `System`, Note, dan Damaged Photo dari dialog, tanpa node `Reported damaged by` dan tanpa menimpa What happened `Lensa berjamur {runId}`
76. Aktor penemuan aset `Hendra Saputra {runId}` menjalankan Mark as Found Damaged atas `Camera Canon EOS - 182 {runId}` dengan Note `Ditemukan rusak di ruang arsip {runId}` dan Damaged Photo `ditemukan-rusak.jpg`
77. Verifikasi server membuat record baru Source `Missing asset` dengan node `Reported damaged by` yang What happened-nya `Ditemukan rusak di ruang arsip {runId}` dan foto `ditemukan-rusak.jpg`

### Event modul aset hilang dicatat sebagai node System
78. Laporan hilang atas `Camera Canon EOS - 183 {runId}` dibuat oleh Aktor penemuan aset `Hendra Saputra {runId}`
79. Verifikasi Damage Log record memuat node `Asset reported missing` dengan pelaku `System`, sedangkan aktor sebenarnya tercatat di log modul aset hilang
80. Laporan hilang `Camera Canon EOS - 184 {runId}` dari pemegang ditolak (Reject) oleh Aktor penemuan aset `Hendra Saputra {runId}`
81. Verifikasi Damage Log record memuat node `Missing report closed` dengan pelaku `System`
82. Aset hilang `Camera Canon EOS - 185 {runId}` dilepas menjadi Disposed
83. Verifikasi Damage Log record memuat node `Disposed` dengan pelaku `System`
84. Total Control `Agus Pratama {runId}` menjalankan Report Missing atas `Camera Canon EOS - 186 {runId}` dari tab Damaged dengan What happened `Terakhir terlihat di gudang lantai dua {runId}` dan Damaged Photo `terakhir-terlihat.jpg`
85. Verifikasi Report Missing itu dicatat sekali oleh modul aset hilang dan Transaction admin log `Agus Pratama {runId}` tidak memuat entri Report Missing tambahan dari Damaged

### Urutan log: snapshot pelaku dan Modified By dari node terbaru
86. Total Control `Agus Pratama {runId}` diganti namanya menjadi `Agus Pratama Putra {runId}`
87. Verifikasi node `Reported damaged by` lama di record `Laptop Dell Latitude 5420 - 111 {runId}` tetap menyebut pelaku `Agus Pratama {runId}`
88. Pemegang Update `Rina Wulandari {runId}` menjalankan Report Disposal atas `Laptop Dell Latitude 5420 - 111 {runId}` dengan Reason `Unit sudah tidak ekonomis untuk diperbaiki {runId}`
89. Verifikasi Modified By record itu adalah `Rina Wulandari {runId}` karena node terbarunya dibuat pelaku yang berbeda

### Pembukaan dialog dan Download tidak dicatat, dan record tak terlibat tidak mendapat entri
90. Total Control `Agus Pratama {runId}` membuka Damage Log `Laptop Dell Latitude 5420 - 111 {runId}` dan mengunduh Download daftar record Active
91. Verifikasi jumlah entri Activity Log dan System Log `Agus Pratama {runId}` serta jumlah node Damage Log tidak bertambah dari pembukaan dialog dan Download itu
92. Verifikasi jumlah node Damage Log `Camera Canon EOS - 116 {runId}` yang tidak terlibat tetap sama, dan tidak ada entri milik entitas `Mitra Lain {runId}` yang ikut tercatat

### Unassign bermarker Damaged atas aset yang sudah punya record menautkan laporan tanpa Damage Report kedua
93. Aktor penugasan `Dewi Anggraini {runId}` melakukan Unassign berstatus `Unassigned` bermarker `Damaged` atas `Tablet Samsung Tab A8 - 165 {runId}` yang sudah punya record `Waiting for Confirmation` dengan Description `Layar tergores saat dikembalikan {runId}` dan foto Unassign `foto-unassign.jpg`
94. Verifikasi laporan yang sudah ada ditautkan dan Damaged Photo `foto-unassign.jpg` ditambahkan tanpa Damage Report kedua, sehingga aset itu tetap hanya memiliki satu record berjalan

### Transaction log aset membentuk satu baris per peristiwa dengan Status record setelah peristiwa
95. Verifikasi Transaction log aset `Laptop Dell Latitude 5420 - 112 {runId}` memuat baris dari Report Damaged oleh Pelapor admin dengan Status `Damaged` dan kolom User memuat pelapor record itu
96. Verifikasi Transaction log aset `Projector Epson EB-X06 - 151 {runId}` memuat baris Reported damaged Source `Registration` dengan Status `Damaged`
97. Verifikasi Transaction log aset `Tablet Samsung Tab A8 - 161 {runId}` memuat baris dari Report Damaged oleh pelapor umum `Yoga Tanuwijaya {runId}` dengan Status `Waiting for Confirmation` dan User `Yoga Tanuwijaya {runId}`
98. Verifikasi Transaction log aset `Monitor Dell P2422H - 121 {runId}` memuat baris Report confirmed dengan Status `Damaged`
99. Verifikasi Transaction log aset `Monitor Dell P2422H - 122 {runId}` memuat baris Report rejected dengan Status `Rejected`
100. Verifikasi Transaction log aset `Printer HP LaserJet M404 - 131 {runId}` memuat baris Repaired dengan Status `Repaired`
101. Verifikasi Transaction log aset `Scanner Fujitsu fi-7160 - 144 {runId}` memuat baris Disposed dengan Status `Disposed`
102. Verifikasi Transaction log aset `Camera Canon EOS - 183 {runId}`, `Camera Canon EOS - 184 {runId}`, `Camera Canon EOS - 181 {runId}`, `Scanner Fujitsu fi-7160 - 141 {runId}`, `Scanner Fujitsu fi-7160 - 142 {runId}`, dan `Scanner Fujitsu fi-7160 - 143 {runId}` tidak memuat baris dari peristiwa `Asset reported missing`, `Missing report closed`, `Asset found`, `Disposal reported`, `Disposal report declined`, maupun `Disposal report canceled`
103. Verifikasi kolom Transaction log aset `Monitor Dell P2422H - 121 {runId}` berurutan Date (format `General Settings`), Status, dan User (hover menampilkan nama lengkap), tanpa kolom Transaction ID, Reader name, Group, dan Requested by

### Transaction admin log memuat satu baris per tindakan per aset dengan kolom Date, Activity, Name, Source, dan Group
104. Verifikasi Transaction admin log `Agus Pratama Putra {runId}` sub-tab Damaged memuat satu baris Report Damaged atas `Laptop Dell Latitude 5420 - 112 {runId}` dan satu baris atas `Laptop Dell Latitude 5420 - 113 {runId}` dari aksi bulk itu, serta tidak ada baris atas `Toyota Avanza - 114 {runId}` dan `Drill Bosch GSB - 115 {runId}` yang dilewati
105. Verifikasi baris Report Damaged atas `Laptop Dell Latitude 5420 - 111 {runId}` di Transaction admin log `Agus Pratama Putra {runId}` memuat Date waktu tindakan itu dalam Date Format `dd/MM/yy` dan Time Format `24h`, Activity `Reported damaged` tanpa akhiran `by [Pelaku]`, Name `Laptop Dell Latitude 5420 - 111 {runId}`, Source yang sama dengan Source record itu, dan Group `Head Office {runId}`
106. Verifikasi Transaction admin log `Rina Wulandari {runId}` sub-tab Damaged memuat baris Activity `Report confirmed` atas `Monitor Dell P2422H - 121 {runId}`
107. Verifikasi Transaction admin log `Rina Wulandari {runId}` sub-tab Damaged memuat baris Activity `Report rejected` atas `Monitor Dell P2422H - 122 {runId}`
108. Verifikasi Transaction admin log `Rina Wulandari {runId}` sub-tab Damaged memuat baris Activity `Marked as repaired` atas `Printer HP LaserJet M404 - 131 {runId}`

### Report Damaged dan Cancel Report dari halaman transaksi, Task Detail Audit, dan Task Maintenance dicatat di Transaction admin log, sedangkan dari My Asset tidak
109. Verifikasi Transaction admin log `Yoga Tanuwijaya {runId}` memuat baris Activity `Reported damaged` atas `Tablet Samsung Tab A8 - 161 {runId}` dengan Source `Borrow return`, sedangkan sub-tab transaksi asalnya tidak memuat laporan itu
110. Aktor peminjaman `Yoga Tanuwijaya {runId}` melakukan Cancel Report dari halaman Return Borrow tempat ia melapor atas `Tablet Samsung Tab A8 - 161 {runId}`
111. Verifikasi Damage Log record memuat node `Report canceled by` dengan pelaku `Yoga Tanuwijaya {runId}` dan Transaction admin log `Yoga Tanuwijaya {runId}` memuat baris Activity `Report canceled` atas aset itu dengan Source `Borrow return`
112. Verifikasi pembatalan itu tidak membentuk baris di Transaction log aset `Tablet Samsung Tab A8 - 161 {runId}`
113. Verifikasi Transaction admin log `Sinta Marlina {runId}` memuat baris Activity `Reported damaged` atas `Forklift Toyota 8FD - 171 {runId}` dengan Source `Audit`, walau ia pelapor umum
114. Staff Auditor `Sinta Marlina {runId}` menjalankan `Cancel my report` di Task Detail Audit atas laporannya sendiri `Forklift Toyota 8FD - 171 {runId}`
115. Verifikasi Damage Log record memuat node `Report canceled by` dengan pelaku `Sinta Marlina {runId}`, Transaction admin log `Sinta Marlina {runId}` memuat baris Activity `Report canceled` atas aset itu dengan Source `Audit`, dan Transaction log aset tidak memuat baris dari pembatalan itu
116. Staff Executor `Joko Prasetyo {runId}` mengirim Report Damaged atas `Generator Honda EU22i - 187 {runId}` dari Task Maintenance dengan What happened `Layar retak setelah terjatuh dari meja {runId}` dan Damaged Photo `layar-retak.jpg`
117. Verifikasi server membuat record `Waiting for Confirmation` dengan Source `Maintenance`, karena Staff Executor tanpa hak Aktor Damaged adalah pelapor umum, dan Transaction admin log `Joko Prasetyo {runId}` memuat baris Activity `Reported damaged` atas aset itu dengan Source `Maintenance`
118. Staff Executor `Joko Prasetyo {runId}` menjalankan `Cancel my report` di Task Maintenance atas laporannya sendiri `Generator Honda EU22i - 187 {runId}`
119. Verifikasi Transaction admin log `Joko Prasetyo {runId}` memuat baris Activity `Report canceled` atas aset itu dengan Source `Maintenance`, sedangkan Transaction log aset tidak memuat baris dari pembatalan itu
120. Pemegang Update `Rina Wulandari {runId}` mengirim Report Damaged dari `My Asset` atas `Monitor Dell P2422H - 124 {runId}` yang ia pegang dengan What happened `Layar retak setelah terjatuh dari meja {runId}` dan Damaged Photo `layar-retak.jpg`
121. Verifikasi server membuat record `Damaged` karena `Rina Wulandari {runId}` adalah Pelapor admin, sedangkan Transaction admin log `Rina Wulandari {runId}` tidak memuat baris atas aset itu dan riwayat laporannya tercatat di User Log

### Damage Log tidak menampilkan foto yang dihapus dari File Manager
122. Total Control `Agus Pratama Putra {runId}` menghapus berkas Damaged Photo milik laporan `Laptop Dell Latitude 5420 - 112 {runId}` dan berkas After photo milik Mark as Repaired `Printer HP LaserJet M404 - 132 {runId}` dari `File Manager`
123. Verifikasi node `Reported damaged by` pada `Laptop Dell Latitude 5420 - 112 {runId}` tidak menampilkan Damaged Photo, sedangkan What happened tetap tampil dan node `Reported damaged by` pada `Laptop Dell Latitude 5420 - 113 {runId}` yang berkasnya tidak dihapus tetap menampilkan Damaged Photo `layar-retak.jpg`
124. Verifikasi node `Marked as repaired by` pada `Printer HP LaserJet M404 - 132 {runId}` tidak menampilkan After photo, sedangkan Repair note `Komponen rusak sudah diganti {runId}` dan Manual identification tetap tampil

### Kolom baris Transaction admin log mengikuti tindakan yang dicatat
125. Verifikasi kolom Date baris Report Damaged atas `Laptop Dell Latitude 5420 - 111 {runId}` di Transaction admin log `Agus Pratama Putra {runId}` memuat tanggal dan jam tindakan Report Damaged itu dalam Date Format `dd/MM/yy` dan Time Format `24h`
126. Verifikasi kolom Activity baris itu memuat nama node `Reported damaged` tanpa akhiran `by [Pelaku]`
127. Verifikasi kolom Name baris itu memuat aset yang terdampak dengan format `[Asset Name] - [Increment]`, yaitu `Laptop Dell Latitude 5420 - 111 {runId}`
128. Verifikasi kolom Source baris Reported damaged dan baris Report canceled atas `Tablet Samsung Tab A8 - 161 {runId}` sama-sama memuat Source record itu, yaitu `Borrow return`
129. Verifikasi kolom Group baris Report Damaged atas `Laptop Dell Latitude 5420 - 111 {runId}` memuat grup aset saat tindakan dieksekusi, yaitu `Head Office {runId}`

### Kolom Group baris Transaction admin log adalah snapshot grup aset saat tindakan dengan hierarki lengkap
130. Total Control `Agus Pratama Putra {runId}` mengirim Report Damaged atas `Laptop Dell Latitude 5420 - 195 {runId}` di Group `Divisi IT {runId}` dengan What happened `Layar retak setelah terjatuh dari meja {runId}` dan Damaged Photo `layar-retak.jpg`
131. Verifikasi kolom Group baris Report Damaged atas `Laptop Dell Latitude 5420 - 195 {runId}` di Transaction admin log `Agus Pratama Putra {runId}` memuat Group `Divisi IT {runId}` dengan hierarki lengkap `Head Office {runId} > Divisi IT {runId}`
132. Aktor pemindahan aset `Tono Riyadi {runId}` memindahkan `Laptop Dell Latitude 5420 - 195 {runId}` ke Group `Branch Surabaya {runId}` sampai pemindahan itu diterima
133. Verifikasi Group aset `Laptop Dell Latitude 5420 - 195 {runId}` sekarang `Branch Surabaya {runId}`
134. Verifikasi kolom Group baris Report Damaged yang sama di Transaction admin log `Agus Pratama Putra {runId}` tetap memuat Group `Divisi IT {runId}` dengan hierarki `Head Office {runId} > Divisi IT {runId}`, bukan `Branch Surabaya {runId}`

### Report Damaged saat penerimaan pemindahan dicatat di Transaction admin log pelapor
135. Verifikasi Transaction admin log `Tono Riyadi {runId}` memuat baris Activity `Reported damaged` atas `Forklift Toyota 8FD - 172 {runId}` dengan Source `Transfer receive`

### Laporan dari Task Detail Audit dan dari Unassign bermarker Damaged tidak tercatat di sub-tab transaksi asalnya
136. Verifikasi laporan atas `Forklift Toyota 8FD - 171 {runId}` yang dibuat dari Task Detail Audit tidak memiliki baris di sub-tab transaksi asalnya, dan asalnya terbaca dari Source `Audit` pada baris Transaction admin log `Sinta Marlina {runId}`
137. Verifikasi laporan atas `Tablet Samsung Tab A8 - 162 {runId}` yang dibuat dari Unassign bermarker `Damaged` tidak memiliki baris di sub-tab transaksi asalnya, dan asalnya terbaca dari Source `Assign return` pada baris Transaction admin log `Dewi Anggraini {runId}`

### Form modul asal yang tidak lolos tidak membuat record dari Unassign bermarker Damaged, Mark as Found Damaged, dan penerimaan pemindahan
138. Aktor penugasan `Dewi Anggraini {runId}` melakukan Unassign berstatus `Unassigned` bermarker `Damaged` atas `Tablet Samsung Tab A8 - 166 {runId}` dengan Description tidak diisi
139. Verifikasi Unassign itu ditolak oleh form modul asal dan `Tablet Samsung Tab A8 - 166 {runId}` tetap `Assigned` kepada `Budi Santoso {runId}`
140. Verifikasi tidak ada Damage record yang dibuat untuk `Tablet Samsung Tab A8 - 166 {runId}`
141. Aktor penemuan aset `Hendra Saputra {runId}` menjalankan Mark as Found Damaged atas `Camera Canon EOS - 187 {runId}` dengan Note tidak diisi dan Damaged Photo `ditemukan-rusak.jpg`
142. Verifikasi Mark as Found Damaged itu ditolak oleh form modul asal dan tidak ada Damage record yang dibuat untuk `Camera Canon EOS - 187 {runId}`
143. Aktor pemindahan aset `Tono Riyadi {runId}` menerima pemindahan `Forklift Toyota 8FD - 174 {runId}` dan melaporkan Damaged saat penerimaan dengan What happened tidak diisi dan Damaged Photo `garpu-bengkok.jpg`
144. Verifikasi penerimaan itu ditolak oleh form modul asal dan tidak ada Damage record yang dibuat untuk `Forklift Toyota 8FD - 174 {runId}`
