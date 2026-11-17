---
id: TC-FA-MYASSET-E2E-030-tab-borrowed-isi-dan-aksi-baris-dep-borrow
title: "Tab Borrowed pada data nyata: satu baris per aset, nilai kolom, tooltip progres approval, dan aksi per status"
layer: ui-e2e
priority: Medium
caseType: Positive
status: draft
sourceRules: ["§1.2#r13", "§1.2#r28", "§1.2#r30", "§1.2#r38", "§1.2#r60", "§1.2#r85", "§1.2#r86", "§1.2#r87", "§1.2#r88", "§1.2#r89", "§2.1#r1", "§2.1#r12", "§2.1#b3", "§4.1b#r1", "§4.1b#r2", "§4.1b#r3", "§4.1b#r4", "§4.1b#r5", "§4.1b#r6", "§4.1b#r7", "§4.1b#r10", "§4.1b#r11", "§4.1b#r12", "§4.1b#r13", "§4.1b#r14", "§4.1b#r15", "§4.1b#r16", "§4.1b#r19", "§4.1b#p5", "§4.2.1#b3", "§Dialog aksi baris (tab Borrowed dan Assigned)#r5", "§4.4#r11", "§4.8#r1", "§4.8#r10", "§4.8#r13", "§9.4.3#b7", "§10#r3", "§1.2#r23"]
smoke: ["§1.2#r23"]
dependsOn: ["Transactions > Borrow: pinjaman, approval, sesi Handover, Extension, dan Return oleh Aktor Borrow"]
trace:
  "§1.2#r13": [8, 16, 24, 28, 32]
  "§1.2#r28": [39, 43, 50, 53]
  "§1.2#r30": 51
  "§1.2#r38": 19
  "§1.2#r60": 29
  "§1.2#r85": [34, 37]
  "§1.2#r86": [34, 37]
  "§1.2#r87": [34, 37]
  "§1.2#r88": [34, 37]
  "§1.2#r89": [35, 59]
  "§2.1#r1": [2, 6]
  "§2.1#r12": [39, 43]
  "§2.1#b3": [50, 72]
  "§4.1b#r1": [9, 10]
  "§4.1b#r2": 11
  "§4.1b#r3": 12
  "§4.1b#r4": 13
  "§4.1b#r5": 14
  "§4.1b#r6": 15
  "§4.1b#r7": [16, 24, 26, 28, 32]
  "§4.1b#r10": [17, 29]
  "§4.1b#r11": [18, 25, 30]
  "§4.1b#r12": 19
  "§4.1b#r13": [8, 20]
  "§4.1b#r14": [21, 27, 47]
  "§4.1b#r15": 22
  "§4.1b#r16": [23, 31]
  "§4.1b#r19": [39, 43, 50, 57]
  "§4.1b#p5": [39, 40, 43, 44]
  "§4.2.1#b3": [65, 67, 68]
  "§Dialog aksi baris (tab Borrowed dan Assigned)#r5": [59, 63]
  "§4.4#r11": [57, 58]
  "§4.8#r1": [2, 4]
  "§4.8#r10": 71
  "§4.8#r13": [39, 43, 50]
  "§9.4.3#b7": 52
  "§10#r3": 8
  "§1.2#r23": [6, 7]
anchor: [70]
coverage:
  web: automated
---

# Tab Borrowed pada data nyata: satu baris per aset, nilai kolom, tooltip progres approval, dan aksi per status

## Prerequisites
- Aktor: Borrower `Budi Santoso {runId}`, pengguna karyawan ber-akun login tanpa role admin.
- Layar awal: halaman Fixed Asset (FAMS) dengan navbar.
- Data:
  - DU-030-1: User `Budi Santoso {runId}`, tanpa role admin, cakupan Group `Head Office`.
  - DU-030-2: User `Rina Wulandari {runId}`, role Asset Admin dengan hak Aktor Borrow, cakupan Group `Head Office`.
  - DU-030-3: User `Dewi Lestari {runId}`, role Approver, cakupan Group `Head Office`.
  - DU-030-4: User `Hendra Gunawan {runId}`, role Approver, cakupan Group `Head Office`.
  - DU-030-5: User `Agus Prasetyo {runId}`, tanpa role admin, cakupan Group `Head Office`.
  - DU-030-6: pinjaman Admin atas nama `Budi Santoso {runId}`, aset `Proyektor Epson EB-X06 {runId}`, Group `Head Office`, Status `Waiting for Handover`, Duration `3 days`. Satu transaksi dengan DU-030-7.
  - DU-030-7: pinjaman Admin atas nama `Budi Santoso {runId}`, aset `Printer Canon G3010 {runId}`, Group `Head Office`, Status `Waiting for Handover`, Duration `3 days`. Satu transaksi dengan DU-030-6.
  - DU-030-8: pinjaman Admin atas nama `Budi Santoso {runId}`, aset `Monitor Dell 24 inci {runId}`, Group `Head Office`, Status `Waiting for Approval`, Duration `3 days`, Approval type `All approvers` dengan approver `Dewi Lestari {runId}` dan `Hendra Gunawan {runId}`, `Dewi Lestari {runId}` sudah Approve.
  - DU-030-9: pinjaman Admin atas nama `Budi Santoso {runId}`, aset `Laptop Dell Latitude 5420 {runId}`, Brand `Dell`, Model/Type `Latitude 5420`, foto utama aset berkas `laptop-dell-5420.jpg`, Group `Head Office`, Status `Borrowed`, Duration `3 days`, Handed Over At `T0`.
  - DU-030-10: pinjaman Self-service atas nama `Budi Santoso {runId}`, aset `Meeting Mic Set {runId}`, tanpa foto utama, Group `Head Office`, Status `Borrowed`, Duration `4 days`, Handed Over At `T0`.
  - DU-030-11: pinjaman Admin atas nama `Budi Santoso {runId}`, aset `Kamera Canon EOS 90D {runId}`, Group `Head Office`, Status `Overdue`, Duration `2 days`, Handed Over At `T0 − 5 hari`.
  - DU-030-12: pinjaman Admin atas nama `Budi Santoso {runId}`, aset `Tripod Manfrotto {runId}`, Group `Head Office`, Status `Extension Approval`, Duration `5 days`, Handed Over At `T0 − 3 hari`, Approval type `Any one approver` dengan dua approver yang berhak, `Hendra Gunawan {runId}` dan `Dewi Lestari {runId}`, keduanya belum Approve pada pengajuan ini, pengajuan Extend sudah diteruskan Aktor Borrow `Rina Wulandari {runId}`.
  - DU-030-13: pinjaman Admin atas nama `Agus Prasetyo {runId}`, aset `Proyektor BenQ {runId}`, Group `Head Office`, Status `Borrowed`, Duration `3 days`, Handed Over At `T0`.
  - Due Date `T0 + 3 hari` untuk DU-030-9 dan `T0 − 3 hari` untuk DU-030-11 dihitung dari Handed Over At ditambah Duration. Remaining yang diharapkan: `Due in 3 days` untuk DU-030-9 dan `3 days overdue` untuk DU-030-11.
- Kondisi:
  - Date Format bernilai `dd/MM/yy`.
  - Time Format bernilai `24 jam`.
  - Tab Borrowed `Budi Santoso {runId}` hanya berisi 7 baris aset, dari DU-030-6 sampai DU-030-12.

## Test Steps

### Menu profil dan tab Borrowed memuat baris milik pengguna
1. Klik avatar di navbar untuk membuka menu profil
2. Verifikasi item `My Asset` tampil di menu profil
3. Klik `My Asset`
4. Verifikasi tab `Task`, `Borrowed`, `Assigned`, dan `History` tampil
5. Klik tab `Borrowed`
6. Verifikasi tabel Borrowed memuat 7 baris
7. Verifikasi baris `Proyektor BenQ {runId}` milik `Agus Prasetyo {runId}` tidak tampil di tabel
8. Verifikasi baris `Proyektor Epson EB-X06 {runId}` dan baris `Printer Canon G3010 {runId}` memakai Transaction ID yang sama berformat `BRW-YYYY-NNNN`

### Nilai sel baris Borrowed dari data nyata
9. Verifikasi kolom Photo baris `Laptop Dell Latitude 5420 {runId}` menampilkan foto utama aset DU-030-9
10. Verifikasi kolom Photo baris `Meeting Mic Set {runId}` menampilkan placeholder gambar standar
11. Verifikasi kolom Name baris DU-030-9 memuat Asset Name `Laptop Dell Latitude 5420 {runId}` beserta increment dari server
12. Verifikasi kolom Asset ID baris DU-030-9 menampilkan kode aset milik DU-030-9
13. Verifikasi kolom Brand baris DU-030-9 bernilai `Dell`
14. Verifikasi kolom Model/Type baris DU-030-9 bernilai `Latitude 5420`
15. Verifikasi kolom Group baris DU-030-9 bernilai `Head Office`
16. Verifikasi kolom Status baris DU-030-9 bernilai `Borrowed`
17. Verifikasi kolom Due Date baris DU-030-9 menampilkan tanggal `T0 + 3 hari` berformat `dd/MM/yy` tanpa jam
18. Verifikasi kolom Remaining baris DU-030-9 bernilai `Due in 3 days`
19. Verifikasi kolom Borrower baris DU-030-9 bernilai `Me`
20. Verifikasi kolom Transaction ID baris DU-030-9 berformat `BRW-YYYY-NNNN`
21. Verifikasi kolom Source baris DU-030-9 bernilai `Admin`
22. Verifikasi kolom Duration baris DU-030-9 bernilai `3 days`
23. Verifikasi kolom Handed Over At baris DU-030-9 menampilkan tanggal dan jam `T0` berformat `dd/MM/yy` dengan jam 24 jam
24. Verifikasi kolom Status baris `Kamera Canon EOS 90D {runId}` bernilai `Overdue`
25. Verifikasi kolom Remaining baris `Kamera Canon EOS 90D {runId}` bernilai `3 days overdue`
26. Verifikasi kolom Status baris `Tripod Manfrotto {runId}` bernilai `Extension Approval`
27. Verifikasi kolom Source baris `Meeting Mic Set {runId}` bernilai `Self-service`

### Baris sebelum handover dan sebelum approval selesai
28. Verifikasi kolom Status baris `Proyektor Epson EB-X06 {runId}` bernilai `Waiting for Handover`
29. Verifikasi kolom Due Date baris `Proyektor Epson EB-X06 {runId}` bernilai `—`
30. Verifikasi kolom Remaining baris `Proyektor Epson EB-X06 {runId}` bernilai `—`
31. Verifikasi kolom Handed Over At baris `Proyektor Epson EB-X06 {runId}` bernilai `—`
32. Verifikasi kolom Status baris `Monitor Dell 24 inci {runId}` bernilai `Waiting for Approval`

### Tooltip progres approval tanpa nama approver
33. Arahkan kursor ke badge `Waiting for Approval` pada baris `Monitor Dell 24 inci {runId}`
34. Verifikasi tooltip badge bertuliskan `Approval: 1 of 2 approved`
35. Verifikasi tooltip badge tidak memuat nama approver `Dewi Lestari {runId}` dan `Hendra Gunawan {runId}`
36. Arahkan kursor ke badge `Extension Approval` pada baris `Tripod Manfrotto {runId}`
37. Verifikasi tooltip badge bertuliskan `Approval: 0 of 1 approved`

### Aksi menu pada pinjaman yang belum diserahkan dan belum disetujui
38. Klik `⋯` pada baris `Proyektor Epson EB-X06 {runId}`
39. Verifikasi menu baris memuat `Borrow Log` dan `Cancel Borrow`
40. Verifikasi `Request Extension`, `Return`, `Report Damaged`, dan `Report Missing` tidak tampil di menu baris
41. Tekan `Esc` untuk menutup menu baris
42. Klik `⋯` pada baris `Monitor Dell 24 inci {runId}`
43. Verifikasi menu baris memuat `Borrow Log` dan `Cancel Borrow`
44. Verifikasi `Request Extension`, `Return`, `Report Damaged`, dan `Report Missing` tidak tampil di menu baris
45. Tekan `Esc` untuk menutup menu baris

### Return hanya pada pinjaman self-service dan Hand over serta Review tidak ada
46. Klik `⋯` pada baris `Meeting Mic Set {runId}`
47. Verifikasi menu baris memuat `Return`
48. Tekan `Esc` untuk menutup menu baris
49. Klik `⋯` pada baris `Laptop Dell Latitude 5420 {runId}`
50. Verifikasi menu baris memuat `Borrow Log`, `Request Extension`, `Report Damaged`, dan `Report Missing`
51. Verifikasi `Hand over` dan `Review` tidak tampil di menu baris
52. Verifikasi `Return` tidak tampil di menu baris
53. Verifikasi `Cancel Borrow` tidak tampil di menu baris
54. Tekan `Esc` untuk menutup menu baris

### Borrow Log tanpa nama approver
55. Klik `⋯` pada baris `Monitor Dell 24 inci {runId}`
56. Klik `Borrow Log`
57. Verifikasi dialog `Borrow Log` tampil
58. Verifikasi node `Approved` tampil di dialog
59. Verifikasi nama approver `Dewi Lestari {runId}` tidak tampil pada node `Approved`
60. Klik `✕` pada dialog `Borrow Log`
61. Klik `⋯` pada baris `Tripod Manfrotto {runId}`
62. Klik `Borrow Log`
63. Verifikasi node `Extension forwarded` tampil bersama nama Aktor Borrow `Rina Wulandari {runId}`
64. Klik `✕` pada dialog `Borrow Log`

### Badge tab Borrowed dan toolbar tanpa Borrow an Asset
65. Verifikasi badge tab `Borrowed` bernilai `7`
66. Ketik Search `Laptop Dell Latitude 5420 {runId}`, tekan Enter
67. Verifikasi tabel hanya memuat baris `Laptop Dell Latitude 5420 {runId}`
68. Verifikasi badge tab `Borrowed` tetap bernilai `7`
69. Klik `(←)` pada kotak Search
70. Verifikasi ikon `Search`, `Filter`, dan `Download` tampil di toolbar tab Borrowed
71. Verifikasi tombol `Borrow an Asset` tidak tampil di toolbar tab Borrowed
72. Verifikasi menu `Transactions > Borrow` dan `Transactions > Assignment` tidak tampil di sidebar
