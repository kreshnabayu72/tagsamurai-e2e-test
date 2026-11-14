---
id: TC-FA-FATR-BE-108-timeout-disposal-dep-disposal
title: "Transaction timeout dan versi setting pada transaksi Disposal"
layer: be-e2e
priority: Critical
caseType: Positive
status: draft
sourceRules:
  - "§Aturan Logika Modul#r5"
  - "§Aturan Logika Modul#r28"
  - "§Aturan Logika Modul#r37"
  - "§4.1#r204"
  - "§4.1#r205"
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
  - "§9.2#b437"
  - "§9.2#b439"
  - "§9.4.2#r46"
  - "§9.4.2#r127"
  - "§9.4.2#r129"
  - "§9.4.2#r139"
  - "§9.4.2#r142"
  - "§9.4.2#r143"
  - "§9.4.3#b10"
  - "§9.4.4#r37"
  - "§9.6#r5"
  - "§9.7#r2"
  - "§9.7#r11"
  - "§9.7#r22"
  - "§9.7#r31"
  - "§9.7#r34"
  - "§9.10.1#b8"
  - "§11#r21"
smoke: []
dependsOn:
  - "Disposal: pengajuan, approval, dan Execute"
owner: BE
trace:
  "§Aturan Logika Modul#r5": [43, 46, 47, 49]
  "§Aturan Logika Modul#r28": [60, 61, 66]
  "§Aturan Logika Modul#r37": 46
  "§4.1#r204": [6, 20]
  "§4.1#r205": [34, 35]
  "§9.2#b128": 52
  "§9.2#b140": [46, 47]
  "§9.2#b201": 28
  "§9.2#b203": 6
  "§9.2#b205": [60, 66]
  "§9.2#b206": [60, 66, 67]
  "§9.2#b207": [61, 65]
  "§9.2#b208": 62
  "§9.2#b213": 3
  "§9.2#b216": [20, 31]
  "§9.2#b217": 34
  "§9.2#b218": [3, 27]
  "§9.2#b219": 27
  "§9.2#b221": [6, 20]
  "§9.2#b225": 13
  "§9.2#b267": [34, 35]
  "§9.2#b268": [7, 20]
  "§9.2#b269": 8
  "§9.2#b270": [20, 31]
  "§9.2#b271": [20, 21]
  "§9.2#b272": [40, 41]
  "§9.2#b273": 39
  "§9.2#b285": 34
  "§9.2#b286": 35
  "§9.2#b291": 36
  "§9.2#b293": 8
  "§9.2#b300": [76, 80]
  "§9.2#b383": [43, 49]
  "§9.2#b395": 3
  "§9.2#b396": 6
  "§9.2#b437": [46, 47]
  "§9.2#b439": 60
  "§9.4.2#r46": [34, 35, 36]
  "§9.4.2#r127": [46, 47]
  "§9.4.2#r129": [60, 66]
  "§9.4.2#r139": 6
  "§9.4.2#r142": 34
  "§9.4.2#r143": [7, 20, 31, 65]
  "§9.4.3#b10": 46
  "§9.4.4#r37": 9
  "§9.6#r5": 11
  "§9.7#r2": [62, 65, 66]
  "§9.7#r11": 49
  "§9.7#r22": 6
  "§9.7#r31": [8, 9]
  "§9.7#r34": [40, 41]
  "§9.10.1#b8": 69
  "§11#r21": [6, 34]
---

# Transaction timeout dan versi setting pada transaksi Disposal

## Prerequisites
- Aktor: Spec ini memakai entitas khusus yang tidak dipakai spec lain. Pengaju Disposal `Sinta Dewi {runId}`. Aktor lain: Approver `Taufik Hidayat {runId}`, yang menyetujui Disposal, Total Control `Wawan Setiawan {runId}`, yang menyimpan perubahan setting dan memindahkan aset, dan Operator platform di luar tenant, yang mengubah status entitas aktor. Job Transaction timeout berjalan tanpa aktor.
- Data:
  - DU-108-1: Entitas `Entitas Timeout {runId}`, Pemakai `hanya spec ini`
  - DU-108-2: Group `Workshop Timeout {runId}`
  - DU-108-3: Group `Gudang Override {runId}`, Group override Allow Disposal `Deny`
  - DU-108-4: Category `Mesin Timeout {runId}`, Allowed disposal types `Sell, Scrap, Lost, Donate, Trade-in, Write-off`, Require approval `ON`, Approval type `Any one approver`
  - DU-108-5: Category `Mesin Versi {runId}`, Allowed disposal types `Sell, Scrap`, Allowed disposal types setelah Save Changes `Scrap`, Require approval `ON`, Approval type `Any one approver`
  - DU-108-6: User `Sinta Dewi {runId}`, Role `Pengaju Disposal`, Cakupan `Workshop Timeout {runId}, Gudang Override {runId}`, Status `Aktif`
  - DU-108-7: User `Taufik Hidayat {runId}`, Role `Role Transaksi Approver Disposal`, Cakupan `Workshop Timeout {runId}`, Status `Aktif`
  - DU-108-8: User `Wawan Setiawan {runId}`, Role `Total Control`, Cakupan `seluruh entitas`, Status `Aktif`
  - DU-108-9: Disposal `Mesin Cetak Q0 {runId}`, Category `Mesin Timeout {runId}`, Group `Workshop Timeout {runId}`, Status `Waiting for Approval`, Masuk status sejak `T0`, Batas Transaction timeout `7 hari sama dengan 168 jam`
  - DU-108-10: Asset `Mesin Cetak E1 {runId}`, Category `Mesin Timeout {runId}`, Group `Workshop Timeout {runId}`, Tag `Ber-tag`, Condition `Active`
  - DU-108-11: Asset `Mesin Cetak E2 {runId}`, Category `Mesin Timeout {runId}`, Group `Workshop Timeout {runId}`, Tag `Ber-tag`, Condition `Active`
  - DU-108-12: Disposal `Mesin Draft D1 {runId}`, Category `Mesin Timeout {runId}`, Group `Workshop Timeout {runId}`, Status `Draft`, Masuk status sejak `T0`
  - DU-108-13: Disposal `Mesin Laporan P1 {runId}`, Category `Mesin Timeout {runId}`, Group `Workshop Timeout {runId}`, Status `Reported`, Masuk status sejak `T0`
  - DU-108-14: Disposal `Mesin Eksekusi X1 {runId}`, Category `Mesin Timeout {runId}`, Group `Workshop Timeout {runId}`, Status `Executed menunggu posting`, Masuk status sejak `T0`
  - DU-108-15: Disposal `Mesin Laporan P2 {runId}`, Category `Mesin Timeout {runId}`, Group `Workshop Timeout {runId}`, Status `Waiting for Approval`, Masuk status sejak `T0`, Disposal Report `Proceeded`, Condition aset sebelum dilaporkan `Normal`
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
- Kondisi:
  - Transaction timeout Disposal bernilai `7` (days), nilai awal Company default. Approval Timeout platform bernilai tidak lebih besar daripada `7` (days).
  - Require approval Disposal pada Category uji bernilai `ON` dengan Approval type `Any one approver`, dan Approval Workflow tersedia di plan entitas aktor.
  - Khusus kelompok langkah «Approval Workflow tidak tersedia di plan: versi setting tercatat pada transaksi tanpa langkah approval»: Approval Workflow tidak tersedia di plan entitas aktor.
  - Entitas aktor berstatus aktif pada awal spec. Status entitas diubah Operator platform hanya pada kelompok langkah «Job timeout tanpa aktor tetap berjalan saat entitas Suspended atau Expired».

## Test Steps

### Batas Transaction timeout Waiting for Approval tepat N kali 24 jam dihitung sejak masuk status itu
1. Waktu berlalu 167 jam sejak Disposal `Mesin Cetak Q0 {runId}` masuk status `Waiting for Approval`
2. Job Transaction timeout berjalan
3. Verifikasi Disposal `Mesin Cetak Q0 {runId}` tetap berstatus `Waiting for Approval` karena batas Transaction timeout Disposal `7` hari, yaitu 168 jam sejak masuk status itu, belum tercapai
4. Waktu berlalu sampai 168 jam sejak Disposal `Mesin Cetak Q0 {runId}` masuk status `Waiting for Approval`
5. Job Transaction timeout berjalan
6. Verifikasi Disposal `Mesin Cetak Q0 {runId}` ditutup saat batas Transaction timeout tercapai dan berstatus `Canceled`, bukan `Expired`
7. Verifikasi baris DSP `Mesin Cetak Q0 {runId}` dicatat dengan Note `Timed out (Waiting for Approval)`
8. Verifikasi `System` yang menutup Disposal `Mesin Cetak Q0 {runId}` dan log transaksi mencatat Modified By `System`
9. Verifikasi penutupan itu tidak menambah entri System Log karena aksi sistem tanpa user aktor mengikuti Aturan Terkunci #7
10. Job Transaction timeout berjalan lagi
11. Verifikasi Disposal `Mesin Cetak Q0 {runId}` yang sudah ditutup tidak diproses lagi: statusnya tetap `Canceled` dan log transaksi tidak bertambah dibanding sebelum job berjalan lagi
12. `Sinta Dewi {runId}` mengajukan ulang Disposal jenis `Scrap` atas aset `Mesin Cetak Q0 {runId}` dengan scan tag aset
13. Verifikasi pengajuan ulang diterima dan Disposal berstatus `Waiting for Approval`

### Batas Execute Waiting for Execution dihitung per baris
14. `Sinta Dewi {runId}` mengajukan satu Disposal jenis `Scrap` berisi dua baris, aset `Mesin Cetak E1 {runId}` dan `Mesin Cetak E2 {runId}`, dengan scan tag aset
15. `Taufik Hidayat {runId}` menyetujui baris `Mesin Cetak E1 {runId}` pada Disposal itu
16. Waktu berlalu empat hari
17. `Taufik Hidayat {runId}` menyetujui baris `Mesin Cetak E2 {runId}` pada Disposal yang sama
18. Waktu berlalu sampai batas Transaction timeout `7` hari terlampaui sejak baris `Mesin Cetak E1 {runId}` masuk status `Waiting for Execution` dan belum terlampaui sejak baris `Mesin Cetak E2 {runId}` masuk status itu
19. Job Transaction timeout berjalan
20. Verifikasi baris DSP `Mesin Cetak E1 {runId}` berstatus `Canceled` dengan Note `Timed out (Waiting for Execution)` karena batas Execute terlampaui
21. Verifikasi baris DSP `Mesin Cetak E2 {runId}` tetap berstatus `Waiting for Execution` karena batas Execute dihitung per baris, walaupun baris `Mesin Cetak E1 {runId}` pada Disposal yang sama sudah `Canceled`

### Pindah status memulai hitungan batas lagi dan Approval Timeout hanya untuk status menunggu approval
22. `Sinta Dewi {runId}` mengajukan Disposal jenis `Scrap` atas `Mesin Siklus R1 {runId}` dengan scan tag aset
23. Waktu berlalu enam hari sejak Disposal `Mesin Siklus R1 {runId}` masuk status `Waiting for Approval`
24. `Taufik Hidayat {runId}` menyetujui Disposal atas `Mesin Siklus R1 {runId}`
25. Waktu berlalu sampai batas Transaction timeout `7` hari terlampaui sejak Disposal `Mesin Siklus R1 {runId}` masuk status `Waiting for Approval` tetapi belum terlampaui sejak Disposal itu masuk status `Waiting for Execution`
26. Job Transaction timeout berjalan
27. Verifikasi Disposal `Mesin Siklus R1 {runId}` tetap berstatus `Waiting for Execution` karena pindah status memulai hitungan batas lagi
28. Verifikasi Disposal `Mesin Siklus R1 {runId}` tidak ditutup oleh Approval Timeout karena Approval Timeout hanya berlaku untuk status menunggu approval
29. Waktu berlalu sampai batas Transaction timeout `7` hari terlampaui sejak Disposal `Mesin Siklus R1 {runId}` masuk status `Waiting for Execution`
30. Job Transaction timeout berjalan
31. Verifikasi Disposal `Mesin Siklus R1 {runId}` berstatus `Canceled` dengan Note `Timed out (Waiting for Execution)`

### Draft, Disposal Report, dan Disposal Executed menunggu posting tidak memiliki timeout
32. Waktu berlalu sampai batas Transaction timeout `7` hari terlampaui sejak Disposal `Mesin Draft D1 {runId}`, `Mesin Laporan P1 {runId}`, dan `Mesin Eksekusi X1 {runId}` masuk statusnya masing-masing
33. Job Transaction timeout berjalan
34. Verifikasi Draft Disposal `Mesin Draft D1 {runId}` tidak memiliki timeout, tidak pernah ditutup otomatis, dan tetap berstatus `Draft`
35. Verifikasi Disposal Report `Mesin Laporan P1 {runId}` pada tab Reported tidak memiliki timeout dan tidak pernah ditutup otomatis
36. Verifikasi Disposal `Mesin Eksekusi X1 {runId}` yang Executed menunggu posting tidak pernah ditutup otomatis

### Penutupan timeout mengembalikan Condition aset dan mempertahankan Disposal Report sebagai arsip
37. Waktu berlalu sampai batas Transaction timeout `7` hari terlampaui sejak Disposal `Mesin Laporan P2 {runId}` dan `Mesin Manual M1 {runId}` masuk status `Waiting for Approval`
38. Job Transaction timeout berjalan
39. Verifikasi Disposal Report `Mesin Laporan P2 {runId}` tetap `Proceeded` sebagai arsip sesudah Disposal asalnya ditutup
40. Verifikasi Condition aset `Mesin Laporan P2 {runId}` kembali menjadi `Normal`, yaitu nilai sebelum aset dilaporkan, dan aset itu tidak memiliki record kondisi yang tersisa
41. Verifikasi Condition aset `Mesin Manual M1 {runId}` kembali ke nilai sebelum Disposal diajukan karena Source Disposal `Manual`

### Transaksi berjalan memakai versi setting saat diajukan dan tidak terpengaruh perubahan setting
42. `Sinta Dewi {runId}` mengajukan Disposal jenis `Sell` atas `Mesin Versi V1 {runId}` dengan scan tag aset dan Nilai jual `5.000.000`
43. Verifikasi Disposal itu mencatat versi setting yang berlaku saat diajukan, sama dengan versi setting yang tampil di sheet Info Export rules sebelum Save Changes berikutnya
44. `Wawan Setiawan {runId}` mengubah Allowed disposal types Category `Mesin Versi {runId}` di tab Disposal menjadi `Scrap`, lalu Save Changes
45. `Taufik Hidayat {runId}` menyetujui Disposal atas `Mesin Versi V1 {runId}`
46. Verifikasi Disposal jenis `Sell` atas `Mesin Versi V1 {runId}` tetap berjalan dan berstatus `Waiting for Execution` walaupun jenis `Sell` kini tidak lagi ada di Allowed disposal types, karena ia memakai aturan lama sampai selesai
47. Verifikasi versi setting yang tercatat pada Disposal `Mesin Versi V1 {runId}` tidak berubah dan tetap versi saat diajukan
48. `Sinta Dewi {runId}` mengajukan Disposal jenis `Scrap` atas `Mesin Versi V2 {runId}` dengan scan tag aset
49. Verifikasi versi setting yang tercatat pada Disposal `Mesin Versi V2 {runId}` lebih besar daripada versi pada Disposal `Mesin Versi V1 {runId}` karena transaksi baru mencatat versi setting baru

### Cakupan override dievaluasi dinamis terhadap data saat ini
50. Total Control memindahkan aset `Mesin Pindah G1 {runId}` ke Group `Gudang Override {runId}`
51. `Sinta Dewi {runId}` mengajukan Disposal jenis `Scrap` atas `Mesin Pindah G1 {runId}` dengan scan tag aset
52. Verifikasi pengajuan ditolak karena override Group `Gudang Override {runId}` bernilai Deny berlaku untuk aset yang kini berada di Group itu, walaupun aset belum ada di Group itu saat override dibuat

### Perubahan Transaction timeout menghitung ulang batas transaksi yang sedang menunggu
53. `Sinta Dewi {runId}` mengajukan Disposal jenis `Scrap` atas `Mesin Cetak Q2 {runId}` dengan scan tag aset
54. Waktu berlalu empat hari
55. `Sinta Dewi {runId}` mengajukan Disposal jenis `Scrap` atas `Mesin Cetak Q1 {runId}` dengan scan tag aset
56. Waktu berlalu satu hari
57. `Sinta Dewi {runId}` mengajukan Disposal jenis `Scrap` atas `Mesin Cetak Q3 {runId}` dengan scan tag aset
58. Waktu berlalu satu hari
59. `Wawan Setiawan {runId}` mengubah Transaction timeout Disposal menjadi `3`, lalu Save Changes
60. Verifikasi batas waktu Disposal `Mesin Cetak Q1 {runId}` dihitung ulang dari saat masuk status `Waiting for Approval` ditambah nilai baru `3` hari, bukan nilai lama `7` hari
61. Verifikasi batas waktu Disposal `Mesin Cetak Q2 {runId}` tidak jatuh sebelum waktu Save dan tidak ditutup segera, karena batas barunya jatuh sebelum waktu Save disetel ke waktu Save ditambah 24 jam
62. Verifikasi peringatan 1 hari sebelum batas dengan event `*_almost_timeout` dikirim ulang untuk Disposal `Mesin Cetak Q2 {runId}` karena sisa waktu ke batas baru 24 jam atau kurang
63. Waktu berlalu sampai 24 jam sejak Save Changes tersimpan terlampaui
64. Job Transaction timeout berjalan
65. Verifikasi Disposal `Mesin Cetak Q2 {runId}` berstatus `Canceled` dengan Note `Timed out (Waiting for Approval)` karena batas barunya, yaitu waktu Save ditambah 24 jam, terlampaui
66. Verifikasi Disposal `Mesin Cetak Q1 {runId}` berstatus `Canceled` dengan Note `Timed out (Waiting for Approval)` karena batas barunya `3` hari sejak masuk status terlampaui, walaupun batas lama `7` hari belum terlampaui
67. Verifikasi Disposal `Mesin Cetak Q3 {runId}` tetap berstatus `Waiting for Approval` karena batas barunya `3` hari sejak masuk status belum terlampaui

### Approval Workflow tidak tersedia di plan: versi setting tercatat pada transaksi tanpa langkah approval
68. `Sinta Dewi {runId}` mengajukan Disposal jenis `Scrap` atas `Mesin Plan P1 {runId}` dengan scan tag aset dan Reason `Aset rusak berat`
69. Verifikasi Disposal itu tercatat tanpa langkah approval dan mencatat versi setting yang berlaku saat diajukan

### Job timeout tanpa aktor tetap berjalan saat entitas Suspended atau Expired
70. `Sinta Dewi {runId}` mengajukan Disposal jenis `Scrap` atas `Mesin Suspend S1 {runId}` dengan scan tag aset
71. Waktu berlalu dua hari
72. `Sinta Dewi {runId}` mengajukan Disposal jenis `Scrap` atas `Mesin Kedaluwarsa S2 {runId}` dengan scan tag aset
73. Operator platform mengubah status entitas aktor menjadi `Suspended`
74. Waktu berlalu sampai batas Transaction timeout `3` hari terlampaui sejak Disposal `Mesin Suspend S1 {runId}` masuk status `Waiting for Approval` dan belum terlampaui sejak Disposal `Mesin Kedaluwarsa S2 {runId}` masuk status itu
75. Job Transaction timeout berjalan
76. Verifikasi Disposal `Mesin Suspend S1 {runId}` berstatus `Canceled` walaupun entitas aktor `Suspended`, karena job timeout tanpa aktor tetap berjalan
77. Operator platform mengubah status entitas aktor menjadi `Expired`
78. Waktu berlalu sampai batas Transaction timeout `3` hari terlampaui sejak Disposal `Mesin Kedaluwarsa S2 {runId}` masuk status `Waiting for Approval`
79. Job Transaction timeout berjalan
80. Verifikasi Disposal `Mesin Kedaluwarsa S2 {runId}` berstatus `Canceled` walaupun entitas aktor `Expired`, karena job timeout tanpa aktor tetap berjalan
