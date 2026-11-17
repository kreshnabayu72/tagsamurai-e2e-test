---
id: TC-FA-MYASSET-E2E-052-tab-assigned-isi-dan-aksi-baris-dep-assignment
title: "Tab Assigned pada data nyata: baris per aset, nilai kolom, aksi per status, dan perpindahan ke History"
layer: ui-e2e
priority: Medium
caseType: Positive
status: draft
sourceRules: ["T-MYA-04", "§1.2#r15", "§1.2#r28", "§1.2#r74", "§1.2#r77", "§1.2#r78", "§1.2#r79", "§1.2#r82", "§1.2#r83", "§2.1#r10", "§2.1#r13", "§3#p9", "§4.8#r5", "§4.8#r14", "§9.4.2#r17", "§9.4.2#r23", "§9.7#r8", "§9.7#r10", "§1.2#r23"]
smoke: ["§1.2#r23"]
dependsOn:
  - "Transactions > Assignment: penugasan, approval, sesi Handover, Change PIC, dan Unassign oleh Aktor Assignment"
trace:
  "T-MYA-04": [3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
  "§1.2#r15": [2, 3, 4, 5]
  "§1.2#r28": [14, 15, 23, 24]
  "§1.2#r74": [3, 4, 5, 38]
  "§1.2#r77": [19, 20, 26, 32]
  "§1.2#r78": [14, 15, 16, 17, 18]
  "§1.2#r79": [23, 24, 25, 29, 30, 31]
  "§1.2#r82": [19, 26, 32]
  "§1.2#r83": [19, 20, 32]
  "§2.1#r10": [19, 20, 26, 32]
  "§2.1#r13": [14, 34]
  "§3#p9": [14, 15, 16, 23, 24, 25, 29, 30, 31]
  "§4.8#r5": [19, 20, 26, 32]
  "§4.8#r14": [14, 34]
  "§9.4.2#r17": [45, 47, 48]
  "§9.4.2#r23": [53, 55, 56, 61, 63, 64]
  "§9.7#r8": [38, 41, 64]
  "§9.7#r10": [45, 47, 48, 53, 55, 56]
  "§1.2#r23": [2, 7]
anchor: [44, 52, 60]
coverage:
  web: automated
---

# Tab Assigned pada data nyata: baris per aset, nilai kolom, aksi per status, dan perpindahan ke History

## Prerequisites
- Aktor: Assignee `Budi Santoso {runId}` (karyawan ber-akun login, role `Read Only`, cakupan Group `Head Office`). Aktor Assignment `Rina Wijaya {runId}` (role `Asset Admin`, cakupan Group `Head Office`) dan Approver `Dewi Lestari {runId}` (role `Approver`, cakupan Group `Head Office`) hanya memicu perubahan.
- Layar awal: halaman My Asset, tab Task.
- Data:
  - DU-052-1: pengguna `Budi Santoso {runId}`, Assignee Employee, role `Read Only`, cakupan Group `Head Office`, akun aktif, tanpa penugasan lain selain DU-052-8, DU-052-9, DU-052-10, dan DU-052-11.
  - DU-052-2: pengguna `Rina Wijaya {runId}`, role `Asset Admin`, cakupan Group `Head Office`, akun aktif.
  - DU-052-3: pengguna `Dewi Lestari {runId}`, role `Approver`, cakupan Group `Head Office`, akun aktif.
  - DU-052-4: aset `Laptop Dell Latitude 5420 {runId}`, Group `Head Office`, status `Assigned` kepada `Budi Santoso {runId}`, diserahkan oleh `Rina Wijaya {runId}`, ada di entitas aktor.
  - DU-052-5: aset `Printer HP LaserJet M404 {runId}`, Group `Head Office`, status `Waiting for Handover`, ada di entitas aktor.
  - DU-052-6: aset `Scanner Zebra DS2208 {runId}`, Group `Head Office`, status `Waiting for Approval`, ada di entitas aktor.
  - DU-052-7: aset `Projector Epson EB-X06 {runId}`, Group `Head Office`, belum ditugaskan, ada di entitas aktor.
  - DU-052-8: penugasan untuk `Budi Santoso {runId}` atas DU-052-4, status `Assigned`.
  - DU-052-9: penugasan untuk `Budi Santoso {runId}` atas DU-052-5, status `Waiting for Handover`.
  - DU-052-10: penugasan untuk `Budi Santoso {runId}` atas DU-052-6, status `Waiting for Approval`, menunggu keputusan `Dewi Lestari {runId}`.
- Kondisi:
  - Date Format bernilai `dd/MM/yy`.
  - Time Format bernilai `24 jam`.

## Test Steps

### Baris per aset dan nilai kolom pada tab Assigned
1. Klik tab `Assigned`
2. Verifikasi tepat tiga baris tampil pada tab `Assigned`, yaitu aset `Laptop Dell Latitude 5420 {runId}`, `Printer HP LaserJet M404 {runId}`, dan `Scanner Zebra DS2208 {runId}`
3. Verifikasi Status baris `Laptop Dell Latitude 5420 {runId}` adalah `Assigned`
4. Verifikasi Status baris `Printer HP LaserJet M404 {runId}` adalah `Waiting for Handover`
5. Verifikasi Status baris `Scanner Zebra DS2208 {runId}` adalah `Waiting for Approval`
6. Verifikasi Group baris `Laptop Dell Latitude 5420 {runId}` adalah `Head Office`
7. Verifikasi kolom `Assigned To` ketiga baris bernilai `Me`
8. Verifikasi kolom `Transaction ID` baris `Laptop Dell Latitude 5420 {runId}` mengikuti format `ASG-YYYY-NNNN`
9. Verifikasi kolom `Assigned Date` baris `Laptop Dell Latitude 5420 {runId}` tampil dalam Date Format `dd/MM/yy` dan Time Format `24 jam`
10. Verifikasi kolom `Assigned By` baris `Laptop Dell Latitude 5420 {runId}` berisi nama Aktor Assignment `Rina Wijaya {runId}` dalam format nama singkat
11. Verifikasi kolom `Assigned Date` baris `Printer HP LaserJet M404 {runId}` dan `Scanner Zebra DS2208 {runId}` bernilai `—`
12. Verifikasi kolom `Assigned By` baris `Printer HP LaserJet M404 {runId}` dan `Scanner Zebra DS2208 {runId}` bernilai `—`

### Aksi menu baris Assigned
13. Klik `⋯` pada baris `Laptop Dell Latitude 5420 {runId}`
14. Verifikasi aksi `Assignment Log` tampil pada menu baris `Laptop Dell Latitude 5420 {runId}`
15. Verifikasi aksi `Report Damaged` tampil pada menu baris `Laptop Dell Latitude 5420 {runId}`
16. Verifikasi aksi `Report Missing` tampil pada menu baris `Laptop Dell Latitude 5420 {runId}`
17. Verifikasi aksi `Cancel Damage Report` tidak tampil pada menu baris `Laptop Dell Latitude 5420 {runId}` karena belum ada laporan yang diajukan
18. Verifikasi aksi `Cancel Missing Report` tidak tampil pada menu baris `Laptop Dell Latitude 5420 {runId}` karena belum ada laporan yang diajukan
19. Verifikasi aksi `Unassign` tidak tampil pada menu baris `Laptop Dell Latitude 5420 {runId}`
20. Verifikasi aksi permintaan Unassign tidak tampil pada menu baris `Laptop Dell Latitude 5420 {runId}`
21. Tutup menu baris `Laptop Dell Latitude 5420 {runId}`
22. Klik `⋯` pada baris `Printer HP LaserJet M404 {runId}`
23. Verifikasi aksi `Assignment Log` tampil pada menu baris `Printer HP LaserJet M404 {runId}`
24. Verifikasi aksi `Report Damaged` tidak tampil pada menu baris `Printer HP LaserJet M404 {runId}`
25. Verifikasi aksi `Report Missing` tidak tampil pada menu baris `Printer HP LaserJet M404 {runId}`
26. Verifikasi aksi `Unassign` tidak tampil pada menu baris `Printer HP LaserJet M404 {runId}`
27. Tutup menu baris `Printer HP LaserJet M404 {runId}`
28. Klik `⋯` pada baris `Scanner Zebra DS2208 {runId}`
29. Verifikasi aksi `Assignment Log` tampil pada menu baris `Scanner Zebra DS2208 {runId}`
30. Verifikasi aksi `Report Damaged` tidak tampil pada menu baris `Scanner Zebra DS2208 {runId}`
31. Verifikasi aksi `Report Missing` tidak tampil pada menu baris `Scanner Zebra DS2208 {runId}`
32. Verifikasi aksi `Unassign` tidak tampil pada menu baris `Scanner Zebra DS2208 {runId}`
33. Klik `[Assignment Log]` pada menu baris `Scanner Zebra DS2208 {runId}`
34. Verifikasi dialog Assignment Log aset `Scanner Zebra DS2208 {runId}` tampil
35. Klik `✕` pada dialog Assignment Log

### Baris baru dan perubahan status lewat pengajuan dan keputusan Approval
36. Aktor Assignment `Rina Wijaya {runId}` mengajukan penugasan aset `Projector Epson EB-X06 {runId}` kepada `Budi Santoso {runId}`
37. Muat ulang halaman
38. Verifikasi baris `Projector Epson EB-X06 {runId}` tampil pada tab `Assigned` dengan Status `Waiting for Approval`
39. Approver `Dewi Lestari {runId}` menyetujui penugasan aset `Projector Epson EB-X06 {runId}` sampai seluruh approval terpenuhi
40. Muat ulang halaman
41. Verifikasi Status baris `Projector Epson EB-X06 {runId}` adalah `Waiting for Handover`

### Baris Laptop pindah ke History sesudah Unassign oleh admin
42. Aktor Assignment `Rina Wijaya {runId}` melepas penugasan aset `Laptop Dell Latitude 5420 {runId}` (Unassign)
43. Muat ulang halaman
44. Verifikasi baris `Printer HP LaserJet M404 {runId}` tetap tampil pada tab `Assigned`
45. Verifikasi baris `Laptop Dell Latitude 5420 {runId}` tidak tampil pada tab `Assigned`
46. Klik tab `History`
47. Verifikasi Type baris `Laptop Dell Latitude 5420 {runId}` adalah `Assignment`
48. Verifikasi Status baris `Laptop Dell Latitude 5420 {runId}` adalah `Unassigned`

### Baris Printer pindah ke History sesudah penugasan dibatalkan
49. Klik tab `Assigned`
50. Aktor Assignment `Rina Wijaya {runId}` membatalkan penugasan aset `Printer HP LaserJet M404 {runId}`
51. Muat ulang halaman
52. Verifikasi baris `Scanner Zebra DS2208 {runId}` tetap tampil pada tab `Assigned`
53. Verifikasi baris `Printer HP LaserJet M404 {runId}` tidak tampil pada tab `Assigned`
54. Klik tab `History`
55. Verifikasi Type baris `Printer HP LaserJet M404 {runId}` adalah `Assignment`
56. Verifikasi Status baris `Printer HP LaserJet M404 {runId}` adalah `Canceled`

### Baris Scanner pindah ke History sesudah penugasan ditolak
57. Klik tab `Assigned`
58. Approver `Dewi Lestari {runId}` menolak penugasan aset `Scanner Zebra DS2208 {runId}`
59. Muat ulang halaman
60. Verifikasi baris `Projector Epson EB-X06 {runId}` tetap tampil pada tab `Assigned`
61. Verifikasi baris `Scanner Zebra DS2208 {runId}` tidak tampil pada tab `Assigned`
62. Klik tab `History`
63. Verifikasi Type baris `Scanner Zebra DS2208 {runId}` adalah `Assignment`
64. Verifikasi Status baris `Scanner Zebra DS2208 {runId}` adalah `Rejected`
