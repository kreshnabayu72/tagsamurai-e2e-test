---
id: TC-FA-BORROW-BE-079-extend-aturan-server
title: "Extend per baris: syarat, batas Max duration dan Max extensions, approval, dan siklus pengajuan Extension"
layer: be-e2e
priority: Critical
caseType: Positive
status: draft
sourceRules: ["BORROW-LOGIC-10a", "BORROW-LOGIC-10b", "BORROW-LOGIC-10c", "BORROW-LOGIC-10d", "BORROW-LOGIC-10e", "BORROW-LOGIC-10f", "BORROW-LOGIC-10g", "BORROW-LOGIC-10h", "BORROW-LOGIC-10i", "BORROW-LOGIC-10j", "EC-BRW-103", "EC-BRW-111", "EC-BRW-132", "EC-BRW-137", "EC-BRW-138", "EC-BRW-145", "EC-BRW-146", "EC-BRW-147", "EC-BRW-155", "EC-BRW-158", "EC-BRW-21", "EC-BRW-22", "EC-BRW-23", "EC-BRW-24", "EC-BRW-44", "EC-BRW-67a", "EC-BRW-68", "EC-BRW-81", "EC-BRW-82", "EC-BRW-95", "EC-BRW-96", "EC-BRW-97", "F-BORROW-07.k1", "F-BORROW-07.k10", "F-BORROW-07.k11", "F-BORROW-07.k12", "F-BORROW-07.k2", "F-BORROW-07.k3", "F-BORROW-07.k4", "F-BORROW-07.k5", "F-BORROW-07.k6", "F-BORROW-07.k7", "F-BORROW-07.k8", "F-BORROW-07.k9", "§9.2#b50", "§9.2#b51", "§9.2#b53", "§9.2#b54", "§9.2#b55", "§9.2#b56", "§9.2#b57", "§9.2#b58", "§9.2#b60", "§9.2#p33", "§9.2#r39", "§9.2#r40", "§9.2#r41", "§9.2#r42", "§9.2#r43", "§9.2#b61", "§9.2#b62", "§9.2#b63"]
smoke: []
dependsOn: []
owner: BE
trace:
  "BORROW-LOGIC-10a": 2
  "BORROW-LOGIC-10b": 66
  "BORROW-LOGIC-10c": 37
  "BORROW-LOGIC-10d": [4, 14]
  "BORROW-LOGIC-10e": 16
  "BORROW-LOGIC-10f": [28, 29]
  "BORROW-LOGIC-10g": 113
  "BORROW-LOGIC-10h": [77, 82]
  "BORROW-LOGIC-10i": 78
  "BORROW-LOGIC-10j": 125
  "EC-BRW-103": [73, 74]
  "EC-BRW-111": [49, 50, 52]
  "EC-BRW-132": [160, 161]
  "EC-BRW-137": [63, 64, 65]
  "EC-BRW-138": [69, 70, 71]
  "EC-BRW-145": [33, 34]
  "EC-BRW-146": [54, 56, 58, 60, 61]
  "EC-BRW-147": [39, 40, 41]
  "EC-BRW-155": [77, 78, 80]
  "EC-BRW-158": [82, 84, 86, 87, 88]
  "EC-BRW-21": [34, 36]
  "EC-BRW-22": 18
  "EC-BRW-23": [28, 29]
  "EC-BRW-24": 66
  "EC-BRW-44": [43, 44, 45, 46, 47]
  "EC-BRW-67a": [90, 91, 92, 93, 95, 99]
  "EC-BRW-68": [163, 164]
  "EC-BRW-81": [139, 140, 141]
  "EC-BRW-82": [152, 153]
  "EC-BRW-95": [131, 132]
  "EC-BRW-96": [134, 135]
  "EC-BRW-97": [110, 111]
  "F-BORROW-07.k1": [2, 15, 63, 64, 69, 70, 116]
  "F-BORROW-07.k10": [24, 25, 26, 139, 141]
  "F-BORROW-07.k11": [143, 144, 145, 146, 147, 149]
  "F-BORROW-07.k12": [90, 102, 106, 110]
  "F-BORROW-07.k2": [12, 33, 36, 44, 45]
  "F-BORROW-07.k3": [18, 163]
  "F-BORROW-07.k4": [3, 39, 54, 60]
  "F-BORROW-07.k5": [95, 97, 101, 102, 104]
  "F-BORROW-07.k6": [77, 80, 82, 84, 86]
  "F-BORROW-07.k7": [28, 29]
  "F-BORROW-07.k8": 134
  "F-BORROW-07.k9": [130, 131, 132]
  "§9.2#b50": [4, 14, 16, 30, 65, 125, 126]
  "§9.2#b51": [7, 22, 31, 52]
  "§9.2#b53": [10, 11, 29, 66]
  "§9.2#b54": 8
  "§9.2#b55": [113, 114, 115, 116, 125, 126]
  "§9.2#b56": [118, 134]
  "§9.2#b57": [119, 120, 121, 129, 135]
  "§9.2#b58": [123, 124]
  "§9.2#b60": 9
  "§9.2#p33": 21
  "§9.2#r39": [5, 6, 23]
  "§9.2#r40": [24, 25, 26]
  "§9.2#r41": [143, 144, 145, 146, 147, 149]
  "§9.2#r42": [154, 155, 156, 157]
  "§9.2#r43": [90, 91, 99, 102, 106, 108]
  "§9.2#b61": [91, 92, 107, 157]
  "§9.2#b62": 20
  "§9.2#b63": 137
---

# Extend per baris: syarat, batas Max duration dan Max extensions, approval, dan siklus pengajuan Extension

## Prerequisites
- Aktor: Asset Admin `Agus Pratama {runId}` dengan Group penugasan `Head Office {runId}` (DU-079-1) sebagai pengaju Extend; Borrower `Rina Wijaya {runId}` (DU-079-2); Asset Admin kedua `Tika Rahma {runId}` (DU-079-3); Approver `Sari Dewi {runId}` (DU-079-4); Asset Admin `Maya Putri {runId}` dengan hak Aktor Missing dan Aktor Damaged (DU-079-5).
- Data:
  - DU-079-1: Pengguna, Asset Admin pengaju Extend: Name `Agus Pratama {runId}`, Role `Asset Admin`, Group penugasan `Head Office {runId}`.
  - DU-079-2: Pengguna, Borrower dengan akun login: Name `Rina Wijaya {runId}`, Role `Karyawan aktif dengan akun login`, Group `Head Office {runId}`.
  - DU-079-3: Pengguna, Asset Admin kedua: Name `Tika Rahma {runId}`, Role `Asset Admin`, Group penugasan `Head Office {runId}`.
  - DU-079-4: Pengguna, Approver aset: Name `Sari Dewi {runId}`, Role `Approver`, Group penugasan `Head Office {runId}`.
  - DU-079-5: Pengguna, Aktor dengan hak memutuskan laporan hilang dan rusak: Name `Maya Putri {runId}`, Role `Asset Admin dengan hak Aktor Missing dan Aktor Damaged`, Group penugasan `Head Office {runId}`.
  - DU-079-6: Baris Borrow, Extend yang total durasinya memenuhi Auto-approve: BRW `BRW 1`, Borrower `Rina Wijaya {runId}`, Asset Name `Laptop Dell Latitude {runId}`, Category `Laptop`, Duration `1 Days`, Status baris `Borrowed`, Max duration `10 Days`, Max extensions `2`, Extensions terpakai `0`, Auto-approve `3 days`, Require approval `OFF`.
  - DU-079-7: Baris Borrow, Extend yang total durasinya melewati Auto-approve dan butuh approval: BRW `BRW 2 bersama DU-079-8`, Borrower `Rina Wijaya {runId}`, Asset Name `Proyektor Epson {runId}`, Category `Proyektor`, Duration `2 Days`, Status baris `Borrowed`, Max duration `10 Days`, Max extensions `2`, Extensions terpakai `0`, Auto-approve `3 days`, Require approval `ON`, Approver `Sari Dewi {runId}`.
  - DU-079-8: Baris Borrow, Baris kedua dalam pengajuan approval yang sama: BRW `BRW 2 bersama DU-079-7`, Borrower `Rina Wijaya {runId}`, Asset Name `Kamera Mirrorless {runId}`, Category `Kamera`, Duration `2 Days`, Status baris `Borrowed`, Max duration `10 Days`, Max extensions `2`, Extensions terpakai `0`, Auto-approve `3 days`, Require approval `ON`, Approver `Sari Dewi {runId}`.
  - DU-079-9: Baris Borrow, Baris Overdue: BRW `BRW 3`, Borrower `Rina Wijaya {runId}`, Asset Name `Monitor Samsung {runId}`, Category `Monitor`, Duration `1 Days`, Status baris `Overdue`, Max duration `10 Days`, Max extensions `2`, Auto-approve `3 days`, Require approval `OFF`.
  - DU-079-10: Baris Borrow, Baris yang total handover sampai Due date saat ini sudah sama dengan Max duration: BRW `BRW 4 bersama DU-079-11`, Borrower `Rina Wijaya {runId}`, Asset Name `Speaker Portable JBL {runId}`, Category `Audio`, Duration `5 Days`, Status baris `Borrowed`, Max duration `5 Days`, Max extensions `2`, Extensions terpakai `0`.
  - DU-079-11: Baris Borrow, Baris yang Max extensions-nya sudah terpakai: BRW `BRW 4 bersama DU-079-10`, Borrower `Rina Wijaya {runId}`, Asset Name `Mikrofon Wireless Shure {runId}`, Category `Audio`, Duration `2 Days`, Status baris `Borrowed`, Max duration `10 Days`, Max extensions `1`, Extensions terpakai `1`.
  - DU-079-12: Baris Borrow, Baris Days dengan Max duration 7 Days: BRW `BRW 5 bersama DU-079-13`, Borrower `Rina Wijaya {runId}`, Asset Name `Tripod Kamera {runId}`, Category `Aksesori Kamera`, Duration `3 Days`, Status baris `Borrowed`, Max duration `7 Days`, Max extensions `3`, Require approval `OFF`.
  - DU-079-13: Baris Borrow, Baris Hours dengan Max duration 12 Hours: BRW `BRW 5 bersama DU-079-12`, Borrower `Rina Wijaya {runId}`, Asset Name `Walkie Talkie Motorola {runId}`, Category `Peralatan Komunikasi`, Duration `6 Hours`, Status baris `Borrowed`, Max duration `12 Hours`, Max extensions `3`, Require approval `OFF`.
  - DU-079-14: Baris Borrow, Baris Hours yang Due date-nya mendekati tengah malam: BRW `BRW 6`, Borrower `Rina Wijaya {runId}`, Asset Name `Meeting Mic Set {runId}`, Category `Peralatan Rapat`, Duration `12 Hours`, Status baris `Borrowed`, Due date saat ini `22:00`, Due date baru yang diharapkan `02:00 hari berikutnya`, Max duration `48 Hours`, Max extensions `3`, Require approval `OFF`.
  - DU-079-15: Baris Borrow, Baris Hours Overdue: BRW `BRW 7`, Borrower `Rina Wijaya {runId}`, Asset Name `Mixer Audio {runId}`, Category `Peralatan Rapat`, Duration `6 Hours`, Status baris `Overdue`, Max duration `48 Hours`, Max extensions `3`, Require approval `OFF`.
  - DU-079-16: Baris Borrow, Baris untuk uji validasi isian Extend: BRW `BRW 8`, Borrower `Rina Wijaya {runId}`, Asset Name `Router Cisco {runId}`, Category `Perangkat Jaringan`, Duration `3 Days`, Status baris `Borrowed`, Max duration `10 Days`, Max extensions `3`, Require approval `OFF`.
  - DU-079-17: Baris Borrow, Baris dalam BRW yang langsung berlaku: BRW `BRW 9 bersama DU-079-18`, Borrower `Rina Wijaya {runId}`, Asset Name `Kursi Lipat Rapat {runId}`, Category `Furnitur`, Duration `1 Days`, Status baris `Borrowed`, Max duration `10 Days`, Max extensions `3`, Auto-approve `3 days`, Require approval `OFF`.
  - DU-079-18: Baris Borrow, Baris dalam BRW yang sama yang tidak diperpanjang: BRW `BRW 9 bersama DU-079-17`, Borrower `Rina Wijaya {runId}`, Asset Name `Kursi Lipat Cadangan {runId}`, Category `Furnitur`, Duration `1 Days`, Status baris `Borrowed`, Max duration `10 Days`, Max extensions `3`, Auto-approve `3 days`, Require approval `OFF`.
  - DU-079-19: Baris Borrow, Baris dalam BRW yang butuh approval: BRW `BRW 10`, Borrower `Rina Wijaya {runId}`, Asset Name `Papan Tulis {runId}`, Category `Furnitur`, Duration `2 Days`, Status baris `Borrowed`, Max duration `10 Days`, Max extensions `3`, Auto-approve `3 days`, Require approval `ON`, Approver `Sari Dewi {runId}`.
  - DU-079-20: Baris Borrow, Baris BRW yang akan berubah status sebelum Submit: BRW `BRW 11 bersama DU-079-21`, Borrower `Rina Wijaya {runId}`, Asset Name `Proyektor Mini {runId}`, Category `Proyektor`, Duration `2 Days`, Status baris `Borrowed`, Max duration `10 Days`, Max extensions `3`, Auto-approve `3 days`, Require approval `OFF`.
  - DU-079-21: Baris Borrow, Baris kedua dalam BRW yang gagal disimpan: BRW `BRW 11 bersama DU-079-20`, Borrower `Rina Wijaya {runId}`, Asset Name `Layar Proyektor {runId}`, Category `Proyektor`, Duration `2 Days`, Status baris `Borrowed`, Max duration `10 Days`, Max extensions `3`, Auto-approve `3 days`, Require approval `OFF`.
  - DU-079-22: Baris Borrow, Baris BRW lain yang tetap tersimpan: BRW `BRW 12`, Borrower `Rina Wijaya {runId}`, Asset Name `Spotlight LED {runId}`, Category `Peralatan Studio`, Duration `2 Days`, Status baris `Borrowed`, Max duration `10 Days`, Max extensions `3`, Auto-approve `3 days`, Require approval `OFF`.
  - DU-079-23: Baris Borrow, Aset volume yang jumlah baris Extend-nya melebihi Bulk Transaction Row Limit satu aset: BRW `BRW 13`, Borrower `Rina Wijaya {runId}`, Asset Name `Aset Pinjam Batas {n} {runId}`, Category `Perlengkapan Kantor`, Duration `3 Days`, Status baris `Borrowed`.
  - DU-079-24: Baris Borrow, Baris dengan Extension Approval menunggu, kemudian asetnya Unmanaged: BRW `BRW 14`, Borrower `Rina Wijaya {runId}`, Asset Name `Printer Warna Epson {runId}`, Category `Printer`, Duration `3 Days`, Status baris `Borrowed`, Max duration `10 Days`, Max extensions `3`, Extension menunggu `approval oleh Sari Dewi {runId}`, Status aset `Unmanaged`.
  - DU-079-25: Baris Borrow, Baris Overdue dengan aset In Audit: BRW `BRW 15`, Borrower `Rina Wijaya {runId}`, Asset Name `Server Rack Mini {runId}`, Category `Perangkat Jaringan`, Duration `2 Days`, Status baris `Overdue`, Max duration `10 Days`, Activity Lock `In Audit`.
  - DU-079-26: Baris Borrow, Baris Borrowed dengan aset Under Maintenance: BRW `BRW 16`, Borrower `Rina Wijaya {runId}`, Asset Name `Mesin Bor Listrik {runId}`, Category `Peralatan Lapangan`, Duration `3 Days`, Status baris `Borrowed`, Max duration `10 Days`, Activity Lock `Under Maintenance`.
  - DU-079-27: Baris Borrow, Baris dengan Extension Approval menunggu yang akan dilaporkan rusak Borrower: BRW `BRW 17`, Borrower `Rina Wijaya {runId}`, Asset Name `Kamera Canon EOS {runId}`, Category `Kamera`, Duration `3 Days`, Status baris `Borrowed`, Max duration `10 Days`, Max extensions `3`, Extension menunggu `approval oleh Sari Dewi {runId}`.
  - DU-079-28: Baris Borrow, Baris dengan Extension Request menunggu review yang akan dilaporkan rusak Asset Admin: BRW `BRW 18`, Borrower `Rina Wijaya {runId}`, Asset Name `Lensa Sigma {runId}`, Category `Kamera`, Duration `3 Days`, Status baris `Borrowed`, Max duration `10 Days`, Max extensions `3`, Extension menunggu `review Aktor Borrow`.
  - DU-079-29: Baris Borrow, Baris dengan Extension Approval menunggu yang akan dilaporkan hilang Borrower: BRW `BRW 19`, Borrower `Rina Wijaya {runId}`, Asset Name `Genset Portable {runId}`, Category `Peralatan Lapangan`, Duration `3 Days`, Status baris `Borrowed`, Max duration `10 Days`, Max extensions `3`, Extension menunggu `approval oleh Sari Dewi {runId}`.
  - DU-079-30: Baris Borrow, Baris dengan Extension Approval menunggu yang akan dikembalikan: BRW `BRW 20`, Borrower `Rina Wijaya {runId}`, Asset Name `Drone Mini {runId}`, Category `Drone`, Duration `3 Days`, Status baris `Borrowed`, Max duration `10 Days`, Max extensions `3`, Extension menunggu `approval oleh Sari Dewi {runId}`.
  - DU-079-31: Baris Borrow, Baris dengan Extension Request menunggu review yang akan dikembalikan: BRW `BRW 21`, Borrower `Rina Wijaya {runId}`, Asset Name `Meja Rapat Lipat {runId}`, Category `Furnitur`, Duration `3 Days`, Status baris `Borrowed`, Max duration `10 Days`, Max extensions `3`, Extension menunggu `review Aktor Borrow`.
  - DU-079-32: Baris Borrow, Baris yang diajukan Extend oleh Borrower dan butuh approval: BRW `BRW 22`, Borrower `Rina Wijaya {runId}`, Asset Name `Gimbal DJI {runId}`, Category `Kamera`, Duration `2 Days`, Status baris `Borrowed`, Max duration `10 Days`, Max extensions `3`, Self service `OFF`, Auto-approve `3 days`, Require approval `ON`, Approver `Sari Dewi {runId}`.
  - DU-079-33: Baris Borrow, Baris yang pengajuan Extend-nya ditarik Borrower: BRW `BRW 23`, Borrower `Rina Wijaya {runId}`, Asset Name `Tripod Mini {runId}`, Category `Aksesori Kamera`, Duration `3 Days`, Status baris `Borrowed`, Max duration `10 Days`, Max extensions `3`, Self service `OFF`, Extension menunggu `review Aktor Borrow`.
  - DU-079-34: Baris Borrow, Baris dengan Extension Request menunggu review yang dibuka dua Asset Admin: BRW `BRW 24`, Borrower `Rina Wijaya {runId}`, Asset Name `Tablet Samsung {runId}`, Category `Tablet`, Duration `3 Days`, Status baris `Borrowed`, Max duration `10 Days`, Max extensions `3`, Self service `OFF`, Auto-approve `3 days`, Require approval `OFF`, Extension menunggu `review Aktor Borrow`.
  - DU-079-35: Baris Borrow, Baris dengan Extension Request menunggu review yang semua Approve Duration-nya 0: BRW `BRW 25`, Borrower `Rina Wijaya {runId}`, Asset Name `Stylus Pen {runId}`, Category `Aksesori Tablet`, Duration `3 Days`, Status baris `Borrowed`, Max duration `10 Days`, Max extensions `3`, Self service `OFF`, Extension menunggu `review Aktor Borrow`.
  - DU-079-36: Baris Borrow, Baris dengan Self service ON pada snapshot baris: BRW `BRW 26`, Borrower `Rina Wijaya {runId}`, Asset Name `Headset Logitech {runId}`, Category `Aksesori Audio`, Duration `2 Days`, Status baris `Borrowed`, Max duration `10 Days`, Max extensions `3`, Self service `ON`, Require approval `OFF`.
  - DU-079-37: Baris Borrow, Baris dengan Extension Approval menunggu yang Due date-nya lewat lalu ditolak: BRW `BRW 27`, Borrower `Rina Wijaya {runId}`, Asset Name `Printer Label {runId}`, Category `Printer`, Duration `1 Days`, Status baris `Borrowed`, Max duration `10 Days`, Max extensions `3`, Extension menunggu `approval oleh Sari Dewi {runId}`, Notifikasi Overdue `belum pernah dikirim`.
  - DU-079-38: Baris Borrow, Baris dengan Extension Approval menunggu sampai Transaction timeout: BRW `BRW 28`, Borrower `Rina Wijaya {runId}`, Asset Name `Lampu Studio {runId}`, Category `Peralatan Studio`, Duration `3 Days`, Status baris `Borrowed`, Max duration `10 Days`, Max extensions `3`, Extension menunggu `approval oleh Sari Dewi {runId}`.
  - DU-079-39: Baris Borrow, Baris dengan Extension Request menunggu review sampai Transaction timeout: BRW `BRW 29`, Borrower `Rina Wijaya {runId}`, Asset Name `Reflektor Studio {runId}`, Category `Peralatan Studio`, Duration `3 Days`, Status baris `Borrowed`, Max duration `10 Days`, Max extensions `3`, Extension menunggu `review Aktor Borrow`.
  - DU-079-40: Baris Borrow, Baris dengan Extension Approval menunggu yang dibatalkan pengaju saat approver membuka Review: BRW `BRW 30`, Borrower `Rina Wijaya {runId}`, Asset Name `Kabel Roll {runId}`, Category `Peralatan Studio`, Duration `3 Days`, Status baris `Borrowed`, Max duration `10 Days`, Max extensions `3`, Extension menunggu `approval oleh Sari Dewi {runId}`.
  - DU-079-41: Baris Borrow, Baris pertama dari BRW yang sama yang diajukan Extend pada waktu berbeda: BRW `BRW 31 bersama DU-079-42`, Borrower `Rina Wijaya {runId}`, Asset Name `Kamera Fujifilm {runId}`, Category `Kamera`, Duration `2 Days`, Status baris `Borrowed`, Max duration `10 Days`, Max extensions `3`, Require approval `ON`, Approver `Sari Dewi {runId}`.
  - DU-079-42: Baris Borrow, Baris kedua dari BRW yang sama yang diajukan Extend pada waktu berbeda: BRW `BRW 31 bersama DU-079-41`, Borrower `Rina Wijaya {runId}`, Asset Name `Lensa Fujinon {runId}`, Category `Kamera`, Duration `2 Days`, Status baris `Borrowed`, Max duration `10 Days`, Max extensions `3`, Require approval `ON`, Approver `Sari Dewi {runId}`.
  - DU-079-43: Baris Borrow, Baris yang diajukan Extend bersamaan oleh Borrower dan Asset Admin: BRW `BRW 32`, Borrower `Rina Wijaya {runId}`, Asset Name `Kamera Sony A7 {runId}`, Category `Kamera`, Duration `2 Days`, Status baris `Borrowed`, Max duration `10 Days`, Max extensions `3`, Require approval `ON`, Approver `Sari Dewi {runId}`.
- Kondisi:
  - Bulk Transaction Row Limit berlaku sebagai nilai lingkungan.
  - Setiap baris di atas memakai aturan efektif per baris yang tertulis di entri datanya (Max duration, Max extensions, Auto-approve, Require approval, Self service) sebagai snapshot baris.

## Test Steps

### Extend per baris yang langsung berlaku karena total durasi memenuhi Auto-approve
1. Asset Admin mengirim Extend atas `Laptop Dell Latitude {runId}` dengan Extend by `2 days` dan Reason `Perpanjangan pekerjaan lapangan`
2. Verifikasi Extend diajukan per baris atas `Laptop Dell Latitude {runId}`
3. Verifikasi Extend by dan Reason wajib per baris aktif dan sudah terisi
4. Verifikasi approval dinilai dari total durasi `3 days` sejak handover sampai New due date, bukan dari Extend by `2 days` saja, sehingga Auto-approve `3 days` terpenuhi dan Extend langsung berlaku
5. Verifikasi Due date menjadi New due date dan jumlah Extend bertambah satu
6. Verifikasi `borrow_extension_resolved` (Applied) dikirim
7. Verifikasi New due date dihitung saat Submit dari Due date saat ini
8. Verifikasi ambang Due date reminders dihitung ulang terhadap Due date baru
9. Verifikasi Extend yang diajukan Asset Admin tidak melewati review Extend ajuan Borrower
10. Verifikasi baris dievaluasi dengan snapshot baris
11. Verifikasi Extend tidak butuh scan
12. Verifikasi syarat per baris terpenuhi: New due date lebih besar dari Due date saat ini, total handover sampai New due date tidak melebihi Max duration `10 Days`, dan jumlah perpanjangan sesudahnya tidak melebihi Max extensions `2`

### Extend yang butuh approval, satu pengajuan per BRW, dan keputusan per aset
13. Asset Admin mengirim Extend atas `Proyektor Epson {runId}` dengan Extend by `2 days` dan atas `Kamera Mirrorless {runId}` dengan Extend by `3 days`, keduanya dengan Reason `Perpanjangan pekerjaan lapangan`, dalam satu Submit
14. Verifikasi total durasi `4 days` pada `Proyektor Epson {runId}` melewati Auto-approve `3 days` sehingga masuk pengajuan approval tipe `Extension` baru
15. Verifikasi kedua baris dari BRW yang sama masuk satu pengajuan `Extension`
16. Verifikasi selama menunggu Due date lama tetap berlaku
17. Asset Admin mengirim Extend kedua atas `Proyektor Epson {runId}` selagi pengajuan pertama menunggu
18. Verifikasi Extend kedua ditolak dengan pesan `An extension is already waiting for approval.`
19. Approver `Sari Dewi {runId}` menyetujui `Proyektor Epson {runId}` dan menolak `Kamera Mirrorless {runId}` dengan Approval note `Stok kamera dibutuhkan tim lain`
20. Verifikasi pengajuan Extension berisi beberapa baris diputuskan per aset oleh approver masing-masing
21. Verifikasi status pengajuan menjadi `Partially Approved` karena satu aset disetujui dan satu ditolak
22. Verifikasi New due date `Proyektor Epson {runId}` dihitung saat keputusan akhir approver
23. Verifikasi Due date `Proyektor Epson {runId}` menjadi New due date dan jumlah Extend bertambah satu
24. Verifikasi Due date `Kamera Mirrorless {runId}` tetap karena Extension ditolak
25. Verifikasi jumlah Extend `Kamera Mirrorless {runId}` tidak bertambah
26. Verifikasi `borrow_extension_resolved` (Rejected) memuat reason `Stok kamera dibutuhkan tim lain`

### Extend saat Overdue
27. Asset Admin mengirim Extend atas `Monitor Samsung {runId}` yang `Overdue` dengan Extend by `2 days` dan Reason `Perpanjangan pekerjaan lapangan`
28. Verifikasi Extend saat Overdue diperbolehkan
29. Verifikasi baris kembali `Borrowed` karena Extend berlaku
30. Verifikasi Extend berlaku langsung karena Require approval `OFF`
31. Verifikasi New due date dihitung dari hari ini karena baris `Overdue`

### Batas Max duration dan Max extensions
32. Asset Admin mengirim Extend atas `Speaker Portable JBL {runId}` yang total handover sampai Due date saat ini sudah sama dengan Max duration `5 Days`
33. Verifikasi Extend ditolak dengan alasan `Max duration reached (5 Days).`
34. Verifikasi Due date `Speaker Portable JBL {runId}` tidak berubah
35. Asset Admin mengirim Extend atas `Mikrofon Wireless Shure {runId}` yang Max extensions-nya sudah terpakai
36. Verifikasi Extend ditolak dengan alasan `No extensions left (1 / 1).`
37. Verifikasi batas Extend adalah Max duration total sejak handover termasuk semua perpanjangan, dan Max extensions
38. Asset Admin mengirim Extend atas `Speaker Portable JBL {runId}` dan `Mikrofon Wireless Shure {runId}` yang keduanya nonaktif
39. Verifikasi server menolak Submit itu dengan pesan `None of these assets can be extended`
40. Verifikasi Submit tetap diterima walau semua baris nonaktif
41. Verifikasi tidak ada baris yang diajukan
42. Asset Admin mengirim Extend atas `Tripod Kamera {runId}` dengan Extend by `6 days` dan atas `Walkie Talkie Motorola {runId}` dengan Extend by `8 hours`, dengan Reason `Perpanjangan pekerjaan lapangan`, dalam satu Submit
43. Verifikasi Extend by dihitung per satuan dan tiap baris dihitung dari Due date-nya sendiri
44. Verifikasi server menolak `Tripod Kamera {runId}` dengan pesan `Max 7 days in total. You can extend until [Date].`
45. Verifikasi server menolak `Walkie Talkie Motorola {runId}` dengan pesan `Max 12 hours in total. You can extend until [Date] [Time].`
46. Verifikasi baris yang melewati batas tetap terisi setelah penolakan
47. Verifikasi baris yang sudah di batas tetap nonaktif pada Submit yang sama
48. Asset Admin mengirim Extend atas `Meeting Mic Set {runId}` dengan Due date saat ini `22:00`, Extend by `4 hours`, dan Reason `Perpanjangan pekerjaan lapangan`
49. Verifikasi Current Due Date dan New Due Date baris Hours menyimpan tanggal dan jam
50. Verifikasi New due date adalah Due date saat ini + Extend by, yaitu `02:00` pada hari berikutnya
51. Asset Admin mengirim Extend atas `Mixer Audio {runId}` yang `Overdue` dengan Extend by `2 hours` dan Reason `Perpanjangan pekerjaan lapangan`
52. Verifikasi New due date baris Hours yang Due date-nya sudah lewat dihitung dari waktu saat Due date baru ditetapkan

### Validasi isian Extend per baris aktif
53. Asset Admin mengirim Extend atas `Router Cisco {runId}` tanpa mengisi Extend by
54. Verifikasi server menolak dengan pesan `Extend by must not be empty`
55. Asset Admin mengirim Extend atas `Router Cisco {runId}` dengan Extend by `0`
56. Verifikasi server menolak dengan pesan `Enter an extension of at least 1`
57. Asset Admin mengirim Extend atas `Router Cisco {runId}` dengan Extend by `1.5`
58. Verifikasi server menolak Extend by yang bukan bilangan bulat positif dengan pesan `Enter an extension of at least 1`
59. Asset Admin mengirim Extend atas `Router Cisco {runId}` dengan Extend by `2 days` tanpa mengisi Reason
60. Verifikasi server menolak dengan pesan `Reason must not be empty`
61. Verifikasi tidak ada baris yang diajukan sampai semua baris aktif terisi dan valid atau dikeluarkan

### Extend lintas BRW, atomik per BRW, dan batas jumlah baris
62. Asset Admin mengirim Extend atas `Kursi Lipat Rapat {runId}` dengan Extend by `2 days` dan atas `Papan Tulis {runId}` dengan Extend by `2 days`, dengan Reason `Perpanjangan pekerjaan lapangan`, dalam satu Submit
63. Verifikasi pada BRW 9 Due date baru `Kursi Lipat Rapat {runId}` langsung berlaku
64. Verifikasi pada BRW 10 `Papan Tulis {runId}` menjadi satu pengajuan `Extension` ber-Transaction ID BRW 10
65. Verifikasi hasil campuran dalam satu Submit dikembalikan per hasil dengan toast `Success, due date has been changed for [Changed] of [Total] assets. [Submitted] submitted for approval.`
66. Verifikasi Due date `Kursi Lipat Cadangan {runId}` yang tidak diperpanjang berbeda dari Due date `Kursi Lipat Rapat {runId}`
67. Baris `Proyektor Mini {runId}` dikembalikan oleh Asset Admin lain sesaat sebelum Submit
68. Asset Admin mengirim Extend atas `Proyektor Mini {runId}`, `Layar Proyektor {runId}`, dan `Spotlight LED {runId}` dengan Extend by `2 days` dan Reason `Perpanjangan pekerjaan lapangan`, dalam satu Submit
69. Verifikasi BRW 12 tetap tersimpan walau BRW 11 gagal
70. Verifikasi baris BRW 11 yang gagal tetap dengan pesan error
71. Verifikasi Due date `Layar Proyektor {runId}` tidak berubah karena tidak ada perubahan sebagian di dalam satu BRW
72. Asset Admin mengirim Extend atas `Aset Pinjam Batas {n} {runId}` sejumlah Bulk Transaction Row Limit ditambah satu
73. Verifikasi server menolak Submit itu dengan Dialog Blok `D-BRW-18` dan tidak ada baris yang diproses
74. Verifikasi isian tidak direset

### Aset terkunci: Extend tidak ditawarkan, Extension menunggu tidak terpengaruh
75. Aset `Printer Warna Epson {runId}` menjadi Unmanaged saat Extension Approval menunggu
76. Asset Admin mengirim Extend atas `Printer Warna Epson {runId}`
77. Verifikasi Extend ditolak dengan alasan `This asset is [Status] and can't be extended.`
78. Verifikasi Extension yang sudah menunggu tidak diubah oleh penguncian itu
79. Asset Admin mengembalikan `Printer Warna Epson {runId}` yang Unmanaged
80. Verifikasi Return tetap boleh
81. Asset Admin mengirim Extend atas `Server Rack Mini {runId}` yang ber-Activity Lock `In Audit`
82. Verifikasi Extend ditolak dengan alasan `This asset is [Status] and can't be extended.`
83. Asset Admin mengirim laporan rusak atas `Server Rack Mini {runId}`
84. Verifikasi laporan rusak tetap boleh walau aset `In Audit`
85. Asset Admin mengirim laporan hilang atas `Mesin Bor Listrik {runId}` yang ber-Activity Lock `Under Maintenance`
86. Verifikasi laporan hilang tetap boleh walau aset `Under Maintenance`
87. Verifikasi laporan itu tidak mengubah Stock Opname dan Work Order
88. Verifikasi status `Overdue` `Server Rack Mini {runId}` tetap dihitung

### Extension menunggu dibatalkan otomatis oleh System
89. Borrower mengirim laporan rusak atas `Kamera Canon EOS {runId}` yang Extension Approval-nya menunggu
90. Verifikasi pengajuan otomatis `Canceled` oleh System dengan alasan `Damage reported`
91. Verifikasi approver `Sari Dewi {runId}` yang belum bertindak diberi tahu lewat `borrow_extension_resolved` varian Canceled
92. Verifikasi tidak ada notifikasi tambahan ke pengaju
93. Verifikasi Due date `Kamera Canon EOS {runId}` tetap
94. Asset Admin `Maya Putri {runId}` menolak laporan rusak atas `Kamera Canon EOS {runId}`
95. Verifikasi pengajuan tidak dipulihkan karena laporan kemudian Rejected
96. Asset Admin mengirim Extend atas `Kamera Canon EOS {runId}` selagi laporan rusak aktif
97. Verifikasi Extend ditolak dengan pesan `This asset has a damage report. Return it first.`
98. Asset Admin mengirim laporan rusak atas `Lensa Sigma {runId}` yang Extension Request-nya menunggu review
99. Verifikasi Extension Request itu otomatis `Canceled` dengan alasan `Damage reported`
100. Borrower mengirim laporan hilang atas `Genset Portable {runId}` yang Extension Approval-nya menunggu
101. Verifikasi Extend atas `Genset Portable {runId}` ditolak dengan pesan `This asset is reported missing.`
102. Verifikasi Extension yang menunggu otomatis `Canceled` oleh System dengan alasan `Asset reported missing`
103. Asset Admin `Maya Putri {runId}` menolak laporan hilang atas `Genset Portable {runId}`
104. Verifikasi Extension tidak dipulihkan karena laporan kemudian Rejected
105. Asset Admin mengembalikan `Drone Mini {runId}` yang Extension Approval-nya menunggu
106. Verifikasi Extension untuk baris itu otomatis `Canceled` dengan alasan `Asset returned`
107. Verifikasi `borrow_extension_resolved` varian Canceled dikirim ke approver item Extension itu yang belum bertindak
108. Verifikasi pengajuan berisi beberapa baris hanya mengeluarkan baris itu dan pengajuan kosong menjadi `Canceled`
109. Asset Admin mengembalikan `Meja Rapat Lipat {runId}` yang Extension Request-nya menunggu review
110. Verifikasi pengajuan baris itu ditutup otomatis
111. Verifikasi pengajuan baris itu tidak tampil di halaman Review

### Extend ajuan Borrower direview Asset Admin lebih dulu
112. Borrower mengirim Extension Request atas `Gimbal DJI {runId}` dan `Headset Logitech {runId}` dengan Extend by `2 days` dan Reason `Perpanjangan pekerjaan lapangan`, dalam satu Submit
113. Verifikasi Extend ajuan Borrower direview Asset Admin lebih dulu dan tidak langsung berlaku
114. Verifikasi pengajuan tidak langsung masuk pengajuan approval dan baris berstatus `Extension Request` dengan Due date lama tetap
115. Verifikasi pengajuan memuat Extend by, New due date, dan Reason dari Borrower
116. Verifikasi pengajuan review tercatat per BRW dan baris itu tidak dapat diajukan Extend lagi selama menunggu
117. Asset Admin `Agus Pratama {runId}` mereview `Gimbal DJI {runId}` dengan Approve dan Approve Duration `1 days`
118. Verifikasi review per aset memuat Approval, Approve Duration yang tidak melebihi Extend by yang diminta, dan Approval Note
119. Verifikasi aset Approve dihitung ulang dengan Approve Duration `1 days` sebagai New due date dan masuk pengajuan approval tipe `Extension` karena Auto-approve `3 days` tidak terpenuhi
120. Verifikasi Requested By adalah `Agus Pratama {runId}` dan Request Date adalah waktu penerusan, sedangkan Borrower tetap `Rina Wijaya {runId}`
121. Verifikasi `Agus Pratama {runId}` dikeluarkan dari daftar approver oleh self-approval guard
122. Borrower menarik pengajuan atas `Tripod Mini {runId}` dengan `Cancel Extension Request`
123. Verifikasi Due date tetap setelah pengajuan ditarik
124. Verifikasi status header dan status tampil baris kembali diturunkan dari data baris
125. Verifikasi baris `Headset Logitech {runId}` yang Self service-nya `ON` pada snapshot baris langsung berlaku tanpa review
126. Verifikasi hasil campuran dalam satu Submit memakai toast `Success, due date has been changed for [Changed] of [Total] assets. [Submitted] sent for review.`
127. Asset Admin `Agus Pratama {runId}` dan `Tika Rahma {runId}` membuka review `Tablet Samsung {runId}`
128. Asset Admin `Agus Pratama {runId}` mengirim review `Tablet Samsung {runId}` dengan Approve dan Approve Duration `1 days` lebih dulu
129. Verifikasi aset Approve dihitung ulang dengan Approve Duration `1 days` dan langsung berlaku karena Auto-approve `3 days` terpenuhi
130. Verifikasi cukup satu Asset Admin yang mereview
131. Verifikasi review `Tika Rahma {runId}` yang masuk kedua mendapat Dialog Blok `D-BRW-16` saat Submit
132. Verifikasi keputusan `Tika Rahma {runId}` yang masuk kedua tidak disimpan
133. Asset Admin mereview `Stylus Pen {runId}` dengan Approve dan Approve Duration `0 days`
134. Verifikasi Approve dengan Approve Duration 0 dihitung Reject
135. Verifikasi pengajuan ditutup, Due date tetap, dan header kembali diturunkan dari baris

### Extension ditolak, timeout, dibatalkan, dan pengajuan terpisah per waktu
136. Waktu berlalu sampai Due date `Printer Label {runId}` lewat saat Extension Approval-nya menunggu
137. Verifikasi baris menjadi `Overdue` dengan Due date lama selama pengajuan menunggu dan notifikasi Overdue tetap dikirim
138. Approver `Sari Dewi {runId}` menolak Extension `Printer Label {runId}` dengan Approval note `Stok kamera dibutuhkan tim lain`
139. Verifikasi baris tetap `Overdue` dengan Due date lama
140. Verifikasi notifikasi Overdue dikirim karena belum pernah dikirim untuk baris itu
141. Verifikasi Borrower menerima reason penolakan
142. Transaction timeout berlalu atas Extension Approval `Lampu Studio {runId}`
143. Verifikasi Extension `Canceled` oleh System dengan alasan `Timed out (Waiting for Approval)` dan node `Extension canceled`
144. Verifikasi baris kembali `Borrowed` (`Overdue` bila Due date lama sudah lewat)
145. Verifikasi Due date tetap dan jumlah Extend tidak bertambah
146. Verifikasi baris tidak kembali ke Draft
147. Verifikasi `borrow_extension_resolved` (Timed out) dikirim ke Borrower dan ke approver yang belum bertindak
148. Transaction timeout berlalu atas Extension Request `Reflektor Studio {runId}` yang menunggu review
149. Verifikasi Extension `Canceled` oleh System dengan alasan `Timed out (Waiting for Review)`
150. Approver `Sari Dewi {runId}` membuka Review Extension `Kabel Roll {runId}`
151. Pengaju membatalkan Extension `Kabel Roll {runId}` lewat `Cancel Extension`
152. Verifikasi approver melihat `D-BRW-09` varian Canceled
153. Verifikasi keputusan approver yang belum dikirim dibuang
154. Verifikasi Extension baris itu `Canceled`
155. Verifikasi Due date tetap dan jumlah Extend tidak bertambah
156. Verifikasi pengajuan `Canceled` dan hilang dari antrean approver bila tidak ada aset yang tersisa
157. Verifikasi `borrow_extension_resolved` varian Canceled dikirim ke approver item Extension itu yang belum bertindak, tanpa notifikasi tambahan ke pengaju
158. Asset Admin mengirim Extend atas `Kamera Fujifilm {runId}` dengan Extend by `3 days` dan Reason `Perpanjangan pekerjaan lapangan`
159. Asset Admin mengirim Extend atas `Lensa Fujinon {runId}` dengan Extend by `3 days` dan Reason `Perpanjangan pekerjaan lapangan` pada waktu berbeda
160. Verifikasi terbentuk dua pengajuan `Extension` terpisah ber-Transaction ID sama, dibedakan Request Date dan Total Asset
161. Verifikasi snapshot approver, timeout, dan notifikasi dihitung per pengajuan
162. Borrower dan Asset Admin mengajukan Extend atas `Kamera Sony A7 {runId}` bersamaan
163. Verifikasi hanya satu pengajuan `Extension` terbentuk untuk `Kamera Sony A7 {runId}`
164. Verifikasi pengajuan yang ditolak mendapat pesan `An extension is already waiting for approval.`
