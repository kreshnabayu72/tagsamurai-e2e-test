---
id: TC-FA-DAMAGED-BE-201-report-damaged-kelayakan-dan-status
title: "Server membuat satu Damage record per aset layak dengan status menurut jenis pelapor dan Source titik masuk, menolak aset ber-record berjalan, Disposed, Missing, di luar cakupan, dan laporan ganda"
layer: be-e2e
priority: Critical
caseType: Negative
status: ready-for-automation
sourceRules: ["§Aturan Logika Modul#r10", "§Aturan Logika Modul#r11", "§Aturan Logika Modul#r12", "§Aturan Logika Modul#r13", "§Aturan Logika Modul#r15", "§Aturan Logika Modul#r16", "§Aturan Logika Modul#r42", "§Aturan Logika Modul#r43", "§Aturan Logika Modul#r44", "§Aturan Logika Modul#r48", "§Aturan Logika Modul#r75", "§9.2#r2", "S-DMG-22", "§9.2#b2", "§9.2#b3", "§9.2#b4", "S-DMG-21", "§4.2.3#b1", "§4.2.3#b4", "§9.4.3#b1", "§9.6#r1", "§3#p2", "V-DMG-10", "EC-DMG-01", "EC-DMG-02", "EC-DMG-04", "EC-DMG-05", "EC-DMG-27", "FLD-DMG-01", "FLD-DMG-02", "§9.4.4#r1", "§9.4.4#r2", "§9.4.4#r5", "§9.4.4#r7", "§2#b6", "§2#b7", "§9.4.1#r6", "§9.4.1#r7", "EB-FRM-4@what-happened", "F-DMG-01"]
smoke: []
dependsOn: []
owner: BE
trace:
  "§Aturan Logika Modul#r10": 5
  "§Aturan Logika Modul#r11": [25, 59, 63, 65]
  "§Aturan Logika Modul#r12": [6, 69, 70, 71]
  "§Aturan Logika Modul#r13": [24, 31, 33]
  "§Aturan Logika Modul#r15": 43
  "§Aturan Logika Modul#r16": 42
  "§Aturan Logika Modul#r42": [2, 87]
  "§Aturan Logika Modul#r43": [15, 18, 20, 22]
  "§Aturan Logika Modul#r44": 4
  "§Aturan Logika Modul#r48": 3
  "§Aturan Logika Modul#r75": 38
  "§9.2#r2": 2
  S-DMG-22: [24, 35, 40, 44, 82, 84]
  "§9.2#b2": [2, 42]
  "§9.2#b3": [25, 31, 33]
  "§9.2#b4": 3
  S-DMG-21: [46, 47]
  "§4.2.3#b1": 35
  "§4.2.3#b4": [40, 85]
  "§9.4.3#b1": [25, 61, 67, 72]
  "§9.6#r1": [7, 9]
  "§3#p2": [2, 15, 16, 79, 80]
  V-DMG-10: [43, 48]
  EC-DMG-01: [29, 43]
  EC-DMG-02: [24, 26]
  EC-DMG-04: 35
  EC-DMG-05: 46
  EC-DMG-27: [11, 13]
  FLD-DMG-01: 51
  FLD-DMG-02: 55
  "§9.4.4#r1": [2, 27, 43]
  "§9.4.4#r2": [35, 36]
  "§9.4.4#r5": 49
  "§9.4.4#r7": 8
  "§2#b6": [2, 11, 12, 82, 84, 87]
  "§2#b7": [15, 18, 20, 22, 74, 76, 77]
  "§9.4.1#r6": 46
  "§9.4.1#r7": 24
  EB-FRM-4@what-happened: [53, 57]
  F-DMG-01: 2
---

# Server membuat satu Damage record per aset layak dengan status menurut jenis pelapor dan Source titik masuk, menolak aset ber-record berjalan, Disposed, Missing, di luar cakupan, dan laporan ganda

## Prerequisites
- Aktor:
  - Total Control `Agus Pratama {runId}`.
  - Pemegang Manage asset & TAG (Update) `Rina Wulandari {runId}`.
  - Aktor Borrow `Yoga Tanuwijaya {runId}`, tanpa hak Update Manage asset & TAG.
  - Aktor Assignment `Dewi Anggraini {runId}`, tanpa hak Update Manage asset & TAG.
  - Pelapor umum `Budi Santoso {runId}`, pemegang aset, tanpa role Damaged.
  - Pelapor umum `Dedi Kurniawan {runId}`, pengguna aktif yang memindai TAG, tanpa role Damaged.
  - Group Manager `Gita Permatasari {runId}`, Group binaan `Head Office {runId}` beserta sub-group.
  - Pelapor umum `Maya Kusuma {runId}`, PIC karyawan tanpa akun `Bagus Hartono {runId}`.
  - Aktor Missing `Hendra Saputra {runId}`, Aktor Transfer `Tono Riyadi {runId}`, dan pemilik sesi Stock Opname `Sinta Marlina {runId}`.
- Data:
  - DU-201-1: User `Agus Pratama {runId}`, Total Control, cakupan seluruh client.
  - DU-201-2: User `Rina Wulandari {runId}`, Manage asset & TAG (Update), cakupan Group `Head Office {runId}` beserta descendant.
  - DU-201-3: User `Yoga Tanuwijaya {runId}`, Aktor Borrow, cakupan Group `Head Office {runId}`.
  - DU-201-4: User `Dewi Anggraini {runId}`, Aktor Assignment, cakupan Group `Head Office {runId}`.
  - DU-201-5: User `Budi Santoso {runId}`, pelapor umum, pemegang aset, cakupan aset yang ia pegang.
  - DU-201-6: User `Dedi Kurniawan {runId}`, pelapor umum, pemindai TAG, cakupan aset yang ia pindai.
  - DU-201-7: User `Hendra Saputra {runId}`, Aktor Missing, cakupan Group `Head Office {runId}`.
  - DU-201-8: User `Tono Riyadi {runId}`, Aktor Transfer, cakupan Group `Head Office {runId}`.
  - DU-201-9: User `Sinta Marlina {runId}`, pemilik sesi Stock Opname, cakupan Group `Head Office {runId}`.
  - DU-201-10: Group `Head Office {runId}`.
  - DU-201-11: Group `Branch Surabaya {runId}`, di luar cakupan Update `Rina Wulandari {runId}`.
  - DU-201-12: Aset `Laptop Dell Latitude 5420 - 1 {runId}`, Group `Head Office {runId}`, Normal, tanpa record berjalan.
  - DU-201-13: Aset `Tablet Samsung Tab A8 - 3 {runId}`, Group `Head Office {runId}`, Assigned kepada `Rina Wulandari {runId}`, tanpa record berjalan.
  - DU-201-14: Aset `Projector Epson EB-X06 - 2 {runId}`, Group `Head Office {runId}`, Borrowed oleh `Budi Santoso {runId}`, tanpa record berjalan.
  - DU-201-15: Aset `Monitor Dell P2422H - 6 {runId}`, Group `Head Office {runId}`, Assigned kepada `Budi Santoso {runId}`, tanpa record berjalan.
  - DU-201-16: Aset `Office Chair Ergo - 31 {runId}`, Group `Head Office {runId}`, Normal, tanpa record berjalan.
  - DU-201-17: Aset `Camera Canon EOS - 1 {runId}`, Group `Head Office {runId}`, Assigned kepada `Budi Santoso {runId}`, tanpa record berjalan.
  - DU-201-18: Aset `Scanner Fujitsu fi-7160 - 2 {runId}`, Group `Head Office {runId}`, punya record `Waiting for Confirmation` dengan What happened `Port charger patah`.
  - DU-201-19: Aset `Toyota Avanza - 2 {runId}`, Group `Head Office {runId}`, punya record `Damaged` dengan What happened `Kaca spion pecah`.
  - DU-201-20: Aset `Printer HP LaserJet M404 - 8 {runId}`, Group `Head Office {runId}`, punya record `Reported Disposal` dengan What happened `Roller macet`.
  - DU-201-21: Aset `Monitor Dell P2422H - 7 {runId}`, Group `Head Office {runId}`, punya record `In Disposal Process` dengan What happened `Panel bergaris`.
  - DU-201-22: Aset `Drill Bosch GSB - 4 {runId}`, Group `Head Office {runId}`, Disposed, tanpa record berjalan.
  - DU-201-23: Aset `Forklift Toyota 8FD - 1 {runId}`, Group `Head Office {runId}`, Missing (hilang), tanpa record Damaged.
  - DU-201-24: Aset `Handheld Scanner Zebra TC21 - 2 {runId}`, Group `Branch Surabaya {runId}`, Normal, tanpa record berjalan.
  - DU-201-25: Aset `Laptop Dell Latitude 5420 - 4 {runId}`, Group `Head Office {runId}`, Normal, tanpa record berjalan.
  - DU-201-26: Aset `Laptop Dell Latitude 5420 - 6 {runId}`, Group `Head Office {runId}`, Normal, tanpa record berjalan.
  - DU-201-27: Aset `Toyota Avanza - 1 {runId}`, Group `Head Office {runId}`, Normal, tanpa record berjalan.
  - DU-201-28: Aset `Toyota Avanza - 3 {runId}`, Group `Head Office {runId}`, Normal, tanpa record berjalan.
  - DU-201-29: Aset `Printer HP LaserJet M404 - 2 {runId}`, Group `Head Office {runId}`, Normal, tanpa record berjalan.
  - DU-201-30: Aset `Laptop Dell Latitude 5420 - 9 {runId}`, Group `Head Office {runId}`, Assigned kepada `Budi Santoso {runId}`, punya record `Damaged` Source `Manual` dengan What happened `Engsel longgar`.
  - DU-201-31: Aset `Camera Canon EOS - 3 {runId}`, Group `Head Office {runId}`, Missing (hilang) dengan Condition sebelumnya Damaged, punya record `Damaged` ditahan dengan What happened `Lensa berjamur`.
  - DU-201-32: Aset `Projector Epson EB-X06 - 5 {runId}`, Group `Head Office {runId}`, draf registrasi dengan Condition `Damaged` dan Damage note `Lensa tergores saat pengiriman`, belum Active.
  - DU-201-33: Aset `Forklift Toyota 8FD - 2 {runId}`, Group `Head Office {runId}`, dalam Transfer menuju `Branch Surabaya {runId}`, punya record `Damaged` dengan What happened `Garpu bengkok`.
  - DU-201-34: Aset `Drill Bosch GSB - 6 {runId}`, Group `Head Office {runId}`, termasuk sesi Stock Opname milik `Sinta Marlina {runId}`, punya record `Damaged` dengan What happened `Mata bor patah`.
  - DU-201-35: What happened `Layar retak setelah terjatuh dari meja`, Damaged Photo `layar-retak.jpg`.
  - DU-201-36: What happened `Kursi roda patah saat dipakai`, Damaged Photo `roda-patah.jpg`.
  - DU-201-37: What happened `Laporan kedua atas aset yang sama`, Damaged Photo `laporan-kedua.jpg`.
  - DU-201-38: What happened `Unit mengalami kerusakan fisik pada bagian layar dan engsel setelah terjatuh saat dipindahkan antar ruangan kantor, Unit mengalami kerusakan fisik pada bagian layar dan engsel setelah terjatuh saat dipindahkan antar ruangan kantor, Unit mengalami kerusakan fisik pada bagian layar dan engsel setelah terjatuh saat dipindahkan antar ruangan kantor, Unit mengala`, Damaged Photo `foto-360.jpg`.
  - DU-201-39: What happened `Unit mengalami kerusakan fisik pada bagian layar dan engsel setelah terjatuh saat dipindahkan antar ruangan kantor, Unit mengalami kerusakan fisik pada bagian layar dan engsel setelah terjatuh saat dipindahkan antar ruangan kantor, Unit mengalami kerusakan fisik pada bagian layar dan engsel setelah terjatuh saat dipindahkan antar ruangan kantor, Unit mengalay`, Damaged Photo `foto-361.jpg`.
  - DU-201-40: What happened dikosongkan, Damaged Photo `foto-kosong.jpg`.
  - DU-201-41: What happened `Printer macet saat mencetak`, tanpa Damaged Photo.
  - DU-201-42: User `Gita Permatasari {runId}`, Group Manager, cakupan Group binaan `Head Office {runId}` beserta sub-group.
  - DU-201-43: User `Maya Kusuma {runId}`, pelapor umum, PIC karyawan tanpa akun, cakupan aset yang dipegang karyawan `Bagus Hartono {runId}`.
  - DU-201-44: Karyawan tanpa akun `Bagus Hartono {runId}`, PIC `Maya Kusuma {runId}`.
  - DU-201-45: Aset `Laptop Dell Latitude 5420 - 11 {runId}`, Group `Head Office {runId}`, Normal, punya record `Repaired` selesai dengan What happened `Baterai kembung`, tanpa record berjalan.
  - DU-201-46: Aset `Projector Epson EB-X06 - 7 {runId}`, Group `Head Office {runId}`, Borrowed oleh `Budi Santoso {runId}`, tanpa record berjalan.
  - DU-201-47: Aset `Tablet Samsung Tab A8 - 5 {runId}`, Group `Head Office {runId}`, Assigned kepada karyawan `Bagus Hartono {runId}` dengan PIC `Maya Kusuma {runId}`, tanpa record berjalan.
  - DU-201-48: Aset `Office Chair Ergo - 33 {runId}`, Group `Head Office {runId}`, Normal, tanpa record berjalan.
  - DU-201-49: Aset `Printer HP LaserJet M404 - 9 {runId}`, Group `Head Office {runId}`, Normal, tanpa record berjalan.
  - DU-201-50: Aset `Laptop Dell Latitude 5420 - 12 {runId}`, Group `Head Office {runId}`, Normal, tanpa record berjalan.
  - DU-201-51: Aset `Handheld Scanner Zebra TC21 - 4 {runId}`, Group `Branch Surabaya {runId}`, Normal, tanpa record berjalan.
  - DU-201-52: Aset `Tablet Samsung Tab A8 - 6 {runId}`, Group `Head Office {runId}`, dalam Transfer menuju `Branch Surabaya {runId}`, tanpa record berjalan.

## Test Steps

### Pelapor admin melapor aset layak: record langsung Damaged, Source Manual, tercatat
1. Total Control `Agus Pratama {runId}` mengirim Report Damaged atas `Laptop Dell Latitude 5420 - 1 {runId}` dari Asset List dengan What happened `Layar retak setelah terjatuh dari meja` dan satu Damaged Photo `layar-retak.jpg`
2. Verifikasi server membuat tepat satu Damage record untuk aset `Laptop Dell Latitude 5420 - 1 {runId}` dengan status `Damaged`
3. Verifikasi Source record itu adalah `Manual`
4. Verifikasi What happened `Layar retak setelah terjatuh dari meja` dan Damaged Photo `layar-retak.jpg` tersimpan sebagai bukti laporan
5. Verifikasi record itu tidak memiliki nomor transaksi
6. Verifikasi record itu dikenali lewat aset dan waktu laporan
7. Verifikasi status global aset berubah menjadi `Damaged` bersamaan dengan pembuatan record, sebagai satu kesatuan per aset
8. Verifikasi laporan itu tercatat di Damage Log record sebagai node `Reported damaged by` dengan pelapor `Agus Pratama {runId}`
9. Verifikasi laporan itu tercatat di Transaction log aset

### Pemegang Manage asset & TAG (Update) melapor dari My Asset: langsung Damaged tanpa Confirm
10. Pemegang Update `Rina Wulandari {runId}` mengirim Report Damaged atas `Tablet Samsung Tab A8 - 3 {runId}` yang ia pegang dari halaman aset yang dipegangnya dengan What happened `Kursi roda patah saat dipakai` dan satu Damaged Photo `roda-patah.jpg`
11. Verifikasi server membuat record berstatus `Damaged`, bukan `Waiting for Confirmation`
12. Verifikasi Source record itu adalah `Reported by holder`
13. Verifikasi Confirm dan Reject tidak berlaku bagi record itu dan permintaannya ditolak

### Aktor Borrow dan Aktor Assignment tanpa hak Damaged melapor dari halaman transaksinya: Waiting for Confirmation dengan Source titik masuk
14. Aktor peminjaman `Yoga Tanuwijaya {runId}` mengirim Report Damaged atas `Projector Epson EB-X06 - 2 {runId}` yang sedang dipinjam dari halaman transaksi peminjaman dengan What happened `Layar retak setelah terjatuh dari meja` dan Damaged Photo `layar-retak.jpg`
15. Verifikasi server membuat record berstatus `Waiting for Confirmation`, bukan `Damaged`, dengan Source `Borrowed asset`
16. Verifikasi pemegang `Budi Santoso {runId}` tetap memegang aset itu
17. Aktor penugasan `Dewi Anggraini {runId}` mengirim Report Damaged atas `Monitor Dell P2422H - 6 {runId}` yang sedang ditugaskan dari halaman transaksi penugasan dengan What happened `Layar retak setelah terjatuh dari meja` dan Damaged Photo `layar-retak.jpg`
18. Verifikasi server membuat record berstatus `Waiting for Confirmation`, bukan `Damaged`, dengan Source `Assigned asset`

### Pelapor umum melapor: record Waiting for Confirmation menurut titik masuk
19. Pelapor umum `Dedi Kurniawan {runId}` mengirim Report Damaged atas `Office Chair Ergo - 31 {runId}` dari hasil scan TAG di mobile dengan What happened `Kursi roda patah saat dipakai` dan Damaged Photo `roda-patah.jpg`
20. Verifikasi server membuat record berstatus `Waiting for Confirmation` dengan Source `Reported by scan`
21. Pelapor umum `Budi Santoso {runId}` mengirim Report Damaged atas `Camera Canon EOS - 1 {runId}` yang ia pegang dari halaman aset yang dipegangnya dengan What happened `Layar retak setelah terjatuh dari meja` dan Damaged Photo `layar-retak.jpg`
22. Verifikasi server membuat record berstatus `Waiting for Confirmation` dengan Source `Reported by holder`

### Aset yang sudah punya record berjalan tidak dapat dilaporkan lagi
23. Total Control `Agus Pratama {runId}` mengirim Report Damaged atas `Scanner Fujitsu fi-7160 - 2 {runId}` dengan What happened `Laporan kedua atas aset yang sama` dan Damaged Photo `laporan-kedua.jpg`
24. Verifikasi laporan itu ditolak karena aset sudah punya record berjalan
25. Verifikasi aset itu tetap hanya memiliki satu record berjalan
26. Verifikasi record itu tetap berstatus `Waiting for Confirmation` dengan What happened `Port charger patah`
27. Verifikasi tidak ada node Damage Log baru di record itu
28. Total Control `Agus Pratama {runId}` mengirim Report Damaged atas `Toyota Avanza - 2 {runId}` dengan What happened `Laporan kedua atas aset yang sama` dan Damaged Photo `laporan-kedua.jpg`
29. Verifikasi laporan itu ditolak dan record tetap berstatus `Damaged` dengan What happened `Kaca spion pecah`
30. Total Control `Agus Pratama {runId}` mengirim Report Damaged atas `Printer HP LaserJet M404 - 8 {runId}` dengan What happened `Laporan kedua atas aset yang sama` dan Damaged Photo `laporan-kedua.jpg`
31. Verifikasi laporan itu ditolak dan record tetap berstatus `Reported Disposal` dengan What happened `Roller macet`
32. Total Control `Agus Pratama {runId}` mengirim Report Damaged atas `Monitor Dell P2422H - 7 {runId}` dengan What happened `Laporan kedua atas aset yang sama` dan Damaged Photo `laporan-kedua.jpg`
33. Verifikasi laporan itu ditolak dan record tetap berstatus `In Disposal Process` dengan What happened `Panel bergaris`

### Aset Disposed atau sedang Missing tidak dapat dilaporkan rusak
34. Total Control `Agus Pratama {runId}` mengirim Report Damaged atas `Drill Bosch GSB - 4 {runId}` yang berstatus Disposed dengan What happened `Layar retak setelah terjatuh dari meja` dan Damaged Photo `layar-retak.jpg`
35. Verifikasi laporan itu ditolak dan tidak ada Damage record untuk aset itu
36. Verifikasi tidak ada node Damage Log baru
37. Total Control `Agus Pratama {runId}` mengirim Report Damaged atas `Forklift Toyota 8FD - 1 {runId}` yang sedang hilang dengan What happened `Layar retak setelah terjatuh dari meja` dan Damaged Photo `layar-retak.jpg`
38. Verifikasi laporan itu ditolak dan tidak ada Damage record untuk aset yang sedang hilang

### Aset di luar cakupan Update ditolak server
39. Pemegang Update `Rina Wulandari {runId}` mengirim Report Damaged atas `Handheld Scanner Zebra TC21 - 2 {runId}` di Group `Branch Surabaya {runId}` dengan What happened `Layar retak setelah terjatuh dari meja` dan Damaged Photo `layar-retak.jpg`
40. Verifikasi laporan itu ditolak karena aset di luar cakupan Update dan tidak ada Damage record untuk aset itu

### Laporan banyak aset: satu record per aset layak, aset tidak layak dilewati dengan keterangan
41. Total Control `Agus Pratama {runId}` mengirim satu Report Damaged atas `Laptop Dell Latitude 5420 - 4 {runId}`, `Laptop Dell Latitude 5420 - 6 {runId}`, `Toyota Avanza - 2 {runId}`, dan `Drill Bosch GSB - 4 {runId}` dengan What happened `Layar retak setelah terjatuh dari meja` dan Damaged Photo `layar-retak.jpg` per aset
42. Verifikasi server membuat satu Damage record `Damaged` untuk `Laptop Dell Latitude 5420 - 4 {runId}` dan satu untuk `Laptop Dell Latitude 5420 - 6 {runId}`
43. Verifikasi aset `Toyota Avanza - 2 {runId}` yang sudah punya record berjalan dilewati dengan keterangan `Already reported damaged` dan tidak mendapat record baru
44. Verifikasi aset `Drill Bosch GSB - 4 {runId}` yang Disposed dilewati dengan keterangan `Can't be reported damaged` dan tidak mendapat record

### Dua laporan bersamaan atas aset tanpa record menghasilkan satu record
45. Total Control `Agus Pratama {runId}` mengirim Report Damaged atas `Toyota Avanza - 1 {runId}` dan, bersamaan, pemegang Update `Rina Wulandari {runId}` mengirim Report Damaged atas `Toyota Avanza - 1 {runId}` dan `Toyota Avanza - 3 {runId}`, masing-masing dengan What happened `Kursi roda patah saat dipakai` dan Damaged Photo `roda-patah.jpg`
46. Verifikasi `Toyota Avanza - 1 {runId}` memiliki tepat satu Damage record berjalan, apa pun urutan tiba kedua permintaan
47. Verifikasi hanya satu permintaan yang menolak `Toyota Avanza - 1 {runId}` dengan keterangan `Already reported damaged`, dan laporan yang kalah tidak membuat record
48. Verifikasi `Toyota Avanza - 3 {runId}` tetap diproses dan memiliki satu Damage record `Damaged`
49. Verifikasi `Toyota Avanza - 1 {runId}` hanya memiliki satu node `Reported damaged by`

### Bukti laporan wajib: What happened 1 sampai 360 karakter dan satu Damaged Photo
50. Total Control `Agus Pratama {runId}` mengirim Report Damaged atas `Printer HP LaserJet M404 - 2 {runId}` dengan What happened dikosongkan dan Damaged Photo `foto-kosong.jpg`
51. Verifikasi laporan itu ditolak karena What happened kosong dan tidak ada Damage record
52. Total Control `Agus Pratama {runId}` mengirim Report Damaged atas `Printer HP LaserJet M404 - 2 {runId}` dengan What happened `Unit mengalami kerusakan fisik pada bagian layar dan engsel setelah terjatuh saat dipindahkan antar ruangan kantor, Unit mengalami kerusakan fisik pada bagian layar dan engsel setelah terjatuh saat dipindahkan antar ruangan kantor, Unit mengalami kerusakan fisik pada bagian layar dan engsel setelah terjatuh saat dipindahkan antar ruangan kantor, Unit mengalay` (361 karakter) dan Damaged Photo `foto-361.jpg`
53. Verifikasi laporan itu ditolak karena What happened lebih dari 360 karakter dan tidak ada Damage record
54. Total Control `Agus Pratama {runId}` mengirim Report Damaged atas `Printer HP LaserJet M404 - 2 {runId}` dengan What happened `Printer macet saat mencetak` tanpa Damaged Photo
55. Verifikasi laporan itu ditolak karena Damaged Photo tidak ada dan tidak ada Damage record
56. Total Control `Agus Pratama {runId}` mengirim Report Damaged atas `Printer HP LaserJet M404 - 2 {runId}` dengan What happened `Unit mengalami kerusakan fisik pada bagian layar dan engsel setelah terjatuh saat dipindahkan antar ruangan kantor, Unit mengalami kerusakan fisik pada bagian layar dan engsel setelah terjatuh saat dipindahkan antar ruangan kantor, Unit mengalami kerusakan fisik pada bagian layar dan engsel setelah terjatuh saat dipindahkan antar ruangan kantor, Unit mengala` (360 karakter) dan Damaged Photo `foto-360.jpg`
57. Verifikasi laporan itu diterima dan server membuat satu Damage record `Damaged` dengan What happened sepanjang 360 karakter

### Aset yang sudah punya record berjalan tidak mendapat record kedua lewat jalur modul lain
58. Aktor penugasan `Dewi Anggraini {runId}` menyelesaikan Unassign berstatus `Unassigned` bermarker `Damaged` atas `Laptop Dell Latitude 5420 - 9 {runId}` dengan Description `Engsel longgar` dan satu foto Unassign
59. Verifikasi Unassign selesai dan aset itu tetap hanya memiliki satu record berjalan `Damaged` dengan What happened `Engsel longgar`
60. Aktor penemuan aset `Hendra Saputra {runId}` menjalankan Mark as Found Damaged atas `Camera Canon EOS - 3 {runId}` dengan Note `Lensa berjamur` dan satu Damaged Photo
61. Verifikasi server menambah node ke record yang ada dan aset itu tetap hanya memiliki satu record berjalan
62. Total Control `Agus Pratama {runId}` mengaktifkan registrasi `Projector Epson EB-X06 - 5 {runId}` yang ber-Condition `Damaged`
63. Verifikasi aset itu hanya memiliki satu record berjalan dengan Source `Registration`
64. Aktor pemindahan aset `Tono Riyadi {runId}` menerima pemindahan `Forklift Toyota 8FD - 2 {runId}` dan melaporkan Damaged saat penerimaan
65. Verifikasi aset itu tetap hanya memiliki satu record berjalan dan tidak ada record kedua
66. Pemilik sesi opname `Sinta Marlina {runId}` melaporkan kondisi rusak atas `Drill Bosch GSB - 6 {runId}` dari sesinya
67. Verifikasi aset itu tetap hanya memiliki satu record berjalan dan tidak ada record kedua

### Aset dengan record selesai dapat dilaporkan lagi: dua record dibedakan oleh urutan laporan
68. Total Control `Agus Pratama {runId}` mengirim Report Damaged atas `Laptop Dell Latitude 5420 - 11 {runId}` yang punya record `Repaired` selesai dengan What happened `Layar retak setelah terjatuh dari meja` dan Damaged Photo `layar-retak.jpg`
69. Verifikasi server membuat record baru berstatus `Damaged` dengan What happened `Layar retak setelah terjatuh dari meja` untuk aset itu
70. Verifikasi record `Repaired` dengan What happened `Baterai kembung` tetap ada dan tidak berubah
71. Verifikasi kedua record dikenali sebagai record terpisah lewat aset yang sama dan waktu laporannya, dengan record `Damaged` dilaporkan sesudah record `Repaired`
72. Verifikasi aset itu hanya memiliki satu record berjalan, yaitu record `Damaged`

### Pemegang Borrow dan PIC karyawan tanpa akun melapor dari aset yang dipegang: Waiting for Confirmation
73. Pelapor umum `Budi Santoso {runId}` mengirim Report Damaged atas `Projector Epson EB-X06 - 7 {runId}` yang ia pinjam dari halaman aset yang dipegangnya dengan What happened `Layar retak setelah terjatuh dari meja` dan Damaged Photo `layar-retak.jpg`
74. Verifikasi server membuat record berstatus `Waiting for Confirmation` dengan Source `Reported by holder`
75. PIC `Maya Kusuma {runId}` mengirim Report Damaged atas `Tablet Samsung Tab A8 - 5 {runId}` yang dipegang karyawan `Bagus Hartono {runId}` dari halaman aset yang dipegangnya dengan What happened `Kursi roda patah saat dipakai` dan Damaged Photo `roda-patah.jpg`
76. Verifikasi server membuat record berstatus `Waiting for Confirmation` dengan Source `Reported by holder`
77. Verifikasi pelapor record itu dicatat sebagai PIC `Maya Kusuma {runId}` atas nama karyawan `Bagus Hartono {runId}`

### Pelapor admin melapor lewat scan mobile: record langsung Damaged
78. Pemegang Update `Rina Wulandari {runId}` mengirim Report Damaged atas `Office Chair Ergo - 33 {runId}` dari hasil scan TAG di mobile dengan What happened `Layar retak setelah terjatuh dari meja` dan Damaged Photo `layar-retak.jpg`
79. Verifikasi server membuat record berstatus `Damaged`, bukan `Waiting for Confirmation`
80. Verifikasi status global aset berubah menjadi `Damaged`

### Group Manager melapor aset Group binaan: langsung Damaged, aset di luar binaan dilewati
81. Group Manager `Gita Permatasari {runId}` mengirim Report Damaged atas `Printer HP LaserJet M404 - 9 {runId}` dari Asset List dengan What happened `Layar retak setelah terjatuh dari meja` dan Damaged Photo `layar-retak.jpg`
82. Verifikasi server membuat record berstatus `Damaged`, bukan `Waiting for Confirmation`
83. Group Manager `Gita Permatasari {runId}` mengirim satu Report Damaged atas `Laptop Dell Latitude 5420 - 12 {runId}` dan `Handheld Scanner Zebra TC21 - 4 {runId}` dengan What happened `Layar retak setelah terjatuh dari meja` dan Damaged Photo `layar-retak.jpg` per aset
84. Verifikasi server membuat satu Damage record `Damaged` untuk `Laptop Dell Latitude 5420 - 12 {runId}`
85. Verifikasi aset `Handheld Scanner Zebra TC21 - 4 {runId}` di luar Group binaan dilewati dengan keterangan `Can't be reported damaged`, ditolak server, dan tidak mendapat record

### Aktor Transfer melapor dari halaman transaksinya: langsung Damaged
86. Aktor pemindahan aset `Tono Riyadi {runId}` mengirim Report Damaged atas `Tablet Samsung Tab A8 - 6 {runId}` dari halaman transaksi pemindahan dengan What happened `Layar retak setelah terjatuh dari meja` dan Damaged Photo `layar-retak.jpg`
87. Verifikasi server membuat record berstatus `Damaged`, bukan `Waiting for Confirmation`
