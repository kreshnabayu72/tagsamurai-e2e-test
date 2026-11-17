---
id: TC-FA-DAMAGED-BE-212-event-notifikasi
title: "Modul memicu event damaged_reported, damaged_review_requested, damaged_review_resolved, dan damaged_resolved hanya pada kejadian yang ditetapkan, tanpa event untuk jalur modul asal dan transisi Disposal, dan mengirim sinyal task selesai"
layer: be-e2e
priority: Critical
caseType: Positive
status: ready-for-automation
sourceRules: ["damaged_reported", "damaged_review_requested", "damaged_review_resolved", "damaged_resolved", "§9.8#p4", "EC-DMG-19", "§9.4.4#r18", "§9.4.4#r3", "§9.4.4#r7"]
smoke: []
dependsOn: []
owner: BE
trace:
  damaged_reported: [3, 4, 6, 8, 26, 28, 30, 32, 34]
  damaged_review_requested: [10, 12]
  damaged_review_resolved: [14, 16, 18]
  damaged_resolved: [18, 20, 22, 24, 36, 38, 40, 42, 44, 46, 48, 50, 52]
  "§9.8#p4": [54, 55, 56]
  EC-DMG-19: 60
  "§9.4.4#r18": 60
  "§9.4.4#r3": [8, 10]
  "§9.4.4#r7": 6
---

# Modul memicu event damaged_reported, damaged_review_requested, damaged_review_resolved, dan damaged_resolved hanya pada kejadian yang ditetapkan, tanpa event untuk jalur modul asal dan transisi Disposal, dan mengirim sinyal task selesai

## Prerequisites
- Aktor:
  - Total Control `Agus Pratama {runId}`, Aktor Damaged.
  - Pemegang Manage asset & TAG (Update) `Rina Wulandari {runId}`, Aktor Damaged pada Group `Head Office {runId}`.
  - Aktor peminjaman `Yoga Tanuwijaya {runId}`, Aktor penugasan `Dewi Anggraini {runId}`, Aktor penemuan aset `Hendra Saputra {runId}`, dan Aktor pelepasan aset `Maya Puspita {runId}`.
  - Pelapor umum `Budi Santoso {runId}`, `Dedi Kurniawan {runId}`, dan `Hana Lestari {runId}`, tanpa role Damaged.
- Data:
  - DU-212-1: User `Agus Pratama {runId}`, Total Control, cakupan seluruh client.
  - DU-212-2: User `Rina Wulandari {runId}`, Manage asset & TAG (Update), cakupan Group `Head Office {runId}` beserta descendant.
  - DU-212-3: User `Yoga Tanuwijaya {runId}`, Aktor Borrow, cakupan Group `Head Office {runId}`.
  - DU-212-4: User `Dewi Anggraini {runId}`, Aktor Assignment, cakupan Group `Head Office {runId}`.
  - DU-212-5: User `Hendra Saputra {runId}`, Aktor Missing, cakupan Group `Head Office {runId}`.
  - DU-212-6: User `Maya Puspita {runId}`, Asset Admin sub-tab Disposal, cakupan Group `Head Office {runId}`.
  - DU-212-7: User `Budi Santoso {runId}`, pelapor umum, pemegang aset, cakupan aset yang ia pegang.
  - DU-212-8: User `Dedi Kurniawan {runId}`, pelapor umum, pemindai TAG, cakupan aset yang ia pindai.
  - DU-212-9: User `Hana Lestari {runId}`, pelapor umum, pemegang aset yang kemudian dinonaktifkan, cakupan aset yang ia pegang.
  - DU-212-10: Group `Head Office {runId}`.
  - DU-212-11: Aset `Laptop Dell Latitude 5420 - 301 {runId}`, Group `Head Office {runId}`, `Normal`, tanpa record berjalan.
  - DU-212-12: Aset `Tablet Samsung Tab A8 - 302 {runId}`, Group `Head Office {runId}`, `Assigned` kepada `Rina Wulandari {runId}`, tanpa record berjalan.
  - DU-212-13: Aset `Projector Epson EB-X06 - 303 {runId}`, Group `Head Office {runId}`, `Borrowed` oleh `Budi Santoso {runId}`, tanpa record berjalan.
  - DU-212-14: Aset `Monitor Dell P2422H - 304 {runId}`, Group `Head Office {runId}`, `Assigned` kepada `Budi Santoso {runId}`, tanpa record berjalan.
  - DU-212-15: Aset `Office Chair Ergo - 305 {runId}`, Group `Head Office {runId}`, `Normal`, tanpa record berjalan.
  - DU-212-16: Aset `Camera Canon EOS - 311 {runId}`, Group `Head Office {runId}`, punya record `Waiting for Confirmation` dari laporan `Budi Santoso {runId}`.
  - DU-212-17: Aset `Camera Canon EOS - 312 {runId}`, Group `Head Office {runId}`, punya record `Waiting for Confirmation` dari laporan `Budi Santoso {runId}`.
  - DU-212-18: Aset `Camera Canon EOS - 313 {runId}`, Group `Head Office {runId}`, punya record `Waiting for Confirmation` dari laporan `Budi Santoso {runId}`.
  - DU-212-19: Aset `Printer HP LaserJet M404 - 321 {runId}`, Group `Head Office {runId}`, TAG `RFID-C321 {runId}`, punya record `Damaged`.
  - DU-212-20: Aset `Printer HP LaserJet M404 - 322 {runId}`, Group `Head Office {runId}`, punya record `In Disposal Process` dengan baris pelepasan aset yang akan dieksekusi.
  - DU-212-21: Aset `Printer HP LaserJet M404 - 323 {runId}`, Group `Head Office {runId}`, `Missing` dengan record `Damaged` ditahan yang akan menjadi `Disposed`.
  - DU-212-22: Aset `Tablet Samsung Tab A8 - 331 {runId}`, Group `Head Office {runId}`, `Borrowed` oleh `Budi Santoso {runId}`, tanpa record berjalan.
  - DU-212-23: Aset `Tablet Samsung Tab A8 - 332 {runId}`, Group `Head Office {runId}`, `Assigned` kepada `Budi Santoso {runId}`, tanpa record berjalan.
  - DU-212-24: Aset `Tablet Samsung Tab A8 - 333 {runId}`, Group `Head Office {runId}`, `Missing` dengan record `Damaged` ditahan.
  - DU-212-25: Aset `Tablet Samsung Tab A8 - 334 {runId}`, Group `Head Office {runId}`, draf registrasi ber-Condition `Damaged`, belum Active.
  - DU-212-26: Aset `Tablet Samsung Tab A8 - 335 {runId}`, Group `Head Office {runId}`, termasuk sesi opname milik `Agus Pratama {runId}`, tanpa record berjalan.
  - DU-212-27: Aset `Forklift Toyota 8FD - 341 {runId}`, Group `Head Office {runId}`, punya record `Damaged`.
  - DU-212-28: Aset `Forklift Toyota 8FD - 342 {runId}`, Group `Head Office {runId}`, punya record `Reported Disposal`.
  - DU-212-29: Aset `Forklift Toyota 8FD - 344 {runId}`, Group `Head Office {runId}`, punya record `In Disposal Process` dengan baris pelepasan aset yang akan kedaluwarsa.
  - DU-212-30: Aset `Drill Bosch GSB - 351 {runId}`, Group `Head Office {runId}`, TAG `RFID-H351 {runId}`, punya record `Waiting for Confirmation` dari laporan `Hana Lestari {runId}`.
  - DU-212-31: Aset `Drill Bosch GSB - 352 {runId}`, Group `Head Office {runId}`, punya record `Waiting for Confirmation` dari laporan `Budi Santoso {runId}`.
  - DU-212-32: What happened `Layar retak setelah terjatuh dari meja {runId}`, Damaged Photo `layar-retak.jpg`.
  - DU-212-33: Reason `Foto yang dikirim bukan foto aset ini {runId}`.
  - DU-212-34: Repair note `Komponen rusak sudah diganti {runId}`.
  - DU-212-35: Description `Engsel longgar saat dikembalikan {runId}`, foto Return `foto-return.jpg`.
  - DU-212-36: Description `Layar tergores saat dikembalikan {runId}`, foto Unassign `foto-unassign.jpg`.
  - DU-212-37: Note `Ditemukan rusak di ruang arsip {runId}`, Damaged Photo `ditemukan-rusak.jpg`.
  - DU-212-38: Aset `Forklift Toyota 8FD - 345 {runId}`, Group `Head Office {runId}`, punya record `Reported Disposal` dari laporan `Maya Puspita {runId}`.
  - DU-212-39: Aset `Forklift Toyota 8FD - 346 {runId}`, Group `Head Office {runId}`, punya record `Reported Disposal`.
  - DU-212-40: Aset `Forklift Toyota 8FD - 347 {runId}`, Group `Head Office {runId}`, punya record `In Disposal Process` dengan baris pelepasan aset yang akan ditolak.
  - DU-212-41: Aset `Forklift Toyota 8FD - 348 {runId}`, Group `Head Office {runId}`, punya record `In Disposal Process` dengan baris pelepasan aset yang akan dibatalkan.
  - DU-212-42: Aset `Forklift Toyota 8FD - 349 {runId}`, Group `Head Office {runId}`, punya record `In Disposal Process` dengan baris pelepasan aset yang akan dihapus.

## Test Steps

### Report Damaged oleh Pelapor admin memicu damaged_reported, sedangkan laporan dari halaman peminjaman tidak
1. Catat jumlah event `damaged_reported`, `damaged_review_requested`, `damaged_review_resolved`, dan `damaged_resolved` untuk aset uji
2. Total Control `Agus Pratama {runId}` mengirim Report Damaged atas `Laptop Dell Latitude 5420 - 301 {runId}` dengan What happened `Layar retak setelah terjatuh dari meja {runId}` dan Damaged Photo `layar-retak.jpg`
3. Verifikasi tepat satu event `damaged_reported` dipicu untuk record itu
4. Verifikasi tidak ada event `damaged_review_requested` untuk record itu
5. Pemegang Update `Rina Wulandari {runId}` mengirim Report Damaged atas `Tablet Samsung Tab A8 - 302 {runId}` yang ia pegang dari halaman aset yang dipegangnya dengan What happened `Layar retak setelah terjatuh dari meja {runId}` dan Damaged Photo `layar-retak.jpg`
6. Verifikasi event `damaged_reported` dipicu karena record langsung `Damaged` sebagai Pelapor admin, bukan `damaged_review_requested`
7. Aktor peminjaman `Yoga Tanuwijaya {runId}` mengirim Report Damaged atas `Projector Epson EB-X06 - 303 {runId}` yang sedang dipinjam dari halaman transaksi peminjaman dengan What happened `Layar retak setelah terjatuh dari meja {runId}` dan Damaged Photo `layar-retak.jpg`
8. Verifikasi tidak ada event `damaged_reported` maupun `damaged_review_requested` dipicu karena notifikasinya dimiliki modul asal, dan baris peminjaman tidak berubah

### Report Damaged oleh pelapor umum memicu damaged_review_requested
9. Pelapor umum `Budi Santoso {runId}` mengirim Report Damaged atas `Monitor Dell P2422H - 304 {runId}` yang ia pegang dari halaman aset yang dipegangnya dengan What happened `Layar retak setelah terjatuh dari meja {runId}` dan Damaged Photo `layar-retak.jpg`
10. Verifikasi tepat satu event `damaged_review_requested` dipicu dan tidak ada event `damaged_reported`
11. Pelapor umum `Dedi Kurniawan {runId}` mengirim Report Damaged atas `Office Chair Ergo - 305 {runId}` dari hasil scan TAG di mobile dengan What happened `Layar retak setelah terjatuh dari meja {runId}` dan Damaged Photo `layar-retak.jpg`
12. Verifikasi tepat satu event `damaged_review_requested` dipicu dan tidak ada event `damaged_reported`

### Confirm dan Reject memicu damaged_review_resolved, Cancel Report tidak
13. Total Control `Agus Pratama {runId}` melakukan Confirm atas laporan `Camera Canon EOS - 311 {runId}`
14. Verifikasi tepat satu event `damaged_review_resolved` dipicu untuk pelapor `Budi Santoso {runId}`
15. Total Control `Agus Pratama {runId}` melakukan Reject atas laporan `Camera Canon EOS - 312 {runId}` dengan Reason `Foto yang dikirim bukan foto aset ini {runId}`
16. Verifikasi tepat satu event `damaged_review_resolved` dipicu
17. Pelapor umum `Budi Santoso {runId}` melakukan Cancel Report atas `Camera Canon EOS - 313 {runId}`
18. Verifikasi tidak ada event `damaged_*` yang dipicu oleh pembatalan itu

### Mark as Repaired dan Disposed memicu damaged_resolved
19. Total Control `Agus Pratama {runId}` menjalankan Mark as Repaired atas `Printer HP LaserJet M404 - 321 {runId}` dengan Scan TAG `RFID-C321 {runId}` milik aset dan Repair note `Komponen rusak sudah diganti {runId}`
20. Verifikasi tepat satu event `damaged_resolved` dipicu saat record menjadi `Repaired`
21. Pelepasan aset `Printer HP LaserJet M404 - 322 {runId}` dieksekusi (Executed)
22. Verifikasi tepat satu event `damaged_resolved` dipicu saat record menjadi `Disposed` karena pelepasan aset dieksekusi
23. Aset hilang `Printer HP LaserJet M404 - 323 {runId}` dilepas menjadi Disposed
24. Verifikasi tepat satu event `damaged_resolved` dipicu saat record menjadi `Disposed` dari aset hilang

### Jalur modul asal tidak memicu event damaged
25. Aktor peminjaman `Yoga Tanuwijaya {runId}` mengirim Report Damaged dari halaman Return Borrow atas `Tablet Samsung Tab A8 - 331 {runId}` dengan Description `Engsel longgar saat dikembalikan {runId}` dan foto Return `foto-return.jpg`
26. Verifikasi record `Waiting for Confirmation` dibuat tanpa event `damaged_reported` maupun `damaged_review_requested`, karena notifikasinya dimiliki modul asal
27. Aktor penugasan `Dewi Anggraini {runId}` melakukan Unassign berstatus `Unassigned` bermarker `Damaged` atas `Tablet Samsung Tab A8 - 332 {runId}` dengan Description `Layar tergores saat dikembalikan {runId}` dan foto Unassign `foto-unassign.jpg`
28. Verifikasi record `Damaged` dibuat tanpa event `damaged_*`
29. Aktor penemuan aset `Hendra Saputra {runId}` menjalankan Mark as Found Damaged atas `Tablet Samsung Tab A8 - 333 {runId}` dengan Note `Ditemukan rusak di ruang arsip {runId}` dan Damaged Photo `ditemukan-rusak.jpg`
30. Verifikasi node ditambahkan tanpa event `damaged_*`, karena notifikasinya dimiliki modul asal
31. Total Control `Agus Pratama {runId}` mengaktifkan registrasi `Tablet Samsung Tab A8 - 334 {runId}` yang ber-Condition `Damaged`
32. Verifikasi record otomatis dibuat tanpa notifikasi dan tanpa event `damaged_*`
33. Pemilik sesi opname `Agus Pratama {runId}` melaporkan kondisi rusak atas `Tablet Samsung Tab A8 - 335 {runId}` dari sesinya
34. Verifikasi record `Damaged` dibuat tanpa event `damaged_*`

### Transisi pelepasan aset tidak memicu event damaged
35. Total Control `Agus Pratama {runId}` menjalankan Report Disposal atas `Forklift Toyota 8FD - 341 {runId}` dengan Reason `Unit sudah tidak ekonomis untuk diperbaiki {runId}`
36. Verifikasi tidak ada event `damaged_*` dipicu saat record menjadi `Reported Disposal`
37. Aktor pelepasan aset `Maya Puspita {runId}` menjalankan Decline atas laporan `Forklift Toyota 8FD - 342 {runId}`
38. Verifikasi tidak ada event `damaged_*` dipicu saat record kembali `Damaged`
39. Aktor pelepasan aset `Maya Puspita {runId}` men-Submit Request atas `Forklift Toyota 8FD - 341 {runId}` yang laporan pelepasan asetnya sudah diterima
40. Verifikasi tidak ada event `damaged_*` dipicu saat record menjadi `In Disposal Process`
41. Baris pelepasan aset `Forklift Toyota 8FD - 344 {runId}` kedaluwarsa (timeout) tanpa user aktor
42. Verifikasi tidak ada event `damaged_*` dipicu saat record kembali `Damaged`
43. Aktor pelepasan aset `Maya Puspita {runId}` menjalankan Cancel Report atas laporan `Forklift Toyota 8FD - 345 {runId}` dari tab Reported
44. Verifikasi tidak ada event `damaged_*` dipicu saat record kembali `Damaged` karena Cancel Report atas laporan pelepasan aset
45. Total Control `Agus Pratama {runId}` menjalankan Cancel Disposal Report atas `Forklift Toyota 8FD - 346 {runId}` dari tab Damaged
46. Verifikasi tidak ada event `damaged_*` dipicu saat record kembali `Damaged` karena Cancel Disposal Report
47. Baris pelepasan aset `Forklift Toyota 8FD - 347 {runId}` ditolak (Reject) oleh approver
48. Verifikasi tidak ada event `damaged_*` dipicu saat record kembali `Damaged` karena baris pelepasan aset ditolak
49. Baris pelepasan aset `Forklift Toyota 8FD - 348 {runId}` dibatalkan (Cancel) oleh pembuatnya
50. Verifikasi tidak ada event `damaged_*` dipicu saat record kembali `Damaged` karena baris pelepasan aset dibatalkan
51. Baris pelepasan aset `Forklift Toyota 8FD - 349 {runId}` dihapus (Remove)
52. Verifikasi tidak ada event `damaged_*` dipicu saat record kembali `Damaged` karena baris pelepasan aset dihapus

### Sinyal task selesai
53. Catat sinyal task selesai untuk `Camera Canon EOS - 311 {runId}`, `Printer HP LaserJet M404 - 321 {runId}`, dan `Forklift Toyota 8FD - 342 {runId}`
54. Verifikasi sinyal task selesai terkirim saat laporan pelapor umum di-Confirm, di-Reject, atau dibatalkan
55. Verifikasi sinyal task selesai terkirim saat record keluar dari `Damaged` menjadi `Repaired` atau `Disposed`
56. Verifikasi tidak ada sinyal task selesai saat record berpindah antara `Damaged` dan `Reported Disposal` atau `In Disposal Process`

### Pelapor yang dinonaktifkan tidak menerima notifikasi penyelesaian
57. User `Hana Lestari {runId}`, pelapor `Drill Bosch GSB - 351 {runId}`, dinonaktifkan
58. Total Control `Agus Pratama {runId}` melakukan Confirm atas laporan `Drill Bosch GSB - 351 {runId}`
59. Total Control `Agus Pratama {runId}` menjalankan Mark as Repaired atas `Drill Bosch GSB - 351 {runId}` dengan Scan TAG `RFID-H351 {runId}` milik aset dan Repair note `Komponen rusak sudah diganti {runId}`
60. Verifikasi record tetap diproses dan notifikasi penyelesaian tidak dikirim ke `Hana Lestari {runId}`
