---
id: TC-FA-ASSIGN-BE-212-timeout-dan-penutupan-otomatis
title: "Transaction timeout, batas serah terima, dan penutupan otomatis"
layer: be-e2e
priority: Critical
caseType: Negative
status: ready-for-automation
sourceRules: ["F-ASSIGN-09.k1", "F-ASSIGN-09.k2", "EC-ASG-20", "EC-ASG-21", "EC-ASG-22", "EC-ASG-55", "EC-ASG-57", "§9.5#r14", "§9.4.3#b7", "ASSIGN-LOGIC-12a", "ASSIGN-LOGIC-12b", "ASSIGN-LOGIC-12c", "ASSIGN-LOGIC-12d", "ASSIGN-LOGIC-12e", "ASSIGN-LOGIC-12f", "ASSIGN-LOGIC-12g", "ASSIGN-LOGIC-12h", "ASSIGN-LOGIC-12i", "ASSIGN-LOGIC-12j", "ASSIGN-LOGIC-12k", "ASSIGN-LOGIC-12l", "ASSIGN-LOGIC-12m", "ASSIGN-LOGIC-12n", "ASSIGN-LOGIC-12o", "ASSIGN-LOGIC-12p", "ASSIGN-LOGIC-12q", "ASSIGN-LOGIC-12r", "ASSIGN-LOGIC-12s", "ASSIGN-LOGIC-12t", "ASSIGN-LOGIC-12u", "ASSIGN-LOGIC-12v", "ASSIGN-LOGIC-12w"]
smoke: []
dependsOn: []
owner: BE
trace:
  "F-ASSIGN-09.k1": [4, 10, 13, 18, 63, 70]
  "F-ASSIGN-09.k2": 29
  "EC-ASG-20": [2, 4, 6, 7, 8, 11]
  "EC-ASG-21": [13, 14]
  "EC-ASG-22": 29
  "EC-ASG-55": [16, 17, 18, 20]
  "EC-ASG-57": [23, 24, 26, 27, 66, 67]
  "§9.5#r14": [4, 51]
  "§9.4.3#b7": 29
  "ASSIGN-LOGIC-12a": 5
  "ASSIGN-LOGIC-12b": [4, 10, 53]
  "ASSIGN-LOGIC-12c": [4, 13, 51]
  "ASSIGN-LOGIC-12d": 23
  "ASSIGN-LOGIC-12e": [4, 49, 58]
  "ASSIGN-LOGIC-12f": 7
  "ASSIGN-LOGIC-12g": [6, 16]
  "ASSIGN-LOGIC-12h": [8, 17]
  "ASSIGN-LOGIC-12i": [6, 21]
  "ASSIGN-LOGIC-12j": 9
  "ASSIGN-LOGIC-12k": 36
  "ASSIGN-LOGIC-12l": [60, 69]
  "ASSIGN-LOGIC-12m": 62
  "ASSIGN-LOGIC-12n": [53, 55]
  "ASSIGN-LOGIC-12o": 29
  "ASSIGN-LOGIC-12p": 34
  "ASSIGN-LOGIC-12q": [4, 8, 14]
  "ASSIGN-LOGIC-12r": [39, 41]
  "ASSIGN-LOGIC-12s": 45
  "ASSIGN-LOGIC-12t": [20, 27, 66, 67]
  "ASSIGN-LOGIC-12u": 26
  "ASSIGN-LOGIC-12v": 37
  "ASSIGN-LOGIC-12w": 32
---

# Transaction timeout, batas serah terima, dan penutupan otomatis

## Prerequisites
- Aktor: Aktor Assignment sekaligus pengaju `Teguh Prakoso {runId}` (Asset Admin, cakupan Group `Head Office {runId}`); Aktor Assignment lain `Rina Wijaya {runId}` (Asset Admin, cakupan Group `Head Office {runId}`); Approver `Mira Handayani {runId}` (cakupan Group `Head Office {runId}`); Aktor Missing `Maya Sari {runId}` (pemegang hak keputusan menu Missing pada Group `Head Office {runId}`); Assignee Employee ber-akun login seperti di entri data.
- Data:
  - DU-212-1: User, Pengaju sekaligus Aktor Assignment: Nama `Teguh Prakoso {runId}`, Role `Asset Admin`, Cakupan Group `Head Office {runId}`.
  - DU-212-2: User, Aktor Assignment lain: Nama `Rina Wijaya {runId}`, Role `Asset Admin`, Cakupan Group `Head Office {runId}`.
  - DU-212-3: User, Approver Group: Nama `Mira Handayani {runId}`, Role `Approver`, Cakupan Group `Head Office {runId}`.
  - DU-212-4: Assignment, ASG dengan satu baris Waiting for Handover yang melewati Transaction timeout: Assignee `Umi Kalsum {runId}`, Tipe Assignee `Employee`, Group `Head Office {runId}`, Pengaju `Teguh Prakoso {runId}`, Baris 1 `Kamera Nikon D7500 {runId}`, Status baris `Waiting for Handover`, Purpose baris 1 `Dokumentasi acara`, Note `Untuk kegiatan kantor`.
  - DU-212-5: Assignment, ASG dengan satu baris Waiting for Approval yang melewati Transaction timeout: Assignee `Vera Anggraini {runId}`, Tipe Assignee `Employee`, Group `Head Office {runId}`, Pengaju `Teguh Prakoso {runId}`, Baris 1 `Printer Canon G3010 {runId}`, Status baris `Waiting for Approval`, Approver `Mira Handayani {runId}`, Purpose baris 1 `Cetak dokumen`, Override Asset Require approval setelah baris ditutup timeout `OFF`.
  - DU-212-6: Assignment, ASG dengan dua baris yang melewati Transaction timeout dan satu baris yang masih berjalan: Assignee `Winda Safitri {runId}`, Tipe Assignee `Employee`, Group `Head Office {runId}`, Pengaju `Teguh Prakoso {runId}`, Baris 1 `Proyektor Epson A {runId}`, Baris 2 `Proyektor Epson B {runId}`, Baris 3 `Proyektor Epson C {runId}`, Status baris `Waiting for Handover`, Purpose baris 1 `Presentasi klien`, Note `Rapat triwulan`.
  - DU-212-7: Assignment, ASG dengan baris Assigned yang sudah lebih lama dari Transaction timeout: Assignee `Xena Putri {runId}`, Tipe Assignee `Employee`, Group `Head Office {runId}`, Pengaju `Teguh Prakoso {runId}`, Baris 1 `Laptop Dell Precision {runId}`, Status baris `Assigned`.
  - DU-212-8: Assignment, ASG dengan baris Waiting for Handover yang dibatalkan sebelum handover tanpa Draft: Assignee `Yoga Pratama {runId}`, Tipe Assignee `Employee`, Group `Head Office {runId}`, Pengaju `Teguh Prakoso {runId}`, Baris 1 `Monitor Dell U2723 {runId}`, Status baris `Waiting for Handover`.
  - DU-212-9: Assignment, ASG dengan baris Waiting for Handover yang dibatalkan dengan Save as Draft to edit: Assignee `Zaki Firmansyah {runId}`, Tipe Assignee `Employee`, Group `Head Office {runId}`, Pengaju `Teguh Prakoso {runId}`, Baris 1 `Mouse Wireless Logitech {runId}`, Status baris `Waiting for Handover`, Purpose baris 1 `Cetak laporan`, Note `Laporan bulanan`.
  - DU-212-10: Assignment, ASG Division dengan baris Waiting for Handover dan No PIC: Assignee `Marketing {runId}`, Tipe Assignee `Division`, Group `Head Office {runId}`, Pengaju `Teguh Prakoso {runId}`, Baris 1 `Genset Perkins N1 {runId}`, Status baris `Waiting for Handover`, PIC `tidak ada PIC aktif`.
  - DU-212-11: Assignment, ASG dengan baris Waiting for Handover yang TAG-nya sudah dilaporkan: Assignee `Aldi Nugraha {runId}`, Tipe Assignee `Employee`, Group `Head Office {runId}`, Pengaju `Teguh Prakoso {runId}`, Baris 1 `Forklift Toyota N2 {runId}`, Status baris `Waiting for Handover`, Tag baris 1 `tag tidak terbaca, sudah dilaporkan`.
  - DU-212-12: Assignment, ASG Division yang PIC-nya diganti di tengah batas serah terima: Assignee `Keuangan {runId}`, Tipe Assignee `Division`, Group `Head Office {runId}`, Pengaju `Teguh Prakoso {runId}`, Baris 1 `Brankas Krisbow {runId}`, Status baris `Waiting for Handover`, PIC `Indah Permata {runId}`, PIC pengganti `Joko Susilo {runId}`.
  - DU-212-13: Assignment, ASG dengan baris Waiting for Approval yang disetujui di tengah Transaction timeout: Assignee `Dani Hermawan {runId}`, Tipe Assignee `Employee`, Group `Head Office {runId}`, Pengaju `Teguh Prakoso {runId}`, Baris 1 `Speaker JBL {runId}`, Status baris `Waiting for Approval`, Approver `Mira Handayani {runId}`.
  - DU-212-14: Assignment, ASG yang Assignee-nya dinonaktifkan: Assignee `Bayu Setiawan {runId}`, Tipe Assignee `Employee`, Group `Head Office {runId}`, Pengaju `Teguh Prakoso {runId}`, Baris 1 `Kursi Staff {runId}`, Status baris `Waiting for Handover`.
  - DU-212-15: Assignment, ASG yang asetnya dilaporkan hilang: Assignee `Cindy Permata {runId}`, Tipe Assignee `Employee`, Group `Head Office {runId}`, Pengaju `Teguh Prakoso {runId}`, Baris 1 `Meja Lipat {runId}`, Status baris `Waiting for Handover`.
  - DU-212-16: User, Aktor Missing: Nama `Maya Sari {runId}`, Role `pemegang hak keputusan menu Missing`, Cakupan Group `Head Office {runId}`.
  - DU-212-17: Assignment, ASG yang diserahkan sebelum Transaction timeout: Assignee `Eko Wijaya {runId}`, Tipe Assignee `Employee`, Group `Head Office {runId}`, Pengaju `Teguh Prakoso {runId}`, Baris 1 `Kulkas Sharp {runId}`, Status baris `Waiting for Handover`, Need recipient confirmation `No`, Photo at start `OFF`.
  - DU-212-18: Assignment, entitas dengan Feature Suite Assignment level `Basic` yang memuat satu baris Waiting for Handover dan satu baris Waiting for Approval: Entitas `Entitas Basic {runId}`, Assignee `Fitri Handayani {runId}`, Tipe Assignee `Employee`, Group `Head Office {runId}`, Baris 1 `Rak Besi Basic {runId}`, Status baris 1 `Waiting for Handover`, Baris 2 `Lemari Kaca Basic {runId}`, Status baris 2 `Waiting for Approval`.
  - DU-212-19: Assignment, entitas yang turun dari level `Full` ke level `None` di T-0 dan memuat satu baris Waiting for Approval dan satu baris Waiting for Handover: Entitas `Entitas Downgrade {runId}`, Assignee `Gilang Ramadhan {runId}`, Tipe Assignee `Employee`, Group `Head Office {runId}`, Baris 1 `Bufet Kayu {runId}`, Status baris 1 `Waiting for Approval`, Baris 2 `Sofa Tamu {runId}`, Status baris 2 `Waiting for Handover`.
- Kondisi:
  - Transaction timeout memakai nilai yang berlaku untuk entitas aktor dan tidak diubah spec ini; waktu berlalu ditulis relatif terhadap nilai itu.

## Test Steps

### Waiting for Handover melewati Transaction timeout kembali ke Draft baru
1. Waktu berlalu sampai satu hari sebelum baris `Kamera Nikon D7500 {runId}` pada DU-212-4 melewati Transaction timeout sejak masuk `Waiting for Handover`
2. Verifikasi Aktor Assignment `Rina Wijaya {runId}` dan pengaju `Teguh Prakoso {runId}` menerima notifikasi `assignment_almost_timeout`
3. Waktu berlalu sampai baris `Kamera Nikon D7500 {runId}` melewati Transaction timeout sejak masuk `Waiting for Handover`
4. Verifikasi baris `Kamera Nikon D7500 {runId}` berstatus `Canceled` oleh `System` dengan alasan `Not handed over`
5. Verifikasi tidak ada baris berstatus `Expired` pada ASG itu
6. Verifikasi baris yang ditutup tetap berada di ASG asal sebagai `Canceled` dan ASG itu tampil di tab History karena semua barisnya tertutup
7. Verifikasi Custody aset `Kamera Nikon D7500 {runId}` kembali `Available`
8. Verifikasi satu Draft baru tanpa nomor ASG terbentuk dengan keterangan `Restored from [Transaction ID]` yang memuat aset beserta Purpose `Dokumentasi acara` dan Note `Untuk kegiatan kantor`
9. Verifikasi pembuat Draft itu adalah pengaju `Teguh Prakoso {runId}`
10. Verifikasi Assignment Log baris itu memuat node `Canceled by [Actor]` dengan Actor `System`
11. Verifikasi Aktor Assignment dan pengaju menerima notifikasi `assignment_auto_canceled` saat baris ditutup

### Waiting for Approval melewati Transaction timeout
12. Waktu berlalu sampai baris `Printer Canon G3010 {runId}` pada DU-212-5 melewati Transaction timeout sejak masuk `Waiting for Approval` tanpa keputusan approver `Mira Handayani {runId}`
13. Verifikasi baris `Printer Canon G3010 {runId}` berstatus `Canceled` oleh `System` dengan alasan `Timed out (Waiting for Approval)`
14. Verifikasi aset `Printer Canon G3010 {runId}` kembali ke Draft baru

### Hanya sebagian baris yang timeout
15. Waktu berlalu sampai baris `Proyektor Epson A {runId}` dan `Proyektor Epson B {runId}` pada DU-212-6 melewati Transaction timeout sedangkan `Proyektor Epson C {runId}` belum
16. Verifikasi kedua baris yang timeout berstatus `Canceled` di ASG asal yang nomornya tetap bersama baris `Proyektor Epson C {runId}` yang masih berjalan
17. Verifikasi asetnya dikumpulkan ke satu Draft baru tanpa nomor `Restored from [Transaction ID]` untuk ASG asal itu
18. Verifikasi Assignment Log kedua baris memuat node `Canceled by [Actor]` dengan Actor `System` dan tautan ke Draft
19. Waktu berlalu sampai baris `Proyektor Epson C {runId}` melewati Transaction timeout
20. Verifikasi baris `Proyektor Epson C {runId}` berstatus `Canceled` dan asetnya masuk Draft baru yang terpisah dari Draft hasil timeout sebelumnya
21. Verifikasi semua baris ASG asal sudah tertutup sehingga ASG berstatus `Canceled` dan tampil di tab History

### Draft hasil timeout tidak punya timeout dan di-Submit ulang
22. Waktu berlalu sampai Transaction timeout lewat sekali lagi tanpa Draft hasil timeout baris `Proyektor Epson A {runId}` di-Submit
23. Verifikasi Draft hasil timeout itu tetap ada tanpa penutupan otomatis
24. Verifikasi Draft hasil timeout baris `Kamera Nikon D7500 {runId}` tidak memiliki nomor ASG sebelum di-Submit
25. Teguh menekan `[Submit]` pada Draft hasil timeout baris `Kamera Nikon D7500 {runId}`
26. Verifikasi ASG baru terbentuk dengan nomor ASG yang diberikan saat Submit
27. Verifikasi aturan efektif dan approver baris di ASG baru di-snapshot ulang

### Baris Assigned tidak pernah ditutup otomatis
28. Job penutupan timeout berjalan setelah baris `Laptop Dell Precision {runId}` pada DU-212-7 yang berstatus `Assigned` melewati Transaction timeout
29. Verifikasi baris `Laptop Dell Precision {runId}` tetap `Assigned` dan tidak pernah dikembalikan atau ditutup otomatis
30. Rina memverifikasi tag baris `Laptop Dell Precision {runId}`
31. Rina menekan `[Submit]` pada halaman Unassign untuk Assignee `Xena Putri {runId}`
32. Verifikasi baris `Laptop Dell Precision {runId}` berstatus `Unassigned` lewat Unassign, cara yang sah selain Report Missing yang dikonfirmasi untuk mengakhiri baris Assigned

### Cancel diperbolehkan sebelum handover
33. Rina membatalkan baris `Monitor Dell U2723 {runId}` pada DU-212-8 yang berstatus `Waiting for Handover` tanpa `Save as Draft to edit`
34. Verifikasi baris `Monitor Dell U2723 {runId}` berstatus `Canceled` tanpa Draft baru
35. Rina membatalkan baris `Mouse Wireless Logitech {runId}` pada DU-212-9 dengan `Save as Draft to edit` dicentang
36. Verifikasi baris `Mouse Wireless Logitech {runId}` berstatus `Canceled` dan satu Draft baru tanpa nomor ASG terbentuk dengan Assignee, aset, Purpose `Cetak laporan`, dan Note `Laporan bulanan` yang sama, sehingga polanya sama dengan Draft hasil timeout
37. Verifikasi Origin Draft hasil timeout adalah `Restored by system` sedangkan Origin Draft hasil Cancel dengan `Save as Draft to edit` adalah `Restored`

### Batas serah terima berjalan per baris dan tidak dimulai ulang
38. Waktu berlalu sampai baris `Genset Perkins N1 {runId}` pada DU-212-10 yang ditandai `No PIC` melewati Transaction timeout
39. Verifikasi baris `Genset Perkins N1 {runId}` berstatus `Canceled` dengan alasan `Not handed over` walau ditandai `No PIC`
40. Waktu berlalu sampai baris `Forklift Toyota N2 {runId}` pada DU-212-11 yang TAG-nya sudah dilaporkan melewati Transaction timeout
41. Verifikasi baris `Forklift Toyota N2 {runId}` berstatus `Canceled` dengan alasan `Not handed over` walau TAG dilaporkan, dan penghitungannya per baris
42. Waktu berlalu sampai setengah Transaction timeout sejak baris `Brankas Krisbow {runId}` pada DU-212-12 masuk `Waiting for Handover`
43. Rina mengganti PIC ASG DU-212-12 dari `Indah Permata {runId}` menjadi `Joko Susilo {runId}`
44. Waktu berlalu sampai Transaction timeout sejak baris `Brankas Krisbow {runId}` masuk `Waiting for Handover`
45. Verifikasi baris `Brankas Krisbow {runId}` berstatus `Canceled` pada batas semula karena Change PIC tidak memulai ulang jam

### Jam batas serah terima dimulai saat baris masuk Waiting for Handover
46. Waktu berlalu sampai setengah Transaction timeout sejak baris `Speaker JBL {runId}` pada DU-212-13 diajukan tanpa keputusan
47. Mira menyetujui baris `Speaker JBL {runId}`
48. Waktu berlalu sampai Transaction timeout sejak baris `Speaker JBL {runId}` diajukan
49. Verifikasi baris `Speaker JBL {runId}` masih `Waiting for Handover` karena jam batas serah terima dihitung sejak baris masuk status itu
50. Waktu berlalu sampai Transaction timeout sejak baris `Speaker JBL {runId}` masuk `Waiting for Handover`
51. Verifikasi baris `Speaker JBL {runId}` berstatus `Canceled` dengan alasan `Not handed over`

### Penutupan karena Assignee dinonaktifkan atau aset hilang tanpa Draft
52. Assignee `Bayu Setiawan {runId}` pada DU-212-14 dinonaktifkan
53. Verifikasi baris `Kursi Staff {runId}` berstatus `Canceled` oleh `System` dengan alasan `Assignee deactivated` dan tanpa Draft baru
54. Maya melaporkan aset `Meja Lipat {runId}` pada DU-212-15 hilang
55. Verifikasi baris `Meja Lipat {runId}` berstatus `Canceled` oleh `System` dengan alasan `Asset reported missing` dan tanpa Draft baru

### Baris yang diserahkan sebelum timeout tidak ditutup
56. Rina memverifikasi tag baris `Kulkas Sharp {runId}` pada DU-212-17 sebelum Transaction timeout
57. Rina menekan `[Complete Handover]` untuk baris `Kulkas Sharp {runId}`
58. Verifikasi baris `Kulkas Sharp {runId}` berstatus `Assigned` dan tidak ditutup oleh job timeout

### Level Basic dan None tanpa Draft
59. Waktu berlalu sampai baris `Rak Besi Basic {runId}` yang berstatus `Waiting for Handover` pada DU-212-18 dengan Feature Suite Assignment level `Basic` melewati Transaction timeout
60. Verifikasi baris `Rak Besi Basic {runId}` berstatus `Canceled` dengan alasan `Not handed over` tanpa Draft baru
61. Downgrade entitas pada DU-212-19 ke Feature Suite Assignment level `None` berlaku di T-0 saat ada baris `Bufet Kayu {runId}` yang `Waiting for Approval` dan baris `Sofa Tamu {runId}` yang `Waiting for Handover`
62. Verifikasi kedua baris berstatus `Canceled` oleh `System` dengan alasan `Assignment not available on plan` tanpa Draft baru

### Penutupan Waiting for Approval oleh System tercatat di Assignment Log
63. Verifikasi Assignment Log baris `Printer Canon G3010 {runId}` pada DU-212-5 memuat node `Canceled by [Actor]` dengan Actor `System`

### Draft hasil timeout di-Submit dengan aturan efektif yang sudah berubah
64. Teguh mengubah override Asset `Printer Canon G3010 {runId}` pada DU-212-5 menjadi Require approval `OFF` setelah baris itu ditutup oleh timeout
65. Teguh menekan `[Submit]` pada Draft hasil timeout baris `Printer Canon G3010 {runId}`
66. Verifikasi ASG baru terbentuk dengan nomor ASG baru dan baris `Printer Canon G3010 {runId}` berstatus `Waiting for Handover` dengan Approval `Not required`
67. Verifikasi aturan efektif baris di ASG baru di-snapshot ulang dengan Require approval `OFF`, bukan nilai `ON` pada ASG asal, dan tanpa approver `Mira Handayani {runId}`

### Timeout level Basic untuk Waiting for Approval dan pencatatannya di Assignment Log
68. Waktu berlalu sampai baris `Lemari Kaca Basic {runId}` pada DU-212-18 yang berstatus `Waiting for Approval` melewati Transaction timeout
69. Verifikasi baris `Lemari Kaca Basic {runId}` berstatus `Canceled` dengan alasan `Timed out (Waiting for Approval)` tanpa Draft baru
70. Verifikasi Assignment Log baris `Rak Besi Basic {runId}` dan `Lemari Kaca Basic {runId}` memuat node `Canceled by [Actor]` dengan Actor `System`
