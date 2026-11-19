---
id: TC-FA-BORROW-BE-087-log-transaksi-peristiwa
title: "Peristiwa dicatat sekali ke log transaksi dengan pelaku, detail, dan yang tidak dicatat"
layer: be-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["BORROW-LOGIC-17a", "BORROW-LOGIC-17b", "BORROW-LOGIC-17c", "BORROW-LOGIC-17d", "§8#r5", "§8#r6", "§8#r7", "§8.1#r6", "§8.1#r7", "§8.1#r8", "§8.1#r9", "§8.1#r10", "§8.1#r11", "§8.1#r12", "§8.1#r13", "§8.1#r14", "§8.1#r15", "§8.1#r16", "§8.1#r17", "§8.1#r18", "§8.1#r19", "§8.1#r20", "§8.1#r21", "§8.1#r22", "§8.1#r23", "§8.1#r24", "§8.1#r25", "§8.1#r26", "§8.1#r27", "§8.1#p4", "§8.3#b1", "§8.3#b2", "§8.3#b3", "§8.3#b4", "§8.3#p1", "§8.3#p2"]
smoke: []
dependsOn: []
owner: BE
trace:
  "BORROW-LOGIC-17a": 3
  "BORROW-LOGIC-17b": 29
  "BORROW-LOGIC-17c": 31
  "BORROW-LOGIC-17d": [8, 43, 145, 146]
  "§8#r5": 2
  "§8#r6": [43, 57]
  "§8#r7": [127, 128, 153, 156, 157, 159]
  "§8.1#r6": [4, 51, 137, 138]
  "§8.1#r7": [6, 7, 43, 141, 143, 144]
  "§8.1#r8": [52, 148]
  "§8.1#r9": [11, 12]
  "§8.1#r10": [16, 17, 49, 56, 172, 176, 178, 180]
  "§8.1#r11": [19, 20, 25, 27, 28, 280]
  "§8.1#r12": [41, 47, 185, 186]
  "§8.1#r13": [60, 61, 192, 201]
  "§8.1#r14": [63, 194]
  "§8.1#r15": [65, 66, 207, 212, 221]
  "§8.1#r16": [69, 218]
  "§8.1#r17": [72, 75, 196, 203, 264, 270, 276]
  "§8.1#r18": 83
  "§8.1#r19": [96, 240, 247]
  "§8.1#r20": [98, 99, 242, 249]
  "§8.1#r21": [93, 101]
  "§8.1#r22": [76, 87, 89, 255, 282, 288]
  "§8.1#r23": 121
  "§8.1#r24": [107, 226, 227, 234, 235]
  "§8.1#r25": [119, 120]
  "§8.1#r26": [109, 110]
  "§8.1#r27": [113, 229]
  "§8.1#p4": [21, 30, 38, 77, 124, 165, 168, 258]
  "§8.3#b1": [31, 32, 33]
  "§8.3#b2": [44, 53, 58, 84, 256]
  "§8.3#b3": 130
  "§8.3#b4": [34, 102]
  "§8.3#p1": [131, 132]
  "§8.3#p2": [132, 133, 134, 135]
---

# Peristiwa dicatat sekali ke log transaksi dengan pelaku, detail, dan yang tidak dicatat

## Prerequisites
- Aktor:
  - Asset Admin DU-087-25, Group penugasan Head Office (pengaju, pemberi, dan penerima).
  - Approver DU-087-30 dan Approver DU-087-31, keduanya Role Approver dengan Group penugasan Head Office. Approver pada langkah tanpa nama adalah DU-087-30, satu-satunya approver eligible untuk aset Head Office kecuali DU-087-6, DU-087-39, DU-087-40, dan DU-087-57.
  - Group Manager DU-087-32, Group Head Office (pembatal Cancel Borrow dan Cancel Extension, penerima approval dialihkan).
  - Asset Admin DU-087-33, Group penugasan Branch Surabaya.
  - Asset Admin DU-087-73, Group penugasan Head Office (pembatal Cancel Extension atas pengajuan Asset Admin DU-087-25).
  - Aktor Missing DU-087-68, Asset Admin dengan hak Aktor Missing pada Group Head Office. Asset Admin DU-087-25 tidak punya hak Aktor Missing.
  - Total Control, cakupan seluruh client (pengaju Cancel Borrow dan Cancel Extension, dan hanya menyimpan Draft C).
  - Borrower DU-087-14, Borrower DU-087-15 (PIC DU-087-34), dan Borrower DU-087-49.
- Data:
  - DU-087-1: Asset, aset untuk pengajuan, approval, handover, Extension, dan Return; Asset Name `Laptop Latitude 5440 {runId}`; Group `Head Office`.
  - DU-087-2: Asset, aset untuk pengajuan yang ditolak; Asset Name `Proyektor Epson EB-X49 {runId}`; Group `Head Office`.
  - DU-087-3: Asset, aset untuk handover yang dibatalkan Cancel Request; Asset Name `Kamera Canon EOS R10 {runId}`; Group `Head Office`.
  - DU-087-4: Asset, aset untuk handover dikonfirmasi PIC; Asset Name `Tablet Samsung Galaxy Tab S9 {runId}`; Group `Head Office`.
  - DU-087-5: Asset, aset dengan approval otomatis; Asset Name `Printer Canon G3010 {runId}`; Group `Head Office`.
  - DU-087-6: Asset, aset tanpa approver yang eligible; Asset Name `Monitor Dell P2422H {runId}`; Group `Head Office`.
  - DU-087-7: Asset, aset yang melewati Due date; Asset Name `Speaker JBL PartyBox 110 {runId}`; Group `Head Office`.
  - DU-087-8: Asset, aset untuk laporan Damaged dan TAG; Asset Name `Laptop ThinkPad E14 {runId}`; Group `Head Office`.
  - DU-087-9: Asset, aset untuk laporan Missing ditolak dan dibatalkan; Asset Name `Scanner Epson V39 {runId}`; Group `Head Office`.
  - DU-087-10: Asset, aset untuk laporan Missing dikonfirmasi; Asset Name `Printer Epson L3250 {runId}`; Group `Head Office`.
  - DU-087-12: Asset, aset untuk peminjaman mandiri; Asset Name `Kamera Sony ZV-E10 {runId}`; Group `Head Office`.
  - DU-087-13: Asset, aset untuk Cancel Borrow dengan Save as Draft to edit; Asset Name `Proyektor Optoma HD146X {runId}`; Group `Head Office`.
  - DU-087-14: User, Borrower yang punya akun login; Name `Rudi Hartono {runId}`.
  - DU-087-15: User, Borrower tanpa akun login dengan PIC; Name `Wahyu Setiawan {runId}`; PIC `Lina Susanti {runId}`.
  - DU-087-16: Parameter pengajuan, Duration dan Purpose setiap pengajuan; Duration `5 Day(s)`; Purpose `Presentasi klien {runId}`.
  - DU-087-17: Note approver, Note saat approver menyetujui; Note `Disetujui untuk presentasi klien {runId}`.
  - DU-087-18: Reason penolakan, Reason saat approver menolak aset; Reason `Proyektor dibutuhkan untuk acara internal {runId}`.
  - DU-087-19: Parameter Extension, Durasi Extension yang diajukan; Extend duration `2 Day(s)`.
  - DU-087-20: Reason penolakan Extension, Reason saat approver menolak Extension; Reason `Aset dijadwalkan untuk pemakaian lain {runId}`.
  - DU-087-22: Reason Missing, Reason laporan Missing dari Borrower; Reason `Aset tidak ditemukan di meja kerja sejak pagi {runId}`.
  - DU-087-23: Reason penolakan Missing, Reason saat Aktor Missing menolak laporan; Reason `Laporan belum dapat diverifikasi {runId}`.
  - DU-087-25: User, Asset Admin aktor spec ini, Group penugasan Head Office; Name `Bayu Nugroho {runId}`; Group `Head Office`; Role `Asset Admin`.
  - DU-087-26: Asset, aset Draft A; Asset Name `Laptop Asus Vivobook 14 {runId}`; Group `Head Office`.
  - DU-087-27: Asset, aset Draft B; Asset Name `Laptop Acer Aspire 5 {runId}`; Group `Head Office`.
  - DU-087-28: Asset, aset Draft C di Group Head Office; Asset Name `Monitor LG 24MP400 {runId}`; Group `Head Office`.
  - DU-087-29: Asset, aset Draft C di Group Branch Surabaya; Asset Name `Printer HP LaserJet M111w {runId}`; Group `Branch Surabaya`.
  - DU-087-30: User, Approver; Name `Dewi Lestari {runId}`; Group `Head Office`; Role `Approver`.
  - DU-087-31: User, Approver kedua; Name `Hendra Wijaya {runId}`; Group `Head Office`; Role `Approver`.
  - DU-087-32: User, Group Manager Head Office; Name `Siti Aminah {runId}`; Group `Head Office`; Role `Group Manager`.
  - DU-087-33: User, Asset Admin Branch Surabaya; Name `Agus Pratama {runId}`; Group `Branch Surabaya`; Role `Asset Admin`.
  - DU-087-34: User, PIC dengan akun login untuk Borrower DU-087-15; Name `Lina Susanti {runId}`; PIC untuk `Wahyu Setiawan {runId}`.
  - DU-087-35: Parameter pengajuan, Duration dan Purpose pengajuan yang memenuhi Auto-approve; Duration `3 Day(s)`; Purpose `Presentasi klien {runId}`.
  - DU-087-36: Parameter pengajuan, Duration, Purpose, dan Extend duration pengajuan singkat; Duration `2 Day(s)`; Purpose `Presentasi klien {runId}`; Extend duration `1 Day(s)`.
  - DU-087-37: Parameter Draft, Purpose baru Draft D; Purpose `Rapat vendor {runId}`.
  - DU-087-38: Parameter PIC, PIC baru Borrower DU-087-15; PIC `Rina Kusuma {runId}`.
  - DU-087-39: Asset, aset Approval type All; Asset Name `Laptop HP ProBook 450 {runId}`; Group `Head Office`.
  - DU-087-40: Asset, aset Approval type Any one dengan dua approver; Asset Name `Laptop Lenovo IdeaPad 3 {runId}`; Group `Head Office`.
  - DU-087-41: Asset, aset tanpa Require approval; Asset Name `Mouse Logitech M331 {runId}`; Group `Head Office`.
  - DU-087-42: Asset, aset tanpa approver eligible di Group tanpa Group Manager; Asset Name `Proyektor BenQ MH733 {runId}`; Group `Branch Surabaya`.
  - DU-087-43: Asset, aset BRW multi-baris yang dibatalkan; Asset Name `Kamera Fujifilm X-T30 {runId}`; Group `Head Office`.
  - DU-087-44: Asset, aset BRW multi-baris diserahkan dan dikembalikan; Asset Name `Tripod Manfrotto 190 {runId}`; Group `Head Office`.
  - DU-087-45: Asset, aset BRW multi-baris diserahkan dan dikembalikan; Asset Name `Lensa Sigma 30mm {runId}`; Group `Head Office`.
  - DU-087-46: Asset, aset BRW multi-baris diserahkan; Asset Name `Flash Godox TT685 {runId}`; Group `Head Office`.
  - DU-087-47: Asset, aset untuk pengingat Due date; Asset Name `Walkie Talkie Motorola T82 {runId}`; Group `Head Office`.
  - DU-087-48: Asset, aset Draft D; Asset Name `Monitor Samsung S24R350 {runId}`; Group `Head Office`.
  - DU-087-49: User, Borrower yang punya akun login dan akan dinonaktifkan; Name `Fajar Ramadhan {runId}`.
  - DU-087-50: Asset, aset untuk baris yang dibatalkan karena Borrower dinonaktifkan; Asset Name `Headset Jabra Evolve2 {runId}`; Group `Head Office`.
  - DU-087-51: Asset, aset Cancel Borrow oleh PIC; Asset Name `Kursi Ergonomis Ergotec {runId}`; Group `Head Office`.
  - DU-087-52: Asset, aset Cancel Borrow oleh Group Manager; Asset Name `Meja Lipat Informa {runId}`; Group `Head Office`.
  - DU-087-53: Asset, aset Cancel Borrow oleh Total Control; Asset Name `Papan Tulis Sakura 90x120 {runId}`; Group `Head Office`.
  - DU-087-54: Asset, aset handover yang dicentang Borrower; Asset Name `Laptop Dell Inspiron 14 {runId}`; Group `Head Office`.
  - DU-087-55: Asset, aset handover yang tidak dicentang; Asset Name `Mouse Wireless Logitech M185 {runId}`; Group `Head Office`.
  - DU-087-56: Asset, aset handover kedua yang tidak dicentang; Asset Name `Keyboard Logitech K380 {runId}`; Group `Head Office`.
  - DU-087-57: Asset, aset Approval type All untuk Extension oleh PIC; Asset Name `Genset Honda EU22i {runId}`; Group `Head Office`.
  - DU-087-58: Asset, aset Extension oleh Aktor Borrow; Asset Name `Bor Listrik Bosch GSB 550 {runId}`; Group `Head Office`.
  - DU-087-59: Asset, aset Auto-approve untuk Extension langsung; Asset Name `Speaker Aktif Yamaha HS5 {runId}`; Group `Head Office`.
  - DU-087-60: Asset, aset Auto-approve untuk Review Extension; Asset Name `Mikrofon Shure SM58 {runId}`; Group `Head Office`.
  - DU-087-61: Asset, aset Extension yang ditolak Aktor Borrow; Asset Name `Layar Proyektor Screenview {runId}`; Group `Head Office`.
  - DU-087-62: Asset, aset peminjaman mandiri dan Extension mandiri; Asset Name `Kamera GoPro Hero 11 {runId}`; Group `Head Office`.
  - DU-087-63: Asset, aset laporan Missing oleh PIC; Asset Name `Tablet Lenovo Tab M10 {runId}`; Group `Head Office`.
  - DU-087-64: Asset, aset laporan Missing oleh Aktor Borrow tanpa hak Aktor Missing; Asset Name `Smartphone Samsung A54 {runId}`; Group `Head Office`.
  - DU-087-65: Asset, aset laporan Damaged oleh PIC; Asset Name `Router Mikrotik hAP ax2 {runId}`; Group `Head Office`.
  - DU-087-66: Asset, aset laporan Damaged oleh Aktor Borrow; Asset Name `Switch TP-Link TL-SG108 {runId}`; Group `Head Office`.
  - DU-087-67: Asset, aset Return dengan Report Damaged; Asset Name `Laptop Acer Swift 3 {runId}`; Group `Head Office`.
  - DU-087-68: User, Aktor Missing di Group Head Office; Name `Maya Putri {runId}`; Group `Head Office`; Role `Asset Admin` dengan hak Aktor Missing.
  - DU-087-69: Laporan Damaged, What happened dan Photo; What happened `Casing retak di sudut atas {runId}`; Photo `kerusakan-casing-{runId}.jpg`.
  - DU-087-70: Asset, aset Extension yang dibatalkan Borrower sendiri; Asset Name `Handycam Sony FDR-AX43 {runId}`; Group `Head Office`.
  - DU-087-71: Asset, aset Extension yang dibatalkan PIC sendiri; Asset Name `Tablet Huawei MatePad 11 {runId}`; Group `Head Office`.
  - DU-087-72: Asset, aset Extension yang dibatalkan Asset Admin lain; Asset Name `Proyektor Acer X1128H {runId}`; Group `Head Office`.
  - DU-087-73: User, Asset Admin lain di Group penugasan Head Office; Name `Yudi Pranoto {runId}`; Group `Head Office`; Role `Asset Admin`.
  - DU-087-74: Asset, aset dengan foto serah terima dan foto return; Asset Name `Kamera Nikon Z50 {runId}`; Group `Head Office`.
  - DU-087-75: Asset, aset satuan Hours yang terlambat dikembalikan; Asset Name `Walkie Talkie Baofeng UV-5R {runId}`; Group `Head Office`.
  - DU-087-76: Foto serah terima dan return, Photo saat serah terima dan Photo saat return; Photo serah terima `foto-serah-terima-{runId}.jpg`; Photo return `foto-return-{runId}.jpg`.
  - DU-087-77: Parameter pengajuan jam, Duration dan Purpose pengajuan satuan Hours; Duration `2 Hour(s)`; Purpose `Presentasi klien {runId}`.
- Kondisi:
  - Setiap aset DU-087 Group Head Office berada di Group penugasan Asset Admin DU-087-25. Aset DU-087-42 berada di Group Branch Surabaya, Group penugasan Asset Admin DU-087-33.
  - Akun DU-087-30, DU-087-31, DU-087-32, DU-087-33, DU-087-34, DU-087-49, DU-087-68, dan DU-087-73 aktif, dan kredensialnya disediakan fase 2.
  - Aturan efektif aset DU-087-39 memuat Approval type `All approvers` dengan approver DU-087-30 dan DU-087-31. Aturan efektif aset DU-087-40 memuat `Any one approver` dengan approver DU-087-30 dan DU-087-31, dan aset DU-087-57 memuat `All approvers` dengan approver yang sama. Aturan efektif aset DU-087-41 memuat Require approval OFF.
  - Aturan efektif aset DU-087-59 dan DU-087-60 memuat `Auto-approve within 3 days`. Aset DU-087-12 dan DU-087-62 memuat Self service ON.
  - Group Branch Surabaya tidak punya Group Manager dan tidak ada approver yang eligible untuk aset DU-087-42.
  - Aturan efektif aset DU-087-5 memuat `Auto-approve within 3 days`.
  - Tidak ada approver yang eligible untuk aset DU-087-6.
  - Aturan efektif aset DU-087-74 memuat Photo at start ON dan Photo at end ON. Aturan efektif aset DU-087-75 memuat satuan Hours.
  - Draft A dan Draft B berisi aset di Group penugasan Asset Admin DU-087-25; Draft C juga berisi aset Group Branch Surabaya yang di luar cakupannya.

## Test Steps

### Pengajuan dicatat sekali dan terbaca lewat tiga tampilan
1. Asset Admin DU-087-25 mengajukan BRW untuk aset DU-087-1 atas nama Borrower DU-087-14 dengan Duration `5 Day(s)` dan Purpose `Presentasi klien {runId}`
2. Verifikasi peristiwa `Borrow requested by [Actor]` untuk aset DU-087-1 tercatat tepat satu entri dengan pelaku pengaju
3. Verifikasi catatan peristiwa itu terbaca di Borrow Log per aset dalam BRW, Transaction log aset, dan Transaction admin log dari satu sumber peristiwa
4. Verifikasi detail node memuat Duration `5 Day(s)`, Purpose `Presentasi klien {runId}`, dan Approval `Waiting 1 approver`

### Keputusan approver dicatat per aset
5. Approver menyetujui aset DU-087-1 dengan Note `Disetujui untuk presentasi klien {runId}`
6. Verifikasi node `Approved by [Approver]` untuk aset DU-087-1 tercatat dengan pelaku Approver yang menyetujui
7. Verifikasi detail node memuat Approved duration `5 Day(s)`, Mode `Any one`, dan Note `Disetujui untuk presentasi klien {runId}`
8. Verifikasi keputusan approver pada aset DU-087-1 mencatat mode, waktu, dan pelaku

### Penolakan mencatat Reason apa adanya
9. Asset Admin DU-087-25 mengajukan BRW untuk aset DU-087-2 atas nama Borrower DU-087-14 dengan Duration `5 Day(s)` dan Purpose `Presentasi klien {runId}`
10. Approver menolak aset DU-087-2 dengan Reason `Proyektor dibutuhkan untuk acara internal {runId}`
11. Verifikasi node `Rejected by [Approver]` untuk aset DU-087-2 tercatat dengan pelaku Approver yang menolak
12. Verifikasi detail Reason memuat `Proyektor dibutuhkan untuk acara internal {runId}` persis seperti diketik, tanpa diterjemahkan

### Cancel Borrow oleh Aktor Borrow dengan Save as Draft to edit
13. Asset Admin DU-087-25 mengajukan BRW untuk aset DU-087-13 atas nama Borrower DU-087-14 dengan Duration `5 Day(s)` dan Purpose `Presentasi klien {runId}`
14. Approver menyetujui aset DU-087-13
15. Asset Admin DU-087-25 membatalkan baris aset DU-087-13 lewat Cancel Borrow dengan opsi `Save as Draft to edit`
16. Verifikasi node `Canceled by [Actor]` untuk aset DU-087-13 tercatat dengan pelaku Asset Admin DU-087-25 dan baris detail `Saved as draft`
17. Verifikasi node `Canceled by [Actor]` itu tidak memuat Reason karena pelakunya bukan `System`

### Serah terima Aktor Borrow dengan Borrower yang punya akun
18. Asset Admin DU-087-25 menyerahkan aset DU-087-1 kepada Borrower DU-087-14 dengan Condition `Normal`
19. Verifikasi node `Handed over by [Giver]` untuk aset DU-087-1 tercatat dengan pelaku Asset Admin DU-087-25
20. Verifikasi detail node memuat Duration `5 Day(s)`, Due date, Condition `Normal`, dan Confirmation `Accepted`
21. Verifikasi Borrow Log aset DU-087-1 tidak memuat node `Confirmed`, `Verified`, maupun `Level n approved`

### Serah terima untuk Borrower tanpa akun dikonfirmasi PIC
22. Asset Admin DU-087-25 mengajukan BRW untuk aset DU-087-4 atas nama Borrower DU-087-15 dengan Duration `5 Day(s)` dan Purpose `Presentasi klien {runId}`
23. Approver menyetujui aset DU-087-4
24. Asset Admin DU-087-25 menyerahkan aset DU-087-4 kepada Borrower DU-087-15 dengan Condition `Normal`, PIC DU-087-15 mengonfirmasi atas nama Borrower
25. Verifikasi detail node `Handed over by [Giver]` untuk aset DU-087-4 memuat Confirmation `Confirmed by [Actor or PIC] on behalf of [Borrower]`

### Peminjaman mandiri Borrower dicatat tanpa jejak di log yang tidak dipakai
26. Borrower DU-087-14 meminjam aset DU-087-12 lewat self-service dengan Duration `5 Day(s)` dan Purpose `Presentasi klien {runId}`
27. Verifikasi node `Borrowed via self-service by [Borrower]` untuk aset DU-087-12 tercatat dengan pelaku Borrower DU-087-14
28. Verifikasi detail node memuat Confirmation `Confirmed (self)`
29. Verifikasi peristiwa itu terbaca di log pengguna Borrower DU-087-14
30. Verifikasi Transaction admin log tidak memuat baris atas tindakan Borrower DU-087-14 atas pinjamannya sendiri
31. Verifikasi Changelog tidak memuat entri peristiwa Borrow atas aset DU-087-12
32. Verifikasi System Log tidak memuat entri peristiwa Borrow atas aset DU-087-12
33. Verifikasi Activity Log tidak memuat entri peristiwa Borrow atas aset DU-087-12
34. Verifikasi TAG Log aset DU-087-12 tidak memuat entri dari Borrow

### Handover dibatalkan Aktor Borrow dan Remind Borrower tidak dicatat
35. Asset Admin DU-087-25 mengajukan BRW untuk aset DU-087-3 atas nama Borrower DU-087-14 dengan Duration `5 Day(s)` dan Purpose `Presentasi klien {runId}`
36. Approver menyetujui aset DU-087-3
37. Asset Admin DU-087-25 menjalankan Remind Borrower pada baris aset DU-087-3 yang berstatus Waiting for Handover
38. Verifikasi Borrow Log aset DU-087-3 tidak memuat node dari Remind Borrower
39. Asset Admin DU-087-25 memulai handover aset DU-087-3
40. Asset Admin DU-087-25 menjalankan `Cancel Request` atas handover aset DU-087-3
41. Verifikasi node `Handover not confirmed` untuk aset DU-087-3 tercatat dengan pelaku Asset Admin DU-087-25, baris detail Started by Asset Admin DU-087-25, dan baris tetap Waiting for Handover

### Approval otomatis dan jendela konfirmasi handover oleh System
42. Asset Admin DU-087-25 mengajukan BRW untuk aset DU-087-5 atas nama Borrower DU-087-14 dengan Duration `3 Day(s)` dan Purpose `Presentasi klien {runId}`
43. Verifikasi node `Auto-approved` untuk aset DU-087-5 tercatat dengan pelaku `System`, Rule `Auto-approve within 3 days` beserta versi setting, dan Approved duration `3 Day(s)`
44. Verifikasi peristiwa `Auto-approved` itu terbaca di log pengguna Borrower DU-087-14 dengan pelaku `System`
45. Asset Admin DU-087-25 memulai handover aset DU-087-5
46. Waktu berlalu sampai jendela konfirmasi handover berakhir
47. Verifikasi node `Handover not confirmed` untuk aset DU-087-5 tercatat dengan pelaku `System`, baris detail Started by Asset Admin DU-087-25, dan baris tetap Waiting for Handover
48. Waktu berlalu sampai batas pengambilan aset terlewati
49. Verifikasi node `Canceled by [Actor]` untuk aset DU-087-5 tercatat dengan pelaku `System` dan Reason `Not picked up`

### Approval dialihkan dan penutupan timeout oleh System
50. Asset Admin DU-087-25 mengajukan BRW untuk aset DU-087-6 atas nama Borrower DU-087-14 dengan Duration `5 Day(s)` dan Purpose `Presentasi klien {runId}`
51. Verifikasi detail Approval node `Borrow requested by [Actor]` untuk aset DU-087-6 memuat `Routed to: Group Manager (no eligible approver)`
52. Verifikasi node `Approval rerouted` untuk aset DU-087-6 tercatat dengan pelaku `System`, Routed to Group Manager, dan Reason `No eligible approver`
53. Verifikasi peristiwa approval dialihkan itu terbaca di log pengguna Borrower DU-087-14 dengan pelaku `System`
54. Waktu berlalu sampai batas Waiting for Approval terlewati
55. Job Transaction timeout berjalan
56. Verifikasi node `Canceled by [Actor]` untuk aset DU-087-6 tercatat dengan pelaku `System` dan Reason `Timed out (Waiting for Approval)`
57. Verifikasi peristiwa dari job tanpa user aktor memakai aktor `System` dan Action node katalog yang bersangkutan
58. Verifikasi peristiwa penutupan timeout itu terbaca di log pengguna Borrower DU-087-14 dengan pelaku `System`

### Extension diajukan, diteruskan, dan disetujui
59. Borrower DU-087-14 mengajukan Extend aset DU-087-1 dengan Extend duration `2 Day(s)`
60. Verifikasi node `Extension requested by [Actor]` untuk aset DU-087-1 tercatat dengan pelaku Borrower DU-087-14 dan Extend duration `2 Day(s)`
61. Verifikasi detail node itu memuat Proposed due date
62. Asset Admin DU-087-25 meneruskan permintaan Extension aset DU-087-1 ke approval
63. Verifikasi node `Extension forwarded to approval by [Actor]` untuk aset DU-087-1 tercatat dengan pelaku Asset Admin DU-087-25 dan Approval `Waiting 1 approver`
64. Approver menyetujui Extension aset DU-087-1
65. Verifikasi node `Extension approved by [Approver]` untuk aset DU-087-1 tercatat dengan pelaku Approver yang menyetujui
66. Verifikasi detail node memuat Due date lama dan baru serta Extension dengan format `n of max`

### Extension ditolak dan dibatalkan
67. Asset Admin DU-087-25 mengajukan Extend aset DU-087-1 dengan Extend duration `2 Day(s)`
68. Approver menolak Extension aset DU-087-1 dengan Reason `Aset dijadwalkan untuk pemakaian lain {runId}`
69. Verifikasi node `Extension rejected by [Actor]` untuk aset DU-087-1 tercatat dengan pelaku Approver dan Reason `Aset dijadwalkan untuk pemakaian lain {runId}`
70. Asset Admin DU-087-25 mengajukan Extend aset DU-087-1 dengan Extend duration `2 Day(s)`
71. Asset Admin DU-087-25 menjalankan Cancel Extension atas pengajuan itu
72. Verifikasi node `Extension canceled by [Actor]` untuk aset DU-087-1 tercatat dengan pelaku Asset Admin DU-087-25
73. Asset Admin DU-087-25 mengajukan Extend aset DU-087-1 dengan Extend duration `2 Day(s)`
74. Asset Admin DU-087-25 menerima kembali aset DU-087-1 dengan Condition `Normal`
75. Verifikasi node `Extension canceled by [Actor]` untuk pengajuan terakhir tercatat dengan pelaku `System` dan Reason `Asset returned`
76. Verifikasi node `Returned to [Receiver]` untuk aset DU-087-1 tercatat dengan penerima Asset Admin DU-087-25 dan Condition `Normal`
77. Verifikasi Borrow Log aset DU-087-1 tidak memuat node edit Extension

### Overdue oleh System dan pengembalian terlambat
78. Asset Admin DU-087-25 mengajukan BRW untuk aset DU-087-7 atas nama Borrower DU-087-14 dengan Duration `5 Day(s)` dan Purpose `Presentasi klien {runId}`
79. Approver menyetujui aset DU-087-7
80. Asset Admin DU-087-25 menyerahkan aset DU-087-7 kepada Borrower DU-087-14 dengan Condition `Normal`
81. Waktu berlalu sampai 1 hari sesudah Due date aset DU-087-7
82. Job Overdue berjalan
83. Verifikasi node `Overdue` untuk aset DU-087-7 tercatat dengan pelaku `System` dan Due date
84. Verifikasi peristiwa `Overdue` itu terbaca di log pengguna Borrower DU-087-14 dengan pelaku `System`
85. Waktu berlalu sampai 2 hari sesudah Due date aset DU-087-7
86. Asset Admin DU-087-25 menerima kembali aset DU-087-7 dengan Condition `Normal`
87. Verifikasi detail node `Returned to [Receiver]` untuk aset DU-087-7 memuat Late dengan format `n days`

### Pengembalian mandiri oleh Borrower
88. Borrower DU-087-14 mengembalikan aset DU-087-12 lewat self-service
89. Verifikasi node `Returned via self-service by [Borrower]` untuk aset DU-087-12 tercatat dengan pelaku Borrower DU-087-14

### Damage dilaporkan lalu dibatalkan dan TAG dilaporkan
90. Asset Admin DU-087-25 mengajukan BRW untuk aset DU-087-8 atas nama Borrower DU-087-14 dengan Duration `5 Day(s)` dan Purpose `Presentasi klien {runId}`
91. Approver menyetujui aset DU-087-8
92. Asset Admin DU-087-25 menjalankan `I Can't Scan the TAG` saat menyerahkan aset DU-087-8
93. Verifikasi node `TAG reported by [Reporter]` untuk aset DU-087-8 dari Handover tercatat dengan pelaku Asset Admin DU-087-25 dan kode TAG yang dilaporkan
94. Asset Admin DU-087-25 menyerahkan aset DU-087-8 kepada Borrower DU-087-14 dengan Condition `Normal` sesudah Replace TAG atas aset itu selesai
95. Borrower DU-087-14 melaporkan kerusakan aset DU-087-8 dengan What happened `Casing retak di sudut atas {runId}` dan Photo `kerusakan-casing-{runId}.jpg`
96. Verifikasi node `Damage reported by [Reporter]` untuk aset DU-087-8 tercatat dengan pelaku Borrower DU-087-14, Type, Description `Casing retak di sudut atas {runId}`, dan Report No.
97. Borrower DU-087-14 membatalkan laporan kerusakan aset DU-087-8
98. Verifikasi node `Damage report canceled by [Actor]` untuk aset DU-087-8 tercatat dengan pelaku Borrower DU-087-14 dan Report No.
99. Verifikasi baris aset DU-087-8 tetap berstatus Borrowed sesudah laporan dibatalkan
100. Asset Admin DU-087-25 menjalankan `I Can't Scan the TAG` saat menerima kembali aset DU-087-8
101. Verifikasi node `TAG reported by [Reporter]` untuk aset DU-087-8 tercatat dengan pelaku Asset Admin DU-087-25, kode semua TAG yang dilaporkan, Report Type, dan Report No.
102. Verifikasi TAG Log aset DU-087-8 memuat entri dari laporan TAG yang dipicu `I Can't Scan the TAG` saat Return

### Laporan Missing ditolak atau dibatalkan
103. Asset Admin DU-087-25 mengajukan BRW untuk aset DU-087-9 atas nama Borrower DU-087-14 dengan Duration `5 Day(s)` dan Purpose `Presentasi klien {runId}`
104. Approver menyetujui aset DU-087-9
105. Asset Admin DU-087-25 menyerahkan aset DU-087-9 kepada Borrower DU-087-14 dengan Condition `Normal`
106. Borrower DU-087-14 melaporkan kehilangan aset DU-087-9 dengan Reason `Aset tidak ditemukan di meja kerja sejak pagi {runId}`
107. Verifikasi node `Reported missing by [Actor]` untuk aset DU-087-9 tercatat dengan pelaku Borrower DU-087-14, Reason `Aset tidak ditemukan di meja kerja sejak pagi {runId}`, dan Status `Waiting for Confirmation`
108. Aktor yang berhak atas laporan kehilangan menolak laporan kehilangan aset DU-087-9 dengan Reason `Laporan belum dapat diverifikasi {runId}`
109. Verifikasi node `Missing report rejected by [Actor]` untuk aset DU-087-9 tercatat dengan pelaku aktor yang berhak atas laporan kehilangan dan Reason `Laporan belum dapat diverifikasi {runId}`
110. Verifikasi baris aset DU-087-9 tetap berstatus Borrowed sesudah laporan ditolak
111. Borrower DU-087-14 melaporkan kehilangan aset DU-087-9 dengan Reason `Aset tidak ditemukan di meja kerja sejak pagi {runId}`
112. Borrower DU-087-14 membatalkan laporan kehilangan aset DU-087-9
113. Verifikasi node `Missing report canceled by [Actor]` untuk aset DU-087-9 tercatat dengan pelaku Borrower DU-087-14

### Laporan Missing dikonfirmasi
114. Asset Admin DU-087-25 mengajukan BRW untuk aset DU-087-10 atas nama Borrower DU-087-14 dengan Duration `5 Day(s)` dan Purpose `Presentasi klien {runId}`
115. Approver menyetujui aset DU-087-10
116. Asset Admin DU-087-25 menyerahkan aset DU-087-10 kepada Borrower DU-087-14 dengan Condition `Normal`
117. Borrower DU-087-14 melaporkan kehilangan aset DU-087-10 dengan Reason `Aset tidak ditemukan di meja kerja sejak pagi {runId}`
118. Aktor yang berhak atas laporan kehilangan mengonfirmasi laporan kehilangan aset DU-087-10
119. Verifikasi node `Missing confirmed by [Actor]` untuk aset DU-087-10 tercatat dengan pelaku aktor yang berhak atas laporan kehilangan
120. Verifikasi baris aset DU-087-10 ditutup `Returned` dengan penanda `Missing`

### Pengembalian biasa tidak memakai penanda Plan change
121. Verifikasi node `Returned to [Receiver]` untuk aset DU-087-7 tidak memuat penanda `Plan change`

### Bulk Delete Draft menulis satu entri per Draft yang berhasil
122. Asset Admin DU-087-25 menyimpan Draft A berisi aset DU-087-26 untuk Borrower DU-087-14
123. Asset Admin DU-087-25 menyimpan Draft B berisi aset DU-087-27 untuk Borrower DU-087-14
124. Verifikasi Borrow Log dan Transaction log aset DU-087-26 tidak memuat peristiwa dari penyimpanan Draft A
125. Total Control menyimpan Draft C berisi aset DU-087-28 dan aset DU-087-29 untuk Borrower DU-087-14
126. Asset Admin DU-087-25 menjalankan bulk Delete Draft atas Draft A, Draft B, dan Draft C
127. Verifikasi Transaction admin log Asset Admin DU-087-25 memuat satu entri untuk Draft A dan satu entri untuk Draft B
128. Verifikasi Draft C yang dilewati karena di luar cakupan tidak menulis entri di Transaction admin log Asset Admin DU-087-25

### Aksi Asset Admin hanya menulis Transaction admin log dan Download tidak dicatat
129. Asset Admin DU-087-25 mengunduh daftar transaksi Borrow
130. Verifikasi Transaction admin log Asset Admin DU-087-25 tidak memuat entri baru dari Download
131. Verifikasi tindakan transaksi Asset Admin DU-087-25 atas aset DU-087-7 tercatat di Transaction admin log sebagai surface log transaksi terpisah
132. Verifikasi tindakan itu tidak menulis Activity Log aktor Asset Admin DU-087-25
133. Verifikasi tindakan itu tidak menulis System Log aktor Asset Admin DU-087-25
134. Verifikasi riwayat aset DU-087-7 dalam BRW-nya dibaca di Borrow Log
135. Verifikasi tindakan itu disimpan sekali dan terbaca lewat Borrow Log dan Transaction admin log dari catatan yang sama

### Approval mode All dan Any one dicatat per aset beserta waktu keputusan
136. Asset Admin DU-087-25 mengajukan BRW untuk aset DU-087-39, DU-087-40, dan DU-087-41 atas nama Borrower DU-087-14 dengan Duration `5 Day(s)` dan Purpose `Presentasi klien {runId}`
137. Verifikasi node `Borrow requested by [Actor]` untuk aset DU-087-39 memuat Approval `Waiting 2 approvers`
138. Verifikasi node `Borrow requested by [Actor]` untuk aset DU-087-41 memuat Approval `Not required`
139. Approver DU-087-30 menyetujui aset DU-087-39
140. Approver DU-087-30 menyetujui aset DU-087-40
141. Verifikasi aset DU-087-39 belum berstatus Waiting for Handover karena keputusan Approver DU-087-31 belum masuk
142. Approver DU-087-31 menyetujui aset DU-087-39
143. Verifikasi aset DU-087-39 memuat satu node `Approved by [Approver]` untuk tiap approver, yaitu pelaku Approver DU-087-30 dan pelaku Approver DU-087-31, masing-masing dengan Mode `All`
144. Verifikasi aset DU-087-40 memuat satu node `Approved by [Approver]` dengan pelaku Approver DU-087-30 dan Mode `Any one`
145. Verifikasi setiap node `Approved by [Approver]` pada aset DU-087-39 dan aset DU-087-40 memuat waktu keputusannya
146. Verifikasi log aset DU-087-41 memuat node `Auto-approved` dengan pelaku `System` dan tidak memuat node `Approved by [Approver]`

### Approval dialihkan ke Total Control bila Group tidak punya Group Manager
147. Asset Admin DU-087-33 mengajukan BRW untuk aset DU-087-42 atas nama Borrower DU-087-14 dengan Duration `5 Day(s)` dan Purpose `Presentasi klien {runId}`
148. Verifikasi node `Approval rerouted` untuk aset DU-087-42 tercatat dengan pelaku `System`, Routed to `Total Control`, dan Reason `No eligible approver`

### Aksi multi-baris menulis satu entri per baris dan baris yang dilewati tidak menulis entri
149. Asset Admin DU-087-25 mengajukan BRW untuk aset DU-087-43, DU-087-44, DU-087-45, dan DU-087-46 atas nama Borrower DU-087-14 dengan Duration `5 Day(s)` dan Purpose `Presentasi klien {runId}`
150. Approver DU-087-30 menyetujui aset DU-087-43, DU-087-44, DU-087-45, dan DU-087-46
151. Catat jumlah entri Transaction admin log Asset Admin DU-087-25
152. Asset Admin DU-087-25 menyerahkan aset DU-087-44, DU-087-45, dan DU-087-46 sekaligus kepada Borrower DU-087-14 dengan Condition `Normal`
153. Verifikasi Transaction admin log Asset Admin DU-087-25 bertambah satu entri `Handed over by [Giver]` untuk tiap aset DU-087-44, DU-087-45, dan DU-087-46 dibanding jumlah yang dicatat
154. Catat jumlah entri Transaction admin log Asset Admin DU-087-25 sesudah serah terima
155. Asset Admin DU-087-25 membatalkan seluruh BRW itu lewat Cancel Borrow per BRW
156. Verifikasi baris aset DU-087-43 berstatus Canceled dan baris aset DU-087-44, DU-087-45, dan DU-087-46 tetap Borrowed karena dilewati
157. Verifikasi Transaction admin log Asset Admin DU-087-25 bertambah satu entri `Canceled by [Actor]` untuk aset DU-087-43 dan tidak bertambah entri untuk aset DU-087-44, DU-087-45, dan DU-087-46 yang dilewati, dibanding jumlah yang dicatat sesudah serah terima
158. Asset Admin DU-087-25 menerima kembali aset DU-087-44 dan DU-087-45 sekaligus dengan Condition `Normal`
159. Verifikasi Transaction admin log Asset Admin DU-087-25 bertambah satu entri `Returned to [Receiver]` untuk tiap aset DU-087-44 dan DU-087-45

### Pengingat Due date otomatis tidak dicatat
160. Asset Admin DU-087-25 mengajukan BRW untuk aset DU-087-47 atas nama Borrower DU-087-14 dengan Duration `5 Day(s)` dan Purpose `Presentasi klien {runId}`
161. Approver DU-087-30 menyetujui aset DU-087-47
162. Asset Admin DU-087-25 menyerahkan aset DU-087-47 kepada Borrower DU-087-14 dengan Condition `Normal`
163. Waktu berlalu sampai ambang pengingat Due date aset DU-087-47 tercapai
164. Job Due date reminders berjalan
165. Verifikasi Borrow Log aset DU-087-47 tidak memuat node dari pengingat otomatis

### Perubahan isi Draft tidak dicatat
166. Asset Admin DU-087-25 menyimpan Draft D berisi aset DU-087-48 untuk Borrower DU-087-14
167. Asset Admin DU-087-25 mengubah Purpose Draft D menjadi `Rapat vendor {runId}`
168. Verifikasi Borrow Log dan Transaction log aset DU-087-48 tidak memuat peristiwa dari penyimpanan maupun perubahan isi Draft D

### Canceled oleh System karena Borrower dinonaktifkan
169. Asset Admin DU-087-25 mengajukan BRW untuk aset DU-087-50 atas nama Borrower DU-087-49 dengan Duration `5 Day(s)` dan Purpose `Presentasi klien {runId}`
170. Approver DU-087-30 menyetujui aset DU-087-50
171. Borrower DU-087-49 dinonaktifkan
172. Verifikasi node `Canceled by [Actor]` untuk aset DU-087-50 tercatat dengan pelaku `System` dan Reason `Borrower deactivated`

### Cancel Borrow oleh PIC, Group Manager, dan Total Control
173. Asset Admin DU-087-25 mengajukan BRW untuk aset DU-087-51, DU-087-52, dan DU-087-53 atas nama Borrower DU-087-15 dengan Duration `5 Day(s)` dan Purpose `Presentasi klien {runId}`
174. Approver DU-087-30 menyetujui aset DU-087-51, DU-087-52, dan DU-087-53
175. PIC DU-087-34 membatalkan baris aset DU-087-51 lewat Cancel Borrow dari halaman pinjamannya
176. Verifikasi node `Canceled by [Actor]` untuk aset DU-087-51 tercatat dengan pelaku PIC DU-087-34 yang bertindak atas nama Borrower DU-087-15 (`[PIC] on behalf of [Borrower]`)
177. Group Manager DU-087-32 membatalkan baris aset DU-087-52 lewat Cancel Borrow
178. Verifikasi node `Canceled by [Actor]` untuk aset DU-087-52 tercatat dengan pelaku Group Manager DU-087-32
179. Total Control membatalkan baris aset DU-087-53 lewat Cancel Borrow
180. Verifikasi node `Canceled by [Actor]` untuk aset DU-087-53 tercatat dengan pelaku Total Control

### Handover tidak dikonfirmasi karena aset tidak dicentang Borrower
181. Asset Admin DU-087-25 mengajukan BRW untuk aset DU-087-54, DU-087-55, dan DU-087-56 atas nama Borrower DU-087-14 dengan Duration `5 Day(s)` dan Purpose `Presentasi klien {runId}`
182. Approver DU-087-30 menyetujui aset DU-087-54, DU-087-55, dan DU-087-56
183. Asset Admin DU-087-25 memulai handover aset DU-087-54, DU-087-55, dan DU-087-56
184. Borrower DU-087-14 mengonfirmasi handover dari halaman pinjamannya dengan mencentang aset DU-087-54 saja
185. Verifikasi satu node `Handover not confirmed` untuk aset DU-087-55 dan satu node untuk aset DU-087-56 tercatat dengan pelaku Borrower DU-087-14 dan baris tetap Waiting for Handover
186. Verifikasi aset DU-087-54 tidak memuat node `Handover not confirmed`

### Extension oleh PIC diteruskan ke beberapa approver lalu dibatalkan Group Manager
187. Asset Admin DU-087-25 mengajukan BRW untuk aset DU-087-57 atas nama Borrower DU-087-15 dengan Duration `5 Day(s)` dan Purpose `Presentasi klien {runId}`
188. Approver DU-087-30 menyetujui aset DU-087-57
189. Approver DU-087-31 menyetujui aset DU-087-57
190. Asset Admin DU-087-25 menyerahkan aset DU-087-57 kepada Borrower DU-087-15 dengan Condition `Normal`, PIC DU-087-34 mengonfirmasi atas nama Borrower
191. PIC DU-087-34 mengajukan Extend aset DU-087-57 dengan Extend duration `2 Day(s)`
192. Verifikasi node `Extension requested by [Actor]` untuk aset DU-087-57 tercatat dengan pelaku PIC DU-087-34
193. Asset Admin DU-087-25 meneruskan permintaan Extension aset DU-087-57 ke approval
194. Verifikasi node `Extension forwarded to approval by [Actor]` untuk aset DU-087-57 tercatat dengan pelaku Asset Admin DU-087-25 dan Approval `Waiting 2 approvers`
195. Group Manager DU-087-32 menjalankan Cancel Extension atas pengajuan itu
196. Verifikasi node `Extension canceled by [Actor]` untuk aset DU-087-57 tercatat dengan pelaku Group Manager DU-087-32

### Extension oleh Aktor Borrow dibatalkan Total Control
197. Asset Admin DU-087-25 mengajukan BRW untuk aset DU-087-58 atas nama Borrower DU-087-15 dengan Duration `5 Day(s)` dan Purpose `Presentasi klien {runId}`
198. Approver DU-087-30 menyetujui aset DU-087-58
199. Asset Admin DU-087-25 menyerahkan aset DU-087-58 kepada Borrower DU-087-15 dengan Condition `Normal`, PIC DU-087-34 mengonfirmasi atas nama Borrower
200. Asset Admin DU-087-25 mengajukan Extend aset DU-087-58 dengan Extend duration `2 Day(s)`
201. Verifikasi node `Extension requested by [Actor]` untuk aset DU-087-58 tercatat dengan pelaku Asset Admin DU-087-25
202. Total Control menjalankan Cancel Extension atas pengajuan itu
203. Verifikasi node `Extension canceled by [Actor]` untuk aset DU-087-58 tercatat dengan pelaku Total Control

### Extension yang memenuhi Auto-approve dicatat otomatis oleh System
204. Asset Admin DU-087-25 mengajukan BRW untuk aset DU-087-59 atas nama Borrower DU-087-14 dengan Duration `2 Day(s)` dan Purpose `Presentasi klien {runId}`
205. Asset Admin DU-087-25 menyerahkan aset DU-087-59 kepada Borrower DU-087-14 dengan Condition `Normal`
206. Asset Admin DU-087-25 mengajukan Extend aset DU-087-59 dengan Extend duration `1 Day(s)`
207. Verifikasi node `Extension auto-approved` untuk aset DU-087-59 tercatat dengan pelaku `System`

### Review Extend dari My Asset diterapkan Aktor Borrow tanpa approval
208. Asset Admin DU-087-25 mengajukan BRW untuk aset DU-087-60 atas nama Borrower DU-087-14 dengan Duration `2 Day(s)` dan Purpose `Presentasi klien {runId}`
209. Asset Admin DU-087-25 menyerahkan aset DU-087-60 kepada Borrower DU-087-14 dengan Condition `Normal`
210. Borrower DU-087-14 mengajukan Extend aset DU-087-60 dengan Extend duration `1 Day(s)` dari halaman pinjamannya
211. Asset Admin DU-087-25 menyetujui pengajuan Extend aset DU-087-60 lewat Review Extension Request
212. Verifikasi node `Extension applied by [Actor]` untuk aset DU-087-60 tercatat dengan pelaku Asset Admin DU-087-25

### Review Extend dari My Asset ditolak Aktor Borrow
213. Asset Admin DU-087-25 mengajukan BRW untuk aset DU-087-61 atas nama Borrower DU-087-14 dengan Duration `2 Day(s)` dan Purpose `Presentasi klien {runId}`
214. Approver DU-087-30 menyetujui aset DU-087-61
215. Asset Admin DU-087-25 menyerahkan aset DU-087-61 kepada Borrower DU-087-14 dengan Condition `Normal`
216. Borrower DU-087-14 mengajukan Extend aset DU-087-61 dengan Extend duration `1 Day(s)` dari halaman pinjamannya
217. Asset Admin DU-087-25 menolak pengajuan Extend aset DU-087-61 lewat Review Extension Request dengan Reason `Aset dijadwalkan untuk pemakaian lain {runId}`
218. Verifikasi node `Extension rejected by [Actor]` untuk aset DU-087-61 tercatat dengan pelaku Asset Admin DU-087-25 dan Reason `Aset dijadwalkan untuk pemakaian lain {runId}`

### Extension mandiri Borrower dicatat sebagai self-service
219. Borrower DU-087-14 meminjam aset DU-087-62 lewat self-service dengan Duration `2 Day(s)` dan Purpose `Presentasi klien {runId}`
220. Borrower DU-087-14 mengajukan Extend aset DU-087-62 dengan Extend duration `1 Day(s)`
221. Verifikasi node `Extended via self-service by [Borrower]` untuk aset DU-087-62 tercatat dengan pelaku Borrower DU-087-14

### Laporan Missing oleh PIC menunggu konfirmasi lalu dibatalkan
222. Asset Admin DU-087-25 mengajukan BRW untuk aset DU-087-63 atas nama Borrower DU-087-15 dengan Duration `5 Day(s)` dan Purpose `Presentasi klien {runId}`
223. Approver DU-087-30 menyetujui aset DU-087-63
224. Asset Admin DU-087-25 menyerahkan aset DU-087-63 kepada Borrower DU-087-15 dengan Condition `Normal`, PIC DU-087-34 mengonfirmasi atas nama Borrower
225. PIC DU-087-34 melaporkan kehilangan aset DU-087-63 dengan Reason `Aset tidak ditemukan di meja kerja sejak pagi {runId}`
226. Verifikasi node `Reported missing by [Actor]` untuk aset DU-087-63 tercatat dengan pelaku PIC DU-087-34 dan Status `Waiting for Confirmation`
227. Verifikasi baris aset DU-087-63 tetap berstatus Borrowed sesudah laporan dibuat
228. PIC DU-087-34 membatalkan laporan kehilangan aset DU-087-63
229. Verifikasi node `Missing report canceled by [Actor]` untuk aset DU-087-63 tercatat dengan pelaku PIC DU-087-34

### Laporan Missing oleh Aktor Borrow tanpa hak Aktor Missing
230. Asset Admin DU-087-25 mengajukan BRW untuk aset DU-087-64 atas nama Borrower DU-087-14 dengan Duration `5 Day(s)` dan Purpose `Presentasi klien {runId}`
231. Approver DU-087-30 menyetujui aset DU-087-64
232. Asset Admin DU-087-25 menyerahkan aset DU-087-64 kepada Borrower DU-087-14 dengan Condition `Normal`
233. Asset Admin DU-087-25 melaporkan kehilangan aset DU-087-64 dengan Reason `Aset tidak ditemukan di meja kerja sejak pagi {runId}`
234. Verifikasi node `Reported missing by [Actor]` untuk aset DU-087-64 tercatat dengan pelaku Asset Admin DU-087-25 dan Status `Waiting for Confirmation`
235. Verifikasi baris aset DU-087-64 tetap berstatus Borrowed sesudah laporan dibuat

### Laporan Damaged oleh PIC dibatalkan PIC
236. Asset Admin DU-087-25 mengajukan BRW untuk aset DU-087-65 atas nama Borrower DU-087-15 dengan Duration `5 Day(s)` dan Purpose `Presentasi klien {runId}`
237. Approver DU-087-30 menyetujui aset DU-087-65
238. Asset Admin DU-087-25 menyerahkan aset DU-087-65 kepada Borrower DU-087-15 dengan Condition `Normal`, PIC DU-087-34 mengonfirmasi atas nama Borrower
239. PIC DU-087-34 melaporkan kerusakan aset DU-087-65 dengan What happened `Casing retak di sudut atas {runId}` dan Photo `kerusakan-casing-{runId}.jpg`
240. Verifikasi node `Damage reported by [Reporter]` untuk aset DU-087-65 tercatat dengan pelaku PIC DU-087-34
241. PIC DU-087-34 membatalkan laporan kerusakan aset DU-087-65
242. Verifikasi node `Damage report canceled by [Actor]` untuk aset DU-087-65 tercatat dengan pelaku PIC DU-087-34

### Laporan Damaged oleh Aktor Borrow dibatalkan pelapornya sendiri
243. Asset Admin DU-087-25 mengajukan BRW untuk aset DU-087-66 atas nama Borrower DU-087-14 dengan Duration `5 Day(s)` dan Purpose `Presentasi klien {runId}`
244. Approver DU-087-30 menyetujui aset DU-087-66
245. Asset Admin DU-087-25 menyerahkan aset DU-087-66 kepada Borrower DU-087-14 dengan Condition `Normal`
246. Asset Admin DU-087-25 melaporkan kerusakan aset DU-087-66 dengan What happened `Casing retak di sudut atas {runId}` dan Photo `kerusakan-casing-{runId}.jpg`
247. Verifikasi node `Damage reported by [Reporter]` untuk aset DU-087-66 tercatat dengan pelaku Asset Admin DU-087-25
248. Asset Admin DU-087-25 membatalkan laporan kerusakannya sendiri atas aset DU-087-66
249. Verifikasi node `Damage report canceled by [Actor]` untuk aset DU-087-66 tercatat dengan pelaku Asset Admin DU-087-25

### Return dengan Report Damaged mencatat Report No. pada node Returned
250. Asset Admin DU-087-25 mengajukan BRW untuk aset DU-087-67 atas nama Borrower DU-087-14 dengan Duration `5 Day(s)` dan Purpose `Presentasi klien {runId}`
251. Approver DU-087-30 menyetujui aset DU-087-67
252. Asset Admin DU-087-25 menyerahkan aset DU-087-67 kepada Borrower DU-087-14 dengan Condition `Normal`
253. Asset Admin DU-087-25 menjalankan Report Damaged pada halaman Return aset DU-087-67 dengan What happened `Casing retak di sudut atas {runId}` dan Photo `kerusakan-casing-{runId}.jpg`
254. Asset Admin DU-087-25 menerima kembali aset DU-087-67 dengan Condition `Normal`
255. Verifikasi detail node `Returned to [Receiver]` untuk aset DU-087-67 memuat Report No. dengan tautan ke laporan

### Pembatalan Extension karena aset kembali terbaca di log pengguna Borrower
256. Verifikasi peristiwa `Extension canceled by [Actor]` dengan Reason `Asset returned` untuk aset DU-087-1 terbaca di log pengguna Borrower DU-087-14 dengan pelaku `System`

### Perubahan PIC Borrower tidak dicatat di Borrow Log
257. PIC Borrower DU-087-15 diubah menjadi `Rina Kusuma {runId}`
258. Verifikasi Borrow Log aset DU-087-4 tidak memuat node dari perubahan PIC Borrower DU-087-15

### Extension dibatalkan oleh pengajunya sendiri dan oleh Asset Admin lain
259. Asset Admin DU-087-25 mengajukan BRW untuk aset DU-087-70 atas nama Borrower DU-087-14 dengan Duration `5 Day(s)` dan Purpose `Presentasi klien {runId}`
260. Approver DU-087-30 menyetujui aset DU-087-70
261. Asset Admin DU-087-25 menyerahkan aset DU-087-70 kepada Borrower DU-087-14 dengan Condition `Normal`
262. Borrower DU-087-14 mengajukan Extend aset DU-087-70 dengan Extend duration `2 Day(s)` dari halaman pinjamannya
263. Borrower DU-087-14 menjalankan Cancel Extension Request atas pengajuan itu dari halaman pinjamannya
264. Verifikasi node `Extension canceled by [Actor]` untuk aset DU-087-70 tercatat dengan pelaku Borrower DU-087-14
265. Asset Admin DU-087-25 mengajukan BRW untuk aset DU-087-71 atas nama Borrower DU-087-15 dengan Duration `5 Day(s)` dan Purpose `Presentasi klien {runId}`
266. Approver DU-087-30 menyetujui aset DU-087-71
267. Asset Admin DU-087-25 menyerahkan aset DU-087-71 kepada Borrower DU-087-15 dengan Condition `Normal`, PIC DU-087-34 mengonfirmasi atas nama Borrower
268. PIC DU-087-34 mengajukan Extend aset DU-087-71 dengan Extend duration `2 Day(s)`
269. PIC DU-087-34 menjalankan Cancel Extension atas pengajuan itu
270. Verifikasi node `Extension canceled by [Actor]` untuk aset DU-087-71 tercatat dengan pelaku PIC DU-087-34
271. Asset Admin DU-087-25 mengajukan BRW untuk aset DU-087-72 atas nama Borrower DU-087-14 dengan Duration `5 Day(s)` dan Purpose `Presentasi klien {runId}`
272. Approver DU-087-30 menyetujui aset DU-087-72
273. Asset Admin DU-087-25 menyerahkan aset DU-087-72 kepada Borrower DU-087-14 dengan Condition `Normal`
274. Asset Admin DU-087-25 mengajukan Extend aset DU-087-72 dengan Extend duration `2 Day(s)`
275. Asset Admin DU-087-73 menjalankan Cancel Extension atas pengajuan Asset Admin DU-087-25
276. Verifikasi node `Extension canceled by [Actor]` untuk aset DU-087-72 tercatat dengan pelaku Asset Admin DU-087-73

### Foto serah terima dan foto return tercatat pada node
277. Asset Admin DU-087-25 mengajukan BRW untuk aset DU-087-74 atas nama Borrower DU-087-14 dengan Duration `5 Day(s)` dan Purpose `Presentasi klien {runId}`
278. Approver DU-087-30 menyetujui aset DU-087-74
279. Asset Admin DU-087-25 menyerahkan aset DU-087-74 kepada Borrower DU-087-14 dengan Condition `Normal` dan Photo `foto-serah-terima-{runId}.jpg`
280. Verifikasi detail node `Handed over by [Giver]` untuk aset DU-087-74 memuat Photo yang diambil saat serah terima
281. Asset Admin DU-087-25 menerima kembali aset DU-087-74 dengan Condition `Normal` dan Photo `foto-return-{runId}.jpg`
282. Verifikasi detail node `Returned to [Receiver]` untuk aset DU-087-74 memuat Photo yang diambil saat return

### Return baris Hours yang terlambat kurang dari satu hari mencatat Late dalam jam
283. Asset Admin DU-087-25 mengajukan BRW untuk aset DU-087-75 atas nama Borrower DU-087-14 dengan Duration `2 Hour(s)` dan Purpose `Presentasi klien {runId}`
284. Approver DU-087-30 menyetujui aset DU-087-75
285. Asset Admin DU-087-25 menyerahkan aset DU-087-75 kepada Borrower DU-087-14 dengan Condition `Normal`
286. Waktu berlalu sampai 2 jam sesudah Due date aset DU-087-75
287. Asset Admin DU-087-25 menerima kembali aset DU-087-75 dengan Condition `Normal`
288. Verifikasi detail node `Returned to [Receiver]` untuk aset DU-087-75 memuat Late dengan format `n hours`
