---
id: TC-FA-BORROW-BE-073-pecah-brw-per-group
title: "Server memecah Submit menjadi satu BRW per Group asal dengan Transaction ID sendiri"
layer: be-e2e
priority: Critical
caseType: Positive
status: ready-for-automation
owner: BE
sourceRules: ["BORROW-LOGIC-05a", "BORROW-LOGIC-05b", "BORROW-LOGIC-05c", "BORROW-LOGIC-05d", "BORROW-LOGIC-05e", "BORROW-LOGIC-05f", "BORROW-LOGIC-05g", "BORROW-LOGIC-05h", "BORROW-LOGIC-05i", "BORROW-LOGIC-05j", "F-BORROW-03.k11", "F-BORROW-03.k12", "§9.2#b20", "§9.2#b21", "§10#r2"]
smoke: []
dependsOn: []
trace:
  "BORROW-LOGIC-05a": 6
  "BORROW-LOGIC-05b": 7
  "BORROW-LOGIC-05c": 11
  "BORROW-LOGIC-05d": 13
  "BORROW-LOGIC-05e": 14
  "BORROW-LOGIC-05f": [16, 18, 20]
  "BORROW-LOGIC-05g": 9
  "BORROW-LOGIC-05h": [2, 3]
  "BORROW-LOGIC-05i": 4
  "BORROW-LOGIC-05j": 12
  "F-BORROW-03.k11": [6, 7, 10]
  "F-BORROW-03.k12": [14, 16, 20]
  "§9.2#b20": 13
  "§9.2#b21": 4
  "§10#r2": [6, 8]
---

# Server memecah Submit menjadi satu BRW per Group asal dengan Transaction ID sendiri

## Prerequisites
- Aktor: Aktor Borrow (Asset Admin) yang cakupannya meliputi `Head Office {runId}` dan `Branch Surabaya {runId}`.
- Data:
  - DU-073-1: Group, Group asal pertama di form: Name `Head Office {runId}`.
  - DU-073-2: Group, Group asal kedua di form: Name `Branch Surabaya {runId}`.
  - DU-073-3: User, Borrower karyawan aktif dengan akun login: Name `Budi Santoso {runId}`, Group `Head Office {runId}`, Status `Aktif`.
  - DU-073-4: User, Borrower karyawan aktif dengan akun login: Name `Sari Wulandari {runId}`, Group `Head Office {runId}`, Status `Aktif`.
  - DU-073-5: Asset, Aset yang dipinjam: Name `Laptop Dell Latitude {runId}`, Group asal `Head Office {runId}`, Condition `Normal`, Custody `Available`, Require approval `OFF`.
  - DU-073-6: Asset, Aset yang dipinjam: Name `Projector Epson EB {runId}`, Group asal `Head Office {runId}`, Condition `Normal`, Custody `Available`, Require approval `OFF`.
  - DU-073-7: Asset, Aset yang dipinjam: Name `Camera Canon EOS {runId}`, Group asal `Head Office {runId}`, Condition `Normal`, Custody `Available`, Require approval `OFF`.
  - DU-073-8: Asset, Aset yang dipinjam: Name `Meeting Mic Set {runId}`, Group asal `Head Office {runId}`, Condition `Normal`, Custody `Available`, Require approval `OFF`.
  - DU-073-9: Asset, Aset yang dipinjam: Name `Toyota Innova {runId}`, Group asal `Branch Surabaya {runId}`, Condition `Normal`, Custody `Available`, Require approval `OFF`.
  - DU-073-10: Asset, Aset yang dipinjam: Name `Kipas Angin Cosmos {runId}`, Group asal `Head Office {runId}`, Condition `Normal`, Custody `Available`, Require approval `OFF`.
  - DU-073-11: Asset, Aset yang dipinjam: Name `Mesin Cuci Sharp {runId}`, Group asal `Branch Surabaya {runId}`, Condition `Damaged`, Custody `Available`, Require approval `OFF`.
  - DU-073-12: Draft, Draft Borrow atas nama Budi dengan kelima aset dalam satu form: Borrower `Budi Santoso {runId}`, Note `Peminjaman untuk kegiatan pelatihan`, Aset 1 `Laptop Dell Latitude {runId}`, Duration 1 `7`, Unit 1 `Days`, Purpose 1 `Training`, Aset 2 `Projector Epson EB {runId}`, Duration 2 `3`, Unit 2 `Days`, Purpose 2 `Training`, Aset 3 `Camera Canon EOS {runId}`, Duration 3 `3`, Unit 3 `Days`, Purpose 3 `Event`, Aset 4 `Meeting Mic Set {runId}`, Duration 4 `3`, Unit 4 `Hours`, Purpose 4 `Training`, Aset 5 `Toyota Innova {runId}`, Duration 5 `5`, Unit 5 `Days`, Purpose 5 `Training`.
  - DU-073-13: Draft, Draft Sari dengan satu aset layak dan satu aset Damaged dari Group berbeda: Borrower `Sari Wulandari {runId}`, Aset 1 `Kipas Angin Cosmos {runId}`, Aset 2 `Mesin Cuci Sharp {runId}`, Duration `2`, Unit `Days`, Purpose `Perawatan`.
- Kondisi:
  - Time Zone penyewa dipakai untuk jam akhir Due date baris Days.
  - Setting Due date reminders efektif untuk baris Hours mengirim pengingat 1 jam sebelum dan saat Due date.

## Test Steps

### Satu baris gagal membuat tidak ada BRW yang dibuat
1. Aktor Borrow mengirim Submit atas Draft atas nama `Sari Wulandari {runId}`
2. Verifikasi Submit ditolak dan tidak ada BRW yang dibuat untuk Group asal mana pun, termasuk Group asal `Head Office {runId}` yang seluruh barisnya layak
3. Verifikasi Custody aset `Kipas Angin Cosmos {runId}` tetap `Available`

### Submit memecah per Group asal dengan Transaction ID sendiri
4. Verifikasi Draft atas nama `Budi Santoso {runId}` memuat kelima aset dalam satu Draft, belum dipecah, dan tanpa Transaction ID
5. Aktor Borrow mengirim Submit atas Draft atas nama `Budi Santoso {runId}`
6. Verifikasi satu Submit menghasilkan dua BRW
7. Verifikasi satu BRW memuat `Laptop Dell Latitude {runId}`, `Projector Epson EB {runId}`, `Camera Canon EOS {runId}`, dan `Meeting Mic Set {runId}`, dan BRW lain hanya memuat `Toyota Innova {runId}`, karena kunci pengelompokan adalah Group asal aset
8. Verifikasi header tiap BRW menyimpan satu Group asal, yaitu `Head Office {runId}` atau `Branch Surabaya {runId}`
9. Verifikasi tiap BRW mendapat Transaction ID sendiri berformat `BRW-YYYY-NNNN` dan kedua nomor berbeda
10. Verifikasi nomor BRW `Head Office {runId}` lebih kecil daripada nomor BRW `Branch Surabaya {runId}` karena urutan BRW mengikuti urutan kelompok di form
11. Verifikasi kedua BRW menyimpan Borrower yang sama, yaitu `Budi Santoso {runId}`
12. Verifikasi tidak ada penanda pada kedua BRW yang mengikat keduanya sebagai hasil satu Submit
13. Verifikasi BRW `Head Office {runId}` tetap satu BRW walaupun barisnya punya Duration `7` dan `3` serta Purpose `Training` dan `Event` yang berbeda
14. Verifikasi BRW `Head Office {runId}` memuat baris Days dan baris Hours dalam satu BRW

### Due date, Overdue, dan pengingat dihitung per baris
15. Aktor Borrow menyelesaikan Handover baris `Laptop Dell Latitude {runId}` dan `Meeting Mic Set {runId}` dengan konfirmasi Borrower
16. Verifikasi Due date baris `Laptop Dell Latitude {runId}` adalah tanggal handover ditambah 6 hari, berakhir pukul 23:59:59 menurut Time Zone penyewa, dan Due date baris `Meeting Mic Set {runId}` adalah jam handover ditambah 3 jam
17. Waktu berlalu sampai 1 jam sebelum Due date baris `Meeting Mic Set {runId}`
18. Verifikasi pengingat Due date dikirim ke Borrower untuk baris `Meeting Mic Set {runId}`, dan tidak ada pengingat untuk baris `Laptop Dell Latitude {runId}` dalam 5 detik
19. Waktu berlalu sampai 1 jam setelah Due date baris `Meeting Mic Set {runId}`
20. Verifikasi baris `Meeting Mic Set {runId}` berstatus `Overdue` sedangkan baris `Laptop Dell Latitude {runId}` tetap `Borrowed`
