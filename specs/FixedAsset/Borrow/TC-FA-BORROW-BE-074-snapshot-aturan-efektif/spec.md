---
id: TC-FA-BORROW-BE-074-snapshot-aturan-efektif
title: "Aturan efektif tiap baris di-snapshot saat Submit dan perubahan setting atau data sesudahnya tidak berlaku surut"
layer: be-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
owner: BE
sourceRules: ["BORROW-LOGIC-02a", "BORROW-LOGIC-02b", "BORROW-LOGIC-02c", "BORROW-LOGIC-02d", "BORROW-LOGIC-02e", "BORROW-LOGIC-02f", "BORROW-LOGIC-02g", "BORROW-LOGIC-02h", "BORROW-LOGIC-02i", "BORROW-LOGIC-02j", "BORROW-LOGIC-02k", "BORROW-LOGIC-02l", "EC-BRW-55", "EC-BRW-56", "EC-BRW-57", "EC-BRW-58", "EC-BRW-59", "EC-BRW-60", "EC-BRW-61", "EC-BRW-62", "EC-BRW-63", "EC-BRW-64", "EC-BRW-65", "EC-BRW-66", "§9.4.3#b6", "§9.10#r1", "§9.10#r2", "§9.10#r3", "§9.10#r4", "§9.10#r5", "§9.10#r6", "§9.10#r7", "§9.10#r8", "§9.10#r9", "§9.10#r10", "§9.10#r11", "§9.10#r12", "§9.10#r13", "§9.10#r14"]
smoke: []
dependsOn: []
trace:
  "BORROW-LOGIC-02a": [4, 101, 102]
  "BORROW-LOGIC-02b": 2
  "BORROW-LOGIC-02c": 5
  "BORROW-LOGIC-02d": 6
  "BORROW-LOGIC-02e": 9
  "BORROW-LOGIC-02f": 7
  "BORROW-LOGIC-02g": [33, 75, 77, 79]
  "BORROW-LOGIC-02h": [18, 21]
  "BORROW-LOGIC-02i": 16
  "BORROW-LOGIC-02j": [94, 97]
  "BORROW-LOGIC-02k": 91
  "BORROW-LOGIC-02l": [95, 98]
  "EC-BRW-55": 12
  "EC-BRW-56": [16, 18]
  "EC-BRW-57": [24, 27]
  "EC-BRW-58": [32, 33, 35, 109, 111]
  "EC-BRW-59": [39, 42]
  "EC-BRW-60": [56, 58, 60, 65, 113]
  "EC-BRW-61": 67
  "EC-BRW-62": [91, 92, 95, 98, 99]
  "EC-BRW-63": [47, 48]
  "EC-BRW-64": 54
  "EC-BRW-65": [52, 118]
  "EC-BRW-66": [75, 77, 79, 81]
  "§9.4.3#b6": 18
  "§9.10#r1": 2
  "§9.10#r2": [8, 44, 47]
  "§9.10#r3": [4, 18]
  "§9.10#r4": 21
  "§9.10#r5": 72
  "§9.10#r6": 60
  "§9.10#r7": [33, 35]
  "§9.10#r8": 69
  "§9.10#r9": 71
  "§9.10#r10": [83, 85]
  "§9.10#r11": [37, 42, 104, 105]
  "§9.10#r12": 87
  "§9.10#r13": [91, 94, 97]
  "§9.10#r14": [88, 89]
---

# Aturan efektif tiap baris di-snapshot saat Submit dan perubahan setting atau data sesudahnya tidak berlaku surut

## Prerequisites
- Aktor: Aktor Borrow (Asset Admin) yang cakupannya meliputi `Head Office {runId}`, `Gudang Pusat {runId}`, dan `Gudang Dingin {runId}`, serta Group `Branch Surabaya {runId}` bagi Borrower yang berada di sana.
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
  - DU-074-16: Category, Category awal aset presentasi dengan Max duration lebih kecil dari Category tujuan, dipindah sesudah Submit: Name `Perangkat Presentasi {runId}`, Max duration `5`, Unit `Days`.
  - DU-074-17: Category, Category dengan batas Max assets per borrower: Name `Laptop Kerja {runId}`, Max assets per borrower `2`.
  - DU-074-18: Asset, Aset yang dipinjam: Name `Laptop Asus Zenbook {runId}`, Group asal `Head Office {runId}`, Condition `Normal`, Custody `Available`, Category `Elektronik {runId}`.
  - DU-074-19: Asset, Aset yang dipinjam: Name `Laptop Lenovo Yoga {runId}`, Group asal `Head Office {runId}`, Condition `Normal`, Custody `Available`, Category `Elektronik {runId}`, Override Asset Name `Max duration 8 Days`.
  - DU-074-20: Asset, Aset yang dipinjam: Name `Laptop MSI Modern {runId}`, Group asal `Gudang Pusat {runId}`, Condition `Normal`, Custody `Available`, Category `Elektronik {runId}`, Override Asset Name `Max duration 8 Days`.
  - DU-074-21: Asset, Aset yang dipinjam: Name `Laptop HP EliteBook {runId}`, Group asal `Gudang Pusat {runId}`, Condition `Normal`, Custody `Available`, Category `Elektronik {runId}`, Override Asset Name `Max duration 8 Days`, Override Asset `Max duration 4 Days`.
  - DU-074-22: Asset, Aset yang dipinjam: Name `Laptop Acer Aspire {runId}`, Group asal `Gudang Dingin {runId}`, Condition `Normal`, Custody `Available`, Category `Elektronik {runId}`, Override Asset `Allow Borrow Allow`.
  - DU-074-23: Asset, Aset yang dipinjam: Name `Laptop Toshiba Dynabook {runId}`, Group asal `Head Office {runId}`, Condition `Normal`, Custody `Available`, Category `Peralatan Kantor {runId}`.
  - DU-074-24: Draft, Draft Ilham yang disimpan sebelum Max duration Category diperkecil: Borrower `Ilham Maulana {runId}`, Aset 1 `Laptop Toshiba Dynabook {runId}`, Duration `9`, Unit `Days`, Purpose `Survei`.
  - DU-074-25: Asset, Aset yang dipinjam: Name `Laptop Dell XPS {runId}`, Group asal `Head Office {runId}`, Condition `Normal`, Custody `Available`, Category `Elektronik {runId}`, Override Asset `Max duration 6 Days`, Max extensions `1`, Require approval `OFF`.
  - DU-074-26: Asset, Aset yang dipinjam: Name `Laptop Lenovo T14 {runId}`, Group asal `Head Office {runId}`, Condition `Normal`, Custody `Available`, Category `Elektronik {runId}`, Override Asset `Max duration 6 Days`, Require approval `OFF`.
  - DU-074-27: Asset, Aset yang dipinjam: Name `Printer Canon IP {runId}`, Group asal `Head Office {runId}`, Condition `Normal`, Custody `Available`, Category `Elektronik {runId}`, Override Asset `Allow Borrow Allow`, Require approval `OFF`.
  - DU-074-28: Asset, Aset yang dipinjam: Name `Scanner Brother {runId}`, Group asal `Head Office {runId}`, Condition `Normal`, Custody `Available`, Category `Elektronik {runId}`, Allowed borrower `semua karyawan`, Require approval `OFF`.
  - DU-074-29: Asset, Aset yang dipinjam: Name `Printer Epson L3250 {runId}`, Group asal `Head Office {runId}`, Condition `Normal`, Custody `Available`, Category `Elektronik {runId}`, Override Asset `Allow Borrow Deny`.
  - DU-074-30: Asset, Aset yang dipinjam: Name `Scanner Fujitsu {runId}`, Group asal `Head Office {runId}`, Condition `Normal`, Custody `Available`, Category `Elektronik {runId}`, Allowed borrower `Same Group only`.
  - DU-074-31: Asset, Aset yang dipinjam: Name `Tablet iPad Air {runId}`, Group asal `Head Office {runId}`, Condition `Normal`, Custody `Available`, Category `Elektronik {runId}`, Require approval `OFF`, Auto-approve `sampai 5 hari`.
  - DU-074-32: Asset, Aset yang dipinjam: Name `Monitor LG UltraWide {runId}`, Group asal `Head Office {runId}`, Condition `Normal`, Custody `Available`, Category `Monitor {runId}`, Require approval `OFF`.
  - DU-074-33: Asset, Aset yang dipinjam: Name `Monitor Samsung Odyssey {runId}`, Group asal `Head Office {runId}`, Condition `Normal`, Custody `Available`, Category `Monitor {runId}`.
  - DU-074-34: Draft, Draft Lina dengan Duration tersimpan dalam satuan Days: Borrower `Lina Marlina {runId}`, Aset 1 `Monitor Samsung Odyssey {runId}`, Duration `3`, Unit `Days`, Purpose `Presentasi`.
  - DU-074-35: Asset, Aset yang dipinjam: Name `Proyektor Epson Pro {runId}`, Group asal `Head Office {runId}`, Condition `Normal`, Custody `Available`, Category `Perangkat Presentasi {runId}`, Require approval `OFF`, Asset Name sesudah diganti `Proyektor Epson Pro EB {runId}`.
  - DU-074-36: Asset, Aset yang dipinjam: Name `Excavator Komatsu {runId}`, Group asal `Head Office {runId}`, Condition `Normal`, Custody `Available`, Category `Elektronik {runId}`, Require approval `ON`, Approval type `Any one`, Approver `Rina Wijaya {runId}`.
  - DU-074-37: Asset, Aset yang dipinjam: Name `Laptop Samsung Galaxy Book {runId}`, Group asal `Head Office {runId}`, Condition `Normal`, Custody `Borrowed`, Category `Laptop Kerja {runId}`.
  - DU-074-38: Asset, Aset yang dipinjam: Name `Laptop Apple MacBook {runId}`, Group asal `Head Office {runId}`, Condition `Normal`, Custody `Available`, Category `Laptop Kerja {runId}`, Require approval `OFF`.
  - DU-074-39: Asset, Aset yang dipinjam: Name `Laptop Lenovo Legion {runId}`, Group asal `Head Office {runId}`, Condition `Normal`, Custody `Available`, Category `Laptop Kerja {runId}`.
  - DU-074-40: BRW, BRW awal Joko dengan satu baris Laptop aktif: Borrower `Joko Widodo {runId}`, Aset 1 `Laptop Samsung Galaxy Book {runId}`, Status 1 `Borrowed`.
  - DU-074-41: Asset, Aset yang dipinjam: Name `Laptop Fujitsu Lifebook {runId}`, Group asal `Head Office {runId}`, Condition `Normal`, Custody `Available`, Category `Elektronik {runId}`.
  - DU-074-42: Asset, Aset yang dipinjam: Name `Laptop Axioo Hype {runId}`, Group asal `Head Office {runId}`, Condition `Normal`, Custody `Available`, Category `Elektronik {runId}`.
  - DU-074-43: Asset, Aset yang dipinjam: Name `Tablet Xiaomi Pad {runId}`, Group asal `Head Office {runId}`, Condition `Normal`, Custody `Available`, Category `Elektronik {runId}`.
  - DU-074-44: BRW, BRW awal Kiki dengan satu baris Overdue dan satu baris Waiting for Handover: Borrower `Kiki Amelia {runId}`, Aset 1 `Laptop Fujitsu Lifebook {runId}`, Status 1 `Overdue`, Aset 2 `Laptop Axioo Hype {runId}`, Status 2 `Waiting for Handover`.
  - DU-074-45: Asset, Aset yang dipinjam: Name `Kamera Fujifilm {runId}`, Group asal `Head Office {runId}`, Condition `Normal`, Custody `Available`, Category `Elektronik {runId}`, Self service `ON`, Allowed borrower `Same Group only`.
  - DU-074-46: Asset, Aset yang dipinjam: Name `Tripod Manfrotto {runId}`, Group asal `Head Office {runId}`, Condition `Normal`, Custody `Available`, Category `Elektronik {runId}`, Photo at start `ON`, Due date reminders `D-1`, Send email notifications `OFF`, Require approval `OFF`.
  - DU-074-47: Asset, Aset yang dipinjam: Name `Lensa Sigma {runId}`, Group asal `Gudang Pusat {runId}`, Condition `Normal`, Custody `Available`, Category `Elektronik {runId}`, Require approval `OFF`.
  - DU-074-48: Asset, Aset yang dipinjam: Name `Bor Listrik Bosch {runId}`, Group asal `Head Office {runId}`, Condition `Normal`, Custody `Available`, Category `Elektronik {runId}`.
  - DU-074-49: BRW, BRW awal Hana yang menunggu approval sejak T0 - 3 hari: Borrower `Hana Pertiwi {runId}`, Aset 1 `Bor Listrik Bosch {runId}`, Status 1 `Waiting for Approval`, Masuk status `T0 - 3 hari`, Transaction timeout awal `7 hari`.
  - DU-074-50: User, Borrower karyawan aktif dengan akun login di Group lain dari Group asal aset: Name `Nanda Prakoso {runId}`, Group `Branch Surabaya {runId}`, Division `Pemasaran {runId}`, Status `Aktif`.
  - DU-074-51: User, Borrower karyawan aktif dengan akun login di Group lain dari Group asal aset: Name `Putri Handayani {runId}`, Group `Branch Surabaya {runId}`, Division `Pemasaran {runId}`, Status `Aktif`.
  - DU-074-52: Asset, Aset yang dipinjam, batas Max duration-nya diperbesar sebelum Submit baru: Name `Laptop Acer Swift {runId}`, Group asal `Head Office {runId}`, Condition `Normal`, Custody `Available`, Category `Elektronik {runId}`, Override Asset `Max duration 6 Days`, Require approval `OFF`.
  - DU-074-53: Category, Category tanpa Max duration sendiri sehingga memakai Company default: Name `Alat Umum {runId}`.
  - DU-074-54: Asset, Aset yang dipinjam: Name `Mesin Fotokopi Ricoh {runId}`, Group asal `Head Office {runId}`, Condition `Normal`, Custody `Available`, Category `Alat Umum {runId}`.
  - DU-074-55: Category, Category dengan Duration unit Hours: Name `Peralatan Studio {runId}`, Max duration `12`, Unit `Hours`.
  - DU-074-56: Asset, Aset ber-Auto-approve dalam jam: Name `Mixer Audio Behringer {runId}`, Group asal `Head Office {runId}`, Condition `Normal`, Custody `Available`, Category `Peralatan Studio {runId}`, Require approval `ON`, Auto-approve `sampai 4 jam`.
  - DU-074-57: Asset, Aset ber-Auto-approve dalam jam: Name `Speaker Aktif JBL {runId}`, Group asal `Head Office {runId}`, Condition `Normal`, Custody `Available`, Category `Peralatan Studio {runId}`, Require approval `ON`, Auto-approve `sampai 4 jam`.
  - DU-074-58: Asset, Aset yang dipinjam, Allow Borrow-nya diubah menjadi Deny sebelum Submit baru: Name `Printer Brother HL {runId}`, Group asal `Head Office {runId}`, Condition `Normal`, Custody `Available`, Category `Elektronik {runId}`, Override Asset `Allow Borrow Allow`, Require approval `OFF`.
  - DU-074-59: Asset, Aset yang dipinjam, Allowed borrower-nya dipersempit sebelum Submit baru: Name `Scanner Canon DR {runId}`, Group asal `Head Office {runId}`, Condition `Normal`, Custody `Available`, Category `Elektronik {runId}`, Allowed borrower `semua karyawan`, Require approval `OFF`.
  - DU-074-60: Asset, Aset yang dipinjam: Name `Laptop Asus ROG {runId}`, Group asal `Head Office {runId}`, Condition `Normal`, Custody `Available`, Category `Laptop Kerja {runId}`.
  - DU-074-61: Asset, Aset ber-override Asset Name yang namanya diganti saat baris aktif: Name `Mikrofon Shure {runId}`, Group asal `Head Office {runId}`, Condition `Normal`, Custody `Available`, Category `Elektronik {runId}`, Override Asset Name `Max duration 3 Days`, Require approval `OFF`, Asset Name sesudah diganti `Mikrofon Shure SM58 {runId}`.
- Kondisi:
  - Block new borrow when overdue bernilai ON.
  - Max duration Company default bernilai `14` Days.
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
8. Verifikasi satuan `Days` melekat pada tiap baris sebagai satuan Duration yang diinput

### Draft belum punya snapshot dan dievaluasi dengan aturan terbaru
9. Verifikasi Draft atas nama `Ilham Maulana {runId}` yang memuat aset `Laptop Toshiba Dynabook {runId}` belum punya snapshot aturan efektif
10. Aktor Admin memperkecil Max duration Category `Peralatan Kantor {runId}` dari `10` menjadi `5` Days
11. Aktor Borrow mengirim Submit atas Draft atas nama `Ilham Maulana {runId}` yang memuat aset `Laptop Toshiba Dynabook {runId}` dengan Duration `9` Days
12. Verifikasi Submit ditolak karena Duration `9` melebihi Max duration terbaru `5`

### Perubahan Max duration dan Max extensions sesudah Submit tidak berlaku surut
13. Aktor Borrow mengirim Submit untuk Borrower `Nanda Prakoso {runId}` dengan aset `Laptop Dell XPS {runId}`, `Laptop Lenovo T14 {runId}`, `Printer Canon IP {runId}`, dan `Scanner Brother {runId}`, masing-masing Duration `4` Days
14. Aktor Borrow menyelesaikan Handover keempat baris milik Borrower `Nanda Prakoso {runId}`
15. Aktor Admin memperkecil override Asset Max duration baris `Laptop Dell XPS {runId}` dari `6` menjadi `3` Days
16. Verifikasi baris `Laptop Dell XPS {runId}` tetap memakai snapshot Max duration `6`, dan Duration serta Due date tidak berubah
17. Aktor Borrow mengajukan Extend baris `Laptop Dell XPS {runId}` sampai total `5` Days
18. Verifikasi Extend langsung berlaku tanpa pengajuan approval karena memakai snapshot baris (Max duration `6` dan Require approval OFF), bukan versi setting saat Extend diajukan
19. Aktor Admin memperbesar Max extensions baris `Laptop Dell XPS {runId}` dari `1` menjadi `3`
20. Aktor Borrow mengajukan Extend kedua baris `Laptop Dell XPS {runId}`
21. Verifikasi Extend kedua ditolak dengan `No extensions left ([Used] / [Max]).` sesuai Max extensions snapshot `1`, bukan Max extensions terbaru
22. Aktor Admin memperbesar override Asset Max duration baris `Laptop Lenovo T14 {runId}` dari `6` menjadi `12` Days
23. Aktor Borrow mengajukan Extend baris `Laptop Lenovo T14 {runId}` sampai total `8` Days
24. Verifikasi snapshot baris `Laptop Lenovo T14 {runId}` tidak berubah dan Extend ditolak dengan `Max [Limit] days in total. You can extend until [Date].` karena batas baru hanya berlaku untuk pengajuan baru, bukan Extend baris berjalan
25. Aktor Admin memperbesar override Asset Max duration `Laptop Acer Swift {runId}` dari `6` menjadi `12` Days
26. Aktor Borrow mengirim Submit baru untuk Borrower `Ilham Maulana {runId}` dengan aset `Laptop Acer Swift {runId}`, Duration `9` Days
27. Verifikasi pengajuan baru diterima tanpa penolakan Duration karena Duration `9` di atas batas lama `6` tetapi di bawah batas baru `12`

### Perubahan Allow Borrow dan Allowed borrower sesudah Submit tidak berlaku surut
28. Aktor Admin mengubah override Asset baris `Printer Canon IP {runId}` menjadi Allow Borrow Deny
29. Aktor Admin mempersempit Allowed borrower baris `Scanner Brother {runId}` menjadi `Same Group only`
30. Aktor Borrow mengajukan Extend baris `Printer Canon IP {runId}` sampai total `5` Days
31. Aktor Borrow mengajukan Extend baris `Scanner Brother {runId}` sampai total `5` Days
32. Verifikasi baris `Printer Canon IP {runId}` tetap berjalan menurut snapshot sampai selesai, termasuk Extend yang berlaku walaupun override Asset kini Allow Borrow Deny
33. Verifikasi baris `Scanner Brother {runId}` tetap berjalan menurut snapshot sampai selesai, termasuk Extend yang berlaku walaupun Borrower `Nanda Prakoso {runId}` berada di Group `Branch Surabaya {runId}`, bukan Group asal aset
34. Aktor Borrow mengirim Submit baru untuk Borrower `Putri Handayani {runId}` dengan aset `Printer Epson L3250 {runId}` dan `Scanner Fujitsu {runId}`
35. Verifikasi hanya pengajuan baru yang ditolak dengan pesan kelayakan `Can't be borrowed: this asset is not available for borrowing. Contact [Name] (Manage asset & TAG).` dan `[Borrower] can't borrow assets from [Group].`

### Perubahan Require approval, Duration unit, Category, dan approver sesudah Submit
36. Aktor Borrow mengirim Submit untuk Borrower `Lina Marlina {runId}` dengan aset `Tablet iPad Air {runId}`, `Monitor LG UltraWide {runId}`, `Proyektor Epson Pro {runId}`, dan `Excavator Komatsu {runId}`, masing-masing Duration `3` Days
37. Verifikasi baris `Tablet iPad Air {runId}` berstatus `Waiting for Handover` dan dicatat Auto-approved, dan baris `Excavator Komatsu {runId}` berstatus `Waiting for Approval`
38. Aktor Admin menyalakan Require approval dan menghapus Auto-approve pada aset `Tablet iPad Air {runId}`
39. Verifikasi baris `Tablet iPad Air {runId}` tetap `Waiting for Handover`
40. Aktor Borrow menyelesaikan Handover baris `Tablet iPad Air {runId}`
41. Aktor Borrow mengajukan Extend baris `Tablet iPad Air {runId}` sampai total `4` Days
42. Verifikasi Extend langsung berlaku tanpa pengajuan approval karena memakai snapshot Require approval OFF dan Auto-approve saat Submit
43. Aktor Borrow menyelesaikan Handover baris `Monitor LG UltraWide {runId}`
44. Verifikasi Due date baris `Monitor LG UltraWide {runId}` terisi dan dihitung dalam satuan `Days` dari Duration `3` sejak Handover
45. Aktor Admin mengubah Duration unit Category `Monitor {runId}` dari Days menjadi Hours
46. Aktor Borrow mengajukan Extend baris `Monitor LG UltraWide {runId}` sampai total `5` Days
47. Verifikasi baris `Monitor LG UltraWide {runId}` tetap memakai satuan Days menurut snapshot sampai selesai, dan Extend berlaku dalam satuan Days
48. Verifikasi Duration `3` pada Draft atas nama `Lina Marlina {runId}` dikosongkan saat Draft dibuka dan Submit ditolak sampai Duration terisi dalam satuan Hours
49. Aktor Borrow menyelesaikan Handover baris `Proyektor Epson Pro {runId}`
50. Aktor Admin memindahkan Category aset `Proyektor Epson Pro {runId}` ke `Elektronik {runId}` dan mengganti Asset Name-nya menjadi `Proyektor Epson Pro EB {runId}`
51. Aktor Borrow mengajukan Extend baris `Proyektor Epson Pro EB {runId}` sampai total `7` Days
52. Verifikasi baris `Proyektor Epson Pro EB {runId}` tetap memakai snapshot Max duration `5` sampai selesai dan Extend ditolak dengan `Max [Limit] days in total. You can extend until [Date].`, walaupun Category baru `Elektronik {runId}` bermaksimum `10`
53. Aktor Admin menambahkan Approver `Agus Salim {runId}` ke Approver Group `Head Office {runId}` dan mencabut `Rina Wijaya {runId}`
54. Verifikasi baris `Excavator Komatsu {runId}` tetap memakai snapshot approver `Rina Wijaya {runId}` dan `Agus Salim {runId}` tidak melihat pengajuan itu

### Max assets per borrower diturunkan di bawah jumlah pinjaman aktif
55. Aktor Borrow mengirim Submit untuk Borrower `Joko Widodo {runId}` dengan aset `Laptop Apple MacBook {runId}`
56. Verifikasi pengajuan diterima karena baris aktif Joko `1` ditambah baris baru `1` tidak melebihi batas Category `Laptop Kerja {runId}` `2`
57. Aktor Admin menurunkan Max assets per borrower Category `Laptop Kerja {runId}` dari `2` menjadi `1`
58. Verifikasi dua pinjaman aktif Borrower `Joko Widodo {runId}` (`Laptop Samsung Galaxy Book {runId}` dan `Laptop Apple MacBook {runId}`) tidak terpengaruh dan statusnya tidak berubah
59. Aktor Borrow mengirim Submit untuk Borrower `Joko Widodo {runId}` dengan aset `Laptop Lenovo Legion {runId}`
60. Verifikasi pengajuan baru ditolak dengan `[Name] can borrow up to [Max] assets at a time.` sampai jumlah aktif di bawah batas baru
61. Aktor Borrow menyelesaikan Return baris `Laptop Samsung Galaxy Book {runId}` milik Borrower `Joko Widodo {runId}`
62. Aktor Borrow menyelesaikan Handover baris `Laptop Apple MacBook {runId}` milik Borrower `Joko Widodo {runId}`
63. Aktor Borrow menyelesaikan Return baris `Laptop Apple MacBook {runId}` milik Borrower `Joko Widodo {runId}`
64. Aktor Borrow mengirim Submit untuk Borrower `Joko Widodo {runId}` dengan aset `Laptop Lenovo Legion {runId}`
65. Verifikasi pengajuan diterima karena jumlah aktif Joko `0` ditambah baris baru `1` tidak melebihi batas baru `1`

### Block new borrow when overdue tidak menghentikan baris yang sudah diajukan
66. Aktor Borrow menyelesaikan Handover baris `Laptop Axioo Hype {runId}` milik Borrower `Kiki Amelia {runId}`
67. Verifikasi Handover berhasil walaupun Borrower punya baris Overdue karena baris memakai snapshot
68. Aktor Borrow mengirim Submit baru untuk Borrower `Kiki Amelia {runId}` dengan aset `Tablet Xiaomi Pad {runId}`
69. Verifikasi pengajuan baru ditolak dengan `[Name] has an overdue borrow: [Asset Code], due [Date]. Return it first.`

### Perubahan data Borrower dan pembacaan setting lain oleh alur
70. Aktor Borrow mengirim Submit untuk Borrower `Mira Setiawati {runId}` dengan aset `Kamera Fujifilm {runId}` dan `Tripod Manfrotto {runId}`, dan aset `Lensa Sigma {runId}` dari Group asal `Gudang Pusat {runId}`, masing-masing Duration `2` Days
71. Verifikasi baris `Kamera Fujifilm {runId}` berstatus `Waiting for Handover` tanpa approval karena Self service ON
72. Verifikasi Due date semua baris bernilai `—` dan masa pinjam tidak punya tanggal mulai karena Max advance booking tidak ada di Transaction Settings
73. Aktor Admin memindahkan Borrower `Mira Setiawati {runId}` ke Group `Branch Surabaya {runId}` dan mengubah Division-nya menjadi `Pemasaran {runId}`
74. Aktor Borrow menyelesaikan Handover baris `Kamera Fujifilm {runId}`
75. Verifikasi Handover baris `Kamera Fujifilm {runId}` berhasil tanpa menilai ulang Allowed borrower `Same Group only`, karena snapshot berlaku sampai Returned
76. Aktor Borrow mengajukan Extend baris `Kamera Fujifilm {runId}` sampai total `3` Days
77. Verifikasi Extend baris `Kamera Fujifilm {runId}` berlaku tanpa menilai ulang kelayakan Borrower
78. Aktor Borrow menyelesaikan Return baris `Kamera Fujifilm {runId}`
79. Verifikasi Return baris `Kamera Fujifilm {runId}` berhasil tanpa menilai ulang kelayakan Borrower
80. Aktor Borrow mengirim Submit baru untuk Borrower `Mira Setiawati {runId}` dengan aset `Scanner Fujitsu {runId}`
81. Verifikasi pengajuan baru ditolak dengan `[Borrower] can't borrow assets from [Group].` karena Allowed borrower dan Group baru berlaku untuk pengajuan baru
82. Aktor Borrow menyelesaikan Handover baris `Tripod Manfrotto {runId}` tanpa foto
83. Verifikasi Handover ditolak dengan `1 asset needs a handover photo.` karena Photo at start ON
84. Aktor Borrow menyelesaikan Handover baris `Tripod Manfrotto {runId}` dengan foto
85. Verifikasi Handover baris `Tripod Manfrotto {runId}` berhasil dan Due date terisi
86. Waktu berlalu sampai 1 hari sebelum Due date baris `Tripod Manfrotto {runId}`
87. Verifikasi pengingat Due date dikirim ke Borrower sesuai pilihan `D-1` pada setting efektif
88. Verifikasi Borrower tidak menerima email notifikasi baris `Tripod Manfrotto {runId}` karena Send email notifications OFF
89. Verifikasi email konfirmasi handover baris `Tripod Manfrotto {runId}` tetap dikirim

### Perubahan Transaction timeout menghitung ulang batas baris yang menunggu
90. Aktor Admin menyimpan Transaction timeout Company default menjadi `2` hari
91. Verifikasi batas waktu baris `Bor Listrik Bosch {runId}` yang menunggu sejak T0 - 3 hari jatuh sebelum waktu Save, sehingga disetel ke waktu Save ditambah 24 jam
92. Verifikasi peringatan 1 hari sebelum batas dikirim ulang karena sisa waktu ke batas baru 24 jam
93. Aktor Admin menyimpan Transaction timeout Company default menjadi `4` hari
94. Verifikasi batas waktu baris `Bor Listrik Bosch {runId}` dihitung ulang dari saat baris masuk status itu ditambah nilai baru
95. Verifikasi peringatan 1 hari sebelum batas dikirim ulang karena sisa waktu ke batas baru 24 jam atau kurang
96. Aktor Admin menyimpan Transaction timeout Company default menjadi `5` hari
97. Verifikasi batas waktu baris `Bor Listrik Bosch {runId}` dihitung ulang dari saat baris masuk status itu ditambah `5` hari
98. Verifikasi peringatan 1 hari sebelum batas tidak dikirim ulang karena sisa waktu ke batas baru lebih dari 24 jam, dibanding jumlah peringatan sebelum Save, dalam 5 detik
99. Verifikasi Draft tidak terpengaruh karena tidak memiliki timeout

### Max duration dari Company default dipakai bila tidak ada aturan yang lebih spesifik
100. Aktor Borrow mengirim Submit untuk Borrower `Ilham Maulana {runId}` dengan aset `Mesin Fotokopi Ricoh {runId}`, Duration `4` Days
101. Verifikasi baris `Mesin Fotokopi Ricoh {runId}` memakai nilai efektif Max duration `14` dari Company default karena Category `Alat Umum {runId}` tidak menetapkan Max duration
102. Verifikasi Category `Elektronik {runId}` menggantikan Company default pada baris `Laptop Asus Zenbook {runId}`: nilai efektifnya `10`, bukan `14`

### Auto-approve memakai satuan Duration unit aset
103. Aktor Borrow mengirim Submit untuk Borrower `Putri Handayani {runId}` dengan aset `Mixer Audio Behringer {runId}` Duration `3` Hours dan `Speaker Aktif JBL {runId}` Duration `6` Hours
104. Verifikasi baris `Mixer Audio Behringer {runId}` berstatus `Waiting for Handover` dan dicatat Auto-approved karena Duration `3` Hours tidak melebihi Auto-approve `sampai 4 jam`
105. Verifikasi baris `Speaker Aktif JBL {runId}` berstatus `Waiting for Approval` karena Duration `6` Hours melebihi Auto-approve `sampai 4 jam`

### Pengajuan baru atas aset yang Allow Borrow dan Allowed borrower-nya diubah ditolak
106. Aktor Admin mengubah override Asset aset `Printer Brother HL {runId}` menjadi Allow Borrow Deny
107. Aktor Admin mempersempit Allowed borrower aset `Scanner Canon DR {runId}` menjadi `Same Group only`
108. Aktor Borrow mengirim Submit baru untuk Borrower `Putri Handayani {runId}` dengan aset `Printer Brother HL {runId}`
109. Verifikasi pengajuan baru ditolak dengan `Can't be borrowed: this asset is not available for borrowing. Contact [Name] (Manage asset & TAG).` karena override Asset aset itu diubah menjadi Allow Borrow Deny sesudah awalnya Allow
110. Aktor Borrow mengirim Submit baru untuk Borrower `Putri Handayani {runId}` dengan aset `Scanner Canon DR {runId}`
111. Verifikasi pengajuan baru ditolak dengan `[Borrower] can't borrow assets from [Group].` karena Allowed borrower aset itu dipersempit menjadi `Same Group only` sesudah awalnya semua karyawan, dan Borrower berada di Group `Branch Surabaya {runId}`, bukan Group asal aset

### Pengajuan baru ditolak saat jumlah aktif di atas batas baru walaupun di bawah batas lama
112. Aktor Borrow mengirim Submit untuk Borrower `Joko Widodo {runId}` dengan aset `Laptop Asus ROG {runId}`
113. Verifikasi pengajuan baru ditolak dengan `[Name] can borrow up to [Max] assets at a time.` karena jumlah aktif Joko `1` ditambah baris baru `1` melebihi batas baru `1` walaupun tidak melebihi batas lama `2`

### Penggantian Asset Name saat baris aktif tidak mengubah snapshot
114. Aktor Borrow mengirim Submit untuk Borrower `Ilham Maulana {runId}` dengan aset `Mikrofon Shure {runId}`, Duration `3` Days
115. Aktor Borrow menyelesaikan Handover baris `Mikrofon Shure {runId}`
116. Aktor Admin mengganti Asset Name aset `Mikrofon Shure {runId}` menjadi `Mikrofon Shure SM58 {runId}`
117. Aktor Borrow mengajukan Extend baris `Mikrofon Shure SM58 {runId}` sampai total `6` Days
118. Verifikasi baris `Mikrofon Shure SM58 {runId}` tetap memakai snapshot Max duration `3` sampai selesai dan Extend ditolak dengan `Max [Limit] days in total. You can extend until [Date].`, walaupun Asset Name aset itu sudah diganti
