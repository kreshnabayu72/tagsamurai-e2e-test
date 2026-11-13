---
id: TC-FA-FAREG-E2E-115-damage-record-dep-damage-record
title: "Aset Active ber-Condition Damaged mendapat Damage record"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: [FAREG-LOGIC-05l, §9.4.2#r52, EB-XM-2@damaged]
smoke: []
dependsOn: ["Damage Record: Damage record"]
trace:
  FAREG-LOGIC-05l: [7, 8, 10, 18, 19, 29, 40, 42, 54, 64, 75, 79, 82]
  §9.4.2#r52: [7, 8, 10, 18, 19, 29, 64, 75, 79]
  EB-XM-2@damaged: [7, 8, 40, 42, 54]
anchor: []
coverage:
  web: automated
---

# Aset Active ber-Condition Damaged mendapat Damage record

## Prerequisites
- Aktor:
  - Rina, role Manage asset & TAG dengan Group terkelola `Gudang Rusak OFF {runId}`, serta capability Update pada node Group `Gudang Rusak ON {runId}`, `Gudang Rusak Tolak {runId}`, `Gudang Rusak Koreksi {runId}`, `Gudang Rusak Kondisi {runId}`, dan `Gudang Rusak Kembali {runId}`, serta Group terkelola `Gudang Rusak Batal {runId}`, pengaju pengajuan yang dibatalkan.
- Layar awal: Fixed Asset > Assets > Registration > Draft.
- Data:
  - DU-115-1: Group `Gudang Rusak OFF {runId}`, ada di entitas aktor.
  - DU-115-2: Group `Gudang Rusak ON {runId}`, ada di entitas aktor.
  - DU-115-3: Group `Gudang Rusak Tolak {runId}`, ada di entitas aktor.
  - DU-115-4: Asset Name `Genset Rusak {runId}` dengan TAG Type `Non-TAG`, Brand `Cummins`, Model `C150D5`.
  - DU-115-5: batch Draft `Gudang Rusak OFF {runId}` milik Rina berisi 1 aset Asset Name `Genset Rusak {runId}` dengan Condition `Damaged` dan Damage note `Panel kontrol retak {runId}`, tanpa Photo.
  - DU-115-6: pengajuan berstatus Waiting for Approval milik Siti (Manage asset & TAG) di Group `Gudang Rusak ON {runId}`, berisi 1 aset Asset Name `Genset Rusak {runId}` dengan Condition `Damaged` dan Damage note `Radiator bocor {runId}`.
  - DU-115-7: pengajuan berstatus Waiting for Approval milik Siti (Manage asset & TAG) di Group `Gudang Rusak Tolak {runId}`, berisi 1 aset Asset Name `Genset Rusak {runId}` dengan Condition `Damaged` dan Damage note `Aki soak {runId}`.
  - DU-115-8: Reason `Aset duplikat` yang diketik Rina untuk keputusan `Reject`.
  - DU-115-17: Group `Gudang Rusak Koreksi {runId}`, ada di entitas aktor.
  - DU-115-18: Group `Gudang Rusak Kondisi {runId}`, ada di entitas aktor.
  - DU-115-19: Group `Gudang Rusak Kembali {runId}`, ada di entitas aktor.
  - DU-115-20: Group `Gudang Rusak Batal {runId}`, ada di entitas aktor.
  - DU-115-21: Group `Gudang Rusak Kedaluwarsa {runId}`, ada di entitas aktor.
  - DU-115-10: pengajuan berstatus Waiting for Approval milik Siti (Manage asset & TAG) di Group `Gudang Rusak Koreksi {runId}`, berisi 1 aset Asset Name `Genset Rusak {runId}` dengan Condition `Damaged` dan Damage note `Bumper penyok {runId}`.
  - DU-115-11: pengajuan berstatus Waiting for Approval milik Siti (Manage asset & TAG) di Group `Gudang Rusak Kondisi {runId}`, berisi 1 aset Asset Name `Genset Rusak {runId}` dengan Condition `Normal`.
  - DU-115-12: pengajuan berstatus Waiting for Approval milik Siti (Manage asset & TAG) di Group `Gudang Rusak Kembali {runId}`, berisi 1 aset Asset Name `Genset Rusak {runId}` dengan Condition `Damaged` dan Damage note `Oli bocor {runId}`.
  - DU-115-13: batch Draft `Gudang Rusak Batal {runId}` milik Rina berisi 1 aset Asset Name `Genset Rusak {runId}` dengan Condition `Damaged` dan Damage note `Kaca spion retak {runId}`.
  - DU-115-14: pengajuan berstatus Waiting for Approval milik Siti (Manage asset & TAG) di Group `Gudang Rusak Kedaluwarsa {runId}`, berisi 1 aset Asset Name `Genset Rusak {runId}` dengan Condition `Damaged` dan Damage note `Kopling aus {runId}`.
  - DU-115-15: nilai koreksi approver: Damage note `Bumper penyok dan lampu pecah {runId}` untuk pengajuan `Gudang Rusak Koreksi {runId}`, serta Condition `Damaged` dengan Damage note `Lensa pecah {runId}` untuk pengajuan `Gudang Rusak Kondisi {runId}`.
  - DU-115-16: Reason `Foto aset buram` yang diketik Rina untuk keputusan `Return to Draft`.
- Kondisi:
  - approval registrasi bernilai OFF pada Group `Gudang Rusak OFF {runId}`, dan ON pada Group `Gudang Rusak ON {runId}`, `Gudang Rusak Tolak {runId}`, `Gudang Rusak Koreksi {runId}`, `Gudang Rusak Kondisi {runId}`, `Gudang Rusak Kembali {runId}`, `Gudang Rusak Batal {runId}`, dan `Gudang Rusak Kedaluwarsa {runId}`.
  - sisa kuota Group dan tenant mencukupi.

## Test Steps

### Approval OFF: Damage record dibuat saat Activate
1. Ketik Search `Gudang Rusak OFF {runId}`, tekan Enter
2. Klik row action `Edit` pada baris batch `Gudang Rusak OFF {runId}`
3. Klik `[Submit]`
4. Klik `[Activate]`
5. Buka Damage Record
6. Ketik Search `Panel kontrol retak {runId}`, tekan Enter
7. Verifikasi Damage record dengan deskripsi `Panel kontrol retak {runId}` tampil
8. Verifikasi Damage record itu ber-Source `Registration` dan berstatus `Damaged`

### Approval ON: Damage record dibuat saat Approve
9. Ganti isi kotak search dengan `Radiator bocor {runId}`, tekan Enter
10. Verifikasi tidak ada Damage record dengan deskripsi `Radiator bocor {runId}`, empty state `No results found` tampil
11. Buka Approvals > Registration > Active
12. Ketik Search `Gudang Rusak ON {runId}`, tekan Enter
13. Klik row action `Review` pada baris pengajuan `Gudang Rusak ON {runId}`
14. Klik `[Submit]`
15. Klik `[Submit]` pada dialog `Submit Approval`
16. Buka Damage Record
17. Ketik Search `Radiator bocor {runId}`, tekan Enter
18. Verifikasi Damage record dengan deskripsi `Radiator bocor {runId}` tampil
19. Verifikasi Damage record itu ber-Source `Registration` dan berstatus `Damaged`

### Reject tidak membuat Damage record
20. Buka Approvals > Registration > Active
21. Ketik Search `Gudang Rusak Tolak {runId}`, tekan Enter
22. Klik row action `Review` pada baris pengajuan `Gudang Rusak Tolak {runId}`
23. Ubah Decision aset `Genset Rusak {runId}` menjadi `Reject`
24. Isi Reason `Aset duplikat`
25. Klik `[Submit]`
26. Klik `[Submit]` pada dialog `Submit Approval`
27. Buka Damage Record
28. Ketik Search `Aki soak {runId}`, tekan Enter
29. Verifikasi tidak ada Damage record dengan deskripsi `Aki soak {runId}`, empty state `No results found` tampil

### Koreksi approver atas Damage note menjadi nilai akhir Damage record
30. Buka Approvals > Registration > Active
31. Ketik Search `Gudang Rusak Koreksi {runId}`, tekan Enter
32. Klik row action `Review` pada baris pengajuan `Gudang Rusak Koreksi {runId}`
33. Klik row option `Edit` pada baris aset `Genset Rusak {runId}`
34. Ganti Damage note menjadi `Bumper penyok dan lampu pecah {runId}`
35. Klik `[Save correction]`
36. Klik `[Submit]`
37. Klik `[Submit]` pada dialog `Submit Approval`
38. Buka Damage Record
39. Ketik Search `Bumper penyok dan lampu pecah {runId}`, tekan Enter
40. Verifikasi Damage record dengan deskripsi `Bumper penyok dan lampu pecah {runId}` tampil
41. Ganti isi kotak search dengan `Bumper penyok {runId}`, tekan Enter
42. Verifikasi tidak ada Damage record dengan deskripsi `Bumper penyok {runId}`, empty state `No results found` tampil

### Koreksi approver atas Condition menjadi nilai akhir Damage record
43. Buka Approvals > Registration > Active
44. Ketik Search `Gudang Rusak Kondisi {runId}`, tekan Enter
45. Klik row action `Review` pada baris pengajuan `Gudang Rusak Kondisi {runId}`
46. Klik row option `Edit` pada baris aset `Genset Rusak {runId}`
47. Pilih Condition `Damaged`
48. Isi Damage note `Lensa pecah {runId}`
49. Klik `[Save correction]`
50. Klik `[Submit]`
51. Klik `[Submit]` pada dialog `Submit Approval`
52. Buka Damage Record
53. Ketik Search `Lensa pecah {runId}`, tekan Enter
54. Verifikasi Damage record dengan deskripsi `Lensa pecah {runId}` tampil

### Return to Draft tidak membuat Damage record
55. Buka Approvals > Registration > Active
56. Ketik Search `Gudang Rusak Kembali {runId}`, tekan Enter
57. Klik row action `Review` pada baris pengajuan `Gudang Rusak Kembali {runId}`
58. Ubah Decision aset `Genset Rusak {runId}` menjadi `Return to Draft`
59. Isi Reason `Foto aset buram`
60. Klik `[Submit]`
61. Klik `[Submit]` pada dialog `Submit Approval`
62. Buka Damage Record
63. Ketik Search `Oli bocor {runId}`, tekan Enter
64. Verifikasi tidak ada Damage record dengan deskripsi `Oli bocor {runId}`, empty state `No results found` tampil

### Cancel oleh pengaju tidak membuat Damage record
65. Buka Fixed Asset > Assets > Registration > Draft
66. Ketik Search `Gudang Rusak Batal {runId}`, tekan Enter
67. Klik row action `Edit` pada baris batch `Gudang Rusak Batal {runId}`
68. Klik `[Submit]`
69. Klik `[Submit for Approval]`
70. Buka Fixed Asset > Assets > Registration > Waiting for Approval
71. Klik row action `Cancel registration` pada baris pengajuan `Gudang Rusak Batal {runId}`
72. Klik `[Cancel Registration]` pada dialog `Cancel Registration`
73. Buka Damage Record
74. Ketik Search `Kaca spion retak {runId}`, tekan Enter
75. Verifikasi tidak ada Damage record dengan deskripsi `Kaca spion retak {runId}`, empty state `No results found` tampil

### Auto-cancel sistem tidak membuat Damage record
76. Waktu berlalu melewati Approval Timeout platform tanpa keputusan atas pengajuan `Gudang Rusak Kedaluwarsa {runId}`, sehingga sistem membatalkannya otomatis
77. Buka Damage Record
78. Ketik Search `Kopling aus {runId}`, tekan Enter
79. Verifikasi tidak ada Damage record dengan deskripsi `Kopling aus {runId}`, empty state `No results found` tampil

### Damage record dibuat tanpa Damaged Photo
80. Buka Damage Record
81. Ketik Search `Panel kontrol retak {runId}`, tekan Enter
82. Verifikasi Damage record itu tidak memiliki Damaged Photo
