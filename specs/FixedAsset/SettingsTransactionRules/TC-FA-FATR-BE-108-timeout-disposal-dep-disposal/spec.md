---
id: TC-FA-FATR-BE-108-timeout-disposal-dep-disposal
title: "Transaction timeout dan versi setting pada transaksi Disposal"
layer: be-e2e
priority: Critical
caseType: Positive
status: ready-for-automation
sourceRules:
  - "§Aturan Logika Modul#r5"
  - "§Aturan Logika Modul#r31"
  - "§Aturan Logika Modul#r40"
  - "§4.1#r213"
  - "§4.1#r214"
  - "§9.2#b128"
  - "§9.2#b140"
  - "§9.2#b201"
  - "§9.2#b203"
  - "§9.2#b205"
  - "§9.2#b206"
  - "§9.2#b207"
  - "§9.2#b208"
  - "§9.2#b213"
  - "§9.2#b216"
  - "§9.2#b217"
  - "§9.2#b218"
  - "§9.2#b219"
  - "§9.2#b221"
  - "§9.2#b225"
  - "§9.2#b267"
  - "§9.2#b268"
  - "§9.2#b269"
  - "§9.2#b270"
  - "§9.2#b271"
  - "§9.2#b272"
  - "§9.2#b273"
  - "§9.2#b285"
  - "§9.2#b286"
  - "§9.2#b291"
  - "§9.2#b293"
  - "§9.2#b300"
  - "§9.2#b383"
  - "§9.2#b395"
  - "§9.2#b396"
  - "§9.2#b436"
  - "§9.2#b438"
  - "§9.4.2#r46"
  - "§9.4.2#r135"
  - "§9.4.2#r137"
  - "§9.4.2#r147"
  - "§9.4.2#r150"
  - "§9.4.2#r151"
  - "§9.4.3#b10"
  - "§9.4.4#r37"
  - "§9.6#r5"
  - "§9.7#r2"
  - "§9.7#r11"
  - "§9.7#r22"
  - "§9.7#r31"
  - "§9.7#r34"
  - "§9.10.1#b8"
  - "§11#r24"
  - "§9.4.3#b9"
  - "§9.10.1#r11"
  - "§9.2#b382"
  - "§9.2#b445"
  - "§Aturan Logika Modul#r76"
  - "§9.8#r6"
  - "§9.8#r7"
  - "§9.4.4#r54"
  - "§9.10.1#r12"
  - "§Aturan Logika Modul#r83"
  - "§9.4.2#r37"
smoke: []
dependsOn:
  - "Disposal: pengajuan, approval, dan Execute"
owner: BE
trace:
  "§Aturan Logika Modul#r5": [45, 48, 49, 51]
  "§Aturan Logika Modul#r31": [63, 64, 69]
  "§Aturan Logika Modul#r40": 48
  "§4.1#r213": [12, 26]
  "§4.1#r214": [41, 42]
  "§9.2#b128": 54
  "§9.2#b140": [48, 49]
  "§9.2#b201": 34
  "§9.2#b203": 12
  "§9.2#b205": [63, 69]
  "§9.2#b206": [63, 69, 70]
  "§9.2#b207": [64, 68]
  "§9.2#b208": 65
  "§9.2#b213": 9
  "§9.2#b216": [26, 37]
  "§9.2#b217": 41
  "§9.2#b218": [9, 33]
  "§9.2#b219": 33
  "§9.2#b221": [12, 26]
  "§9.2#b225": 19
  "§9.2#b267": [41, 42]
  "§9.2#b268": [13, 26]
  "§9.2#b269": 14
  "§9.2#b270": [26, 37]
  "§9.2#b271": [26, 27]
  "§9.2#b272": [4, 5]
  "§9.2#b273": 3
  "§9.2#b285": 41
  "§9.2#b286": 42
  "§9.2#b291": 43
  "§9.2#b293": 14
  "§9.2#b300": [90, 94]
  "§9.2#b383": [45, 51]
  "§9.2#b395": 9
  "§9.2#b396": 12
  "§9.2#b436": [48, 49]
  "§9.2#b438": 63
  "§9.4.2#r46": [41, 42, 43]
  "§9.4.2#r135": [48, 49]
  "§9.4.2#r137": [63, 69]
  "§9.4.2#r147": 12
  "§9.4.2#r150": 41
  "§9.4.2#r151": [13, 26, 37, 68]
  "§9.4.3#b10": 48
  "§9.4.4#r37": 15
  "§9.6#r5": 17
  "§9.7#r2": [65, 68, 69]
  "§9.7#r11": 51
  "§9.7#r22": 12
  "§9.7#r31": [14, 15]
  "§9.7#r34": [4, 5]
  "§9.10.1#b8": [79, 82]
  "§11#r24": [12, 41]
  "§9.10.1#r11": 79
  "§9.2#b382": 79
  "§9.2#b445": 79
  "§Aturan Logika Modul#r76": 79
  "§9.4.3#b9": [41, 42, 43]
  "§9.8#r6": [12, 13, 14]
  "§9.8#r7": [26, 37, 38]
  "§9.4.4#r54": [72, 80]
  "§9.10.1#r12": [76, 77, 79]
  "§Aturan Logika Modul#r83": [73, 81]
  "§9.4.2#r37": [76, 79, 80, 81]
---

# Transaction timeout dan versi setting pada transaksi Disposal

## Prerequisites
- Aktor: Spec ini memakai entitas khusus yang tidak dipakai spec lain. Pengaju Disposal `Sinta Dewi {runId}`. Aktor lain: Approver `Taufik Hidayat {runId}`, yang menyetujui Disposal, Total Control `Wawan Setiawan {runId}`, yang menyimpan perubahan setting dan memindahkan aset, dan Operator platform di luar tenant, yang mengubah status entitas aktor dan plan entitas aktor. Job Transaction timeout berjalan tanpa aktor.
- Data:
  - DU-108-1: Entitas `Entitas Timeout {runId}`, Pemakai `hanya spec ini`
  - DU-108-2: Group `Workshop Timeout {runId}`
  - DU-108-3: Group `Gudang Override {runId}`, Group override Allow Disposal `Deny`
  - DU-108-4: Category `Mesin Timeout {runId}`, Allowed disposal types `Sell, Scrap, Donate, Trade-in`, Require approval `ON`, Approval type `Any one approver`
  - DU-108-5: Category `Mesin Versi {runId}`, Allowed disposal types `Sell, Scrap`, Allowed disposal types setelah Save Changes `Scrap`, Require approval `ON`, Approval type `Any one approver`
  - DU-108-6: User `Sinta Dewi {runId}`, Role `Pengaju Disposal`, Cakupan `Workshop Timeout {runId}, Gudang Override {runId}`, Status `Aktif`
  - DU-108-7: User `Taufik Hidayat {runId}`, Role `Role Transaksi Approver Disposal`, Cakupan `Workshop Timeout {runId}`, Status `Aktif`
  - DU-108-8: User `Wawan Setiawan {runId}`, Role `Total Control`, Cakupan `seluruh entitas`, Status `Aktif`
  - DU-108-9: Asset `Mesin Cetak Q0 {runId}`, Category `Mesin Timeout {runId}`, Group `Workshop Timeout {runId}`, Tag `Ber-tag`, Condition `Active`, Batas Transaction timeout Disposal `7 hari sama dengan 168 jam`
  - DU-108-10: Asset `Mesin Cetak E1 {runId}`, Category `Mesin Timeout {runId}`, Group `Workshop Timeout {runId}`, Tag `Ber-tag`, Condition `Active`
  - DU-108-11: Asset `Mesin Cetak E2 {runId}`, Category `Mesin Timeout {runId}`, Group `Workshop Timeout {runId}`, Tag `Ber-tag`, Condition `Active`
  - DU-108-12: Disposal `Mesin Draft D1 {runId}`, Category `Mesin Timeout {runId}`, Group `Workshop Timeout {runId}`, Status `Draft`, Masuk status sejak `T0`
  - DU-108-13: Disposal `Mesin Laporan P1 {runId}`, Category `Mesin Timeout {runId}`, Group `Workshop Timeout {runId}`, Status `Reported`, Masuk status sejak `T0`
  - DU-108-14: Disposal `Mesin Eksekusi X1 {runId}`, Category `Mesin Timeout {runId}`, Group `Workshop Timeout {runId}`, Status `Executed menunggu posting`, Masuk status sejak `T0`
  - DU-108-15: Disposal `Mesin Laporan P2 {runId}`, Category `Mesin Timeout {runId}`, Group `Workshop Timeout {runId}`, Status `Waiting for Approval`, Masuk status sejak `T0`, Disposal Report asal `Proceeded`, Condition aset sebelum dilaporkan `Normal`
  - DU-108-16: Disposal `Mesin Manual M1 {runId}`, Category `Mesin Timeout {runId}`, Group `Workshop Timeout {runId}`, Status `Waiting for Approval`, Masuk status sejak `T0`, Source `Manual`, Condition aset sebelum Disposal `Damaged`
  - DU-108-17: Asset `Mesin Cetak Q1 {runId}`, Category `Mesin Timeout {runId}`, Group `Workshop Timeout {runId}`, Tag `Ber-tag`, Condition `Active`, Transaction timeout setelah Save Changes `3`
  - DU-108-18: Asset `Mesin Cetak Q2 {runId}`, Category `Mesin Timeout {runId}`, Group `Workshop Timeout {runId}`, Tag `Ber-tag`, Condition `Active`
  - DU-108-19: Asset `Mesin Cetak Q3 {runId}`, Category `Mesin Timeout {runId}`, Group `Workshop Timeout {runId}`, Tag `Ber-tag`, Condition `Active`
  - DU-108-20: Asset `Mesin Siklus R1 {runId}`, Category `Mesin Timeout {runId}`, Group `Workshop Timeout {runId}`, Tag `Ber-tag`, Condition `Active`
  - DU-108-21: Asset `Mesin Versi V1 {runId}`, Category `Mesin Versi {runId}`, Group `Workshop Timeout {runId}`, Tag `Ber-tag`, Condition `Active`, Nilai jual yang diajukan `5.000.000`
  - DU-108-22: Asset `Mesin Versi V2 {runId}`, Category `Mesin Versi {runId}`, Group `Workshop Timeout {runId}`, Tag `Ber-tag`, Condition `Active`
  - DU-108-23: Asset `Mesin Pindah G1 {runId}`, Category `Mesin Timeout {runId}`, Group `Workshop Timeout {runId}`, Tag `Ber-tag`, Condition `Active`, Group sesudah dipindahkan `Gudang Override {runId}`
  - DU-108-24: Asset `Mesin Plan P1 {runId}`, Category `Mesin Timeout {runId}`, Group `Workshop Timeout {runId}`, Tag `Ber-tag`, Condition `Active`, Reason `Aset rusak berat`
  - DU-108-25: Asset `Mesin Suspend S1 {runId}`, Category `Mesin Timeout {runId}`, Group `Workshop Timeout {runId}`, Tag `Ber-tag`, Condition `Active`
  - DU-108-26: Asset `Mesin Kedaluwarsa S2 {runId}`, Category `Mesin Timeout {runId}`, Group `Workshop Timeout {runId}`, Tag `Ber-tag`, Condition `Active`
  - DU-108-27: Asset `Mesin Plan P2 {runId}`, Category `Mesin Timeout {runId}`, Group `Workshop Timeout {runId}`, Tag `Ber-tag`, Condition `Active`
- Kondisi:
  - Transaction timeout Disposal bernilai `7` (days), nilai awal Company default. Approval Timeout platform bernilai `7` (days), sama dengan Transaction timeout Disposal sehingga tidak mendahuluinya.
  - Require approval Disposal pada Category uji bernilai `ON` dengan Approval type `Any one approver`, dan Approval Workflow tersedia di plan entitas aktor.
  - Level Feature Suite Disposal entitas aktor bernilai `Full`.
  - Approval Workflow tersedia di plan entitas aktor pada awal spec. Operator platform mematikannya dan menyalakannya kembali hanya pada kelompok langkah «Approval Workflow tidak tersedia di plan: approval dilewati, Reason wajib, penugasan Approver tidak dipakai, dan versi setting tercatat».
  - Entitas aktor berstatus aktif pada awal spec. Status entitas diubah Operator platform hanya pada kelompok langkah «Job timeout tanpa aktor tetap berjalan saat entitas Suspended atau Expired».

## Test Steps

### Penutupan timeout mengembalikan Disposal Report ke Reported dan Condition aset ke Reported Disposal
1. Waktu berlalu sampai batas Transaction timeout `7` hari terlampaui sejak Disposal `Mesin Laporan P2 {runId}` dan `Mesin Manual M1 {runId}` masuk status `Waiting for Approval`
2. Job Transaction timeout berjalan
3. Verifikasi Disposal Report `Mesin Laporan P2 {runId}` kembali ke `Reported` sesudah Disposal asalnya ditutup
4. Verifikasi Condition aset `Mesin Laporan P2 {runId}` kembali menjadi `Reported Disposal` karena baris berasal dari Report, bukan `Normal`, dan record Damaged atau Missing aset itu tetap ada dengan Condition `Reported Disposal`
5. Verifikasi Condition aset `Mesin Manual M1 {runId}` kembali ke nilai sebelum Disposal diajukan karena Source Disposal `Manual`

### Batas Transaction timeout Waiting for Approval tepat N kali 24 jam dihitung sejak masuk status itu
6. `Sinta Dewi {runId}` mengajukan Disposal jenis `Scrap` atas aset `Mesin Cetak Q0 {runId}` dengan scan tag aset
7. Waktu berlalu 167 jam sejak Disposal `Mesin Cetak Q0 {runId}` masuk status `Waiting for Approval`
8. Job Transaction timeout berjalan
9. Verifikasi Disposal `Mesin Cetak Q0 {runId}` tetap berstatus `Waiting for Approval` karena batas Transaction timeout Disposal `7` hari, yaitu 168 jam sejak masuk status itu, belum tercapai
10. Waktu berlalu sampai 168 jam sejak Disposal `Mesin Cetak Q0 {runId}` masuk status `Waiting for Approval`
11. Job Transaction timeout berjalan
12. Verifikasi Disposal `Mesin Cetak Q0 {runId}` ditutup saat batas Transaction timeout tercapai dan berstatus `Canceled`, bukan `Expired`
13. Verifikasi baris DSP `Mesin Cetak Q0 {runId}` dicatat dengan Note `Timed out (Waiting for Approval)`
14. Verifikasi `System` yang menutup Disposal `Mesin Cetak Q0 {runId}` dan log transaksi mencatat Modified By `System`
15. Verifikasi penutupan itu tidak menambah entri System Log karena aksi sistem tanpa user aktor mengikuti Aturan Terkunci #7
16. Job Transaction timeout berjalan lagi
17. Verifikasi Disposal `Mesin Cetak Q0 {runId}` yang sudah ditutup tidak diproses lagi: statusnya tetap `Canceled` dan log transaksi tidak bertambah dibanding sebelum job berjalan lagi
18. `Sinta Dewi {runId}` mengajukan ulang Disposal jenis `Scrap` atas aset `Mesin Cetak Q0 {runId}` dengan scan tag aset
19. Verifikasi pengajuan ulang diterima dan Disposal berstatus `Waiting for Approval`

### Batas Execute Waiting for Execution dihitung per baris
20. `Sinta Dewi {runId}` mengajukan satu Disposal jenis `Scrap` berisi dua baris, aset `Mesin Cetak E1 {runId}` dan `Mesin Cetak E2 {runId}`, dengan scan tag aset
21. `Taufik Hidayat {runId}` menyetujui baris `Mesin Cetak E1 {runId}` pada Disposal itu
22. Waktu berlalu empat hari
23. `Taufik Hidayat {runId}` menyetujui baris `Mesin Cetak E2 {runId}` pada Disposal yang sama
24. Waktu berlalu sampai batas Transaction timeout `7` hari terlampaui sejak baris `Mesin Cetak E1 {runId}` masuk status `Waiting for Execution` dan belum terlampaui sejak baris `Mesin Cetak E2 {runId}` masuk status itu
25. Job Transaction timeout berjalan
26. Verifikasi baris DSP `Mesin Cetak E1 {runId}` berstatus `Canceled` dengan Note `Timed out (Waiting for Execution)` karena batas Execute terlampaui
27. Verifikasi baris DSP `Mesin Cetak E2 {runId}` tetap berstatus `Waiting for Execution` karena batas Execute dihitung per baris, walaupun baris `Mesin Cetak E1 {runId}` pada Disposal yang sama sudah `Canceled`

### Pindah status memulai hitungan batas lagi dan Approval Timeout hanya untuk status menunggu approval
28. `Sinta Dewi {runId}` mengajukan Disposal jenis `Scrap` atas `Mesin Siklus R1 {runId}` dengan scan tag aset
29. Waktu berlalu enam hari sejak Disposal `Mesin Siklus R1 {runId}` masuk status `Waiting for Approval`
30. `Taufik Hidayat {runId}` menyetujui Disposal atas `Mesin Siklus R1 {runId}`
31. Waktu berlalu sampai batas Transaction timeout `7` hari terlampaui sejak Disposal `Mesin Siklus R1 {runId}` masuk status `Waiting for Approval` tetapi belum terlampaui sejak Disposal itu masuk status `Waiting for Execution`
32. Job Transaction timeout berjalan
33. Verifikasi Disposal `Mesin Siklus R1 {runId}` tetap berstatus `Waiting for Execution` karena pindah status memulai hitungan batas lagi
34. Verifikasi Disposal `Mesin Siklus R1 {runId}` tidak ditutup oleh Approval Timeout karena Approval Timeout hanya berlaku untuk status menunggu approval
35. Waktu berlalu sampai batas Transaction timeout `7` hari terlampaui sejak Disposal `Mesin Siklus R1 {runId}` masuk status `Waiting for Execution`
36. Job Transaction timeout berjalan
37. Verifikasi Disposal `Mesin Siklus R1 {runId}` berstatus `Canceled` dengan Note `Timed out (Waiting for Execution)`
38. Verifikasi log transaksi Disposal `Mesin Siklus R1 {runId}` mencatat penutupan itu dengan Modified By `System`

### Draft, Disposal Report, dan Disposal Executed menunggu posting tidak memiliki timeout
39. Waktu berlalu sampai batas Transaction timeout `7` hari terlampaui sejak Disposal `Mesin Draft D1 {runId}`, `Mesin Laporan P1 {runId}`, dan `Mesin Eksekusi X1 {runId}` masuk statusnya masing-masing
40. Job Transaction timeout berjalan
41. Verifikasi Draft Disposal `Mesin Draft D1 {runId}` tidak memiliki timeout, tidak pernah ditutup otomatis, dan tetap berstatus `Draft`
42. Verifikasi Disposal Report `Mesin Laporan P1 {runId}` pada tab Reported tidak memiliki timeout dan tidak pernah ditutup otomatis
43. Verifikasi Disposal `Mesin Eksekusi X1 {runId}` yang Executed menunggu posting tidak pernah ditutup otomatis

### Transaksi berjalan memakai versi setting saat diajukan dan tidak terpengaruh perubahan setting
44. `Sinta Dewi {runId}` mengajukan Disposal jenis `Sell` atas `Mesin Versi V1 {runId}` dengan scan tag aset dan Nilai jual `5.000.000`
45. Verifikasi Disposal itu mencatat versi setting yang berlaku saat diajukan, sama dengan versi setting yang tampil di sheet Info Export rules sebelum Save Changes berikutnya
46. `Wawan Setiawan {runId}` mengubah Allowed disposal types Category `Mesin Versi {runId}` di tab Disposal menjadi `Scrap`, lalu Save Changes
47. `Taufik Hidayat {runId}` menyetujui Disposal atas `Mesin Versi V1 {runId}`
48. Verifikasi Disposal jenis `Sell` atas `Mesin Versi V1 {runId}` tetap berjalan dan berstatus `Waiting for Execution` walaupun jenis `Sell` kini tidak lagi ada di Allowed disposal types, karena ia memakai aturan lama sampai selesai
49. Verifikasi versi setting yang tercatat pada Disposal `Mesin Versi V1 {runId}` tidak berubah dan tetap versi saat diajukan
50. `Sinta Dewi {runId}` mengajukan Disposal jenis `Scrap` atas `Mesin Versi V2 {runId}` dengan scan tag aset
51. Verifikasi versi setting yang tercatat pada Disposal `Mesin Versi V2 {runId}` lebih besar daripada versi pada Disposal `Mesin Versi V1 {runId}` karena transaksi baru mencatat versi setting baru

### Cakupan override dievaluasi dinamis terhadap data saat ini
52. Total Control memindahkan aset `Mesin Pindah G1 {runId}` ke Group `Gudang Override {runId}`
53. `Sinta Dewi {runId}` mengajukan Disposal jenis `Scrap` atas `Mesin Pindah G1 {runId}` dengan scan tag aset
54. Verifikasi pengajuan ditolak karena override Group `Gudang Override {runId}` bernilai Deny berlaku untuk aset yang kini berada di Group itu, walaupun aset belum ada di Group itu saat override dibuat

### Perubahan Transaction timeout menghitung ulang batas transaksi yang sedang menunggu
55. `Sinta Dewi {runId}` mengajukan Disposal jenis `Scrap` atas `Mesin Cetak Q2 {runId}` dengan scan tag aset
56. Waktu berlalu empat hari
57. `Sinta Dewi {runId}` mengajukan Disposal jenis `Scrap` atas `Mesin Cetak Q1 {runId}` dengan scan tag aset
58. Waktu berlalu satu hari
59. `Sinta Dewi {runId}` mengajukan Disposal jenis `Scrap` atas `Mesin Cetak Q3 {runId}` dengan scan tag aset
60. Waktu berlalu satu hari
61. `Wawan Setiawan {runId}` mengubah Transaction timeout Disposal menjadi `3`, lalu Save Changes
62. Job batch penghitungan ulang batas Transaction timeout berjalan
63. Verifikasi batas waktu Disposal `Mesin Cetak Q1 {runId}` dihitung ulang dari saat masuk status `Waiting for Approval` ditambah nilai baru `3` hari, bukan nilai lama `7` hari
64. Verifikasi batas waktu Disposal `Mesin Cetak Q2 {runId}` tidak jatuh sebelum waktu Save dan tidak ditutup segera, karena batas barunya jatuh sebelum waktu Save disetel ke waktu Save ditambah 24 jam
65. Verifikasi peringatan 1 hari sebelum batas dengan event `*_almost_timeout` dikirim ulang untuk Disposal `Mesin Cetak Q2 {runId}` karena sisa waktu ke batas baru 24 jam atau kurang
66. Waktu berlalu sampai 24 jam sejak Save Changes tersimpan terlampaui
67. Job Transaction timeout berjalan
68. Verifikasi Disposal `Mesin Cetak Q2 {runId}` berstatus `Canceled` dengan Note `Timed out (Waiting for Approval)` karena batas barunya, yaitu waktu Save ditambah 24 jam, terlampaui
69. Verifikasi Disposal `Mesin Cetak Q1 {runId}` berstatus `Canceled` dengan Note `Timed out (Waiting for Approval)` karena batas barunya `3` hari sejak masuk status terlampaui, walaupun batas lama `7` hari belum terlampaui
70. Verifikasi Disposal `Mesin Cetak Q3 {runId}` tetap berstatus `Waiting for Approval` karena batas barunya `3` hari sejak masuk status belum terlampaui

### Approval Workflow tidak tersedia di plan: approval dilewati, Reason wajib, penugasan Approver tidak dipakai, dan versi setting tercatat
71. `Sinta Dewi {runId}` mengajukan Disposal jenis `Scrap` atas `Mesin Plan P2 {runId}` dengan scan tag aset, tanpa Reason
72. Verifikasi Disposal `Mesin Plan P2 {runId}` berstatus `Waiting for Approval` karena nilai efektif Require approval Disposal `ON` selama Approval Workflow tersedia di plan
73. Verifikasi permintaan approval atas Disposal `Mesin Plan P2 {runId}` diterima `Taufik Hidayat {runId}` karena penugasan Role Transaksi `Approver` dipakai selama Approval Workflow tersedia di plan
74. Operator platform menonaktifkan Approval Workflow pada plan entitas aktor
75. `Sinta Dewi {runId}` mengajukan Disposal jenis `Scrap` atas `Mesin Plan P1 {runId}` dengan scan tag aset, tanpa Reason
76. Verifikasi pengajuan ditolak karena Reason wajib diisi pada Disposal yang berjalan seperti Require approval OFF saat Approval Workflow tidak tersedia di plan
77. Verifikasi aset `Mesin Plan P1 {runId}` tidak memiliki Disposal aktif baru dibanding sebelum pengajuan tanpa Reason
78. `Sinta Dewi {runId}` mengajukan ulang Disposal jenis `Scrap` atas `Mesin Plan P1 {runId}` dengan scan tag aset dan Reason `Aset rusak berat`
79. Verifikasi Disposal `Mesin Plan P1 {runId}` langsung berstatus `Waiting for Execution` tanpa langkah approval dan tanpa melewati `Waiting for Approval`, karena Approval Workflow tidak tersedia di plan sehingga nilai efektif Require approval OFF
80. Verifikasi nilai efektif Require approval Disposal atas `Mesin Plan P1 {runId}` bernilai OFF walaupun Require approval Category `Mesin Timeout {runId}` tersimpan `ON`
81. Verifikasi `Taufik Hidayat {runId}`, yang ditugaskan Role Transaksi `Approver` pada Group aset, tidak menerima permintaan approval atas Disposal `Mesin Plan P1 {runId}` karena penugasan Role Transaksi `Approver` tidak dipakai selama Approval Workflow tidak tersedia di plan
82. Verifikasi Disposal `Mesin Plan P1 {runId}` mencatat versi setting yang berlaku saat diajukan
83. Operator platform mengaktifkan kembali Approval Workflow pada plan entitas aktor

### Job timeout tanpa aktor tetap berjalan saat entitas Suspended atau Expired
84. `Sinta Dewi {runId}` mengajukan Disposal jenis `Scrap` atas `Mesin Suspend S1 {runId}` dengan scan tag aset
85. Waktu berlalu dua hari
86. `Sinta Dewi {runId}` mengajukan Disposal jenis `Scrap` atas `Mesin Kedaluwarsa S2 {runId}` dengan scan tag aset
87. Operator platform mengubah status entitas aktor menjadi `Suspended`
88. Waktu berlalu sampai batas Transaction timeout `3` hari terlampaui sejak Disposal `Mesin Suspend S1 {runId}` masuk status `Waiting for Approval` dan belum terlampaui sejak Disposal `Mesin Kedaluwarsa S2 {runId}` masuk status itu
89. Job Transaction timeout berjalan
90. Verifikasi Disposal `Mesin Suspend S1 {runId}` berstatus `Canceled` walaupun entitas aktor `Suspended`, karena job timeout tanpa aktor tetap berjalan
91. Operator platform mengubah status entitas aktor menjadi `Expired`
92. Waktu berlalu sampai batas Transaction timeout `3` hari terlampaui sejak Disposal `Mesin Kedaluwarsa S2 {runId}` masuk status `Waiting for Approval`
93. Job Transaction timeout berjalan
94. Verifikasi Disposal `Mesin Kedaluwarsa S2 {runId}` berstatus `Canceled` walaupun entitas aktor `Expired`, karena job timeout tanpa aktor tetap berjalan
