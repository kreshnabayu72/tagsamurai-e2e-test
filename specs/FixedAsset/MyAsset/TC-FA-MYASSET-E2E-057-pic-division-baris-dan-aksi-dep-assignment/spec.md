---
id: TC-FA-MYASSET-E2E-057-pic-division-baris-dan-aksi-dep-assignment
title: "PIC Division: baris penugasan Division, penanda di Task, dan aksi atas nama Division"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["T-MYA-04", "§1.2#r16", "§1.2#r25", "§1.2#r44", "§1.2#r45", "§1.2#r46", "§1.2#r47", "§1.2#r73", "§1.2#r83", "§2.1#r1", "§2.1#r2", "§2.1#r3", "§2.1#r4", "§2.1#r5", "§2.1#r6", "§2.1#r7", "§2.1#r8", "§2.1#r9", "§2.1#r10", "§2.1#r11", "§2.1#r12", "§2.1#r13", "§3#p9", "§4.8#r1", "§4.8#r2", "§4.8#r3", "§4.8#r4", "§4.8#r5", "§4.8#r6", "§4.8#r7", "§4.8#r8", "§4.8#r9", "§4.8#r10", "§4.8#r11", "§4.8#r12", "§4.8#r13", "§4.8#r14"]
smoke: []
dependsOn:
  - "Transactions > Assignment: penugasan, approval, sesi Handover, Change PIC, dan Unassign oleh Aktor Assignment"
trace:
  "T-MYA-04": [19, 20, 21, 23]
  "§1.2#r16": [19, 20]
  "§1.2#r25": 19
  "§1.2#r44": [6, 19, 48]
  "§1.2#r45": [20, 23, 48]
  "§1.2#r46": [7, 9]
  "§1.2#r47": [16, 17, 26, 27, 28, 37, 45]
  "§1.2#r73": 6
  "§1.2#r83": [28, 29]
  "§2.1#r1": [2, 4]
  "§2.1#r2": [11, 16]
  "§2.1#r3": 53
  "§2.1#r4": [53, 59]
  "§2.1#r5": 53
  "§2.1#r6": 53
  "§2.1#r7": [26, 31, 35]
  "§2.1#r8": [27, 41, 43]
  "§2.1#r9": [37, 45]
  "§2.1#r10": [28, 29]
  "§2.1#r11": 54
  "§2.1#r12": [53, 58, 64]
  "§2.1#r13": [25, 50, 57, 63]
  "§3#p9": [19, 20, 26, 27]
  "§4.8#r1": [2, 4]
  "§4.8#r2": 53
  "§4.8#r3": 53
  "§4.8#r4": [6, 11, 13]
  "§4.8#r5": [28, 29]
  "§4.8#r6": [53, 59]
  "§4.8#r7": 53
  "§4.8#r8": [26, 35]
  "§4.8#r9": [27, 43]
  "§4.8#r10": 54
  "§4.8#r11": 53
  "§4.8#r12": [37, 45]
  "§4.8#r13": [53, 58, 64]
  "§4.8#r14": [25, 50, 57, 63]
anchor: []
coverage:
  web: automated
---

# PIC Division: baris penugasan Division, penanda di Task, dan aksi atas nama Division

## Prerequisites
- Aktor: PIC Division `Budi Santoso {runId}` (karyawan ber-akun login, role `Read Only`, cakupan Group `Head Office`, tanpa hak Aktor Missing pada Group `Head Office`, PIC Division `Finance {runId}`). Aktor Assignment `Rina Wijaya {runId}` (role `Asset Admin`, cakupan Group `Head Office`) hanya memicu sesi Handover.
- Layar awal: halaman utama FAMS dengan navbar.
- Data:
  - DU-057-1: pengguna `Budi Santoso {runId}`, role `Read Only`, cakupan Group `Head Office`, akun aktif, PIC Division `Finance {runId}` pada seluruh penugasan DU-057-8 sampai DU-057-11, tanpa pinjaman dan tanpa penugasan pribadi.
  - DU-057-2: pengguna `Rina Wijaya {runId}`, role `Asset Admin`, cakupan Group `Head Office`, akun aktif, Aktor Assignment penyerah.
  - DU-057-3: Division `Finance {runId}`, PIC `Budi Santoso {runId}`, ada di entitas aktor.
  - DU-057-4: aset `Scanner Zebra DS2208 {runId}`, Group `Head Office`, penugasan kepada Division `Finance {runId}` berstatus `Waiting for Handover`.
  - DU-057-5: aset `Laptop Dell Latitude 5420 {runId}`, Group `Head Office`, status `Assigned` kepada Division `Finance {runId}`, tanpa laporan lain.
  - DU-057-6: aset `Monitor Dell 24 inch {runId}`, Group `Head Office`, status `Assigned` kepada Division `Finance {runId}`, tanpa laporan lain.
  - DU-057-7: aset `Projector Epson EB-X06 {runId}`, Group `Head Office`, pernah ditugaskan kepada Division `Finance {runId}` lalu dilepas (Unassigned).
  - DU-057-8: penugasan Division `Finance {runId}` atas DU-057-4, status `Waiting for Handover`, Need recipient confirmation `Yes`, belum ada sesi Handover berjalan.
  - DU-057-9: penugasan Division `Finance {runId}` atas DU-057-5, status `Assigned`.
  - DU-057-10: penugasan Division `Finance {runId}` atas DU-057-6, status `Assigned`.
  - DU-057-11: penugasan Division `Finance {runId}` atas DU-057-7, status akhir `Unassigned`.
  - DU-057-12: laporan atas DU-057-5 dari `Budi Santoso {runId}` atas nama Division `Finance {runId}`, What happened `Layar laptop retak sesudah terjatuh dari meja` dan Damaged Photo `laptop-layar-retak.jpg`, dibuat oleh langkah spec ini.
  - DU-057-13: laporan atas DU-057-6 dari `Budi Santoso {runId}` atas nama Division `Finance {runId}`, status `Waiting for Confirmation`, dibuat oleh langkah spec ini.
- Kondisi:
  - Jendela konfirmasi sesi Handover DU-057-8 belum habis selama spec berjalan.

## Test Steps

### Pintu masuk My Asset dari menu profil
1. Klik avatar pada navbar untuk membuka menu profil
2. Verifikasi item `My Asset` tampil pada menu profil
3. Klik `My Asset` pada menu profil
4. Verifikasi tab `Task`, `Borrowed`, `Assigned`, dan `History` tampil pada halaman My Asset

### Task Confirm Handover atas nama Division tampil bagi PIC Division
5. Aktor Assignment `Rina Wijaya {runId}` menekan `[Request Confirmation]` pada Handover penugasan DU-057-8
6. Verifikasi tepat satu baris Task dengan badge `Confirm Handover` tampil pada tab `Task`
7. Verifikasi sel Transaction ID baris Task memuat nama Division `Finance {runId}`
8. Arahkan kursor ke penanda Division pada sel Transaction ID baris Task
9. Verifikasi tooltip `On behalf of: [Division]` tampil dengan `[Division]` diisi `Finance {runId}`

### Confirm Handover atas nama Division sampai berhasil
10. Klik `⋯` pada baris Task
11. Verifikasi aksi `Confirm Handover` tampil pada menu baris Task
12. Klik `[Confirm Handover]` pada menu baris Task
13. Verifikasi dialog `Confirm Handover` tampil
14. Centang pernyataan tanggung jawab pada dialog
15. Klik `[Confirm]` pada footer dialog
16. Verifikasi toast sukses Confirm Handover tampil
17. Verifikasi `No tasks` tampil pada tab `Task` sesudah Confirm

### Baris penugasan Division pada tab Assigned
18. Klik tab `Assigned`
19. Verifikasi tepat tiga baris tampil pada tab `Assigned`, yaitu aset `Scanner Zebra DS2208 {runId}`, `Laptop Dell Latitude 5420 {runId}`, dan `Monitor Dell 24 inch {runId}`
20. Verifikasi kolom `Assigned To` ketiga baris bernilai nama Division `Finance {runId}`
21. Verifikasi Status baris `Scanner Zebra DS2208 {runId}` adalah `Assigned`
22. Arahkan kursor ke nilai `Assigned To` baris `Laptop Dell Latitude 5420 {runId}`
23. Verifikasi tooltip `PIC: [Full Name]` tampil dengan `[Full Name]` diisi `Budi Santoso {runId}`

### Aksi atas nama Division pada baris Assigned
24. Klik `⋯` pada baris `Laptop Dell Latitude 5420 {runId}`
25. Verifikasi aksi `Assignment Log` tampil pada menu baris `Laptop Dell Latitude 5420 {runId}`
26. Verifikasi aksi `Report Damaged` tampil pada menu baris `Laptop Dell Latitude 5420 {runId}`
27. Verifikasi aksi `Report Missing` tampil pada menu baris `Laptop Dell Latitude 5420 {runId}`
28. Verifikasi aksi `Unassign` tidak tampil pada menu baris `Laptop Dell Latitude 5420 {runId}`
29. Verifikasi aksi permintaan Unassign tidak tampil pada menu baris `Laptop Dell Latitude 5420 {runId}`
30. Klik `[Report Damaged]` pada menu baris `Laptop Dell Latitude 5420 {runId}`
31. Verifikasi dialog `Report Damaged` tampil dengan aset `Laptop Dell Latitude 5420 {runId}`
32. Isi `What happened` dengan `Layar laptop retak sesudah terjatuh dari meja`
33. Unggah foto `laptop-layar-retak.jpg` pada `Damaged Photo`
34. Klik `[Report Damaged]` pada footer dialog
35. Verifikasi toast sukses tampil untuk laporan yang dikirim atas nama Division
36. Klik `⋯` pada baris `Laptop Dell Latitude 5420 {runId}`
37. Verifikasi aksi `Cancel Damage Report` tampil pada menu baris `Laptop Dell Latitude 5420 {runId}`
38. Tutup menu baris `Laptop Dell Latitude 5420 {runId}`
39. Klik `⋯` pada baris `Monitor Dell 24 inch {runId}`
40. Klik `[Report Missing]` pada menu baris `Monitor Dell 24 inch {runId}`
41. Verifikasi dialog `Report Missing` tampil dengan aset `Monitor Dell 24 inch {runId}`
42. Klik `[Report Missing]` pada footer dialog
43. Verifikasi toast `Success, your report has been sent to the asset admins.` tampil
44. Klik `⋯` pada baris `Monitor Dell 24 inch {runId}`
45. Verifikasi aksi `Cancel Missing Report` tampil pada menu baris `Monitor Dell 24 inch {runId}`
46. Tutup menu baris `Monitor Dell 24 inch {runId}`

### Riwayat penugasan Division pada tab History
47. Klik tab `History`
48. Verifikasi kolom `Holder` baris `Projector Epson EB-X06 {runId}` bernilai nama Division `Finance {runId}`
49. Klik `⋯` pada baris `Projector Epson EB-X06 {runId}`
50. Verifikasi aksi `Assignment Log` tampil pada menu baris `Projector Epson EB-X06 {runId}`
51. Tutup menu baris `Projector Epson EB-X06 {runId}`

### Elemen pinjaman tidak tersedia bagi PIC Division
52. Klik tab `Borrowed`
53. Verifikasi `You're not borrowing anything` tampil pada tab `Borrowed`
54. Verifikasi tombol `Borrow an Asset` tidak tampil pada tab `Borrowed`

### Menu baris PIC Division tidak memuat aksi pinjaman
55. Klik tab `Assigned`
56. Klik `⋯` pada baris `Laptop Dell Latitude 5420 {runId}`
57. Verifikasi aksi `Assignment Log` tampil pada menu baris `Laptop Dell Latitude 5420 {runId}`
58. Verifikasi aksi `Borrow Log` tidak tampil pada menu baris `Laptop Dell Latitude 5420 {runId}`
59. Verifikasi aksi `Cancel Borrow` tidak tampil pada menu baris `Laptop Dell Latitude 5420 {runId}`
60. Tutup menu baris `Laptop Dell Latitude 5420 {runId}`
61. Klik tab `History`
62. Klik `⋯` pada baris `Projector Epson EB-X06 {runId}`
63. Verifikasi aksi `Assignment Log` tampil pada menu baris `Projector Epson EB-X06 {runId}`
64. Verifikasi aksi `Borrow Log` tidak tampil pada menu baris `Projector Epson EB-X06 {runId}`
65. Tutup menu baris `Projector Epson EB-X06 {runId}`
