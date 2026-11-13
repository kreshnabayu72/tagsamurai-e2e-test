---
id: TC-FA-FAREG-UI-033-approval-bulk-action
title: "Halaman Approval: Bulk Action per grup Accordion"
layer: ui-client
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: [FI-REG-16, FI-REG-17, FI-REG-18, V-REG-15, §4.2.4#p2, §4.2.4#b5, §4.8#r22, §9.9#r19]
smoke: []
dependsOn: []
trace:
  FI-REG-16: [3, 5, 6]
  FI-REG-17: [12, 13, 15, 17]
  FI-REG-18: [23, 24, 25, 32, 33, 34, 35, 36, 38, 39, 47, 48, 49, 58, 59, 60, 68, 75]
  V-REG-15: [61, 67, 74]
  §4.2.4#p2: [5, 8]
  §4.2.4#b5: [5, 23, 32, 33, 47, 48, 49, 58]
  §4.8#r22: [3, 5, 8, 15, 17]
  §9.9#r19: [24, 34, 35, 61, 67, 74, 80]
anchor: [2, 7, 51]
coverage:
  web: automated
---
# Halaman Approval: Bulk Action per grup Accordion

## Prerequisites
- Aktor: Dewi A (approver, role Group Manager, cakupan Group binaan + sub-group termasuk Gudang 1, bukan pengaju pengajuan).
- Layar awal: Halaman Approval pengajuan yang dibuka dari antrean Approvals tab Active.
- Komponen: Halaman Approval
- Data:
  - DU-033-1: pengajuan Registration ID `REG-20261109-00003`, Status `Waiting for Approval`, Group `Gudang 1`, Requested By `Rina W`, Total Asset `4`.
  - DU-033-2: aset Name `Laptop - 128`, Category `Computers`, Brand `Dell`, Model `Latitude 5440`, Group `Gudang 1`, TAG `Verified`, Condition `Normal`, Corrections `—`, Decision `Approve`, tanpa Reason.
  - DU-033-3: aset Name `Laptop - 129`, Category `Computers`, Brand `Dell`, Model `Latitude 5440`, Group `Gudang 1`, TAG `Skipped`, Condition `Damaged`, Corrections `1`, Decision `Approve`, tanpa Reason.
  - DU-033-4: aset Name `Laptop - 130`, Category `Computers`, Brand `Dell`, Model `Latitude 5440`, Group `Gudang 1`, TAG `Verified`, Condition `Normal`, Corrections `—`, Decision `Approve`, tanpa Reason.
  - DU-033-5: aset Name `Office Desk - 12`, Category `Furniture`, Brand `Kayu Jati`, Model `No Model`, Group `Gudang 1`, TAG `No tag`, Condition `Normal`, Corrections `—`, Decision `Approve`, tanpa Reason.
  - DU-033-6: aset Name `Laptop - 129`, Category `Computers`, Brand `Dell`, Model `Latitude 5440`, Group `Gudang 1`, TAG `Skipped`, Condition `Damaged`, Corrections `1`, Decision `Return to Draft`, Reason `Photo is missing`.
- Kondisi:
  - K1: pengajuan DU-033-1 berisi aset DU-033-2 sampai DU-033-4 dalam grup Accordion `Laptop` dan DU-033-5 dalam grup Accordion `Office Desk`, dengan Decision awal `Approve` dan tanpa Reason, dan approver berhak memutuskan.
  - K2: pengajuan DU-033-1 berisi aset DU-033-2, DU-033-6, dan DU-033-4 dalam grup Accordion `Laptop` dan DU-033-5 dalam grup Accordion `Office Desk`, dan approver berhak memutuskan.

## Test Steps

### Bulk Action tampil per grup setelah aset terpilih
1. Tampilkan Halaman Approval dengan kondisi K1
2. Verifikasi grup `Laptop` memuat baris `Laptop - 128`
3. Verifikasi pilihan Bulk Action belum tampil pada grup `Laptop` sebelum ada aset terpilih
4. Centang baris `Laptop - 128`
5. Verifikasi pilihan Bulk Action grup `Laptop` `Approve`, `Return to Draft`, dan `Reject` tampil
6. Verifikasi toolbar tidak memuat tombol terpisah untuk `Approve`, `Return to Draft`, atau `Reject`
7. Verifikasi grup `Office Desk` memuat baris `Office Desk - 12`
8. Verifikasi pilihan Bulk Action tidak tampil pada grup `Office Desk`

### Field Reason dan tombol Apply tampil setelah aksi dipilih
9. Tampilkan Halaman Approval dengan kondisi K1
10. Centang baris `Laptop - 128`
11. Pilih aksi `Approve` pada Bulk Action grup `Laptop`
12. Verifikasi field Reason Bulk Action tampil setelah aksi `Approve` dipilih
13. Verifikasi tombol `[Apply]` tampil sesudah field Reason
14. Pilih aksi `Return to Draft` pada Bulk Action grup `Laptop`
15. Verifikasi field Reason Bulk Action tampil setelah aksi `Return to Draft` dipilih
16. Pilih aksi `Reject` pada Bulk Action grup `Laptop`
17. Verifikasi field Reason Bulk Action tampil setelah aksi `Reject` dipilih

### Apply pada satu baris terpilih
18. Tampilkan Halaman Approval dengan kondisi K1
19. Centang baris `Laptop - 128`
20. Pilih aksi `Reject` pada Bulk Action grup `Laptop`
21. Isi Reason Bulk Action dengan `Duplicate entry`
22. Klik `[Apply]`
23. Verifikasi Decision pada baris `Laptop - 128` menampilkan `Reject`
24. Verifikasi Reason pada baris `Laptop - 128` menampilkan `Duplicate entry`
25. Verifikasi Decision pada baris `Laptop - 129` tetap `Approve`

### Apply pada banyak baris terpilih dan Reason dapat diedit per baris
26. Tampilkan Halaman Approval dengan kondisi K1
27. Centang baris `Laptop - 128`
28. Centang baris `Laptop - 129`
29. Pilih aksi `Return to Draft` pada Bulk Action grup `Laptop`
30. Isi Reason Bulk Action dengan `Photo is missing`
31. Klik `[Apply]`
32. Verifikasi Decision pada baris `Laptop - 128` menampilkan `Return to Draft`
33. Verifikasi Decision pada baris `Laptop - 129` menampilkan `Return to Draft`
34. Verifikasi Reason pada baris `Laptop - 128` menampilkan `Photo is missing`
35. Verifikasi Reason pada baris `Laptop - 129` menampilkan `Photo is missing`
36. Verifikasi Decision pada baris `Laptop - 130` tetap `Approve`
37. Ganti isi Reason pada baris `Laptop - 129` dengan `Photo is blurry`
38. Verifikasi Reason pada baris `Laptop - 129` menampilkan `Photo is blurry`
39. Verifikasi Reason pada baris `Laptop - 128` tetap `Photo is missing`

### Apply pada seluruh baris grup
40. Tampilkan Halaman Approval dengan kondisi K1
41. Centang baris `Laptop - 128`
42. Centang baris `Laptop - 129`
43. Centang baris `Laptop - 130`
44. Pilih aksi `Reject` pada Bulk Action grup `Laptop`
45. Isi Reason Bulk Action dengan `Duplicate entry`
46. Klik `[Apply]`
47. Verifikasi Decision pada baris `Laptop - 128` menampilkan `Reject`
48. Verifikasi Decision pada baris `Laptop - 129` menampilkan `Reject`
49. Verifikasi Decision pada baris `Laptop - 130` menampilkan `Reject`

### Apply Approve pada seleksi dengan Decision campuran
50. Tampilkan Halaman Approval dengan kondisi K2
51. Verifikasi Decision pada baris `Laptop - 129` menampilkan `Return to Draft`
52. Centang baris `Laptop - 128`
53. Centang baris `Laptop - 129`
54. Centang baris `Laptop - 130`
55. Pilih aksi `Approve` pada Bulk Action grup `Laptop`
56. Kosongkan Reason Bulk Action
57. Klik `[Apply]`
58. Verifikasi Decision pada baris `Laptop - 129` menampilkan `Approve`
59. Verifikasi Decision pada baris `Laptop - 128` menampilkan `Approve`
60. Verifikasi Decision pada baris `Laptop - 130` menampilkan `Approve`
61. Verifikasi pesan `Reason must not be empty` tidak tampil pada Reason Bulk Action

### Reason Bulk Action wajib untuk Return to Draft
62. Tampilkan Halaman Approval dengan kondisi K1
63. Centang baris `Laptop - 128`
64. Pilih aksi `Return to Draft` pada Bulk Action grup `Laptop`
65. Kosongkan Reason Bulk Action
66. Klik `[Apply]`
67. Verifikasi pesan `Reason must not be empty` tampil di bawah field Reason Bulk Action
68. Verifikasi Decision pada baris `Laptop - 128` tetap `Approve`

### Reason Bulk Action wajib untuk Reject
69. Tampilkan Halaman Approval dengan kondisi K1
70. Centang baris `Laptop - 128`
71. Pilih aksi `Reject` pada Bulk Action grup `Laptop`
72. Kosongkan Reason Bulk Action
73. Klik `[Apply]`
74. Verifikasi pesan `Reason must not be empty` tampil di bawah field Reason Bulk Action untuk aksi `Reject`
75. Verifikasi Decision pada baris `Laptop - 128` tetap `Approve` setelah `Reject` ditolak

### Batas panjang Reason Bulk Action
76. Tampilkan Halaman Approval dengan kondisi K1
77. Centang baris `Laptop - 128`
78. Pilih aksi `Return to Draft` pada Bulk Action grup `Laptop`
79. Isi Reason Bulk Action dengan `perbaiki-foto-aset-dan-lengkapi-data-fisik-sebelum-diajukan-ulang-perbaiki-foto-aset-dan-lengkapi-data-fisik-sebelum-diajukan-ulang-perbaiki-foto-aset-dan-lengkapi-data-fisik-sebelum-diajukan-ulang-perbaiki-foto-aset-dan-lengkapi-data-fisik-sebelum-diajukan-ulang-perbaiki-foto-aset-dan-lengkapi-data-fisik-sebelum-diajukan-ulang-perbaiki-foto-aset-dan-lengkapy` (361 karakter)
80. Verifikasi pesan `Max. 360 characters` tampil di bawah field Reason Bulk Action
