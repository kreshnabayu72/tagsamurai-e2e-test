---
id: TC-FA-BORROW-BE-080-overdue-pengingat-timeout
title: "Overdue per baris, pengingat Due date, Transaction timeout, dan penutupan otomatis menjadi Draft"
layer: be-e2e
priority: Critical
caseType: Positive
status: ready-for-automation
sourceRules: ["BORROW-LOGIC-11a", "BORROW-LOGIC-11b", "BORROW-LOGIC-11c", "BORROW-LOGIC-11d", "BORROW-LOGIC-11e", "BORROW-LOGIC-11f", "BORROW-LOGIC-11g", "BORROW-LOGIC-11h", "BORROW-LOGIC-11i", "BORROW-LOGIC-11j", "BORROW-LOGIC-12aa", "BORROW-LOGIC-12ab", "BORROW-LOGIC-12ac", "BORROW-LOGIC-12ad", "BORROW-LOGIC-12ae", "BORROW-LOGIC-12af", "BORROW-LOGIC-12ag", "BORROW-LOGIC-12ah", "BORROW-LOGIC-12ai", "BORROW-LOGIC-12aj", "BORROW-LOGIC-12ak", "BORROW-LOGIC-12b", "BORROW-LOGIC-12c", "BORROW-LOGIC-12d", "BORROW-LOGIC-12e", "BORROW-LOGIC-12f", "BORROW-LOGIC-12g", "BORROW-LOGIC-12h", "BORROW-LOGIC-12i", "BORROW-LOGIC-12j", "BORROW-LOGIC-12k", "BORROW-LOGIC-12l", "BORROW-LOGIC-12m", "BORROW-LOGIC-12n", "BORROW-LOGIC-12o", "BORROW-LOGIC-12p", "BORROW-LOGIC-12q", "BORROW-LOGIC-12r", "BORROW-LOGIC-12s", "BORROW-LOGIC-12t", "BORROW-LOGIC-12u", "BORROW-LOGIC-12v", "BORROW-LOGIC-12w", "BORROW-LOGIC-12x", "BORROW-LOGIC-12y", "BORROW-LOGIC-12z", "EC-BRW-127", "EC-BRW-128", "EC-BRW-129", "EC-BRW-130", "EC-BRW-139", "EC-BRW-159", "EC-BRW-164", "EC-BRW-177", "EC-BRW-33", "F-BORROW-09.k1", "F-BORROW-09.k2", "F-BORROW-09.k3", "F-BORROW-10.k10", "F-BORROW-10.k2", "F-BORROW-10.k3", "F-BORROW-10.k4", "F-BORROW-10.k5", "F-BORROW-10.k9", "§9.2#r46", "§9.2#r47", "§9.2#p36", "§9.4.3#b7", "§9.5#r16"]
smoke: []
dependsOn: []
owner: BE
trace:
  "BORROW-LOGIC-11a": [1, 2]
  "BORROW-LOGIC-11b": 6
  "BORROW-LOGIC-11c": [15, 22, 118]
  "BORROW-LOGIC-11d": [6, 11, 120, 123]
  "BORROW-LOGIC-11e": 12
  "BORROW-LOGIC-11f": [16, 25, 118]
  "BORROW-LOGIC-11g": [27, 30]
  "BORROW-LOGIC-11h": 46
  "BORROW-LOGIC-11i": 3
  "BORROW-LOGIC-11j": [13, 125]
  "BORROW-LOGIC-12aa": [50, 127, 128]
  "BORROW-LOGIC-12ab": [3, 31]
  "BORROW-LOGIC-12ac": 32
  "BORROW-LOGIC-12ad": 34
  "BORROW-LOGIC-12ae": [2, 4]
  "BORROW-LOGIC-12af": 57
  "BORROW-LOGIC-12ag": [58, 59]
  "BORROW-LOGIC-12ah": [76, 150, 151]
  "BORROW-LOGIC-12ai": 72
  "BORROW-LOGIC-12aj": [92, 96]
  "BORROW-LOGIC-12ak": 94
  "BORROW-LOGIC-12b": 54
  "BORROW-LOGIC-12c": [55, 81]
  "BORROW-LOGIC-12d": [79, 130]
  "BORROW-LOGIC-12e": 81
  "BORROW-LOGIC-12f": [85, 89, 132, 133]
  "BORROW-LOGIC-12g": [86, 133, 153, 155]
  "BORROW-LOGIC-12h": 87
  "BORROW-LOGIC-12i": 60
  "BORROW-LOGIC-12j": 61
  "BORROW-LOGIC-12k": 62
  "BORROW-LOGIC-12l": 64
  "BORROW-LOGIC-12m": 66
  "BORROW-LOGIC-12n": 75
  "BORROW-LOGIC-12o": 73
  "BORROW-LOGIC-12p": 69
  "BORROW-LOGIC-12q": 70
  "BORROW-LOGIC-12r": [91, 98, 134]
  "BORROW-LOGIC-12s": 99
  "BORROW-LOGIC-12t": [101, 138]
  "BORROW-LOGIC-12u": 102
  "BORROW-LOGIC-12v": 104
  "BORROW-LOGIC-12w": 105
  "BORROW-LOGIC-12x": 47
  "BORROW-LOGIC-12y": 48
  "BORROW-LOGIC-12z": 52
  "EC-BRW-127": [61, 64, 66, 67]
  "EC-BRW-128": [105, 106, 108]
  "EC-BRW-129": [75, 76, 77, 79, 130, 147, 150]
  "EC-BRW-130": [91, 92, 93, 96]
  "EC-BRW-139": [39, 40, 41, 43, 44, 141, 142]
  "EC-BRW-159": [34, 36, 37]
  "EC-BRW-164": [113, 115, 116]
  "EC-BRW-177": [110, 111]
  "EC-BRW-33": [46, 55, 91, 98]
  "F-BORROW-09.k1": [6, 7, 8, 9, 37, 120, 121]
  "F-BORROW-09.k2": [15, 18, 20, 22, 25, 39, 118]
  "F-BORROW-09.k3": [46, 115]
  "F-BORROW-10.k10": [64, 65, 78]
  "F-BORROW-10.k2": [55, 144, 145]
  "F-BORROW-10.k3": 81
  "F-BORROW-10.k4": [61, 63]
  "F-BORROW-10.k5": [56, 99, 101]
  "F-BORROW-10.k9": 105
  "§9.2#r46": [55, 68, 144, 145]
  "§9.2#r47": [83, 84]
  "§9.2#p36": [56, 101]
  "§9.4.3#b7": 47
  "§9.5#r16": [81, 82]
---

# Overdue per baris, pengingat Due date, Transaction timeout, dan penutupan otomatis menjadi Draft

## Prerequisites
- Aktor: Asset Admin `Agus Pratama {runId}` dengan Group penugasan `Head Office {runId}` (DU-080-1); Borrower `Rina Wijaya {runId}` (DU-080-2); Requester `Tika Rahma {runId}` (DU-080-3); Approver `Sari Dewi {runId}` (DU-080-4); Asset Admin `Maya Putri {runId}` dengan hak Aktor Missing (DU-080-5); Borrower `Bagas Prasetyo {runId}` (DU-080-27); Approver kedua `Rizal Hakim {runId}` (DU-080-39). Job sistem berjalan tanpa Aktor.
- Data:
  - DU-080-1: Pengguna, Asset Admin pelaku aksi: Name `Agus Pratama {runId}`, Role `Asset Admin`, Group penugasan `Head Office {runId}`.
  - DU-080-2: Pengguna, Borrower dengan akun login: Name `Rina Wijaya {runId}`, Role `Karyawan aktif dengan akun login`, Group `Head Office {runId}`.
  - DU-080-3: Pengguna, Requester BRW yang membuat pengajuan: Name `Tika Rahma {runId}`, Role `Asset Admin`, Group penugasan `Head Office {runId}`.
  - DU-080-4: Pengguna, Approver aset: Name `Sari Dewi {runId}`, Role `Approver`, Group penugasan `Head Office {runId}`.
  - DU-080-5: Pengguna, Aktor dengan hak memutuskan laporan hilang: Name `Maya Putri {runId}`, Role `Asset Admin dengan hak Aktor Missing`, Group penugasan `Head Office {runId}`.
  - DU-080-6: Baris Borrow, Baris Days untuk Due date, Overdue, dan pengingat: BRW `BRW 1`, Borrower `Rina Wijaya {runId}`, Asset Name `Laptop Dell Latitude {runId}`, Category `Laptop`, Duration `3 Days`, Status baris `Borrowed`, Waktu handover `00:30` menurut Time Zone penyewa (di UTC masih tanggal sebelumnya), Due date yang diharapkan `tanggal handover + 2 hari pukul 23:59:59`.
  - DU-080-7: Baris Borrow, Baris Hours untuk pengingat dan Overdue: BRW `BRW 2`, Borrower `Rina Wijaya {runId}`, Asset Name `Meeting Mic Set {runId}`, Category `Peralatan Rapat`, Duration `6 Hours`, Status baris `Borrowed`, Due date reminders `1 jam sebelum dan saat Due date`.
  - DU-080-8: Baris Borrow, Baris yang laporan hilang Borrower-nya menunggu konfirmasi saat ambang tiba: BRW `BRW 3`, Borrower `Rina Wijaya {runId}`, Asset Name `Drone Mini {runId}`, Category `Drone`, Duration `3 Days`, Status baris `Borrowed`, Due date reminders `D-3, D-1, D-day`, Record hilang `Waiting for Confirmation`.
  - DU-080-9: Baris Borrow, Baris Overdue milik Borrower dengan Block new borrow when overdue ON: BRW `BRW 4`, Borrower `Rina Wijaya {runId}`, Asset Name `Monitor Samsung {runId}`, Category `Monitor`, Duration `1 Days`, Status baris `Overdue` dan tetap `Overdue` sepanjang spec ini, Block new borrow when overdue `ON`.
  - DU-080-10: Aset, Aset Available untuk pengajuan baru: Asset Name `Kursi Lipat Rapat {runId}`, Category `Furnitur`, Custody `Available`, Condition `Normal`, Block new borrow when overdue `ON` pada aturan efektif aset.
  - DU-080-11: Baris Borrow, Baris Hours yang Due date-nya baru lewat: BRW `BRW 5`, Borrower `Rina Wijaya {runId}`, Asset Name `Walkie Talkie Motorola {runId}`, Category `Peralatan Komunikasi`, Duration `2 Hours`, Status baris `Borrowed`.
  - DU-080-12: Baris Borrow, Baris Hours yang melewati pergantian DST: BRW `BRW 6`, Borrower `Rina Wijaya {runId}`, Asset Name `Mikrofon Wireless Shure {runId}`, Category `Audio`, Duration `24 Hours`, Status baris `Borrowed`, Time Zone General Settings `zona dengan pergantian DST`.
  - DU-080-13: Baris Borrow, Baris Waiting for Approval pertama yang timeout, dalam BRW dengan Requester Tika: BRW `BRW 7 bersama DU-080-14 dan DU-080-15`, Borrower `Bagas Prasetyo {runId}`, Asset Name `Laptop Lenovo ThinkPad {runId}`, Category `Laptop`, Duration `3 Days`, Status baris `Waiting for Approval`, Requester `Tika Rahma {runId}`, Approver `Sari Dewi {runId}`, Duration dan Purpose `Duration 3 Days, Purpose Pelatihan, Note Catatan pelatihan`.
  - DU-080-14: Baris Borrow, Baris Waiting for Approval kedua yang timeout pada run yang sama: BRW `BRW 7 bersama DU-080-13 dan DU-080-15`, Borrower `Bagas Prasetyo {runId}`, Asset Name `Proyektor Mini {runId}`, Category `Proyektor`, Duration `2 Days`, Status baris `Waiting for Approval`, Requester `Tika Rahma {runId}`, Approver `Sari Dewi {runId}`.
  - DU-080-15: Baris Borrow, Baris Waiting for Approval ketiga yang baru timeout pada run berikutnya: BRW `BRW 7 bersama DU-080-13 dan DU-080-14`, Borrower `Bagas Prasetyo {runId}`, Asset Name `Layar Proyektor {runId}`, Category `Proyektor`, Duration `2 Days`, Status baris `Waiting for Approval`, Requester `Tika Rahma {runId}`, Approver `Sari Dewi {runId}`, Masuk status `belakangan dari DU-080-13 dan DU-080-14`.
  - DU-080-16: Baris Borrow, Baris Waiting for Handover yang tidak diambil: BRW `BRW 8`, Borrower `Rina Wijaya {runId}`, Asset Name `Tripod Kamera {runId}`, Category `Aksesori Kamera`, Duration `2 Days`, Status baris `Waiting for Handover`, Requester `Tika Rahma {runId}`.
  - DU-080-17: Baris Borrow, Baris self-service yang langsung Borrowed: BRW `BRW 9 self-service`, Borrower `Rina Wijaya {runId}`, Asset Name `Camera Sony Alpha {runId}`, Category `Kamera`, Duration `3 Days`, Status baris `Borrowed`.
  - DU-080-18: Baris Borrow, Baris Borrowed dengan Extension Request menunggu review Aktor Borrow: BRW `BRW 10`, Borrower `Rina Wijaya {runId}`, Asset Name `Gimbal DJI {runId}`, Category `Kamera`, Duration `3 Days`, Status baris `Borrowed`, Extension menunggu `review Aktor Borrow`.
  - DU-080-19: Baris Borrow, Baris Overdue dengan Extension Request menunggu review Aktor Borrow: BRW `BRW 11`, Borrower `Rina Wijaya {runId}`, Asset Name `Kamera Fujifilm {runId}`, Category `Kamera`, Duration `1 Days`, Status baris `Overdue`, Extension menunggu `review Aktor Borrow`.
  - DU-080-20: Baris Borrow, Baris Borrowed dengan Extension Approval menunggu: BRW `BRW 12`, Borrower `Rina Wijaya {runId}`, Asset Name `Lensa Sigma {runId}`, Category `Kamera`, Duration `3 Days`, Status baris `Borrowed`, Extension menunggu `approval oleh Sari Dewi {runId}`.
  - DU-080-21: Baris Borrow, Baris Borrowed dengan Extension Request yang diteruskan Aktor Borrow ke approval: BRW `BRW 13`, Borrower `Rina Wijaya {runId}`, Asset Name `Tablet Samsung {runId}`, Category `Tablet`, Duration `3 Days`, Status baris `Borrowed`, Extension menunggu `review Aktor Borrow lalu diteruskan ke approval`.
  - DU-080-22: Baris Borrow, Baris Waiting for Approval pada level plan Basic: BRW `BRW 14`, Borrower `Rina Wijaya {runId}`, Asset Name `Printer Warna Epson {runId}`, Category `Printer`, Duration `3 Days`, Status baris `Waiting for Approval`, Level Feature Suite Borrowing `Basic`.
  - DU-080-23: Baris Borrow, Baris Borrowed dengan Extension Approval menunggu pada level plan Basic: BRW `BRW 15`, Borrower `Rina Wijaya {runId}`, Asset Name `Mesin Bor Listrik {runId}`, Category `Peralatan Lapangan`, Duration `3 Days`, Status baris `Borrowed`, Extension menunggu `approval oleh Sari Dewi {runId}`, Level Feature Suite Borrowing `Basic`.
  - DU-080-24: Baris Borrow, Baris Borrowed yang melewati Due date pada level plan None: BRW `BRW 16`, Borrower `Rina Wijaya {runId}`, Asset Name `Server Rack Mini {runId}`, Category `Perangkat Jaringan`, Duration `1 Days`, Status baris `Borrowed` sebelum Due date lewat, Level Feature Suite Borrowing `None`.
  - DU-080-25: Baris Borrow, Baris Waiting for Approval pada Client Suspended: BRW `BRW 17`, Borrower `Rina Wijaya {runId}`, Asset Name `Lampu Studio {runId}`, Category `Peralatan Studio`, Duration `3 Days`, Status baris `Waiting for Approval`, Status Client `Suspended`.
  - DU-080-26: Baris Borrow, Baris Borrowed yang menjadi Overdue pada Client Suspended: BRW `BRW 18`, Borrower `Rina Wijaya {runId}`, Asset Name `Reflektor Studio {runId}`, Category `Peralatan Studio`, Duration `1 Days`, Status baris `Borrowed`, Status Client `Suspended`.
  - DU-080-27: Pengguna, Borrower terpisah untuk uji Block new borrow dan Draft hasil timeout: Name `Bagas Prasetyo {runId}`, Role `Karyawan aktif dengan akun login`, Group `Head Office {runId}`.
  - DU-080-28: Baris Borrow, Baris Overdue milik Borrower terpisah dengan Block new borrow when overdue ON: BRW `BRW 19`, Borrower `Bagas Prasetyo {runId}`, Asset Name `Hard Disk Eksternal {runId}`, Category `Perangkat Penyimpanan`, Duration `1 Days`, Status baris `Overdue`, Block new borrow when overdue `ON`.
  - DU-080-29: Baris Borrow, Baris Borrowed untuk Cancel Borrow yang ditolak: BRW `BRW 20`, Borrower `Rina Wijaya {runId}`, Asset Name `Proyektor Kecil {runId}`, Category `Proyektor`, Duration `3 Days`, Status baris `Borrowed`.
  - DU-080-30: Baris Borrow, Baris Waiting for Handover untuk Cancel Borrow sebelum handover: BRW `BRW 21`, Borrower `Rina Wijaya {runId}`, Asset Name `Tripod Studio {runId}`, Category `Aksesori Kamera`, Duration `2 Days`, Status baris `Waiting for Handover`.
  - DU-080-31: Baris Borrow, Baris Days untuk pengingat D-3, D-1, dan D-day: BRW `BRW 22`, Borrower `Rina Wijaya {runId}`, Asset Name `Laptop Asus Zenbook {runId}`, Category `Laptop`, Duration `10 Days`, Status baris `Borrowed`, Due date reminders `D-3, D-1, D-day`.
  - DU-080-32: Baris Borrow, Baris Days untuk pengingat D-day yang dikirim: BRW `BRW 23`, Borrower `Rina Wijaya {runId}`, Asset Name `Laptop Acer Swift {runId}`, Category `Laptop`, Duration `5 Days`, Status baris `Borrowed`, Due date reminders `D-3, D-1, D-day`.
  - DU-080-33: Baris Borrow, Baris Days pertama yang menjadi Overdue lebih dulu: BRW `BRW 24 bersama DU-080-34`, Borrower `Rina Wijaya {runId}`, Asset Name `Kursi Tamu {runId}`, Category `Furnitur`, Duration `1 Days`, Status baris `Borrowed`.
  - DU-080-34: Baris Borrow, Baris Days kedua yang menjadi Overdue belakangan: BRW `BRW 24 bersama DU-080-33`, Borrower `Rina Wijaya {runId}`, Asset Name `Meja Tamu {runId}`, Category `Furnitur`, Duration `3 Days`, Status baris `Borrowed`.
  - DU-080-35: Baris Borrow, Baris Waiting for Handover pertama yang timeout lebih dulu: BRW `BRW 25 bersama DU-080-36`, Borrower `Rina Wijaya {runId}`, Asset Name `Sound System {runId}`, Category `Peralatan Panggung`, Duration `2 Days`, Status baris `Waiting for Handover`.
  - DU-080-36: Baris Borrow, Baris Waiting for Handover kedua yang masuk status itu belakangan: BRW `BRW 25 bersama DU-080-35`, Borrower `Rina Wijaya {runId}`, Asset Name `Mixer Panggung {runId}`, Category `Peralatan Panggung`, Duration `2 Days`, Status baris `Waiting for Handover`, Masuk status `belakangan dari DU-080-35`.
  - DU-080-37: Baris Borrow, Baris yang laporan hilang Borrower-nya dibatalkan saat ambang tiba: BRW `BRW 26`, Borrower `Rina Wijaya {runId}`, Asset Name `Drone Mavic Mini {runId}`, Category `Drone`, Duration `3 Days`, Status baris `Borrowed`, Due date reminders `D-3, D-1, D-day`, Record hilang `Waiting for Confirmation`.
  - DU-080-38: Baris Borrow, Baris Borrowed dengan Extension Request menunggu review yang diteruskan ke approval: BRW `BRW 27`, Borrower `Rina Wijaya {runId}`, Asset Name `Tablet Lenovo {runId}`, Category `Tablet`, Duration `3 Days`, Status baris `Borrowed`, Extension menunggu `review Aktor Borrow`.
  - DU-080-39: Pengguna, Approver kedua: Name `Rizal Hakim {runId}`, Role `Approver`, Group penugasan `Head Office {runId}`.
  - DU-080-40: Baris Borrow, Baris Waiting for Approval dengan dua approver, satu sudah bertindak: BRW `BRW 28`, Borrower `Rina Wijaya {runId}`, Asset Name `Papan Presentasi {runId}`, Category `Furnitur`, Duration `3 Days`, Status baris `Waiting for Approval`, Requester `Tika Rahma {runId}`, Approver `Sari Dewi {runId}` (belum bertindak) dan `Rizal Hakim {runId}` (sudah Approve), Approval type `All`.
  - DU-080-41: Baris Borrow, Baris Waiting for Approval yang timeout lalu Draft hasilnya di-Submit setelah approver pada aturan efektif aset berubah: BRW `BRW 29`, Borrower `Rina Wijaya {runId}`, Asset Name `Printer Laser Brother {runId}`, Category `Printer`, Duration `3 Days`, Status baris `Waiting for Approval`, Requester `Tika Rahma {runId}`, Approver pada aturan efektif aset `Sari Dewi {runId}` lalu diubah menjadi `Rizal Hakim {runId}` sebelum Draft di-Submit.
  - DU-080-42: Baris Borrow, Baris Waiting for Handover yang tanggalnya melewati masa Duration sebelum Transaction timeout: BRW `BRW 30`, Borrower `Rina Wijaya {runId}`, Asset Name `Speaker Aktif {runId}`, Category `Audio`, Duration `1 Days`, Status baris `Waiting for Handover`, Requester `Tika Rahma {runId}`.
- Kondisi:
  - Time Zone General Settings penyewa berlaku sebagai nilai lingkungan.
  - Level Feature Suite Borrowing bernilai `Full` kecuali entri data yang menyebut level lain.
  - Transaction timeout mengikuti Company default saja dan tidak di-snapshot; setting efektif pengingat mengikuti nilai efektif aset dan berlaku sebagai snapshot baris.

## Test Steps

### Due date baris Days dan Time Zone penyewa
1. Verifikasi Due date `Laptop Dell Latitude {runId}` adalah pukul `23:59:59` pada tanggal jatuh tempo menurut Time Zone General Settings penyewa
2. Verifikasi tanggal handover `Laptop Dell Latitude {runId}` pukul `00:30` dibaca di Time Zone yang sama, sehingga tanggal handover adalah tanggal menurut zona penyewa walau di UTC waktu itu masih tanggal sebelumnya, dan Due date jatuh 2 hari sesudahnya
3. Verifikasi Due date baris Days disimpan sebagai instan UTC absolut
4. Verifikasi Time Zone General Settings menentukan tampilan, jam Due date baris Days, dan batas H+1 Overdue pada saat dievaluasi

### Overdue per baris dan penanda Overdue
5. Waktu berlalu sampai pukul `00:00` pada H+1 setelah Due date `Laptop Dell Latitude {runId}`
6. Verifikasi baris `Laptop Dell Latitude {runId}` menjadi `Overdue` mulai pukul `00:00` pada H+1 menurut Time Zone saat dievaluasi
7. Verifikasi penanda `Overdue` tampil di samping status header dan bukan menjadi status header
8. Verifikasi Needs attention `Borrow overdue` dengan aksi `Return` tampil pada aset itu di daftar aset dan detail aset
9. Verifikasi Borrow Log mencatat node `Overdue` dengan pelaku `System`
10. Waktu berlalu 1 jam setelah Due date `Walkie Talkie Motorola {runId}`
11. Verifikasi baris Hours menjadi `Overdue` 1 jam setelah Due date baris itu, dihitung per baris
12. Verifikasi notifikasi Overdue dikirim satu kali per baris pada saat itu
13. Verifikasi tidak ada eskalasi lanjutan sesudah notifikasi Overdue

### Pengingat Due date mengikuti setting efektif dan berhenti saat Returned
14. Job harian berjalan pukul `00:00` zona waktu penyewa pada `D-3` sebelum tanggal Due date `Laptop Asus Zenbook {runId}`
15. Verifikasi pengingat `D-3` dikirim ke Borrower oleh job harian terhadap tanggal kalender Due date
16. Verifikasi pengingat mengikuti setting efektif aset `D-3, D-1, D-day`
17. Waktu berlalu sampai 1 jam sebelum Due date `Meeting Mic Set {runId}`
18. Verifikasi pengingat baris Hours dikirim 1 jam sebelum Due date
19. Waktu berlalu sampai saat Due date `Meeting Mic Set {runId}`
20. Verifikasi pengingat baris Hours dikirim saat Due date
21. Job harian berjalan pukul `00:00` pada `D-1` sebelum tanggal Due date `Laptop Asus Zenbook {runId}`
22. Verifikasi pengingat `D-1` dikirim ke Borrower
23. Asset Admin mengembalikan `Laptop Asus Zenbook {runId}`
24. Job harian berjalan pukul `00:00` pada `D-day`, yaitu tanggal Due date `Laptop Asus Zenbook {runId}`
25. Verifikasi pengingat `D-day` tidak dikirim karena baris sudah `Returned`

### Block new borrow when overdue
26. Asset Admin mengajukan BRW baru atas `Kursi Lipat Rapat {runId}` dengan Borrower `Bagas Prasetyo {runId}` yang punya baris `Overdue`
27. Verifikasi pengajuan ditolak karena Borrower dengan baris `Overdue` tidak bisa menjadi Borrower pada pengajuan baru saat Block new borrow when overdue `ON`
28. Asset Admin mengembalikan `Hard Disk Eksternal {runId}`, satu-satunya baris `Overdue` milik `Bagas Prasetyo {runId}`
29. Asset Admin mengajukan BRW baru atas `Kursi Lipat Rapat {runId}` dengan Borrower `Bagas Prasetyo {runId}`
30. Verifikasi pengajuan diterima setelah semua baris `Overdue` Borrower itu `Returned`

### Waktu absolut, jam Hours, DST, dan perubahan Time Zone
31. Verifikasi Due date disimpan sebagai waktu absolut UTC
32. Verifikasi durasi satuan Hours dihitung sebagai jam absolut
33. Waktu berlalu melewati pergantian DST atas baris `Mikrofon Wireless Shure {runId}`
34. Verifikasi pergantian DST tidak menggeser Due date
35. Time Zone General Settings penyewa diubah
36. Verifikasi Due date absolut UTC tidak berubah dan durasi Hours tetap jam absolut
37. Verifikasi hanya tampilan dan batas H+1 Overdue pukul `00:00` yang mengikuti Time Zone saat dievaluasi

### Laporan hilang Borrower menunggu konfirmasi saat ambang Due date atau Overdue tiba
38. Waktu berlalu sampai ambang Due date dan Overdue `Drone Mini {runId}` tiba saat laporan hilang Borrower berstatus `Waiting for Confirmation`
39. Verifikasi `borrow_due_soon` varian Borrower tidak dikirim
40. Verifikasi `borrow_overdue` varian Borrower tidak dikirim
41. Verifikasi baris tetap menjadi `Overdue` dan `borrow_overdue` varian Aktor Borrow dikirim
42. Asset Admin `Maya Putri {runId}` menolak laporan hilang atas `Drone Mini {runId}`
43. Verifikasi ambang yang sudah lewat tidak dikirim mundur
44. Verifikasi `borrow_overdue` varian Borrower dikirim saat itu karena baris `Overdue` dan belum pernah dikirim

### Baris Borrowed dan Overdue tidak pernah ditutup otomatis oleh timeout
45. Transaction timeout berlalu atas baris `Monitor Samsung {runId}` yang `Overdue`
46. Verifikasi Overdue tidak pernah ditutup otomatis oleh timeout dan baris tetap `Overdue`
47. Verifikasi baris Borrowed dan Overdue tidak pernah dikembalikan atau ditutup otomatis
48. Verifikasi yang dapat ditutup timeout hanya pengajuan Extension di baris itu
49. Asset Admin mengirim Cancel Borrow atas baris `Monitor Samsung {runId}` yang `Overdue`
50. Verifikasi Cancel ditolak karena baris Borrowed dan Overdue hanya bisa Return
51. Asset Admin mengirim Cancel Borrow atas baris `Tripod Studio {runId}` yang masih `Waiting for Handover`
52. Verifikasi Cancel diperbolehkan sebelum handover

### Transaction timeout menutup baris dan mengembalikan aset ke Draft baru
53. Transaction timeout berlalu atas baris `Laptop Lenovo ThinkPad {runId}` dan `Proyektor Mini {runId}` yang `Waiting for Approval`, sementara `Layar Proyektor {runId}` masih berjalan
54. Verifikasi Transaction timeout berlaku untuk `Waiting for Approval` dan `Waiting for Handover`
55. Verifikasi baris yang melewatinya ditutup `Canceled` oleh `System` dengan alasan `Timed out (Waiting for Approval)`
56. Verifikasi hitungan timeout dimulai sejak baris masuk status itu
57. Verifikasi baris yang melewati Transaction timeout tercatat di tab History
58. Verifikasi aset baris yang timeout dikembalikan ke Draft baru
59. Verifikasi pengembalian ke Draft baru itu terjadi pada level plan `Full`
60. Verifikasi Custody aset dilepas ke `Available`
61. Verifikasi baris yang timeout tetap di BRW asal sebagai `Canceled` dengan nomornya bersama baris yang masih berjalan
62. Verifikasi jejak audit utuh karena baris tetap di BRW asal
63. Verifikasi baris lain di BRW yang sama tidak terpengaruh
64. Verifikasi asetnya beserta Duration, Purpose, dan Note dikumpulkan ke satu Draft baru tanpa nomor BRW berisi `Restored from [BRW No.]`
65. Verifikasi Draft baru berisi Borrower `Bagas Prasetyo {runId}` dan aset baris yang dibatalkan dengan Duration dan Purpose per baris serta Note yang sama
66. Verifikasi baris satu BRW yang timeout pada run job yang sama dikumpulkan ke satu Draft baru
67. Verifikasi node `Canceled by System` memuat tautan Draft
68. Verifikasi notifikasi 1 hari sebelum dan saat baris dikembalikan dikirim ke pengaju `Tika Rahma {runId}` dan approver yang belum bertindak
69. Verifikasi pembuat Draft baru adalah pengaju BRW `Tika Rahma {runId}`
70. Verifikasi pola hasilnya sama dengan Cancel dengan `Save as Draft to edit`
71. Transaction timeout berlalu atas baris `Layar Proyektor {runId}` pada run berikutnya
72. Verifikasi baris yang timeout pada run berikutnya membuat Draft baru terpisah tanpa menambah ke Draft yang sudah ada
73. Verifikasi bila semua baris BRW sudah tertutup, BRW asal berstatus `Canceled` dan tampil di tab History
74. Asset Admin `Tika Rahma {runId}` mengajukan Submit atas Draft hasil timeout `Laptop Lenovo ThinkPad {runId}`
75. Verifikasi Draft tidak memiliki nomor dan nomor BRW baru diberikan saat Submit
76. Verifikasi approval dan snapshot Draft baru dihitung ulang saat Submit
77. Verifikasi aturan efektif dan approver di-snapshot ulang saat Submit
78. Verifikasi Draft baru mengikuti aturan Draft bersama dan kelayakan asetnya dievaluasi ulang saat Submit
79. Verifikasi Draft tidak memiliki timeout, termasuk Draft hasil timeout

### Batas pengambilan baris Waiting for Handover
80. Transaction timeout berlalu sejak baris `Tripod Kamera {runId}` menjadi `Waiting for Handover`
81. Verifikasi baris Waiting for Handover yang belum diserahkan dalam Transaction timeout ditutup `Canceled` dengan alasan `Not picked up`
82. Verifikasi asetnya kembali ke Draft baru
83. Verifikasi pengingat 1 hari sebelum batas pengambilan dikirim sebagai `borrow_almost_timeout` varian PIC admin ke Requester `Tika Rahma {runId}`
84. Verifikasi Borrower `Rina Wijaya {runId}` tidak menerima pengingat itu
85. Verifikasi batas pengambilan dihitung per baris
86. Verifikasi tidak ada no-show berbasis tanggal
87. Verifikasi masa pinjam baru dimulai saat handover
88. Transaction timeout berlalu atas baris self-service `Camera Sony Alpha {runId}` yang langsung `Borrowed`
89. Verifikasi batas pengambilan tidak berlaku untuk pinjaman self-service yang langsung `Borrowed`

### Pengajuan Extension yang timeout
90. Transaction timeout berlalu atas Extension Request `Gimbal DJI {runId}` yang menunggu review Aktor Borrow
91. Verifikasi Extension ditutup oleh `System` sebagai Extension `Canceled` dengan alasan `Timed out (Waiting for Review)` dan node `Extension canceled`
92. Verifikasi status tampil baris `Extension Request` kembali `Borrowed`
93. Verifikasi Borrow Log mencatat node `Extension canceled` dan Borrower diberi tahu
94. Verifikasi barisnya tidak ikut kembali ke Draft
95. Transaction timeout berlalu atas Extension Request `Kamera Fujifilm {runId}` yang Due date lamanya sudah lewat
96. Verifikasi barisnya tetap `Overdue` karena Due date lama sudah lewat
97. Transaction timeout berlalu atas Extension Approval `Lensa Sigma {runId}`
98. Verifikasi Extension ditutup `Canceled` oleh `System` dengan alasan `Timed out (Waiting for Approval)`
99. Verifikasi hitungan Transaction timeout Extension dimulai sejak Extension masuk status itu
100. Asset Admin meneruskan Extension Request `Tablet Samsung {runId}` ke approval
101. Verifikasi hitungan Transaction timeout dimulai lagi saat Extension Request diteruskan ke approval
102. Verifikasi peringatan 1 hari untuk Extension yang menunggu review tidak dikirim

### Level plan saat job Transaction timeout berjalan
103. Transaction timeout berlalu atas baris `Printer Warna Epson {runId}` pada level plan `Basic` saat job berjalan
104. Verifikasi level Feature Suite Borrowing yang berlaku saat job berjalan menentukan hasilnya
105. Verifikasi baris ditutup `Canceled` oleh `System` dengan alasan `Timed out (Waiting for Approval)` tanpa Draft baru karena pada level Basic dan None Draft tidak ada
106. Verifikasi tidak ada Draft yang tersimpan maupun dipulihkan pada level itu
107. Transaction timeout berlalu atas Extension Approval `Mesin Bor Listrik {runId}` pada level plan `Basic` saat job berjalan
108. Verifikasi pengajuan Extension yang timeout selalu menjadi Extension `Canceled` oleh System dan barisnya kembali `Borrowed`, bukan Draft
109. Waktu berlalu sampai `Server Rack Mini {runId}` melewati Due date pada level plan `None`
110. Verifikasi Overdue tetap dihitung
111. Verifikasi pengingat dan `borrow_overdue` tidak dikirim

### Client Suspended, Expired, atau Grace tidak menghentikan job sistem
112. Transaction timeout berlalu atas baris `Lampu Studio {runId}` saat Client berstatus `Suspended`
113. Verifikasi Transaction timeout tetap menutup baris yang menunggu karena job tanpa Aktor tidak diblokir
114. Waktu berlalu sampai `Reflektor Studio {runId}` melewati Due date saat Client berstatus `Suspended`
115. Verifikasi status Overdue tetap dihitung
116. Verifikasi baris Borrowed dan Overdue tidak pernah ditutup job

### Pengingat D-day dikirim oleh job harian untuk baris Days
117. Job harian berjalan pukul `00:00` pada `D-day`, yaitu tanggal Due date `Laptop Acer Swift {runId}`
118. Verifikasi pengingat `D-day` dikirim ke Borrower oleh job harian pukul `00:00` pada tanggal Due date, mengikuti setting efektif aset `D-3, D-1, D-day`

### Overdue dihitung per baris dalam satu BRW dan penanda Overdue bila minimal satu baris Overdue
119. Waktu berlalu sampai pukul `00:00` pada H+1 setelah Due date `Kursi Tamu {runId}`, sebelum Due date `Meja Tamu {runId}` lewat
120. Verifikasi baris `Kursi Tamu {runId}` menjadi `Overdue` dan baris `Meja Tamu {runId}` tetap `Borrowed`
121. Verifikasi penanda `Overdue` tampil pada header BRW itu walau hanya satu baris yang `Overdue`
122. Waktu berlalu sampai pukul `00:00` pada H+1 setelah Due date `Meja Tamu {runId}`
123. Verifikasi baris `Meja Tamu {runId}` menjadi `Overdue` pada waktunya sendiri, dihitung per baris

### Tidak ada eskalasi lanjutan sesudah notifikasi Overdue
124. Waktu berlalu 1 hari sesudah notifikasi Overdue `Walkie Talkie Motorola {runId}` dikirim
125. Verifikasi tidak ada notifikasi eskalasi lanjutan untuk baris `Walkie Talkie Motorola {runId}` sesudah waktu berlalu

### Cancel Borrow ditolak pada baris Borrowed
126. Asset Admin mengirim Cancel Borrow atas baris `Proyektor Kecil {runId}` yang `Borrowed`
127. Verifikasi Cancel ditolak karena baris Borrowed hanya bisa Return
128. Verifikasi baris `Proyektor Kecil {runId}` tetap `Borrowed`

### Draft tidak memiliki timeout
129. Transaction timeout berlalu atas Draft `Layar Proyektor {runId}` hasil timeout yang masih Draft
130. Verifikasi Draft `Layar Proyektor {runId}` tetap ada dan tidak ditutup oleh timeout

### Batas pengambilan dihitung per baris tanpa no-show berbasis tanggal
131. Waktu berlalu sampai batas Transaction timeout `Sound System {runId}` terlewati, sementara `Mixer Panggung {runId}` yang masuk `Waiting for Handover` belakangan belum melewati batasnya sendiri
132. Verifikasi baris `Sound System {runId}` ditutup `Canceled` dengan alasan `Not picked up`
133. Verifikasi baris `Mixer Panggung {runId}` di BRW yang sama tetap `Waiting for Handover` dan tidak ditutup karena batas dihitung per baris, bukan per BRW dan bukan berdasarkan tanggal

### Node Extension canceled pada timeout approval
134. Verifikasi Borrow Log `Lensa Sigma {runId}` mencatat node `Extension canceled` oleh `System` atas Extension yang timeout saat menunggu approval

### Hitungan timeout dimulai lagi saat Extension Request diteruskan ke approval
135. Waktu berlalu sebagian Transaction timeout sejak Extension Request `Tablet Lenovo {runId}` menunggu review, belum melewati batas
136. Asset Admin meneruskan Extension Request `Tablet Lenovo {runId}` ke approval
137. Waktu berlalu sampai batas yang dihitung dari Extension Request awal terlewati, tetapi batas baru sejak diteruskan belum terlewati
138. Verifikasi Extension `Tablet Lenovo {runId}` belum ditutup timeout dan tetap menunggu approval karena hitungan dimulai lagi saat diteruskan

### Laporan hilang Borrower dibatalkan saat ambang Due date atau Overdue sudah lewat
139. Waktu berlalu sampai ambang Due date dan Overdue `Drone Mavic Mini {runId}` tiba saat laporan hilang Borrower berstatus `Waiting for Confirmation`
140. Borrower membatalkan laporan hilang atas `Drone Mavic Mini {runId}` dengan `Cancel Missing Report`
141. Verifikasi ambang yang sudah lewat tidak dikirim mundur untuk `Drone Mavic Mini {runId}`
142. Verifikasi `borrow_overdue` varian Borrower dikirim saat laporan dibatalkan karena baris `Overdue` dan belum pernah dikirim

### Notifikasi timeout hanya ke pengaju dan approver yang belum bertindak
143. Transaction timeout berlalu atas baris `Papan Presentasi {runId}` yang `Waiting for Approval`, sesudah approver `Rizal Hakim {runId}` menyetujui dan `Sari Dewi {runId}` belum bertindak
144. Verifikasi notifikasi 1 hari sebelum dan saat baris dikembalikan dikirim ke pengaju `Tika Rahma {runId}` dan approver `Sari Dewi {runId}` yang belum bertindak
145. Verifikasi approver `Rizal Hakim {runId}` yang sudah bertindak tidak menerima notifikasi itu

### Draft hasil timeout di-Submit dengan aturan efektif yang sudah berubah
146. Transaction timeout berlalu atas baris `Printer Laser Brother {runId}` yang `Waiting for Approval` dengan approver `Sari Dewi {runId}`
147. Verifikasi baris `Printer Laser Brother {runId}` ditutup `Canceled` oleh `System` dengan alasan `Timed out (Waiting for Approval)` dan asetnya masuk Draft baru
148. Approver pada aturan efektif aset `Printer Laser Brother {runId}` diubah dari `Sari Dewi {runId}` menjadi `Rizal Hakim {runId}` sebelum Draft di-Submit
149. Asset Admin `Tika Rahma {runId}` mengajukan Submit atas Draft hasil timeout `Printer Laser Brother {runId}`
150. Verifikasi aturan efektif dan approver baris `Printer Laser Brother {runId}` di-snapshot ulang saat Submit: approver pada baris baru adalah `Rizal Hakim {runId}`, bukan `Sari Dewi {runId}` dari snapshot lama
151. Verifikasi approval baris baru dihitung ulang saat Submit: baris `Waiting for Approval` menunggu keputusan `Rizal Hakim {runId}`

### Tidak ada no-show berbasis tanggal
152. Waktu berlalu sampai tanggal melewati masa Duration `1 Days` baris `Speaker Aktif {runId}` sejak masuk `Waiting for Handover`, sementara Transaction timeout belum terlewati
153. Verifikasi baris `Speaker Aktif {runId}` tetap `Waiting for Handover` dan tidak ditutup walau tanggal sudah melewati masa Duration
154. Waktu berlalu sampai Transaction timeout `Speaker Aktif {runId}` terlewati
155. Verifikasi baris `Speaker Aktif {runId}` ditutup `Canceled` dengan alasan `Not picked up`, sesuai batas Transaction timeout dan bukan tanggal
