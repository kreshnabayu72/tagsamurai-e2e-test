---
id: TC-FA-ASSIGN-E2E-022-visibilitas-draft-per-cakupan
title: "Visibilitas Draft menurut cakupan Group aktor"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["§9.11#r1", "§9.11#r2", "§9.11#r3", "§9.11#r4", "§9.11#p2", "§9.11#p4", "§9.11#p5", "§9.11#p6", "§9.11#p7", "§9.11#p8"]
smoke: []
dependsOn: []
trace:
  "§9.11#r1": [25, 26, 27, 32, 41]
  "§9.11#r2": [37, 38, 40, 41]
  "§9.11#r3": [46, 47, 51]
  "§9.11#r4": [6, 7, 13, 14, 16, 17, 18, 20, 23]
  "§9.11#p2": 6
  "§9.11#p4": 13
  "§9.11#p5": [13, 16, 17]
  "§9.11#p6": [18, 20]
  "§9.11#p7": [23, 30]
  "§9.11#p8": 63
anchor: [22, 29, 50, 62]
coverage:
  web: automated
---

# Visibilitas Draft menurut cakupan Group aktor

## Prerequisites
- Aktor:
  - Aktor A: Asset Admin dengan cakupan Group `Head Office`, pembuat Draft.
  - Aktor B: Asset Admin dengan cakupan Group `Branch Surabaya`.
  - Aktor M: Monitoring & Report dengan cakupan Group `Head Office`.
  - Aktor R: Read Only dengan cakupan seluruh client.
  - Aktor P dan Aktor Q: Approver pada Group `Head Office`.
  - Aktor V: Assignee Employee `Dewi Anggraini`, memakai My Asset.
- Layar awal: Transactions > Assignment, tab Transactions.
- Data:
  - DU-022-1: Aktor A `Citra Larasati {runId}`, Asset Admin, cakupan `Head Office`.
  - DU-022-2: Aktor B `Eko Prabowo {runId}`, Asset Admin, cakupan `Branch Surabaya`.
  - DU-022-3: Aktor M `Fitri Handayani {runId}`, Monitoring & Report, cakupan `Head Office`; Aktor R `Gilang Saputra {runId}`, Read Only, seluruh client.
  - DU-022-4: Aktor P `Maya Putri {runId}` dan Aktor Q `Bayu Nugroho {runId}`, Approver pada Group `Head Office`.
  - DU-022-5: Aset `Laptop Dell Latitude 5420 {runId}` dan `Monitor LG 24 {runId}` Group `Head Office`, serta `Printer HP M404 {runId}` Group `Branch Surabaya`, semuanya `Available` dan `Normal`.
  - DU-022-6: Draft bersama Assignee `Sari Dewi`, dibuat Aktor A, berisi `Laptop Dell Latitude 5420 {runId}`, `Monitor LG 24 {runId}`, dan `Printer HP M404 {runId}`.
  - DU-022-7: Draft tanpa aset Assignee `Budi Setiawan`, dibuat Aktor A.
  - DU-022-8: ASG Assignee `Dewi Anggraini`, Group `Head Office`, berstatus Waiting for Approval, berisi `Toyota Avanza {runId}` (approver Aktor P), `Excavator PC200 {runId}` (semua approver: Aktor P dan Aktor Q, Aktor Q sudah menyetujui dengan Approval Note `Setuju untuk operasional lapangan`), dan `Projector Epson EB-X49 {runId}` (approver Aktor Q).
  - DU-022-9: ASG Assignee `Sari Dewi`, Group `Branch Surabaya`, berstatus Waiting for Handover, berisi `Scanner Epson DS-530 {runId}`.
  - DU-022-10: ASG Assignee `Dewi Anggraini`, Group `Head Office`, berstatus Assigned, berisi `Generator Honda EU70 {runId}` yang disetujui Aktor P dan Aktor Q.
  - DU-022-11: Assignee Employee `Sari Dewi`, karyawan aktif dengan akun login.
  - DU-022-12: Assignee Employee `Budi Setiawan`, karyawan aktif dengan akun login.
  - DU-022-13: Assignee Employee `Dewi Anggraini`, karyawan aktif dengan akun login.
- Kondisi:
  - Feature Suite Assignment bernilai `Full`.
  - Akun semua aktor aktif dan kredensialnya disediakan fase 2.

## Test Steps

### Pembuat melihat Draft bersama dan Draft tanpa aset
1. Masuk sebagai Aktor A
2. Klik tab `Drafts`
3. Klik `[Filter]`
4. Pilih `Citra Larasati {runId}` pada filter `Modified By`
5. Klik `[Apply]`
6. Verifikasi Draft Assignee `Sari Dewi` berisi aset Group `Head Office` dan `Branch Surabaya` tampil bagi pembuatnya
7. Verifikasi Draft tanpa aset Assignee `Budi Setiawan` tampil bagi pembuatnya

### Aktor Assignment lain melihat Draft sesuai cakupan Group
8. Masuk sebagai Aktor B
9. Klik tab `Drafts`
10. Klik `[Filter]`
11. Pilih `Citra Larasati {runId}` pada filter `Modified By`
12. Klik `[Apply]`
13. Verifikasi Draft Assignee `Sari Dewi` tampil bagi Aktor B karena cakupannya meliputi aset `Printer HP M404 {runId}`
14. Verifikasi Draft tanpa aset Assignee `Budi Setiawan` tidak tampil bagi Aktor B
15. Klik Assignee `Sari Dewi` pada baris Draft
16. Verifikasi Purpose baris `Printer HP M404 {runId}` dapat diubah oleh Aktor B
17. Verifikasi baris `Laptop Dell Latitude 5420 {runId}` dan `Monitor LG 24 {runId}` read-only dengan nama aset dan Group `Head Office`
18. Verifikasi `[Submit]` Disabled karena cakupan Aktor B tidak meliputi semua Group di Draft
19. Klik `[Cancel]` pada form (form belum diubah, tanpa dialog Unsaved Changes)
20. Verifikasi aksi `Delete` pada baris Draft `Sari Dewi` Disabled karena cakupan Aktor B tidak meliputi semua Group di Draft

### Monitoring & Report dan Read Only tidak melihat tab Drafts
21. Masuk sebagai Aktor M
22. Verifikasi tab `Transactions` tampil
23. Verifikasi tab `Drafts` tidak tampil bagi Aktor M
24. Ketik Search `{runId}`, tekan Enter
25. Verifikasi ASG Assignee `Dewi Anggraini` dengan Group `Head Office` tampil bagi Aktor M
26. Verifikasi ASG Assignee `Sari Dewi` dengan Group `Branch Surabaya` tidak tampil bagi Aktor M
27. Verifikasi `[+ Assign]` tidak tampil bagi Aktor M
28. Masuk sebagai Aktor R
29. Verifikasi tab `Transactions` tampil bagi Aktor R
30. Verifikasi tab `Drafts` tidak tampil bagi Aktor R
31. Ketik Search `{runId}`, tekan Enter
32. Verifikasi ASG Assignee `Dewi Anggraini` dan ASG Assignee `Sari Dewi` keduanya tampil bagi Aktor R

### Approver memutuskan hanya aset miliknya
33. Masuk sebagai Aktor P
34. Buka `Approvals > Assignment`
35. Ketik Search `Toyota Avanza {runId}`, tekan Enter
36. Klik Transaction ID pengajuan pada baris hasil
37. Verifikasi baris aset `Toyota Avanza {runId}` dapat diputuskan Aktor P dengan aksi `Approve` dan `Reject`
38. Verifikasi baris aset `Projector Epson EB-X49 {runId}` read-only dengan `Not your approval`
39. Klik sel Approval Rule baris `Excavator PC200 {runId}`
40. Verifikasi dialog `Approval Progress` menampilkan status dan waktu keputusan Aktor Q
41. Verifikasi Approval Note `Setuju untuk operasional lapangan` tidak tampil pada dialog `Approval Progress`

### Assignee melihat aset miliknya di My Asset tanpa nama approver
42. Masuk sebagai Aktor V
43. Buka `My Asset`
44. Klik tab `Assigned`
45. Ketik Search `Generator Honda EU70 {runId}`, tekan Enter
46. Verifikasi aksi `Report Damaged` tersedia pada baris `Generator Honda EU70 {runId}`
47. Verifikasi aksi `Report Missing` tersedia pada baris `Generator Honda EU70 {runId}`
48. Klik `⋯` pada baris `Generator Honda EU70 {runId}`
49. Klik `Assignment Log`
50. Verifikasi node `Assignment requested by [Actor]` tampil pada riwayat aset milik Assignee
51. Verifikasi nama approver `Maya Putri {runId}` dan `Bayu Nugroho {runId}` tidak tampil pada node `Approved`
52. Klik `✕` pada dialog Assignment Log

### Picker aset hanya memuat aset dalam cakupan
53. Masuk sebagai Aktor B
54. Buka `Transactions > Assignment`
55. Klik `[+ Assign]`
56. Klik pilihan `Employee`
57. Klik `[Select Assignee]`
58. Pilih baris `Sari Dewi` pada dialog Select Assignee
59. Klik `[Select]`
60. Klik `[+ Asset]`
61. Ketik Search `{runId}`, tekan Enter
62. Verifikasi baris `Printer HP M404 {runId}` tampil sebagai aset dalam cakupan Aktor B pada dialog Select Asset
63. Verifikasi baris `Laptop Dell Latitude 5420 {runId}` dan `Monitor LG 24 {runId}` tidak tampil sama sekali pada dialog Select Asset, termasuk sebagai baris disabled
64. Klik `[Cancel]` pada dialog Select Asset
65. Klik `[Cancel]` pada form (form belum diubah, tanpa dialog Unsaved Changes)
