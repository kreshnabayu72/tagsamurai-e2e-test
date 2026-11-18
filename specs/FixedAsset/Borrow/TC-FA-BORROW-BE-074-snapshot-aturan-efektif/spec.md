---
id: TC-FA-BORROW-BE-074-snapshot-aturan-efektif
title: "Aturan efektif tiap baris di-snapshot saat Submit dan perubahan setting atau data sesudahnya tidak berlaku surut"
layer: be-e2e
priority: Medium
caseType: Positive
status: draft
owner: BE
sourceRules: ["BORROW-LOGIC-02a", "BORROW-LOGIC-02b", "BORROW-LOGIC-02c", "BORROW-LOGIC-02d", "BORROW-LOGIC-02e", "BORROW-LOGIC-02f", "BORROW-LOGIC-02g", "BORROW-LOGIC-02h", "BORROW-LOGIC-02i", "BORROW-LOGIC-02j", "BORROW-LOGIC-02k", "BORROW-LOGIC-02l", "EC-BRW-55", "EC-BRW-56", "EC-BRW-57", "EC-BRW-58", "EC-BRW-59", "EC-BRW-60", "EC-BRW-61", "EC-BRW-62", "EC-BRW-63", "EC-BRW-64", "EC-BRW-65", "EC-BRW-66", "§9.4.3#b6", "§9.10#r1", "§9.10#r2", "§9.10#r3", "§9.10#r4", "§9.10#r5", "§9.10#r6", "§9.10#r7", "§9.10#r8", "§9.10#r9", "§9.10#r10", "§9.10#r11", "§9.10#r12", "§9.10#r13", "§9.10#r14"]
smoke: []
dependsOn: []
trace:
  "BORROW-LOGIC-02a": 4
  "BORROW-LOGIC-02b": 2
  "BORROW-LOGIC-02c": 5
  "BORROW-LOGIC-02d": 6
  "BORROW-LOGIC-02e": 9
  "BORROW-LOGIC-02f": 7
  "BORROW-LOGIC-02g": [25, 51]
  "BORROW-LOGIC-02h": 17
  "BORROW-LOGIC-02i": 15
  "BORROW-LOGIC-02j": [58, 60]
  "BORROW-LOGIC-02k": 58
  "BORROW-LOGIC-02l": 61
  "EC-BRW-55": 12
  "EC-BRW-56": [15, 17]
  "EC-BRW-57": 22
  "EC-BRW-58": [25, 27]
  "EC-BRW-59": 31
  "EC-BRW-60": [40, 42]
  "EC-BRW-61": 44
  "EC-BRW-62": [58, 60, 61, 62]
  "EC-BRW-63": [33, 34]
  "EC-BRW-64": 38
  "EC-BRW-65": 36
  "EC-BRW-66": 51
  "§9.4.3#b6": 17
  "§9.10#r1": 2
  "§9.10#r2": 8
  "§9.10#r3": 4
  "§9.10#r4": 19
  "§9.10#r5": 49
  "§9.10#r6": 42
  "§9.10#r7": [7, 27]
  "§9.10#r8": 46
  "§9.10#r9": 48
  "§9.10#r10": 53
  "§9.10#r11": [29, 31]
  "§9.10#r12": 55
  "§9.10#r13": 60
  "§9.10#r14": 56
---

# Aturan efektif tiap baris di-snapshot saat Submit dan perubahan setting atau data sesudahnya tidak berlaku surut

## Prerequisites
- Aktor: Aktor Borrow (Asset Admin) yang cakupannya meliputi `Head Office {runId}`, `Gudang Pusat {runId}`, dan `Gudang Dingin {runId}`.
  - Aktor Admin yang berwenang mengubah Transaction Settings dan data Borrower, hanya untuk langkah perubahan setting dan data.
- Data:
  - DU-074-1: Group, Group asal dengan Division: Name `Head Office {runId}`, Division `Operasional {runId}`.
  - DU-074-2: Group, Group asal dengan override Max duration: Name `Gudang Pusat {runId}`, Division `Operasional {runId}`, Override Group `Max duration 6 Days`.
  - DU-074-3: Group, Group asal dengan override Deny: Name `Gudang Dingin {runId}`, Division `Operasional {runId}`, Override Group `Allow Borrow Deny`.
  - DU-074-4: Group, Group tujuan pindah Borrower: Name `Branch Surabaya {runId}`, Division `Pemasaran {runId}`.
  - DU-074-5: User, Borrower karyawan aktif dengan akun login: Name `Hana Pertiwi {runId}`, Group `Head Office {runId}`, Division `Operasional {runId}`, Status `Aktif`.
  - DU-074-6: User, Borrower karyawan aktif dengan akun login: Name `Ilham Maulana {runId}`, Group `Head Office {runId}`, Division `Operasional {runId}`, Status `Aktif`.
  - DU-074-7: User, Borrower karyawan aktif dengan akun login: Name `Lina Marlina {runId}`, Group `Head Office {runId}`, Division `Operasional {runId}`, Status `Aktif`.
  - DU-074-8: User, Borrower karyawan aktif dengan akun login: Name `Joko Widodo {runId}`, Group `Head Office {runId}`, Division `Operasional {runId}`, Status `Aktif`.
  - DU-074-9: User, Borrower karyawan aktif dengan akun login: Name `Kiki Amelia {runId}`, Group `Head Office {runId}`, Division `Operasional {runId}`, Status `Aktif`.
  - DU-074-10: User, Borrower karyawan aktif dengan akun login: Name `Mira Setiawati {runId}`, Group `Head Office {runId}`, Division `Operasional {runId}`, Status `Aktif`.
  - DU-074-11: User, Approver Group Head Office pada snapshot: Name `Rina Wijaya {runId}`, Role `Approver`, Cakupan `Head Office {runId}`.
  - DU-074-12: User, Approver baru yang ditambahkan ke Approver Group sesudah Submit: Name `Agus Salim {runId}`, Role `Approver`, Cakupan `Head Office {runId}`.
  - DU-074-13: Category, Category Elektronik dengan Max duration 10 Days: Name `Elektronik {runId}`, Max duration `10`, Unit `Days`, Allow Borrow `Allow`.
  - DU-074-14: Category, Category yang Max duration-nya diperkecil sesudah Draft disimpan: Name `Peralatan Kantor {runId}`, Max duration `10`, Unit `Days`.
  - DU-074-15: Category, Category yang Duration unit-nya diubah dari Days ke Hours: Name `Monitor {runId}`, Max duration `10`, Unit `Days`.
  - DU-074-16: Category, Category awal aset presentasi, dipindah sesudah Submit: Name `Perangkat Presentasi {runId}`, Max duration `10`, Unit `Days`.
  - DU-074-17: Category, Category dengan batas Max assets per borrower: Name `Laptop Kerja {runId}`, Max assets per borrower `2`.
  - DU-074-18: Asset, Aset yang dipinjam: Name `Laptop Asus Zenbook {runId}`, Group asal `Head Office {runId}`, Condition `Normal`, Custody `Available`, Category `Elektronik {runId}`.
  - DU-074-19: Asset, Aset yang dipinjam: Name `Laptop Lenovo Yoga {runId}`, Group asal `Head Office {runId}`, Condition `Normal`, Custody `Available`, Category `Elektronik {runId}`, Override Asset Name `Max duration 8 Days`.
  - DU-074-20: Asset, Aset yang dipinjam: Name `Laptop MSI Modern {runId}`, Group asal `Gudang Pusat {runId}`, Condition `Normal`, Custody `Available`, Category `Elektronik {runId}`, Override Asset Name `Max duration 8 Days`.
  - DU-074-21: Asset, Aset yang dipinjam: Name `Laptop HP EliteBook {runId}`, Group asal `Gudang Pusat {runId}`, Condition `Normal`, Custody `Available`, Category `Elektronik {runId}`, Override Asset Name `Max duration 8 Days`, Override Asset `Max duration 4 Days`.
  - DU-074-22: Asset, Aset yang dipinjam: Name `Laptop Acer Aspire {runId}`, Group asal `Gudang Dingin {runId}`, Condition `Normal`, Custody `Available`, Category `Elektronik {runId}`, Override Asset `Allow Borrow Allow`.
  - DU-074-23: Asset, Aset yang dipinjam: Name `Laptop Toshiba Dynabook {runId}`, Group asal `Head Office {runId}`, Condition `Normal`, Custody `Available`, Category `Peralatan Kantor {runId}`.
  - DU-074-24: Draft, Draft Hana yang disimpan sebelum Max duration Category diperkecil: Borrower `Hana Pertiwi {runId}`, Aset 1 `Laptop Toshiba Dynabook {runId}`, Duration `9`, Unit `Days`, Purpose `Survei`.
  - DU-074-25: Asset, Aset yang dipinjam: Name `Laptop Dell XPS {runId}`, Group asal `Head Office {runId}`, Condition `Normal`, Custody `Available`, Category `Elektronik {runId}`, Override Asset `Max duration 6 Days`, Max extensions `1`.
  - DU-074-26: Asset, Aset yang dipinjam: Name `Laptop Lenovo T14 {runId}`, Group asal `Head Office {runId}`, Condition `Normal`, Custody `Available`, Category `Elektronik {runId}`, Override Asset `Max duration 6 Days`.
  - DU-074-27: Asset, Aset yang dipinjam: Name `Printer Canon IP {runId}`, Group asal `Head Office {runId}`, Condition `Normal`, Custody `Available`, Category `Elektronik {runId}`, Override Asset `Allow Borrow Allow`.
  - DU-074-28: Asset, Aset yang dipinjam: Name `Scanner Brother {runId}`, Group asal `Head Office {runId}`, Condition `Normal`, Custody `Available`, Category `Elektronik {runId}`, Allowed borrower `semua karyawan`.
  - DU-074-29: Asset, Aset yang dipinjam: Name `Printer Epson L3250 {runId}`, Group asal `Head Office {runId}`, Condition `Normal`, Custody `Available`, Category `Elektronik {runId}`, Override Asset `Allow Borrow Deny`.
  - DU-074-30: Asset, Aset yang dipinjam: Name `Scanner Fujitsu {runId}`, Group asal `Head Office {runId}`, Condition `Normal`, Custody `Available`, Category `Elektronik {runId}`, Allowed borrower `Same Group only`.
  - DU-074-31: Asset, Aset yang dipinjam: Name `Tablet iPad Air {runId}`, Group asal `Head Office {runId}`, Condition `Normal`, Custody `Available`, Category `Elektronik {runId}`, Require approval `OFF`, Auto-approve `sampai 5 hari`.
  - DU-074-32: Asset, Aset yang dipinjam: Name `Monitor LG UltraWide {runId}`, Group asal `Head Office {runId}`, Condition `Normal`, Custody `Available`, Category `Monitor {runId}`.
  - DU-074-33: Asset, Aset yang dipinjam: Name `Monitor Samsung Odyssey {runId}`, Group asal `Head Office {runId}`, Condition `Normal`, Custody `Available`, Category `Monitor {runId}`.
  - DU-074-34: Draft, Draft Lina dengan Duration tersimpan dalam satuan Days: Borrower `Lina Marlina {runId}`, Aset 1 `Monitor Samsung Odyssey {runId}`, Duration `3`, Unit `Days`, Purpose `Presentasi`.
  - DU-074-35: Asset, Aset yang dipinjam: Name `Proyektor Epson Pro {runId}`, Group asal `Head Office {runId}`, Condition `Normal`, Custody `Available`, Category `Perangkat Presentasi {runId}`.
  - DU-074-36: Asset, Aset yang dipinjam: Name `Excavator Komatsu {runId}`, Group asal `Head Office {runId}`, Condition `Normal`, Custody `Available`, Category `Elektronik {runId}`, Require approval `ON`, Approval type `Any one`, Approver `Rina Wijaya {runId}`.
  - DU-074-37: Asset, Aset yang dipinjam: Name `Laptop Samsung Galaxy Book {runId}`, Group asal `Head Office {runId}`, Condition `Normal`, Custody `Available`, Category `Laptop Kerja {runId}`.
  - DU-074-38: Asset, Aset yang dipinjam: Name `Laptop Apple MacBook {runId}`, Group asal `Head Office {runId}`, Condition `Normal`, Custody `Available`, Category `Laptop Kerja {runId}`.
  - DU-074-39: Asset, Aset yang dipinjam: Name `Laptop Lenovo Legion {runId}`, Group asal `Head Office {runId}`, Condition `Normal`, Custody `Available`, Category `Laptop Kerja {runId}`.
  - DU-074-40: BRW, BRW awal Joko dengan dua baris Laptop aktif: Borrower `Joko Widodo {runId}`, Aset 1 `Laptop Samsung Galaxy Book {runId}`, Status 1 `Borrowed`, Aset 2 `Laptop Apple MacBook {runId}`, Status 2 `Waiting for Approval`.
  - DU-074-41: Asset, Aset yang dipinjam: Name `Laptop Fujitsu Lifebook {runId}`, Group asal `Head Office {runId}`, Condition `Normal`, Custody `Available`, Category `Elektronik {runId}`.
  - DU-074-42: Asset, Aset yang dipinjam: Name `Laptop Axioo Hype {runId}`, Group asal `Head Office {runId}`, Condition `Normal`, Custody `Available`, Category `Elektronik {runId}`.
  - DU-074-43: Asset, Aset yang dipinjam: Name `Tablet Xiaomi Pad {runId}`, Group asal `Head Office {runId}`, Condition `Normal`, Custody `Available`, Category `Elektronik {runId}`.
  - DU-074-44: BRW, BRW awal Kiki dengan satu baris Overdue dan satu baris Waiting for Handover: Borrower `Kiki Amelia {runId}`, Aset 1 `Laptop Fujitsu Lifebook {runId}`, Status 1 `Overdue`, Aset 2 `Laptop Axioo Hype {runId}`, Status 2 `Waiting for Handover`.
  - DU-074-45: Asset, Aset yang dipinjam: Name `Kamera Fujifilm {runId}`, Group asal `Head Office {runId}`, Condition `Normal`, Custody `Available`, Category `Elektronik {runId}`, Self service `ON`.
  - DU-074-46: Asset, Aset yang dipinjam: Name `Tripod Manfrotto {runId}`, Group asal `Head Office {runId}`, Condition `Normal`, Custody `Available`, Category `Elektronik {runId}`, Photo at start `ON`, Due date reminders `D-1`, Send email notifications `OFF`.
  - DU-074-47: Asset, Aset yang dipinjam: Name `Lensa Sigma {runId}`, Group asal `Gudang Pusat {runId}`, Condition `Normal`, Custody `Available`, Category `Elektronik {runId}`.
  - DU-074-48: Asset, Aset yang dipinjam: Name `Bor Listrik Bosch {runId}`, Group asal `Head Office {runId}`, Condition `Normal`, Custody `Available`, Category `Elektronik {runId}`.
  - DU-074-49: BRW, BRW awal Hana yang menunggu approval sejak T0 - 3 hari: Borrower `Hana Pertiwi {runId}`, Aset 1 `Bor Listrik Bosch {runId}`, Status 1 `Waiting for Approval`, Masuk status `T0 - 3 hari`, Transaction timeout awal `7 hari`.
- Kondisi:
  - Block new borrow when overdue bernilai ON.
  - Max assets per borrower Company default bernilai `5`, dan batas Category `Laptop Kerja {runId}` bernilai `2`.
  - Transaction timeout Company default bernilai `7` hari sampai diubah oleh langkah kelompok Transaction timeout.
  - Time Zone penyewa dipakai untuk jam akhir Due date baris Days.

## Test Steps

### Deny pada override menang atas aturan lain
1. Aktor Borrow mengirim Submit untuk Borrower `Hana Pertiwi {runId}` dengan aset `Laptop Acer Aspire {runId}`
2. Verifikasi Submit ditolak dan baris `Laptop Acer Aspire {runId}` ditandai dengan alasan `Can't be borrowed: this asset is not available for borrowing. Contact [Name] (Manage asset & TAG).` walaupun override Asset menyatakan Allow Borrow Allow

### Aturan efektif diselesaikan menurut hierarki dan di-snapshot saat Submit
3. Aktor Borrow mengirim Submit untuk Borrower `Hana Pertiwi {runId}` dengan aset `Laptop Asus Zenbook {runId}`, `Laptop Lenovo Yoga {runId}`, `Laptop MSI Modern {runId}`, dan `Laptop HP EliteBook {runId}`, masing-masing Duration `4` Days
4. Verifikasi nilai efektif Max duration tiap baris mengikuti hierarki: `Laptop Asus Zenbook {runId}` memakai Category `10`, `Laptop Lenovo Yoga {runId}` memakai override Asset Name `8`, `Laptop MSI Modern {runId}` memakai override Group `6`, dan `Laptop HP EliteBook {runId}` memakai override Asset `4`
5. Verifikasi baris `Laptop Asus Zenbook {runId}` dan `Laptop Lenovo Yoga {runId}` dalam satu BRW punya aturan efektif berbeda
6. Verifikasi saat Submit aturan efektif tiap baris di-snapshot ke baris beserta versi setting, nilai efektif, daftar approver, dan Approval type
7. Verifikasi snapshot memuat Group `Head Office {runId}` dan Division `Operasional {runId}` Borrower saat Submit untuk menilai Allowed borrower
8. Verifikasi satuan `Days` melekat pada tiap baris dan dipakai untuk Due date dan Overdue per baris

### Draft belum punya snapshot dan dievaluasi dengan aturan terbaru
9. Verifikasi Draft atas nama `Hana Pertiwi {runId}` belum punya snapshot aturan efektif
10. Aktor Admin memperkecil Max duration Category `Peralatan Kantor {runId}` dari `10` menjadi `5` Days
11. Aktor Borrow mengirim Submit atas Draft atas nama `Hana Pertiwi {runId}` dengan Duration `9` Days
12. Verifikasi Submit ditolak karena Duration `9` melebihi Max duration terbaru `5`

### Perubahan Max duration dan Max extensions sesudah Submit tidak berlaku surut
13. Aktor Borrow mengirim Submit untuk Borrower `Ilham Maulana {runId}` dengan aset `Laptop Dell XPS {runId}`, `Laptop Lenovo T14 {runId}`, `Printer Canon IP {runId}`, dan `Scanner Brother {runId}`, masing-masing Duration `4` Days
14. Aktor Admin memperkecil override Asset Max duration baris `Laptop Dell XPS {runId}` dari `6` menjadi `3` Days
15. Verifikasi baris `Laptop Dell XPS {runId}` tetap memakai snapshot Max duration `6`, dan Duration serta Due date tidak berubah
16. Aktor Borrow mengajukan Extend baris `Laptop Dell XPS {runId}` sampai total `5` Days
17. Verifikasi Extend diterima karena memakai snapshot baris, bukan versi setting saat Extend diajukan
18. Aktor Borrow mengajukan Extend kedua baris `Laptop Dell XPS {runId}`
19. Verifikasi Extend kedua ditolak dengan `No extensions left ([Used] / [Max]).` sesuai Max extensions snapshot
20. Aktor Admin memperbesar override Asset Max duration baris `Laptop Lenovo T14 {runId}` dari `6` menjadi `12` Days
21. Aktor Borrow mengajukan Extend baris `Laptop Lenovo T14 {runId}` sampai total `8` Days
22. Verifikasi snapshot baris `Laptop Lenovo T14 {runId}` tidak berubah dan Extend ditolak dengan `Max [Limit] days in total. You can extend until [Date].` karena batas baru hanya berlaku untuk pengajuan baru

### Perubahan Allow Borrow dan Allowed borrower sesudah Submit tidak berlaku surut
23. Aktor Admin mengubah override Asset baris `Printer Canon IP {runId}` menjadi Allow Borrow Deny
24. Aktor Admin mempersempit Allowed borrower baris `Scanner Brother {runId}` menjadi `Same Group only`
25. Verifikasi baris `Printer Canon IP {runId}` dan `Scanner Brother {runId}` tetap berjalan menurut snapshot sampai selesai, termasuk Extend
26. Aktor Borrow mengirim Submit baru untuk Borrower `Ilham Maulana {runId}` dengan aset `Printer Epson L3250 {runId}` dan `Scanner Fujitsu {runId}`
27. Verifikasi hanya pengajuan baru yang ditolak dengan pesan kelayakan `Can't be borrowed: this asset is not available for borrowing. Contact [Name] (Manage asset & TAG).` dan `[Borrower] can't borrow assets from [Group].`

### Perubahan Require approval, Duration unit, Category, dan approver sesudah Submit
28. Aktor Borrow mengirim Submit untuk Borrower `Lina Marlina {runId}` dengan aset `Tablet iPad Air {runId}`, `Monitor LG UltraWide {runId}`, `Proyektor Epson Pro {runId}`, dan `Excavator Komatsu {runId}`, masing-masing Duration `3` Days
29. Verifikasi baris `Tablet iPad Air {runId}` berstatus `Waiting for Handover` dan dicatat Auto-approved, dan baris `Excavator Komatsu {runId}` berstatus `Waiting for Approval`
30. Aktor Admin menyalakan Require approval dan menghapus Auto-approve pada aset `Tablet iPad Air {runId}`
31. Verifikasi baris `Tablet iPad Air {runId}` tetap `Waiting for Handover` dan Extend berikutnya memakai snapshot Auto-approve dan Require approval saat Submit
32. Aktor Admin mengubah Duration unit Category `Monitor {runId}` dari Days menjadi Hours
33. Verifikasi baris `Monitor LG UltraWide {runId}` tetap memakai satuan Days menurut snapshot sampai selesai, termasuk Extend
34. Verifikasi Duration `3` pada Draft atas nama `Lina Marlina {runId}` dikosongkan saat Draft dibuka dan Submit ditolak sampai Duration terisi dalam satuan Hours
35. Aktor Admin memindahkan Category aset `Proyektor Epson Pro {runId}` ke `Elektronik {runId}` dan mengganti Asset Name-nya
36. Verifikasi baris `Proyektor Epson Pro {runId}` memakai snapshot sampai selesai, termasuk Extend
37. Aktor Admin menambahkan Approver `Agus Salim {runId}` ke Approver Group `Head Office {runId}` dan mencabut `Rina Wijaya {runId}`
38. Verifikasi baris `Excavator Komatsu {runId}` tetap memakai snapshot approver `Rina Wijaya {runId}` dan `Agus Salim {runId}` tidak melihat pengajuan itu

### Max assets per borrower diturunkan di bawah jumlah pinjaman aktif
39. Aktor Admin menurunkan Max assets per borrower Category `Laptop Kerja {runId}` dari `2` menjadi `1`
40. Verifikasi pinjaman aktif Borrower `Joko Widodo {runId}` tidak terpengaruh
41. Aktor Borrow mengirim Submit untuk Borrower `Joko Widodo {runId}` dengan aset `Laptop Lenovo Legion {runId}`
42. Verifikasi pengajuan baru ditolak dengan `[Name] can borrow up to [Max] assets at a time.` sampai jumlah aktif di bawah batas baru

### Block new borrow when overdue tidak menghentikan baris yang sudah diajukan
43. Aktor Borrow menyelesaikan Handover baris `Laptop Axioo Hype {runId}` milik Borrower `Kiki Amelia {runId}`
44. Verifikasi Handover berhasil walaupun Borrower punya baris Overdue karena baris memakai snapshot
45. Aktor Borrow mengirim Submit baru untuk Borrower `Kiki Amelia {runId}` dengan aset `Tablet Xiaomi Pad {runId}`
46. Verifikasi pengajuan baru ditolak dengan `[Name] has an overdue borrow: [Asset Code], due [Date]. Return it first.`

### Perubahan data Borrower dan pembacaan setting lain oleh alur
47. Aktor Borrow mengirim Submit untuk Borrower `Mira Setiawati {runId}` dengan aset `Kamera Fujifilm {runId}` dan `Tripod Manfrotto {runId}`, dan aset `Lensa Sigma {runId}` dari Group asal `Gudang Pusat {runId}`
48. Verifikasi baris `Kamera Fujifilm {runId}` berstatus `Waiting for Handover` tanpa approval karena Self service ON
49. Verifikasi Due date semua baris bernilai `—` dan masa pinjam tidak punya tanggal mulai karena Max advance booking tidak ada di Transaction Settings
50. Aktor Admin memindahkan Borrower `Mira Setiawati {runId}` ke Group `Branch Surabaya {runId}` dan mengubah Division-nya
51. Verifikasi Handover, Extend, dan Return baris Borrower `Mira Setiawati {runId}` tidak menilai ulang kelayakan, karena snapshot berlaku sampai Returned
52. Aktor Borrow menyelesaikan Handover baris `Tripod Manfrotto {runId}` tanpa foto
53. Verifikasi Handover ditolak dengan `1 asset needs a handover photo.` karena Photo at start ON
54. Waktu berlalu sampai 1 hari sebelum Due date baris `Tripod Manfrotto {runId}`
55. Verifikasi pengingat Due date dikirim ke Borrower sesuai pilihan `D-1` pada setting efektif
56. Verifikasi Borrower tidak menerima email notifikasi baris `Tripod Manfrotto {runId}` karena Send email notifications OFF, sedangkan email konfirmasi handover tetap dikirim

### Perubahan Transaction timeout menghitung ulang batas baris yang menunggu
57. Aktor Admin menyimpan Transaction timeout Company default menjadi `2` hari
58. Verifikasi batas waktu baris `Bor Listrik Bosch {runId}` yang menunggu sejak T0 - 3 hari jatuh sebelum waktu Save, sehingga disetel ke waktu Save ditambah 24 jam
59. Aktor Admin menyimpan Transaction timeout Company default menjadi `4` hari
60. Verifikasi batas waktu baris `Bor Listrik Bosch {runId}` dihitung ulang dari saat baris masuk status itu ditambah nilai baru
61. Verifikasi peringatan 1 hari sebelum batas dikirim ulang karena sisa waktu ke batas baru 24 jam atau kurang
62. Verifikasi Draft tidak terpengaruh karena tidak memiliki timeout
