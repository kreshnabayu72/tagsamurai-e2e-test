---
id: TC-FA-ASSIGN-E2E-042-pemisahan-peran-handover-dan-unassign
title: "Aktor yang juga Assignee atau PIC memproses Handover dan Unassign sendiri dengan scan TAG"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: [EC-ASG-75, EC-ASG-120, FI-ASG-20, FI-ASG-43, FI-ASG-55, FI-ASG-63, FI-ASG-64, FI-ASG-65, FI-ASG-66, ASSIGN-LOGIC-15a, ASSIGN-LOGIC-15b, ASSIGN-LOGIC-15c, ASSIGN-LOGIC-15g, ASSIGN-LOGIC-15i]
smoke: []
dependsOn: []
trace:
  EC-ASG-75: [47, 51, 53, 54, 55, 60, 62, 67, 68, 69, 70, 71]
  EC-ASG-120: [8, 13, 14, 15, 16, 17, 18, 24, 29, 30, 31, 33, 34, 35, 36, 41, 43]
  FI-ASG-20: [29, 30, 33, 34, 35, 36, 47, 50, 53, 54, 55]
  FI-ASG-43: [9, 10, 11, 12]
  FI-ASG-55: [14, 15, 16, 67, 68, 69]
  FI-ASG-63: 7
  FI-ASG-64: [5, 6, 10, 12, 13]
  FI-ASG-65: [14, 15, 16, 69]
  FI-ASG-66: 24
  ASSIGN-LOGIC-15a: [8, 13, 17, 18, 29, 30, 47, 50, 66, 70, 71]
  ASSIGN-LOGIC-15b: [14, 69]
  ASSIGN-LOGIC-15c: [33, 34, 35, 36, 41, 53, 54, 55, 60]
  ASSIGN-LOGIC-15g: [15, 16, 31, 32, 51, 52, 67, 68]
  ASSIGN-LOGIC-15i: [24, 43, 62]
anchor: [18]
coverage:
  web: automated
---

# Aktor yang juga Assignee atau PIC memproses Handover dan Unassign sendiri dengan scan TAG

## Prerequisites
- Aktor: Asset Admin `Hendra Kusuma` (Aktor Assignment) dengan cakupan Group `Head Office`, juga Assignee dan PIC pada ASG di bawah (sesi `Hendra Kusuma`).
- Layar awal: Transactions > Assignment, tab Transactions.
- Data:
  - DU-042-1: User `Hendra Kusuma`, Asset Admin dengan cakupan Group `Head Office`, anggota aktif Division `Procurement` dengan akun login.
  - DU-042-2: User `Rizky Aditya`, anggota aktif Division `Procurement` dengan akun login, PIC pada ASG DU-042-12 dan DU-042-14.
  - DU-042-3: User `Fajar Nugroho`, karyawan aktif dengan akun login, Assignee ASG DU-042-16.
  - DU-042-4: Division `Procurement`.
  - DU-042-5: Aset `Kalkulator Casio {runId}`, Group `Head Office`, TAG `RFID` dapat dibaca, berstatus `Waiting for Handover`.
  - DU-042-6: Aset `Mesin Hitung Uang {runId}`, Group `Head Office`, TAG `RFID` dapat dibaca, berstatus `Assigned`.
  - DU-042-7: ASG dengan Assignee `Hendra Kusuma` (Employee), Group `Head Office`, memuat DU-042-5 dan DU-042-6, dengan Approval `Not required` dan Purpose `Perlengkapan kerja pribadi {runId}`.
  - DU-042-8: Aset `Printer Epson L3250 {runId}`, Group `Head Office`, TAG `RFID` dapat dibaca, berstatus `Waiting for Handover`.
  - DU-042-9: Aset `Scanner Fujitsu {runId}`, Group `Head Office`, TAG `RFID` dapat dibaca, berstatus `Assigned`.
  - DU-042-10: ASG dengan Assignee Division `Procurement`, PIC `Hendra Kusuma`, Group `Head Office`, memuat DU-042-8 dan DU-042-9, dengan Approval `Not required` dan Purpose `Peralatan kantor pengadaan {runId}`.
  - DU-042-11: Aset `Laptop Asus Vivobook {runId}`, Group `Head Office`, tanpa TAG (`Non TAG`), berstatus `Assigned`.
  - DU-042-12: ASG dengan Assignee Division `Procurement`, PIC `Rizky Aditya`, Group `Head Office`, memuat DU-042-11, dengan Approval `Not required` dan Purpose `Laptop staf pengadaan {runId}`.
  - DU-042-13: Aset `Monitor Samsung 27 {runId}`, Group `Head Office`, tanpa TAG (`Non TAG`), berstatus `Assigned`.
  - DU-042-14: ASG dengan Assignee Division `Procurement`, PIC `Rizky Aditya`, Group `Head Office`, memuat DU-042-13, dengan Approval `Not required` dan Purpose `Monitor staf pengadaan {runId}`.
  - DU-042-15: Aset `Genset Honda 5KVA {runId}`, Group `Branch Surabaya`, tanpa TAG (`Non TAG`), berstatus `Assigned`.
  - DU-042-16: ASG dengan Assignee `Fajar Nugroho` (Employee), Group `Branch Surabaya`, memuat DU-042-15, dengan Approval `Not required` dan Purpose `Cadangan listrik gudang {runId}`.
- Kondisi:
  - Feature Suite Assignment pada level `Full`.
  - Need recipient confirmation efektif bernilai `Yes` untuk DU-042-5 dan DU-042-8.
  - Photo at start dan Photo at end bernilai `OFF`.
  - Akun `Hendra Kusuma` aktif dan kredensialnya disediakan fase 2.

## Test Steps

### Halaman Unassign memuat aset penugasan sendiri
1. Ketik Search `Mesin Hitung Uang {runId}`, tekan Enter
2. Klik Transaction ID pada baris hasil pencarian
3. Klik tombol `[Unassign]` di bawah tabel Assets
4. Buka dropdown field `Assignee`
5. Verifikasi opsi `Hendra Kusuma (Employee)` dengan jumlah `1 asset` tampil
6. Verifikasi opsi `Procurement (Division)` dengan jumlah `3 assets` tampil
7. Verifikasi opsi `Fajar Nugroho (Employee)` tidak tampil
8. Pilih opsi `Hendra Kusuma (Employee)`
9. Klik `[+ Asset]`
10. Verifikasi dialog Select Asset memuat DU-042-6
11. Centang baris `Mesin Hitung Uang {runId}`
12. Klik `[Select]`

### Aset penugasan sendiri wajib dipindai saat Aktor sebagai Assignee menerima Unassign
13. Verifikasi baris DU-042-6 tampil di daftar dengan Verification `Unverified` tanpa penanda ⚠
14. Verifikasi aksi `I Can't Scan the TAG` tidak tersedia pada baris DU-042-6
15. Pindai TAG aset DU-042-6 lewat `[Verify Asset]`
16. Verifikasi kolom Verification DU-042-6 menampilkan `Verified`
17. Klik `[Submit]`
18. Verifikasi toast `Success, 1 asset has been unassigned.` tampil
19. Verifikasi halaman Unassign ditutup setelah Unassign selesai

### Assignment Log menandai Unassign pemrosesan sendiri
20. Buka halaman Transactions > Assignment, tab Transactions
21. Ketik Search `Mesin Hitung Uang {runId}`, tekan Enter
22. Klik Transaction ID pada baris hasil pencarian
23. Klik row action `Assignment Log` pada baris aset `Mesin Hitung Uang {runId}`
24. Verifikasi node `Unassigned by` pada Assignment Log DU-042-6 tampil dengan Processing `Self-processed`
25. Verifikasi kolom Status DU-042-6 menampilkan `Unassigned`

### Aktor sebagai Assignee memulai Handover dan menyelesaikannya tanpa konfirmasi penerima
26. Buka halaman Transactions > Assignment, tab Transactions
27. Ketik Search `Kalkulator Casio {runId}`, tekan Enter
28. Klik menu ⋯ pada baris ASG DU-042-7
29. Verifikasi aksi `Hand Over` pada baris ASG DU-042-7 aktif
30. Klik `Hand Over`
31. Pindai TAG aset DU-042-5 lewat `[Verify Asset]`
32. Verifikasi kolom Verification DU-042-5 menampilkan `Verified`
33. Verifikasi tombol utama `[Complete Handover]` tampil
34. Klik `[Complete Handover]`
35. Verifikasi popup `Waiting for Confirmation` tidak tampil
36. Verifikasi opsi `Confirm on This Device` tidak tampil

### Handover pemrosesan sendiri tercatat Assigned dan Self-processed
37. Buka halaman Transactions > Assignment, tab Transactions
38. Ketik Search `Kalkulator Casio {runId}`, tekan Enter
39. Klik Transaction ID pada baris hasil pencarian
40. Verifikasi kolom Status DU-042-5 menampilkan `Assigned`
41. Verifikasi kolom Confirmation DU-042-5 menampilkan `Confirmed (self)`
42. Klik row action `Assignment Log` pada baris aset `Kalkulator Casio {runId}`
43. Verifikasi node `Handed over by` pada Assignment Log DU-042-5 tampil dengan Processing `Self-processed`

### Aktor sebagai PIC Division memulai Handover dengan scan TAG
44. Buka halaman Transactions > Assignment, tab Transactions
45. Ketik Search `Printer Epson L3250 {runId}`, tekan Enter
46. Klik menu ⋯ pada baris ASG DU-042-10
47. Verifikasi aksi `Hand Over` pada baris ASG DU-042-10 aktif
48. Verifikasi aksi `Remind Assignee` pada baris ASG DU-042-10 aktif
49. Verifikasi aksi `Change PIC` pada baris ASG DU-042-10 aktif
50. Klik `Hand Over`
51. Pindai TAG aset DU-042-8 lewat `[Verify Asset]`
52. Verifikasi kolom Verification DU-042-8 menampilkan `Verified`
53. Verifikasi tombol utama `[Complete Handover]` tampil
54. Klik `[Complete Handover]`
55. Verifikasi popup `Waiting for Confirmation` tidak tampil
56. Buka halaman Transactions > Assignment, tab Transactions
57. Ketik Search `Printer Epson L3250 {runId}`, tekan Enter
58. Klik Transaction ID pada baris hasil pencarian
59. Verifikasi kolom Status DU-042-8 menampilkan `Assigned`
60. Verifikasi kolom Confirmation DU-042-8 menampilkan `Confirmed (self)`
61. Klik row action `Assignment Log` pada baris aset `Printer Epson L3250 {runId}`
62. Verifikasi node `Handed over by` pada Assignment Log DU-042-8 tampil dengan Processing `Self-processed`

### Aktor sebagai PIC Division menerima Unassign dengan scan TAG
63. Buka halaman Transactions > Assignment, tab Transactions
64. Ketik Search `Scanner Fujitsu {runId}`, tekan Enter
65. Klik Transaction ID pada baris hasil pencarian
66. Klik row action `Unassign` pada baris aset `Scanner Fujitsu {runId}` di tabel Assets
67. Pindai TAG aset DU-042-9 lewat `[Verify Asset]`
68. Verifikasi baris DU-042-9 tampil di daftar dengan Verification `Verified` tanpa penanda ⚠
69. Verifikasi aksi `I Can't Scan the TAG` tidak tersedia pada baris DU-042-9
70. Klik `[Submit]`
71. Verifikasi toast `Success, 1 asset has been unassigned.` tampil
